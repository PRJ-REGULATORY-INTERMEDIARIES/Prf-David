# NEW TEST 3x3 — EXECUTION LOG

Append-only. Times are local (UTC-03:00) on 2026-10-05.

## 1. Setup
- 20:12 Workspace confirmed: `NEW TEST 3x3/` (empty at start; folder name is upper-case "NEW TEST 3x3" in the repository). Subfolders 00_PROTOCOL … 05_SELECTION_FREEZE, LOGS created.
- Git state at start: branch main, many untracked directories; no git write operation performed (commit/push/reset/branch not used).

## 2. Directories inspected (read-only)
Repository root listing; Before_R2/ (dataset-eurlex, dataset-eurlex-cleanroom, Estudos Preliminares e testes, Inputs, Exercício Dataset); R4_CROSS_DOMAIN_VALIDATION/ (incl. 01_baseline/R3_ORIGINAL, R3_HISTORY_STAGING, 02_sources, 03_extraction, 08_reports); ENVIO_R4_TO_DAVID/; RELATIONAL_LEXIMETRICS_PILOT/PILOT_01–03; AUTONOMOUS_ROTEM_COMPARISON_20260930_2047/07_CASE_SELECTION; CODEX_ROTEM_SHARE_PACKAGE_20260930_2153/; WORK_2_1/; RGAM/pilot/GDPR_PILOT_01 (extraction CSVs and design only); COMPARATIVE_PILOTS/V8_COMP_01_2026-10-04 (pointer files only); Enviados/Email 01; RELATORIOS_DE_ESTADO_DO_PROJETO; RESEARCH_CLOSEOUT_2026-10-01.md. Full CSV header/row scan: 518 CSV files catalogued (scratch scan, not stored in project).

## 3. Pre-registration
- Pre-registration written BEFORE ranking/selection: `00_PROTOCOL/TEST_3X3_PRE_REGISTRATION.md`
- SHA-256 at registration: `23bb989a6451dad966ca9570ac8adf12a8cd6a7c71d4426cf5e1144ae2e328a1`
- CASE_SELECTION_PROTOCOL.md and NON_CIRCULARITY_RULES.md written immediately after.

## 4. Source files used for metrics (read-only; SHA-256 of every file in `01_CASE_UNIVERSE/CASE_SOURCE_PROVENANCE.csv`)
- R3: `R4_CROSS_DOMAIN_VALIDATION/01_baseline/R3_HISTORY_STAGING/PRJ-DAVID-R3/R3_CLEANROOM/{04_actor_register/ACTOR_REGISTER.csv, 05_law_intermediary/LAW_INTERMEDIARY_REGISTER.csv, 06_relations/RELATIONS_ADJUDICATED.csv, 06_relations/NEGATIVE_BOUNDARY_CASES.csv, 02_corpus/R3_CORPUS_VALIDATION_REGISTER.csv, 12_audits/R3_PHASE_6_INTERMEDIATION_AUDIT.md}`; workbook `R3_ORIGINAL/final_package/REGULATORY_INTERMEDIATION_ARCHITECTURE_CASE_STUDY_DATASET.xlsx`; `ENVIO_R4_TO_DAVID/12_ARCHIVE_SUPPORT/R4_R3_RECONCILIATION.csv` (all PASS).
- R2: `Before_R2/dataset-eurlex/cases/final_human_review_v2/*`, `cases/case_0N/primary_coding/*.json`, `03_human/stage4_attempt_02/ra_4way/RA_4way_comparison.csv`, `methodology/codebook.md`, `docs/methodology/PRODUCTION_CHANGELOG.md`, `Enviados/Email 01/DATASET_EURLEX_RIT_FINAL_FOR_DAVID.xlsx`.
- PoC: `Before_R2/Estudos Preliminares e testes/PoC 01/Entrega-04/data/*`, `Entrega-02/data/rit_relationships_v3.csv`, `v1/PoC/data/rit_coded_sample{,_v2}.csv`.
- PILOT: `RELATIONAL_LEXIMETRICS_PILOT/PILOT_01/03_PILOT_DATA/RELATIONSHIP_OBSERVATIONS.csv`, `PILOT_02/02_CODING_A/RELATIONSHIPS_CODER_A.csv`, `PILOT_03/{03_SOURCE_PROVISIONS,04_MODEL_A,05_MODEL_B,01_PROTOCOL,06_ONTOLOGY_TESTS}/*`, `PILOT_03/99_REPRODUCIBILITY/PILOT_03_MANIFEST_FINAL.json`.
- R4: `ENVIO_R4_TO_DAVID/{03_SOURCE_DATA_AND_CORPUS,04_R4_2_STRUCTURAL_EXTRACTION,01_FINAL_R4_DATASET}/*`, `R4_CROSS_DOMAIN_VALIDATION/R4_2_METHOD_NOTE.md`.
- GDPR_PILOT_01 (extraction layer only): `RGAM/pilot/GDPR_PILOT_01/03_EXTRACTION/{QUALIFIED_RELATIONS,NORMATIVE_ASSIGNMENTS,POSITIONS_AND_DEVICES}.csv`, `00_PROTOCOL/{RESEARCH_DESIGN,DECISION_RULES}.md`.
- Rotem: `RELATIONAL_LEXIMETRICS_PILOT/PILOT_01/00_SOURCES/dataset_of_EU_regulatory_intermediation.xlsx`; `CODEX_ROTEM_SHARE_PACKAGE_20260930_2153/03_WORKBOOK/ROTEM_PILOT_RESULTS_SUMMARY.xlsx`; `AUTONOMOUS_ROTEM_COMPARISON_20260930_2047/{06_CODEBOOK/CODEBOOK_VERSION_DIFF.md, 07_CASE_SELECTION/CASE_REGISTER.csv, 01_BASELINES/BASELINE_R4_EXTRACTION_DSA_ART21_22_37_42.csv}`.
- Pointer-only (no metric taken): V8_COMP_01 inventory / selection memo / MDR, DSA, Lei 13.848 READMEs.

## 5. Definitions recovered
R3 three-condition gate; R2 production codebook v1.0 + changelog v1.1/v1.2 (five conditions; v1.2 decisions 1–2 broaden I to comitology/advisory input); PoC RIT_CODEBOOK_v4; PILOT_03 CODING_RULES_V0_3_ADJUDICATED and derivation rules; Rotem REV (via CODEBOOK_VERSION_DIFF); RGAM decision rules; R4.2 method note. Common operational denominator found (decision D1) → §7 stop rule not triggered. See `02_COMPARABILITY/METRIC_DEFINITION_REGISTER.md`.

## 6. Decisions made
- D1 common denominator = relational R–I–T test (shared in wording by R3, R2, PoC; applied differently).
- D2 Rotem/RGAM/R4 metrics are off-denominator (C4/C5).
- D3 no reconciliation of R2 vs R3 gate application (needs new interpretation) → separate strata (G4).
- D4 canonical version of the Climate Law = R3 frozen (G5); R2 Climate Law versions retained as duplicates and used only as the bridge.
- D5 Final comparability gate = COMPARABILITY_CONDITIONAL_PASS (stratum S1 only).
- D6 Domains assigned before ranking from titles/objectives; Level-1 = distinct domain for diversity.
- D7 Ranking run on S1 only; diversity constraint fails (2 Level-1 domains) → NO FREEZE; final gate TEST_3X3_SELECTION_BLOCKED.

## 7. Exclusions (all recorded in CASE_UNIVERSE_MASTER.csv; none silent)
5 eligible; 2 conditionally eligible (CBAM, EUDR — stratum S2); 19 non-comparable studied instruments (4 PoC, 10 PILOT, 3 R4, P2B, CDSM); 3 insufficient source (Taxonomy, MDR, Lei 13.848); 41 duplicate/version rows; 101 Rotem-only rows (external dataset, never studied in a pilot); 2 prohibited V8-stage items (not opened).
Diversity-constraint exclusions: Climate Law (rank 3), ETS (rank 4), MSR (rank 5), all D01.

## 8. Harmonizations (HARMONIZATION_REGISTER.csv; 48 rows)
Used: R3 regulators/targets recount (C2); Climate-Law bridge. Computed, not used: R3 alternates, R2 triple-unit/actor recounts, PILOT_03 Model B recount. Not harmonizable: R2 relation census, R2 gate application, H-R2-PROXY (considered and rejected), R4/GDPR/Rotem metrics. No original value overwritten.

## 9. Uncertainties
- Bridge rests on one shared instrument (Climate Law).
- R2 final relation file reconstructed from a corrupted working file (06_PROVENANCE).
- R2 label-level parsing for sensitivity recounts.
- Domain ambiguity: SCF (D02 vs D01), CBAM (D03 vs D01), EUDR (D01 vs D03).
- Rotem docx not re-read directly.
- Counts were visible to the agent in aggregate reports before the pre-registration was written (disclosed in §11 of the pre-registration).

## 10. Script note
`LOGS/scripts/compute_metrics.py` (recounts) → `build_universe.py` (master, provenance, comparability, harmonization) → `build_ranking.py` (domain classification, ranking, diversity test). All read-only on sources. `metrics_computed.json` and `ranking_result.json` are intermediate outputs. A first run of the R2 label parser kept role annotations in labels (regex defect); it was corrected before any table was used and the tables were regenerated.

## 11. Hashes of controlling outputs (SHA-256, computed after the final build)
18195c4fd4a517ac9ee8d661c6f4defaa3451e08071a640ed3352aba18ed1ae7  00_PROTOCOL/CASE_SELECTION_PROTOCOL.md
4ca8a2039a4f176948211d2fbc56abfc57d1ebeca2893a1743462109869bf0bb  00_PROTOCOL/NON_CIRCULARITY_RULES.md
23bb989a6451dad966ca9570ac8adf12a8cd6a7c71d4426cf5e1144ae2e328a1  00_PROTOCOL/TEST_3X3_PRE_REGISTRATION.md
7e47e9d016e30c447631208abb659609cbf07ba5ee0ca2016e05d318bc8d45c2  01_CASE_UNIVERSE/CASE_SOURCE_PROVENANCE.csv
094550b930dd38fce6a5b060a9754a26b2db07dc89926087bfa4740c051abfca  01_CASE_UNIVERSE/CASE_UNIVERSE_MASTER.csv
40771321cff3ce2da195fcde7bed2ecf19eed51ea90fbea68b5a89a3d3aab8ff  01_CASE_UNIVERSE/CASE_UNIVERSE_NOTES.md
dce6cbfd34c577a3ee6c4ff57e5c99b2ad8b231660331261102d639fa39d46f4  02_COMPARABILITY/CASE_METRIC_COMPARABILITY.csv
99b85ca43e7ed7fa09e0e014cd157463671ae5c6819313e2520c8353cac3ba76  02_COMPARABILITY/COMPARABILITY_AUDIT_REPORT.md
ca1a8086ebaf1339bb2a955a14e1c0ca8954912c30762aed6b7dd0aaed7c329b  02_COMPARABILITY/HARMONIZATION_REGISTER.csv
31473de6561c00abecd25b811d5896d13a51af1d8ade5a0203db089cdcf44b3d  02_COMPARABILITY/METRIC_DEFINITION_REGISTER.md
173a1eb2af5918d2ca7d212f5dec76802e2c38506066951e460cc74a463c5a68  03_DOMAIN_CLASSIFICATION/CASE_DOMAIN_CLASSIFICATION.csv
15d612f34c4e3660146370cdfd3ae01575d7c2487507fd8f28769ea146c35046  03_DOMAIN_CLASSIFICATION/DOMAIN_TAXONOMY.md
3bf68709ef6af7680d3e3c775c752acc7162ca45d50ab7cff411363e55ca7057  04_RANKING_AND_SELECTION/CONTINGENT_OPTIONS_NOT_SELECTION.csv
a365891b3f8e9bfd115bb319210f27a0dbbf47c0bd3e5a07ba783bc653e43fd4  04_RANKING_AND_SELECTION/DOMAIN_CASE_RANKING.csv
250b6e4185c8b77b3697d4ae6899b7e7321c242e944839b120387a98da625af7  04_RANKING_AND_SELECTION/GLOBAL_CASE_RANKING.csv
096b2379c3b12d0b1339fd801d088a2f1ad01967b5e9bcf16a5fd5c0f23674b2  04_RANKING_AND_SELECTION/THREE_CASE_SELECTION_DECISION.md
b4783e7eb6cd3eca073732c44ba8077fc92c913668db57a98368cae8d86c075a  05_SELECTION_FREEZE/README_NO_FREEZE.md
5cfd86452a3b157fa55b3d6d67bbf6ce953bb00cebe48478e9e50d058733f90d  LOGS/scripts/build_ranking.py
ae0ce558396a247be8caa8a8f721228055c89773bf75b7149ccbace7397a6f71  LOGS/scripts/build_universe.py
efe5568b457e919b9021f82951ef0eebcf203f2bbcc603d1355bdf9b22b4f90a  LOGS/scripts/compute_metrics.py
5cdba71e03641df446bc53ea95883e38eda1652fb5e1041d030320cc6fb148a0  LOGS/scripts/metrics_computed.json
183ebb6a6ee7d1d02469b5ecfc2b133599a94c094ff9cc0985d49cf1e9f8317c  LOGS/scripts/ranking_result.json

(This log itself is not hashed here because it is appended to after hashing.)

## 12. Final state
Final gate: `TEST_3X3_SELECTION_BLOCKED / METHODOLOGICAL_REVIEW_REQUIRED`. V8 not started. No git operation performed. Awaiting Igor's decision (Option C / P / B / D in `04_RANKING_AND_SELECTION/THREE_CASE_SELECTION_DECISION.md`).
