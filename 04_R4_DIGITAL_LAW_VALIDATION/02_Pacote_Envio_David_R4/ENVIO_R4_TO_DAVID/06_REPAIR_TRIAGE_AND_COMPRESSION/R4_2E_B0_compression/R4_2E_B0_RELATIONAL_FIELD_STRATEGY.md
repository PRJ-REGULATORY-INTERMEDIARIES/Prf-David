# R4.2E-B0 — Relational field strategy

## Observed property in the frozen extraction

- Counterpart and recipient are both populated in 995 records.
- Counterpart-only: 0; recipient-only: 0.
- The populated values are identical in 995/995 jointly populated records.
- Therefore: `COUNTERPART_RECIPIENT_OPERATIONAL_REDUNDANCY = OBSERVED_IN_CURRENT_EXTRACTION` and `CURRENT_EXTRACTION_PROVIDES_ZERO_OBSERVED_FIELD_DIFFERENTIATION_BETWEEN_COUNTERPART_AND_RECIPIENT_WHEN_POPULATED`.

This is an empirical property of the current extraction, not proof that the concepts are theoretically identical. The prior flag `COUNTERPART_RECIPIENT = VARIABLE_PARSIMONY_CANDIDATE` remains in force. Neither field is deleted or merged.

## Repair-review strategy

For any future case, inspect the relational phrase once in context, then record separate explicit decisions:

1. Is there an explicit actor-capable relational entity?
2. What grammatical/legal relation does it occupy?
3. Does that relation justify counterpart?
4. Does it justify recipient?
5. Does it justify both?
6. Does it justify neither?

Do not ask an advanced model to reread the same span twice because two dataset columns exist. Preserve a field-level rationale for each separate value. No relational field is changed in B0.