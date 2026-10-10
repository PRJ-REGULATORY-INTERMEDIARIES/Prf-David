# RGAM — Candidate morphological-relational ontology, v0.4

**Date:** 2026-10-03 · **Revision:** rev3 — decisions D01–D03, D04–D09, regression patches PT-6…PT-8 (approved as provisional) and D10 (AR-1 refined) (see `DECISION_LOG.md`); changes listed in the revision log at the end · **Status:** `CANDIDATE_CONCEPTUAL_ONTOLOGY` — a proposal for discussion. **Not** an approved OWL ontology, not a production codebook, not validated. Every example marked TOY is invented: `TOY / NOT REAL LEGAL EVIDENCE`.
**Builds on:** David Levi-Faur, V6 (definition, three levels, ladder, stopping rule preserved) · `theory/DAVID_TO_ARCHITECTURAL_ONTOLOGY_CROSSWALK.md` · `theory/THEORETICAL_SELECTION_MATRIX_v0_4.md` · `theory/MATERIALITY_CRITICAL_REALISM_NOTE_v0_4.md`.
**Research question:** How can a materially anchored and configurational ontology extend David Levi-Faur's relational leximetrics framework, enabling empirically verifiable reconstruction of regulatory governance architecture while distinguishing properties of constituent parts from those of the architectural whole?

## 1. Definition

**David's definition (V6 §5.2, preserved):** a governance architecture is the legally constituted configuration through which governance work, authority, discretion and accountability are distributed among actors and organized through relationships, mechanisms and instruments.

**RGAM specification (our proposal):**

> A **regulatory governance architecture** is a *bounded*, *temporally indexed* configuration of legally constituted **positions** and **qualified relations** (with the **instruments** that constitute their interfaces) through which governance work, authority, discretion and accountability are distributed. Its properties arise from the **arrangement** of the relations rather than from an inventory of its parts. It is reconstructed from **material inscriptions**, and its formal legal constitution, institutional instantiation and enacted operation are analytically distinct.

**PT-BR:** *Uma arquitetura de governança regulatória é uma configuração delimitada e temporalmente situada de **posições** juridicamente constituídas e **relações qualificadas** (com os **instrumentos** que formam suas interfaces), por meio da qual se distribuem trabalho de governança, autoridade, discricionariedade e accountability. Suas propriedades decorrem do **arranjo** das relações, e não de um inventário de partes. É reconstruída a partir de **inscrições materiais**, e sua constituição jurídica formal, sua instanciação institucional e sua operação efetiva são analiticamente distintas.*

What the specification adds to David's definition: (i) **bounded and time-indexed** (V6 already demands scope, §5.2.3); (ii) **parts vs whole** stated as a rule; (iii) **material anchoring** and the three-way separation. It removes nothing.

## 2. Strata

| Stratum | Content | Role | V6 anchor |
|---|---|---|---|
| **E** Evidence | source, version/date/status, provision, institutional statement, provenance | Inscriptions from which everything else is derived. A source is **not** an actor. | ladder levels 1–2 |
| **P** Parts | **Position** (organization / legally specified office / actor category — three distinct types; an office is not its holder); **Institutional device** (a distinct type, *not* a position; §3.2) | Positions are the nodes of the actor-position projection; devices are not | Actors, Instruments |
| **R** Qualified relations | reified relation with type, parties/roles, direction (if defensible), modality, condition, validity interval, object, function(s), mechanism(s), authority, discretion, accountability profile, status, provenance | The pivotal bridge | Relationships; Level II attributes |
| **S** Subconfigurations | theoretically specified sets of R (+P): local arrangements, overlapping or nested, function- or stage-specific | Local structure; where named patterns are matched | §5.2.3, ladder level 4 |
| **A** Whole | the architecture of an explicitly bounded corpus (§5) | Whole-level properties | ladder level 5 (6 with regime boundary) |
| **M** Material anchoring (**transversal**, not a tier) | for any E/P/R/S/A element: referent, evidence type, level A/B/C, limitation, status | Warrant | RGAM proposal; echoes V6 §6.9, §6.13 |
| **X** Adjacent layers | strategy annotation, governance logics, implemented/operational architecture, genesis/aims, sociomaterial enactment, outcomes | Available, not constitutive of morphology | Strategies, Logics, §6.13 |

### 2.1 What is **not** a node

Objects, functions, mechanisms, authority, discretion and accountability are **qualifiers or attributes of relations**; strategies are **annotations**; logics sit in X. Turning each V6 category into a node would (a) make an actor, a verb and a concept equivalent vertices, and (b) lose V6's own point that relations are typed rather than generic. In the **actor-position projection** the nodes are positions only; devices appear as interfaces on edges. Other projections (§3.2) may treat devices as nodes. A graph is an analytical projection of the ontology, not the ontology.

## 3. Entity classes

For each class: definition · inclusion/exclusion · identifying evidence · material anchoring · scale · adjacent classes · one non-trivial counterexample (TOY).

### 3.1 Position (P)
- **Definition:** a legally specified place in at least one qualified relation: an organization, an office, or an actor category.
- **Include:** entities the text constitutes, recognizes or designates. **[PT-1] Constitution by mandate:** a provision commanding that a position be established ("shall be established by…") creates an obligation relation (e.g. Minister → establish); the position itself takes its status from the constituting act, and until that act is itself legally constituted it is `documented`/planned, not `legally_constituted`. **Exclude:** a source document; a named holder; a platform (see 3.2); a mere mention without a relation.
- **[R2] Position model (D08).** Four things are kept apart: **`position_type`** (a generic legal category, e.g. "national competent authority"), **`position_instance`** (a specific institution or office), **`jurisdiction`**, and **`temporal_reference`** (interval). Relations may be stated at *type* level. An instance is recorded only with **its own source** (e.g. a national designating act), with jurisdiction and interval; **no instance is ever inferred from a generic category**. Each type carries `legal_multiplicity` where the text states one (exactly one / one or more / unspecified). **[PT-7]** A whole-level property that depends on counts (decision-centre plurality, centralization) is computed only from *evidenced instances* or reported as bounded by `legal_multiplicity`; at type level otherwise it is `undetermined`, never an invented number.
- **Evidence / anchoring:** (A) text constituting the position; (B) independent evidence that it is filled/established — never inferred from the mandate.
- **Scale:** part. Properties: *intrinsic* (what the text confers on it), *positional* (depends on the whole; §6).
- **Adjacent:** Role is relation-relative (V6 §1, §3.2). Position ≠ role ≠ holder.
- **Counterexample (TOY):** a statute names "the Verifier" in a recital only; no provision gives it any power or duty. It is **not** a position of the architecture (a mention without a relation).

### 3.2 Instruments, devices, artifacts and positions — three situations (D01)

**Four kinds kept apart:** **Position** (legal place in relations) · **Instrument** (a typed *category* of governing tool, e.g. licence, audit, register) · **Institutional device** (a juridically constituted entity with its own boundary and rules: a register, a certification or accreditation scheme, a reporting platform) · **Documentary artifact** (an inscription-bearing object: statute text, a certificate, a published report, a register extract; evidence in E by default, or an *output* of a device).

**Three analytical situations:**

| | Situation | Condition | New entity? | Status it can reach |
|---|---|---|---|---|
| **I1** | Instrument as a **typed characteristic of a relation** | The source of R names the tool | No | that of R |
| **I2** | **Device as a juridically constituted entity** | The source gives it (a) *identity* — it can be singled out — and (b) an *operator*, *governing rules*, or a legally specified function with a boundary. Promotion I1→I2 needs a recorded source-based reason | Yes (type Device, in P) | `legally_constituted` (never beyond, on legal text alone) |
| **I3** | **Materially instantiated device** | Evidence *beyond the legal prescription* (level B) that the device exists as an operating entity — platform live, register accessible, scheme operator active — with its own provenance | No (a status of the I2 entity) | `materially_instantiated`; *use* is a separate level-C claim |

**Rules.** I2 does not imply I3. A device is never an actor/position. An artifact is not a device (a certificate is an output; the certification scheme is the device). A visualisation without legal effect is neither (S11). Not every entity becomes a node of the actor-position graph.

**Projections** (each declares what it omits; none is legal evidence): **PR-A** actor-position graph — nodes = positions, edges = R, devices as edge interfaces; **PR-D** device-mediated graph — positions and devices as nodes; **PR-E** evidence graph — E items linked to R/P/Device.

**Open (V6-02):** whether the (a)+(b) threshold is adequate.

### 3.3 Qualified relation (R)
- **Definition:** a legally constituted connection among two or more positions, reified so it can carry qualifiers and provenance.
- **Fields (minimum):** `type` (V6's ten: authority/control, delegation/authorization, oversight/supervision, accountability, information/reporting, verification/assurance, review/adjudication, representation/participation, contractual/exchange, beneficiary/protective) · `parties` with roles (n-ary allowed) · `direction` · `modality` (obligation, permission, power, prohibition) · `condition` · `validity` (from/to, version) · `object` · `function(s)` · `mechanism(s)` · `instrument` (I1 characteristic, or reference to a Device) · `authority`, `discretion` · `accountable_via` (pointers, §3.3.1) · `depends_on` · `external_ref` (§3.7) · `status` ∈ {established, conditional, expressly prohibited} · `derivation` ∈ {direct, derived from provisions P1…Pn} · `provenance`; and **M**: level, evidence, claim status.
- **Absence:** "not found" is a statement about the *search*, recorded on the corpus, not a relation. Silence is neither permission nor prohibition (S06, S10).
- **Include:** relations the text supports directly or derives by a stated rule. **Exclude:** relations inferred from the *presence* of two actors, from a network drawing, or from an obligation on one party alone.
- **Counterexample (TOY):** "Firms shall submit annual reports." There is an obligation and an information function, but **no R** to a named receiving position until some provision designates a recipient (V6 §6.7, step 2).

### 3.3.1 Accountability (D02, refined by D04)

Accountability occurs in two roles, linked **by reference, not by duplication**:
- **AC relation** — a qualified relation of type *accountability*: one R object.
- **`accountable_via`** on another R or on an S — a *pointer* (`qualifies: R_x | S_y`) to the AC relation(s) that qualify it. It is a view of the pointer and is never coded separately.

**Elements, each with its own source span:** (1) legal source; (2) responsible actor (account-giver position); (3) **forum** — a position, **or a distributed/public forum** (the public, affected persons, stakeholders) *whose relevant capacities are institutionally identifiable* (a defined category plus an institutional channel); (4) a **duty of explanation and justification**; (5) the forum's institutionalized **questioning capacity**; (6) the forum's institutionalized **assessment/judgment capacity** (any institutionalized evaluative capacity: judgment, review, complaint to a body, binding referral); (7) a **grounded possibility of consequences** (provided for in the legal source, not merely hoped for). Further attributes — publicity, periodicity, remedy — need their own provenance and are never inherited. Bovens (2007) is the reference for the actor–forum conception: bibliographic record and abstract verified (actor–forum relationship in which the actor has an obligation to explain and justify its conduct); the detailed conditions (forum questions and passes judgment; consequences may follow) are taken from V6 §4.3's characterization — **`[CITATION CHECK]` against the full text**.

**Four classes (D10, refining D04):**

| Class | Evidence | Treatment |
|---|---|---|
| **INFO** — information / disclosure / reporting | information to a position or to the public; publicity; periodic reports; no duty to justify | information relation; **never** AC or ANSWERABILITY; publicity alone is never accountability |
| **ANSWERABILITY** — answerability without all accountability elements | an identifiable actor–forum relationship with a duty of explanation and justification **and** questioning capacity (elements 1–5), but assessment/judgment capacity or a grounded possibility of consequences is absent or not evidenced | one R of type accountability, flagged `answerability_only`, with the missing elements listed |
| **AC** — sufficiently established accountability | all of elements 1–7 institutionally identifiable in the corpus | one AC relation |
| **IND** — indeterminate | an assertion of accountability whose elements cannot be established from the corpus (no forum, no duty, no channel, ambiguous text, or evidence insufficient) | record the assertion and the **missing elements**; no AC; may be resolved by other provisions or external references |

**Distributed public forums are admissible** in ANSWERABILITY or AC when their relevant capacities are institutionally identifiable (e.g., a hearing where any person may put questions and the body must answer in writing: ANSWERABILITY; add a body empowered to assess the answers with provided consequences: AC). **No inference of operation:** that capacities are legally constituted does not show that the arrangement operates; whether it is exercised is a separate level-C claim. *Assumption AR-1 is closed by D10.*

**Other rules.** Supervision/oversight alone is not AC: it may supply the forum's assessment capacity, but the duty (4) must also be present, and then `derivation: derived`. **Exercise is not required:** a legally constituted accountability arrangement is shown by its constituting provisions; whether it is exercised is a separate level-C claim. One provision yielding supervision *and* answerability gives two R objects; the AC `qualifies` the supervision R. Absence of a recipient (no forum at all, no duty) → IND, or no R where there is only a bare obligation (A01).

### 3.4 Subconfiguration (S)
- **Definition:** a set of relations (and their positions) that satisfies a stated pattern rule — e.g., a verification chain, a delegation triangle, an accountability loop. May overlap or nest. Always scoped (function, stage, subsystem).
- **Named patterns** (V6 §5.2.2: hierarchical, delegated, self-regulation, enforced self-regulation, meta-regulation, enhanced self-regulation, accreditation/assurance, networked, polycentric, multilevel) are **patterns matched to S**, each with its own inference rule (V6 §6.7), not labels for whole laws.
- **Counterexample (TOY):** a single reporting relation does not constitute a reporting *system* where nothing receives, assesses or follows up (V6 §6.7, step 3).

### 3.5 Whole architecture (A)
- **Definition:** the architecture of a **bounded** set: *corpus/instruments × jurisdiction × domain × interval × version × boundary rule*. No default boundary: a statute is not automatically one architecture (container fallacy, V6 §6.8).
- **Output:** a **profile** of whole-level properties (§6) plus a **status profile** (§4) — never one score, never one label.
- **Counterexample (TOY):** a long statute combining direct licensing for one product and accredited verification for another contains two S patterns; "the architecture of the statute" is not defined until the subsystem is stated.

### 3.6 Evidence (E), artifacts and evidentiary anchoring (M) — D06

- **Artifacts keep their own metadata:** authenticity (verified / unverified / disputed), provenance, and temporal data (issued, valid from/to, version, retrieval date).
- **Evidence status belongs to the individual scientific claim, not to the artifact.** An **evidence link** is a record `(claim, artifact(s), level A/B/C, support: direct | indirect, limitation)`. The same artifact may support different claims at different levels: a register extract supports "the instrument exists" (B), "an entry was recorded on date d" (C, limited to the act of recording, not its accuracy or effect), and "the text created the register" (not at all). An artifact with unverified authenticity cannot raise the status of any claim above `documented`.

### 3.7 External architectural references (D05)

Legally relevant positions, devices, standards or duties may be constituted **outside the immediate corpus boundary** — in another instrument, in another part of the same instrument, or in a non-legal normative document incorporated by reference. They are represented by a typed **external reference** and are **not** automatically imported into the corpus.

| Field | Content |
|---|---|
| `external_reference_id` | stable identifier; links to the provision span that makes the reference (traceability) |
| `referenced_legal_source` | the instrument/provision referred to, with version/date as far as stated |
| `source_kind` **[PT-6, additive]** | `legal_instrument` · `technical_standard` · `administrative_act` · `other_normative` — a technical standard is not a legal source in the strict sense |
| `reference_role` | `constitutes_position` · `constitutes_device` · `designates_competence` · `supplies_rule/standard` · `defines_term` · `other` |
| `source_verification_status` | `not_checked` · `located` · `authentic_text_verified` · `version_matched` · `unavailable` |
| `boundary_status` | `outside_corpus_not_expanded` · `outside_corpus_pending_decision` · `included_by_decision` |
| `constitutive_dependency` | which element (R/Position/Device/I1) depends on the reference, and how: `constitutes` · `qualifies` · `conditions` · `specifies` |

**Rules.** (1) A reference shows **legal relevance only**: it never demonstrates instantiation or operation. (2) The dependent element's `legally_constituted` claim is `undetermined` until the external source reaches `authentic_text_verified` **and** `version_matched`; then it is stated *citing the external source*. (3) No silent import: relations contained in the external source do not enter the architecture unless a boundary decision (`included_by_decision`) is recorded in the declaration of A. (4) **[PT-8]** An absence-dependent property (§6) whose path touches an unresolved external reference with a constitutive dependency is `undetermined`, or is stated as "within the declared corpus only", listing the unresolved references.

### 3.8 Observed arrangements — adjacent layer (D07)

Operational-only relationships (practice without legal basis, or practice that departs from a constituted relation) are **outside the primary scope** of the legally constituted architecture. They may be recorded in an explicitly separate adjacent layer as **`ObservedArrangement`** objects: `parties`, `description`, `evidence` (level C, with limitation), optional `relates_to: R_id` (`supplements | deviates_from`), and `provenance`. They are never R objects, never enter whole-level properties of the legal architecture, and any comparison between formal and operational architecture is stated explicitly (V6 §6.13). A practice grounded in a *documented but non-binding* text keeps that text as `documented`; it does not become legally constituted by being practiced.

## 4. Materiality — substantive concern, four distinctions (D03)

**Why not provenance alone.** Provenance says where a datum came from. Materiality, as used here, concerns how a legally constituted architecture **finds expression and support** through identifiable **inscriptions** (texts, register entries, certificates) and **institutional devices** (offices, registers, platforms, procedures, infrastructures) — i.e. what carries the constituted relation so that it can exist as law, be exercised, and be shown. Provenance is necessary for every claim; it is not what materiality is.

| Distinction | Asserts | Evidence |
|---|---|---|
| **Documentary inscription** | an authentic, versioned document or trace exists — *even if* draft, repealed or non-binding | level A |
| **Legal constitution** | the inscription has legal effect for the stated version and interval (enacted, in force, applicable) | A + legal-status evidence (publication, entry into force, repeal) |
| **Material instantiation** | the constituted position or device exists as an established, functioning entity | level B, independent of the mandate |
| **Observed operation** | practice is observed (use, compliance, appropriation) | level C — an adjacent layer (X) |

**Claim statuses:** `conceptually_projected` · `documented` · `legally_constituted` · `materially_instantiated` · `operationally_observed`. Each is independently evidenced; none is inferred from another; they are **not** a life cycle (a practice may precede a formal basis; a norm may lapse). Statuses attach **per element** and per interval; the whole receives a **status profile** (e.g. "11 relations legally constituted; 2 materially instantiated; 0 observed"). A draft bill is *documented*, not legally constituted; a mandated unbuilt platform is *legally constituted* (as a device), not instantiated; an accessible PDF proves documentation only. The Phase-1 status `normatively_inscribed/formally_constituted` is split into `documented` and `legally_constituted`.

**Materiality and evidentiary anchoring (D09).** *Materiality* is the substantive theoretical concept: how legally constituted architectures find expression and support in inscriptions and institutional devices. *Evidentiary anchoring* (stratum M, §3.6) is its **methodological counterpart**: the records through which claims about those dependencies are supported. They are not synonyms.

**[PT-2] Which element can bear which status.** `materially_instantiated` applies to **Positions and Devices** only. A relation has no body: its own statuses are `conceptually_projected`, `documented`, `legally_constituted` and `operationally_observed`. A relation carries `depends_on` (the positions and devices through which it exists or is exercised) and a **support-gap report** (e.g. "verifier → register: legally constituted; depends on Device *national register*: not instantiated"). Dependencies are expectations, never gates: if practice is observed without the device, the level-C evidence stands and the gap is reported. This is where materiality bears on relations substantively, beyond provenance.

**[PT-3] Legal constitution is a property of a norm or arrangement**, usually evidenced by inscriptions — not a property of the inscription. Constitution by custom or convention is recorded `constituted_by: custom`, evidenced only through secondary inscriptions (judgments, official statements); it is **outside the first-round scope** (reconstruction from enacted text).

**Ontological point retained (critical realism).** Existence is not reduced to observability: an operating arrangement may exist undocumented. Materiality governs the **warrant** of a reconstruction and the dependence of constituted relations on their carriers; sociomateriality remains a complementary lens on enacted practice (layer X). Implementation is not the principal object.

## 5. Boundary rules

1. Every A declares: instrument set, jurisdiction, domain, interval, text version, and the rule that fixes membership. It also lists its **external references** with their `boundary_status` (§3.7) and, for absence-dependent claims, its closure/coverage statement.
2. Moving from one law to a regime requires an explicit boundary decision (V6 §6.7, final rule).
3. Architectural claims state scope: whole law, subsystem, function or stage (V6 §5.2.3).
4. **Out of scope of the constitutive core:** effectiveness, compliance, outcomes, sociomaterial enactment — available in X.
5. **Stopping rule (V6 §6.10):** assert only the highest level the evidence warrants; stop at relation or configuration where evidence stops.

## 6. Part/whole properties — the bearer table

Four kinds of property, never interchanged without an explicit rule:

| Kind | Bearer | Defined from | Examples (V6 terms) |
|---|---|---|---|
| **Intrinsic** | P | what the text confers on the position | powers held; functions assigned |
| **Relational** | R | the relation's own qualifiers | type, direction, authority, discretion, accountability profile |
| **Positional** | P *within* S/A | its relations to the others (depends on the whole) | structural position, being a necessary stage, depth from the rule-maker, substitutability, centrality |
| **Emergent/whole** | S, A | arrangement of R across P | distribution and structure properties below |

**[PT-4] Absence-dependent properties** (necessity of a stage, substitutability, exclusivity, "no alternative path") may be asserted only with a declared **closure/coverage statement** for the corpus (which provisions and instruments were searched, and how); otherwise the property is `undetermined`.

**Guards:** atomistic fallacy (do not lift a part property to the whole); ecological fallacy (do not push a whole property down to every part) — V6 §6.8.

### 6.1 V6's ten architectural dimensions: bearer and RGAM family

Five **property families** (from v0.3, kept): F1 composition/distribution · F2 typed relational configuration · F3 authority stratification/distribution · F4 integration/segmentation · F5 interface/boundary permeability. They are **families, not validated metrics, and no composite score**. The mapping below is **an RGAM proposal**; some dimensions straddle families.

| V6 dimension (§5.2.1) | Bearer | Computed from | Family |
|---|---|---|---|
| Centralization | A | authority attributes over R across P | F3 |
| Directness and intermediation | S (per function) → A | paths routed through third-party positions | F2 |
| Public–private allocation | A | function allocation by actor sector | F1 |
| Self-regulatory autonomy | S/A (per function) | allocation of formulate/administer/enforce to regulated positions | F5 (public–private boundary) |
| Vertical distribution | A | jurisdictional level of positions | F3 |
| Decision-centre plurality | A | number of partly autonomous centres with decision capacity | F3 |
| Relational depth | S → A | stages between rule-making and implementation | F2 |
| Functional allocation | A (per function S) | location of rule-making/monitoring/verification/enforcement | F1 |
| Discretion distribution | A | **profile**: discretion by function × position × qualified relation, each value with provenance — **no aggregate score** (D09-W05) | F3 |
| Accountability structure | A | forums and closure of accountability relations | F4 |

**No dimension is reduced to a scalar score** unless a later, separately justified rule is adopted (V6 §6.6 itself declines a composite).

V6 §6.11 lists a separate set of twelve candidate measures (e.g., accountability closure, redundancy, reciprocity, monitoring density, enforcement concentration); the two lists are not yet harmonised — a decision for David (register V6-13, new).

### 6.2 Same inventory, different configuration — the discriminating test
`TOY / NOT REAL LEGAL EVIDENCE.` Positions: Authority **X**, Verifier **V**, Firm **F**; same functions in both.
- **Law α:** X accredits V; V verifies F; F reports to X; X may sanction F and V.
- **Law β:** V verifies F; F reports to V; V informs X only in aggregate; X may sanction F only on V's referral; X has no power over V.
Identical inventory; different relations. Positional properties diverge: in β, V is a *necessary stage* (gatekeeper) and X has no direct line to F; in α X has both a direct and a supervisory path. **A part-level reading of "V verifies F" is identical in both laws and cannot distinguish them**, which is exactly why architecture is not inferable from the part. (V6's §6.15 illustration should be re-read with this test.)

## 7. Competency questions

1. Which provisions (E) constitute this relation, and are they in force for the stated version?
2. Is this relation *established, conditional, expressly prohibited*, or merely *not found*?
3. At which claim status is this element: projected, inscribed, instantiated, observed — and on what level-A/B/C evidence?
4. Is this device an interface (reified instrument) or only a characteristic of a relation?
5. Which positions lie on every path from rule-maker to target (necessary stage)?
6. Does the property claimed belong to a part, a relation, a subconfiguration or the whole?
7. Do two corpora with the same position/function inventory differ in relations — and in which properties?
8. What is the highest claim the evidence authorizes (stopping rule)?
9. What boundary fixes this architecture, and could a different boundary change the result?
10. Where do formal, instantiated and observed profiles diverge for this architecture?

## 8. Inter-architecture relation (corpus level)

Rotem's revised-codebook variable `architecture_configuration` (Single / Alternative / Sequential / Complementary / Separate) is read as a relation **between different architectures coded for one act**, not as a property inside one architecture (the codebook instructs this). In RGAM it is a candidate relation among S/A objects. Exhaustiveness and mutual exclusivity are **not assumed**. Mapping to V6 §5.2.3 is proposed, not verified with Rotem or David.

## 9. Bridge to the intermediation database — RELATIONSHIP_MAP (proposed)

Status: concept relayed by Igor; **no source document located**; the specification here is ours. RELATIONSHIP_MAP = a *many-to-many mapping layer* from provision-linked statements (V6's observation unit; Rotem's provision events) to R objects, with `provision ↔ relation` links, derivation flag and status field. Rotem's actor/action/recipient fields supply parties and function; the layer neither replaces the codebook nor modifies baselines. Compatible with V6 §6.3 ("pivotal bridge"; many-to-many).

## 10. Strongest objections and unresolved points (for Igor/David)

| # | Objection | Current response | Status |
|---|---|---|---|
| 1 | "Material" may just mean "provenance-tracked" and add no ontology | D03: materiality is the dependence of constituted relations on inscriptions and devices (`depends_on`, support-gap report, PT-2); provenance is necessary but separate. Residual: the word may still be read as "documentary"; "evidentially anchored" remains an alternative | PARTLY ADDRESSED |
| 2 | Hillier–Hanson transfer is analogical; legal relations lack adjacency/metric | Only analytic structure transfers; no metric imported; claim is conditional (selection matrix §4) | OPEN — test in Phase 3 |
| 3 | Bhaskar and Orlikowski are not jointly consistent | Different layers; pragmatic, not unified; declared limitation | DECLARED |
| 4 | Ontology heavier than coders can use (David: coordination, innovation, **practical progress**) | Coders need only R-level fields; S/A are *derived*, never coded at first pass (V6 §6.4) | MITIGATED |
| 5 | Instrument representation needs judgment | D01 three situations; D05 typed external references for out-of-corpus devices and positions. Open: the (a)+(b) threshold for I2 | PARTLY ADDRESSED |
| 6 | Reification of legal positions as social reality | Formal ≠ instantiated ≠ operational | MITIGATED |
| 7 | Accountability is both relation type and attribute in V6 | D02/D04/D10: AC relation + `accountable_via` pointer; INFO / ANSWERABILITY / AC / IND; distributed forums admissible when capacities are institutionally identifiable. The "grounded possibility of consequences" criterion is untested on real text | ADDRESSED (provisional) |
| 8 | The two V6 lists of architectural measures differ | Harmonise | OPEN |

## 11. Revision log

- **rev1 (2026-10-03):** D01 (three instrument situations, four entity kinds, projections), D02 (accountability criteria and pointer), D03 (four distinctions; statuses split; substantive materiality). The earlier statuses `normatively_inscribed/formally_constituted` became `documented` + `legally_constituted`; the Phase-1 "instrument-device (P, conditional) two-state rule" became I1/I2/I3.
- **rev1 + PT-1…PT-5 (same day):** post-stress-test patches, marked `[PT-n]`, see `validation/ONTOLOGY_STRESS_TEST_MATERIALITY_DELTA_v0_4.md`. The patches were made by the executing agent from test failures; they are **not** author-approved decisions.
- **Open after the first self-test:** M12, I04, A05, X03, X04, W05 — now handled by D04–D09 (below).
- **rev2 (2026-10-03):** D04 diffuse accountability forums (INFO/AC/IND; exercise not required); D05 typed external references; D06 claim-level evidence and artifact metadata; D07 observed arrangements as an adjacent layer; D08 position type/instance/jurisdiction/time; D09 no aggregate discretion score; materiality vs evidentiary anchoring. Regression patches from `validation/ONTOLOGY_STRESS_TEST_REGRESSION_v0_4_rev2.md`: **PT-6** (`source_kind` on external references), **PT-7** (count-dependent properties at type level), **PT-8** (absence-dependent claims and unresolved external references). These patches are agent proposals pending review.
- **rev3 (2026-10-03):** D10 — AR-1 approved with refinement: four accountability classes (INFO, ANSWERABILITY, AC, IND); AC requires actor–forum relation, duty of explanation and justification, questioning capacity, assessment/judgment capacity and a grounded possibility of consequences; no inference of operation. PT-6 approved; PT-7 and PT-8 approved as provisional scientific corrections. Ontological development provisionally closed; priority moves to the manuscript.
- **Still open:** the I2 threshold; a rule for reading drafting cues ("is established" vs "shall be established") in translated texts.

## 12. Not done in this round

JSON registry; `V0_3_AUDIT_DELTA`; bibliography; manuscript; real-law demonstration (GDPR candidate unselected). `scripts/validate_repository.py` absent: **NOT RUN**.
