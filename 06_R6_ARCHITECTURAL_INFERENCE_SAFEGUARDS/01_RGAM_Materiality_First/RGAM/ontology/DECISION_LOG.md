# RGAM scientific decision log

Append-only. Do not overwrite earlier entries or imply approval that does not exist. A decision by Igor Caires Machado is recorded as such; an agent-made change is recorded as a **proposal pending review**. David Levi-Faur and Rotem Medzini have approved none of these entries.

Earlier (Phase 1) decisions are recorded in `00_ADMIN/EXECUTION_ADDENDUM_v0_4.md` and the ontology revision log; they are not re-entered here.

## D01 — Instrument representation · 2026-10-03

- **Decider:** Igor Caires Machado (message of 2026-10-03). **Status:** `DECIDED` (conceptual); operational thresholds open.
- **Decision:** Approve the instrument rule with refinement. Keep three analytical situations apart: **I1** instrument as typed characteristic of a legally constituted relation; **I2** instrument-device as a distinct juridically constituted entity, when the legal source supports it; **I3** materially instantiated device, requiring empirical evidence beyond the legal prescription. Keep positions, instruments, documentary artifacts and institutional devices distinct. Not every ontological entity is a node of the actor-position graph; **graphs are analytical projections of the ontology, not the ontology**.
- **Rationale:** V6 §3.5 itself says both "characteristic of a relationship" and "building block of architectures" and "sufficiently distinct institutional device"; a three-situation scheme resolves this without forcing devices into the actor graph and separates legal constitution from instantiation.
- **Objection:** the (a) identity + (b) operator/rules/boundary threshold for I2 involves judgment; out-of-corpus constitution is unresolved (test I04).
- **Alternative not chosen:** treat every instrument as a node (rejected: equates actors and tools); treat instruments only as relation characteristics (rejected: cannot represent registers/platforms that have their own boundary and infrastructure).
- **Affected:** `ontology/ONTOLOGY_v0_4.md` §§2, 3.2, 3.3; `handoff/00_ONTOLOGY_AT_A_GLANCE_v0_4.md`; supersedes the Phase-1 "two-state rule".
- **Retrospective effect:** none on frozen baselines.

## D02 — Accountability · 2026-10-03

- **Decider:** Igor Caires Machado. **Status:** `DECIDED` (conceptual); needs David's confirmation as author of the V6 definition.
- **Decision:** Approve the distinction between accountability as a **qualified relationship** and as an **attribute of another relationship or arrangement**, with explicit operational criteria: reporting does not imply accountability; supervision does not imply a complete accountability arrangement; preserve legal source, responsible actor, identifiable forum, applicable obligation and independently supported attributes; where accountability qualifies another relation, keep the reference and avoid duplicate observations; test missing forums, incomplete evidence and reporting without demonstrated accountability.
- **Implementation:** one AC relation object; `accountable_via` pointer on an R or S (`qualifies`); five elements (source, responsible actor, identifiable forum, obligation to inform/justify, forum capacity); classification table; attributes need their own provenance.
- **Rationale:** V6 lists accountability both as a relationship type (§3.6 table) and as an attribute (§3.6 list); V6 §4.3 states that reporting alone does not create accountability.
- **Objection:** "identifiable forum" for diffuse forums (the public, stakeholders) is underdetermined (test A05); some would count transparency-based forums.
- **Alternative not chosen:** accountability only as an attribute (loses cases where it is itself a legally constituted relation); only as a type (duplicates observations and cannot mark qualification).
- **Affected:** `ontology/ONTOLOGY_v0_4.md` §3.3, §3.3.1; glance page; crosswalk row 9 (to be read together with this entry).
- **Retrospective effect:** none on frozen baselines.

## D03 — Materiality safeguard · 2026-10-03

- **Decider:** Igor Caires Machado. **Status:** `DECIDED` (conceptual).
- **Decision:** Keep the distinction between ontological existence and empirical observability (critical realism). Do not reduce materiality to documentary provenance: treat it as a substantive concern with how legally constituted architectures find expression and support through identifiable inscriptions and institutional devices. Distinguish **documentary inscription, legal constitution, material instantiation, observed operation**. Sociomateriality stays complementary; implementation is not the principal object.
- **Implementation:** claim statuses `conceptually_projected · documented · legally_constituted · materially_instantiated · operationally_observed`; the earlier `normatively_inscribed/formally_constituted` split in two.
- **Rationale:** a draft or repealed text is an inscription without legal constitution; a constituted device may be unbuilt.
- **Objection:** "material" may still be read as "documentary" (kept open; alternative label *evidentially anchored*).
- **Alternative not chosen:** materiality as provenance only (rejected by D03).
- **Affected:** ontology §4; materiality note (to be read with this entry: the note's two-thesis resolution stands, its three-state/four-status table is superseded by ontology §4); glance page.
- **Retrospective effect:** none.

## Agent proposals from stress testing · 2026-10-03 · `PROPOSAL_PENDING_REVIEW`

Made by the executing agent after the self-test (`validation/ONTOLOGY_STRESS_TEST_MATERIALITY_DELTA_v0_4.md`); **not author-approved**.

| ID | Proposal | Triggered by | Status |
|---|---|---|---|
| PT-1 | Constitution by mandate: a duty to establish a position ≠ the position's constitution | X01 (failed) | applied; review requested |
| PT-2 | Instantiation applies to positions/devices only; relations carry `depends_on` and a support-gap report; dependencies are expectations, not gates | X02 (failed) | applied; review requested |
| PT-3 | Legal constitution is a property of a norm/arrangement; custom flagged, out of first-round scope | L03 (failed) | applied; review requested |
| PT-4 | Absence-dependent properties require a declared corpus closure/coverage | W02 (failed) | applied; review requested |
| PT-5 | Default "incomplete" row for accountability | A09 (inconclusive) | applied |

**Open, unpatched:** M12 (artifact level attaches to the claim, not the artifact — candidate rule), I04, A05, X03 (category vs instance), X04 (operational-only relations), W05 (per-function aggregation).

## Decisions of 2026-10-03, second round (D04–D09) · decider: Igor Caires Machado · status `DECIDED` (conceptual)

| ID | Decision | Rationale / reference | Objection or limitation | Alternative not chosen | Affected |
|---|---|---|---|---|---|
| **D04** (A05) | Accountability to the public or a distributed forum is **not automatically excluded**. Distinguish INFO (transparency/disclosure without sufficient elements), AC (supported by identifiable duties and institutionalized capacities of questioning, justification and assessment), and IND (documentary evidence insufficient). Reporting or publicity alone never yields full accountability. The **exercise** of accountability is not needed to show a legally constituted arrangement. Bovens (2007) as theoretical reference | Rev1 excluded diffuse forums by default; the accountability literature includes public forums. Bovens: **`[CITATION CHECK]`**, original not stored locally; only V6's characterization is used | Assumption **AR-1**: the minimum for AC (duty + justification + questioning) is the agent's operationalization, pending Igor/David | Exclude diffuse forums (rejected by D04); treat any public reporting as accountability (rejected) | ontology §3.3.1 |
| **D05** (I04) | Typed **external references** for devices/positions constituted outside the corpus boundary, with `external_reference_id`, `referenced_legal_source`, `reference_role`, `source_verification_status`, `boundary_status`, `constitutive_dependency`. A reference shows legal relevance only, never instantiation or operation; no automatic corpus expansion; traceability preserved. To be tested before GDPR Arts 42–43 | The V6 regime-boundary rule (§6.7) requires explicit boundary decisions | Additive field `source_kind` (**PT-6**) added by the agent because technical standards are not legal sources; **needs Igor's approval** | Expand the corpus to every referenced instrument (rejected) | ontology §3.7, §5 |
| **D06** (M12) | Evidence status belongs to individual **claims**; artifacts keep their own authenticity, provenance and temporal metadata | A single artifact can support claims at different levels | Level-C coding guidelines deferred | Level attached to the artifact (rejected) | ontology §3.6 |
| **D07** (X04) | Operational-only relationships stay outside the primary legal architecture; representable as `ObservedArrangement` in a separate adjacent layer | Keeps implementation out of the principal object (D03) | No method to reconstruct operational architecture | Include them as R (rejected) | ontology §3.8 |
| **D08** (X03) | Distinguish `position_type`, `position_instance`, `jurisdiction`, `temporal_reference`; invent no instance from a generic category | Multi-jurisdiction law (e.g. national authorities) | Counts at type level: **PT-7** | Treat each generic category as one actor (rejected) | ontology §3.1 |
| **D09** (W05; materiality) | No unsupported aggregate discretion score; keep discretion by function, position and qualified relation. Materiality stays a **substantive theoretical concept**; evidentiary anchoring is its **methodological counterpart, not a synonym** | V6 §6.6 declines a composite; D03 | Cross-law comparison needs an ordinal scheme later | Scalar discretion index (rejected) | ontology §4, §6.1 |

### Agent proposals from the regression test · `PROPOSAL_PENDING_REVIEW`

| ID | Proposal | Triggered by | Status |
|---|---|---|---|
| PT-6 | `source_kind` on external references | I04d (failed) | applied; review requested |
| PT-7 | Count-dependent whole properties at type level only from evidenced instances or `legal_multiplicity` bounds | X03c (failed) | applied; review requested |
| PT-8 | Absence-dependent claims touching an unresolved external reference are `undetermined` or scoped to the declared corpus | W02b (failed) | applied; review requested |

Test evidence: `validation/ONTOLOGY_STRESS_TEST_REGRESSION_v0_4_rev2.md` (internal regression, not independent validation). Retrospective effect on frozen baselines: none.

## Decisions of 2026-10-03, third round · decider: Igor Caires Machado

| ID | Decision | Notes |
|---|---|---|
| **PT-6** | **APPROVED.** Retain `source_kind`, distinguishing source type from legal or normative force | Status changes from `PROPOSAL_PENDING_REVIEW` to approved |
| **PT-7, PT-8** | **APPROVED as provisional scientific corrections** | To be revisited if real-text work shows them inadequate |
| **D10 (AR-1)** | **APPROVED WITH REFINEMENT.** Four classes: **INFO** (information/disclosure), **ANSWERABILITY** (answerability without all accountability elements), **AC** (sufficiently established accountability), **IND** (indeterminate evidence). AC requires an identifiable accountability relationship, a duty of explanation and justification, questioning capacity, assessment/judgment capacity and a grounded possibility of consequences. Distributed public forums are admissible when their relevant capacities are institutionally identifiable. Do not infer actual operation from legally constituted capacities | Supersedes the agent's AR-1 (AC = duty + justification + questioning). Bovens (2007) consulted: bibliographic record and abstract verified via Crossref (DOI 10.1111/j.1468-0386.2007.00378.x); the full text was **not** read — detailed conditions are cited through V6 §4.3. Effect on the rev2 regression (not re-run, because stress testing is stopped): A05b becomes ANSWERABILITY (no assessment/consequence), A05e an ANSWERABILITY arrangement; A05a, A05c, A05d unchanged |
| **D11 (priority)** | Ontological development **provisionally closed**. Stop extraction, stress testing, GDPR coding and database engineering. Immediate priority: the independent article *From Architectural Configuration to Regulatory Governance Architecture: Towards a Morphological and Materially Anchored Ontology of Law*, in `paper/MANUSCRIPT_v0_4.md` | Deferred: GDPR Articles 42–43 demonstration, JSON registry, independent blind testing |

Affected: `ontology/ONTOLOGY_v0_4.md` (rev3, §3.3.1, objections, revision log).
