# CASE_QA_REPORT — RGAM_O_DIR_86_361 (recovery run; machine-generated and provisional)

Scope: independent verification, by the recovery executor, of the 19 analytical tables produced by the earlier (interrupted) executor, against the frozen legal source and the frozen method (protocol v1.0, decision rules, data dictionary, output schema, execution-gap addendum). Verification scripts (mechanical only; they read the emitted CSVs, `units.json` and the frozen source and generate no analytical content): `_work/validate.py` (35+ checks including dictionary rules 1–10), `_work/verify2.py` (29 supplementary checks), `_work/verify_units.py` (independent source-coverage check). Final results: validate.py FAILS 0; verify2.py FAILS 0; verify_units.py: all 93 units found in source order and the only residual source text is article headings, the `*****` separator and numbering labels. Outputs are kept in `_work/validation_output.txt` and `_work/verify2_output.txt` (scratch folder, outside the manifest).

## A. The 19 QA checks of the final-recovery specification

| # | Check | Result | Basis |
|---:|---|---|---|
| 1 | Source hash MATCH | PASS | `sha256sum` of `31986L0361_official_en.html` = `d3f55bd448695b2a5e2c5f9f9167f7f5027c9a80c609a80072439756e80d8c57` = `CASE_METADATA.json`; also recomputed inside build.py and validate.py; W_DECLARATION `hash_match = Y` |
| 2 | Every unit inventoried | PASS | 93 units; source re-parsed independently (verify_units.py): unit texts occur in source order and exhaust the body text apart from headings, separator and numbering labels; 12 articles and 0 annexes match the neutral metadata; `text_sha256` recomputes; verbatim substring of the normalized source body |
| 3 | Every unit screened | PASS | UNIT_SCREENING has 93 rows, same ids and order as the inventory; `governance_relevance = Yes` iff statements are listed; INSTRUMENT_LEVEL_SUMMARY `units_total = units_screened = 93` |
| 4 | Frozen headers unchanged | PASS | all 19 headers identical to the capsule templates (read from `OUTPUT_TEMPLATES/`); UTF-8 BOM present; exactly 19 CSV files plus the report |
| 5 | Stable IDs unique | PASS | ST/NA/PD/QR/EXT/SC/ARCH/PROP/CL/UNC/HQ ids unique within table and follow the frozen patterns; LNK ids unique; DEV-nn and RUN-nn as specified |
| 6 | All ID references resolve | PASS | every `*_ids`, `*_pd_id`, `bearer_id`, `closure_ref`, `record_refs`, `dependent_record_ids`, `supporting_record_ids`, `affected_claim_ids` field resolves; reciprocity between INSTITUTIONAL_STATEMENTS.derived_record_ids and the statement_ids of NA/QR holds |
| 7 | Evidence spans supported by the cited unit | PASS (after correction C1) | for ST, NA, QR and PD, every `evidence_span` is non-empty, at most 400 characters and a verbatim substring of at least one cited unit (checked per unit, not on the concatenation) |
| 8 | Every QR has valid origin and counterpart | PASS | all 39 QR carry `origin_pd_id` and `counterpart_pd_id` resolving to PD records; additional parties resolve; no QR rests on a recital |
| 9 | No counterparty invented | PASS | all 20 NA have `counterpart_status = NONE_IDENTIFIABLE` and a blank counterpart; the parties of every QR were re-read in the cited unit (A2(8), A3, A4, A5, A6(2), A7, A8, A9, A11); relations whose actor or recipient the text does not state (A6(1) subparagraph 2 publication; A7(2) last sentence; A7(4)(a) information duties) were not coded as relations and are queued (HQ-DIRECTION) |
| 10 | No prohibition is a QR | PASS | no QR has modality `prohibition`; the single prohibition (A6(2) no further tests) is NA-0006 with `constraint_only = Y` |
| 11 | Derived records state derivation | PASS (after correction C2) | 7 QR and 5 NA are `derived`; each states a derivation rule and cites at least two units or an explicit cross-reference; direct records carry a blank derivation_rule |
| 12 | Every S has configurational warrant | PASS | all six S state pattern rule, governance question, QR members, organizing mechanism, warrant basis (grounded in cross-references or explicit conditions, not chapter/vocabulary/theme), boundary and competing grouping; `default_status = S` |
| 13 | Every A applies I1–I4 | PASS | ARCH-01 and ARCH-02 state I1, I2, I3, I4 with statuses, rival grouping, boundary sensitivity and `anticircularity_sequence_followed = Y`; both outcomes INDETERMINATE with stated basis |
| 14 | INTEGRATED/OVERLAPPING A queued for human review | PASS (vacuous) | no ARCH outcome is INTEGRATED or OVERLAPPING; both are INDETERMINATE and are nevertheless queued (HQ-016, HQ-017); an INTEGRATED outcome would require all four statuses SATISFIED (checked) |
| 15 | Human-decision fields blank | PASS | `human_decision`, `human_rationale`, `decided_by`, `decision_date` blank in all 19 HQ rows |
| 16 | Every higher-order claim vertically traceable | PASS | A → S → QR/NA/PD → ST → unit → verbatim span resolves for every S and ARCH member (every member QR/NA has statement ids; every statement cites units and a verbatim span); PROVENANCE_LINKS has rows for every ST/PD/NA/QR/EXT/SC/ARCH/PROP and mirrors `supporting_unit_ids`; TR-01 and TR-02 chains contain every member QR/NA of the traced candidate and resolve to units and spans; selection recomputed independently (seed 3556072404; eligible ARCH-01, ARCH-02, SC-01, SC-02, SC-03, SC-05, SC-06; drawn SC-05; largest support ARCH-02) |
| 17 | External sources not retrieved | PASS | no web or external access; all 10 EXT `not_checked` and `outside_corpus_not_expanded`; the four EXT with constitutive dependency make the dependent claims `undetermined` or restricted to the declared corpus |
| 18 | No V8/historical output accessed | PASS | see ACCESS_AND_CONTAMINATION_LOG.md: the recovery executor read only allow-listed paths; the earlier executor's accesses are covered by the orchestrator's transcript audit |
| 19 | Frozen method unchanged | PASS | no protocol, dictionary, rule, schema or template file was written; method gaps were handled only through the execution addendum (GAP-01 to GAP-07) and logged in PROTOCOL_DEVIATION_LOG |

## B. Data-dictionary integrity rules 1–10

| Rule | Result |
|---:|---|
| 1 unit ids exist in the inventory; units screened = units total | PASS (every unit_id column of every table, including `units_spanned` text; 93 = 93) |
| 2 NA/PD/QR/EXT cite ≥1 ST; every ST cites ≥1 unit; recital_only=Y has no derived records | PASS (no ST rests on a recital unit; all `recital_only = N`; PD and EXT cite statements through `derived_record_ids`, the tables carrying no statement_ids column for them) |
| 3 id fields resolve; accountable_via_qr_ids point to accountability QR | PASS (QR-0025, QR-0027, QR-0028, QR-0032, QR-0033, QR-0034 point to QR-0026, the only accountability relation) |
| 4 every QR has origin and counterpart, modality ≠ prohibition, no material_establishment_evidenced | PASS |
| 5 every NA/QR/SC/ARCH/PROP has provenance rows; derived records state a rule and cite ≥2 units or a cross-reference | PASS (after C2) |
| 6 INTEGRATED/OVERLAPPING have an HQ item; INTEGRATED only if I1–I4 all SATISFIED | PASS (vacuous: both outcomes INDETERMINATE) |
| 7 PROP with closure_dependency Y has a resolving closure_ref; closure UNDETERMINED forces PROP undetermined | PASS (PROP-012 and PROP-013 undetermined; PROP-011 depends on an asserted-within-corpus closure) |
| 8 every EXT not_checked and outside_corpus_not_expanded | PASS |
| 9 HQ human columns blank | PASS |
| 10 TRACE vertical_chain resolves to existing ids, units and spans | PASS |

## C. Brief-specific confirmations

- Only allow-listed files were read (see ACCESS_AND_CONTAMINATION_LOG.md). No V8 output, no historical extraction, no other RGAM case result was read.
- All records have stable ids; unsupported claims were rejected or deferred (relations without an identifiable origin or counterparty; feedback consequence from A8(4) to A6 not asserted; no instance inferred from a type; no external relation admitted).
- INDETERMINATE remained available and was used (both ARCH outcomes; instrument-level result). NO_ARCHITECTURE_WARRANTED and DISTINGUISHABLE were considered and not asserted: the S-level groupings are warranted from stated relations, and a DISTINGUISHABLE outcome requires sufficient coverage, which unresolved constitutive external references prevent.
- Human-review items were not adjudicated; the machine recommendation columns are provisional.
- Execution-addendum uses are logged with `gap_ref`: GAP-01 (DEV-01, DEV-03), GAP-03 (DEV-05), GAP-04 (DEV-06), GAP-05 (DEV-07), GAP-06 (DEV-08, token `NON_OPERATIVE_SOURCE_GAP`), GAP-07 (DEV-09); GAP-02 did not arise (no provision of W amends another act). Tokens `FUNCTION_VOCABULARY_UNRESOLVED` (one NA, two QR) and `NON_OPERATIVE_SOURCE_GAP` were used only as the addendum prescribes.
- External-reference handling: references resolved inside W (Article 2(8), Article 7, Article 8(1)-(2), Article 4, Article 5) are supporting units and derivation rules, not EXT (GAP-03); amending-act EXT was not needed.

## D. Corrections and reviews made by the recovery executor (nothing repaired silently)

| Ref | What | Why | Nature |
|---|---|---|---|
| C1 | ST-0048 `evidence_span` shortened from 410 to under 400 characters by dropping the leading words "the certificate of conformity issued by the approved laboratory which has carried out the tests " (the span still starts at "must be accompanied by the data…" and is verbatim from A7.P3; the bearer remains in the statement summary and in NA-0010's span) | frozen dictionary limit of 400 characters | mechanical; trace TR-01/TR-02 text regenerated accordingly |
| C2 | NA-0011 `derivation` changed from `derived` to `direct` (derivation rule blank) | a derived record needs ≥2 units or an explicit cross-reference (dictionary §1 DERIV, rule 5); the permission and its conditions are stated in one unit (A7.P4.ptb), so no multi-provision derivation exists | minimal reading of the same unit; recorded in DEV-15 |
| C3 | Four fragments of internal authoring keys removed from prose: PROPERTY_REGISTER PROP-009 and PROP-010 `inference_rule`; UNCERTAINTY_LOG UNC-018 `effect_on_claims`; PROTOCOL_DEVIATION_LOG DEV-09 `impact` | output hygiene (keys such as `a4_cept` leaked into text); wording replaced by references to the supporting records | mechanical |
| C4 | `validate.py` fixed: it looked up `statement_ids` in EXTERNAL_REFERENCES (a column that table does not have) and crashed; EXT now checked through INSTITUTIONAL_STATEMENTS.derived_record_ids; two vacuous placeholder checks neutralized by the independent checks of `verify2.py` (V3, V14) | the script had never been run | mechanical |
| C5 | DEV-14 and DEV-15 added to PROTOCOL_DEVIATION_LOG; RUN_METADATA rewritten to describe the recovery run | honesty about the trace-selection procedure (generator and meaning of "part" not fixed by the frozen text) and about the recovery | documentation |
| R1 | Reviewed and retained without change: the ACCOUNTABILITY class with sufficiency `indeterminate` and missing elements for QR-0026 (queued HQ-004); the definition-derived QR-0001/QR-0002 under GAP-07 (queued HQ-011); the INDETERMINATE reading of RGAM-DR-25 for both candidates (DEV-11, HQ-016); the status-ceiling rule (DEV-12, HQ-015) | each is a documented, queued, conservative reading of a gap; changing them would substitute the recovery executor's preference for a human decision | review |

Record counts and all substantive records (statements, assignments, positions, relations, external references, subconfigurations, architecture candidates, properties, closure rows, uncertainties, queue items) are unchanged by the corrections.

## E. Residual limitations

Machine-generated and provisional; the same model family produced and re-verified the analysis, so this QA is not inter-coder reliability. The recovery executor could not recover the earlier executor's reading notes; the independence of the verification rests on re-reading each unit against each record, not on a second blind coding. The reasoning-effort setting displayed to the recovery executor was not the highest setting requested in the brief (see EXECUTION_PROVENANCE.md).
