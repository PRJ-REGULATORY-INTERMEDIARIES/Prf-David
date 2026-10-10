# Ontology regression test — rev2

**Date:** 2026-10-03 · **Status:** `INTERNAL_REGRESSION` — same single, non-blind evaluator as the first self-test. **Not independent scientific validation.**
**Preserved unchanged:** `validation/ONTOLOGY_STRESS_TEST_MATERIALITY_DELTA_v0_4.md` (the original 39-case report) and the 16 historical tests.
**Object tested:** `ontology/ONTOLOGY_v0_4.md` **rev2** (D04–D09). All cases invented: `TOY / NOT REAL LEGAL EVIDENCE`; no GDPR text is used or asserted.
**Weighting caveat:** the rules and the variants were written in the same session; PASSED results are weak evidence. The informative results are the three failures found by the variants (§3).

## 1. Re-run of the ten cases (original result → revision → new result → remaining limitation)

| ID | Original result | Applicable revision | New result | Remaining limitation |
|---|---|---|---|---|
| X01 mandate to establish an authority | FAILED | PT-1 (constitution by mandate) | **PASSED** | Drafting cues ("is established" vs "shall be established") may not survive translation; ambiguous wording → adjudicate (variants X01b, X01c) |
| X02 relation depends on an unbuilt register | FAILED | PT-2 (`depends_on`, support-gap report; instantiation only for positions/devices) | **PASSED** | `depends_on` is entered by the coder; no automatic detection |
| L03 custom/convention without enacted text | FAILED | PT-3 | **PASSED** | Out of first-round scope; no rule yet for evidencing custom |
| W02 "necessary stage" from a partly coded corpus | FAILED | PT-4 (closure/coverage), extended by PT-8 | **PASSED** | Closure declarations are hard to verify; unresolved external references weaken them (variant W02b) |
| A05 "accountable to the public" | INCONCLUSIVE | D04 (INFO / AC / IND; diffuse forums allowed with channel + duty) | **PASSED** — classified **IND** (not excluded; elements missing) | Threshold AR-1 (duty + justification + questioning; assessment distinguishes a fuller form) is an assumption |
| I04 "accredited under the applicable scheme", rules outside the corpus | INCONCLUSIVE | D05 (typed external reference) | **PASSED** — I1 + external reference; constitution `undetermined`; no instantiation | Needs the external source to be located and verified case by case |
| M12 artifact level (register extract, certificate) | INCONCLUSIVE | D06 (evidence status per claim; artifact metadata separate) | **PASSED** | Which claims count as level C (single entry vs operation of a relation) needs coding guidelines |
| X03 category vs instance ("competent authority") | INCONCLUSIVE | D08 (type / instance / jurisdiction / time) | **PASSED** | Type-level architecture for multi-jurisdiction law; counts need PT-7 (variant X03c) |
| X04 practice without legal basis | INCONCLUSIVE | D07 (`ObservedArrangement`, separate layer) | **PASSED** | No method yet for reconstructing operational architecture; no comparison metric |
| W05 discretion by function | INCONCLUSIVE | D09 (profile; no aggregate score) | **PASSED** | Cross-law comparison without a scalar needs an ordinal scheme, deferred |

**Result:** 10 of 10 re-run cases PASSED under rev2 (self-assessed). The variants below test the same rules from other angles.

## 2. Targeted variants

"First application" = the rule set as it stood when the variant was applied.

### 2.1 A05 — diffuse forums (D04)

| ID | TOY case | Expected | First application | After patch |
|---|---|---|---|---|
| A05a | "The Board shall publish an annual report on its website." | INFO (transparency); not AC | **PASSED** | — |
| A05b | "The Board shall hold an annual public hearing at which any person may put questions, and shall answer in writing within 30 days." | AC (answerability) with a diffuse forum, channel and duty; assessment capacity recorded as **absent** | **PASSED** (under AR-1) | — |
| A05c | "The Board is accountable to the public." | IND (missing elements recorded) | **PASSED** | — |
| A05d | "Decisions shall be published in the official journal." | INFO; publicity alone is not AC | **PASSED** | — |
| A05e | Hearing duty as in A05b; no hearing is ever held | AC arrangement still **legally constituted**; exercise is a separate level-C claim | **PASSED** | — |

### 2.2 I04 — external references (D05)

| ID | TOY case | Expected | First application | After patch |
|---|---|---|---|---|
| I04a | "Verifiers accredited under the applicable scheme"; scheme constituted in another instrument, not checked | I1 + external reference (`not_checked`, `outside_corpus_not_expanded`); constitution `undetermined` | **PASSED** | — |
| I04b | "…the accreditation body designated under Regulation Z"; Z located, authentic text verified, version matched | position type referenced; `legally_constituted` stated *citing Z*; **not** instantiated | **PASSED** | — |
| I04c | Reference to an external instrument that was repealed before the interval studied | `version_matched` fails → constitution `undetermined` for the interval | **PASSED** | — |
| I04d | "…tested in accordance with technical standard T" (a private standard incorporated by reference) | an external reference to a **non-legal normative source** | **FAILED** — the field is `referenced_legal_source`; a technical standard is not a legal source in the strict sense, so the record cannot be filled faithfully | **PT-6**: additive `source_kind` field (`legal_instrument · technical_standard · administrative_act · other_normative`); self-assessed PASS |
| I04e | A provision in the corpus slice refers to "the supervisory authority" constituted by another Article of the *same* instrument, outside the slice | external reference with `boundary_status: outside_corpus_not_expanded`; same-instrument references count | **PASSED** | — |
| I04f | The external instrument contains a relation relevant to the architecture | not imported silently; enters only by an `included_by_decision` boundary decision | **PASSED** | — |

### 2.3 M12, X03, X04, W05

| ID | TOY case | Expected | First application | After patch |
|---|---|---|---|---|
| M12a | A register extract records an entry dated *d* | claim "entry recorded on *d*": level C, limited to the act of recording; artifact keeps authenticity/provenance/date metadata | **PASSED** | — |
| M12b | The same extract also shows the register exists | second claim ("register exists"): level B; the two claims are evidenced separately | **PASSED** | — |
| M12c | An unverified screenshot of a register | no claim above `documented`; authenticity = unverified | **PASSED** | — |
| X03a | "Each Member State shall designate one or more competent authorities" | `position_type` + `legal_multiplicity: one or more`; **no instances created**; duty on States as R (PT-1 logic) | **PASSED** | — |
| X03b | A national act designates body *Y* in State A for 2024–2026, then replaces it | two `position_instance` records with jurisdiction and interval; State A's instance not applied to State B | **PASSED** | — |
| X03c | Claim: "decision-centre plurality is high" for a type-level, multi-jurisdiction architecture | not computable without instances; report as bounded by `legal_multiplicity` or `undetermined` | **FAILED** — rev2 gave type-level positions but did not forbid computing count-dependent properties from them | **PT-7**: count-dependent whole properties use evidenced instances or are bounded by `legal_multiplicity`, else `undetermined`; self-assessed PASS |
| X04a | Observed reporting routine with no legal basis | `ObservedArrangement`, level C, outside R and outside whole-level properties | **PASSED** | — |
| X04b | Practice (automatic approval) departs from a constituted review power | `ObservedArrangement` `deviates_from: R_id`; the constituted R is unchanged (cf. S12) | **PASSED** | — |
| W05a | Discretion high in enforcement prioritization, low in the standard | profile function × position × relation; no scalar | **PASSED** | — |

### 2.4 Re-run variants for X01, X02, L03, W02

| ID | TOY case | Expected | First application | After patch |
|---|---|---|---|---|
| X01b | "A Verification Authority is hereby established" vs "shall be established" | first: position constituted; second: mandate only | **PASSED** (limitation: translation cues) | — |
| X01c | "The Authority shall assess…" with no establishing text in the corpus | position referenced; constitution via external reference | **PASSED** | — |
| X02b | Practice shows the verifier recording results manually although the register is unbuilt | level-C evidence stands for the act; support gap reported; no gating | **PASSED** | — |
| L03a | A convention is recorded only in a judgment | `constituted_by: custom`, secondary inscription, outside first-round scope | **PASSED** | — |
| W02a | "V is a necessary stage" without closure statement | `undetermined` | **PASSED** | — |
| W02b | Closure declared over the corpus, but an unresolved external reference with a constitutive dependency touches the path | not asserted as necessity; "within the declared corpus only", references listed | **FAILED** — PT-4 as written accepted a closure declaration without regard to unresolved external references | **PT-8**: such claims are `undetermined` or scoped to the declared corpus, listing the references; self-assessed PASS |

## 3. Summary

| Set | Cases | Passed at first application | Failed at first application | Inconclusive |
|---|---|---|---|---|
| Ten original cases, re-run | 10 | 10 | 0 | 0 |
| Targeted variants | 26 | 23 | **3** (I04d, X03c, W02b) | 0 |
| **Total** | **36** | **33** | **3** | **0** |

The three failures were patched (PT-6, PT-7, PT-8); the post-patch passes are **self-assessed, not independent**. No case is inconclusive because the decisions supplied rules; that does not show the rules will be sufficient on real text.

## 4. Remaining limitations and open assumptions

1. **AR-1** — the minimum for accountability (duty + justification + questioning) is an assumption. A stricter reading requiring institutionalized assessment would reclassify A05b as INFO-plus.
2. **I2 threshold** (identity + operator/rules/bounded function) is untested on real devices.
3. **Verification of external sources** is manual and case by case; unresolved references reduce the force of absence-dependent claims.
4. **Bovens (2007)** is not stored locally; only V6's characterization is relied on (`[CITATION CHECK]`).
5. **Translated or consolidated texts:** drafting cues and authenticity must be checked on the authentic text (L02, X01b).
6. Coding guidelines for level-C claims and for cross-law comparison without scalar scores are deferred.
7. No independent reviewer has run any case.

## 5. Readiness for the GDPR Articles 42–43 microcase

**No unresolved defect prevents beginning it.** Recommendation: **proceed**, treating the items below as *protocol requirements of the demonstration*, not as a new conceptual cycle:

1. Fix the corpus boundary (Articles 42–43) and the text version from the **authentic** published text, not a consolidated copy.
2. Keep an **external-reference register** from the first pass (positions, devices and standards referred to but constituted elsewhere — to be identified from the text, not assumed here), each with `boundary_status` and verification status.
3. Represent national bodies at **type level** with `legal_multiplicity`; create no instances.
4. Apply the **INFO / AC / IND** test to every reporting, supervision or review element, and record AR-1 as an explicit assumption.
5. Declare a **closure/coverage statement** before any absence-dependent claim.
6. Report **status profiles** (documented / legally constituted / instantiated / observed), expecting most elements to stop at legally constituted.
7. Do not claim effectiveness or operation from the legal text.

---

## Addendum (2026-10-03, after the third-round decisions) — not a re-run

Decision D10 refined the accountability classes (INFO / ANSWERABILITY / AC / IND). Stress testing was stopped by instruction, so no case was re-run. Expected effects, by inspection: **A05b** → ANSWERABILITY (assessment capacity and grounded consequences absent); **A05e** → an ANSWERABILITY arrangement legally constituted, exercise separate; A05a, A05c, A05d and all other cases unchanged. The tables above are left as originally recorded.
