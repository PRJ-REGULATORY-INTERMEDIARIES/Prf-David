# Common statement data dictionary

## Purpose and boundary

`COMMON_STATEMENT_REGISTER.csv` is the frozen neutral input for the prospective V8-COMP-01 A/B comparison. It records statement-sized observations from the ten verified legal anchors only. It is neither a historical Model A/B output nor an architectural, configurational, or relational conclusion.

| Field | Definition / permitted values |
|---|---|
| `statement_id` | Stable identifier: `CS-<case>-<three-digit number>`. |
| `case_id` | `P03` or `P04`; the authorized operational microcases only. |
| `CELEX` | Official CELEX legal identifier. |
| `legal_version` | Instrument identity and OJ publication version represented by the frozen official HTML. |
| `provision_anchor` | Historical anchor ID plus exact provision locator. It preserves provenance but does not import its historical normalized statement. |
| `exact_legal_excerpt` | Verbatim bounded legal text from FE-001 or FE-003. A sentence may be repeated where separate operative actions are registered. |
| `source_manifest_id` / `source_sha256` | Controlling primary source in `FROZEN_EVIDENCE_MANIFEST.csv`, and its verified hash. |
| `institutional_statement` | Neutral short label for retrieval; it adds no legal or architectural conclusion. |
| `actor` | Textually expressed actor, grammatical subject where the text provides one, or `NOT_EXPRESSED_IN_SENTENCE`. |
| `legal_modality` | Textual modal operator (`shall`, `must`, `may`) where present. |
| `action` | Literal operative verb or a minimal normalized form that does not add a relationship. |
| `object_or_recipient` | Textual object and/or explicit recipient. It is not an inferred edge. |
| `explicit_condition` | Express conditions, timing, qualifications, or alternatives only. |
| `segmentation_rationale` | Why a provision was divided or retained as one statement. |
| `uncertainty_flag` | `TRUE` if grammar, scope, or segmentation needs prospective attention; `FALSE` does not imply a Track A/B conclusion. |
| `evidence_completeness` | `FULL_PRIMARY_TEXT` when the bounded quotation is available in verified official HTML. |
| `human_review_status` | Provenance-only status. `HISTORICAL_HUMAN_REVIEW_AVAILABLE_NOT_APPLIED`, `HISTORICAL_CLASSIFICATION_AVAILABLE_NOT_APPLIED`, or `NO_CASE_SPECIFIC_HUMAN_ADJUDICATION`. |

## Exclusions and controls

- No field records centrality, configuration, architectural significance, cross-level inference, or an eight-operation outcome.
- `P04` Article 22(7) is expressly excluded: it remains contextual audit evidence and is not a common statement.
- Historical PILOT_03 Model A/B and adjudications may be consulted later as labeled reference material, but they do not determine this register’s values.
- Track A and Track B must use the exact same frozen register and controlling primary hashes. Track A must be completed and frozen before Track B begins.
