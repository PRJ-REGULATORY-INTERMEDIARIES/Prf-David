# 01 — Final R4 dataset

## Final consolidated delivery dataset

**`R4_Digital_Validation_Dashboard.xlsx`**

Status: `FINAL_R4_CONSOLIDATED_DATASET` / `FINAL_R4_DELIVERY_DATASET`

Purpose: the researcher-facing consolidation of the R4 digital structural-validation findings.
It integrates the final interpreted metrics, the source summary and the interpretation
guardrails needed to understand the result of this round without reading the full evidence
chain.

Worksheets:

| Sheet | Contents |
| --- | --- |
| **Dashboard** | Headline figures — 1,404 structural records, 143 advanced-reviewed cases, 63 sensitivity-adjusted Action corrections, 296 potential template coverage — with per-act records, reviewed counts and review share, plus four charts: corpus and B1 review by act, B1 defect decisions by act, field corrections proposed, and relational differentiation. |
| **Key Findings** | Executive interpretation in five numbered findings — structural portability, variable parsimony, Action sensitivity, repair templates, diagnostic controls — followed by an explicit "what is NOT yet concluded" block. |
| **Metrics** | Normalised per-act and total metrics behind the charts, each row carrying its own method note (for example "Within B1 only", "Purposive/enriched validation set"). |
| **Source Data** | The full dimension-by-instrument table, mirroring `R4_DIGITAL_VALIDATION_SUMMARY_FOR_DAVID.csv`. |
| **Method Notes** | Interpretation guardrails: B1 review design, sampling interpretation, the Action sensitivity audit, the status of the controls, the compression gate, template validation, the untouched original corpus, the next analytical layer, and the independence firewall. |

> The Excel workbook is the final consolidated R4 delivery dataset. It integrates the final
> validated R4 findings in a researcher-facing format with dashboard, metrics, methodological
> notes and source-summary views. The original 1,404-row structural extraction remains preserved
> separately as the immutable source dataset and was not corpus-wide repaired.

## Supporting summary

**`R4_DIGITAL_VALIDATION_SUMMARY_FOR_DAVID.csv`**

Status: `FINAL_R4_EXECUTIVE_SUMMARY_DATA`

The same aggregate table in plain CSV, for anyone who wants the numbers without the workbook.
It reports both the frozen and the sensitivity-adjusted Action correction counts side by side.

## Immutable structural source

`R4_STRUCTURAL_EXTRACTION.csv`, in `03_SOURCE_DATA_AND_CORPUS/`, holds the **1,404 original
structural records** and remains the frozen source extraction. It was read only throughout R4
and is unmodified.

```text
CORPUS_WIDE_REPAIR = NOT_EXECUTED
```

No repaired 1,404-row corpus was produced, and none is claimed. The Excel workbook is the final
consolidated R4 **delivery** dataset; the 1,404-row extraction remains the immutable underlying
**structural** dataset. The two serve different purposes and neither replaces the other.

```text
RIT_CODING             = NOT_STARTED
MECHANISM_CODING       = NOT_STARTED
ROTEM_CODING_CONSULTED = NO
R4_3                   = NOT_STARTED
CORPUS_WIDE_REPAIR     = NOT_EXECUTED
```
