# NDA Review — TS Capital Markup Skill

An AI-assisted NDA review skill calibrated to TS Capital's standard negotiating positions. Produces a tracked-changes Word file with redlines + margin comments, in the style of a real TS Capital first-markup.

**Status:** internal team tool. Distilled (no raw NDAs bundled) — safe to share within the team and across LLM platforms.

---

## What's in here

| Path | Purpose |
|------|---------|
| `SKILL.md` | The prompt/skill content (~9k words) — instructs the LLM how to review |
| `apply_redlines.py` | Python script that turns a JSON of changes into a tracked-changes .docx |
| `tools/extract_paragraphs.py` | Helper to extract verbatim paragraph text from a .docx (use before building `changes.json` to avoid "text not found" errors) |
| `tools/distill.py` | Maintainer tool — re-generates `precedents-distilled.md` after you add new precedents to your local raw folder |
| `knowledge/precedents-distilled.md` | Anonymized patterns from 12 signed precedents + 8 human markups + CITIC guideline. **This file replaces the raw NDA bundle** — no counterparty names, addresses, signatories, or deal amounts are exposed |
| `examples/pingpong-walkthrough.md` | End-to-end worked example using PingPong NDA |
| `CHANGELOG.md` | Version history |

**Note on knowledge design**: Raw signed/tracked NDA files are intentionally NOT bundled. They live only on the maintainer's local machine. The distilled file (~10KB) plus the skill's embedded Key Precedent Facts and Gallery Examples are sufficient for the skill to operate. This keeps the repo safe to share within the team without risking exposure of confidential deal content.

---

## Quick start (Claude Code users)

```bash
# 1. Clone into your Claude Code skills folder
git clone <repo-url> ~/.claude/skills/nda-review

# 2. In Claude Code, run:
/nda-review path/to/your/NDA.docx
```

Output: `path/to/your/NDA_TS_markup.docx` with tracked changes + margin comments.

## Quick start (Claude.ai web Project users)

1. Create a new Project on claude.ai
2. Upload `SKILL.md` as the Project instructions
3. Upload everything in `knowledge/` as Project files
4. In a chat: "Review this NDA" + paste NDA text or upload the .docx
5. Claude returns redline blocks; you run `apply_redlines.py` locally with the resulting `changes.json` to produce the marked-up Word file

## Quick start (ChatGPT Custom GPT)

1. Create a new Custom GPT
2. Paste `SKILL.md` into Instructions
3. Upload `knowledge/` files into Knowledge
4. Enable Code Interpreter (so the GPT can run `apply_redlines.py` directly and return the .docx)
5. Chat: upload NDA, get marked-up file back

## Quick start (generic LLM via API)

`SKILL.md` is a self-contained system prompt. Send it as `system`, the NDA text as `user`, and run `apply_redlines.py` on the returned JSON.

---

## Usage flow

```
NDA.docx
   │
   ├──> [1] LLM reads SKILL.md + knowledge/ + the NDA
   │       Produces: Part 0 checklist + Part 1 summary + Part 2 redline blocks
   │
   ├──> [2] LLM outputs changes.json (12-entry array of original/replacement/comment)
   │
   ├──> [3] tools/extract_paragraphs.py confirms every `original` appears verbatim in the .docx
   │       (avoids the most common failure mode: text not found)
   │
   └──> [4] apply_redlines.py NDA.docx NDA_TS_markup.docx changes.json
              Produces: NDA_TS_markup.docx with tracked changes + margin comments
                        (author: "TS Capital Partners Management Limited")
```

---

## Requirements

- **Python 3.10+** (for `apply_redlines.py` and `extract_paragraphs.py`)
- **lxml** (optional but recommended): `pip install lxml`
- An LLM with strong instruction-following (Claude Sonnet 4.6+ recommended; the skill was calibrated for it)
- The NDA in **.docx format** (export PDFs to .docx first via Word or Acrobat)

---

## Maintenance (for the skill owner)

You keep the raw NDA folder (`signed/` + `tracked/`) on your local machine — NOT in this repo. The repo only ever contains the distilled summary.

**When a new NDA gets marked up by a senior team member:**
1. Add the marked-up `.docx` to your local raw `tracked/` folder
2. Run `python tools/distill.py /path/to/your/raw/folder` to regenerate counts/patterns
3. Manually update `knowledge/precedents-distilled.md` to reflect the new precedent (Section B row + any new aggregate pattern)
4. Commit + push the updated `precedents-distilled.md` only

**When you discover a calibration error (skill flagged something that shouldn't be, or missed something that should):**
1. Edit `SKILL.md` — usually update a Category cell or add a Gallery example
2. Commit with a message explaining the lesson (e.g., "PingPong: 'not prohibited by law' ≠ 'reasonably practicable'")
3. Update `CHANGELOG.md`

---

## Confidentiality

The distilled file uses code names only (Helix, Adam, Star, Thor, etc.) and contains no real counterparty names, addresses, signatories, or deal amounts. The repo is **safe to share with the internal team** via private GitHub repo, internal Git, or zipped email.

⚠️ Still keep the GitHub repo **private** — code names + negotiating patterns are still TS Capital IP. Do not fork to a public account.
