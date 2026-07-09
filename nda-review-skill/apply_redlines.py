#!/usr/bin/env python3
"""
apply_redlines.py - Apply tracked changes + margin comments to a Word .docx NDA

Usage:
    python apply_redlines.py <input.docx> <output.docx> <changes.json>

changes.json format:
    [
      {
        "original": "exact text to delete",
        "replacement": "new text (empty string for pure deletion)",
        "comment": "WHY this change is being made (appears as Word margin comment)"
      },
      ...
    ]
"""

import sys
import json
import zipfile
import shutil
import os
from copy import deepcopy
from datetime import datetime

try:
    from lxml import etree
    def new_elem(tag): return etree.Element(tag)
    def to_bytes(tree): return etree.tostring(tree, xml_declaration=True, encoding='UTF-8', standalone=True)
    def from_bytes(b): return etree.fromstring(b)
    USE_LXML = True
except ImportError:
    import xml.etree.ElementTree as etree
    def new_elem(tag): return etree.Element(tag)
    def to_bytes(tree):
        etree.register_namespace('', 'http://schemas.openxmlformats.org/wordprocessingml/2006/main')
        return etree.tostring(tree, encoding='unicode').encode('utf-8')
    def from_bytes(b): return etree.fromstring(b.decode('utf-8'))
    USE_LXML = False

W   = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
XML_NS = 'http://www.w3.org/XML/1998/namespace'
AUTHOR   = "TS Capital Partners Management Limited"
INITIALS = "TSC"
DATE     = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

COMMENTS_TEMPLATE = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    '<w:comments xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas"'
    ' xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'
    ' xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
    '</w:comments>'
)


def w(tag):
    return f'{{{W}}}{tag}'


# 1:1 char map so index positions survive normalization (curly quotes,
# full-width parens, NBSP). Both haystack and needle are normalized before
# matching; the deleted span keeps the document's original characters.
_NORM = str.maketrans({
    '‘': "'", '’': "'",   # curly single quotes
    '“': '"', '”': '"',   # curly double quotes
    '（': '(', '）': ')',   # full-width parens
    ' ': ' ',                  # non-breaking space
})


def norm(s):
    return s.translate(_NORM)


def get_para_text(para):
    return ''.join((t.text or '') for t in para.iter(w('t')))


def apply_change_to_para(para, original_text, replacement_text, rev_id):
    """Wrap original_text in w:del and optionally insert replacement_text as w:ins.

    Walks paragraph children IN ORDER. Each w:r in run_info is replaced in place
    by its decomposed pieces (before-r, del-wrapper, after-r); non-run elements
    (existing ins/del from prior changes, comment range markers, pPr, etc.) pass
    through at their original positions. The INS is inserted immediately after
    the last DEL produced by THIS change. This preserves the relative ordering
    of multiple changes within one paragraph and keeps each edit visually
    inline with its strikethrough.
    """
    runs = para.findall(w('r'))
    if not runs:
        return 0

    run_info = []
    pos = 0
    for run in runs:
        t_elem = run.find(w('t'))
        text = (t_elem.text or '') if t_elem is not None else ''
        run_info.append((run, text, pos, pos + len(text)))
        pos += len(text)

    total_text = ''.join(t for _, t, _, _ in run_info)
    idx = total_text.find(original_text)
    if idx == -1:
        # Retry with quote/paren normalization (1:1 char map keeps indices valid)
        idx = norm(total_text).find(norm(original_text))
    if idx == -1:
        return 0
    end_idx = idx + len(original_text)

    # Decompose each run into its replacement pieces (could be [run] unchanged,
    # or [before, del, after] subsets). Track last rPr seen for INS styling.
    processed_pairs = []  # list of (original_run, [pieces])
    last_rpr = None

    for run, text, run_start, run_end in run_info:
        rpr = run.find(w('rPr'))
        if rpr is not None:
            last_rpr = deepcopy(rpr)

        overlap_start = max(run_start, idx)
        overlap_end   = min(run_end, end_idx)

        if overlap_end <= overlap_start:
            processed_pairs.append((run, [run]))
            continue

        pieces = []

        # Portion before the change
        if overlap_start > run_start:
            br = deepcopy(run)
            bt = br.find(w('t'))
            if bt is not None:
                bt.text = text[:overlap_start - run_start]
                bt.set(f'{{{XML_NS}}}space', 'preserve')
            pieces.append(br)

        # Overlapping portion → w:del
        change_text = text[overlap_start - run_start:overlap_end - run_start]
        del_run = deepcopy(run)
        t_elem = del_run.find(w('t'))
        if t_elem is not None:
            t_elem.tag = w('delText')
            t_elem.text = change_text
            t_elem.set(f'{{{XML_NS}}}space', 'preserve')
        del_elem = new_elem(w('del'))
        del_elem.set(w('id'), str(rev_id))
        del_elem.set(w('author'), AUTHOR)
        del_elem.set(w('date'), DATE)
        del_elem.append(del_run)
        pieces.append(del_elem)

        # Portion after the change
        if overlap_end < run_end:
            ar = deepcopy(run)
            at = ar.find(w('t'))
            if at is not None:
                at.text = text[overlap_end - run_start:]
                at.set(f'{{{XML_NS}}}space', 'preserve')
            pieces.append(ar)

        processed_pairs.append((run, pieces))

    consumed = 1
    ins_elem = None
    if replacement_text:
        ins_elem = new_elem(w('ins'))
        ins_elem.set(w('id'), str(rev_id + 1))
        ins_elem.set(w('author'), AUTHOR)
        ins_elem.set(w('date'), DATE)
        ins_run = new_elem(w('r'))
        if last_rpr is not None:
            ins_run.append(last_rpr)
        ins_t = new_elem(w('t'))
        ins_t.set(f'{{{XML_NS}}}space', 'preserve')
        ins_t.text = replacement_text
        ins_run.append(ins_t)
        ins_elem.append(ins_run)
        consumed = 2

    # Walk para children IN ORDER, swap each tracked run for its pieces.
    # Non-tracked elements (pPr, prior ins/del wrappers, comment markers) pass
    # through at their original position.
    new_children = []
    last_del_in_new = -1
    for child in list(para):
        replaced = False
        for orig_run, pieces in processed_pairs:
            if child is orig_run:
                for piece in pieces:
                    new_children.append(piece)
                    if piece.tag == w('del'):
                        last_del_in_new = len(new_children) - 1
                replaced = True
                break
        if not replaced:
            new_children.append(child)

    # Insert INS right after the last DEL produced by this change.
    if ins_elem is not None:
        if last_del_in_new >= 0:
            new_children.insert(last_del_in_new + 1, ins_elem)
        else:
            new_children.append(ins_elem)

    # Replace para's children with the new ordered list.
    for child in list(para):
        para.remove(child)
    for child in new_children:
        para.append(child)

    return consumed


def add_comment_anchors(para, comment_id, del_elems_added):
    """
    Wrap the last del/ins group in w:commentRangeStart / End and add w:commentReference.
    We anchor to the first del element in the paragraph (simplest approach).
    """
    # Find the del/ins elements we just added (they are the last-added elements)
    children = list(para)

    # Insert commentRangeStart before the first del elem
    for i, child in enumerate(children):
        if child.tag == w('del') or child.tag == w('ins'):
            crs = new_elem(w('commentRangeStart'))
            crs.set(w('id'), str(comment_id))
            para.insert(i, crs)
            break

    # Insert commentRangeEnd after the last del/ins
    children = list(para)
    last_idx = -1
    for i, child in enumerate(children):
        if child.tag in (w('del'), w('ins')):
            last_idx = i

    if last_idx >= 0:
        cre = new_elem(w('commentRangeEnd'))
        cre.set(w('id'), str(comment_id))
        para.insert(last_idx + 1, cre)

        # Add comment reference run after the range end
        ref_run = new_elem(w('r'))
        ref_rpr = new_elem(w('rPr'))
        rStyle = new_elem(w('rStyle'))
        rStyle.set(w('val'), 'CommentReference')
        ref_rpr.append(rStyle)
        ref_run.append(ref_rpr)
        ref_elem = new_elem(w('commentReference'))
        ref_elem.set(w('id'), str(comment_id))
        ref_run.append(ref_elem)
        para.insert(last_idx + 2, ref_run)


def build_comment_xml(comment_id, comment_text):
    """Build a <w:comment> element."""
    comment = new_elem(w('comment'))
    comment.set(w('id'), str(comment_id))
    comment.set(w('author'), AUTHOR)
    comment.set(w('date'), DATE)
    comment.set(w('initials'), INITIALS)

    p = new_elem(w('p'))
    pPr = new_elem(w('pPr'))
    pStyle = new_elem(w('pStyle'))
    pStyle.set(w('val'), 'CommentText')
    pPr.append(pStyle)
    p.append(pPr)

    # Annotation ref run
    ref_run = new_elem(w('r'))
    ref_rpr = new_elem(w('rPr'))
    rStyle = new_elem(w('rStyle'))
    rStyle.set(w('val'), 'CommentReference')
    ref_rpr.append(rStyle)
    ref_run.append(ref_rpr)
    ann = new_elem(w('annotationRef'))
    ref_run.append(ann)
    p.append(ref_run)

    # Comment text run
    txt_run = new_elem(w('r'))
    t = new_elem(w('t'))
    t.set(f'{{{XML_NS}}}space', 'preserve')
    t.text = comment_text
    txt_run.append(t)
    p.append(txt_run)

    comment.append(p)
    return comment


def apply_all_changes(xml_bytes, changes):
    tree = from_bytes(xml_bytes)
    rev_id     = 200   # revision IDs for del/ins
    comment_id = 1     # comment IDs
    comments   = []    # list of (comment_id, comment_text)

    for change in changes:
        original    = change.get('original', '')
        replacement = change.get('replacement', '')
        comment_txt = change.get('comment', '')
        if not original:
            continue

        applied = False
        for para in tree.iter(w('p')):
            if norm(original) in norm(get_para_text(para)):
                consumed = apply_change_to_para(para, original, replacement, rev_id)
                if consumed:
                    if comment_txt:
                        add_comment_anchors(para, comment_id, consumed)
                        comments.append((comment_id, comment_txt))
                        comment_id += 1
                    rev_id += consumed + 1
                    applied = True
                    break

        if not applied:
            print(f"  WARNING: text not found: {original[:60]!r}", file=sys.stderr)

    return to_bytes(tree), comments


def build_comments_xml(comments_list):
    """Build the full comments.xml content."""
    root = from_bytes(COMMENTS_TEMPLATE.encode('utf-8'))
    for cid, ctext in comments_list:
        root.append(build_comment_xml(cid, ctext))
    return to_bytes(root)


def process_docx(input_path, output_path, changes):
    with zipfile.ZipFile(input_path, 'r') as zin:
        file_map = {name: zin.read(name) for name in zin.namelist()}

    if 'word/document.xml' not in file_map:
        print("ERROR: word/document.xml not found — not a valid .docx file.", file=sys.stderr)
        sys.exit(1)

    print(f"Applying {len(changes)} change(s)...", file=sys.stderr)
    new_doc_xml, comments_list = apply_all_changes(file_map['word/document.xml'], changes)
    file_map['word/document.xml'] = new_doc_xml

    if comments_list:
        file_map['word/comments.xml'] = build_comments_xml(comments_list)
        # Ensure comments.xml is referenced in [Content_Types].xml and .rels
        ct = file_map.get('[Content_Types].xml', b'').decode('utf-8')
        if 'comments' not in ct.lower():
            ct = ct.replace(
                '</Types>',
                '<Override PartName="/word/comments.xml" '
                'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.comments+xml"/>'
                '</Types>'
            )
            file_map['[Content_Types].xml'] = ct.encode('utf-8')

        rels = file_map.get('word/_rels/document.xml.rels', b'').decode('utf-8')
        if 'comments' not in rels.lower():
            rels = rels.replace(
                '</Relationships>',
                '<Relationship Id="rIdComments" '
                'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/comments" '
                'Target="comments.xml"/>'
                '</Relationships>'
            )
            file_map['word/_rels/document.xml.rels'] = rels.encode('utf-8')

        print(f"  Added {len(comments_list)} margin comment(s).", file=sys.stderr)

    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zout:
        for name, content in file_map.items():
            zout.writestr(name, content)

    print(f"Redlined document saved: {output_path}", file=sys.stderr)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python apply_redlines.py input.docx output.docx changes.json", file=sys.stderr)
        sys.exit(1)

    input_path   = sys.argv[1]
    output_path  = sys.argv[2]
    changes_path = sys.argv[3]

    if not os.path.exists(input_path):
        print(f"ERROR: file not found: {input_path}", file=sys.stderr)
        sys.exit(1)

    with open(changes_path, 'r', encoding='utf-8') as f:
        changes = json.load(f)

    process_docx(input_path, output_path, changes)
