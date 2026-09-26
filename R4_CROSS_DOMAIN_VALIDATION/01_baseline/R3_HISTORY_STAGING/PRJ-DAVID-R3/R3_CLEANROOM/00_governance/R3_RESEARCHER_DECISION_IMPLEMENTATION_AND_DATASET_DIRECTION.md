# R3 Researcher Decision Note
## Mechanism Boundary, Implementation, and Dataset Direction

**Project:** Regulatory Intermediation — David Levi-Faur  
**Round:** R3  
**Decision owner:** Igor Caires Machado  
**Status:** Researcher adjudication adopted for continuation of R3  
**Decision ID:** `R3-D08-IMPLEMENTATION`

---

## 1. Decision

The three Phase 8B codebook-boundary cases involving the operational implementation and material delivery of benefits will remain classified as **supported regulatory intermediation**.

They will not be reclassified as direct regulation or non-RIT relations.

The researcher therefore adopts a provisional tenth elementary mechanism:

`IMPLEMENTATION`

The three affected mechanism events will be recoded from:

`MECHANISM_UNRESOLVED / CODEBOOK_BOUNDARY`

to:

`IMPLEMENTATION`

This is a **researcher decision**, not a claim that `IMPLEMENTATION` is already part of a published Levi-Faur mechanism taxonomy.

The decision will be presented to David for evaluation as part of the proposed R3 dataset.

---

## 2. Why the decision is being made

The existing nine-code vocabulary successfully classified seven mechanism events but failed to classify three legally structured mediating events involving implementation and delivery.

Forcing those cases into `TRANSLATION` would stretch the existing definition.

Under the R3 codebook, `TRANSLATION` concerns the conversion of legal, scientific, technical, or regulatory content into another usable register.

The three boundary cases instead involve an operational transformation:

> a legally authorized regulatory programme, resources, or measures are converted by a formally recognized third actor into concrete implementation or delivery toward the target/beneficiary class.

The relevant transformation is therefore material/operational rather than primarily semantic, informational, interpretive, evaluative, or verificatory.

---

## 3. Conceptual definition

### IMPLEMENTATION

**Definition**

A regulatory intermediary performs `IMPLEMENTATION` when it operationally enacts a regulator's legally structured programme, measure, entitlement, or regulatory intervention vis-à-vis a target through a formally assigned third-party role.

Typical structure:

`regulatory programme / authorized measure / resources → I → operational execution or delivery → T`

### Diagnostic question

> Does the intermediary convert an upstream regulatory decision, programme, or legally authorized measure into concrete regulatory action or delivery toward the target?

### Include when

The intermediary has a formally recognized role in:

- executing a regulatory programme;
- operationalizing legally authorized measures;
- administering implementation toward a target group;
- delivering benefits, services, investments, or measures that constitute the operative link between R's programme and T.

### Exclude when

- the actor is merely complying with a rule as T;
- the actor only passes information (`TRANSMISSION`);
- the actor converts content between registers (`TRANSLATION`);
- the actor checks conformity (`VERIFICATION`);
- the actor evaluates adequacy (`EVALUATION_ASSESSMENT`);
- the actor merely provides a commercial or logistical service with no demonstrable role in an R–T regulatory relationship.

---

## 4. Boundary with TRANSLATION

`TRANSLATION` and `IMPLEMENTATION` remain distinct.

### TRANSLATION

Changes the **form, register, or usability of content**.

Example structure:

`scientific/legal/technical content → I → operationally usable content`

### IMPLEMENTATION

Changes the **state of regulatory action**.

Example structure:

`authorized programme/measure/resources → I → concrete execution/delivery toward T`

A plan becoming operational action is not automatically translation.

---

## 5. Boundary with ordinary policy delivery

Implementation is not automatically regulatory intermediation.

The existing three-condition RIT gate remains mandatory:

1. identifiable R–T regulatory relationship;
2. distinct institutionalized third-party role;
3. demonstrable mediating function.

`IMPLEMENTATION` is coded only after the relation has already passed this RIT test.

This prevents all contractors, administrators, service providers, or implementation bodies from automatically becoming regulatory intermediaries.

---

## 6. Status of the mechanism ontology

The R3 empirical mechanism vocabulary now contains ten provisional elementary mechanisms:

### Articulation
1. `TRANSMISSION`
2. `AGGREGATION`
3. `REPRESENTATION`

### Information treatment
4. `TRANSLATION`
5. `INTERPRETATION`
6. `EVALUATION_ASSESSMENT`
7. `CLASSIFICATION_RANKING`

### Regulatory reliability
8. `MONITORING`
9. `VERIFICATION`

### Provisional unassigned mechanism
10. `IMPLEMENTATION`

`IMPLEMENTATION` will remain:

`FAMILY_UNASSIGNED_PROVISIONAL`

until comparative analysis establishes whether it:

- belongs to an existing higher-order family;
- requires a separate family such as operationalization;
- should instead be treated at another analytical level.

The 3–4–2 family structure is therefore not silently rewritten.

---

## 7. Implications for Phase 8B

The researcher decision does not overwrite the Phase 8 or Phase 8B historical files.

Preserve:

- original Phase 8 coding;
- adversarial Phase 8B results;
- the three `CODEBOOK_BOUNDARY` findings.

Create a new researcher-adjudicated version recording:

- previous status;
- researcher decision;
- final mechanism code;
- rationale;
- date;
- decision ID.

This preserves the provenance chain:

`Phase 8 → Phase 8B adversarial review → researcher adjudication`

---

# 8. Main research question

The R3 dataset will now be developed primarily to answer:

> **How are regulatory intermediation mechanisms organized and combined across actors and regulatory relations in EU climate regulation, and what regulatory capacities do these configurations appear designed to provide?**

This question has two analytically distinct parts.

## Part A — empirically observable from the legal design

> How are mechanisms distributed and combined across intermediaries, relations, and laws?

## Part B — theoretical interpretation

> What regulatory capacities do different configurations appear designed to provide?

The dataset should answer Part A directly.

Part B must be derived later and must not be coded as an assumed result.

---

# 9. Dataset architecture required by the research question

The dataset should not become one flat spreadsheet.

It should preserve linked analytical levels:

## Level 1 — INSTRUMENT

Unit:

`LAW`

Answers:

- what regulatory system does the law establish?
- what is its declared orientation?

## Level 2 — INTERMEDIARY

Unit:

`LAW × INTERMEDIARY`

Answers:

- who intermediates?
- under what institutional configuration?
- with what status, independence, accountability, and legal effect?

## Level 3 — RELATION

Unit:

`LAW × R–I–T RELATION`

Answers:

- who regulates whom through whom?
- what regulatory object is involved?

## Level 4 — MECHANISM EVENT

Unit:

`RELATION × INTERMEDIARY × TRANSFORMATION`

Answers:

- how does intermediation occur?
- what is the input?
- what transformation occurs?
- what output is produced?
- who receives it?

## Level 5 — MECHANISM CONFIGURATION

Unit:

`RELATION / LAW × CONFIGURATION`

Answers:

- which mechanisms coexist?
- which are sequential?
- which are parallel?
- which combinations recur?

## Level 6 — REGULATORY CAPACITY

Derived analytical layer.

Potential constructs include:

- Knowing
- Assuring
- Steering

These must remain hypotheses until derived from the empirical mechanism configurations.

## Level 7 — ARCHITECTURE

Derived comparative layer.

Answers:

- how are actors, relations, mechanisms, institutional attributes, and regulatory capacities configured across laws?

---

# 10. Core dataset tables

The proposed final R3 dataset should contain at minimum:

1. `INSTRUMENT_PROFILE`
2. `ACTOR_REGISTER`
3. `LAW_INTERMEDIARY`
4. `RELATIONS`
5. `MECHANISM_EVENTS`
6. `MECHANISM_CONFIGURATIONS`
7. `ACCOUNTABILITY_AND_CONTROL`
8. `LEGAL_EVIDENCE`
9. `NEGATIVE_BOUNDARY_CASES`
10. `RESEARCH_QUESTION_MAP`
11. `DERIVED_CAPACITY_PROFILE` — later analytical layer
12. `DATA_DICTIONARY`
13. `DECISION_LOG`

The primary human-facing comparative sheet should remain:

`LAW_INTERMEDIARY`

but mechanisms must remain in a one-to-many child table.

---

# 11. Next analytical sequence

The R3 should continue before being presented to David.

### Phase 8C — Researcher adjudication update
Implement this decision without rewriting historical audit outputs.

### Phase 9 — Mechanism configurations
Determine whether multiple events within relations are independent, parallel, or sequential.

### Phase 10 — Research-question-oriented dataset design
Construct the final linked schema explicitly around the main research question.

### Phase 11 — Capacity derivation
Evaluate whether empirical mechanism configurations support higher-order capacities such as Knowing, Assuring, and Steering.

These capacities must be derived, not imposed.

### Phase 12 — Cross-case architecture
Compare laws, intermediaries, relations, configurations, and derived capacities.

### David package
Present:

- the empirical dataset proposal;
- the mechanism codebook including the researcher-added `IMPLEMENTATION`;
- the rationale and provenance of that addition;
- the main research question;
- the structure linking actors → relations → mechanisms → configurations → capacities;
- specific points on which David's evaluation is requested.

---

# 12. What will be presented to David

The message to David should not ask him to make the researcher's unresolved coding decision.

Instead it should state:

> During the adversarial mechanism review, three supported intermediation relations involving material programme implementation did not fit the nine-mechanism vocabulary. I decided to retain these relations as intermediation and provisionally add `IMPLEMENTATION` as a tenth elementary mechanism, rather than broaden `TRANSLATION`. I preserved the original boundary finding and the full audit trail so that you can evaluate the decision.

David can then evaluate:

- whether the decision is theoretically defensible;
- whether implementation belongs at mechanism level;
- whether the ten-code vocabulary is appropriate;
- whether the proposed dataset architecture answers the research question.

---

## 13. Current research principle

The researcher is responsible for making transparent and auditable analytical decisions.

David's role at this stage is not to substitute for researcher adjudication, but to evaluate and challenge the proposed conceptual architecture.

The R3 therefore proceeds with a documented researcher decision rather than remaining blocked at the mechanism boundary.

---

**Decision status:** `ADOPTED_PROVISIONALLY_FOR_R3`

**Next status:** `READY_FOR_PHASE_8C_AND_DATASET_ARCHITECTURE_DEVELOPMENT`
