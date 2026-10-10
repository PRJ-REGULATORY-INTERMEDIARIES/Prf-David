# GDPR Pilot 01 — whole-instrument reconstruction (RGAM)

**Status:** `MACHINE_PROVISIONAL`, exploratory, single evaluator. Not validated; not an approved reconstruction; not a statement that the GDPR "has" particular architectures. Executed 2026-10-03 under `paper/MANUSCRIPT_v0_6_1.md` (provisional authority).

**Start with** `PILOT_01_EXECUTIVE_REPORT.md`.

| Folder | Content |
|---|---|
| `00_PROTOCOL/` | research design; corpus and version register; frozen decision rules (v1.0 + logged v1.1, v1.2); ontology alignment and precedence |
| `01_SOURCES/` | source manifest + hashes; raw EUR-Lex files; parsed text; corrigendum log; unit inventory (389 paragraphs, 382 points); external-reference register |
| `02_COVERAGE/` | `ARTICLE_COVERAGE_REGISTER.csv` (389 rows); `COVERAGE_REPORT.md` |
| `03_EXTRACTION/` | `NORMATIVE_ASSIGNMENTS.csv` (157), `QUALIFIED_RELATIONS.csv` (238), `POSITIONS_AND_DEVICES.csv` (47), `EXTRACTION_UNCERTAINTIES.md`; the batch scripts (`batch_01…11`) and `run_all.py`, `emit.py` rebuild every CSV from the records |
| `04_RECONSTRUCTION/` | `SUBCONFIGURATIONS.md`, `ARCHITECTURAL_INFERENCE_REGISTER.csv` (AI-01…AI-09), `INITIAL_ARCHITECTURAL_PROFILE.md`, `WORKED_LEGAL_TRACE.md` |
| `05_SCIENTIFIC_ASSESSMENT/` | `V6_RGAM_INCREMENTAL_COMPARISON.md`, `THEORY_PROBLEMS_ENCOUNTERED.md`, `HUMAN_ADJUDICATION_QUEUE.md` |

**Reproducibility:** `python 01_SOURCES/build_working_text.py` (parse + corrigendum), then in `03_EXTRACTION/`: `python run_all.py && python emit.py && python emit_docs.py`; in `04_RECONSTRUCTION/`: `python reconstruct.py && python profile_stats.py && python build_inference_register.py`. Raw files are in `01_SOURCES/raw/` with hashes.

**Not modified:** `paper/MANUSCRIPT_v0_6_1.md` and all earlier manuscripts; V6; Rotem's codebook; PILOT_03; the frozen ontology and historical validation results. No Git operation. No parallel agents.
