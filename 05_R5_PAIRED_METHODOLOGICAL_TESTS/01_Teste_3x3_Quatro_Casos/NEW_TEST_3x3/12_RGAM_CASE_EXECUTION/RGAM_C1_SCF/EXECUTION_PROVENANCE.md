# EXECUTION_PROVENANCE — RGAM_C1_SCF

## 1. Run identity
- Case id: RGAM_C1_SCF (Regulation (EU) 2023/955, CELEX 32023R0955).
- Method version: RGAM paired execution protocol v1.0 (decision rules v1.0, data dictionary v1.0, case output schema v1.0, blindness and access policy v1.0) with the execution-gap decisions addendum v1.0 (GAP-01..07).
- Protocol manifest SHA-256: `9ca016b97289b39049dc099b265c20662c1ebc05e86bc720f0fbe80e0bac5932` as stated in `RGAM_EXECUTION_GAP_DECISIONS_v1_0.md`; the capsule files do not state it (the manifest file itself was not provided to the executor and was not read).
- Source SHA-256 verified: `cf8c60fc233311436dfdd3ee236d0c8399eda55fea174610e91b5594f84a0408` (MATCH with `CASE_METADATA.json`).

## 2. Model and parameters (as observed)
- Model identifier: `claude-sonnet-5-5` (stated in the invocation context as "Sonnet 5.5").
- Reasoning/effort setting: the invocation context displayed `reasoning_effort = 10`; the brief asked for the highest available effort, but the displayed setting could not be changed by the executor; the setting is therefore recorded as displayed.
- Temperature: NOT_EXPOSED. Top-p: NOT_EXPOSED. Seed: NOT_EXPOSED. Token limits: NOT_EXPOSED (a remaining context-token counter of about 15 000 000 was displayed at the start; it is not a configured limit).
- Fresh context attested: yes (no prior case content; no memory or CLAUDE.md read).

## 3. Times (local time, UTC-03:00)
- Start (first recorded command): 2026-10-06T15:19:41-03:00.
- Record tables and report generated: 2026-10-06T15:59:29-03:00 (RUN_METADATA end_time).
- Documentation files and freeze manifest completed after 2026-10-06T16:00:33-03:00 (time of writing this file).

## 4. Method trail
P0 hash verification; P1 structure parse (706 units) and coverage check; P2 screening of every unit in source order; P3 statements, assignments, positions and devices, relations, external references; P4 dependency, support-gap and accountability passes; P5 subconfigurations from relations; P6 I1-I4 assessment of three candidate wholes; P7 properties with bearer, scale and aggregation; P8 closure tests; P9 profile, trace demonstrations by the fixed rule, human-review queue, integrity checks; stop. Human adjudication (MS section 8.4(8)) is outside machine execution and was not performed.

## 5. Scripts used (all in `_work/`; mechanical work only)
| Script | Purpose | Analytical content created? |
|---|---|---|
| `parse_probe.py`, `dump_tree.py`, `build_units.py`, `coverage_check.py` | parse the allow-listed source file into addressable units (ids, text, hashes), dump structure, check that every text node of the source is contained in a unit, extract embedded images | No |
| `reg.py` | helper library: id assignment, key-to-id resolution, verbatim-span validation (every evidence span must be a substring of a cited unit and at most 400 characters), CSV helpers | No |
| `rec_a1_statements.py`, `rec_a2_statements.py`, `rec_a3_statements.py`, `rec_b_pd.py`, `rec_c_na.py`, `rec_d_qr.py`, `rec_e_ext.py`, `rec_f_sc_arch.py`, `rec_g_unc_hq.py`, `rec_h_screen.py` | **data-entry files**: the analytical records (statements, positions and devices, assignments, relations, external references, subconfigurations, candidates, properties, closure statements, uncertainties, queue items, deviations, screening notes) written by the executor from its own reading of the unit text; Python is used only as the container and for span/id validation. Two wrapper functions (`N` in `rec_c_na.py`, `Q` in `rec_d_qr.py`) fill boilerplate defaults (validity note, support-gap text, constitution-effect wording by modality) and apply the status-ceiling rule recorded as DEV-12: `legal_constitution_evidenced` only for direct records in force with no unresolved constitutive external reference (the choice of direct versus derived and of the external-dependency set is the executor's per-record decision), otherwise `documented`. | Records are authored by the executor, not derived by rules from keywords or patterns |
| `assemble.py` | mechanical assembly: resolves keys to ids, computes derived-record links, reverse queue and uncertainty pointers, provenance links, descriptive tallies, the seeded trace selection and chain text, and writes the 19 CSV tables with the frozen headers (UTF-8 with BOM, CRLF) | No (derivations are mechanical cross-links) |
| `check.py`, `vocab_check.py` | integrity rules 1-10, structural checks and controlled-vocabulary checks of the emitted tables | No |
| `generate_report.py` | composes `CASE_RGAM_REPORT.md` from the emitted tables | No |

The trace-selection rule of RGAM-DR-29 was implemented mechanically: seed = integer value of the first 8 hexadecimal digits of the source SHA-256 (`cf8c60fc` = 3482083580); the eligible candidates are the subconfigurations and candidate architectures citing units from at least two parts of the instrument (sorted by id); the seeded draw uses Python `random.Random(seed).choice` over that sorted list; the second trace is the candidate with the largest number of distinct supporting units.

## 6. Output files
19 CSV tables with the frozen headers, `CASE_RGAM_REPORT.md`, `CASE_QA_REPORT.md`, `ACCESS_AND_CONTAMINATION_LOG.md`, this file, `CASE_GATE.md`, `CASE_FREEZE_MANIFEST.csv` and `CASE_FREEZE_MANIFEST_SHA256.txt`. The blank templates were not left in the output directory: the populated tables replace them with identical headers (verified by the checker).
