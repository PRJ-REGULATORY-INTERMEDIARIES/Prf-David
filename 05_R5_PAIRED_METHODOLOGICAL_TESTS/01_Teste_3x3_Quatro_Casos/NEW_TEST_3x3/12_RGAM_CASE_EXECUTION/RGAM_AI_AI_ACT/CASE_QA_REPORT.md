# CASE_QA_REPORT — RGAM_AI_AI_ACT

Prepared by the case executor at P9 and checked by an independent mechanical validation script (`_work/validate.py`, result in `_work/validate_result.json`) run on the delivered CSV files. The checks below are mechanical and structural; they are not a validation of analytical correctness.

## 1. Required verifications

| # | Verification | Result | Evidence |
|---|---|---|---|
| 1 | Source hash matches the capsule | PASS (MATCH) | SHA-256 of `LEGAL_SOURCE/32024R1689_official_en.xhtml` = `8f0b656302f9864cc87e040c371f209a9d65ae1a6cecc25ca5eb737e872d721a`, equal to `source_sha256` in `CASE_METADATA.json`; W_DECLARATION `hash_match = Y` |
| 2 | Only allow-listed files read | PASS | exact paths in `ACCESS_AND_CONTAMINATION_LOG.md` and RUN_METADATA `files_read`; the one extra file read was the recovery-state note authorised in the launch instruction |
| 3 | No V8 output read | PASS | no V8 path, directory or file was opened, listed or requested |
| 4 | No historical extraction read | PASS | no historical relationship register, pilot or earlier extraction was opened |
| 5 | No other RGAM case result read | PASS | no other capsule or case directory was opened |
| 6 | All records have stable ids | PASS | every id column matches its frozen pattern (`ST-nnnn`, `NA-nnnn`, `PD-nnn`, `QR-nnnn`, `EXT-nnn`, `SC-nn`, `ARCH-nn`, `PROP-nnn`, `CL-nn`, `LNK-nnnnn`, `UNC-nnn`, `HQ-nnn`, `TR-nn`, `DEV-nn`, `RUN-nn`) and is unique within its table; unit ids unique and in source order |
| 7 | Every higher-order claim is vertically traceable (A to S to R/NA/PD to ST to unit to span) | PASS | every ARCH member SC exists; every SC member QR/NA exists; every NA and QR cites at least one existing ST and unit and carries a verbatim span (at most 400 characters) found in a supporting unit or statement unit; every SC, ARCH and PROP has provenance rows; both trace chains (TR-01 seeded draw SC-12, TR-02 largest support ARCH-09) resolve to ids, units and spans (`chain_complete = Y`) |
| 8 | Unsupported claims were rejected or deferred | PASS | examples recorded without invention: Article 89(2) complaint addressee (assignment without counterparty, HQ-DIRECTION); Article 46(1) requester (assignment without counterparty); Article 111(1) bound party (statement only); Article 62(2) fee-setting party (statement only); Article 44(3) appeal forum (no relation); Article 41(5) justification recipient (assignment without counterparty); Article 5(1) prohibitions (bearer at category level, queued) |
| 9 | INDETERMINATE remained available | PASS | 3 of 9 architecture candidates are INDETERMINATE (ARCH-05 combined rule-making, ARCH-07 governance bodies, ARCH-08 biometric identification chain); 5 of 14 properties are undetermined and 1 not_attributable; 2 of 7 closure records are UNDETERMINED |
| 10 | Human-review items not adjudicated | PASS | 35 HUMAN_REVIEW_QUEUE rows; `human_decision`, `human_rationale`, `decided_by`, `decision_date` blank in all rows |
| 11 | Frozen method not altered | PASS | no frozen document was written to (the write scope was the case directory only); convention and gap uses are recorded in PROTOCOL_DEVIATION_LOG (12 entries, GAP-01 to GAP-07 each recorded with `gap_ref`) |

## 2. Data-dictionary integrity rules 1 to 10

| Rule | Statement | Result |
|---|---|---|
| 1 | Every `unit_id` in any table exists in SOURCE_UNIT_INVENTORY; `units_screened` = `units_total` | PASS: 1553 units inventoried, 1553 screened, same order; INSTRUMENT_LEVEL_SUMMARY states 1553 = 1553 |
| 2 | Every NA, PD, QR, EXT cites at least one ST; every ST cites at least one unit; `recital_only = Y` statements have no derived NA/PD/QR | PASS: 251 NA, 71 PD, 281 QR and 59 EXT are each derived from at least one of the 400 statements; no statement is recital-only (0 recital-only statements; all 180 recitals are screened No) |
| 3 | Every `*_ids` and `*_pd_id` field resolves; `accountable_via_qr_ids` resolve to QR records of type accountability | PASS: all referenced PD, QR, NA, SC, EXT, UNC and HQ ids exist; the two relations referenced by `accountable_via_qr_ids` are of type accountability |
| 4 | Every QR has origin and counterpart, modality other than prohibition, no `material_establishment_evidenced` | PASS: 281 relations; 0 with prohibition modality; 0 with material_establishment_evidenced (prohibitions are 21 assignments with `constraint_only = Y`) |
| 5 | Every NA/QR/SC/ARCH/PROP has provenance rows; derived records state `derivation_rule` and cite at least two units or an explicit cross-reference | PASS: 31 derived assignments and 64 derived relations each state a derivation rule and cite at least two units; provenance rows mirror the unit lists of NA, QR, PD and EXT records (4793 rows) |
| 6 | INTEGRATED and OVERLAPPING outcomes have an HQ item; INTEGRATED only if I1-I4 all SATISFIED | PASS: 5 INTEGRATED (all four SATISFIED, each with an HQ-INTEGRATION item), 1 OVERLAPPING_OR_PARTIALLY_INTEGRATED (HQ-OVERLAP), 3 INDETERMINATE, 0 DISTINGUISHABLE |
| 7 | Properties with `closure_dependency = Y` have a resolving `closure_ref`; UNDETERMINED closure forces undetermined status | PASS: 5 closure-dependent properties; the two linked to UNDETERMINED closure records (CL-05, CL-07) are undetermined; at least one COVERAGE row (2 present) |
| 8 | Every EXT is `not_checked` with `outside_corpus_not_expanded` | PASS: 59 of 59 |
| 9 | Human-only columns blank | PASS: 35 of 35 |
| 10 | Trace chains resolve step by step to ids, a unit and an evidence span | PASS: TR-01 and TR-02 |

## 3. Further checks (output schema section 4)

- The 19 CSV tables have headers identical to the blank capsule templates, UTF-8 with BOM, and `CASE_RGAM_REPORT.md` is present; the template copy of the report was replaced.
- Units screened = units inventoried; no QR with prohibition modality; no `material_establishment_evidenced` on relations; every EXT `not_checked`; human columns blank; traceability chains resolve.
- Controlled vocabularies (epistemic status, legal status, modality, relation type, function including the registered tokens, accountability class, ARCH outcome) validated for all NA and QR rows.
- Down-coding rule applied (RGAM-DR-19/20): 9 assignments and 3 relations whose legal effect is conditioned on an unresolved external reference with constitutive dependency are kept at `documented` and flagged in `not_constituted_note` or `support_gap_report`.
- The report and the tables contain no numeric score, composite, threshold, ranking or graph index; counts are descriptors only.

## 4. Known limitations (stated, not resolved)

- Recitals REC34 to REC180 were screened from their opening text and length (DEV-11); this cannot affect records under RGAM-DR-07.
- `property_family` is blank for all 14 properties because the family mapping is outside the allow-list (DEV-10).
- Devices (EU database, AI regulatory sandbox) are used as relation counterparts (DEV-09); function vocabulary tokens and unit-id forms are execution conventions (DEV-05, DEV-08).
- Technical read-deny was not relied on; the allow-list was the control and no read outside it occurred.
- All results are machine-generated and provisional; the I2/I3 thresholds are unvalidated and queued for human review.
