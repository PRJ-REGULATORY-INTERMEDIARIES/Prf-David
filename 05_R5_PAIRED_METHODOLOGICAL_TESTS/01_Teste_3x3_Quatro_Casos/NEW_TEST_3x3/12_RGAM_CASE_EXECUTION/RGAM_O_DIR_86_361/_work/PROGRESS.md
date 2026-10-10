# Progress note
- P0 hash MATCH; units.json (93 units)
- Authored: data_st/p/qr/ext_sc/gov/screen .py ; build.py written
- TODO: run build, validate.py, report/QA/provenance/access log/manifest/gate

## RECOVERY RUN (started 2026-10-07T07:37 -03:00, model claude-sonnet-5-5)
- R0: read brief, recovery note, frozen protocol docs, gap addendum, capsule metadata/readme/source/report template. Source SHA-256 re-verified MATCH (d3f55b...8c57).
- R1: reviewed parse_paras.py, make_units.py, build.py, validate.py: all mechanical (validate.py has 2 vacuous checks, to be replaced/extended).
- NEXT: independent re-parse of source -> compare with units.json; read each table in full (substantive review); extend validate (verify2.py); fix; write report/QA/logs/provenance/manifest/gate.
- R2 (recovery): independent source re-parse check (verify_units.py) PASS; read all 19 tables; validate.py bug fixed; verify2.py added; corrections applied in data_st/data_p/data_gov/build.py (ST-0048 span, NA-0011 derivation, text key leaks, DEV-14/15, RUN row); rebuild OK; validate.py FAILS 0, verify2.py FAILS 0.
- NEXT: write CASE_RGAM_REPORT.md, CASE_QA_REPORT.md, ACCESS_AND_CONTAMINATION_LOG.md, EXECUTION_PROVENANCE.md; final rebuild with RGAM_END_TIME; rerun validate/verify2; manifest (exclude _work), sidecar, CASE_GATE.md
- R3 (recovery): reports written (CASE_RGAM_REPORT, CASE_QA_REPORT, ACCESS log, EXECUTION_PROVENANCE); final rebuild with end_time 2026-10-07T07:45:05-03:00; validate/verify2 FAILS 0. NEXT: CASE_GATE.md, manifest + sidecar, final return.
- R4: CASE_GATE RGAM_CASE_FROZEN; manifest sha256 3dc9add69f04c3a9e5658c0dc90a4a1b5fe6be348e286aae102c4ba8a6c30b1b. DONE.
