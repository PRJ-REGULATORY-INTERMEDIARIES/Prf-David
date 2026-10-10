# MECHANICAL integrity checks of the emitted tables (data dictionary section 4, rules 1-10, plus structural checks).
import csv, os, re, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import reg
OUT = os.path.dirname(reg.W)
TPL = 'G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_C1_SCF/OUTPUT_TEMPLATES'
TABLES = ['W_DECLARATION', 'SOURCE_UNIT_INVENTORY', 'UNIT_SCREENING', 'INSTITUTIONAL_STATEMENTS', 'NORMATIVE_ASSIGNMENTS',
          'POSITIONS_AND_DEVICES', 'QUALIFIED_RELATIONS', 'EXTERNAL_REFERENCES', 'SUBCONFIGURATIONS', 'ARCHITECTURE_CANDIDATES',
          'PROPERTY_REGISTER', 'CLOSURE_REGISTER', 'PROVENANCE_LINKS', 'UNCERTAINTY_LOG', 'HUMAN_REVIEW_QUEUE', 'TRACE_DEMONSTRATIONS',
          'INSTRUMENT_LEVEL_SUMMARY', 'PROTOCOL_DEVIATION_LOG', 'RUN_METADATA']
T = {}
fails = []
notes = []


def fail(msg):
    fails.append(msg)


for t in TABLES:
    raw = open(os.path.join(OUT, t + '.csv'), 'rb').read()
    assert raw[:3] == b'\xef\xbb\xbf', t
    rows = list(csv.reader(raw.decode('utf-8-sig').splitlines(keepends=False), strict=True)) if False else None
    import io
    rows = list(csv.reader(io.StringIO(raw.decode('utf-8-sig'), newline='')))
    hdr = rows[0]
    tplh = open(os.path.join(TPL, t + '.csv'), 'rb').read().decode('utf-8-sig').strip('\r\n').split(',')
    if hdr != tplh:
        fail(f'{t}: header differs from template')
    T[t] = [dict(zip(hdr, r)) for r in rows[1:]]

units = {r['unit_id']: r for r in T['SOURCE_UNIT_INVENTORY']}
UT = {full: reg.UT[full[len(reg.CASE) + 1:]] for full in units}


def split(s):
    return [x for x in s.split(';') if x] if s else []


# unique ids
idcol = {'INSTITUTIONAL_STATEMENTS': 'st_id', 'NORMATIVE_ASSIGNMENTS': 'na_id', 'POSITIONS_AND_DEVICES': 'pd_id', 'QUALIFIED_RELATIONS': 'qr_id',
         'EXTERNAL_REFERENCES': 'ext_id', 'SUBCONFIGURATIONS': 'sc_id', 'ARCHITECTURE_CANDIDATES': 'arch_id', 'PROPERTY_REGISTER': 'prop_id',
         'CLOSURE_REGISTER': 'closure_id', 'PROVENANCE_LINKS': 'link_id', 'UNCERTAINTY_LOG': 'unc_id', 'HUMAN_REVIEW_QUEUE': 'hq_id',
         'TRACE_DEMONSTRATIONS': 'trace_id', 'PROTOCOL_DEVIATION_LOG': 'dev_id', 'RUN_METADATA': 'run_id'}
fmt = {'st_id': r'ST-\d{4}', 'na_id': r'NA-\d{4}', 'pd_id': r'PD-\d{3}', 'qr_id': r'QR-\d{4}', 'ext_id': r'EXT-\d{3}', 'sc_id': r'SC-\d{2}',
       'arch_id': r'ARCH-\d{2}', 'prop_id': r'PROP-\d{3}', 'closure_id': r'CL-\d{2}', 'link_id': r'LNK-\d{5}', 'unc_id': r'UNC-\d{3}',
       'hq_id': r'HQ-\d{3}', 'trace_id': r'TR-\d{2}', 'dev_id': r'DEV-\d{2}', 'run_id': r'RUN-\d{2}'}
ALL = {}
for t, c in idcol.items():
    seen = set()
    for r in T[t]:
        v = r[c]
        if not re.fullmatch(fmt[c], v):
            fail(f'{t}: bad id format {v}')
        if v in seen:
            fail(f'{t}: duplicate id {v}')
        seen.add(v)
        ALL[v] = (t, r)

# rule 1
inv = set(units)
bad = 0
for r in T['SOURCE_UNIT_INVENTORY']:
    if r['parent_unit_id'] and r['parent_unit_id'] not in inv:
        fail(f"inventory parent missing {r['parent_unit_id']}")
for t, cols in {'UNIT_SCREENING': ['unit_id'], 'INSTITUTIONAL_STATEMENTS': ['supporting_unit_ids'], 'NORMATIVE_ASSIGNMENTS': ['supporting_unit_ids'],
                'POSITIONS_AND_DEVICES': ['supporting_unit_ids', 'instance_source_unit_ids'], 'QUALIFIED_RELATIONS': ['supporting_unit_ids'],
                'EXTERNAL_REFERENCES': ['supporting_unit_ids'], 'SUBCONFIGURATIONS': ['units_spanned'], 'ARCHITECTURE_CANDIDATES': ['i1_scope_units'],
                'PROVENANCE_LINKS': ['unit_id'], 'UNCERTAINTY_LOG': ['unit_ids']}.items():
    for r in T[t]:
        for c in cols:
            for u in split(r[c]):
                if u not in inv:
                    fail(f'rule1: {t}.{c} unknown unit {u}')
sc_units = [r['unit_id'] for r in T['UNIT_SCREENING']]
if len(sc_units) != len(set(sc_units)) or set(sc_units) != inv or len(sc_units) != len(inv):
    fail('rule1: screening does not cover the inventory exactly once')
s = T['INSTRUMENT_LEVEL_SUMMARY'][0]
if int(s['units_total']) != int(s['units_screened']) or int(s['units_total']) != len(inv):
    fail('rule1: units_total != units_screened')
RES1 = 'PASS' if not [f for f in fails if f.startswith('rule1')] else 'FAIL'

# rule 2
STS = {r['st_id']: r for r in T['INSTITUTIONAL_STATEMENTS']}
r2 = 0
for t, c in (('NORMATIVE_ASSIGNMENTS', 'statement_ids'), ('QUALIFIED_RELATIONS', 'statement_ids')):
    for r in T[t]:
        ss = split(r[c])
        if not ss:
            fail(f"rule2: {t} {r[idcol[t]]} cites no statement")
        for x in ss:
            if x not in STS:
                fail(f'rule2: {t} unknown statement {x}')
                continue
            if STS[x]['recital_only'] == 'Y':
                fail(f'rule2: recital-only statement used {x}')
# PD and EXT carry no statement_ids column: check through derived_record_ids of statements
derived = {}
for st_ in T['INSTITUTIONAL_STATEMENTS']:
    if not split(st_['supporting_unit_ids']):
        fail(f"rule2: statement {st_['st_id']} has no unit")
    for d in split(st_['derived_record_ids']):
        derived.setdefault(d, []).append(st_['st_id'])
for t, c in (('POSITIONS_AND_DEVICES', 'pd_id'), ('EXTERNAL_REFERENCES', 'ext_id'), ('NORMATIVE_ASSIGNMENTS', 'na_id'), ('QUALIFIED_RELATIONS', 'qr_id')):
    for r in T[t]:
        if r[c] not in derived:
            fail(f'rule2: {r[c]} not cited by any statement derived_record_ids')
for r in T['NORMATIVE_ASSIGNMENTS'] + T['QUALIFIED_RELATIONS']:
    rid_ = r.get('na_id') or r.get('qr_id')
    if set(split(r['statement_ids'])) != set(derived.get(rid_, [])):
        fail(f'rule2: statement/derived mismatch for {rid_}')
RES2 = 'PASS' if not [f for f in fails if f.startswith('rule2')] else 'FAIL'

# rule 3 (all id-valued fields resolve)
known = set(ALL)
idfields = {'NORMATIVE_ASSIGNMENTS': ['statement_ids', 'subject_pd_id', 'instrument_ref', 'depends_on_pd_ids', 'uncertainty_ids', 'hq_ids'],
            'POSITIONS_AND_DEVICES': ['uncertainty_ids', 'hq_ids'],
            'QUALIFIED_RELATIONS': ['statement_ids', 'origin_pd_id', 'counterpart_pd_id', 'additional_party_pd_ids', 'instrument_ref',
                                    'accountable_via_qr_ids', 'depends_on_pd_ids', 'external_ref_ids', 'uncertainty_ids', 'hq_ids'],
            'EXTERNAL_REFERENCES': ['dependent_record_ids'],
            'SUBCONFIGURATIONS': ['member_qr_ids', 'member_na_ids', 'member_pd_ids', 'overlap_sc_ids', 'nested_in_sc_id', 'uncertainty_ids', 'hq_ids'],
            'ARCHITECTURE_CANDIDATES': ['member_sc_ids', 'i2_qr_ids', 'i4_external_dependencies', 'uncertainty_ids', 'hq_ids'],
            'PROPERTY_REGISTER': ['bearer_id', 'supporting_record_ids', 'closure_ref', 'hq_ids'],
            'CLOSURE_REGISTER': ['unresolved_ext_ids', 'affected_claim_ids'],
            'UNCERTAINTY_LOG': ['record_ids'], 'HUMAN_REVIEW_QUEUE': ['record_refs'],
            'PROVENANCE_LINKS': ['record_id']}
for t, cols in idfields.items():
    for r in T[t]:
        for c in cols:
            for x in split(r[c]):
                if re.fullmatch(r'(ST|NA|PD|QR|EXT|SC|ARCH|PROP|CL|UNC|HQ|LNK)-\d+', x):
                    if x not in known:
                        fail(f'rule3: {t}.{c} unresolved id {x}')
                elif c not in ('instrument_ref',):
                    fail(f'rule3: {t}.{c} non-id value {x[:40]}')
QRS = {r['qr_id']: r for r in T['QUALIFIED_RELATIONS']}
for r in T['QUALIFIED_RELATIONS']:
    for x in split(r['accountable_via_qr_ids']):
        if x not in QRS or QRS[x]['relation_type'] != 'accountability':
            fail(f'rule3: accountable_via {x} is not an accountability QR')
RES3 = 'PASS' if not [f for f in fails if f.startswith('rule3')] else 'FAIL'

# rule 4
for r in T['QUALIFIED_RELATIONS']:
    if not r['origin_pd_id'] or not r['counterpart_pd_id']:
        fail(f"rule4: {r['qr_id']} missing party")
    if r['modality'] == 'prohibition':
        fail(f"rule4: {r['qr_id']} prohibition")
    if r['epistemic_status'] == 'material_establishment_evidenced':
        fail(f"rule4: {r['qr_id']} material establishment")
RES4 = 'PASS' if not [f for f in fails if f.startswith('rule4')] else 'FAIL'

# rule 5
links = {}
for r in T['PROVENANCE_LINKS']:
    links.setdefault(r['record_id'], []).append(r)
for t, c in (('NORMATIVE_ASSIGNMENTS', 'na_id'), ('QUALIFIED_RELATIONS', 'qr_id'), ('SUBCONFIGURATIONS', 'sc_id'), ('ARCHITECTURE_CANDIDATES', 'arch_id'),
             ('PROPERTY_REGISTER', 'prop_id')):
    for r in T[t]:
        if r[c] not in links:
            fail(f'rule5: {r[c]} has no provenance link')
for t, c in (('NORMATIVE_ASSIGNMENTS', 'na_id'), ('QUALIFIED_RELATIONS', 'qr_id')):
    for r in T[t]:
        if r['derivation'] == 'derived':
            if not r['derivation_rule']:
                fail(f'rule5: {r[c]} derived without rule')
            if len(split(r['supporting_unit_ids'])) < 2 and 'cross-reference' not in r['derivation_rule']:
                fail(f'rule5: {r[c]} derived with <2 units')
        elif r['derivation'] != 'direct':
            fail(f'rule5: {r[c]} bad derivation value')
# provenance links mirror supporting units of NA/QR/PD
for t, c in (('NORMATIVE_ASSIGNMENTS', 'na_id'), ('QUALIFIED_RELATIONS', 'qr_id'), ('POSITIONS_AND_DEVICES', 'pd_id'), ('EXTERNAL_REFERENCES', 'ext_id'),
             ('INSTITUTIONAL_STATEMENTS', 'st_id')):
    for r in T[t]:
        have = {l['unit_id'] for l in links.get(r[c], [])}
        sup = set(split(r['supporting_unit_ids']))
        if not sup <= have:
            fail(f'rule5: {r[c]} supporting units not mirrored in provenance: {sorted(sup - have)[:3]}')
RES5 = 'PASS' if not [f for f in fails if f.startswith('rule5')] else 'FAIL'

# rule 6
hqs = {r['hq_id']: r for r in T['HUMAN_REVIEW_QUEUE']}
for r in T['ARCHITECTURE_CANDIDATES']:
    if r['outcome'] in ('INTEGRATED', 'OVERLAPPING_OR_PARTIALLY_INTEGRATED'):
        ok = False
        for h in split(r['hq_ids']):
            tc = hqs[h]['trigger_code']
            if tc in ('HQ-INTEGRATION', 'HQ-OVERLAP') and r['arch_id'] in split(hqs[h]['record_refs']):
                ok = True
        if not ok:
            fail(f"rule6: {r['arch_id']} outcome without HQ item")
    if r['outcome'] == 'INTEGRATED' and not all(r[k] == 'SATISFIED' for k in ('i1_status', 'i2_status', 'i3_status', 'i4_status')):
        fail(f"rule6: {r['arch_id']} INTEGRATED without all SATISFIED")
RES6 = 'PASS' if not [f for f in fails if f.startswith('rule6')] else 'FAIL'

# rule 7
CL = {r['closure_id']: r for r in T['CLOSURE_REGISTER']}
for r in T['PROPERTY_REGISTER']:
    if r['closure_dependency'] == 'Y':
        if r['closure_ref'] not in CL:
            fail(f"rule7: {r['prop_id']} closure_ref unresolved")
        elif CL[r['closure_ref']]['result'] == 'UNDETERMINED' and r['status'] != 'undetermined':
            fail(f"rule7: {r['prop_id']} closure UNDETERMINED but status {r['status']}")
    elif r['closure_ref']:
        fail(f"rule7: {r['prop_id']} closure_ref without dependency")
RES7 = 'PASS' if not [f for f in fails if f.startswith('rule7')] else 'FAIL'

# rule 8
for r in T['EXTERNAL_REFERENCES']:
    if r['source_verification_status'] != 'not_checked' or r['boundary_status'] != 'outside_corpus_not_expanded':
        fail(f"rule8: {r['ext_id']}")
RES8 = 'PASS' if not [f for f in fails if f.startswith('rule8')] else 'FAIL'

# rule 9
for r in T['HUMAN_REVIEW_QUEUE']:
    if any(r[c] for c in ('human_decision', 'human_rationale', 'decided_by', 'decision_date')):
        fail(f"rule9: {r['hq_id']} human column filled")
RES9 = 'PASS' if not [f for f in fails if f.startswith('rule9')] else 'FAIL'

# rule 10: vertical chain resolution
def nspace(x):
    return re.sub(r'\s+', ' ', x).strip()


for r in T['TRACE_DEMONSTRATIONS']:
    chain = r['vertical_chain']
    items = chain.split(' ## ')[1:]
    if not items:
        fail(f"rule10: {r['trace_id']} empty chain")
    for it in items:
        m = re.match(r'^((?:NA|QR)-\d+) -> ([^>]+) -> ([^>]+) -> span: "(.*)"$', it, re.S)
        if not m:
            fail(f"rule10: {r['trace_id']} cannot parse item {it[:60]}")
            continue
        rec, stids, us, span = m.groups()
        if rec not in ALL:
            fail(f'rule10: unknown record {rec}')
            continue
        row = ALL[rec][1]
        for sid in stids.split(','):
            if sid not in STS or sid not in split(row['statement_ids']):
                fail(f'rule10: {rec} -> {sid} not linked')
        ulist = split(us.strip())
        if not ulist or any(u not in inv for u in ulist):
            fail(f'rule10: {rec} units unresolved')
        if not any(nspace(p) in nspace(UT[u]) for u in ulist for p in span.split(' || ')):
            fail(f'rule10: {rec} span not found in units')
        if span != row['evidence_span']:
            fail(f'rule10: {rec} chain span differs from record span')
RES10 = 'PASS' if not [f for f in fails if f.startswith('rule10')] else 'FAIL'

# additional checks: verbatim spans
for t, c in (('INSTITUTIONAL_STATEMENTS', 'st_id'), ('NORMATIVE_ASSIGNMENTS', 'na_id'), ('POSITIONS_AND_DEVICES', 'pd_id'), ('QUALIFIED_RELATIONS', 'qr_id')):
    for r in T[t]:
        sp = r['evidence_span']
        if len(sp) > 400:
            fail(f'span>400 {r[c]}')
        us = split(r['supporting_unit_ids'])
        for part in sp.split(' || '):
            if not any(nspace(part) in nspace(UT[u]) for u in us):
                fail(f'span not verbatim {r[c]}: {part[:60]}')
# ext units subset of statements units
for r in T['EXTERNAL_REFERENCES']:
    su = set()
    for s_ in [k for k, v in derived.items() if k == r['ext_id']]:
        pass
    sts = derived.get(r['ext_id'], [])
    sunits = set()
    for sid in sts:
        sunits |= set(split(STS[sid]['supporting_unit_ids']))
    if not set(split(r['supporting_unit_ids'])) <= sunits:
        fail(f"ext {r['ext_id']} units not within its statements' units")
# PD parties: QR origin/cp are PD ids
pdids = {r['pd_id'] for r in T['POSITIONS_AND_DEVICES']}
for r in T['QUALIFIED_RELATIONS']:
    for c in ('origin_pd_id', 'counterpart_pd_id'):
        if r[c] not in pdids:
            fail(f"QR {r['qr_id']} {c} not a PD")
    for x in split(r['additional_party_pd_ids']):
        if x not in pdids:
            fail(f"QR {r['qr_id']} additional party not PD")
# SC members: parties of member QRs and subjects of member NAs are member PDs
QRD = {r['qr_id']: r for r in T['QUALIFIED_RELATIONS']}
NAD = {r['na_id']: r for r in T['NORMATIVE_ASSIGNMENTS']}
for sc_ in T['SUBCONFIGURATIONS']:
    mp = set(split(sc_['member_pd_ids']))
    for q in split(sc_['member_qr_ids']):
        for c in ('origin_pd_id', 'counterpart_pd_id'):
            if QRD[q][c] not in mp:
                fail(f"SC {sc_['sc_id']}: {q} {c} {QRD[q][c]} not in member PDs")
        for x in split(QRD[q]['additional_party_pd_ids']):
            if x not in mp:
                fail(f"SC {sc_['sc_id']}: {q} additional party {x} not in member PDs")
    for n in split(sc_['member_na_ids']):
        if NAD[n]['subject_pd_id'] not in mp:
            fail(f"SC {sc_['sc_id']}: {n} subject {NAD[n]['subject_pd_id']} not in member PDs")
# no V8 vocabulary words (simple sanity), no score words
for t in TABLES:
    for r in T[t]:
        for v in r.values():
            if re.search(r'\bO[1-8]\b', v) and t not in ('SOURCE_UNIT_INVENTORY',):
                notes.append(f'possible operation-code token in {t}: {v[:40]}')
# human review trigger coverage
for r in T['NORMATIVE_ASSIGNMENTS']:
    if r['norm_type'] in ('COMPOUND', 'AMBIGUOUS') and not any(hqs[h]['trigger_code'] == 'HQ-NORMTYPE' for h in split(r['hq_ids'])):
        fail(f"HQ-NORMTYPE missing for {r['na_id']}")
for r in T['EXTERNAL_REFERENCES']:
    if r['constitutive_dependency'] == 'Y':
        if not any(hqs[h]['trigger_code'] == 'HQ-EXTDEP' and r['ext_id'] in split(hqs[h]['record_refs']) for h in hqs):
            fail(f"HQ-EXTDEP missing for {r['ext_id']}")
for r in T['POSITIONS_AND_DEVICES']:
    if r['device_classification'] == 'BORDERLINE_INS-TYPE' and not split(r['hq_ids']):
        fail(f"HQ-DEV missing for {r['pd_id']}")
for r in T['QUALIFIED_RELATIONS']:
    if r['accountability_sufficiency'] == 'indeterminate' and not any(hqs[h]['trigger_code'] == 'HQ-ACCOUNT' for h in split(r['hq_ids'])):
        fail(f"HQ-ACCOUNT missing for {r['qr_id']}")
# status ceilings
for t in ('NORMATIVE_ASSIGNMENTS', 'POSITIONS_AND_DEVICES', 'QUALIFIED_RELATIONS'):
    for r in T[t]:
        if r['epistemic_status'] not in ('documented', 'legal_constitution_evidenced', 'conceptually_projected'):
            fail(f'status above ceiling {t}')
# gap tokens recorded
dev_gaps = {r['gap_ref'] for r in T['PROTOCOL_DEVIATION_LOG']}
for g in ('GAP-01', 'GAP-02', 'GAP-03', 'GAP-04', 'GAP-05', 'GAP-06', 'GAP-07'):
    if g not in dev_gaps:
        fail(f'deviation log lacks {g}')

res = dict(rule1=RES1, rule2=RES2, rule3=RES3, rule4=RES4, rule5=RES5, rule6=RES6, rule7=RES7, rule8=RES8, rule9=RES9, rule10=RES10)
print(json.dumps(res))
print('FAILS:', len(fails))
for f in fails[:80]:
    print(' -', f)
print('NOTES:', notes[:10])
json.dump(dict(res=res, fails=fails), open(os.path.join(reg.W, 'check_result.json'), 'w'), indent=1)
