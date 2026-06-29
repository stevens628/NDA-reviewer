#!/usr/bin/env python3
"""
Extract verbatim paragraph text from a .docx file.

Usage:
    python extract_paragraphs.py <input.docx> [search_term]

Without search_term: prints every non-empty paragraph with index.
With search_term:    prints only paragraphs that contain it, with surrounding context.

Use this BEFORE building changes.json to confirm the exact spelling, quote
style (curly vs straight), spacing (single vs double space), and any
non-breaking characters in the text you intend to put in `original`.

The most common failure mode of apply_redlines.py is "text not found",
caused by typing the original from memory instead of extracting it verbatim.
"""

import sys
import io
import zipfile
import xml.etree.ElementTree as ET

# Force UTF-8 output (Windows console defaults to GBK and chokes on curly quotes)
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
W = f"{{{NS['w']}}}"


def extract_paragraphs(docx_path: str) -> list[str]:
    with zipfile.ZipFile(docx_path) as z:
        xml_bytes = z.read("word/document.xml")
    root = ET.fromstring(xml_bytes)
    paragraphs = []
    for p in root.iter(f"{W}p"):
        text = "".join((t.text or "") for t in p.iter(f"{W}t"))
        if text.strip():
            paragraphs.append(text)
    return paragraphs


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1

    path = sys.argv[1]
    search = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        paragraphs = extract_paragraphs(path)
    except FileNotFoundError:
        print(f"ERROR: file not found: {path}")
        return 2
    except zipfile.BadZipFile:
        print(f"ERROR: not a .docx (or corrupt): {path}")
        return 2

    if search is None:
        for i, para in enumerate(paragraphs, 1):
            print(f"[{i:03d}] {para}\n")
        return 0

    found = 0
    for i, para in enumerate(paragraphs, 1):
        if search in para:
            idx = para.find(search)
            start = max(0, idx - 50)
            end = min(len(para), idx + len(search) + 50)
            print(f"[P{i:03d}] ...{para[start:end]}...")
            print(f"      (raw repr): {para[start:end]!r}\n")
            found += 1
    if found == 0:
        print(f"NOT FOUND: {search!r}")
        print("Try a shorter substring, or check for curly quotes/apostrophes.")
        return 3
    return 0


if __name__ == "__main__":
    sys.exit(main())
