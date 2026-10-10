# Claude Track A - Self-QA report (V8 only)

Scope: self-check of the Track A outputs against `COMPARISON_EVALUATION_CRITERIA.md`. This report makes no comparison with any other track or system and claims no superiority of any method.

## 1. Count checks (computed from the output files)

| Check | Result |
|---|---|
| Register SHA-256 equals the expected `417A35A3...E77F` | PASS (verified before any coding) |
| P03 and P04 primary HTML hashes equal the expected values | PASS (`01D5BDB1...6888`; `62AFB4DD...1449`) |
| Statements coded | 20 of 20 (P03 = 6, P04 = 14); statement IDs equal the register's 20 IDs; provision anchors equal the register's anchors |
| P04 Article 22(7) | Not coded (excluded context) |
| Relationships recorded | 34 (P03 = 11; P04 = 23) |
| Relationship decisions | ACCEPTED 19 (P03 6; P04 13); DEFERRED 7 (P03 2; P04 5); REJECTED 8 (P03 3; P04 5) |
| Every relationship has at least one supporting statement | PASS (34 of 34; all cited statement IDs exist in the register) |
| Statement rows and relationship rows cross-reference each other | PASS (every statement lists the relationships it supports and every relationship lists only existing supporting statements; the cross-listing was checked by script and three omissions were corrected) |
| Controlled vocabularies | PASS: `coding_status` in {direct_text, cross_provision_inference, human_review_needed, deferred}; `claim_level` in {statement, relation}; `decision` in {ACCEPTED, REJECTED, DEFERRED} |
| Claims above relation level | 6 configuration-level claims (CL-P03-01 to -03, CL-P04-01 to -03); 0 architecture; 0 regime |
| Every claim traceable to source and hash | PASS: claim -> configuration -> relationships -> statements -> provision anchor -> FE-001 or FE-003 and hash, stated for all 7 claims in the architectural inferences file |
| Uncertainty register | 30 entries; every uncertainty ID cited in the coding, configuration or inference files exists; 29 of 30 are cited by statement rows (U-29 is cited by configurations and relationships only) |
| Human review flags | 8 relationships flagged TRUE (7 deferred, plus R-P04-15 accepted with an unresolved authority reading) |

## 2. Assessment against the pre-registered criteria

### 2.1 Inferential defensibility (does the claim stop where the evidence stops?)

- Highest level reached is candidate configuration for both cases. Section 3 of the architectural inferences file tests the architecture-level requirements of V8 rule 4 and records which are unmet.
- Fourteen declined claims are listed with the missing evidence.
- Known judgment calls that could be challenged: (a) R-P03-02 and R-P03-03 (designation) are accepted at relation level on a relative-clause antecedent (U-01); (b) R-P04-03 (consultation) is accepted as a thin participation relation (U-15); (c) R-P04-15 (consent) is accepted with the Registry supplied from the adjacent statement and no authority consequence coded (U-23, U-24); (d) merging of statement pairs into single relationships (U-03, U-20). Each is recorded as an accepted ambiguity or flagged for human review; no higher-level claim depends on them.
- Possible under-coding: relationships in the deferred class (R-P03-11, R-P04-04, R-P04-05, R-P04-09, R-P04-14, R-P04-18, R-P03-07) could be accepted by a reviewer who allows wider text of the same instruments; this was avoided on scope grounds.

### 2.2 Legal traceability

- Chain claim -> configuration -> relationship -> statement -> provision -> source/hash is written out for each claim.
- Each relationship row names its supporting statements and the cross-provisions used (Annex III points 3.1, 3.2 and 6 for R-P03-04 and C-P03-03; Article 23(1) second sentence for the list reference; Article 9 for scope reading only).
- Cross-provisions and wider text consulted are logged in the execution log with line locations in the official text files.

### 2.3 Unsupported-relationship attribution

- Eight candidate relationships were rejected because a unilateral duty, a receipt or a shared term would otherwise have become an edge: R-P03-08, R-P03-09, R-P03-10, R-P04-12, R-P04-16, R-P04-19, R-P04-22, R-P04-23.
- Seven were deferred because a party, an addressee, an object or a content was missing from the frozen statements.
- Reporting was never coded as accountability: all accepted information relations record 'information component only'; accountability relations R-P03-10 and R-P04-12 were rejected.
- Normative assignments whose duty-bearer is unexpressed (CS-P03-004, CS-P04-012) were not turned into relations.
- Discretion was coded only from explicit indicators (permissive 'may'; open-textured 'reasonable intervals'; stated choice of provider from a list; stated manner criteria) and never from a job title. Implementation, practice and effectiveness were not inferred.

### 2.4 Cross-level errors (property bearer and boundary)

- Properties are attached to the relationship or configuration that bears them (Section 6 of the inferences file). No actor-level or instrument-level property was projected upward.
- Specific guards applied: legal atomistic (single relations not promoted to architectures), frequency (counts of Registry and notified-body relations not used as significance), container (no whole-Directive or whole-Regulation claim), functional and implementation (formal text only), ecological (no cross-case claim).
- Residual risk: the configuration groupings are analyst constructs (alternatives are given in the configurations file); a reviewer may split or merge them without changing any member relationship.

### 2.5 Structural clarification

- Track A as defined here uses V8 rules only. No positional, part-whole or boundary/sensitivity deliverables were produced, by design. Alternatives are noted inside the configurations file as V8 rule 4 requires.
- Structural information recorded by V8 means: sequence within configurations is stated only where the text states it (for example 'before the agreement is concluded', 'after consulting', 'at the end of the phased registration').

### 2.6 Uncertainty and stopping compliance

- Thirty uncertainties are recorded with a treatment and a status: 12 deferred, 12 accepted ambiguity, 3 resolved by text, 3 human review needed.
- Stopping-rule decisions are explicit (SR-P03, SR-P04, SR-P04-ADR, SR-P03-004 / SR-P04-012); no regime-boundary decision was made.
- No `deferred` or `human_review_needed` item was promoted.

### 2.7 Incremental value

Not assessed. The criterion concerns a comparison between tracks, and no comparison was made or is made here.

### 2.8 Effort

- Elapsed time and decision counts are in the execution log (approximately 110 recorded decisions).
- Added fields beyond the register: coding of function, mechanism, instrument and three attribute notes per statement; typed relationships with direction, modality, condition and attributes; configuration and inference files; uncertainty register with 30 entries.

## 3. Known limitations

1. The register's excerpts for CS-P03-001 and CS-P03-002 end before later sentences in Article 10(1) and 10(2); these were not used (U-02).
2. The audit object in Article 12(5) lies outside the frozen statements; R-P04-05 is therefore deferred (U-13). A registered amendment would change that result.
3. Wider text of the same two instruments was read for cross-reference resolution; the reading extended beyond the strict minimum in some places (see the log). Content not needed for resolving a cross-reference or wording ambiguity was not coded, but the analyst had sight of it, and that exposure is stated rather than hidden.
4. Single analyst, single pass; no inter-coder comparison, so reliability of Level II attribute notes and configuration groupings is not tested.
5. Level II notes are qualitative and text-bound; no ordinal grades (low/medium/high) were assigned because the statements do not support them.
