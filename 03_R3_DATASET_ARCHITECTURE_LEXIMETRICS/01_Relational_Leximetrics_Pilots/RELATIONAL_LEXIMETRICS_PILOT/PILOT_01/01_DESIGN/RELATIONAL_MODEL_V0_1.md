# Relational Leximetrics Pilot 01 — Relational Model v0.1

## Scope and status

This is an isolated methodological pilot. It does not modify the production dataset, the official codebook, or the source workbook. It tests whether five already assessed rows in Rotem Medzini's current workbook can be represented as provision-anchored directed relationships.

The candidate unit is a legally constituted relationship, represented provisionally as:

`ACT × PROVISION × OBJECT × ACTOR_A × FUNCTION × MECHANISM × RELATIONSHIP_TYPE × ACTOR_B`

An intermediary is represented as an actor position (`ACTOR_I`) when the source supports a distinct third actor. A provision may support several relationships, and one relationship may require several evidence provisions.

## Analytical layers

**Layer A — OBSERVED.** Act, provision reference, actor identity, legally expressed action, direction, modal character, and supporting text or normalized source statement.

**Layer B — CODED.** Object, function, mechanism, relationship type, institutional type, authority, discretion, accountability, transparency, contestability and related classifications. Every coded value must point to Layer A evidence.

**Layer C — INFERRED.** Regulatory intermediation, R–I–T configurations, strategies, architectures and governance logics. These are derived from combinations of Layer A and B; they are not directly coded from an isolated phrase.

## Entity definitions

| Entity | Provisional definition |
|---|---|
| ACTS | One row per legal act, with stable identifier and act-level attributes. |
| PROVISIONS | One row per addressable article, paragraph, subparagraph, annex or other textual unit. |
| ACTORS | One row per legally identifiable actor/category; identity is distinct from role. |
| RELATIONSHIPS | One row per directed legally constituted connection, with A, optional I and B positions. |
| RELATIONSHIP_EVIDENCE | Many-to-many link between relationship claims and provisions/source statements. |
| RELATIONSHIP_CODING | Coded object, function, mechanism, instrument/device and relational attributes. |
| INTERMEDIARY_REGISTER | Derived/consolidated view of actors that perform intermediary work across relationships. |
| ARCHITECTURE_INFERENCE | Higher-order configurations derived from the relationship layer. |
| CODING_DECISIONS | Provenance for existing, pilot, derived and adjudicated decisions. |

## Preliminary relationship ontology

The pilot distinguishes `R_I_T`, `R_T`, `I_T`, `R_I`, `I_R`, and `ACTOR_TO_ACTOR_UNRESOLVED` as relationship forms. `R_I_T` is used only where a regulator, a distinct intermediary and a target are all supported. A chain is not assumed merely because an actor is institutionally important.

Actions are retained as verb phrases (`designate`, `issue`, `assess`, `audit`, `report`, `adjudicate`, `provide coverage`) before standardization. Functions answer what regulatory work is performed; mechanisms answer how influence is exercised; instruments/devices identify the concrete legal or institutional carrier (certificate, audit, registry, escrow, ADR procedure, etc.).

## Actor identity and relational role

`ACTOR_IDENTITY` is stable within the pilot only as a label for the legally identifiable actor/category. `RELATIONAL_ROLE` is relationship-specific and may be regulator, intermediary, target, beneficiary, recipient or another position. `INSTITUTIONAL_CONTEXT` is stored separately because a public authority, private body, registry or self-regulatory body can occupy different positions in different edges.

## Inference rules

1. Create an observed edge only where the current dataset supplies an action and a legal reference or an explicit limitation is recorded.
2. Split a flat record when actor, action, object, recipient, or legal device changes.
3. Link multiple provisions to one edge rather than duplicating the edge.
4. Do not infer implementation practice, effectiveness, or governance logic from formal legal text.
5. Treat function/mechanism duplication as an issue, not as a reason to silently normalize the taxonomy.
6. Preserve the original value and the pilot value side by side; `MODEL_PILOT` never overwrites `HUMAN_EXISTING`.

## Unresolved conceptual questions

- Whether assurance is a function, a mechanism family, or a result of verification/testing.
- Whether audit is a distinct mechanism when it performs monitoring and assurance simultaneously.
- Whether insurance companies are regulatory intermediaries or supporting institutional devices in the electromagnetic-compatibility case.
- Whether a self-regulatory body named as an alternative to an external auditor should be one actor category or an unresolved branch.
- Whether `R_I_T` should be mandatory for an intermediary claim, or whether `I_T` and `R_I` edges can establish the configuration compositionally.
- Whether the current codebook's act-level self-regulation fields can be derived without importing operational assumptions.

The pilot contains 5 cases, 20 provisional relationship rows, and 20 evidence links. These are not production counts and must not be generalized.
