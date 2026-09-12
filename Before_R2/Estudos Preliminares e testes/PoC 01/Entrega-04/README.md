# Entrega-04 — Complete report on regulatory intermediaries

This is the versioned five-act delivery for PoC 01. `Entrega-02/` and
`Entrega-03/` remain available as historical and protocol reference
deliveries; the v4 adjustments and generated outputs are isolated here.

## Status

- Five CELEX acts were collected from EUR-Lex on 6 September 2026 and linked
  to `data/CELEX_MANIFEST_v4.csv` and its JSON mirror.
- Lexical Stage A1 produced 1,092 hits: 1,079 reproduced from the four-act
  v3 corpus and 13 from the Taxonomy Regulation.
- The seven v3 human-validated R-I-T relationships were preserved in
  `data/rit_relationships_v4.csv`.
- Twenty new units were selected deterministically (four per act) for human
  adjudication. They are marked `PENDING_HUMAN` and do not enter the positive
  relationship dataset.
- OpenAI API access and model listing worked, but the first generation call
  returned `credit_balance_exhausted`. Consequently `data/ai_runs_v4.jsonl`
  contains only 201 schema smoke-test calls from `dry_run`; it contains no
  substantive model finding.
- `data/api_cost_estimate_v4.json` estimates the planned 201-call live run at
  approximately US$2.2027 at the published `gpt-5.6-terra` rates; the account
  dashboard remains authoritative.
- `data/api_attempt_v4.json` records the unsuccessful live-generation attempt
  without storing the API key.
- `MODEL_SELECTION_RESULTS_v4.md` records why no model score or winner is
  reported.

## Main deliverables

- `RELATORIO_COMPLETO_INTERMEDIARIES_EN.qmd` and `.docx` — report prepared for
  Prof. David Levi-Faur.
- `data/` — manifest, preserved HTML, screening, candidate, relationship,
  actor and audit-sample files, plus AI, validation and review views.
- `scripts/collect_v4.py` — collect the five CELEX records and write hashes.
- `scripts/screening_v4.py` — reproducible lexical screening.
- `scripts/prepare_samples_v4.py` — seeded four-per-act sample selection.
- `scripts/run_ai_v4.py` — three-run A2/B1/B2 pipeline and optional Stage C;
  defaults to `dry_run`, and never writes authoritative CSVs.
- `scripts/build_auxiliary_outputs_v4.py` — materialises reviewable CSV views
  from the append-only AI log without promoting proposals.
- `scripts/estimate_v4.py` — prompt-based live-run cost estimate.
- `scripts/validate_v4.py` — acceptance checks.
- `schemas/` and `prompts/` — Structured Outputs contracts and prompts.
- `figures/` — the descriptive screening figure and six analytical figures.

## Reproduction

From this directory:

```text
python scripts/collect_v4.py
python scripts/screening_v4.py
python scripts/prepare_samples_v4.py
python scripts/build_datasets_v4.py
python scripts/run_ai_v4.py --provider dry_run --model dry-run-v4 --include-c
python scripts/build_auxiliary_outputs_v4.py
python scripts/make_figure_v4.py
python scripts/make_figures_v4.py
python scripts/validate_v4.py
quarto render RELATORIO_COMPLETO_INTERMEDIARIES_EN.qmd --to docx
```

For a later real API run, set `OPENAI_API_KEY` in the process environment and
run `scripts/run_ai_v4.py --provider openai --model gpt-5.6-terra` only after
the account has credits and the 20 units have been independently adjudicated.
Real outputs remain in the run log and review queue; they are never merged
automatically into `rit_relationships_v4.csv`.
