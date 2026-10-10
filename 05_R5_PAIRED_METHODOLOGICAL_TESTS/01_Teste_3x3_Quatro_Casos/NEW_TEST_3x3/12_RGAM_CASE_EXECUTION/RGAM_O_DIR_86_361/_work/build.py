# MECHANICAL assembler: resolves keys to ids, derives unions/links/tallies, writes the 19 CSV tables.
# No analytical content is generated here; all analytical records are authored in data_*.py.
import json, csv, hashlib, random, re, sys, os, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data_st import ST
from data_p import PD, NA, TR
from data_qr import QR
from data_ext_sc import EXT, SC, ARCH
from data_gov import UNC, HQ, DEV, CL, PROP
from data_screen import SCREEN

CASE = 'RGAM_O_DIR_86_361'
ROOT = 'G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3'
OUT = ROOT + '/12_RGAM_CASE_EXECUTION/' + CASE
CAP = ROOT + '/11_RGAM_PROTOCOL_FREEZE/CAPSULES/' + CASE
TPL = CAP + '/OUTPUT_TEMPLATES'
SRC = CAP + '/LEGAL_SOURCE/31986L0361_official_en.html'
META = json.load(open(CAP + '/CASE_METADATA.json', encoding='utf-8'))
UNITS = json.load(open(os.path.dirname(os.path.abspath(__file__)) + '/units.json', encoding='utf-8'))
U = {u['unit_id']: u for u in UNITS}
def full(u): return CASE + '.' + u
def fulls(us): return ';'.join(full(u) for u in us)

# ---------- ids
ID = {}
def assign(tag, items, fmt):
    for i, it in enumerate(items, 1):
        ID[(tag, it['k'])] = fmt % i
assign('ST', ST, 'ST-%04d'); assign('PD', PD, 'PD-%03d'); assign('NA', NA, 'NA-%04d'); assign('QR', QR, 'QR-%04d')
assign('EXT', EXT, 'EXT-%03d'); assign('SC', SC, 'SC-%02d'); assign('ARCH', ARCH, 'ARCH-%02d'); assign('PROP', PROP, 'PROP-%03d')
assign('CL', CL, 'CL-%02d'); assign('UNC', UNC, 'UNC-%03d'); assign('HQ', HQ, 'HQ-%03d')
def rid(tok):
    t, k = tok.split(':', 1)
    return ID[(t, k)]
def ids(tag, keys): return ';'.join(ID[(tag, k)] for k in keys)
byk = {}
for tag, lst in [('ST', ST), ('PD', PD), ('NA', NA), ('QR', QR), ('EXT', EXT), ('SC', SC), ('ARCH', ARCH), ('PROP', PROP), ('CL', CL), ('UNC', UNC), ('HQ', HQ)]:
    for it in lst: byk[(tag, it['k'])] = it

def st_units(keys):
    out = []
    for k in keys:
        for u in byk[('ST', k)]['u']:
            if u not in out: out.append(u)
    return out
def rec_units(tok):
    t, k = tok.split(':', 1)
    r = byk[(t, k)]
    if t in ('NA', 'QR'): return st_units(r['st'])
    if t == 'ST': return list(r['u'])
    if t == 'PD': return list(r['units'])
    return []

# ---------- templates
def hdr(name):
    with open(TPL + '/' + name + '.csv', encoding='utf-8-sig') as f:
        return next(csv.reader(f))
def write(name, rows):
    h = hdr(name)
    with open(OUT + '/' + name + '.csv', 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f, lineterminator='\n')
        w.writerow(h)
        for r in rows:
            w.writerow([r.get(c, '') for c in h])
    return len(rows)

# ---------- W
src_sha = hashlib.sha256(open(SRC, 'rb').read()).hexdigest()
assert src_sha == META['source_sha256']
nart = len({u['article_or_annex_no'] for u in UNITS if u['structure_class'] == 'OPERATIVE_ARTICLE'})
nrec = len([u for u in UNITS if u['structure_class'] == 'RECITAL'])
W = [dict(case_id=CASE, instrument_title='Council Directive 86/361/EEC of 24 July 1986 on the initial stage of the mutual recognition of type approval for telecommunications terminal equipment', celex=META['celex'],
          jurisdiction='European Economic Community (Council directive addressed to the Member States, A12.P0)',
          domain_declaration='Telecommunications terminal equipment: the initial stage of mutual recognition of type approval, namely mutual recognition of the results of tests of conformity with common conformity specifications for mass-produced telecommunications terminal equipment (from the title and the object clause of Article 1 only)',
          instrument_type='Directive (Council Directive)', version_type='Original act as published, OJ L 217, 05/08/1986, p. 21 (official EUR-Lex HTML, English); no consolidation',
          temporal_reference=TR + '. The act is dated 24 July 1986 (FRM8); Article 11(1) sets a Member State implementation period of not more than one year following adoption (derived deadline 24 July 1987); W states no entry-into-force date; neutral metadata: historical original act, later repealed (1992), no successor act substituted. Legal status is asserted only for this interval, not for any other date.',
          inclusion_rule='All units of the frozen source file: formal preamble units, 14 recitals (unnumbered "Whereas" clauses), Articles 1-12 (no annexes) and the closing formal units',
          exclusions='EUR-Lex page chrome (banner, metadata block, language links, header title lines duplicating the title); the "*****" separator; the "Article N" heading lines as separate units (kept as locators); no tables or annexes exist; Official Journal page layout is not representable in the source file',
          source_file='11_RGAM_PROTOCOL_FREEZE/CAPSULES/' + CASE + '/LEGAL_SOURCE/31986L0361_official_en.html', source_sha256=src_sha, expected_sha256=META['source_sha256'], hash_match='Y',
          article_count_parsed=str(nart), annex_count_parsed='0', recital_count_parsed=str(nrec),
          structure_check='MATCH (articles 12 parsed = 12 in neutral metadata; annexes 0 = 0; recital count is not stated in the neutral metadata, 14 parsed; 93 units in total)',
          closure_scope_statement='Within W the search is complete (all units inventoried and screened; internal cross-references followed). W cannot close questions that depend on sources outside W: the Memorandum of Understanding on NETs, the CEPT accreditation system, Article 9 of Directive 73/23/EEC, Directive 83/189/EEC, national measures and any other instrument; "not found" is a statement about the search of W only; silence is neither permission nor prohibition.',
          w_is_not_a='W != A')]

# ---------- inventory & screening
INV = []; SCR = []
st_by_unit = {}
for s in ST:
    for u in s['u']: st_by_unit.setdefault(u, []).append(ID[('ST', s['k'])])
for u in UNITS:
    INV.append(dict(unit_id=full(u['unit_id']), case_id=CASE, structure_class=u['structure_class'], article_or_annex_no=u['article_or_annex_no'], paragraph=u['paragraph'], point=u['point'],
                    parent_unit_id=full(u['parent_unit_id']) if u['parent_unit_id'] else '', locator_text=u['locator_text'], text_sha256=u['text_sha256'], source_anchor=u['source_anchor']))
    tag, note = SCREEN[u['unit_id']]
    sts = st_by_unit.get(u['unit_id'], [])
    SCR.append(dict(unit_id=full(u['unit_id']), governance_relevance='Yes' if sts else 'No', governance_role_tag=tag, statement_ids=';'.join(sts), screening_note=note))

# ---------- reverse maps
unc_rev, hq_rev = {}, {}
def note_refs(tag, items):
    for it in items:
        for u in it.get('unc', []): unc_rev.setdefault(u, []).append(ID[(tag, it['k'])])
        for h in it.get('hq', []): hq_rev.setdefault(h, []).append(ID[(tag, it['k'])])
for tag, lst in [('PD', PD), ('NA', NA), ('QR', QR), ('SC', SC), ('ARCH', ARCH), ('PROP', PROP)]: note_refs(tag, lst)

# ---------- derived record ids per statement
derived = {}
for tag, lst in [('PD', PD), ('NA', NA), ('QR', QR), ('EXT', EXT)]:
    for r in lst:
        for s in r['st']: derived.setdefault(s, []).append(ID[(tag, r['k'])])
STROWS = []
for s in ST:
    STROWS.append(dict(st_id=ID[('ST', s['k'])], supporting_unit_ids=fulls(s['u']), statement_kind=s['kind'], statement_summary=s['sum'], evidence_span=s['span'],
                       derived_record_ids=';'.join(sorted(derived.get(s['k'], []))), recital_only='N'))

# ---------- PD
PDROWS = []
for p in PD:
    PDROWS.append(dict(pd_id=ID[('PD', p['k'])], case_id=CASE, kind=p['kind'], label=p['label'], type_or_instance=p['ti'], instance_source_unit_ids=fulls(p['inst']), jurisdiction=p['jur'], temporal_reference=TR,
                       legal_multiplicity=p['mult'], establishment_norm_type=p['norm'], device_identity_evidence=p['idev'], device_function_evidence=p['fdev'],
                       device_classification=p['cls'], legal_constitution_status=p['lcs'], material_establishment_evidence='not_assessed', epistemic_status='documented',
                       supporting_unit_ids=fulls(p['units']), evidence_span=p['span'], uncertainty_ids=ids('UNC', p['unc']), hq_ids=ids('HQ', p['hq'])))

# ---------- NA
NAROWS = []
for n in NA:
    NAROWS.append(dict(na_id=ID[('NA', n['k'])], case_id=CASE, statement_ids=ids('ST', n['st']), supporting_unit_ids=fulls(st_units(n['st'])), subject_pd_id=ID[('PD', n['subj'])], action=n['action'], object=n['obj'],
                       function=n['fn'], mechanism=n['mech'], instrument_ref=n['instr'], modality=n['mod'], conditions=n['cond'], counterpart_if_identifiable=n['cp'], counterpart_status=n['cps'],
                       norm_type=n['nt'], constitution_effect=n['ceff'], not_constituted_note=n['nconst'], constraint_only=n['co'], derivation=n['der'], derivation_rule=n['rule'],
                       depends_on_pd_ids=ids('PD', n['dep']), legal_status_of_norm=n['ls'], epistemic_status=n['ep'], evidence_span=n['span'], uncertainty_ids=ids('UNC', n['unc']), hq_ids=ids('HQ', n['hq'])))

# ---------- EXT
EXTROWS = []
def tokids(toks): return ';'.join(rid(t) for t in toks)
for e in EXT:
    EXTROWS.append(dict(ext_id=ID[('EXT', e['k'])], case_id=CASE, supporting_unit_ids=fulls(st_units(e['st'])), referenced_legal_source=e['src'], source_kind=e['kind'], reference_role=e['role'],
                        source_verification_status='not_checked', boundary_status='outside_corpus_not_expanded', dependent_record_ids=tokids(e['dep']), dependency_kind=e['dkind'],
                        constitutive_dependency=e['cdep'], effect_on_claims=e['eff']))

# ---------- QR
QRROWS = []
for q in QR:
    ext_ids = ids('EXT', q['ext'])
    QRROWS.append(dict(qr_id=ID[('QR', q['k'])], case_id=CASE, statement_ids=ids('ST', q['st']), supporting_unit_ids=fulls(st_units(q['st'])), origin_pd_id=ID[('PD', q['org'])], counterpart_pd_id=ID[('PD', q['cp'])],
                       additional_party_pd_ids=ids('PD', q['add']), relation_type=q['rt'], type_note=q['tn'], textual_direction=q['td'], governance_direction=q['gd'], action=q['action'], object=q['obj'],
                       function=q['fn'], mechanism=q['mech'], instrument_ref=q['instr'], modality=q['mod'], conditions=q['cond'], validity_note=q['vn'], legal_status_of_norm=q['ls'], epistemic_status=q['ep'],
                       derivation=q['der'], derivation_rule=q['rule'], authority_attribute=q['auth'], discretion_attribute=q['disc'], accountability_class=q['ac'], accountability_sufficiency=q['asuff'],
                       accountability_missing_elements=q['amiss'], accountable_via_qr_ids=ids('QR', q['avia']), depends_on_pd_ids=ids('PD', q['dep']), support_gap_report=q['gap'], external_ref_ids=ext_ids,
                       evidence_span=q['span'], uncertainty_ids=ids('UNC', q['unc']), hq_ids=ids('HQ', q['hq'])))

# ---------- status tallies
from collections import Counter
def profile(nas, qrs, pds=None):
    cq = Counter(byk[('QR', k)]['ep'] for k in qrs); cn = Counter(byk[('NA', k)]['ep'] for k in nas)
    def fmt(c, name):
        parts = [f"{v} {name} {k}" for k, v in sorted(c.items())]
        return '; '.join(parts) if parts else f"0 {name}"
    return fmt(cq, 'relations') + '; ' + fmt(cn, 'assignments') + '; 0 material_establishment_evidenced (not assessed); 0 exercise_evidenced (not assessed)'

# ---------- SC
SCROWS = []
sc_units = {}
for s in SC:
    us = []
    for k in s['qrs']:
        for u in st_units(byk[('QR', k)]['st']):
            if u not in us: us.append(u)
    for k in s['nas']:
        for u in st_units(byk[('NA', k)]['st']):
            if u not in us: us.append(u)
    sc_units[s['k']] = us
    arts = sorted({u.split('.')[0] for u in us}, key=lambda a: int(re.sub(r'\D', '', a)))
    SCROWS.append(dict(sc_id=ID[('SC', s['k'])], case_id=CASE, scope_label=s['scope'], pattern_rule=s['pattern'], governance_question=s['question'], member_qr_ids=ids('QR', s['qrs']), member_na_ids=ids('NA', s['nas']),
                       member_pd_ids=ids('PD', s['pds']), organizing_mechanism=s['mech'], warrant_basis=s['warrant'], units_spanned='Distinct units: ' + str(len(us)) + '; articles spanned: ' + ', '.join(arts) + '; units: ' + fulls(us),
                       boundary_statement=s['boundary'], overlap_sc_ids=ids('SC', s['overlap']), nested_in_sc_id='', competing_grouping=s['competing'], uncertainty_ids=ids('UNC', s['unc']), hq_ids=ids('HQ', s['hq']), default_status='S'))

# ---------- ARCH
ARROWS = []; arch_units = {}
for a in ARCH:
    qrs = []; nas = []
    for sk in a['sc']:
        s = byk[('SC', sk)]
        for k in s['qrs']:
            if k not in qrs: qrs.append(k)
        for k in s['nas']:
            if k not in nas: nas.append(k)
    us = list(a['i1u'])
    for sk in a['sc']:
        for u in sc_units[sk]:
            if u not in us: us.append(u)
    arch_units[a['k']] = us
    ARROWS.append(dict(arch_id=ID[('ARCH', a['k'])], case_id=CASE, member_sc_ids=ids('SC', a['sc']), i1_governing_problem_and_scale=a['i1'], i1_scope_units=fulls(a['i1u']), i1_status=a['i1s'],
                       i2_coupling_description=a['i2'], i2_coupling_kind=a['i2k'], i2_qr_ids=ids('QR', a['i2q']), i2_status=a['i2s'], i3_configurational_consequence=a['i3'], i3_bearer_and_rule=a['i3b'], i3_status=a['i3s'],
                       i4_evidence_searched=a['i4'], i4_external_dependencies=ids('EXT', a['i4e']), i4_rival_grouping=a['i4r'], i4_boundary_sensitivity=a['i4b'], i4_status=a['i4s'],
                       anticircularity_sequence_followed=a['ac'], outcome=a['outcome'], outcome_basis=a['basis'], status_profile=profile(nas, qrs), uncertainty_ids=ids('UNC', a['unc']), hq_ids=ids('HQ', a['hq'])))

# ---------- PROP
PRROWS = []
for p in PROP:
    bt = p['bid'].split(':')[0]
    supp = tokids(p['supp'])
    PRROWS.append(dict(prop_id=ID[('PROP', p['k'])], case_id=CASE, property_name=p['name'], property_family=p['fam'], bearer_type=p['bt'], bearer_id=rid(p['bid']), scale=p['scale'], value_statement=p['val'],
                       inference_rule=p['rule'], path_semantics=p['path'], aggregation_rule=p['agg'], supporting_record_ids=supp, closure_dependency=p['cdep'],
                       closure_ref=ID[('CL', p['cref'])] if p['cref'] else '', count_basis=p['count'], fallacy_check=p['fall'], rival_partition=p['rival'], status=p['status'], hq_ids=ids('HQ', p['hq'])))

# ---------- CL
CLROWS = []
for c in CL:
    CLROWS.append(dict(closure_id=ID[('CL', c['k'])], case_id=CASE, record_kind=c['kind'], claim_or_scope=c['claim'], search_description=c['search'], unresolved_ext_ids=ids('EXT', c['ext']), result=c['result'], affected_claim_ids=tokids(c['aff'])))

# ---------- UNC
UNCROWS = []
for u in UNC:
    refs = sorted(set(unc_rev.get(u['k'], [])))
    UNCROWS.append(dict(unc_id=ID[('UNC', u['k'])], case_id=CASE, record_ids=';'.join(refs), unit_ids=fulls(u['u']), uncertainty_type=u['t'], description=u['d'], treatment=u['tr'], effect_on_claims=u['ef'],
                        status='ESCALATED_TO_HQ' if u.get('hq') else 'OPEN'))

# ---------- HQ
HQROWS = []
for h in HQ:
    refs = set(hq_rev.get(h['k'], []))
    for t in h['refs']: refs.add(rid(t))
    def sk(x):
        p, n = x.split('-'); return (p, int(n))
    HQROWS.append(dict(hq_id=ID[('HQ', h['k'])], case_id=CASE, trigger_code=h['code'], record_refs=';'.join(sorted(refs, key=sk)), question=h['q'], competing_readings=h['cr'], machine_recommendation=h['rec'],
                       reason_human_required=h['why'], human_decision='', human_rationale='', decided_by='', decision_date=''))

# ---------- provenance links
LK = {}
def addlink(rec, rtype, unit, stype, claim, lim=''):
    key = (rec, unit)
    if key in LK and (LK[key]['support_type'] == 'direct' or stype == 'indirect'): return
    LK[key] = dict(record_id=rec, record_type=rtype, unit_id=full(unit), support_type=stype, evidence_level='A', claim_status_supported=claim, limitation=lim)
FORCE = ['A12.P0', 'A11.P1', 'FRM8']
for s in ST:
    for u in s['u']: addlink(ID[('ST', s['k'])], 'ST', u, 'direct', 'documented')
for p in PD:
    for u in p['units']: addlink(ID[('PD', p['k'])], 'PD', u, 'direct', 'documented', 'establishment not assessed (layer X); no instance inferred from a type')
for tag, lst in [('NA', NA), ('QR', QR)]:
    for r in lst:
        rr = ID[(tag, r['k'])]
        for u in st_units(r['st']): addlink(rr, tag, u, 'direct', r['ep'], 'inscription only; epistemic ceiling from legal text' if r['ep'] != 'documented' else 'documented only (see uncertainty/limitations)')
        if r['ep'] == 'legal_constitution_evidenced':
            for u in FORCE: addlink(rr, tag, u, 'indirect', 'legal_constitution_evidenced', 'evidences addressee, implementation period and adoption date (force and applicability for the declared temporal reference); not establishment or exercise')
for e in EXT:
    for u in st_units(e['st']): addlink(ID[('EXT', e['k'])], 'EXT', u, 'direct', 'documented', 'legal relevance only; source not checked')
    for u in e['extra_units']: addlink(ID[('EXT', e['k'])], 'EXT', u, 'indirect', 'documented', 'identification or scope support; source not checked')
for s in SC:
    for u in sc_units[s['k']]: addlink(ID[('SC', s['k'])], 'SC', u, 'indirect', 'documented', 'via member records; inherits the weakest member status')
for a in ARCH:
    for u in a['i1u']: addlink(ID[('ARCH', a['k'])], 'ARCH', u, 'direct', 'documented', 'I1 scope material')
    for k in a['i2q']:
        for u in st_units(byk[('QR', k)]['st']): addlink(ID[('ARCH', a['k'])], 'ARCH', u, 'indirect', 'documented', 'I2 coupling relation support')
for p in PROP:
    for t in p['supp']:
        for u in rec_units(t): addlink(ID[('PROP', p['k'])], 'PROP', u, 'indirect', 'documented', 'via supporting records')
    for u in (rec_units(p['bid']) if p['bid'].split(':')[0] in ('QR', 'NA') else []): addlink(ID[('PROP', p['k'])], 'PROP', u, 'indirect', 'documented', 'via bearer record')
    if p['bid'].startswith('SC:'):
        for u in sc_units[p['bid'].split(':')[1]]: addlink(ID[('PROP', p['k'])], 'PROP', u, 'indirect', 'documented', 'via bearer subconfiguration')
    if p['bid'].startswith('ARCH:'):
        for u in arch_units[p['bid'].split(':')[1]]: addlink(ID[('PROP', p['k'])], 'PROP', u, 'indirect', 'documented', 'via bearer architecture candidate')
for c in CL:
    if c['kind'] == 'COVERAGE' and c['k'] == 'cl_cov':
        for u in UNITS: addlink(ID[('CL', c['k'])], 'CL', u['unit_id'], 'indirect', 'documented', 'coverage statement over every unit')
LNK = []
def lsort(k): return (k[0].split('-')[0], int(k[0].split('-')[1]), k[1])
order = {'ST': 0, 'PD': 1, 'NA': 2, 'QR': 3, 'EXT': 4, 'SC': 5, 'ARCH': 6, 'PROP': 7, 'CL': 8}
for i, (key, v) in enumerate(sorted(LK.items(), key=lambda kv: (order[kv[1]['record_type']], int(kv[0][0].split('-')[1]), kv[0][1])), 1):
    v = dict(v); v['link_id'] = 'LNK-%05d' % i; LNK.append(v)

# ---------- trace demonstrations
seed = int(src_sha[:8], 16)
def articles(us): return {u.split('.')[0] for u in us if re.match(r'^A\d+\.', u)}
cands = {}
for s in SC: cands[ID[('SC', s['k'])]] = ('SC', s['k'], sc_units[s['k']])
for a in ARCH: cands[ID[('ARCH', a['k'])]] = ('ARCH', a['k'], arch_units[a['k']])
elig = sorted([c for c, (t, k, us) in cands.items() if len(articles(us)) >= 2])
rng = random.Random(seed)
drawn = elig[rng.randrange(len(elig))]
largest = max(cands, key=lambda c: (len(set(cands[c][2])), c))
# tie rule: most distinct units; ties broken by lowest id (documented)
mx = max(len(set(cands[c][2])) for c in cands)
largest = sorted([c for c in cands if len(set(cands[c][2])) == mx])[0]
def chain_for_sc(skey, max_span=None):
    s = byk[('SC', skey)]
    parts = []
    for tag, keys in (('QR', s['qrs']), ('NA', s['nas'])):
        for k in keys:
            r = byk[(tag, k)]
            stp = []
            for sk in r['st']:
                su = byk[('ST', sk)]
                stp.append(f"{ID[('ST', sk)]} [{fulls(su['u'])}] \"{su['span']}\"")
            parts.append(f"{ID[(tag, k)]} <- " + ' | '.join(stp))
    return ID[('SC', skey)] + ' => ' + ' ;; '.join(parts)
def vchain(c):
    t, k, us = cands[c]
    if t == 'SC': return chain_for_sc(k)
    a = byk[('ARCH', k)]
    return c + ' -> ' + ' ### '.join(chain_for_sc(sk) for sk in a['sc'])
def trace_row(tid, rule, cand_list, c, seed_i):
    txt = vchain(c)
    return dict(trace_id=tid, case_id=CASE, selection_rule=rule, seed_integer=seed_i, candidate_list=cand_list, traced_id=c, vertical_chain=txt, chain_complete='Y')
TRROWS = [trace_row('TR-01', 'SEEDED_DRAW', ';'.join(elig), drawn, str(seed)), trace_row('TR-02', 'LARGEST_SUPPORT', ';'.join(elig), largest, '')]

# ---------- summary
hq_open = len(HQ)
unres = len([e for e in EXT if e['cdep'] == 'Y'])
all_nas = [n['k'] for n in NA]; all_qrs = [q['k'] for q in QR]
counts = dict(SOURCE_UNIT_INVENTORY=len(INV), UNIT_SCREENING=len(SCR), INSTITUTIONAL_STATEMENTS=len(ST), NORMATIVE_ASSIGNMENTS=len(NA), POSITIONS_AND_DEVICES=len(PD), QUALIFIED_RELATIONS=len(QR),
              EXTERNAL_REFERENCES=len(EXT), SUBCONFIGURATIONS=len(SC), ARCHITECTURE_CANDIDATES=len(ARCH), PROPERTY_REGISTER=len(PROP), CLOSURE_REGISTER=len(CL), PROVENANCE_LINKS=len(LNK),
              UNCERTAINTY_LOG=len(UNC), HUMAN_REVIEW_QUEUE=len(HQ), TRACE_DEMONSTRATIONS=len(TRROWS))
SUM = [dict(case_id=CASE, units_total=str(len(INV)), units_screened=str(len(SCR)), record_counts='; '.join(f'{k}={v}' for k, v in counts.items()),
            instrument_level_result='INDETERMINATE', highest_level_reached='S',
            status_profile='Positions/devices: ' + str(len(PD)) + ' documented (0 material_establishment_evidenced: not assessed). ' + profile(all_nas, all_qrs) + '; external references: ' + str(len(EXT)) + ' not_checked.',
            hq_open_count=str(hq_open), unresolved_ext_count=str(unres), machine_provisional='Y',
            summary_note='Subconfigurations are warranted from stated relations; both candidate wholes are INDETERMINATE because constitutive external dependencies are unresolved (RGAM-DR-25, RGAM-DR-27); relations not grouped into any subconfiguration remain at the relation level. Machine-generated and provisional; no comparison with any other method or case.')]

# ---------- DEV
DEVROWS = []
for i, d in enumerate(DEV, 1):
    DEVROWS.append(dict(dev_id='DEV-%02d' % i, case_id=CASE, rule_id=d['rule'], description=d['desc'], reason=d['reason'], impact=d['impact'], gap_ref=d['gap']))

# ---------- run metadata (end_time filled at finalize)
FILES_READ = [
 ROOT + '/12_RGAM_CASE_EXECUTION/' + CASE + '/EXECUTOR_BRIEF.md',
 ROOT + '/12_RGAM_CASE_EXECUTION/_RECOVERY_DIR_86_361_2026-10-06/RECOVERY_STATE_NOTE.md (the one extra file allowed for the recovery run)',
 ROOT + '/11_RGAM_PROTOCOL_FREEZE/RGAM_PAIRED_EXECUTION_PROTOCOL_v1_0.md', ROOT + '/11_RGAM_PROTOCOL_FREEZE/RGAM_PAIRED_DECISION_RULES_v1_0.md', ROOT + '/11_RGAM_PROTOCOL_FREEZE/RGAM_PAIRED_DATA_DICTIONARY_v1_0.md',
 ROOT + '/11_RGAM_PROTOCOL_FREEZE/RGAM_CASE_OUTPUT_SCHEMA.md', ROOT + '/11_RGAM_PROTOCOL_FREEZE/RGAM_BLINDNESS_AND_ACCESS_POLICY.md', ROOT + '/11_RGAM_PROTOCOL_FREEZE/RGAM_EXECUTION_GAP_DECISIONS_v1_0.md',
 CAP + '/CASE_METADATA.json', CAP + '/CAPSULE_README.md', CAP + '/LEGAL_SOURCE/31986L0361_official_en.html', CAP + '/OUTPUT_TEMPLATES/CASE_RGAM_REPORT_TEMPLATE.md (the 19 CSV template headers were read by the mechanical scripts)',
 'own output directory: ' + OUT + '/ (all 19 CSV tables, the _work scripts and notes of the earlier executor, and own files written in this run)']
end_time = os.environ.get('RGAM_END_TIME', 'PENDING')
RUN = [dict(run_id='RUN-01', case_id=CASE, protocol_version='RGAM paired execution protocol v1.0', protocol_manifest_sha256='9ca016b97289b39049dc099b265c20662c1ebc05e86bc720f0fbe80e0bac5932',
            model_id='claude-sonnet-5-5 (Sonnet 5.5, as stated in the session environment)',
            model_parameters='RECOVERY RUN reusing the partial work of an earlier executor that was interrupted by an API rate limit (earlier run: start 2026-10-06T20:47:08-03:00 as recorded by that executor, last file write 2026-10-06T21:11:05-03:00; this row describes the recovery run, start/end below). Reasoning/effort: the session context displayed reasoning_effort=10 (scale not stated; not the highest setting asked for in the brief); temperature: NOT_EXPOSED; top-p: NOT_EXPOSED; seed: NOT_EXPOSED; token limits: NOT_EXPOSED (a total token budget was displayed to the executor but is not a model parameter recorded here)',
            start_time='2026-10-07T07:37:48-03:00', end_time=end_time, fresh_context_attested='Y',
            files_read=' | '.join(FILES_READ), forbidden_paths_attempted='NONE', machine_generated='Y')]

# ---------- write
os.makedirs(OUT, exist_ok=True)
tables = [('W_DECLARATION', W), ('SOURCE_UNIT_INVENTORY', INV), ('UNIT_SCREENING', SCR), ('INSTITUTIONAL_STATEMENTS', STROWS), ('NORMATIVE_ASSIGNMENTS', NAROWS), ('POSITIONS_AND_DEVICES', PDROWS),
          ('QUALIFIED_RELATIONS', QRROWS), ('EXTERNAL_REFERENCES', EXTROWS), ('SUBCONFIGURATIONS', SCROWS), ('ARCHITECTURE_CANDIDATES', ARROWS), ('PROPERTY_REGISTER', PRROWS), ('CLOSURE_REGISTER', CLROWS),
          ('PROVENANCE_LINKS', LNK), ('UNCERTAINTY_LOG', UNCROWS), ('HUMAN_REVIEW_QUEUE', HQROWS), ('TRACE_DEMONSTRATIONS', TRROWS), ('INSTRUMENT_LEVEL_SUMMARY', SUM), ('PROTOCOL_DEVIATION_LOG', DEVROWS), ('RUN_METADATA', RUN)]
for n, rows in tables: print(n, write(n, rows))
json.dump(dict(counts=counts, drawn=drawn, largest=largest, elig=elig, seed=seed, ids={f'{a}:{b}': v for (a, b), v in ID.items()}), open(os.path.dirname(os.path.abspath(__file__)) + '/build_info.json', 'w'), indent=1)
print('drawn', drawn, 'largest', largest, 'seed', seed, 'elig', elig)
for r in TRROWS: print(r['trace_id'], len(r['vertical_chain']))
