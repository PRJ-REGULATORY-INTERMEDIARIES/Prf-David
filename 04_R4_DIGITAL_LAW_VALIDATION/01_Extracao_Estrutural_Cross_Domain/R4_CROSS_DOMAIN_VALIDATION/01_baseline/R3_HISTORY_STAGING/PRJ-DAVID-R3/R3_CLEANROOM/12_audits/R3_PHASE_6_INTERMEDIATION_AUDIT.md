# R3 — Phase 6 Regulatory Intermediation Audit

Status: complete for researcher review. Phase 6 adjudicated all 56 Phase 5 candidate relations and stopped before intermediary-level consolidation or formal mechanism coding.

## A. Inputs used

Only the following authorized R3 clean-room files were used:

- `02_corpus/32003L0087/act_numbered.md`
- `02_corpus/32015D1814/act_numbered.md`
- `02_corpus/32018R0842/act_numbered.md`
- `02_corpus/32021R1119/act_numbered.md`
- `02_corpus/32023R0955/act_numbered.md`
- `03_instrument_profiles/INSTRUMENT_PROFILE.csv`
- `03_instrument_profiles/INSTRUMENT_MEMO_32003L0087.md`
- `03_instrument_profiles/INSTRUMENT_MEMO_32015D1814.md`
- `03_instrument_profiles/INSTRUMENT_MEMO_32018R0842.md`
- `03_instrument_profiles/INSTRUMENT_MEMO_32021R1119.md`
- `03_instrument_profiles/INSTRUMENT_MEMO_32023R0955.md`
- `04_actor_register/ACTOR_REGISTER.csv`
- `04_actor_register/ACTOR_PROVISION_MAP.csv`
- `04_actor_register/ACTOR_ALIAS_LOG.csv`
- `06_relations/RELATION_CANDIDATES.csv`
- `06_relations/CROSS_PROVISION_RELATION_MAP.csv`
- `12_audits/R3_PHASE_5_RELATION_AUDIT.md`

## B. Clean-room compliance

The clean-room firewall remained active. No prior-round coding, earlier intermediary classification, previous R/I/T assignment, mechanism assignment, prior dataset, old case note, adjudication spreadsheet, or prior human-review output was consulted.

The Phase 5 universe was preserved: 56 relations were adjudicated; none was silently added or deleted. `NEW_RELATION_POSSIBLE = NO`.

No formal mechanism family, architectural theory, LAW × INTERMEDIARY register, accountability classification, or meta-intermediation analysis was created.

## C. Final classification counts

| CELEX | SUPPORTED_INTERMEDIATION | DIRECT_R_T | LEGAL_RELATION_NON_RIT | UNCERTAIN | NOT_SUPPORTED | Total |
|---|---:|---:|---:|---:|---:|---:|
| 32003L0087 | 1 | 7 | 1 | 0 | 0 | 9 |
| 32015D1814 | 0 | 4 | 2 | 0 | 0 | 6 |
| 32018R0842 | 2 | 5 | 3 | 0 | 0 | 10 |
| 32021R1119 | 1 | 3 | 7 | 0 | 0 | 11 |
| 32023R0955 | 5 | 4 | 10 | 1 | 0 | 20 |
| **Total** | **9** | **23** | **23** | **1** | **0** | **56** |

The 23 direct relations are retained as the non-mediated regulatory baseline. The 23 non-RIT relations remain legally relevant but lack an identifiable regulator–target structure in the relation adjudicated.

## D. Three-condition results

| Condition | YES | NO | UNCERTAIN | NOT_APPLICABLE |
|---|---:|---:|---:|---:|
| C1 — identifiable R–T relation | 33 | 23 | 0 | 0 |
| C2 — distinct institutionalized third party | 12 | 1 | 0 | 43 |
| C3 — demonstrable mediating function | 9 | 3 | 1 | 43 |

All nine `SUPPORTED_INTERMEDIATION` rows have C1=YES, C2=YES and C3=YES. No relation was supported on institutional presence, advice, consultation, or non-binding expertise alone.

## E. Third-actor adjudication

The 13 Phase 5 third-actor candidates produced:

- 9 `SUPPORTED_INTERMEDIATION`;
- 1 `DIRECT_R_T` after the third actor failed C3;
- 2 `LEGAL_RELATION_NON_RIT` after C1 failed;
- 1 `UNCERTAIN` because C3 could not be resolved;
- 0 `NOT_SUPPORTED`.

Supported third actors:

- `REL-32003-006` — Independent verifiers;
- `REL-32018-005` — Central Administrator;
- `REL-32018-007` — European Environment Agency;
- `REL-32021-010` — European Environment Agency;
- `REL-32023-007` to `REL-32023-009` — Public or private implementing entities;
- `REL-32023-013` — Implementing authorities;
- `REL-32023-014` — Audit bodies.

Third-actor failures or unresolved cases:

| Relation | Actor | Result | Primary reason |
|---|---|---|---|
| REL-32015-001 | Common auction platform | DIRECT_R_T | `NO_MEDIATING_FUNCTION` |
| REL-32018-004 | Market intermediaries acting on an agency basis | LEGAL_RELATION_NON_RIT | `NO_IDENTIFIABLE_RT_RELATION` |
| REL-32021-008 | Relevant stakeholders | LEGAL_RELATION_NON_RIT | `NO_IDENTIFIABLE_RT_RELATION` |
| REL-32023-015 | OLAF | UNCERTAIN | `INSUFFICIENT_EVIDENCE` for C3 |

## F. Results for the 18-relation Phase 5 review set

The review set resulted in:

- 9 `SUPPORTED_INTERMEDIATION`;
- 2 `DIRECT_R_T`;
- 6 `LEGAL_RELATION_NON_RIT`;
- 1 `UNCERTAIN`.

Seventeen review flags were resolved. Resolution rested on provision-specific evidence showing either a complete C1–C3 chain, a supported direct relation without a mediating function, or a legally meaningful relation lacking C1. `REL-32023-015` remains unresolved because Article 21 establishes OLAF's institutional status and access rights but does not specify a resulting output and its entry into the Commission–Member State payment or recovery relation.

The detailed result and rationale for every review-set row are in `INTERMEDIATION_TEST_MATRIX.csv`.

## G. Boundary cases

Eight negative or unresolved boundary cases were preserved in `NEGATIVE_BOUNDARY_CASES.csv`. The most informative boundaries are:

- a platform can be operationally present without performing a demonstrated mediating function;
- an actor can mediate a peer transaction without mediating a regulator–target relation;
- formal scientific advice does not establish intermediation when no separate regulatory target is identified;
- committee assistance is not enough without an R–T relation;
- mandatory consultation and stakeholder participation do not by themselves establish intermediation;
- formal access and control rights do not resolve C3 when the output and its regulatory connection are unspecified.

These are analytical negative cases, not coding failures.

## H. Role switching

Four actor-law combinations occupy more than one final relation-specific role:

- 32003L0087 — Member States: R and T;
- 32015D1814 — Member States: R and T;
- 32018R0842 — Central Administrator: I and R;
- 32023R0955 — Member States: R and T.

Twenty-one relation rows involving those actor-law combinations have `role_switch_observed=YES`. This is reported without theoretical interpretation.

## I. Evidence quality

Supported intermediation by evidence level:

- E1: 9;
- E2: 0;
- E3: 0.

Uncertain relations by evidence level:

- E1: 1 (`REL-32023-015`);
- E2: 0;
- E3: 0.

No E3 relation was classified as supported, so no exceptional justification was required.

## J. Upstream issues

### UPSTREAM_REVIEW_NOTE 1

- phase: Phase 4 and Phase 5
- file: `ACTOR_PROVISION_MAP.csv`; `RELATION_CANDIDATES.csv`
- record: `APM-32015-008`, `APM-32015-009`, `REL-32015-001`, `REL-32015-002`, `REL-32015-003`
- issue: the common and opt-out auction platforms are explicitly named in recital 6, while Article 1(8) refers only to auction calendars. The Phase 4 map treated the platform identity as operative E1 evidence at the Article 1(8) anchor.
- legal evidence: `02_corpus/32015D1814/act_numbered.md:L000060-L000066` and `L000163-L000168`
- possible consequence: Phase 6 retains the relations but treats `REL-32015-002` and `REL-32015-003` as E2 cross-provision reconstructions and adds recital 6 to their downstream source basis. `REL-32015-001` remains E1 for the direct Commission–Member State relation, while its third-actor test also uses recital 6.

No upstream file was silently rewritten.

## K. Researcher decisions required

1. Decide whether incorporated Financial Regulation powers provide sufficient cross-instrument evidence to resolve C3 for OLAF in `REL-32023-015`.
2. Decide whether the Phase 4 and Phase 5 auction-platform evidence records should be formally corrected upstream from operative E1 to recital-supported cross-provision evidence.

No other unresolved substantive decision remains in Phase 6.

## Required outputs

Created exactly for Phase 6:

- `06_relations/RELATIONS_ADJUDICATED.csv`
- `06_relations/INTERMEDIATION_TEST_MATRIX.csv`
- `06_relations/NEGATIVE_BOUNDARY_CASES.csv`
- `06_relations/UNCERTAIN_RELATIONS.csv`
- `12_audits/R3_PHASE_6_INTERMEDIATION_AUDIT.md`

## Q1–Q17 quality gate

| Gate | Result |
|---|---|
| Q1 — all 56 Phase 5 relations adjudicated | PASS |
| Q2 — every supported case satisfies C1, C2 and C3 | PASS |
| Q3 — every intermediary tied to an identifiable R–T relation | PASS |
| Q4 — advice alone rejected as sufficient | PASS |
| Q5 — consultation alone rejected as sufficient | PASS |
| Q6 — institutionalization alone rejected as sufficient | PASS |
| Q7 — non-bindingness not used as a rejection rule | PASS |
| Q8 — direct R–T relations preserved | PASS |
| Q9 — non-RIT legal relations distinguished from direct regulation | PASS |
| Q10 — negative boundary cases preserved | PASS |
| Q11 — uncertain cases preserved | PASS |
| Q12 — R/I/T roles assigned relation-specifically | PASS |
| Q13 — no formal mechanism coding | PASS |
| Q14 — no formal mechanism-family coding | PASS |
| Q15 — no later architectural family coding | PASS |
| Q16 — no LAW × INTERMEDIARY table created | PASS |
| Q17 — clean-room firewall respected | PASS |

Phase 6 is complete. Phase 7 has not begun.

R3_PHASE_6_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION
