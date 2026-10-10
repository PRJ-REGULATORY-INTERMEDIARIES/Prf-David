# Coding procedure

**DRAFT — NOT VALIDATED**

Allocate an immutable record ID and create the typed row in the same transaction. Preserve source metadata and evidence locators before interpreting them. Record roles per episode and relationships between contextual roles. Each role/relation requires a rationale and explicit/supported_inference/contested classification. Link multiple supporting or contesting evidence items as appropriate, explaining each link. Never infer role from organization type alone.

Candidate → coding → under_review → adjudicated → validated is a proposed workflow; rejected is a retained disposition. SQL constrains labels, not the entire transition graph. Record each material decision in append-only `coding_decisions`, including variable, proposed value, coder, reviewer, rationale, outcome, date and codebook version. Correct by appending a superseding decision for the same record and variable, not overwriting prior reasoning. Record disagreement rather than suppressing it. Keep uncertainty notes and unknown values explicit.

A validated record requires a current unsuperseded validation decision. Human reviewers must check that the decision still supports the current record; exact-content public authorization provides an additional check at release time. The Phase 01 database is not an immutable event store or authentication system.
