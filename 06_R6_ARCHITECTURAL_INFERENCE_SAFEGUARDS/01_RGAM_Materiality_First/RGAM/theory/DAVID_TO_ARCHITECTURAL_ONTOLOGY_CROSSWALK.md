# David-to-RGAM crosswalk — the twelve V6 categories

> **Superseded in part by D01–D03 (`ontology/DECISION_LOG.md`, ontology rev1):** the "two-state rule" for Instruments (card 5) is now the three situations I1/I2/I3, and Accountability (cards 7–9) is now an AC relation plus an `accountable_via` pointer with a five-element test. The rest of this crosswalk stands. Read the cards for 5 and 9 together with ontology §§3.2 and 3.3.1.

**Version:** v0_4 · **Date:** 2026-10-03 · **Status:** `WORKING_ANALYTICAL_NOTE`. Not approved by David, Rotem or any other author; not validated.
**Baseline:** David Levi-Faur, *Law and the Architectures of Governance: Towards a Relational Leximetrics Approach*, V6 (2 Oct 2026), `Enviados/Artigo v6/draft v6  Law_and_Governance_Architectures_Revised.docx` (SHA-256 `38360a6f…ba61b`, read in full).

## 0. Attribution and reading rules

- **Definitions in column "V6 definition" are David's** (paraphrased from the cited V6 section; no new wording is attributed to him). RGAM does not claim to have discovered any of the twelve categories, the three levels, the inference ladder or the stopping rule.
- **"RGAM role" is our proposal** (Igor + executing agent). It specifies *what kind of ontological entity* each V6 category is when an architecture is reconstructed, and *which bearer* (part, relation, subconfiguration, whole) carries it. It is open to David's correction.
- Locators are V6 section numbers. (V6 numbering has two sections labelled 6.13; 6.14 is absent; see §4.)
- **Do not read this as "twelve node types".** Only a minority of V6 categories become nodes (§2).
- Strata used below are those of `ontology/ONTOLOGY_v0_4.md`: **E** evidence/inscription · **P** parts · **R** qualified relations · **S** subconfigurations · **A** whole architecture · **M** material anchoring (transversal) · **X** adjacent layers.

## 1. Summary

| # | V6 category | V6 level / § | RGAM ontological role | Becomes a node? | Bearer |
|---|---|---|---|---|---|
| 1 | Objects | I · §3.1 | Scope qualifier: what a relation is directed at | No | R |
| 2 | Actors | I · §3.2 | **Position** (legally specified place in a relation); not a fixed identity | **Yes** (P) | P |
| 3 | Functions | I · §3.3 | Qualifier of a relation; aggregated as *functional allocation* of the whole | No | R → A |
| 4 | Mechanisms | I · §3.4 | Qualifier of a relation (how influence operates) | No | R |
| 5 | Instruments | I · §3.5 | Relation characteristic by default; **part** only if the text constitutes a distinct device with its own boundary | Conditionally (P) | R or P |
| 6 | Relationships | I · §3.6 | **Reified qualified relation** — the pivotal bridge | Reified (R) | R |
| 7 | Authority | II · §4.1 | Relation attribute; aggregated as distribution over the whole | No | R → A |
| 8 | Discretion | II · §4.2 | Relation attribute, function-specific; aggregated as distribution | No | R → A |
| 9 | Accountability | II · §4.3 | Relation type **and** relation attribute; aggregated as structure | No (see §4) | R → A |
| 10 | Strategies | III · §5.1 | Derived design profile of a set of relations; non-morphological annotation | No | S (annotation) |
| 11 | Architectures | III · §5.2 | The bounded whole; named forms = recurrent subconfiguration patterns | Whole (A) | S, A |
| 12 | Governance logics | III · §5.3 | Interpretive horizon above A; not constitutive of morphology | No | X |

## 2. Category cards

Format: V6 definition · RGAM role · evidentiary referent (M) · units (coding / analysis / inference, V6 §6.1) · inference rule or guard · attribution/status.

### 1. Objects (V6 §3.1)
- **V6:** the behaviour, entity, process, relationship or institutional arrangement toward which governance is directed; eight object families (conduct, organizations, processes, information, products/technologies, relationships, risks, governance systems — "regulating the regulator").
- **RGAM:** a *scope qualifier* on a relation ("this supervision concerns *processes*"). Not an actor node. The two reflexive families (*relationships*, *governance systems*) are what produce **nesting** — a relation whose object is another relation or sub-system — and are therefore the entry point for subconfigurations (S).
- **M:** the provision or instrument that names the object (level A inscription).
- **Units:** coded per statement; analysed per relation; infers nothing alone.
- **Guard:** an object does not establish an actor or relation. `[RGAM proposal]`

### 2. Actors (V6 §3.2)
- **V6:** entities occupying roles in governance; actors have no fixed governance identity — position depends on the legally constituted relationship (V6 §1, §3.6).
- **RGAM:** the node type is a **Position** (legally specified place, or actor category, as it figures in relations). Three distinctions retained from v0.3: *organization* ≠ *office/position* ≠ *holder*. "Role" is **relation-relative**, so one position may be regulator in R₁ and target in R₂ — this preserves David's relational premise.
- **M:** (A) text creating/recognizing the position; (B) independent evidence it is filled/established (register, appointment) — never inferred from the mandate.
- **Units:** coded per statement; analysed per position-in-relation; part-level property = position in the configuration.
- **Guard:** presence of an actor ≠ architecture (V6 §6.8, atomistic fallacy).

### 3. Functions (V6 §3.3)
- **V6:** governance work performed (rule-making, implementation, interpretation, information provision, monitoring, enforcement, adjudication, remediation).
- **RGAM:** *what the relation does*. Carried as a qualifier on R. At whole level it yields **functional allocation** (V6 §5.2.1: where rule-making, monitoring, verification, enforcement sit).
- **M:** (A) the provision assigning the task; formal assignment ≠ performance (functional fallacy, V6 §6.8).
- **Guard:** keep distinct from Mechanism and Instrument (§3 below, "F/M/I").

### 4. Mechanisms (V6 §3.4)
- **V6:** a distinct means through which an actor or arrangement shapes the conduct, capacities, information, choices or decisions of another; elementary means, not complete systems.
- **RGAM:** *how influence operates* in a relation; qualifier on R; many-to-many with functions and instruments (V6 §3.5).
- **Open issue (verified in the DOCX):** in the V6 mechanism table seven rows (Registration, Notification, Reporting, Certification, Auditing, Ranking & Rating, Conformity Assessment) have both the "governing logic" and "illustrative device" cells empty, Assurance has no illustrative device, and several of these terms also appear in the instrument-family table. See `FOUNDATIONAL_PAPER_REVIEW/04_REGISTRO_QUESTOES_DECISOES.md`, V6-02.
- **Guard:** the same word ("auditing", "disclosure") can denote a mechanism or an instrument; code from role + device, not from the word.

### 5. Instruments (V6 §3.5)
- **V6:** legally constituted or recognized concrete institutional devices through which governing activity is made operational (licences, registers, certification schemes…). V6 itself proposes coding them "as observable characteristics of legally constituted governance relationships", but also calls them "building blocks of architectures" and says to code them separately "where the legal text establishes or recognizes a sufficiently distinct institutional device".
- **RGAM:** resolves the two V6 statements with a **two-state rule**: (i) default = *relation characteristic*; (ii) **reified as a Part** when the text constitutes a device with its own boundary, rules and (potentially) infrastructure — a register, a certification scheme, a reporting platform. An instrument-part is an **interface** between positions, never an actor.
- **M:** this is where materiality bites hardest: (A) the legal text creating the device; (B) evidence the register/platform exists; (C) evidence of use — three separable claims (v0.3 §1).
- **Guard:** an instrument is not inferred from a function or mechanism (V6 §3.5).

### 6. Relationships (V6 §3.6, §6.3)
- **V6:** legally constituted connections between two or more actors through which authority, obligations, information, resources, oversight, accountability, representation, etc. are exercised; ten types; directional; typed, not generic; the *pivotal bridge* between statements and architecture; many-to-many with provisions (V6 §6.3). Notation `Rᵢ = (A, B, Object, Function, Mechanism, Instrument, Authority, Discretion, Accountability)`.
- **RGAM:** the **reified qualified relation** (stratum R) — carrying type, parties, direction where defensible, deontic modality, conditions, temporal validity, status (`established / conditional / expressly prohibited / not found`) and provenance. n-ary where the text requires it. This is the entity that RGAM's ontology is built around, and it is the **proposed locus of the RELATIONSHIP_MAP bridge** (§3 below).
- **M:** every relation points to ≥1 provision (A); several provisions may jointly constitute one relation.
- **Guard:** an obligation on A does not by itself yield an A→B relation (V6 §6.7, second step; D2 in the foundational review).

### 7–9. Authority, Discretion, Accountability (V6 §§4.1–4.3)
- **V6:** *relational attributes* qualifying the relations. Authority = legally consequential capacity; Discretion = legally structured space for choice (relational and function-specific); Accountability = institutionalized relation in which an actor must provide information or justification to a forum entitled to scrutinize, assess, question or respond, with possible consequences. Reporting alone ≠ accountability (V6 §4.3).
- **RGAM:** attributes **of R** at part scale, but also **distributions over the whole** at A scale (V6 §5.2.1 treats discretion and accountability "as architectural distributions": discretion distribution, accountability structure). The same word therefore names two properties on two bearers — which RGAM keeps apart (`ontology §6`).
- **Accountability caveat:** V6 lists "Accountability" both as one of ten relationship *types* (§3.6 table) and as a relationship *attribute* ("to whom B is answerable", §3.6 attribute list). RGAM proposes: type = the answerability relation itself; attribute = the accountability profile of *other* relations. Needs David's confirmation.
- **M:** (A) provisions conferring capacity / margin / answerability; the *exercise* of authority or discretion is C-level, not inferred.

### 10. Strategies (V6 §5.1)
- **V6:** patterned approach through which public authority structures the obligations of regulated actors (prescriptive, procedural, process, management, performance, outcomes, principles/goals, risk-based, responsive); not mutually exclusive; may be embedded in different architectures.
- **RGAM:** a **derived design profile** of a set of command-type relations (what is specified: conduct, process, performance, outcome). **Orthogonal to morphology**: V6 says the same strategy can sit in different architectures; RGAM therefore records strategy as an *annotation* on S, and does not use it to define configuration.
- **Guard:** coded after relations, never at first pass (V6 §6.4).

### 11. Architectures (V6 §5.2, §6.5–6.11)
- **V6:** legally constituted configuration through which governance work, authority, discretion and accountability are distributed among actors and organized through relationships, mechanisms and instruments; *emergent*, not inferable from one instrument/actor; multidimensional, not mutually exclusive; ten dimensions (§5.2.1); ten named recurrent configurations (§5.2.2); twelve candidate measures (§6.11); varies *within* a statute (§5.2.3).
- **RGAM:** **A** is the bounded whole for an explicitly stated corpus, domain, jurisdiction and interval. Named configurations (hierarchical, delegated, enhanced self-regulation, accreditation chain, …) are **patterns matched to subconfigurations (S)**, not labels for whole laws — which is exactly V6's own §5.2.3. RGAM's addition is the **bearer assignment** for every dimension (`ontology §6`).
- **Guard:** container fallacy (V6 §6.8): a statute is not automatically one architecture.

### 12. Governance logics (V6 §5.3)
- **V6:** broader organizing principle (hierarchical, market, associational, professional, network, experimentalist); laws combine several.
- **RGAM:** an **interpretive horizon above A** (stratum X). It is not required for reconstruction and is not a morphological property. **Observation on V6:** §5.3 consists of a single paragraph whose final sentence ends mid-clause ("…so the empirical task is to examine"). The DOCX text appears truncated; V6-06 in the review register stays open.

## 3. F/M/I, RELATIONSHIP_MAP, architecture_configuration, frequency, Seidl–Kosti

**Function / Mechanism / Instrument (refinement 3).** V6 defines them as *what work* / *how influence operates* / *which institutional device* and states the relation is not one-to-one (V6 §3.5). RGAM keeps three separate slots on R and adds the two-state instrument rule above. Contrastive TOY pattern: *a public register* (instrument) *activates disclosure* (mechanism) *while performing information provision* (function) — V6's own example. Nothing is merged.

**RELATIONSHIP_MAP (refinement 2).** Status: **concept described by Igor; no source document located (PENDING).** RGAM specification proposed here: a *mapping layer* that (a) takes each provision-linked statement (Rotem's provision-event unit; V6's Law×Provision×… observation) and (b) produces zero, one or several R objects, with a many-to-many link table `provision ↔ relation` and a status field (`established / conditional / prohibited / not found`). It is the "pivotal bridge" of V6 §6.3 made explicit. Its relation to Rotem's database is *schematic*: Rotem's actor/action/recipient fields feed R's parties and function; the bridge is not a replacement of the codebook.

**`architecture_configuration` (refinement 4).** In Rotem's revised codebook the variable (values Single, Alternative, Sequential, Complementary, Separate; multiple values except with Single) records the **relationship *between different regulatory architectures coded for the act***, and the entry says not to use it for steps within one architecture. RGAM therefore reads it as an **inter-architecture relation at act/corpus scale**, i.e. a property of a *set of S or A*, **not** a property inside one architecture. Candidate only: exhaustiveness and mutual exclusivity are not assumed (the codebook itself permits multiple values). It maps to V6 §5.2.3 ("mixed and overlapping architectures"; architecture varying within a statute).

**Frequency vs architectural significance (refinement 5).** V6 §6.6 gives `Significance = f(Frequency, Authority, Centrality, Exclusivity, Sequence, Consequence, Substitutability)` and "counts identify composition; configurations identify organization". RGAM keeps **composition (counts)** as a descriptor of E/P, and reserves "significance" for relations/subconfigurations with explicit evidence on the other six dimensions; no composite score (V6 §6.6 itself declines one).

**Seidl & Kosti (2026) (refinement 6; read in the local PDF).** Lessons we take, verified in the paper: (i) the legal act is too coarse a unit; provisions are the working unit and aggregate "freely upward"; (ii) human-validated LLM ensemble with reported agreement (provision-level tasks: inter-coder agreement .92–.97 proportion, Krippendorff's α .88–.91; ensemble and encoder agreement lower for *regulated actor* than for *digital policy* — i.e. agreement falls as interpretive load rises); (iii) stated limitations: every provision is treated as having equal legal weight, and **provisions are not related to each other** — "we do not know how provisions relate". RGAM's distinctive step is precisely the reconstruction of **relations among provisions' institutional content** and their aggregation into configurations — not provision classification. We do not claim S&K lack a relational ambition; we claim their paper states this limitation. *Appendix not read.*

## 4. Points where V6 itself needs David's decision (carried to the register)

1. Accountability as relation type vs attribute (above).
2. Mechanism table: empty rows; overlap with instrument families (V6-02).
3. §5.3 Governance logics appears truncated (V6-06).
4. Section numbering: two §6.13; no §6.14 (cosmetic).
5. The §6.15 illustration's accreditation premise (V6-08) — unchanged from the foundational review.

## 5. Correspondence of V6's ladder and levels to RGAM strata

V6 states that the three conceptual levels do **not** map mechanically onto the six-step ladder (FOUNDATIONAL_PAPER_REVIEW §2). RGAM respects this:

| V6 ladder (§6.2) | RGAM stratum |
|---|---|
| 1 Legal text | **E** (inscriptions) |
| 2 Institutional statements | **E → P/R candidates** |
| 3 Governance relationships | **R** |
| 4 Governance configurations | **S** |
| 5 Legal architectures | **A** (bounded corpus) |
| 6 Governance regimes | **A**, with an explicit multi-instrument boundary decision (V6 §6.7, final rule) |
| *(not in ladder)* implemented / operational architecture (V6 §6.13) | **X**, distinguished from A through **M** levels B and C |
