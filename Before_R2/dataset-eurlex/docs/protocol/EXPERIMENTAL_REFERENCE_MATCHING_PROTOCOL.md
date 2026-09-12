# Experimental reference-matching protocol

**Status:** prospective and frozen before any G0, G1, or G2 run  
**Scope:** post-run comparison only; no reference candidate information is supplied to an experimental condition

This protocol defines how experimental relations will be matched to the complete frozen reference corpus after reference lock and after the experimental outputs are available. It does not create, expose, or preselect experimental candidate locations.

## Inputs and unit of matching

The matching inputs are the complete frozen reference benchmark and one raw, validated experimental output for a condition. The reference may contain reference-only identifiers; these identifiers are comparison-artifact metadata and are never sent to G0, G1, or G2. `relation_id` is run-local and is not assumed to identify a reference unit.

Matching is one-to-one. Each reference relation and each experimental relation can participate in at most one accepted match. Matching is performed independently for each condition using the same frozen rules.

## Matching rules

### 1. Exact-location matching

First normalize each structural location component (`article`, `paragraph`, `point`, `subparagraph`, and `recital`) by trimming surrounding whitespace, case-folding, and treating null and empty values as equivalent. An exact-location match has the same normalized complete coordinate tuple, with the same corpus/CELEX context. Missing coordinates do not match an otherwise populated coordinate.

An exact-location match is eligible only when the relation identity is not contradicted by the remaining coded fields. If multiple units share an exact location, apply the tie-breaking rules below; do not match all units to one another.

### 2. Hierarchical-location overlap

When exact location is unavailable, compare the ordered structural path from the most specific available component to its ancestors. A hierarchical overlap exists when one relation identifies an ancestor location and the other identifies a descendant within that same path, such as an article-level record and an article/paragraph/point record.

Hierarchical overlap is weaker than exact location. It is eligible only when actor/relation identity and evidence support the same provision. A shared article alone is insufficient. If more than one candidate remains eligible at the same overlap depth, the case is unresolved rather than automatically matched.

### 3. Actor and relation identity

For comparison, actor-label arrays are normalized by trimming, case-folding, and collapsing repeated whitespace. Ordering is ignored for equality; repeated labels remain visible in the raw output and are flagged during duplicate review. Identity is assessed separately for `R`, `I`, and `T`. Empty arrays mean that no actor was coded in that role and must not be treated as a wildcard actor.

Actor agreement is supporting evidence, not a requirement that a model reproduce the reference perfectly: omissions and over-inclusions in R/I/T remain scorable after a match. A relation-identity assessment also considers the coded action, object, mediating function, mechanism, decision, and evidence as available. Labels that are merely similar are not silently merged; semantic equivalence requires documented adjudication.

### 4. One-to-one matching

Construct all eligible reference–experimental pairs, rank them prospectively, and accept pairs in rank order while removing both units after acceptance. A unit already matched cannot be reused. Unmatched units remain explicit comparison records.

### 5. Duplicate handling

Preserve every raw row. Exact duplicate rows within a source are flagged using normalized location, actor arrays, action/object/function, mechanism, decision, and evidence. The matching index may represent an exact duplicate group once for unit-level comparison, but the raw duplicate count and member identifiers must be retained in the audit artifact.

Non-identical rows at the same location are not silently collapsed. They are separate units and are resolved by the one-to-one rules; unresolved cases go to manual review.

### 6. Split relations

A split relation occurs when one conceptual reference relation is represented by multiple experimental rows, or when one experimental row contains only a component of the reference relation. At most one component can match the reference unit. The selected component is the highest-ranked eligible row; additional components are retained as unmatched experimental relations and flagged `split_relation`. No many-to-one credit is assigned.

### 7. Merged relations

A merged relation occurs when one experimental row combines two or more distinct reference relations. It may match at most one reference unit. The highest-ranked compatible reference unit is matched; every other covered reference unit remains unmatched and is flagged `merged_relation`. No one-to-many credit is assigned.

### 8. Unmatched relations

Every experimental relation with no accepted pair is reported as an unmatched experimental relation. Every reference positive with no accepted pair is reported as an unmatched benchmark positive. These are not silently discarded and drive over-inclusion and omission reporting respectively. Non-positive reference units may also be retained in the audit trail but do not become benchmark positives merely because no experimental match exists.

## Deterministic ranking and tie-breaking

Eligible pairs are ranked by the following fixed priority, from strongest to weakest:

1. exact complete location;
2. hierarchical overlap with the greatest number of shared structural components;
3. exact agreement of the normalized actor sets in `R`, `I`, and `T`;
4. greatest actor-label overlap across `R`, `I`, and `T`;
5. agreement on action, object, mediating function, and mechanism;
6. greatest normalized evidence overlap, using location and text only as corroboration;
7. deterministic lexical order of the comparison-side stable unit key, then the raw row index.

The final key is only a deterministic tie-breaker; it is not substantive evidence of identity. Experimental `relation_id` values are used only within their run. If a tie remains after all fixed criteria, the pair is unresolved and is not auto-matched.

## Manual review and blinding

Manual review is permitted only for unresolved matching ambiguity, including competing same-location candidates, non-identical duplicates, split/merged relations, and possible semantic actor equivalence. Reviewers receive the relevant source evidence and anonymized comparison-side unit keys, but not the G0/G1/G2 condition label where blinding is possible. The condition label may be disclosed only when technically necessary for an audit, and that disclosure must be recorded.

Manual review cannot add a new candidate, alter the frozen benchmark, or use an experimental result to redefine the rules. Review decisions and reasons are recorded in the post-hoc matching artifact. The same decision rule is applied without condition-specific adjustment.
