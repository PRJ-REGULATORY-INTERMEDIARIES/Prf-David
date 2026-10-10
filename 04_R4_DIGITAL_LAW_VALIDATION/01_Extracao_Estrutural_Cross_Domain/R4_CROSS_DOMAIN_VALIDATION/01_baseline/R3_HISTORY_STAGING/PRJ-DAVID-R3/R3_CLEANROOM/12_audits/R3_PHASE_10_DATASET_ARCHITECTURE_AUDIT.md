# R3 — Phase 10 Dataset Architecture Audit

## A. Inputs used

Only authorized R3 clean-room materials were used, principally:

- `INSTRUMENT_PROFILE.csv` — 5 instruments;
- `ACTOR_REGISTER.csv` — 89 LAW × ACTOR records;
- `LAW_INTERMEDIARY_REGISTER.csv` and relation links — 7 LAW × INTERMEDIARY units;
- `RELATIONS_ADJUDICATED.csv` — 56 relations: 24 direct R–T, 23 legal non-RIT, and 9 supported intermediation;
- researcher-adjudicated mechanism event, trace, and decision-provenance files — 10 events;
- Phase 9 configuration tables — 9 configurations and 1 confirmed edge;
- Phase 8C and Phase 9 audits and the researcher decision.

No prior round, old coding, capacity assignment, architecture hypothesis, or statistical result was used.

## B. Research question adopted

> How are regulatory intermediation mechanisms organized and combined across actors and regulatory relations in EU climate regulation, and what regulatory capacities do these configurations appear designed to provide?

RQ-A is treated as the current empirical-configuration component. RQ-B is represented only by an empty future-derived schema.

## C. Units preserved

Eleven levels or units are explicitly distinguished in `R3_ANALYTICAL_UNIT_MATRIX.csv`, including LAW, LAW × ACTOR, LAW × INTERMEDIARY, REGULATORY RELATION, MECHANISM EVENT, MECHANISM CONFIGURATION, MECHANISM EDGE, LEGAL EVIDENCE, DECISION PROVENANCE, future CAPACITY CLAIM, and future ARCHITECTURAL COMPARISON.

LAW × INTERMEDIARY remains the principal human-facing unit. It does not absorb child relations or events into authoritative multivalue cells.

## D. Proposed tables

The normalized architecture contains ten substantive tables:

1. `INSTRUMENT`;
2. `ACTOR`;
3. `LAW_INTERMEDIARY`;
4. `REGULATORY_RELATION`;
5. `MECHANISM_EVENT`;
6. `MECHANISM_CONFIGURATION`;
7. `MECHANISM_EDGE`;
8. `LEGAL_EVIDENCE`;
9. `DECISION_PROVENANCE`;
10. `REGULATORY_CAPACITY` — empty future layer.

Architecture comparison remains a future analytical level and was not substantively designed or classified.

## E. Variable counts by priority class

`R3_VARIABLE_PRIORITY_REGISTER.csv` contains 137 unique table-variable records:

| Priority class | Variables |
|---|---:|
| `CORE` | 43 |
| `EXPLANATORY` | 30 |
| `PROVENANCE` | 34 |
| `DERIVED` | 15 |
| `FUTURE_THEORETICAL` | 13 |
| `DROP_CANDIDATE` | 2 |

All 43 CORE variables link to at least one RQ identifier. The draft data dictionary contains 135 retained, normalized, derived, merged, or future-layer fields; the two drop candidates are excluded from the proposed final-field dictionary but remain visible in the priority register.

Recommendation totals are:

- `KEEP`: 81;
- `NORMALIZE`: 25;
- `DERIVE`: 15;
- `MERGE_CANDIDATE`: 1;
- `DROP_CANDIDATE`: 2;
- `FUTURE_LAYER`: 13.

No upstream field was deleted.

## F. Redundancies identified

- `R_name`, `I_name`, and `T_name` in relation-level outputs should be derived from ACTOR for displays; actor IDs remain authoritative.
- semicolon-delimited `supported_relation_ids` should be a derived view over child relation records.
- `n_output_types` should derive from normalized output values.
- material, territorial, and temporal scope can be merged for a concise human-facing `scope`, while detailed upstream components remain preserved.
- `configuration_hint` is superseded by the Phase 9 MECHANISM_CONFIGURATION table and is a drop candidate for the final authoritative schema.
- `n_relevant_provisions` is sensitive to drafting granularity and lacks a clear role in the current RQs; it is a drop candidate for the final schema.
- distributed source-provision/source-anchor fields and separate evidence tables should be normalized into LEGAL_EVIDENCE without destroying historical provenance.
- model, adversarial, and researcher decision fields should be normalized into DECISION_PROVENANCE while retaining original audit files.

## G. Variables moved to future layers

Thirteen fields belong exclusively to the empty REGULATORY_CAPACITY layer: identifiers and links, proposed capacity, definition, derivation rule, empirical and theoretical bases, alternative interpretation, confidence, and researcher adjudication. No capacity value was populated.

Architectural classes, scores, maturity, complexity, and governance outcomes were not proposed as current empirical fields.

## H. Schema-validation results

Six required tests passed with `represented_without_loss = YES`:

1. substantive-zero law;
2. repeated `IMPLEMENTATION` across three target-specific relations;
3. `VERIFICATION → EVALUATION_ASSESSMENT` sequence;
4. the same intermediary type appearing across laws;
5. researcher-added mechanism provenance;
6. a valid mechanism with provisional/unassigned family.

No schema-distorting problem was found. Two implementation recommendations remain: govern stable cross-law actor keys and normalize existing provenance through reconciled migration.

## I. Negative-case support

REGULATORY_RELATION retains all 56 adjudicated records and their final classifications. Mechanism tables restrict children to `SUPPORTED_INTERMEDIATION`, while direct and legal non-RIT relations remain available as analytical baselines. Boundary and review metadata are retained as provenance.

## J. Zero-case support

`32015D1814` remains an INSTRUMENT row with zero intermediary, supported-relation, mechanism-event, configuration, and edge children. Zero counts are produced through left joins, not fabricated placeholder records.

## K. Decision-provenance support

The schema distinguishes evidence from decisions and supports many decisions per analytical unit and one decision affecting many units. It explicitly preserves `R3-D08-IMPLEMENTATION`, researcher ownership, initial unresolved values, Phase 8B boundary results, and final `IMPLEMENTATION` values.

## L. Capacity firewall

`REGULATORY_CAPACITIES_CODED = NO`

## M. RIA firewall

`RIA_CLASSIFICATION_CREATED = NO`

## N. Statistical-analysis firewall

`STATISTICAL_MODELING_PERFORMED = NO`

No factor analysis, PCA, clustering, latent-class analysis, regression, correspondence analysis, network centrality, causal analysis, or other statistical model was performed.

## O. Research-question test

`RQ_A_STRUCTURALLY_ANSWERABLE = YES`

A researcher receiving the schema and properly coded data can reconstruct how mechanisms are distributed and combined across actors and regulatory relations by following keys from LAW and LAW_INTERMEDIARY to RELATION, MECHANISM_EVENT, MECHANISM_CONFIGURATION, and MECHANISM_EDGE.

## P. Future-capacity test

`RQ_B_STRUCTURALLY_ANALYZABLE_WITHOUT_PRIOR_CAPACITY_ASSUMPTIONS = YES`

The empty capacity layer requires explicit derivation, empirical basis, theoretical basis, alternatives, confidence, and adjudication. It therefore supports later capacity analysis without encoding capacities into mechanisms or configurations in advance.

## Q. Researcher decisions required before Phase 11

Genuine conceptual decisions remain:

1. approve the working definitions and admissible domain of candidate regulatory capacities;
2. decide whether capacity claims attach primarily to configurations, relations, LAW × INTERMEDIARY units, laws, or a controlled subset of these levels;
3. authorize derivation rules and the minimum evidence threshold for a capacity proposition;
4. decide whether institutional attributes operate as evidence for capacity, explanatory conditions, or contextual moderators rather than parts of the capacity definition;
5. define how alternative interpretations and negative capacity findings will be adjudicated.

These decisions were not preempted in Phase 10.

## David concern test

The architecture explicitly answers how dimensions fit together and how research-question-oriented classification is prioritized:

- institutional attributes characterize intermediaries;
- mechanisms characterize transformations;
- configurations characterize relations among mechanisms;
- future capacities are derived claims about configurations or other authorized units;
- outcomes remain empirically separate;
- only variables linked to research questions, explanation, auditability, reproducible derivation, or an explicitly future theoretical test enter the proposed architecture.

This is the researcher's proposed design, not David's endorsed model.

## Output integrity

| Phase 10 output | SHA-256 |
|---|---|
| `R3_ANALYTICAL_UNIT_MATRIX.csv` | `C840DF5D30FD96D5478AC27AA4209908D6F0624683B3411C6896E0F4023247CF` |
| `R3_DATA_DICTIONARY_DRAFT.csv` | `A85E4B7C6528F79C63FCAFC6366AA6B2BF9977338473A82617C1DC2E7CA54F22` |
| `R3_DATASET_ARCHITECTURE_PROPOSAL.md` | `11170B93C4044E6E72EE16B65D0D2F68F276405916038D6F594FDEFDEBC9F6D0` |
| `R3_DAVID_DATASET_VIEW_SPEC.md` | `E0C615D396F94717F7E9807055C0B8294FC912F478A9BAE5B6199A5ABBCE231F` |
| `R3_ENTITY_RELATIONSHIP_SPEC.md` | `4157680996BE75019DCD2D4E79DD4FE55A9E32148F5971039E8C2987ECA189B0` |
| `R3_RESEARCH_QUESTION_VARIABLE_MAP.csv` | `5827551D3CBC6F286133C260AD490BFF9C90B64F8A16F270D7814385B874DED6` |
| `R3_SCHEMA_VALIDATION_CASES.csv` | `2CBA4C57D2DEA0FE907EEA00536571886A5792A5F7C7D2F755C04F833ACCC3DF` |
| `R3_VARIABLE_PRIORITY_REGISTER.csv` | `FB9527655861F64CA776707651C97435C0EDE05F57AEE912581A24777C3C0044` |

## Quality gate Q1–Q20

| Gate | Result |
|---|---|
| Q1 — all analytical levels explicitly separated | PASS |
| Q2 — LAW × INTERMEDIARY preserved as primary human-facing unit | PASS |
| Q3 — relations represented independently | PASS |
| Q4 — mechanism events represented independently | PASS |
| Q5 — mechanism configurations represented independently | PASS |
| Q6 — evidence normalized and traceable in proposed architecture | PASS |
| Q7 — decision provenance preserved | PASS |
| Q8 — negative cases structurally representable | PASS |
| Q9 — substantive-zero law structurally representable | PASS |
| Q10 — multi-relational intermediaries represented without flattening | PASS |
| Q11 — multi-mechanism relations represented without flattening | PASS |
| Q12 — `IMPLEMENTATION` may remain family-unassigned | PASS |
| Q13 — researcher-added mechanism distinguishable by provenance | PASS |
| Q14 — every CORE variable linked to at least one research question | PASS |
| Q15 — unsupported/redundant variables marked drop, merge, derive, normalize, or future | PASS |
| Q16 — capacities not coded | PASS |
| Q17 — RIA not classified | PASS |
| Q18 — no statistical modeling performed | PASS |
| Q19 — schema can answer RQ-A | PASS |
| Q20 — schema supports later RQ-B testing without circularity | PASS |

R3_PHASE_10_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION
