# Knowledge Folder

Place your precedent files here before using the NDA review skill.

## Directory Structure

```
knowledge/
├── guideline.pdf       ← Your NDA markup policy / internal memo (required)
├── signed/             ← Signed/executed NDAs showing what was ultimately conceded
└── tracked/            ← First-markup tracked-changes files (primary calibration data)
```

## What to put in `tracked/`

Word `.docx` files containing your team's tracked-changes redlines on past NDAs.
These are the primary reference — the skill uses them to calibrate what to flag and
what language to use. The more precedents here, the more accurate the output.

Naming convention used in the skill: `ProjectName_NDA_TS Markup_v1.docx`

Prefix human-reviewed markups with `[人工]` or `[Human]` — the skill treats those
as ground truth. Files named `*_TS_markup*` WITHOUT that prefix are assumed to be
prior machine output and are never used as precedent.

## What to put in `signed/`

Final signed or near-final versions of past NDAs, showing the concessions actually
accepted after negotiation. The skill uses these to set fallback positions
(what to accept if the counterparty pushes back).

## What to put as `guideline.pdf`

Your internal NDA markup policy or memo. The skill reads this at the start of
each session to understand firm-wide positions on standard issues.

## Notes

- `.doc` binary files (older Word format) cannot be parsed for verbatim edits
  but still serve as evidence that certain edit categories occur
- The skill will check for deal-name-matching files before starting any review
  (e.g., if reviewing `Project Helix_NDA.docx`, it looks for
  `tracked/Project Helix_NDA_TS Markup_v1.docx` first)
- PDF files in `signed/` are readable for contextual reference
