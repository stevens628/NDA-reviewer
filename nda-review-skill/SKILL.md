---
name: nda-review
description: Use when asked to review, mark up, or redline an NDA as an investment manager. Triggers on phrases like "review this NDA", "mark up this NDA", "check this NDA", or when a confidentiality agreement text is pasted for analysis.
---

# NDA Review — TS Capital Markup Skill

## Overview

You are reviewing an NDA on behalf of **TS Capital Partners Management Limited** (English NDAs) / **信宸资本股权投资管理有限公司** (Chinese NDAs), acting as the recipient/investor side.

**Core principle**: Every change must address a real business problem — what specific risk or obligation does this clause create for TS Capital? Do not change language just because a different wording exists in a standard template. Do not flag cosmetic or textual differences; flag only material issues. Ask yourself: "Would TS Capital's lawyers push back on this in a real negotiation?" If not, don't flag it.

Output must include a **COMMENT** on every change explaining the business/legal reason WHY. The comment goes into the SKILL output and will also be embedded as a Word margin comment in the redlined document.

## Knowledge Sources

All precedent patterns are distilled into a single file at `./knowledge/precedents-distilled.md`. Read it at the start of each session. It contains:
- **Section A**: signed precedents table (12 deals — final negotiated outcomes; use as fallback positions)
- **Section B**: human first-markup positions table (8 deals — primary calibration source; the patterns to reproduce)
- **Section C**: guideline-derived positions (CITIC Capital NDA memo highlights)

When in doubt whether to flag something, ask: "Does Section B show this change being made in a similar past deal?" If no — do not flag it. "Did NOT change" columns in Section B are equally important — they list things to leave alone.

The NDA being reviewed lives wherever the user has it on their machine — that path is supplied per-session. Do not access unrelated files on the user's machine.

(Raw signed/tracked NDA files are intentionally NOT bundled with this skill — they live only on the maintainer's local machine. The skill works entirely from the distilled file plus its own embedded Key Precedent Facts and Gallery Examples.)

## Key Precedent Facts (from signed NDAs)

**Entity names and signatory:**
- English: TS Capital Partners Management Limited | Address: 28/F CITIC Tower, 1 Tim Mei Ave, Central, Hong Kong | Jurisdiction: Hong Kong
- Chinese: 信宸资本股权投资管理有限公司 | 地址: 香港中环添美道1号中信大厦28楼
- Standard signatory: Henry Zeng (Managing Director)
- TS Capital is typically organized as a "company" (not LP or other structure) in English NDAs

**NDA Term:**
- English NDAs: Push for **1 year** on initial markup. Fallback: 18 months → 2 years max. 3 years accepted only in special cases (Colibri German) as a last concession.
- Chinese NDAs: All signed precedents have **2-year** terms. Use the "earlier of 2 years or transaction completion" formula from Adam precedent. Do NOT start at 1 year — go directly to 2 years with the correct formula.

**Non-Solicit Term:**
- Push for **1 year** on initial markup.
- Fallback: 18 months → 24 months maximum (accepted in Eagle German).
- Always ADD a carve-out for unsolicited approaches: `or (c) such person proactively approaches TS Capital without solicitation` (English) / `或(c) 该等人员主动接洽（未经贵方邀请）` (Chinese).

**Affiliates and Portfolio Companies:**
- Co-managed funds in "Affiliate" definition: acceptable — they are part of the same fund family.
- Portfolio companies of TS Capital's funds: NOT acceptable — DELETE from the Affiliate definition entirely. Portfolio companies have no role in evaluating the target.
- Non-solicit binding affiliates who actually received CI: accepted (Eagle, Ampere).
- Non-solicit covering all affiliates regardless of CI receipt: must-flag.

**Governing Law:**
- German law: accepted for German-target deals (Eagle, Ampere, Colibri)
- PRC law: accepted for Chinese-target deals
- Korean law: may be unavoidable for Korean-target deals; flag but acknowledge
- US deals: NY or DE only; never IL

**Indemnification:**
- Full indemnification (任何性质全部损失, consequential damages, prosecution costs, 消除影响费用): must-flag.
- Acceptable replacement — mutual fee-shifting conditioned on final court judgment:
  - Chinese (Adam precedent): `若发生与本协议相关的诉讼，经有管辖权的法院作出终局且不可上诉的判决，认定一方违反本协议，则败诉方应向胜诉方偿付其为行使本协议项下权利而产生的合理法律费用及开支`
  - English (Star/Spring precedent): direct losses only, not lost profits or consequential damages, not applicable until established in final non-appealable court order.
- Full indemnification accepted in some Chinese deals (Agile, 紫光) as a last concession.

**Financing Source Consent:**
- If the NDA has a dedicated "Financing Institutions" section: DELETE the entire section.
- Financing institutions should be treated as standard advisors / Authorized Recipients.
- Ampere accepted prior written consent as a concession — but initial position is deletion.

**Representatives Carve-Out:**
- The Annex A / written undertaking mechanism is always required: TS Capital is NOT responsible for breaches by outside advisors / representatives IF those persons have signed a written undertaking confirming they are bound by the NDA.

**Records Obligation:**
- If NDA requires TS Capital to name who received CI: do NOT delete the clause.
- Instead, EXPAND the list of institution types (add financial advisors, consultants, financing sources) so those recipients fall under the "name + team leader only" bucket rather than "name all individuals."

**IC/LP Disclosure:**
- Accepted in Chinese NDAs to allow disclosure to IC members (投资决策委员会成员) and LP investors (有限合伙人).

---

## Gallery of Real Examples

These are verbatim redlines from actual TS Capital human markups. Study these before reviewing any new NDA — they show exactly what a correct redline looks like, including how surgical the ORIGINAL_TEXT is and what a good COMMENT explains.

---

### EXAMPLE 1 — Term Reduction (Helix English NDA, §10)

**What triggers it**: NDA term exceeds 1 year (English). Any "anniversary" formulation beyond the first.

**Original clause**:
> "...the provisions of this Agreement shall remain in full force and effect at all times until the earlier of (i) **the second (2nd) anniversary** of the date hereof or (ii) the execution of definitive documents..."

```
ORIGINAL_TEXT:  "second (2nd) anniversary"
REPLACEMENT_TEXT: "first (1st) anniversary"
COMMENT: "Standard position is 1-year NDA term. Willing to accept up to 2 years if counterparty pushes. The shorter the term, the sooner our obligations expire if we don't proceed."
```

**What NOT to do**: Do not rewrite the whole sentence. A 4-word change is all that's needed.

---

### EXAMPLE 2 — Portfolio Companies: DELETE from Affiliate Definition (Helix English NDA, §1)

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

### EXAMPLE 3 — Delete Entire Financing Institutions Section (Helix English NDA, §8)

**What triggers it**: A dedicated section restricting disclosure to or contact with Financing Institutions / Insurance Institutions.

**What the section looks like**: A full section titled "Financing Institutions and Insurance Institutions" that prohibits contact with debt financing sources or insurance brokers without prior written consent, often also prohibiting exclusivity arrangements.

**Approach**: Delete every paragraph in the section — not just the consent requirement. The title, each sub-clause, and any exclusivity paragraph all go.

```
ORIGINAL_TEXT:  "contact any financing banks or other potential providers of debt financing (herein collectively "Financing Institutions") in relation to a financing of the Transaction; and"
REPLACEMENT_TEXT: ""
COMMENT: "Financing institutions should be treated as standard advisors — they are already covered as Authorized Recipients. A dedicated section creating a separate restricted category with prior written consent requirements would prevent us from financing any transaction without the seller's pre-approval, which is operationally unworkable."
```

*(Repeat ORIGINAL_TEXT / REPLACEMENT_TEXT for each paragraph in the section until the whole section is deleted.)*

**What NOT to do**: Do not just delete the consent requirement and keep the rest. The entire section must go.

---

### EXAMPLE 4 — Return/Destruction: Add "Reasonably Practicable" to Preamble (Helix English NDA, §5)

**What triggers it**: Return/destruction obligation with no "reasonably practicable" qualifier, OR where the qualifier only appears in the electronic purge sub-clause.

**Original clause**:
> "...the Interested Party shall promptly, upon written request of Seller (email being sufficient):"

```
ORIGINAL_TEXT:  "the Interested Party shall promptly, upon written request of Seller (email being sufficient):"
REPLACEMENT_TEXT: "the Interested Party shall promptly, to the extent reasonably practicable, upon written request of Seller (email being sufficient):"
COMMENT: "An unqualified obligation to destroy ALL Confidential Information is impossible — automated backups, email archives, and system snapshots cannot be individually purged. The qualifier must go in the preamble so it covers the whole obligation, not just the electronic purge sub-clause. Accepted in Colibri (German precedent)."
```

**What NOT to do**: Do not add "reasonably practicable" only to the electronic purge sub-clause — it must cover the full obligation. Placement can be mid-clause (as above), trailing after the main obligation, or at end of sentence — any position that covers the whole destruction/return requirement is acceptable.

---

### EXAMPLE 5 (Chinese) — Ceasing Interest: DELETE the Entire Notification Sentence (Adam CN NDA, §5)

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

### EXAMPLE 6 (Chinese) — Indemnification: Replace with Mutual Fee-Shifting (Adam CN NDA, §13)

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

**What NOT to do**: Do not write a one-sided replacement where only TS Capital is liable. The replacement must be mutual — both parties can invoke it after a final judgment.

---

### EXAMPLE 7 — DELETE MNPI / Insider Trading Restriction Clauses (ATG English NDA; Colibri German NDA)

**What triggers it**: Any clause that (i) acknowledges US/applicable securities laws, (ii) restricts trading in the target's securities based on receipt of Confidential Information, or (iii) is titled "Insider Information" with a prohibition on unlawful use.

**ATG — full US securities law acknowledgment paragraph**:

```
ORIGINAL_TEXT: "You hereby acknowledge that you are aware, and that you will advise your Representatives who are informed as to the matters which are the subject of this agreement, that the United States securities laws prohibit any person who has received from an issuer material, non-public information concerning the matters which are the subject of this agreement from purchasing or selling securities of such issuer"
REPLACEMENT_TEXT: ""
COMMENT: "TS Capital has its own internal MNPI compliance procedures. A blanket US securities law acknowledgment is inappropriate for a non-US entity. Deleted in full — ATG precedent."
```

**Colibri — section heading + clause body (two separate changes)**:

```
ORIGINAL_TEXT: "Insider Information"
REPLACEMENT_TEXT: ""
COMMENT: "Section heading deleted consequentially — the entire Insider Information section is being removed."
```

```
ORIGINAL_TEXT: "The Interested Party acknowledges that some or all of the Information may constitute, or be deemed to constitute, price-sensitive information, the use of which may be subject to regulation or prohibition under applicable insider trading laws. The Interested Party undertakes not to use the Information for any unlawful purpose."
REPLACEMENT_TEXT: ""
COMMENT: "TS Capital already has internal compliance obligations not to misuse MNPI. An NDA-level undertaking creates duplicative and potentially conflicting obligations. Deleted in full — Colibri precedent."
```

**What NOT to do**: Do not narrow the clause or add a carve-out. DELETE the entire provision — both in ATG and Colibri the entire text was removed with no replacement.

---

### EXAMPLE 8 — Indemnification: English Formula (Star English NDA)

**What triggers it**: Full indemnification clause with "any loss, damage, expense or other liability... including attorney's fees and court costs" and no court-order prerequisite and no direct-losses-only limitation.

**Original clause**:
> `"we agree to indemnify and hold the Company and the Company's Representatives harmless and indemnified against any loss, damage, expense or other liability caused by such breach, including, but not limited to, attorney's fees and court costs incurred in connection with the enforcement hereof."`

**One surgical change** — replace the period at the end with a qualifying clause (do NOT delete the indemnification; qualify it):

```
ORIGINAL_TEXT: "attorney's fees and court costs incurred in connection with the enforcement hereof."
REPLACEMENT_TEXT: "attorney's fees and court costs incurred in connection with the enforcement hereof, provided that the foregoing indemnification shall not apply until the existence of such breach is established in a final, non-appealable order of a court of competent jurisdiction and, in any event, shall apply only to direct losses, damages, costs, or expenses (but not lost profits or any other indirect or consequential losses, damages, costs or expenses). In the event of litigation relating to this Agreement, if a court of competent jurisdiction determines in a final non-appealable order that a party has breached this Agreement, then the non-prevailing party will reimburse the prevailing party for the reasonable legal fees and expenses incurred by it in connection with enforcing its rights hereunder, including any appeal therefrom."
COMMENT: "Full indemnification without a court-order prerequisite creates open-ended financial exposure. Qualified to: (i) direct losses only, no consequential damages; (ii) not applicable until a final non-appealable court order confirms a breach; (iii) mutual fee-shifting — both parties can invoke it. Star precedent."
```

**What NOT to do**: Do not delete the indemnification clause entirely — the fix is a qualification, not a deletion. Keep the "including attorney's fees and court costs" language; just add the carve-out after it.

---

### EXAMPLE 9 — Ceasing Interest: English Version (ATG English NDA)

**What triggers it**: Any parenthetical or clause requiring TS Capital to notify the counterparty of a decision not to proceed, typically embedded in the return/destruction clause.

**Original clause (excerpt)**:
> `"...or on your own initiative if you decide not to proceed with the Transaction (of which decision you will promptly, and in any event within 24 hours, notify the Company), you will, as directed by the Company..."`

```
ORIGINAL_TEXT: " (of which decision you will promptly, and in any event within 24 hours, notify the Company)"
REPLACEMENT_TEXT: ""
COMMENT: "TS Capital has no obligation to inform a counterparty whether it will or will not invest. Investment decisions are entirely internal. Deleting the entire notification obligation — not just the 24-hour time limit. ATG precedent."
```

**What NOT to do**: Do not delete only the 24-hour limit while keeping the notification obligation. Delete the entire parenthetical in one change.

---

### EXAMPLE 10 — Remedy Asymmetry: Add Mutual Clause (ATG English NDA)

**What triggers it**: Injunctive relief, specific performance, or equitable remedy provisions that are one-sided — i.e., they can only be enforced by the Company/disclosing party against TS Capital, with no reciprocal right for TS Capital.

**Original clause (final sentence)**:
> `"Such remedy shall not be deemed to be the exclusive remedy for your breach of this agreement, but shall be in addition to all other remedies available at law or in equity to the Company."`

**Fix: ADD a mutual clause — do NOT delete the original provision**:

```
ORIGINAL_TEXT: "Such remedy shall not be deemed to be the exclusive remedy for your breach of this agreement, but shall be in addition to all other remedies available at law or in equity to the Company."
REPLACEMENT_TEXT: "Such remedy shall not be deemed to be the exclusive remedy for your breach of this agreement, but shall be in addition to all other remedies available at law or in equity to the Company. These provisions shall apply mutatis mutandis to both Parties, and the same remedies shall be available to the Receiving Party to enforce against the Disclosing Party in respect of any breach of this Agreement by the Disclosing Party or its Representatives."
COMMENT: "Injunctive relief and equitable remedies should be available to both parties equally. Adding a mutatis mutandis reciprocity clause rather than deleting the original provision — TS Capital should also have access to injunctive relief if the disclosing party breaches. ATG precedent."
```

**What NOT to do**: Do not delete the one-sided provision. The fix is to extend the same remedies to TS Capital by adding a reciprocal clause.

---

### EXAMPLE 11 — CI Exceptions: Add Missing Carve-Outs (Colibri German NDA)

**What triggers it**: The "Confidential Information does not include" carve-out list has only one item (typically "publicly available information") and is missing the other three standard exceptions.

**Original clause**:
> `"Information within the meaning of this Agreement does not include Information that the Interested Party can demonstrate is publicly available, provided such public availability is not the result of a breach of any statutory obligation or of any agreement between the Parties."`

**Fix: Format (i) properly and ADD (ii)–(iv)**:

```
ORIGINAL_TEXT: "does not include Information that the Interested Party can demonstrate is publicly available, provided such public availability is not the result of a breach of any statutory obligation or of any agreement between the Parties."
REPLACEMENT_TEXT: "does not include: (i) Information that the Interested Party can demonstrate is publicly available, provided such public availability is not the result of a breach of any statutory obligation or of any agreement between the Parties; (ii) was lawfully in the possession of the Interested Party prior to disclosure by [Disclosing Party]; (iii) lawfully obtained by the Interested Party from a third party that is not known to be bound by any confidentiality obligation to [Disclosing Party]; (iv) independently developed by or for the Interested Party without use of any Confidential Information received hereunder."
COMMENT: "Standard CI exceptions must include all four carve-outs: (i) public info; (ii) prior possession; (iii) received from third party without restriction; (iv) independently developed. The NDA currently has only (i). Colibri precedent."
```

**What NOT to do**: Do not add exceptions piecemeal or in different locations. Reformat the entire carve-out block to include all four in one numbered list.

---

### EXAMPLE 12 — Permitted Disclosure: Add "To Extent Legally Permissible" to Notice Obligation (ATG English NDA)

**What triggers it**: In the compelled disclosure clause, the notification obligation to the disclosing party has no "to the extent legally permissible and reasonably practicable" qualifier — meaning TS Capital must notify even when legally prohibited from doing so (e.g., under a gag order).

**Original clause (excerpt)**:
> `"the Receiving Party agrees to immediately notify the Disclosing Party of the existence, terms and circumstances surrounding such request, so that it may seek an appropriate protective order"`

Two changes needed — remove "immediately" AND add the qualifier:

```
ORIGINAL_TEXT: "the Receiving Party agrees to immediately notify the Disclosing Party of the existence, terms and circumstances surrounding such request, so that it may seek an appropriate protective order"
REPLACEMENT_TEXT: "the Receiving Party agrees to notify the Disclosing Party of the existence, terms and circumstances surrounding such request to the extent legally permissible and reasonably practicable, so that it may seek an appropriate protective order"
COMMENT: "Removing 'immediately' (unrealistic where legal advice is needed first) and adding 'to the extent legally permissible and reasonably practicable' — a gag order accompanying a subpoena may legally prohibit TS Capital from disclosing that a compelled disclosure request has been made. ATG precedent."
```

**What NOT to do**: Do not change the rest of the compelled disclosure clause (e.g., "all best efforts to preserve confidentiality of the remainder" and "written opinion" language). Only the notification obligation needs the qualifier.

**Also do NOT skip this change just because a similar-sounding qualifier already exists.** "To the extent not prohibited by law" and "to the extent permitted by law" both look adequate but are not — they only protect against legal prohibition (gag orders), not against practical impossibility (need for counsel, response time, drafting). Normalize to the exact phrase "to the extent legally permissible and reasonably practicable" every time. PingPong precedent shows this change being applied even where "to the extent not prohibited by law" was already in the original.

---

### EXAMPLE 13 — Representatives Narrowing: Eagle-Style Carve-Out vs Thor-Style Hard Delete (PingPong English NDA)

**What triggers it**: Representatives definition extends to "Affiliates" of a Party (e.g., "officers, directors... of a Party or such Party's Affiliates"). This makes the Recipient responsible for breaches by employees of all controlled affiliates / portfolio companies.

**Two acceptable approaches** — pick one based on context:

**Approach A — Eagle-style carve-out (preferred when definition is otherwise reasonable; PingPong precedent)**

Keep the existing definition intact; append a "Notwithstanding" carve-out that limits the Recipient's exposure AND explicitly excludes equityholders (LP investors):

```
ORIGINAL_TEXT: "controlling, or under common control with a Party."  [end of Affiliates definition block]
REPLACEMENT_TEXT: "controlling, or under common control with a Party. Notwithstanding the foregoing, in relation to the Recipient, Representatives shall not include equityholders or Affiliates to whom the Recipient has not provided Confidential Information."
COMMENT: "Limits Recipient's exposure to Affiliates that actually received Confidential Information (Eagle precedent) AND explicitly excludes equityholders — preserves IC/LP disclosure flexibility without rewriting the underlying definition. PingPong precedent."
```

**Approach B — Thor-style hard delete (use when minimal change footprint is preferred)**

```
ORIGINAL_TEXT: "advisors of a Party or such Party's Affiliates"
REPLACEMENT_TEXT: "advisors of a Party"
COMMENT: "Narrows Representatives to a Party's own personnel — removes responsibility for breaches by Affiliates' personnel. Thor precedent."
```

**When to choose A**: NDA is otherwise sensibly drafted; equityholders/LPs need explicit protection; diplomatic markup preferred (preserves the counterparty's drafting). This is the better default for English NDAs going forward.

**When to choose B**: NDA already has many flagged issues and you want minimal change footprint; the Affiliates qualifier is the only Representatives concern.

**What NOT to do**: Do not do both. Pick one. Approach A is preferred when in doubt.

---

## Standard Changes (Always Apply on First Markup)

These changes are made on every NDA regardless of whether the specific language triggers a must-fix flag. Apply them as tracked changes with comments.

### S1 — Fill In ALL Blanks (Date, Entity, Address, Contact)

**Step 1 — Scan for placeholders FIRST**, before analyzing any substantive clause. Look for: `[●]`, `[日期]`, `[Date]`, `[协议对方名称]`, `[Interested Party]`, `[Bidder]`, `[地址]`, `[Address]`, `[联络人姓名]`.

Fill in every blank found:

**Date** (`[日期]` / `[Date]` / `[●]` / `[mm] [dd], [yyyy]`): Fill ONLY if the user provides an actual execution date. Otherwise **leave the placeholder unchanged** — the date is filled at signing time, not at markup. Do not pre-fill with `[●]`, `TBD`, or anything else. PingPong precedent.

**Entity name** (every occurrence in header, preamble, body, and signature block):
- Chinese NDAs: `信宸资本股权投资管理有限公司`
- English NDAs: `TS Capital Partners Management Limited`

**Address**:
- Chinese NDAs: `香港中环添美道1号中信大厦28楼`
- English NDAs: `28/F CITIC Tower, 1 Tim Mei Ave, Central, Hong Kong`

**Signatory / contact name** (`[联络人姓名]` / `[●]` in letter header): Fill in the TS Capital deal contact for this project. Ask the user if unknown. Do NOT use Henry Zeng unless this is the formal signature block.

**Signature block**: Replace "Interested Party" / "Bidder" / "乙方" with the correct entity name. Delete any commercial register clause.

**Case convention**: Use the entity's natural legal-name case throughout the document (e.g., `TS Capital Partners Management Limited`), even when the placeholder is in ALL CAPS (e.g., `[NAME OF COUNTERPARTY]`). Placeholder formatting is not part of the entity name. PingPong precedent.

COMMENT: "Filling in the correct TS Capital entity and contact details. Only this specific fund entity should be named — not a broader CITIC entity or an affiliate."

### S2 — NDA Term: Push to Target

**English NDAs**: If the NDA term is more than 1 year, change to 1 year on initial markup.

Simple number replacement (Helix precedent):
ORIGINAL_TEXT example: `the second (2nd) anniversary`
REPLACEMENT_TEXT example: `the first (1st) anniversary`

**Preferred formula — dual-trigger (Thor precedent)**: If the clause structure permits, replace the entire term sentence with a dual-trigger formula that terminates on the earlier of 1 year OR deal completion:

REPLACEMENT_TEXT example: `"This Agreement shall expire and cease to have any force or effect on the earlier of (i) the first anniversary of the date hereof and (ii) the date of consummation of the Transaction between the parties."`

The dual-trigger is better than a bare 1-year term because it also terminates the NDA automatically on deal close, so TS Capital is not bound by confidentiality obligations after it has invested.

**Chinese NDAs**: If the NDA term is more than 2 years, change to 2 years using the Adam formula. See Chinese NDA section for exact replacement text.

COMMENT: "Standard position is 1-year NDA term (English) / 2-year (Chinese). Preferred English formula: earlier of 1st anniversary or deal completion. Willing to accept up to 2 years if counterparty pushes (English)."

### S3 — Non-Solicit: Push to 1 Year + Add Unsolicited Approach Carve-Out

Change non-solicit period to 1 year. Additionally, ALWAYS add the unsolicited approach carve-out — regardless of whether you are changing the term.

**Add to existing carve-outs**:
- English: `or (c) such person proactively contacts TS Capital without any solicitation by TS Capital`
- Chinese: `或(c) 该等人员主动接洽（未经贵方邀请）`

COMMENT: "Standard position on non-solicitation is 1 year. Also adding carve-out for unsolicited approaches — employees who contact TS Capital on their own initiative should not be restricted."

### S4 — Permitted Disclosure: Broaden the Trigger

If the permitted disclosure trigger is "mandatory law, regulation, court order or applicable stock exchange rules" (or a similarly narrow formulation), broaden it.

ORIGINAL_TEXT example: `mandatory law, regulation, court order or applicable stock exchange rules`
REPLACEMENT_TEXT example: `any law, regulation or legal, regulatory or judicial process`

COMMENT: "The narrow 'mandatory law' formulation prevents TS Capital from making disclosures required in the ordinary course (regulatory filings, internal compliance processes). Broadening to 'any law, regulation or legal, regulatory or judicial process' is the standard investor-side position."

**Also flag — reduce required cooperation**: If the NDA requires TS Capital to "pursue all available legal remedies" or "exhaust all available means" to resist a legally compelled disclosure, change to "take reasonable legal steps to limit the scope of disclosure."

ORIGINAL_TEXT example: `pursue all available legal remedies against official or court orders`
REPLACEMENT_TEXT example: `take reasonable legal steps to limit the scope of disclosure`

COMMENT: "An obligation to 'pursue all available legal remedies' is open-ended and could require costly litigation even where resistance is futile. 'Reasonable legal steps' is the market-standard formulation — it maintains a good-faith cooperation obligation without mandating full-scale legal proceedings. Accepted in Colibri (German) precedent."

### S5 — Return/Destruction: Add Reasonably Practicable Qualifier

Add "to the extent reasonably practicable" to the return/destruction obligation so that it covers the full obligation — not just the electronic purge sub-clause.

**Placement is flexible** — use whichever position fits the sentence:
- Mid-clause in the preamble (Helix precedent): `the Interested Party shall promptly, to the extent reasonably practicable, upon written request of Seller`
- As a trailing qualifier to the main obligation (Star precedent): `we agree to destroy all Confidential Information in our possession or to which we have access to the extent reasonably practicable`
- At the end of the whole sentence (Colibri precedent): `refrain from further use to the extent reasonably practicable and technologically feasible`

"And technologically feasible" is also acceptable (Colibri).

The key requirement: the qualifier must cover the **full** obligation, not just an electronic purge sub-clause buried at the end.

COMMENT: "An unqualified obligation to return or destroy ALL Confidential Information is impossible to comply with — automated backups, email archives, and system snapshots cannot be individually purged. Accepted in Colibri (German) as 'reasonably practicable and technologically feasible'."

### S6 — Change Written Consent → Timely Notice for Permitted Disclosures

If any permitted disclosure condition (other than disclosing to financing sources) requires "prior written consent" / `书面同意` from the counterparty, change to "timely notice" / `及时通知`.

Example: disclosure conditions `(i) business need, (ii) 书面同意, (iii) legal requirement` → change (ii) to `及时通知`

COMMENT: "Requiring prior written consent before any permitted disclosure creates an approval bottleneck that is operationally unworkable. Timely notification is sufficient — TS Capital should not need counterparty approval before sharing information with its own advisors and representatives."

### S7 — DELETE MNPI / Insider Trading Restriction Clauses

If the NDA contains any clause restricting TS Capital's securities trading activity based on receipt of information — including US securities law acknowledgments, insider trading undertakings, price-sensitive information lockups, or MNPI-based trading prohibitions — DELETE the entire clause in full, including any dedicated section heading.

ORIGINAL_TEXT example (ATG): `"You hereby acknowledge that you are aware, and that you will advise your Representatives who are informed as to the matters which are the subject of this agreement, that the United States securities laws prohibit any person who has received from an issuer material, non-public information concerning the matters which are the subject of this agreement from purchasing or selling securities of such issuer"`
REPLACEMENT_TEXT: `""`

ORIGINAL_TEXT example (Colibri — section heading): `"Insider Information"`
REPLACEMENT_TEXT: `""`

ORIGINAL_TEXT example (Colibri — clause body): `"The Interested Party acknowledges that some or all of the Information may constitute, or be deemed to constitute, price-sensitive information, the use of which may be subject to regulation or prohibition under applicable insider trading laws. The Interested Party undertakes not to use the Information for any unlawful purpose."`
REPLACEMENT_TEXT: `""`

COMMENT: "TS Capital has its own internal compliance procedures for managing MNPI. An NDA-level trading restriction creates duplicative and potentially conflicting obligations — in particular, a blanket 'acknowledge-and-advise' clause on US securities laws is inappropriate where TS Capital is not a US entity and the transaction is not US-listed. Deleted in full on multiple precedent deals (ATG, Colibri)."

---

## Must-Fix Issues to Scan

Only flag an issue if the NDA actually contains the problematic language. Scan every category below, output only the ones triggered. Each flagged issue must have a COMMENT explaining the WHY.

| # | Category | Flag if NDA contains... |
|---|----------|------------------------|
| 1 | Blank Date | Date field is unfilled — handled by S1, but flag separately if date is blank and a specific date is expected |
| 2 | Signatory Entity | Company name anywhere in the NDA is "CITIC" or any entity other than "TS Capital Partners Management Limited" / "信宸资本股权投资管理有限公司". Do NOT flag pre-filled individual signatory names or titles. |
| 3 | Portfolio Companies / Affiliates in Affiliate or Reps Definition | (a) "Affiliate" definition explicitly includes portfolio companies of TS Capital's funds — DELETE portfolio companies from the definition entirely (co-managed funds may stay). (b) Representatives definition extends to "a Party's Affiliates" (broad "common control" definition then captures portfolio companies indirectly) — preferred fix is Approach A (Eagle-style Notwithstanding carve-out with equityholders exclusion, PingPong precedent); fallback Approach B (Thor-style hard delete of the "or such Party's Affiliates" qualifier). See Gallery Example 13. |
| 4 | Standard Exceptions | Missing any of the 4 carve-outs from "Confidential Information": (i) public info, (ii) prior possession, (iii) received from 3rd party without restriction, (iv) independently developed. Fix: reformat the carve-out block and add the missing items — see Gallery Example 11 for verbatim language. |
| 5 | Representatives Definition | Excludes financing sources (debt/equity), or narrower than: directors, officers, employees, advisors (attorneys, accountants, consultants, bankers, financial advisors), financing sources |
| 6 | Representatives Carve-Out | TS Capital held fully responsible for ALL representative breaches with no carve-out. Fix: Replace with — TS Capital is not responsible for breaches by outside representatives IF those representatives have signed a written undertaking confirming they are bound by the NDA's terms |
| 7 | Mutual Non-Publicity | Non-publicity or no-shop provision binds only TS Capital and not the other party |
| 9 | Notice/Consent — Financing | NDA has a dedicated section restricting contact with or disclosure to Financing Institutions / Insurance Institutions. Fix: DELETE the entire Financing Institutions section. If NDA requires written consent before disclosing to financing sources but no dedicated section, flag the consent requirement for deletion. Prior concession: Ampere (signed, German) accepted prior written consent. |
| 10 | Notice/Consent — Misuse (cost-shifting) | NDA includes language requiring TS Capital to bear the counterparty's costs of investigating misuse / misappropriation (e.g., "贵方承担" / "at your cost or expense"). Fix: DELETE ONLY the cost-shifting language — do NOT delete the underlying notification obligation. |
| 11 | Notice/Consent — Ceasing Interest | NDA requires TS Capital to notify the target when it decides not to proceed. Fix: DELETE the entire ceasing-interest notification sentence. Also delete any associated hard time limit (e.g., "于24小时内" / "within 24 hours"). Initial markup position is to delete the obligation entirely. Fallback if counterparty pushes: accept the notification but delete the hard time limit. |
| 12 | Copies | Restriction on making copies applies to copies shared with Representatives |
| 13 | Permitted Disclosure | (a) Trigger is "mandatory law" or similarly narrow — should be "any law, regulation or legal, regulatory or judicial process" (see S4). (b) The notification obligation to the disclosing party does not contain the EXACT phrase "to the extent legally permissible and reasonably practicable". **Equivalent-sounding qualifiers such as "to the extent not prohibited by law" or "to the extent permitted by law" are NOT acceptable substitutes** — they cover legal prohibition (e.g., a gag order) but not practical impossibility (lawyer review needed, time to react). Replace any narrower formulation with the exact market-standard phrase, even when a similar qualifier is already present. PingPong precedent. Also remove "immediately" if present (see Gallery Example 12). |
| 14 | Return/Destruction | (a) No "reasonably practicable" qualifier — must cover the full obligation, not just the electronic purge sub-clause (see S5); (b) Obligation to provide a signed certificate / written confirmation of destruction — initial position is to DELETE. **Fallback if §10 already contains a backup-files carve-out paragraph (limiting the scope of what is being certified)**: certification may be kept as a concession, since the backup carve-out already softens practical exposure (PingPong precedent — human kept certifications because backup carve-out was present); (c) Return/destruction triggered automatically without requiring a written request. (d) Hard time-window (e.g., "within ten (10) days") — surgical fix is to replace with "promptly, to the extent reasonably practicable" rather than deleting the deadline entirely. |
| 15 | Non-Solicit Term | Non-solicit period exceeds 1 year. Push to 1 year on initial markup (see S3). Max accepted: 24 months (Eagle precedent). Also check: is the unsolicited approach carve-out present? If not, add it (see S3). |
| 16 | Non-Solicit Scope | Non-solicit binds ALL affiliates/funds regardless of whether they received CI (binding affiliates who actually received CI is accepted — Eagle precedent). Flag if applies to all affiliates without CI-receipt limitation. |
| 17 | Term | NDA term exceeds 1 year (English) / 2 years (Chinese). Push to 1 year on initial markup for English; 2 years for Chinese using the "earlier of 2 years or deal completion" formula. Max accepted (English): 2 years; 3 years only as a last concession. |
| 18 | Third Party Beneficiaries | NDA grants rights to third parties beyond the standard sell-side process agent role, or context is not a formal sell-side process. Third-party beneficiary accepted in German NDAs (Eagle, Ampere, Colibri) and Korean (Thor) — flag but note as common in banker-run processes. |
| 19 | Governing Law | US deal with governing law other than NY or DE (never agree to IL); or governing law does not match the target's home jurisdiction |
| 20 | Indemnification | NDA requires TS Capital to indemnify for: any consequential/indirect damages, prosecution or enforcement costs, "消除影响" costs, or any losses without a final court judgment prerequisite. Fix: DELETE the full indemnification clause. REPLACE with mutual fee-shifting formula conditioned on final court judgment (see Indemnification section in Key Precedent Facts for exact language). Do NOT use a one-sided replacement — the replacement must be mutual (both parties can invoke it). |
| 21 | Standstill | Any standstill provision present on initial review; or standstill binds affiliates/Representatives; or includes prohibition on requesting waiver |
| 22 | Remedy Asymmetry | Remedy or injunctive relief provisions apply only against TS Capital, not mutually. Fix: ADD a reciprocal clause ("These provisions shall apply mutatis mutandis to both Parties, and the same remedies shall be available to the Receiving Party...") — do NOT delete the original provision. For arbitration clauses: add "The arbitration proceeding and remedies shall be equally enforceable by both Parties without unilateral procedural disadvantage." See Gallery Example 10. |
| 23 | Records Obligation | NDA requires TS Capital to maintain logs of who received CI and report them on request. Do NOT delete this clause — instead, EXPAND the list of institution types (add financial advisors, consultants, financing sources) so those recipients fall under the "name + team leader only" bucket. |
| 24 | MNPI / Securities Trading Restrictions | Provisions restrict TS Capital from trading beyond standard insider trading compliance (e.g., US securities law acknowledgments, insider trading undertakings, MNPI-based lockups). Fix: DELETE the entire provision in full, including any dedicated section heading (see S7). Deleted in ATG and Colibri precedents. |

---

## What NOT to Flag (Negative Space)

These patterns commonly look problematic at first read but were **NOT changed** in any of the tracked human markups. Do not flag them on initial markup. If you find yourself wanting to flag something on this list, stop and reread the relevant tracked file before doing so.

**Process / banker-driven structure (typically kept):**
- Third-party beneficiary clauses naming the M&A advisor (e.g., "Lincoln International" in Thor). Standard banker-run process structure.
- Single-point-of-contact requirement ("direct all requests for information to [Bank]") — kept in Thor.
- Prior consent for contacting Company employees/customers/suppliers during the process — kept in Thor.

**Equitable relief / one-sided remedy preamble (do NOT delete):**
- The full equitable relief preamble (specific performance, injunctive relief, "money damages inadequate", waiver of bond) — kept in ATG. The fix for asymmetry is to ADD a mutual reciprocity clause at the end (see Gallery Example 10), not to delete the existing language.

**Compelled disclosure clause specifics (only change what Example 12 changes):**
- "All best efforts to preserve confidentiality of the remainder of the Evaluation Material" — kept in ATG.
- "Outside legal counsel" trigger formulation (when broad enough on its face) — kept in ATG.
- Only the notification obligation needs the "to extent legally permissible" qualifier — do not rewrite the rest of the compelled disclosure clause.

**Confidentiality scope (when reasonably complete):**
- Pre-existing CI exceptions (i)(ii)(iii) — kept in Thor; only added the missing (iv).
- "We will be responsible for any breach by our Representatives" without an Annex A undertaking carve-out — kept in Thor for process deals where adding the carve-out is impractical.

**Governing law (matching deal jurisdiction):**
- DIS Stuttgart arbitration for German deals — kept in Colibri.
- PRC arbitration for Chinese deals — accepted across all signed Chinese precedents.
- Lincoln-style banker process governance — kept.

**Non-solicit pre-existing carve-outs (typically kept):**
- Advisor carve-out (`"excluding Representatives who are debt financing sources, attorneys, accountants, consultants, agents and financial advisors so long as such Representatives are not acting on our behalf with respect to employee solicitation or hiring"`) — kept in Thor; only change the period.
- "Employees" defined as those with actual contact / who become known in connection with the transaction — kept in Thor (already narrow enough).
- Generalized media advertisement carve-out — kept in ATG.

**Indemnification (when adding qualifier is enough):**
- The "including attorney's fees and court costs" enumeration — kept in Star. Only ADD the "provided that... direct losses only... final non-appealable order... mutual fee-shifting" qualifier (see Gallery Example 8); do not delete the surrounding language.

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

Standard Changes:
| # | Standard Change | Y/N | Location / Note |
|---|-----------------|-----|-----------------|
| S1 | Fill blanks (date, entity, address, contact) | Y/N | header / preamble / signature |
| S2 | NDA term reduction (1yr EN / 2yr CN) | Y/N | §X — current term |
| S3 | Non-solicit 1yr + unsolicited approach carve-out | Y/N | §X |
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
| S2 | Standard | Term reduction | §16 | 10 years → 2 years (Adam formula) |
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
python "<path-to-skill>/apply_redlines.py" "input.docx" "input_TS_markup.docx" "changes.json"
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
3. **Nothing missed** — scan the full document one more time for unfilled placeholders (`[●]`, `[日期]`, `[地址]`, `[联络人]`) and confirm Part 0 caught every triggered category.
4. **Replacement text quality** — read each REPLACEMENT_TEXT aloud (mentally). Is it grammatically correct? Does it flow naturally in context? Fix any typos or awkward phrasing.
5. **Comments are clear** — each COMMENT should state the business reason in plain language. Remove any comment that just describes the change without explaining why.
6. **Coherence** — does the full set of changes tell a consistent story? Are there any contradictions between changes?

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

All signed Chinese NDAs have 2-year terms. Initial markup should change any term exceeding 2 years to 2 years using the Adam formula:

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

COMMENT: "Providing a signed destruction certificate is operationally difficult and creates legal exposure — a signed certificate confirming 'complete' destruction may itself be inaccurate due to system backups and email archives."

### 不招揽条款 — Non-Solicit Carve-Out

When modifying non-solicit scope or term, ALWAYS add the unsolicited approach carve-out:

**Add**: `或(c) 该等人员主动接洽（未经贵方邀请）`

This is in addition to the standard passive job posting carve-out `(a)`.

### 赔偿条款 — Indemnification Replacement

If the NDA contains a full indemnification clause (any reference to `任何性质的全部损失`、`成本`、`权利主张`、`受偿人`、`消除影响费用` etc.):

**Delete**: The entire full indemnification clause

**Insert**: The Adam mutual fee-shifting formula:
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
2. **Calibrate against human markups** — before finalising any redline, check whether a similar change appears in Section B of `./knowledge/precedents-distilled.md`. If no past markup shows this kind of change, reconsider whether the change is truly necessary.
3. **Be surgical — never over-delete** — only delete or replace the specific problematic language. If an obligation has a problematic rider (e.g., "at your cost"), delete only the rider, not the whole obligation. Read the full clause and identify precisely what is wrong before touching anything.
4. **Read every placeholder first** — before analyzing substantive clauses, scan the entire document for unfilled blanks (`[●]`, `[日期]`, `[地址]`, `[协议对方名称]`, `[联络人]`) and fill every one as part of S1.
5. **Verify exact text from the document** — before writing ORIGINAL_TEXT, extract the actual paragraph text from the document XML to confirm character-level accuracy. Watch for half-width `()` vs full-width `（）`, and curly `"` vs ASCII `"` quotes.
6. **Always include WHY** — every change gets a comment explaining the business reason. The comment goes in the redline block AND as a margin comment in the Word document.
7. **Fallback positions** — include the fallback in the comment where one exists ("if they push back, the fallback is..."). Signed precedents show what was conceded — use them as fallbacks, not as reasons to skip the initial markup change.
8. **Standard changes are not optional** — S1–S6 are applied on every NDA. Do not skip them because the template "seems fine."
9. **Don't remove clauses from exception lists — rewrite them** — if a clause needs to be limited (e.g., §13 indemnification), rewrite it to a reasonable scope. Keeping the rewritten clause as a permanent exception is correct. Do not remove §13 from the exceptions list just because the indemnification was problematic — fix the clause instead.
