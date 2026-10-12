#!/usr/bin/env python3
"""Draw the PROPOSED human-validation sample from the mapping base. Deterministic; no network.

This only proposes which rows a second person should classify. It assigns nobody, simulates no
judgement, and writes no classification. The sample is a proposal until the researcher in charge
decides sizes, strata and reviewer.

Strata (a row can qualify for several; it is drawn once, under the first stratum that claims it):
  S1 ambiguous    census: category INDETERMINATE, or individuation not INDIVIDUATED
  S2 scope        census: eligibility UNCERTAIN
  S3 boundary     census: set AB; plus a random draw of sets A and B among INDIVIDUATED rows, per round
  S4 individuated random draw among the remaining INDIVIDUATED rows, stratified by level and first round
  S5 relations    census of CANDIDATE relations with MEDIUM confidence; random draw of SUPPORTED relations
"""
import argparse
import csv
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / 'mapping' / 'data'
SEED = 20261010
DRAW = {'S3_set_A': 12, 'S3_set_B': 12, 'S4_per_cell': 4, 'S5_supported': 8}


def read(path):
    with Path(path).open(encoding='utf-8-sig', newline='') as fh:
        return list(csv.DictReader(fh))


def draw(resources, relations, seed=SEED, sizes=DRAW):
    rng = random.Random(seed)
    taken, out = set(), []

    def take(rows, stratum, n=None, key=lambda r: r['resource_id']):
        rows = sorted((r for r in rows if r['resource_id'] not in taken), key=key)
        picked = rows if n is None else rng.sample(rows, min(n, len(rows)))
        for r in sorted(picked, key=key):
            taken.add(r['resource_id'])
            out.append({'unit': 'RESOURCE', 'id': r['resource_id'], 'stratum': stratum, 'resource_level': r['resource_level'],
                        'first_round': r['first_round'], 'category': r['resource_category'], 'set': r['resource_set'],
                        'individuation': r['individuation_status'], 'eligibility': r['eligibility_preliminary'],
                        'agent_classification_hidden_from_reviewer': 'YES'})
    take([r for r in resources if r['resource_category'] == 'INDETERMINATE' or r['individuation_status'] != 'INDIVIDUATED'], 'S1_ambiguous')
    take([r for r in resources if r['eligibility_preliminary'] == 'UNCERTAIN'], 'S2_scope')
    take([r for r in resources if r['resource_set'] == 'AB'], 'S3_boundary_AB')
    indiv = [r for r in resources if r['individuation_status'] == 'INDIVIDUATED']
    take([r for r in indiv if r['resource_set'] == 'A'], 'S3_boundary_A', sizes['S3_set_A'])
    take([r for r in indiv if r['resource_set'] == 'B'], 'S3_boundary_B', sizes['S3_set_B'])
    cells = sorted({(r['resource_level'], r['first_round']) for r in indiv})
    for level, rnd in cells:
        take([r for r in indiv if r['resource_level'] == level and r['first_round'] == rnd], f'S4_{level}_{rnd}', sizes['S4_per_cell'])
    for r in sorted((r for r in relations if r['relation_status'] == 'CANDIDATE' and r['confidence'] == 'MEDIUM'), key=lambda r: r['relation_id']):
        out.append({'unit': 'RELATION', 'id': r['relation_id'], 'stratum': 'S5_relation_candidate_medium', 'resource_level': '', 'first_round': '',
                    'category': r['relation_type'], 'set': '', 'individuation': '', 'eligibility': '', 'agent_classification_hidden_from_reviewer': 'YES'})
    supported = sorted((r for r in relations if r['relation_status'] == 'SUPPORTED'), key=lambda r: r['relation_id'])
    for r in sorted(rng.sample(supported, min(sizes['S5_supported'], len(supported))), key=lambda r: r['relation_id']):
        out.append({'unit': 'RELATION', 'id': r['relation_id'], 'stratum': 'S5_relation_supported_draw', 'resource_level': '', 'first_round': '',
                    'category': r['relation_type'], 'set': '', 'individuation': '', 'eligibility': '', 'agent_classification_hidden_from_reviewer': 'YES'})
    return out


COLS = ['unit', 'id', 'stratum', 'resource_level', 'first_round', 'category', 'set', 'individuation', 'eligibility',
        'agent_classification_hidden_from_reviewer']


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--out', default=str(ROOT / 'mapping' / 'reports' / 'evidence' / 'VALIDATION_SAMPLE_PROPOSED.csv'))
    args = ap.parse_args()
    rows = draw(read(DATA / 'resources.csv'), read(DATA / 'resource_relations.csv'))
    with Path(args.out).open('w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=COLS, lineterminator='\n')
        w.writeheader()
        w.writerows(rows)
    by = {}
    for r in rows:
        by[(r['unit'], r['stratum'].split('_')[0])] = by.get((r['unit'], r['stratum'].split('_')[0]), 0) + 1
    print(len(rows), 'units;', dict(sorted(by.items())))


if __name__ == '__main__':
    main()
