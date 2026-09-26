# R4 PRE-R4.2 CHECKPOINT

**Checkpoint date:** 2026-09-26  
**Repository:** `git-PRJ-REGULATORY-INTERMEDIARIES--Prf-David`  
**Checkpoint status:** `PRE_R4_2_BASELINE_FROZEN`

## Phase nomenclature

- `R4.0 — BASELINE_AND_AI_PROTOCOL`: initial setup, AI protocol and frozen-baseline logic.
- `R4.1 — DIGITAL_LEGAL_CORPUS`: acquisition, validation, normalization, provenance and freeze of GDPR, DSA and AI Act.
- `R4.1B — R3_HISTORICAL_INTEGRATION`: read-only historical R3 inventory and reconciliation.
- `R4.1C — COMMUNICATIONS_PROVENANCE`: communications and transmitted-deliverable provenance archive.
- `R4.2 — AI_ASSISTED_STRUCTURAL_EXTRACTION`: not authorized and not started.

Historical execution labels previously using `R4.2` are preserved in `R4_AI_EXECUTION_LOG.csv` and reclassified through explicit fields. See `R4_PREEXISTING_R4_2_CHANGE_AUDIT.csv`.

## R4.0 — Baseline and AI protocol

Status: `COMPLETE`

The governing protocol remains active. Human review remains required for substantive interpretation and adjudication.

## R4.1 — Digital legal corpus

Status: `COMPLETE`

Cases:

- GDPR — `VALIDATED_AND_FROZEN`
- DSA — `VALIDATED_AND_FROZEN`
- AI Act — `VALIDATED_AND_FROZEN`

The three official English EUR-Lex XHTML originals and processing copies are preserved and structurally validated. Existing validation notes and the requirement for human corpus acceptance remain visible; no substantive legal coding was performed.

## R4.1B — R3 historical integration

Status: `COMPLETE`

- Archive: `PRJ-DAVID-R3.zip`
- Archive SHA-256: `DBF2C57CE66512A20563A455686B683CAD1C03DD03F8812C47FA49BD94D49713`
- Files inventoried: `127`
- Reconciliation: `R3_HISTORY_INTEGRATED_AS_READ_ONLY_PROVENANCE`
- Read-only status: `R3_HISTORY = INTEGRATED_AND_RECONCILED`
- Empirical modification: `NO`

The authoritative layers remain separated as `R3_ORIGINAL`, `R3_AUTHORITATIVE_BASELINE` (the researcher-adjudicated recovered records and frozen R3 package) and `R4_WORKING_REFERENCE`. The historical archive is not imported as pre-coded R4 data.

## R4.1C — Communications provenance

Status: `COMPLETE_WITH_DOCUMENTED_GAPS`

- 8 communications indexed;
- 2 primary representations preserved;
- 6 records based on secondary references;
- 14 deliverables mapped;
- 5 research requests;
- 4 decision/feedback items;
- 2 documented threads.

`COMMUNICATIONS_PROVENANCE = COMPLETE_WITH_DOCUMENTED_GAPS`. Original communications, secondary references, researcher notes and AI summaries remain distinguished. The gaps do not block R4 and were not filled by inference.

## R3 authoritative baseline

Status: `FROZEN`

Reconciliation totals: 5 laws; 89 LAW × ACTOR records; 56 adjudicated relations; 9 supported intermediation relations; 7 LAW × INTERMEDIARY units; 10 mechanism events; 1 sequential configuration; 1 substantive-zero law.

## R3 mechanism codebook

Status: `FROZEN`

The R3 codebook and researcher decision `R3-D08-IMPLEMENTATION` remain historical/provisional R3 material. They are not silently promoted to universal R4 mechanisms.

## Rotem coding

Status: `NOT_CONSULTED`

## Digital structural extraction

Status: `NOT_STARTED`

## Digital R–I–T coding

Status: `NOT_STARTED`

## Digital mechanism coding

Status: `NOT_STARTED`

The directories `03_extraction/`, `04_coding/` and `05_mechanisms/` contain no files. No `PREMATURE_R4_OUTPUT` was found.

## Pre-existing R4.2 change audit

`R4_PREEXISTING_R4_2_CHANGE_AUDIT.csv` contains 155 individually inventoried files. Results: 155 `MISLABELED_BASELINE`, 0 `PREPARATORY_NON_SUBSTANTIVE` file entries, 0 `PREMATURE_R4_OUTPUT` and 0 `UNRESOLVED`. The 127-file historical staging tree is reclassified to `R4.1B`; the 21-file communications archive and related provenance records are reclassified to `R4.1C`.

## Next phase

`R4.2 — AI-Assisted Structural Extraction`

Requires explicit researcher authorization. This checkpoint is the stop boundary; no extraction, actor identification, regulator identification, target identification, intermediary identification, mechanism search, mechanism classification or Rotem comparison begins here.
