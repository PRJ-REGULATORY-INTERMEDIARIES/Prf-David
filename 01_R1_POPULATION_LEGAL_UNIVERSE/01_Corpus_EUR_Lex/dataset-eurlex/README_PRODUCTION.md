# dataset-eurlex — Production Workflow

This file is the operational entry point for the simplified three-case production phase. The original `README.md` remains unchanged as the historical pilot instructions and must be retained for audit.

## Status

`SIMPLIFIED_PRODUCTION_WORKFLOW_READY`  
`EMPIRICAL_CODING_NOT_STARTED`

Case 01 is the existing European Climate Law corpus, copied into `cases/case_01/` with its source and hashes preserved. Cases 02 and 03 are now selected and corpus-locked under `docs/methodology/CASE_SELECTION_MATRIX.md`.

## Workflow

```text
official EU act → frozen corpus → Claude primary coding
→ Luna secondary review → researcher adjudication → final case dataset
```

Use the same `prompts/production/CLAUDE_PRIMARY_CODER.md` and `prompts/production/LUNA_SECONDARY_REVIEWER.md` for every case. The common matrix is defined by `methodology/production_v1.0/coding_matrix_schema.json`.

For each case, preserve source, corpus, hashes, codebook, prompts, model metadata, raw outputs, reviews, human decisions, and final data in the corresponding case directory. Do not create a final dataset before researcher adjudication.

## Key files

- `cases/CASE_REGISTRY.yaml` — case identity, provenance, hashes, and status;
- `config/production.yaml` — production roles, observable model metadata, and allowed states;
- `prompts/production/` — one prompt per production role;
- `methodology/production_v1.0/` — production schemas;
- `docs/methodology/CASE_SELECTION_PROTOCOL.md` — pre-coding case selection rules;
- `docs/methodology/METHODOLOGY_WORKING_DRAFT_SIMPLIFIED.md` — English working draft;
- `docs/methodology/LEGACY_PILOT_AND_SIMPLIFICATION_NOTE.md` — preserved pilot context.

## Prohibitions

Do not run new Terra R1/R2 or Claude R1/R2 replications, G0/G1/G2 executions, automated blind RA, majority voting, or silent output corrections. Claude and Luna propose; only the researcher produces final classifications.
