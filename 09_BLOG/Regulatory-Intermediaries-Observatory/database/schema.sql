-- DRAFT — NOT VALIDATED. Schema 0.1.0. Enable foreign_keys on EVERY connection.
PRAGMA foreign_keys = ON;
BEGIN;
CREATE TABLE schema_versions(version TEXT PRIMARY KEY, applied_on TEXT NOT NULL);
INSERT INTO schema_versions VALUES ('0.1.0','2026-10-09');
CREATE TABLE codebook_versions(version TEXT PRIMARY KEY, description TEXT NOT NULL);
INSERT INTO codebook_versions VALUES ('0.1.0','DRAFT — NOT VALIDATED');
CREATE TABLE records (
 id TEXT PRIMARY KEY NOT NULL CHECK(length(trim(id)) > 0),
 kind TEXT NOT NULL CHECK(kind IN ('datasets_catalog','actors','episodes','episode_roles','relations','instruments','sources','evidence')),
 status TEXT NOT NULL DEFAULT 'candidate' CHECK(status IN ('candidate','coding','under_review','adjudicated','validated','rejected')),
 is_synthetic INTEGER NOT NULL DEFAULT 0 CHECK(is_synthetic IN (0,1)),
 public_eligible INTEGER NOT NULL DEFAULT 0 CHECK(public_eligible IN (0,1)),
 schema_version TEXT NOT NULL DEFAULT '0.1.0' REFERENCES schema_versions(version),
 codebook_version TEXT NOT NULL DEFAULT '0.1.0' REFERENCES codebook_versions(version),
 created_on TEXT NOT NULL,
 uncertainty_note TEXT
);
CREATE TABLE datasets_catalog (id TEXT PRIMARY KEY NOT NULL REFERENCES records(id), title TEXT NOT NULL, provider TEXT, url TEXT, license TEXT, coverage TEXT, access_method TEXT, version TEXT, reviewed_on TEXT, rit_relevance TEXT CHECK(rit_relevance IN ('explicit','inferable_pending_validation','not_demonstrable','unknown')), search_log_ref TEXT);
CREATE TRIGGER datasets_catalog_kind_insert BEFORE INSERT ON datasets_catalog
WHEN (SELECT kind FROM records WHERE id=NEW.id) != 'datasets_catalog'
BEGIN SELECT RAISE(ABORT,'record kind mismatch'); END;
CREATE TRIGGER datasets_catalog_kind_update BEFORE UPDATE ON datasets_catalog
WHEN (SELECT kind FROM records WHERE id=NEW.id) != 'datasets_catalog'
BEGIN SELECT RAISE(ABORT,'record kind mismatch'); END;
CREATE TABLE actors (id TEXT PRIMARY KEY NOT NULL REFERENCES records(id), name TEXT NOT NULL, actor_type TEXT, jurisdiction TEXT, external_identifier TEXT);
CREATE TRIGGER actors_kind_insert BEFORE INSERT ON actors
WHEN (SELECT kind FROM records WHERE id=NEW.id) != 'actors'
BEGIN SELECT RAISE(ABORT,'record kind mismatch'); END;
CREATE TRIGGER actors_kind_update BEFORE UPDATE ON actors
WHEN (SELECT kind FROM records WHERE id=NEW.id) != 'actors'
BEGIN SELECT RAISE(ABORT,'record kind mismatch'); END;
CREATE TABLE episodes (id TEXT PRIMARY KEY NOT NULL REFERENCES records(id), title TEXT NOT NULL, domain TEXT, jurisdiction TEXT, start_date TEXT, end_date TEXT, temporal_note TEXT, description TEXT NOT NULL, CHECK(start_date IS NULL OR end_date IS NULL OR start_date <= end_date));
CREATE TRIGGER episodes_kind_insert BEFORE INSERT ON episodes
WHEN (SELECT kind FROM records WHERE id=NEW.id) != 'episodes'
BEGIN SELECT RAISE(ABORT,'record kind mismatch'); END;
CREATE TRIGGER episodes_kind_update BEFORE UPDATE ON episodes
WHEN (SELECT kind FROM records WHERE id=NEW.id) != 'episodes'
BEGIN SELECT RAISE(ABORT,'record kind mismatch'); END;
CREATE TABLE episode_roles (id TEXT PRIMARY KEY NOT NULL REFERENCES records(id), episode_id TEXT NOT NULL REFERENCES episodes(id), actor_id TEXT NOT NULL REFERENCES actors(id), role TEXT NOT NULL CHECK(role IN ('R','I','T')), function TEXT, evidence_mode TEXT NOT NULL CHECK(evidence_mode IN ('explicit','supported_inference','contested')), rationale TEXT NOT NULL, confidence TEXT CHECK(confidence IN ('low','medium','high','unknown')), UNIQUE(episode_id,actor_id,role), UNIQUE(id,episode_id));
CREATE TRIGGER episode_roles_kind_insert BEFORE INSERT ON episode_roles
WHEN (SELECT kind FROM records WHERE id=NEW.id) != 'episode_roles'
BEGIN SELECT RAISE(ABORT,'record kind mismatch'); END;
CREATE TRIGGER episode_roles_kind_update BEFORE UPDATE ON episode_roles
WHEN (SELECT kind FROM records WHERE id=NEW.id) != 'episode_roles'
BEGIN SELECT RAISE(ABORT,'record kind mismatch'); END;
CREATE TABLE relations (id TEXT PRIMARY KEY NOT NULL REFERENCES records(id), episode_id TEXT NOT NULL REFERENCES episodes(id), from_role_id TEXT NOT NULL, to_role_id TEXT NOT NULL, function TEXT NOT NULL, evidence_mode TEXT NOT NULL CHECK(evidence_mode IN ('explicit','supported_inference','contested')), rationale TEXT NOT NULL, FOREIGN KEY(from_role_id,episode_id) REFERENCES episode_roles(id,episode_id), FOREIGN KEY(to_role_id,episode_id) REFERENCES episode_roles(id,episode_id));
CREATE TRIGGER relations_kind_insert BEFORE INSERT ON relations
WHEN (SELECT kind FROM records WHERE id=NEW.id) != 'relations'
BEGIN SELECT RAISE(ABORT,'record kind mismatch'); END;
CREATE TRIGGER relations_kind_update BEFORE UPDATE ON relations
WHEN (SELECT kind FROM records WHERE id=NEW.id) != 'relations'
BEGIN SELECT RAISE(ABORT,'record kind mismatch'); END;
CREATE TABLE instruments (id TEXT PRIMARY KEY NOT NULL REFERENCES records(id), title TEXT NOT NULL, instrument_type TEXT, locator TEXT, issued_on TEXT);
CREATE TRIGGER instruments_kind_insert BEFORE INSERT ON instruments
WHEN (SELECT kind FROM records WHERE id=NEW.id) != 'instruments'
BEGIN SELECT RAISE(ABORT,'record kind mismatch'); END;
CREATE TRIGGER instruments_kind_update BEFORE UPDATE ON instruments
WHEN (SELECT kind FROM records WHERE id=NEW.id) != 'instruments'
BEGIN SELECT RAISE(ABORT,'record kind mismatch'); END;
CREATE TABLE sources (id TEXT PRIMARY KEY NOT NULL REFERENCES records(id), title TEXT NOT NULL, locator TEXT NOT NULL, accessed_on TEXT NOT NULL, version TEXT, sha256 TEXT, rights_note TEXT);
CREATE TRIGGER sources_kind_insert BEFORE INSERT ON sources
WHEN (SELECT kind FROM records WHERE id=NEW.id) != 'sources'
BEGIN SELECT RAISE(ABORT,'record kind mismatch'); END;
CREATE TRIGGER sources_kind_update BEFORE UPDATE ON sources
WHEN (SELECT kind FROM records WHERE id=NEW.id) != 'sources'
BEGIN SELECT RAISE(ABORT,'record kind mismatch'); END;
CREATE TABLE evidence (id TEXT PRIMARY KEY NOT NULL REFERENCES records(id), source_id TEXT NOT NULL REFERENCES sources(id), item_reference TEXT NOT NULL, excerpt TEXT, observation TEXT NOT NULL);
CREATE TRIGGER evidence_kind_insert BEFORE INSERT ON evidence
WHEN (SELECT kind FROM records WHERE id=NEW.id) != 'evidence'
BEGIN SELECT RAISE(ABORT,'record kind mismatch'); END;
CREATE TRIGGER evidence_kind_update BEFORE UPDATE ON evidence
WHEN (SELECT kind FROM records WHERE id=NEW.id) != 'evidence'
BEGIN SELECT RAISE(ABORT,'record kind mismatch'); END;
CREATE TRIGGER stable_identity BEFORE UPDATE OF id,kind ON records
BEGIN SELECT RAISE(ABORT,'record identity and kind are immutable'); END;
CREATE TABLE episode_instruments (
 episode_id TEXT NOT NULL REFERENCES episodes(id),
 instrument_id TEXT NOT NULL REFERENCES instruments(id),
 PRIMARY KEY(episode_id,instrument_id)
);
CREATE TABLE evidence_links (
 record_id TEXT NOT NULL REFERENCES records(id),
 evidence_id TEXT NOT NULL REFERENCES evidence(id),
 support_note TEXT NOT NULL CHECK(length(trim(support_note)) > 0),
 PRIMARY KEY(record_id,evidence_id)
);
CREATE TABLE coding_decisions (
 decision_id TEXT PRIMARY KEY NOT NULL,
 record_id TEXT NOT NULL REFERENCES records(id),
 variable TEXT NOT NULL,
 proposed_value TEXT,
 coder TEXT NOT NULL,
 reviewer TEXT,
 outcome TEXT NOT NULL CHECK(outcome IN ('proposed','disputed','adjudicated','validated','rejected')),
 rationale TEXT NOT NULL CHECK(length(trim(rationale)) > 0),
 decided_on TEXT NOT NULL,
 supersedes_id TEXT REFERENCES coding_decisions(decision_id),
 codebook_version TEXT NOT NULL REFERENCES codebook_versions(version)
);
CREATE TRIGGER preserve_decisions_update BEFORE UPDATE ON coding_decisions
BEGIN SELECT RAISE(ABORT,'append a superseding decision'); END;
CREATE TRIGGER preserve_decisions_delete BEFORE DELETE ON coding_decisions
BEGIN SELECT RAISE(ABORT,'coding decisions are append-only'); END;
CREATE INDEX roles_episode ON episode_roles(episode_id);
CREATE INDEX relations_episode ON relations(episode_id);
CREATE INDEX links_evidence ON evidence_links(evidence_id);
CREATE INDEX decisions_record ON coding_decisions(record_id);
COMMIT;
