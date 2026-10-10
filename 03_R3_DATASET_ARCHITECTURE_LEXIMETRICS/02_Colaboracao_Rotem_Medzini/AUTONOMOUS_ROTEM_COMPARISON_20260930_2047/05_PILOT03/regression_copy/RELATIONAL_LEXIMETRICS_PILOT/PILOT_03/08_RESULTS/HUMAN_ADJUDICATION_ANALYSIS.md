# HUMAN_ADJUDICATION_ANALYSIS

## Validation

- Total adjudicated items: **19**.
- Decision IDs: H_001–H_019, unique and complete.
- Status: 19/19 `ADJUDICATED`.
- Provenance: 19/19 `HUMAN_ADJUDICATED`.
- Rationale: 19/19 present.
- Backward impact: **14** items.

## Decision distribution

| raw human_decision | n |
| --- | ---: |
| `OPTION_1` | 7 |
| `OPTION_2` | 9 |
| `BOTH_IN_PART` | 1 |
| `NEITHER` | 2 |
| qualified/custom human decision | 0 |

Substantive corrected outcomes with `UNRESOLVED` are **8**. They concern the candidate field/edge, not uncertainty about the whole legal act.

## Cause classification

| primary cause | decision IDs | n |
| --- | --- | ---: |
| `COMPOSITE_EDGE` | H_001, H_005, H_015, H_017 | 4 |
| `WRONG_RECIPIENT_OR_DIRECTION` | H_006, H_011 | 2 |
| `CANDIDATE_OPTIONS_MISSPECIFIED` | H_007, H_016 | 2 |
| `ACTION_NORMALIZATION_ERROR` | H_008 | 1 |
| `INTERMEDIARY_STATUS_OVERATTRIBUTION` | H_009, H_010, H_018, H_019 | 4 |
| `FUNCTION_MECHANISM_BOUNDARY` | H_003, H_012, H_013, H_014 | 4 |
| `MODALITY_OR_CONDITIONALITY` | H_002, H_004 | 2 |

The 19 items therefore do not represent 19 equivalent coder disagreements. Nine are primarily edge construction, recipient/direction or candidate-option problems; four are intermediary-status over-attribution; four refine Function × Mechanism × Device boundaries; and two refine modality/conditional instantiation. Six items (H_002–H_004 and H_012–H_014) are the main ontology-rule refinement set.

## Model reassessment

1. The binary primitive becomes more defensible: adjudication repeatedly required separating actor, recipient, direction and action rather than abandoning the edge model.
2. Nine disagreements would disappear or materially change after action-recipient alignment and elementary-edge decomposition.
3. Derived relationship families are preferable for higher-order classification, while `RELATIONSHIP_TYPE_DIRECT` should remain as an audit/descriptive field.
4. Stable enough for extended validation: act/provision anchoring, Actor A/B, verbatim action, object, direction, modality, and evidence provenance.
5. Requires further calibration within the extended validation: legal-effect representation, conditional intermediary positions, R–I–T composition, relationship-family derivation, and higher-order strategy/architecture fields.

## Reliability boundary

The pre-adjudication model-model comparison remains descriptive. The completed stage is one human adjudication layer applied to disagreements from two independent model passes. It is **not human intercoder reliability**.
