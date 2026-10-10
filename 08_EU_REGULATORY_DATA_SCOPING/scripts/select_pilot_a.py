#!/usr/bin/env python3
"""Deterministic, seeded, constrained selection of the Pilot A calibration sample.

Produces a CANDIDATE list for human approval. It classifies nothing and decides
no eligibility. Standard library only.

Inputs read from inputs/seed_inventory_v0_1.csv -- ONLY these columns:
    source_seed_id, layer, name, resource_type, source_url
The columns rgam_potential, initial_priority, limitations, possible_legal_id,
observation_unit and announced_access are dropped at load time and cannot
influence the result (see tests/test_pilot_a_selection.py).

Procedure (fully specified so it can be re-implemented):
  1. Records are sorted by source_seed_id.
  2. FORCED = every record that shares an identical source_url with another one.
  3. Attempt k: start from FORCED; for each family (layer, in sorted order) not
     yet represented, draw one of its records; then draw records from the rest
     until the sample has SIZE records. Every draw is
     pool[int(rng.random() * len(pool))] on the sorted pool, rng = random.Random(seed).
  4. The first attempt that satisfies every constraint C1-C8 is the result.
  5. If no attempt within MAX_ATTEMPTS satisfies them, the script stops with exit
     code 3 and reports how often each constraint failed. It does not relax anything.

Required groups (G1-READY): a JSON file may list groups of records that must enter
the sample together. They are an explicit, human-authored constraint, recorded in
the log with their stated reason, and are added to FORCED in step 2. Before any
draw, `feasibility()` checks necessary conditions for C1-C8 given the forced
records; if one cannot be met, no sampling is attempted.

Default seed: the first 8 hex digits of the SHA-256 of the seed inventory file,
read as an integer. It is derived from the data, not chosen by the operator.
"""
import argparse
import csv
import hashlib
import json
import random
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SEEDS = ROOT / 'inputs' / 'seed_inventory_v0_1.csv'
OUT = ROOT / 'pilot_a' / 'selection'

ALLOWED_COLUMNS = ('source_seed_id', 'layer', 'name', 'resource_type', 'source_url')
# Generic hosting platforms: sharing one of these hosts says nothing about a relation.
GENERIC_HOSTS = {'github.com', 'zenodo.org', 'huggingface.co'}

PARAMS = {
    'SIZE': 20,                  # C1
    'MIN_PER_FAMILY': 1,         # C2: every family (layer) represented
    'FORCE_IDENTICAL_URL': True, # C3: groups with an identical source_url enter complete
    'MIN_HOST_CLUSTERS': 3,      # C4: host clusters with >= 2 selected members
    'MIN_COMPOSITE_TYPE': 3,     # C5: records whose resource_type holds two labels ("A/B")
    'MIN_DISTINCT_TYPES': 18,    # C6: distinct resource_type values in the sample
    'MAX_PER_FAMILY': 4,         # C7: no family dominates
    'MIN_HOLDOUT_FAMILIES': 9,   # C8: families still present among the unselected records
    'MAX_ATTEMPTS': 200000,
}


def load(path=SEEDS):
    with path.open('r', encoding='utf-8-sig', newline='') as handle:
        rows = [{c: r[c] for c in ALLOWED_COLUMNS} for r in csv.DictReader(handle)]
    return sorted(rows, key=lambda r: r['source_seed_id'])


def default_seed(path=SEEDS):
    return int(hashlib.sha256(path.read_bytes()).hexdigest()[:8], 16)


def host(url):
    return (urlsplit(url).hostname or '').lower()


def derive(rows):
    """Objective groupings computed from factual columns only."""
    by_url, by_host = defaultdict(list), defaultdict(list)
    for r in rows:
        by_url[r['source_url']].append(r['source_seed_id'])
        if host(r['source_url']) not in GENERIC_HOSTS:
            by_host[host(r['source_url'])].append(r['source_seed_id'])
    return {
        'identical_url_groups': {u: ids for u, ids in sorted(by_url.items()) if len(ids) > 1},
        'host_clusters': {h: ids for h, ids in sorted(by_host.items()) if len(ids) > 1},
        'composite_type': sorted(r['source_seed_id'] for r in rows if '/' in r['resource_type']),
        'families': sorted({r['layer'] for r in rows}),
    }


def check(sample_ids, rows, groups, params):
    """Return {constraint: bool} for a candidate sample."""
    by_id = {r['source_seed_id']: r for r in rows}
    chosen = [by_id[i] for i in sample_ids]
    rest = [r for r in rows if r['source_seed_id'] not in sample_ids]
    fam = Counter(r['layer'] for r in chosen)
    sel = set(sample_ids)
    return {
        'C1_size': len(sel) == params['SIZE'],
        'C2_all_families': all(fam[f] >= params['MIN_PER_FAMILY'] for f in groups['families']),
        'C3_identical_url_complete': all(set(ids) <= sel for ids in groups['identical_url_groups'].values()),
        'C4_host_clusters': sum(1 for ids in groups['host_clusters'].values() if len(sel & set(ids)) >= 2) >= params['MIN_HOST_CLUSTERS'],
        'C5_composite_type': len(sel & set(groups['composite_type'])) >= params['MIN_COMPOSITE_TYPE'],
        'C6_distinct_types': len({r['resource_type'] for r in chosen}) >= params['MIN_DISTINCT_TYPES'],
        'C7_max_per_family': max(fam.values()) <= params['MAX_PER_FAMILY'],
        'C8_holdout_families': len({r['layer'] for r in rest}) >= params['MIN_HOLDOUT_FAMILIES'],
    }


def draw(rng, pool):
    return pool[int(rng.random() * len(pool))]


FEASIBILITY_SALT = 0x5F5E100  # separate random stream: the feasibility search never touches the selection stream


def forced_ids(rows, groups, params, required_groups=None):
    """Records that enter every sample: identical-URL groups plus the explicit required groups."""
    known = {r['source_seed_id'] for r in rows}
    forced = {i for ids in groups['identical_url_groups'].values() for i in ids} if params['FORCE_IDENTICAL_URL'] else set()
    for group in required_groups or []:
        unknown = sorted(set(group) - known)
        if unknown:
            raise ValueError(f'required group cites identifiers that are not in the inventory: {unknown}')
        forced |= set(group)
    return sorted(forced)


def bounds(rows, groups, params, forced):
    """Necessary conditions for C1-C8 given the forced records. A failed bound proves infeasibility."""
    by_id = {r['source_seed_id']: r for r in rows}
    fset, size = set(forced), params['SIZE']
    free = size - len(fset)
    fam_size = Counter(r['layer'] for r in rows)
    fam_forced = Counter(by_id[i]['layer'] for i in fset)
    uncovered = [f for f in groups['families'] if fam_forced[f] < params['MIN_PER_FAMILY']]
    free_after_families = free - len(uncovered)
    # C4: clusters already holding two forced members, plus the cheapest ones to complete with free slots
    have, needs = 0, []
    for ids in groups['host_clusters'].values():
        inside = len(fset & set(ids))
        if inside >= 2:
            have += 1
        else:
            needs.append(2 - inside)
    slots, best_c4 = max(free, 0), have
    for need in sorted(needs):
        if need <= slots:
            slots -= need
            best_c4 += 1
    comp = set(groups['composite_type'])
    best_c5 = len(comp & fset) + min(max(free, 0), len(comp - fset))
    forced_types = {by_id[i]['resource_type'] for i in fset}
    other_types = {r['resource_type'] for r in rows if r['source_seed_id'] not in fset} - forced_types
    best_c6 = len(forced_types) + min(max(free, 0), len(other_types))
    # C8: a family can stay in the reserve only if one of its records can remain unselected
    best_c8 = sum(1 for f in groups['families'] if fam_size[f] - max(fam_forced[f], params['MIN_PER_FAMILY']) >= 1)
    worst_family = max(fam_forced.values()) if fam_forced else 0
    return {
        'C1_size': {'ok': len(fset) <= size, 'forced': len(fset), 'required': f'<= {size}'},
        'C2_all_families': {'ok': free_after_families >= 0, 'families_still_to_cover': len(uncovered), 'free_slots': free,
                            'required': 'free slots >= families still to cover'},
        'C3_identical_url_complete': {'ok': True, 'note': 'identical-URL groups are forced'},
        'C4_host_clusters': {'ok': best_c4 >= params['MIN_HOST_CLUSTERS'], 'best_possible': best_c4, 'required': params['MIN_HOST_CLUSTERS']},
        'C5_composite_type': {'ok': best_c5 >= params['MIN_COMPOSITE_TYPE'], 'best_possible': best_c5, 'required': params['MIN_COMPOSITE_TYPE']},
        'C6_distinct_types': {'ok': best_c6 >= params['MIN_DISTINCT_TYPES'], 'best_possible': best_c6, 'required': params['MIN_DISTINCT_TYPES'],
                              'distinct_types_among_forced': len(forced_types), 'forced': len(fset)},
        'C7_max_per_family': {'ok': worst_family <= params['MAX_PER_FAMILY'], 'largest_forced_family': worst_family,
                              'required': f"<= {params['MAX_PER_FAMILY']}", 'forced_per_family': dict(sorted(fam_forced.items()))},
        'C8_holdout_families': {'ok': best_c8 >= params['MIN_HOLDOUT_FAMILIES'], 'best_possible': best_c8, 'required': params['MIN_HOLDOUT_FAMILIES']},
    }


def feasibility(rows, required_groups=None, seed=0, params=PARAMS, trials=2000):
    """Assess the constraints BEFORE selecting.

    INFEASIBLE   a necessary condition fails (a proof; nothing is sampled)
    FEASIBLE     the bounds hold and a search on a separate random stream found
                 at least one sample meeting C1-C8 (a constructive witness)
    UNDETERMINED the bounds hold but no witness was found in `trials` attempts
    The witness itself is not returned: it must not become an alternative sample.
    """
    groups = derive(rows)
    forced = forced_ids(rows, groups, params, required_groups)
    b = bounds(rows, groups, params, forced)
    out = {'forced': forced, 'bounds': b, 'search': None}
    if not all(x['ok'] for x in b.values()):
        out['status'] = 'INFEASIBLE'
        out['violated'] = [k for k, x in b.items() if not x['ok']]
        return out
    rng = random.Random(seed ^ FEASIBILITY_SALT)
    accepted, failures = 0, Counter()
    for _ in range(trials):
        verdict = check(attempt(rng, rows, groups, params, forced), rows, groups, params)
        if all(verdict.values()):
            accepted += 1
        else:
            for name, ok in verdict.items():
                if not ok:
                    failures[name] += 1
    out['search'] = {'trials': trials, 'accepted': accepted, 'acceptance_rate': accepted / trials,
                     'failures_by_constraint': dict(sorted(failures.items())),
                     'stream': 'random.Random(seed XOR 0x5F5E100), independent of the selection stream'}
    out['status'] = 'FEASIBLE' if accepted else 'UNDETERMINED'
    return out


def attempt(rng, rows, groups, params, forced=None):
    if forced is None:
        forced = forced_ids(rows, groups, params)
    sample = list(forced)
    by_id = {r['source_seed_id']: r for r in rows}
    for family in groups['families']:
        if not any(by_id[i]['layer'] == family for i in sample):
            pool = [r['source_seed_id'] for r in rows if r['layer'] == family and r['source_seed_id'] not in sample]
            sample.append(draw(rng, pool))
    while len(sample) < params['SIZE']:
        pool = [r['source_seed_id'] for r in rows if r['source_seed_id'] not in sample]
        sample.append(draw(rng, pool))
    return sorted(sample)


def select(seed, rows=None, params=PARAMS, required_groups=None, precheck=True):
    rows = rows if rows is not None else load()
    groups = derive(rows)
    forced = forced_ids(rows, groups, params, required_groups)
    base = {'groups': groups, 'forced': forced, 'infeasible': []}
    if precheck:
        violated = [k for k, x in bounds(rows, groups, params, forced).items() if not x['ok']]
        if violated:  # proved infeasible: no draw is made and nothing is relaxed
            return {**base, 'sample': None, 'attempts': 0, 'failures': {}, 'verdict': None, 'infeasible': violated}
    rng = random.Random(seed)
    failures = Counter()
    for k in range(1, params['MAX_ATTEMPTS'] + 1):
        sample = attempt(rng, rows, groups, params, forced)
        verdict = check(sample, rows, groups, params)
        if all(verdict.values()):
            return {**base, 'sample': sample, 'attempts': k, 'failures': dict(failures), 'verdict': verdict}
        for name, ok in verdict.items():
            if not ok:
                failures[name] += 1
    return {**base, 'sample': None, 'attempts': params['MAX_ATTEMPTS'], 'failures': dict(failures), 'verdict': None}


def roles(seed_id, groups):
    """Which objective properties a record carries (description, not a classification)."""
    tags = []
    for ids in groups['identical_url_groups'].values():
        if seed_id in ids:
            tags.append('identical_url:' + '+'.join(ids))
    for h, ids in groups['host_clusters'].items():
        if seed_id in ids:
            tags.append('host:' + h)
    if seed_id in groups['composite_type']:
        tags.append('composite_type')
    return ';'.join(tags)


def write_outputs(result, seed, seed_source, rows, out=None, required_spec=None, label=None, feasibility_report=None):
    out = Path(out) if out else OUT
    out.mkdir(parents=True, exist_ok=True)
    groups, sel = result['groups'], set(result['sample'])
    for name, keep in (('PILOT_A_CANDIDATE_SAMPLE.csv', True), ('PILOT_A_CONFIRMATION_RESERVE.csv', False)):
        with (out / name).open('w', encoding='utf-8-sig', newline='') as handle:
            w = csv.writer(handle, lineterminator='\n')
            w.writerow(['source_seed_id', 'layer', 'name', 'resource_type', 'source_url', 'objective_properties'])
            for r in rows:
                if (r['source_seed_id'] in sel) == keep:
                    w.writerow([r[c] for c in ALLOWED_COLUMNS] + [roles(r['source_seed_id'], groups)])
    chosen = [r for r in rows if r['source_seed_id'] in sel]
    rest = [r for r in rows if r['source_seed_id'] not in sel]
    log = {
        'generated_at_utc': datetime.now(timezone.utc).isoformat(timespec='seconds'),
        'script': 'scripts/select_pilot_a.py',
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'input': 'inputs/seed_inventory_v0_1.csv',
        'input_sha256': hashlib.sha256(SEEDS.read_bytes()).hexdigest(),
        'columns_read': list(ALLOWED_COLUMNS),
        'columns_never_read': ['rgam_potential', 'initial_priority', 'limitations', 'possible_legal_id', 'observation_unit', 'announced_access'],
        'seed': seed, 'seed_source': seed_source,
        'parameters': PARAMS,
        'generic_hosts_excluded_from_clusters': sorted(GENERIC_HOSTS),
        'attempts_until_acceptance': result['attempts'],
        'constraint_failures_in_rejected_attempts': result['failures'],
        'constraints_satisfied': result['verdict'],
        'objective_groups': groups,
        'sample': result['sample'],
        'reserve': [r['source_seed_id'] for r in rest],
        'summary': {
            'families_in_sample': dict(sorted(Counter(r['layer'] for r in chosen).items())),
            'families_in_reserve': dict(sorted(Counter(r['layer'] for r in rest).items())),
            'distinct_resource_types_in_sample': len({r['resource_type'] for r in chosen}),
            'composite_type_in_sample': sorted(sel & set(groups['composite_type'])),
            'host_clusters_with_two_or_more_in_sample': {h: sorted(sel & set(ids)) for h, ids in groups['host_clusters'].items() if len(sel & set(ids)) >= 2},
        },
        'status': (f'PROPOSED ({label}) - requires human approval; nothing was classified or screened' if label
                   else 'CANDIDATE - requires human approval; nothing was classified or screened'),
        'required_groups': required_spec,
        'forced_records': result.get('forced'),
        'feasibility_before_selection': feasibility_report,
    }
    (out / 'PILOT_A_SELECTION_LOG.json').write_text(json.dumps(log, indent=2, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
    return log


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--seed', type=int, help='integer seed; default is derived from the SHA-256 of the seed inventory')
    ap.add_argument('--no-write', action='store_true', help='print the result without writing files')
    ap.add_argument('--required-groups', help='JSON file: {"status": ..., "groups": [{"ids": [...], "reason": ...}]}')
    ap.add_argument('--out', help='output folder (default: pilot_a/selection)')
    ap.add_argument('--label', help='label written to the log status, e.g. "G1-READY option B"')
    ap.add_argument('--feasibility-only', action='store_true', help='report feasibility and stop before any selection')
    args = ap.parse_args()
    rows = load()
    seed, source = (args.seed, 'given on the command line') if args.seed is not None else (default_seed(), 'first 8 hex digits of sha256(inputs/seed_inventory_v0_1.csv)')
    spec = json.loads(Path(args.required_groups).read_text(encoding='utf-8')) if args.required_groups else None
    required = [g['ids'] for g in spec['groups']] if spec else None
    report = feasibility(rows, required, seed=seed)
    print('feasibility:', report['status'], '| forced:', ' '.join(report['forced']))
    for name, b in report['bounds'].items():
        if not b['ok']:
            print('  violated', name, json.dumps(b, ensure_ascii=False))
    if report['search']:
        print('  search:', json.dumps(report['search'], ensure_ascii=False))
    if report['status'] == 'INFEASIBLE':
        print('Nothing was sampled, relaxed or written. Review the required groups or the constraints with the team.')
        return 3
    if args.feasibility_only:
        return 0
    result = select(seed, rows, required_groups=required)
    if result['sample'] is None:
        print(f'NO SAMPLE satisfies all constraints within {PARAMS["MAX_ATTEMPTS"]} attempts (seed {seed}).')
        print('Constraint failure counts:', json.dumps(result['failures'], indent=2))
        print('Nothing was relaxed and nothing was written. Review the constraints with the team.')
        return 3
    print(f'seed={seed} ({source}); accepted at attempt {result["attempts"]}')
    print('sample:', ' '.join(result['sample']))
    print('rejected-attempt failures:', result['failures'])
    if not args.no_write:
        log = write_outputs(result, seed, source, rows, out=args.out, required_spec=spec, label=args.label, feasibility_report=report)
        print('written to', args.out or OUT.relative_to(ROOT))
        print(json.dumps(log['summary'], indent=2, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
