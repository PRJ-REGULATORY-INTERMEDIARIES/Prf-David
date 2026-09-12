# Changelog v4

## v4 — 06/09/2026 — AI-assisted interpretive coding layer (scaffolding, not yet executed)

Adds `Entrega-03/`, a new delivery folder (kept separate from `Entrega-02/`
by explicit user decision, rather than nested inside it) incorporating an
LLM as a formally protocol-bound "assisted interpretive coder" for Stage
B/C, plus new Stage A2 (semantic candidate detection) and an extension of
Stage C's attribute coding — authorized explicitly by David.

**What was built this round:**
- `AI_CODING_PROTOCOL.md` — the LLM's role, the four stages it participates
  in, and seven hard structural guardrails (evidence-before-code, rewarded
  abstention, corpus-constrained coding with a stated verification caveat,
  bounded context-request loop, unaveraged self-consistency checking,
  full reproducibility logging, no direct writes to human files).
- `MODEL_SELECTION_PROTOCOL.md` — a two-tier experiment design (Tier 0:
  free tuning against the 10 existing v3 candidates, never reported as a
  score; Tier 1: 15–20 fresh held-out candidates, hand-adjudicated by Igor
  *before* seeing AI output, which produces the number that counts) plus a
  weighted 8-criterion scorecard and a mandatory adversarial
  training-data-contamination test.
- Four Structured-Outputs JSON schemas (`schemas/`) — one per stage — built
  on shared `$defs` (`CodedValue`, `CategoricalValue`, `TestCondition`,
  `ContextEscapeHatch`) that reuse `DATA_DICTIONARY_v3.md`'s exact
  missingness codes (`1/0/NA/UNK/NOE/EXT`) and observability classes
  (`DIRECT/INFERRED/EXTERNAL/NOT_OBSERVABLE`) rather than inventing new
  vocabulary.
- Prompt templates (`prompts/`) for all four stages plus one shared
  guardrail block reused across them, with Stage B1's system prompt
  explicitly narrating the project's own CAND-09/RIT-007 correction (an
  architecture-reconstruction error the human coder made and fixed) as the
  motivation for "reconstruct before classify."
- Six orchestration scripts (`scripts/`) — legal-context package assembly
  (extends `screening_v3.py`'s article extraction rather than
  reimplementing it), a provider-agnostic model adapter (OpenAI
  implemented; Claude/Gemini stubbed), per-stage execution with schema
  validation and run-logging, 3x self-consistency checking, a
  bounded (1-round) context-request loop, and the Tier 0/1 experiment
  orchestrator.

**Explicit decisions, per the approved plan:**
- All four stages (A2, B1, B2, C) scaffolded together in this round, not
  phased — accepting a larger error surface, offset by defaulting every
  unit to full human review until Tier 1 validates a model.
- Separate `Entrega-03/` folder, not `Entrega-02/ai/` — keeps this
  experiment visibly distinct from the validated v3 delivery.
- OpenAI only this round (`OPENAI_API_KEY` present, `openai` SDK 2.32.0
  installed); Claude/Gemini deferred (no API keys present for either).
- Two deliberately dropped fields from the original proposal:
  `rule_source`/`direct_regulator`/`oversight_authority` were **not**
  revived in the schemas — v3 already declined to use them
  (`VARIABLE_MAP_v3.md`), and reviving them inside an AI schema without a
  deliberate `DATA_DICTIONARY_v3.md` change would silently overturn that
  decision.

**What was explicitly NOT done this round:**
- **No real API call has been made.** `MODEL_SELECTION_PROTOCOL.md`'s
  prerequisites checklist (confirm exact model id + current pricing on the
  user's own OpenAI dashboard) is unchecked — running
  `model_selection_experiment.py` for real requires that confirmation
  first.
- No Tier 1 held-out set has been hand-adjudicated yet.
- No AI output exists yet in `data/` — the folder is scaffolded empty.
- Corpus-scale application of any stage (all 1,079 Stage A screening hits;
  the full ~20-field autonomy/accountability battery) remains out of scope
  until Tier 1 validates a model and a second, smaller validation of each
  additional stage is run.
- Cross-provider (Claude Opus 5, Gemini) comparison — blocked on missing
  API keys, `model_adapter.py`'s stubs exist but are unimplemented.

## v3 and earlier
See `../Entrega-02/CHANGELOG_v3.md`.

## Execution note — 6 September 2026

The OpenAI adapter was wired to the installed `openai` 2.32.0 Responses API
using strict JSON Schema output and `store=false`. The account model list
exposed `gpt-5.6-terra`, but the first generation request returned
`credit_balance_exhausted`; no substantive response was accepted. The
five-act execution and the 201-call dry-run are documented in
`../Entrega-04/`.
