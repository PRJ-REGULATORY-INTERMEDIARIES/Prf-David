# Production Methodology — Working Draft v1.1

**Project:** `dataset-eurlex`
**Version:** production v1.1 (supersedes v1.0 for all cases, per change control)
**Status:** consolidates a methodological refinement derived from a researcher's deep reading of Case 01 and confirmed against RIT theory and EU legislative-drafting doctrine; three-case production coding under this version has not yet started as of this document's creation
**Predecessor:** `METHODOLOGY_WORKING_DRAFT_SIMPLIFIED.md` (v1.0), preserved unchanged

## 1. What changed and why

Two decisions, both general rules rather than Case-01-specific corrections:

1. **Sequence.** The reading procedure identifies the R–T regulatory relationship first and examines third actors only afterward, testing each one functionally rather than searching directly for "intermediaries." Searching for intermediary-shaped actors first risks converting "what is the structure of this regulatory relationship?" into "does some actor here resemble a familiar regulatory institution?" — increasing the influence of institutional labels and prior expectation over textual function. This restores the RIT model's own premise: intermediaries are identified by the function they perform in a relationship, not by organisational type (Abbott, Levi-Faur & Snidal, "Theorizing Regulatory Intermediaries: The RIT Model," *The ANNALS of the American Academy of Political and Social Science* 670(1), 2017, pp. 14–35; "Enriching the RIT Framework," same volume, pp. 280–288).
2. **Evidentiary layering.** Operative provisions (articles, paragraphs, points, annexes forming the enacting terms) and recitals are not the same kind of evidence. Recitals "set out concise reasons for the chief provisions of the enacting terms ... and shall not contain normative provisions" (Interinstitutional Agreement of 22 December 1998 on common guidelines for the quality of drafting of Community legislation, Guideline 10, OJ C 73, 17.3.1999). The Court of Justice has repeatedly held that "the preamble to a Community act has no binding legal force and cannot be relied on as a ground for derogating from the actual provisions of the act in question" (Case C-134/08, *Hauptzollamt Bremen v J.E. Tyson Parketthandel*, judgment of 2 April 2009, para. 16). A recital may support interpretation; it cannot, alone, generate a positive R–I–T finding.

## 2. Research workflow (unchanged in shape)

```text
OFFICIAL EU ACT
       ↓
FROZEN CORPUS
       ↓
PRIMARY INTERPRETIVE READER
       ↓
STRUCTURED R-I-T MATRIX (operative-anchored)
       ↓
SECONDARY CRITICAL REVIEWER
       ↓
RESEARCHER ADJUDICATION
       ↓
FINAL CASE DATASET
```

The workflow shape, the three cases, and the states in `config/production.yaml` are unchanged. What changes is the reading procedure and the record schema used at the primary and secondary stages.

## 3. R–T-first reconstruction

Order of analysis for every candidate passage:

1. Is there a regulatory episode at all?
2. Who is R (the regulator exercising the focal function)?
3. Who is T (the actor, actor class, or institutional role subject to that function)?
4. Only once R and T are reconstructed: which third actors, if any, are materially present in that architecture?
5. For each such actor X, apply the Third-Actor Functional Test (§4).

`R`, `I`, and `T` remain relational roles rather than fixed properties of organisations, and `object ≠ target` remains load-bearing: activities, information, products, processes, conduct, and compliance states are `object`.

## 4. Third-Actor Functional Test

For every candidate third actor X:

- **A. Distinction** — is X analytically distinct from R and from T?
- **B. Function** — does the text attribute to X a specific, relevant action or competence?
- **C. Regulatory integration** — does that function participate in the way R affects, supervises, informs, evaluates, or structures T's conduct? (Assisting R prepare R's own act, without any attributed function toward T, fails this dimension.)
- **D. Evidence** — is the connection supported by operative text, not by a recital or by institutional plausibility?
- **E. Counterfactual** — if X's function were removed, would a relevant step of the R→T mechanism actually be lost?

Each dimension is recorded `YES`/`NO`/`UNCLEAR` with a short note, in the record's `third_actor_test` field (`methodology/production_v1.1/coding_matrix_schema.json`). The test is a documented reasoning aid and audit trail, not a mechanical trigger: no combination of results automatically forces a particular `relation_type`. This is a deliberate design choice. The predecessor pilot methodology (`methodology/v1.1.0/`) enforced "a distinct third actor (condition C = YES) requires the `I` field to be populated" regardless of whether that actor mediated anything (condition D), which produced a documented, irreducible structural conflict with the separate rule that a direct relationship carries no `I` (see `03_human/stage4_attempt_02/pre_ra_4way/KNOWN_LIMITATIONS_V1_1.md` and the resulting structural-limitation corrections in every downstream reference/RA output). v1.1 keeps the five-dimension record for transparency and reviewability while leaving the relation_type judgment itself to the coder's substantive reasoning, precisely so a distinct-but-non-mediating third actor never forces an inconsistent state.

third actor ≠ intermediary, exactly as actor mention ≠ regulatory relationship. A distinct actor with a documented function that nonetheless fails regulatory integration or the counterfactual test is not `I` in this relation; record it as a considered-and-rejected candidate in the uncertainty log (`issue_type` such as `third_actor_considered_not_mediating`).

Intermediation is a relational position, not a degree of power: informational, consultative, scientific, verifying, certifying, auditing, transmitting, delegated-implementing, enforcement-supporting, coordinating, and monitoring functions can all satisfy the test provided the five dimensions are met on the corpus's own terms. `relation_type` should never be used as a proxy for characterizing *what kind* of intermediation is present — that belongs in `mediating_function` and `mechanism`.

## 5. Two-layer corpus and the evidence rule

**Primary operative corpus:** articles, their internal subdivisions, and annexes that normatively integrate into the regulatory mechanism — the enacting terms. This is the corpus of primary extraction.

**Contextual interpretive corpus:** recitals and other preambular material. Function: interpret purpose, clarify institutional design, situate the regulatory problem, explain actors, clarify terminology, and provide additional interpretive support. It is not an autonomous corpus for generating positive relations.

**Evidence rule.** No R–I–T relation may be coded `intermediated` or `direct` on the strength of a recital alone. A positive relation requires a non-null `operative_anchor_location`:

- *Article + recital* can jointly support a relation when the article itself supplies sufficient evidence of the regulatory architecture and the recital adds interpretive context.
- *Recital alone* cannot produce a positive relation. Log it instead as a contextual candidate in the uncertainty file (`issue_type: "contextual_candidate_recital_only"`), stating what operative anchor would be needed to promote it.

**Illustration (Case 01, Article 8(4)).** The proposed relation Commission → EEA → Member States is anchored in the operative text itself — Article 8(4) attributes to the EEA the specific duty of assisting the Commission in preparing the Article 6/7 assessments — with Recital 37 providing interpretive support, not the relation's only basis. Removing the recital does not remove the relation, because the operative anchor survives on its own. By contrast, the mere presence of reports or scientific input referenced in an assessment context does not, by itself, establish an intermediary. This same provision was examined, and its `intermediated` classification rejected, by the earlier pilot's blind reference adjudication on grounds squarely about regulatory integration (§4.C) — that assisting R prepare R's own act is service on the regulator's side, not mediation toward T, since nothing in the act gives the EEA a function toward the Member States themselves. This tension is not resolved by the evidentiary-layer rule alone, since both readings rest on operative text; it remains open for the secondary reviewer and the researcher, and must not be treated as settled by this working draft.

## 6. Primary and secondary coding

Unchanged from v1.0 in division of labour: the primary interpretive reader proposes; the secondary critical reviewer checks for omission, over-coding, target/object confusion, actor-role errors, unsupported mediating functions, mechanism errors, evidentiary limitations, and — new in v1.1 — recital-only anchoring and actor-versus-instrument confusion (an automated system or registry is an instrument unless the text attributes it an independent function). The reviewer classifies each proposal `ACCEPT`, `REVISE`, `QUESTION`, or `ADD_MISSING_RELATION` and does not silently alter the primary output. See `prompts/production/PRIMARY_INTERPRETIVE_READER.md` and `prompts/production/SECONDARY_CRITICAL_REVIEWER.md`.

## 7. Researcher adjudication and final data

Unchanged from v1.0: the researcher alone assigns `APPROVE`, `CHANGE`, `EXCLUDE`, or `UNRESOLVED` and records final R, I, T, and relation type where applicable, informed by the primary proposal, the secondary review, and canonical evidence. Only after human adjudication may the workflow create `final_case_dataset.csv`/`.json`.

## 8. Functional role naming

Analytical roles are now named functionally rather than by provider or model: **Primary Interpretive Reader** (formerly "Claude primary coder") and **Secondary Critical Reviewer** (formerly "Luna secondary reviewer"). This separates the analytical role from its computational implementation. Per-run computational metadata — provider, model, model version, reasoning effort, run date, run identifier, prompt version — is recorded separately, per run, in each case's `primary_coding/` or `secondary_review/` directory, and is never invented when unobserved.

Historical files that already name a specific model (e.g. `CLAUDE_CODING_PROPOSAL.json`, `LUNA_SECONDARY_REVIEW_NOTE.md`, and every artifact of the earlier intensive pilot) are preserved unaltered for audit and are not retroactively renamed or reattributed. Only prompts, documentation, schemas, and outputs created from this version onward use functional naming.

## 9. Epistemic status

These are methodological refinements derived from exploratory empirical reading and checked against RIT theory and EU drafting/interpretive doctrine. They do not establish that recitals are empirically irrelevant, that every third actor is an intermediary, that only formally delegated actors can be intermediaries, or that Article 8(4) is definitively adjudicated in either direction. They establish more restrictive, more reproducible rules under which that question — and equivalent questions in Case 02 and Case 03 — can be examined.

## 10. Consolidated principle

> The unit of analysis is the legally evidenced regulatory relationship, not the actor. Identify the R–T regulatory relationship first. Then examine every materially involved third actor and determine, through a functional test, whether that actor occupies an intermediary position in the regulatory mechanism. A positive relationship requires an operative normative anchor. Recitals may support interpretation but cannot independently generate a positive R–I–T coding.

## 11. Application to all three cases

This version applies identically to Case 01 (European Climate Law), Case 02 (CBAM), and Case 03 (EUDR) — no case-specific adaptation, per `docs/methodology/CASE_SELECTION_PROTOCOL.md`'s change-control principle. Re-reading a case under this version and reaching different classifications than the v1.0 proposal is an expected and intended effect of the calibration, not a defect to be reconciled away.

## References

- Abbott, Kenneth W.; Levi-Faur, David; Snidal, Duncan. "Theorizing Regulatory Intermediaries: The RIT Model." *The ANNALS of the American Academy of Political and Social Science*, v. 670, n. 1, 2017, pp. 14–35.
- Abbott, Kenneth W.; Levi-Faur, David; Snidal, Duncan. "Enriching the RIT Framework." *The ANNALS of the American Academy of Political and Social Science*, v. 670, n. 1, 2017, pp. 280–288.
- European Parliament, Council, Commission. *Interinstitutional Agreement of 22 December 1998 on common guidelines for the quality of drafting of Community legislation*, OJ C 73, 17.3.1999, p. 1, Guideline 10.
- Court of Justice of the European Union, Case C-134/08, *Hauptzollamt Bremen v J.E. Tyson Parketthandel GmbH hanse j.*, judgment of 2 April 2009, ECLI:EU:C:2009:229, para. 16.
