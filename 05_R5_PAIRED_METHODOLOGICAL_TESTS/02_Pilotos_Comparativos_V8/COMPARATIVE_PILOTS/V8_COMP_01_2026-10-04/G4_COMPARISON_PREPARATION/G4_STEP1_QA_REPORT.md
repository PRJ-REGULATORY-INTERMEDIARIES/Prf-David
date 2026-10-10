# G4 Step 1 — normalization QA report

**Date:** 2026-10-04T19:28:09-03:00 · **Executor:** Claude Code (Sonnet 5.5), single sequential pass · **Status of checks:** 25 PASS, 0 FAIL, 1 informational (of 26)

All checks are automatic or mechanical comparisons against the local register and the frozen cell files. They test integrity, preservation and consistency; they are **not** an independent human audit of the normalised wording and **do not** assess legal validity.

## 1. Check results

| ID | Check | Result | Detail |
|---|---|---|---|
| Q01 | Required 24 fields present in the stated order | **PASS** | first 24 columns = specified list |
| Q02 | Original units per cell equal Step 0 (24/29/28/31); 112 total | **PASS** | {'CODEX_A': 24, 'CODEX_B': 29, 'CLAUDE_A': 28, 'CLAUDE_B': 31} |
| Q03 | Two STEP0_DERIVED units, one per Claude cell | **PASS** | CL-P03-02#CORE (Claude A), CL-P04-02#CORE (Claude B) |
| Q04 | Unique (cell, claim id) keys; unique unit_id | **PASS** | 114 unique |
| Q05 | One-to-one with Step 0 rows (same cell/claim id/step0_row_id) | **PASS** | 114 mapped |
| Q06 | Statement IDs exist in the local register; anchors and case recomputed from the register match | **PASS** | invalid ids: []; anchor/case mismatches: [] |
| Q07 | No blank required field (explicit NOT_APPLICABLE/NONE used instead) | **PASS** | blank: [] |
| Q08 | Scope classes reproduce Step 0 (SC-A 105, SC-B 2, SC-C 5, SC-D 0) | **PASS** | {'SC-A': 105, 'SC-C': 5, 'SC-B': 2} |
| Q09 | The five material deviations are exactly those reported at Step 0 | **PASS** | [('CLAUDE_A', 'CL-P03-02'), ('CLAUDE_A', 'CL-P03-03'), ('CLAUDE_A', 'R-P03-04'), ('CLAUDE_B', 'CL-P04-02'), ('CLAUDE_B', 'R-P04-05')] |
| Q10 | The two borderline units are exactly CL-P04-04 and CL-P04-07 (Claude B) | **PASS** | [('CLAUDE_B', 'CL-P04-04'), ('CLAUDE_B', 'CL-P04-07')] |
| Q11 | 13 peripheral observations preserved | **PASS** | Step 0: 13; Step 1: 13 |
| Q12 | No original unit changed eligibility from Step 0 (derived units formalised as provisional) | **PASS** | changed: [] |
| Q13 | Eligibility counts: YES 94; YES_WITH_PERIPHERAL_FLAG 11; NO_SENSITIVITY_ONLY 5; PROVISIONAL(SC-B) 2; derived provisional 2 | **PASS** | {'YES': 94, 'NO_SENSITIVITY_ONLY': 5, 'YES_WITH_PERIPHERAL_FLAG': 11, 'YES_PROVISIONAL_PENDING_HUMAN_CONFIRMATION': 2, 'PROVISIONAL_PENDING_P1_HUMAN_CONFIRMATION (STEP0_DERIVED; Step 0 value was YES)': 2} |
| Q14 | Eligibility register aligned row by row with the claims register | **PASS** | 114 aligned |
| Q15 | Dependency propagation: material only where the unit itself is SC-C (5); no inherited material dependency; peripheral/borderline inheritance recorded | **PASS** | {'NONE': 95, 'MATERIAL_DIRECT': 5, 'PERIPHERAL_INHERITED': 11, 'BORDERLINE_INHERITED': 1, 'NOT_APPLICABLE_DERIVED': 2} |
| Q16 | Original formulations preserved verbatim (relations: all record fields; other units: every line found in the frozen source file) | **PASS** | failures: [] |
| Q17 | Source-file SHA-256 recorded in the register equals recalculated value | **PASS** | mismatches: [] |
| Q18 | Relation normalisation carries actors, modality, condition and statement IDs of the original record | **PASS** | failures: [] |
| Q19 | INFORMATIONAL (not pass/fail): lexical coverage of non-relation normalised texts by original text/warrant/member fields; units below 0.75 listed and read manually | **INFO** | n=41; mean coverage 0.84; below 0.75: 6 |
| Q20 | No matching, agreement, improvement, regression or superiority fields; no working or protocol A-to-B label values in the registers | **PASS** | forbidden headers: []; label occurrences: 0 |
| Q21 | External E0-E3 labels not mapped; candidate column explicitly unauthenticated and not adopted | **PASS** | status NOT_MAPPED on 114 rows |
| Q22 | Existing 28-item review queue preserved (same IDs, priorities, order) | **PASS** | 28 items; {'P1': 7, 'P3': 7, 'P2': 14} |
| Q23 | Priority-1 items carry exact frozen excerpts, original claim, uncertainty, non-frozen text in question and the reason for human judgment | **PASS** | 7 P1 items |
| Q24 | No human decision fields filled (no simulated human review) | **PASS** | all blank |
| Q25 | Four frozen cells (6+11 Codex, 7+11 Claude outputs) and the common register unchanged | **PASS** | 0 mismatches; Codex outputs checked 17 |
| Q26 | Step 0 files unchanged since the Step 0 manifest (only the authorisation file was appended) | **PASS** | changed: [] |

## 2. Units extracted and classified per cell

| Cell | Original units | of which relations | configuration/relation-level claims | positional | architecture-level decisions | STEP0_DERIVED |
|---|---|---|---|---|---|---|
| CODEX_A | 24 | 16 | 6 | 0 | 2 | 0 |
| CODEX_B | 29 | 17 | 6 | 4 | 2 | 0 |
| CLAUDE_A | 28 | 19 | 7 | 0 | 2 | 1 |
| CLAUDE_B | 31 | 19 | 6 | 4 | 2 | 1 |

Original units 112 + 2 STEP0_DERIVED = 114 rows. Six original units received IDs at Step 0 because the cell did not label them (Codex B positional rows `TB-O5-*`; Claude B `AD-P03`, `AD-P04`); they are marked `ORIGINAL_CELL_CLAIM_ID_ASSIGNED_AT_STEP0`.

## 3. Eligibility (restating the preserved Step 0 findings; no new classification)

| Primary-comparison eligibility | Units |
|---|---|
| YES | 94 |
| YES_WITH_PERIPHERAL_FLAG | 11 |
| NO_SENSITIVITY_ONLY | 5 |
| YES_PROVISIONAL_PENDING_HUMAN_CONFIRMATION | 2 |
| PROVISIONAL_PENDING_P1_HUMAN_CONFIRMATION (STEP0_DERIVED; Step 0 value was YES) | 2 |

Sensitivity-only (not eligible for any primary improvement claim): 5 units (Claude A: R-P03-04, CL-P03-02, CL-P03-03; Claude B: R-P04-05, CL-P04-02). Provisional pending human confirmation: 2 SC-B units (Claude B CL-P04-04, CL-P04-07) and the 2 STEP0_DERIVED core units. Peripheral flags: 13 units.

Dependency propagation (see eligibility register, `propagation_assessment`): {'NONE': 95, 'MATERIAL_DIRECT': 5, 'PERIPHERAL_INHERITED': 11, 'BORDERLINE_INHERITED': 1, 'NOT_APPLICABLE_DERIVED': 2}. No higher-order unit inherits a *material* dependency beyond the five units that are themselves SC-C; the negative stopping decisions SR-P03 (Claude A) and AD-P04 (Claude B) list SC-C configurations among their supported configurations and are recorded as `PERIPHERAL_INHERITED` because each decision would stand without them (Step 0 judgement preserved). CL-P04-07 inherits a borderline dependency from CL-P04-04.

## 4. Descriptive candidate counts (not comparable; not an assessment)

| Cell | Candidate records in the relationship export |
|---|---|
| CODEX_A | 16 records exported (accepted only; the export has no disposition column) |
| CODEX_B | 23 records: {'ACCEPT': 17, 'REJECT': 2, 'DEFER': 4} |
| CLAUDE_A | 34 records: {'ACCEPTED': 19, 'DEFERRED': 7, 'REJECTED': 8} |
| CLAUDE_B | 32 records: {'ACCEPTED': 19, 'DEFERRED': 5, 'REJECTED': 8} |

The four exports follow different candidate-listing policies. **Codex A exported accepted relationships only: missing rejected or deferred candidates are not negative decisions and must not be read as 'considered and rejected'.** These counts must not be read as acceptance rates, effort or merit, and they are kept out of the claim register.

## 5. Normalization fidelity

- **Relations (71):** the normalised text is built mechanically from the record's own fields (actors, relation label as the cell wrote it, modality, condition, statement IDs); Q18 confirms every field value appears in the normalised text. The cell's relation vocabulary is kept (for example Codex 'mandatory_auditor_appointment' and Claude 'Appointment (designation/authorization family)' are not harmonised).
- **Other units (41 original):** normalised by a restatement written by the executor from the cell's own text. Q19 reports lexical coverage (mean 0.84; 6 units below 0.75, listed below). Lexical coverage cannot detect a changed meaning; the executor reread each normalised text against its original at drafting, which is not independent verification.

Units below 0.75 coverage (candidate wording differences to be read by a reviewer):

- S1-073 (CODEX_A TA-P03-CFG-02): coverage 0.72; words absent from the original: concerning, expressed, manufacturer's, monitoring, together. **Manual reading:** Reread: difference is connective wording ('concerning', 'together'); content equals original (audit, report, retained assignment, CS-P03-004 excluded).
- S1-076 (CODEX_A TA-P04-CFG-03): coverage 0.65; words absent from the original: commission's, continuity, describes, escrow-continuity', labels, registry's, registry-escrow, wording. **Manual reading:** Reread: 'continuity' wording is the cell's own (original: 'arrange continuity-preserving custody'); the normalised text additionally marks that the wording is not found in the frozen statements (UPQ-01). This is an added annotation, not a changed claim.
- S1-084 (CODEX_B TB-P04-CFG-03): coverage 0.67; words absent from the original: commission's, described, escrow-continuity', information', labels, registry's, wording. **Manual reading:** Reread: same as TA-P04-CFG-03; the cell's function label 'continuity arrangement and information' is quoted; UPQ-01 annotation added.
- S1-099 (CLAUDE_A SR-P03): coverage 0.40; words absent from the original: actually, applies, decides, highest, regime-level, supported. **Manual reading:** Reread: the normalised text restates the summary-table row (highest level, no architecture claim, no regime decision) and the SR bullet; 'actually supported' echoes the table header, not found in the extracted row.
- S1-100 (CLAUDE_A SR-P04): coverage 0.44; words absent from the original: actually, decides, highest, regime-level, supported. **Manual reading:** Reread: as SR-P03.
- S1-109 (CLAUDE_B CL-P04-07): coverage 0.57; words absent from the original: identifying, outside, positional, providers, registry, selects. **Manual reading:** Reread: the phrase on text outside the frozen statements is an annotation taken from the cell's own uncertainty entry U-27, not a new claim.

## 6. Limitations

- One AI executor, one pass; the normalisation was not independently reviewed; no human assessment was made or simulated.
- The evidence-scope classes are those of Step 0 (preliminary AI-assisted); the 5 SC-C, 2 SC-B, 2 derived-core and central-architecture items still require human adjudication before final comparative scoring.
- External specification not available (waiver in force); the E0–E3 description relayed through ChatGPT is unauthenticated and not mapped.
- Interpretive vocabulary is preserved as the cells wrote it; it is routed to later dimension-D review, not neutralised.
- Uncertainty fields are joined from each cell's own register by explicit ID or by statement and level overlap and may be incomplete or over-inclusive for aggregate units.
- Statement-ID and anchor checks use the local register only.
