# Data architecture

**DRAFT — NOT VALIDATED · schema/codebook 0.1.0**

`records` is a shared identity/workflow registry; each row has exactly one intended typed record in `datasets_catalog`, `actors`, `episodes`, `episode_roles`, `relations`, `instruments`, `sources` or `evidence`. SQL enforces typed-row identity and kind; the validator detects an incomplete registry entry. Create registry and typed rows in one transaction. IDs are immutable text identifiers, allocated once (UUIDs recommended for future intake); names must not be used as identity keys.

Track A uses `datasets_catalog`. Track B uses episodes and associated entities. They share provenance infrastructure, not observational units. There is deliberately no automatic mapping from catalog relevance to episode roles.

Actors may have multiple R/I/T roles in one episode and different roles across episodes. A role's `function` is a draft free-text description rather than a frozen theory taxonomy. Relationships connect two role assignments in the same episode through composite foreign keys, preserving direction and context. An instrument may occur in multiple episodes through `episode_instruments`.

`evidence` records an observation/excerpt at a source locator. `evidence_links` attaches multiple pieces of evidence to a claim, with a support note. Evidence classification belongs to the role or relation claim: explicit, supported_inference, contested. A documentary observation and its analytical interpretation are kept separate. `coding_decisions.record_id` references the registry, avoiding unprotected polymorphic identifiers. Decision rows are append-only; corrections append a superseding row. `schema_versions` and `codebook_versions` retain version identifiers. Migrations are not silently applied.

SQL enforces primary keys, foreign keys, allowed statuses/classifications and basic interval order. The validator checks registry completeness, current review decisions and documentary support for validated claims. It cannot verify document authenticity, source rights, date semantics, inter-coder independence, scientific validity or truth. A rejected/superseded record remains auditable. Missing values mean unknown/unrecorded, never a negative finding.

For conservative Phase 01 public staging, the entire curated database must satisfy eligibility, including supporting sources/evidence. Mixed provisional/validated databases are rejected rather than automatically pruned. An explicit human approval must match a SHA-256 fingerprint of the full snapshot including private coding decisions. Any subsequent content edit invalidates it. Public output excludes coding decisions; all remaining fields (including excerpts and uncertainty notes) require rights/privacy review. Approval identity is hashed in the manifest, not exposed. This is a local procedural gate, not authentication or tamper-proof access control.

Exports are sorted by all columns, UTF-8, LF terminated and deterministic. JSON retains nulls; CSV encodes null as an empty cell. CSV is a data interchange format: import text columns as text in spreadsheet software. Checksums cover each payload file. Public staging never uploads files.
