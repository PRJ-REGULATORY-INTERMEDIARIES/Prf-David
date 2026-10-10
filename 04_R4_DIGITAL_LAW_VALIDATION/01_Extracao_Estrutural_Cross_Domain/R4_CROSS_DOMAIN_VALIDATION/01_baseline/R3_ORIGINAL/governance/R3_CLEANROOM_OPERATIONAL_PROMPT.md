# R3 CLEAN-ROOM — OPERATIONAL PROMPT
## Five-Case Pilot for Regulatory Intermediation Architecture

**Project:** Regulatory Intermediation — David Levi-Faur  
**Round:** R3  
**Mode:** Full clean-room reconstruction  
**Primary objective:** build a new five-case dataset from scratch, using only newly acquired official legal sources and the methodological learning register, without reusing any previous corpus, coding, classification, adjudication, or dataset output.

---

# 0. NON-NEGOTIABLE EXECUTION RULE

This prompt MUST NOT be executed end-to-end in one run.

The agent must work in **strict phases**.

At the end of every phase:

1. save all outputs;
2. produce an audit report;
3. list uncertainties;
4. list methodological decisions made;
5. list researcher decisions required;
6. STOP;
7. wait for explicit researcher authorization.

The agent may proceed only after receiving a command such as:

`CONTINUE TO PHASE 2`

or:

`APPROVED — CONTINUE`

Silence is not authorization.

Never skip a phase.

Never combine two phases in one execution unless the researcher explicitly instructs it.

---

# 1. R3 CLEAN-ROOM PRINCIPLE

Create a completely new research workspace.

## Forbidden as empirical inputs

Do NOT use, open, inspect, copy, parse, compare, quote, or rely on:

- Pilot A;
- R2;
- R2.1;
- v1.3;
- v1.4;
- datasets previously sent to David;
- previous corpora;
- prior actor maps;
- prior relation maps;
- prior mechanism assignments;
- prior adjudication notes;
- prior human-review outputs;
- prior model outputs;
- prior Excel workbooks;
- prior explanatory notes;
- prior summaries of the five cases;
- previous case-specific decisions.

The only exception is metadata strictly necessary to identify that a forbidden file exists. Do not inspect substantive contents.

## Allowed methodological inputs

The agent MAY use:

1. this operational prompt;
2. `R3_LEARNING_REGISTER_AND_CLEANROOM_PLAN.md`;
3. theoretical sources explicitly authorized by the researcher;
4. newly acquired official legal texts;
5. newly created R3 outputs;
6. researcher decisions issued during R3.

If a prior file contains a legal text, do not use it. Acquire a new official copy instead.

---

# 2. R3 RESEARCH OBJECTIVE

The goal is not simply to identify intermediaries.

The goal is to construct a dataset capable of explaining the **architecture of regulatory intermediation** across five EU regulatory instruments.

The dataset must reveal:

- what each law seeks to regulate;
- who regulates whom;
- which third actors intervene;
- whether they qualify as regulatory intermediaries;
- what they mediate;
- how they mediate it;
- what mechanism is used;
- what legal effect their output has;
- how they are institutionalized;
- how they are held accountable;
- whether intermediaries are themselves regulated;
- whether mechanisms form chains;
- whether recurrent architectural patterns appear across the five cases.

---

# 3. FIVE R3 CASES

The five cases are fixed for this pilot:

1. `32003L0087`
2. `32015D1814`
3. `32018R0842`
4. `32021R1119`
5. `32023R0955`

The excluded case:

`32000D0293`

must NOT be reintroduced.

Do not use previous labels, titles, descriptions, classifications or case summaries.

For each CELEX number, resolve the official title independently from EUR-Lex.

---

# 4. SOURCE POLICY

For each of the five CELEX acts:

1. acquire a fresh copy directly from an official EU legal source;
2. prioritize EUR-Lex / CELLAR;
3. record the exact URL;
4. record retrieval date and time;
5. record CELEX;
6. record document type;
7. record language;
8. record whether the text is:
   - original act as adopted;
   - corrigendum;
   - consolidated version;
   - amended version.

## Default coding source

Use the **original Official Journal act as adopted** as the primary coding source, unless the researcher explicitly changes this rule.

A current consolidated version may be downloaded for reference, but must remain outside substantive coding unless authorized.

Do not mix versions within a case.

Generate SHA-256 hashes for every acquired source.

---

# 5. NEW R3 DIRECTORY

Create a new independent folder:

`R3_CLEANROOM/`

Recommended structure:

```text
R3_CLEANROOM/
├── 00_governance/
├── 01_sources/
│   ├── 32003L0087/
│   ├── 32015D1814/
│   ├── 32018R0842/
│   ├── 32021R1119/
│   └── 32023R0955/
├── 02_corpus/
├── 03_instrument_profiles/
├── 04_actor_register/
├── 05_law_intermediary/
├── 06_relations/
├── 07_mechanisms/
├── 08_evidence/
├── 09_research_questions/
├── 10_cross_case/
├── 11_dataset/
├── 12_audits/
└── 13_reports/
```

Do not modify any prior project folder.

---

# 6. CORE UNIT ARCHITECTURE

The new R3 dataset must use linked levels.

## LEVEL 1 — INSTRUMENT

One row per law.

## LEVEL 2 — LAW × INTERMEDIARY

One row per combination of law and intermediary.

This is the main comparative unit requested by David in his feedback to Ivana.

## LEVEL 3 — REGULATORY RELATION

One row per reconstructed R–I–T or R–T relation.

## LEVEL 4 — MECHANISM EVENT

One row per mechanism within a relation.

A single relation may contain multiple mechanisms.

## LEVEL 5 — LEGAL EVIDENCE

One row per evidentiary fragment supporting a claim.

## LEVEL 6 — RESEARCH QUESTION MAP

One row per theoretical or empirical question the dataset can help answer.

---

# 7. THREE-CONDITION INTERMEDIATION TEST

A third actor qualifies as a regulatory intermediary only when all three conditions are satisfied.

## Condition 1 — identifiable R–T relationship

There must be an identifiable regulatory relationship between regulator and target.

## Condition 2 — institutionalized third-party role

The third actor must have a legally or institutionally recognizable role distinct from R and T.

## Condition 3 — demonstrable mediating function

The actor must perform a function that mediates something relevant to the R–T relationship.

Possible operations include:

- transmission;
- translation;
- aggregation;
- interpretation;
- evaluation;
- classification;
- representation;
- monitoring;
- verification;
- other transformation only if explicitly justified.

Do not classify a relation as intermediation merely because:

- the actor is consulted;
- the actor advises;
- the actor has expertise;
- the actor is independent;
- the actor is institutionally recognized;
- three actors appear in the same article.

---

# 8. CROSS-PROVISION RECONSTRUCTION

R, I and T need not appear in the same article.

A relation may be reconstructed across provisions.

Every relation must identify legal evidence for:

- R;
- T;
- R–T regulatory relationship;
- I;
- I’s mediating role;
- mechanism.

Evidence levels:

- `E1_EXPLICIT`
- `E2_CROSS_PROVISION_RECONSTRUCTED`
- `E3_INFERRED_CONTEXTUAL`

E3 relations should normally remain uncertain unless exceptionally well-supported.

---

# 9. ROLE-SPECIFIC CODING

Do not assign permanent organizational identities such as:

> Commission = always R

or:

> Agency = always I.

R, I and T are relation-specific roles.

If the same actor appears to occupy different roles across relations, flag:

`ROLE_SWITCH_REVIEW = YES`

Do not treat role switching as theoretically settled.

---

# 10. MECHANISM ONTOLOGY

Use the following nine elementary mechanisms.

Do not infer them from actor type.

---

## FAMILY A — ARTICULATION

### TRANSMISSION
Moves information, signals, claims, reports or regulatory content from one actor to another.

### AGGREGATION
Combines multiple inputs into a structured or synthesized output.

### REPRESENTATION
Articulates the interests, preferences, experiences or voice of a constituency.

---

## FAMILY B — TREATMENT OF INFORMATION

### TRANSLATION
Converts content from one register or context into another usable form.

### INTERPRETATION
Clarifies or stabilizes the meaning of a rule, standard or concept.

### EVALUATION / ASSESSMENT
Applies criteria, expertise or judgment to evidence, proposals, behavior or claims.

### CLASSIFICATION / RANKING
Assigns a category, score, rating, status or ordered position.

---

## FAMILY C — REGULATORY RELIABILITY

### MONITORING
Observes, tracks or records behavior, performance or conditions over time.

### VERIFICATION
Checks whether a claim, condition or behavior conforms to a pre-existing requirement or standard.

---

# 11. STATUS OF THE 3–4–2 FAMILIES

The three families are:

- Articulation — 3 mechanisms
- Treatment of Information — 4 mechanisms
- Regulatory Reliability — 2 mechanisms

They are **exploratory derived categories**.

They are NOT to be represented as a published taxonomy of David Levi-Faur.

They may be used:

- descriptively;
- didactically;
- comparatively;
- as a future empirical hypothesis.

Do NOT perform factor analysis in R3.

Do NOT claim that a law is more mature, effective or better because it activates more families.

---

# 12. SEPARATE ANALYTICAL DIMENSIONS

Never collapse the following into one variable.

## Actor
Who acts.

## Legal action
What the legal text says the actor does.

## Regulatory function
Why that action matters in the regulatory arrangement.

## Mechanism
How mediation occurs.

## Institutional technology
A compound device such as:

- audit;
- testing;
- certification;
- accreditation;
- environmental impact assessment.

## Systemic effect
Possible effects such as:

- assurance;
- trust;
- credibility;
- compliance;
- legitimacy.

---

# 13. MECHANISM TRACE REQUIREMENT

Every supported mechanism event must complete:

> [I] receives/observes [X], transforms it through [M], produces [Y], and this output contributes to [R]’s regulation of [T] through [regulatory connection].

Required fields:

- input;
- mediated object;
- transformation;
- output;
- recipient;
- regulatory relevance.

If this cannot be stated clearly and supported by evidence, the mechanism must not be treated as confirmed.

---

# 14. LAW × INTERMEDIARY PROFILE

Each identified intermediary must receive its own row within each law.

Fields should include at minimum:

- `law_intermediary_id`
- `instrument_id`
- `intermediary_actor_id`
- `intermediary_name`
- `intermediary_type`
- `institutionalization`
- `mandatory_or_voluntary`
- `separation_from_target`
- `independence`
- `capacity_brought`
- `centrality`
- `orientation`
- `output_legal_effect`
- `accountability_to_whom`
- `accountability_for_what`
- `accountability_mechanism`
- `sanctions_or_consequences`
- `meta_intermediary_present`
- `notes`

---

# 15. OUTPUT LEGAL EFFECT

Code the legal effect of intermediary output separately from intermediation.

Possible categories:

- `INFORMATION_ONLY`
- `ADVISORY`
- `SUPPORTING_EVIDENCE`
- `MUST_BE_CONSIDERED`
- `COMPLIANCE_EVIDENCE`
- `ESTABLISHES_STATUS`
- `BINDING_DECISION`
- `UNCERTAIN`
- `OTHER_JUSTIFIED`

Do not assume bindingness from procedural obligation.

---

# 16. ACCOUNTABILITY AND META-INTERMEDIATION

For every intermediary, ask:

- accountable to whom?
- accountable for what?
- through what procedure?
- what happens if it fails?
- is there supervision?
- is there accreditation?
- is there peer review?
- is there independent review?
- is another intermediary regulating this intermediary?

Where supported, reconstruct chains such as:

`R → I2 → I1 → T`

or:

`R → I1 → T`
with
`I2 → supervises/verifies I1`

---

# 17. RESEARCH QUESTION MAP

The R3 dataset must not be designed only around coding convenience.

For every major variable, ask:

> What question will this variable help answer?

Create:

`RESEARCH_QUESTION_MAP.csv`

Fields:

- `research_question_id`
- `research_question`
- `theoretical_or_empirical`
- `variables_required`
- `unit_of_analysis`
- `comparison_logic`
- `possible_hypothesis`
- `data_requirements`
- `status`
- `notes`

Initial research questions may include:

1. Which regulatory functions are delegated to intermediaries?
2. Which types of intermediaries are associated with which mechanisms?
3. Which mechanisms co-occur?
4. Which mechanisms form recurrent chains?
5. How does institutionalization relate to legal effect of intermediary output?
6. Who regulates the intermediaries?
7. When does triadic intermediation become chained or nested?
8. Do regulator-facing and target-facing intermediaries use different mechanisms?
9. How does independence relate to monitoring and verification?
10. Do different EU climate laws display different combinations of articulation, treatment of information and regulatory reliability?
11. How does declared regulatory orientation compare with observed intermediation architecture?
12. Which architecture patterns recur across the five cases?

---

# 18. EXECUTION PHASES

---

# PHASE 0 — CLEAN-ROOM ENVIRONMENT AUDIT

Objective:

prove that R3 starts independently.

Tasks:

- create `R3_CLEANROOM/`;
- inventory only the new R3 directory;
- record forbidden prior roots as firewall locations without inspecting them;
- copy the learning register into `00_governance/`;
- copy this prompt verbatim into `00_governance/`;
- create a researcher decision log;
- verify that no prior empirical files have been imported.

Outputs:

- `R3_PHASE_0_ENVIRONMENT_AUDIT.md`
- `R3_FIREWALL_REGISTER.csv`
- `R3_RESEARCHER_DECISION_LOG.md`
- `R3_PROMPT_VERBATIM.md`
- `R3_LEARNING_REGISTER_VERBATIM.md`

STOP.

End:

`R3_PHASE_0_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION`

---

# PHASE 1 — FRESH SOURCE ACQUISITION

Objective:

acquire the five official legal texts independently.

For each CELEX:

- retrieve fresh official source;
- resolve official title;
- identify type of legal act;
- identify Official Journal reference;
- record language;
- record source URL;
- record retrieval timestamp;
- record whether original or consolidated;
- calculate SHA-256;
- store raw source unchanged.

Do not analyze substantive content yet.

Outputs:

- `R3_SOURCE_REGISTER.csv`
- one `SOURCE_MANIFEST.yaml` per case;
- raw source folders;
- `R3_PHASE_1_SOURCE_AUDIT.md`

Audit:

- source authority;
- completeness;
- version consistency;
- duplicate or conflicting versions;
- acquisition errors.

STOP.

`R3_PHASE_1_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION`

---

# PHASE 2 — CORPUS CONSTRUCTION

Objective:

construct a lightweight, traceable corpus for each law.

For each case create:

- full normalized text;
- recitals;
- operative provisions;
- article-numbered version;
- structural index.

Preserve links to raw official source.

Do not code actors, R/I/T or mechanisms.

Outputs:

- `act_full.md`
- `recitals.md`
- `operative.md`
- `article_index.csv`
- `CORPUS_MANIFEST.yaml`
- `R3_PHASE_2_CORPUS_AUDIT.md`

Quality checks:

- article continuity;
- recital continuity;
- annex presence/absence;
- lost text;
- duplicated text;
- broken numbering;
- hash linkage.

STOP.

`R3_PHASE_2_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION`

---

# PHASE 3 — WHOLE-INSTRUMENT PROFILES

Objective:

understand each law as a whole before relational coding.

For each law independently identify:

- declared regulatory objective;
- regulatory object;
- legal scope;
- principal target classes;
- principal regulatory authorities;
- institutional architecture;
- main obligations;
- major governance components;
- declared orientation;
- how major sections relate functionally.

Do NOT identify intermediaries yet.

Do NOT code mechanisms yet.

Do NOT classify the law into the 3–4–2 families.

Outputs:

- `INSTRUMENT_PROFILE.csv`
- one `INSTRUMENT_MEMO_<CELEX>.md` per case;
- `R3_PHASE_3_INSTRUMENT_AUDIT.md`

Distinguish:

- `EXPLICIT_TEXT`
- `CROSS_PROVISION_RECONSTRUCTION`
- `ANALYTICAL_INFERENCE`

STOP.

`R3_PHASE_3_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION`

---

# PHASE 4 — ACTOR REGISTER

Objective:

identify all legally relevant actors before deciding who is R, I or T.

For each law identify:

- actor name;
- actor class;
- institutional type;
- level of governance;
- formal tasks;
- legal provisions;
- possible relational roles.

Do not assign permanent R/I/T identities.

Outputs:

- `ACTOR_REGISTER.csv`
- `ACTOR_PROVISION_MAP.csv`
- `R3_PHASE_4_ACTOR_AUDIT.md`

STOP.

`R3_PHASE_4_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION`

---

# PHASE 5 — REGULATORY RELATION RECONSTRUCTION

Objective:

identify regulatory relations without yet forcing intermediation.

For each candidate relation code:

- R candidate;
- T candidate;
- possible I candidate;
- regulatory object;
- action;
- relation purpose;
- relevant provisions;
- evidence level.

Include direct R–T relations.

Outputs:

- `RELATION_CANDIDATES.csv`
- `CROSS_PROVISION_RELATION_MAP.csv`
- `R3_PHASE_5_RELATION_AUDIT.md`

Audit:

- uncertain R;
- uncertain T;
- uncertain third actor;
- cross-provision chains;
- role-switch candidates.

STOP.

`R3_PHASE_5_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION`

---

# PHASE 6 — INTERMEDIATION ADJUDICATION

Objective:

apply the three-condition test.

For every candidate relation classify:

- `SUPPORTED_INTERMEDIATION`
- `DIRECT_R_T`
- `LEGAL_RELATION_NON_RIT`
- `UNCERTAIN`
- `NOT_SUPPORTED`

Create negative boundary cases.

Special scrutiny:

- advisory bodies;
- expert bodies;
- consultation bodies;
- committees;
- national authorities;
- accreditation bodies;
- auditors;
- certifiers;
- database operators;
- scientific bodies.

Outputs:

- `RELATIONS_ADJUDICATED.csv`
- `NEGATIVE_BOUNDARY_CASES.csv`
- `UNCERTAIN_RELATIONS.csv`
- `R3_PHASE_6_INTERMEDIATION_AUDIT.md`

STOP.

`R3_PHASE_6_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION`

---

# PHASE 7 — LAW × INTERMEDIARY REGISTER

Objective:

implement David's requested comparative unit.

For every confirmed or plausible intermediary:

one row per `LAW × INTERMEDIARY`.

Populate:

- institutionalization;
- voluntarism;
- separation from target;
- independence;
- capacities;
- centrality;
- orientation;
- legal effect of output;
- accountability;
- sanctions;
- meta-intermediation.

Do not yet code mechanisms beyond references needed to connect later tables.

Outputs:

- `LAW_INTERMEDIARY_REGISTER.csv`
- `INTERMEDIARY_INSTITUTIONAL_PROFILE.csv`
- `R3_PHASE_7_LAW_INTERMEDIARY_AUDIT.md`

STOP.

`R3_PHASE_7_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION`

---

# PHASE 8 — MECHANISM CODING

Objective:

identify elementary mechanisms independently of actor labels.

For each mechanism event identify:

- relation;
- intermediary;
- input;
- mediated object;
- transformation;
- output;
- recipient;
- mechanism;
- family;
- evidence;
- confidence.

Allow multiple mechanism events per relation.

Do not force more than one mechanism if only one is supported.

Do not use `audit`, `certification`, `accreditation` or `testing` as substitutes for elementary mechanism coding.

Outputs:

- `MECHANISM_EVENTS.csv`
- `MECHANISM_TRACE.csv`
- `MECHANISM_UNCERTAINTY_LOG.csv`
- `R3_PHASE_8_MECHANISM_AUDIT.md`

STOP.

`R3_PHASE_8_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION`

---

# PHASE 9 — MECHANISM CHAINS AND META-INTERMEDIATION

Objective:

identify supported sequences and nested relations.

Possible examples:

- `TRANSMISSION → EVALUATION`
- `AGGREGATION → EVALUATION → TRANSLATION`
- `MONITORING → VERIFICATION`
- `MONITORING → TRANSMISSION → EVALUATION`
- `VERIFICATION → CLASSIFICATION`
- `I2 verifies I1 → I1 verifies T`

Code only evidence-supported chains.

Outputs:

- `MECHANISM_CHAINS.csv`
- `META_INTERMEDIATION_MAP.csv`
- `CHAIN_DIAGRAM_SPEC.md`
- `R3_PHASE_9_CHAIN_AUDIT.md`

STOP.

`R3_PHASE_9_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION`

---

# PHASE 10 — RESEARCH QUESTION CALIBRATION

Objective:

respond directly to David's request.

Review the dataset architecture and ask:

> What theoretically interesting questions can these variables actually answer?

Create or revise the research question map.

For every research question identify:

- unit of analysis;
- required variables;
- whether current data can answer it;
- whether five cases are sufficient for exploratory comparison;
- whether a larger population would be required;
- what theoretical contribution might emerge.

Outputs:

- `RESEARCH_QUESTION_MAP.csv`
- `R3_THEORETICAL_QUESTION_MEMO.md`
- `R3_PHASE_10_RESEARCH_QUESTION_AUDIT.md`

STOP.

`R3_PHASE_10_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION`

---

# PHASE 11 — CROSS-CASE ARCHITECTURE

Objective:

compare the five laws.

Create descriptive comparisons for:

- number of intermediaries;
- intermediary types;
- mechanisms;
- mechanism families;
- chains;
- output legal effects;
- accountability structures;
- meta-intermediation;
- orientations;
- cross-provision complexity.

Create the derived 3–4–2 profile.

Fields:

- `instrument_id`
- `n_articulation_events`
- `n_information_treatment_events`
- `n_regulatory_reliability_events`
- `share_articulation`
- `share_information_treatment`
- `share_regulatory_reliability`
- `mechanism_diversity_n`
- `family_diversity_n`
- `dominant_observed_family`
- `declared_orientation`
- `declared_vs_observed_note`

Do not claim causal relationships.

Do not claim maturity.

Do not perform factor analysis.

Outputs:

- `CROSS_CASE_ARCHITECTURE.csv`
- `MECHANISM_FAMILY_PROFILE.csv`
- `CROSS_CASE_COMPARISON_MEMO.md`
- `R3_PHASE_11_CROSS_CASE_AUDIT.md`

STOP.

`R3_PHASE_11_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION`

---

# PHASE 12 — FINAL DATASET ASSEMBLY

Create:

`R3_REGULATORY_INTERMEDIATION_ARCHITECTURE.xlsx`

Required sheets:

1. `README`
2. `INSTRUMENT_PROFILE`
3. `ACTOR_REGISTER`
4. `LAW_INTERMEDIARY`
5. `RELATIONS`
6. `MECHANISM_EVENTS`
7. `MECHANISM_CHAINS`
8. `META_INTERMEDIATION`
9. `LEGAL_EVIDENCE`
10. `NEGATIVE_BOUNDARY_CASES`
11. `UNCERTAIN_CASES`
12. `RESEARCH_QUESTION_MAP`
13. `MECHANISM_FAMILY_PROFILE`
14. `DECISION_LOG`
15. `DATA_DICTIONARY`

Also create:

- `R3_METHOD_REPORT.md`
- `R3_MECHANISM_CODEBOOK.md`
- `R3_CHANGELOG.md`
- `R3_FINAL_AUDIT.md`

Important:

Do not compare against old datasets yet.

R3 must first be frozen independently.

STOP.

`R3_PHASE_12_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION`

---

# PHASE 13 — OPTIONAL HISTORICAL COMPARISON

Execute only if explicitly authorized.

Only after R3 is frozen may the agent compare R3 with prior rounds.

If authorized, compare:

- units of analysis;
- intermediary counts;
- relations;
- mechanism coding;
- uncertainty;
- explanatory capacity;
- auditability;
- theoretical question coverage.

Never silently modify R3 based on previous outputs.

Any later revision becomes a new version.

STOP.

---

# 19. AUDIT TEMPLATE FOR EVERY PHASE

Each phase audit must contain:

## A. Work completed

## B. Inputs used

## C. Outputs created

## D. Quantitative summary

## E. Methodological decisions

## F. Uncertainties

## G. Deviations from prompt

## H. Quality-control checks

## I. Researcher decisions required

## J. Status

End with:

`READY_FOR_RESEARCHER_REVIEW`

Then STOP.

---

# 20. QUALITY CONTROL RULES

Throughout R3:

- never overwrite previous phase outputs;
- version changed files explicitly;
- preserve hashes;
- preserve source provenance;
- separate evidence from interpretation;
- separate legal action from mechanism;
- separate regulatory target from regulatory object;
- separate institutional technology from elementary mechanism;
- separate output bindingness from intermediation;
- preserve direct R–T relations;
- preserve negative cases;
- preserve uncertainty;
- do not infer intermediary status from actor type;
- do not infer mechanism from actor label;
- do not force the 3–4–2 families;
- do not use prior coding as calibration;
- document every cross-provision reconstruction.

---

# 21. FINAL R3 SUCCESS TEST

The final R3 dataset must allow the researcher to answer, for each law and across the five cases:

1. What does the law seek to regulate?
2. Who regulates?
3. Who is regulated?
4. Which third actors intervene?
5. Which qualify as intermediaries?
6. What is the `LAW × INTERMEDIARY` unit?
7. What relation does each intermediary enter?
8. What does it mediate?
9. What mechanism does it use?
10. What is the input?
11. What transformation occurs?
12. What output is produced?
13. Who receives the output?
14. What is the legal effect of the output?
15. Is participation mandatory or voluntary?
16. How independent is the intermediary from the target?
17. What capacity does the intermediary add?
18. Who holds the intermediary accountable?
19. Is there meta-intermediation?
20. Do mechanisms form chains?
21. Which mechanism families appear?
22. What regulatory intermediation architecture emerges?
23. Which patterns recur across laws?
24. Which theoretical questions can the dataset answer?
25. Which questions require a larger population?

---

# 22. FIRST COMMAND

Begin only with:

# PHASE 0 — CLEAN-ROOM ENVIRONMENT AUDIT

Do not acquire legal sources yet.

Do not analyze any law.

Do not open prior empirical materials.

At completion, produce the Phase 0 audit and STOP.

End exactly with:

`R3_PHASE_0_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION`
