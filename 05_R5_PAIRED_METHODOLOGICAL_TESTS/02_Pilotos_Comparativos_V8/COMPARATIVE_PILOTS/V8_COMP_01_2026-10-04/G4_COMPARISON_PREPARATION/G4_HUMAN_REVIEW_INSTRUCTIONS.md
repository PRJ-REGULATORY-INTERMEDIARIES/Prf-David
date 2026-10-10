# G4 — Human review instrument: instructions for reviewers

**File to complete:** `G4_HUMAN_REVIEW_TEMPLATE.csv` (one row per review item).
**Not given to reviewers:** `G4_HUMAN_REVIEW_MAPPING_KEY_SEALED.csv` (identity of the system and method behind each item). It is held separately and opened only after all ratings are returned.
**Status:** instrument prepared 2026-10-04; **no human evaluation has been collected; none has been simulated.**

## What you are reviewing

Each row is a case-level **architecture decision** from one analysis of the same frozen legal evidence: either a claim that a governance architecture is supported, or a decision to stop at a lower level. Both are equally valid outcomes; do not assume that a claim is better than a stop, or the reverse. Cell-internal reference codes have been replaced by `[ref]`; statement IDs (CS-P03-xxx, CS-P04-xxx) are the shared evidence IDs and are kept.

Every item of the same case shows the **same legal evidence** (all frozen statements of that case, exact excerpts). Judge only on that evidence.

## Scope rule you must apply

You may rely on the frozen excerpts shown. You may read the cited statute elsewhere only (a) to identify what a quoted cross-reference or anaphor points to, or (b) as background. If a claim needs a party, action, object, purpose, condition or consequence that appears **only** in text outside the excerpts, mark `beyond_frozen_evidence_used = YES` and say what it is.

## Criteria (one rating per item; the notes columns are optional but encouraged)

| Column | Question | Allowed values |
|---|---|---|
| A_fidelity_to_evidence | Is every element of the claim in the frozen excerpts (modality, condition, actor preserved)? | `FAITHFUL` · `PARTLY_UNSUPPORTED` · `UNSUPPORTED` · `CANNOT_JUDGE` |
| B_relational_classification_defensible | Are the relationships the item relies on (parties, direction, type) defensible on the excerpts? | `DEFENSIBLE` · `DEFENSIBLE_BUT_ALTERNATIVE_READING` · `NOT_DEFENSIBLE` · `CANNOT_JUDGE` |
| C_unsupported_edge_or_inferred_actor | Does the item promote a one-sided duty, a shared actor or co-occurrence to a relation, or supply an actor the text does not express? | `NO` · `YES` · `UNSURE` |
| D_stops_at_supported_level | Does the item stop at the highest level the evidence supports (statement / relation / configuration / architecture / regime)? | `STOPS_AT_SUPPORTED_LEVEL` · `GOES_TOO_FAR` · `STOPS_TOO_EARLY` · `UNSURE` |
| E_traceable_to_legal_anchors | Can you follow the claim back to specific statements and provisions from what the item shows? | `FULLY` · `PARTLY` · `NOT_TRACEABLE` |
| F_uncertainty_treated_appropriately | Are ambiguities (e.g. unexpressed actors, missing consequences) preserved rather than resolved by assumption? | `APPROPRIATE` · `PARTLY` · `INAPPROPRIATE` · `UNSURE` |
| your_own_highest_supported_level_for_this_case | Independently of the item, what is the highest level you would support on this evidence? | `statement` · `relation` · `configuration` · `architecture` · `regime` · `UNSURE` |
| uncertainty_level_of_your_rating | Your confidence in this row | `LOW` · `MEDIUM` · `HIGH` (HIGH = very uncertain) |

Also fill `reviewer_id` (your code, not necessarily your name), `review_date`, `time_spent_minutes` and `legal_expertise_self_rating` (free text or `EU_LAW` / `REGULATION` / `GOVERNANCE_THEORY` / `OTHER`).

## What is **not** a criterion

Length, style, vocabulary, number of configurations or relationships, how many alternatives are listed, or whether you agree with the item's conclusion. Do not try to guess which system or method produced the text; if you believe you can tell, say so in `free_comments` (this is itself information about the anonymisation).

## Known limits of the anonymisation

Identifiers and method/track labels were removed mechanically; wording and structure were not altered. Some items contain tell-tale content (for example sensitivity analysis, positional or part–whole vocabulary, differing length). The mapping key is sealed but the anonymisation is partial; a reviewer's guess of provenance should be recorded rather than suppressed.

## Procedure

Review items in the order shown (already shuffled; seed in the preparation record). Complete each row before opening the next. Do not discuss items with other reviewers until all ratings are returned. Independent review by at least two reviewers is recommended; disagreements are to be reported, not averaged away.

## Tier note

This version contains **Tier 1** only (8 case-level architecture decisions). Tier 2 (configuration-level and relation-level claims, including pairs selected by the claim-matching rules) is added at G4 step 1 under the same template.
