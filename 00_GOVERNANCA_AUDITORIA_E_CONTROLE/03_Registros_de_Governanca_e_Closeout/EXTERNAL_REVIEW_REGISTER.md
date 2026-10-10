# External Review Register — ARQGOV

**Register date:** 2026-10-01
**Project state:** `EXTERNAL_REVIEW_PENDING`
**Dispatch source:** user report by Igor; local hold notice preserved

## Registered communication

| Field | Recorded value | Evidence status |
|---|---|---|
| Date | 2026-10-01 | User-reported and recorded in local notice |
| Recipients | David Levi-Faur; Rotem Medzini | User-reported; no Gmail audit available |
| Dispatch | `SENT — reported by Igor` | Not independently verified |
| Response | `EXTERNAL_REVIEW_PENDING` | Registered hold state |
| Materials described | David conceptual-architecture technical note; Rotem coding-calibration technical note; interactive ARQGOV model | Local draft archive and hold notice |
| Cover email | Earlier draft retained in archive | Not the certified final sent email |

## What is under review

### David stream

Review concerns the proposed reconstruction of the eight dimensions, the 83 conceptual-table entries, their relationships and incomplete operational definitions, and the interactive architecture. The review question is whether the interpretation faithfully represents the preliminary manuscript and whether proposed operationalizations should be accepted, revised or rejected by the author.

### Rotem stream

Review concerns the relationship between the revised regulatory-intermediation codebook and the documented pilot exercises. The registered record includes structural extraction, 19 human-adjudicated pilot decisions, 14 retrospective implications and the historical gate `ONTOLOGY_STABLE_WITH_REVISIONS`. It does not represent PILOT_03 as approved production coding or as two-model independent validation.

## Pending external decisions

| ID | Decision needed | Stream | Baseline to protect |
|---|---|---|---|
| ER-01 | Whether the conceptual architecture accurately reconstructs the manuscript's intended dimensions and relationships | David | Manuscript source and ARQGOV v1.2 snapshot |
| ER-02 | Which proposed operational definitions, if any, should be adopted by the author | David | Conceptual note and ontology snapshot |
| ER-03 | Whether the pilot's provision-linked layer is useful alongside intermediary × act coding | Rotem | Revised codebook and Rotem workbook |
| ER-04 | How identification basis, recognition pathway and structural reliance should be distinguished | Rotem / human project decision | PILOT_03 decisions and Rotem reply |
| ER-05 | How assurance, auditing, monitoring, evaluation and information transmission should be calibrated | Rotem / human project decision | Revised function rules and diagnostic cases |
| ER-06 | Whether any change is authorized before further coding or implementation | David and/or Rotem | All frozen baselines |

## Evidence and provenance rules

1. Treat each incoming response as a new immutable record with sender, date, channel and verbatim content.
2. Mark statements as author recommendations, methodological observations, questions, or our interpretations. Do not collapse those categories.
3. Do not add external feedback directly into a manuscript, ontology, codebook, dataset or production configuration.
4. Map every proposed change to the affected version, rule, field, source provision and historical records.
5. Preserve disagreements and unresolved questions instead of silently resolving them.
6. A new Codex or model interpretation is `MODEL_REVIEWED` or `CODEX_SYNTHESIS`; it is never `HUMAN_ADJUDICATED`.

## Unavailable or qualified documentary items

- The final transmitted email is not independently available; the local cover email is a draft archive.
- Gmail/Drive delivery and recipient access were not independently audited in this workspace.
- Earlier Igor comments to Rotem were not recovered in the prior project audit.
- The GitHub and GitHub Pages references were supplied as baseline pointers; the closeout does not claim a fresh live-site verification.
- The ARQGOV interactive model remains a proposed interpretation pending author review.
