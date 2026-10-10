# Recovery log

## 2026-09-30

1. Inspected `RUN_LOG.md`, `RUN_CONFIG.md`, `ISSUES_AND_DECISIONS.csv`, `INPUT_MANIFEST.csv`, directory contents and file timestamps. Confirmed that `STATUS.md` and `OUTPUT_MANIFEST.csv` are absent.
2. Identified the late R08 first-pass CSVs and the empty blind-pass output. Copied all 29 R08 files into `01_RECOVERED_DATA/R08_AS_FOUND/`; SHA-256 equality is recorded in `R08_RECOVERY_MANIFEST.csv`.
3. Located Rotem's reply, the original and revised codebooks, Chart Key, implemented workbook, David manuscript, official legal texts, and PILOT_03 decision and build files. Registered their SHA-256 hashes in `SOURCE_REGISTER.csv`.
4. Checked the four priority cases and one optional actor–action–recipient case against original official-act text. Selected 16 short provision/activity excerpts for the workbook; every excerpt appears in the archived legal text.
5. Rechecked PILOT_03's 19 unique `HUMAN_ADJUDICATED` rows, 14 retrospective-impact flags, and final historical gate. Verified the A/B build scripts. No historical decision was changed.
6. Built the 10-sheet English technical attachment. Omitted the R08 Cartesian-context error interpretation and any reliability claim from scripted A/B outputs.
7. Ran workbook QA and SHA-256 continuity checks. See `02_VALIDATION/WORKBOOK_QA.md` and `VALIDATION_LOG.md`.

Only the new `CODEX_ROTEM_SHARE_PACKAGE_20260930_2153/` directory contains deliverables. No email was sent. No historical file was edited.
