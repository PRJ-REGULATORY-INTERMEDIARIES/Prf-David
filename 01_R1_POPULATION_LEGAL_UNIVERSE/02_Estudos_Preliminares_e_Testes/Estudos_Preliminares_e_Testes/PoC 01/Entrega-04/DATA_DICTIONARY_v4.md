# Data dictionary v4

## Shared conventions

Missingness: `1` explicitly present, `0` explicitly absent, `NA` not
applicable, `UNK` unknown/insufficient information, `NOE` not observable from
legal text alone, `EXT` requiring external evidence. Observability:
`DIRECT`, `INFERRED`, `EXTERNAL`, `NOT_OBSERVABLE`.

## Dataset fields

| Dataset | Field | Meaning | Evidence / rule |
|---|---|---|---|
| screening | `screening_id` | Stable row identifier | unique within v4 output |
| screening | `source_celex`, `article` | Legal source and carrier article | linked to manifest and preserved HTML |
| screening | `candidate_mechanism`, `semantic_role` | Lexical signal and ontology | semantic role is actor, mechanism, instrument or procedure |
| screening | `entity_form` | Form of an actor mention | orthogonal: public_body, private_organization, professional_body, committee, association, individual_role, office, hybrid_body or other |
| screening | `screening_confidence` | Anchor/weak signal strength | high or low; not an adjudication |
| candidates | `relational_test_result` | Five-condition test result | positive, negative, conditional or insufficient_evidence |
| candidates | `construct_validity` | Status of the coding decision | confirmed for inherited v3; pending for new sample |
| candidates | `inclusion_decision` | Whether a candidate was promoted | only a human-approved positive can be included |
| relationships | `R_actor_id`, `I_actor_id`, `T_actor_id` | Foreign keys for the specific triad | all present, distinct and valid |
| relationships | `primary_mechanism`, `secondary_mechanism` | Mechanism(s) through which I mediates | primary requires functional justification; secondary is optional and uses `NA`, never blank |
| relationships | `intermediary_present` | Third actor mediates R-T | `1` only after all five conditions hold |
| relationships | `formal_role_present` | Role established in the act | direct legal evidence required |
| relationships | `participation_in_scheme_voluntary` | Joining scheme is optional | independent from mandatory use |
| relationships | `use_of_intermediary_mandatory` | Use required once scheme applies | independent from voluntary participation |
| relationships | `regulatory_level`, `sphere_primary` | Level and substantive sphere | free text when hybrid/multilevel |
| relationships | `motivation`, `centrality` | Institutional attribute families | `NOE` in this PoC; deferred rather than silently inferred |
| relationships | `mode_of_operation` | state/business/NGO/professional/hybrid resemblance | inferred, relationship-specific |
| relationships | `organizational_separation` | internal, external, hybrid or NA | inferred from institutional context |
| relationships | `legal_independence_required` | Explicit independence requirement | do not infer absence; use UNK/EXT |
| relationships | `supervision_present` | Named authority supervises intermediary | direct textual basis |
| relationships | `responsibilization_present`, `empowerment_present` | Independent strategy indicators | each uses `1`, `0`, `UNCLEAR` or `NOE`; no combined score |
| all | `verbatim_evidence` | Literal legal support | required for positive relationship rows |
| v4 provenance | `ai_assisted`, `ai_run_ref` | AI provenance if human promotes a row | no v4 row is AI-promoted in this run |
| v4 provenance | `run_id`, `model_snapshot`, `input_hash`, `output_hash`, `cost_estimate` | Per-call provenance | stored in `ai_runs_v4.csv` and JSONL |
| v4 structure | `rule_source_id`, `standard_setter_id`, `direct_regulator_id`, `oversight_authority_id`, `enforcement_authority_id` | Distinct institutional roles | `UNK` unless supported by supplied evidence |
| v4 structure | `nested_intermediation_present`, `chain_id`, `intermediation_level`, `parent_relationship_id`, `meta_regulatory_relation` | Nested governance | meta-relation only with a documented parent chain and evidence |
| actors | `actor_type_hint`, `role_scope` | Inherited descriptive hint | role-specific reference; not an intrinsic R/I/T type |

The full deferred autonomy/accountability battery remains a proposal queue;
it is not converted into indices or outcome claims.
