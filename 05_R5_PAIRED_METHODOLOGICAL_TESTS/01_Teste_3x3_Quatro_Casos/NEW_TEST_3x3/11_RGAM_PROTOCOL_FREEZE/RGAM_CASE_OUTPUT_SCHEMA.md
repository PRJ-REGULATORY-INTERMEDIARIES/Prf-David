# RGAM — CASE OUTPUT SCHEMA v1.0 (frozen before case execution)

Defines the file set each future case execution must produce. The authoritative field-level definition is `RGAM_PAIRED_DATA_DICTIONARY_v1_0.md`; blank header-only templates are in each capsule's `OUTPUT_TEMPLATES/` (one per table, identical headers). This schema is **case-general**.

## 1. Output location and naming

`12_RGAM_EXECUTION/<CAPSULE_ID>/` (created only when execution is separately authorized), containing exactly:

| # | File | Stratum | Required |
|---:|---|---|---|
| 1 | `W_DECLARATION.csv` | W | yes (1 row) |
| 2 | `SOURCE_UNIT_INVENTORY.csv` | E | yes (every unit) |
| 3 | `UNIT_SCREENING.csv` | E | yes (every unit) |
| 4 | `INSTITUTIONAL_STATEMENTS.csv` | E | yes |
| 5 | `NORMATIVE_ASSIGNMENTS.csv` | P | yes (may have zero rows) |
| 6 | `POSITIONS_AND_DEVICES.csv` | P | yes (may have zero rows) |
| 7 | `QUALIFIED_RELATIONS.csv` | R | yes (may have zero rows) |
| 8 | `EXTERNAL_REFERENCES.csv` | R/E | yes (may have zero rows) |
| 9 | `SUBCONFIGURATIONS.csv` | S | yes (may have zero rows) |
| 10 | `ARCHITECTURE_CANDIDATES.csv` | A | yes (may have zero rows) |
| 11 | `PROPERTY_REGISTER.csv` | S/A | yes (may have zero rows) |
| 12 | `CLOSURE_REGISTER.csv` | W/A | yes (≥1 COVERAGE row) |
| 13 | `PROVENANCE_LINKS.csv` | all | yes |
| 14 | `UNCERTAINTY_LOG.csv` | all | yes (may have zero rows) |
| 15 | `HUMAN_REVIEW_QUEUE.csv` | all | yes (human columns blank) |
| 16 | `TRACE_DEMONSTRATIONS.csv` | A | yes (≥1 row, or `NOT_APPLICABLE_NO_CANDIDATE`) |
| 17 | `INSTRUMENT_LEVEL_SUMMARY.csv` | profile | yes (1 row) |
| 18 | `PROTOCOL_DEVIATION_LOG.csv` | meta | yes (may have zero rows) |
| 19 | `RUN_METADATA.csv` | meta | yes (1 row) |
| 20 | `CASE_RGAM_REPORT.md` | narrative | yes (sections of §3) |

A zero-row table is a legitimate result (e.g., no subconfiguration warranted); the header must still be present. `NO_ARCHITECTURE_WARRANTED` and `INDETERMINATE` are valid instrument-level results; a table may not be padded to appear complete.

## 2. Stratum-to-file map (native chain)

`W` → W_DECLARATION · `E` → SOURCE_UNIT_INVENTORY, UNIT_SCREENING, INSTITUTIONAL_STATEMENTS · `P` → NORMATIVE_ASSIGNMENTS, POSITIONS_AND_DEVICES · `R` → QUALIFIED_RELATIONS, EXTERNAL_REFERENCES · `S` → SUBCONFIGURATIONS · `A` → ARCHITECTURE_CANDIDATES, TRACE_DEMONSTRATIONS · profile → PROPERTY_REGISTER, INSTRUMENT_LEVEL_SUMMARY · `M` (transversal) → `epistemic_status`, `legal_status_of_norm`, `depends_on_*`, `support_gap_report`, PROVENANCE_LINKS on every record · closure → CLOSURE_REGISTER · governance → UNCERTAINTY_LOG, HUMAN_REVIEW_QUEUE, PROTOCOL_DEVIATION_LOG, RUN_METADATA.

## 3. Narrative report (`CASE_RGAM_REPORT.md`)

Sections: (1) W declaration and coverage; (2) record counts by table (descriptors only); (3) subconfigurations and warrants; (4) candidate architectures with I1–I4, rival groupings and outcomes; (5) property register summary with scales, bearers and aggregation; (6) status profile; (7) closure and external-reference limitations; (8) open human-review items; (9) deviations and gaps; (10) statement of provisional status. The report contains no comparison with any other method or case, and no ranking, score or index.

## 4. Required self-checks at P9 (recorded in the report)

The ten referential-integrity rules of the data dictionary §4; units screened = units inventoried; every ARCH outcome INTEGRATED/OVERLAPPING has an HQ item; no QR with prohibition modality; no `material_establishment_evidenced` on relations; every EXT `not_checked`; human columns blank; traceability chains resolve.

## 5. What an output must never contain

A numeric score, composite, threshold or ranking; a graph index; a V8-vocabulary relabelling; content from another case or from any prior extraction; a human decision; an architecture asserted without I1–I4; a relation without two identified parties; a counterparty invented for an assignment; a claim above the status its evidence supports.
