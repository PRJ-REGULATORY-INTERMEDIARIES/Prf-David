"""SQLite lifecycle, deterministic internal exports and explicit local release staging."""
from __future__ import annotations

import csv
import hashlib
import io
import json
from pathlib import Path
import sqlite3

ROOT = Path(__file__).resolve().parents[2]
ENTITIES = ('datasets_catalog', 'actors', 'episodes', 'episode_roles', 'relations',
            'instruments', 'sources', 'evidence')
TABLES = ('schema_versions', 'codebook_versions', 'records', *ENTITIES,
          'episode_instruments', 'evidence_links', 'coding_decisions')
PUBLIC_TABLES = tuple(t for t in TABLES if t != 'coding_decisions')


def connect(path: Path) -> sqlite3.Connection:
    """Open an existing file; never silently create a typo-named database."""
    con = sqlite3.connect(Path(path).resolve().as_uri() + '?mode=rw', uri=True)
    con.row_factory = sqlite3.Row
    con.execute('PRAGMA foreign_keys=ON')
    return con


def initialize(path: Path) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive creation: reinitialization must never truncate existing research.
    with path.open('xb'):
        pass
    try:
        with connect(path) as con:
            con.executescript((ROOT / 'database/schema.sql').read_text(encoding='utf-8'))
        con.close()
    except Exception:
        # Retain failed file for inspection; do not conceal partial initialization.
        raise


def load_fixture(con: sqlite3.Connection, path: Path) -> None:
    fixture = json.loads(Path(path).read_text(encoding='utf-8'))
    if fixture.get('label') != 'SYNTHETIC — NOT RESEARCH DATA':
        raise ValueError('Only explicitly labeled synthetic fixtures are accepted')
    rows = fixture['tables']
    if not rows.get('records') or any(r.get('is_synthetic') != 1 for r in rows['records']):
        raise ValueError('Every fixture record must be synthetic')
    if set(rows) - set(TABLES):
        raise ValueError('Unknown fixture table')
    with con:
        for table in TABLES:
            for row in rows.get(table, []):
                allowed = {r['name'] for r in con.execute(f'PRAGMA table_info({table})')}
                if not row or set(row) - allowed:
                    raise ValueError('Unknown fixture column')
                columns = ','.join(row)
                con.execute(f'INSERT INTO {table} ({columns}) VALUES ({",".join("?" for _ in row)})',
                            tuple(row.values()))


def validate(con: sqlite3.Connection) -> list[str]:
    """Structural checks, plus evidence/review requirements for validated claims."""
    errors = []
    if con.execute('PRAGMA foreign_keys').fetchone()[0] != 1:
        errors.append('Foreign-key enforcement is disabled')
    present = {r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table'")}
    if missing := set(TABLES) - present:
        return errors + [f'Missing tables: {sorted(missing)}']
    if list(con.execute('PRAGMA foreign_key_check')):
        errors.append('Foreign-key violations')
    if con.execute('PRAGMA integrity_check').fetchone()[0] != 'ok':
        errors.append('SQLite integrity check failed')
    if [r[0] for r in con.execute('SELECT version FROM schema_versions')] != ['0.1.0']:
        errors.append('Unsupported schema version')
    for rec in con.execute('SELECT * FROM records ORDER BY id'):
        kind = rec['kind']
        if kind not in ENTITIES or not con.execute(f'SELECT 1 FROM {kind} WHERE id=?', (rec['id'],)).fetchone():
            errors.append(f"Missing typed record: {rec['id']}")
        if rec['status'] == 'validated':
            decision = con.execute('''SELECT 1 FROM coding_decisions d
                WHERE d.record_id=? AND d.outcome='validated'
                AND length(trim(d.reviewer))>0 AND length(trim(d.coder))>0
                AND NOT EXISTS(SELECT 1 FROM coding_decisions s WHERE s.supersedes_id=d.decision_id)''',
                (rec['id'],)).fetchone()
            if not decision:
                errors.append(f"Missing current validation decision: {rec['id']}")
            if kind in ('episodes', 'episode_roles', 'relations', 'instruments', 'actors', 'datasets_catalog'):
                if not con.execute('SELECT 1 FROM evidence_links WHERE record_id=?', (rec['id'],)).fetchone():
                    errors.append(f"Missing documentary evidence: {rec['id']}")
    for d in con.execute('''SELECT d.decision_id FROM coding_decisions d
            JOIN coding_decisions old ON old.decision_id=d.supersedes_id
            WHERE d.record_id != old.record_id OR d.variable != old.variable'''):
        errors.append(f'Invalid supersession: {d[0]}')
    return errors


def snapshot(con: sqlite3.Connection) -> dict:
    return {t: [dict(r) for r in con.execute(f'SELECT * FROM {t} ORDER BY ' +
            ','.join(str(i + 1) for i in range(len(con.execute(f'PRAGMA table_info({t})').fetchall()))))]
            for t in TABLES}


def canonical(data: object) -> str:
    return json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2) + '\n'


def digest(data: object) -> str:
    return hashlib.sha256(canonical(data).encode('utf-8')).hexdigest()


def export(con: sqlite3.Connection, destination: Path, *, public: bool = False,
           approval: dict | None = None) -> str:
    """Stage a complete snapshot locally. No upload or publication is implemented.

    Public staging is all-or-nothing: prepare a curated database first. An approval
    must identify the exact internal snapshot hash, including audit decisions.
    """
    destination = Path(destination).resolve()
    base = (ROOT / 'data' / ('public' if public else 'processed')).resolve()
    if not destination.is_relative_to(base) or destination == base:
        raise ValueError(f'Destination must be a new subdirectory of {base}')
    if destination.exists():
        raise FileExistsError(destination)
    # One read transaction makes validation and serialization refer to one state.
    if con.in_transaction:
        raise ValueError('Commit pending edits before exporting')
    con.execute('BEGIN')
    try:
        if errors := validate(con):
            raise ValueError('; '.join(errors))
        data = snapshot(con)
        sha = digest(data)
        if public:
            records = data['records']
            if not records or any(r['status'] != 'validated' or r['public_eligible'] != 1
                                  or r['is_synthetic'] != 0 for r in records):
                raise ValueError('All records must be validated, explicitly eligible and non-synthetic')
            required = ('authorized_by', 'authorized_on', 'license_decision', 'rights_review',
                        'privacy_review', 'scientific_review')
            if not approval or approval.get('snapshot_sha256') != sha or any(
                    not isinstance(approval.get(k), str) or not approval[k].strip() for k in required):
                raise ValueError('Documented human approval for this exact snapshot is required')
            data = {t: data[t] for t in PUBLIC_TABLES}
    finally:
        con.rollback()
    destination.mkdir(parents=True, exist_ok=False)
    (destination / 'snapshot.json').write_text(canonical(data), encoding='utf-8', newline='\n')
    for table, rows in data.items():
        columns = [r['name'] for r in con.execute(f'PRAGMA table_info({table})')]
        with (destination / f'{table}.csv').open('w', encoding='utf-8', newline='') as stream:
            writer = csv.DictWriter(stream, fieldnames=columns, lineterminator='\n')
            writer.writeheader()
            writer.writerows(rows)
    manifest = {'schema_version': '0.1.0', 'input_snapshot_sha256': sha,
                'mode': 'approved-local-staging' if public else 'internal-only',
                'csv_null_policy': 'NULL is empty; use JSON for lossless null/empty distinction',
                'files': {f.name: hashlib.sha256(f.read_bytes()).hexdigest()
                          for f in sorted(destination.iterdir())}}
    if public:
        # Names and private review notes stay internal; approval is bound by hash.
        manifest['approval_sha256'] = digest(approval)
    (destination / 'manifest.json').write_text(canonical(manifest), encoding='utf-8', newline='\n')
    return sha
