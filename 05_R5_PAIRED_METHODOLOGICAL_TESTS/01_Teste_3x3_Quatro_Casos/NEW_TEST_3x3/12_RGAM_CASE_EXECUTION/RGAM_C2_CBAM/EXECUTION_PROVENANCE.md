# EXECUTION_PROVENANCE — RGAM_C2_CBAM

| Item | Value |
|---|---|
| Case id | RGAM_C2_CBAM |
| Method version | RGAM paired execution protocol v1.0 (decision rules v1.0, data dictionary v1.0, output schema v1.0, blindness policy v1.0, execution gap decisions v1.0) |
| Protocol manifest SHA-256 | `9ca016b97289b39049dc099b265c20662c1ebc05e86bc720f0fbe80e0bac5932` — as stated in `RGAM_EXECUTION_GAP_DECISIONS_v1_0.md` (it is not stated in the capsule metadata or README; the manifest file itself is outside the allow-list and was not read) |
| Model | `claude-sonnet-5-5` (Sonnet 5.5), as stated in the session context |
| Reasoning/effort setting | `reasoning_effort=10` as displayed in the session context; the brief asked for the highest available effort, which was not settable by the executor |
| Temperature, top-p, seed, token limits | NOT_EXPOSED |
| Start (UTC) | 2026-10-06T19:03:42Z |
| End of table construction / P9 (UTC) | 2026-10-06T19:43:24Z (RUN_METADATA.end_time) |
| End of case documentation (UTC) | 2026-10-06T19:43:25Z |
| Fresh context attested | Y (isolated executor; only the brief, the allow-listed documents and the capsule were read) |
| Source SHA-256 | `c47e2793e7b92333ce9a891aba18924ff21b15b2745fffda98348b04b15a770e` (MATCH with capsule) |

## Hashes of the frozen inputs at the end of the run

- `RGAM_PAIRED_EXECUTION_PROTOCOL_v1_0.md`: `084d96da502afde0cf654f51220d2876aed6780be8040bd2c2003346b187d32d`
- `RGAM_PAIRED_DECISION_RULES_v1_0.md`: `1dd0e47064b24fb520e4c226c1634701820c4b17876fe5f947305f108fc0b141`
- `RGAM_PAIRED_DATA_DICTIONARY_v1_0.md`: `db77af669c1d676b95ab5553a77466bf7cbb9dcf0b6c56d8420b4b3d349d6278`
- `RGAM_CASE_OUTPUT_SCHEMA.md`: `40659fc0889b3bde59748f8a8793104769586abe6547fbf562d1fbad04dc9c97`
- `RGAM_BLINDNESS_AND_ACCESS_POLICY.md`: `89f2159373123c48e181e3ae30f44063030d316837a3393d07ee1f2cf1fb6097`
- `RGAM_EXECUTION_GAP_DECISIONS_v1_0.md`: `b9dc184ebc857e5e3aae85ea5e1b5ac28f64c9947086b2bbe763a3b936e02da4`
- capsule `CASE_METADATA.json`: `d0770e56a920e09e983d2aeca7df8c0f96d36a976d5fca8882cefc326f8ddad6`
- capsule `CAPSULE_README.md`: `4be13b29f43d208c08e849d72f079c436eeebd83018f67b9794468fa051cd949`
- capsule `LEGAL_SOURCE/32023R0956_official_en.xhtml`: `c47e2793e7b92333ce9a891aba18924ff21b15b2745fffda98348b04b15a770e`

## Scripts used (mechanical work only; all in `_work/`)

- `dump_struct.py` (exploratory structure outline of the source file), `parse_units.py` (split the source file into addressable units, compute text hashes and ids), `cov_check.py` (compare every source paragraph with the parsed units), `rgam_lib.py` (record containers and mechanical id/legal-status helpers), `check1.py` (span and key checks), `build.py` (id assignment, derivation of mechanical columns, CSV writing, integrity checks), `make_report.py` and `make_docs.py` (assemble report and QA text from the finished tables).
- The analytical records (statements, normative assignments, positions and devices, relations, external references, subconfigurations, architecture candidates, properties, closure statements, uncertainties, queue items, deviation entries and screening notes) were written by the executor from its own reading of the unit text in the data files `rec_01_pd.py`, `rec_02_ch1.py`, `rec_03_ch2.py`, `rec_04_ch3.py`, `rec_05_ch4_6.py`, `rec_06_ch7_11.py`, `rec_07_annex.py`, `rec_86_ext_more.py`, `rec_85_screening.py`, `rec_80_sc_arch.py`, `rec_82_prop.py`, `rec_90_hq_unc.py`; the scripts serialize them and apply rules stated in the frozen protocol (legal status from the act's own application schedule; down-coding of records with constitutive external dependencies; seeded draw for traceability), not keyword or pattern rules.
- No script derives any analytical record from keywords or patterns.

## Other facts

- Reference date for legal status: 2026-01-01 (executor selection from Article 36(2); queued, HQ-OTHER).
- Trace selection: seed = 3296602003 (first 8 hex digits of the source SHA-256); candidate list and draw in TRACE_DEMONSTRATIONS.csv.
