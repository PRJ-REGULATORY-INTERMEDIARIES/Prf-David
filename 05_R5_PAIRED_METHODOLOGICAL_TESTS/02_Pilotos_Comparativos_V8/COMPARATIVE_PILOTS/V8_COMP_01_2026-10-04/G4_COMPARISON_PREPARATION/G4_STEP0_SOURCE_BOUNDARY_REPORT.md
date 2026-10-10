# G4 Step 0 — source-boundary audit report

**Date:** 2026-10-04 · **Scope:** legal-evidence scope classification only.
**Not done (by rule):** no claim matching across cells; no judgement that Codex or Claude is superior; no judgement that Track B improves Track A. Counts below describe evidence-boundary status of each cell's own claims and are **not** comparative merit.
Companion files: `G4_EVIDENCE_SCOPE_DICTIONARY.md`, `G4_STEP0_EVIDENCE_CLASSIFICATION.csv` (114 rows: 112 cell units + 2 derived core units), `G4_STEP0_HUMAN_REVIEW_QUEUE.csv`.

## 1. Method (identical for the four cells)

1. Units: every **accepted relationship** and every **architectural-level claim** in the cell's files — configuration claims, positional claims accepted in Track B, and architecture-level claims or stopping decisions. Rejected and deferred candidates are not claims; where a cell lists them they are noted but not classified.
2. For each unit: original ID; cell; cited common statement IDs; legal anchors from the register; premise inventory (parties, act/modality, object, condition/timing, direction/type, stated purpose, consequence); check of each element against the frozen excerpts and register fields (automatic keyword test on parties, then manual reading of every unit); check of the cell's own record of wider-text use (cross-provision fields, uncertainty registers, execution logs, QA reports, part-whole and positional files).
3. Classification with the dictionary; materiality test (load-bearing vs peripheral); core split for mixed claims; interpretive vocabulary routed to dimension D rather than treated as scope.
4. Where reliance on outside text could not be established either way from the record, the issue is stated as unresolved; compliance is not assumed. Missing rejected/deferred candidate rows are **not** treated as evidence that those candidates were considered and rejected (Codex Track A's relationship table contains accepted relations only, 16 rows, no decision column).
5. Provenance of non-frozen text was verified against the official text only to determine what the non-frozen sentence says (Art. 12(5) third sentence; Art. 23(1) second sentence; Annex III points 3.1, 3.2, 6; Art. 9; recital 13).

**Evidence inspected per cell:** relationship tables, configuration files, architectural-inference files, positional analysis (Codex B), uncertainty registers, execution logs and QA reports (where they exist), part-whole and sensitivity files (Claude B: scanned; Codex B: scanned by keyword). Codex Track A has no execution log; Codex B's log records no consultations.

## 2. Results

### 2.1 Units classified per cell

| Cell | Relations accepted | Configuration claims | Positional claims | Architecture decisions | **Total** | SC-A | SC-B | SC-C | SC-D |
|---|---|---|---|---|---|---|---|---|---|
| Codex Track A | 16 | 6 | – | 2 | **24** | 24 | 0 | 0 | 0 |
| Codex Track B | 17 | 6 | 4 | 2 | **29** | 29 | 0 | 0 | 0 |
| Claude Track A | 19 | 7 | – | 2 | **28** | 25 | 0 | 3 | 0 |
| Claude Track B | 19 | 6 | 4 | 2 | **31** | 27 | 2 | 2 | 0 |
| **All** | 71 | 25 | 8 | 8 | **112** | 105 | 2 | 5 | 0 |

Plus two derived core units (`CL-P03-02#CORE`, `CL-P04-02#CORE`), which are Step 0 constructs and not cell claims. IDs for Codex B positional rows and for Claude B architecture decisions (which have no native ID) were assigned at Step 0 and are marked in `source_location`.

### 2.2 Claims with material evidence-scope deviations (SC-C or load-bearing SC-D): **5**

| Cell | Unit | Non-frozen text relied on | Element supplied |
|---|---|---|---|
| Claude A | R-P03-04 | Annex III point 3.1; point 6; Art. 10(1) | counterparty (manufacturer); identity of 'notified body' |
| Claude A | CL-P03-02 | same (via R-P03-04) | member relation; separable core exists |
| Claude A | CL-P03-03 | Annex III point 6; Art. 10(1) | the coupling premise itself; no core |
| Claude B | R-P04-05 | Art. 12(5), third sentence | audited party, object and purpose of the audit |
| Claude B | CL-P04-02 | Art. 12(5), third sentence | warrant ('auditee') and chain member R-P04-05; separable core exists |

There is **no** load-bearing SC-D unit. All five are `NO_SENSITIVITY_ONLY`.

### 2.3 Borderline referent identification (SC-B, provisional): **2** (Claude B CL-P04-04, CL-P04-07)

Both use the second sentence of Art. 23(1) to identify "the list referred to in the first paragraph of Article 23" and read it as the Registry-selected providers. This is a referent identification that nevertheless supplies the coupling between the complainant's choice and the Registry's selection. Eligible provisionally; human confirmation required (SC-B vs SC-C).

### 2.4 Peripheral outside or unresolved elements: **13** units carry a flag (2 of them are the SC-B rows above)

- **Codex (4 units — TA-P04-CFG-03, TA-P04-AI-01, TB-P04-CFG-03, TB-P04-AI-01):** the label "continuity" for the escrow arrangement states a purpose that is not in CS-P04-009..011 and whose source the cell does not record. The official text contains the same idea in recital 13 (outside the frozen boundary and outside Art. 15); the cells do not say they consulted it. The configuration's membership, coupling and the architecture conclusion do not depend on the label. Classified SC-A with a flag; **UPQ-01**.
- **Claude A (2):** R-P04-21 (Art. 23(1) second sentence read for a coupling that the cell then deferred); SR-P03 (negative stopping decision whose supporting reasons cite Art. 9 alternative routes and list the SC-C configuration CL-P03-03; the stop would stand without them).
- **Claude B (7):** R-P03-02 (owner attribution of CS-P03-003 from Annex III points 2/3.1, recorded as not counted); R-P04-16 and R-P04-19 (Art. 23(1) list referent read, not a premise of those relations); CL-P03-02 (claim wording 'assesses the manufacturer's quality system'); AD-P04 (negative decision citing configuration C-P04-B and a declined claim based on 'per wider text'); CL-P04-04 and CL-P04-07 (above).

### 2.5 Unresolved provenance questions: **5**

| ID | Question | Units |
|---|---|---|
| UPQ-01 | Source of the 'continuity' purpose label in the escrow configuration and the architecture claims | 4 (Codex A, Codex B) |
| UPQ-02 | Referent identification of 'the list' (Art. 23(1)): SC-B or SC-C | 2 (Claude B) |
| UPQ-03 | Codex Track A: no execution log or consultation record; claims verified against frozen text but influence of unrecorded reading cannot be excluded | cell-level |
| UPQ-04 | Codex Track B: execution log without consultation record; same limit | cell-level |
| UPQ-05 | Claude A/B: logs record reading beyond the frozen statements (Art. 22(7), 14, 15(2), 23(2)-(4)); influence on which candidates were considered cannot be measured | cell-level |

## 3. Claude Track B R-P04-05 and Article 12(5), third sentence

**What the frozen evidence says.** CS-P04-001: "At the end of the phased registration an independent audit shall be performed at the expense of the Registry and shall report its findings to the Commission." CS-P04-002: "The auditor shall be appointed by the Registry after consulting the Commission."

**What it does not say.** What is audited, and why. The register's own field for CS-P04-001 states that "the text grammatically makes the audit report; no natural-person actor is inserted"; nothing in either statement names an audited party or purpose.

**What R-P04-05 (Claude B) states.** `auditor → Registry`, "verification/assurance (audit of the Registry's administration of the phased registration)", accepted at `cross_provision_inference`, `human_review_needed`.

**Where that content comes from.** The third sentence of Art. 12(5) (verified in the official text): "The purpose of the audit shall be to confirm the fair, appropriate and sound operational and technical administration of the phased registration period by the Registry." The cell records this (uncertainty U-13: "it comes from the third sentence of Art. 12(5), consulted to resolve 'audit of what'"; log W-05; part-whole PW-26).

**Three layers.**
1. *Explicitly in frozen evidence:* Registry appoints and pays; findings go to the Commission; timing. The Registry–auditor link of appointment/funding type is already coded as R-P04-02.
2. *Context permitted for provenance verification:* reading Art. 12(5) as a whole to confirm the locator and segmentation.
3. *Additional substantive legal evidence outside the boundary:* the object and purpose of the audit and the identification of the Registry as audited party. This is the load-bearing content of R-P04-05, so the relation is **SC-C**. It is not a wording clarification of an expression in the frozen excerpt (there is no quoted expression that points to it), so it is not SC-B.

**Propagation (same rule everywhere).** CL-P04-02 (Claude B) is SC-C because its warrant and chain rely on the same premise; its textual claim sentence is frozen-text only and is carried as `CL-P04-02#CORE`. AD-P04 (negative decision) carries a peripheral flag. The same premise appears in Claude B's uncertainty U-16 and refused claim RL-03 ("per wider text") — refused claims are not accepted claims and are not classified.

**Counterpart treatment of the same relation in the other cells (scope only, no comparison of conclusions).** Claude A read the same sentence and recorded that it was **not used** (R-P04-05 deferred): SC-A for its claims. Codex A and Codex B record no auditor→Registry verification relation and no audit purpose; their audit configurations (TA/TB-P04-CFG-01) state no audited party. Applying the same rule to them finds no use of the sentence in any accepted unit.

**Not done.** The Claude B artifacts were not modified; no scope-clean re-coding was produced.

## 4. Other uses of non-frozen text, treated by the same rule

| Cell | Use | Rule outcome |
|---|---|---|
| Claude A | Annex III 3.1 and 6 to supply the manufacturer and identify 'notified body' with Art. 10(1) bodies (R-P03-04, CL-P03-02, CL-P03-03) | SC-C (counterparty and coupling premise from outside the frozen set; point 3.2 is quoted in the excerpt but identifies only the requirements) |
| Claude B | Annex III 2/3.1 for CS-P03-003 owner | peripheral, recorded as not counted as support |
| Claude B | Art. 9, Art. 14, Art. 15(1) anaphora, Art. 15(2) | context only or anaphor resolved within frozen statements: SC-A |
| Claude B | Art. 23(1) second sentence | SC-B (borderline), UPQ-02 |
| Claude A | Art. 9 alternative routes inside a negative decision; Art. 23(1) for a deferred coupling | peripheral |
| Codex A/B | No cross-provision field; 'continuity' label (recital 13 plausible) | SC-A with UPQ-01 flag |

An anaphor that resolves to another **frozen** statement (for example "that agreement" in CS-P04-010 → CS-P04-009; "the escrow agent") remains SC-A in every cell.

## 5. Symmetry and recording asymmetry

The rule, tests and materiality criteria were applied identically. The cells differ in how much they **record** about wider-text use: both Claude cells log every consultation and mark cross-provisions per relation; the Codex cells have no such field or log. Findings in section 2.2 therefore reflect *recorded* reliance plus claim-by-claim verification; they do not show that the Codex cells consulted less, nor that they complied better. Cell-level questions UPQ-03/04 remain open for exactly this reason. Nothing in this report compares quality or superiority.

## 6. Consequences for G4 (conditional on gate decision)

- **Primary comparison set:** 105 SC-A units (94 `YES` without flag and 11 `YES_WITH_PERIPHERAL_FLAG`), the 2 derived core units once confirmed, and the 2 SC-B units **only after human confirmation**.
- **Sensitivity-only set (separately labelled):** the 5 SC-C units (and the 2 SC-B units if a reviewer rules them SC-C).
- **Human review queue:** 28 items (7 P1, 14 P2, 7 P3) in `G4_STEP0_HUMAN_REVIEW_QUEUE.csv`, covering contested scope, the 8 central architecture decisions, borderline referents, unresolved provenance, derived-core confirmation and cell-flagged items.
- Within-Claude A/B contrasts must not classify as improvement any difference caused by SC-C units (matching rule 2): for example the accepted-versus-deferred status of R-P04-05 across Claude A and Claude B.

## 7. Limits of this audit

Scope is judged by one AI session (the Claude-arm orchestrator, deviation D-15) and is therefore preliminary; keyword tests cover parties, not acts, conditions or purposes, which were read manually; the external specification's definitions were not available, so label reconciliation is pending; the official text verifies *what non-frozen sentences say*, not whether they are legally controlling; classification does not evaluate legal correctness.
