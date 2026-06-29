# Distilled Precedents

This file replaces the raw `signed/` and `tracked/` NDA files. It encodes the patterns the skill needs, with all counterparty names, addresses, signatories, and deal-specific terms removed. Deal codenames are kept (they are internal identifiers, not real entity names).

Maintainer note: regenerate this file by running `tools/distill.py` after adding new precedents to your local (un-committed) `signed/` and `tracked/` folders.

---

## A. Signed precedents (final negotiated outcomes)

These are what counterparties ultimately accepted. Use as **fallback positions** when the counterparty pushes back, not as initial markup.

| Code | Target jurisdiction | Term agreed | Non-solicit agreed | Indemnification | Notable concession |
|------|--------------------|-------------|--------------------|-----------------|--------------------|
| Adam | China | 2yr (Adam formula: earlier of 2yr or deal close) | n/a | Mutual fee-shifting after final court judgment | IC/LP disclosure expressly allowed; ceasing-interest notice accepted |
| Agile | China | 2yr | n/a | Full indemnification including 3rd-party claims **accepted as concession** | — |
| Ampere | Germany | 2yr | 24mo (CI recipients only) | None | Prior written consent for financing-source disclosure **kept as concession**; 3rd-party beneficiary accepted |
| Colibri | Germany | 3yr **accepted as concession** (TS pushed 1yr) | n/a | None | DIS Stuttgart arbitration; 3rd-party beneficiary |
| Copper | China | 2yr | n/a | Limited | — |
| Eagle | Germany | 2yr | 24mo (CI recipients only) | None | Non-solicit binding affiliates **only** where they actually received CI |
| Spring | China | 2yr | n/a | Direct losses only + court-order prerequisite | Zero markup needed — template was already acceptable |
| Star | US | 2yr | n/a | Direct losses only + final non-appealable order + mutual fee-shifting | 3yr → 2yr conceded (TS pushed lower) |
| Thor | Korea | 1yr or deal close (dual-trigger) | 24mo (with broad advisor carve-out) | Limited | Korean law unavoidable; Lincoln-style 3rd-party beneficiary; MNPI lockup; records obligation |
| 惠康科技 (Hui-Kang) | China | 2yr | n/a | Limited | — |
| 紫光 (Tsinghua-Unigroup) | China | 2yr | n/a | Full indemnification accepted as concession | Notice-of-suspected-breach **accepted as concession** |
| 股权投资 (Equity-Investment) | China | 2yr | n/a | Limited | — |

**Aggregate signed-precedent patterns**:
- Term: **9 of 12 deals settled at exactly 2 years**. 1 at 3 years (Colibri, German concession). 1 at 1yr/deal-close (Thor). 1 unique (Adam formula = earlier of 2yr or deal close).
- Non-solicit: 24 months is the practical ceiling when present. Most Chinese deals had none.
- Indemnification: "Direct losses only + final non-appealable court order" is the most common limit. Full indemnification has been conceded in 2 Chinese deals.
- Governing law: **always matched the target's home jurisdiction**. No deal forced an unrelated jurisdiction.

---

## B. Human first-markup positions (TS Capital's opening offers)

These are what TS Capital marked up on initial review. Use as **primary calibration** — the patterns the skill should reproduce.

| Code | Changes made on first markup | Changes deliberately NOT made |
|------|------------------------------|-------------------------------|
| ATG (English) | Date/entity fill-in; MNPI clause deleted in full; permitted disclosure: removed "immediately" + added "to extent legally permissible and reasonably practicable"; ceasing-interest parenthetical deleted; non-solicit 2yr → 1yr; equitable-relief preamble made mutual via reciprocity clause added; term 2yr → 1yr | Equitable-relief preamble itself **kept** (mutual clause added, not deleted); "all best efforts to preserve confidentiality of remainder" kept; "outside legal counsel" trigger formulation kept |
| Colibri (German) | Entity + address fill-in; CI definition reformatted to add (ii)(iii)(iv); permitted disclosure cooperation: "pursue all legal remedies" → "take reasonable legal steps"; return/destruction added "to extent reasonably practicable and technologically feasible"; term 5yr → 1yr; MNPI section (heading + body) deleted in full; arbitration: added "equally enforceable by both Parties" reciprocity clause | DIS Stuttgart arbitration **kept**; German governing law **kept** |
| Helix (German) | Term 2yr → 1yr; portfolio companies deleted from Affiliate definition (and follow-on consent paragraph deleted); Financing Institutions section deleted in full; return/destruction "to extent reasonably practicable" added to preamble | Co-managed funds in Affiliate definition **kept** |
| PingPong (Cayman/HK) | Entity + address fill-in (recipient address added since preamble had none); term 10yr → dual-trigger (earlier of 1yr or deal close); return/destruction "reasonably practicable" added + 10-day deadline removed + 2× certifications deleted; Reps definition narrowed (removed "or such Party's Affiliates"); CI exception (d) "independently developed" added; Rep undertaking carve-out added to §7(d); §8 non-publicity made mutual ("Recipient" → "neither Party") | Hong Kong law / HKIAC arbitration **kept** (matches TS jurisdiction); §17 no-third-party-beneficiary disclaimer **kept**; §9 compelled-disclosure structure largely **kept** (only notification qualifier touched) |
| Spring (China) | (zero changes — template was acceptable) | — |
| Star (English) | Return/destruction "to extent reasonably practicable" added; indemnification qualified with "provided that... applies only to direct losses... not until final non-appealable court order"; term 3yr → 2yr | "Including attorney's fees and court costs" enumeration **kept** (only qualifier added) |
| Thor (Korean) | Reps definition narrowed (removed "all controlled affiliates and subsidiaries"); CI exception (iv) "in our possession prior to disclosure" added; non-solicit 2yr → 1yr (the existing advisor carve-out **kept**); term replaced with dual-trigger formula (earlier of 1yr or deal close); entity fill-in | Lincoln 3rd-party beneficiary **kept**; pre-existing CI exceptions (i)(ii)(iii) **kept**; broad rep responsibility "we will be responsible for any breach by our Representatives" **kept** (no Annex A in this process deal); non-contact restriction on employees/customers **kept**; advisor carve-out in non-solicit **kept** |
| Adam (Chinese) | Date + entity fill-in (header + signature); 保密期限 → Adam formula (earlier of 2yr or deal close); 停止参与通知 sentence deleted in full; 销毁证明 obligation deleted; 不招揽 carve-out for unsolicited approaches added; 赔偿条款 replaced with mutual fee-shifting formula; 消除影响费用 separately deleted | IC/LP disclosure permission **kept**; 关联人员 definition **kept** (already broad enough); arbitration **kept** |

**Aggregate first-markup patterns** (the skill should reproduce these reliably):
- **Term**: always pushed to 1 year on initial markup (English). Chinese: 2yr with Adam formula.
- **MNPI / insider trading restrictions**: deleted in full every time present (ATG, Colibri — both deals where it appeared).
- **Ceasing-interest notification**: deleted in full every time present (ATG, Adam).
- **Return/destruction**: "to extent reasonably practicable" added every time missing (Helix, Star, Colibri, PingPong, Adam). Placement is flexible (preamble or trailing); ATG used preamble, Star used trailing.
- **Non-solicit period**: 1 year first position, every time (ATG, Thor).
- **Mutual non-publicity / mutual remedies**: ADDED reciprocity clause (do not delete original) (ATG, Colibri, PingPong).
- **Portfolio companies / Affiliates in Reps**: two acceptable approaches — Thor-style hard delete OR PingPong-style Eagle carve-out with equityholders exclusion. Choose by context.
- **Indemnification**: when full, qualified to "direct losses only + final non-appealable order + mutual fee-shifting" (Star — English) or replaced with Adam mutual formula (Adam — Chinese).
- **Permitted disclosure notification qualifier**: always replace any narrower formulation ("not prohibited by law", "permitted by law") with the exact phrase "to the extent legally permissible and reasonably practicable" — they are not equivalent.

**Aggregate "did NOT change" patterns** (the skill should respect):
- Governing law matching target jurisdiction.
- Arbitration venue matching deal type (DIS for German, HKIAC for HK, PRC for Chinese targets).
- 3rd-party beneficiary clauses naming the M&A advisor (Lincoln, LBBW) in banker-run processes.
- Pre-existing equitable-relief preamble — add mutual reciprocity, never delete.
- Pre-existing advisor carve-outs in non-solicit clauses.
- Backup-files paragraph in return/destruction §s — softens certification requirement.

---

## C. Guideline-derived positions (CITIC Capital NDA review memo)

The full guideline PDF is not bundled. Its key positions are encoded throughout SKILL.md (Key Precedent Facts section + 24 Must-Fix Categories + Standard Changes S1–S7). Highlights:
- TS Capital is the Recipient/investor side. Entity: TS Capital Partners Management Limited (English) / 信宸资本股权投资管理有限公司 (Chinese).
- Term targets: 1yr (English) / 2yr (Chinese) initial position.
- Non-solicit target: 1yr initial position with unsolicited-approach carve-out.
- Always required: Annex A / written undertaking mechanism for outside reps.
- Always delete: MNPI/insider trading clauses, ceasing-interest notifications, Financing Institutions dedicated sections, 销毁证明 requirements.
- Always limit: indemnification (direct losses + court-order prerequisite + mutual fee-shifting).

For positions not captured here, consult SKILL.md (which is itself the primary distillation of the guideline).
