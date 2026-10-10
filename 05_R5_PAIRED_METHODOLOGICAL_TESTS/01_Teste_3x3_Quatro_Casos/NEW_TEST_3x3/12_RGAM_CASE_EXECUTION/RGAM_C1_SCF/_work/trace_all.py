# MECHANICAL: verify vertical traceability of every higher-order record (A -> S -> R/NA/PD -> ST -> unit -> verbatim span)
import csv, io, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import reg
OUT = os.path.dirname(reg.W)


def rows(n):
    return list(csv.DictReader(io.StringIO(open(os.path.join(OUT, n + '.csv'), 'rb').read().decode('utf-8-sig'), newline='')))


def split(s):
    return [x for x in s.split(';') if x]


def ns(x):
    return re.sub(r'\s+', ' ', x).strip()


ST = {r['st_id']: r for r in rows('INSTITUTIONAL_STATEMENTS')}
NA = {r['na_id']: r for r in rows('NORMATIVE_ASSIGNMENTS')}
QR = {r['qr_id']: r for r in rows('QUALIFIED_RELATIONS')}
PD = {r['pd_id']: r for r in rows('POSITIONS_AND_DEVICES')}
SC = {r['sc_id']: r for r in rows('SUBCONFIGURATIONS')}
AR = {r['arch_id']: r for r in rows('ARCHITECTURE_CANDIDATES')}
PR = {r['prop_id']: r for r in rows('PROPERTY_REGISTER')}
UT = {reg.full(k): v for k, v in reg.UT.items()}
fails = []
checked = {'ARCH': 0, 'SC': 0, 'PROP': 0, 'QR': 0, 'NA': 0, 'PD': 0, 'ST': 0}


def trace_leaf(rec_id, row):
    """leaf record -> statements -> units -> span"""
    sts = split(row.get('statement_ids', ''))
    if not sts:  # PD has no statement_ids column: use statements whose derived_record_ids list the PD
        sts = [s for s, r in ST.items() if rec_id in split(r['derived_record_ids'])]
    if not sts:
        fails.append(f'{rec_id}: no statement')
        return
    for s in sts:
        if s not in ST:
            fails.append(f'{rec_id}: unknown statement {s}')
            continue
        us = split(ST[s]['supporting_unit_ids'])
        if not us or any(u not in UT for u in us):
            fails.append(f'{rec_id}: statement {s} units unresolved')
        sp = ST[s]['evidence_span']
        if not sp or not all(any(ns(p) in ns(UT[u]) for u in us) for p in sp.split(' || ')):
            fails.append(f'{rec_id}: statement {s} span not verbatim in its units')
    sp = row['evidence_span']
    us = split(row['supporting_unit_ids'])
    if not all(any(ns(p) in ns(UT[u]) for u in us) for p in sp.split(' || ')):
        fails.append(f'{rec_id}: record span not verbatim in its units')
    checked[rec_id.split('-')[0]] += 1


def leaf(i):
    if i.startswith('QR-'):
        return QR[i]
    if i.startswith('NA-'):
        return NA[i]
    if i.startswith('PD-'):
        return PD[i]
    raise KeyError(i)


for s in SC.values():
    for i in split(s['member_qr_ids']) + split(s['member_na_ids']) + split(s['member_pd_ids']):
        trace_leaf(i, leaf(i))
    checked['SC'] += 1
for a in AR.values():
    for sid in split(a['member_sc_ids']):
        if sid not in SC:
            fails.append(f"{a['arch_id']}: member {sid} missing")
    for q in split(a['i2_qr_ids']):
        trace_leaf(q, QR[q])
    checked['ARCH'] += 1


def prop_leaves(p, seen=()):
    out = []
    for i in split(p['supporting_record_ids']):
        if i.startswith('PROP-'):
            out += prop_leaves(PR[i], seen + (p['prop_id'],))
        else:
            out.append(i)
    return out


for p in PR.values():
    for i in prop_leaves(p):
        trace_leaf(i, leaf(i))
    b = p['bearer_id']
    if not (b in SC or b in AR or b in QR or b in PD):
        fails.append(f"{p['prop_id']}: bearer {b} unresolved")
    checked['PROP'] += 1
print('TRACE_ALL fails:', len(fails), checked)
for f in fails[:30]:
    print(' -', f)
