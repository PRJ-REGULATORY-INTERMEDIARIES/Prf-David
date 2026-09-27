# R4.2D — Human diagnostic rule candidates

**Status:** `HUMAN_DIAGNOSTIC_CANDIDATE_RULES` — derived from 12 purposively selected, human-adjudicated cases. These are candidates for the controlled repair phase, not instructions already applied corpus-wide and not a finalized ontology.

1. `STRUCTURAL_EXTRACTION_MUST_PRESERVE_LEGAL_VERB` — Do not replace legal verbs with paraphrases or synonyms. For example, `shall consult` must not become `consult or hear`.
2. `PRESERVE_LEGAL_MODALITY` — Preserve `shall`, `should`, `may`, `must`, and complete deontic constructions.
3. `PRESERVE_MODAL_DEONTIC_LEXICAL_CONSTRUCTION` — Preserve constructions such as `should be entitled to charge`; do not reduce them to `charge`.
4. `ALLOW_NO_EXPLICIT_ACTOR` — A passive construction may legitimately have no explicit actor.
5. `DO_NOT_INFER_ACTOR_IN_PASSIVE_CONSTRUCTION` — Do not turn a beneficiary, nominal complement, or actor from an adjacent clause into an invented agent.
6. `PREPOSITION_DOES_NOT_IMPLY_RECIPIENT` — `to`, `from`, `with`, `with regard to`, `due regard to`, and `subject to` do not by themselves establish a counterpart or recipient.
7. `RELATIONAL_ENTITY_MUST_BE_ACTOR_CAPABLE` — A counterpart/recipient should normally be a person, organization, authority, institution, or other entity capable of occupying a relational position.
8. `EMBEDDED_SOURCE_RELATION_MUST_NOT_BE_PROMOTED` — A phrase such as `mandate received from the provider` does not make the provider the matrix proposition's counterpart/recipient.
9. `PROPOSITION_BOUNDARIES_MUST_BE_PRESERVED` — Do not combine actor/action/object/counterpart values from adjacent propositions.
10. `COORDINATED_PREDICATES_MUST_REMAIN_DISTINCT` — Keep distinct predicates such as `shall be considered to be` and `shall be subject to` analytically separate.
11. `DISCOURSE_ADVERB_IS_NOT_ACTION` — `also`, `further`, and `however` cannot alone fill the Action field.
12. `TEMPORAL_SPATIAL_MANNER_MODIFIERS_ARE_NOT_CORE_ACTION_OR_OBJECT` — Separate temporal context, spatial scope, manner, means, procedural context, and normative consideration from core action/object where possible.
13. `EXPLICIT_RELATIONAL_ACTOR_MUST_NOT_BE_DROPPED` — Preserve explicit relational entities, e.g. the supervisory authority in `consult the supervisory authority`, an individual/entity to be notified, or FRA/EDPS invitees.
14. `OBJECT_MUST_NOT_FUNCTION_AS_RESIDUAL_BUCKET` — Do not place action, recipient, counterpart, temporal context, spatial scope, manner, means, or adjacent-proposition material in Object merely because it remains unassigned.
15. `MODEL_DETECTION_PATTERN_DOES_NOT_EQUAL_HUMAN_ROOT_CAUSE` — Keep `MODEL_SELECTION_PATTERN` distinct from `HUMAN_DIAGNOSTIC_DEFECT_CLASS` and any human primary root-cause judgment.

## Use boundary

These candidates are to inform `R4.2E — CONTROLLED STRUCTURAL REPAIR` design. They have not been applied to the 1,404-row extraction, and they do not authorize corpus-wide repair, automatic recoding, R/I/T coding, mechanism coding, ROTEM consultation, or R4.3. Human raw decisions remain in the separate completed CSV; no historical Luna or Terra artifact is replaced.
