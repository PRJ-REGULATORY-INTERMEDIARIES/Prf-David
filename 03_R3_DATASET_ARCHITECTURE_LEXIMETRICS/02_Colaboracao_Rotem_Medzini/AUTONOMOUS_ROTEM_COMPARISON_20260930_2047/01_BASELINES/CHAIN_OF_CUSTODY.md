# CHAIN_OF_CUSTODY (R01)

## Principles applied
1. **Originals are read-only.** No file outside `AUTONOMOUS_ROTEM_COMPARISON_20260930_2047/` was created, modified, moved or deleted. Before-and-after hashes of the originals are compared in R12 (`12_FINAL/FINAL_QA.md`, test `T-PRESERVE`).
2. **Every derived artefact states how it was made.**
   - Derived text files (`01_BASELINES/derived_text/*.md`) carry an HTML-comment header with source path, SHA-256, `SOURCE_STATUS`, transformation and time.
   - `BASELINE_*` files are either byte copies (hash-verified, `BASELINE_FREEZE_LOG.csv`) or verbatim sheet exports (Rotem workbook, cell values as stored, empty rows skipped, Excel row numbers retained in `WB_ROW`).
3. **Official legal texts** were fetched once (2026-09-30, ~21:00 −03:00) from the Publications Office Cellar and stored as raw HTML plus a plain-text rendering, with SHA-256 for both (`official_texts/OFFICIAL_TEXT_MANIFEST.csv`). Legal quotations in this run are taken from these stored texts, or from the local R4 DSA copy where stated. They are never taken from memory.
4. **Downloads files** were read only when named individually in `SOURCE_REGISTER.csv`. The folder was not scanned beyond a file-name filter.
5. **Human decisions** (PILOT_03 H_001–H_019, R4.2D 12 cases) are copied byte-for-byte into `BASELINE_*`. They are never edited, re-labelled or re-adjudicated.

## Custody chain per critical input

| Input | Origin → run | Transformation | Verification |
|---|---|---|---|
| Rotem e-mail | `Enviados/30_09_26/email e chat` → quoted in `06_CODEBOOK/*` | Quotation of lines 2–20 only | SHA-256 546E4BBC… |
| Unrevised codebook | Downloads → `derived_text/CODEBOOK_UNREVISED_BASELINE.md` | docx → md; paragraph numbers `[¶n]` added | Source SHA-256 in header |
| Chart Key | Downloads → `derived_text/CHART_KEY_UNREVISED_BASELINE.md` | docx → md | Source SHA-256 in header |
| Revised codebook | PILOT_01/00_SOURCES → `derived_text/CODEBOOK_REVISED.md` | docx → md | Source SHA-256 in header; identical to the Downloads copy |
| Rotem workbook | PILOT_01/00_SOURCES → `BASELINE_ROTEM_WB_*.csv` (3 sheets) | Verbatim cell export | Workbook SHA-256 in `BASELINE_FREEZE_LOG.csv` |
| PILOT_03 human decisions | PILOT_03/07_HUMAN_ADJUDICATION → `BASELINE_REL_PILOT03_*` | Byte copy | Hash equality asserted |
| R3 relations / mechanisms | R3_CLEANROOM staging → `BASELINE_REL_R3_*` | Byte copy | Hash equality asserted |
| R4.2D human diagnostic | ENVIO_R4_TO_DAVID → `BASELINE_R4_2D_HUMAN_DIAGNOSTIC_COMPLETED.csv` | Byte copy | Hash equality asserted |
| R4 DSA extraction subset | ENVIO_R4_TO_DAVID → `BASELINE_R4_EXTRACTION_DSA_ART21_22_37_42.csv` | Row filter; values verbatim | Source SHA-256 recorded |
| Official texts (17 CELEX) | Cellar → `official_texts/{CELEX}.html/.txt` | HTML stored; tag-stripped text rendering | SHA-256 of both; HTTP 200 for all 17 |

## Known custody caveats
- **CRLF normalisation.** The project's git configuration uses `core.autocrlf=true`, and some historical text hashes match their recorded values only after LF normalisation. `SOURCE_REGISTER.csv` therefore also records `SHA256_LF_NORMALIZED` for text files. Comparisons in R03–R05 report both hashes.
- **Downloads is volatile.** Files there may be moved or deleted after this run. Their hashes as of this run are in `BASELINE_HASHES.csv`.
- **The R3 original** at `C:/PROJETOS/ICM-PMO/...` was not re-read. The run uses the staging copy under `R4_CROSS_DOMAIN_VALIDATION/01_baseline/R3_HISTORY_STAGING/`.
