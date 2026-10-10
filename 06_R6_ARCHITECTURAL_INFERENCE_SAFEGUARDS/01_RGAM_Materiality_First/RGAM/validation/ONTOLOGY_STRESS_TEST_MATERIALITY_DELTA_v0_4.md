# Ontology stress test — materiality delta and targeted tests (v0.4 rev1)

**Date:** 2026-10-03 · **Status:** `SELF_TEST` — single evaluator, not blind, run by the agent that wrote the rules. **Not a validation.**
**Object tested:** `ontology/ONTOLOGY_v0_4.md` **rev1** (decisions D01–D03 applied; *before* the post-test patches PT-1…PT-5 listed in §4).
**Historical tests:** the 16 hypotheticals S01–S16 in `historical_audit_copy/ONTOLOGY_STRESS_TEST.md` are untouched and are cited only by ID. They extend, not replace.
**All cases are invented:** `TOY / NOT REAL LEGAL EVIDENCE`. David's forwarded analytical documents (`source_context/david_forwarded/`) were **not present** in the repository; no case relies on them.

## 1. Protocol

For each case the rev1 rules were applied as written and compared with an *expected* classification taken from V6 (§§4.3, 6.7, 6.8, 6.13) and the v0.3 criteria.
- **PASSED** — the rules yield a determinate classification equal to the expected one and block the prohibited inference.
- **FAILED** — the rules yield a wrong classification, no classification, or permit a prohibited inference.
- **INCONCLUSIVE** — the rules underdetermine the outcome; adjudication or additional rules/evidence are needed.

**Caveat.** Many cases were designed after the D01–D03 rules were drafted, so PASSED results carry **low evidential weight**. The informative output is the FAILED and INCONCLUSIVE sets.

## 2. Results at a glance

| Result | Count | Cases |
|---|---|---|
| **PASSED** | 28 | M01–M11, I01–I03, I05, A01–A04, A06–A08, L01–L02, W01, W03, W04, W06 |
| **FAILED** | 4 | X01, X02, L03, W02 |
| **INCONCLUSIVE** | 7 | M12, I04, A05, A09, X03, X04, W05 |
| **Total** | 39 | |

## 3. Cases

### 3.1 Materiality delta (the twelve planned cases)

| ID | TOY case | Expected | Rule applied | Result | Defect exposed / note |
|---|---|---|---|---|---|
| M01 | Academic diagram of a regulator with no legal or institutional referent | `conceptually_projected`; not an empirical reconstruction | §4 statuses | **PASSED** | — |
| M02 | Draft statute proposes an authority; never enters into force | `documented`; not `legally_constituted` | §4 | **PASSED** | — |
| M03 | Enacted statute says "An Authority is hereby established"; no independent evidence it exists | position `legally_constituted`, not `materially_instantiated` | §3.2, §4 | **PASSED** | Contrast with X01 (mandate to establish) |
| M04 | Statute mandates a national reporting platform; none built | Device (I2) `legally_constituted`; not instantiated | §3.2 I2/I3 | **PASSED** | — |
| M05 | A register site is live; no evidence of entries or use | Device I3 `materially_instantiated`; use not observed | §3.2 I3; §4 | **PASSED** | — |
| M06 | Instrument is publicly accessible as a PDF | `documented` (and `legally_constituted` only with legal-status evidence); no claim of instantiation | §4 | **PASSED** | — |
| M07 | Two laws, same positions and functions, different relations | different architectures; difference located in R and positional properties | §6.2 | **PASSED** | Absence-dependent positional claims: see W02 |
| M08 | A platform appears as interface | Device (not a position; not an actor) | §3.2 | **PASSED** | — |
| M09 | A rule is conditional/expired, or expressly prohibits a relation | `status: conditional`/prohibited; validity interval ends | §3.3 | **PASSED** | — |
| M10 | A network drawing contains an edge with no source | rejected; projection is not evidence | §3.3 Include/Exclude; §3.2 projections | **PASSED** | — |
| M11 | A legally constituted relation vs independently observed practice | separate claims: `legally_constituted` vs `operationally_observed` | §4 | **PASSED** | Practice *without* legal basis: X04 |
| M12 | Material evidence about law vs material mediation of an actual interaction | A-level text of the law vs C-level trace of the interaction | v0.3 levels | **INCONCLUSIVE** | A register extract or certificate is an A-level inscription *and* may trace an act (C). rev1 does not say that the level attaches to the **claim**, not the artifact |

### 3.2 Instrument representations (D01)

| ID | TOY case | Expected | Result | Note |
|---|---|---|---|---|
| I01 | "The Authority may grant a licence" | I1: typed characteristic of an authority/authorization R | **PASSED** | No new entity |
| I02 | "A register of certified verifiers shall be kept by the Authority; Art. 9 governs entry and removal" | I2: Device (identity + operator + rules); not a node in PR-A | **PASSED** | — |
| I03 | The same register, with an accessible live site (level-B evidence) | I3: Device `materially_instantiated` | **PASSED** | Use of the register remains a C-level claim |
| I04 | "Verifiers accredited under the applicable scheme" — scheme rules in an instrument outside the corpus | I1 + flag *external reference*; no promotion to I2 on this corpus | **INCONCLUSIVE** | Promotion rule needs (a)+(b) "from the source"; how out-of-corpus constitution is handled is a regime-boundary decision (V6 §6.7) left open. Relevant to later real-law work |
| I05 | A certificate issued by a verifier | Artifact (output); the scheme is the Device; "certification" is I1 on the verification R | **PASSED** | — |

### 3.3 Accountability and reporting (D02)

| ID | TOY case | Expected | Result | Note |
|---|---|---|---|---|
| A01 | "The Agency shall report annually." (no recipient) | obligation; **no R**; not accountability | **PASSED** | §3.3 counterexample |
| A02 | "…report annually to the Parliament." | information relation; AC *candidate*, not AC | **PASSED** | element 5 absent |
| A03 | "…report annually to the Parliament, which may summon the Agency's head to explain and may adopt a censure" | AC relation; consequence recorded with its own provenance | **PASSED** | — |
| A04 | "The Authority supervises the Verifier and may inspect and sanction it" | oversight R; **not** AC | **PASSED** | element 4 (duty to inform/justify) absent |
| A05 | "The Board is accountable to the public" | uncertain: diffuse forum | **INCONCLUSIVE** | rev1 says a forum is a position with legal capacity "unless a procedure gives it standing"; what counts as such a procedure (complaint right? publication? consultation?) is unspecified. Under rev1 it is classed as *incomplete*; the accountability literature may treat transparency-based forums differently |
| A06 | "Verifiers' decisions are reviewable by the Appeals Board" and "the Authority answers to Parliament for the verification system as a whole" | AC pointers target an R *and* an S | **PASSED** | `qualifies: R_x | S_y` |
| A07 | One provision gives both supervision and a duty to explain to the supervisor | two R objects; AC `qualifies` → supervision; no duplicate observation | **PASSED** | — |
| A08 | AC relation in the statute; its "publicity" asserted only in a guidance note outside the corpus | publicity not inherited; needs its own provenance | **PASSED** | — |
| A09 | "The Agency is accountable for its decisions." (no forum, no duty) | record as unparsed assertion; no R | **INCONCLUSIVE** | The classification table has no row for missing element 4 *and* 3; outcome obvious, rule absent (minor) |

### 3.4 Incomplete legal relationships and instantiation

| ID | TOY case | Expected | Result | Note |
|---|---|---|---|---|
| X01 | "A Verification Authority shall be established by the Minister within twelve months." | a duty (Minister → establish) is `legally_constituted`; the **Authority position is not yet constituted** (`documented`/planned) | **FAILED** | rev1 defines a Position as one the text "constitutes, recognizes or designates" and has no *mandate-to-constitute* rule; applying it as written would label the Authority `legally_constituted` |
| X02 | A verifier's duty to record each result in a national register; the register is unbuilt | R `legally_constituted`; **support gap** visible (depends on an uninstantiated Device) | **FAILED** | rev1 attaches statuses "per element" including R, but gives no criterion for `materially_instantiated` of a *relation*, and no way to state a support dependency. D03's substantive concern (what carries a constituted relation) cannot be expressed |
| X03 | "The competent authority" is a category filled differently by each Member State | category-level Position at the corpus level; instances per jurisdiction | **INCONCLUSIVE** | rev1 lists "actor category" as a position type but has no category-to-instance rule; matters for multi-jurisdiction corpora |
| X04 | Observed practice creates a reporting routine with no legal basis | recorded in layer X as an *observed arrangement*, not as an R | **INCONCLUSIVE** | rev1 defines R as legally constituted and leaves operational-only relations unrepresented |

### 3.5 Legal status (inscription vs constitution, D03)

| ID | TOY case | Expected | Result | Note |
|---|---|---|---|---|
| L01 | A statute repealed on a stated date | `documented`; `legally_constituted` only for the interval before repeal | **PASSED** | per-interval statuses |
| L02 | An unofficial consolidated text, with a disclaimer of legal effect | `documented`; not `legally_constituted` until the authentic text is identified | **PASSED** | Relevant to later real-law work: consolidated versions are not themselves the authentic text |
| L03 | A norm constituted by custom/convention; no enacted text | legal constitution without an enacted inscription; flagged out of first-round scope | **FAILED** | rev1 defines legal constitution as a property *of an inscription*, which couples the two notions D03 asks us to separate and excludes a real class of constitution |

### 3.6 Part-level vs whole-level properties

| ID | TOY case | Expected | Result | Note |
|---|---|---|---|---|
| W01 | α/β (§6.2): "V verifies F" identical in both | part-level coding cannot distinguish; positional/relational properties do | **PASSED** | — |
| W02 | "V is a necessary stage" asserted from a partly coded corpus; an unseen provision may give X a direct line to F | `undetermined` unless corpus closure/coverage is declared | **FAILED** | rev1 says "not found" is a statement about the search but does not forbid absence-dependent positional claims (necessity, substitutability, exclusivity) without a closure declaration — the guard against over-claiming is missing |
| W03 | Monitoring routed through accredited third parties; enforcement entirely public | property stated **per function**; no whole-architecture label "intermediated" | **PASSED** | §6.1 per-function bearer; ecological fallacy blocked |
| W04 | A single self-assessment duty; claim "self-regulatory architecture" | rejected; pattern rule and stopping rule not met | **PASSED** | atomistic fallacy blocked |
| W05 | Discretion high in enforcement prioritization, low in the substantive standard; aggregate "discretion distribution" at A | profile by function | **INCONCLUSIVE** | §6.1 gives the bearer (A, from R) but no per-function aggregation rule |
| W06 | Ten reporting provisions vs one pre-market certification gate | composition counted; significance claimed only with evidence on authority, sequence, consequence, substitutability… | **PASSED** | counts ≠ significance |

## 4. Post-test patches applied to the ontology (marked `[PT]` there)

| Patch | Addresses | Content | Status |
|---|---|---|---|
| **PT-1** | X01 | *Constitution by mandate*: a provision commanding that a position be established creates an obligation R; the position's status follows the constituting act itself | patched; **re-test = self-assessed PASS, not independent** |
| **PT-2** | X02 | Instantiation applies to **Positions and Devices** only. R carries `depends_on` (positions/devices) and a **support-gap report**; R's own statuses are `projected / documented / legally_constituted / operationally_observed`. Dependencies are expectations, never a gate: if practice is observed without the device, the C-level evidence stands and the gap is reported | patched; self-assessed PASS |
| **PT-3** | L03 | Legal constitution is a property of a **norm or arrangement**, usually evidenced by inscriptions. Custom/convention is recorded `constituted_by: custom`, evidenced only through secondary inscriptions, outside the first-round scope | patched; self-assessed PASS |
| **PT-4** | W02 | **Absence-dependent properties** (necessity, substitutability, exclusivity) require a declared closure/coverage statement for the corpus; otherwise `undetermined` | patched; self-assessed PASS |
| **PT-5** | A09 | Default row: missing elements → *incomplete*; the statement is kept as an unparsed assertion | patched (trivial) |

**Not patched (left OPEN, need adjudication):** M12 (candidate rule: the level attaches to the *claim supported*, not to the artifact), I04, A05, X03, X04, W05.

## 5. Strongest objection to "architecture presupposes materiality" and the answer

*Objection:* institutional reality is not a pile of paper or hardware; requiring material referents risks reducing legal-institutional facts to documents (formalism, physicalism). *Answer (D03):* materiality here is the dependence of a constituted relation on its carriers — inscriptions and institutional devices — and a constraint on the **warrant** of a reconstruction; existence is not reduced to observability, and unwritten or undocumented arrangements are not denied (L03 shows the first draft got this wrong and PT-3 corrects it). The residual risk, that "material" will still be read as "documentary", stays open (decision log D03).

## 6. What these tests do not show

They do not validate the ontology, do not test it on real legal text, do not test inter-coder reliability, and do not show that the minimum viable ontology is sufficient for the GDPR demonstration (not started). The next informative test is an independent reviewer (David, Rotem, or a second coder) running a subset of these cases blind.
