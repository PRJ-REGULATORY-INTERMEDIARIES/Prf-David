#!/usr/bin/env python3
"""Build the G2 mapping base (mapping/data/*.csv) from curation inputs and evidence logs.

Inputs (none of them is modified):
    inputs/seed_inventory_v0_1.csv                 the 41 original seed records
    mapping/curation/round1.py, round2.py          provisional judgements, with field-level source tags;
                                                   round 2 patches round-1 rows and adds new ones
    mapping/evidence/captures/CAPTURE_LOG.jsonl    page and record captures (scripts/capture_evidence.py)
    mapping/evidence/searches/SEARCH_LOG.jsonl     registered searches (mapping_search.py) and their responses
    mapping/evidence/inspections/INSPECTION_LOG.jsonl  first-bytes inspections (verify_resources.py peek)
    mapping/protocol/INSTITUTIONAL_SWEEP_G2_ROUND2.csv   institutional sweep registry
    pilot_a/evidence_procedure_test/CAPTURE_LOG.jsonl    the G1-READY capture of the ELDS page (read only)

The build is deterministic: same inputs, same bytes. No network. The round-1 tables are
frozen in mapping/snapshots/round1/ and are never rewritten.
"""
import copy
import csv
import importlib.util
import json
import re
import sys
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[2]
MAPPING = ROOT / 'mapping'
sys.path.insert(0, str(Path(__file__).resolve().parent))
import mapping_search  # noqa: E402
import verify_resources  # noqa: E402

NA = 'NOT_ASSESSED'
TAGS = {'P': 'PRIMARY_PAGE', 'M': 'API_METADATA', 'S': 'SEED_UNVERIFIED', 'I': 'AGENT_INFERENCE', 'O': 'OPERATIONAL_INSPECTION'}
GOOD_BASIS = ('PRIMARY_PAGE', 'API_METADATA', 'OPERATIONAL_INSPECTION')
FIELDS = [('name', 'verified_name'), ('maint', 'maintainer'), ('terr', 'territorial_scope'), ('eu', 'eu_connection_note'),
          ('theme', 'thematic_coverage'), ('temp', 'temporal_coverage'), ('unit', 'observation_unit'), ('upd', 'update_mode'),
          ('fmt', 'formats'), ('acc', 'access_modes'), ('ids', 'identifiers_supported'), ('hist', 'historical_versions'),
          ('cond', 'access_conditions'), ('lic', 'licence_or_reuse')]
SEED_FALLBACK = {'unit': 'observation_unit', 'ids': 'possible_legal_id'}  # carried from the seed inventory, tagged unverified

LEVEL_I = {'DATASET', 'CORPUS', 'BENCHMARK', 'ADMINISTRATIVE_REGISTER', 'REPOSITORY'}
LEVEL_II = {'CATALOGUE', 'ACCESS_PORTAL', 'SEARCH_INTERFACE', 'API', 'INFRASTRUCTURE', 'STANDARD_OR_VOCABULARY',
            'SOFTWARE_OR_PIPELINE', 'DESCRIPTIVE_PAGE'}

RESOURCE_COLS = ['resource_id', 'seed_id', 'registered_name', 'verified_name', 'maintainer', 'resource_category', 'category_status',
                 'resource_set', 'territorial_scope', 'eu_connection_note', 'thematic_coverage', 'temporal_coverage', 'observation_unit',
                 'update_mode', 'formats', 'access_modes', 'identifiers_supported', 'historical_versions', 'access_conditions',
                 'licence_or_reuse', 'description_url', 'primary_access_url', 'individuation_status', 'eligibility_preliminary',
                 'verification_status', 'verification_date', 'discovery_origin', 'field_basis', 'classification_basis',
                 'researcher_confirmed', 'evidence_ids', 'uncertainties',
                 'resource_level', 'identity_level', 'data_availability_level', 'capability_level', 'first_round']
ENDPOINT_COLS = ['endpoint_id', 'resource_id', 'endpoint_role', 'url', 'url_source', 'auth_required', 'access_status', 'http_status',
                 'final_url', 'tested_at_utc', 'evidence_id', 'notes']
RELATION_COLS = ['relation_id', 'source_resource_id', 'relation_type', 'target_resource_id', 'confidence', 'relation_status', 'basis',
                 'evidence_ids', 'justification', 'assessed_by', 'researcher_confirmed', 'assessed_on']
DISCOVERY_COLS = ['discovery_id', 'entry_type', 'resource_id', 'origin', 'search_id', 'platform', 'query', 'language', 'executed_at_utc',
                  'total_reported', 'hits_returned', 'hits_linked_to_resources', 'hit_rank', 'platform_record_id', 'hit_title',
                  'evidence_id', 'note']
EVIDENCE_COLS = ['evidence_id', 'evidence_type', 'related_record', 'url', 'final_url', 'accessed_at_utc', 'outcome', 'http_status',
                 'content_type', 'bytes', 'sha256', 'stored_file', 'tool', 'note']
DECISION_COLS = ['decision_id', 'decision_type', 'subject', 'decision', 'rationale', 'evidence_ids', 'decided_by', 'decided_on', 'status']
SEED_AUDIT_COLS = ['seed_id', 'resource_id', 'registered_name', 'verified_name', 'maintainer', 'resource_category', 'resource_set',
                   'registered_url', 'registered_url_role', 'description_url', 'primary_access_url', 'territorial_scope',
                   'thematic_coverage', 'temporal_coverage', 'observation_unit', 'update_mode', 'formats', 'access_modes',
                   'identifiers_supported', 'historical_versions', 'access_conditions', 'licence_or_reuse', 'relations',
                   'evidence_ids', 'verification_date', 'verification_status', 'field_basis', 'uncertainties']
HISTORY_COLS = ['history_id', 'resource_id', 'round', 'from_status', 'to_status', 'reason', 'evidence_ids', 'changed_on']
INSPECTION_COLS = ['inspection_id', 'resource_id', 'url', 'outcome', 'http_status', 'content_type', 'bytes_read', 'content_kind',
                   'availability_observed', 'fields_observed', 'evidence_id']
CAPABILITY_COLS = ['capability_id', 'resource_id', 'capability', 'observed_fields', 'method', 'evidence_id', 'note']
SWEEP_COLS = ['sweep_id', 'step', 'body', 'body_type', 'url', 'purpose', 'outcome', 'http_status', 'final_url', 'evidence_id',
              'found_resources', 'result_note']
LYNX_COLS = ['lynx_id', 'source', 'area', 'url', 'law', 'case_law', 'eli', 'ecli', 'access_interface', 'in_scope_by_rule',
             'match_status', 'matched_resource_id', 'match_basis', 'source_evidence_id', 'note']


def rid(n):
    return f'MR-{n:04d}'


# --------------------------------------------------------------------------- curation
def _load_module(path):
    spec = importlib.util.spec_from_file_location(Path(path).stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_curation(directory=MAPPING / 'curation'):
    """Merge the curation files in round order. Round-1 rows keep their numbers; later rounds patch and append."""
    files = sorted(Path(directory).glob('round[0-9]*.py'))
    merged = SimpleNamespace(RESOURCES=[], ENDPOINTS=[], RELATIONS=[], DECISIONS=[], SEED_REFOUND={}, EXTRA_EVIDENCE={},
                             SHARED_URL_JUSTIFICATIONS={}, PATCH_LOG=[], LYNX=[], VERIFICATION_DATE='', ROUNDS=[], SWEEP_NOTES={})
    by_n = {}
    for path in files:
        mod = _load_module(path)
        merged.ROUNDS.append(mod.ROUND)
        merged.VERIFICATION_DATE = mod.VERIFICATION_DATE
        for n, patch in getattr(mod, 'PATCHES', {}).items():
            row = by_n[n]
            changes = {}
            for key, value in patch.items():
                if key in ('status_reason',):
                    continue
                if key == 'unc_add':
                    row['unc'] = (row.get('unc', '') + ' [' + mod.ROUND + '] ' + value).strip()
                    continue
                if row.get(key) != value:
                    changes[key] = (row.get(key), value)
                    row[key] = value
            row['last_round'] = mod.ROUND
            merged.PATCH_LOG.append({'n': n, 'round': mod.ROUND, 'changes': changes, 'reason': patch.get('status_reason', ''),
                                     'date': mod.VERIFICATION_DATE})
        for r in copy.deepcopy(mod.RESOURCES):
            r.setdefault('first_round', mod.ROUND)
            r['last_round'] = r['first_round']
            by_n[r['n']] = r
            merged.RESOURCES.append(r)
        merged.ENDPOINTS += [tuple(e) for e in mod.ENDPOINTS]
        merged.RELATIONS += [tuple(x) for x in mod.RELATIONS]
        merged.DECISIONS += [tuple(x) for x in mod.DECISIONS]
        for n, specs in getattr(mod, 'SEED_REFOUND', {}).items():
            merged.SEED_REFOUND.setdefault(n, []).extend(specs)
        for n, specs in getattr(mod, 'EXTRA_EVIDENCE', {}).items():
            merged.EXTRA_EVIDENCE.setdefault(n, []).extend(specs)
        merged.SHARED_URL_JUSTIFICATIONS.update(getattr(mod, 'SHARED_URL_JUSTIFICATIONS', {}))
        merged.LYNX += list(getattr(mod, 'LYNX_ROWS', []))
        merged.SWEEP_NOTES.update(getattr(mod, 'SWEEP_NOTES', {}))
    return merged


def read_jsonl(path):
    path = Path(path)
    if not path.exists():
        return []
    return [json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x.strip()]


def read_csv(path):
    path = Path(path)
    if not path.exists():
        return []
    with path.open(encoding='utf-8-sig', newline='') as fh:
        return list(csv.DictReader(fh))


def split_tag(value):
    """'text|P' -> ('text', 'PRIMARY_PAGE'); untagged or NOT_ASSESSED -> (value, '')."""
    if isinstance(value, str) and len(value) > 2 and value[-2] == '|' and value[-1] in TAGS:
        return value[:-2], TAGS[value[-1]]
    return value, ''


def resource_level(category):
    if category in LEVEL_I:
        return 'LEVEL_I_DATA'
    if category in LEVEL_II:
        return 'LEVEL_II_INFRASTRUCTURE'
    if category == 'DATA_DISTRIBUTION':
        return 'DISTRIBUTION_OF_LEVEL_I'
    return 'UNASSIGNED'


# --------------------------------------------------------------------------- evidence
def build_evidence(capture_log, search_log, historical_log, inspection_log):
    rows, by_url, by_search, by_label, hist = [], {}, {}, {}, ''
    for rec in historical_log:
        if rec.get('outcome') == 'CAPTURED':
            hist = 'EVH-0001'
            rows.append({'evidence_id': hist, 'evidence_type': 'HISTORICAL_CAPTURE', 'related_record': rec['record_id'],
                         'url': rec['original_url'], 'final_url': rec.get('final_url', ''), 'accessed_at_utc': rec['captured_at_utc'],
                         'outcome': 'CAPTURED', 'http_status': rec.get('http_status', ''), 'content_type': rec.get('content_type', ''),
                         'bytes': rec['bytes'], 'sha256': rec['sha256'],
                         'stored_file': 'pilot_a/evidence_procedure_test/' + rec['raw_file'], 'tool': rec.get('tool', ''),
                         'note': 'Captured during G1-READY; preserved, not copied.'})
            break
    for i, rec in enumerate(capture_log, 1):
        eid = f'EVC-{i:04d}'
        last = rec['attempts'][-1] if rec.get('attempts') else {}
        ok = rec['outcome'] == 'CAPTURED'
        rows.append({'evidence_id': eid, 'evidence_type': 'PAGE_CAPTURE' if ok else 'ACCESS_FAILURE', 'related_record': rec['record_id'],
                     'url': rec['original_url'], 'final_url': rec.get('final_url') or '', 'accessed_at_utc': rec['captured_at_utc'],
                     'outcome': rec['outcome'], 'http_status': rec.get('http_status') or last.get('http_status') or '',
                     'content_type': rec.get('content_type') or '', 'bytes': rec.get('bytes') or '', 'sha256': rec.get('sha256') or '',
                     'stored_file': ('mapping/evidence/captures/' + rec['raw_file']) if rec.get('raw_file') else '',
                     'tool': rec.get('tool', ''),
                     'note': '' if ok else f"{len(rec['attempts'])} attempt(s); last error: {last.get('error', '')}. Access failure, not evidence of absence."})
        by_url[rec['original_url']] = (eid, rec)  # a later capture of the same URL supersedes the earlier one
        by_label.setdefault(rec['record_id'], []).append((eid, ok))
    for rec in sorted(search_log, key=lambda r: r['search_id']):
        eid = 'EVS-' + rec['search_id'].rsplit('-', 1)[-1]
        ok = rec['outcome'] == 'EXECUTED'
        rows.append({'evidence_id': eid, 'evidence_type': 'SEARCH_RESPONSE', 'related_record': rec['search_id'], 'url': rec['request_url'],
                     'final_url': '', 'accessed_at_utc': rec['executed_at_utc'], 'outcome': rec['outcome'],
                     'http_status': rec.get('http_status', ''), 'content_type': 'application/json' if ok else '',
                     'bytes': rec.get('bytes', ''), 'sha256': rec.get('sha256', ''),
                     'stored_file': ('mapping/evidence/searches/' + rec['raw_file']) if ok else '', 'tool': rec.get('tool', ''),
                     'note': f"query: {rec['query']}" + ('' if ok else f"; error: {rec.get('error', '')}")})
        by_search[rec['search_id']] = eid
    peek_ids = []
    for i, rec in enumerate(inspection_log, 1):
        eid = f'EVP-{i:04d}'
        ok = rec['outcome'] == 'READ' and rec.get('bytes_read')
        rows.append({'evidence_id': eid, 'evidence_type': 'DATA_PEEK', 'related_record': rec['resource_id'], 'url': rec['url'],
                     'final_url': rec.get('final_url') or '', 'accessed_at_utc': rec['started_utc'],
                     'outcome': 'READ' if ok else 'FAILED', 'http_status': rec.get('http_status', ''),
                     'content_type': rec.get('content_type') or '', 'bytes': rec.get('bytes_read') or '', 'sha256': rec.get('sha256') or '',
                     'stored_file': ('mapping/evidence/inspections/' + rec['stored_file']) if rec.get('stored_file') else '',
                     'tool': rec.get('tool', ''),
                     'note': f"first {rec.get('bytes_read') or 0} bytes only" + ('' if ok else f"; {rec.get('error', rec.get('outcome'))}")})
        peek_ids.append(eid)
        by_label.setdefault(rec['resource_id'], []).append((eid, bool(ok)))
    return rows, by_url, by_search, by_label, hist, peek_ids


def derive_levels(row, success_ids, peeks, caps):
    """The three evidence levels, derived only from what the row and its evidence say. Never typed by hand."""
    basis = {}
    for item in filter(None, row['field_basis'].split('; ')):
        col, _, tag = item.rpartition(':')
        basis[col] = tag
    full = (row['verified_name'] != NA and row['maintainer'] != NA and row['description_url'] != NA
            and basis.get('verified_name') in GOOD_BASIS and basis.get('maintainer') in GOOD_BASIS)
    if success_ids and full:
        identity = 'IDENTITY_VERIFIED'
    elif success_ids:
        identity = 'IDENTITY_PARTIAL'
    else:
        identity = 'NOT_VERIFIED'
    seen = {p['obs']['availability'] for p in peeks}
    if 'DATA_AVAILABILITY_VERIFIED' in seen:
        availability = 'DATA_AVAILABILITY_VERIFIED'
    elif 'DOCUMENT_ONLY' in seen:
        availability = 'DOCUMENT_ONLY'
    elif 'LANDING_PAGE_ONLY' in seen:
        availability = 'LANDING_PAGE_ONLY'
    elif 'LISTING_ONLY' in seen:
        availability = 'LISTING_ONLY'
    elif 'ACCESS_FAILED' in seen:
        availability = 'ACCESS_FAILED'
    else:
        availability = 'NOT_TESTED'
    capability = 'CAPABILITY_VERIFIED' if caps else 'NOT_ASSESSED'
    return identity, availability, capability


# --------------------------------------------------------------------------- build
def build(curation=None, seed_path=ROOT / 'inputs' / 'seed_inventory_v0_1.csv', capture_dir=MAPPING / 'evidence' / 'captures',
          search_dir=MAPPING / 'evidence' / 'searches', historical_dir=ROOT / 'pilot_a' / 'evidence_procedure_test',
          inspection_dir=MAPPING / 'evidence' / 'inspections', sweep_registry=None):
    cur = curation or load_curation()
    seeds = {r['source_seed_id']: r for r in read_csv(seed_path)}
    capture_log = read_jsonl(Path(capture_dir) / 'CAPTURE_LOG.jsonl')
    search_log = mapping_search.read_log(search_dir)
    inspection_log = verify_resources.read_inspections(inspection_dir)
    evidence, by_url, by_search, by_label, hist, peek_ids = build_evidence(
        capture_log, search_log, read_jsonl(Path(historical_dir) / 'CAPTURE_LOG.jsonl'), inspection_log)
    hits = mapping_search.build_hits(search_dir)
    hit_index = {}
    for h in hits:
        hit_index.setdefault((h['search_id'], h['platform_record_id']), h)
    prefix_rows = {}
    for h in hits:
        prefix_rows.setdefault(h['search_id'], []).append(h)

    def handle(h):
        kind, _, key = h.partition(':')
        if kind == 'C':
            return by_url[key][0]
        if kind == 'S':
            return by_search[key]
        if kind == 'H':
            return hist
        raise ValueError(f'unknown evidence handle {h!r}')

    def match_hits(spec):
        sid, exact = spec[0], spec[1]
        if exact:
            found = [hit_index[(sid, exact)]] if (sid, exact) in hit_index else []
        else:
            found = [h for h in prefix_rows.get(sid, []) if h['platform_record_id'].startswith(spec[2])]
        if not found:
            raise ValueError(f'curation points to a hit that is not in the stored responses: {spec}')
        return found

    # ---- inspections: observation of every peek
    peeks_by_resource, peek_by_url = {}, {}
    inspection_rows, capability_rows = [], []
    for eid, rec in zip(peek_ids, inspection_log):
        obs = verify_resources.observe(rec, root=inspection_dir)
        item = {'eid': eid, 'rec': rec, 'obs': obs}
        peeks_by_resource.setdefault(rec['resource_id'], []).append(item)
        peek_by_url[rec['url']] = item
        inspection_rows.append({'inspection_id': eid, 'resource_id': rec['resource_id'], 'url': rec['url'], 'outcome': rec['outcome'],
                                'http_status': rec.get('http_status', ''), 'content_type': rec.get('content_type') or '',
                                'bytes_read': rec.get('bytes_read') or 0, 'content_kind': obs['content_kind'] or '',
                                'availability_observed': obs['availability'], 'fields_observed': ';'.join(obs['fields'])[:400],
                                'evidence_id': eid})
    caps_by_resource = {}
    for item in sorted((i for lst in peeks_by_resource.values() for i in lst), key=lambda x: x['eid']):
        if not item['obs']['fields']:
            continue
        resource = item['rec']['resource_id']
        found = verify_resources.capabilities(item['obs']['fields'])
        entries = [('SCHEMA_FIELDS_OBSERVED', item['obs']['fields'][:25], 'SCHEMA_LISTING',
                    f"{item['obs']['content_kind']} sample: field or key names read from the first {item['rec']['bytes_read']} bytes")]
        entries += [(cap, names, 'FIELD_NAME_MATCH', 'A field with a matching name exists in the sample; its content and completeness were not examined')
                    for cap, names in sorted(found.items())]
        for cap, names, method, note in entries:
            caps_by_resource.setdefault(resource, []).append(cap)
            capability_rows.append({'resource_id': resource, 'capability': cap, 'observed_fields': ';'.join(names)[:300],
                                    'method': method, 'evidence_id': item['eid'], 'note': note})
    for i, c in enumerate(capability_rows, 1):
        c['capability_id'] = f'CAP-{i:04d}'

    # ---- endpoints (explicit curation)
    endpoints, ev_by_resource, counter = [], {}, {}
    for n, role, url, source, auth, js, note in cur.ENDPOINTS:
        counter[n] = counter.get(n, 0) + 1
        eid, rec = by_url.get(url, ('', None))
        status, http, final, tested = 'NOT_TESTED', '', '', ''
        if rec:
            tested = rec['captured_at_utc']
            last = rec['attempts'][-1]
            http = rec.get('http_status') or last.get('http_status') or ''
            final = rec.get('final_url') or ''
            if rec['outcome'] == 'CAPTURED':
                status = 'JS_ONLY_SHELL' if js else 'ACCESSIBLE'
            elif http == 401:
                status = 'AUTH_REQUIRED'
            elif http == 403:
                status = 'BLOCKED_TO_TOOL'
            else:
                status = 'NETWORK_ERROR'
            ev_by_resource.setdefault(n, []).append(eid)
        if url in peek_by_url:  # a first-bytes inspection of this very address
            item = peek_by_url[url]
            tested, eid = item['rec']['started_utc'], item['eid']
            http, final = item['rec'].get('http_status', ''), item['rec'].get('final_url') or ''
            if item['obs']['availability'] == 'ACCESS_FAILED':
                status = {401: 'AUTH_REQUIRED', 403: 'BLOCKED_TO_TOOL'}.get(http, 'HTTP_ERROR' if http else 'NETWORK_ERROR')
            else:
                status = 'JS_ONLY_SHELL' if js else 'ACCESSIBLE'
            ev_by_resource.setdefault(n, []).append(eid)
        endpoints.append({'endpoint_id': f'{rid(n)}-E{counter[n]:02d}', 'resource_id': rid(n), 'endpoint_role': role, 'url': url,
                          'url_source': source, 'auth_required': auth, 'access_status': status, 'http_status': http, 'final_url': final,
                          'tested_at_utc': tested, 'evidence_id': eid, 'notes': note})

    # ---- resources and discovery log
    resources, discovery, linked = [], [], {}
    for r in cur.RESOURCES:
        n, seed = r['n'], r.get('seed', '')
        s = seeds.get(seed, {})
        row = {c: NA for c in RESOURCE_COLS}
        basis = []
        for key, col in FIELDS:
            raw = r.get(key)
            if raw is None and key in SEED_FALLBACK and s.get(SEED_FALLBACK[key]):
                raw = s[SEED_FALLBACK[key]] + '|S'
            if raw is None:
                continue
            value, tag = split_tag(raw)
            row[col] = value
            if tag:
                basis.append(f'{col}:{tag}')
        origin = r.get('origin') or ('SEED' if seed else 'SYSTEMATIC_SEARCH')
        ev = list(ev_by_resource.get(n, []))
        for h in cur.EXTRA_EVIDENCE.get(n, []):
            ev.append(handle(h))
        ev += [e for e, _ in by_label.get(rid(n), [])]  # captures and inspections filed under the resource identifier
        if seed:
            discovery.append({'entry_type': 'RESOURCE_DISCOVERY', 'resource_id': rid(n), 'origin': 'SEED',
                              'note': 'Record of the exploratory inventory (inputs/seed_inventory_v0_1.csv); not found by a registered search.'})
            for spec in cur.SEED_REFOUND.get(n, []):
                for h in match_hits(spec):
                    ev.append(by_search[h['search_id']])
                    linked[h['search_id']] = linked.get(h['search_id'], 0) + 1
                    discovery.append({'entry_type': 'SEED_REFOUND_BY_SEARCH', 'resource_id': rid(n), 'origin': 'SEED', 'search_id': h['search_id'],
                                      'platform': h['platform'], 'hit_rank': h['rank'], 'platform_record_id': h['platform_record_id'],
                                      'hit_title': h['title'], 'evidence_id': by_search[h['search_id']],
                                      'note': 'The seed, one of its distributions or its data paper was returned by this search.'})
        for spec in r.get('hits', []):
            for h in match_hits(spec):
                ev.append(by_search[h['search_id']])
                linked[h['search_id']] = linked.get(h['search_id'], 0) + 1
                discovery.append({'entry_type': 'RESOURCE_DISCOVERY', 'resource_id': rid(n), 'origin': origin, 'search_id': h['search_id'],
                                  'platform': h['platform'], 'hit_rank': h['rank'], 'platform_record_id': h['platform_record_id'],
                                  'hit_title': h['title'], 'evidence_id': by_search[h['search_id']],
                                  'note': 'Dataset located through a hit that uses or cites it.' if origin == 'BACKWARD_FORWARD_DISCOVERY' else ''})
        for label in ([r['found_in']] if r.get('found_in') else []):
            eid = by_url[label][0]
            ev.append(eid)
            discovery.append({'entry_type': 'RESOURCE_DISCOVERY', 'resource_id': rid(n), 'origin': origin, 'evidence_id': eid,
                              'note': f'Named or linked in the captured page {label}'})
        if r.get('sweep'):
            for eid, _ in by_label.get(r['sweep'], []):
                ev.append(eid)
                discovery.append({'entry_type': 'RESOURCE_DISCOVERY', 'resource_id': rid(n), 'origin': origin, 'evidence_id': eid,
                                  'note': f"Institutional sweep step {r['sweep']}: {r.get('sweep_note', '')}".strip()})
        ev = sorted(set(ev))
        good = {e['evidence_id'] for e in evidence if e['outcome'] in ('CAPTURED', 'EXECUTED', 'READ')}
        success = [e for e in ev if e in good]
        peeks = [p for p in peeks_by_resource.get(rid(n), [])]
        caps = caps_by_resource.get(rid(n), [])
        auto_notes = []  # derived, deterministic notes from the inspections
        for item in peeks:
            avail, rec_ = item['obs']['availability'], item['rec']
            if avail == 'ACCESS_FAILED':
                auto_notes.append(f"[inspection {item['eid']}] {rec_['url'][:90]} answered {rec_.get('http_status') or rec_.get('error', '')[:60]}; an access failure, not evidence about the resource.")
            elif avail == 'LANDING_PAGE_ONLY':
                auto_notes.append(f"[inspection {item['eid']}] {rec_['url'][:90]} returned an HTML page, not data.")
            elif avail == 'LISTING_ONLY':
                auto_notes.append(f"[inspection {item['eid']}] only a repository listing was read.")
        row.update({'resource_id': rid(n), 'seed_id': seed, 'registered_name': s.get('name', ''), 'resource_category': r['cat'],
                    'category_status': 'CANDIDATE', 'resource_set': r['set'], 'description_url': r.get('desc', NA),
                    'primary_access_url': r.get('url', NA), 'individuation_status': r['indiv'],
                    'eligibility_preliminary': r.get('elig', 'INCLUDE'), 'verification_status': r['status'],
                    'verification_date': VERIFICATION_DATES.get(r.get('last_round'), cur.VERIFICATION_DATE),
                    'discovery_origin': origin, 'field_basis': '; '.join(basis),
                    'classification_basis': 'AGENT_PROVISIONAL', 'researcher_confirmed': 'NO',
                    'evidence_ids': ';'.join(ev), 'uncertainties': ' '.join([r.get('unc', '')] + auto_notes).strip(), 'first_round': r['first_round']})
        row['resource_level'] = resource_level(r['cat'])
        row['identity_level'], row['data_availability_level'], row['capability_level'] = derive_levels(row, success, peeks, caps)
        resources.append(row)

    runs = []
    for rec in sorted(search_log, key=lambda x: x['search_id']):
        note = rec['outcome'] if rec['outcome'] != 'EXECUTED' else ('first 25 results screened by title' if rec.get('hits_returned') else 'no results')
        if rec['outcome'] == 'EXECUTED' and rec.get('depth_rationale'):
            note = f"{rec['hits_returned']} results; depth: {rec['depth_rationale']}"
        runs.append({'entry_type': 'SEARCH_RUN', 'search_id': rec['search_id'], 'platform': rec['platform'], 'query': rec['query'],
                     'language': rec['language'], 'executed_at_utc': rec['executed_at_utc'],
                     'total_reported': '' if rec.get('total_reported') is None else rec['total_reported'],
                     'hits_returned': rec.get('hits_returned', ''), 'hits_linked_to_resources': linked.get(rec['search_id'], 0),
                     'evidence_id': by_search[rec['search_id']], 'note': note})
    discovery = runs + discovery
    for i, d in enumerate(discovery, 1):
        d['discovery_id'] = f'DL-{i:04d}'

    # ---- relations
    relations = []
    for i, (src, rtype, dst, conf, status, basis, handles, why) in enumerate(cur.RELATIONS, 1):
        relations.append({'relation_id': f'MREL-{i:05d}', 'source_resource_id': rid(src), 'relation_type': rtype,
                          'target_resource_id': rid(dst), 'confidence': conf, 'relation_status': status, 'basis': basis,
                          'evidence_ids': ';'.join(handle(h) for h in handles), 'justification': why, 'assessed_by': 'AGENT_PROVISIONAL',
                          'researcher_confirmed': 'NO', 'assessed_on': cur.VERIFICATION_DATE})

    # ---- decisions
    decisions = [{'decision_id': f'DEC-{i:04d}', 'decision_type': t, 'subject': subj, 'decision': dec, 'rationale': why,
                  'evidence_ids': ';'.join(handle(h) for h in handles), 'decided_by': 'AGENT_PROVISIONAL',
                  'decided_on': cur.VERIFICATION_DATE, 'status': 'OPEN_TO_REVISION'}
                 for i, (t, subj, dec, why, handles) in enumerate(cur.DECISIONS, 1)]

    # ---- verification history (status changes made by later rounds)
    history = []
    for p in cur.PATCH_LOG:
        change = p['changes'].get('status')
        if change:
            history.append({'resource_id': rid(p['n']), 'round': p['round'], 'from_status': change[0], 'to_status': change[1],
                            'reason': p['reason'], 'evidence_ids': ';'.join(sorted({e for e, _ in by_label.get(rid(p['n']), [])})),
                            'changed_on': p['date']})
    for i, h in enumerate(history, 1):
        h['history_id'] = f'VH-{i:04d}'

    # ---- seed audit
    audit = []
    for seed_id, s in seeds.items():
        r = next(x for x in resources if x['seed_id'] == seed_id)
        role = next((e['endpoint_role'] for e in endpoints if e['resource_id'] == r['resource_id'] and e['url'] == s['source_url']), 'NOT_RECORDED_AS_ENDPOINT')
        rels = [f"{x['relation_type']}>{x['target_resource_id']}({x['relation_status']},{x['confidence']})" for x in relations if x['source_resource_id'] == r['resource_id']]
        rels += [f"{x['source_resource_id']}>{x['relation_type']}(in;{x['relation_status']},{x['confidence']})" for x in relations if x['target_resource_id'] == r['resource_id']]
        row = {c: r.get(c, '') for c in SEED_AUDIT_COLS}
        row.update({'seed_id': seed_id, 'registered_name': s['name'], 'registered_url': s['source_url'], 'registered_url_role': role,
                    'relations': ' | '.join(rels)})
        audit.append(row)
    assert {r['resource_id'] for r in resources} >= {rid(i) for i in range(1, 42)}

    # ---- institutional sweep
    sweep_rows = []
    sweep_path = sweep_registry if sweep_registry is not None else MAPPING / 'protocol' / 'INSTITUTIONAL_SWEEP_G2_ROUND2.csv'
    for row in read_csv(sweep_path):
        got = by_label.get(row['sweep_id'], [])
        eid, ok = got[-1] if got else ('', False)
        rec = by_url.get(row['url'], ('', None))[1]
        last = (rec['attempts'][-1] if rec and rec.get('attempts') else {})
        found, note = cur.SWEEP_NOTES.get(row['sweep_id'], ([], ''))
        sweep_rows.append({'sweep_id': row['sweep_id'], 'step': row['step'], 'body': row['body'], 'body_type': row['body_type'],
                           'url': row['url'], 'purpose': row['purpose'], 'outcome': ('CAPTURED' if ok else 'FAILED') if got else 'NOT_RUN',
                           'http_status': (rec.get('http_status') or last.get('http_status') or '') if rec else '',
                           'final_url': (rec.get('final_url') or '') if rec else '', 'evidence_id': eid,
                           'found_resources': ';'.join(rid(x) for x in found), 'result_note': note})

    # ---- prior-art reference list
    lynx_rows = []
    for i, x in enumerate(cur.LYNX, 1):
        evid = [e for e, _ in by_label.get('LYNX-D2.8-PDF', [])] if x['source'] in ('D2.8', 'BOTH') else [e for e, _ in by_label.get('LYNX-D2.7-PDF', [])]
        lynx_rows.append({'lynx_id': f'LYX-{i:03d}', 'source': x['source'], 'area': x['area'], 'url': x['url'], 'law': x['law'],
                          'case_law': x['case_law'], 'eli': x['eli'], 'ecli': x['ecli'], 'access_interface': x['access'],
                          'in_scope_by_rule': x['scope'], 'match_status': x['match'], 'matched_resource_id': x.get('matched', ''),
                          'match_basis': x.get('basis', ''), 'source_evidence_id': evid[-1] if evid else '', 'note': x.get('note', '')})

    return {'resources': (RESOURCE_COLS, resources), 'access_endpoints': (ENDPOINT_COLS, endpoints),
            'resource_relations': (RELATION_COLS, relations), 'discovery_log': (DISCOVERY_COLS, discovery),
            'evidence_registry': (EVIDENCE_COLS, evidence), 'decisions_log': (DECISION_COLS, decisions),
            'seed_audit': (SEED_AUDIT_COLS, audit), 'search_hits': (mapping_search.HIT_FIELDS, hits),
            'verification_history': (HISTORY_COLS, history), 'data_inspections': (INSPECTION_COLS, inspection_rows),
            'capabilities': (CAPABILITY_COLS, capability_rows), 'institutional_sweep': (SWEEP_COLS, sweep_rows),
            'lynx_reference': (LYNX_COLS, lynx_rows)}


VERIFICATION_DATES = {'G2-R1': '2026-10-10', 'G2-R2': '2026-10-10'}


def write(tables, out_dir=MAPPING / 'data'):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for name, (cols, rows) in tables.items():
        with (out_dir / f'{name}.csv').open('w', encoding='utf-8', newline='') as fh:
            w = csv.DictWriter(fh, fieldnames=cols, lineterminator='\n', restval='')
            w.writeheader()
            w.writerows(rows)


if __name__ == '__main__':
    built = build()
    write(built)
    for name, (_, rows) in built.items():
        print(f'{name}.csv: {len(rows)} rows')
