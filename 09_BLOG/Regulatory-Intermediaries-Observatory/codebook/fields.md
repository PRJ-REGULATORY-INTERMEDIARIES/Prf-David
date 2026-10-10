# Storage field dictionary

**DRAFT — NOT VALIDATED · schema 0.1.0**

Generated from the executable schema. Shared workflow fields live in records; typed tables reference that immutable ID. NULL denotes unknown/unrecorded. Full CHECK constraints and compound foreign keys are authoritative in database/schema.sql.

## actors

| Field | Type | Required | Default | Primary key |
|---|---|---|---|---|
| id | TEXT | yes | — | 1 |
| name | TEXT | yes | — | — |
| actor_type | TEXT | no | — | — |
| jurisdiction | TEXT | no | — | — |
| external_identifier | TEXT | no | — | — |

- Foreign key: `id` → `records.id` (group 0, position 0).

## codebook_versions

| Field | Type | Required | Default | Primary key |
|---|---|---|---|---|
| version | TEXT | yes | — | 1 |
| description | TEXT | yes | — | — |


## coding_decisions

| Field | Type | Required | Default | Primary key |
|---|---|---|---|---|
| decision_id | TEXT | yes | — | 1 |
| record_id | TEXT | yes | — | — |
| variable | TEXT | yes | — | — |
| proposed_value | TEXT | no | — | — |
| coder | TEXT | yes | — | — |
| reviewer | TEXT | no | — | — |
| outcome | TEXT | yes | — | — |
| rationale | TEXT | yes | — | — |
| decided_on | TEXT | yes | — | — |
| supersedes_id | TEXT | no | — | — |
| codebook_version | TEXT | yes | — | — |

- Foreign key: `codebook_version` → `codebook_versions.version` (group 0, position 0).
- Foreign key: `supersedes_id` → `coding_decisions.decision_id` (group 1, position 0).
- Foreign key: `record_id` → `records.id` (group 2, position 0).

## datasets_catalog

| Field | Type | Required | Default | Primary key |
|---|---|---|---|---|
| id | TEXT | yes | — | 1 |
| title | TEXT | yes | — | — |
| provider | TEXT | no | — | — |
| url | TEXT | no | — | — |
| license | TEXT | no | — | — |
| coverage | TEXT | no | — | — |
| access_method | TEXT | no | — | — |
| version | TEXT | no | — | — |
| reviewed_on | TEXT | no | — | — |
| rit_relevance | TEXT | no | — | — |
| search_log_ref | TEXT | no | — | — |

- Foreign key: `id` → `records.id` (group 0, position 0).

## episode_instruments

| Field | Type | Required | Default | Primary key |
|---|---|---|---|---|
| episode_id | TEXT | yes | — | 1 |
| instrument_id | TEXT | yes | — | 2 |

- Foreign key: `instrument_id` → `instruments.id` (group 0, position 0).
- Foreign key: `episode_id` → `episodes.id` (group 1, position 0).

## episode_roles

| Field | Type | Required | Default | Primary key |
|---|---|---|---|---|
| id | TEXT | yes | — | 1 |
| episode_id | TEXT | yes | — | — |
| actor_id | TEXT | yes | — | — |
| role | TEXT | yes | — | — |
| function | TEXT | no | — | — |
| evidence_mode | TEXT | yes | — | — |
| rationale | TEXT | yes | — | — |
| confidence | TEXT | no | — | — |

- Foreign key: `actor_id` → `actors.id` (group 0, position 0).
- Foreign key: `episode_id` → `episodes.id` (group 1, position 0).
- Foreign key: `id` → `records.id` (group 2, position 0).

## episodes

| Field | Type | Required | Default | Primary key |
|---|---|---|---|---|
| id | TEXT | yes | — | 1 |
| title | TEXT | yes | — | — |
| domain | TEXT | no | — | — |
| jurisdiction | TEXT | no | — | — |
| start_date | TEXT | no | — | — |
| end_date | TEXT | no | — | — |
| temporal_note | TEXT | no | — | — |
| description | TEXT | yes | — | — |

- Foreign key: `id` → `records.id` (group 0, position 0).

## evidence

| Field | Type | Required | Default | Primary key |
|---|---|---|---|---|
| id | TEXT | yes | — | 1 |
| source_id | TEXT | yes | — | — |
| item_reference | TEXT | yes | — | — |
| excerpt | TEXT | no | — | — |
| observation | TEXT | yes | — | — |

- Foreign key: `source_id` → `sources.id` (group 0, position 0).
- Foreign key: `id` → `records.id` (group 1, position 0).

## evidence_links

| Field | Type | Required | Default | Primary key |
|---|---|---|---|---|
| record_id | TEXT | yes | — | 1 |
| evidence_id | TEXT | yes | — | 2 |
| support_note | TEXT | yes | — | — |

- Foreign key: `evidence_id` → `evidence.id` (group 0, position 0).
- Foreign key: `record_id` → `records.id` (group 1, position 0).

## instruments

| Field | Type | Required | Default | Primary key |
|---|---|---|---|---|
| id | TEXT | yes | — | 1 |
| title | TEXT | yes | — | — |
| instrument_type | TEXT | no | — | — |
| locator | TEXT | no | — | — |
| issued_on | TEXT | no | — | — |

- Foreign key: `id` → `records.id` (group 0, position 0).

## records

| Field | Type | Required | Default | Primary key |
|---|---|---|---|---|
| id | TEXT | yes | — | 1 |
| kind | TEXT | yes | — | — |
| status | TEXT | yes | 'candidate' | — |
| is_synthetic | INTEGER | yes | 0 | — |
| public_eligible | INTEGER | yes | 0 | — |
| schema_version | TEXT | yes | '0.1.0' | — |
| codebook_version | TEXT | yes | '0.1.0' | — |
| created_on | TEXT | yes | — | — |
| uncertainty_note | TEXT | no | — | — |

- Foreign key: `codebook_version` → `codebook_versions.version` (group 0, position 0).
- Foreign key: `schema_version` → `schema_versions.version` (group 1, position 0).

## relations

| Field | Type | Required | Default | Primary key |
|---|---|---|---|---|
| id | TEXT | yes | — | 1 |
| episode_id | TEXT | yes | — | — |
| from_role_id | TEXT | yes | — | — |
| to_role_id | TEXT | yes | — | — |
| function | TEXT | yes | — | — |
| evidence_mode | TEXT | yes | — | — |
| rationale | TEXT | yes | — | — |

- Foreign key: `to_role_id` → `episode_roles.id` (group 0, position 0).
- Foreign key: `episode_id` → `episode_roles.episode_id` (group 0, position 1).
- Foreign key: `from_role_id` → `episode_roles.id` (group 1, position 0).
- Foreign key: `episode_id` → `episode_roles.episode_id` (group 1, position 1).
- Foreign key: `episode_id` → `episodes.id` (group 2, position 0).
- Foreign key: `id` → `records.id` (group 3, position 0).

## schema_versions

| Field | Type | Required | Default | Primary key |
|---|---|---|---|---|
| version | TEXT | yes | — | 1 |
| applied_on | TEXT | yes | — | — |


## sources

| Field | Type | Required | Default | Primary key |
|---|---|---|---|---|
| id | TEXT | yes | — | 1 |
| title | TEXT | yes | — | — |
| locator | TEXT | yes | — | — |
| accessed_on | TEXT | yes | — | — |
| version | TEXT | no | — | — |
| sha256 | TEXT | no | — | — |
| rights_note | TEXT | no | — | — |

- Foreign key: `id` → `records.id` (group 0, position 0).

