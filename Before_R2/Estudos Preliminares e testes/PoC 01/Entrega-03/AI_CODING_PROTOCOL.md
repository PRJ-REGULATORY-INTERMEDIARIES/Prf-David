# AI Coding Protocol

Governs the role of a large language model (LLM) as an assisted
interpretive coder in this project, across four stages (A2, B1, B2, C).
This document does not redefine the coding rules themselves — those remain
`reference/RIT_CODEBOOK_v3.md` (the five-condition relational test) and
`reference/DATA_DICTIONARY_v3.md` (variable definitions, missingness codes,
observability classes). This document governs how an LLM is bound to those
rules, and what it is structurally forbidden from doing regardless of how
it is prompted.

## Role
The LLM is an **assisted interpretive coder**, not an autonomous coder and
not a replacement for the human relational test. It proposes candidate
codings; a human (Igor) decides what enters the project's authoritative
human-coded files. This mirrors, at the AI layer, the same discipline
`RELATIONSHIP_VALIDATION_PROTOCOL_v3.md` already applies to a hypothetical
second human coder: independent proposal, then adjudication, never silent
merge.

## The four stages and what the LLM does at each

| Stage | LLM task | Consumes | Produces |
|---|---|---|---|
| A2 | Semantic candidate detection — flag provisions that might contain intermediation even without canonical lexical markers | one provision's text | `AI_candidate`, `candidate_actor`, `candidate_function`, `candidate_mechanism`, `verbatim_evidence`, `AI_confidence` |
| B1 | Regulatory architecture extraction — list actors and explicitly stated relations, **before** any R/I/T role assignment | full-article legal-context package | list of actors, list of relations, `architecture_summary` |
| B2 | R-I-T adjudication — answer the five relational-test conditions individually, then a final verdict | legal-context package + B1 output + the five conditions (verbatim from `RIT_CODEBOOK_v3.md`) | per-condition answers, `relational_test_result`, R/I/T actors + evidence, mechanism |
| C | Institutional attribute coding — only for B2-positive relationships | relationship text + confirmed R/I/T + the specific `DATA_DICTIONARY_v3.md` field definitions being requested | value/evidence/observability_class/confidence per attribute |

## Hard guardrails (structural, not just prompt suggestions)

1. **Evidence before code.** Every coded field requires non-null evidence
   unless the value itself is an abstention code, in which case an
   abstention reason is required instead. A confident value with no
   evidence is a schema violation, not a valid answer.
2. **Abstention is rewarded, not penalized.** `UNK`/`NOE`/`EXT`/
   `conditional`/`insufficient_evidence`/`UNCLEAR` are correct answers when
   the supplied text does not clearly support a determination — never
   force-completed to look like a finished R-I-T triad. This is scored
   explicitly in `MODEL_SELECTION_PROTOCOL.md`'s rubric (15% weight).
3. **Corpus-constrained coding.** During Stage B/C, the model receives only
   the supplied legal-context package — no autonomous web/browsing tool
   use. Known caveat, stated plainly: a frontier model may have parametric
   knowledge of these regulations from training; this instruction cannot be
   verified by the prompt alone. The mitigant is the evidence-fidelity
   scoring dimension (does the quoted evidence actually appear in, and say
   what is claimed about, the supplied text) plus a mandatory adversarial
   test in `MODEL_SELECTION_PROTOCOL.md`.
4. **Bounded context-request loop.** If the model judges it needs a
   specific additional provision, it emits `additional_context_required`
   with `requested_source` and `reason` rather than filling the gap from
   memory. The pipeline resolves this at most once per unit per stage
   (`scripts/context_request_loop.py`); a second request routes the unit
   straight to human review.
5. **Self-consistency, never averaged.** Each unit is run 3× with identical
   input. Any disagreement on substantive fields (relational_test_result,
   R/I/T identity, primary_mechanism) routes the unit to
   `human_review_required=1`. No majority vote is silently taken as truth.
6. **Reproducibility logging on every call**: `model_provider`, `model_id`,
   `model_snapshot` (a pinned version, never a rolling alias),
   `reasoning_effort`, `prompt_version`, `schema_version`, `timestamp`,
   `input_hash`, `output_hash` — written to
   `data/model_selection_runs_v1.jsonl`.
7. **No direct writes to human files.** The LLM (and the scripts that call
   it) never write to `../Entrega-02/data/*.csv`. Output lives in
   `data/*.jsonl` until a human promotes a specific row.

## Constructs the LLM may never code, at any stage

```
AI_MAY_NOT_CODE:
  effectiveness
  legitimacy
  trust
  polycentricity_score
  autonomy_index
  accountability_index
```

These sit below the "boundary of this coding layer" line in the project's
own conceptual framework (see `../Entrega-02/RELATORIO_FINAL_APRESENTACAO.qmd`,
figure 1). The Stage C schema requires an `out_of_bounds_check` field the
model must set to `false` (with a one-line note) if a prompt or its own
reasoning tempts it toward one of these — enforced structurally via the
schema's fixed enum, not left to the model's judgment alone.

## Promotion path (AI output → human-authored dataset)

1. AI produces a candidate record in `data/ai_adjudications_v1.jsonl` (or
   the relevant stage's JSONL).
2. Igor reads the record, including all evidence quotes and the routing
   tier it landed in (fast-track spot-check vs. full human adjudication).
3. If accepted, Igor writes the row himself into
   `../Entrega-02/data/candidate_adjudications_v3.csv` and/or
   `rit_relationships_v3.csv`, with his own `coder` and `coding_date`, plus
   two new provenance columns added to those files at first use:
   - `ai_assisted` (`1`/`0`) — whether an AI proposal informed this row.
   - `ai_run_ref` — the `screening_id`/`relationship_candidate_id` +
     `output_hash` pointing back to the exact AI record in `Entrega-03/`.
4. If rejected or inconclusive, the record stays in `data/*.jsonl` and
   `data/human_review_queue_v1.csv`, documented but never promoted.

This is the same "document the process, don't hide it" instinct already
visible in `RIT_CODEBOOK_v3.md`'s CAND-09 correction note — an AI-assisted
row should always be traceable as such, not indistinguishable from a
fully-manual one.

## Scope discipline for this round
Per the approved plan: all four stages are being scaffolded in this round,
but **routing defaults to full human review** for everything until
`MODEL_SELECTION_RESULTS.md` shows a validated, stable, schema-compliant
model on the Tier 1 held-out set. Corpus-scale application (all 1,079
Stage-A screening hits, the full ~20-field autonomy/accountability
battery) is explicitly out of scope for this round — see
`CHANGELOG_v4.md`.
