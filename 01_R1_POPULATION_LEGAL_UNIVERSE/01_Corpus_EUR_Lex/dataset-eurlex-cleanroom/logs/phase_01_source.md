# Phase 01 — Source acquisition

All three acts were downloaded fresh via `scripts/acquire_source.py`,
using CELEX-based content negotiation against the EUR-Lex / Publications
Office CELLAR repository (`Accept: application/xhtml+xml`,
`Accept-Language: eng`). Each request was verified to resolve to an
official `publications.europa.eu` CELLAR document with content-type
`application/xhtml+xml` before any file was written; the script aborts
(`[STOP]`) otherwise. No previous project's XHTML files were reused.

| case | CELEX | resolved CELLAR document | bytes | SHA256 |
|---|---|---|---|---|
| case_01 | 32021R1119 | `cellar/365a2e8e-e04f-11eb-895a-01aa75ed71a1.0006.03/DOC_1` | 151943 | `8bbe15af032af1a3950cf1e42bead62e0c816afbf56dced883ececb604da6075` |
| case_02 | 32023R0956 | `cellar/e5587bf5-f383-11ed-a05c-01aa75ed71a1.0006.03/DOC_1` | 496976 | `c47e2793e7b92333ce9a891aba18924ff21b15b2745fffda98348b04b15a770e` |
| case_03 | 32023R1115 | `cellar/d80446fe-0660-11ee-b12e-01aa75ed71a1.0006.03/DOC_1` | 387997 | `fc30a30a1b6701800ad8abeb63e1d606769a4128bc97ddb2e481ee4bf6057259` |

Acquisition timestamps (UTC): 2026-09-09T01:44:52 / 01:44:53 / 01:44:54.

Each case's full provenance record is in
`cases/case_0N/source/source_manifest.yaml`. Files on disk:
`cases/case_0N/source/act_official.xhtml`.

State: `setup → source_acquired`.
