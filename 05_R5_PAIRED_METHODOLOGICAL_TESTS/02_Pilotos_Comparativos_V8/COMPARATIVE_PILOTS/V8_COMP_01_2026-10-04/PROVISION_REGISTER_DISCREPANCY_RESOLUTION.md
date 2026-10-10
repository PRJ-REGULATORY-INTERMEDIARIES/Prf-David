# Provision-register discrepancy resolution

**Date:** 2026-10-04  
**Scope:** historical `PILOT_03` provision-register copies; no source file was changed.

## Compared records

- **Canonical:** `../../RELATIONAL_LEXIMETRICS_PILOT/PILOT_03/03_SOURCE_PROVISIONS/PROVISION_REGISTER.csv` (FE-005; SHA-256 `EDBBB5A4C7BAB6334C6B8A195A7443899669180B8843B9359A9CC9E3ED1B59F0`).
- **Regression copy:** `../../AUTONOMOUS_ROTEM_COMPARISON_20260930_2047/05_PILOT03/regression_copy/RELATIONAL_LEXIMETRICS_PILOT/PILOT_03/03_SOURCE_PROVISIONS/PROVISION_REGISTER.csv` (preserved comparison artifact; not rewritten or substituted for FE-005).

## Result

The ten selected anchors are byte-for-field equivalent across the two CSV records: `P03_PR01`–`P03_PR04` and `P04_PR01`–`P04_PR06`. The files’ differing overall hashes arise from `capture_date` values in 15 unselected blind-challenge rows (`C01_PR01`–`C05_PR03`). No selected anchor, provision identifier, CELEX, source location, excerpt locator, or historic classification differs.

## Controlling record by question

| Question | Controlling record | Reason |
|---|---|---|
| Exact legal wording and legal version | FE-001 / FE-003 official legal HTML | Official primary text is authoritative. |
| Convenient line-level reading | FE-002 / FE-004 derived text | Paired rendering only; cannot override HTML. |
| Historical P03/P04 anchor selection and provenance | Canonical FE-005 | It is the frozen manifest’s declared historical record and passed integrity recheck. |
| Regression reproducibility check | Preserved regression copy | It is an independent historical comparator; it does not control legal text or replace FE-005. |
| Historical model/adjudication claims | FE-007–FE-009 | They evidence historical work only, not prospective Track A/B conclusions. |

## Relevance and disposition

There is no provenance conflict for the ten legal anchors used in this freeze. The discrepancy is material to broad historical reproducibility only and is explicitly retained rather than reconciled. `BLOCKED_SOURCE_INTEGRITY` is not triggered.
