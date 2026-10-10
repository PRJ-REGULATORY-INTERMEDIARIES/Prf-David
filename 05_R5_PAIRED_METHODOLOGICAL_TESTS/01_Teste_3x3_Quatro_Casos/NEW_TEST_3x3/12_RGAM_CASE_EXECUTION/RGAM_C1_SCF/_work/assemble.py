# MECHANICAL assembly: resolves keys to ids, derives cross-links (derived_record_ids, reverse hq/unc pointers, provenance links),
# computes descriptive tallies, and writes the 19 CSV tables. No analytical content is created here.
import os, sys, csv, re, json, hashlib, random, shutil
from collections import Counter, OrderedDict, defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import reg
from reg import REG, K, KT, UT, UORDER, UCLASS, CASE, full, norm, L

FILES = ['rec_a1_statements.py', 'rec_a2_statements.py', 'rec_a3_statements.py', 'rec_b_pd.py', 'rec_c_na.py', 'rec_d_qr.py',
         'rec_e_ext.py', 'rec_f_sc_arch.py', 'rec_g_unc_hq.py', 'rec_h_screen.py']
for f in FILES:
    exec(compile(open(os.path.join(reg.W, f), encoding='utf-8').read(), f, 'exec'), {})

OUT = os.path.dirname(reg.W)
TPL = 'G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_C1_SCF/OUTPUT_TEMPLATES'
SRC_SHA = 'cf8c60fc233311436dfdd3ee236d0c8399eda55fea174610e91b5594f84a0408'
PROTO_MANIFEST = '9ca016b97289b39049dc099b265c20662c1ebc05e86bc720f0fbe80e0bac5932'
START = os.environ.get('RGAM_START', '2026-10-06T15:19:41-03:00')
END = os.environ.get('RGAM_END', '')

BY = {t: {r['key']: r for r in REG[t]} for t in REG}


def rid(x):
    return K.get(x, x)


def ids(lst):
    return ';'.join(rid(x) for x in lst)


def uids(lst):
    seen = []
    for u in lst:
        if u not in seen:
            seen.append(u)
    return ';'.join(full(u) for u in seen)


def instr(x):
    return K.get(x, x)


# ---------------- reverse links ----------------
REC_TABLES = ['NA', 'QR', 'PD', 'SC', 'ARCH', 'PROP']
for t in ['NA', 'QR']:
    for r in REG[t]:
        fn = r['function']
        if fn.endswith('*') and 'u_residual_tag' not in r['unc']:
            r['unc'].append('u_residual_tag')
        if fn == 'FUNCTION_VOCABULARY_UNRESOLVED' and 'u_function_unres' not in r['unc']:
            r['unc'].append('u_function_unres')
for h in REG['HQ']:
    for k in h['records']:
        t = KT.get(k)
        if t in REC_TABLES:
            r = BY[t][k]
            if h['key'] not in r['hq']:
                r['hq'].append(h['key'])
UNC_REC = defaultdict(list)
for t in REC_TABLES:
    for r in REG[t]:
        for u in r.get('unc', []):
            if r['key'] not in UNC_REC[u]:
                UNC_REC[u].append(r['key'])
for u in REG['UNC']:
    for k in u['records']:
        if k not in UNC_REC[u['key']]:
            UNC_REC[u['key']].append(k)

# ---------------- statements: derived record ids ----------------
ST_DER = defaultdict(list)
for t in ['NA', 'PD', 'QR', 'EXT']:
    for r in REG[t]:
        for s in r.get('sts', []):
            if r['key'] not in ST_DER[s]:
                ST_DER[s].append(r['key'])

# ---------------- helper structures ----------------
ST_BY_UNIT = defaultdict(list)
for r in REG['ST']:
    for u in r['supporting_unit_ids']:
        ST_BY_UNIT[u].append(r['key'])
PDLABEL = {r['key']: r['label'] for r in REG['PD']}


def rec_units(r):
    return list(r['units']) + [x for x in r.get('ind', []) if x not in r['units']]


def csvwrite(name, rows):
    tpl = open(os.path.join(TPL, name), 'rb').read().decode('utf-8-sig')
    header = tpl.strip('\r\n').split(',')
    path = os.path.join(OUT, name)
    with open(path, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f, lineterminator='\r\n')
        w.writerow(header)
        for r in rows:
            assert len(r) == len(header), (name, len(r), len(header), r[:3])
            w.writerow(r)
    return len(rows)


COUNTS = {}

# ---------------- 2 SOURCE_UNIT_INVENTORY ----------------
UNITS = json.load(open(os.path.join(reg.W, 'units.json'), encoding='utf-8'))
rows = []
for u in UNITS:
    rows.append([u['unit_id'], CASE, u['structure_class'], u['article_or_annex_no'], u['paragraph'], u['point'],
                 u['parent_unit_id'], u['locator_text'], u['text_sha256'], u['source_anchor']])
COUNTS['SOURCE_UNIT_INVENTORY'] = csvwrite('SOURCE_UNIT_INVENTORY.csv', rows)

# ---------------- 3 UNIT_SCREENING ----------------
ROLE = {'assignment_bearing': 'operative-assignment', 'relation_bearing': 'relation-bearing', 'position_defining': 'position-defining',
        'device_defining': 'position-defining (device)', 'definitional': 'scope/definitional-context', 'scope': 'scope/definitional-context',
        'procedural': 'procedural-mechanism', 'external_referencing': 'external-referencing', 'final_formal': 'final/formal',
        'other': 'substantive-rule-without-governance-structure'}
STK = {r['key']: r for r in REG['ST']}
rows = []
for u in UORDER:
    sts = ST_BY_UNIT.get(u, [])
    sc_ = reg.SCREEN.get(u)
    if sc_:
        rel, role, note = sc_['rel'], sc_['role'], sc_['note']
        if rel == 'Yes' and not sts:
            raise ValueError(f'screened Yes without statement: {u}')
        if rel == 'No' and sts:
            raise ValueError(f'screened No but cited by statement: {u} {sts}')
        if rel == 'Yes':
            pass
    else:
        if not sts:
            raise ValueError(f'unit without screening and without statement: {u}')
        rel = 'Yes'
        roles = []
        for s in sts:
            rr = ROLE[STK[s]['statement_kind']]
            if rr not in roles:
                roles.append(rr)
        role = '; '.join(roles)
        note = 'Derives ' + ', '.join(K[s] for s in sts) + ': ' + STK[sts[0]]['statement_summary'][:200]
    rows.append([full(u), rel, role, ';'.join(K[s] for s in sts), note])
COUNTS['UNIT_SCREENING'] = csvwrite('UNIT_SCREENING.csv', rows)
SCREEN_YES = sum(1 for r in rows if r[1] == 'Yes')
SCREEN_NO = sum(1 for r in rows if r[1] == 'No')

# ---------------- 4 INSTITUTIONAL_STATEMENTS ----------------
rows = []
for r in REG['ST']:
    rows.append([r['st_id'], uids(r['supporting_unit_ids']), r['statement_kind'], r['statement_summary'], r['evidence_span'],
                 ids(ST_DER.get(r['key'], [])), r['recital_only']])
COUNTS['INSTITUTIONAL_STATEMENTS'] = csvwrite('INSTITUTIONAL_STATEMENTS.csv', rows)

# ---------------- 5 NORMATIVE_ASSIGNMENTS ----------------
rows = []
for r in REG['NA']:
    rows.append([r['na_id'], CASE, ids(r['sts']), uids(rec_units(r)), rid(r['subj']), r['action'], r['object'], r['function'],
                 r['mechanism'], instr(r['instrument_ref']), r['modality'], r['conditions'], r['counterpart_if_identifiable'],
                 r['counterpart_status'], r['norm_type'], r['constitution_effect'], r['not_constituted_note'], r['constraint_only'],
                 r['derivation'], r['derivation_rule'], ids(r['deps']), r['legal_status_of_norm'], r['epistemic_status'],
                 r['evidence_span'], ids(r['unc']), ids(r['hq'])])
COUNTS['NORMATIVE_ASSIGNMENTS'] = csvwrite('NORMATIVE_ASSIGNMENTS.csv', rows)

# ---------------- 6 POSITIONS_AND_DEVICES ----------------
rows = []
for r in REG['PD']:
    rows.append([r['pd_id'], CASE, r['kind'], r['label'], r['type_or_instance'], uids(r['instance_source_unit_ids']), r['jurisdiction'],
                 r['temporal_reference'], r['legal_multiplicity'], r['establishment_norm_type'], r['device_identity_evidence'],
                 r['device_function_evidence'], r['device_classification'], r['legal_constitution_status'], 'not_assessed',
                 r['epistemic_status'], uids(rec_units(r)), r['evidence_span'], ids(r['unc']), ids(r['hq'])])
COUNTS['POSITIONS_AND_DEVICES'] = csvwrite('POSITIONS_AND_DEVICES.csv', rows)

# ---------------- 7 QUALIFIED_RELATIONS ----------------
rows = []
for r in REG['QR']:
    tdir = r['tdir'] or f"{PDLABEL[r['origin']]} -> {PDLABEL[r['cp']]}"
    rows.append([r['qr_id'], CASE, ids(r['sts']), uids(rec_units(r)), rid(r['origin']), rid(r['cp']), ids(r['add']), r['relation_type'],
                 r['type_note'], tdir, r['governance_direction'], r['action'], r['object'], r['function'], r['mechanism'],
                 instr(r['instrument_ref']), r['modality'], r['conditions'], r['validity_note'], r['legal_status_of_norm'],
                 r['epistemic_status'], r['derivation'], r['derivation_rule'], r['authority_attribute'], r['discretion_attribute'],
                 r['accountability_class'], r['accountability_sufficiency'], r['accountability_missing_elements'], ids(r['accvia']),
                 ids(r['deps']), r['support_gap_report'], ids(r['ext']), r['evidence_span'], ids(r['unc']), ids(r['hq'])])
COUNTS['QUALIFIED_RELATIONS'] = csvwrite('QUALIFIED_RELATIONS.csv', rows)

# ---------------- 8 EXTERNAL_REFERENCES ----------------
rows = []
for r in REG['EXT']:
    rows.append([r['ext_id'], CASE, uids(r['units']), r['referenced_legal_source'], r['source_kind'], r['reference_role'],
                 'not_checked', 'outside_corpus_not_expanded', ids(r['dependents']), r['dependency_kind'],
                 r['constitutive_dependency'], r['effect_on_claims']])
COUNTS['EXTERNAL_REFERENCES'] = csvwrite('EXTERNAL_REFERENCES.csv', rows)

# ---------------- membership helpers ----------------


def sc_units(s):
    us = []
    for k in s['qrs'] + s['nas']:
        t = KT[k]
        for u in rec_units(BY[t][k]):
            if u not in us:
                us.append(u)
    return us


def arch_units(a):
    us = []
    for s in a['member_scs']:
        for u in sc_units(BY['SC'][s]):
            if u not in us:
                us.append(u)
    return us


# ---------------- 9 SUBCONFIGURATIONS ----------------
rows = []
for s in REG['SC']:
    us = sc_units(s)
    rows.append([s['sc_id'], CASE, s['scope_label'], s['pattern_rule'], s['governance_question'], ids(s['qrs']), ids(s['nas']), ids(s['pds']),
                 s['organizing_mechanism'], s['warrant_basis'], uids(us), s['boundary_statement'], ids(s['overlap']),
                 rid(s['nested_in']) if s['nested_in'] else '', s['competing_grouping'], ids(s['unc']), ids(s['hq']), 'S'])
COUNTS['SUBCONFIGURATIONS'] = csvwrite('SUBCONFIGURATIONS.csv', rows)

# overlap sc symmetry (mechanical): add reverse overlap links
for s in REG['SC']:
    for o in s['overlap']:
        t = BY['SC'][o]
        if s['key'] not in t['overlap']:
            t['overlap'].append(s['key'])


# ---------------- status profile tallies ----------------
def tally(keys):
    parts = []
    for t, lab in (('QR', 'relations'), ('NA', 'assignments'), ('PD', 'positions/devices')):
        ks = [k for k in keys if KT.get(k) == t]
        if not ks:
            continue
        c = Counter(BY[t][k]['epistemic_status'] for k in ks)
        parts.append(f"{len(ks)} {lab}: " + '; '.join(f"{c[e]} {e}" for e in ('legal_constitution_evidenced', 'documented') if c[e]))
    parts.append('0 material_establishment_evidenced (not_assessed); 0 exercise_evidenced')
    return ' | '.join(parts)


def sc_member_keys(s):
    return s['qrs'] + s['nas'] + s['pds']


# ---------------- 10 ARCHITECTURE_CANDIDATES ----------------
rows = []
for a in REG['ARCH']:
    keys = []
    for sck in a['member_scs']:
        for k in sc_member_keys(BY['SC'][sck]):
            if k not in keys:
                keys.append(k)
    prof = tally(keys) if a['profile'] == 'AUTO' else a['profile']
    a['profile_text'] = prof
    rows.append([a['arch_id'], CASE, ids(a['member_scs']), a['i1'], uids(a['i1_units']), a['i1s'], a['i2'], a['i2k'], ids(a['i2_qrs']),
                 a['i2s'], a['i3'], a['i3b'], a['i3s'], a['i4_searched'], ids(a['i4_ext']), a['i4_rival'], a['i4_sens'], a['i4s'],
                 'Y', a['outcome'], a['basis'], prof, ids(a['unc']), ids(a['hq'])])
COUNTS['ARCHITECTURE_CANDIDATES'] = csvwrite('ARCHITECTURE_CANDIDATES.csv', rows)

# ---------------- 11 PROPERTY_REGISTER ----------------
rows = []
for p in REG['PROP']:
    rows.append([p['prop_id'], CASE, p['property_name'], p['property_family'], p['bearer_type'], rid(p['bearer']), p['scale'],
                 p['value_statement'], p['inference_rule'], p['path_semantics'], p['aggregation_rule'], ids(p['supporting']),
                 p['closure_dependency'], rid(p['closure_ref']) if p['closure_ref'] else '', p['count_basis'], p['fallacy_check'],
                 p['rival_partition'], p['status'], ids(p['hq'])])
COUNTS['PROPERTY_REGISTER'] = csvwrite('PROPERTY_REGISTER.csv', rows)

# ---------------- 12 CLOSURE_REGISTER ----------------
rows = []
for c in REG['CL']:
    rows.append([c['closure_id'], CASE, c['record_kind'], c['claim_or_scope'], c['search_description'], ids(c['unresolved_ext']),
                 c['result'], ids(c['affected'])])
COUNTS['CLOSURE_REGISTER'] = csvwrite('CLOSURE_REGISTER.csv', rows)

# ---------------- 13 PROVENANCE_LINKS ----------------
LINKS = []
FORCE = {'A29.P1', 'A29.P2', 'FIN.BIND'}


def add_link(rec_id, rtype, unit, stype, status, limitation=''):
    LINKS.append([f'LNK-{len(LINKS) + 1:05d}', rec_id, rtype, full(unit), stype, 'A', status, limitation])


for r in REG['ST']:
    for u in r['supporting_unit_ids']:
        add_link(r['st_id'], 'ST', u, 'direct', 'documented')
for t, idk in (('PD', 'pd_id'), ('NA', 'na_id'), ('QR', 'qr_id')):
    for r in REG[t]:
        derived = r.get('derivation') == 'derived'
        for u in r['units']:
            lim = 'derived record: support combined through the stated derivation rule' if derived else ''
            add_link(r[idk], t, u, 'direct', r['epistemic_status'], lim)
        for u in r.get('ind', []):
            if u in r['units']:
                continue
            if u in FORCE and r['epistemic_status'] == 'legal_constitution_evidenced':
                lim = 'supports force and applicability of the norm for the temporal reference only (entry into force, application, binding formula)'
            else:
                lim = 'indirect support: cross-referenced or contextual provision; does not state the claim itself'
            add_link(r[idk], t, u, 'indirect', 'documented' if not (u in FORCE and r['epistemic_status'] == 'legal_constitution_evidenced') else 'legal_constitution_evidenced', lim)
for r in REG['EXT']:
    for u in r['units']:
        add_link(r['ext_id'], 'EXT', u, 'direct', 'documented', 'a reference shows legal relevance only; source not checked (no external retrieval)')
    for u in r['ind']:
        add_link(r['ext_id'], 'EXT', u, 'indirect', 'documented', 'footnote identifying the referenced instrument; editorial support only')
for s in REG['SC']:
    st_ = 'documented' if any(BY[KT[k]][k]['epistemic_status'] == 'documented' for k in s['qrs'] + s['nas']) else 'legal_constitution_evidenced'
    for u in sc_units(s):
        add_link(s['sc_id'], 'SC', u, 'indirect', st_, 'support through member relations and assignments; inherits the weakest member status')
for a in REG['ARCH']:
    for u in a['i1_units']:
        add_link(a['arch_id'], 'ARCH', u, 'direct', 'documented', 'I1 scope material')
    seen = set(a['i1_units'])
    for qk in a['i2_qrs']:
        for u in rec_units(BY['QR'][qk]):
            if u not in seen:
                seen.add(u)
                add_link(a['arch_id'], 'ARCH', u, 'indirect', 'documented', 'I2 coupling relation support')


def prop_units(p, depth=0):
    us = []
    for k in p['supporting']:
        t = KT[k]
        if t == 'PROP':
            for u in prop_units(BY['PROP'][k], depth + 1):
                if u not in us:
                    us.append(u)
        elif t in ('QR', 'NA', 'PD'):
            for u in rec_units(BY[t][k]):
                if u not in us:
                    us.append(u)
    return us


for p in REG['PROP']:
    for u in prop_units(p):
        add_link(p['prop_id'], 'PROP', u, 'indirect', 'documented', 'support through the records on which the property rests')
COUNTS['PROVENANCE_LINKS'] = csvwrite('PROVENANCE_LINKS.csv', LINKS)

# ---------------- 14 UNCERTAINTY_LOG ----------------
rows = []
for u in REG['UNC']:
    recs = UNC_REC.get(u['key'], [])
    rows.append([u['unc_id'], CASE, ids(recs), uids(u['units']), u['uncertainty_type'], u['description'], u['treatment'],
                 u['effect_on_claims'], 'ESCALATED_TO_HQ' if u['hq'] else 'OPEN'])
COUNTS['UNCERTAINTY_LOG'] = csvwrite('UNCERTAINTY_LOG.csv', rows)

# ---------------- 15 HUMAN_REVIEW_QUEUE ----------------
rows = []
for h in REG['HQ']:
    rows.append([h['hq_id'], CASE, h['trigger_code'], ids(h['records']), h['question'], h['competing_readings'], h['machine_recommendation'],
                 h['reason_human_required'], '', '', '', ''])
COUNTS['HUMAN_REVIEW_QUEUE'] = csvwrite('HUMAN_REVIEW_QUEUE.csv', rows)

# ---------------- 16 TRACE_DEMONSTRATIONS ----------------


def part_of(u):
    m = re.match(r'^A(\d+)\.', u)
    if m:
        n = int(m.group(1))
        return 'CH1' if n <= 3 else 'CH2' if n <= 6 else 'CH3' if n <= 21 else 'CH4' if n <= 26 else 'CH5'
    m = re.match(r'^ANX(\d)', u)
    if m:
        return 'ANX' + m.group(1)
    return 'OTHER'


cands = {}
for s in REG['SC']:
    cands[s['sc_id']] = sc_units(s)
for a in REG['ARCH']:
    cands[a['arch_id']] = arch_units(a)
elig = sorted([k for k, us in cands.items() if len({part_of(u) for u in us if part_of(u) != 'OTHER'}) >= 2])
seed = int(SRC_SHA[:8], 16)
draw = random.Random(seed).choice(elig)
largest = max(sorted(cands), key=lambda k: (len({u for u in cands[k]}), ))
# deterministic tie handling: first in sorted order among maxima
mx = max(len(set(v)) for v in cands.values())
largest = sorted([k for k, v in cands.items() if len(set(v)) == mx])[0]
ID2KEY = {v: k for k, v in K.items()}


def chain_for(cid):
    key = ID2KEY[cid]
    items = []
    complete = True
    if KT[key] == 'ARCH':
        a = BY['ARCH'][key]
        head = f"{cid} -> member S: {ids(a['member_scs'])}; I2 coupling relations traced below"
        qks = a['i2_qrs']
        nks = []
    else:
        s = BY['SC'][key]
        head = f"{cid} -> member relations and assignments traced below"
        qks, nks = s['qrs'], s['nas']
    for k in qks + nks:
        r = BY[KT[k]][k]
        rid_ = K[k]
        stk = r['sts']
        us = r['units']
        span = r['evidence_span']
        for u in us:
            if u not in UT:
                complete = False
        if not span or not stk:
            complete = False
        items.append(f"{rid_} -> {','.join(K[s_] for s_ in stk)} -> {uids(us)} -> span: \"{span}\"")
    return head + ' ## ' + ' ## '.join(items), complete


rows = []
ch1, ok1 = chain_for(K[draw] if draw in K else draw)
rows.append(['TR-01', CASE, 'SEEDED_DRAW', seed, ';'.join(elig), draw, ch1, 'Y' if ok1 else 'N'])
ch2, ok2 = chain_for(largest)
rows.append(['TR-02', CASE, 'LARGEST_SUPPORT', '', ';'.join(elig), largest, ch2, 'Y' if ok2 else 'N'])
COUNTS['TRACE_DEMONSTRATIONS'] = csvwrite('TRACE_DEMONSTRATIONS.csv', rows)

# ---------------- 17 INSTRUMENT_LEVEL_SUMMARY ----------------
rc = '; '.join(f'{t}={COUNTS[t]}' for t in ['SOURCE_UNIT_INVENTORY', 'UNIT_SCREENING', 'INSTITUTIONAL_STATEMENTS', 'NORMATIVE_ASSIGNMENTS',
                                          'POSITIONS_AND_DEVICES', 'QUALIFIED_RELATIONS', 'EXTERNAL_REFERENCES', 'SUBCONFIGURATIONS',
                                          'ARCHITECTURE_CANDIDATES', 'PROPERTY_REGISTER', 'CLOSURE_REGISTER', 'PROVENANCE_LINKS',
                                          'UNCERTAINTY_LOG', 'HUMAN_REVIEW_QUEUE', 'TRACE_DEMONSTRATIONS'])
prof_all = []
for t, lab in (('QR', 'relations'), ('NA', 'assignments'), ('PD', 'positions/devices')):
    c = Counter(r['epistemic_status'] for r in REG[t])
    prof_all.append(f"{len(REG[t])} {lab}: " + '; '.join(f"{c[e]} {e}" for e in ('legal_constitution_evidenced', 'documented') if c[e]))
prof_all.append(f"{len(REG['EXT'])} external references: not_checked; 0 material_establishment_evidenced; 0 exercise_evidenced")
unres = sum(1 for r in REG['EXT'] if r['constitutive_dependency'] == 'Y')
outc = Counter(a['outcome'] for a in REG['ARCH'])
rows = [[CASE, len(UNITS), COUNTS['UNIT_SCREENING'], rc, 'OVERLAPPING_OR_PARTIALLY_INTEGRATED', 'A', ' | '.join(prof_all), len(REG['HQ']), unres,
         'Y',
         'Candidate outcomes: ' + '; '.join(f"{a['arch_id']}={a['outcome']}" for a in REG['ARCH']) +
         '. Machine-generated and provisional; counts are evidence descriptors only; no score, index or ranking; no comparison with any other method or case.']]
COUNTS['INSTRUMENT_LEVEL_SUMMARY'] = csvwrite('INSTRUMENT_LEVEL_SUMMARY.csv', rows)

# ---------------- 18 PROTOCOL_DEVIATION_LOG ----------------
rows = [[d['dev_id'], CASE, d['rule_id'], d['description'], d['reason'], d['impact'], d['gap_ref']] for d in REG['DEV']]
COUNTS['PROTOCOL_DEVIATION_LOG'] = csvwrite('PROTOCOL_DEVIATION_LOG.csv', rows)

# ---------------- 19 RUN_METADATA ----------------
FILES_READ = [
    'G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/12_RGAM_CASE_EXECUTION/RGAM_C1_SCF/EXECUTOR_BRIEF.md',
    'G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/RGAM_PAIRED_EXECUTION_PROTOCOL_v1_0.md',
    'G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/RGAM_PAIRED_DECISION_RULES_v1_0.md',
    'G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/RGAM_PAIRED_DATA_DICTIONARY_v1_0.md',
    'G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/RGAM_CASE_OUTPUT_SCHEMA.md',
    'G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/RGAM_BLINDNESS_AND_ACCESS_POLICY.md',
    'G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/RGAM_EXECUTION_GAP_DECISIONS_v1_0.md',
    'G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_C1_SCF/CASE_METADATA.json',
    'G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_C1_SCF/CAPSULE_README.md',
    'G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_C1_SCF/LEGAL_SOURCE/32023R0955_official_en.html',
    'G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_C1_SCF/OUTPUT_TEMPLATES/ (20 files: 19 CSV templates and CASE_RGAM_REPORT_TEMPLATE.md)',
    'G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/12_RGAM_CASE_EXECUTION/RGAM_C1_SCF/_work/ (own scratch files)']
rows = [['RUN-01', CASE, 'RGAM paired execution protocol v1.0', PROTO_MANIFEST + ' (as stated in RGAM_EXECUTION_GAP_DECISIONS_v1_0.md; not stated in the capsule files)',
         'claude-sonnet-5-5 (as stated in the invocation context: Sonnet 5.5)',
         'reasoning_effort=10 (value displayed in the invocation context; the brief requested the highest available effort and the displayed setting could not be changed by the executor); temperature NOT_EXPOSED; top-p NOT_EXPOSED; seed NOT_EXPOSED; token limits NOT_EXPOSED (a remaining context-token counter was displayed at about 15 000 000 at start)',
         START, END or 'SEE_EXECUTION_PROVENANCE', 'Y', ' ; '.join(FILES_READ), 'NONE', 'Y']]
COUNTS['RUN_METADATA'] = csvwrite('RUN_METADATA.csv', rows)

# ---------------- 1 W_DECLARATION ----------------
Wrow = [CASE, 'REGULATION (EU) 2023/955 OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL of 10 May 2023 establishing a Social Climate Fund and amending Regulation (EU) 2021/1060',
        '32023R0955', 'European Union',
        'Establishment of a Social Climate Fund (title; A1.P1) and amendment of Regulation (EU) 2021/1060 (title); the object clause of A1.P2 and A3 concerns financial support to Member States for measures and investments in Social Climate Plans addressing the social impacts of the inclusion of greenhouse gas emissions from buildings and road transport within the scope of Directive 2003/87/EC.',
        'Regulation', 'Original act as published (OJ L 130, 16 May 2023); no consolidation',
        'Reference date 30 June 2024 (date from which the Regulation applies, A29.P2); entry into force on the twentieth day following publication (A29.P1; publication date 16.5.2023 as printed in the source header); Fund interval 2026-2032 (A1.P1) with payments until 31 December 2033 (A20.P8). The neutral metadata state the original act and give no repeal-related information; the baseline is not asserted to be the law applicable at any other date.',
        'All units of the controlling frozen source file (LEGAL_SOURCE/32023R0955_official_en.html): page header, title, citations, recitals, enacting formula, chapter and article headings, articles with paragraphs, points and sub-points, final formula, footnotes and Annexes I-V; identifiers documented in the deviation log (d_units).',
        'Content not representable as text in the source file: embedded formula images of Annex I (11 image elements: six image-only paragraphs carried as placeholder units and five inline) and the empty cells and layout of the Annex V template tables; list markers of enumerations are carried in locator text, not as units. No consolidation, no corrigenda and no external text are included.',
        'LEGAL_SOURCE/32023R0955_official_en.html (capsule RGAM_C1_SCF)', SRC_SHA, SRC_SHA, 'Y',
        sum(1 for u in UNITS if re.match(r'^A\d+\.HD$', u['unit_id'][len(CASE) + 1:])),
        sum(1 for u in UNITS if re.match(r'^ANX\d\.HD$', u['unit_id'][len(CASE) + 1:])),
        sum(1 for u in UNITS if u['structure_class'] == 'RECITAL'),
        'MATCH: 29 articles and 5 annexes parsed (metadata: 29 and 5); recitals parsed 47 (not stated in the metadata)',
        'W is a documentary universe, not an architecture; it can close only statements about the complete instrument as published (coverage of all units); it cannot close statements about the sources it cites or about establishment, operation or outcomes; absence-dependent claims are limited to the search of W (not found is a statement about the search, not about the law).',
        'W != A']
COUNTS['W_DECLARATION'] = csvwrite('W_DECLARATION.csv', [Wrow])

# ---------------- save state for report generation ----------------
STATE = dict(COUNTS=COUNTS, SCREEN_YES=SCREEN_YES, SCREEN_NO=SCREEN_NO, seed=seed, elig=elig, draw=draw, largest=largest,
             n_units=len(UNITS), unres=unres, outc=dict(outc))
json.dump(STATE, open(os.path.join(reg.W, 'state.json'), 'w', encoding='utf-8'), indent=1)
print(json.dumps(STATE, indent=1))
