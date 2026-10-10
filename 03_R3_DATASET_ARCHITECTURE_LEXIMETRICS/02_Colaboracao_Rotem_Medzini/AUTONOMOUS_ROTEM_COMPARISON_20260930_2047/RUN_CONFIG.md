# RUN_CONFIG — AUTONOMOUS_ROTEM_COMPARISON_20260930_2047

| Item | Value |
|---|---|
| Run ID | `AUTONOMOUS_ROTEM_COMPARISON_20260930_2047` |
| Run root (absolute) | `G:/Meu Drive/PRJ-David/Prf-David/AUTONOMOUS_ROTEM_COMPARISON_20260930_2047/` |
| Project root (verified) | `G:/Meu Drive/PRJ-David/Prf-David/` (git repo, branch `main`, HEAD `ef3a14c` "R4 complete") |
| Started | 2026-09-30 20:47 (local, America/Sao_Paulo per system clock; no TZ string exposed by `date`) |
| Executing agent | Claude Code session, model `claude-opus-5-5` (Opus 5.5), single executing agent. One context-isolated sub-session of the same model family used only for the R08 blind second pass (see `08_DUAL_CODING/INTERNAL_REVIEW_LOG.md`). Three read-only exploration sub-sessions (same model family) were used during planning to locate sources; their findings were re-verified in this run before use. |
| Operational round IDs | R00–R12 (this run). **Not** to be confused with historical project rounds R1, R2, R2.1, R3, R4.x, PILOT_01–03 (see `11_SYNTHESIS/FINAL_REPORT.md` §2 for the mapping). |
| Master instruction | "PROMPT MESTRE — REEXECUÇÃO AUTÔNOMA, EM RODADAS, DA COMPARAÇÃO METODOLÓGICA COM ROTEM" (pasted by the user; a copy is also in `C:/Users/Adm/Downloads/PROMPT_MESTRE_REEXECUCAO_AUTONOMA_ROTEM_OPUS.md`) + "ATUALIZAÇÃO DE ESTADO — INCORPORAR AO PROTOCOLO MESTRE" (delta, 15 points, pasted by the user in the same session). |

## Permissions actually exercised
- READ: project files; a closed list of named files in `C:/Users/Adm/Downloads/` (codebook versions, Chart Key, R1/R2 reports, learning log, PILOT_03 filled adjudication CSV); official EU texts via the Publications Office Cellar endpoint (`http://publications.europa.eu/resource/celex/{CELEX}`, content negotiation `Accept: text/html`, `Accept-Language: eng`).
- WRITE: only inside this run root.
- NOT DONE (by design): no modification of any original; no git stage/commit/push/reset (the repository index already had ~1,141 staged deletions and 14 untracked top-level entries **before** this run — pre-existing user state, left untouched); no e-mail sent (only `EMAIL_DRAFT_EN.md`); no publication; no production authorisation; no human adjudication created.

## Environment capabilities (verified 2026-09-30)
| Capability | Status |
|---|---|
| Python | 3.14.4 |
| python-docx / openpyxl / pandas / PyMuPDF / pypdf / lxml | present (1.2.0 / 3.1.5 / 3.0.2 / 1.27.2.3 / 6.14.0 / 6.1.0) |
| pdfplumber, PyPDF2 | absent |
| pandoc | 3.9.0.2 |
| PowerShell 7 / Git Bash | present |
| EUR-Lex HTML front-end (`eur-lex.europa.eu/legal-content/...`) | **blocked** for scripted access (HTTP 202, empty body — bot challenge) |
| Publications Office Cellar (`publications.europa.eu/resource/celex/...`) | **works** (HTTP 200, full HTML text of the act) |

## Status vocabularies used in this run
- `EVIDENCE_STATUS`: `VERIFIED_LOCAL`, `VERIFIED_OFFICIAL_URL`, `SECONDARY_ONLY`, `HYPOTHETICAL`, `MISSING`.
- Coding provenance: `MODEL_CODED` (first pass by the executing agent), `MODEL_BLIND_SECOND_PASS` (context-isolated same-model pass), `MODEL_REVIEWED` (executing agent reconciliation), `HUMAN_ADJUDICATED` (**only** for pre-existing human decisions verified in files), `ROTEM_IMPLEMENTED` (verbatim from Rotem's workbook), `INTERPRETIVE_APPLICATION` (our application of Rotem's written codebook where her workbook has no value).
- Source status (delta §2): `UNREVISED_BASELINE` for the unrevised codebook and the Chart Key.
- Schema layer (delta §4–6): `LAYER_1_CONCEPTUAL` (Rotem's e-mail), `LAYER_2_DOCUMENTED` (codebooks + Chart Key), `LAYER_3_IMPLEMENTED` (workbook); alignment states `PRESENT_AND_IMPLEMENTED`, `DESCRIBED_BUT_NOT_IMPLEMENTED`, `IMPLEMENTED_BUT_NOT_EXPLICITLY_DESCRIBED`, `NOT_FOUND`; initial divergence class `DOCUMENTATION_IMPLEMENTATION_GAP`.
- Recommendation vocabulary: `NO_CHANGE_NEEDED` / `NO_CHANGE_RECOMMENDED`, `CLARIFICATION_ONLY`, `OPTIONAL_FIELD`, `NEW_SUBORDINATE_TABLE`, `UNRESOLVED`; PILOT_03 diagnostic outcomes `ROTEM_SCHEMA_SUFFICIENT`, `CLARIFICATION_NEEDED`, `OPTIONAL_EXTENSION_USEFUL`, `STRUCTURAL_EXTENSION_NEEDED`.
- Gates per round: `PASS`, `PASS_WITH_LIMITATIONS`, `BLOCKED`. Run gate: one of `COMPARATIVE_PACKAGE_READY`, `READY_WITH_LIMITATIONS`, `BLOCKED_BY_MISSING_SOURCES`, `INTERNAL_QA_FAILED`, `CONFLICT_WITH_HUMAN_ADJUDICATION`. Additional delta gate: `GATE_DOCUMENTARY_RECONCILIATION` (PASS / `FINAL_WITH_DOCUMENTED_LIMITATIONS`).

## Round dependency map
```
R00 ─► R01 ─┬─► R02 (R1 history) ─► R03 (R2 corpus) ─► R04 (R3→R4.2D) ─┐
            ├─► R05 (PILOT_03 audit + regression) ─────────────────────┤
            └─► R06 (codebook layers) ─► R07 (case selection) ─► R08 (dual coding + blind pass)
                                                                    │
                                   R09 (7 axes) ◄───────────────────┘◄─┘
                                   R10 (sensitivity/adversarial)
                                   GATE_DOCUMENTARY_RECONCILIATION
                                   R11 (synthesis) ─► R12 (final QA, index, manifests)
```
R02–R05 (history) do not block R06–R08 (contemporary comparison); both must be complete before R11.
