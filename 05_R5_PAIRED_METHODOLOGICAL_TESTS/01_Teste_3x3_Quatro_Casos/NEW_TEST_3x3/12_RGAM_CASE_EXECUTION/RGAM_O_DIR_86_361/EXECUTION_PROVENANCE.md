# EXECUTION_PROVENANCE — RGAM_O_DIR_86_361

## 1. Nature of the run

This case was frozen by a **recovery run** that reused the partial work of an earlier executor.

- **Earlier executor (interrupted).** Started 2026-10-06T20:47:08-03:00 (its own record); last file write 2026-10-06T21:11:05-03:00; stopped by an API rate limit. It produced: the parsing scripts (`parse_paras.py`, `make_units.py`), `units.json` (93 units), the authored analytical source files (`data_st.py`, `data_p.py`, `data_qr.py`, `data_ext_sc.py`, `data_gov.py`, `data_screen.py`), the mechanical assembler `build.py`, all 19 populated CSV tables, `validate.py` (written, never run) and `PROGRESS.md`. It produced no report, QA report, access log, provenance file, manifest or gate. Per the orchestrator's recovery-state note the counts were provisional and nothing was validated.
- **Recovery executor (this run).** Model `claude-sonnet-5-5` (displayed as Sonnet 5.5). Start 2026-10-07T07:37:48-03:00; end 2026-10-07T07:45:05-03:00 (analytical completion; manifest generation follows). Fresh sub-context with no content from any other case, V8 or historical material; it did inherit the earlier executor's own output for this same case, which it was instructed to reuse and verify.

## 2. What was reused and what was independently verified

Reused as the starting state: the parsed unit file, the authored analytical records (statements, positions and devices, assignments, relations, external references, subconfigurations, architecture candidates, properties, closure rows, uncertainties, queue items, deviation entries, screening notes) and the mechanical assembler.

Independently verified by the recovery executor from the frozen legal source and the frozen method: source SHA-256 (MATCH); source-unit inventory completeness (independent re-parse check); frozen headers; unique stable ids; resolution of every id reference; verbatim evidence spans against each cited unit; vertical traceability; relation admission (both parties, no invented counterparty, no prohibition as a relation, no material_establishment_evidenced on relations); derivation rules; explicit configurational warrant for every S; I1–I4 and rival grouping for every A; queue coverage; blank human columns; coverage; logged use of the execution addendum. Every analytical table was read in full against the source text (see ACCESS_AND_CONTAMINATION_LOG.md).

Corrected (details in CASE_QA_REPORT.md section D): one evidence span above 400 characters (ST-0048); one derivation label (NA-0011, derived → direct); four fragments of internal authoring keys in prose; a crash in `validate.py`; two deviation entries (DEV-14, DEV-15) and a rewritten RUN_METADATA row added. No record was added or removed; record counts are unchanged.

## 3. Executor settings (as observable)

| Item | Value |
|---|---|
| Model identifier | `claude-sonnet-5-5` (Sonnet 5.5), as stated in the session environment |
| Reasoning/effort | the session context displayed `reasoning_effort = 10` (scale not stated); this is not the highest available effort that the brief asks for; no other effort display was available |
| Temperature, top-p, seed | NOT_EXPOSED |
| Token limits | NOT_EXPOSED as a model parameter (a total token budget of about 15 million was displayed; it is not recorded as a parameter) |
| Tools used | Read, Write, Edit, Bash (Git Bash), PowerShell, Glob/Grep not used on the repository; no subagent; no web |
| Method version | RGAM paired execution protocol v1.0 with decision rules v1.0, data dictionary v1.0, output schema v1.0 and execution-gap addendum v1.0 |
| Protocol manifest SHA-256 | `9ca016b97289b39049dc099b265c20662c1ebc05e86bc720f0fbe80e0bac5932` as stated in the execution-gap addendum (the capsule files themselves do not state it; it is not independently re-computed here because the manifest file is outside the allow-list) |

## 4. Scripts (mechanical only; none generates an analytical record)

| Script | Role | Author |
|---|---|---|
| `_work/parse_paras.py`, `_work/make_units.py` | split the source file into paragraphs and units; hash unit texts | earlier executor |
| `_work/build.py` | resolves authoring keys to stable ids, derives unions, links and tallies, selects trace demonstrations by the fixed rule, writes the 19 CSVs | earlier executor; run metadata block rewritten by the recovery executor |
| `_work/data_*.py` | the authored analytical records, kept as Python data (analytical content, not mechanics); three files edited in the recovery run as listed in CASE_QA_REPORT.md | earlier executor; minimal edits by the recovery executor |
| `_work/validate.py` | schema and integrity checks of data-dictionary rules 1–10 and vocabularies | earlier executor; one mechanical bug fixed by the recovery executor |
| `_work/verify_units.py`, `_work/verify2.py` | independent source-coverage and supplementary integrity checks | recovery executor |

Review of `validate.py` before running: it opens the emitted CSVs, the template headers, `units.json` and the source, and performs only header, referential-integrity, vocabulary, verbatim-span and consistency checks; it generates no statement, relation or judgment. Its crash (nonexistent `statement_ids` column in EXTERNAL_REFERENCES) was a mechanical error and was fixed without changing any substantive rule.

## 5. Trace-demonstration selection

Seed: first 8 hex digits of the source SHA-256 (`d3f55bd4`) = 3556072404. Candidates: S/ARCH records citing units from at least two articles (the instrument has no chapters; "part" read as article), sorted by id: ARCH-01, ARCH-02, SC-01, SC-02, SC-03, SC-05, SC-06. The draw used Python `random.Random(seed).randrange(7)` (the generator is not fixed by the frozen documents; logged DEV-14) and selected SC-05 (TR-01); the candidate with the largest number of distinct supporting units is ARCH-02 (TR-02). Both were recomputed independently by `verify2.py`.

## 6. Isolation attestation

The recovery executor read only the allow-listed paths plus the one permitted recovery note (ACCESS_AND_CONTAMINATION_LOG.md). Contamination status: CLEAN. The earlier executor's accesses are covered by the orchestrator's transcript audit.
