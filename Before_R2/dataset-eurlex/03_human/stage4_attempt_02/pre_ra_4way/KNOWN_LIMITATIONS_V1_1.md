# Known limitations of methodology v1.1.0 for pre-RA comparison

This document is descriptive. It records limitations exposed by the four validated outputs and the locked v1.1.0 artifacts. It does not modify the codebook, schema, validator, candidate universe, or any coding.

## C, D, and the overloaded `I` field

The codebook distinguishes:

```text
C = existence of a distinct third actor
D = mediating regulatory function
```

Accordingly, `C=YES, D=NO` is conceptually possible. In `codebook.md`, condition C asks whether a third actor is analytically distinct from R and T, while condition D separately asks whether that actor performs a regulatory function mediating the R–T relationship.

The current `validate_reference_logic.py`, however, requires `I != null` whenever `C=YES`. As a result, `I` sometimes contains a third actor that the coding expressly did not recognize as a mediator (`D=NO`). This behavior is documented in the Claude validation logs and is present in the validated artifacts.

Consequences:

- `I != null` alone is not proof of intermediation;
- `D=YES` and `relational_result=positive` are more informative for identifying an affirmative mediated relationship;
- any conceptual correction belongs only in a future methodology v1.2.0, not in this preparation.

## Free-text actor roles

The schema requires each actor object to contain a free-text `role`. Literal equality of that prose confounds actor identity with drafting style. Structural placement already determines whether a label is proposed as R, I, or T, so the principal four-way signature compares normalized `label` sets only and never uses `actor.role`.

## Conservative normalization boundary

Normalization is restricted to Unicode NFKC, casefold, trimming, whitespace collapse, trivial punctuation normalization, and explicit mappings in `actor_label_aliases.yaml`. There is no fuzzy matching, silent entity resolution, or automatic splitting/merging of compound labels. Consequently, some remaining R/I/T disagreements may combine conceptual disagreement with non-trivial naming granularity; they are retained as disagreements for adjudicator review.

## Class imbalance and agreement

The negative class dominates all four codings. Observed agreement can therefore be high even when the rare positive sets are unstable. Every kappa is reported with observed agreement, and positive-set Jaccard is reported separately. Kappa can also be unstable or undefined when one or both coders use a category with near-zero prevalence.

## Screening status

`screening_status` is compared separately and is not part of the principal substantive signature. Differences in screening vocabulary do not automatically trigger a human gate when all four codings are negative, no relevant I/D or other substantive difference exists, and the candidate is not selected for the audit sample.

## Provenance and causal interpretation

The Terra artifacts do not machine-record exact model or effort, whereas the Claude manifests record a provider/model claim and a default effort setting. Platforms, model families, execution scaffolds, effort settings, correction histories, and provenance completeness differ. These differences prevent interpreting Terra × Claude disagreements as a pure causal effect of model architecture.

## Scope

The universe contains one act and 90 frozen candidates. The four outputs are independent construction replicas, not an adjudicated benchmark. No majority pattern is truth, no family is the default, and these descriptive metrics do not establish a winning model.
