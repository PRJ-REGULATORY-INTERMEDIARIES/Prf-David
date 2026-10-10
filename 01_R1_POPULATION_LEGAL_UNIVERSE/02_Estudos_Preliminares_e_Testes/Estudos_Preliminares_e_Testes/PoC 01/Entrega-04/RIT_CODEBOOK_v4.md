# R-I-T codebook v4

This delivery retains the v3 operationalisation and applies it to a five-act
corpus. The theoretical construct is regulatory intermediation: a third actor
mediates a relationship between a rule-maker/regulator and a rule-taker/target.
The eight institutional attributes and the four mechanisms are operational
choices for this dataset, not claims that the proposal's ontology is
exhaustive.

## Five-condition relational test

For each candidate, code conditions independently and in order:

1. an identifiable regulator/rule-maker exists;
2. an identifiable target/rule-taker exists;
3. a third actor is analytically distinct from both;
4. that actor performs a regulatory function mediating the regulator-target
   relationship, rather than merely advising or receiving the same duty;
5. explicit legal text or a documented institutional reconstruction supports
   the relationship.

`positive` requires five YES answers. Any NO yields `negative`. An UNCLEAR
condition yields `conditional` or `insufficient_evidence`; it is never rounded
up to positive. Only positive cases enter `rit_relationships_v4.csv`.

## Mechanisms and strategies

The primary mechanisms are `reporting`, `certification`, `ranking_rating` and
`auditing`. `secondary_mechanism` allows stacked mechanisms (for example,
auditing plus certification). Reporting and intermediation are independent:
a direct reporting duty can be negative on the R-I-T test.

`responsibilization` and `empowerment` are independent future batteries; this
delivery does not collapse them into one strategy category. No index of
autonomy, accountability, effectiveness, legitimacy, trust or polycentricity
is produced.

Actor roles are relational, not intrinsic. Code `Role(actor, relationship)`;
do not treat an actor's R/I/T position in one relationship as a permanent
type. Keep rule source, standard setter, direct regulator, oversight authority,
enforcement authority, intermediary and target distinct where the evidence
allows. `R_actor_id` is the focal R role for the specific relationship.

The primary mechanism is the mechanism with the strongest functional support
in the legal evidence, not the mechanism with the most lexical hits. A second
mechanism is recorded only when it has separate functional support; otherwise
use `NA`. Do not infer strategy, capture, failure, autonomy or accountability
indices from a hit count.

## Normalisation rules

Actors are stored in `actors_v4.csv` and referenced by foreign keys. R, I and
T must be pairwise distinct within a relationship. Chains are decomposed into
separate rows with `chain_id`, `intermediation_level` and
`parent_relationship_id`; multiple roles are never compressed into one cell.
