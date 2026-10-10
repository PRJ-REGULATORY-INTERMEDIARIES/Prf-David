# Human adjudication instructions — G4 Step 2A

## Purpose and scope

This package requests independent human decisions on the specified G4 claim, evidence-scope, and provisional-correspondence items. It is not a request to choose a preferred model or protocol, and AI agreement is not evidence of legal correctness.

The frozen comparison input is the 20-statement `COMMON_STATEMENT_REGISTER.csv` (SHA-256 `417A35A361E44F8BECFBD8FC39B34738C026591C59B7E837FDDF292F9EF3E77F`). Its legal cases are P03, Directive 91/263/EEC (CELEX 31991L0263), and P04, Regulation (EC) No 874/2004 (CELEX 32004R0874). The exact statement-level excerpts relevant to each item are reproduced in `HUMAN_ADJUDICATION_MASTER.csv` and the priority subset.

## How to review

1. Review each `review_item_id` independently. The identity key is restricted provenance material and must not be supplied to a blinded reviewer.
2. Assess the stated proposition against `exact_frozen_evidence`. Statement IDs identify the frozen anchors; they do not themselves prove a proposition.
3. Material expressly labelled `OUTSIDE_FROZEN_EVIDENCE` or `HISTORICAL ANALYTIC SCOPE NOTES` is contextual only. Keep it separate from the frozen input. Decide whether a proposition is supportable from the frozen text, whether a narrower text-grounded core can be separated, or whether the issue is indeterminate.
4. For correspondence items, decide whether propositions are the same, partly overlapping, distinct, cross-level, unmatched/non-comparable, or not determinable as appropriate. A relation is not equivalent to a configuration or architecture incorporating that relation. Do not force a match.
5. For legal relationships, identify the legally expressed actors, direction, action, modality, condition and legal consequence. Do not infer an actor-to-actor edge from co-occurrence or from an institutional assignment alone.
6. For configuration or architectural propositions, state which lower-level propositions and legal anchors support the conclusion. If the evidence warrants only a lower analytical level, say so and stop there.
7. Record a decision, confidence (1–5), concise reasoned justification, reviewer identity or documented reviewer code, and ISO date (`YYYY-MM-DD`). If a decision cannot responsibly be made, record `INDETERMINATE` or `ABSTAIN` with the reason; do not leave an item silently unanswered.

The interpretations shown in the package are review frames, not recommendations. No prior analytical label, majority, model consensus, or greater number of claims is to be treated as the correct legal answer. Do not edit frozen evidence, Step 1 or Step 2A outputs, or source files. Return a separately named, dated adjudication file so its provenance remains clear.

## Priority

`HUMAN_ADJUDICATION_P1.csv` contains seven priority-1 claim/scope items plus two correspondence cards explicitly dependent on P1 items. The latter are labelled `DEPENDENT_ON_P1_ITEM`; they are not reclassified as P1 claims. `HUMAN_ADJUDICATION_LOWER_PRIORITY.csv` contains the remaining 21 queue items and 11 correspondence cards. The master file contains all 41 items.
