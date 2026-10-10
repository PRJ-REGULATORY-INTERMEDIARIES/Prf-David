# Screening codebook v4

Stage A1 is a salience screen, not a relationship decision. It writes one
row per provision and lexical signal with `screening_id`, CELEX, article,
paragraph, provision type, candidate mechanism, semantic role, entity form,
matched pattern, confidence and verbatim evidence.

`semantic_role` is one of `actor`, `mechanism`, `instrument` or `procedure`.
`entity_form` is orthogonal and may be `public_body`, `private_organization`,
`professional_body`, `committee`, `association`, `individual_role`,
`office`, `hybrid_body` or `other`; non-actor signals use `NA`. These fields
must not be collapsed into an intrinsic “intermediary” label.

The lexical families are reporting, certification, ranking/rating and
auditing. Anchor patterns are high confidence; generic patterns are low
confidence. The output is `data/screening_hits_v4.csv` and remains separate
from A2 semantic candidate detection and B2 relational adjudication.
