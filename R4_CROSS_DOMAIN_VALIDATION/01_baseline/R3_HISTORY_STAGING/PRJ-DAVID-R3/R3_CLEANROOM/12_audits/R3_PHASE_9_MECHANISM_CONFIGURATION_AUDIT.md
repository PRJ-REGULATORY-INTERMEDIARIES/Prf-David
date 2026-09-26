# R3 — Phase 9 Mechanism Configuration Audit

## A. Input universe

Phase 9 used only authorized R3 clean-room materials and preserved the frozen Phase 8C universe:

- supported R–I–T relations: `9`;
- LAW × INTERMEDIARY units: `7`;
- researcher-adjudicated mechanism events: `10`;
- event distribution: 4 `VERIFICATION`, 3 `EVALUATION_ASSESSMENT`, 3 `IMPLEMENTATION`.

No relation, intermediary, mechanism event, mechanism code, or R/I/T membership was added or changed.

## B. Relation configuration results

| Configuration type | Relations |
|---|---:|
| `SINGLE_MECHANISM` | 8 |
| `MULTI_MECHANISM_PARALLEL` | 0 |
| `MULTI_MECHANISM_SEQUENTIAL` | 1 |
| `MULTI_MECHANISM_MIXED` | 0 |
| `MULTI_MECHANISM_ORDER_UNRESOLVED` | 0 |

The sole multi-mechanism relation is `REL-32023-014`. All ten frozen events are represented exactly once at relation level.

## C. Sequence results

Confirmed mechanism edges: `1`.

`REL-32023-014_ME_01 [VERIFICATION] → REL-32023-014_ME_02 [EVALUATION_ASSESSMENT]`

- transferred object: audit findings and identified control weaknesses;
- evidence level: `S1_EXPLICIT_SEQUENCE`;
- legal basis: Article 21(2)(c)(ii), which requires a summary of audits and an analysis of weaknesses identified and corrective action taken;
- functional finding: verification identifies findings and weaknesses that are necessary inputs to the subsequent evaluative analysis.

The edge is based on functional dependency, not textual order. No edge was created between separate relations.

## D. Intermediary-level profiles

| Intermediary configuration profile | Units |
|---|---:|
| `SINGLE_RELATION_SINGLE_MECHANISM` | 5 |
| `SINGLE_RELATION_MULTI_MECHANISM` | 1 |
| `MULTI_RELATION_REPEATED_MECHANISM` | 1 |
| `MULTI_RELATION_VARIED_MECHANISM` | 0 |
| `MULTI_RELATION_MIXED_CONFIGURATION` | 0 |

The audit bodies constitute the single relation with multiple sequential mechanisms. Public or private implementing entities constitute the multi-relation repeated-mechanism profile.

## E. Multi-target repetition

The LAW × INTERMEDIARY unit `32023R0955_LI_001` performs `IMPLEMENTATION` independently in three supported relations involving:

- vulnerable households;
- vulnerable micro-enterprises;
- vulnerable transport users.

This is repeated use of the same mechanism across three R–I–T relations and three T classes. It is not a sequence or chain.

## F. Law-level profiles

| CELEX | Supported intermediaries | Supported relations | Events | Distinct mechanisms | Relation configurations |
|---|---:|---:|---:|---:|---|
| `32003L0087` | 1 | 1 | 1 | 1 | 1 single |
| `32015D1814` | 0 | 0 | 0 | 0 | substantive zero |
| `32018R0842` | 2 | 2 | 2 | 2 | 2 single |
| `32021R1119` | 1 | 1 | 1 | 1 | 1 single |
| `32023R0955` | 3 | 5 | 6 | 3 | 4 single; 1 sequential |

These profiles are descriptive. Instruments were not ranked, and no regulatory capacity was derived.

## G. Zero preservation

`32015D1814 = SUBSTANTIVE_ZERO`

It has 0 supported intermediaries, 0 supported intermediation relations, 0 mechanism events, and 0 mechanism configurations. This is not missing data.

## H. Implementation status

`IMPLEMENTATION = FAMILY_UNASSIGNED_PROVISIONAL`

No fourth mechanism family was created. The three `IMPLEMENTATION` events remain researcher-adjudicated and unchanged.

## I. Capacity firewall

`KNOWING_ASSURING_STEERING_CODED = NO`

## J. RIA firewall

`RIA_USED_AS_CODING_FRAME = NO`

## K. Outcome firewall

`EMPIRICAL_GOVERNANCE_OUTCOMES_INFERRED = NO`

No claim was made about compliance, enforcement, legitimacy, trust, effectiveness, maturity, sophistication, or architecture.

## L. Upstream issues

- `UPSTREAM_CONFIGURATION_REVIEW_NOTE`: none.
- `UPSTREAM_EVENT_DUPLICATION_REVIEW_REQUIRED`: none.

The two events in `REL-32023-014` remain distinct transformations: conformity checking produces findings; substantive evaluation analyzes the weaknesses identified and corrective action taken.

## M. Research-question contribution

Phase 8C established which elementary mechanisms exist. Phase 9 adds the empirical organization layer: it distinguishes single from multi-mechanism relations, identifies one legally supported within-relation sequence, and separates that sequence from repetition of the same mechanism across distinct targets and relations. The normalized outputs can now answer how mechanisms are organized and combined without treating configuration as capacity or outcome.

## N. Researcher decisions required

`NONE_BEFORE_PHASE_10`

No unresolved sequence, duplicated event, upstream inconsistency, or codebook change requires adjudication before a separately authorized Phase 10.

## Output integrity

| Phase 9 output | SHA-256 |
|---|---|
| `08_configuration/RELATION_MECHANISM_CONFIGURATIONS.csv` | `1913FC02F07FAF9A082D37ED36E717D18C0841507B7AECEDBD1D180CE0FF0A3D` |
| `08_configuration/MECHANISM_CONFIGURATION_EDGES.csv` | `1D146C4559B89897A94876D8EE3ED59D0FC1F1D82E029BDD436A1D867DDF298B` |
| `08_configuration/LAW_INTERMEDIARY_MECHANISM_PROFILE.csv` | `14416F5ECE7295F6214E9A17DDE88D420FCA49A44EA8B94912FD6A69256766B2` |
| `08_configuration/LAW_MECHANISM_CONFIGURATION_PROFILE.csv` | `6121205B4D0AF1B5F12EDF630F42564DFFCDBBA2A5F58953D1752C749C722FFE` |
| `08_configuration/MECHANISM_CONFIGURATION_TRACE.csv` | `3365A8B5881F26CC4154F258EBF5C484E723CDA0366AC612CB43AF640FF7D39E` |
| `08_configuration/MECHANISM_CONFIGURATION_MATRIX.csv` | `29BE26B69D3ECBC468FEFBE8ADF33EC44ED535EB3BC33CD7129D6D8A2958B8D6` |
| `08_configuration/PHASE9_RESEARCH_QUESTION_TRACE.csv` | `A8FEA899F353334E6FBD2D00753A3B92F9AE3A940CFDD0450B62099BFAA0AB65` |

## Quality gate Q1–Q16

| Gate | Result |
|---|---|
| Q1 — exactly 9 supported relations represented | PASS |
| Q2 — exactly 7 LAW × INTERMEDIARY units represented | PASS |
| Q3 — all 10 mechanism events accounted for | PASS |
| Q4 — single and multi-mechanism relations distinguished | PASS |
| Q5 — parallel and sequential configurations tested through functional dependency | PASS |
| Q6 — every confirmed edge legally supported | PASS |
| Q7 — cross-relation repetition distinguished from within-relation sequence | PASS |
| Q8 — implementation intermediary treated as repetition, not chain | PASS |
| Q9 — no new mechanism created | PASS |
| Q10 — no mechanism code changed | PASS |
| Q11 — `IMPLEMENTATION` remains family-unassigned | PASS |
| Q12 — Knowing, Assuring, and Steering not coded | PASS |
| Q13 — RIA not coded | PASS |
| Q14 — governance outcomes not inferred | PASS |
| Q15 — zero law preserved | PASS |
| Q16 — clean-room firewall respected | PASS |

R3_PHASE_9_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION
