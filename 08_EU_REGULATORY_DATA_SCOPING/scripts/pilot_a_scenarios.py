#!/usr/bin/env python3
"""G1-READY: required-group scenarios for the Pilot A sample (option B of G1-PREP).

Step 1 (`feasibility`) assesses every scenario BEFORE any selection.
Step 2 (`select`) runs the registered seed once per feasible scenario and writes
each result to its own folder, marked PROPOSED. Nothing here approves a sample.

The designation rule for the scenario put forward as the revised candidate is
fixed in DESIGNATION_RULE below, before any sample is drawn.
"""
import argparse
import json
from pathlib import Path

import select_pilot_a as sel

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'pilot_a' / 'selection_v2_PROPOSED'

G = {
    'EP': {'ids': ['EU08', 'EU09'], 'reason': 'Interface and collection of the same institution on different hosts; the host proxy of G1-PREP could not pair them.',
           'tests': 'R2 versus R10; distribution_of versus overlaps_with'},
    'TED': {'ids': ['EU33', 'EU34'], 'reason': 'Data service and search API of the same publisher on different hosts; left incomplete by G1-PREP.',
            'tests': 'R2 versus R10; distribution_of'},
    'DISC': {'ids': ['EU11'], 'reason': 'Only record whose inventory name marks it as an old dataset; no discontinued resource was in the G1-PREP sample.',
             'tests': 'protocol criterion I5; relation successor_of; evidence for a discontinued resource'},
    'ACAD_DERIV': {'ids': ['EU35', 'EU39'], 'reason': 'Research corpus and benchmark task built on EU legislation; candidate derivation chain between two third-party resources (relation not verified).',
                   'tests': 'R6; derived_from between derived corpora'},
    'ACAD_ACQUIS': {'ids': ['EU37', 'EU38'], 'reason': 'Two parallel corpora on the same host with the same name stem.',
                    'tests': 'overlaps_with versus part_of; same-maintainer rule'},
    'ACAD_EURLEX': {'ids': ['EU35', 'EU36'], 'reason': 'Two research corpora sharing the EURLEX name stem.',
                    'tests': 'overlaps_with versus successor_of'},
}
SCENARIOS = {
    'S0_G1PREP': [],
    'S1_pairs': ['EP', 'TED'],
    'S2_pairs_disc': ['EP', 'TED', 'DISC'],
    'S3a_deriv': ['EP', 'TED', 'DISC', 'ACAD_DERIV'],
    'S3b_acquis': ['EP', 'TED', 'DISC', 'ACAD_ACQUIS'],
    'S3c_eurlex': ['EP', 'TED', 'DISC', 'ACAD_EURLEX'],
    'S4_two_academic_pairs': ['EP', 'TED', 'DISC', 'ACAD_DERIV', 'ACAD_ACQUIS'],
    'S5_academic_triad': ['EP', 'TED', 'DISC', 'ACAD_DERIV', 'ACAD_EURLEX'],
}
DESIGNATED = 'S3a_deriv'
DESIGNATION_RULE = (
    'Fixed before any sample was drawn: the revised candidate is the scenario with the smallest set of '
    'required groups that covers every item listed for evaluation in the G1-READY task (EU08+EU09, '
    'EU33+EU34, EU11, one related pair of academic corpora), the academic pair being the one that '
    'exercises derived_from (rule R6), the relation most relevant to the purpose of the study. '
    'The other scenarios are reported for comparison and remain available to the team.')


def spec(name):
    return {'status': 'PROPOSED - not approved; explicit human-reviewable constraint', 'scenario': name,
            'designation_rule': DESIGNATION_RULE if name == DESIGNATED else None,
            'groups': [G[k] for k in SCENARIOS[name]]}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('step', choices=['feasibility', 'select'])
    args = ap.parse_args()
    rows, seed = sel.load(), sel.default_seed()
    OUT.mkdir(parents=True, exist_ok=True)
    if args.step == 'feasibility':
        report = {'seed': seed, 'designated': DESIGNATED, 'designation_rule': DESIGNATION_RULE, 'scenarios': {}}
        for name in SCENARIOS:
            s = spec(name)
            f = sel.feasibility(rows, [g['ids'] for g in s['groups']], seed=seed)
            report['scenarios'][name] = {'required_groups': [g['ids'] for g in s['groups']], **f}
            tight = {k: v for k, v in f['bounds'].items() if 'best_possible' in v and v['best_possible'] == v['required']}
            rate = f['search']['acceptance_rate'] if f['search'] else None
            print(f'{name}: {f["status"]}; forced={len(f["forced"])}; acceptance={rate}; '
                  f'violated={f.get("violated", [])}; bounds_at_limit={sorted(tight)}')
        (OUT / 'FEASIBILITY_BEFORE_SELECTION.json').write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
        return 0
    feas = json.loads((OUT / 'FEASIBILITY_BEFORE_SELECTION.json').read_text(encoding='utf-8'))
    for name in SCENARIOS:
        f = feas['scenarios'][name]
        if f['status'] != 'FEASIBLE':
            print(f'{name}: skipped ({f["status"]})')
            continue
        s = spec(name)
        folder = OUT / name
        folder.mkdir(parents=True, exist_ok=True)
        (folder / 'REQUIRED_GROUPS.json').write_text(json.dumps(s, indent=2, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
        result = sel.select(seed, rows, required_groups=[g['ids'] for g in s['groups']])
        label = f'G1-READY option B, scenario {name}' + (' - DESIGNATED revised candidate' if name == DESIGNATED else ' - comparison scenario')
        sel.write_outputs(result, seed, 'first 8 hex digits of sha256(inputs/seed_inventory_v0_1.csv)', rows,
                          out=folder, required_spec=s, label=label, feasibility_report={k: f[k] for k in ('status', 'bounds', 'search')})
        print(f'{name}: attempt {result["attempts"]}: {" ".join(result["sample"])}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
