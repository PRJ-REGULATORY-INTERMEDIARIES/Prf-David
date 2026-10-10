# R3 — Phase 10B David Dataset Proposal Package Audit

## A. Package scope

The package was created at:

`10_dataset/DAVID_DATASET_PROPOSAL_V1/`

It translates frozen R3 findings and the approved Phase 10 architecture into a researcher-facing proposal. It does not replace normalized source tables, recode cases, derive capacities, or claim population-level results.

## B. Files created

1. `README_DAVID_PACKAGE.md`
2. `R3_EXECUTIVE_NOTE_FOR_DAVID.md`
3. `R3_DATASET_PROPOSAL_MEMO_FOR_DAVID.md`
4. `R3_DATASET_PROPOSAL_FOR_DAVID_V1.xlsx`
5. `R3_DAVID_GROUPED_VIEW.xlsx`
6. `R3_METHOD_PIPELINE_FOR_DAVID.md`
7. `R3_MECHANISM_CODEBOOK_RESEARCHER_ADJUDICATED.md`
8. `R3_DATASET_ARCHITECTURE_PROPOSAL.md`
9. `R3_DATA_DICTIONARY_DRAFT.csv`
10. `R3_RESEARCH_QUESTION_VARIABLE_MAP.csv`
11. `R3_DECISION_PROVENANCE_EXTRACT.csv`

The four copied support files are byte-identical to their approved upstream versions.

## C. Main-workbook reconciliation

`R3_DATASET_PROPOSAL_FOR_DAVID_V1.xlsx` contains exactly 15 requested sheets:

- README;
- R3_OVERVIEW;
- INSTRUMENTS;
- LAW_INTERMEDIARY;
- SUPPORTED_RELATIONS;
- MECHANISM_EVENTS;
- CONFIGURATIONS;
- NEGATIVE_BASELINE;
- SUBSTANTIVE_ZERO;
- CODEBOOK;
- EVIDENCE;
- DECISION_PROVENANCE;
- RESEARCH_QUESTIONS;
- DATA_ARCHITECTURE;
- DATA_DICTIONARY.

Reconciled frozen values:

| Observation | Package value |
|---|---:|
| laws | 5 |
| LAW × ACTOR records | 89 |
| adjudicated relations | 56 |
| `DIRECT_R_T` | 24 |
| `LEGAL_RELATION_NON_RIT` | 23 |
| `SUPPORTED_INTERMEDIATION` | 9 |
| LAW × INTERMEDIARY units | 7 |
| mechanism events | 10 |
| `VERIFICATION` | 4 |
| `EVALUATION_ASSESSMENT` | 3 |
| `IMPLEMENTATION` | 3 |
| `SINGLE_MECHANISM` relations | 8 |
| `MULTI_MECHANISM_SEQUENTIAL` relations | 1 |
| confirmed mechanism edges | 1 |
| substantive-zero laws | 1 |

No percentages or prevalence claims were calculated.

## D. Grouped-view reconciliation

`R3_DAVID_GROUPED_VIEW.xlsx` contains:

- 7 parent LAW × INTERMEDIARY rows;
- 9 child relation rows;
- 10 mechanism-event subrows;
- 26 analytical display rows in total.

No merged cells are used. Rows remain sortable and filterable. The three `IMPLEMENTATION` events appear under three separate target-specific relations, with no arrow between them. `REL-32023-014` retains its two event subrows and sequential configuration.

## E. Package readability checks

| David test | Result |
|---|---|
| D1 — research question understandable without internal audits | PASS |
| D2 — unit hierarchy understandable | PASS |
| D3 — intermediary attributes distinguishable from mechanisms | PASS |
| D4 — multiple relations per intermediary visible | PASS |
| D5 — multiple mechanisms per relation visible | PASS |
| D6 — researcher-adjudicated decisions identifiable | PASS |
| D7 — `IMPLEMENTATION` not mistaken for David's taxonomy | PASS |
| D8 — negative and zero cases visible | PASS |
| D9 — five-case possibilities and limits explicit | PASS |
| D10 — questions to David are conceptual, not coding requests | PASS |

The memo contains approximately 2,022 words. The executive note contains approximately 466 words and remains below the 700-word maximum.

## F. Provenance preservation

The package exposes five major decision areas:

- the three-condition RIT adjudication logic;
- the OLAF Phase 6B decision;
- auction-platform evidence-level adjudication;
- Phase 8B adversarial mechanism review;
- researcher decision `R3-D08-IMPLEMENTATION`.

Model-assisted structured coding/review, adversarial review, and researcher adjudication are visibly distinguished. The workbooks retain stable relation, intermediary, event, and source-anchor identifiers.

## G. IMPLEMENTATION representation

`IMPLEMENTATION` is shown as:

- a researcher-added provisional mechanism;
- authorized through `R3-D08-IMPLEMENTATION`;
- distinct from `TRANSLATION`;
- `FAMILY_UNASSIGNED_PROVISIONAL`;
- not attributed to David Levi-Faur;
- present in three distinct relations rather than a chain.

The historical unresolved and codebook-boundary stages remain visible through the decision extract and copied codebook/architecture materials.

## H. Negative-case representation

The `NEGATIVE_BASELINE` sheet contains all 47 non-positive adjudicated relations: 24 `DIRECT_R_T` and 23 `LEGAL_RELATION_NON_RIT`. It includes boundary flags and concise relation information without reproducing excessive evidence text.

## I. Zero-case representation

`32015D1814` is explicitly shown with zero supported intermediaries, zero supported intermediation relations, zero mechanism events, and zero configurations under:

`SUBSTANTIVE ZERO — NOT MISSING DATA`

## J. Research-question representation

The exact main research question appears in the executive note, memo, workbook README, and research-question sheet. RQ-A is identified as descriptively demonstrated by the five-case pilot. RQ-B is identified as structurally enabled but theoretically and empirically open.

The package makes the proposed hierarchy explicit:

`LAW → LAW × ACTOR → LAW × INTERMEDIARY → R–I–T RELATION → MECHANISM EVENT → MECHANISM CONFIGURATION → FUTURE REGULATORY CAPACITY`

It is presented as the researcher's proposal, not an endorsed model attributed to David.

## K. Capacity firewall

`REGULATORY_CAPACITIES_CODED = NO`

Knowing, Assuring, and Steering appear only as candidate theoretical ideas for later evaluation; no current case or configuration receives any of these labels.

## L. RIA firewall

`RIA_CLASSIFICATION_CREATED = NO`

No RIA type, architectural class, score, maturity, complexity, or empirical architecture finding was generated.

## M. New-analysis firewall

`NEW_SUBSTANTIVE_CODING_CREATED = NO`

The package contains presentation transformations and derived display summaries only.

## N. Unresolved presentation issues

`NONE_REQUIRING_PACKAGE_REVISION`

Future researcher choices may concern visual branding or whether to send the full grouped workbook, but these do not affect empirical reconciliation or conceptual readability.

## O. Package integrity

| File | SHA-256 |
|---|---|
| `README_DAVID_PACKAGE.md` | `1727F3189F075ED86816AA790876E77718BE49C0EC98C57BBA88A5A4B80FB79C` |
| `R3_EXECUTIVE_NOTE_FOR_DAVID.md` | `A6B1F5AD886CA0CC7221A3B759E52504F85B0E20B31E280A8B910251A4ACF782` |
| `R3_DATASET_PROPOSAL_MEMO_FOR_DAVID.md` | `697F98928750BFF582854B91A62529D56B07A5C42868C7615404D1F4229DB51E` |
| `R3_DATASET_PROPOSAL_FOR_DAVID_V1.xlsx` | `EE96829A560F998AF04579C47F4C4AF1A2855AE5C0AF102085A7F98A178634F9` |
| `R3_DAVID_GROUPED_VIEW.xlsx` | `03601C663E446D0F29F3E4AF7550763B549CC1996CB8ADE0A8F5BA6395E70EBD` |
| `R3_METHOD_PIPELINE_FOR_DAVID.md` | `7104A6967C51229CF685E4A63C53236E4BCFA5AA7F76FEEAE746E55D3CE0C012` |
| `R3_MECHANISM_CODEBOOK_RESEARCHER_ADJUDICATED.md` | `9EC2796D385DAB52EF0599857FA9C223D8DE33B7E9A99D650176448437A6F804` |
| `R3_DATASET_ARCHITECTURE_PROPOSAL.md` | `11170B93C4044E6E72EE16B65D0D2F68F276405916038D6F594FDEFDEBC9F6D0` |
| `R3_DATA_DICTIONARY_DRAFT.csv` | `A85E4B7C6528F79C63FCAFC6366AA6B2BF9977338473A82617C1DC2E7CA54F22` |
| `R3_RESEARCH_QUESTION_VARIABLE_MAP.csv` | `5827551D3CBC6F286133C260AD490BFF9C90B64F8A16F270D7814385B874DED6` |
| `R3_DECISION_PROVENANCE_EXTRACT.csv` | `A022FF27014CB2827820180EEE380BA73F77CE9B7377246665B4BA41148D4BD7` |

R3_PHASE_10B_COMPLETE — DAVID_DATASET_PROPOSAL_READY_FOR_RESEARCHER_REVIEW
