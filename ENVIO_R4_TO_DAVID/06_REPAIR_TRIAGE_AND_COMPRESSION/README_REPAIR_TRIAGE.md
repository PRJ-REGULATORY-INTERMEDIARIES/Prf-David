# 06 — Repair triage and compression

## R4.2E-A — deterministic triage

`R4_2E_A_triage/` holds a deterministic heuristic run across all 1,404 records, classifying each
as a repair candidate: **YES 713, UNCERTAIN 346, NO 345**, with complexity NONE 345, SIMPLE 160,
MODERATE 514, COMPLEX 385.

These are **candidate signals, not confirmed defects**. The heuristic was validated against the
known human cases and rediscovered **9 of 12**, missing three that remain recorded blind spots in
`R4_2E_A_HUMAN_CASE_RULE_REDISCOVERY.csv`. A step that misses a quarter of known defects is a
triage device, not a detector, and it was used only as the former.

Two focused audits sit alongside it: one on actor/action fragmentation and one on the
counterpart/recipient coding burden, the latter feeding directly into the parsimony question.

## R4.2E-B0 — compression

`R4_2E_B0_compression/` holds the compression of 524 candidate records into **211 repair
families** sharing a structural signature, reducing advanced review to **131 cases** and
reserving 185 for human-only handling.

`R4_2E_B0_REPAIR_FAMILY_REGISTER.csv` defines the families and their sizes;
`R4_2E_B0_REPAIR_SIGNATURE_REGISTER.csv` gives each record its signature and route. These two
files are what later made it possible to test whether a family's representative is actually
representative — and the advanced validation found that in six families it is not.

`R4_2E_B0_RELATIONAL_FIELD_STRATEGY.md` is worth reading directly. It froze the requirement that
counterpart and recipient be assessed independently, with a separate rationale each, and recorded
the 995/995 identity as an operational property explicitly **not** as theoretical equivalence.

`R4_2E_B0_HEURISTIC_BLIND_SPOTS.md` documents the known limitations honestly rather than leaving
them implicit.

```text
RIT_CODING             = NOT_STARTED
MECHANISM_CODING       = NOT_STARTED
ROTEM_CODING_CONSULTED = NO
R4_3                   = NOT_STARTED
CORPUS_WIDE_REPAIR     = NOT_EXECUTED
```
