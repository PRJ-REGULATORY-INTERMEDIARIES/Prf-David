# Model-selection results v4

**Status: blocked before generation.**

- Model selected for implementation: `gpt-5.6-terra`.
- Account model-list request: successful.
- Installed SDK: `openai 2.32.0`.
- Live generation attempt: `credit_balance_exhausted` / `insufficient_quota`.
- Substantive responses accepted: `0`.
- Tier 0 anchor score: not computed, because no generated output exists.
- Tier 1 scorecard: not run; the 20 held-out units also require independent
  human adjudication before any Tier 1 call.
- Dry-run: 201 schema-valid orchestration calls, explicitly excluded from
  model-selection scoring.

The provider error and next action are recorded in
`data/api_attempt_v4.json`. This file must not be amended into a model winner
or accuracy claim after the fact; the next run should append fresh records
with a newly confirmed account state and the same pre-registered procedure.
