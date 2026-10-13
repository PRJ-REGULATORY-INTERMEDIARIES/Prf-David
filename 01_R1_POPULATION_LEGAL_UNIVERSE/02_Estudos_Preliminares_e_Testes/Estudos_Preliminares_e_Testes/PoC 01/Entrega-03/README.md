# Delivery 03 — AI-Assisted Coding Layer (v4)

This folder **does not replace** `../Entrega-02/`. `Entrega-02/` remains the current delivery of the human-coding exercise (Stages A/B/C, v3). Its `candidate_adjudications_v3.csv` and `rit_relationships_v3.csv` are the authoritative records and are not modified by this package.

`Entrega-03/` is an additive experiment. It introduces an LLM as an interpretive coder, formally integrated into a protocol explicitly authorized by David and constrained by the same five-condition relational test established in `RIT_CODEBOOK_v3.md`. The model is never a substitute for that test.

## Most important structural rule

**Nothing in `data/*.jsonl` is automatically copied or merged into the human CSVs in `Entrega-02/`.** A machine-generated row can become a human record only if Igor reviews the item in `data/human_review_queue_v1.csv` and, if accepted, personally enters the row into `Entrega-02/data/candidate_adjudications_v3.csv` or `rit_relationships_v3.csv`. The new entry must retain the responsible `coder` and `coding_date`, as well as `ai_assisted` and `ai_run_ref` columns (see `AI_CODING_PROTOCOL.md`).

## Reading order

1. `AI_CODING_PROTOCOL.md` — the role, limits and safeguards for AI assistance.
2. `MODEL_SELECTION_PROTOCOL.md` — model-selection procedure, specified before any execution.
3. `MODEL_SELECTION_RESULTS.md` — to be completed only after running Tier 1.
4. `CHANGELOG_v4.md` — additions introduced in this round.

## Contents

- `reference/` — read-only copies of materials previously validated in `Entrega-02/` (codebook, data dictionary, human CSVs and already acquired raw HTML; no new network collection).
- `schemas/` — JSON Schemas and structured-output specifications by stage.
- `prompts/` — system/user prompt templates and shared safeguards.
- `scripts/` — reproducible pipeline for context assembly, model adapters, stage execution, self-consistency checks, follow-up context requests and the model-selection experiment.
- `data/` — AI execution outputs; initially empty until the first real run.

## Historical status recorded for this delivery

**No real API call had been made at the time this package was documented.** It contained a complete design (protocols, schemas, prompts and scripts), but Tier 0 execution required the user's explicit confirmation that the model identifier and current OpenAI price had been checked in the provider dashboard. See prerequisites in `MODEL_SELECTION_PROTOCOL.md`.

This README describes the historical status of the archived v4 delivery and must not be read as an up-to-date statement about later executions.
