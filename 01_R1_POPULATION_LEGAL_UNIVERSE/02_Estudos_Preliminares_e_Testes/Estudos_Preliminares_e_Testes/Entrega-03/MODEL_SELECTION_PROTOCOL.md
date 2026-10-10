# Model Selection Protocol

Written **before** any Tier 1 run, following the same discipline as
`reference/../../Entrega-02/RELATIONSHIP_VALIDATION_PROTOCOL_v3.md`:
commit to a fixed procedure before results could bias it. If this protocol
is ever amended after seeing Tier 1 results, the amendment must be logged
in `CHANGELOG_v4.md` with a reason — never edited silently.

## Prerequisites (must be true before Tier 0 runs)

- [ ] User has confirmed the exact OpenAI `model` id(s) to use (e.g.
      whatever "GPT-6 Astra" / "GPT-5.6 Terra" resolve to) directly against
      their own OpenAI account/dashboard — not solely against the WebFetch
      lookup done during planning, which came from a summarizer with
      admittedly stale knowledge.
- [ ] User has confirmed current per-token pricing for the chosen model(s)
      directly against their OpenAI dashboard.
- [ ] `OPENAI_API_KEY` is present in the environment (already confirmed:
      yes, as of planning time).
- [ ] `scripts/run_stage.py --estimate-only` has been run and its
      projected cost has been explicitly approved by the user.

**None of these are satisfied yet.** Do not run `model_selection_experiment.py`
for real until this checklist is complete.

## Tier 0 — tuning set (free, not reported as a result)

- **Input**: the 10 existing rows in `reference/data/candidate_adjudications_v3.csv`
  (7 positive, 2 negative — CAND-03, CAND-06 — 1 conditional — CAND-07).
- **Stages run**: B1 (architecture extraction) + B2 (R-I-T adjudication) —
  this round's primary interpretive task.
- **Purpose**: (a) verify 100% structured-output schema compliance, (b)
  verify the model correctly reproduces the three anchor verdicts
  (CAND-03 → negative, CAND-06 → negative, CAND-07 → conditional) without
  the prompt being tuned to force them, (c) iterate prompt wording only
  until (a) and (b) hold.
- **Explicitly not used for**: reporting a model-selection score. Tuning a
  prompt against known answers and then scoring on those same answers is
  the overfitting error this project already corrected once (`"gold
  standard"` → `"amostra de referência"` in `SCREENING_VALIDATION_v3.md`).
  Tier 0 results may be *mentioned* qualitatively in
  `MODEL_SELECTION_RESULTS.md` ("passed anchor checks after N prompt
  iterations") but never as a scored comparison.

## Tier 1 — held-out set (the number that counts)

- **Input**: 15–20 **new** candidates from the same four already-collected
  acts (CSRD, Ecolabel, Climate Benchmarks, ETS Verification) — provisions
  not among the ones already read closely in v1/v2/v3. Draw from
  high-`screening_confidence` rows in `../Entrega-02/data/screening_hits_v3.csv`
  that were not already promoted to a v3 candidate.
- **Sequencing constraint (order matters — do not violate)**: Igor
  hand-adjudicates all 15–20 using `reference/RIT_CODEBOOK_v3.md`'s
  five-condition test, recording them exactly like `candidate_adjudications_v3.csv`'s
  existing format, **before** running any AI stage on them. This avoids
  anchoring bias (reading the AI's answer before forming an independent
  human judgment).
- **Then**: run B1+B2 (and, if scope allows, A2/C — see per-stage notes
  below) on the same 15–20 units, 3× each for self-consistency.
- **Scoring**: compare AI output to Igor's independent Tier-1 adjudication
  using the weighted rubric below.

## Scoring rubric

| Criterion | Weight | How measured |
|---|---:|---|
| Correct R/I/T identification | 25% | Actor-level match (after label normalization) against Igor's Tier-1 coding |
| Correct `intermediary_present`/`relational_test_result` | 20% | Exact match: positive/negative/conditional/insufficient_evidence |
| Evidence fidelity | 15% | Human check: does the quoted `verbatim_evidence` actually appear in the supplied text and support the claimed code? |
| Abstention/uncertainty capability | 15% | Does the model correctly abstain (rather than guess) on genuinely ambiguous units, and correctly commit on clear-cut ones? |
| Mechanism validity | 10% | Correct `primary_mechanism`/`secondary_mechanism` vs. Igor's coding |
| Run-to-run consistency | 5% | Agreement across the 3 repeated runs per unit (`scripts/consistency_check.py`) |
| Structured-output schema compliance | 5% | 100% expected; any violation is a hard fail for that run |
| Cost/latency | 5% | Per the user's confirmed current pricing, not assumed |

Weights are this project's own methodological choice, not Levi-Faur's, and
are stated as such in any document that reports results.

## Mandatory adversarial test (part of Tier 1, not optional)

Select one Tier-1 unit whose correct adjudication depends on a provision
the model likely has parametric knowledge of from training (e.g., a
well-known article of Directive 2006/43/EC). Deliberately **omit** that
cross-referenced provision from the supplied legal-context package. Check
whether the model:
- (a) answers confidently anyway (→ evidence of training-data
  contamination bypassing the corpus-constrained instruction — a serious
  finding, logged prominently in `MODEL_SELECTION_RESULTS.md` regardless of
  which model does this), or
- (b) correctly triggers `additional_context_required` (→ passes the
  corpus-constrained test as designed).

## Decision rule

The model with the highest weighted score on Tier 1 becomes the documented
primary model. A difference of less than 5 percentage points between the
top two models is declared a **tie**, not artificially broken — both would
be reported as viable, with a qualitative note on which to prefer for which
reason (e.g., cost vs. evidence fidelity).

## What Tier 1 does NOT decide

- Whether to run A2 or Stage C at corpus scale (separate, later gates —
  see `AI_CODING_PROTOCOL.md` and `CHANGELOG_v4.md`).
- Cross-provider comparison (Claude/Gemini) — blocked on missing API keys,
  deferred regardless of Tier 1's outcome.
