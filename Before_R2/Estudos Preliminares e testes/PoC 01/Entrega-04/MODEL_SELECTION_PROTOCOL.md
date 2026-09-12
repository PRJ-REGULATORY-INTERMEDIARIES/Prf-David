# Model selection protocol v4

## Registered decision rule

The model is an assisted coder, not the final authority. A primary model and
a challenger should be compared where feasible using the same prompt,
schema, legal-context package, sample and human cases. Criteria are evidence
fidelity, abstention/context-request discipline, R-I-T condition validity,
mechanism validity, structured-output validity, repeatability and cost.

Tier 0 is a small anchor set used to detect obvious failures. Tier 1 is the
held-out sample after independent human adjudication. Agreement is compared
field by field; it is never hidden in a single aggregate score. A model is not
called “best” unless the registered comparison has actually been completed.

## v4 status

The account model list exposed `gpt-5.6-terra` and the Responses API adapter
was implemented with strict JSON Schema output. The first generation call
returned `credit_balance_exhausted` / `insufficient_quota`, so zero
substantive model outputs exist. No challenger comparison, Tier 0 score,
Tier 1 score or model winner is reported. The 201 local dry-run records are
schema/orchestration smoke tests only.

The next execution must restore credits, complete the 20 independent human
adjudications, run the same three repetitions, preserve run metadata and
review every proposed promotion. Account pricing and availability must be
rechecked at execution time.
