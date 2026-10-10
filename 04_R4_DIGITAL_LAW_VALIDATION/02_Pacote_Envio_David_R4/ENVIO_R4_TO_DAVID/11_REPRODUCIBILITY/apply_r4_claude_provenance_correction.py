"""Apply the final Claude provenance correction to the Claude-produced R4 artifacts.

The researcher selected 'Claude Opus 5.5 Extra High' in the VS Code Claude agent UI.
The execution environment reported 'Claude Opus 5' with identifier 'claude-opus-5'.
That relationship cannot be independently verified, so both are recorded and the
match is explicitly marked NOT_VERIFIABLE.

Only the provenance columns are rewritten. Every other cell, including RUN_TIMESTAMP,
is preserved byte-for-byte and the script asserts this before writing. Terra provenance
for B1-01, B1-02 and B1-03 is never touched.
"""
import csv, hashlib, os, shutil

R4 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BATCH = os.path.join(R4, '03_extraction', 'qa', 'repair', 'R4_2E_B1')

B1_04 = os.path.join(BATCH, 'R4_2E_B1_ADVANCED_VALIDATION_B1_04.csv')
B1_04_PRE = os.path.join(BATCH, 'R4_2E_B1_ADVANCED_VALIDATION_B1_04_v1_PROVENANCE_SUPERSEDED.csv')
B1S = os.path.join(BATCH, 'R4_2E_B1_ACTION_SENSITIVITY_AUDIT.csv')
B1S_PRE = os.path.join(BATCH, 'R4_2E_B1_ACTION_SENSITIVITY_AUDIT_v1_PROVENANCE_SUPERSEDED.csv')

RESEARCHER_SELECTED = 'Claude Opus 5.5 Extra High'
RUNTIME_VARIANT = ('RUNTIME_REPORTED_MODEL=Claude Opus 5; RUNTIME_MODEL_ID=claude-opus-5; '
                   'MODEL_SELECTION_RUNTIME_MATCH=NOT_VERIFIABLE')
AUDIT_PROVENANCE = ('EXECUTION_ENVIRONMENT=Claude Code / VS Code extension; '
                    'RESEARCHER_SELECTED_MODEL=Claude Opus 5.5 Extra High; '
                    'RUNTIME_REPORTED_MODEL=Claude Opus 5; RUNTIME_MODEL_ID=claude-opus-5; '
                    'MODEL_SELECTION_RUNTIME_MATCH=NOT_VERIFIABLE')


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest().upper()


def rewrite(path, pre_path, mutate, protected_check):
    """Preserve the pre-correction file, then rewrite only provenance columns."""
    before = sha(path)
    with open(path, encoding='utf-8-sig', newline='') as fh:
        rdr = csv.DictReader(fh)
        cols = rdr.fieldnames
        rows = list(rdr)
    original = [dict(r) for r in rows]

    if not os.path.exists(pre_path):
        shutil.copy2(path, pre_path)

    for r in rows:
        mutate(r)

    # every non-provenance cell must be unchanged
    for o, n in zip(original, rows):
        for c in cols:
            if c in protected_check:
                continue
            if o[c] != n[c]:
                raise SystemExit(f'non-provenance cell changed: {n.get("RECORD_ID")}.{c}')
    if len(rows) != len(original):
        raise SystemExit('row count changed')

    with open(path, 'w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=cols, quoting=csv.QUOTE_ALL, lineterminator='\r\n')
        w.writeheader()
        w.writerows(rows)
    return before, sha(path), len(rows)


def main():
    def m_b104(r):
        r['MODEL_REQUESTED'] = RESEARCHER_SELECTED
        r['MODEL_RESEARCHER_SELECTED'] = RESEARCHER_SELECTED
        r['MODEL_RUNTIME_VARIANT'] = RUNTIME_VARIANT

    b, a, n = rewrite(B1_04, B1_04_PRE, m_b104,
                      {'MODEL_REQUESTED', 'MODEL_RESEARCHER_SELECTED', 'MODEL_RUNTIME_VARIANT'})
    print(f'B1-04  rows={n}')
    print(f'  pre-correction  SHA256={b}')
    print(f'  corrected       SHA256={a}')

    def m_b1s(r):
        r['AUDIT_MODEL_PROVENANCE'] = AUDIT_PROVENANCE

    b2, a2, n2 = rewrite(B1S, B1S_PRE, m_b1s, {'AUDIT_MODEL_PROVENANCE'})
    print(f'B1S    rows={n2}')
    print(f'  pre-correction  SHA256={b2}')
    print(f'  corrected       SHA256={a2}')

    # confirm Terra rows in B1-04 sibling files were not touched
    for f in ['R4_2E_B1_ADVANCED_VALIDATION.csv', 'R4_2E_B1_ADVANCED_VALIDATION_B1_02.csv',
              'R4_2E_B1_ADVANCED_VALIDATION_B1_03.csv']:
        p = os.path.join(BATCH, f)
        vals = set()
        for r in csv.DictReader(open(p, encoding='utf-8-sig')):
            vals.add((r['MODEL_REQUESTED'], r['MODEL_RESEARCHER_SELECTED'],
                      r['MODEL_RUNTIME_VARIANT']))
        print(f'{f}: {sorted(vals)}  SHA256={sha(p)}')

    # B1-04 substantive decisions must be identical to the preserved pre-correction file
    pre = {r['RECORD_ID']: r for r in csv.DictReader(open(B1_04_PRE, encoding='utf-8-sig'))}
    now = {r['RECORD_ID']: r for r in csv.DictReader(open(B1_04, encoding='utf-8-sig'))}
    prov = {'MODEL_REQUESTED', 'MODEL_RESEARCHER_SELECTED', 'MODEL_RUNTIME_VARIANT'}
    diffs = [(k, c) for k in pre for c in pre[k] if c not in prov and pre[k][c] != now[k][c]]
    print(f'\nB1-04 non-provenance differences vs preserved v1: {len(diffs)}')


if __name__ == '__main__':
    main()
