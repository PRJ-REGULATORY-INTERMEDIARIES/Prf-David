# R3 — Phase 8B Adversarial Mechanism Adjudication Audit

Status: complete for researcher review. All ten Phase 8 events received an independent reconstruction and adversarial comparison. No Phase 9 work was performed.

## Inputs used

Only R3 clean-room materials were consulted:

- the validated legal corpora for the five CELEX instruments;
- `06_relations/RELATIONS_ADJUDICATED.csv`;
- `06_relations/INTERMEDIATION_TEST_MATRIX.csv`;
- `05_law_intermediary/LAW_INTERMEDIARY_REGISTER.csv`;
- `05_law_intermediary/LAW_INTERMEDIARY_RELATION_LINK.csv`;
- `07_mechanisms/MECHANISM_EVENTS.csv`;
- `07_mechanisms/MECHANISM_TRACE.csv`;
- `07_mechanisms/MECHANISM_UNCERTAINTY_LOG.csv`;
- `12_audits/R3_PHASE_8_MECHANISM_AUDIT.md`.

No prior-round mechanism coding or previous empirical output was consulted.

## A. Original Phase 8 universe

- mechanism events: 10;
- `CONFIRMED`: 7;
- `UNRESOLVED`: 3;
- supported R–I–T relations: 9;
- LAW × INTERMEDIARY units: 7.

The original Phase 8 files were not overwritten.

## B. Independent reconstruction results

| Event | Independent candidate | Agreement with Phase 8 | Adversarial result |
|---|---|---|---|
| REL-32003-006_ME_01 | VERIFICATION | YES | CONFIRM_PHASE8 |
| REL-32018-005_ME_01 | VERIFICATION | YES | CONFIRM_PHASE8 |
| REL-32018-007_ME_01 | EVALUATION_ASSESSMENT | YES | CONFIRM_PHASE8 |
| REL-32021-010_ME_01 | EVALUATION_ASSESSMENT | YES | CONFIRM_PHASE8 |
| REL-32023-007_ME_01 | Material implementation and delivery — non-codebook description | Phase 8 non-assignment sustained | CODEBOOK_BOUNDARY |
| REL-32023-008_ME_01 | Material implementation and delivery — non-codebook description | Phase 8 non-assignment sustained | CODEBOOK_BOUNDARY |
| REL-32023-009_ME_01 | Material implementation and delivery — non-codebook description | Phase 8 non-assignment sustained | CODEBOOK_BOUNDARY |
| REL-32023-013_ME_01 | VERIFICATION | YES | CONFIRM_PHASE8 |
| REL-32023-014_ME_01 | VERIFICATION | YES | CONFIRM_PHASE8 |
| REL-32023-014_ME_02 | EVALUATION_ASSESSMENT | YES | CONFIRM_PHASE8 |

Labels were accepted only after reconstructing input, mediated object, transformation, output, recipient and R–T connection independently.

## C. Confirmed, revised and boundary outcomes

- confirmed unchanged: 7;
- revised to another existing mechanism: 0;
- ambiguous between existing mechanisms: 0;
- residual unresolved without diagnosed boundary: 0;
- `CODEBOOK_BOUNDARY`: 3;
- `UPSTREAM_RIT_REVIEW`: 0.

The three boundary events retain `MECHANISM_UNRESOLVED` as their formal mechanism value because no tenth mechanism was added. Their adjudication status is now specifically `CODEBOOK_BOUNDARY`.

## D. Specific boundary adjudications

### Evaluation versus verification

- `REL-32018-007_ME_01`: evaluation survives. The EEA supports judgment of plan robustness and adequacy; legal obligations provide context but do not reduce the task to a binary conformity test.
- `REL-32003-006_ME_01`: verification survives. Annex V provides predefined criteria and requires a satisfactory or unsatisfactory finding.
- `REL-32023-014_ME_01`: verification survives for the conformity check against rules and audit standards.
- `REL-32023-014_ME_02`: evaluation survives because analysis of weaknesses and corrective action requires a distinct judgment after findings exist.

### Evaluation versus aggregation

`REL-32021-010_ME_01`: evaluation survives. Multiple reports and datasets are inputs, but the legally consequential contribution is judgment of progress and consistency. No separately consequential synthesized output is assigned to the EEA, so aggregation remains ancillary.

### Verification versus monitoring

`REL-32023-013_ME_01`: verification survives. The implementing authorities determine achievement of milestones and targets and absence of specified irregularities against predefined requirements. Repeated desk or on-site observation is a means, not the dominant output.

### Verification/evaluation separation in audit bodies

The two events in `REL-32023-014` are classified `DISTINCT_POSSIBLY_SEQUENTIAL`:

1. ME_01 checks systems and operations against applicable rules and standards;
2. ME_02 uses the resulting findings to analyze weaknesses and corrective responses.

They are not duplicated descriptions of the same transformation. No formal chain was created.

### Material implementation versus translation

The three implementation events are not translation under the current definition. Their dominant inputs and outputs are material resources, measures, services and benefits. They do not primarily convert legal, technical or regulatory content into another content register.

Forcing translation would silently broaden the code from content conversion to programme execution.

## E. Implementation cases

### REL-32023-007_ME_01

- transformation: Plan resources and measures become delivered services, investments or benefits for vulnerable households;
- T status: a legally defined beneficiary class whose access to support is shaped, but not clearly a target in the conventional conduct/compliance sense;
- C3: remains provisionally defensible because the act recognizes a distinct pass-through actor and requires statutory or contractual safeguards ensuring that the entire benefit reaches T;
- ontology fit: no existing mechanism fits without definition expansion;
- action: preserve as `CODEBOOK_BOUNDARY` and seek conceptual adjudication.

### REL-32023-008_ME_01

- transformation: Plan resources and measures become delivered services, investments or benefits for vulnerable micro-enterprises;
- T status: a legally defined beneficiary class whose access to support is shaped, but not clearly a target in the conventional conduct/compliance sense;
- C3: remains provisionally defensible because the entity is legally interposed and the full benefit must pass through to T;
- ontology fit: no existing mechanism fits without definition expansion;
- action: preserve as `CODEBOOK_BOUNDARY` and seek conceptual adjudication.

### REL-32023-009_ME_01

- transformation: Plan resources and mobility measures become delivered mobility services, investments or benefits for vulnerable transport users;
- T status: a legally defined beneficiary class whose access to support is shaped, but not clearly a target in the conventional conduct/compliance sense;
- C3: remains provisionally defensible because the entity is legally interposed and the full benefit must pass through to T;
- ontology fit: no existing mechanism fits without definition expansion;
- action: preserve as `CODEBOOK_BOUNDARY` and seek conceptual adjudication.

The evidence presently favors H1 — an incomplete vocabulary for a material implementation/delivery relation — over silently broadening translation. H3 remains conceptually credible because the targets are principally beneficiaries. No Phase 6 reclassification is applied without researcher or David adjudication.

PROVISIONAL_NEW_MECHANISM_REQUIRED = YES

This is a boundary flag, not creation of a tenth formal mechanism.

## F. Ontology assessment

NINE_MECHANISM_VOCABULARY_SUFFICIENT_FOR_CURRENT_POSITIVE_UNIVERSE = NO

This finding is limited to the frozen R3 positive universe and does not establish a general theoretical conclusion.

## G. Upstream changes

No relation is automatically reopened in Phase 8B. `upstream_review_required=NO` for all ten events.

If the researcher or David rejects H1 and concludes that material service delivery is not mediation of a regulatory R–T relation, Phase 6 C1/C3 must be reopened for `REL-32023-007`, `REL-32023-008` and `REL-32023-009`. This possibility is recorded but not applied.

## H. David questions

One conceptual question remains necessary:

> When a formally recognized third actor implements a regulator's programme and delivers legally safeguarded material benefits to a defined beneficiary group, should this remain regulatory intermediation despite falling outside the nine mechanisms, should translation be broadened to cover it, or should the R–I–T classification be reopened because the beneficiary is not a regulatory target in the required sense?

No additional question is required for the seven confirmed events; their adversarial distinctions are resolved by the legal evidence.

## I. Capability firewall

KNOWING_ASSURING_STEERING_CODED = NO

## J. RIA firewall

RIA_USED_AS_CODING_FRAME = NO

## Required outputs

Created:

- `07_mechanisms/MECHANISM_ADJUDICATION_MATRIX.csv`
- `07_mechanisms/MECHANISM_EVENTS_ADJUDICATED.csv`
- `07_mechanisms/MECHANISM_CODEBOOK_BOUNDARY_CASES.csv`
- `12_audits/R3_PHASE_8B_MECHANISM_ADJUDICATION_AUDIT.md`

No Phase 9 file or formal mechanism chain was created.

## Q1–Q9 success gate

| Gate | Result |
|---|---|
| Q1 — all ten events independently reviewed | PASS |
| Q2 — no label retained merely because Phase 8 assigned it | PASS |
| Q3 — every event distinguished from its strongest alternative | PASS |
| Q4 — implementation cases not forced into translation | PASS |
| Q5 — incomplete ontology considered separately from incorrect RIT | PASS |
| Q6 — no tenth mechanism silently added | PASS |
| Q7 — potential upstream RIT concern explicitly recorded | PASS |
| Q8 — David's conceptual question preserved | PASS |
| Q9 — no capability or architecture coding | PASS |

Phase 8B is complete. Phase 9 has not begun.

R3_PHASE_8B_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION
