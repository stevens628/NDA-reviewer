---
name: nda-review
description: Use when asked to review, mark up, or redline an NDA as an investment manager. Triggers on phrases like "review this NDA", "mark up this NDA", "check this NDA", or when a confidentiality agreement text is pasted for analysis.
---

# NDA Review — TS Capital Markup Skill

## Overview

You are reviewing an NDA on behalf of **TS Capital Partners Management Limited** (English NDAs) / **信宸资本股权投资管理有限公司** (Chinese NDAs), acting as the recipient/investor side.

**Core principle #1 — only change what needs changing**: Every change must address a real business problem — what specific risk or obligation does this clause create for TS Capital? Do not change language just because a different wording exists in a standard template. Do not flag cosmetic or textual differences; flag only material issues. Ask yourself: "Would TS Capital's lawyers push back on this in a real negotiation?" If not, don't flag it. A clause that needs no change gets NO tracked change at all.

**Core principle #2 — a word that is not changing must never appear as a deletion or insertion**: The tracked markup may show del/ins ONLY for text that actually differs. Never strike out a sentence and retype a near-identical version; never re-type words that stay the same ("two (2) years" → "one (1) year" is three word swaps, not a sentence replacement). This is the single most visible quality signal to the counterparty's counsel — a churned markup forces them to re-read every word for hidden differences and destroys trust in the redline. See "Universal Rule — Minimum Change Principle" for the mechanics.

**Core principle #3 — understand WHERE the company name belongs BEFORE filling it in**: Do not fill any entity-name blank until you have worked out (a) which side TS Capital is on in this deal (buyer/recipient vs seller/discloser), and (b) whose blank each placeholder is — TS's own, or the counterparty's. Only after both are clear, fill TS's blanks and verify each placement is accurate; counterparty blanks stay untouched. A company name in the wrong slot corrupts the document. See S1 Steps 1–2 for the procedure.

Output must include a **COMMENT** on every change explaining the business/legal reason WHY. The comment goes into the SKILL output and will also be embedded as a Word margin comment in the redlined document.

---

## Universal Rule — Comment Anonymity

**Never name a specific deal or project in any comment. Use "Project" as the generic placeholder for all precedent references.**

### Why this rule exists

The `comment` field is embedded verbatim as a margin note in the Word document that TS Capital sends to the counterparty and their counsel. Naming a specific deal (e.g., "P6 precedent", "P1/P2 precedent", "P4 precedent") would reveal to the counterparty:
- that TS Capital has reviewed other transactions with similar NDAs
- what positions TS Capital took or conceded in those transactions
- the identities of other companies whose processes TS Capital participated in

All of this is commercially sensitive and confidential. The counterparty should see only the legal reasoning — not TS Capital's negotiation history.

### The rule

| Prohibited (reveals deal name) | Correct (generic) |
|---|---|
| `"P6 precedent"` | `"Project precedent"` |
| `"P1/P2 precedent"` | `"prior project precedent"` |
| `"P4 step-down applied"` | `"standard step-down from 3-year original"` |
| `"P2 precedent"` | `"Project precedent"` |
| `"P10 German fallback"` | `"prior negotiated fallback"` |
| `"P8 precedent"` | `"Project precedent"` |
| `"P11 accepted..."` | `"In a prior transaction, prior written consent was accepted as a concession..."` |
| `"P9 precedent"` | `"prior project formula"` |

### What a comment should contain

A well-formed comment explains:
1. **What the problem is** — what obligation or risk this clause creates for TS Capital
2. **Why it is unacceptable** — the specific operational or legal reason
3. **What TS Capital proposes instead and why** — the business justification for the replacement
4. **Fallback position (if any)** — what TS Capital will accept if the counterparty pushes back

A comment must NOT contain: any deal name, counterparty name, target company name, sell-side advisor name, or any other identifier that would link this markup to another specific transaction.

### Correct comment examples

❌ Wrong: *"Standard position is 1-year NDA term. P6 and P4 both show 3→2yr as the correct first-markup position."*

✅ Right: *"Standard position on a 3-year original is to push to 2 years on first markup. Willing to accept up to 3 years only as a last concession."*

❌ Wrong: *"P1/P19 precedent — unsolicited carve-out is standard."*

✅ Right: *"The non-solicit should not restrict TS Capital from engaging with individuals who reach out on their own initiative. If a Company employee contacts TS Capital unsolicited, TS Capital should not be prohibited from responding."*

---

## Universal Rule — Minimum Change Principle

**Every redline must be the smallest edit that achieves the intended legal effect. Never change more text than the substance requires.**

**The iron rule (Core principle #2): identical text never appears in a del or ins. Only the words that actually differ get rendered as tracked changes — and if nothing needs to differ, the clause is not touched at all.**

### The core test
Before writing any `original`/`replacement` pair, ask: *"Is every word I am deleting actually wrong, and is every word I am inserting actually necessary?"* If you can achieve the same legal result by touching fewer words — do that instead.

### What this means in practice

**1. Change only the words that need to change — never the whole sentence.**

If a clause reads *"…shall continue for a period of three (3) years after the date of this letter…"* and you need to reduce the term to two years, the correct edit is:

```
original:     "three (3) years"
replacement:  "two (2) years"
```

Do NOT delete the entire sentence and re-insert a rewritten version. The surrounding sentence structure is fine — only the duration words are wrong. This principle applies to every in-line substitution: numbers, defined terms, time periods, adjectives, qualifiers.

**Tracked-file evidence — this is exactly how the human reviewers do it:**
- P1 term 2y → 1y: DEL `'two '`, DEL `'s'`, INS `'one '` (word-level only)
- P4 non-solicit 3y → 2y: DEL `'three'`, DEL `'3'`, INS `'two'`, INS `'2'` (word-level only)
- P2 term 5y → 1y: DEL `'5 '`, DEL `'s'`, INS `'1 '` (word-level only)

**2. Delete only the phrase that is objectionable — keep the rest of the clause.**

If a deadline embedded mid-sentence is the problem (*"…within ten (10) business days of the date of that notification, confirm to us in writing…"*), delete only the time-window phrase:

```
original:     "within ten (10) business days of the date of that notification, "
replacement:  ""
```

The obligation to confirm in writing is acceptable. Only the fixed deadline is not. Do not delete the whole paragraph.

**3. When adding language, append or insert into the existing sentence — do not rewrite it.**

If a non-solicit clause needs an unsolicited-approach carve-out, insert the carve-out text at the end of the existing sentence rather than replacing the sentence:

```
original:     "about whom you have received Information material to the recruitment of that individual."
replacement:  "about whom you have received Information material to the recruitment of that individual, or (c) such person proactively contacts TS Capital without any solicitation by TS Capital."
```

**4. When adding a qualifier to an obligation, insert the qualifier phrase — do not rewrite the obligation.**

```
original:     "in such event within ten (10) business days, you will return to us"
replacement:  "in such event you will, to the extent reasonably practicable, promptly return to us"
```

Only the qualifier phrase and the deadline are changed; the obligation to return remains.

**5. Entire-sentence or entire-paragraph deletion is only correct when the whole unit is objectionable and there is no acceptable version of it.**

Permitted examples: deleting an MNPI/insider-trading paragraph in full (the whole concept is unwanted); deleting a ceasing-interest notification clause in full (the whole obligation is unwanted). In these cases every word of the paragraph is the problem, so a full deletion is the minimum change.

**6. When adding items to an existing numbered list, APPEND ONLY — do not renumber or touch the existing items.**

The P21 human added two CI exceptions to a list ending "…or (ii) was disclosed in good faith to us by a third person legally entitled to disclose it." by appending `; (iii) was lawfully in our possession prior to disclosure by [Seller]; or (iv) was or becomes publicly available other than as a result of a breach of this confidentiality undertaking.` — the existing "or (ii)" was left exactly as it was. Do not add "consequential renumbering" micro-edits (deleting the `or`/`或` before the old last item): they multiply the tracked changes for zero legal effect. A resulting "(i) …, or (ii) …; (iii) …; or (iv) …" is acceptable; the counterparty's counsel will not care.

### The wrong pattern — never do this

❌ **Wrong** — deletes a correct sentence and re-inserts a modified version:
```
original:     "Subject to paragraph 7.3, the obligations pursuant to this letter shall be continuing for a period of three (3) years after the date of this letter, subject to earlier termination pursuant to the terms of this letter."
replacement:  "Subject to paragraph 7.3, the obligations pursuant to this letter shall be continuing for a period of two (2) years after the date of this letter, subject to earlier termination pursuant to the terms of this letter."
```

✅ **Right** — changes only what is wrong:
```
original:     "three (3) years"
replacement:  "two (2) years"
```

The wrong pattern produces an unnecessarily large tracked change that makes the counterparty review every word of the sentence for hidden differences. The right pattern makes the single point of disagreement immediately visible.

### Exception — genuine structural rewrites
Some changes require rewriting a whole sentence because the sentence's logical structure must change (not just a value within it). Example: P5's term clause, where the old sentence read *"This Agreement…will continue for a period of two (2) years from the date hereof"* and the replacement introduced a dual-trigger *"expire and cease…on the earlier of (i)…and (ii)…"* formula that cannot be expressed by editing words within the original. These are rare. If you are tempted to do a structural rewrite, confirm that no word-level or phrase-level edit can achieve the same result first.

### How the helper script renders your pairs
`apply_redlines.py` word-diffs each `original`/`replacement` pair and emits del/ins ONLY for the words that actually differ — unchanged words are never struck out and retyped (e.g. a sentence-level pair changing "two (2) years" renders as `DEL two INS one · DEL 2 INS 1 · DEL years INS year`; a pure append renders as a single INS with no deletion). This safety net does NOT relax the Minimum Change Principle: keep `original` scoped to the sentence or clause being changed, because (a) the margin comment anchors to the whole matched region, and (b) an over-broad `original` risks matching or colliding with other edits in the same paragraph.

---

## Knowledge Sources

At the start of each review session, read all three:
1. **Guideline**: `./knowledge/guideline.pdf`
2. **Signed precedents**: all files in `./knowledge/signed/` — final negotiated outcomes; show what was conceded.
3. **Human markup examples**: all files in `./knowledge/tracked/` — TS Capital's first-markup positions on real deals. **These are the primary reference for what to flag and how to redline.** If a type of issue never appears in the tracked markups, it is almost certainly not a material concern. Files prefixed `[人工]` or `[Human]` are human ground truth; files named `*_TS_markup*` without that prefix may be prior machine output — do NOT treat those as precedent.

When in doubt whether to flag something, ask: "Does this appear in the tracked human markups?" If no — do not flag it.

**Per-deal precedent lookup (mandatory first step)**: before reviewing any NDA, check whether `tracked/` or `signed/` contains a file whose name matches the deal name (e.g., reviewing `Project P2_NDA.docx` → check for `tracked/Project P2_NDA_TS Markup_v1.docx` and `signed/Project P2_NDA_TS-[Disclosing Party] Markup_vSigned.pdf`). If a matching tracked file exists, extract its insertions/deletions FIRST and mirror them — that file is the authoritative answer, not a starting point. Deviate from a matching tracked file only when you can articulate why the new NDA's text differs in a material way.

The **Tracked-File Index** below in this skill catalogues the verbatim edits for every readable tracked file — use it as a direct lookup table. Lean on it instead of re-deriving rules from the guideline.

Never access files outside `./knowledge/`.

---

## Step 0 — Classify the NDA Form (before anything else)

The human reviewers take systematically different positions depending on the NDA's form. Most historical over-edits came from applying one form's fixes to another form. Classify first; state the classification in your output.

| Form | How to recognize it | Positions that CHANGE by form |
|---|---|---|
| **A. US/HK company-form bilateral** (P8, P1, P4, P5) | "This Agreement is entered into by and between [Company] and [Recipient]"; numbered sections; Recipient/Company defined terms | Entity fill: natural-case full legal name in preamble (letter-style "To:" fills are ALL CAPS). Rep-responsibility sentence: KEEP (no undertaking carve-out — use Reps-definition carve-out instead, Example 13). Non-publicity: keep one-sided. Certifications/deadlines: keep when backup carve-out exists. |
| **B. German/European seller letter or agreement** (P7, P2, P10, P11) | Seller/Interested Party terminology; German-law references (verbundene Unternehmen, steht dafür ein); often [Disclosing Party]/seller-drafted | Undertaking carve-out for Authorized Recipients: ADD (P7 verbatim). Standalone Financing/Insurance Institutions section: DELETE in full. Portfolio-companies limb in Affiliate definition: DELETE. Records obligation: EXPAND institution list. |
| **C. Banker-run process letter** (P6/[sell-side bank], P5/[M&A advisor] governance elements, P14, P15) | Addressed "To: [bidder]" via the sell-side bank; Finance Provider / W&I Provider defined terms; process rules (single point of contact, no-contact) | Finance Provider / W&I sections: KEEP (never challenged). Process governance (contact rules, banker third-party-beneficiary): KEEP. Term/non-solicit still stepped down per the ladders. |
| **D. Chinese letter-form** (P9, [目标公司], P20) | 保密协议函; 贵方/本公司; letter header with [日期]/[联络人姓名] | Term: 2yr P9 dual-trigger formula (never 1yr). Non-solicit: keep 2yr and scope, add carve-out (c) only. Keep: 5-day window, 连带责任, waiver clauses, cost enumeration. Delete: 证明书 sentence, ceasing-interest sentence, 费用由贵方承担 rider, 消除影响 item. |

If the form is ambiguous, default to the most conservative treatment (fewer edits) and note the ambiguity.

**Bilingual EN/CN documents (P21, P22, P23)**: classify by the underlying form as above, then edit BOTH language versions in parallel — every English edit gets a Chinese twin in the paired paragraph. Entity names: `TS Capital Partners Management Limited` in English text, `信宸资本股权投资管理有限公司` in Chinese text (P22 signature block shows both). Signatory Name/Title: leave blank — differs per deal (see S1).

---

## Key Precedent Facts (from signed NDAs)

**Entity names and signatory:**
- English: TS Capital Partners Management Limited | Address: 28/F CITIC Tower, 1 Tim Mei Ave, Central, Hong Kong | Jurisdiction: Hong Kong
- Chinese: 信宸资本股权投资管理有限公司 | 地址: 香港中环添美道1号中信大厦28楼
- Signatory: NEVER fill a specific person's name or title in a signature block — in any case. The signatory is decided at signing time (Henry Zeng has signed some past deals but must not be written into markups)
- TS Capital is typically organized as a "company" (not LP or other structure) in English NDAs

**NDA Term:**
- English NDAs, original term ≤2 years: push to **1 year** on initial markup (P1, P5, P7). Fallback: 18 months → 2 years max.
- English NDAs, original term 3 years or longer: push to **2 years** via minimal word swap (P4 3→2, P6 3→2, P8 10→2). Do NOT jump to 1 year in one round.
- Chinese NDAs: All signed precedents have **2-year** terms. Use the "earlier of 2 years or transaction completion" formula from P9 precedent. Do NOT start at 1 year — go directly to 2 years with the correct formula.

**Non-Solicit Term:**
- English: same ladder as the NDA term — original ≤2yr and clock from signing → push to **1 year**; original ≥3yr → push to **2 years** on first markup (P4). Clock from return/destruction request → keep unchanged (P6). Fallback: 18 months → 24 months maximum (accepted in P10 German).
- Chinese: a **2-year** non-solicit is ACCEPTED as-is — the P9 CN human markup kept `两年` unchanged and also kept the `任何关联方` scope unchanged; the only edit was adding carve-out (c). Do not reduce the CN period or narrow the CN scope on initial markup.
- Always ADD a carve-out for unsolicited approaches: `or (c) such person proactively approaches TS Capital without solicitation` (English) / `或(c) 该等人员主动接洽（未经贵方邀请）` (Chinese).

**Affiliates and Portfolio Companies:**
- Co-managed funds in "Affiliate" definition: acceptable — they are part of the same fund family.
- Portfolio companies of TS Capital's funds: NOT acceptable — DELETE from the Affiliate definition entirely. Portfolio companies have no role in evaluating the target.
- Non-solicit binding affiliates who actually received CI: accepted (P10, P11).
- Non-solicit covering all affiliates regardless of CI receipt: must-flag.

**Governing Law:**
- German law: accepted for German-target deals (P10, P11, P2)
- PRC law: accepted for Chinese-target deals
- Korean law: may be unavoidable for Korean-target deals; flag but acknowledge
- US deals: NY or DE only; never IL

**Indemnification:**
- Full indemnification (任何性质全部损失, consequential damages, prosecution costs, 消除影响费用): must-flag.
- Acceptable replacement — mutual fee-shifting conditioned on final court judgment:
  - Chinese (P9 precedent): `若发生与本协议相关的诉讼，经有管辖权的法院作出终局且不可上诉的判决，认定一方违反本协议，则败诉方应向胜诉方偿付其为行使本协议项下权利而产生的合理法律费用及开支`
  - English (P4/P3 precedent): direct losses only, not lost profits or consequential damages, not applicable until established in final non-appealable court order.
- Full indemnification accepted in some Chinese deals (P12, P13) as a last concession.

**Financing Source Consent — two distinct patterns, opposite treatments:**
- **Pattern A — standalone restriction section in a company/seller-form bilateral NDA** (a bolt-on section titled e.g. "Financing Institutions and Insurance Institutions" that prohibits contacting financing banks/insurers without prior written consent): DELETE the entire section, heading and every sub-clause including any exclusivity paragraph. The P7 human markup deleted all 7 paragraphs of this section. Financing institutions should be treated as standard advisors / Authorized Recipients.
- **Pattern B — Finance Provider / W&I Provider architecture woven into a banker-run process letter** (defined terms like "Finance Provider" used throughout the Authorised Persons scheme; [sell-side bank]/[M&A advisor]-style processes — P6, P5, P14, P15): KEEP unchanged. These are process structure requirements; no tracked markup ever challenged them.
- Discriminator: is the NDA a bilateral company/seller form with a self-contained financing-restriction section (→ delete), or a sell-side process letter where the financing restrictions are integrated into the definitions and process mechanics (→ keep)?
- P11 accepted prior written consent as a concession — but the initial position for Pattern A is deletion.

**Representatives Carve-Out (undertaking mechanism) — apply selectively, not always:**
- Human markups added the undertaking carve-out ONLY where the NDA contains an express "[recipient] shall be responsible for any failure by any of its Authorized Recipients / Representatives" sentence in a German/European seller-form NDA (P7). P7 verbatim replacement: DEL `The Interested Party shall be responsible for any failure by any of its Authorized Recipients to comply with the terms of this Agreement.` → INS ` Notwithstanding anything contained herein to the contrary, the recipient will not be responsible for any breach or failure to comply with the terms of this Agreement by, or arising out of the actions of, any of the recipient's Representatives (other than the recipient's directors, officers or employees) if such Representative has signed an undertaking written confirmation, in which such the Representative confirms to be bound by all provisions of this agreement as if it was a party to this agreement.` (grammar quirks preserved from the human markup).
- In US/HK company-form NDAs the equivalent responsibility sentence was consistently KEPT: P8 human left "be responsible for any breach of this Agreement caused by any of its Representatives" untouched (the Reps-definition Notwithstanding carve-out did the work instead); P5 kept it too. P9 CN human kept the 连带责任 sentence. Do NOT add the undertaking carve-out in those forms.

**Records Obligation:**
- If NDA requires TS Capital to name who received CI: do NOT delete the clause.
- Instead, EXPAND the list of institution types (add financial advisors, consultants, financing sources) so those recipients fall under the "name + team leader only" bucket rather than "name all individuals."

**IC/LP Disclosure:**
- Accepted in Chinese NDAs to allow disclosure to IC members (投资决策委员会成员) and LP investors (有限合伙人).

---

## Tracked-File Index — Verbatim Human Edits (Primary Calibration Data)

Below is the **complete, verbatim** list of every insertion and deletion the human reviewer made across the readable `.docx` files in `./knowledge/tracked/`. This is the ground truth — the Gallery examples that follow are explanations of these edits. **If you are about to flag something not covered here or in the Gallery, stop.** This index supersedes any general rule that says otherwise.

Three tracked files are legacy OLE `.doc` binaries and cannot be parsed by the helper script: `P17_NDA_Trustar_MZH251216.docx` (a `.doc` misnamed with a `.docx` extension), `Standard NDA(EN)_P18 2020_P18 Legal20260601_TS Cmmts.doc`, and `Trustar Capital_NDA - 02.05.2026_TS markup.doc`. Headless Word COM conversion hangs on them. If the user manually opens each in Word and does Save As → .docx, extract their tracked changes and add them to this index — until then, rely on the readable files below for exact wording.

### `P1 - Company Form NDA (Clean)_TS Markup_v1.docx` (6 ins, 7 del)
- INS `'May 13, 2026'` — date fill (user-provided)
- INS `'TS CAPITAL PARTNERS MANAGEMENT '` — entity fill (note: old markup used ALL CAPS shorthand; current standard is `TS Capital Partners Management Limited` in all placements)
- INS `' to the extent legally permissible and reasonably practicable'` — compelled-disclosure notice qualifier (Cat 13b / Example 12)
- INS `'one '` (×2) — replaces "two" in the term and non-solicit clauses
- INS `' These provisions shall apply mutatis mutandis to both Parties, and the same remedies shall be available to the Receiving Party to enforce against the Disclosing Party in respect of any breach of this Agreement by the Disclosing Party or its Representatives.'` — Remedy mutuality clause (Cat 22 / Example 10)
- DEL the full US-securities MNPI acknowledgment paragraph (Cat 24 / Example 7)
- DEL `'immediately '` — pairs with the "to the extent legally permissible…" insert (Example 12)
- DEL `' (of which decision you will promptly, and in any event within 24 hours, notify the Company)'` — ceasing-interest deletion (Cat 11 / Example 9)
- DEL `'two '` (×2), `'s'` (×2) — pairs with the two "one" inserts for term and non-solicit (2y → 1y)

### `Project P2_NDA_TS Markup_v1.docx` (12 ins, 8 del)
- INS `'TS CAPITAL PARTNERS MANAGEMENT'` — entity fill (note: old markup used ALL CAPS shorthand; current standard is `TS Capital Partners Management Limited`)
- INS `'28/F CITIC Tower, 1 Tim Mei Ave '` + INS `'Central, Hong Kong'` — address split across the two original placeholder lines
- INS `':'` + INS `'('` + INS `'i) '` — recasting the existing (i) in the CI carve-out (Example 11)
- INS `'; (ii) was lawfully in the possession of the Interested Party prior to disclosure by [Disclosing Party]; (iii) lawfully obtained by the Interested Party from a third party that is not known to be bound by any confidentiality obligation to [Disclosing Party]; (iv) independently developed by or for the Interested Party without use of any Confidential Information received hereunder.'` — adding (ii)/(iii)/(iv) CI exceptions
- INS `'take reasonable legal steps to limit the scope of disclosure'` — replaces "pursue all available legal remedies…" (S4)
- INS `' written'` — narrows "request" to "written request" (S5)
- INS `' to the extent reasonably practicable and technologically feasible'` — destruction qualifier (S5, Example 4 variant)
- INS `'1 '` + DEL `'5 '` + DEL `'s'` — term 5 years → 1 year (S2)
- INS `' The arbitration proceeding and remedies shall be equally enforceable by both Parties without unilateral procedural disadvantage'` — arbitration mutuality (Cat 22 variant)
- DEL `'[name]'`, DEL `'[address]'` — placeholder removals before the entity/address fills
- DEL `'.'` (the period at end of existing CI exception (i))
- DEL `'pursue all available legal remedies against official or court orders'` (paired with the S4 insert)
- DEL `'Insider Information'` (heading) and DEL of the full insider-trading body paragraph (S7 / Example 7)

### `Project P3_NDA _TS markup_v1.docx` (0 ins, 0 del)
The tracked file shows zero in-text edits — likely the human chose to comment-only or the markup was lost. Do not treat absence of edits here as evidence the NDA was clean; cross-reference against the signed version if making a decision.

### `Project P4_NDA_Trustar Markup.docx` (8 ins, 3 del)
- INS `'to the extent reasonably practicable'` — destruction qualifier, **shorter P4 variant without "and technologically feasible"** (S5)
- INS `', '` — punctuation only
- INS `'provided that the foregoing indemnification shall not apply until the existence of such breach is established in a final, non-appealable order of a court of competent jurisdiction and, in any event, shall apply only to direct losses, damages, costs, or expenses (but not lost profits or any other indirect or consequential losses, damages, costs or expenses).'` — indemnification qualification (Cat 20 / Example 8)
- INS `' In the event of litigation relating to this Agreement, if a court of competent jurisdiction determines in a final non-appealable order that a party has breached this Agreement, then the non-prevailing party will reimburse the prevailing party for the reasonable legal fees and expenses incurred by it in connection with enforcing its rights hereunder, including any appeal therefrom.'` — mutual fee-shifting clause (Example 8)
- INS `'two'` + INS `'2'` + DEL `'three'` + DEL `'3'` — **non-solicit reduced 3 years → 2 years (NOT 1 year) on FIRST markup**. This is the standard first-markup position whenever the original period was 3 years or longer (same ladder as the NDA term — see S3).
- DEL `'.'` — punctuation pair for the indemnification qualifier insert

### `Project P5_NDA_TS markup_v1.docx` (15 ins, 7 del)
- DEL `'all of '` and DEL `' controlled affiliates and subsidiaries and its and their'` — **P5-style Reps narrowing**: the exact phrasing the human deleted from the Representatives definition. This is Approach B in Example 13. The deletion targets "all of [X] controlled affiliates and subsidiaries and its and their [Y]" → "[X] [Y]" — note that "all of " and the long affiliates clause are removed as TWO separate cuts, not one.
- DEL `'or '` and DEL `'.'` — punctuation/connector adjustments paired with the Reps deletions
- INS `', or (iv) was in '` + INS `'our'` + INS `' possession prior to '` + INS `'the '` + INS `'disclosure'` + INS `'.'` — **adds CI exception (iv) "prior possession"** to an existing list that already had (i)–(iii). Surgical, multi-insert approach (not one long insert).
- INS `'one '` + INS `'1'` + DEL `'two '` + DEL `'2'` — term 2 years → 1 year (S2)
- DEL `'This Agreement and the obligations thereunder will continue for a period of two (2) years from the date hereof.'` — old term sentence deleted in full
- INS `'This '` + INS `'a'` + INS `'greement expire and cease to have any force or effect on the earlier of (i) the first anniversary of the date hereof and (ii) the date of consummation of the '` + INS `'t'` + INS `'ransaction between the parties'` + INS `'.'` — **P5 dual-trigger term formula, verbatim** (note: "expire" not "shall expire" — preserved as-is from the human). This combination of "delete the old term sentence + insert dual-trigger" is the S2 preferred replacement.
- INS `' TS CAPITAL PARTNERS MANAGEMENT'` — entity fill (note: old markup used ALL CAPS shorthand; current standard is `TS Capital Partners Management Limited`)

### `[人工]P7 - Confidentiality Agreement - PE_Trustar markup_202510.docx` (20 changed paragraphs) — German seller-form bilateral NDA
- Preamble fill (in-sentence, natural case): DEL `[●]` placeholders → INS `TS Capital Partners Management Limited` + INS `company` + INS `Hong Kong` + INS `28/F CITIC Tower, 1 Tim Mei Ave, Central, Hong Kong` + DEL `and registered with the commercial register of [●] under [●] ` — **natural-case full legal name, NOT all caps** (S1)
- DEL portfolio-companies limb (ii) from the Affiliate definition (Example 2) + DEL the full follow-on paragraph (`Any provision of Confidential Information to portfolio companies of a Fund shall require prior written approval by Seller. Seller acknowledges that directors...`) (Cat 3)
- DEL `The Interested Party shall be responsible for any failure by any of its Authorized Recipients to comply with the terms of this Agreement.` → INS the Notwithstanding-undertaking carve-out (verbatim in Key Precedent Facts → Representatives Carve-Out) (Cat 6)
- Records obligation EXPANDED, not deleted: INS `, consultants, financial advisor` after "law firm" + INS `, ` + INS `potential sources of financing and other representatives` after "accounting firm" (Cat 23)
- Permitted-disclosure trigger broadened: INS `any law, regulation or legal, regulatory or judicial process ` + DEL `mandatory law, regulation, court order or applicable stock exchange rules` (S4)
- Return/destruction preamble qualifier: INS `to the extent reasonably practicable, ` after "shall promptly, " (S5 / Example 4)
- No-contact clause: appended an ordinary-course-of-Seller's-business exception to the existing no-name-basis carve-out (minor; only add when the clause lacks any ordinary-course carve-out)
- Non-solicit 2y → 1y: INS `one (1) year ` + DEL `two (2) years ` (S3)
- **Financing Institutions and Insurance Institutions section DELETED IN FULL** — heading + all six paragraphs including the exclusivity/treeing paragraph (Cat 9 Pattern A / Example 3)
- Term: INS `first ` + INS `(1st) ` + DEL `second (2nd) ` anniversary (S2 / Example 1)
- Signature block: DEL `[Interested Party]` → INS `TS Capital Partners Management Limited` (natural case)

### `[人工]NDA-P8_TCP comments 250918.docx` (7 changed paragraphs) — US-style company-form bilateral NDA (Cayman company)
- Preamble fill (in-sentence, natural case): INS `TS Capital Partners Management Limited` + DEL `[full legal company name]`; DEL `[place of company's formation & entity type]` → INS `company` + INS ` duly established and existing under the laws of Hong Kong`. **Date placeholder `[mm] [dd], [yyyy]` left UNCHANGED.** No address added.
- Reps definition: appended Approach A carve-out at end of Affiliates definition: INS `Notwithstanding the foregoing, in relation to the Recipient, Representatives shall not include equityholders or Affiliates to whom the Recipient has not provided Confidential Information.` (Cat 3 / Example 13-A)
- CI exceptions: DEL `or ` before (c) + INS `, or (d) was or is independently developed by the Recipient or on its behalf without violating the terms of this Agreement` (Cat 4)
- Compelled-disclosure qualifier normalized: DEL `not prohibited by law` → INS `legally permissible and reasonable practicable` (Cat 13b — applied even though a law-based qualifier already existed; "reasonable practicable" is the human's typo — write `reasonably practicable` in new markups)
- Return/destruction: INS `to the extent reasonable practicable, ` before "destroy" — **10-day deadline KEPT, both certifications KEPT** (backup carve-out was present in the same section) (Cat 14; same typo note — use `reasonably practicable`)
- Term 10y → 2y minimal swap: DEL `ten ` + INS `two ` + DEL `10` + INS `2` (S2 ladder — NOT the dual-trigger, NOT 1 year)
- Signature block: INS `TS Capital Partners Management Limited` (natural case) + DEL `[NAME OF COUNTERPARTY]`
- **NOT changed**: one-sided secrecy-of-discussions clause (Cat 7); "responsible for any breach…by any of its Representatives" (Cat 6); Governing law; Remedies.

### `P9_NDA Form - CN-模板-Trustar Makeup.DOCX` (9 changed paragraphs) — Chinese letter-form NDA ([目标公司] target)
- Date: DEL `[日期]` → INS `2025年11月10日` (user-provided); entity/address/contact fills: `信宸资本股权投资管理有限公司`, `香港中环添美道1号中信大厦28楼`, contact `程希科`
- §1 permitted-disclosure condition (ii): INS `及时通知` + DEL `书面` + DEL `同意披露` → reads `(ii)及时通知本公司` (S6)
- §2 misuse assistance: DEL ONLY `，有关费用由贵方承担` — notification + assistance obligation KEPT (Cat 10)
- §5 ceasing interest: DEL the whole sentence `则贵方应尽快(且在任何情况下于24小时内)通知本公司该决定。` (Cat 11 / Example 5); DEL the whole 证明书 sentence (销毁证明); **5-working-day window KEPT unqualified**
- §12 non-solicit: 两年 KEPT; 任何关联方 scope KEPT; DEL `或` before (b) + INS `，或(c) 该等人员主动接洽（未经贵方邀请）` (S3)
- §13 indemnification: replace full-indemnity body with the mutual fee-shifting formula + DEL `，以及受偿人为消除影响而发生的费用` + INS trailing `赔偿仅在 有管辖权的法院作出终局且不可上诉的判决，确认违约事实存在后才生效。` — cost enumeration KEPT (Example 6)
- §16 term: DEL `而前述条款在适用法律允许的最迟日期前一直具有约束力，本协议函其余条款自本协议函签订之日起十年后逾期失效。` → INS the P9 dual-trigger 2-year formula; **第13条 KEPT in the permanent-exceptions list** (Revision Principle 9)
- **NOT changed**: 连带责任 sentence; 律师意见 wording; waiver-of-claims clause; 5-working-day window; non-solicit term/scope.

### `[Human]Project P6 - NDA vF_TS_markup.docx` (8 changes) — [Target], [sell-side bank] process, Netherlands law
- DEL `'To:'` + DEL `'[●]'` → INS `'To:TS CAPITAL PARTNERS MANAGEMENT'` — entity fill (note: old markup used ALL CAPS shorthand; current standard is `To:TS Capital Partners Management Limited`)
- DEL `'in such event within ten (10) business days, you will return to us'` → INS `'in such event you will, to the extent reasonably practicable, promptly return to us'` — return qualifier + deadline removal (S5/Cat14)
- DEL `'within ten (10) business days of the date of that notification, '` — ONLY the time-window from certification clause; full clause kept because §7.3 backup-files carve-out already limits exposure (Cat14b fallback applies)
- INS `', or (c) such person proactively contacts TS Capital without any solicitation by TS Capital.'` — unsolicited carve-out added; **non-solicit period NOT changed** (2yr kept; trigger is from return/destruction request, not from signing)
- DEL `'three'` + DEL `'3'` → INS `'two'` + INS `'2'` — **NDA term 3 → 2 years (NOT 1 year)**; P4 3→2yr step-down applied
- DEL `'thereof and the (direct and indirect) shareholders '` — surgical narrowing of third-party beneficiary (Cat18)
- DEL `'[●] hereby agrees to the terms of the above letter.'` → INS `'TS CAPITAL PARTNERS MANAGEMENT hereby agrees to the terms of the above letter.'` — entity fill (note: old markup used ALL CAPS shorthand; current standard is `TS Capital Partners Management Limited hereby agrees...`)
- DEL `'For and on behalf of'` + DEL `'[●]'` → INS `'For and on behalf ofTS Capital Partners Management Limited'` — signature block fill (S1)
- **NOT changed (all kept)**: Finance Provider exclusion from Authorised Persons; Finance Provider disclosure prohibition; paras 9.4/9.5/9.6 (Finance Provider contact, co-investor consent, W&I Provider); Finance Provider definition; W&I Provider definition. **[sell-side bank] banker-run deal — these are process structure requirements, same reason P5 kept [M&A advisor] governance. Finance Provider sections are NEVER challenged in any tracked markup (see Negative Space).**

### `[Human]Project P21_Confidentiality Undertaking_Bilingual_TS markup_v2.docx` (18 changed paragraphs) — bilingual EN/CN seller letter-form undertaking, HK law/HKIAC, TS = buyer/recipient
- **Party-role lesson**: letterhead `[Seller entity]`, `[Seller address]` and date `[●], 2026` ALL LEFT UNFILLED — they are the counterparty's blanks. A machine run that filled them with TS's name/address was corrected by the human. TS details go ONLY in the signature block ("receiving entity").
- Signature block: entity filled EN+CN (`TS Capital Partners Management Limited` / `信宸资本股权投资管理有限公司`). The human also filled `Name:`/`Title:`/address in that file, but per user instruction (2026-07-16) NEVER put a specific person's name/title in the signature block in any markup — leave them blank; do not copy that part of this precedent
- MNPI/insider-trading sentence: deleted in full, EN + CN. Margin comment adds the fallback: "We only accept it for listed company."
- Return/destruction: INS `, to extent reasonably practicable, ` before `promptly` (human typo — write `to the extent`); the destruction-certification sentence DELETED IN FULL in both languages (`The destruction of Confidential Information will be certified in writing to you by an authorized officer supervising such destruction.` / `机密信息的销毁将由监督该等销毁的授权人员以书面形式向贵司证明。`); `upon your request` KEPT — no ` written` added
- Term (original was INDEFINITE — until public availability or Seller notice): full structural rewrite to a 1-year dual-trigger that absorbs the old public-availability limb: INS `will expire and cease to have any force or effect on the earlier of (i) the first anniversary of the date hereof, (ii) when all the Confidential Information becomes available to the public otherwise than by disclosure in breach of the terms of this confidentiality undertaking, or (iii) the date of consummation of the transaction between the parties.` CN twin: `将于下列最早发生之时终止并失效：(i) 本保密承诺书签署之日起满一周年之日，(ii) 所有机密信息并非因违反本保密承诺书条款的披露而为公众所知之时，或 (iii) 双方完成交易之日。` — an indefinite original is treated like a ≤2yr original (1-year dual-trigger), NOT like a ≥3yr original
- CI exceptions: APPEND-ONLY after `disclose it`: `; (iii) was lawfully in our possession prior to disclosure by [Seller]; or (iv) was or becomes publicly available other than as a result of a breach of this confidentiality undertaking.` — the existing `or (ii)` was NOT renumbered; CN twin appended likewise
- Compelled disclosure: qualifier INS `, to` + `extent legally permissible and reasonably practicable, ` added ONLY to the unqualified notice obligation; a `to the extent legally permissible` already present in the secrecy-of-discussions parenthetical was LEFT UNTOUCHED
- Remedy mutuality: P1 mutatis-mutandis clause appended VERBATIM (keeps "Receiving Party"/"Disclosing Party" wording even though those terms are undefined in the letter); CN twin: `上述条款对双方同等适用，如披露方或其代表违反本保密承诺书，接收方亦有权寻求相同的救济。`
- **NON-SOLICIT KEPT ENTIRELY UNCHANGED** — 2 years from signing, no reduction, no unsolicited carve-out added. The clause was already narrow: only employees "connected with the Proposed Transaction", with existing carve-outs for general recruitment ads and employees departed 6+ months. When scope is that narrow with real carve-outs, a 2-year period is accepted as-is.
- Every EN edit has a CN twin in the paired Chinese paragraph.
- **NOT changed**: one-sided secrecy-of-discussions + no-consortium sentence; designated-contact/no-contact clause; non-reliance disclaimer; HK governing law/HKIAC; severability; all `[Seller]` references in the body.

### Cross-file patterns
- **Entity fill**: use the full legal name `TS Capital Partners Management Limited` (natural case with "Limited") in all placements — letterhead, preamble, signature block, all references.
- **Term reduction**: the ladder is driven by the ORIGINAL term. Original ≤2 years → push to 1 year (P1 2→1, P5 2→1, P7 2→1). Original 3 years or longer → push to **2 years** via minimal word swap (P4 3→2, P6 3→2, **P8 10→2**: DEL `ten`/`10`, INS `two`/`2`) — do NOT jump to 1yr in one round from a long original, and do NOT use the P5 dual-trigger rewrite for the step-down (the human used a simple number swap even on a 10-year original). P2 5→1 is the lone aggressive outlier (German seller letter); treat it as an exception, not the default. **INDEFINITE original (no fixed outside date at all — e.g. "until public availability or Seller notice") → treat like a ≤2yr original: 1-year dual-trigger structural rewrite, preserving any useful existing limb inside the new formula (P21).**
- **Non-solicit reduction**: same original-term ladder as the NDA term — English ≤2yr original with clock from signing → 1 year (P1 2→1, P7 2→1); ≥3yr original → 2 years on first markup (P4 3→2); **when trigger is from return/destruction request (not from signing), the period is kept unchanged (P6)**; **when the clause is already narrowly scoped (only employees connected with the transaction) AND already carries real carve-outs (general recruitment ads, long-departed employees), a 2-year period is KEPT with no edits at all — not even the unsolicited carve-out (P21)**. Chinese: 2yr kept as-is (P9) — carve-out (c) is the only edit.
- **CI exceptions**: when the NDA has some but not all of (i)–(iv), only add what's missing — P5 added just (iv) because (i)–(iii) were already present.
- **MNPI / Insider Information**: always deleted in full (P1, P2).
- **Compelled disclosure notice**: always normalized to "to the extent legally permissible and reasonably practicable" (P1).
- **Ceasing-interest notification**: always deleted entirely, not just the time limit (P1).
- **Remedy mutuality**: always ADDED as an appended clause, never as a replacement (P1, P2).

---

## Gallery of Real Examples

These are verbatim redlines from actual TS Capital human markups. Study these before reviewing any new NDA — they show exactly what a correct redline looks like, including how surgical the ORIGINAL_TEXT is and what a good COMMENT explains.

---

### EXAMPLE 1 — Term Reduction (P7 English NDA, §10)

**What triggers it**: NDA term exceeds the ladder target (see S2): original ≤2yr → push to 1yr (this example); original ≥3yr → push to 2yr instead.

**Original clause**:
> "...the provisions of this Agreement shall remain in full force and effect at all times until the earlier of (i) **the second (2nd) anniversary** of the date hereof or (ii) the execution of definitive documents..."

```
ORIGINAL_TEXT:  "second (2nd) anniversary"
REPLACEMENT_TEXT: "first (1st) anniversary"
COMMENT: "Standard position is 1-year NDA term. Willing to accept up to 2 years if counterparty pushes. The shorter the term, the sooner our obligations expire if we don't proceed."
```

**What NOT to do**: Do not rewrite the whole sentence. A 4-word change is all that's needed.

---

### EXAMPLE 2 — Portfolio Companies: DELETE from Affiliate Definition (P7 English NDA, §1)

**What triggers it**: The Affiliate definition includes "portfolio companies of each of such Funds."

**Original clause**:
> `"Affiliate" shall mean... including, in the case of an Interested Party which manages or advises private equity or similar funds, (i) each of such funds and the managers and the funds managed by the same manager... (herein "Funds"), **and (ii) the portfolio companies of each of such Funds... (herein the "Portfolio Companies"), to the extent such Portfolio Companies have actually received Confidential Information**`

Two changes needed — one in the definition, one in the follow-on paragraph:

```
ORIGINAL_TEXT:  "and (ii) the portfolio companies of each of such Funds (and in each case their respective affiliates (verbundene Unternehmen) within the meaning of Section 15 German Stock Corporation Act (AktG) or corresponding provisions under the laws of other jurisdictions) (herein the \"Portfolio Companies\"), to the extent such Portfolio Companies have actually received Confidential Information"
REPLACEMENT_TEXT: ""
COMMENT: "Portfolio companies of our funds are separate businesses with no role in evaluating this transaction. We have no control over their day-to-day operations and should not be responsible for their conduct. Co-managed funds (limb (i)) remain in the definition — they are legitimately part of our fund family."
```

```
ORIGINAL_TEXT:  "Any provision of Confidential Information to portfolio companies of a Fund shall require prior written approval by Seller."
REPLACEMENT_TEXT: ""
COMMENT: "Consequential deletion — the follow-on paragraph only exists because portfolio companies were in the definition. Once deleted from the definition, this paragraph is moot."
```

**What NOT to do**: Do not delete limb (i) (co-managed funds). Do not add language limiting portfolio companies to "those who received CI" — delete them entirely.

---

### EXAMPLE 3 — Delete Entire Financing Institutions Section (P7 English NDA, §8)

**What triggers it**: A dedicated section restricting disclosure to or contact with Financing Institutions / Insurance Institutions.

**What the section looks like**: A full section titled "Financing Institutions and Insurance Institutions" that prohibits contact with debt financing sources or insurance brokers without prior written consent, often also prohibiting exclusivity arrangements.

**Approach**: Delete every paragraph in the section — not just the consent requirement. The title, each sub-clause, and any exclusivity paragraph all go.

```
ORIGINAL_TEXT:  "contact any financing banks or other potential providers of debt financing (herein collectively "Financing Institutions") in relation to a financing of the Transaction; and"
REPLACEMENT_TEXT: ""
COMMENT: "Financing institutions should be treated as standard advisors — they are already covered as Authorized Recipients. A dedicated section creating a separate restricted category with prior written consent requirements would prevent us from financing any transaction without the seller's pre-approval, which is operationally unworkable."
```

*(Repeat ORIGINAL_TEXT / REPLACEMENT_TEXT for each paragraph in the section until the whole section is deleted. The P7 human markup deleted the heading plus all six body paragraphs, including the exclusivity/treeing paragraph.)*

**What NOT to do**: Do not just delete the consent requirement and keep the rest. The entire section must go.

**Scope limit**: This deletion applies ONLY to a standalone bolt-on section in a company/seller-form bilateral NDA (Pattern A). Finance Provider / W&I Provider restrictions integrated into a banker-run process letter (P6, P5) are KEPT — see Cat 9 and Negative Space.

---

### EXAMPLE 4 — Return/Destruction: Add "Reasonably Practicable" to Preamble (P7 English NDA, §5)

**What triggers it**: Return/destruction obligation with no "reasonably practicable" qualifier, OR where the qualifier only appears in the electronic purge sub-clause.

**Original clause**:
> "...the Interested Party shall promptly, upon written request of Seller (email being sufficient):"

```
ORIGINAL_TEXT:  "the Interested Party shall promptly, upon written request of Seller (email being sufficient):"
REPLACEMENT_TEXT: "the Interested Party shall promptly, to the extent reasonably practicable, upon written request of Seller (email being sufficient):"
COMMENT: "An unqualified obligation to destroy ALL Confidential Information is impossible — automated backups, email archives, and system snapshots cannot be individually purged. The qualifier must go in the preamble so it covers the whole obligation, not just the electronic purge sub-clause. Accepted in a prior German-law project precedent."
```

**What NOT to do**: Do not add "reasonably practicable" only to the electronic purge sub-clause — it must cover the full obligation. Placement can be mid-clause (as above), trailing after the main obligation, or at end of sentence — any position that covers the whole destruction/return requirement is acceptable.

---

### EXAMPLE 5 (Chinese) — Ceasing Interest: DELETE the Entire Notification Sentence (P9 CN NDA, §5)

**What triggers it**: A clause requiring TS Capital to notify the counterparty if it decides not to proceed, especially with a hard time limit (24小时内).

**Original clause**:
> `5、（a）如果贵方决定不进行相关交易，则贵方应尽快(且在任何情况下于24小时内)通知本公司该决定。在该情况下，或在本公司要求的任何其他时间...`

```
ORIGINAL_TEXT:  "则贵方应尽快(且在任何情况下于24小时内)通知本公司该决定。"
REPLACEMENT_TEXT: ""
COMMENT: "TS Capital has no obligation to tell a counterparty whether it will or will not invest. This is an investment decision that is entirely internal. Deleting the entire notification obligation, not just the 24-hour time limit — the obligation itself is what we object to."
```

**What NOT to do**: Do not delete only `且在任何情况下于24小时内` while keeping the ceasing-interest notification. Delete the entire sentence.

---

### EXAMPLE 6 (Chinese) — Indemnification: Replace with Mutual Fee-Shifting (P9 CN NDA, §13)

**What triggers it**: Full indemnification clause covering `任何性质的全部损失、损害赔偿、成本、权利主张` without requiring a court judgment first, or including `消除影响费用`.

**Original clause (excerpt)**:
> `...任何性质的全部损失、损害赔偿、成本、权利主张、要求、责任和费用，贵方同意向本公司(为本公司并且代表本公司代表)(统称"受偿人")作出赔偿、辩护并使本公司免于承担责任。为免疑义，赔偿包括(但不限于)...律师费、公证费、差旅费，以及受偿人为消除影响而发生的费用等)。`

Two changes — replace the main clause, then separately delete the 消除影响 item:

```
ORIGINAL_TEXT:  "任何性质的全部损失、损害赔偿、成本、权利主张、要求、责任和费用，贵方同意向本公司(为本公司并且代表本公司代表) (统称"受偿人")作出赔偿、辩护并使本公司免于承担责任。为免疑义，赔偿包括(但不限于)任何受偿人在执行本协议函条款时或由于就本协议函项下的责任主张权利要求进行抗辩或解决该权利要求而产生的任何费用或开支"
REPLACEMENT_TEXT: "经有管辖权的法院作出终局且不可上诉的判决，认定一方违反本协议，则败诉方应向胜诉方偿付其为行使本协议项下权利而产生的合理法律费用及开支"
COMMENT: "Full indemnification creates open-ended financial exposure with no upper limit and no need for a court to find a breach. Replaced with a mutual fee-shifting formula conditioned on a final non-appealable judgment — both parties can invoke it, and only after a court confirms a violation."
```

```
ORIGINAL_TEXT:  "，以及受偿人为消除影响而发生的费用"
REPLACEMENT_TEXT: ""
COMMENT: "Reputation cleanup costs (消除影响费用) are entirely open-ended and subjective. Even under the revised mutual formula, these costs should not be recoverable."
```

The P9 human also appended a final-judgment prerequisite AFTER the surviving cost enumeration (third change, verbatim): INS `赔偿仅在 有管辖权的法院作出终局且不可上诉的判决，确认违约事实存在后才生效。` — and KEPT the `(包括但不限于调查费、鉴证费、律师费、公证费、差旅费等)` enumeration itself (minus the 消除影响 item). Do not delete the enumeration.

**What NOT to do**: Do not write a one-sided replacement where only TS Capital is liable. The replacement must be mutual — both parties can invoke it after a final judgment. Do not delete the cost enumeration parenthetical.

---

### EXAMPLE 7 — DELETE MNPI / Insider Trading Restriction Clauses (P1 English NDA; P2 German NDA)

**What triggers it**: Any clause that (i) acknowledges US/applicable securities laws, (ii) restricts trading in the target's securities based on receipt of Confidential Information, or (iii) is titled "Insider Information" with a prohibition on unlawful use.

**P1 — full US securities law acknowledgment paragraph**:

```
ORIGINAL_TEXT: "You hereby acknowledge that you are aware, and that you will advise your Representatives who are informed as to the matters which are the subject of this agreement, that the United States securities laws prohibit any person who has received from an issuer material, non-public information concerning the matters which are the subject of this agreement from purchasing or selling securities of such issuer"
REPLACEMENT_TEXT: ""
COMMENT: "TS Capital has its own internal MNPI compliance procedures. A blanket US securities law acknowledgment is inappropriate for a non-US entity. Deleted in full — prior project precedent."
```

**P2 — section heading + clause body (two separate changes)**:

```
ORIGINAL_TEXT: "Insider Information"
REPLACEMENT_TEXT: ""
COMMENT: "Section heading deleted consequentially — the entire Insider Information section is being removed."
```

```
ORIGINAL_TEXT: "The Interested Party acknowledges that some or all of the Information may constitute, or be deemed to constitute, price-sensitive information, the use of which may be subject to regulation or prohibition under applicable insider trading laws. The Interested Party undertakes not to use the Information for any unlawful purpose."
REPLACEMENT_TEXT: ""
COMMENT: "TS Capital already has internal compliance obligations not to misuse MNPI. An NDA-level undertaking creates duplicative and potentially conflicting obligations. Deleted in full — prior project precedent."
```

**What NOT to do**: Do not narrow the clause or add a carve-out. DELETE the entire provision — both in P1 and P2 the entire text was removed with no replacement.

---

### EXAMPLE 8 — Indemnification: English Formula (P4 English NDA)

**What triggers it**: Full indemnification clause with "any loss, damage, expense or other liability... including attorney's fees and court costs" and no court-order prerequisite and no direct-losses-only limitation.

**Original clause**:
> `"we agree to indemnify and hold the Company and the Company's Representatives harmless and indemnified against any loss, damage, expense or other liability caused by such breach, including, but not limited to, attorney's fees and court costs incurred in connection with the enforcement hereof."`

**One surgical change** — replace the period at the end with a qualifying clause (do NOT delete the indemnification; qualify it):

```
ORIGINAL_TEXT: "attorney's fees and court costs incurred in connection with the enforcement hereof."
REPLACEMENT_TEXT: "attorney's fees and court costs incurred in connection with the enforcement hereof, provided that the foregoing indemnification shall not apply until the existence of such breach is established in a final, non-appealable order of a court of competent jurisdiction and, in any event, shall apply only to direct losses, damages, costs, or expenses (but not lost profits or any other indirect or consequential losses, damages, costs or expenses). In the event of litigation relating to this Agreement, if a court of competent jurisdiction determines in a final non-appealable order that a party has breached this Agreement, then the non-prevailing party will reimburse the prevailing party for the reasonable legal fees and expenses incurred by it in connection with enforcing its rights hereunder, including any appeal therefrom."
COMMENT: "Full indemnification without a court-order prerequisite creates open-ended financial exposure. Qualified to: (i) direct losses only, no consequential damages; (ii) not applicable until a final non-appealable court order confirms a breach; (iii) mutual fee-shifting — both parties can invoke it. Prior project precedent."
```

**What NOT to do**: Do not delete the indemnification clause entirely — the fix is a qualification, not a deletion. Keep the "including attorney's fees and court costs" language; just add the carve-out after it.

---

### EXAMPLE 9 — Ceasing Interest: English Version (P1 English NDA)

**What triggers it**: Any parenthetical or clause requiring TS Capital to notify the counterparty of a decision not to proceed, typically embedded in the return/destruction clause.

**Original clause (excerpt)**:
> `"...or on your own initiative if you decide not to proceed with the Transaction (of which decision you will promptly, and in any event within 24 hours, notify the Company), you will, as directed by the Company..."`

```
ORIGINAL_TEXT: " (of which decision you will promptly, and in any event within 24 hours, notify the Company)"
REPLACEMENT_TEXT: ""
COMMENT: "TS Capital has no obligation to inform a counterparty whether it will or will not invest. Investment decisions are entirely internal. Deleting the entire notification obligation — not just the 24-hour time limit. Prior project precedent."
```

**What NOT to do**: Do not delete only the 24-hour limit while keeping the notification obligation. Delete the entire parenthetical in one change.

---

### EXAMPLE 10 — Remedy Asymmetry: Add Mutual Clause (P1 English NDA)

**What triggers it**: Injunctive relief, specific performance, or equitable remedy provisions that are one-sided — i.e., they can only be enforced by the Company/disclosing party against TS Capital, with no reciprocal right for TS Capital.

**Original clause (final sentence)**:
> `"Such remedy shall not be deemed to be the exclusive remedy for your breach of this agreement, but shall be in addition to all other remedies available at law or in equity to the Company."`

**Fix: ADD a mutual clause — do NOT delete the original provision**:

```
ORIGINAL_TEXT: "Such remedy shall not be deemed to be the exclusive remedy for your breach of this agreement, but shall be in addition to all other remedies available at law or in equity to the Company."
REPLACEMENT_TEXT: "Such remedy shall not be deemed to be the exclusive remedy for your breach of this agreement, but shall be in addition to all other remedies available at law or in equity to the Company. These provisions shall apply mutatis mutandis to both Parties, and the same remedies shall be available to the Receiving Party to enforce against the Disclosing Party in respect of any breach of this Agreement by the Disclosing Party or its Representatives."
COMMENT: "Injunctive relief and equitable remedies should be available to both parties equally. Adding a mutatis mutandis reciprocity clause rather than deleting the original provision — TS Capital should also have access to injunctive relief if the disclosing party breaches. Prior project precedent."
```

**What NOT to do**: Do not delete the one-sided provision. The fix is to extend the same remedies to TS Capital by adding a reciprocal clause.

---

### EXAMPLE 11 — CI Exceptions: Add Missing Carve-Outs (P2 German NDA)

**What triggers it**: The "Confidential Information does not include" carve-out list has only one item (typically "publicly available information") and is missing the other three standard exceptions.

**Original clause**:
> `"Information within the meaning of this Agreement does not include Information that the Interested Party can demonstrate is publicly available, provided such public availability is not the result of a breach of any statutory obligation or of any agreement between the Parties."`

**Fix: Format (i) properly and ADD (ii)–(iv)**:

```
ORIGINAL_TEXT: "does not include Information that the Interested Party can demonstrate is publicly available, provided such public availability is not the result of a breach of any statutory obligation or of any agreement between the Parties."
REPLACEMENT_TEXT: "does not include: (i) Information that the Interested Party can demonstrate is publicly available, provided such public availability is not the result of a breach of any statutory obligation or of any agreement between the Parties; (ii) was lawfully in the possession of the Interested Party prior to disclosure by [Disclosing Party]; (iii) lawfully obtained by the Interested Party from a third party that is not known to be bound by any confidentiality obligation to [Disclosing Party]; (iv) independently developed by or for the Interested Party without use of any Confidential Information received hereunder."
COMMENT: "Standard CI exceptions must include all four carve-outs: (i) public info; (ii) prior possession; (iii) received from third party without restriction; (iv) independently developed. The NDA currently has only (i). Prior project precedent."
```

**What NOT to do**: Do not add exceptions piecemeal or in different locations. Reformat the entire carve-out block to include all four in one numbered list.

---

### EXAMPLE 12 — Permitted Disclosure: Add "To Extent Legally Permissible" to Notice Obligation (P1 English NDA)

**What triggers it**: In the compelled disclosure clause, the notification obligation to the disclosing party has no "to the extent legally permissible and reasonably practicable" qualifier — meaning TS Capital must notify even when legally prohibited from doing so (e.g., under a gag order).

**Original clause (excerpt)**:
> `"the Receiving Party agrees to immediately notify the Disclosing Party of the existence, terms and circumstances surrounding such request, so that it may seek an appropriate protective order"`

Two changes needed — remove "immediately" AND add the qualifier:

```
ORIGINAL_TEXT: "the Receiving Party agrees to immediately notify the Disclosing Party of the existence, terms and circumstances surrounding such request, so that it may seek an appropriate protective order"
REPLACEMENT_TEXT: "the Receiving Party agrees to notify the Disclosing Party of the existence, terms and circumstances surrounding such request to the extent legally permissible and reasonably practicable, so that it may seek an appropriate protective order"
COMMENT: "Removing 'immediately' (unrealistic where legal advice is needed first) and adding 'to the extent legally permissible and reasonably practicable' — a gag order accompanying a subpoena may legally prohibit TS Capital from disclosing that a compelled disclosure request has been made. Prior project precedent."
```

**What NOT to do**: Do not change the rest of the compelled disclosure clause (e.g., "all best efforts to preserve confidentiality of the remainder" and "written opinion" language). Only the notification obligation needs the qualifier.

**Also do NOT skip this change just because a similar-sounding qualifier already exists.** "To the extent not prohibited by law" and "to the extent permitted by law" both look adequate but are not — they only protect against legal prohibition (gag orders), not against practical impossibility (need for counsel, response time, drafting). Normalize to the exact phrase "to the extent legally permissible and reasonably practicable" every time. P8 precedent shows this change being applied even where "to the extent not prohibited by law" was already in the original.

---

### EXAMPLE 13 — Representatives Narrowing: P10-Style Carve-Out vs P5-Style Hard Delete (P8 English NDA)

**What triggers it**: Representatives definition extends to "Affiliates" of a Party (e.g., "officers, directors... of a Party or such Party's Affiliates"). This makes the Recipient responsible for breaches by employees of all controlled affiliates / portfolio companies.

**Two acceptable approaches** — pick one based on context:

**Approach A — P10-style carve-out (preferred when definition is otherwise reasonable; P8 precedent)**

Keep the existing definition intact; append a "Notwithstanding" carve-out that limits the Recipient's exposure AND explicitly excludes equityholders (LP investors):

```
ORIGINAL_TEXT: "controlling, or under common control with a Party."  [end of Affiliates definition block]
REPLACEMENT_TEXT: "controlling, or under common control with a Party. Notwithstanding the foregoing, in relation to the Recipient, Representatives shall not include equityholders or Affiliates to whom the Recipient has not provided Confidential Information."
COMMENT: "Limits Recipient's exposure to Affiliates that actually received Confidential Information (prior project precedent) AND explicitly excludes equityholders — preserves IC/LP disclosure flexibility without rewriting the underlying definition. Prior project precedent."
```

**Approach B — P5-style hard delete (use when minimal change footprint is preferred; VERBATIM P5 edits)**

In P5 the human deleted exactly these two strings from the Representatives definition (separate cuts, not one):

```
ORIGINAL_TEXT: "all of "
REPLACEMENT_TEXT: ""

ORIGINAL_TEXT: " controlled affiliates and subsidiaries and its and their"
REPLACEMENT_TEXT: ""

COMMENT: "Narrows Representatives by removing 'all of [Party's] controlled affiliates and subsidiaries and its and their [people]' — TS Capital should not be on the hook for breaches by every controlled entity in the corporate tree. Surgical: two short deletions, no rewriting. Prior project precedent."
```

When the target NDA uses different wording but the same structural problem (Representatives extended to a Party's Affiliates), adapt the surgical principle: find the smallest contiguous string whose deletion narrows the definition cleanly. Do NOT replace with a rewritten clause — just delete.

**When to choose A**: NDA is otherwise sensibly drafted; equityholders/LPs need explicit protection; diplomatic markup preferred (preserves the counterparty's drafting). This is the better default for English NDAs going forward.

**When to choose B**: NDA already has many flagged issues and you want minimal change footprint; the Affiliates qualifier is the only Representatives concern.

**What NOT to do**: Do not do both. Pick one. Approach A is preferred when in doubt.

---

## Standard Changes (Always Apply on First Markup)

These changes are made on every NDA regardless of whether the specific language triggers a must-fix flag. Apply them as tracked changes with comments.

### S1 — Fill In TS Capital's Blanks (Date, Entity, Address, Contact)

**Step 1 — Identify TS Capital's role BEFORE touching any placeholder.** TS Capital is usually the buyer/recipient (evaluating a target), but in exit processes TS is the seller/discloser and the counterparty signs. Determine the role from the document's structure, not from assumptions:
- Who SIGNS this document ("we", the party giving the undertaking, the signature block)? Who is it ADDRESSED to ("you", the letterhead/addressee block)?
- In a letter-form undertaking, the letterhead at the top is the ADDRESSEE — the other side. The signing party appears only in the signature block at the bottom.

**Step 2 — For every placeholder, ask: WHOSE blank is this?** Fill ONLY placeholders that denote TS Capital's own party. **LEAVE counterparty placeholders unfilled** — `[Seller entity]`, `[Seller address]`, `[Seller]`, `[Company]`, `[Target]`, and any addressee block that belongs to the other side. Filling a counterparty blank with TS Capital's name corrupts the document (P21 failure: a skill run filled the `[Seller entity]`/`[Seller address]` letterhead with TS's name and address; the human left both untouched because TS was the buyer — TS's details belong only in the signature block, which says "receiving entity").

**Step 3 — Scan for TS-side placeholders** and fill every one: `[●]`, `[日期]`, `[Date]`, `[协议对方名称]`, `[Interested Party]`, `[Bidder]`, `[地址]`, `[Address]`, `[联络人姓名]`, `[insert full company name of receiving entity]`, `[插入接收实体全称]` — but only after Step 2 confirms the blank refers to TS's role.

**Date** (`[日期]` / `[Date]` / `[●]` / `[mm] [dd], [yyyy]`): Fill ONLY if the user provides an actual execution date. Otherwise **leave the placeholder unchanged** — the date is filled at signing time, not at markup. Do not pre-fill with `[●]`, `TBD`, or anything else. P8 precedent.

**Entity name** — use the full legal name everywhere:
- **All placements** (letterhead, preamble, signature block, body references): use `TS Capital Partners Management Limited` (full name, natural case, with "Limited").
- **In-sentence party identification in the preamble/body** (agreement-style NDAs: "...is entered into by and between X and `[full legal company name]`, a `[place of formation & entity type]`..." — P8, P7): fill with `TS Capital Partners Management Limited` and fill the formation blank as `company` organized/established under the laws of `Hong Kong`. P8-style fill (verbatim): `TS Capital Partners Management Limited, a company duly established and existing under the laws of Hong Kong`. Do NOT add the Hong Kong address in the preamble unless the original placeholder asks for one. DELETE any commercial-register tail (P7 human deleted `and registered with the commercial register of [●] under [●]`).
- Chinese NDAs (all placements): `信宸资本股权投资管理有限公司`.

**Address**:
- Chinese NDAs: `香港中环添美道1号中信大厦28楼`
- English NDAs: `28/F CITIC Tower, 1 Tim Mei Ave, Central, Hong Kong`. If the original placeholder spans TWO paragraphs (e.g., street on one line, city on the next), split the address across those two paragraphs to preserve layout — do NOT collapse onto one line. P2 precedent: `28/F CITIC Tower, 1 Tim Mei Ave ` on line 1 and `Central, Hong Kong` on line 2.

**Contact name** (`[联络人姓名]` / `[●]` in letter header): Fill in the TS Capital deal contact for this project. Ask the user if unknown. Never default to Henry Zeng — the contact and the signatory both vary per deal.

**Signature block — fill the ENTITY only; leave the person blank**:
- Entity: replace "Interested Party" / "Bidder" / "乙方" / "[insert full company name of receiving entity]" with `TS Capital Partners Management Limited`; Chinese twin `[插入接收实体全称]` → `信宸资本股权投资管理有限公司`. Delete any commercial register clause.
- `Name:` / `姓名:` / `Title:` / `职务：` — ALWAYS LEAVE BLANK. Never put a specific person's name in the signature block, in any case — the signatory is decided at signing, not at markup.
- Date blanks in the signature area — leave blank (filled at signing).

COMMENT: "Filling in the correct TS Capital entity and contact details. Only this specific fund entity should be named — not a broader CITIC entity or an affiliate."

### S2 — NDA Term: Push to Target (ladder driven by the ORIGINAL term)

**English NDAs**: if the original term is **2 years or less**, push to 1 year. If the original term is **3 years or longer**, push to 2 years via minimal word swap — see the Judgment rule below. If the term is **INDEFINITE** (no fixed outside date — e.g. obligations continue "until the information becomes public" or "until the discloser gives notice"), treat it like a ≤2yr original: structural rewrite to the 1-year dual-trigger, folding any useful existing limb (such as a public-availability trigger) into the new formula as an extra limb (P21 precedent, verbatim in the Tracked-File Index). Never leave the term above 2 years (or indefinite) unflagged.

Simple number replacement (P7 precedent, 2yr original → 1yr):
ORIGINAL_TEXT example: `the second (2nd) anniversary`
REPLACEMENT_TEXT example: `the first (1st) anniversary`

**Preferred formula — dual-trigger (P5 precedent, VERBATIM)**: If the existing term clause is a standalone sentence, DELETE the whole sentence and INSERT the P5 dual-trigger formula. The human's actual edits in P5 were:

```
ORIGINAL_TEXT (delete in full): "This Agreement and the obligations thereunder will continue for a period of two (2) years from the date hereof."
REPLACEMENT_TEXT (insert in full): "This agreement expire and cease to have any force or effect on the earlier of (i) the first anniversary of the date hereof and (ii) the date of consummation of the transaction between the parties."
```

Note the P5 verbatim quirks: lowercase "agreement"/"transaction", "expire" not "shall expire". Preserve them — this is what shipped in the human markup, and copying the human's exact phrasing reduces the risk that downstream review treats it as a substantive variation.

If the term clause is mid-sentence (e.g., "...for a period of 5 years."), prefer the simple number replacement (P7 style above) — don't try to rewrite the surrounding sentence.

The dual-trigger is better than a bare 1-year term because it also terminates the NDA automatically on deal close, so TS Capital is not bound by confidentiality obligations after it has invested.

**Chinese NDAs**: If the NDA term is more than 2 years, change to 2 years using the P9 formula. See Chinese NDA section for exact replacement text.

**Judgment rule — ladder driven by the ORIGINAL term (verified against every human markup)**:
- Original **≤2 years** → push to **1 year** (P5 2→1, P1 2→1, P7 2→1). Use the P5 dual-trigger only here, and only when the term clause is a standalone sentence.
- Original **3 years or longer** → push to **2 years** via minimal word swap (P4 3→2: DEL `three`/`3`, INS `two`/`2`; P6 3→2; **P8 10→2**: DEL `ten`/`10`, INS `two`/`2`). Do NOT push to 1 year in one round, and do NOT replace the sentence with the dual-trigger formula — the human used a simple number swap even on P8's 10-year original. P2 5→1 is a documented outlier, not the default.

COMMENT: "Standard position is 1-year NDA term (English, 2yr-or-less originals) / 2-year (Chinese, and English NDAs whose original term was 3 years or longer). Willing to accept up to 2 years if counterparty pushes."

### S3 — Non-Solicit: Same Ladder as the Term + Add Unsolicited Approach Carve-Out

The non-solicit period follows the SAME original-term ladder as S2 (verified against every human markup):
- English, original ≤2 years, clock runs from signing → push to **1 year** (P1 2→1, P7 2→1).
- English, original 3 years or longer → push to **2 years** via minimal word swap on FIRST markup (P4 3→2: DEL `three`, DEL `3`, INS `two`, INS `2`) — not 1 year.
- English, clock runs from the return/destruction request instead of signing → KEEP the period unchanged (P6 kept 2yr; effective duration is shorter than it reads).
- **English, clause already NARROWLY SCOPED with real carve-outs → KEEP the whole clause unchanged, including the period, and do NOT add the unsolicited carve-out (P21: 2yr from signing kept as-is because the restriction covered only employees "connected with the Proposed Transaction" and already carved out general recruitment ads and employees departed 6+ months).** Check narrowness BEFORE reaching for the ladder.
- Chinese → do NOT change a 2-year period or its scope — the P9 CN human markup kept `两年` and `任何关联方` as-is.

In every case EXCEPT the narrow-scope keep-everything case above, add the unsolicited approach carve-out (P6 added it even while keeping the period unchanged):
- English: `or (c) such person proactively contacts TS Capital without any solicitation by TS Capital`
- Chinese: `或(c) 该等人员主动接洽（未经贵方邀请）`

**Negotiation fallbacks if the pushed period is refused**: 18 months → 24 months (P10 precedent maxed at 24 months).

COMMENT: "Standard position on non-solicitation is 1 year (2 years when the original period was 3 years or longer). Also adding carve-out for unsolicited approaches — employees who contact TS Capital on their own initiative should not be restricted. Fallback: up to 24 months."

### S4 — Permitted Disclosure: Broaden the Trigger

If the permitted disclosure trigger is "mandatory law, regulation, court order or applicable stock exchange rules" (or a similarly narrow formulation), broaden it.

ORIGINAL_TEXT example: `mandatory law, regulation, court order or applicable stock exchange rules`
REPLACEMENT_TEXT example: `any law, regulation or legal, regulatory or judicial process`

COMMENT: "The narrow 'mandatory law' formulation prevents TS Capital from making disclosures required in the ordinary course (regulatory filings, internal compliance processes). Broadening to 'any law, regulation or legal, regulatory or judicial process' is the standard investor-side position."

**Also flag — reduce required cooperation**: If the NDA requires TS Capital to "pursue all available legal remedies" or "exhaust all available means" to resist a legally compelled disclosure, change to "take reasonable legal steps to limit the scope of disclosure."

ORIGINAL_TEXT example: `pursue all available legal remedies against official or court orders`
REPLACEMENT_TEXT example: `take reasonable legal steps to limit the scope of disclosure`

COMMENT: "An obligation to 'pursue all available legal remedies' is open-ended and could require costly litigation even where resistance is futile. 'Reasonable legal steps' is the market-standard formulation — it maintains a good-faith cooperation obligation without mandating full-scale legal proceedings. Accepted in a prior German-law project precedent."

### S5 — Return/Destruction: Add Reasonably Practicable Qualifier

Add "to the extent reasonably practicable" to the return/destruction obligation so that it covers the full obligation — not just the electronic purge sub-clause.

**Placement is flexible** — use whichever position fits the sentence:
- Mid-clause in the preamble (P7 precedent): `the Interested Party shall promptly, to the extent reasonably practicable, upon written request of Seller`
- As a trailing qualifier to the main obligation (P4 precedent): `we agree to destroy all Confidential Information in our possession or to which we have access to the extent reasonably practicable`
- At the end of the whole sentence (P2 precedent): `refrain from further use to the extent reasonably practicable and technologically feasible`

"And technologically feasible" is also acceptable (P2).

The key requirement: the qualifier must cover the **full** obligation, not just an electronic purge sub-clause buried at the end.

COMMENT: "An unqualified obligation to return or destroy ALL Confidential Information is impossible to comply with — automated backups, email archives, and system snapshots cannot be individually purged. A prior German-law project precedent accepted 'reasonably practicable and technologically feasible'."

### S6 — Change Written Consent → Timely Notice for Permitted Disclosures

If any permitted disclosure condition (other than disclosing to financing sources) requires "prior written consent" / `书面同意` from the counterparty, change to "timely notice" / `及时通知`.

Example: disclosure conditions `(i) business need, (ii) 书面同意, (iii) legal requirement` → change (ii) to `及时通知`

COMMENT: "Requiring prior written consent before any permitted disclosure creates an approval bottleneck that is operationally unworkable. Timely notification is sufficient — TS Capital should not need counterparty approval before sharing information with its own advisors and representatives."

### S7 — DELETE MNPI / Insider Trading Restriction Clauses

If the NDA contains any clause restricting TS Capital's securities trading activity based on receipt of information — including US securities law acknowledgments, insider trading undertakings, price-sensitive information lockups, or MNPI-based trading prohibitions — DELETE the entire clause in full, including any dedicated section heading.

ORIGINAL_TEXT example (P1): `"You hereby acknowledge that you are aware, and that you will advise your Representatives who are informed as to the matters which are the subject of this agreement, that the United States securities laws prohibit any person who has received from an issuer material, non-public information concerning the matters which are the subject of this agreement from purchasing or selling securities of such issuer"`
REPLACEMENT_TEXT: `""`

ORIGINAL_TEXT example (P2 — section heading): `"Insider Information"`
REPLACEMENT_TEXT: `""`

ORIGINAL_TEXT example (P2 — clause body): `"The Interested Party acknowledges that some or all of the Information may constitute, or be deemed to constitute, price-sensitive information, the use of which may be subject to regulation or prohibition under applicable insider trading laws. The Interested Party undertakes not to use the Information for any unlawful purpose."`
REPLACEMENT_TEXT: `""`

COMMENT: "TS Capital has its own internal compliance procedures for managing MNPI. An NDA-level trading restriction creates duplicative and potentially conflicting obligations — in particular, a blanket 'acknowledge-and-advise' clause on US securities laws is inappropriate where TS Capital is not a US entity and the transaction is not US-listed. Deleted in full on multiple precedent deals."

**Fallback** (P21 human comment): an insider-trading undertaking is acceptable only where the target/counterparty is a LISTED company. Include this fallback in the margin comment ("We only accept it for listed company") when the deal involves private targets.

---

## Must-Fix Issues to Scan

Only flag an issue if the NDA actually contains the problematic language. Scan every category below, output only the ones triggered. Each flagged issue must have a COMMENT explaining the WHY.

| # | Category | Flag if NDA contains... |
|---|----------|------------------------|
| 1 | Blank Date | Date field is unfilled — handled by S1, but flag separately if date is blank and a specific date is expected |
| 2 | Signatory Entity | Company name anywhere in the NDA is "CITIC" or any entity other than "TS Capital Partners Management Limited" / "信宸资本股权投资管理有限公司". Do NOT flag pre-filled individual signatory names or titles. |
| 3 | Portfolio Companies / Affiliates in Affiliate or Reps Definition | (a) "Affiliate" definition explicitly includes portfolio companies of TS Capital's funds — DELETE portfolio companies from the definition entirely (co-managed funds may stay). (b) Representatives definition extends to "a Party's Affiliates" (broad "common control" definition then captures portfolio companies indirectly) — preferred fix is Approach A (P10-style Notwithstanding carve-out with equityholders exclusion, P8 precedent); fallback Approach B (P5-style hard delete of the "or such Party's Affiliates" qualifier). See Gallery Example 13. |
| 4 | Standard Exceptions | Missing any of the 4 carve-outs from "Confidential Information": (i) public info, (ii) prior possession, (iii) received from 3rd party without restriction, (iv) independently developed. Fix: reformat the carve-out block and add the missing items — see Gallery Example 11 for verbatim language. |
| 5 | Representatives Definition | Excludes financing sources (debt/equity), or narrower than: directors, officers, employees, advisors (attorneys, accountants, consultants, bankers, financial advisors), financing sources |
| 6 | Representatives Carve-Out | Flag ONLY in German/European seller-form NDAs with an express "shall be responsible for any failure by any of its Authorized Recipients" sentence — replace that sentence with the P7 verbatim undertaking carve-out (see Key Precedent Facts → Representatives Carve-Out). Do NOT flag in US/HK company-form NDAs (P8, P5 kept the responsibility sentence) or CN letter NDAs (P9 kept 连带责任) — in company-form NDAs the exposure is handled via the Reps-definition carve-out (Cat 3/Example 13) instead. |
| 7 | Mutual Non-Publicity | **Do NOT flag on initial markup.** No tracked human markup ever made a one-sided non-publicity / non-disclosure-of-discussions clause mutual — the P8 human left "the Recipient shall not, nor permit any of its Representatives to, disclose to any person…" fully one-sided. Remedy mutuality (Cat 22) has precedent; publicity mutuality does not. Flag only if the clause goes beyond secrecy of discussions (e.g., an embedded no-shop or exclusivity obligation). |
| 9 | Notice/Consent — Financing | **Two patterns, opposite treatments** (see Key Precedent Facts → Financing Source Consent). Pattern A — standalone "Financing Institutions / Insurance Institutions" restriction section in a company/seller-form bilateral NDA: DELETE the entire section (P7 human markup deleted all 7 paragraphs; Gallery Example 3). Pattern B — Finance Provider / W&I Provider architecture in a banker-run process letter (P6, P5, P14, P15): do NOT flag, keep unchanged. Classify the NDA form first. |
| 10 | Notice/Consent — Misuse (cost-shifting) | NDA includes language requiring TS Capital to bear the counterparty's costs of investigating misuse / misappropriation (e.g., "贵方承担" / "at your cost or expense"). Fix: DELETE ONLY the cost-shifting language — do NOT delete the underlying notification obligation. |
| 11 | Notice/Consent — Ceasing Interest | NDA requires TS Capital to notify the target when it decides not to proceed. Fix: DELETE the entire ceasing-interest notification sentence. Also delete any associated hard time limit (e.g., "于24小时内" / "within 24 hours"). Initial markup position is to delete the obligation entirely. Fallback if counterparty pushes: accept the notification but delete the hard time limit. |
| 12 | Copies | Restriction on making copies applies to copies shared with Representatives |
| 13 | Permitted Disclosure | (a) Trigger is "mandatory law" or similarly narrow — should be "any law, regulation or legal, regulatory or judicial process" (see S4). (b) The notification obligation to the disclosing party does not contain the EXACT phrase "to the extent legally permissible and reasonably practicable". **Equivalent-sounding qualifiers such as "to the extent not prohibited by law" or "to the extent permitted by law" are NOT acceptable substitutes** — they cover legal prohibition (e.g., a gag order) but not practical impossibility (lawyer review needed, time to react). Replace any narrower formulation with the exact market-standard phrase, even when a similar qualifier is already present. P8 precedent. Also remove "immediately" if present (see Gallery Example 12). **Scope limit: this applies to the compelled-disclosure notice clause only — do not hunt down similar qualifiers in other clauses (P21 human left a "to the extent legally permissible" inside the secrecy-of-discussions parenthetical untouched and fixed only the unqualified compelled-disclosure notice).** |
| 14 | Return/Destruction | Treatment depends on the NDA form (both precedent NDAs had backup-files carve-outs — form is the discriminator, not the carve-out). **Company-form bilateral (Form A — P8)**: the human's ONLY edit was inserting `to the extent reasonably practicable, ` immediately before "destroy" — the 10-day deadline was KEPT, both certification obligations were KEPT. Mirror that: one qualifier insert, nothing else. **Process letter (Form C — P6)**: (a) replace the return deadline with the qualifier (`in such event you will, to the extent reasonably practicable, promptly return to us`); (b) delete only the time-window from the certification clause, keep the certification itself. **Chinese (Form D — P9)**: delete the 证明书 sentence in full; KEEP the 5-working-day window unqualified. **Seller letter-form incl. bilingual (P21)**: insert the reasonably-practicable qualifier AND delete the destruction-certification sentence in full (EN + CN twins); do NOT add ` written` to "upon your request" (P21 kept it bare — the P2 ` written` insert is a German-seller-letter pattern, not universal). Invariants across all forms: always ensure a reasonably-practicable qualifier covers the destruction obligation; certification treatment is form-driven — KEPT in US/HK company-form (P8), time-window-only softened in process letters (P6), DELETED in full in seller letter-forms and Chinese NDAs (P21, P9). |
| 15 | Non-Solicit Term | (English) Ladder by ORIGINAL period, same as the term: ≤2yr original with clock from signing → push to 1yr; ≥3yr original → push to 2yr (P4 first markup). **If the clock starts at return/destruction request** (e.g., "ending 2 years after the request for return/destruction"), the effective duration is shorter than it reads — 2yr is accepted without reduction (P6 precedent); only add the unsolicited carve-out. **If the clause is already narrowly scoped with real carve-outs (only transaction-connected employees + general-ads and departed-employee carve-outs), KEEP it entirely — no period change, no added carve-out (P21).** (Chinese) A 2-year period is accepted without change — P9 CN human kept 两年. Otherwise check: is the unsolicited approach carve-out present? If not, add it (see S3). |
| 16 | Non-Solicit Scope | (English) Non-solicit binds ALL affiliates/funds regardless of whether they received CI (binding affiliates who actually received CI is accepted — P10 precedent). Flag if applies to all affiliates without CI-receipt limitation. (Chinese) Do NOT flag — the P9 CN human markup left `贵方或贵方的任何关联方` unchanged; scope narrowing has no CN precedent. |
| 17 | Term | NDA term exceeds 1 year (English) / 2 years (Chinese), or is indefinite. English ladder by ORIGINAL term: ≤2yr original → push to 1yr; ≥3yr original → push to 2yr via minimal word swap (P4/P6 3→2, P8 10→2); INDEFINITE (no outside date) → 1yr dual-trigger structural rewrite, folding any useful existing limb into the new formula (P21). Chinese: 2 years using the "earlier of 2 years or deal completion" formula. Max accepted (English): 2 years; 3 years only as a last concession. |
| 18 | Third Party Beneficiaries | NDA grants rights to third parties beyond the standard sell-side process agent role, or context is not a formal sell-side process. Third-party beneficiary accepted in German NDAs (P10, P11, P2) and Korean (P5) — flag but note as common in banker-run processes. |
| 19 | Governing Law | US deal with governing law other than NY or DE (never agree to IL); or governing law does not match the target's home jurisdiction |
| 20 | Indemnification | NDA requires TS Capital to indemnify for: any consequential/indirect damages, prosecution or enforcement costs, "消除影响" costs, or any losses without a final court judgment prerequisite. Fix: DELETE the full indemnification clause. REPLACE with mutual fee-shifting formula conditioned on final court judgment (see Indemnification section in Key Precedent Facts for exact language). Do NOT use a one-sided replacement — the replacement must be mutual (both parties can invoke it). |
| 21 | Standstill | Any standstill provision present on initial review; or standstill binds affiliates/Representatives; or includes prohibition on requesting waiver |
| 22 | Remedy Asymmetry | Remedy or injunctive relief provisions apply only against TS Capital, not mutually. Fix: ADD a reciprocal clause ("These provisions shall apply mutatis mutandis to both Parties, and the same remedies shall be available to the Receiving Party...") — do NOT delete the original provision. For arbitration clauses: add "The arbitration proceeding and remedies shall be equally enforceable by both Parties without unilateral procedural disadvantage." See Gallery Example 10. |
| 23 | Records Obligation | NDA requires TS Capital to maintain logs of who received CI and report them on request. Do NOT delete this clause — instead, EXPAND the list of institution types (add financial advisors, consultants, financing sources) so those recipients fall under the "name + team leader only" bucket. |
| 24 | MNPI / Securities Trading Restrictions | Provisions restrict TS Capital from trading beyond standard insider trading compliance (e.g., US securities law acknowledgments, insider trading undertakings, MNPI-based lockups). Fix: DELETE the entire provision in full, including any dedicated section heading (see S7). Deleted in P1 and P2 precedents. |

---

## What NOT to Flag (Negative Space)

These patterns commonly look problematic at first read but were **NOT changed** in any of the tracked human markups. Do not flag them on initial markup. If you find yourself wanting to flag something on this list, stop and reread the relevant tracked file before doing so.

**Process / banker-driven structure (typically kept):**
- Third-party beneficiary clauses naming the M&A advisor (e.g., "[M&A advisor]" in P5). Standard banker-run process structure.
- Single-point-of-contact requirement ("direct all requests for information to [Bank]") — kept in P5.
- Prior consent for contacting Company employees/customers/suppliers during the process — kept in P5.
- **Finance Provider / W&I Provider restrictions in BANKER-RUN PROCESS LETTERS** — kept without challenge in every process-letter tracked file (P14, P15, P16, P6). These are process structure requirements in formal sell-side processes. Do NOT flag, do NOT delete. Only carve-out: when the exclusion of Finance Providers from the Authorized Person definition is paired with a written consent mechanism, note it as a fallback concession point (P11 signed = accepted prior written consent), but do not mark it as a must-fix. **This kept-pattern applies ONLY to process letters — a standalone "Financing Institutions and Insurance Institutions" restriction section in a company/seller-form bilateral NDA is DELETED in full (P7 human markup; Cat 9 Pattern A / Gallery Example 3).**

**Equitable relief / one-sided remedy preamble (do NOT delete):**
- The full equitable relief preamble (specific performance, injunctive relief, "money damages inadequate", waiver of bond) — kept in P1. The fix for asymmetry is to ADD a mutual reciprocity clause at the end (see Gallery Example 10), not to delete the existing language.

**Compelled disclosure clause specifics (only change what Example 12 changes):**
- "All best efforts to preserve confidentiality of the remainder of the Evaluation Material" — kept in P1.
- "Outside legal counsel" trigger formulation (when broad enough on its face) — kept in P1.
- Only the notification obligation needs the "to extent legally permissible" qualifier — do not rewrite the rest of the compelled disclosure clause.

**Confidentiality scope (when reasonably complete):**
- Pre-existing CI exceptions (i)(ii)(iii) — kept in P5; only added the missing (iv).
- "We will be responsible for any breach by our Representatives" without an Annex A undertaking carve-out — kept in P5 AND P8 (US/HK company-form) and in P9 CN (连带责任 kept). The undertaking carve-out is a German/European seller-form fix only (P7) — see Cat 6.

**One-sided secrecy-of-discussions / non-publicity clauses:**
- "The Recipient shall not disclose the existence or status of discussions" style clauses binding only TS Capital — kept one-sided in P8. Never made mutual in any tracked markup. Do not flag (Cat 7).

**Return/destruction specifics in company-form NDAs (P8, Form A):**
- The hard deadline ("within ten (10) days after such written request") — KEPT.
- Both written destruction-certification obligations — KEPT.
- The only edit: insert `to the extent reasonably practicable, ` before "destroy".
- (Process letters — Form C/P6 — soften the return deadline instead; see Cat 14.)

**Chinese NDA items verified KEPT in the P9 CN human markup:**
- 5-working-day return window (`应在5个工作日内`) — kept unqualified; do NOT add 合理可行 to it.
- Non-solicit 2-year period (`两年`) and `任何关联方` scope — kept; only carve-out (c) added.
- 连带责任 sentence for representative breaches — kept.
- 律师意见 vs 律师建议 terminology — not changed (minor counsel terminology, Revision Principle 1).
- Waiver-of-claims / non-reliance clauses (贵方不可撤销地承诺…避免…提出任何要求 / 本公司不对评估资料准确性负责) — kept; do NOT delete.
- The (包括但不限于调查费、鉴证费、律师费、公证费、差旅费等) cost enumeration inside the indemnity — kept, except the 消除影响 item which is deleted separately.

**Governing law (matching deal jurisdiction):**
- DIS Stuttgart arbitration for German deals — kept in P2.
- PRC arbitration for Chinese deals — accepted across all signed Chinese precedents.
- [M&A advisor]-style banker process governance — kept.

**Counterparty placeholders (never fill):**
- `[Seller entity]`, `[Seller address]`, `[Seller]`, `[Company]`, `[Target]`, addressee letterhead blocks, and execution-date blanks — these belong to the other side or to signing time. The P21 human left all of them untouched; a machine run that filled the Seller letterhead with TS's details was corrected. See S1 Steps 1–2.

**Narrow non-solicit clauses (kept in full):**
- A 2-year non-solicit limited to employees "connected with the Proposed Transaction", with carve-outs for general recruitment ads and employees departed 6+ months — kept entirely unchanged in P21 (no period reduction, no unsolicited carve-out added).

**Non-solicit pre-existing carve-outs (typically kept):**
- Advisor carve-out (`"excluding Representatives who are debt financing sources, attorneys, accountants, consultants, agents and financial advisors so long as such Representatives are not acting on our behalf with respect to employee solicitation or hiring"`) — kept in P5; only change the period.
- "Employees" defined as those with actual contact / who become known in connection with the transaction — kept in P5 (already narrow enough).
- Generalized media advertisement carve-out — kept in P1.

**Indemnification (when adding qualifier is enough):**
- The "including attorney's fees and court costs" enumeration — kept in P4. Only ADD the "provided that... direct losses only... final non-appealable order... mutual fee-shifting" qualifier (see Gallery Example 8); do not delete the surrounding language.

**General negative rule**: If a clause type does NOT appear in any tracked-files redline, it is almost certainly not material. Search the tracked extraction first; do not flag based on guideline-derived intuition alone.

---

## Output Format

### Part 0 — Mandatory Coverage Checklist (must complete before anything else)

Before writing Part 1, go through every Standard Change (S1–S7) and every Must-Fix Category (1–24) exactly once. Mark each YES (triggered, fix needed) or NO (not present in this NDA). Skipping a row is not allowed — every row must have YES or NO with a one-line note.

**Rules:**
- Every YES MUST appear as a redline block in Part 2. No YES without a matching block.
- Every NO is final — do not raise that item later. If you discover a NO was actually a YES while writing Part 2, restart Part 0 from scratch.
- Use the Negative Space section above to calibrate before marking YES on borderline items.

```
COVERAGE CHECKLIST

NDA form (Step 0): A / B / C / D — one-line justification

Standard Changes:
| # | Standard Change | Y/N | Location / Note |
|---|-----------------|-----|-----------------|
| S1 | Fill blanks (date, entity, address, contact) | Y/N | header / preamble / signature |
| S2 | NDA term ladder (≤2yr orig → 1yr; ≥3yr orig → 2yr; CN → 2yr formula) | Y/N | §X — current term |
| S3 | Non-solicit (EN 1yr if from-signing; CN keep 2yr) + unsolicited carve-out | Y/N | §X |
| S4 | Permitted disclosure trigger / cooperation scope | Y/N | §X |
| S5 | Return/destruction "reasonably practicable" | Y/N | §X |
| S6 | Written consent → timely notice | Y/N | §X |
| S7 | MNPI / insider trading restriction deletion | Y/N | §X |

Must-Fix Categories:
| # | Category | Y/N | Location / Note |
|---|----------|-----|-----------------|
| 1 | Blank Date | Y/N | - |
| 2 | Signatory Entity (CITIC vs TS Capital) | Y/N | - |
| 3 | Portfolio Companies in Affiliate Definition | Y/N | - |
| 4 | Missing CI Standard Exceptions | Y/N | - |
| 5 | Representatives Definition too narrow | Y/N | - |
| 6 | Representatives Carve-Out (Annex A undertaking) | Y/N | - |
| 7 | Mutual Non-Publicity | Y/N | - |
| 9 | Notice/Consent — Financing | Y/N | - |
| 10 | Notice/Consent — Misuse cost-shifting | Y/N | - |
| 11 | Notice/Consent — Ceasing Interest | Y/N | - |
| 12 | Copies | Y/N | - |
| 13 | Permitted Disclosure (a)/(b) | Y/N | - |
| 14 | Return/Destruction certification or auto-trigger | Y/N | - |
| 15 | Non-Solicit Term exceeds 1yr | Y/N | - |
| 16 | Non-Solicit Scope (all affiliates) | Y/N | - |
| 17 | Term exceeds target | Y/N | - |
| 18 | Third Party Beneficiaries | Y/N | - |
| 19 | Governing Law (US: NY/DE only) | Y/N | - |
| 20 | Indemnification (full / without court order) | Y/N | - |
| 21 | Standstill | Y/N | - |
| 22 | Remedy Asymmetry | Y/N | - |
| 23 | Records Obligation | Y/N | - |
| 24 | MNPI / Securities Trading Restrictions | Y/N | - |
```

After completing the checklist, count: the number of YES rows MUST equal the number of redline blocks in Part 2. If they don't match, restart.

### Part 1 — Summary Table

Show all standard changes (S1–S7) that apply AND all must-fix issues found.

```
STANDARD CHANGES + MUST-FIX ISSUES

| # | Type | Issue | Location | Summary |
|---|------|-------|----------|---------|
| S1 | Standard | Entity/date fill-in | Header, Preamble, Signature | Fill in TS Capital details |
| S2 | Standard | Term reduction | §16 | 10 years → 2 years (P9 formula) |
| S3 | Standard | Non-solicit reduction | §12 | 2 years → 1 year + unsolicited approach carve-out |
| S7 | Standard | MNPI clause deletion | §11 | Delete insider trading restriction in full |
| 3 | Must-Fix | Portfolio Companies | §1.2 | Portfolio companies in Affiliate definition |
| 6 | Must-Fix | Rep Carve-Out | §3.3 | No undertaking mechanism |
| 9 | Must-Fix | Financing Section | §8 | Delete entire §8 |
```

Number every row in Part 1 must match a YES row in Part 0 and a redline block in Part 2.

### Part 2 — Redline Block Per Change

For each item in the summary table, output one block. ORIGINAL_TEXT and REPLACEMENT_TEXT must be exact verbatim strings — copy from document text, not from memory. Watch for half-width `()` vs full-width `（）` parentheses, and curly `"` vs straight `"` quotes.

```
══════════════════════════════════════════════
ISSUE #1 — Portfolio Companies in Affiliate Definition [§1.2]
══════════════════════════════════════════════

ORIGINAL CLAUSE:
  "...including, in the case of an Interested Party which manages or advises private
  equity or similar funds, (i) each of such funds...(herein 'Funds'), and (ii) the
  portfolio companies of each of such Funds..."

ORIGINAL_TEXT: "and (ii) the portfolio companies of each of such Funds (and in each case their respective affiliates...), to the extent such portfolio companies have actually received Confidential Information"
REPLACEMENT_TEXT: ""

REVISION:
  Delete limb (ii) (portfolio companies) from the Affiliate definition entirely.

COMMENT:
  Portfolio companies of TS Capital's funds are separate businesses with no role in
  evaluating this transaction. TS Capital has no control over their day-to-day operations.
  Co-managed funds (limb (i)) remain — those are legitimately part of the fund family.
══════════════════════════════════════════════
```

### Part 3 — Generate Redlined Word Document

After completing Parts 1 and 2, generate the tracked-changes .docx output.

**This step requires the NDA as a .docx file.** For PDFs, export to .docx first.

#### Step A — Build changes.json

Collect all ORIGINAL_TEXT / REPLACEMENT_TEXT pairs from every redline block into a JSON array. Before finalizing each entry, extract the actual paragraph text from the document XML and confirm the `original` string appears verbatim.

```json
[
  {
    "original": "the second (2nd) anniversary",
    "replacement": "the first (1st) anniversary",
    "comment": "Standard position is 1-year NDA term. Willing to accept up to 2 years if counterparty pushes."
  }
]
```

The `comment` field will be embedded as a Word margin comment in the output document.

#### Step B — Run the helper script

```
python apply_redlines.py "input.docx" "input_TS_markup.docx" "changes.json"
```

Name the output: `[original filename]_TS_markup.docx`, saved in the same folder as the NDA.

The output .docx opens in Word with all changes as tracked revisions (author: "TS Capital Partners Management Limited") and margin comments explaining each change.

#### Troubleshooting

- **Text not found warning**: The `original` string must match document text exactly. Re-read the paragraph and copy verbatim — watch for half-width `()` vs full-width `（）` parentheses, and curly `"` vs straight `"` quotes. Extract the text with Python from the document XML rather than typing from memory.
- **Python not installed**: `winget install Python.Python.3.12`

### Part 4 — Final Review (mandatory before delivering output)

After completing Parts 0–3, read through the entire set of changes one final time and verify:

1. **Count consistency** — count the YES rows in Part 0, the rows in Part 1, and the redline blocks in Part 2. All three counts MUST be equal. If any mismatch: stop, identify what was missed or double-counted, and fix.
2. **Material only** — is every change driven by a real business issue? Cross-check against Negative Space — if any change matches a "do not flag" pattern there, remove it.
3. **Nothing missed** — scan the full document one more time for unfilled placeholders (`[●]`, `[日期]`, `[地址]`, `[联络人]`) and confirm Part 0 caught every triggered category. Counterparty placeholders (`[Seller entity]`, `[Seller]`, addressee blocks) and unset execution dates are SUPPOSED to remain unfilled — verify none of them received TS Capital's details by mistake.
4. **Replacement text quality** — read each REPLACEMENT_TEXT aloud (mentally). Is it grammatically correct? Does it flow naturally in context? Fix any typos or awkward phrasing.
5. **Comments are clear** — each COMMENT should state the business reason in plain language. Remove any comment that just describes the change without explaining why.
6. **Coherence** — does the full set of changes tell a consistent story? Are there any contradictions between changes?
7. **Final in-context read-through (mandatory)** — open the generated `_TS_markup.docx` (or simulate by extracting the modified paragraph XML) and read every clause that contains a tracked change in its full sentence/paragraph context. For each clause, verify:
   - **Grammatical flow** — sentence reads cleanly after all inserts/deletes are accepted; no double spaces, no orphaned punctuation, no broken capitalization, no duplicated words ("limit ... limit"), no awkward fragments.
   - **Surgical scope** — each tracked change covers the MINIMUM text needed. If a single ORIGINAL_TEXT/REPLACEMENT_TEXT replaces an entire sentence where the human would have made 2–3 small inserts/deletes, split it into smaller surgical edits. Compare against `tracked/` examples for the same change type to calibrate scope.
   - **Format consistency** — paragraph numbering, indentation, list bullets, heading styles, and font/case usage remain consistent with the surrounding document. The redlined section should look like the rest of the document, not like a fresh paste-over.
   - **Word-boundary correctness** — inserted text begins/ends at word boundaries (no mid-word splits, correct leading/trailing spaces).
   - **Multi-paragraph fills** — when filling a header/address that originally spans multiple paragraphs (e.g., name on one line, address on the next), preserve that paragraph break instead of collapsing onto one line.
8. **End review — font and font-size consistency (mandatory last step)** — go through every tracked change one more time and confirm the font family and font size of ALL inserted text match the pre-change document exactly. No inconsistencies allowed: an inserted run must carry the same `w:rFonts` (incl. `eastAsia` for Chinese text) and `w:sz` as the surrounding original runs in that paragraph. Check programmatically: extract the `w:rPr` of every run inside a `w:ins` and compare against the neighbouring original runs; any mismatch (or an inserted run with NO `rPr` where neighbours have one) must be fixed and the .docx regenerated before delivery.

If any item fails, fix the change set and regenerate the .docx before delivering.

Only deliver the output after passing this review.

---

## Chinese NDA — Additional Checks

Apply all 24 categories plus the following Chinese-specific checks. Chinese letter-form NDAs typically have a header with `[日期]`, `[协议对方名称]`, `[地址]`, `[联络人姓名]` that all need to be filled in.

### Placeholder Scan (Chinese NDAs)
Before doing anything else: find and fill every placeholder:
- `[日期]` → execution date
- `[协议对方名称]` → `信宸资本股权投资管理有限公司` (every occurrence)
- `[地址]` → `香港中环添美道1号中信大厦28楼`
- `[联络人姓名]` → project contact at 信宸资本 (ask user if unknown)

### 保密期限 — Term Replacement Formula

All signed Chinese NDAs have 2-year terms. Initial markup should change any term exceeding 2 years to 2 years using the P9 formula:

**Delete**: `本协议函其余条款自本协议函签订之日起[X]年后逾期失效` (and the preceding "而前述条款在适用法律允许的最迟日期前一直具有约束力，")

**Insert**: `双方在本协议项下承担的保密义务和责任，自本协议签署之日起生效，并于以下较早日期终止并失效：(i) 本协议签署之日起满两周年之日（除非经双方协商一致解除本协议），或(ii) 双方完成交易之日。`

**Important**: Keep whatever clauses (`第5条`, `第13条`, `第20条`, etc.) are listed as permanent exceptions — do NOT remove them from the exceptions list just because §13 (indemnification) exists. Instead, rewrite §13 to be a reasonable obligation (see Indemnification below), then §13 can safely remain a permanent exception.

### 保密例外 — Permitted Disclosure Conditions

If condition (ii) for permitted disclosure requires `书面同意` (written consent), change to `及时通知` (timely notice):

**Delete**: `书面同意披露`
**Insert**: `及时通知`

COMMENT: "Prior written consent for each disclosure is operationally unworkable. Timely notification is sufficient — TS Capital should not need the counterparty's approval before sharing information with its own advisors."

### 泄露通知 — Misuse Notification Cost-Shifting

If the misuse/misappropriation assistance clause includes an obligation for TS Capital to bear the other party's costs:

**Delete ONLY**: `，有关费用由贵方承担` (the cost-shifting rider)
**Keep**: The underlying notification and assistance obligation

Do NOT delete the whole clause — the obligation to notify and assist is standard; it is only the "at your cost" rider that is unacceptable.

### 停止参与通知 — Ceasing Interest

If the NDA requires TS Capital to notify the target upon deciding not to proceed:

**Delete**: The entire sentence stating the obligation to notify (e.g., `则贵方应尽快(且在任何情况下于24小时内)通知本公司该决定。`)

Do NOT just delete the time limit — delete the entire notification obligation. If the counterparty pushes back, can accept the obligation but must delete any hard time limit.

### 销毁证明 — Certification of Destruction

If the NDA requires TS Capital to provide a signed written certificate confirming destruction:

**Delete**: The entire certification/证明书 obligation (e.g., `如果销毁或删除评估资料，贵方应向本公司提供由贵方正式授权代表签署的、确认已销毁或删除的证明书。`)

**Keep**: Any working-day return window (e.g., `应在5个工作日内`) — the P9 CN human markup kept the 5-working-day window unqualified. Do not add 合理可行 to it and do not delete it.

COMMENT: "Providing a signed destruction certificate is operationally difficult and creates legal exposure — a signed certificate confirming 'complete' destruction may itself be inaccurate due to system backups and email archives."

### 不招揽条款 — Non-Solicit Carve-Out

Do NOT change the non-solicit term or scope in Chinese NDAs: the P9 CN human markup kept `两年` and `任何关联方` unchanged. The ONLY change is adding the unsolicited approach carve-out:

**Add**: `或(c) 该等人员主动接洽（未经贵方邀请）` (the P9 human also deleted the `或` before (b) so the list reads (a)、(b)，或(c))

This is in addition to the standard passive job posting carve-out `(a)`.

### 赔偿条款 — Indemnification Replacement

If the NDA contains a full indemnification clause (any reference to `任何性质的全部损失`、`成本`、`权利主张`、`受偿人`、`消除影响费用` etc.):

**Delete**: The entire full indemnification clause

**Insert**: The P9 mutual fee-shifting formula:
`若发生与本协议相关的诉讼，经有管辖权的法院作出终局且不可上诉的判决，认定一方违反本协议，则败诉方应向胜诉方偿付其为行使本协议项下权利而产生的合理法律费用及开支`

**Also delete separately**: Any `消除影响费用` (reputation cleanup costs) language within any remaining parenthetical list.

This replacement is mutual — both parties can invoke it after a final judgment. Do NOT use a one-sided replacement.

### 关联人员 Definition
Must include IC members (投资决策委员会成员), LP investors (有限合伙人), external advisors (律师、会计师、顾问).

### 争议解决
Arbitration is standard and acceptable. Flag only clearly inappropriate venue.

### 单向义务
Flag if all obligations are one-sided against 信宸资本 with no reciprocal obligations from the disclosing party.

---

## Revision Principles

1. **Material issues only — not textual** — every change must fix a real business problem. Ask: what obligation or risk does this clause create for TS Capital? If the answer is "nothing material, just different wording," do not change it. Examples of what NOT to flag: minor counsel terminology, verb choice ("ensure" vs "direct"), notice format details. Examples of what TO flag: portfolio companies bound by the NDA, indefinite term, open-ended indemnification, obligation to notify if not investing.
2. **Calibrate against human markups** — before finalising any redline, check whether similar changes appear in `./knowledge/tracked/`. If not, reconsider whether the change is truly necessary.
3. **Be surgical — never over-delete** — only delete or replace the specific problematic language. If an obligation has a problematic rider (e.g., "at your cost"), delete only the rider, not the whole obligation. Read the full clause and identify precisely what is wrong before touching anything.
4. **Read every placeholder first — then ask whose blank it is** — before analyzing substantive clauses, scan the entire document for unfilled blanks (`[●]`, `[日期]`, `[地址]`, `[协议对方名称]`, `[联络人]`). Fill the ones that denote TS Capital's own party (per S1 Steps 1–2); leave counterparty blanks and unset execution dates untouched.
5. **Verify exact text from the document** — before writing ORIGINAL_TEXT, extract the actual paragraph text from the document XML to confirm character-level accuracy. Watch for half-width `()` vs full-width `（）`, and curly `"` vs ASCII `"` quotes.
6. **Always include WHY** — every change gets a comment explaining the business reason. The comment goes in the redline block AND as a margin comment in the Word document.
7. **Fallback positions** — include the fallback in the comment where one exists ("if they push back, the fallback is..."). Signed precedents show what was conceded — use them as fallbacks, not as reasons to skip the initial markup change.
8. **Standard changes are not optional** — S1–S7 are checked on every NDA (each per its own trigger and the Step 0 form ladders). Do not skip them because the template "seems fine."
9. **Don't remove clauses from exception lists — rewrite them** — if a clause needs to be limited (e.g., §13 indemnification), rewrite it to a reasonable scope. Keeping the rewritten clause as a permanent exception is correct. Do not remove §13 from the exceptions list just because the indemnification was problematic — fix the clause instead.
