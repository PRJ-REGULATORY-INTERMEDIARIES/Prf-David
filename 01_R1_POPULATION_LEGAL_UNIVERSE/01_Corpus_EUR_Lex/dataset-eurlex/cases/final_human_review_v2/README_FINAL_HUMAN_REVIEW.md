# Final Human Review v2 — Actor-in-Role Architecture

## Purpose

This is the final structured package for researcher adjudication. It is **not** a final published dataset. It transforms the extant relationship evidence into an actor-in-role review surface; it does not perform a new legal-text search or recode the three acts.

## Four analytical levels

1. **Act / regulatory regime** — the documentary and comparative context.
2. **Actor-in-role** — the principal substantive unit: actor × act × role (and, only where needed, context).
3. **Intermediary function / mechanism** — the function and orientation recorded when the role is I.
4. **Regulatory relation / episode** — the coding and evidentiary layer that supports the role classification.

## Main scientific logic

Regulatory relationships establish evidence. Actors-in-role are the primary substantive units for mapping regulatory intermediation. Acts/regimes provide the comparative architecture. R/I/T are contextual roles, not permanent properties of organisations.

## Evidence and recital rule

The relation evidence file preserves operative anchors and quotations available in the source dataset. `NOT_RECOVERED` is retained where the damaged R2 relation CSV no longer preserved a quotation; it is not replaced with a new quotation. Recitals can support interpretation but cannot independently generate a positive relationship.

## Human decisions and provenance

The package distinguishes researcher decisions already recorded in R2, the current agent-derived transformation, and pending final adjudication. The source relation CSV was damaged after an earlier complete read: it is preserved untouched; the 20 base records in `FINAL_DATASET_FOR_HUMAN_REVIEW.csv` were reconstructed from that read plus surviving decision cells; five further relations were promoted from explicit researcher changes in the intact uncertainty file. See `06_PROVENANCE.csv` for the full trail. Missing human rationales are `NOT_RECORDED`, never invented.

## Files

- `01_RELATION_EVIDENCE.csv` — one record per relation/episode, including direct, uncertain, and not-supported records.
- `02_ACTOR_ROLE_MAP.csv` — the master actor × case × role map.
- `03_INTERMEDIARY_MECHANISMS.csv` — one intermediary actor-role × mechanism × case.
- `04_ACT_REGIME_SUMMARY.csv` — one row per act.
- `05_UNRESOLVED_FOR_RESEARCHER.csv` — only issues requiring a substantive researcher decision.
- `06_PROVENANCE.csv` — source, reconstruction, method, prompt, and derivation trail.
- `ACTOR_NORMALIZATION_LOG.csv` — conservative name-normalization decisions.
- `FINAL_HUMAN_REVIEW_WORKBOOK.xlsx` — review workbook; CSVs remain canonical.

## Review instructions

Open `FINAL_HUMAN_REVIEW_WORKBOOK.xlsx`, begin with **UNRESOLVED_CASES**, then review **ACTOR_ROLE_MAP** and **INTERMEDIARY_MECHANISMS**. Fill only the blank `final_human_*` columns. Do not alter evidence or provenance columns. The one pending substantive item is `case_02-U07`; it remains `RESEARCHER_DECISION_REQUIRED` and is not promoted to the accepted data.

## Current derived counts

| Case | Relation evidence | Unique actors | R roles | I roles | T roles | Unique intermediaries | Unresolved issues |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| case_01 | 8 | 8 | 2 | 3 | 3 | 3 | 0 |
| case_02 | 10 | 16 | 2 | 5 | 9 | 5 | 1 |
| case_03 | 7 | 13 | 2 | 4 | 7 | 4 | 0 |
| TOTAL | 25 | 37 | 6 | 12 | 19 | 12 | 1 |
| **TOTAL** | **25** | **37** | **6** | **12** | **19** | **12** | **1** |

These are three-case calibration results, not population estimates.
