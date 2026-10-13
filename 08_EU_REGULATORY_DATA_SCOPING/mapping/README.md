# mapping/ — Systematic Mapping of EU Legislative and Regulatory Data

Independent research under the scientific responsibility of Igor Caires Machado. Initiated at gate G2 (10 October 2026) after a redirection of the *EU Regulatory Data Scoping* study. All G0 through G1-READY artifacts remain outside this folder and were not modified.

**Status:** Round 2 completed (10 October 2026). The inventory contains **252 candidate resources**, all provisionally classified by an AI agent; **none of these rows has been confirmed by a human researcher**. The Round 1 state (105 candidates) is preserved in `snapshots/round1/`.

## Where to start

| Purpose | Open |
|---|---|
| Understand why the study was redirected | [Independent mapping reorientation](protocol/INDEPENDENT_MAPPING_REORIENTATION_v1_0.md) |
| Review search and verification procedures | [Systematic mapping protocol](protocol/SYSTEMATIC_MAPPING_PROTOCOL_v1_0_DRAFT.md) |
| Read the initial results | [Initial G2 report](reports/G2_INITIAL_MAPPING_REPORT.md) |
| Review the next steps | [Next-round plan](reports/G2_NEXT_ROUND_PLAN.md) |
| Assess publication potential | [Publication potential note](reports/PUBLICATION_POTENTIAL_NOTE.md) |
| Inspect the data tables | [Resources table](data/resources.csv) and [data dictionary](data/DATA_DICTIONARY.md) |

## Round 2 documentation

| Purpose | Open |
|---|---|
| Results of the second round | [Round 2 results](reports/G2_ROUND2_RESULTS.md) |
| Data/infrastructure distinction and evidence levels | [Amendment A01](protocol/AMENDMENT_A01_DATA_VS_INFRASTRUCTURE_v1_0.md) |
| LYNX comparison and previous research | [Prior art and LYNX comparison](reports/PRIOR_ART_AND_LYNX_COMPARISON.md) |
| Proposed human validation | [Human validation proposal](protocol/HUMAN_VALIDATION_PROPOSAL_v0_1.md) |
| Changes made to Round 1 files | [Round 2 changes](CHANGES_ROUND2.md) |

## Folder structure

```text
mapping/
  protocol/    Research reorientation, protocol and round-specific search records
  curation/    Provisional coding judgments and evidence for each field
  data/        Generated data tables (do not edit manually) and data dictionary
  schemas/     Controlled vocabularies
  scripts/     Recorded searches, deterministic builder and validator
  evidence/    Search responses and captured source pages, with logs and checksums
  reports/     Reports, future-work plan, publication note and test outputs
  MANIFEST.sha256
```

## Reproduce the local outputs

```bash
python mapping/scripts/build_mapping_base.py   # Rebuild tables from curation and evidence
python mapping/scripts/validate_mapping.py     # Run consistency checks
python -m unittest discover -s tests            # 152 tests: 87 earlier, 26 from Round 1 and 39 from Round 2
```

These commands do not use the network. Network requests are made only by `mapping_search.py run` and `scripts/capture_evidence.py capture`.

## Start another round

1. Create `protocol/SEARCH_QUERIES_G2_ROUND<n>.csv` and run `python mapping/scripts/mapping_search.py run --registry <file>`.
2. Capture relevant pages with `scripts/capture_evidence.py` (output directory: `mapping/evidence/captures`).
3. Add provisional coding decisions to a curation file, then rebuild and validate the tables.
4. Never reuse `MR-nnnn` identifiers and never delete historical evidence.

## Interpretation and preservation cautions

- `VERIFIED` means that a resource's name and location were found in a preserved primary source. **No complete dataset was opened.**
- `NOT_ASSESSED` means not collected or examined, **not** that something does not exist.
- An access failure is not evidence of absence.
- `evidence/` contains third-party webpage captures. Before publishing that folder, establish whether redistribution is permitted.
