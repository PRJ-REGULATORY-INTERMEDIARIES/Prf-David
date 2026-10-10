# Migration policy

Initial schema: 0.1.0. No migration is needed for a newly initialized database.

Do not re-run schema.sql against an existing database. Future migrations require a reviewed numbered SQL file, a backup, a transaction, explicit schema_versions updates, and tests of preservation/rollback. Keep old codebook versions and record-level provenance. No automatic migration runner is implemented in Phase 01.
