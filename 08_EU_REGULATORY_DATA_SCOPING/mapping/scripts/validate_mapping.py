#!/usr/bin/env python3
"""Quality checks for the G2 mapping base. No network.

Returns a list of (severity, check, message). ERROR means the base breaks a rule
of the protocol; WARNING is something a person should look at. The checks test
the form and the internal consistency of the base. They say nothing about
whether the mapping covers the field.
"""
import csv
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[2]
MAPPING = ROOT / 'mapping'
SEED_SHA256 = '45316803ea07f677e0e25b0c559ae2cbee43790da06fb86240953cc9bf670bdd'  # inputs/seed_inventory_v0_1.csv since G0
TABLES = ['resources', 'access_endpoints', 'resource_relations', 'discovery_log', 'evidence_registry', 'decisions_log', 'seed_audit',
          'verification_history', 'data_inspections', 'capabilities', 'institutional_sweep', 'lynx_reference']
ID_PATTERNS = {'resources': ('resource_id', r'^MR-\d{4}$'), 'access_endpoints': ('endpoint_id', r'^MR-\d{4}-E\d{2}$'),
               'resource_relations': ('relation_id', r'^MREL-\d{5}$'), 'discovery_log': ('discovery_id', r'^DL-\d{4}$'),
               'evidence_registry': ('evidence_id', r'^EV[CSHP]-\d{3,4}$'), 'decisions_log': ('decision_id', r'^DEC-\d{4}$'),
               'verification_history': ('history_id', r'^VH-\d{4}$'), 'data_inspections': ('inspection_id', r'^EVP-\d{4}$'),
               'capabilities': ('capability_id', r'^CAP-\d{4}$'), 'institutional_sweep': ('sweep_id', r'^SW-\d{3}$'),
               'lynx_reference': ('lynx_id', r'^LYX-\d{3}$')}
VOCAB_COLUMNS = {
    'resources': {'resource_category': 'resource_category', 'category_status': 'category_status', 'resource_set': 'resource_set',
                  'territorial_scope': 'territorial_scope', 'individuation_status': 'individuation_status',
                  'eligibility_preliminary': 'eligibility_preliminary', 'verification_status': 'verification_status',
                  'discovery_origin': 'discovery_origin', 'classification_basis': 'classification_basis',
                  'researcher_confirmed': 'researcher_confirmed', 'resource_level': 'resource_level', 'identity_level': 'identity_level',
                  'data_availability_level': 'data_availability_level', 'capability_level': 'capability_level'},
    'access_endpoints': {'endpoint_role': 'endpoint_role', 'url_source': 'endpoint_url_source', 'auth_required': 'auth_required',
                         'access_status': 'access_status'},
    'resource_relations': {'relation_type': 'relation_type', 'confidence': 'relation_confidence', 'relation_status': 'relation_status',
                           'basis': 'relation_basis'},
    'discovery_log': {'entry_type': 'discovery_entry_type'},
    'evidence_registry': {'evidence_type': 'evidence_type', 'outcome': 'evidence_outcome'},
    'decisions_log': {'decision_type': 'decision_type', 'decided_by': 'decided_by'},
    'capabilities': {'capability': 'capability', 'method': 'capability_method'},
    'institutional_sweep': {'outcome': 'sweep_outcome'},
    'lynx_reference': {'match_status': 'lynx_match_status', 'in_scope_by_rule': 'lynx_scope'},
}


def read_table(path):
    with Path(path).open(encoding='utf-8-sig', newline='') as fh:
        return list(csv.DictReader(fh))


def load(data_dir=MAPPING / 'data'):
    return {t: read_table(Path(data_dir) / f'{t}.csv') for t in TABLES}


def valid_url(url):
    parts = urlsplit(url)
    return parts.scheme in ('http', 'https') and bool(parts.netloc) and ' ' not in url


def split_ids(cell):
    return [x for x in cell.split(';') if x]


def validate(tables, vocab, seed_path=ROOT / 'inputs' / 'seed_inventory_v0_1.csv', shared_urls=(), check_files=True, root=ROOT):
    out = []

    def err(check, msg):
        out.append(('ERROR', check, msg))

    def warn(check, msg):
        out.append(('WARNING', check, msg))

    res, ends, rels = tables['resources'], tables['access_endpoints'], tables['resource_relations']
    disc, evid, decs = tables['discovery_log'], tables['evidence_registry'], tables['decisions_log']

    # 1. identifiers: unique, well formed
    for table, (col, pattern) in ID_PATTERNS.items():
        seen = set()
        for row in tables[table]:
            v = row[col]
            if not re.match(pattern, v):
                err('id_format', f'{table}: malformed identifier {v!r}')
            if v in seen:
                err('id_unique', f'{table}: duplicate identifier {v}')
            seen.add(v)

    # 2. controlled vocabularies
    for table, cols in VOCAB_COLUMNS.items():
        for row in tables[table]:
            for col, key in cols.items():
                if row[col] not in vocab[key]:
                    err('vocabulary', f'{table}.{col}: {row[col]!r} is not in vocabulary {key}')
    for row in res:
        for item in filter(None, row['field_basis'].split('; ')):
            if item.rsplit(':', 1)[-1] not in vocab['field_basis']:
                err('vocabulary', f"{row['resource_id']}: field basis {item!r} not in vocabulary")

    # 3. referential integrity
    rids = {r['resource_id'] for r in res}
    eids = {e['evidence_id'] for e in evid}
    for e in ends:
        if e['resource_id'] not in rids:
            err('reference', f"{e['endpoint_id']}: unknown resource {e['resource_id']}")
        if e['evidence_id'] and e['evidence_id'] not in eids:
            err('reference', f"{e['endpoint_id']}: unknown evidence {e['evidence_id']}")
    for r in rels:
        for col in ('source_resource_id', 'target_resource_id'):
            if r[col] not in rids:
                err('reference', f"{r['relation_id']}: {col} {r[col]} does not exist")
        if r['source_resource_id'] == r['target_resource_id']:
            err('reference', f"{r['relation_id']}: relation of a resource with itself")
    for table, rows, idcol in (('resources', res, 'resource_id'), ('resource_relations', rels, 'relation_id'), ('decisions_log', decs, 'decision_id')):
        for row in rows:
            for x in split_ids(row['evidence_ids']):
                if x not in eids:
                    err('reference', f'{row[idcol]}: unknown evidence {x}')
    for d in disc:
        if d['resource_id'] and d['resource_id'] not in rids:
            err('reference', f"{d['discovery_id']}: unknown resource {d['resource_id']}")
        if d['evidence_id'] and d['evidence_id'] not in eids:
            err('reference', f"{d['discovery_id']}: unknown evidence {d['evidence_id']}")

    # 4. URL syntax
    for e in ends:
        if not valid_url(e['url']):
            err('url_syntax', f"{e['endpoint_id']}: {e['url']!r}")
    for r in res:
        for col in ('description_url', 'primary_access_url'):
            if r[col] != vocab['not_assessed_token'] and not valid_url(r[col]):
                err('url_syntax', f"{r['resource_id']}.{col}: {r[col]!r}")

    # 5. exact duplicates
    seen = {}
    for r in res:
        key = (r['verified_name'].casefold(), r['maintainer'].casefold())
        if key in seen:
            err('duplicate', f"{r['resource_id']} repeats name and maintainer of {seen[key]}")
        seen[key] = r['resource_id']
    for col in ('primary_access_url', 'description_url'):
        seen = {}
        for r in res:
            u = r[col]
            if u == vocab['not_assessed_token']:
                continue
            if u in seen and u not in shared_urls:
                err('duplicate', f"{r['resource_id']} and {seen[u]} share {col} {u} without a recorded justification")
            seen.setdefault(u, r['resource_id'])
    seen = set()
    for r in rels:
        key = (r['source_resource_id'], r['relation_type'], r['target_resource_id'])
        if key in seen:
            err('duplicate', f"{r['relation_id']}: relation repeated {key}")
        seen.add(key)
    seen = set()
    for e in ends:
        key = (e['resource_id'], e['url'])
        if key in seen:
            err('duplicate', f"{e['endpoint_id']}: endpoint URL repeated within the resource")
        seen.add(key)

    # 6. evidence behind verified statements; verified versus inferred
    good = {e['evidence_id'] for e in evid if e['outcome'] in ('CAPTURED', 'EXECUTED')}
    for r in res:
        ev = split_ids(r['evidence_ids'])
        status = r['verification_status']
        if status in ('VERIFIED', 'PARTIALLY_VERIFIED') and not any(x in good for x in ev):
            err('evidence', f"{r['resource_id']}: status {status} without any successful evidence")
        if status == 'VERIFIED':
            for col in ('verified_name', 'maintainer'):
                tag = next((b.rsplit(':', 1)[-1] for b in r['field_basis'].split('; ') if b.startswith(col + ':')), '')
                if col == 'verified_name' and tag not in ('PRIMARY_PAGE', 'API_METADATA'):
                    err('evidence', f"{r['resource_id']}: VERIFIED but the name is not based on a primary page or API metadata")
        if status == 'INACCESSIBLE' and any(x in good for x in ev):
            err('evidence', f"{r['resource_id']}: INACCESSIBLE although a successful capture is attached")
        if status in ('DISCOVERED', 'INDETERMINATE', 'INACCESSIBLE') and not ev:
            err('evidence', f"{r['resource_id']}: no evidence of how it was found or attempted")
        if r['classification_basis'] == 'AGENT_PROVISIONAL' and (r['researcher_confirmed'] != 'NO' or r['category_status'] != 'CANDIDATE'):
            err('provisional', f"{r['resource_id']}: agent-provisional row presented as confirmed")
        if r['classification_basis'] == 'RESEARCHER_CONFIRMED' and r['researcher_confirmed'] != 'YES':
            err('provisional', f"{r['resource_id']}: inconsistent confirmation fields")
        for col in ('verified_name', 'maintainer', 'thematic_coverage', 'temporal_coverage', 'formats', 'licence_or_reuse', 'access_conditions'):
            if r[col] != vocab['not_assessed_token'] and not any(b.startswith(col + ':') for b in r['field_basis'].split('; ')):
                err('basis', f"{r['resource_id']}.{col}: value without a declared basis")
        if not r['uncertainties']:
            warn('uncertainty', f"{r['resource_id']}: no uncertainty or limitation recorded")
    for r in rels:
        ev = split_ids(r['evidence_ids'])
        if not ev or not r['justification']:
            err('evidence', f"{r['relation_id']}: relation without evidence or justification")
        if r['relation_status'] == 'SUPPORTED' and (r['basis'] == 'AGENT_INFERENCE' or r['confidence'] == 'LOW'):
            err('evidence', f"{r['relation_id']}: SUPPORTED relation resting on inference or low confidence")
        if r['basis'] == 'AGENT_INFERENCE' and r['confidence'] != 'LOW':
            err('evidence', f"{r['relation_id']}: inferred relation must carry LOW confidence")
    for e in ends:
        if e['access_status'] != 'NOT_TESTED' and not e['evidence_id']:
            err('evidence', f"{e['endpoint_id']}: tested endpoint without evidence")
        if e['access_status'] == 'AUTH_REQUIRED' and e['auth_required'] != 'YES':
            err('evidence', f"{e['endpoint_id']}: 401 recorded but auth_required is not YES")

    # 7. discovery origins
    searches = {d['search_id'] for d in disc if d['entry_type'] == 'SEARCH_RUN'}
    found = {}
    for d in disc:
        if d['entry_type'] == 'RESOURCE_DISCOVERY':
            found.setdefault(d['resource_id'], []).append(d)
        if d['entry_type'] != 'SEARCH_RUN' and d['search_id'] and d['search_id'] not in searches:
            err('origin', f"{d['discovery_id']}: refers to a search that was not run ({d['search_id']})")
    for r in res:
        rows = found.get(r['resource_id'], [])
        if not rows:
            err('origin', f"{r['resource_id']}: no discovery record")
        if r['discovery_origin'] == 'SYSTEMATIC_SEARCH' and not any(d['search_id'] for d in rows):
            err('origin', f"{r['resource_id']}: origin SYSTEMATIC_SEARCH without a registered search hit")
        if r['discovery_origin'] == 'SEED' and not r['seed_id']:
            err('origin', f"{r['resource_id']}: origin SEED without seed identifier")

    # 7b. evidence levels, inspections, capabilities (round 2)
    insp_by_res = {}
    for i in tables['data_inspections']:
        if i['resource_id'] not in rids:
            err('reference', f"{i['inspection_id']}: unknown resource {i['resource_id']}")
        insp_by_res.setdefault(i['resource_id'], []).append(i)
    caps_by_res = {}
    for c in tables['capabilities']:
        if c['resource_id'] not in rids:
            err('reference', f"{c['capability_id']}: unknown resource {c['resource_id']}")
        if c['evidence_id'] not in eids:
            err('reference', f"{c['capability_id']}: unknown evidence {c['evidence_id']}")
        caps_by_res.setdefault(c['resource_id'], []).append(c)
    for r in res:
        rid_ = r['resource_id']
        level = r['data_availability_level']
        seen = {i['availability_observed'] for i in insp_by_res.get(rid_, [])}
        if level == 'DATA_AVAILABILITY_VERIFIED' and 'DATA_AVAILABILITY_VERIFIED' not in seen:
            err('levels', f'{rid_}: DATA_AVAILABILITY_VERIFIED without an inspection that read data')
        if level == 'NOT_TESTED' and seen:
            err('levels', f'{rid_}: inspections exist but the availability level is NOT_TESTED')
        if r['capability_level'] == 'CAPABILITY_VERIFIED' and not caps_by_res.get(rid_):
            err('levels', f'{rid_}: CAPABILITY_VERIFIED without an observed capability')
        if r['capability_level'] == 'NOT_ASSESSED' and caps_by_res.get(rid_):
            err('levels', f'{rid_}: capabilities observed but the level is NOT_ASSESSED')
        if r['identity_level'] == 'IDENTITY_VERIFIED':
            basis = dict(b.rpartition(':')[::2] for b in r['field_basis'].split('; ') if b)
            if basis.get('verified_name') not in ('PRIMARY_PAGE', 'API_METADATA') or basis.get('maintainer') not in ('PRIMARY_PAGE', 'API_METADATA'):
                err('levels', f'{rid_}: IDENTITY_VERIFIED although name or maintainer is not based on a primary page or record')
        if r['verification_status'] == 'VERIFIED' and r['identity_level'] != 'IDENTITY_VERIFIED':
            warn('levels', f"{rid_}: historical status VERIFIED but identity level {r['identity_level']} (name or maintainer inferred or from the seed)")
        if r['verification_status'] == 'INACCESSIBLE' and r['data_availability_level'] == 'DATA_AVAILABILITY_VERIFIED':
            err('levels', f'{rid_}: INACCESSIBLE with verified data availability')
        expected = ('LEVEL_I_DATA' if r['resource_category'] in ('DATASET', 'CORPUS', 'BENCHMARK', 'ADMINISTRATIVE_REGISTER', 'REPOSITORY')
                    else 'DISTRIBUTION_OF_LEVEL_I' if r['resource_category'] == 'DATA_DISTRIBUTION'
                    else 'UNASSIGNED' if r['resource_category'] == 'INDETERMINATE' else 'LEVEL_II_INFRASTRUCTURE')
        if r['resource_level'] != expected:
            err('levels', f"{rid_}: resource_level {r['resource_level']} does not follow the category {r['resource_category']}")
        if r['resource_category'] == 'DATA_DISTRIBUTION' and r['individuation_status'] == 'INDIVIDUATED':
            err('inclusion', f'{rid_}: a distribution cannot be an individuated resource')
        if r['resource_category'] == 'SOFTWARE_OR_PIPELINE' and r['individuation_status'] == 'INDIVIDUATED':
            warn('inclusion', f'{rid_}: software individuated as a resource; the inclusion rule excludes software without data of its own')
    hist_ids = {h['resource_id'] for h in tables['verification_history']}
    for h in tables['verification_history']:
        if h['resource_id'] not in rids:
            err('reference', f"{h['history_id']}: unknown resource {h['resource_id']}")
        if h['from_status'] == h['to_status']:
            err('history', f"{h['history_id']}: no change of status")
    for sw in tables['institutional_sweep']:
        for x in split_ids(sw['found_resources']):
            if x not in rids:
                err('reference', f"{sw['sweep_id']}: unknown resource {x}")
        if sw['outcome'] == 'FAILED' and sw['found_resources']:
            err('evidence', f"{sw['sweep_id']}: resources attributed to a failed request")
    for ly in tables['lynx_reference']:
        if ly['matched_resource_id'] and ly['matched_resource_id'] not in rids:
            err('reference', f"{ly['lynx_id']}: unknown resource {ly['matched_resource_id']}")
        if ly['match_status'] in ('MATCHED', 'MATCHED_AS_ENDPOINT', 'RELATED') and not (ly['matched_resource_id'] and ly['match_basis']):
            err('evidence', f"{ly['lynx_id']}: match without resource or basis")
        if ly['match_status'] in ('ABSENT_SCOPE_OPEN', 'NOT_APPLICABLE') and ly['matched_resource_id']:
            err('evidence', f"{ly['lynx_id']}: absent entry with a matched resource")

    # 8. preservation of the historical seed inventory
    seed_path = Path(seed_path)
    if hashlib.sha256(seed_path.read_bytes()).hexdigest() != SEED_SHA256:
        err('preservation', 'inputs/seed_inventory_v0_1.csv differs from the G0 file')
    seeds = read_table(seed_path)
    by_seed = {r['seed_id']: r for r in res if r['seed_id']}
    if [s['source_seed_id'] for s in seeds] != [r['seed_id'] for r in res if r['seed_id']]:
        err('preservation', 'seed identifiers are not all present, once each, in the original order')
    for s in seeds:
        r = by_seed.get(s['source_seed_id'])
        if r and r['registered_name'] != s['name']:
            err('preservation', f"{s['source_seed_id']}: registered_name differs from the seed inventory")
    audit = tables['seed_audit']
    if [a['seed_id'] for a in audit] != [s['source_seed_id'] for s in seeds]:
        err('preservation', 'seed_audit.csv does not list the 41 seeds in order')
    for a, s in zip(audit, seeds):
        if a['registered_url'] != s['source_url'] or a['registered_name'] != s['name']:
            err('preservation', f"{a['seed_id']}: seed_audit alters a registered value")

    # 9. stored evidence files match their hashes
    if check_files:
        for e in evid:
            if e['stored_file']:
                path = Path(root) / e['stored_file']
                if not path.exists():
                    err('evidence_file', f"{e['evidence_id']}: file missing ({e['stored_file']})")
                elif hashlib.sha256(path.read_bytes()).hexdigest() != e['sha256']:
                    err('evidence_file', f"{e['evidence_id']}: hash mismatch")
    return out


def main():
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import build_mapping_base as bmb
    vocab = json.loads((MAPPING / 'schemas' / 'mapping_vocabularies.json').read_text(encoding='utf-8'))
    cur = bmb.load_curation()
    findings = validate(load(), vocab, shared_urls=set(cur.SHARED_URL_JUSTIFICATIONS))
    for sev, check, msg in findings:
        print(f'{sev:7} {check:14} {msg}')
    errors = sum(1 for f in findings if f[0] == 'ERROR')
    print(f'{errors} error(s), {len(findings) - errors} warning(s)')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
