# Rotem to relational crosswalk

The CSV is the variable-level register. No source field is deleted; each is assigned a provisional treatment.

| Treatment | Fields |
|---|---:|
| `DERIVE_FROM_RELATIONSHIPS` | 13 |
| `MOVE_TO_ACTOR_TABLE` | 10 |
| `MOVE_TO_ACT_TABLE` | 37 |
| `MOVE_TO_PROVISION_EVIDENCE_TABLE` | 5 |
| `MOVE_TO_RELATIONSHIP_TABLE` | 20 |
| `RETAIN_DIRECTLY` | 49 |
| `RETAIN_WITH_REDEFINITION` | 35 |
| `UNRESOLVED` | 1 |

## Interpretation

Act-level variables move to ACTS; actor and role values separate into ACTORS and RELATIONSHIPS; legal references become many-to-many evidence; strategies and architectures are derived after lower-level coding; unresolved or ambiguous fields remain explicit.
