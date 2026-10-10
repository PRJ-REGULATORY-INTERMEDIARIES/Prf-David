# NEW TEST 3x3 — CASE SELECTION PROTOCOL

Operational companion to `TEST_3X3_PRE_REGISTRATION.md` (which governs in case of conflict).

## Step 0 — Workspace and freeze of prior experiments
Work only in `NEW TEST 3x3/`. Previous experiments (R2, R3, R4, PILOT_01–03, V8_COMP_01, RGAM, ARQGOV) are read-only; no file outside this folder is created, modified, moved or frozen.

## Step 1 — Systematic repository search (case discovery)
Scan every CSV/XLSX/JSON/MD under the repository (excluding `.git`) for extraction records that mention legal instruments, actors, regulators, intermediaries, targets or relations; map them to **source families**:

| Family | Location | Nature |
|---|---|---|
| R3 clean-room (5 climate laws) | `R4_CROSS_DOMAIN_VALIDATION/01_baseline/R3_*` | full-instrument actor register + relation census + R–I–T adjudication |
| R2 `dataset-eurlex` (3 green-transition laws) | `Before_R2/dataset-eurlex/`, `Enviados/Email 01/` | full-act reading, curated R–I–T relation records, researcher review |
| PoC / Entregas v1–v4 | `Before_R2/Estudos Preliminares e testes/` | five-act lexical screening + small R–I–T sample |
| PILOT_01–03 | `RELATIONAL_LEXIMETRICS_PILOT/` | purposive provision-level relational coding |
| R4 digital | `R4_CROSS_DOMAIN_VALIDATION/`, `ENVIO_R4_TO_DAVID/` | whole-instrument structural extraction (no R/I/T) |
| GDPR_PILOT_01 | `RGAM/pilot/GDPR_PILOT_01/` | whole-article relational extraction under RGAM/V6 ontology |
| Rotem dataset | `RELATIONAL_LEXIMETRICS_PILOT/PILOT_01/00_SOURCES/` | external act-level coding of intermediaries |
| R2.1 / V8_COMP_01 provisional | `WORK_2_1/`, `COMPARATIVE_PILOTS/` | source inventories / not-started cases |

## Step 2 — Case-version register
One row per (instrument × source version). Fields: canonical case ID, title, jurisdiction, year, CELEX/identifier, source pilot, directory, extraction version, corpus scope, recorded counts (actors, regulators, intermediaries, targets, relations, intermediation relations), codebook, provenance, limitations, disposition. Versions are cross-referenced, never merged.

## Step 3 — Definitions
Recover controlling definitions of regulator, intermediary, target, regulatory intermediation and relation from project codebooks; compare versions; fix the common operational denominator (G1) or stop.

## Step 4 — Comparability gate
Apply G2–G7 to every case-version × metric. Compute harmonized metrics only from existing records (§9 of the pre-registration) and store them separately. Run the shared-instrument bridge check. Emit the final gate. **If FAIL → stop before ranking.**

## Step 5 — Domain classification
Build a concise Level-1/Level-2 taxonomy from the actual universe; assign every case primary (and, if ambiguous, alternate) domains from title/Article 1 only.

## Step 6 — Ranking
Rank rank-eligible case-versions lexicographically (criteria 1–5, descending). Produce a global ranking and a per-domain ranking. No composite scores or denominators.

## Step 7 — Diversity constraint and selection
Retain the highest-ranked case per domain; walk down the global ranking until exactly three distinct Level-1 domains are filled. If fewer than three distinct domains are available among rank-eligible case-versions, selection is **blocked**, and the report states why and which decisions are required from the research coordinator. Nothing is relaxed automatically.

## Step 8 — Freeze (only if Step 7 succeeds)
Write the selected-cases CSV, freeze note, file manifest and SHA-256 of the manifest in `05_SELECTION_FREEZE/`. State that the cases were selected before any new V8 analysis.

## Step 9 — Stop
Stop. Do not apply V8, construct architectures, run the eight-operation procedure, or compare V8 with alternatives. Return the Portuguese executive summary and one of the two registered final gates.

## Logging
Every directory inspected, source file used, definition recovered, decision, exclusion, harmonization, uncertainty and the hashes of controlling outputs are recorded in `LOGS/TEST_3X3_EXECUTION_LOG.md`.
