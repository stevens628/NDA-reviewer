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
import re
import zipfile
import shutil
import os
from copy import deepcopy
from datetime import datetime
from difflib import SequenceMatcher

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


# Tokens for word-level diffing: each CJK char / full-width punctuation mark is
# its own token; ASCII words and whitespace runs are grouped. This makes the
# tracked output match human reviewer granularity (DEL 'two' INS 'one', not
# strike-and-retype of the whole sentence).
_TOKEN_RE = re.compile(
    r'[　-〿一-鿿豈-﫿＀-￯]'  # CJK char / fullwidth punct
    r'|[A-Za-z0-9]+'                                            # ASCII word
    r'|\s+'                                                     # whitespace run
    r'|.',                                                      # any other single char
    re.S)


def diff_ops(original_text, replacement_text):
    """Word-level diff between original and replacement.

    Returns a list of (del_start, del_end, ins_text) spans relative to
    original_text, covering ONLY the parts that actually differ. Unchanged
    words are never deleted-and-retyped. A pure insertion has
    del_start == del_end; a pure deletion has ins_text == ''.
    """
    a = _TOKEN_RE.findall(original_text)
    b = _TOKEN_RE.findall(replacement_text)
    # char offset of each a-token
    a_off = [0]
    for tok in a:
        a_off.append(a_off[-1] + len(tok))

    sm = SequenceMatcher(None, a, b, autojunk=False)
    # Dissimilar texts (e.g. placeholder -> entity name) share little beyond
    # whitespace; a token diff would fragment into noisy word pairs. Render
    # those as one clean DEL + INS instead, like a human reviewer.
    if replacement_text and sm.ratio() < 0.5:
        return [(0, len(original_text), replacement_text)]

    ops = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            continue
        ops.append((a_off[i1], a_off[i2], ''.join(b[j1:j2])))
    return ops


def _usable_rpr_source(run, rpr, text):
    """Only real document-text runs may donate rPr to inserted text.
    Comment-mark runs (w:commentReference / w:annotationRef, or rStyle
    CommentReference) render at 8pt and must never be inherited."""
    if run.find(w('commentReference')) is not None or run.find(w('annotationRef')) is not None:
        return False
    rs = rpr.find(w('rStyle'))
    if rs is not None and rs.get(w('val')) in ('CommentReference', 'CommentText'):
        return False
    return bool(text)


def apply_span_change(para, start, end, ins_text, rev_id):
    """Wrap chars [start, end) of the paragraph's visible text in w:del and
    insert ins_text as w:ins at that position. start == end → pure insertion.
    Offsets refer to the concatenation of top-level w:r text (tracked del/ins
    from earlier edits are not top-level runs and are skipped automatically).
    Returns number of revision elements created (0 if nothing done).
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

    processed_pairs = []  # (original_run, [pieces])
    last_rpr = None
    ins_anchor_rpr = None

    for run, text, run_start, run_end in run_info:
        rpr = run.find(w('rPr'))
        if rpr is not None and _usable_rpr_source(run, rpr, text):
            last_rpr = deepcopy(rpr)

        overlap_start = max(run_start, start)
        overlap_end   = min(run_end, end)

        if start == end:
            # Insertion point handling: split at 'start' inside the run that
            # contains it (or ends exactly at it, preferring the earlier run).
            if run_start < start <= run_end or (start == 0 and run_start == 0):
                cut = start - run_start
                pieces = []
                if cut > 0:
                    br = deepcopy(run)
                    bt = br.find(w('t'))
                    if bt is not None:
                        bt.text = text[:cut]
                        bt.set(f'{{{XML_NS}}}space', 'preserve')
                    pieces.append(br)
                marker = new_elem(w('r'))  # zero-width placeholder replaced by INS below
                marker.set('temp-ins-anchor', '1')
                pieces.append(marker)
                if cut < len(text):
                    ar = deepcopy(run)
                    at = ar.find(w('t'))
                    if at is not None:
                        at.text = text[cut:]
                        at.set(f'{{{XML_NS}}}space', 'preserve')
                    pieces.append(ar)
                processed_pairs.append((run, pieces))
                ins_anchor_rpr = last_rpr
                start = end = -1  # only split once
            else:
                processed_pairs.append((run, [run]))
            continue

        if overlap_end <= overlap_start:
            processed_pairs.append((run, [run]))
            continue

        pieces = []
        if overlap_start > run_start:
            br = deepcopy(run)
            bt = br.find(w('t'))
            if bt is not None:
                bt.text = text[:overlap_start - run_start]
                bt.set(f'{{{XML_NS}}}space', 'preserve')
            pieces.append(br)

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
    if ins_text:
        ins_elem = new_elem(w('ins'))
        ins_elem.set(w('id'), str(rev_id + 1))
        ins_elem.set(w('author'), AUTHOR)
        ins_elem.set(w('date'), DATE)
        ins_run = new_elem(w('r'))
        rpr_src = ins_anchor_rpr if ins_anchor_rpr is not None else last_rpr
        if rpr_src is not None:
            ins_run.append(deepcopy(rpr_src))
        ins_t = new_elem(w('t'))
        ins_t.set(f'{{{XML_NS}}}space', 'preserve')
        ins_t.text = ins_text
        ins_run.append(ins_t)
        ins_elem.append(ins_run)
        consumed = 2

    new_children = []
    last_del_in_new = -1
    anchor_in_new = -1
    for child in list(para):
        replaced = False
        for orig_run, pieces in processed_pairs:
            if child is orig_run:
                for piece in pieces:
                    if piece.tag == w('r') and piece.get('temp-ins-anchor'):
                        anchor_in_new = len(new_children)  # position, don't append marker
                        continue
                    new_children.append(piece)
                    if piece.tag == w('del'):
                        last_del_in_new = len(new_children) - 1
                replaced = True
                break
        if not replaced:
            new_children.append(child)

    if ins_elem is not None:
        if last_del_in_new >= 0:
            new_children.insert(last_del_in_new + 1, ins_elem)
        elif anchor_in_new >= 0:
            new_children.insert(anchor_in_new, ins_elem)
        else:
            new_children.append(ins_elem)
    elif last_del_in_new < 0 and anchor_in_new < 0:
        return 0  # nothing changed

    for child in list(para):
        para.remove(child)
    for child in new_children:
        para.append(child)

    return consumed


def apply_change_to_para(para, original_text, replacement_text, rev_id):
    """Locate original_text in the paragraph, word-diff it against
    replacement_text, and apply each differing span as its own surgical
    del/ins pair. Unchanged words are never struck out and retyped — a
    change like 'two (2) years' → 'one (1) year' renders as three small
    del/ins pairs, matching human reviewer granularity. Spans are applied
    right-to-left so earlier offsets stay valid.
    """
    runs = para.findall(w('r'))
    if not runs:
        return 0

    total_text = ''.join(
        (r.find(w('t')).text or '') if r.find(w('t')) is not None else ''
        for r in runs)
    idx = total_text.find(original_text)
    if idx == -1:
        # Retry with quote/paren normalization (1:1 char map keeps indices valid)
        idx = norm(total_text).find(norm(original_text))
    if idx == -1:
        return 0

    ops = diff_ops(original_text, replacement_text)
    if not ops:
        return 0

    consumed = 0
    for del_start, del_end, ins_text in reversed(ops):
        consumed += apply_span_change(
            para, idx + del_start, idx + del_end, ins_text, rev_id + consumed)
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


def sanitize_comment_ref_styles(tree):
    """Remove stray rStyle=CommentReference from real text runs.

    When a later change inserts text next to an earlier change's comment
    anchor, the inserted run can inherit the CommentReference character
    style (8pt), making inserted text render visibly smaller. Genuine
    comment-mark runs (containing w:commentReference / w:annotationRef)
    are left untouched.
    """
    fixed = 0
    for r in tree.iter(w('r')):
        rpr = r.find(w('rPr'))
        if rpr is None:
            continue
        rs = rpr.find(w('rStyle'))
        if rs is None or rs.get(w('val')) != 'CommentReference':
            continue
        if r.find(w('commentReference')) is not None or r.find(w('annotationRef')) is not None:
            continue
        has_text = any((t.text or '') for t in r.iter(w('t'))) or \
                   any((t.text or '') for t in r.iter(w('delText')))
        if not has_text:
            continue
        rpr.remove(rs)
        if len(rpr) == 0:
            r.remove(rpr)
        fixed += 1
    if fixed:
        print(f"  Sanitized {fixed} run(s) that had stray CommentReference style.", file=sys.stderr)


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

    sanitize_comment_ref_styles(tree)
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
