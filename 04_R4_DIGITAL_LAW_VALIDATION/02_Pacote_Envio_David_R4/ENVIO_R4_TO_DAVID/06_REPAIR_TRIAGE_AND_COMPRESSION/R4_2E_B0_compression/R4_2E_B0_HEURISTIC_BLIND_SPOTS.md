# R4.2E-B0 — Heuristic blind spots

The deterministic R4.2E-A screen rediscovered 9 of the 12 known human defects by the original model-selection family. The three missed cases remain human-confirmed and authoritative. They are not population-statistical false negatives.

## R4_2D-QA2B-026 — proposition boundary / cross-proposition contamination

The extracted actor is a complement from a preceding transfer proposition, while the relevant later proposition is the Commission's decision to revoke. The role phrase naming a third country or international organisation is itself a plausible entity and a valid prepositional phrase; no local lexical test can tell that it belongs to another proposition. The heuristic screen did not reconstruct proposition anchors across the recital span, so its visible-field tests did not assign the relational pattern family.

## R4_2D-QA2B-056 — cross-proposition contamination / embedded actor-action structure

The populated relational text names a natural or legal person, an actor-capable entity, and therefore passes a lexical actor-capability screen. The defect is that the phrase belongs to an earlier advertising-transparency proposition, not the Commission invitation proposition. Detecting it requires source-location and proposition-to-field alignment, not a rule that treats `from` or a person phrase as erroneous.

## R4_2D-QA2B-089 — multi-proposition contamination / proposition-anchor failure

The Annex VII excerpt combines distant, separately numbered provisions. The extraction's actor fragment and counterpart phrase are each grammatically plausible locally; the source-layout and provision anchor mismatch is the defect. Local role-slot heuristics can fire on action/object boundaries yet fail to rediscover the original counterpart/recipient selection family. Detecting this needs layout-aware provision segmentation and cross-field source-position alignment.

## New detection-rule candidate (not adopted)

`NEW_DETECTION_RULE_CANDIDATE = CROSS_FIELD_SOURCE_ANCHOR_ALIGNMENT_CHECK`: compare the source position/proposition containing each extracted role span with the source position/proposition containing the extracted legal predicate. This is a detection candidate motivated by all three misses; it is not added to or substituted for the 15 human-derived repair rules. It requires testing on counterexamples before adoption.

This analysis motivates family-based interpretation and portable representative context. It does not justify automatic repair or treating heuristic hits as confirmed errors.