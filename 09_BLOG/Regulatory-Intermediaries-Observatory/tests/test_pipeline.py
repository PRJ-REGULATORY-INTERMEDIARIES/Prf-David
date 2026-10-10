"""All records used here are synthetic test material; temporary exports are not research."""
import json
from pathlib import Path
import sqlite3

import pytest

from rio import storage as s


@pytest.fixture
def db(tmp_path):
    path = tmp_path / 'test.sqlite'
    s.initialize(path)
    con = s.connect(path)
    s.load_fixture(con, s.ROOT / 'data/synthetic/minimal.json')
    yield con
    con.close()


def test_initialization_and_required_tables(db, tmp_path):
    assert s.validate(db) == []
    assert db.execute('PRAGMA foreign_keys').fetchone()[0] == 1
    assert set(s.TABLES) <= {r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    path = tmp_path / 'new.sqlite'
    s.initialize(path)
    before = path.read_bytes()
    with pytest.raises(FileExistsError):
        s.initialize(path)
    assert path.read_bytes() == before


def test_missing_database_does_not_create(tmp_path):
    path = tmp_path / 'missing.sqlite'
    with pytest.raises(sqlite3.OperationalError):
        s.connect(path)
    assert not path.exists()


@pytest.mark.parametrize('sql', [
    "INSERT INTO actors(id,name) VALUES ('syn-regulator','duplicate')",
    "INSERT INTO actors(id,name) VALUES ('missing','orphan')",
    "UPDATE records SET status='invented' WHERE id='syn-regulator'",
    "UPDATE records SET is_synthetic=2 WHERE id='syn-regulator'",
    "UPDATE episode_roles SET role='X' WHERE id='syn-role-I'",
    "UPDATE relations SET evidence_mode='certain' WHERE id='syn-relation'",
    "UPDATE evidence SET source_id='missing' WHERE id='syn-evidence'",
    "UPDATE relations SET from_role_id='missing' WHERE id='syn-relation'",
    "DELETE FROM sources WHERE id='syn-source'",
    "UPDATE records SET kind='episodes' WHERE id='syn-regulator'",
    "INSERT INTO actors(id,name) VALUES ('syn-source','wrong kind')",
    "UPDATE coding_decisions SET rationale='overwrite' WHERE decision_id='syn-decision'",
    "DELETE FROM coding_decisions WHERE decision_id='syn-decision'",
])
def test_constraints(db, sql):
    with pytest.raises(sqlite3.IntegrityError):
        with db:
            db.execute(sql)


def add_record(db, identifier, kind):
    db.execute('INSERT INTO records(id,kind,is_synthetic,created_on) VALUES (?,?,1,?)',
               (identifier, kind, '2026-10-09'))


def test_contextual_roles_multiple_intermediaries_and_evidence(db):
    with db:
        add_record(db, 'syn-episode-2', 'episodes')
        db.execute("INSERT INTO episodes(id,title,description) VALUES ('syn-episode-2','SYNTHETIC','SYNTHETIC')")
        add_record(db, 'syn-other-role', 'episode_roles')
        db.execute("""INSERT INTO episode_roles(id,episode_id,actor_id,role,evidence_mode,rationale)
            VALUES ('syn-other-role','syn-episode-2','syn-regulator','T','contested','SYNTHETIC')""")
        add_record(db, 'syn-second-intermediary', 'episode_roles')
        db.execute("""INSERT INTO episode_roles(id,episode_id,actor_id,role,evidence_mode,rationale)
            VALUES ('syn-second-intermediary','syn-episode','syn-target','I','explicit','SYNTHETIC')""")
        add_record(db, 'syn-evidence-2', 'evidence')
        db.execute("""INSERT INTO evidence(id,source_id,item_reference,observation)
            VALUES ('syn-evidence-2','syn-source','SYNTHETIC 2','SYNTHETIC')""")
        db.execute("INSERT INTO evidence_links VALUES ('syn-role-I','syn-evidence-2','SYNTHETIC')")
    assert s.validate(db) == []
    with pytest.raises(sqlite3.IntegrityError):
        with db:
            db.execute("UPDATE relations SET from_role_id='syn-other-role' WHERE id='syn-relation'")


def test_fixture_atomicity_and_preservation(db):
    before = s.snapshot(db)
    with pytest.raises(sqlite3.IntegrityError):
        s.load_fixture(db, s.ROOT / 'data/synthetic/minimal.json')
    assert before == s.snapshot(db)
    assert all(r['is_synthetic'] == 1 for r in before['records'])


def test_export_reproducible_and_roundtrip(db, tmp_path, monkeypatch):
    monkeypatch.setattr(s, 'ROOT', tmp_path)
    a, b = (tmp_path / 'data/processed' / x for x in ['a', 'b'])
    before = s.snapshot(db)
    assert s.export(db, a) == s.export(db, b)
    assert {f.name: f.read_bytes() for f in a.iterdir()} == {f.name: f.read_bytes() for f in b.iterdir()}
    assert json.loads((a / 'snapshot.json').read_text(encoding='utf-8')) == before
    assert s.snapshot(db) == before
    with pytest.raises(FileExistsError):
        s.export(db, a)


@pytest.mark.parametrize('path,public', [('data/public/leak', False), ('data/raw/leak', False),
                                        ('data/public/../../raw/leak', True)])
def test_directory_separation(db, tmp_path, monkeypatch, path, public):
    monkeypatch.setattr(s, 'ROOT', tmp_path)
    with pytest.raises(ValueError):
        s.export(db, tmp_path / path, public=public)
    assert not (tmp_path / path).exists()


def mark_validated(db):
    with db:
        db.execute("UPDATE records SET status='validated',public_eligible=1")
        for row in db.execute('SELECT id FROM records').fetchall():
            db.execute('''INSERT INTO coding_decisions
                (decision_id,record_id,variable,coder,reviewer,outcome,rationale,decided_on,codebook_version)
                VALUES (?,?,'status','SYNTHETIC coder','SYNTHETIC reviewer','validated',
                        'TEST ONLY approval simulation','2026-10-09','0.1.0')''',
                ('test-validation-' + row['id'], row['id']))


def approval(db):
    return {'snapshot_sha256': s.digest(s.snapshot(db)), **{k: 'TEST ONLY — simulated approval'
        for k in ('authorized_by', 'authorized_on', 'license_decision', 'rights_review',
                  'privacy_review', 'scientific_review')}}


def test_public_fails_closed_for_candidates_and_synthetic(db, tmp_path, monkeypatch):
    monkeypatch.setattr(s, 'ROOT', tmp_path)
    out = tmp_path / 'data/public/test'
    with pytest.raises(ValueError, match='validated'):
        s.export(db, out, public=True, approval=approval(db))
    mark_validated(db)
    assert s.validate(db) == []
    with pytest.raises(ValueError, match='non-synthetic'):
        s.export(db, out, public=True, approval=approval(db))
    assert not out.exists()


def test_release_approval_binding_and_success_simulation(db, tmp_path, monkeypatch):
    # Simulate non-synthetic flags ONLY in a pytest temporary database. All content
    # remains explicitly SYNTHETIC; nothing enters the repository public directory.
    monkeypatch.setattr(s, 'ROOT', tmp_path)
    mark_validated(db)
    with db:
        db.execute('UPDATE records SET is_synthetic=0')
    out = tmp_path / 'data/public/test'
    with pytest.raises(ValueError, match='approval'):
        s.export(db, out, public=True)
    approved = approval(db)
    with db:
        db.execute("UPDATE actors SET name='SYNTHETIC changed' WHERE id='syn-target'")
    with pytest.raises(ValueError, match='approval'):
        s.export(db, out, public=True, approval=approved)
    s.export(db, out, public=True, approval=approval(db))
    assert 'coding_decisions' not in json.loads((out / 'snapshot.json').read_text())
    assert not (out / 'coding_decisions.csv').exists()


def test_validated_claims_need_evidence_and_review(db):
    with db:
        db.execute("UPDATE records SET status='validated' WHERE id='syn-role-I'")
        db.execute("DELETE FROM evidence_links WHERE record_id='syn-role-I'")
    errors = s.validate(db)
    assert any('validation decision' in e for e in errors)
    assert any('documentary evidence' in e for e in errors)


def test_orphan_registry_detected(db):
    with db:
        add_record(db, 'syn-orphan', 'actors')
    assert any('Missing typed record' in e for e in s.validate(db))


def test_disabled_fk_and_external_corruption_detected(db):
    db.execute('PRAGMA foreign_keys=OFF')
    with db:
        db.execute("UPDATE evidence SET source_id='missing' WHERE id='syn-evidence'")
    assert 'Foreign-key enforcement is disabled' in s.validate(db)
    db.execute('PRAGMA foreign_keys=ON')
    assert 'Foreign-key violations' in s.validate(db)
