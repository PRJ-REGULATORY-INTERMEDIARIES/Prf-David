# R3 — Phase 7 LAW × INTERMEDIARY Audit

Status: complete. Phase 7 constructed the intermediary-level register exclusively from the nine frozen `SUPPORTED_INTERMEDIATION` relations and stopped before Phase 8.

## A. Inputs used

The following authorized R3 files were read or directly used:

- `02_corpus/32003L0087/act_numbered.md`
- `02_corpus/32015D1814/act_numbered.md`
- `02_corpus/32018R0842/act_numbered.md`
- `02_corpus/32021R1119/act_numbered.md`
- `02_corpus/32023R0955/act_numbered.md`
- `04_actor_register/ACTOR_REGISTER.csv`
- `04_actor_register/ACTOR_PROVISION_MAP.csv`
- `06_relations/RELATIONS_ADJUDICATED.csv`
- `06_relations/INTERMEDIATION_TEST_MATRIX.csv`
- `06_relations/NEGATIVE_BOUNDARY_CASES.csv`
- `06_relations/R3_PHASE_6B_ADJUDICATION_DECISIONS.csv`
- `12_audits/R3_PHASE_6B_ADJUDICATION_AUDIT.md`

## B. Clean-room compliance

No prior-round empirical material, Pilot A or R2 output, previous intermediary list, previous institutional profile, prior mechanism coding, earlier workbook, old case summary, or old adjudication was consulted. All institutional claims derive from the authorized R3 chain.

## C. Input reconciliation

- total adjudicated relations: 56;
- `SUPPORTED_INTERMEDIATION`: 9;
- `DIRECT_R_T`: 24;
- `LEGAL_RELATION_NON_RIT`: 23;
- uncertain or unsupported: 0;
- supported relations used to generate LAW × INTERMEDIARY units: 9;
- non-supported relations used to generate units: 0.

Every supported relation appears once in `LAW_INTERMEDIARY_RELATION_LINK.csv`.

## D. LAW × INTERMEDIARY derivation

- supported relations: 9;
- unique CELEX × intermediary units: 7;
- laws with at least one supported intermediary: 4;
- laws with zero supported intermediaries: 1;
- multi-relational intermediaries: 1.

The multi-relational unit is `32023R0955_LI_001`, Public or private implementing entities. Three supported relations were consolidated into one unit while retaining three different target classes and their output contexts in the relation link and normalized profile.

## E. Distribution by instrument

| CELEX | Supported relations | Unique intermediaries | Actor types | Institutionalization types |
|---|---:|---:|---|---|
| 32003L0087 | 1 | 1 | VERIFICATION_BODY | EXPLICIT_STATUTORY_ROLE |
| 32015D1814 | 0 | 0 | none | none |
| 32018R0842 | 2 | 2 | EU_BODY; EU_AGENCY | PRE_EXISTING_BODY_WITH_ASSIGNED_FUNCTION |
| 32021R1119 | 1 | 1 | EU_AGENCY | PRE_EXISTING_BODY_WITH_ASSIGNED_FUNCTION |
| 32023R0955 | 5 | 3 | OTHER_JUSTIFIED; NATIONAL_AUTHORITY; AUDIT_BODY | PROCEDURALLY_RECOGNIZED_ROLE; FORMALLY_DESIGNATED_ROLE |

This distribution is descriptive and carries no architectural evaluation.

## F. Institutional attributes

### Participation status

- `MANDATORY`: 4;
- `CONDITIONAL_MANDATORY`: 3.

### Separation from T

- `FORMALLY_SEPARATE`: 5;
- `TARGET_INTERNAL`: 2.

### Independence status

- `EXPLICIT_INDEPENDENCE_REQUIREMENT`: 2;
- `NO_EXPLICIT_INDEPENDENCE_RULE`: 5.

### Output legal effect

- `ESTABLISHES_STATUS`: 2;
- `SUPPORTING_EVIDENCE`: 2;
- `COMPLIANCE_EVIDENCE`: 2;
- `OTHER_JUSTIFIED`: 1.

### Accountability status

- `EXPLICIT`: 2;
- `PARTIAL`: 4;
- `NOT_SPECIFIED`: 1.

No subjective centrality score was created. The register contains only the requested transparent counts.

## G. Multi-relational variation

For `32023R0955_LI_001`:

- R differs across relations: NO;
- T differs: YES — vulnerable households, vulnerable micro-enterprises and vulnerable transport users;
- orientation differs: NO — all three are target-facing;
- regulatory object differs: YES — general social-climate benefits versus mobility-specific support;
- output differs: YES — target-specific implemented measures, services, financial benefits or mobility support;
- output legal effect differs: NO;
- relation purpose differs: NO.

No other unit participates in more than one supported relation within the same law. Because orientation and legal effect remain stable, no false `MIXED` generalization was introduced; relation-sensitive variation remains normalized.

## H. Evidence gaps

- `UNCLEAR`: no primary institutional attribute was coded `UNCLEAR`.
- `NOT_SPECIFIED`: Central Administrator accountability channel and procedure; sanctions or consequences for intermediary failure in all seven units.
- `MIXED`: the public/private implementing-entity class has `institutional_level=MIXED`, inherited from the legally open actor class. No primary participation, separation, independence, orientation, output-effect or accountability category required `MIXED`.
- `NO_EXPLICIT_INDEPENDENCE_RULE`: Central Administrator, both EEA units, Public or private implementing entities, and Implementing authorities.
- `analytical_uncertainty=YES`: `32023R0955_LI_001`, because the act leaves the concrete public/private organizational form, designation route and detailed accountability procedure open.

Each unit has ten attribute-level evidence records in `LAW_INTERMEDIARY_EVIDENCE.csv`.

## I. Meta-intermediation candidates

Candidate flags only:

- `32018R0842_LI_001` — Commission registry rules structure the Central Administrator's assigned function;
- `32023R0955_LI_001` — Member State statutory or contractual safeguards structure implementing-entity performance;
- `32023R0955_LI_002` — independent audit bodies may examine systems and operations involving implementing authorities.

No meta-intermediary relation was created or adjudicated.

## J. Zero cases

`32015D1814`: `N_LAW_INTERMEDIARY = 0`.

This is preserved as a substantive zero, not missing data.

## K. Negative-case firewall

No actor was promoted solely from a `DIRECT_R_T`, `LEGAL_RELATION_NON_RIT`, uncertain, unsupported, or negative-boundary relation. Every registered unit has at least one linked supported relation. Auction platforms, market intermediaries in peer transfers, advisory-only actors, consultation actors and other negative cases remain excluded unless independently supported elsewhere; none qualified elsewhere in the frozen universe.

## L. OLAF check

The Phase 6B decision is preserved:

- C1 = YES;
- C2 = YES;
- C3 = NO;
- classification = `DIRECT_R_T`.

OLAF does not appear in `LAW_INTERMEDIARY_REGISTER.csv` or its relation link.

## M. Auction-platform check

Relations `REL-32015-001`, `REL-32015-002` and `REL-32015-003` remain `E2_CROSS_PROVISION_RECONSTRUCTED` at relation level. They remain direct relations and generate no intermediary unit.

## N. Mechanism firewall

FORMAL_MECHANISM_CODES_CREATED = NO

## O. Capability firewall

KNOWING_ASSURING_STEERING_CODED = NO

## P. RIA firewall

RIA_USED_AS_CODING_FRAME = NO

## Q. Upstream issues

### UPSTREAM_REVIEW_NOTE

- affected phase: Phase 4;
- file: `ACTOR_REGISTER.csv`;
- record ID: `ACT-32023-020`;
- suspected problem: `n_provisions=1` is present, but `operative_provisions` and `annexes` are blank even though the actor-provision map records the relevant role in Annex III;
- legal evidence: `APM-32023-042` and `02_corpus/32023R0955/act_numbered.md:L001385-L001437`;
- potential consequence: actor-register metadata completeness only. It does not affect intermediary identity, supported-relation membership, or Phase 7 unit membership.

No upstream issue capable of changing the LAW × INTERMEDIARY universe was found.

## R. Researcher decisions required

No decision is required to preserve the seven-unit universe or to begin a later mechanism-adjudication phase. The open organizational form and detailed accountability procedure for `32023R0955_LI_001` remain transparently marked as analytical uncertainty and may be retained as legally meaningful variation.

## Required outputs

Created exactly:

- `05_law_intermediary/LAW_INTERMEDIARY_REGISTER.csv`
- `05_law_intermediary/LAW_INTERMEDIARY_RELATION_LINK.csv`
- `05_law_intermediary/INTERMEDIARY_INSTITUTIONAL_PROFILE.csv`
- `05_law_intermediary/LAW_INTERMEDIARY_EVIDENCE.csv`
- `12_audits/R3_PHASE_7_LAW_INTERMEDIARY_AUDIT.md`

## Q1–Q22 quality gate

| Gate | Result |
|---|---|
| Q1 — every unit originates from supported intermediation | PASS |
| Q2 — all nine supported relations reconciled | PASS |
| Q3 — repeated same-law intermediaries consolidated | PASS |
| Q4 — every intermediary resolves to a Phase 4 actor | PASS |
| Q5 — every intermediary institutionally evidenced | PASS |
| Q6 — institutionalization distinct from participation | PASS |
| Q7 — participation distinct from output legal effect | PASS |
| Q8 — separation from target distinct from independence | PASS |
| Q9 — actor-level and relation-level attributes kept distinct | PASS |
| Q10 — multi-relational variation preserved | PASS |
| Q11 — accountability claims legally evidenced | PASS |
| Q12 — subjective centrality scoring avoided | PASS |
| Q13 — meta-intermediation not adjudicated | PASS |
| Q14 — formal mechanisms not coded | PASS |
| Q15 — capability families not coded | PASS |
| Q16 — 3–4–2 structure not tested | PASS |
| Q17 — RIA not used as coding template | PASS |
| Q18 — negative boundary cases excluded | PASS |
| Q19 — OLAF adjudication unchanged | PASS |
| Q20 — auction-platform E2 corrections preserved | PASS |
| Q21 — zero-intermediary law preserved | PASS |
| Q22 — clean-room firewall respected | PASS |

Phase 7 is complete. Phase 8 has not begun.

R3_PHASE_7_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION
