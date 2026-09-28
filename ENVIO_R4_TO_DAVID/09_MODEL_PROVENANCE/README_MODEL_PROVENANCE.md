# 09 — Model provenance

`R4_AI_EXECUTION_LOG.csv` records every AI execution across R4 with its model and purpose.
`R4_MODEL_ESCALATION_LOG.csv` records escalations and model changes. Together they are the
authoritative answer to "which model did what" in this round.

## Terra — B1-01, B1-02, B1-03

```text
REQUESTED_MODEL         = GPT-5.6 Terra High
RESEARCHER_SELECTED_MODEL = GPT-5.6 Terra High
MODEL_RUNTIME_VARIANT   = MODEL_VARIANT_NOT_EXPOSED
```

Executed under OpenAI Codex. The runtime variant was never exposed and is recorded as such.

## Claude — B1-04 and the B1S sensitivity audit

```text
EXECUTION_ENVIRONMENT         = Claude Code / VS Code extension
RESEARCHER_SELECTED_MODEL     = Claude Opus 5.5 Extra High
RUNTIME_REPORTED_MODEL        = Claude Opus 5
RUNTIME_MODEL_ID              = claude-opus-5
MODEL_SELECTION_RUNTIME_MATCH = NOT_VERIFIABLE
```

The researcher selected `Claude Opus 5.5 Extra High` in the VS Code Claude agent UI; the
execution environment reported `Claude Opus 5`. The relationship between the two labels could not
be verified from inside the session. **Both are recorded. The runtime did not verify the
researcher's selection, and the two labels are not asserted to be equivalent.**

The correction that established this rewrote only provenance columns; substantive cells were
verified byte-identical. The pre-correction exports are preserved in
`10_FREEZE_AND_INTEGRITY/superseded_preserved/`.

## Earlier stages

Initial extraction and early QA were performed with Luna; R4.2C compared Luna and Terra. That
stage produced its own provenance correction, preserved in folder 05, in which outputs whose
provenance could not be confirmed were reclassified rather than assumed.

## Human authority

`Igor Caires Machado` is the final methodological authority for theoretical decisions, human
adjudication, acceptance or rejection of candidate rules, interpretation, research design and
scientific conclusions. AI output is extraction assistance, structural review, diagnostic
proposal, QA and sensitivity analysis — **not autonomous ground truth**.

`R4_SESSION_CHECKPOINT_2026-09-26.md` and `R4_GIT_SYNC_LOG.md` record execution continuity and
repository synchronisation.

```text
RIT_CODING             = NOT_STARTED
MECHANISM_CODING       = NOT_STARTED
ROTEM_CODING_CONSULTED = NO
R4_3                   = NOT_STARTED
CORPUS_WIDE_REPAIR     = NOT_EXECUTED
```
