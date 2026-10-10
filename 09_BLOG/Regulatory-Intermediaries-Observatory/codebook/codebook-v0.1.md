# Track B preliminary codebook

**DRAFT — NOT VALIDATED · version 0.1.0**

| Concept | Provisional rule and uncertainty handling |
|---|---|
| Episode | Bounded regulatory process/context with documented actors, functions and temporal scope. Split/merge rules await pilot review. |
| Actor | Identifiable person/organization/entity; preserve name, type, jurisdiction and external identifier when available. Do not merge similar names without evidence. |
| R role | Proposed rule-setting or regulatory responsibility within this episode, justified by documents. |
| I role | Proposed mediation function between regulatory actors/targets, demonstrated in context; institutional type is insufficient. |
| T role | Proposed regulated target in this episode; may play another role elsewhere. |
| Function | Describe supported activity, e.g. monitoring, certification, implementation, interpretation or expertise. These are candidate concepts, not established findings or a frozen vocabulary. |
| Relation | Directed from one contextual role to another in the same episode. Direction, function and rationale are explicit. |
| Instrument | Identifiable rule, standard or other regulatory instrument, connected to episodes through a many-to-many link. |
| Source | Documentary object with locator, access date, optional version/hash and rights note. |
| Evidence | Recoverable item reference plus observation and optional excerpt; do not conflate observation with inference. |
| Evidence mode | `explicit`: directly documented claim; `supported_inference`: reasoned inference from identified evidence; `contested`: unresolved competing interpretation. |
| Time | ISO date strings for known full dates, with NULL and temporal_note for unknown/partial dates. Do not invent a day/month. SQL checks interval order only; reviewers check semantic dates. |
| Confidence | low/medium/high/unknown, initially qualitative and uncalibrated. NULL means unrecorded. No numeric certainty is implied. |
| Status | candidate/coding/under_review/adjudicated/validated/rejected; validated requires documented human review, not only passing tests. |
| Decision | Append coder, reviewer, variable, value, outcome, rationale, date and version. Supersede corrections without deleting disagreement history. |
| Missingness | NULL = unknown/unrecorded, never no actor/no relation. Explain consequential uncertainty in records.uncertainty_note. |

Multiple intermediaries and multiple contextual roles are permitted. Each role/relation should be linked to evidence during coding; validated claims must have documentary support. Evidence modes apply to claims, not the source as a whole. Confidence and evidence mode are distinct: an explicit statement can still be unreliable or contested.

Review priorities: episode boundaries, role overlap, functional taxonomy, inference threshold, source triangulation, confidence calibration, temporal granularity and independence of coders. No definitions are frozen or scientifically approved. See `fields.md` for exact storage columns and `database/schema.sql` for executable constraints.
