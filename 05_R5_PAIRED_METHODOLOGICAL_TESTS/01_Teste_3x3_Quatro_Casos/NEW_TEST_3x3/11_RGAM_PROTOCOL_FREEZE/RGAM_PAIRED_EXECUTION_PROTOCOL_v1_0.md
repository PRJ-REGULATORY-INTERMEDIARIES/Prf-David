# RGAM — PAIRED EXECUTION PROTOCOL v1.0

**Experiment:** NEW TEST 3x3 · **Arm:** RGAM (as RGAM) · **Date frozen:** 2026-10-06 · **Status:** frozen before any case execution
**Nature:** a case-general *operationalization wrapper* of the existing RGAM methodology for the paired experiment. It is **not** a revision of RGAM theory and adds no substantive concept. Where the sources are silent, the gap is registered (`RGAM_PAIRED_DECISION_RULES_v1_0.md`, Appendix A) and handled conservatively; nothing is silently filled.

## 0. Controlling sources (summary; full register in `RGAM_SOURCE_AUTHORITY_REGISTER.md`)

| Level | Source | Role |
|---|---|---|
| 1 | `RGAM/paper/MANUSCRIPT_v0_6_1.md` | controlling methodological source wherever it states a rule |
| 2 | `RGAM/ontology/ONTOLOGY_v0_4.md` (rev3) | ontological specification; subordinate to Level 1 |
| 3 | `ONTOLOGY_ALIGNMENT_AND_PRECEDENCE.md`, `V0_6_INTEGRATION_REGISTER.md`, `V0_6_1_SCIENTIFIC_REVISION_REGISTER.md`, ontology `DECISION_LOG.md` | precedence and version control only |
| 4 | `GDPR_PILOT_01/00_PROTOCOL/DECISION_RULES.md` v1.2 | procedural template only; all instrument-specific content removed |

Where ontology v0.4 conflicts materially with manuscript v0.6.1, **v0.6.1 prevails**; every such conflict is recorded in `RGAM_PRECEDENCE_AND_CONFLICT_REGISTER.csv` and none is silently reconciled.

## 1. Non-authorities and prohibitions

The following are **not** used as methodological authority and are **not** imported: the drafting prompt `PROMPT_CODEX_RGAM_v0_3_MATERIALITY_FIRST.md`; the eight-operation sequence O1–O8 of the earlier experimental procedure; any V8 vocabulary, rule or output; `RGAM/V8_ACTIVE/`; any result of earlier R2/R3/R4/PILOT/V8-COMP-01 work; any case-specific architectural finding. The RGAM arm is **RGAM as RGAM**: it keeps RGAM's frozen terminology (including the V6-lineage relation and function vocabularies recorded in the ontology and the template) and is not harmonized with any other vocabulary. A V8–RGAM crosswalk will be produced **after both arms are frozen** (placeholder: `RGAM_PAIRED_DECISION_RULES_v1_0.md` §RGAM-DR-33); it is not constructed here.

## 2. Native analytical chain

RGAM's own architecture of analysis (MS §2.4, §6.2; ON §2) is a chain of strata, not a list of operations:

```
 W  documentary corpus (complete instrument, fixed version and time)
 E  evidence: provision-level inscriptions (units) + institutional statements derived from them
 P  parts: positions (type/instance), institutional devices, normative assignments attached to positions
 R  qualified relations (reified; both parties identifiable)
 S  subconfigurations (pattern-rule sets of relations; may overlap, nest, cross chapters)
 A  architectures A1..Am (reconstructed through I1–I4; not presumed one per instrument)
    → multidimensional PROFILE (properties per S and per A, with scale, bearer and aggregation; status profile)
 M  evidentiary anchoring — TRANSVERSAL control on every claim at every stratum (not a stage)
 D  derived analytic dimensions (strategies, logics) — outside the basic topology; NOT coded
 X  adjacent empirical layers (establishment evidence, operation, outcomes, enactment) — NOT coded from legal text
```

`W ≠ A`: the instrument is the documentary universe, not automatically an architecture. An instrument may yield no architecture, one, several distinguishable, overlapping, or an indeterminate result.

### 2.1 Operational definition of each stratum

| Stratum | Unit of analysis | Admission rule | Exclusion rule | Evidence requirement | Epistemic status (ceiling from legal text) | Provenance | Relation to next stratum |
|---|---|---|---|---|---|---|---|
| **W** | the frozen source file as a whole | complete official source, SHA-256 verified, structure parse consistent with metadata | any content not in the frozen file; consolidations; external texts | hash match; parse check | n/a | W_DECLARATION | supplies the closed universe of units |
| **E (units)** | addressable unit: article paragraph/point, annex point, recital, formal provision | every unit enumerated in source order | none (all units inventoried) | text hash + anchor | `documented` | SOURCE_UNIT_INVENTORY | every unit is screened |
| **E (statements)** | institutional statement derived from ≥1 unit | provisions with governance relevance; operative text and annexes | statements resting only on a recital; headings; editorial structure | verbatim minimal span | `documented`; `legal_constitution_evidenced` where the norm itself constitutes and its force is evidenced | INSTITUTIONAL_STATEMENTS + PROVENANCE_LINKS | statements yield NA, PD, QR, EXT |
| **P (assignments)** | normative assignment (duty/power/permission) attached to a position | assignment stated without an identifiable counterparty; or constraint-only prohibition | any invented counterparty | statement + span | as E | NORMATIVE_ASSIGNMENTS | become relational only if a provision identifies a counterparty, forum or recipient |
| **P (positions/devices)** | position (type/instance) or juridically constituted device | text constitutes, recognizes or designates it and it bears an NA or QR; device meets identity + (operator or rules or bounded function) | source documents; named holders; a mention without NA/QR; platforms/instruments below the device threshold (kept as INS-TYPE characteristics) | statement + span; N-type | per norm type (N1 only → entity `legal_constitution_evidenced`); establishment `not_assessed` | POSITIONS_AND_DEVICES | parties of QR; bearers of NA |
| **R** | qualified relation (reified) | both parties identifiable in the provision or by explicit cross-reference; modality ≠ prohibition | relations inferred from two actors co-occurring, from graph drawings, or from a one-party obligation; recital-only support | statement + span; stated derivation rule if derived | relation: `documented` or `legal_constitution_evidenced`; never `material_establishment_evidenced` (PT-2) | QUALIFIED_RELATIONS | members of S |
| **S** | subconfiguration | explicit configurational warrant: relations satisfy a stated pattern rule through legally qualified coupling | grouping by chapter, vocabulary or theme alone | member records + organizing mechanism | inherits the weakest member status | SUBCONFIGURATIONS | candidate constituents of A |
| **A** | candidate whole assessed by I1–I4 | I1, I2, I3, I4 each stated and evidenced | shared actor, same act, connected graph, shared view, or external citation as sole warrant | ARCHITECTURE_CANDIDATES + CLOSURE_REGISTER | status **profile** (tally), never one label or score | ARCHITECTURE_CANDIDATES | profile of the instrument |

## 3. Execution phases (procedural order of RGAM-documented activities)

The phases below order activities that RGAM itself documents (MS §8.4 items 1–7; template steps). They are an execution aid and are **not** a new analytical theory and **not** an imported operation list. Materiality is not a phase (§4).

| Phase | Activity | Documented in | Output tables |
|---|---|---|---|
| **P0** | Verify the capsule source hash; declare W (instrument, version, temporal reference, inclusion/exclusion, domain from title/object clause only, closure scope). **Stop if the hash does not match.** | MS §2.4, §8.4(1); ON §5.1 | W_DECLARATION |
| **P1** | Parse structure; enumerate every unit; compare parsed counts to neutral metadata; state the coverage procedure. | MS §8.4(2); template §1 | SOURCE_UNIT_INVENTORY; CLOSURE_REGISTER (COVERAGE) |
| **P2** | Screen **every** unit in source order. A "No" is legitimate; headings are never evidence. | template §3 | UNIT_SCREENING |
| **P3** | Derive institutional statements; extract NA, PD, QR, EXT as separate records; classify norm type N1–N4 by wording; assign legal and epistemic statuses; prohibitions as constraints. | MS §4.3, §6.2, §7.1, §8.4(3) | INSTITUTIONAL_STATEMENTS; NORMATIVE_ASSIGNMENTS; POSITIONS_AND_DEVICES; QUALIFIED_RELATIONS; EXTERNAL_REFERENCES; PROVENANCE_LINKS |
| **P4** | Dependency and support-gap pass; accountability classification; external-reference effects on claims. | MS §4.4, §6.4, §6.5; ON PT-2, PT-8 | updates to P3 tables; UNCERTAINTY_LOG |
| **P5** | Construct subconfigurations from relations (not from chapters). | MS §6.2, §8.4(4); template §14 | SUBCONFIGURATIONS |
| **P6** | Assess each candidate whole by I1–I4 in the anti-circularity sequence; consider rival groupings; assign outcome. | MS §6.2 (S→A), §8.4(4); template §15 | ARCHITECTURE_CANDIDATES |
| **P7** | Attribute properties to bearers with scale and aggregation stated first. | MS §5.3, §6.6, §8.4(5); ON §6 | PROPERTY_REGISTER |
| **P8** | Closure test for every absence-dependent claim; effect of unresolved external references. | MS §4.7, §8.4(6)(7); ON PT-4, PT-8 | CLOSURE_REGISTER (ABSENCE_CLAIM) |
| **P9** | Assemble the instrument-level profile; select traceability demonstrations by the fixed rule; compile the human-review queue; run internal integrity checks; **stop**. | MS §7.7, §6.2; template §17–18 | INSTRUMENT_LEVEL_SUMMARY; TRACE_DEMONSTRATIONS; HUMAN_REVIEW_QUEUE; PROTOCOL_DEVIATION_LOG; RUN_METADATA |

The item of MS §8.4(8) — independent validation and human adjudication with blind coding of a subset — is a **separate subsequent stage** and is outside machine execution.

## 4. Materiality (transversal, not a stage)

Materiality is implemented as a **claim-anchoring control** attached to every claim in every phase (MS §4.4–4.5; ON §4 as subordinated by MS), never as a chronological first step.

1. **What it attaches to:** individual claims about parts, relations, subconfigurations and the whole (not to documents). Evidence status belongs to the claim; artifacts keep their own authenticity/provenance metadata.
2. **Four distinctions kept apart:** documentary inscription; legal constitution; material establishment (instantiation); observed exercise (operation).
3. **Two axes kept apart:** *legal status of the norm* for the interval (`in_force`, `not_yet_applicable`, `suspended`, `expired_or_repealed`, `conditional_on_further_act`) versus *epistemic status of the researcher's claim* (`conceptually_projected`, `documented`, `legal_constitution_evidenced`, `material_establishment_evidenced`, `exercise_evidenced`). "Documented" and "legal constitution evidenced" are never values of legal status. The five statuses are not a life cycle and none is inferred from another.
4. **What legal text can support:** `documented` and, where the instrument's own provisions evidence enactment, force and applicability, `legal_constitution_evidenced` of whatever the norm constitutes. `material_establishment_evidenced` and `exercise_evidenced` require evidence beyond the legal prescription that this experiment does not collect (layer X); they are recorded `not_assessed`.
5. **N1–N4 (MS §4.3):** N1 direct establishment constitutes the entity; N2 obligation to establish constitutes the obligation, not the entity; N3 permission/competence constitutes a competence, not the entity or a duty; N4 condition on legal effect constitutes conditionally, effective after the condition is met. Wording is classified on the authentic text; ambiguous or compound wording is recorded as such and queued, never inferred.
6. **Devices (DEV) versus typed characteristics (INS-TYPE):** a device needs identity and (operator or governing rules or a legally specified bounded function); otherwise INS-TYPE; borderline is INS-TYPE plus queue. A device is never an actor. A visualization or an artifact (e.g., a certificate) is not a device.
7. **Relations:** a relation has no body of its own, so instantiation attaches to the positions/devices it depends on (`depends_on`) and the relation carries a **support-gap report**; dependencies are expectations, never gates.
8. **Effect on claim retention:** a claim is retained at the **highest status its evidence supports** (stopping rule). A claim lacking a nameable material referent at the status asserted is **down-coded** (to `documented` or `conceptually_projected`), flagged, and excluded from any statement that an architecture has been "reconstructed" at the higher status. Nothing is deleted. Absence of evidence of establishment is never evidence of non-existence.
9. **Terminology guard:** the label `I1/I2/I3` of ontology v0.4 (instrument situations) is **not used**; instrument situations are written INS-TYPE, DEV and (as a recorded status, here always `not_assessed`) MEST. `I1–I4` is reserved for the S→A warrant conditions (conflict C-04).

## 5. Lower-level records (case-general)

- **Permitted unit of decomposition:** paragraph; point and sub-point where the text enumerates points; annex point; recital (context only). A single-paragraph article uses `P0`.
- **NA** (normative assignment): a duty, power or permission attached to a position **without** an identifiable counterparty; counterparty is **never invented** to convert an NA into a QR; where a provision later identifies a recipient, forum or counterparty, a QR is created and the NA is not duplicated.
- **PD** (position/device): type-level by default; instances only with their own source; an office is not its holder; no instance is inferred from a generic category; legal multiplicity as stated.
- **QR** (qualified relation): see §6.
- **EXT** (external reference): see §9.
- **Properties and bearers:** see §8.
- **Exact provenance:** every record cites supporting units (many-to-many) and a verbatim minimal evidence span; derived records cite all supporting units and state the derivation rule.

## 6. Qualified relations (R)

A QR is admitted only when **both parties are identifiable** in the same provision or by an explicit cross-reference, and the modality is not prohibition. Required fields: origin (legal subject), counterparty, textual direction, relation type (the ten RGAM relation types), action/object, function/mechanism/instrument as three separate slots, modality, condition, validity note, legal status of the norm, epistemic status, direct/derived with rule, exact evidence anchor. Governance direction is recorded separately where it differs from the textual direction. Where a provision supports two relation types, two QR records are made. Excluded: relations inferred from co-occurrence of actors, from a network drawing, from a one-party obligation, or from a recital alone. **Graph reachability is not a legal relation and is not legal transmission.**

## 7. Subconfigurations (S) and part–whole

An S is a set of relations (with their positions) that satisfies a **stated pattern rule** and a **governance question**, scoped to a function, stage or subsystem. It may **not** be created because provisions share a chapter, use related vocabulary or address the same theme. Each S records constituent relations, organizing mechanism, warrant basis, boundary, overlap, nesting, cross-part spans, uncertainty and a competing grouping. Named patterns are matched to S as patterns, not as labels for a whole instrument. Every candidate grouping starts as S; it becomes an A only through §8's warrant.

## 8. Properties, bearers, scale and aggregation

Four property kinds with fixed bearers (ON §6, MS §6.6): **intrinsic** (position: what the text confers), **relational** (relation: its own qualifiers), **positional** (position *within* an S/A: depends on the whole), **emergent/whole** (S or A: arises from the arrangement). A property is assigned to exactly one bearer and cannot be moved between bearers without a stated aggregation rule. **Scale and aggregation come before generalization:** whole-level statements declare their scale (which S), bearer and aggregation rule; values per S are reported before any summary. Guards: atomistic fallacy (do not lift a part property to the whole), ecological fallacy (do not push a whole property down to every part), premature aggregation. **No scalar score, composite or threshold is defined.** No index is imported from spatial or graph analysis (MS §5.3); network position is not legal status; authority, accountability or power are not inferred from connectivity. Count-dependent properties use only evidenced instances or stated legal multiplicity, otherwise `undetermined` (PT-7). Property names come from the lists of ON §6.1 and MS §6.6; others require a deviation entry.

## 9. S→A inference (I1–I4)

The S→A step is **neither a union of sets nor the naming of a connected component**. It follows the anti-circularity sequence: (1) delimit the governance question (I1); (2) identify legally evidenced coupling **independently of the expected global property** (I2); (3) examine the configurational consequence (I3); (4) test rival groupings and boundary sensitivity (I4). Each of the four must be stated and evidenced for each candidate A:

| Condition | Question and minimum warrant | What does not suffice |
|---|---|---|
| **I1** problem and scale | which governance function, domain, jurisdiction and interval the candidate whole is said to organize; the legal material fixing its scope | membership in the same act or chapter |
| **I2** qualified coupling | which legal competence, conditional dependency, delegation, procedural linkage, shared mandatory interface or cross-functional rule relates the S (directed parties, effect, conditions, spans); where integration is itself explicitly constituted by law, record that | common actor, similar vocabulary, visual adjacency, external citation alone |
| **I3** configurational consequence | which property becomes attributable to the whole rather than to each S independently; its bearer and inferential rule | re-describing the inventory; inferring information flow from unqualified reachability; presupposing the integration being warranted |
| **I4** boundary and defeaters | what was searched; unresolved external constitutive dependencies; which rival grouping could explain the same pattern | treating unsearched provisions as absent; assuming the instrument is institutionally self-contained |

One S can qualify as an A (I2 then concerns internal qualified coupling); several S claimed to form a larger A additionally require coupling **between** them. Kinds of connection (shared participation, coordination or communication, qualified procedural dependency, mandatory interface, conditional dependency, integration through distributed powers) are distinguished and are **not an ordered scale**. A shared authority is insufficient. Absence of an edge does not establish separation. **Authorized outcomes per candidate:** `INTEGRATED`, `DISTINGUISHABLE` (distinct architectures or disconnected subconfigurations, only where coverage is sufficient), `OVERLAPPING_OR_PARTIALLY_INTEGRATED` (overlap only where source-supported; the intersection is not automatically a new architecture), `INDETERMINATE`. **No scores, no invented thresholds, no forced architecture.** I1–I4 are provisional warrant expectations, not existence tests; every `INTEGRATED` or `OVERLAPPING_OR_PARTIALLY_INTEGRATED` outcome is queued for human review because the I2/I3 thresholds are unvalidated.

## 10. External references, absence and closure

- Only references to sources **outside W** are EXT records. Intra-instrument cross-references resolve **within W**: they supply support units and derivation (GAP-03; queued when ambiguous). A reference shows legal relevance only; it never demonstrates establishment or operation.
- No external retrieval is authorized in this experiment: `source_verification_status = not_checked` for every EXT; `boundary_status = outside_corpus_not_expanded` unless a recorded boundary decision says otherwise. No relation contained in an external source enters any architecture.
- A claim whose legal constitution depends on an unresolved external reference is `undetermined` until that source is verified (it cannot be in this experiment); absence-dependent claims touching it are `undetermined` or restricted to "within the declared corpus only".
- **Absence-dependent properties** (necessity of a stage, substitutability, exclusivity, "no alternative path", absence of a relation) require a declared coverage/closure statement; "not found" is a statement about the search, not about the law. Silence is neither permission nor prohibition.

## 11. Stopping rule

> **Assert only the highest analytical level authorized by the available evidence.**

Concretely: stop at E where statements cannot be anchored; at P where no counterparty is identifiable; at R where relations lack identifiable parties; at S where no explicit configurational warrant exists; at A unless I1–I4 are all satisfied for the stated scale. `INDETERMINATE` is a legitimate result at every level. `W → A` is never forced when the intermediate evidentiary and inferential conditions are not satisfied. The instrument-level result may be `NO_ARCHITECTURE_WARRANTED`.

## 12. Machine and human review

All outputs are **machine-generated and provisional**; repetition by the same model is not inter-coder reliability. The executor writes the machine columns of HUMAN_REVIEW_QUEUE only and leaves `human_decision`, `human_rationale`, `decided_by`, `decision_date` blank. **Human adjudication is never simulated.** Mandatory queue triggers: ambiguous or compound norm-type wording (HQ-NORMTYPE); device/INS-TYPE borderline (HQ-DEV); accountability sufficiency borderline or an assertion of accountability with missing elements (HQ-ACCOUNT); every INTEGRATED outcome (HQ-INTEGRATION) and every OVERLAPPING outcome (HQ-OVERLAP); ambiguous internal/external cross-reference (HQ-XREF); relation direction not defensible from text (HQ-DIRECTION); any protocol gap encountered (HQ-GAP); constitutive dependency on an unresolved external reference (HQ-EXTDEP).

## 13. Vertical traceability

Every higher-order claim must be auditable down to source text: `A → S → R (and NA/PD) → institutional statement → unit → exact provision and verbatim span`, using stable IDs (`<case>.A{n}.P{k}` units; `ST-`, `NA-`, `PD-`, `QR-`, `EXT-`, `SC-`, `ARCH-`, `PROP-`, `CL-`, `UNC-`, `HQ-`, `LNK-`), many-to-many provenance in PROVENANCE_LINKS, explicit inference rules, epistemic status and property bearer on every record, and uncertainty flags. At least one vertical trace is demonstrated per case, selected by the **fixed rule** in the data dictionary (seeded draw among candidates spanning ≥2 parts of the instrument, plus the deterministic largest-support candidate) — never chosen for expected support.

## 14. Layer discipline

Strategies and governance logics (D) and implementation, operation, outcomes and sociomaterial enactment (X) are **not coded**. Practice without legal basis is not an R; an optional `ObservedArrangement` layer is not used here. A recital creates no record on its own. A source document, a visualization or an ISO-style "view" is not a position, relation or architecture; research views are representations with shared identifiers, not additional juridical architectures.

## 15. Case independence and blind execution

Each case is executed in a **fresh, sequential subcontext** that receives only: the frozen protocol, dictionary, decision rules and output schema; the controlling legal source of that case; neutral case metadata; blank templates. It receives no V8 output, count or conclusion, no R2/R3 output, no historical relationship extraction, no selection ranking and no result of another RGAM case. See `RGAM_BLINDNESS_AND_ACCESS_POLICY.md` for the allow-list, deny-list, technical read-deny status and limitations. The protocol contains no rule derived from any of the four experimental legal texts, none of which was opened or interpreted in constructing it.

## 16. Required narrative outputs per case

In addition to the tables of `RGAM_CASE_OUTPUT_SCHEMA.md`, each case produces `CASE_RGAM_REPORT.md` containing: W declaration and coverage; counts of records by table (as evidence descriptors, not significance); the S list with warrants; each candidate A with I1–I4 and outcome; the property register summary with scales; the status profile; closure and external-reference limitations; open queue items; deviations. The report makes no comparison with any other method or case.

## 17. Immutability

This protocol, the dictionary, the decision rules and the output schema are frozen by `RGAM_PROTOCOL_FREEZE_MANIFEST.csv` (SHA-256 recorded in `RGAM_PROTOCOL_FREEZE_MANIFEST_SHA256.txt`). Any change after freeze requires a separate documented decision and a new version; case analysis may not alter the method.
