# RELATIONAL_MODEL_V0_2

## Status

Provisional output of PILOT_02. Not a production codebook and not a replacement for Rotem's workbook.

## Minimal normalized core

1. `ACTS` — one row per act.
2. `PROVISIONS` — one row per addressable provision with official locator and excerpt.
3. `ACTORS` — verbatim legal identity/category, normalized identity, institutional context.
4. `BINARY_RELATIONSHIPS` — one row per provision-supported directed A→B edge.
5. `RELATIONSHIP_EVIDENCE` — many-to-many provision links.
6. `RELATIONSHIP_CODING` — action, object, function, mechanism, device, relationship type, modality and evidence status.
7. `CONFIGURATION_LINKS` — derived links that compose R→I and I→T into an R–I–T view; never replace the binary evidence.
8. `INTERMEDIARY_REGISTER` — derived view of an actor's intermediary positions, not a fixed actor property.
9. `ADJUDICATION_REGISTER` — coder disagreement and provenance.

## Core rule

Use the binary relationship as the primitive. Expose `ACTOR_I` only as a derived configuration position when two or more elementary edges support it. Keep Device/Instrument separate because it carries concrete legal effects and is not interchangeable with Function or Mechanism.

## Explicit uncertainty

Function/mechanism collapse, conditional audit/supervision and supporting devices remain unresolved. No new production mechanism category is authorized by this model.
