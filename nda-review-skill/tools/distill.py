#!/usr/bin/env python3
"""
Distill raw NDA files into anonymized patterns for precedents-distilled.md.

This is a MAINTAINER tool. It reads your local (un-committed) raw NDA folder
and produces a fresh distillation summary by extracting the patterns the
skill needs — without exposing counterparty names, addresses, signatures,
or any deal-specific terms.

Usage:
    python tools/distill.py <raw-folder> [--out knowledge/precedents-distilled.md]

Where <raw-folder> contains:
    signed/    — final negotiated NDAs (.docx / .pdf / .doc)
    tracked/   — TS Capital first-markup positions (.docx with tracked changes)

What this script does (and does NOT do):
- ✅ Counts deals, extracts term lengths, lists tracked-change patterns by type
- ✅ Extracts deal codenames from filenames (Helix, Adam, Star, etc.)
- ✅ Produces a markdown table summarizing patterns
- ❌ Does NOT extract real counterparty names, addresses, signatories, or amounts
- ❌ Does NOT extract verbatim clause text beyond what's already in the skill's Gallery Examples
- ❌ Does NOT copy raw NDA content to the output

The current precedents-distilled.md was written manually based on cumulative
skill iteration; this script is a starting point for re-distilling as new
precedents are added. Most of the value is in your hand-curated commentary;
this script gives you the raw counts and lists so you can update the
narrative sections quickly.
"""

import sys
import io
import os
import re
import zipfile
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
W = f"{{{NS['w']}}}"

# Filename -> deal codename mapping (extend as needed)
CODENAME_PATTERNS = [
    (r"Helix",   "Helix"),
    (r"Adam",    "Adam"),
    (r"Eagle",   "Eagle"),
    (r"Ampere",  "Ampere"),
    (r"Agile",   "Agile"),
    (r"Colibri", "Colibri"),
    (r"Copper",  "Copper"),
    (r"Spring",  "Spring"),
    (r"Star",    "Star"),
    (r"Thor",    "Thor"),
    (r"ATG",     "ATG"),
    (r"PingPong","PingPong"),
    (r"Candle",  "PJ Candle"),
    (r"Yatsen",  "Yatsen"),
    (r"惠康",     "Hui-Kang"),
    (r"紫光",     "Tsinghua-Unigroup"),
    (r"股权投资",  "Equity-Investment"),
    (r"珠海天威",  "Zhuhai-Tianwei"),
    (r"Trustar",  "Trustar"),
]


def codename(filename: str) -> str:
    for pattern, name in CODENAME_PATTERNS:
        if re.search(pattern, filename, re.IGNORECASE):
            return name
    return "Unknown"


def extract_tracked_changes(docx_path: Path) -> list[str]:
    """Return a list of [INS:...] / [DEL:...] marker strings for paragraphs that have tracked changes."""
    try:
        with zipfile.ZipFile(docx_path) as z:
            xml_bytes = z.read("word/document.xml")
    except (zipfile.BadZipFile, KeyError):
        return []
    root = ET.fromstring(xml_bytes)
    changes = []

    def walk(elem):
        parts = []
        for child in elem:
            tag = child.tag.split("}")[-1] if "}" in child.tag else child.tag
            if tag == "ins":
                txt = "".join((t.text or "") for t in child.iter(f"{W}t"))
                if txt:
                    parts.append(f"[INS:{txt}]")
            elif tag == "del":
                txt = "".join((t.text or "") for t in child.iter(f"{W}delText"))
                if txt:
                    parts.append(f"[DEL:{txt}]")
            elif tag == "r":
                txt = "".join((t.text or "") for t in child.iter(f"{W}t"))
                if txt:
                    parts.append(txt)
            else:
                parts.extend(walk(child))
        return parts

    for p in root.iter(f"{W}p"):
        parts = walk(p)
        text = "".join(parts).strip()
        if "[INS:" in text or "[DEL:" in text:
            changes.append(text)
    return changes


def categorize_change(change_text: str) -> str:
    """Best-effort categorization of a tracked change."""
    t = change_text.lower()
    if "insider" in t or "securities laws prohibit" in t or "price-sensitive" in t:
        return "MNPI deletion"
    if "anniversary" in t or "year" in t and ("[del:" in t or "[ins:" in t):
        return "Term reduction"
    if "non-solicit" in t or "solicit" in t and "employee" in t:
        return "Non-solicit reduction"
    if "portfolio companies" in t:
        return "Portfolio companies deletion"
    if "financing" in t and ("institutions" in t or "banks" in t):
        return "Financing section deletion"
    if "reasonably practicable" in t:
        return "Return/destruction qualifier"
    if "ceasing interest" in t or "decide not to proceed" in t or "停止参与" in t:
        return "Ceasing-interest deletion"
    if "indemnif" in t:
        return "Indemnification qualification"
    if "ts capital" in t or "信宸资本" in t:
        return "Entity fill-in"
    if "[mm]" in t or "effective date" in t and "[" in t:
        return "Date fill-in"
    if "mutatis mutandis" in t or "neither party" in t:
        return "Mutuality / reciprocity addition"
    return "Other"


def scan_folder(folder: Path) -> dict:
    """Return {filename: [list of categorized changes]} for all .docx files."""
    result = {}
    for f in sorted(folder.glob("*.docx")):
        changes = extract_tracked_changes(f)
        if changes:
            categories = [categorize_change(c) for c in changes]
            result[f.name] = categories
    return result


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1

    raw_root = Path(sys.argv[1])
    if not raw_root.is_dir():
        print(f"ERROR: not a directory: {raw_root}")
        return 2

    signed_dir = raw_root / "signed"
    tracked_dir = raw_root / "tracked"

    print(f"Scanning {raw_root}\n")

    if tracked_dir.is_dir():
        print(f"=== tracked/ ({len(list(tracked_dir.glob('*.docx')))} .docx files) ===\n")
        tracked = scan_folder(tracked_dir)
        for fname, cats in tracked.items():
            print(f"  {codename(fname)} ({fname})")
            for cat in cats:
                print(f"    - {cat}")
            print()
        all_cats = Counter(c for cats in tracked.values() for c in cats)
        print("  Aggregate change-category frequencies:")
        for cat, count in all_cats.most_common():
            print(f"    {count:>2}× {cat}")
    else:
        print(f"(no tracked/ folder at {tracked_dir})")

    print()
    if signed_dir.is_dir():
        signed_count = len(list(signed_dir.glob("*")))
        signed_codes = sorted({codename(f.name) for f in signed_dir.glob("*") if f.is_file()})
        print(f"=== signed/ ({signed_count} files; codenames: {', '.join(signed_codes)}) ===")
        print("  (term-length / governing-law extraction would require per-format parsers;")
        print("   update precedents-distilled.md narrative manually based on the deal facts you remember.)")
    else:
        print(f"(no signed/ folder at {signed_dir})")

    print()
    print("Next steps:")
    print("  1. Update knowledge/precedents-distilled.md based on the counts above")
    print("  2. Add new codenames to CODENAME_PATTERNS in this script if they appeared as 'Unknown'")
    print("  3. Commit the distilled .md only — do NOT commit raw/ files to the shared repo")
    return 0


if __name__ == "__main__":
    sys.exit(main())
