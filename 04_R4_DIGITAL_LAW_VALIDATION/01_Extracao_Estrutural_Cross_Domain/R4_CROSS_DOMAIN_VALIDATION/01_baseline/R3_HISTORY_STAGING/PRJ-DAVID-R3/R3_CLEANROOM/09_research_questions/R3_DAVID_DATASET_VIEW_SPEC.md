# R3 David-Facing Dataset View Specification

## Purpose

The David-facing view is a readable discussion layer over the normalized R3 dataset. It is not the analytical source of truth and is not yet the final David package.

## Primary human-facing unit

Use `LAW × INTERMEDIARY` as the parent visual unit because this is the level at which institutional identity, status, independence, accountability, orientation, outputs, and participation can be compared meaningfully across laws.

Do not use one fully flattened row per intermediary. One intermediary may participate in several R–I–T relations and may perform several mechanism events. Flattening would either duplicate institutional attributes or collapse distinct R/T/mechanism combinations into ambiguous cells.

## Recommended presentation: grouped parent–child rows

Each LAW × INTERMEDIARY group contains:

### Parent header

- Law;
- Intermediary;
- Institutional type;
- Institutionalization/participation;
- Independence;
- Orientation;
- Accountability;
- Output legal effect;
- number of supported relations and mechanism events.

### One child row per supported relation

- relation ID;
- R;
- target class;
- regulatory object and mediated object;
- relation purpose;
- output;
- configuration type;
- concise evidence reference.

### Mechanism subrows within each relation

- event ID and ordinal position;
- input → transformation → output;
- final mechanism code;
- family status;
- confirmation/decision source;
- source provision and anchor.

This format permits `32023R0955_LI_001` to display three separate target relations, each with one `IMPLEMENTATION` event, without implying a chain.

## Sequence representation

Where a confirmed edge exists, display an indented sequence under the relation:

`1. VERIFICATION → [audit findings and identified weaknesses] → 2. EVALUATION_ASSESSMENT`

Show the evidence level and legal provision beside the arrow. Do not draw arrows for repeated mechanisms across different relations or for unresolved ordering.

## Compact columns

The proposed visible columns are:

| Level | Fields |
|---|---|
| Parent | Law; Intermediary; Institutional type; Independence; Accountability; Orientation; Output legal effect |
| Relation child | R; Target class; Supported relation; Regulatory object; Output; Configuration |
| Event child | Mechanism; Input/transformation/output; Family; Evidence; Decision source |
| Note | Research note limited to uncertainty, provenance, or conceptual boundary |

Mechanism summaries at parent level may be shown as derived badges, but event rows remain authoritative.

## Multiple relations

Use child rows grouped visually under the same LAW × INTERMEDIARY. This is more defensible than a semicolon-delimited cell because it preserves each R/T/mechanism combination. Controlled multi-value cells are acceptable only in a compact index sheet and must link to the child view.

## Multiple mechanism events

Each event receives its own subrow. Relation-level configuration appears once. Event order is displayed only when supported by a MECHANISM_EDGE. The audit-body relation therefore contains two subrows and one documented arrow; it is not compressed into a compound mechanism label.

## Zero and negative cases

Provide two companion sections:

1. **Substantive-zero instruments:** include `32015D1814` with explicit zeros for intermediaries, supported relations, events, and configurations.
2. **Relation baseline:** summarize counts and permit drill-down into `DIRECT_R_T` and `LEGAL_RELATION_NON_RIT` records alongside supported intermediation.

Do not create placeholder intermediary rows for zero laws.

## Evidence exposure

The concise view shows provision and anchor references. A linked evidence sheet exposes evidence ID, claim/variable, coded value, provision, exact anchor, evidence type, and note. Evidence remains separate from the analytical value so multiple citations can support one claim.

## Decision provenance exposure

Use a visible source badge:

- `MODEL + PHASE 8B REVIEW` for unchanged adversarially confirmed events;
- `RESEARCHER DECISION R3-D08-IMPLEMENTATION` for the three implementation events.

A provenance drill-down shows initial, adversarial, researcher, and final values. This prevents researcher-added classifications from appearing model-derived or attributable to David.

## Visual and export rules

- Freeze parent identifiers and preserve stable IDs in hidden/secondary columns.
- Use indentation/grouping rather than merged cells that impede sorting.
- Keep controlled vocabularies unchanged.
- Label derived counts and summaries explicitly.
- Never use color alone to encode status.
- Permit filters by law, intermediary type, target class, mechanism, configuration, evidence level, and decision source.
- Keep capacity fields absent until a later authorized phase.

## What this view is designed to communicate

The view makes the analytical hierarchy visible:

`who I is → where I acts → how I acts → how events combine → what remains to be theorized`

It shows mechanisms and institutional attributes together without treating them as equivalent, and it shows configuration without prematurely naming a regulatory capacity or architecture.
