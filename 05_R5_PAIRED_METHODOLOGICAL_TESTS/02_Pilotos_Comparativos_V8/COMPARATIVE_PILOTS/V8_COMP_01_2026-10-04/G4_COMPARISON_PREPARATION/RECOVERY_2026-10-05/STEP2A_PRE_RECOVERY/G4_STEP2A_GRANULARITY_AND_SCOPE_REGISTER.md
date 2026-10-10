# G4 Step 2A — granularity and evidence-scope register

**Date:** 2026-10-04 · **Status:** candidate correspondence only (no agreement, improvement, regression or superiority assessment; the original five-category outcome scheme is preserved and **not** applied).

This register documents (A) how the cells segment and level the same frozen statements, so that correspondence is not forced across granularities, and (B) how the Step 0/Step 1 evidence-scope findings travel through the correspondence groups. Companion files: `G4_STEP2A_CORRESPONDENCE_GROUPS.csv`, `G4_STEP2A_CLAIM_MAPPING.csv`, `G4_STEP2A_UNMATCHED_CLAIMS.csv`.

## 1. Headline counts (descriptive only)

| Item | Count |
|---|---|
| Correspondence groups | 26 (relation 16 · configuration 6 · position 2 · architecture-level decision 2) |
| Correspondence types | same proposition 16 · same proposition, different segmentation 2 · overlapping proposition 6 · same subject, same kind of determination 1 · same subject, different kind of determination 1 |
| Original units grouped / unmatched | 101 / 11 (of 112) |
| STEP0_DERIVED units attached to groups | 2 (not counted as original claims) |
| Group memberships | 102 (one original unit, CLAUDE_A:CL-P04-04, belongs to two groups) |

Per cell (originals):

| Cell | Original units | Matched (in ≥1 group) | Unmatched |
|---|---|---|---|
| CODEX_A | 24 | 24 | 0 |
| CODEX_B | 29 | 27 | 2 (TB-O5-P03-01, TB-O5-P04-02) |
| CLAUDE_A | 28 | 24 | 4 (R-P03-02, R-P03-03, R-P03-04, CL-P03-03) |
| CLAUDE_B | 31 | 26 | 5 (R-P04-05, R-P04-13, R-P04-16, CL-P04-07, CL-P04-08) |

These counts describe the register only. Unmatched does **not** mean omission, failure or improvement, and matched counts are not agreement rates.

## 2. Granularity differences

### 2.1 Segmentation of the same statements (many-to-one / one-to-many)

| Case | Statements | Segmentation by cell | Groups |
|---|---|---|---|
| P03 | CS-P03-001, CS-P03-002 (notification and information duties of Member States) | Codex A, Codex B: two relations (one per statement). Claude A, Claude B: one joined relation. Claude B additionally restates it as a relation-level claim | CG-001 (many-to-one) |
| P04 | CS-P04-007, CS-P04-008 (negative and positive notification by the validation agent) | Codex A, Claude A, Claude B: one joined relation. Codex B: two relations (negative; positive) | CG-011 (many-to-one) |
| P04 | CS-P04-013, CS-P04-014 (ADR information; ADR-provider selection) | Codex A, Codex B, Claude A (relations), Claude B: one relation per statement. Claude A also has a relation-level claim CL-P04-04 spanning both | CG-015, CG-016 (one-to-many for CL-P04-04) |
| P03 | CS-P03-001 (designation of bodies inside the notification statement) | Claude A: separate designation relations (R-P03-02, R-P03-03; unmatched). Codex A, Codex B, Claude B: designation kept as object or condition (Codex B records a rejected and Claude B a deferred candidate outside the register) | CG-017 (overlap), unmatched units |
| P04 | CS-P04-009 (beneficiary designation inside the agreement statement) | Codex A, Codex B, Claude A: condition of the agreement relation. Claude B: also a separate relation (R-P04-13; unmatched) | CG-012, CG-021 |
| P04 | CS-P04-001 (audit-report requirement) | Codex A, Codex B: assignment inside the audit configuration, no accepted relation. Claude A, Claude B: auditor/audit-to-Commission relation | CG-006 (two cells), CG-019 |

### 2.2 Differences of level (not forced into one group)

- Claude B CL-P03-01 states a **relation-level** claim for the P03 notification statements; Claude B records **no configuration** for them. It is grouped with the relation group CG-001 (same level), not with the configuration group CG-017.
- Claude A CL-P04-04 states **two relations and no configuration** for the ADR statements. It is attached to the two relation groups CG-015 and CG-016 (one claim, two groups, counted once), not to the configuration group CG-022; the cross-level link is recorded as related-not-grouped.
- Architecture-level decisions are grouped only with architecture-level decisions (CG-025, CG-026). Positive architecture claims (Codex A, Codex B for P04) and stopping decisions (all other architecture-level units) share a subject but are different kinds of determination; the group type says so and no equivalence or contradiction is asserted.
- Positional claims exist only in Codex B and Claude B; two groups (CG-023, CG-024) and four unmatched positional units.
- Configuration groups relate to relation groups and architecture groups to configuration groups through `related_group_ids_cross_level_not_grouped`; these are links, not memberships.

### 2.3 Differences of breadth inside configuration groups

| Group | Difference of membership or breadth |
|---|---|
| CG-017 (configuration, P03) | Codex A and Codex B configurations contain the two information relations only (designation is an object or condition of the statements). Claude A's configuration also contains two designation relations (R-P03-02, R-P03-03; unmatched). Claude B records no configuration for these statements; it states them only as a relation-level claim (grouped in CG-001). |
| CG-018 (configuration, P03) | Codex A and Codex B: audit and audit-report relations, with the assessment of CS-P03-003 retained as an assignment (no relation). Claude A: three relations, including an assessment relation whose counterparty comes from non-frozen text (R-P03-04, SC-C). Claude B: audit and report relations, with CS-P03-003 cited for function and object only. A STEP0_DERIVED core (frozen-text restriction of Claude A's claim) is attached. |
| CG-019 (configuration, P04) | Codex A and Codex B: appointment and consultation only, with the audit-report requirement retained as an assignment. Claude A: appointment, consultation and findings-report relations, with no claim about what is audited. Claude B: also includes an auditor-to-Registry verification relation whose object comes from text outside the frozen statements (SC-C) and a warrant that presupposes an auditee. A STEP0_DERIVED core (frozen-text restriction of Claude B's claim) is attached. |
| CG-020 (configuration, P04) | All four cover CS-P04-003 to CS-P04-008 with corresponding relations (selection, requirement, evidence submission, examination, notification). Pattern labels differ: 'delegated' (both Codex cells); 'partial third-party assurance configuration' (Claude A); 'procedural verification stage' with selection and requirement as a weaker attachment to a core (Claude B). |
| CG-021 (configuration, P04) | All four combine the escrow agreement, the Commission's prior consent and the daily submission (CS-P04-009 to CS-P04-011). Claude B also includes the beneficiary relation (CLAUDE_B R-P04-13, unmatched). Both Codex cells describe the function with a continuity label (wording not found in the frozen statements; UPQ-01); both Claude cells state that the purpose is not stated in the statements. |
| CG-022 (configuration, P04) | Codex A and Codex B: Registry selection and provider information relations, with CS-P04-012 retained without a relation. Claude B: additionally the complainant's choice from the list and the identification of the list with the Registry-selected providers (SC-B, borderline). Claude A's CL-P04-04 states two relations and no configuration (mapped to CG-015 and CG-016; related but not grouped here). |
| CG-023 (position, P04) | Codex B calls the Commission's consent a relation-specific 'gate'; Claude B states it as a precondition on the conclusion of the escrow agreement. Both restrict the claim to the escrow agreement. Only Codex B and Claude B record accepted positional claims. |
| CG-024 (position, P04) | Codex B states that the validation agent occupies a 'necessary' procedural assessment stage in the evidence-to-Registry notification sequence; Claude B states only the order submission, then examination, then notification. The first asserts a stage property; the second an order. |
| CG-025 (architecture-level decision, P03) | All four decide that no architecture-level claim is made for P03 and that the highest level stated is configuration (Claude B also states a relation-level item). The components named differ: two configurations (Codex A and Codex B); three candidate configurations including the designation-to-verification link (Claude A, two of them SC-C); one thin configuration plus the notification relation (Claude B). |
| CG-026 (architecture-level decision, P04) | Codex A and Codex B make a positive architecture-level claim for the P04 microcase (a Registry-centered/coordinated bounded architecture). Claude A and Claude B decide that no architecture-level claim is warranted and stop at configuration level. The subject and level are the same; the kind of determination differs (claim versus stopping decision). Component configurations differ in number and treatment (see CG-019 to CG-022). |

### 2.4 Correspondence types used (candidate only)

| Type | Meaning at Step 2A |
|---|---|
| CANDIDATE_SAME_PROPOSITION | Same case, parties, act, modality, condition and frozen statement(s); vocabulary may differ. Not a determination of substantive equivalence. |
| CANDIDATE_SAME_PROPOSITION_DIFFERENT_SEGMENTATION | As above, but the cells split or join the statements differently. |
| CANDIDATE_OVERLAPPING_PROPOSITION | Same case and statements and same organising idea; membership or asserted property differs. |
| CANDIDATE_SAME_SUBJECT_SAME_KIND_OF_DETERMINATION | Same architecture-level subject and the same kind of determination; supporting components differ. |
| CANDIDATE_SAME_SUBJECT_DIFFERENT_KIND_OF_DETERMINATION | Same architecture-level subject; the kind of determination differs. No finding on consistency. |

## 3. Evidence-scope register

The Step 0 classes (SC-A…SC-D), the five material dependencies, the two borderline units, the two STEP0_DERIVED cores, the 13 peripheral observations and the provenance questions UPQ-01…UPQ-05 are **unchanged**. Normalisation and matching removed nothing.

### 3.1 Where the material and provisional units sit

| Unit | Class | Group | Note |
|---|---|---|---|
| CLAUDE_A:R-P03-04 | SC-C | UNMATCHED | relation whose counterparty comes from Annex III 3.1/6; its parent claim is in CG-018 |
| CLAUDE_A:CL-P03-02 | SC-C | CG-018 | configuration claim; STEP0_DERIVED core CLAUDE_A:CL-P03-02#CORE attached to the same group |
| CLAUDE_A:CL-P03-03 | SC-C | UNMATCHED | the coupling premise itself is non-frozen text; listed among the configurations supported in CG-025 (SR-P03, peripheral) |
| CLAUDE_B:R-P04-05 | SC-C | UNMATCHED | audit object and purpose from Art. 12(5) third sentence; its parent claim is in CG-019 |
| CLAUDE_B:CL-P04-02 | SC-C | CG-019 | configuration claim; STEP0_DERIVED core CLAUDE_B:CL-P04-02#CORE attached |
| CLAUDE_B:CL-P04-04 | SC-B (provisional) | CG-022 | referent identification of 'the list' (Art. 23(1) second sentence); borderline (UPQ-02) |
| CLAUDE_B:CL-P04-07 | SC-B (provisional) | UNMATCHED | same referent identification; positional claim |
| CLAUDE_A:CL-P03-02#CORE | STEP0_DERIVED (provisional) | CG-018 (attached) | not an original claim |
| CLAUDE_B:CL-P04-02#CORE | STEP0_DERIVED (provisional) | CG-019 (attached) | not an original claim |

Three of the five material units are unmatched relations or claims; their parent configuration claims sit in groups CG-018 and CG-019. A material dependency therefore cannot disappear by being unmatched, and groups containing a unit that carries one keep the flag.

### 3.2 Groups with scope flags

| Group | Material (SC-C) | Borderline (SC-B) | Peripheral flag | Scope conflict among members | Propagated flags |
|---|---|---|---|---|---|
| CG-001 | no | no | NO | no | no |
| CG-002 | no | no | YES | no | no |
| CG-003 | no | no | NO | no | no |
| CG-004 | no | no | NO | no | no |
| CG-005 | no | no | NO | no | no |
| CG-006 | no | no | NO | no | no |
| CG-007 | no | no | NO | no | no |
| CG-008 | no | no | NO | no | no |
| CG-009 | no | no | NO | no | no |
| CG-010 | no | no | NO | no | no |
| CG-011 | no | no | NO | no | no |
| CG-012 | no | no | NO | no | no |
| CG-013 | no | no | NO | no | no |
| CG-014 | no | no | NO | no | no |
| CG-015 | no | no | NO | no | YES |
| CG-016 | no | no | YES | no | YES |
| CG-017 | no | no | NO | no | no |
| CG-018 | YES | no | YES | YES | no |
| CG-019 | YES | no | NO | YES | no |
| CG-020 | no | no | NO | no | no |
| CG-021 | no | no | YES | no | no |
| CG-022 | no | YES | YES | YES | no |
| CG-023 | no | no | NO | no | YES |
| CG-024 | no | no | NO | no | no |
| CG-025 | no | no | YES | no | YES |
| CG-026 | no | no | YES | no | YES |

**Evidence-scope conflicts** (members of one group whose classes differ): CG-018, CG-019, CG-022. In each, the non-SC-A member is ineligible (SC-C) or provisional (SC-B) for the primary comparison; the other members are unaffected. Material dependency may not support a primary-comparison improvement claim.

**Propagation to higher-order groups:** CG-025 (P03 architecture-level decisions) inherits a flag from CG-018 (SC-C member); CG-026 (P04 architecture-level decisions) inherits flags from CG-019 (SC-C member) and CG-022 (SC-B member). At the unit level, SR-P03 and AD-P04 keep the Step 0/Step 1 judgement of *peripheral* dependency (each stopping decision stands without the flagged configurations); this judgement remains flagged for human review.

### 3.3 Peripheral observations in groups

- CG-002: peripheral observation: CLAUDE_B:R-P03-02 (Annex III points 2 and 3.1 consulted to attribute the quality system of CS-P03-003 to the manufacturer
- CG-016: peripheral observation: CLAUDE_A:R-P04-21 (Art. 23(1) second sentence (published list) read for configuration-level coupling; peripheral observation: CLAUDE_B:R-P04-19 (Art. 23(1) list sentence read for linkage to CS-P04-012
- CG-018: peripheral observation: CLAUDE_B:CL-P03-02 (Claim wording 'assesses the manufacturer's quality system' uses the owner attribution of CS-P03-003 obtained f)
- CG-021: peripheral observation: CODEX_A:TA-P04-CFG-03 (UPQ-01 'continuity' purpose label: not in frozen content, source not recorded (plausible non-frozen source: re); peripheral observation: CODEX_B:TB-P04-CFG-03 (UPQ-01 'continuity' purpose label: not in frozen content, source not recorded (plausible non-frozen source: re)
- CG-022: 
- CG-025: peripheral observation: CLAUDE_A:SR-P03 (Reasoning cites Art. 9 alternative routes (non-frozen) and lists C-P03-03 (SC-C) among the supported configura)
- CG-026: peripheral observation: CODEX_A:TA-P04-AI-01 (UPQ-01 'continuity' purpose label: not in frozen content, source not recorded (plausible non-frozen source: re); peripheral observation: CODEX_B:TB-P04-AI-01 (UPQ-01 'continuity' purpose label: not in frozen content, source not recorded (plausible non-frozen source: re); peripheral observation: CLAUDE_B:AD-P04 (The headline lists configuration C-P04-B among the supported 

## 4. Statements about unmatched and non-register records

- 11 original units are unmatched (list in `G4_STEP2A_UNMATCHED_CLAIMS.csv`). The register notes, for traceability only, where another cell has a **non-register** record on the same topic (rejected or deferred candidate, declined claim, uncertainty entry). These records were not extracted at Step 1 (decision N-21) and are **not** matched, compared or interpreted here.
- **Codex A exported accepted relationships only.** The absence of rejected or deferred Codex A candidates is not evidence that they were considered and rejected; no unmatched Codex A unit exists, and no Codex A unit is described as 'absent' anywhere in these files.
- Unmatched units: CLAUDE_A:R-P03-02; CLAUDE_A:R-P03-03; CLAUDE_A:R-P03-04; CLAUDE_B:R-P04-05; CLAUDE_B:R-P04-13; CLAUDE_B:R-P04-16; CODEX_B:TB-O5-P03-01; CODEX_B:TB-O5-P04-02; CLAUDE_A:CL-P03-03; CLAUDE_B:CL-P04-07; CLAUDE_B:CL-P04-08.

## 5. Limits

Matching is by one AI executor (the Claude-arm orchestrator; role conflict D-15) and is preliminary. Correspondence is judged on the normalised text and frozen statements, not on legal expertise; CONFOUNDED_INPUT (decision C4) applies to every group; no group asserts substantive equivalence.