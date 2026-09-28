# R4 Digital Regulatory Intermediation Validation
## Complete Research and Traceability Package

**Author:** Igor Caires Machado
**Research context:** collaboration with Professor David Levi-Faur
**Round:** R4 cross-domain structural validation round
**Package built:** 27 September 2026

---

## If you only read two files

1. `01_FINAL_R4_DATASET/R4_Digital_Validation_Dashboard.xlsx` — the final consolidated
   R4 delivery dataset (Dashboard, Key Findings, Metrics, Source Data, Method Notes).
2. `02_EXECUTIVE_REPORTS/R4_DIGITAL_VALIDATION_MEMO_FOR_DAVID.md` — the memo explaining
   what was found, what it means, and what it does not mean.

**If you want the full method:** `00_START_HERE/R4_COMPLETE_WORK_NOTE.md`.
**If you want to audit every file:** `00_START_HERE/R4_FILE_GUIDE.md` and
`00_START_HERE/R4_TRACEABILITY_MAP.csv`.
**If you want to verify integrity:** `10_FREEZE_AND_INTEGRITY/` and
`00_START_HERE/R4_PACKAGE_MANIFEST.csv`.

---

## What R4 tested

R4 asks whether the regulatory-intermediation dataset architecture developed from
green-transition regulation is **structurally portable** to digital regulation, and which of
its variables are worth their coding cost. It tests the architecture against three EU
instruments:

- **GDPR** — Regulation (EU) 2016/679 (`32016R0679`)
- **Digital Services Act** — Regulation (EU) 2022/2065 (`32022R2065`)
- **AI Act** — Regulation (EU) 2024/1689 (`32024R1689`)

This is the **R4 digital structural validation round**. It is not the substantive
Green × Digital governance comparison, which has not been performed.

## The structural dataset

Structural extraction produced **1,404 records** — GDPR 485, DSA 424, AI Act 495 — on the unit

> **LEGAL PROVISION × ACTOR × LEGAL ACTION**

with fields for Actor, Action, Object, Counterpart and Recipient, plus supporting fields for
the legal verb, modality, conditions, triggers, outputs and cross-references.

`R4_STRUCTURAL_EXTRACTION.csv` is the immutable source dataset. It was read only and is
unmodified.

## Methodological stages

| Stage | What it did |
| --- | --- |
| R4.0 | Preserved and reconciled the R3 green baseline; froze it |
| R4.1 | Built the digital corpus from official EU sources; froze the original texts and indexed their structure |
| R4.2 | Deterministic structural extraction of 1,404 records |
| R4.2B | Stratified human QA; ambiguity typology; confidence calibration |
| R4.2C | Cross-model review (Luna and Terra) with explicit provenance correction |
| R4.2D | Human diagnostic on 12 purposively selected cases; 15 candidate structural rules frozen |
| R4.2E-A | Deterministic candidate triage across all 1,404 records |
| R4.2E-B0 | Compression into 211 repair families; advanced workload reduced from 524 to 131 cases |
| R4.2E-B1 | Advanced legal validation of 143 cases, including 12 NO_REPAIR diagnostic controls |
| R4.2E-B1S | Post-hoc Action representation sensitivity audit |
| — | Variable-parsimony analysis and final consolidation |

## Human authority

**Igor Caires Machado** is the final methodological authority for all theoretical decisions,
human adjudication, acceptance or rejection of candidate rules, interpretation, research design
and scientific conclusions.

AI systems were used for extraction assistance, structural review, diagnostic proposal, QA and
sensitivity analysis. **AI output is not autonomous ground truth.** Where a model and the human
researcher disagreed, the human decision governs, and the R4.2D human diagnostic explicitly
records that the model detection pattern frequently differed from the human root cause.

## Model provenance

| Work | Provenance |
| --- | --- |
| Initial extraction and early QA | Luna — see `09_MODEL_PROVENANCE/R4_AI_EXECUTION_LOG.csv` |
| B1-01, B1-02, B1-03 | `REQUESTED_MODEL = GPT-5.6 Terra High`; `RESEARCHER_SELECTED_MODEL = GPT-5.6 Terra High`; `MODEL_RUNTIME_VARIANT = MODEL_VARIANT_NOT_EXPOSED` |
| B1-04 and the B1S sensitivity audit | `RESEARCHER_SELECTED_MODEL = Claude Opus 5.5 Extra High`; `RUNTIME_REPORTED_MODEL = Claude Opus 5`; `RUNTIME_MODEL_ID = claude-opus-5`; `MODEL_SELECTION_RUNTIME_MATCH = NOT_VERIFIABLE` |

The runtime did not verify the researcher's Claude selection, and the two labels are **not**
asserted to be equivalent. Both are recorded verbatim throughout.

## Headline results

- **143 / 143** advanced-validation cases completed and reconciled: 99 family representatives,
  32 individual advanced cases, 12 NO_REPAIR diagnostic controls.
- Frozen B1 defect decisions: **YES 111, PARTIALLY 15, NO 17, ABSTAIN 0**. These describe a
  purposively enriched review set and are **not** corpus prevalence.
- **Counterpart and Recipient** are textually identical across all 1,404 rows, yet advanced
  review found 27 recipient-only and 14 counterpart-only propositions and no case where one
  entity genuinely occupies both. The extraction operationally collapsed two positions that can
  be distinct. Automatic merger is **not** recommended.
- **Action object / Information-or-material object** are identical across all 1,404 rows with no
  case distinguishing them — a strong redundancy candidate.
- **Structural ambiguity** is derivable one-way from **Extraction confidence**; the latter carries
  more information. The two are not equivalent.
- The Action variable is a construct across `LEGAL_ACTION`, `LEGAL_VERB` and `MODALITY`. The B1
  review input exposed only the first, so a post-hoc audit re-examined all 143 Action judgments:
  Action corrections **87 (frozen) versus 63 (sensitivity-adjusted)**, 26 judgments changed, and
  only **1 of 143** overall defect decisions materially affected.
- Repair templates: **zero unconditional validations**; 64 conditionally validated
  representatives across **50 conditionally validated repair families**, a potential coverage
  ceiling of **296 records**. No repair was applied.
- `B0_COMPRESSION_REASSESSMENT_REQUIRED` — a finding about coverage and family
  representativeness, not proof that the corpus is broadly corrupted.

## Scope limitation — what has NOT been done

```text
RIT_CODING            = NOT_STARTED
MECHANISM_CODING      = NOT_STARTED
ROTEM_CODING_CONSULTED = NO
R4_3                  = NOT_STARTED
CORPUS_WIDE_REPAIR    = NOT_EXECUTED
```

Regulator / intermediary / target coding and mechanism coding are the next analytical layer and
have not begun. Rotem's independent coding has deliberately not been consulted, so that the later
comparison remains a genuine independent inter-coder and inter-method test. No corpus-wide repair
was executed, and the 1,404-record extraction is unmodified.

Final status: `R4_2E_B1_ACTION_SENSITIVITY_AUDIT_COMPLETE` and
`R4_DIGITAL_STRUCTURAL_VALIDATION_READY_FOR_DAVID` — **not** `R4_COMPLETE`.

## Package layout

```text
00_START_HERE/                    entry point, file guide, traceability map, manifest
01_FINAL_R4_DATASET/              final consolidated delivery dataset
02_EXECUTIVE_REPORTS/             memo and cover email
03_SOURCE_DATA_AND_CORPUS/        the 1,404-record source and the corpus registers
04_R4_2_STRUCTURAL_EXTRACTION/    extraction-stage registers and logs
05_QA_AND_HUMAN_ADJUDICATION/     R4.2B QA, R4.2C cross-model, R4.2D human diagnostic
06_REPAIR_TRIAGE_AND_COMPRESSION/ R4.2E-A triage and R4.2E-B0 compression
07_ADVANCED_VALIDATION_B1/        the four B1 batches, controls and combined reports
08_ACTION_SENSITIVITY_AUDIT/      B1S audit and variable redundancy audit
09_MODEL_PROVENANCE/              execution and escalation logs
10_FREEZE_AND_INTEGRITY/          freeze records, manifests, superseded-but-preserved files
11_REPRODUCIBILITY/               the scripts that generated the artifacts
12_ARCHIVE_SUPPORT/               baseline, protocol and governance materials
```

Every file in this package is documented individually in `R4_FILE_GUIDE.md` and machine-readably
in `R4_TRACEABILITY_MAP.csv`, with its phase, evidence level, model provenance and SHA-256.
