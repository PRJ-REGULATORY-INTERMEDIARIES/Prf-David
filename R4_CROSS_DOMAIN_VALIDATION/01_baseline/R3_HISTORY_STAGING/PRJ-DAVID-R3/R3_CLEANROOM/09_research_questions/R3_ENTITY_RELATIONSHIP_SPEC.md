# R3 Entity–Relationship Specification

## Scope

This is the proposed normalized analytical schema. It specifies structure only; it neither recodes R3 observations nor assigns regulatory capacities or architecture types.

## Textual ER representation

```text
LAW
  |
  +--< ACTOR
  |      ^
  |      | R_actor_id / I_actor_id / T_actor_id
  |      |
  +--< LAW_INTERMEDIARY >--1 ACTOR
  |          |
  |          +--< SUPPORTED REGULATORY_RELATION
  |                         |
  |                         +--< MECHANISM_EVENT
  |                         |        |\
  |                         |        | +--< LEGAL_EVIDENCE
  |                         |        | +--< DECISION_PROVENANCE
  |                         |        |
  |                         |        +--< MECHANISM_EDGE >--1 MECHANISM_EVENT
  |                         |
  |                         +--1 MECHANISM_CONFIGURATION
  |                                  |
  |                                  +--< MECHANISM_EDGE
  |                                  +--< FUTURE REGULATORY_CAPACITY
  |
  +--< ALL ADJUDICATED REGULATORY_RELATION
  |       (SUPPORTED_INTERMEDIATION / DIRECT_R_T / LEGAL_RELATION_NON_RIT)
  |
  +--< LEGAL_EVIDENCE
```

LEGAL_EVIDENCE and DECISION_PROVENANCE may reference multiple analytical entity types through a controlled `analytical_unit_type` plus `analytical_unit_id`. In a production database, typed junction tables or enforced composite references are preferable to an unconstrained polymorphic key.

## Entities, keys and links

### INSTRUMENT (`LAW`)

- primary key: `instrument_id`;
- alternate unique key: `celex_id`;
- mandatory parent: none;
- children: ACTOR, LAW_INTERMEDIARY, REGULATORY_RELATION;
- current cardinality: 5.

An instrument row is mandatory even when it has zero intermediary children. This represents substantive-zero laws.

### ACTOR (`LAW × ACTOR`)

- primary key: `actor_id`;
- foreign key: `instrument_id → INSTRUMENT.instrument_id`, mandatory;
- optional comparison key: `cross_law_actor_key`;
- referenced by REGULATORY_RELATION as R, I, and T;
- referenced by LAW_INTERMEDIARY through `intermediary_actor_id`;
- current cardinality: 89.

Actor records remain law-scoped. The same actor type or organization in two laws is not collapsed into one actor row.

### LAW_INTERMEDIARY (`LAW × INTERMEDIARY`)

- primary key: `law_intermediary_id`;
- foreign keys: `instrument_id → INSTRUMENT`; `intermediary_actor_id → ACTOR`, both mandatory;
- relationship: INSTRUMENT 1 → 0..N LAW_INTERMEDIARY;
- relationship: LAW_INTERMEDIARY 1 → 1..N supported REGULATORY_RELATION in the positive universe;
- current cardinality: 7.

Derived counts are computed from child relations/events and are never competing sources of truth.

### REGULATORY_RELATION (`LAW × R–I–T RELATION`)

- primary key: `relation_id`;
- foreign keys: `instrument_id`, `R_actor_id`, `T_actor_id`, mandatory;
- `I_actor_id`: mandatory for `SUPPORTED_INTERMEDIATION`, nullable otherwise where no I exists;
- `law_intermediary_id`: mandatory for `SUPPORTED_INTERMEDIATION`, null for non-supported classes;
- controlled final classes: `SUPPORTED_INTERMEDIATION`, `DIRECT_R_T`, `LEGAL_RELATION_NON_RIT`;
- relationship: supported relation 1 → 1..N MECHANISM_EVENT;
- relationship: supported relation 1 → 1 MECHANISM_CONFIGURATION;
- current cardinality: 56 total, 9 supported.

Mechanism analysis filters to supported relations, while the full table preserves negative baselines.

### MECHANISM_EVENT (`RELATION × INTERMEDIARY × TRANSFORMATION`)

- primary key: `mechanism_event_id`;
- mandatory foreign keys: `relation_id → supported REGULATORY_RELATION`; `law_intermediary_id → LAW_INTERMEDIARY`;
- relationship: event 1 → 1..N LEGAL_EVIDENCE in the authoritative target schema;
- relationship: event 1 → 0..N DECISION_PROVENANCE;
- relationship: event 1 → 0..N incoming and 0..N outgoing MECHANISM_EDGE references;
- current cardinality: 10.

`mechanism_code` stores the current final code. Prior values belong in DECISION_PROVENANCE. `mechanism_family` accepts `FAMILY_UNASSIGNED_PROVISIONAL` independently of mechanism code.

### MECHANISM_CONFIGURATION (`SUPPORTED RELATION`)

- primary key: `configuration_id`;
- unique mandatory foreign key: `relation_id → supported REGULATORY_RELATION`;
- cardinality: supported relation 1 ↔ 1 configuration;
- relationship: configuration 1 → 0..N MECHANISM_EDGE;
- current cardinality: 9.

Event membership should be derived by relation foreign key or represented in a junction if configurations later contain selected event subsets. `event_ids` is a derived display field.

### MECHANISM_EDGE (`DIRECTED EVENT DEPENDENCY`)

- primary key: `edge_id`;
- foreign keys: `relation_id`, `from_event_id`, `to_event_id`, all mandatory;
- constraint: both events must belong to the same `relation_id`;
- constraint: `from_event_id ≠ to_event_id`;
- relationship: each edge belongs to exactly one configuration;
- current cardinality: 1.

The database permits zero edges. Conceptual similarity across relations is not an edge.

### LEGAL_EVIDENCE (`ANALYTICAL CLAIM × LEGAL EVIDENCE`)

- primary key: `evidence_id`;
- controlled reference: `analytical_unit_type` + `analytical_unit_id`;
- law reference: `celex_id → INSTRUMENT.celex_id`;
- relationship: one analytical unit 1 → 0..N evidence records;
- current state: proposed normalization of distributed evidence, with no destructive migration.

The variable and coded value are stored so one unit may have distinct evidence for distinct claims. Every MECHANISM_EVENT must have at least one evidence row after migration; links for other unit types may remain optional where no evidence migration has yet been authorized.

### DECISION_PROVENANCE (`ANALYTICAL DECISION`)

- primary key: `decision_id` (or `decision_id + analytical_unit_id` where one decision affects multiple units);
- controlled reference: `analytical_unit_id` plus unit type in implementation;
- relationship: analytical unit 1 → 0..N decisions;
- conceptual many-to-many: one decision may affect N units and one unit may receive N decisions. A `DECISION_UNIT_LINK` junction is recommended in a physical implementation;
- current state: 10 event-provenance rows plus governance decisions.

This structure preserves `R3-D08-IMPLEMENTATION` without overwriting model/adversarial states.

### REGULATORY_CAPACITY (`FUTURE_DERIVED_ANALYTICAL_LAYER`)

- primary key: `capacity_id`;
- references: `analytical_unit_type`, `analytical_unit_id`, optional `configuration_id`;
- mechanism membership: N ↔ N through a future `CAPACITY_EVENT_LINK` or controlled `mechanism_event_ids` staging field;
- current cardinality: 0;
- mandatory before a future claim: derivation rule, empirical basis, theoretical basis, alternatives, confidence, and researcher adjudication.

No capacity vocabulary is populated in Phase 10.

## Cardinality summary

| Parent | Relationship | Child | Mandatory rule |
|---|---|---|---|
| LAW | 1 → N | ACTOR | every actor has one law |
| LAW | 1 → 0..N | LAW_INTERMEDIARY | zero permitted |
| LAW | 1 → N | REGULATORY_RELATION | every relation has one law |
| LAW_INTERMEDIARY | 1 → 1..N | supported REGULATORY_RELATION | required for positive units |
| REGULATORY_RELATION | 1 → 1..N | MECHANISM_EVENT | only supported relations; current minimum one |
| supported REGULATORY_RELATION | 1 → 1 | MECHANISM_CONFIGURATION | one configuration per supported relation |
| MECHANISM_CONFIGURATION | 1 → 0..N | MECHANISM_EDGE | zero is valid |
| MECHANISM_EVENT | 1 → 1..N | LEGAL_EVIDENCE | mandatory in target schema after reconciled migration |
| analytical unit | 1 → 0..N | DECISION_PROVENANCE | review-dependent |
| decision | N ↔ N | analytical unit | physical junction recommended |

## Derived relationships and integrity rules

- LAW_INTERMEDIARY counts derive from child relations/events.
- configuration mechanism sets derive from event codes; they are not independently editable.
- edge mechanism labels derive from referenced events.
- law-level configuration profiles derive through LAW → RELATION → EVENT/CONFIGURATION.
- display names derive from ACTOR where possible; IDs remain authoritative.
- zero counts derive through left joins, not synthetic child records.
- negative relations cannot receive mechanism events unless their final classification changes through a documented upstream decision.

## Authoritative versus human-facing structure

The normalized tables above are authoritative. A David-facing view may denormalize display names and derived summaries, but it must retain keys and child-row boundaries so that multi-relation and multi-event cases remain reversible.
