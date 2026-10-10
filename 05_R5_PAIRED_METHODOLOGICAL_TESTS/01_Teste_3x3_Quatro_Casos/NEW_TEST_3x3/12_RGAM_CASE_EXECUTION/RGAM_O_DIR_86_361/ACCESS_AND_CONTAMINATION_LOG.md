# ACCESS_AND_CONTAMINATION_LOG — RGAM_O_DIR_86_361 (recovery run)

Base path abbreviation: `NT3` = `G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3`. This log covers the **recovery executor** (model `claude-sonnet-5-5`, session started 2026-10-07T07:37:48-03:00). The accesses of the **earlier, interrupted executor** are not logged by it (no ACCESS log existed when it stopped) and are covered by the orchestrator's transcript audit; the recovery executor makes no claim about them.

## 1. Files read (Read tool), exact paths

Allow-listed method and brief files
1. `NT3/12_RGAM_CASE_EXECUTION/RGAM_O_DIR_86_361/EXECUTOR_BRIEF.md`
2. `NT3/12_RGAM_CASE_EXECUTION/_RECOVERY_DIR_86_361_2026-10-06/RECOVERY_STATE_NOTE.md` (the single extra file permitted for this recovery run; nothing else in the `_RECOVERY` directory was opened, listed or modified)
3. `NT3/11_RGAM_PROTOCOL_FREEZE/RGAM_PAIRED_EXECUTION_PROTOCOL_v1_0.md`
4. `NT3/11_RGAM_PROTOCOL_FREEZE/RGAM_PAIRED_DECISION_RULES_v1_0.md`
5. `NT3/11_RGAM_PROTOCOL_FREEZE/RGAM_PAIRED_DATA_DICTIONARY_v1_0.md`
6. `NT3/11_RGAM_PROTOCOL_FREEZE/RGAM_CASE_OUTPUT_SCHEMA.md`
7. `NT3/11_RGAM_PROTOCOL_FREEZE/RGAM_BLINDNESS_AND_ACCESS_POLICY.md`
8. `NT3/11_RGAM_PROTOCOL_FREEZE/RGAM_EXECUTION_GAP_DECISIONS_v1_0.md`

Own capsule
9. `NT3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_O_DIR_86_361/CASE_METADATA.json`
10. `NT3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_O_DIR_86_361/CAPSULE_README.md`
11. `NT3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_O_DIR_86_361/LEGAL_SOURCE/31986L0361_official_en.html`
12. `NT3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_O_DIR_86_361/OUTPUT_TEMPLATES/CASE_RGAM_REPORT_TEMPLATE.md` (the 19 CSV templates were read only by the mechanical scripts for their header rows)

Own output directory `NT3/12_RGAM_CASE_EXECUTION/RGAM_O_DIR_86_361/`
13. the earlier executor's tables, read in full: `INSTITUTIONAL_STATEMENTS.csv`, `POSITIONS_AND_DEVICES.csv`, `NORMATIVE_ASSIGNMENTS.csv`, `QUALIFIED_RELATIONS.csv`, `EXTERNAL_REFERENCES.csv`, `SUBCONFIGURATIONS.csv`, `ARCHITECTURE_CANDIDATES.csv`, `PROPERTY_REGISTER.csv`, `CLOSURE_REGISTER.csv`, `HUMAN_REVIEW_QUEUE.csv`, `PROTOCOL_DEVIATION_LOG.csv`, `UNCERTAINTY_LOG.csv`, `INSTRUMENT_LEVEL_SUMMARY.csv`, `W_DECLARATION.csv`, `UNIT_SCREENING.csv` (SOURCE_UNIT_INVENTORY, PROVENANCE_LINKS and TRACE_DEMONSTRATIONS were examined by scripts, not read line by line)
14. `_work/PROGRESS.md`, `_work/units_view.txt`, `_work/parse_paras.py`, `_work/make_units.py`, `_work/build.py`, `_work/validate.py`; fragments of `_work/data_st.py`, `_work/data_p.py`, `_work/data_gov.py` and `_work/data_ext_sc.py` were displayed by `grep`/`sed` while locating text to correct
15. the recovery executor's own files written in this run (see section 3)

## 2. Shell command categories used (all restricted to allow-listed paths)

- hashing: `sha256sum` of the legal source;
- parsing/verification scripts run with Python on allow-listed paths only: `verify_units.py` (re-parse of the source against `units.json`), `validate.py`, `verify2.py`, `build.py` (mechanical assembler; reads `_work/data_*.py`, `units.json`, the capsule metadata, source and template headers);
- text edits by Python/`sed` of own `_work` files and of `CASE_QA_REPORT.md`;
- directory listings with `Get-ChildItem -Recurse` of exactly two directories: the own capsule directory and the own output directory (both allow-listed); no parent directory and no other directory was listed;
- `date`, `ls` of `_work/`, `cp` of own CSV files to a scratch copy (see section 4), `cmp` between own CSV files, checksum/manifest generation under the own output directory.

No repository-wide grep/glob/find, no web access, no external retrieval, no memory, CLAUDE.md or settings file reads, no subagent.

## 3. Files written

Only under `NT3/12_RGAM_CASE_EXECUTION/RGAM_O_DIR_86_361/`: regenerated CSV tables (by `build.py` after the corrections listed in CASE_QA_REPORT.md section D), `_work/verify_units.py`, `_work/verify2.py`, `_work/validate.py` (edited), `_work/data_st.py`, `_work/data_p.py`, `_work/data_gov.py`, `_work/build.py` (edited), `_work/PROGRESS.md`, `_work/validation_output.txt`, `_work/verify2_output.txt`, `_work/build_info.json`, `CASE_RGAM_REPORT.md`, `CASE_QA_REPORT.md`, this log, `EXECUTION_PROVENANCE.md`, `CASE_FREEZE_MANIFEST.csv`, `CASE_FREEZE_MANIFEST_SHA256.txt`, `CASE_GATE.md`. No protocol, capsule, template or `_RECOVERY` file was modified.

## 4. Attempted or accidental accesses outside the allow-list

None attempted and none accidental, with one disclosed housekeeping deviation: before the corrections, the recovery executor copied the earlier executor's 19 CSV tables from the own output directory to the session scratchpad directory (`C:/Users/Adm/AppData/Local/Temp/claude/g--Meu-Drive-PRJ-David-Prf-David/dbdf310e-f382-4879-8c7a-974aa54f3953/scratchpad/pre_fix/`) in order to compare before and after the rebuild. This is a write outside the brief's write path; the copy contains only the case's own output and no external material, and it was deleted after the comparison. The same scratchpad directory was listed once (`ls`) to confirm the deletion; it contained four unrelated pre-existing files (`csv_scan.txt`, `dump.py`, `scan.py`, `xl.py`) that were not opened, read or modified.

## 5. Observations on content seen

The only analytical material seen was the case's own earlier output and the frozen method. No V8 output, R2/R3/R4 output, historical relationship extraction, selection or ranking material, other RGAM case result, V8-COMP-01 material or RGAM theory/ontology/manuscript source file was requested or seen.

## 6. Contamination status

**CLEAN** (for the recovery executor's accesses; the earlier executor's accesses are covered by the orchestrator's transcript audit and are not asserted here).
