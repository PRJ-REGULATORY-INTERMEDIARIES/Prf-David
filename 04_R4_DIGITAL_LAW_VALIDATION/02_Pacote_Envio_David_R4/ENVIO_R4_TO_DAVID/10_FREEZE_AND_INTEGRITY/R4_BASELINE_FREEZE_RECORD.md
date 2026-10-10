# R4 BASELINE FREEZE RECORD

**Freeze date:** 2026-09-26  
**Freeze status:** `PRE_R4_2_BASELINE_FROZEN`  
**Repository:** `C:\PROJETOS\GITHUB\git-PRJ-REGULATORY-INTERMEDIARIES--Prf-David`

## Phase boundary

This record freezes the boundary between historical evidence, methodological preparation and provenance (`R4.0`, `R4.1`, `R4.1B`, `R4.1C`) and new substantive digital analysis (`R4.2`). The historical labels used in earlier execution records are retained and reconciled; no historical record is silently rewritten.

## Frozen baseline components

- `R3_HISTORY = INTEGRATED_AND_RECONCILED` as read-only historical provenance;
- `R3_NORMALIZED_TABLES = RECOVERED` from the supplied 127-file historical archive;
- `R3_GRANULAR_LOGS = RECOVERED_OR_EXPLICITLY_LIMITED`, with the recovered decision, uncertainty, mechanism and audit records inventoried;
- `R3_AUTHORITATIVE_BASELINE = FROZEN`;
- `R3_CODEBOOK = FROZEN`;
- `DIGITAL_LEGAL_CORPUS = VALIDATED_AND_FROZEN` for the three preserved official-source cases;
- `COMMUNICATIONS_PROVENANCE = COMPLETE_WITH_DOCUMENTED_GAPS`;
- `AI_PROTOCOL = ACTIVE`;
- `ROTEM_CODING = NOT_CONSULTED`;
- `DIGITAL_STRUCTURAL_EXTRACTION = NOT_STARTED`;
- `DIGITAL_RIT_CODING = NOT_STARTED`;
- `DIGITAL_MECHANISM_CODING = NOT_STARTED`.

## Provenance and governance artifacts

- Historical archive hash and 127-file inventory: `R4_R3_HISTORY_ARCHIVE_METADATA.json`, `R4_R3_HISTORY_FILE_INVENTORY.csv`;
- R3 reconciliation: `R4_R3_RECONCILIATION.csv`;
- R3→R4 documentary boundary: `R4_R3_TO_R4_INTEGRATION_MAP.csv`;
- Communications provenance: `01_baseline/R3_ORIGINAL/communications/`;
- Phase/reclassification audit: `R4_PREEXISTING_R4_2_CHANGE_AUDIT.csv`;
- AI execution and escalation logs: `R4_AI_EXECUTION_LOG.csv`, `R4_MODEL_ESCALATION_LOG.csv`.

## Open provenance issues

1. The communications archive has documented gaps: some original messages and referenced files were not located. Secondary references remain secondary.
2. The official digital corpus retains `VALIDATED_WITH_NOTES` and human-acceptance notes in its source register; this does not authorize substantive coding.
3. Earlier `R4.2` labels remain in the historical execution log for chronological transparency and are explicitly reclassified to `R4.1B` or `R4.1C`.

These issues do not block the pre-R4.2 baseline. They must not be resolved by inference or by modifying historical source records.

## Pre-existing R4.2 audit result

`R4_PREEXISTING_R4_2_CHANGE_AUDIT.csv` identified 155 files, all classified as `MISLABELED_BASELINE`. No `PREMATURE_R4_OUTPUT` and no `UNRESOLVED` file was found. The empty directories `03_extraction/`, `04_coding/` and `05_mechanisms/` are preparatory scaffolding only and contain no files.

## Repository state and checkpoint

The validated baseline/provenance paths are isolated for path-specific staging. The unrelated `git-PRJ-REGULATORY-INTERMEDIARIES--Prf-David.code-workspace` file and unrelated prior R4.2 historical-integration working-tree items outside this validated set are excluded from the checkpoint.

`GIT_BASELINE_CHECKPOINT = COMMITTED_BY_POST-COMMIT_HANDOFF`

The commit hash, file count and remaining working-tree state are recorded in the final post-commit handoff. No pull or push is authorized by this checkpoint task.
