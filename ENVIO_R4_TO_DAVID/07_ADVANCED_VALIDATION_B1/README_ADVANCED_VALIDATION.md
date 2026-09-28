# 07 — Advanced validation (R4.2E-B1)

143 cases reviewed against the frozen legal sources: 99 family representatives, 32 individual
advanced cases and 12 NO_REPAIR diagnostic controls, in four frozen batches.

## `batch_outputs/`

The four authoritative outputs. B1-01, B1-02 and B1-03 were produced with GPT-5.6 Terra High
under OpenAI Codex; B1-04 was produced in Claude Code after that environment reached its usage
limit. No earlier batch was rerun or relabelled. Each row carries its own model provenance.

Frozen results across all 143 cases: **YES 111, PARTIALLY 15, NO 17, ABSTAIN 0**. Anchor
confidence HIGH 124, MEDIUM 12, LOW 7. Field corrections: Actor 47, Action 87, Object 83,
Counterpart 88, Recipient 98.

**These are not corpus prevalence.** The set was built by concentrating suspected defects.

## `design/`

The frozen batch allocation and manifest, plus `R4_2E_B1_BLIND_SUBSTANTIVE_REVIEW_INPUT.csv` —
the exact input reviewers saw. That last file is worth opening: it exposes `LEGAL_ACTION` and not
`LEGAL_VERB` or `MODALITY`, which is the design flaw the sensitivity audit in folder 08 then
quantified.

## `diagnostic_controls/`

The control sample and the per-batch results, consolidated in
`R4_2E_B1_CONTROL_DIAGNOSTIC_CONSOLIDATED.csv`: **CLEAN_CONFIRMED 5, DEFECT_FOUND 7,
PARTIAL_DEFECT 0, ABSTAIN 0, SERIOUS 0**.

These are **NO_REPAIR diagnostic controls**, not blind controls. The control sample file lists
all twelve with no batch column and the protocol requires reading it to unblind each batch, so
blinding was not guaranteed. No false-negative rate is calculated from them.

## `freeze_records/`

One per batch. The B1-04 record also documents the corrected Claude provenance and three recorded
design limitations: the blinding compromise, the schema under-exposure, and the cross-model
threshold difference.

## `combined_reports/`

`R4_2E_B1_METHOD_REPORT.md` is the full method report, including the sensitivity audit and the
reasoning behind `B0_COMPRESSION_REASSESSMENT_REQUIRED`. `R4_2E_B1_FINAL_SUMMARY.csv` holds the
reconciled metrics. `R4_2E_B1_NEW_STRUCTURAL_DIAGNOSTIC_CANDIDATES.csv` records seven new issues
for adjudication without altering the 15 frozen rules. `R4_2E_B1_HANDOFF_STATE.md` states the
current position and the unresolved questions.

```text
RIT_CODING             = NOT_STARTED
MECHANISM_CODING       = NOT_STARTED
ROTEM_CODING_CONSULTED = NO
R4_3                   = NOT_STARTED
CORPUS_WIDE_REPAIR     = NOT_EXECUTED
```
