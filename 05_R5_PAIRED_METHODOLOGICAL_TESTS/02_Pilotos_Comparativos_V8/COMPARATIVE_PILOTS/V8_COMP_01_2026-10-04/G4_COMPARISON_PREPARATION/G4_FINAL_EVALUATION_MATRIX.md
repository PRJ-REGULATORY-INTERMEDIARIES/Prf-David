# G4 — Final operational evaluation matrix

**Experiment:** V8-COMP-01 · **Stage:** G3C closeout · **Date:** 2026-10-04
**Status:** `FINALIZED_BEFORE_SYSTEMATIC_CROSS_ARM_CLAIM_MATCHING`
**Written before** the orchestrator opened the architectural-inference files of the four cells for claim extraction. It was **not** written blind: see §0.

References used: `RESEARCH_PROTOCOL_v0_1.md` §6, `COMPARISON_EVALUATION_CRITERIA.md`, `G4_OPERATIONAL_COMPARISON_SPEC_DRAFT.md` (**not available in the workspace**; the external draft could not be consulted, see `DOCUMENTARY_PENDING_ITEMS_REGISTER.md` P-01). Where the draft may differ, a reconciliation step is required before use (G4 step 0.5).

## 0. Epistemic status of this matrix (read first)

1. Exploratory study, two microcases (P03: 6 statements; P04: 14), four executions. No inferential statistics, no causal identification of "model" or "method" effects, no generalisation.
2. This is **not** a blind prospective preregistration. Before this matrix was finalised, the following was already known to people involved: the aggregate structure of each cell (counts of candidate relationships and uncertainty entries, in the Claude completion report); the external G3C audit's findings (reported to the orchestrator only as a task description); the existence and file names of the Codex cells; the R-P04-05 evidence-boundary issue; the Codex execution log's non-blind statement. The orchestrator also read the *contents of the Codex Track B execution log and QA-report limitation passages* and the relationship rows listed in Issue C. The matrix was nevertheless fixed **before** any pairwise claim matching and **before** reading architecture-level claims for extraction.
3. Agreement between AI systems is *not* legal validity. Only (a) traceable anchoring to in-scope frozen evidence and (b) independent human legal review may support a validity statement, and neither is automatic.
4. No composite or weighted index is computed. Counts (accepted relationships, uncertainty entries, words, categories) are reported descriptively and **never** interpreted as methodological merit.

## 1. Evidence-scope rule (uniform for all four cells)

Because the scope rule given to executors was ambiguous ("resolve a cited wording question" / "wording ambiguity"), one rule is fixed prospectively for evaluation. It does **not** change any frozen output.

| Tag | Definition | Allowed as support for a claim? |
|---|---|---|
| **E1 — FROZEN** | Content expressed in the `exact_legal_excerpt` / register fields of the statement(s) the claim cites. | Yes. |
| **E1x — REFERENT** | Text of another provision used **only** to identify the referent of a cross-reference or anaphor that is itself quoted in a cited frozen excerpt (e.g. "Article 9", "point 3.2", "the list referred to in Article 23(1)", "that agreement"). It must not add an actor, action, object, purpose, condition, consequence or modality. | Yes, with the referent source named; claim must be tagged `cross_provision_inference`. |
| **E2 — CONTEXT** | Any other official text of P03/P04 read to verify wording, segmentation, location or terminology. | Provenance only. May **not** be a warrant. |
| **E3 — EXTENDED** | Any element (party, action, object, purpose, condition, consequence, modality) taken from non-frozen text and used in a claim. | Not as support. A claim that depends on E3 is `SCOPE_EXTENDED`; evaluate it **separately**, never as "improved". |

Mixed claims: tag the claim by the weakest element it depends on; if the E1-only core can be separated, evaluate the core (tag `E1_CORE`) and the extension separately. Article 22(7) of P04 is excluded context in all cells. A cell for which the tag cannot be established from its structured fields (the Codex relationship tables contain no cross-provision field) is tagged `SCOPE_NOT_DETERMINABLE` for that claim until a reviewer checks the cited anchors; it is **not** presumed clean.

## 2. Units and contrasts

- **Primary qualitative unit:** the individual *architectural claim* (configuration-level or architecture-level; plus relation-level claims on which they depend), with its legal evidence (statement IDs → provision → source hash), its inferential warrant, counter-evidence and stopping decision.
- **Secondary units:** relationships (accepted / rejected / deferred), uncertainty entries, positional/part–whole/sensitivity assertions (Track B only).
- **Contrast families (pre-specified, each reported separately):**
  1. *Method within model:* Codex A→B; Claude A→B.
  2. *Model within method:* Codex A vs Claude A; Codex B vs Claude B (symmetric; no reference arm).
  3. *Interaction (descriptive only):* whether the A→B pattern in family 1 is similar or different across models. No test statistic.
  4. *Robustness:* which claims are shared by all four cells, by three, two, one.
- Both microcases are reported separately (P03, P04); no pooling.

## 3. Dimensions A–I

Each dimension is scored **per claim or per relationship** with categorical labels — never summed.

| ID | Dimension | Question | Evidence required | Labels |
|---|---|---|---|---|
| **A** | Fidelity to primary legal evidence | Does every element of the claim appear in E1 (or E1x)? Is modality/condition/actor preserved? | Statement IDs, register fields, source hash; scope tag (§1) | `FAITHFUL` · `FAITHFUL_WITH_E1x` · `PARTLY_UNSUPPORTED` · `SCOPE_EXTENDED` · `NOT_DETERMINABLE` |
| **B** | Correctness of relational classification | Are parties, direction, type and modality of accepted/rejected/deferred relations defensible on E1? | Parties and action in the excerpt; V8 rule 2 (counterpart + governance-relevant connection) | `DEFENSIBLE` · `DEFENSIBLE_BUT_ALTERNATIVE_READING` · `INDEFENSIBLE` · `HUMAN_REVIEW` |
| **C** | Unsupported or fabricated edges | Was a unilateral assignment, co-occurrence, shared actor or graph adjacency promoted to an edge? Was a counterparty inferred from a passive/unexpressed actor? | Statement's `actor`/`NOT_EXPRESSED_IN_SENTENCE` field; relation record | `NONE` · `UNSUPPORTED_EDGE` · `ACTOR_INFERRED` · `HUMAN_REVIEW` |
| **D** | Architectural inference and cross-level justification | Does the claim stop at the level the evidence supports? Is the bearer of every property stated? Are problem, scale, coupling, consequence, alternatives and boundary stated? | Warrant, counter-evidence, stopping decision; bearer statement | `STOPS_AT_SUPPORTED_LEVEL` · `PROMOTED_ONE_LEVEL` · `PROMOTED_MULTIPLE_LEVELS` · `BEARER_UNSTATED` · `NO_CLAIM_MADE` · `HUMAN_REVIEW` |
| **E** | Traceability | Can a reader go claim → configuration → relation → statement → provision → source/hash without gaps? | Full chain present and verifiable | `COMPLETE_CHAIN` · `GAP_AT:<level>` · `NOT_TRACEABLE` |
| **F** | Uncertainty and sensitivity | Are ambiguities preserved and claims not promoted over them? Did sensitivity/alternatives test whether the claim survives? | Uncertainty register link; alternatives; survival record | `PRESERVED` · `PARTLY_PRESERVED` · `SUPPRESSED` · `SENSITIVITY_TESTED` · `SENSITIVITY_ABSENT` |
| **G** | Additional analytical effort | What did extra fields/steps cost relative to the information they added? | Number of added fields/files/decisions; reviewer time; redundancy observed (from logs) | descriptive only: `effort items`, `reviewer minutes`, `redundant: yes/no/partly` |
| **H** | Cross-model agreement/disagreement | Do the same-method cells of different models reach the same proposition, same level, same stop? | Matching result (see `G4_CLAIM_MATCHING_RULES.md`) | the seven matching labels; agreement ≠ validity |
| **I** | Methodological contribution of the eight operations | In each model, did an operation change, block, qualify or merely restate what the A cell already contained? | Operation register entry + matched A claim | `B_IMPROVES` · `B_CLARIFIES_ONLY` · `B_EQUIVALENT` · `B_WORSE` · `UNRESOLVED` (protocol vocabulary) |

Mapping of the protocol's pre-registered criteria (a)–(g) to A–I: (a) traceability → E; (b) inferential validity → A, B, C, D; (c) clarity → D, E (reviewer ratings); (d) distinctive sustained discovery → I; (e) robustness → F, H; (f) reproducibility/review → E, human template; (g) analytic cost → G.

## 4. Rules that apply to every dimension

1. Scoring is by claim, anchored to statement IDs. No cell is scored on length, number of sections or number of categories.
2. A claim that is `SCOPE_EXTENDED` or `SCOPE_NOT_DETERMINABLE` cannot support an improvement label (`SUBSTANTIVELY_IMPROVED`, `B_IMPROVES`) until resolved.
3. A *deferral* or "no architecture-level claim" is a valid, scored outcome (dimension D = `NO_CLAIM_MADE` / `STOPS_AT_SUPPORTED_LEVEL`). Not being able to say more is not a defect by itself.
4. Findings are classified with the labels in `G4_CLAIM_MATCHING_RULES.md`. The null result (`EQUIVALENT`, `B_EQUIVALENT`) is a result.
5. All AI-assisted scoring is labelled `PRELIMINARY_AI_ASSISTED`, is logged, and is executed **sequentially** (no parallel agents), by an executor that states what it has seen. Disputed or `HUMAN_REVIEW` items go to the human instrument (`G4_HUMAN_REVIEW_TEMPLATE.csv`). No human judgement is simulated.
6. The AI-assisted pass must record, for each item, what the executor had read beforehand (contamination of the evaluator).
7. Results must be reported separately per case, per contrast family, per dimension; with explicit limitations from `CROSS_MODEL_PROTOCOL_DEVIATIONS.md`.

## 5. Pre-declared interpretations (to prevent post-hoc fitting)

- Convergence between Codex and Claude after the eight operations, if observed, supports at most the statement "outputs became more similar"; it does not distinguish better legal validity from a common procedural template.
- A larger number of uncertainty entries or sensitivity items in B is *effort/exposure*, not by itself better treatment of uncertainty (dimension F is judged on whether claims were un-promoted, not on volume).
- Any difference traceable to the evidence-scope issue (§1), to differing method-input documents between models (see deviations D-07) or to executor context (D-01…D-03) is reported as *confounded* and is not attributed to method or model.
