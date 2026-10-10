# 05 — QA and human adjudication

Three stages, in order.

## R4.2B — stratified human QA

A stratified sample was reviewed through an offline panel. The stage produced an ambiguity
typology, a confidence calibration table, a correction register, QA metrics and a systematic
error audit (with a later updated version, both preserved). Two cross-model-supported patterns
emerged: counterpart/recipient over-attribution and actor/action fragmentation.

`human_review_interface/` holds the panel and its working file — the actual instrument the human
researcher used.

## R4.2C — cross-model review

Two model families reviewed the extraction independently and their outputs were compared. The
comparison tables, the calibrated and independent Terra reviews, their freeze manifests and the
closure report are all here.

This stage also produced an explicit **model provenance correction**
(`R4_2C_MODEL_PROVENANCE_CORRECTION.md` and `R4_2C_OUTPUT_RECLASSIFICATION.csv`): outputs whose
model provenance could not be confirmed were reclassified rather than assumed. The same
discipline was applied later to the Claude model label, which is recorded as
`MODEL_SELECTION_RUNTIME_MATCH = NOT_VERIFIABLE`.

`r4_2c_working_copies/` holds six files that share a filename with a file in this folder but
differ byte-for-byte. Both versions are preserved rather than one silently overwriting the other.

## R4.2D — human diagnostic

`R4_2D_human_diagnostic/` is the most important evidence in this folder for anyone auditing the
human contribution. Twelve purposively selected, cross-model-supported cases were adjudicated by
the researcher; all twelve contained confirmed structural defects.

Read `R4_2D_HUMAN_DIAGNOSTIC_REPORT.md` for the narrative,
`R4_2D_HUMAN_DIAGNOSTIC_COMPLETED.csv` for the case-by-case adjudication, and
`R4_2D_HUMAN_DIAGNOSTIC_RULE_CANDIDATES.md` for the **15 candidate structural rules** frozen
from it. Those rules governed every later stage and were not modified by any AI process.

Two interpretation points carried throughout the project: the twelve cases are diagnostic
evidence about failure modes, **not** a corpus error rate, because they were selected precisely
because models flagged them; and the human root cause frequently differed from the model
detection pattern, which is itself recorded as rule 15.

```text
RIT_CODING             = NOT_STARTED
MECHANISM_CODING       = NOT_STARTED
ROTEM_CODING_CONSULTED = NO
R4_3                   = NOT_STARTED
CORPUS_WIDE_REPAIR     = NOT_EXECUTED
```
