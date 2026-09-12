# Legacy Pilot and Prospective Simplification

## Status and scope

This note preserves the methodological history of `dataset-eurlex`. It does not reinterpret, relabel, or overwrite any prior output. The earlier intensive architecture remains available for audit and is retained as a methodological pilot, calibration, and robustness exercise.

The project began with:

- candidate reconstruction;
- independent R1/R2 coding;
- Terra replication;
- Claude replication;
- four-way comparison;
- blinded research-assistant review; and
- a human-gate design.

That architecture was useful for calibration, but it was not selected as the production workflow for the three empirical cases.

## Methodological lessons retained

The pilot exposed useful risks and failure modes:

- lexical hit ≠ regulatory relationship;
- fragment blindness;
- role instability;
- target/object confusion;
- advice versus mediation;
- source-boundedness;
- model disagreement; and
- excessive operational complexity.

These lessons refine the protocol prospectively. They do not constitute retroactive corrections to the pilot's results.

## Production consequence

The new architecture simplifies execution while preserving the construct and audit trail:

```text
official EU act → frozen corpus → Claude primary coding
→ structured R-I-T matrix → Luna secondary review
→ researcher adjudication → final case dataset
```

`R = Regulator`, `I = Intermediary`, and `T = Target` remain relational roles rather than fixed attributes of actors. A third actor is an intermediary only when it performs a textually demonstrated mediating regulatory function. A keyword hit, actor mention, information, advice, or assistance is not sufficient; an object is not a target.

The exact methodological position is:

> The intensive multi-model exercise is retained as methodological calibration and robustness evidence. The production workflow is simplified to one primary LLM coder, one independent AI review layer, and researcher adjudication.

The simplification is prospective. It does not claim that the earlier pilot was a production run, and it does not treat Claude, Luna, a majority vote, or any previous label as ground truth.
