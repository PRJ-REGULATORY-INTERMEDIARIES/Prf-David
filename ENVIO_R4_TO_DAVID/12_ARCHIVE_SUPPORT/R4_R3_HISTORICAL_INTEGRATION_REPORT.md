# R4.1B — R3 historical integration and baseline reconciliation

**Historical task label preserved:** `R4.2` in the original execution record. Reclassified to `R4.1B` because this operation is historical provenance and baseline reconciliation, not substantive digital extraction.

**Status:** `R3_HISTORY_INTEGRATED_AS_READ_ONLY_PROVENANCE`

**Date:** 2026-09-26

**Current project:** `C:\PROJETOS\GITHUB\git-PRJ-REGULATORY-INTERMEDIARIES--Prf-David`

**Historical source:** `G:\Meu Drive\VSCODE_WORK_IN_PROGRESS\PRJ-DAVID-R3.zip`

## 1. Scope and non-modification rule

This R4.2 operation reconstructed the completed R3 record from the historical ZIP and integrated it into the R4 workspace as auditable provenance. The ZIP was treated as read-only. No file inside the ZIP was modified, and no R3 empirical record was corrected, recoded, or rewritten.

The extracted copy is isolated at:

`01_baseline/R3_HISTORY_STAGING/PRJ-DAVID-R3/`

The R4 package distinguishes three things:

1. historical R3 evidence and decisions;
2. methodological lessons that can inform R4 governance;
3. empirical classifications that must not be imported into current R4 coding.

No substantive analysis of GDPR, DSA, or AI Act was performed in this phase.

## 2. Archive integrity and inventory

| Item | Result |
|---|---|
| Source ZIP SHA-256 | `DBF2C57CE66512A20563A455686B683CAD1C03DD03F8812C47FA49BD94D49713` |
| Source ZIP size | 3,363,189 bytes |
| Extracted files | 127 |
| Relative paths | Preserved under the `PRJ-DAVID-R3/R3_CLEANROOM` archive structure |
| File inventory | `R4_R3_HISTORY_FILE_INVENTORY.csv` |
| Archive metadata | `R4_R3_HISTORY_ARCHIVE_METADATA.json` |

The inventory records relative path, local staging path, file name, extension, file type, analytical function, size, last-write timestamp and SHA-256 for every extracted file. The reproducible inventory script is `09_logs/build_r4_2_history_inventory.ps1`.

### Analytical-function inventory

| Historical function | Files |
|---|---:|
| Root/final historical artifacts | 3 |
| Governance and researcher decisions | 6 |
| Source provenance | 11 |
| Corpus reconstruction and validation | 33 |
| Whole-instrument profiling | 6 |
| Actor layer | 3 |
| LAW × intermediary layer | 4 |
| Relation and R–I–T layer | 7 |
| Mechanism layer | 10 |
| Configuration layer | 7 |
| Dataset architecture and research questions | 8 |
| David-facing dataset/presentation layer | 11 |
| Audit history and quality gates | 18 |
| **Total** | **127** |

## 3. Historical archive topology

The historical archive contains the clean-room structure under `R3_CLEANROOM`:

`00_governance → 01_sources → 02_corpus → 03_instrument_profiles → 04_actor_register → 05_law_intermediary → 06_relations → 07_mechanisms → 08_configuration → 09_research_questions → 10_dataset → 12_audits`

The archive also contains three root-level final artifacts: the email to David, the R3 technical note and the R3 dataset workbook. These are presentation/final-package records and do not override normalized tables.

## 4. Authority hierarchy used for reconciliation

The following hierarchy was applied without flattening the R3 process:

1. researcher-adjudicated final records and explicit researcher decisions;
2. final adjudicated normalized tables;
3. phase-specific candidate, uncertainty and boundary tables;
4. presentation workbooks and David-facing summaries.

Accordingly, the authoritative historical mechanism record is `MECHANISM_EVENTS_RESEARCHER_ADJUDICATED.csv`, while the earlier `MECHANISM_UNRESOLVED` and `CODEBOOK_BOUNDARY` records remain indispensable provenance. The Excel workbooks were inspected as presentation layers; they were not treated as the analytical source of truth.

## 5. R3 historical pipeline reconstructed

The audit files reconstruct the following sequence:

`official source acquisition`

→ `corpus reconstruction and validation`

→ `whole-instrument profiling`

→ `actor inventory`

→ `candidate regulatory relations`

→ `three-condition R–I–T adjudication`

→ `LAW × INTERMEDIARY consolidation`

→ `mechanism identification`

→ `adversarial mechanism review`

→ `researcher adjudication`

→ `mechanism configuration`

→ `dataset architecture`

→ `David-facing dataset proposal`

The historical process used five original-as-adopted EU climate-law instruments: `32003L0087`, `32015D1814`, `32018R0842`, `32021R1119` and `32023R0955`. The R3 source policy excluded consolidated versions from primary coding. External instruments cited by the acts were recorded as dependencies but were not imported into the R3 corpus.

## 6. Historical source and corpus limitations

All five R3 sources were acquired from EUR-Lex in English, with successful retrieval, source hash and page-span checks. The source register records the original-act status and excludes consolidated versions from coding.

The corpus register records structural checks as `STRUCTURAL_CHECK_PASS_REVIEW_REQUIRED` and corpus status as `CORPUS_TEXT_REQUIRES_REVIEW`. Phase 2B subsequently recorded one correction: a standalone lowercase `i` in the 32023R0955 Annex I formula had initially been removed by a case-insensitive header filter and was restored. The historical audit states that all five cases passed source-hash, normalized-text and manifest-hash checks after correction.

These are historical corpus-status and provenance facts. They are not silently upgraded to the R4.1 status vocabulary.

## 7. R3 decision history that must remain visible

### Clean-room and role neutrality

R3 separated methodological learning from empirical ground truth. The firewall register explicitly marked prior Pilot A, R2/R2.1, prior versions, prior datasets, prior corpora, prior coding and prior review outputs as forbidden empirical inputs. Actors were registered before R/I/T assignment, and roles were treated as relation-specific rather than fixed actor properties.

### Three-condition R–I–T gate

The final R3 logic required all three conditions:

1. an identifiable regulator–target relation;
2. a distinct institutionalized third-party role;
3. a demonstrable mediating function connecting that third actor to the R–T relation.

Advice, consultation, expertise, institutional presence and non-bindingness alone were not sufficient. Direct R–T relations, legal non-RIT relations and supported intermediation were kept distinct.

### Phase 6B corrections and adjudications

The OLAF candidate in `REL-32023-015` was resolved to `DIRECT_R_T` because the act did not demonstrate an intermediary object, transformation, output and recipient linking OLAF into the Commission–Member State relation. Three auction-platform relations were corrected to `E2_CROSS_PROVISION_RECONSTRUCTED` because their identity and operative consequences required combining recital 6 with Article 1. These changes were recorded with hashes and did not create intermediary units.

### Researcher decision `R3-D08-IMPLEMENTATION`

Three supported relations involving material programme implementation and delivery were retained as supported intermediation. The researcher added `IMPLEMENTATION` as a tenth elementary mechanism rather than broadening `TRANSLATION`. The mechanism remains `FAMILY_UNASSIGNED_PROVISIONAL`, R3-specific, provisional, non-universal and not attributed to David Levi-Faur. The historical sequence remains queryable as:

`MECHANISM_UNRESOLVED → CODEBOOK_BOUNDARY → R3-D08-IMPLEMENTATION → IMPLEMENTATION`

### Negative and zero cases

The R3 record preserves 24 `DIRECT_R_T` relations, 23 `LEGAL_RELATION_NON_RIT` relations and one substantive-zero law, `32015D1814`. A zero intermediary count is an empirical result, not missing data. The three implementation events repeat across separate target-specific relations and are not treated as a chain.

## 8. Reconciliation results

The authoritative R3 totals were independently recomputed from the extracted normalized tables. All required comparisons passed. Full machine-readable results are in `R4_R3_RECONCILIATION.csv`.

| Metric | Frozen/reconciled value |
|---|---:|
| Instruments | 5 |
| LAW × ACTOR records | 89 |
| Actor–provision mappings | 173 |
| Candidate/adjudicated relations | 56 |
| Direct R–T relations | 24 |
| Legal non-RIT relations | 23 |
| Supported intermediation relations | 9 |
| LAW × INTERMEDIARY units | 7 |
| Researcher-adjudicated mechanism events | 10 |
| `VERIFICATION` events | 4 |
| `EVALUATION_ASSESSMENT` events | 3 |
| `IMPLEMENTATION` events | 3 |
| Relation configurations | 9 |
| Single-mechanism relations | 8 |
| Sequential relations | 1 |
| Confirmed mechanism edges | 1 |
| Substantive-zero laws | 1 |

The five-case R3 pilot does not support population prevalence, causal inference, validated latent dimensions, statistical association, governance-outcome claims or an exhaustive mechanism taxonomy.

## 9. R3-to-R4 integration boundaries

The detailed machine-readable map is `R4_R3_TO_R4_INTEGRATION_MAP.csv`. The governing rule is:

> R3 historical classifications are evidence of what R3 did, not pre-coded answers for R4.

R3 source and corpus procedures may inform R4 provenance and quality-control design. R3 actor, relation, intermediary, mechanism and configuration rows remain reference-only for current R4 substantive coding. The R3 unit architecture, negative-case discipline, decision provenance and firewall principles may be reused as method, but any R4 case must be independently acquired, frozen and coded under the R4 protocol.

In particular:

- R3 `IMPLEMENTATION` is not a universal R4 mechanism;
- R3's 3–4–2 family grouping is not a validated R4 taxonomy;
- `Knowing`, `Assuring`, `Steering` and RIA remain non-coded;
- no R3 case, actor, relation or mechanism was merged with the R4 GDPR, DSA or AI Act corpus;
- the R4.1 digital legal corpus remains a separate official-source freeze.

## 10. Presentation-layer inspection

The main R3 workbook was inspected as a human-facing view and contains 15 sheets, including instruments, LAW × INTERMEDIARY, supported relations, mechanism events, configurations, negative baseline, substantive zero, evidence, decision provenance, research questions and data architecture. Its grouped companion contains one `GROUPED_VIEW` sheet with 29 display rows. These workbooks reconcile to the normalized records but do not override them.

## 11. R4.1B completion status

`R3_HISTORY_INVENTORIED = YES`

`R3_HISTORY_EXTRACTED_TO_ISOLATED_STAGING = YES`

`R3_HISTORY_SOURCE_ZIP_MODIFIED = NO`

`R3_EMPIRICAL_RECORD_MODIFIED = NO`

`R3_TOTALS_RECONCILED = YES`

`R3_TO_R4_BOUNDARIES_DOCUMENTED = YES`

`R4_SUBSTANTIVE_CODING_PERFORMED = NO`

The historical integration is complete as a read-only R4 baseline. Any future R4 actor, relation, mechanism or cross-domain coding requires separate explicit authorization and must not overwrite this record.

## 12. Phase reclassification note

The historical execution entry `R4_2_HIST_001` is retained in `R4_AI_EXECUTION_LOG.csv` for chronological transparency. Its phase is reclassified as:

- `PHASE_RECLASSIFIED_FROM = R4.2`
- `PHASE_RECLASSIFIED_TO = R4.1B`
- `REASON = Historical R3 integration is a baseline/provenance operation and predates substantive digital extraction.`
