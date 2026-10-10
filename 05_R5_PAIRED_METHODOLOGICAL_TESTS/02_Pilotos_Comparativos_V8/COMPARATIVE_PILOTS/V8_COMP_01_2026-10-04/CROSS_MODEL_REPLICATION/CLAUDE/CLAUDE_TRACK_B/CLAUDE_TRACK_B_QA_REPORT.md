# CLAUDE Track B - Self-QA report

Scope: self-check of this track's outputs against COMPARISON_EVALUATION_CRITERIA.md. This report does not compare with any other track or system and does not assess whether the eight-operation protocol is better or worse than any alternative. Count checks were run by script on the written files (header match, ID cross-references, supporting-statement presence).

## 1. Count checks

| Check | Result |
|---|---|
| Register hash 417A35A3...F77F verified before work | PASS (hash match) |
| Source hashes FE-001 HTML (01D5BDB1...6888) and FE-003 HTML (62AFB4DD...1449) | PASS; the derived .txt hashes (FEB9A7C2...15D5; A088F46B...04B5) also match the manifests |
| Statements coded | 20 of 20 (P03 = 6, P04 = 14); statement IDs identical to the register's, in order |
| Frozen excerpts found in the official text | 20 of 20 found in the official HTML and in the reading text; CS-P03-004, -005, -006 occur twice (Annex III and Annex IV) |
| CODING.csv header | matches the 22 specified fields |
| RELATIONSHIPS.csv header and rows | matches the 18 specified fields; 32 candidate relationships (P03 = 7, P04 = 25): 19 ACCEPTED, 5 DEFERRED, 8 REJECTED |
| Every relationship has at least one supporting statement | PASS (0 relationships without a valid statement ID). For REJECTED rows the IDs are the statements that prompted the candidate, labelled "(prompted by)" in some rows |
| Every relationship referenced by a statement row exists, and every relationship is referenced by at least one statement row | PASS (no dangling or orphan relationship IDs) |
| Every uncertainty ID referenced by a statement row exists, and every uncertainty is referenced | PASS (34 uncertainties; 0 orphan) |
| Statement-level decisions | 17 ACCEPTED, 2 DEFERRED (CS-P03-004, CS-P04-012), 1 ASSIGNMENT_ONLY (CS-P03-003), 0 REJECTED at statement level |
| Operation register | 8 rows, O1 to O8 |
| Claims traceable | 10 claims (CL-P03-01, CL-P03-02, CL-P04-01 to CL-P04-08); each has a chain claim, configuration or relation, relationships and elements, statements, provision, source/hash. All IDs used in the Markdown deliverables resolve to existing statements, relationships and uncertainties |
| Property claims and refused lifts in O6 | 46 property claims with bearer and boundary; 14 refused lifts |
| Sensitivity tests in O8 | 12 (S-01 to S-12) |
| Human review flagged in RELATIONSHIPS | 9 relations (R-P03-04, R-P03-05, R-P04-01, -05, -09, -13, -14, -17, -22) |

## 2. Self-check against the pre-registered criteria

### Inferential defensibility (does each claim stop at the level the evidence supports?)

- Stopping rule applied at every level: no architecture-level claim and no regime claim. Four candidate architecture-level claims were tested and declined with the V8 rule 4 requirements itemised (CLAUDE_TRACK_B_ARCHITECTURAL_INFERENCES.md section 4).
- Warrant, counter-evidence, alternatives and boundary limitations are stated for each of the 10 claims.
- Residual risk: the five configurations are thin. A reviewer could classify some of them (for example C-P04-C, which is instrument-defined, or C-P04-D) as clusters of relations rather than configurations. The track states the membership criteria used (CLAUDE_TRACK_B_CONFIGURATIONS.md section 1) so the decision is reviewable.
- Residual risk: C-P04-B depends on identifying "independent audit" with "the auditor" (S-05). C-P04-D depends on one condition-embedded relation (S-06). Both are flagged.

### Legal traceability (claim to provision)

- Each claim has the chain claim, configuration, relationships and elements, statements, provision anchor, source and hash (Architectural inferences, section 3). Each statement row carries the register's provision anchor.
- Wider text was used only for wording and cross-references, each use recorded in the log and in the relevant relationship's cross_provisions_used and uncertainty entries. Where wider text was used for a relation (R-P04-05, R-P04-10, R-P04-14 counterpart) the coding_status is cross_provision_inference and human review is flagged where applicable.

### Unsupported-relationship attribution (did a unilateral duty become an edge?)

- Eight candidate relations were rejected and five deferred, each with a reason; one statement was retained as an assignment (CS-P03-003). Two statements with unexpressed actors (CS-P03-004, CS-P04-012) were not given an actor.
- Residual risk of over-attribution: three accepted relations rest on an actor mention inside a condition or object clause (R-P04-03 consultation, R-P04-13 beneficiary designation, R-P04-16 complainant choice). They are coded thin, with authority "not coded", and are tested in S-06. A stricter reviewer could defer them.
- Residual risk of under-attribution: R-P03-05 (designation presupposed) and R-P04-22 (delegation) are deferred; a reviewer could accept the first (S-04).
- Reporting and notification relations are coded as information; none is coded as accountability.

### Cross-level errors (did an actor or relation property become a configuration, architecture or regime property?)

- Bearer and boundary declared for 46 property claims; 14 lifts refused (O6). Frequency, shared actor and connectivity were not used as support for any claim (RL-02, X-P04-1, S-10).
- Residual risk: the pattern labels attached to configurations ("third-party assurance", "audit with reporting", "escrow arrangement") are descriptive but could be read as architecture-level categories; each is paired with an explicit list of what is not established.

### Structural clarification (does the track clarify order, gateway, condition, position or part-whole by a specific difference rather than an extra label?)

- Specific differences recorded: stated precedence versus entailed order (agreement to deposit, report after audit); consultation versus consent; a permissive power on which a later choice depends (CS-P04-014 and CS-P04-012); a consent precondition limited to the conclusion of one agreement. No gateway, substitutability or conditional-authority claim was supported at configuration level.
- Residual risk: positional vocabulary can add labels without information when the answer is "not stated"; the O5 document marks every NOT SUPPORTED cell.

### Uncertainty and stopping compliance

- 34 uncertainties recorded (17 accepted_ambiguity, 7 deferred, 6 human_review_needed, 4 resolved_by_text), each with a treatment. Deferred and human-review items are linked to the relations they affect.
- No deferred item was promoted. The "what would be needed" lists in section 6 of the Architectural inferences name evidence outside the 20 statements and were not evaluated.

### Effort

- Wall-clock start and end are in the execution log. No per-operation timing was recorded; the qualitative estimates are in the operation register. Added fields and decisions beyond V8-only coding, as observed: five O4-O8 documents; 32 candidate relationships with typed attributes; 5 configurations plus 6 declined groupings; positional tables for 6 units; 46 property-claim entries plus 14 refused lifts; 12 sensitivity tests. O3 carried the largest share of the work; O7 added length without changing any decision.

## 3. Known weaknesses and errors to check

1. Single analyst, single pass: no second coder and no human adjudication; reliability is unknown.
2. Wider-text exposure: while resolving cross-references, adjacent provisions were read (Art 10(1)-(6); Annex III in full; Annex IV 3.3 to 4.3; Art 12(1)-(6); Art 13 to Art 18 in part; Art 22 and Art 23 in full). They were not used as evidence except for the recorded wording or cross-reference resolutions, but their reading may have shaped judgement, for example on what was left unstated (consequence of the agent's finding, parties to the ADR, content of the beneficiary position). The log lists every consultation.
3. Several frozen excerpts are truncated sentences (for example Art 10(2), Art 22(6)); the track did not evaluate the remainder.
4. The Annex III anchor is a register choice: three statements appear verbatim in Annex IV. Claims are confined to the Annex III anchor.
5. The sensitivity tests were chosen by the analyst from the recorded ambiguities; they are not an independent stress test.
6. Thin relations and configurations are judgment calls. The decisions are explicit and reversible through the S-02, S-04, S-06 and S-11 results.
7. Statement-level coding_status uses five values; the rule used (direct_text when every coded element is in the sentence; cross_provision_inference when a coded element is resolved through another provision or statement; deferred when the actor is unexpressed; human_review_needed when a provisional reading is adopted) is the analyst's operationalisation and is not spelled out in the V8 codebook.
8. Function labels such as "designation of a verifier (evidence-supported equivalent)" extend the V8 function list under its "evidence-supported equivalent" clause and are marked uncertain_boundary where the text does not separate function from mechanism.

## 4. Statement of non-comparison

No other track, model or historical classification was consulted (see the log). This report makes no claim about relative value, improvement or equivalence.
