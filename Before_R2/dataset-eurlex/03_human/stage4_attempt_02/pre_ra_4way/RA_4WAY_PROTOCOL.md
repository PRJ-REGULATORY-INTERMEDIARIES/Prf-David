# Protocol for future blind four-way reference adjudication

Version: 1.0.0  
Status: specification only; RA not started; human gate not started.

## Governing principles

The four codings are symmetric, independent replicas of reference construction. Neither Terra nor Claude is a default reference. No provider family, model, replicate order, or majority is privileged. A `3/4` pattern is agreement information only; it is never an automatic truth rule.

The future RA adjudicator must decide each presented candidate again from authorized evidence and methodology v1.1.0. The adjudicator may accept, reject, or replace every proposal, with reasons. This protocol does not alter methodology v1.1.0.

## Blinding

The package builder will assign the four codings a cryptographically random permutation of `Coder A`, `Coder B`, `Coder C`, and `Coder D` only when an RA package is actually prepared. No mapping is generated in this pre-RA stage. The real mapping must be kept outside the RA-accessible package and inaccessible to the adjudicator until adjudication is closed.

The RA package must not disclose provider, model, family, original R1/R2 label, file path, execution metadata, or aggregate language such as “Claude majority” or “Terra majority”. It must not use free-text `actor.role` as an identifier or provider clue. The detailed field-level rules are in `RA_blinding_spec.yaml`.

## Candidate packet

For each candidate presented to RA, provide:

- candidate ID and source location;
- focal excerpt and parent context;
- authorized same-act context;
- canonical corpus when further consultation is necessary;
- codebook v1.1.0 and the reference schema;
- four anonymized coding proposals containing the same field set.

Coder-generated evidence prose is withheld from the blind packet because the canonical evidence is supplied once, identically, and prose style can reveal provenance. Original raw and validated files remain preserved for audit.

## Required RA record

RA must record:

- its own decision, including screening status, R/I/T, A–E, relational result, mechanism, and confidence;
- justification and evidence tied to the canonical source;
- the relationship between its decision and each of Coder A–D's proposals;
- the reason for accepting or rejecting competing interpretations.

RA must not report or use a provider-family majority. If several coders agree, that agreement can be described only as a feature of the proposals.

## Future human-gate inclusion rules

A candidate must enter the future human gate when at least one condition holds:

1. `positive` in any of the four replicas;
2. `conditional` in any replica;
3. `insufficient_evidence` in any replica;
4. `D=YES` in any replica;
5. divergence in `relational_result`;
6. substantive divergence in normalized I labels;
7. substantive divergence in normalized R/I/T in a case that is not unanimously negative;
8. the future RA records `confidence=low`;
9. the future RA differs from all replicas or from the largest agreement grouping among the replicas;
10. an auditable random sample of approximately 10% of candidates that are unanimously negative and have no other trigger, with a minimum of three candidates.

The empirically recalculated union of positives across the four replicas must enter the human gate. Its IDs are never hardcoded into this protocol; they are derived from the current outputs by the comparator.

The pre-RA comparator may reproducibly mark rules 1–7 and select the rule-10 audit sample using a SHA-256 ranking seeded from the four validated-output hashes and the protocol version. Rules 8–9 remain pending until RA exists. This selection prepares a future queue; it does not execute a human gate.

A candidate is not included automatically merely because `screening_status` differs if all four replicas are negative, no relevant I/D or other substantive divergence exists, and it is not selected under rule 10.

## Sequence and controls

1. Reconfirm protected hashes and the 90-ID universe.
2. Generate a fresh random A/B/C/D mapping and store it outside the RA-accessible package.
3. Build candidate packets without provider or family clues.
4. Have RA decide from evidence and codebook without majority adjudication.
5. Validate RA structurally without changing substantive decisions silently.
6. Add rule-8 and rule-9 cases to the already prepared rules 1–7/10 queue.
7. Execute the researcher human gate only after explicit authorization.
8. Lock a benchmark only after the human gate is completed and validated.

None of steps 2–8 has been executed by this preparation.
