# Human audit protocol v4

`data/audit_sample_v4.csv` contains 20 held-out units, four per CELEX act,
selected with reproducible seed `20260906`. Existing v3 candidate articles
were excluded to prevent leakage.

Before any Tier 1 live AI run, the researcher must replace the explicit
`PENDING`/`NOT_YET_EXECUTED` fields with an independent adjudication record:

1. identify R, I and T without consulting AI output;
2. answer conditions (a)-(e) using the RIT codebook;
3. record positive, negative, conditional or insufficient evidence;
4. quote literal legal evidence and document any institutional reconstruction;
5. check for a distinct actor, multiple roles and cross-references.

Only after this independent adjudication may the same 20 units be run as
Tier 1. The adversarial test must omit one load-bearing cross-reference and
check whether the model requests context instead of answering from memory.

Until those steps are completed, every AI unit is routed to full human review,
including stable dry-run outputs.
