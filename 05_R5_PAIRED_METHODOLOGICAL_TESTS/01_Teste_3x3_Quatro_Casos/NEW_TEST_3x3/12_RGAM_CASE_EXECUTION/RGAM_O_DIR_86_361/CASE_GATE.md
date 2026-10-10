# CASE_GATE — RGAM_O_DIR_86_361

**RGAM_CASE_FROZEN**

Factual basis (recovery run, 2026-10-07):
- Source SHA-256 of `LEGAL_SOURCE/31986L0361_official_en.html` re-verified: MATCH with `CASE_METADATA.json` (`d3f55bd448695b2a5e2c5f9f9167f7f5027c9a80c609a80072439756e80d8c57`).
- Coverage complete: 93 units inventoried and 93 screened; structure check MATCH (12 articles, 0 annexes).
- The 19 frozen-schema CSV tables plus `CASE_RGAM_REPORT.md` are present with frozen headers; data-dictionary integrity rules 1-10 pass (validate.py and verify2.py: 0 failures); the 19 QA checks of the recovery specification pass (CASE_QA_REPORT.md).
- Corrections made by the recovery executor are listed in CASE_QA_REPORT.md section D and logged (DEV-15); no substantive record was added or removed.
- No external retrieval; all EXT records not_checked; human-review queue populated and not adjudicated (human_* columns blank).
- Contamination status: CLEAN (recovery executor); the earlier executor's accesses are covered by the orchestrator's transcript audit.
- No method or source failure; case-specific analytical difficulties are recorded as uncertainties and queued, not as grounds for blocking. The instrument-level result INDETERMINATE and all outputs are machine-generated and provisional.
