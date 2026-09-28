# 08 — Action representation sensitivity audit (R4.2E-B1S)

After B1 closed, final QA found a problem with the review instrument rather than with the corpus.

The review input presented an Action field populated from `LEGAL_ACTION`, a controlled-vocabulary
label. The extraction separately holds `LEGAL_VERB`, carrying the source predicate with its
modality, and a `MODALITY` category. Verified deterministically: an explicit modal appears in
`LEGAL_VERB` in **1,370 of 1,404** records and in `LEGAL_ACTION` in **5**. Reviewers therefore
recorded modality as missing when it was present in a column they were not shown.

`R4_2E_B1_ACTION_SENSITIVITY_AUDIT.csv` re-examines all 143 Action judgments against the full
representation, one row per case, with the original judgment, the judgment under full
representation, a sensitivity result and a written reason. No case was rerun and no frozen
adjudication was modified.

`R4_2E_B1_ACTION_SENSITIVITY_SUMMARY.csv` gives the aggregates:

| | |
| --- | --- |
| `ORIGINAL_B1_ACTION_CORRECTION_COUNT` | **87** (frozen, not overwritten) |
| `SENSITIVITY_ADJUSTED_ACTION_CORRECTION_COUNT` | **63** (descriptive) |
| Action decisions changed | 26 (25 one way, 1 the other) |
| Overall defect decisions materially affected | **1 of 143** |

Both counts are reported. The adjusted figure is a
`POST_HOC_ACTION_REPRESENTATION_SENSITIVITY_RESULT`, not a re-review.

Two Action defect classes survive the audit as real rather than representational: entitlement
constructions recorded without "shall" and with modality UNCLEAR, and coordinated predicates
buried inside the object.

`R4_VARIABLE_REDUNDANCY_AUDIT.csv` recomputes five variable pairs with their overlap, exactness,
direction and parsimony status — counterpart/recipient, the two object fields, ambiguity versus
confidence, legal action versus legal verb, and modality versus legal verb. It is the single
best file to read for the variable-parsimony question.

```text
RIT_CODING             = NOT_STARTED
MECHANISM_CODING       = NOT_STARTED
ROTEM_CODING_CONSULTED = NO
R4_3                   = NOT_STARTED
CORPUS_WIDE_REPAIR     = NOT_EXECUTED
```
