# Case QA report

## Scope and integrity

- Case: Directive 86/361/EEC, original frozen English corpus only.
- Legal source SHA-256 before analysis: `d3f55bd448695b2a5e2c5f9f9167f7f5027c9a80c609a80072439756e80d8c57`.
- Legal source SHA-256 after artifact creation: `d3f55bd448695b2a5e2c5f9f9167f7f5027c9a80c609a80072439756e80d8c57`.
- The common corpus was not modified. Only the four named V8 method sources and this case source were used. No browsing or other-case analytical output was used.

## Record counts

- Core Level I/II claims: 18 (C01–C18): 11 Level I and 7 Level II.
- Higher-order records: 3 (K01, A01, X01): 1 Level III configuration, 1 Level III formal architecture claim, and 1 Level III deferred claim.
- Claim register normalization: all 21 rows explicitly identify `case_id=CASE-31986L0361` and `analytical_level` (Level I, Level II, or Level III); values match `claim_level` throughout.
- Typed relations: 12 (R01–R12).
- Level III configurations: 1 (K01).
- Formal architecture claims: 1 (A01); deferred higher-order claim record: 1 (X01).
- Uncertainty records: 12 (U01–U12), explicitly mapped to all nine required categories: source/reference ambiguity (U08); actor ambiguity (U02, U07); action ambiguity (U09); counterparty ambiguity (U10); modality ambiguity (U04); condition ambiguity (U01, U12); cross-provision inference (U11); architectural inference (U05); and stopping-rule uncertainty (U06).
- Screened as not material in this case: source/reference ambiguity, action ambiguity, and counterparty ambiguity (U08–U10). These entries record the screening basis without inventing unresolved uncertainty.
- Traceability rows: 2 (K01 and A01).
- CSV files with no applicable rows: none. All case registers contain only case-specific records.

## Analytical conclusion

V8 warrants a bounded formal legal architecture: distributed conformity assurance under coordinated technical specification and national approval, with a Commission-level safeguard. It does not warrant operational, effectiveness, sector-wide regime, or overarching governance-logic conclusions. Recognition of test results is not conflated with the grant of type approval; committee opinion is not treated as binding; information duties are not automatically treated as accountability.

## Quality checks

- Every substantive higher-order claim has a trace path through relations to article-level legal evidence.
- Every relation is typed and records its modality/attribute boundary; normative assignments are not converted into unsupported dyadic edges.
- Uncertainty about actor identity, discretion, accountability, broader boundaries, and implementation is preserved.
- No frequency-based architectural inference or external factual claim is used.
- The detached freeze manifest records generated artifact hashes and the source/method input hashes.
