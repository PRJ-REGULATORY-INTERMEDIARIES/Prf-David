# R3 — Phase 8 Mechanism Event Audit

Status: complete for researcher adjudication. Phase 8 coded elementary mechanism events only within the nine frozen supported R–I–T relations and stopped before Phase 8B or Phase 9.

## A. Inputs used

The following authorized R3 materials were consulted:

- `02_corpus/32003L0087/act_numbered.md`
- `02_corpus/32015D1814/act_numbered.md`
- `02_corpus/32018R0842/act_numbered.md`
- `02_corpus/32021R1119/act_numbered.md`
- `02_corpus/32023R0955/act_numbered.md`
- `03_instrument_profiles/INSTRUMENT_PROFILE.csv`
- `04_actor_register/ACTOR_REGISTER.csv`
- `04_actor_register/ACTOR_PROVISION_MAP.csv`
- `06_relations/RELATIONS_ADJUDICATED.csv`
- `06_relations/INTERMEDIATION_TEST_MATRIX.csv`
- `05_law_intermediary/LAW_INTERMEDIARY_REGISTER.csv`
- `05_law_intermediary/LAW_INTERMEDIARY_RELATION_LINK.csv`
- `05_law_intermediary/INTERMEDIARY_INSTITUTIONAL_PROFILE.csv`
- `05_law_intermediary/LAW_INTERMEDIARY_EVIDENCE.csv`
- `06_relations/R3_PHASE_6B_ADJUDICATION_DECISIONS.csv`
- `12_audits/R3_PHASE_6B_ADJUDICATION_AUDIT.md`
- `12_audits/R3_PHASE_7_LAW_INTERMEDIARY_AUDIT.md`

## B. Clean-room compliance

No Pilot A, R2, R2.1, previous mechanism classification, old spreadsheet, prior AI output, prior human mechanism adjudication or other previous-round empirical material was consulted. Mechanisms were reconstructed from the fresh R3 evidence and the frozen Phase 6B and Phase 7 units.

## C. Universe reconciliation

- supported R–I–T relations: 9;
- valid LAW × INTERMEDIARY units: 7;
- mechanism events produced: 10;
- supported relations with at least one traceable mechanism event: 9;
- supported relations with at least one confirmed authorized mechanism: 6;
- supported relations with no defensible authorized mechanism code: 3;
- supported relations with no event at all: 0.

All ten events resolve to a supported relation and a valid LAW × INTERMEDIARY unit. No new relation or intermediary was created.

## D. Mechanism distribution

| Mechanism code | Events |
|---|---:|
| TRANSMISSION | 0 |
| AGGREGATION | 0 |
| REPRESENTATION | 0 |
| TRANSLATION | 0 |
| INTERPRETATION | 0 |
| EVALUATION_ASSESSMENT | 3 |
| CLASSIFICATION_RANKING | 0 |
| MONITORING | 0 |
| VERIFICATION | 4 |
| MECHANISM_UNRESOLVED | 3 |

The three unresolved events concern material implementation and benefit delivery. `TRANSLATION` is the nearest authorized alternative, but assigning it would require extending the definition beyond transformation of content or register into another usable form.

## E. Family distribution

- `ARTICULATION`: 0;
- `INFORMATION_TREATMENT`: 3;
- `REGULATORY_RELIABILITY`: 4;
- `NOT_DERIVED` because mechanism is unresolved: 3.

Families were derived mechanically from confirmed elementary codes. They remain `EXPLORATORY_DERIVED_CLASSIFICATION` and were not independently interpreted or tested.

## F. Mechanism status

- `CONFIRMED`: 7;
- `AMBIGUOUS`: 0;
- `UNRESOLVED`: 3.

## G. Evidence level

- `M1_EXPLICIT_FUNCTIONAL`: 6;
- `M2_CROSS_PROVISION_FUNCTIONAL`: 4;
- `M3_ANALYTICAL_INFERENCE`: 0.

Mechanism evidence levels were coded independently from Phase 6 relation-evidence levels.

## H. Confidence

- `HIGH`: 4;
- `MEDIUM`: 3;
- `LOW`: 3.

All MEDIUM and LOW events appear in `MECHANISM_UNCERTAINTY_LOG.csv` and have an explicit alternative-mechanism test.

## I. Boundary problems

### Transmission versus aggregation

No event presented transmission and aggregation as the two leading alternatives. `REL-32021-010_ME_01` considers aggregation as the strongest alternative to evaluation because multiple national inputs are involved; evaluation is preferred because the legally relevant task is judgment of progress and consistency.

### Translation versus interpretation

No event turned on translation versus interpretation. The three delivery events remain unresolved rather than being forced into translation; interpretation is not supported because no rule meaning is being clarified.

### Evaluation versus verification

- `REL-32003-006_ME_01`: verification preferred because Annex V supplies predefined conformity criteria and a satisfactory/unsatisfactory finding;
- `REL-32018-007_ME_01`: evaluation preferred because robustness and adequacy of a corrective plan require substantive judgment;
- `REL-32023-014_ME_01`: verification preferred for checks against rules and audit standards;
- `REL-32023-014_ME_02`: evaluation preferred for analysis of weaknesses and adequacy of corrective action.

### Monitoring versus verification

`REL-32023-013_ME_01`: verification preferred because implementing authorities determine conformity with milestones, targets and financial-control requirements rather than merely observe developments over time.

### Evaluation versus classification

No event required this boundary. The Central Administrator's regular/irregular distinction was tested against classification, but verification remained primary because the result follows a conformity check against registry rules rather than an independent classificatory scheme.

### Representation versus consultation

No supported relation contains a representational event. Consultation-only relations had already been excluded from the positive universe and were not reopened.

### Additional unresolved boundary: material implementation versus translation

`REL-32023-007_ME_01`, `REL-32023-008_ME_01` and `REL-32023-009_ME_01` trace a clear material transformation from Plan resources and measures to delivered benefits, but no authorized code clearly captures implementation and delivery. They remain `MECHANISM_UNRESOLVED` with `TRANSLATION` as the closest alternative.

## J. Multi-mechanism relations

`REL-32023-014` contains two legally distinguishable events:

1. checking systems and operations against rules and audit standards;
2. analyzing identified weaknesses and corrective actions.

No other relation contains more than one event.

## K. Potential sequential configurations

`REL-32023-014_ME_01` and `REL-32023-014_ME_02` are marked `POSSIBLY_SEQUENTIAL`: conformity findings may precede analysis of weaknesses and corrective action. This is a preparatory hint only.

No formal chain was created.

## L. Upstream validation

No supported relation lacks a traceable event. However, three relations lack a defensible authorized mechanism code:

- `REL-32023-007`;
- `REL-32023-008`;
- `REL-32023-009`.

`UPSTREAM_C3_REVIEW_REQUIRED` is recorded on these events. Phase 6 C3 remains intelligible as legally structured implementation and pass-through of benefits, but the nine-code vocabulary does not clearly classify the material transformation. Phase 6 was not silently rewritten.

No Phase 7 output, orientation or institutional profile was contradicted. No `PHASE_7_CONSISTENCY_NOTE` was required.

## M. Zero law

`32015D1814 = 0 mechanism events`

This remains a substantive zero, not missing data.

## N. Capability firewall

KNOWING_ASSURING_STEERING_CODED = NO

## O. RIA firewall

RIA_USED_AS_CODING_FRAME = NO

## P. Chain firewall

FORMAL_MECHANISM_CHAINS_CREATED = NO

## Q. Researcher decisions required

Before Phase 8B, adjudicate:

1. whether material implementation and benefit delivery in `REL-32023-007` to `REL-32023-009` qualifies as `TRANSLATION`, or remains outside the authorized nine-code vocabulary;
2. whether corrective-plan robustness assessment in `REL-32018-007_ME_01` is better treated as evaluation than verification;
3. whether EEA support in `REL-32021-010_ME_01` is substantively evaluative rather than primarily aggregative;
4. whether the weakness-analysis event `REL-32023-014_ME_02` is distinct from, and subsequent to, the audit conformity check.

These decisions do not alter relation or intermediary membership unless the researcher reopens Phase 6 C3 for the three unresolved implementation cases.

## Required outputs

Created exactly:

- `07_mechanisms/MECHANISM_EVENTS.csv`
- `07_mechanisms/MECHANISM_TRACE.csv`
- `07_mechanisms/MECHANISM_UNCERTAINTY_LOG.csv`
- `12_audits/R3_PHASE_8_MECHANISM_AUDIT.md`

No Phase 8B or Phase 9 output was created.

## Q1–Q16 quality gate

| Gate | Result |
|---|---|
| Q1 — every event originates from supported intermediation | PASS |
| Q2 — every event resolves to a valid LAW × INTERMEDIARY unit | PASS |
| Q3 — trace completed before mechanism assignment | PASS |
| Q4 — legal action distinguished from mechanism | PASS |
| Q5 — institutional technologies distinguished from elementary mechanisms | PASS |
| Q6 — multiple events limited to distinct transformations | PASS |
| Q7 — every event legally evidenced | PASS |
| Q8 — strongest alternative explicitly considered | PASS |
| Q9 — unresolved cases preserved | PASS |
| Q10 — every supported relation checked for a defensible mechanism | PASS |
| Q11 — mechanism families mechanically derived | PASS |
| Q12 — zero law preserved | PASS |
| Q13 — capability coding excluded | PASS |
| Q14 — RIA coding excluded | PASS |
| Q15 — no formal chain created | PASS |
| Q16 — clean-room firewall respected | PASS |

Phase 8 is complete and stopped before Phase 8B and Phase 9.

R3_PHASE_8_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION
