# RGAM family stage - execution QA report

Prepared by the RGAM family assembler (fresh isolated context). Every figure below was recomputed by script from the frozen files on disk at assembly time; nothing was taken from a case executor's own QA statements except where explicitly labelled "as recorded". The checks are structural and mechanical; they do not validate the analytical or legal correctness of any record.

**Overall result: 33 of 33 checks pass; 0 fail.**

## 1. Summary of required verifications

| # | Verification | Result |
|---:|---|---|
| 1 | All four case gates read `RGAM_CASE_FROZEN` | PASS (4 of 4) |
| 2 | Each case freeze manifest recomputed (equals its sidecar) and every listed file hash and byte size valid | PASS |
| 3 | Protocol manifest SHA-256 recomputed = `9ca016b9...5932`, equals sidecar, all 107 listed files valid | PASS |
| 4 | Execution-addendum SHA-256 recomputed = `b9dc184e...2da4` | PASS |
| 5 | Same frozen method referenced by all four cases (RUN_METADATA and EXECUTION_PROVENANCE) | PASS |
| 6 | Legal-source SHA-256 of each capsule equals CASE_METADATA (also capsule register and W_DECLARATION) | PASS |
| 7 | Each case's 19 tables have the frozen headers (data dictionary section 3) | PASS |
| 8 | Data-dictionary integrity rules 1-10 independently recomputed for every case | PASS |
| 9 | Family register counts = recomputed counts | PASS |
| 10 | Combined queue count = sum of case queues; every combined item traces to its case row | PASS (89 = 89) |
| 11 | Human-decision fields blank everywhere (case queues and family queue) | PASS |
| 12 | INSTRUMENT_LEVEL_SUMMARY figures consistent with recomputed counts | PASS |
| 13 | Family assembler isolation | stated in section 9 |

## 2. Protocol and addendum hashes

- Protocol manifest `RGAM_PROTOCOL_FREEZE_MANIFEST.csv`: recomputed SHA-256 `9ca016b97289b39049dc099b265c20662c1ebc05e86bc720f0fbe80e0bac5932`; expected `9ca016b97289b39049dc099b265c20662c1ebc05e86bc720f0fbe80e0bac5932`; sidecar `9ca016b97289b39049dc099b265c20662c1ebc05e86bc720f0fbe80e0bac5932`; files listed 107; files valid 107; invalid none. Status: **OK**. Verification of the 107 listed files required computing the SHA-256 of the files named in the manifest, including files that are not on the assembler's read allow-list (PRECEDENCE register, SOURCE_AUTHORITY register, protocol gate/QA files, capsule files, templates); their bytes were hashed by script and their contents were not read or displayed (see section 9).
- Execution addendum `RGAM_EXECUTION_GAP_DECISIONS_v1_0.md`: recomputed `b9dc184ebc857e5e3aae85ea5e1b5ac28f64c9947086b2bbe763a3b936e02da4`; expected `b9dc184ebc857e5e3aae85ea5e1b5ac28f64c9947086b2bbe763a3b936e02da4`; sidecar `b9dc184ebc857e5e3aae85ea5e1b5ac28f64c9947086b2bbe763a3b936e02da4`. Status: **OK**. The addendum is not itself listed in the protocol manifest (it is a prospective addendum with its own sidecar).

## 3. Case gates and freeze manifests

| Case | Gate (CASE_GATE.md) | Manifest SHA-256 (recomputed) | Equals sidecar | Files listed / valid | EXECUTOR_BRIEF.md listed | `_work/` listed |
|---|---|---|---|---:|---|---|
| RGAM_C1_SCF | RGAM_CASE_FROZEN | `7fd01ed8e0e95616c8dfb836694e00f29c5887f04b24f0f483b2220b15ef3f65` | yes | 25 / 25 | yes | no (excluded) |
| RGAM_C2_CBAM | RGAM_CASE_FROZEN | `84647523b5800816b7d56279383cbbfaaeea95296765e7e171e2329dafe6e096` | yes | 25 / 25 | yes | no (excluded) |
| RGAM_AI_AI_ACT | RGAM_CASE_FROZEN | `160217c11f2cf5e70f22a3eb527ac916cb460ce3d9c70a313ae91160e5e15372` | yes | 25 / 25 | yes | no (excluded) |
| RGAM_O_DIR_86_361 | RGAM_CASE_FROZEN | `3dc9add69f04c3a9e5658c0dc90a4a1b5fe6be348e286aae102c4ba8a6c30b1b` | yes | 25 / 25 | yes | no (excluded) |

The orchestrator audit lists the same four manifest hashes (`7fd01ed8...`, `84647523...`, `160217c1...`, `3dc9add6...`). Each case directory contains, beside the manifested files, only the manifest, its sidecar and an unlisted `_work/` scratch folder (not opened by the assembler). `EXECUTOR_BRIEF.md` is listed in each case manifest (25 files per case).

## 4. Same frozen method across cases

| Case | RUN_METADATA protocol_version and manifest hash | EXECUTION_PROVENANCE names manifest hash and addendum | RUN_METADATA files_read lists the six method documents | Method-document hashes cited in provenance equal recomputed |
|---|---|---|---|---:|
| RGAM_C1_SCF | PASS | PASS | PASS | 0 of 6 |
| RGAM_C2_CBAM | PASS | PASS | PASS | 6 of 6 |
| RGAM_AI_AI_ACT | PASS | PASS | PASS | 6 of 6 |
| RGAM_O_DIR_86_361 | PASS | PASS | PASS | 0 of 6 |

Recomputed SHA-256 of the six method documents: RGAM_PAIRED_EXECUTION_PROTOCOL_v1_0.md `084d96da502afde0...`; RGAM_PAIRED_DECISION_RULES_v1_0.md `1dd0e47064b24fb5...`; RGAM_PAIRED_DATA_DICTIONARY_v1_0.md `db77af669c1d676b...`; RGAM_CASE_OUTPUT_SCHEMA.md `40659fc0889b3bde...`; RGAM_BLINDNESS_AND_ACCESS_POLICY.md `89f2159373123c48...`; RGAM_EXECUTION_GAP_DECISIONS_v1_0.md `b9dc184ebc857e5e...`. The C2_CBAM and AI_AI_ACT provenance files list the six document hashes and they equal the recomputed values; the C1_SCF and O_DIR_86_361 provenance files state the protocol manifest hash without listing per-document hashes, and each of those cases records (as the others do) that the manifest hash was taken from the execution addendum, not recomputed by the executor (the manifest file was outside the executors' allow-list). The assembler recomputed it (section 2).

## 5. Legal-source hashes

| Case | Recomputed SHA-256 of capsule LEGAL_SOURCE | Equals CASE_METADATA, capsule register, W_DECLARATION |
|---|---|---|
| RGAM_C1_SCF | `cf8c60fc233311436dfdd3ee236d0c8399eda55fea174610e91b5594f84a0408` | PASS |
| RGAM_C2_CBAM | `c47e2793e7b92333ce9a891aba18924ff21b15b2745fffda98348b04b15a770e` | PASS |
| RGAM_AI_AI_ACT | `8f0b656302f9864cc87e040c371f209a9d65ae1a6cecc25ca5eb737e872d721a` | PASS |
| RGAM_O_DIR_86_361 | `d3f55bd448695b2a5e2c5f9f9167f7f5027c9a80c609a80072439756e80d8c57` | PASS |

Only the byte hash of each LEGAL_SOURCE file was computed; the files were not opened or read.

## 6. Table headers

For each case all 19 CSV tables were compared with the field lists of `RGAM_PAIRED_DATA_DICTIONARY_v1_0.md` sections 3.1-3.19 (the frozen header definition; the capsule `OUTPUT_TEMPLATES/` are outside the assembler's allow-list and were not read; the dictionary states the templates are generated identically).

| Case | Header mismatches | Ragged rows | Files without UTF-8 BOM |
|---|---|---|---|
| RGAM_C1_SCF | none | none | none |
| RGAM_C2_CBAM | none | none | none |
| RGAM_AI_AI_ACT | none | none | none |
| RGAM_O_DIR_86_361 | none | none | none |

## 7. Data-dictionary integrity rules 1-10 (independent recomputation)

Rules checked: (1) unit ids exist, screened = inventoried; (2) every NA/PD/QR/EXT/ST traces to statements and units, recital_only handling; (3) id references resolve and `accountable_via_qr_ids` point to accountability relations; (4) every QR has origin and counterpart, no prohibition modality, no material_establishment_evidenced; (5) provenance rows exist and derived records state a rule and cite two units or a cross-reference; (6) INTEGRATED/OVERLAPPING architecture candidates are queued and INTEGRATED requires I1-I4 SATISFIED; (7) closure-dependent properties resolve and UNDETERMINED closure forces `undetermined`; (8) every EXT is `not_checked` and `outside_corpus_not_expanded`; (9) HQ human columns blank; (10) trace chains resolve.

| Case | Failures found |
|---|---:|
| RGAM_C1_SCF | 0 |
| RGAM_C2_CBAM | 0 |
| RGAM_AI_AI_ACT | 0 |
| RGAM_O_DIR_86_361 | 0 |

The assembler's check does not re-verify evidence spans against the legal source text (the source files were not read); that verification is recorded by each case executor in its own CASE_QA_REPORT.md (as recorded).

## 8. Family files: internal consistency

- family_register: PASS - register rows 4; mismatches against recomputed table/stratum/HQ counts: none
- family_queue: PASS - combined queue rows 89 = sum of case queues 89 (19, 16, 35, 19); every item traced to its case row (all original columns identical): untraceable none; family ids unique: True; recurring_category_label non-empty for all: True
- human_family: PASS - family queue rows 89; non-blank human cells 0

| Case | INSTRUMENT_LEVEL_SUMMARY record_counts entries checked | Mismatches against recomputed rows |
|---|---:|---|
| RGAM_C1_SCF | 15 | none |
| RGAM_C2_CBAM | 13 | none |
| RGAM_AI_AI_ACT | 17 | none |
| RGAM_O_DIR_86_361 | 15 | none |

The combined queue (`RGAM_FAMILY_HUMAN_REVIEW_QUEUE.csv`) preserves every case-level item as its own row (no merging, collapsing or adjudication); it carries the original 12 columns unchanged, plus `family_hq_id`, `trigger_category` (copy of `trigger_code`), `recurring_category_label` (assembler-assigned descriptive label), `source_file`, `source_row_number` and `source_row_sha256`. The register file stores the E/P/R/S/A stratum mapping in its header comment lines.

### 8.1 Observations on the frozen case files (reported, not corrected; no frozen file was modified)

- O_DIR_86_361: DEV numbering cited in `EXECUTION_PROVENANCE.md` (trace-generator choice "logged DEV-14"), `CASE_QA_REPORT.md` section D (C5) and `CASE_GATE.md` (corrections "logged (DEV-15)") does not match the PROTOCOL_DEVIATION_LOG rows (trace-selection convention is DEV-13; recovery run is DEV-14; evidence-span convention is DEV-15).
- C2_CBAM: `INSTRUMENT_LEVEL_SUMMARY.record_counts` lists 13 of the 19 tables; the other cases list different subsets. All listed numbers equal the recomputed counts.
- AI_AI_ACT `RUN_METADATA.model_parameters` records reasoning effort as NOT_EXPOSED while C1_SCF, C2_CBAM and the O_DIR_86_361 recovery run record `reasoning_effort=10` as displayed in their invocation context.
- C2_CBAM: `PROTOCOL_DEVIATION_LOG` rows carry `gap_ref` GAP-01 on two rows and GAP-02 as an examined-not-used entry; O_DIR_86_361 has no GAP-02 row (its QA report states the gap did not arise).
- CASE_GATE.md formatting differs (bold token in C1_SCF, AI_AI_ACT and O_DIR_86_361; plain token in C2_CBAM); all contain the token `RGAM_CASE_FROZEN` on a line of its own.

## 9. Family assembler isolation statement

**Read in full or in part with the Read tool or shell (content seen):** the assembler brief (`_orchestrator/FAMILY_ASSEMBLER_BRIEF.md`); from `11_RGAM_PROTOCOL_FREEZE/`: `RGAM_CASE_OUTPUT_SCHEMA.md`, `RGAM_EXECUTION_GAP_DECISIONS_v1_0.md`, `RGAM_BLINDNESS_AND_ACCESS_POLICY.md`, `RGAM_EXECUTION_CAPSULE_REGISTER.csv`, `RGAM_PAIRED_DATA_DICTIONARY_v1_0.md`, the two SHA-256 sidecar files, `RGAM_PROTOCOL_FREEZE_MANIFEST.csv` (first lines, grep of the rows for the six method documents and CASE_METADATA files, and parsed in full by script for hash verification), and the four `CAPSULES/<id>/CASE_METADATA.json`; `_orchestrator/ISOLATION_AUDIT_SUMMARY.md`; in each of the four case directories the 19 schema tables (by scripts, plus targeted printing of HUMAN_REVIEW_QUEUE, PROTOCOL_DEVIATION_LOG, INSTRUMENT_LEVEL_SUMMARY, RUN_METADATA), `ACCESS_AND_CONTAMINATION_LOG.md`, `EXECUTION_PROVENANCE.md`, `CASE_QA_REPORT.md`, `CASE_GATE.md`, the two manifest files, and `CASE_RGAM_REPORT.md` (headings and keyword lines by grep only; not read in full).

**Hashed by script only (bytes read for SHA-256; content not read or displayed):** the four `LEGAL_SOURCE` files; the files listed in the protocol manifest that are not named above (this includes `RGAM_PAIRED_EXECUTION_PROTOCOL_v1_0.md` and `RGAM_PAIRED_DECISION_RULES_v1_0.md`, which are on the allow-list but were not read, and files outside the allow-list such as the PRECEDENCE register, SOURCE_AUTHORITY register, protocol gate and QA files, capsule READMEs and output templates).

**Names only (directory listings; contents not opened):** a listing of `12_RGAM_CASE_EXECUTION/` (parent of the case directories) exposed the names of the `_RECOVERY_*` folders and the orchestration log file, which are on the do-not-read/do-not-list list; a listing of `11_RGAM_PROTOCOL_FREEZE/` and of `CAPSULES/` exposed names of non-allow-listed protocol files; a recursive file enumeration of the four case directories was filtered to drop `_work/` paths before display, so only the existence of each `_work/` folder was seen (its contents were not opened or displayed). The harness also supplied, with the invocation, a repository status snapshot listing top-level folder and file names (including names on the deny-list), the subjects of recent commits and the names of two additional working directories; none was opened.

**Not done:** no V8 material, no R2/R3/R4/V8-COMP-01 or historical or pilot material, no case-selection or ranking material, no `_RECOVERY_*` content, no orchestration-log content, no memory, CLAUDE.md or settings file, no web access, no repository search; no frozen file was modified; writes were made only under `12_RGAM_CASE_EXECUTION/FAMILY/` (including a `_work/` scratch folder of assembly scripts, excluded from the family manifest). The assembler did not read executor transcripts; statements about executor access rest on the case access logs and the orchestrator's non-substantive audit summary.

**Answer to "read anything outside the allow-list": no file content outside the allow-list was read; the name-only exposures and byte-hashing listed above are disclosed as deviations from a strict reading of the brief.**
