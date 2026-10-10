"""Consolidate all 143 R4.2E-B1 advanced validation cases across the four batches.

Batch-specific source files are read only. Nothing is overwritten.
B1-01..B1-03 = GPT-5.6 Terra High. B1-04 = Claude Opus 5 (Claude Code).
"""
import csv, hashlib, os
from collections import Counter, defaultdict

R4 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BATCH = os.path.join(R4, '03_extraction', 'qa', 'repair', 'R4_2E_B1')
B0 = os.path.join(R4, '03_extraction', 'qa', 'repair', 'R4_2E_B0')

SOURCES = [
    ('B1-01', 'GPT-5.6 Terra High', 'R4_2E_B1_ADVANCED_VALIDATION.csv'),
    ('B1-02', 'GPT-5.6 Terra High', 'R4_2E_B1_ADVANCED_VALIDATION_B1_02.csv'),
    ('B1-03', 'GPT-5.6 Terra High', 'R4_2E_B1_ADVANCED_VALIDATION_B1_03.csv'),
    ('B1-04', 'Claude Opus 5', 'R4_2E_B1_ADVANCED_VALIDATION_B1_04.csv'),
]

CONTROL_FILES = [
    'R4_2E_B1_NO_REPAIR_CONTROL_RESULTS.csv',
    'R4_2E_B1_NO_REPAIR_CONTROL_RESULTS_B1_02.csv',
    'R4_2E_B1_NO_REPAIR_CONTROL_RESULTS_B1_03.csv',
    'R4_2E_B1_NO_REPAIR_CONTROL_RESULTS_B1_04.csv',
]

SUMMARY = os.path.join(BATCH, 'R4_2E_B1_FINAL_SUMMARY.csv')
CONTROLS_OUT = os.path.join(BATCH, 'R4_2E_B1_CONTROL_DIAGNOSTIC_CONSOLIDATED.csv')


def load_all():
    out = []
    for batch, model, fname in SOURCES:
        with open(os.path.join(BATCH, fname), encoding='utf-8-sig') as fh:
            for r in csv.DictReader(fh):
                r['_BATCH'] = batch
                r['_MODEL'] = model
                out.append(r)
    return out


def main():
    rows = load_all()
    assert len(rows) == 143, f'expected 143 consolidated cases, got {len(rows)}'
    ids = [r['RECORD_ID'] for r in rows]
    assert len(set(ids)) == 143, 'duplicate RECORD_ID across batches'

    controls = set(r['RECORD_ID'] for r in
                   csv.DictReader(open(os.path.join(BATCH, 'R4_2E_B1_NO_REPAIR_CONTROL_SAMPLE.csv'),
                                       encoding='utf-8-sig')))
    sig = {r['RECORD_ID']: r for r in
           csv.DictReader(open(os.path.join(B0, 'R4_2E_B0_REPAIR_SIGNATURE_REGISTER.csv'),
                               encoding='utf-8-sig'))}
    fam = {r['REPAIR_FAMILY_ID']: r for r in
           csv.DictReader(open(os.path.join(B0, 'R4_2E_B0_REPAIR_FAMILY_REGISTER.csv'),
                               encoding='utf-8-sig'))}

    def kind(rid):
        if rid in controls:
            return 'HIDDEN_NO_REPAIR_CONTROL'
        route = sig.get(rid, {}).get('PROPOSED_REPAIR_ROUTE', '')
        return 'INDIVIDUAL_ADVANCED_CASE' if route == 'ADVANCED_MODEL_CASE_REVIEW' else 'FAMILY_REPRESENTATIVE'

    for r in rows:
        r['_KIND'] = kind(r['RECORD_ID'])

    print('=== composition ===')
    print(' ', dict(Counter(r['_KIND'] for r in rows)))
    print(' ', dict(Counter(r['_BATCH'] for r in rows)))

    def tally(field, subset=None):
        sub = subset if subset is not None else rows
        return Counter(r[field] for r in sub)

    blocks = []

    def add(metric, value, note=''):
        blocks.append({'METRIC': metric, 'VALUE': str(value), 'NOTE': note})

    add('B1_CASES_TOTAL', len(rows), 'four frozen batches reconciled')
    for b, m, _ in SOURCES:
        add(f'B1_CASES_{b.replace("-", "_")}', sum(1 for r in rows if r['_BATCH'] == b), m)
    for k, v in sorted(Counter(r['_KIND'] for r in rows).items()):
        add(f'COMPOSITION_{k}', v, '')

    print('\n=== defect decisions (143) ===')
    for k, v in tally('ADVANCED_DEFECT_PRESENT').most_common():
        print(f'  {k:12} {v}')
        add(f'DEFECT_{k}', v, 'advanced review adjudication')

    print('\n=== proposition anchor confidence ===')
    for k, v in tally('PROPOSITION_ANCHOR_CONFIDENCE').most_common():
        print(f'  {k:12} {v}')
        add(f'ANCHOR_CONFIDENCE_{k}', v, '')

    print('\n=== field correction counts (value = NO) ===')
    for f in ['ACTOR', 'ACTION', 'OBJECT', 'COUNTERPART', 'RECIPIENT']:
        c = tally(f + '_CORRECT')
        print(f'  {f:12} NO={c.get("NO", 0):3}  YES={c.get("YES", 0):3}  '
              f'N/A={c.get("N/A", 0):3}  UNCERTAIN={c.get("UNCERTAIN", 0):3}')
        add(f'FIELD_CORRECTION_{f}', c.get('NO', 0), 'count of *_CORRECT = NO')

    print('\n=== relational field differentiation ===')
    for k, v in tally('RELATIONAL_FIELD_DIFFERENTIATION').most_common():
        print(f'  {k:28} {v}')
        add(f'RELATIONAL_{k}', v, '')

    reps = [r for r in rows if r['_KIND'] == 'FAMILY_REPRESENTATIVE']
    print(f'\n=== family template status (family representatives only, n={len(reps)}) ===')
    for k, v in tally('FAMILY_TEMPLATE_STATUS', reps).most_common():
        print(f'  {k:32} {v}')
        add(f'TEMPLATE_STATUS_{k}', v, 'family representatives only')

    print('\n=== template generalizability (family representatives) ===')
    for k, v in tally('TEMPLATE_GENERALIZABILITY', reps).most_common():
        print(f'  {k:16} {v}')
        add(f'TEMPLATE_GENERALIZABILITY_{k}', v, 'family representatives only')

    inds = [r for r in rows if r['_KIND'] == 'INDIVIDUAL_ADVANCED_CASE']
    print(f'\n=== individual case routes (n={len(inds)}) ===')
    for k, v in tally('CASE_ROUTE_AFTER_REVIEW', inds).most_common():
        print(f'  {k:46} {v}')
        add(f'INDIVIDUAL_ROUTE_{k}', v, 'individual advanced cases only')

    # Potential template repair coverage: distinct families whose representatives are all
    # VALIDATED or VALIDATED_WITH_CONDITIONS, counted over B0 family sizes.
    by_family = defaultdict(list)
    for r in reps:
        f = sig.get(r['RECORD_ID'], {}).get('REPAIR_FAMILY_ID', '')
        if f:
            by_family[f].append(r['FAMILY_TEMPLATE_STATUS'])
    ok = {'VALIDATED', 'VALIDATED_WITH_CONDITIONS'}
    elig = [f for f, sts in by_family.items() if all(s in ok for s in sts)]
    mixed = [f for f, sts in by_family.items()
             if any(s in ok for s in sts) and not all(s in ok for s in sts)]
    cov = sum(int(fam[f]['NUMBER_OF_RECORDS']) for f in elig if f in fam)
    mixed_cov = sum(int(fam[f]['NUMBER_OF_RECORDS']) for f in mixed if f in fam)
    print(f'\n=== potential template repair coverage ===')
    print(f'  families with a representative reviewed : {len(by_family)}')
    print(f'  families fully validated                : {len(elig)}')
    print(f'  families with mixed representative status: {len(mixed)}')
    print(f'  POTENTIAL_TEMPLATE_REPAIR_COVERAGE       : {cov} corpus records')
    print(f'  records in mixed-status families         : {mixed_cov}')
    add('FAMILIES_WITH_REVIEWED_REPRESENTATIVE', len(by_family), '')
    add('FAMILIES_FULLY_VALIDATED', len(elig), 'all reviewed representatives VALIDATED*')
    add('FAMILIES_MIXED_REPRESENTATIVE_STATUS', len(mixed), 'representatives disagree')
    add('POTENTIAL_TEMPLATE_REPAIR_COVERAGE', cov,
        'corpus records that MIGHT later be eligible for controlled repair; no repair applied')
    add('RECORDS_IN_MIXED_STATUS_FAMILIES', mixed_cov, 'excluded from coverage')

    # Controls
    crows = []
    for cf in CONTROL_FILES:
        p = os.path.join(BATCH, cf)
        for r in csv.DictReader(open(p, encoding='utf-8-sig')):
            crows.append({
                'BATCH_ID': r.get('BATCH_ID', ''),
                'RECORD_ID': r.get('RECORD_ID', ''),
                'CONTROL_RESULT': r.get('CONTROL_RESULT', ''),
                'ADVANCED_DEFECT_PRESENT': r.get('ADVANCED_DEFECT_PRESENT', ''),
                'CONTROL_DEFECT_TYPE': r.get('CONTROL_DEFECT_TYPE', ''),
                'CONTROL_DEFECT_SEVERITY': r.get('CONTROL_DEFECT_SEVERITY', ''),
                'REVIEWING_MODEL': 'Claude Opus 5' if r.get('BATCH_ID') == 'B1-04' else 'GPT-5.6 Terra High',
                'NOTE': r.get('NOTE', ''),
            })
    assert len(crows) == 12, f'expected 12 controls, got {len(crows)}'
    # B1-01 and B1-02 predate the severity taxonomy introduced for B1-03 unblinding.
    for c in crows:
        if c['CONTROL_RESULT'] == 'DEFECT_FOUND' and not c['CONTROL_DEFECT_SEVERITY']:
            c['CONTROL_DEFECT_SEVERITY'] = ('LOCAL' if c['RECORD_ID'] == 'EXT-000085'
                                            else 'NOT_CLASSIFIED_AT_TIME_OF_UNBLINDING')
        if c['CONTROL_RESULT'] == 'DEFECT_FOUND' and not c['CONTROL_DEFECT_TYPE']:
            c['CONTROL_DEFECT_TYPE'] = 'NOT_CLASSIFIED_AT_TIME_OF_UNBLINDING'

    print('\n=== 12/12 control diagnostic ===')
    for k, v in Counter(c['CONTROL_RESULT'] for c in crows).most_common():
        print(f'  {k:20} {v}')
        add(f'CONTROL_{k}', v, 'hidden NO_REPAIR controls, diagnostic only')
    add('CONTROLS_COMPLETED', len(crows), 'of 12')
    sev = Counter(c['CONTROL_DEFECT_SEVERITY'] for c in crows if c['CONTROL_RESULT'] == 'DEFECT_FOUND')
    print('  severity:', dict(sev))
    for k, v in sev.items():
        add(f'CONTROL_SEVERITY_{k}', v, '')
    add('CONTROL_SEVERITY_SERIOUS', sev.get('SERIOUS', 0), 'proposition-level failures')
    for c in crows:
        if c['CONTROL_RESULT'] != 'CLEAN_CONFIRMED':
            print(f"    {c['RECORD_ID']}  {c['BATCH_ID']}  {c['CONTROL_DEFECT_TYPE']}  "
                  f"{c['CONTROL_DEFECT_SEVERITY']}")

    with open(CONTROLS_OUT, 'w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(crows[0].keys()), quoting=csv.QUOTE_ALL,
                           lineterminator='\r\n')
        w.writeheader()
        w.writerows(crows)

    with open(SUMMARY, 'w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=['METRIC', 'VALUE', 'NOTE'], quoting=csv.QUOTE_ALL,
                           lineterminator='\r\n')
        w.writeheader()
        w.writerows(blocks)

    for p in (SUMMARY, CONTROLS_OUT):
        d = hashlib.sha256(open(p, 'rb').read()).hexdigest().upper()
        print(f'\n{os.path.basename(p)} SHA256={d}')


if __name__ == '__main__':
    main()
