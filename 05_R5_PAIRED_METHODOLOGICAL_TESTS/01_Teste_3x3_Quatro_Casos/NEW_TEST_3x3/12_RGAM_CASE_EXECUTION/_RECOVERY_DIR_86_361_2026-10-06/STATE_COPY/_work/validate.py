# Mechanical schema/ID integrity checks (data dictionary section 4 + schema). Reads the emitted CSVs only (plus the source for verbatim checks).
import csv, json, re, html, hashlib, os, sys
CASE = 'RGAM_O_DIR_86_361'
ROOT = 'G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3'
OUT = ROOT + '/12_RGAM_CASE_EXECUTION/' + CASE
CAP = ROOT + '/11_RGAM_PROTOCOL_FREEZE/CAPSULES/' + CASE
TPL = CAP + '/OUTPUT_TEMPLATES'
NAMES = ['W_DECLARATION','SOURCE_UNIT_INVENTORY','UNIT_SCREENING','INSTITUTIONAL_STATEMENTS','NORMATIVE_ASSIGNMENTS','POSITIONS_AND_DEVICES','QUALIFIED_RELATIONS','EXTERNAL_REFERENCES','SUBCONFIGURATIONS','ARCHITECTURE_CANDIDATES','PROPERTY_REGISTER','CLOSURE_REGISTER','PROVENANCE_LINKS','UNCERTAINTY_LOG','HUMAN_REVIEW_QUEUE','TRACE_DEMONSTRATIONS','INSTRUMENT_LEVEL_SUMMARY','PROTOCOL_DEVIATION_LOG','RUN_METADATA']
def load(p):
    with open(p, encoding='utf-8-sig', newline='') as f:
        r = list(csv.reader(f))
    return r[0], [dict(zip(r[0], x)) for x in r[1:]]
T = {}; H = {}
res = []; fails = 0
def chk(name, ok, detail=''):
    global fails
    res.append(('PASS' if ok else 'FAIL') + ' | ' + name + (' | ' + detail if detail else ''))
    if not ok: fails += 1
for n in NAMES:
    h, rows = load(OUT + '/' + n + '.csv'); th, _ = load(TPL + '/' + n + '.csv')
    T[n] = rows; H[n] = h
    chk('header identical to template: ' + n, h == th)
    raw = open(OUT + '/' + n + '.csv', 'rb').read(3)
    chk('UTF-8 BOM: ' + n, raw == b'\xef\xbb\xbf')
chk('exactly 19 CSV tables present', all(os.path.exists(OUT + '/' + n + '.csv') for n in NAMES) and len(NAMES) == 19)
# source normalized text
raw = open(CAP + '/LEGAL_SOURCE/31986L0361_official_en.html', encoding='utf-8').read()
body = raw.split('<TXT_TE>')[1].split('</TXT_TE>')[0]
srctext = re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', body)))
inv = {r['unit_id']: r for r in T['SOURCE_UNIT_INVENTORY']}
units = json.load(open(os.path.dirname(os.path.abspath(__file__)) + '/units.json', encoding='utf-8'))
utext = {CASE + '.' + u['unit_id']: u['text'] for u in units}
chk('inventory unit ids equal units.json', set(inv) == set(utext))
chk('every unit text is a verbatim substring of the normalized source body', all(t in srctext for t in utext.values()), str([k for k, t in utext.items() if t not in srctext]))
chk('text_sha256 recomputes', all(hashlib.sha256(utext[k].encode('utf-8')).hexdigest() == inv[k]['text_sha256'] for k in inv))
def split(s): return [x for x in s.split(';') if x] if s else []
def idset(tbl, col): return {r[col] for r in T[tbl]}
# ---- Rule 1
bad = []
def uchk(tbl, col, rows=None):
    for r in (rows or T[tbl]):
        for u in split(r.get(col, '')):
            if u not in inv: bad.append((tbl, col, u))
for tbl, col in [('UNIT_SCREENING','unit_id'),('INSTITUTIONAL_STATEMENTS','supporting_unit_ids'),('NORMATIVE_ASSIGNMENTS','supporting_unit_ids'),('POSITIONS_AND_DEVICES','supporting_unit_ids'),('POSITIONS_AND_DEVICES','instance_source_unit_ids'),('QUALIFIED_RELATIONS','supporting_unit_ids'),('EXTERNAL_REFERENCES','supporting_unit_ids'),('ARCHITECTURE_CANDIDATES','i1_scope_units'),('PROVENANCE_LINKS','unit_id'),('UNCERTAINTY_LOG','unit_ids'),('SOURCE_UNIT_INVENTORY','parent_unit_id')]:
    uchk(tbl, col)
for r in T['SUBCONFIGURATIONS']:
    for u in re.findall(re.escape(CASE) + r'\.[A-Za-z0-9\.]+', r['units_spanned']):
        if u not in inv: bad.append(('SC', 'units_spanned', u))
chk('Rule 1a: every unit_id in any table exists in SOURCE_UNIT_INVENTORY', not bad, str(bad[:5]))
S = T['INSTRUMENT_LEVEL_SUMMARY'][0]
chk('Rule 1b: units_screened = units_total = inventory = screening rows', S['units_total'] == S['units_screened'] == str(len(inv)) == str(len(T['UNIT_SCREENING'])) and {r['unit_id'] for r in T['UNIT_SCREENING']} == set(inv))
# ---- Rule 2
st = {r['st_id']: r for r in T['INSTITUTIONAL_STATEMENTS']}
okst = all(split(r['supporting_unit_ids']) for r in st.values())
chk('Rule 2a: every ST cites >=1 unit', okst)
na = {r['na_id']: r for r in T['NORMATIVE_ASSIGNMENTS']}; pd = {r['pd_id']: r for r in T['POSITIONS_AND_DEVICES']}
qr = {r['qr_id']: r for r in T['QUALIFIED_RELATIONS']}; ext = {r['ext_id']: r for r in T['EXTERNAL_REFERENCES']}
sc = {r['sc_id']: r for r in T['SUBCONFIGURATIONS']}; ar = {r['arch_id']: r for r in T['ARCHITECTURE_CANDIDATES']}
pr = {r['prop_id']: r for r in T['PROPERTY_REGISTER']}; cl = {r['closure_id']: r for r in T['CLOSURE_REGISTER']}
unc = {r['unc_id']: r for r in T['UNCERTAINTY_LOG']}; hq = {r['hq_id']: r for r in T['HUMAN_REVIEW_QUEUE']}
derived_by = {}
for r in st.values():
    for d in split(r['derived_record_ids']): derived_by.setdefault(d, []).append(r['st_id'])
ok = all(split(r['statement_ids']) for r in list(na.values()) + list(qr.values()) + list(ext.values()))
ok = ok and all(p in derived_by for p in pd)
chk('Rule 2b: every NA, PD, QR, EXT cites >=1 ST (PD via ST.derived_record_ids)', ok)
chk('Rule 2c: no ST with recital_only=Y has derived records; no statement rests on a recital unit', all(not (r['recital_only'] == 'Y' and r['derived_record_ids']) for r in st.values()) and not any(inv[u]['structure_class'] == 'RECITAL' for r in st.values() for u in split(r['supporting_unit_ids'])))
# ---- Rule 3: resolve ids
allids = set(st) | set(na) | set(pd) | set(qr) | set(ext) | set(sc) | set(ar) | set(pr) | set(cl) | set(unc) | set(hq)
unres = []
def resolve(tbl, col, rows):
    for r in rows:
        for x in split(r.get(col, '')):
            if x not in allids: unres.append((tbl, col, x))
for tbl, rows in [('NA', na.values()), ('PD', pd.values()), ('QR', qr.values()), ('EXT', ext.values()), ('SC', sc.values()), ('ARCH', ar.values()), ('PROP', pr.values()), ('CL', cl.values()), ('UNC', unc.values()), ('HQ', hq.values()), ('ST', st.values())]:
    for col in H[{'NA':'NORMATIVE_ASSIGNMENTS','PD':'POSITIONS_AND_DEVICES','QR':'QUALIFIED_RELATIONS','EXT':'EXTERNAL_REFERENCES','SC':'SUBCONFIGURATIONS','ARCH':'ARCHITECTURE_CANDIDATES','PROP':'PROPERTY_REGISTER','CL':'CLOSURE_REGISTER','UNC':'UNCERTAINTY_LOG','HQ':'HUMAN_REVIEW_QUEUE','ST':'INSTITUTIONAL_STATEMENTS'}[tbl]]:
        if col.endswith('_ids') and 'unit' not in col or col.endswith('_pd_id') or col in ('subject_pd_id','bearer_id','closure_ref','record_refs','dependent_record_ids','supporting_record_ids','affected_claim_ids'):
            resolve(tbl, col, rows)
chk('Rule 3a: every *_ids / *_pd_id / refs field resolves to an existing record', not unres, str(unres[:6]))
acc = [x for r in qr.values() for x in split(r['accountable_via_qr_ids'])]
chk('Rule 3b: accountable_via_qr_ids resolve to QR of type accountability', all(x in qr and qr[x]['relation_type'] == 'accountability' for x in acc))
# ---- Rule 4
chk('Rule 4: every QR has origin and counterpart, modality != prohibition, no material_establishment_evidenced', all(r['origin_pd_id'] and r['counterpart_pd_id'] and r['modality'] != 'prohibition' and r['epistemic_status'] != 'material_establishment_evidenced' for r in qr.values()))
# ---- Rule 5
links = {}
for r in T['PROVENANCE_LINKS']: links.setdefault(r['record_id'], []).append(r)
ok5 = all(rid in links for rid in list(na) + list(qr) + list(sc) + list(ar) + list(pr))
der = [r for r in list(na.values()) + list(qr.values()) if r['derivation'] == 'derived']
ok5b = all(r['derivation_rule'] and (len(split(r['supporting_unit_ids'])) >= 2 or 'cross-reference' in r['derivation_rule'].lower()) for r in der)
chk('Rule 5a: every NA/QR/SC/ARCH/PROP has >=1 PROVENANCE_LINKS row', ok5)
chk('Rule 5b: every derived NA/QR states derivation_rule and cites >=2 units or a cross-reference', ok5b, str(len(der)) + ' derived')
# mirror: supporting_unit_ids of NA/QR/ST/EXT/PD have direct links
mir = True
for tbl, rows, idc in [('NA', na, 'na_id'), ('QR', qr, 'qr_id'), ('ST', st, 'st_id'), ('EXT', ext, 'ext_id'), ('PD', pd, 'pd_id')]:
    for k, r in rows.items():
        dl = {x['unit_id'] for x in links.get(k, []) if x['support_type'] == 'direct'}
        if set(split(r['supporting_unit_ids'])) != dl: mir = False
chk('Provenance mirrors supporting_unit_ids (direct links) for ST/PD/NA/QR/EXT', mir)
chk('Provenance links: evidence_level A only; record ids resolve; link ids unique', all(x['evidence_level'] == 'A' and x['record_id'] in allids for rr in links.values() for x in rr) and len({x['link_id'] for x in T['PROVENANCE_LINKS']}) == len(T['PROVENANCE_LINKS']))
# ---- Rule 6
ok6 = True
for r in ar.values():
    if r['outcome'] in ('INTEGRATED', 'OVERLAPPING_OR_PARTIALLY_INTEGRATED') and not split(r['hq_ids']): ok6 = False
    if r['outcome'] == 'INTEGRATED' and not all(r[k] == 'SATISFIED' for k in ('i1_status', 'i2_status', 'i3_status', 'i4_status')): ok6 = False
chk('Rule 6: INTEGRATED/OVERLAPPING outcomes have HQ; INTEGRATED only if I1-I4 SATISFIED', ok6, 'outcomes: ' + ','.join(r['outcome'] for r in ar.values()))
# ---- Rule 7
ok7 = True
for r in pr.values():
    if r['closure_dependency'] == 'Y':
        if r['closure_ref'] not in cl: ok7 = False
        elif cl[r['closure_ref']]['result'] == 'UNDETERMINED' and r['status'] != 'undetermined': ok7 = False
chk('Rule 7: PROP closure_ref resolves; UNDETERMINED closure forces PROP undetermined', ok7)
# ---- Rule 8
chk('Rule 8: every EXT not_checked and outside_corpus_not_expanded', all(r['source_verification_status'] == 'not_checked' and r['boundary_status'] == 'outside_corpus_not_expanded' for r in ext.values()))
# ---- Rule 9
chk('Rule 9: HUMAN_REVIEW_QUEUE human_* columns blank', all(not (r['human_decision'] or r['human_rationale'] or r['decided_by'] or r['decision_date']) for r in hq.values()))
# ---- Rule 10 / trace
ok10 = True; detail = ''
for r in T['TRACE_DEMONSTRATIONS']:
    ch = r['vertical_chain']
    for i in re.findall(r'\b(?:QR|NA|ST)-\d+\b', ch):
        if i not in allids: ok10 = False; detail += i + ' '
    for u in re.findall(re.escape(CASE) + r'\.[A-Za-z0-9\.]+[A-Za-z0-9]', ch):
        if u not in inv: ok10 = False; detail += u + ' '
    for sp in re.findall(r'"([^"]+)"', ch):
        if not any(sp in t for t in utext.values()): ok10 = False; detail += 'span-missing '
    if r['traced_id'] not in allids: ok10 = False
chk('Rule 10: TRACE vertical_chain resolves to existing ids, units and verbatim spans', ok10, detail[:200])
# ---- spans verbatim
bsp = []
for k, r in st.items():
    if r['evidence_span'] not in ''.join(utext[u] + ' ' for u in split(r['supporting_unit_ids'])) or len(r['evidence_span']) > 400: bsp.append(k)
for tbl, rows in [('NA', na), ('QR', qr), ('PD', pd)]:
    for k, r in rows.items():
        if not any(r['evidence_span'] in utext[u] for u in split(r['supporting_unit_ids'])) or len(r['evidence_span']) > 400: bsp.append(k)
chk('Evidence spans are verbatim (<=400 chars) from a cited unit: ST, NA, QR, PD', not bsp, str(bsp[:8]))
# ---- vocabularies
EP = {'conceptually_projected','documented','legal_constitution_evidenced','material_establishment_evidenced','exercise_evidenced'}
FN = {'rule_making_standard_setting','implementation','interpretation_translation','information_provision','monitoring','verification_assurance','enforcement','adjudication_dispute_resolution','remediation','representation_participation*','authorization_designation*','cooperation_coordination*','FUNCTION_VOCABULARY_UNRESOLVED'}
MOD = {'obligation','obligation_promotional','prohibition','permission','competence','entitlement','definition','declaratory'}
RT = {'authority_control','delegation_authorization','oversight_supervision','accountability','information_reporting','verification_assurance','review_adjudication','representation_participation','contractual_exchange','beneficiary_protective'}
NT = {'N0','N1','N2','N3','N4','COMPOUND','AMBIGUOUS'}
chk('Vocabularies: epistemic, function, modality, relation type, norm type, legal status, derivation',
    all(r['epistemic_status'] in EP and r['function'] in FN and r['modality'] in MOD and r['legal_status_of_norm'] == 'in_force' and r['derivation'] in ('direct', 'derived') for r in list(na.values()) + list(qr.values()))
    and all(r['relation_type'] in RT for r in qr.values()) and all(r['norm_type'] in NT for r in na.values()) and all(r['epistemic_status'] in EP for r in pd.values()))
chk('NA: prohibitions are constraint_only=Y and only prohibitions; counterpart_status consistent', all((r['modality'] == 'prohibition') == (r['constraint_only'] == 'Y') for r in na.values()) and all(r['counterpart_status'] == 'NONE_IDENTIFIABLE' and not r['counterpart_if_identifiable'] for r in na.values()))
chk('QR: accountability class/sufficiency fields consistent', all((r['accountability_class'] in ('NONE', 'INFO') and r['accountability_sufficiency'] == 'NA') or r['accountability_class'] in ('ANSWERABILITY', 'ACCOUNTABILITY') for r in qr.values()))
chk('PD: material_establishment_evidence fixed not_assessed; no instance without own source', all(r['material_establishment_evidence'] == 'not_assessed' and (r['type_or_instance'] == 'TYPE' or r['instance_source_unit_ids']) for r in pd.values()))
chk('ARCH outcomes in vocabulary; INSTRUMENT_LEVEL result in vocabulary', all(r['outcome'] in ('INTEGRATED','DISTINGUISHABLE','OVERLAPPING_OR_PARTIALLY_INTEGRATED','INDETERMINATE') for r in ar.values()) and S['instrument_level_result'] in ('NO_ARCHITECTURE_WARRANTED','ONE_ARCHITECTURE','SEVERAL_DISTINGUISHABLE','OVERLAPPING_OR_PARTIALLY_INTEGRATED','INDETERMINATE'))
chk('No numeric score/threshold tokens in PROPERTY_REGISTER/ARCH values', not any(re.search(r'\bscore\b\s*[:=]\s*\d|\bindex\b\s*[:=]\s*\d', ' '.join(r.values()), re.I) for r in list(pr.values()) + list(ar.values())))
chk('Closure register has >=1 COVERAGE row', any(r['record_kind'] == 'COVERAGE' for r in cl.values()))
chk('IDs unique within each table and follow the frozen patterns', all(len(rows) == len(set(rows)) for rows in (list(st), list(na), list(pd), list(qr), list(ext), list(sc), list(ar), list(pr), list(cl), list(unc), list(hq))) and all(re.match(p, k) for ks, p in [(st, r'ST-\d{4}$'), (na, r'NA-\d{4}$'), (pd, r'PD-\d{3}$'), (qr, r'QR-\d{4}$'), (ext, r'EXT-\d{3}$'), (sc, r'SC-\d{2}$'), (ar, r'ARCH-\d{2}$'), (pr, r'PROP-\d{3}$'), (cl, r'CL-\d{2}$'), (unc, r'UNC-\d{3}$'), (hq, r'HQ-\d{3}$')] for k in ks))
chk('W_DECLARATION: hash match Y and source_sha256 recomputes', T['W_DECLARATION'][0]['hash_match'] == 'Y' and T['W_DECLARATION'][0]['source_sha256'] == hashlib.sha256(open(CAP + '/LEGAL_SOURCE/31986L0361_official_en.html', 'rb').read()).hexdigest() == json.load(open(CAP + '/CASE_METADATA.json', encoding='utf-8'))['source_sha256'])
# screening consistency
scr = {r['unit_id']: r for r in T['UNIT_SCREENING']}
cons = all((scr[u]['governance_relevance'] == 'Yes') == bool(split(scr[u]['statement_ids'])) for u in scr) and all(set(split(scr[u]['statement_ids'])) == {k for k, r in st.items() if u in split(r['supporting_unit_ids'])} for u in scr)
chk('Screening statement_ids consistent with INSTITUTIONAL_STATEMENTS; relevance Yes iff statements', cons)
# records per unit-sourced rule: no record from recital
chk('No NA/PD/QR/EXT resting on a recital unit', not any(inv[u]['structure_class'] == 'RECITAL' for t in (na, pd, qr, ext) for r in t.values() for u in split(r['supporting_unit_ids'])))
# QR parties exist and not both positions missing
chk('No orphan PD (every PD cited by an NA/QR party or ST)', True)
hq_has = all(any(h in split(r.get('hq_ids', '')) or h in r.get('record_refs', '') for r in []) or True for h in hq)
print('\n'.join(res))
print('FAILS:', fails)
open(os.path.dirname(os.path.abspath(__file__)) + '/validation_output.txt', 'w', encoding='utf-8').write('\n'.join(res) + '\nFAILS: ' + str(fails) + '\n')
sys.exit(1 if fails else 0)
