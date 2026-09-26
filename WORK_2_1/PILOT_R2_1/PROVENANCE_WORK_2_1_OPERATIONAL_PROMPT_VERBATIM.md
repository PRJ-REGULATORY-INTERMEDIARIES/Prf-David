# WORK 2.1 — PILOT R2.1
## Operational Prompt for a Staged, Auditable Recalibration of the Regulatory Intermediation Dataset

### Purpose

This prompt defines **WORK 2.1 / PILOT R2.1**, a new methodological pilot designed to rebuild and test the coding architecture for regulatory intermediation before any production coding of the five substantive R2 cases.

The pilot must be executed **in stages**, with **mandatory stop points, audit reports, and explicit researcher authorization before continuation**.

The objective is not to maximize the number of coded relations. The objective is to produce a theoretically defensible, auditable and reusable dataset architecture capable of explaining the **regulatory architecture of an instrument as a whole**, the **R–I–T relations embedded in it**, and the **mechanisms through which intermediation occurs**.

Do **not** proceed to the five substantive R2 cases during this work.

---

# 1. Core methodological orientation

The pilot must treat the **regulatory instrument as the primary interpretive context**.

Do not begin by coding articles as isolated analytical units.

Instead, follow this order:

1. understand the instrument as a whole;
2. identify its declared regulatory purpose and orientation;
3. identify all relevant actors;
4. identify regulator–target relationships;
5. reconstruct possible intermediary roles;
6. identify episodes of regulatory intermediation;
7. identify and decompose the mechanisms of intermediation;
8. anchor every claim in precise legal evidence;
9. only then aggregate results to characterize the architecture of the instrument.

Articles, recitals, annexes and cross-references are **units of evidence**, not necessarily the substantive unit of analysis.

---

# 2. Theoretical corrections from David Levi-Faur

The following rules must be treated as binding methodological guidance for this pilot.

## 2.1 Intermediation is not established by the presence of a third actor

Do not infer:

> R + third actor + T = regulatory intermediation.

A third actor must perform a demonstrable mediating function.

## 2.2 Bindingness is not the threshold

The output of an intermediary does not need to be legally binding.

However:

> mandatory consultation is evidence of institutionalization, but is not sufficient by itself to establish intermediation.

Separate:

- procedural mandatoriness;
- substantive bindingness of the output;
- existence of intermediation.

## 2.3 Advice/expertise alone is insufficient

Do not use:

> institutionalized adviser = intermediary.

Require three cumulative conditions:

1. **Identifiable R–T relationship**
2. **Institutionalized third-party role**
3. **Demonstrable mediating function**

The intermediary must do something that mediates the regulatory relationship, such as transmitting, translating, aggregating, interpreting, evaluating, classifying, representing, monitoring, verifying, or otherwise transforming something relevant to R’s regulation of T.

## 2.4 R, I and T are relation-specific working roles, but role switching remains provisional

Do not assume that an organization has a fixed essence as regulator, intermediary or target.

At the same time, do not automatically infer that the same actor can occupy all three roles across relations.

Where a role switch appears, flag it for researcher review.

Use:

`ROLE_SWITCH_REVIEW = YES`

## 2.5 Cross-provision reconstruction is allowed

R, I and T do not need to appear in the same article.

A relation can be reconstructed across provisions when the legal chain can be documented.

Every reconstructed relation must identify the provisions that establish:

- R;
- I;
- T;
- the R–T regulatory relationship;
- the intermediary’s participation;
- the mediating mechanism.

Evidence levels:

- `E1_EXPLICIT`
- `E2_CROSS_PROVISION_RECONSTRUCTED`
- `E3_INFERRED_CONTEXTUAL`

E3 should normally remain uncertain unless the inference is exceptionally strong.

## 2.6 Mechanism must be coded, not only actor

For every supported intermediation relation, answer:

> What precisely is being mediated, through which mechanism, between which actors, and on what legal evidence?

If this cannot be answered, do not classify the relation as confirmed intermediation.

---

# 3. Proposed analytical architecture of the dataset

The dataset must represent the regulation at multiple linked levels.

## LEVEL A — INSTRUMENT

One row per regulatory instrument.

Required fields:

- `instrument_id`
- `celex_id`
- `official_title`
- `instrument_type`
- `date`
- `legal_basis`
- `policy_domain`
- `declared_regulatory_objective`
- `declared_primary_orientation`
- `principal_regulatory_problem`
- `principal_targets_declared_or_implied`
- `primary_regulatory_authorities`
- `notes_on_scope`

Important:

`declared_primary_orientation` must be coded **before** mechanism aggregation.

It must describe what the instrument formally seeks to accomplish, not what mechanisms later appear most frequently.

This permits comparison between:

- **declared regulatory orientation**
- **observed regulatory architecture**

Do not infer one from the other.

---

## LEVEL B — ACTOR REGISTER

One row per actor or actor class identified in the instrument.

Fields:

- `actor_id`
- `actor_name`
- `actor_type`
- `institutional_level`
- `formal_legal_status`
- `provisions`
- `possible_roles`
- `notes`

Do not permanently label an actor as R, I or T at this stage.

---

## LEVEL C — REGULATORY RELATION / EPISODE

This is the core substantive unit.

One row = one reconstructed regulatory relation or episode.

Fields:

- `relation_id`
- `instrument_id`
- `R_actor`
- `I_actor`
- `T_actor`
- `regulatory_object`
- `relation_purpose`
- `relation_description`
- `orientation`
- `intermediation_status`
- `evidence_level`
- `role_switch_review`
- `researcher_review_flag`

Allowed `intermediation_status` values:

- `SUPPORTED_INTERMEDIATION`
- `DIRECT_R_T`
- `LEGAL_RELATION_NON_RIT`
- `UNCERTAIN`
- `NOT_SUPPORTED`

---

## LEVEL D — MECHANISM EVENT

A relation may contain one or more mechanisms.

Do **not** force one mechanism per relation.

Each mechanism must have its own row linked to `relation_id`.

Fields:

- `mechanism_event_id`
- `relation_id`
- `mechanism_code`
- `mechanism_family`
- `primary_or_secondary`
- `input`
- `mediated_object`
- `transformation`
- `output`
- `recipient`
- `mechanism_trace`
- `mechanism_evidence`
- `confidence`
- `researcher_review_flag`

Every supported mechanism must complete this logic:

> INPUT → INTERMEDIARY TRANSFORMATION → OUTPUT → RECIPIENT → RELEVANCE TO R–T

Mandatory `MECHANISM_TRACE` template:

> [I] receives/observes [X], transforms it through [mechanism], produces [Y], and this output contributes to [R]’s regulation of [T] by [regulatory connection].

If this sentence cannot be completed with evidence, the mechanism is not yet supported.

---

## LEVEL E — LEGAL EVIDENCE

One row per evidence fragment.

Fields:

- `evidence_id`
- `relation_id`
- `mechanism_event_id`
- `article`
- `paragraph`
- `recital`
- `annex`
- `quoted_or_paraphrased_text`
- `evidence_function`
- `source_location`
- `evidence_level`
- `coder_note`

---

# 4. Mechanism ontology for the pilot

Use the following nine mechanisms as the **primary operational vocabulary**.

Do not expand this list during initial coding unless a genuinely recurrent mechanism cannot be represented.

## 4.1 ARTICULATION

This family is a **derived didactic and analytical grouping**, not a claim that David Levi-Faur published a fixed three-family taxonomy.

It contains three mechanisms:

### TRANSMISSION
Moves information, signals, reports, demands or regulatory content from one actor to another.

Core question:

> What is being carried from A to B?

### AGGREGATION
Combines multiple inputs into a consolidated or synthesized output.

Core question:

> Are many inputs being transformed into one structured output?

### REPRESENTATION
Carries or articulates the interests, preferences, experiences or voice of a constituency.

Core question:

> On whose behalf does the intermediary speak?

---

# 5. TREATMENT OF INFORMATION

Second derived family.

It contains four mechanisms.

### TRANSLATION
Converts content from one register or context into another usable register.

Examples:

- science → regulatory criteria
- abstract rule → operational guidance
- technical standard → implementation practice

Core question:

> Is something being converted so another actor can use it?

### INTERPRETATION
Clarifies or stabilizes the meaning of a rule, standard or concept.

Core question:

> What does this rule or standard mean?

### EVALUATION / ASSESSMENT
Applies criteria, expertise or judgment to evidence, proposals, conduct or claims.

Core question:

> What judgment is being made and according to which criteria?

### CLASSIFICATION / RANKING
Transforms complexity into categories, ratings, scores, statuses or ordered positions.

Core question:

> Is the intermediary assigning a category, score, status or relative position?

---

# 6. REGULATORY RELIABILITY

Third derived family.

Use the Portuguese analytical label:

**CONFIABILIDADE REGULATÓRIA**

Do not treat this as a guarantee that regulation succeeds.

It means the production of observability, evidentiary confidence or trustworthy compliance information.

It contains two mechanisms.

### MONITORING
Observes, tracks or records conduct, performance or conditions over time.

Core question:

> What is happening with the target?

### VERIFICATION
Checks whether a claim, report, condition or behavior conforms to an existing standard or requirement.

Core question:

> Is the claim or compliance condition supported by evidence?

Mnemonic distinction:

> Monitoring observes. Verification checks.

---

# 7. Important conceptual separations

Do not collapse the following categories.

## 7.1 Actor
Who performs the activity.

## 7.2 Legal action
What the text formally says the actor does.

Examples:

- advise
- consult
- report
- assess
- monitor
- review
- issue an opinion

## 7.3 Regulatory function
Why the activity exists in the regulatory arrangement.

Examples:

- expertise
- advice
- implementation support
- oversight
- compliance support

## 7.4 Mechanism
How the intermediary transforms, moves, evaluates or validates something in the R–T relationship.

## 7.5 Institutional technology
A compound institutional arrangement.

Examples:

- audit
- testing
- certification
- accreditation
- environmental impact assessment

These may combine several mechanisms.

Do not automatically use them as primary mechanisms.

Example:

`institutional_technology = CERTIFICATION`

may contain:

`primary_mechanism = VERIFICATION`

## 7.6 Systemic effect
Possible effects such as:

- assurance
- trust
- credibility
- compliance
- legitimacy

Do not code these as elementary mechanisms.

---

# 8. Derived 3–4–2 profile

Create an instrument-level derived table:

## `MECHANISM_FAMILY_PROFILE`

Fields:

- `instrument_id`
- `n_articulation_events`
- `n_information_treatment_events`
- `n_regulatory_reliability_events`
- `share_articulation`
- `share_information_treatment`
- `share_regulatory_reliability`
- `mechanism_diversity_n`
- `mechanism_family_diversity_n`
- `dominant_family_observed`
- `declared_orientation`
- `declared_vs_observed_note`
- `researcher_review_flag`

The 3–4–2 logic is:

### Articulation — 3
1. Transmission
2. Aggregation
3. Representation

### Treatment of Information — 4
4. Translation
5. Interpretation
6. Evaluation / Assessment
7. Classification / Ranking

### Regulatory Reliability — 2
8. Monitoring
9. Verification

These families are **exploratory derived categories**.

Do not present them as validated factors.

They are being retained:

1. for didactic clarity;
2. for descriptive comparison across instruments;
3. as a future empirical hypothesis.

Future analyses may test whether the mechanisms empirically cluster in these or different dimensions.

Do not perform factor analysis in this pilot.

---

# 9. Regulatory architecture concept

For this pilot, use the working concept:

## Regulatory Intermediation Architecture

Operational definition:

> The configuration of actors, regulatory relations, intermediary mechanisms, functional sequences, orientations and evidentiary links through which a regulatory instrument organizes the production, circulation, treatment and validation of regulatory information and action.

This is a working analytical concept.

Do not claim that it is already a validated extension of the RIT framework.

The pilot must test whether this concept improves explanatory power relative to the previous relation-by-relation coding approach.

---

# 10. Instrument-first analytical logic

The pilot must follow this exact sequence:

## First: What does the regulation claim to do?

Identify:

- regulatory objective;
- regulatory object;
- principal targets;
- principal regulatory authorities;
- scope;
- declared mode of governance.

Do not use mechanism frequencies at this stage.

## Second: Who exists in the instrument?

Build the actor register.

## Third: What regulatory relations exist?

Reconstruct direct and mediated relations.

## Fourth: Where does intermediation occur?

Apply the three-condition test.

## Fifth: What mechanisms occur?

Code mechanism events.

## Sixth: Do mechanisms form chains?

Reconstruct mechanism sequences where evidence supports them.

Example:

`MONITORING → TRANSMISSION → EVALUATION`

Do not invent temporal order where the text does not support it.

## Seventh: What architecture emerges?

Only after coding all relations, aggregate mechanisms and families.

Then compare:

> declared orientation vs observed architecture.

---

# 11. Population context for later work

This pilot does not construct the full population.

However, document the intended population logic for subsequent work.

## Legal universe

The central official source for EU legal acts is EUR-Lex / CELEX.

For later population construction, distinguish:

### Primary law
Treaties and constitutional-level sources.

Not part of the initial regulatory population.

### Binding secondary EU legislation
Initial population candidate:

- Regulations
- Directives
- Decisions

These should be the initial focus.

### Delegated and implementing acts
Treat as a second layer linked to base acts.

Do not mix them automatically with base legislation.

### Soft law
Recommendations, opinions, communications, guidelines and other non-binding instruments.

Keep outside the initial population unless later theoretically justified.

### National law
Member-State legislation and transposition measures.

Outside the initial EU-level population.

It may become a later layer.

Important:

EUR-Lex is an official legal-document universe, not by itself a substantive population definition.

Population inclusion must still be justified by research criteria.

---

# 12. Pilot boundary

This work is a new methodological pilot.

Use the label:

# WORK 2.1 — PILOT R2.1

Do not begin the five substantive R2 cases.

Do not merge this pilot with the production corpus.

Do not overwrite previous pilot files.

Create a new folder / version namespace.

Recommended:

`WORK_2_1/PILOT_R2_1/`

---

# 13. Mandatory staged execution protocol

This prompt must NOT be executed end-to-end in one run.

The agent must proceed phase by phase.

At the end of every phase:

1. save all outputs;
2. produce an audit report;
3. identify uncertainties and methodological risks;
4. explicitly stop;
5. wait for researcher authorization.

The agent may continue only after receiving an explicit command such as:

`CONTINUE TO PHASE 2`

or equivalent.

Never infer authorization from silence.

---

# PHASE 0 — ENVIRONMENT AND SOURCE AUDIT

Objectives:

- inventory all relevant pilot files;
- identify authoritative legal text;
- verify versioning;
- verify hashes where available;
- identify prior coding outputs;
- ensure that previous versions will not be overwritten.

Deliverables:

- `PHASE_0_SOURCE_INVENTORY.csv`
- `PHASE_0_AUDIT_REPORT.md`

Audit report must include:

- files found;
- source hierarchy;
- missing files;
- inconsistencies;
- version risks;
- proposed working directory.

STOP.

End with:

`PHASE_0_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION`

Do not continue.

---

# PHASE 1 — INSTRUMENT-LEVEL RECONSTRUCTION

Read the complete instrument.

Do not code mechanisms yet.

Produce a whole-instrument analytical profile.

Identify:

- declared purpose;
- regulatory object;
- legal scope;
- principal targets;
- principal regulatory authorities;
- governance logic;
- major institutional components.

Deliverables:

- `INSTRUMENT_PROFILE_v0_1.csv`
- `PHASE_1_WHOLE_INSTRUMENT_MEMO.md`
- `PHASE_1_AUDIT_REPORT.md`

The audit must distinguish:

- explicit statements;
- cross-provision reconstruction;
- interpretive inference.

STOP.

`PHASE_1_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION`

---

# PHASE 2 — ACTOR REGISTER

Identify all actors and actor classes across the complete instrument.

Do not assign permanent R/I/T identities.

Document:

- institutional status;
- legal provisions;
- tasks;
- possible relational roles.

Deliverables:

- `ACTOR_REGISTER_v0_1.csv`
- `ACTOR_ROLE_NOTES_v0_1.md`
- `PHASE_2_AUDIT_REPORT.md`

STOP.

`PHASE_2_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION`

---

# PHASE 3 — REGULATORY RELATION RECONSTRUCTION

Reconstruct all candidate regulatory relations.

At this phase, do not yet force an intermediation decision.

For each relation identify:

- R candidate;
- T candidate;
- possible I candidate;
- regulatory object;
- legal action;
- evidence;
- evidence level.

Deliverables:

- `RELATION_REGISTER_v0_1.csv`
- `CROSS_PROVISION_LINKS_v0_1.csv`
- `PHASE_3_AUDIT_REPORT.md`

Audit:

- direct vs triadic candidate relations;
- uncertain targets;
- uncertain regulators;
- reconstructed chains;
- possible role switching.

STOP.

`PHASE_3_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION`

---

# PHASE 4 — INTERMEDIATION GATE

Apply the three-condition test to every candidate relation:

1. identifiable R–T relationship;
2. institutionalized third-party role;
3. demonstrable mediating function.

Classify:

- `SUPPORTED_INTERMEDIATION`
- `DIRECT_R_T`
- `LEGAL_RELATION_NON_RIT`
- `UNCERTAIN`
- `NOT_SUPPORTED`

Deliverables:

- `RELATIONS_ADJUDICATED_v0_1.csv`
- `NEGATIVE_BOUNDARY_CASES_v0_1.csv`
- `UNCERTAIN_CASES_v0_1.csv`
- `PHASE_4_AUDIT_REPORT.md`

The audit must pay special attention to advice/expertise cases.

STOP.

`PHASE_4_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION`

---

# PHASE 5 — MECHANISM CODING

For every supported or plausible intermediation relation, identify the mechanism.

Code:

- input;
- mediated object;
- transformation;
- output;
- recipient;
- primary mechanism;
- secondary mechanism where necessary;
- mechanism family;
- evidence;
- confidence.

Do not code a mechanism from actor type alone.

Deliverables:

- `MECHANISM_EVENTS_v0_1.csv`
- `MECHANISM_TRACE_v0_1.csv`
- `MECHANISM_UNCERTAINTY_LOG_v0_1.csv`
- `PHASE_5_AUDIT_REPORT.md`

STOP.

`PHASE_5_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION`

---

# PHASE 6 — MECHANISM CHAIN RECONSTRUCTION

Identify whether mechanism events form supported sequences.

Possible examples:

- `TRANSMISSION → EVALUATION`
- `MONITORING → TRANSMISSION`
- `MONITORING → VERIFICATION`
- `AGGREGATION → EVALUATION → TRANSLATION`
- `VERIFICATION → TRANSMISSION`

Only code sequences when legal or functional evidence supports the ordering.

Deliverables:

- `MECHANISM_CHAINS_v0_1.csv`
- `CHAIN_DIAGRAM_SPEC_v0_1.md`
- `PHASE_6_AUDIT_REPORT.md`

Audit:

- chain length;
- repeated mechanisms;
- branching;
- feedback loops;
- uncertain ordering.

STOP.

`PHASE_6_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION`

---

# PHASE 7 — 3–4–2 DERIVED PROFILE

Aggregate the nine mechanisms into the three exploratory families.

Produce:

- counts;
- shares;
- family diversity;
- dominant observed family;
- mechanism diversity;
- comparison with declared regulatory orientation.

Deliverables:

- `MECHANISM_FAMILY_PROFILE_v0_1.csv`
- `DECLARED_VS_OBSERVED_PROFILE_v0_1.csv`
- `PHASE_7_AUDIT_REPORT.md`

Important:

Do not infer that presence of all three families means greater quality, maturity or effectiveness.

At this stage this is a descriptive architecture.

STOP.

`PHASE_7_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION`

---

# PHASE 8 — DATASET ASSEMBLY

Assemble the pilot workbook.

Required sheets:

1. `README`
2. `INSTRUMENT_PROFILE`
3. `ACTOR_REGISTER`
4. `RELATIONS`
5. `MECHANISM_EVENTS`
6. `MECHANISM_CHAINS`
7. `MECHANISM_FAMILY_PROFILE`
8. `NEGATIVE_BOUNDARY_CASES`
9. `UNCERTAIN_CASES`
10. `LEGAL_EVIDENCE`
11. `DECISION_LOG`
12. `DATA_DICTIONARY`

Suggested file:

`WORK_2_1_PILOT_R2_1_REGULATORY_INTERMEDIATION_ARCHITECTURE.xlsx`

Also produce:

- `PILOT_R2_1_METHOD_NOTE.md`
- `PILOT_R2_1_CHANGELOG.md`
- `PILOT_R2_1_MECHANISM_CODEBOOK.md`

STOP.

`PHASE_8_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION`

---

# PHASE 9 — COMPARISON WITH PREVIOUS PILOT

Only after explicit authorization.

Compare the new architecture-first pilot with the previous pilot.

The comparison must not ask merely which has more relations.

Evaluate:

- explanatory completeness;
- theoretical clarity;
- mechanism observability;
- treatment of cross-provision relations;
- distinction between action/function/mechanism;
- capacity to reconstruct mechanism chains;
- transparency of negative cases;
- uncertainty handling;
- reproducibility;
- auditability;
- ability to characterize the whole regulatory instrument;
- risk of conceptual stretching.

Deliverables:

- `PILOT_A_VS_R2_1_COMPARISON.csv`
- `PILOT_A_VS_R2_1_METHOD_COMPARISON.md`
- `PHASE_9_AUDIT_REPORT.md`

Do not automatically select a winner.

Identify strengths, weaknesses and trade-offs for researcher/David adjudication.

STOP.

`PHASE_9_COMPLETE — RESEARCHER_ADJUDICATION REQUIRED`

---

# 14. Audit-report template for every phase

Every phase audit must contain:

## A. What was done
Short factual description.

## B. Inputs used
Files, legal sources and prior decisions.

## C. Outputs created
Exact filenames.

## D. Quantitative summary
Counts of rows, actors, relations, mechanisms or other relevant units.

## E. Methodological decisions
Any interpretive decision taken.

## F. Uncertainties
Cases where evidence is incomplete or competing interpretations exist.

## G. Deviations from prompt
Any deviation, however minor.

## H. Quality-control checks
Checks performed for missing values, duplicates, evidence links and logical consistency.

## I. Researcher decisions required
Questions that must be answered before continuing.

## J. Status
Use exactly:

`READY_FOR_RESEARCHER_REVIEW`

Then STOP.

---

# 15. Quality rules

Throughout the pilot:

- preserve provenance;
- do not overwrite prior versions;
- never silently change a classification;
- document every cross-provision reconstruction;
- separate evidence from interpretation;
- keep uncertainty explicit;
- avoid circular mechanism coding;
- do not infer mechanism from actor name;
- do not infer intermediation from consultation alone;
- do not infer target from general policy relevance alone;
- distinguish legal object from regulatory target;
- distinguish procedural force from output bindingness;
- maintain one-to-many relations between relations and mechanism events;
- keep the nine mechanisms as primary codes;
- keep the three families as derived experimental variables.

---

# 16. Final success criterion

PILOT R2.1 is successful if the dataset can answer, for the instrument as a whole:

1. What does this regulation seek to accomplish?
2. Who regulates whom?
3. Which relations are direct and which are intermediated?
4. Which actors function as intermediaries in each relation?
5. What precisely is mediated?
6. Through which mechanism?
7. What is the input?
8. What transformation occurs?
9. What output is produced?
10. Who receives it?
11. How do mechanisms combine into chains?
12. What functional architecture emerges across the whole instrument?
13. How does the observed architecture compare with the regulation’s declared orientation?
14. Which claims are explicit, reconstructed or uncertain?

The agent must not begin production coding of the five substantive R2 cases unless the researcher explicitly authorizes it after reviewing the final pilot audit.

---

# 17. First execution command

Begin ONLY with:

## PHASE 0 — ENVIRONMENT AND SOURCE AUDIT

Do not execute any later phase.

At completion, stop and return the Phase 0 audit report for researcher review.
