# R3 Dataset Architecture Proposal

## 1. Main research question

> How are regulatory intermediation mechanisms organized and combined across actors and regulatory relations in EU climate regulation, and what regulatory capacities do these configurations appear designed to provide?

The architecture separates two linked components:

- **RQ-A — empirical configuration:** directly answerable descriptively from the current R3 through actors, intermediary units, relations, mechanism events, configurations, and edges.
- **RQ-B — regulatory capacity:** a future derived layer. Phase 10 creates its empty schema but does not assign capacity labels.

## 2. Analytical logic

The dataset implements this sequence without collapsing levels:

`law design → actor universe → R–I–T relation → intermediary transformation → elementary mechanism → within-relation configuration → future capacity proposition`

Each transition is represented by keys and links, not by copying all lower-level information into one row. Institutional attributes characterize intermediaries; mechanisms characterize transformations; configurations characterize relationships among mechanism events; capacities will be separately derived from configurations; outcomes remain outside these legal-design observations.

This is the researcher's proposed solution to the design problem of how dimensions fit together and how research questions should prioritize classification. It is not represented as David's endorsed model.

## 3. Units of analysis

The authoritative units are:

1. `LAW` — one instrument;
2. `LAW × ACTOR` — one actor within one instrument;
3. `LAW × INTERMEDIARY` — one adjudicated intermediary within one instrument;
4. `LAW × R–I–T RELATION` — one adjudicated regulatory relation;
5. `RELATION × INTERMEDIARY × TRANSFORMATION` — one mechanism event;
6. `SUPPORTED RELATION` — one mechanism configuration;
7. `DIRECTED EVENT DEPENDENCY` — one mechanism edge;
8. `ANALYTICAL CLAIM × LEGAL EVIDENCE` — one evidence record;
9. `ANALYTICAL DECISION` — one review/adjudication record;
10. `CAPACITY CLAIM` — future derived unit;
11. `ARCHITECTURAL COMPARISON` — future comparative unit, not yet designed substantively.

Counts and authoritative tables appear in `R3_ANALYTICAL_UNIT_MATRIX.csv`.

## 4. Table architecture

### INSTRUMENT

One row per law. Stores identity, legal type and date, regulatory objective/object, targets, authorities, scope, obligation clusters, governance components, structural logic, and declared orientation. Source: Phase 3.

### ACTOR

One row per LAW × ACTOR. Stores law-scoped actor identity and institutional descriptors before regulatory-role assignment. A cross-law actor key permits comparison without merging legally distinct records. Source: Phase 4.

### LAW_INTERMEDIARY

One row per LAW × INTERMEDIARY. This is the principal human-facing comparative unit. It stores institutionalization, participation, separation, independence, orientation, contribution, outputs, legal effect, accountability, and derived structural counts. Mechanism codes are not authoritative here; any mechanism summary is derived from child events. Source: Phase 7 plus derived Phase 9 counts.

### REGULATORY_RELATION

One row per adjudicated relation. It retains all 56 relations and their final classes: 24 `DIRECT_R_T`, 23 `LEGAL_RELATION_NON_RIT`, and 9 `SUPPORTED_INTERMEDIATION`. R, I, and T reference ACTOR records. The LAW_INTERMEDIARY link is mandatory for supported intermediation and null for relations without an adjudicated intermediary. Source: Phase 6B.

### MECHANISM_EVENT

One row per elementary transformation within a supported relation. It is the authoritative mechanism table and stores input, mediated object, transformation, output, recipient, regulatory connection, final mechanism, family status, evidence, and decision provenance. The current ontology has ten provisional mechanisms; `IMPLEMENTATION` remains `FAMILY_UNASSIGNED_PROVISIONAL`. Source: Phase 8C.

### MECHANISM_CONFIGURATION

Exactly one row per supported relation. It represents whether the relation is single, parallel, sequential, mixed, or order-unresolved and links to its event set. Counts and mechanism-code lists are derived summaries, not independent coding. Source: Phase 9.

### MECHANISM_EDGE

One row per confirmed directed dependency between mechanism events. It stores transferred object, dependency, evidence level, and legal evidence. Zero edges are permitted. The current universe contains one edge. Source: Phase 9.

### LEGAL_EVIDENCE

One row per analytical claim × legal-evidence item. It normalizes evidence currently distributed across actor maps, relation evidence, mechanism traces, configuration traces, source provisions, and source anchors. Existing provenance tables remain preserved; migration adds a common backbone rather than replacing historical records.

### DECISION_PROVENANCE

One row per analytical decision. It distinguishes initial model coding, adversarial result, researcher value, final value, owner, rationale, source, and date. It must preserve `R3-D08-IMPLEMENTATION` and the Phase 8 → Phase 8B → researcher → Phase 8C sequence.

### REGULATORY_CAPACITY

Empty future-derived layer. Its schema can relate a future capacity proposition to events and configurations while recording derivation rule, empirical and theoretical basis, alternatives, confidence, and researcher adjudication. No `KNOWING`, `ASSURING`, or `STEERING` value is populated in Phase 10.

## 5. Relationships between tables

Primary relationships are key-based and one-to-many except where noted:

- LAW 1 → N ACTOR;
- LAW 1 → N LAW_INTERMEDIARY;
- LAW 1 → N REGULATORY_RELATION;
- ACTOR 1 → N role references as R, I, or T;
- LAW_INTERMEDIARY 1 → N supported REGULATORY_RELATION;
- supported REGULATORY_RELATION 1 → N MECHANISM_EVENT;
- supported REGULATORY_RELATION 1 → 1 MECHANISM_CONFIGURATION;
- MECHANISM_CONFIGURATION 1 → 0..N MECHANISM_EDGE;
- MECHANISM_EVENT 1 → 0..N incoming/outgoing MECHANISM_EDGE references;
- any empirical analytical unit 1 → N LEGAL_EVIDENCE;
- an analytical unit 1 → 0..N DECISION_PROVENANCE;
- MECHANISM_CONFIGURATION 1 → 0..N future REGULATORY_CAPACITY claims.

The detailed key and optionality rules are in `R3_ENTITY_RELATIONSHIP_SPEC.md`.

## 6. Primary and secondary units

`LAW × INTERMEDIARY` is the primary human-facing comparison because it brings institutional characteristics and structural participation together at a readable level. It is not the sole source of truth.

Secondary authoritative units answer different questions:

- ACTOR defines the institutional universe;
- REGULATORY_RELATION defines who regulates whom through whom;
- MECHANISM_EVENT defines how I transforms an input into an output;
- MECHANISM_CONFIGURATION defines how events relate within one relation;
- MECHANISM_EDGE defines supported sequence dependencies;
- INSTRUMENT supplies law-level context;
- evidence and decision records establish auditability.

## 7. Variable hierarchy

Variables are prioritized as:

- `CORE`: required to answer at least one mapped research question;
- `EXPLANATORY`: institutional or legal-design attributes that may explain variation;
- `PROVENANCE`: legal support and adjudication history;
- `DERIVED`: reproducible summaries computed from lower-level records;
- `FUTURE_THEORETICAL`: fields reserved for later capacity testing;
- `DROP_CANDIDATE`: fields lacking a clear analytical purpose or superseded by normalized records.

Recommendations distinguish `KEEP`, `NORMALIZE`, `DERIVE`, `MERGE_CANDIDATE`, `DROP_CANDIDATE`, and `FUTURE_LAYER`. Phase 10 deletes nothing. The complete register is `R3_VARIABLE_PRIORITY_REGISTER.csv`.

## 8. Evidence architecture

LEGAL_EVIDENCE becomes a polymorphic evidence backbone through `analytical_unit_type` and `analytical_unit_id`. Each row identifies the supported variable and value, CELEX act, provision, exact source anchor, evidence type, and interpretive note.

This removes the need to treat semicolon-delimited provisions as the only audit trail while preserving every historical source table. Evidence normalization should be performed as a controlled migration with reconciliation totals by source table and analytical unit.

## 9. Decision provenance

DECISION_PROVENANCE is distinct from LEGAL_EVIDENCE: evidence supports a claim; a decision explains how competing claims became an authoritative value. A single unit may therefore have many evidence records and many decisions. `R3-D08-IMPLEMENTATION` remains explicitly researcher-owned, and the prior unresolved and codebook-boundary values remain queryable.

## 10. Negative cases

REGULATORY_RELATION retains all final classifications rather than only the nine positive relations. This permits comparison among:

- `SUPPORTED_INTERMEDIATION`;
- `DIRECT_R_T`;
- `LEGAL_RELATION_NON_RIT`;
- recorded boundary/review characteristics.

INSTRUMENT exists independently of positive children, so `32015D1814` remains a substantive zero. Positive mechanism tables link only to supported relations; zero and negative cases are not fabricated into mechanism records.

## 11. Capacity-layer placeholder

The future REGULATORY_CAPACITY table prevents circularity by requiring a capacity claim to state its derivation rule, empirical basis, theoretical basis, alternatives, confidence, and adjudication. Mechanism presence or sequence alone cannot automatically assign capacity. Outcomes are not fields in this layer and would require separate empirical observation beyond legal design.

## 12. Human-facing view for David

The recommended presentation is a grouped parent–child view:

- one visual group per LAW × INTERMEDIARY;
- one child row per supported relation;
- mechanism events displayed within each relation, with numbered sequence arrows only where an edge exists;
- institutional attributes shown once at group level;
- evidence and decision provenance available through concise references/drill-down;
- laws with no intermediary shown in a dedicated substantive-zero section.

This avoids misleading multi-value cells for R/T/mechanism combinations. A compact export may use controlled multi-value summaries, but every summary must be labeled derived and resolve to child records. Full specification: `R3_DAVID_DATASET_VIEW_SPEC.md`.

## 13. Five-case limitations

The five-law R3 supports schema validation, codebook calibration, identification of possible configurations, demonstration of relational structure, detailed process tracing, and hypothesis generation.

It does not support population-level frequency estimates, causal inference, general statistical association, latent-dimension validation, or claims that the observed mechanism repertoire/configurations are exhaustive.

## 14. Expansion to a larger population

Population expansion should preserve keys, controlled vocabularies, evidence anchors, decision states, zero laws, and negative relations. It should add coding-reliability procedures and versioned migrations before statistical work. With sufficient cases, descriptive cross-tabs, multilevel comparisons, sequence/network methods, or configurational analysis may become appropriate; Phase 10 performs none of these.

## 15. Why this design answers the research question

RQ-A is structurally answerable because each intermediary can be followed to each relation, transformation, mechanism, configuration, and confirmed dependency without conflating them. Cross-law and cross-intermediary summaries are reproducibly derived from lower-level records.

RQ-B is structurally analyzable later because configuration evidence and institutional attributes remain linked while capacity claims occupy a separate, auditable layer. The design therefore permits theoretical inference without pre-encoding the desired capacities.

Principal question test:

`RQ_A_RECONSTRUCTABLE_FROM_SCHEMA_AND_CODED_DATA = YES`

`RQ_B_LATER_ANALYZABLE_WITHOUT_PRIOR_CAPACITY_ENCODING = YES`
