#!/usr/bin/env python3
"""Descriptive counts of the mapping base, round 1 (frozen snapshot) versus round 2 (live tables). No network.

The counts describe what the rounds reached. They are not estimates of the population of resources
and a difference between rounds is a difference in effort and method, not growth or shrinkage of the field.
"""
import collections
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / 'mapping' / 'data'
SNAP = ROOT / 'mapping' / 'snapshots' / 'round1'


def read(path):
    with Path(path).open(encoding='utf-8-sig', newline='') as fh:
        return list(csv.DictReader(fh))


def C(rows, key, where=None):
    return dict(collections.Counter(r[key] for r in rows if (where is None or where(r))).most_common())


def family(maintainer):
    m = maintainer
    if 'Publications Office' in m:
        return 'Publications Office'
    if any(x in m for x in ('European Commission', 'Directorate-General', 'Secretariat-General', 'Joint Research Centre')):
        return 'European Commission'
    if any(x in m for x in ('European Securities', 'European Banking', 'Insurance and Occupational', 'Single Resolution', 'European Central Bank')):
        return 'Financial supervision (ESMA, EBA, EIOPA, SRB, ECB)'
    if any(x in m for x in ('Chemicals', 'Medicines', 'Food Safety', 'Railways', 'Maritime', 'Environment Agency', 'Energy Regulators', 'BEREC',
                            'Plant Variety', 'Fisheries Control', 'Data Protection', 'Aviation', 'Ombudsman')):
        return 'Other EU agencies and bodies'
    if any(x in m for x in ('Parliament', 'Council of the European', 'Court of Justice')):
        return 'Parliament, Council, Court'
    if m == 'NOT_ASSESSED':
        return 'Not assessed'
    return 'Academic, individual, civic or national'


def stats(res, rel, disc, evi, ends, caps=None, insp=None):
    s = {}
    s['rows'] = len(res)
    s['individuation'] = C(res, 'individuation_status')
    s['status'] = C(res, 'verification_status')
    s['origin'] = C(res, 'discovery_origin')
    s['set_all'] = C(res, 'resource_set')
    s['category'] = C(res, 'resource_category')
    s['eligibility'] = C(res, 'eligibility_preliminary')
    s['territory'] = C(res, 'territorial_scope')
    if 'resource_level' in res[0]:
        ind = lambda r: r['individuation_status'] == 'INDIVIDUATED'  # noqa: E731
        s['level_individuated'] = C(res, 'resource_level', ind)
        s['level_all'] = C(res, 'resource_level')
        s['identity'] = C(res, 'identity_level')
        s['availability'] = C(res, 'data_availability_level')
        s['capability'] = C(res, 'capability_level')
        s['set_x_level_individuated'] = {f'{k[0]}|{k[1]}': v for k, v in collections.Counter((r['resource_set'], r['resource_level']) for r in res if ind(r)).items()}
        s['availability_by_level'] = {f'{k[0]}|{k[1]}': v for k, v in collections.Counter((r['resource_level'], r['data_availability_level']) for r in res).items()}
        s['availability_by_set'] = {f'{k[0]}|{k[1]}': v for k, v in collections.Counter((r['resource_set'], r['data_availability_level']) for r in res).items()}
    s['licence_stated'] = sum(1 for r in res if r['licence_or_reuse'] != 'NOT_ASSESSED')
    s['temporal_stated'] = sum(1 for r in res if r['temporal_coverage'] != 'NOT_ASSESSED')
    s['formats_stated'] = sum(1 for r in res if r['formats'] != 'NOT_ASSESSED')
    s['maintainer_stated'] = sum(1 for r in res if r['maintainer'] != 'NOT_ASSESSED')
    s['conditions_stated'] = sum(1 for r in res if r['access_conditions'] != 'NOT_ASSESSED')
    s['families_set_B'] = C([dict(r, fam=family(r['maintainer'])) for r in res if r['resource_set'] in ('B', 'AB')], 'fam')
    s['relations_type'] = C(rel, 'relation_type')
    s['relations_status'] = C(rel, 'relation_status')
    s['endpoints_status'] = C(ends, 'access_status')
    s['endpoints_role'] = C(ends, 'endpoint_role')
    s['evidence'] = C(evi, 'evidence_type')
    runs = [d for d in disc if d['entry_type'] == 'SEARCH_RUN']
    s['searches'] = len(runs)
    s['searches_platform'] = C(runs, 'platform')
    s['searches_zero_linked'] = sum(1 for d in runs if d['hits_linked_to_resources'] in ('0', 0))
    s['hits_returned'] = sum(int(d['hits_returned'] or 0) for d in runs)
    s['hits_linked'] = sum(int(d['hits_linked_to_resources']) for d in runs)
    return s


def main():
    r1 = stats(read(SNAP / 'resources.csv'), read(SNAP / 'resource_relations.csv'), read(SNAP / 'discovery_log.csv'),
               read(SNAP / 'evidence_registry.csv'), read(SNAP / 'access_endpoints.csv'))
    res2 = read(DATA / 'resources.csv')
    r2 = stats(res2, read(DATA / 'resource_relations.csv'), read(DATA / 'discovery_log.csv'), read(DATA / 'evidence_registry.csv'),
               read(DATA / 'access_endpoints.csv'))
    out = {'round1': r1, 'round2_live': r2}
    new = [r for r in res2 if r['first_round'] == 'G2-R2']
    out['round2_new_only'] = {
        'rows': len(new), 'individuation': C(new, 'individuation_status'), 'status': C(new, 'verification_status'),
        'origin': C(new, 'discovery_origin'), 'set': C(new, 'resource_set'), 'category': C(new, 'resource_category'),
        'level': C(new, 'resource_level'), 'availability': C(new, 'data_availability_level'), 'identity': C(new, 'identity_level'),
        'families_set_B': C([dict(r, fam=family(r['maintainer'])) for r in new if r['resource_set'] in ('B', 'AB')], 'fam')}
    hist = read(DATA / 'verification_history.csv')
    out['status_changes'] = C([dict(h, pair=f"{h['from_status']}->{h['to_status']}") for h in hist], 'pair')
    out['sweep'] = C(read(DATA / 'institutional_sweep.csv'), 'outcome')
    out['lynx'] = C(read(DATA / 'lynx_reference.csv'), 'match_status')
    insp = read(DATA / 'data_inspections.csv')
    out['inspections'] = {'n': len(insp), 'availability': C(insp, 'availability_observed'), 'content_kind': C(insp, 'content_kind'),
                          'http': C(insp, 'http_status')}
    json.dump(out, sys.stdout, indent=1, ensure_ascii=False)
    print()


if __name__ == '__main__':
    main()
