# PingPong NDA — End-to-End Walkthrough

A real worked example showing what the skill produces from input to output. Use this as onboarding for new team members.

---

## Input

A standard unilateral confidentiality agreement from PingPong (Cayman) Limited, with TS Capital as Recipient. HK law + HKIAC arbitration, 10-year term, no non-solicit, no indemnification, no MNPI clause.

The NDA has 4 placeholders that need filling (date, entity name, formation/address, signature block) and 6 substantive issues that need flagging.

---

## Skill output — Part 0 (Mandatory Coverage Checklist)

The skill scans every Standard Change (S1–S7) and every Must-Fix Category (1–24) and marks each Y/N:

**Triggered (YES):**
- S1 — fill placeholders
- S2 — 10-year term must be reduced
- S5+#14 — return/destruction needs "reasonably practicable" + certification fallback applies
- #3 — Representatives definition extends to "Party's Affiliates" → use Eagle-style carve-out (Example 13 Approach A)
- #4 — §6 missing "(d) independently developed" CI exception
- #6 — §7(d) holds Recipient fully responsible for Rep breaches → add Annex A carve-out
- #7 — §8 non-publicity binds only Recipient → make mutual

**Not triggered (NO):**
- S3, S4, S6, S7 (no non-solicit, disclosure trigger already broad, no consent requirement, no MNPI)
- Categories 9, 10, 11, 12, 13, 15, 16, 18, 19, 20, 21, 22, 23, 24

**7 unique fix items → 7 Part 1 rows → 7 Part 2 redline blocks → 12 verbatim ORIGINAL/REPLACEMENT pairs in changes.json**

---

## Skill output — Part 2 (sample redline blocks)

### Block: Term reduction (Thor dual-trigger formula)
```
ORIGINAL_TEXT:  "the date that is ten (10) years after the Effective Date"
REPLACEMENT_TEXT: "the earlier of (i) the first anniversary of the Effective Date and (ii) the date of consummation of the Purpose between the Parties"
COMMENT: 10 years is far above the 2-year ceiling. Dual-trigger formula
         also terminates the NDA on deal close.
```

### Block: Eagle-style Representatives carve-out
```
ORIGINAL_TEXT:  "controlling, or under common control with a Party."
REPLACEMENT_TEXT: "controlling, or under common control with a Party.
                   Notwithstanding the foregoing, in relation to the Recipient,
                   Representatives shall not include equityholders or Affiliates
                   to whom the Recipient has not provided Confidential Information."
COMMENT: Limits Recipient's exposure to Affiliates that actually received CI
         AND explicitly excludes equityholders (LP investors) — preserves
         IC/LP disclosure flexibility. PingPong precedent.
```

---

## Generating the marked-up Word file

```bash
# 1. (optional but recommended) Verify a tricky ORIGINAL_TEXT exists verbatim:
python tools/extract_paragraphs.py "NDA-PingPong.docx" "common control with a Party"

# 2. Run apply_redlines with the LLM-produced changes.json:
python apply_redlines.py "NDA-PingPong.docx" "NDA-PingPong_TS_markup.docx" "changes.json"
```

Expected output: `Applying 12 change(s)... Added 12 margin comment(s). Redlined document saved`

Open `NDA-PingPong_TS_markup.docx` in Word — every redline is a tracked change attributed to "TS Capital Partners Management Limited", with a margin comment explaining the business reason.

---

## Lessons this exercise encoded into SKILL.md

1. **"to the extent not prohibited by law" is NOT equivalent to "to the extent legally permissible and reasonably practicable"** — the first only covers legal prohibition; the second adds operational latitude. Always normalize to the standard phrase. (Category #13(b) was updated post-PingPong.)
2. **Reps narrowing — Eagle vs Thor**: when the Reps definition is otherwise reasonable, prefer the Eagle-style Notwithstanding carve-out (with explicit equityholders exclusion) over hard-deleting "or such Party's Affiliates". (Added as Gallery Example 13.)
3. **Date placeholder convention**: do NOT pre-fill `[mm] [dd], [yyyy]` — leave it for signing. (S1 was updated post-PingPong.)
4. **Signature case**: use entity's natural case (`TS Capital Partners Management Limited`) even when the placeholder is ALL CAPS. (S1 was updated post-PingPong.)
5. **§10 certifications fallback**: if a backup-files carve-out paragraph already softens exposure, certifications can be kept as a concession rather than deleted on initial markup. (Category #14(b) was updated post-PingPong.)
