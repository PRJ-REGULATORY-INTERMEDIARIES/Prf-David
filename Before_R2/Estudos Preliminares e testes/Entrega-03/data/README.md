Empty by design. No real API call has been made yet (see
`../CHANGELOG_v4.md` and `../MODEL_SELECTION_PROTOCOL.md`'s prerequisites
checklist). Once Tier 0/1 runs happen, this folder fills with:
`model_selection_runs_v1.jsonl`, `ai_candidate_hits_v1.jsonl`,
`ai_adjudications_v1.jsonl`, `ai_stage_c_proposals_v1.jsonl`,
`model_selection_scorecard_v1.csv`, `human_review_queue_v1.csv`.

Smoke-tested during scaffolding with `--provider dry_run` (no cost, no
network calls) to confirm the pipeline runs end-to-end across all 4 acts;
those test artifacts were deleted afterward, not left here, to avoid being
mistaken for real experiment data.
