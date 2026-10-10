# Data dictionary

| Table | Key fields | Purpose |
|---|---|---|
| `sources` | source_id, CELEX, URI, official_journal, language, version_date, hash, retrieval_note | Documentary identity and integrity. |
| `legal_units` | unit_id, source_id, article, paragraph, point, text, parent_unit_id | Stable provision-level provenance. |
| `institutional_statements` | statement_id, unit_id, statement_text, modality, subject, action, object, status | Separates legal propositions within a unit. |
| `elements` | element_id, statement_id, element_type, value, boundary_status | Objects, actors/positions, functions, mechanisms and instruments. |
| `normative_assignments` | assignment_id, statement_id, subject_element, modality, action, object, counterpart_status | Preserves assignments without fabricating edges. |
| `relationships` | relation_id, type, origin, counterpart, direction, modality, condition, validity, coding_status | Qualified governance relations. |
| `relation_evidence` | relation_id, statement_id, support_role | Many-to-many evidence, including cross-provision support. |
| `attributes` | attribute_id, target_type, target_id, attribute_type, component, value, evidence | Authority, discretion and accountability components attached to a position, relationship or configuration where evidence supports that bearer. |
| `configurations` | config_id, question, scope, pattern, status | Candidate situated arrangements. |
| `configuration_members` | config_id, member_type, member_id, role | Many-to-many element/relation membership. |
| `architectural_claims` | claim_id, config_id, dimension, bearer, value, rule, uncertainty | Explicit architectural inference. |
| `regimes` / `regime_members` / `regime_relations` | regime_id, member, relation_type, evidence | Many-to-many regime analysis. |
| `adjudications` | issue_id, target_id, issue, alternatives, decision, reviewer | Human review and unresolved uncertainty. |

All IDs are stable strings. Evidence links are many-to-many. `coding_status` and `claim_level` prevent a machine suggestion or higher-order inference from masquerading as a direct legal observation.
