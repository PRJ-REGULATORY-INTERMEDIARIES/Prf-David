# ACCESS_AND_CONTAMINATION_LOG — RGAM_C1_SCF

Executor: isolated RGAM case executor (fresh context, no prior case content). Brief: `EXECUTOR_BRIEF.md` in this directory.

## 1. Files read (exact paths)

Read with the Read tool (and, where stated, with shell commands operating only on allow-listed paths):

1. `G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/12_RGAM_CASE_EXECUTION/RGAM_C1_SCF/EXECUTOR_BRIEF.md`
2. `G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/RGAM_PAIRED_EXECUTION_PROTOCOL_v1_0.md`
3. `G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/RGAM_PAIRED_DECISION_RULES_v1_0.md`
4. `G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/RGAM_PAIRED_DATA_DICTIONARY_v1_0.md`
5. `G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/RGAM_CASE_OUTPUT_SCHEMA.md`
6. `G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/RGAM_BLINDNESS_AND_ACCESS_POLICY.md`
7. `G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/RGAM_EXECUTION_GAP_DECISIONS_v1_0.md`
8. `G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_C1_SCF/CASE_METADATA.json` (shell `cat`)
9. `G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_C1_SCF/CAPSULE_README.md` (shell `cat`)
10. `G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_C1_SCF/LEGAL_SOURCE/32023R0955_official_en.html` (SHA-256 by shell; parsed by Python scripts; text portions read through the derived scratch files listed in item 13)
11. `G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_C1_SCF/OUTPUT_TEMPLATES/` — all 19 blank CSV templates and `CASE_RGAM_REPORT_TEMPLATE.md` (shell `cat`; headers also used by the emitting script; `xxd` of one template to check the line-ending convention)
12. Directory listings (`ls -la`) of `.../CAPSULES/RGAM_C1_SCF/`, its `LEGAL_SOURCE/` and `OUTPUT_TEMPLATES/` subdirectories, and of the executor's own output directory `.../12_RGAM_CASE_EXECUTION/RGAM_C1_SCF/`.
13. The executor's own scratch and output files under `G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/12_RGAM_CASE_EXECUTION/RGAM_C1_SCF/` including `_work/tree_dump.txt`, `_work/units_text.txt` (text derived from item 10) and three JPEG images extracted from the embedded Annex I formula images of item 10 (`_work/img/ANX1.pt10_0.jpg`, `ANX1.pt13_0.jpg`, `ANX1.pt15_0.jpg`).

## 2. Shell command categories used (all operating only on allow-listed paths)

- hashing (`sha256sum`) of the controlling source file; `date`;
- directory creation (`mkdir -p`) of `_work/` under the output directory;
- listing (`ls -la`) of the allow-listed capsule directories and the own output directory;
- reading (`cat`, `xxd`) of allow-listed capsule files;
- Python scripts (mechanical only; see `EXECUTION_PROVENANCE.md`) that parse the allow-listed source file, write scratch files and the output tables under the own output directory, check integrity and vocabulary, and generate the report skeleton;
- `grep`, `awk`, `sed` on files under the own `_work/` directory;
- Python version/library probes (`python --version`, `import lxml`, `import bs4`).

No network access, no web browsing, no repository-wide search (no repo-wide grep/glob/find), no memory, CLAUDE.md or settings files, no other directory listing, no git command.

## 3. Attempted or accidental reads outside the allow-list

- **Attempted reads outside the allow-list: NONE.**
- **Accidental exposure to names only (disclosed for completeness):** the invocation context supplied automatically by the harness contained a repository status snapshot with the names of top-level directories and files (including names that appear on the deny-list such as `COMPARATIVE_PILOTS/`, `R4_CROSS_DOMAIN_VALIDATION/`, `V8_COMP_01_2026-10-04/`, `RGAM/`, `Enviados/`, `WORK_2_1/`, `AUDIT_RESEARCH_HISTORY/`), the subjects of five recent commits, and the names of two additional working directories. These were not opened, listed or read by the executor; no content, count, conclusion or output from any of them was seen.
- Technical read-deny status: not verified by the executor (the access policy itself records that it may be inactive and bypassable by shell commands); the allow-list was followed as the primary control.

## 4. Specific attestations

- No V8 output, V8 baseline directory content or V8 vocabulary was read or used.
- No R2/R3/R4 output, no V8-COMP-01 or earlier comparison material, no historical relationship register or pilot output was read.
- No case-selection or ranking material and no other RGAM case directory or result was read.
- No RGAM theory, ontology or manuscript source file was read; the frozen protocol documents were the only method sources.
- The source file was verified by SHA-256 before analysis and matches the capsule metadata.

## 5. Contamination status

**CLEAN** (with the disclosure of section 3: harness-supplied directory and commit-subject names were seen, no content).
