# Recovery-run independent MECHANICAL verification (supplements validate.py).
# Reads the emitted CSVs, units.json and the frozen source only. No analytical content is generated.
import csv, json, re, hashlib, random
from collections import Counter

O = 'G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/12_RGAM_CASE_EXECUTION/RGAM_O_DIR_86_361'
CAP = 'G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_O_DIR_86_361'
CASE = 'RGAM_O_DIR_86_361'


def L(n):
    return list(csv.DictReader(open(f'{O}/{n}.csv', encoding='utf-8-sig', newline='')))


def sp(s):
    return [x for x in s.split(';') if x] if s else []


UJ = json.load(open('units.json', encoding='utf-8'))
units = {CASE + '.' + u['unit_id']: u for u in UJ}
res = []
fails = 0


def chk(n, ok, d=''):
    global fails
    res.append(('PASS' if ok else 'FAIL') + ' | ' + n + ((' | ' + str(d)[:300]) if d else ''))
    if not ok:
        fails += 1


ST = L('INSTITUTIONAL_STATEMENTS'); NA = L('NORMATIVE_ASSIGNMENTS'); PD = L('POSITIONS_AND_DEVICES'); QR = L('QUALIFIED_RELATIONS'); EXT = L('EXTERNAL_REFERENCES')
SC = L('SUBCONFIGURATIONS'); AR = L('ARCHITECTURE_CANDIDATES'); PR = L('PROPERTY_REGISTER'); CL = L('CLOSURE_REGISTER'); UN = L('UNCERTAINTY_LOG'); HQ = L('HUMAN_REVIEW_QUEUE')
LK = L('PROVENANCE_LINKS'); TR = L('TRACE_DEMONSTRATIONS'); DV = L('PROTOCOL_DEVIATION_LOG'); SCR = L('UNIT_SCREENING'); INV = L('SOURCE_UNIT_INVENTORY')

# V1 strict per-unit verbatim spans
bad = []
for t, idc in ((ST, 'st_id'), (NA, 'na_id'), (QR, 'qr_id'), (PD, 'pd_id')):
    for r in t:
        if (not r['evidence_span']) or len(r['evidence_span']) > 400 or not any(r['evidence_span'] in units[u]['text'] for u in sp(r['supporting_unit_ids'])):
            bad.append(r[idc])
chk('V1 evidence span verbatim in one cited unit and <=400 chars (ST/NA/QR/PD)', not bad, bad)

# V2 reciprocity
der = {}
for r in ST:
    for d in sp(r['derived_record_ids']):
        der.setdefault(d, set()).add(r['st_id'])
bad = []
for t, idc in ((NA, 'na_id'), (QR, 'qr_id')):
    for r in t:
        if set(sp(r['statement_ids'])) != der.get(r[idc], set()):
            bad.append(r[idc])
chk('V2 NA/QR statement_ids equal the STs listing them as derived records', not bad, bad)

# V3 PD usage
used = set()
for r in NA:
    used |= {r['subject_pd_id']} | set(sp(r['depends_on_pd_ids']))
for r in QR:
    used |= {r['origin_pd_id'], r['counterpart_pd_id']} | set(sp(r['additional_party_pd_ids'])) | set(sp(r['depends_on_pd_ids']))
orph = [p['pd_id'] for p in PD if p['pd_id'] not in used]
bear = {r['subject_pd_id'] for r in NA} | {r['origin_pd_id'] for r in QR} | {r['counterpart_pd_id'] for r in QR} | {x for r in QR for x in sp(r['additional_party_pd_ids'])}
nb = [p['pd_id'] for p in PD if p['pd_id'] not in bear]
chk('V3 no orphan PD (informational: PD that are not a party/bearer of any NA/QR listed)', not orph, {'orphans': orph, 'not_party_or_bearer': nb})

# V4/V5
chk('V4 no QR prohibition; NA prohibition iff constraint_only=Y', all(r['modality'] != 'prohibition' for r in QR) and all((r['modality'] == 'prohibition') == (r['constraint_only'] == 'Y') for r in NA))
chk('V5 epistemic ceilings: NA/QR documented or legal_constitution_evidenced only; PD material establishment not_assessed',
    all(r['epistemic_status'] in ('documented', 'legal_constitution_evidenced') for r in QR + NA) and all(p['material_establishment_evidence'] == 'not_assessed' for p in PD))

# V6 derivation
bad = [r.get('qr_id') or r.get('na_id') for r in QR + NA if r['derivation'] == 'derived' and not (r['derivation_rule'] and (len(sp(r['supporting_unit_ids'])) >= 2 or 'cross-reference' in r['derivation_rule'].lower()))]
chk('V6 derived records state derivation_rule and cite >=2 units or cross-reference', not bad, bad)
chk('V6b direct records have blank derivation_rule', all(not r['derivation_rule'] for r in QR + NA if r['derivation'] == 'direct'))

# V7 S
bad = [s['sc_id'] for s in SC if not (s['warrant_basis'] and s['organizing_mechanism'] and s['pattern_rule'] and s['governance_question'] and sp(s['member_qr_ids']) and s['competing_grouping'] and s['boundary_statement'])]
chk('V7 every S has pattern rule, governance question, QR members, mechanism, warrant, boundary, competing grouping', not bad, bad)
chk('V7b every S default_status = S', all(s['default_status'] == 'S' for s in SC))

# V8 A
need = ('i1_governing_problem_and_scale', 'i1_scope_units', 'i1_status', 'i2_coupling_description', 'i2_coupling_kind', 'i2_status', 'i3_configurational_consequence', 'i3_bearer_and_rule', 'i3_status', 'i4_evidence_searched', 'i4_rival_grouping', 'i4_boundary_sensitivity', 'i4_status', 'outcome_basis')
bad = [a['arch_id'] for a in AR if not all(a[k] for k in need) or a['anticircularity_sequence_followed'] != 'Y']
chk('V8 every A states I1-I4 (all fields), rival grouping, anticircularity=Y', not bad, bad)
chk('V8b INTEGRATED only if I1-I4 all SATISFIED', all(a['outcome'] != 'INTEGRATED' or all(a[k] == 'SATISFIED' for k in ('i1_status', 'i2_status', 'i3_status', 'i4_status')) for a in AR))
chk('V9 every INTEGRATED/OVERLAPPING A queued (vacuous if none)', all(a['outcome'] not in ('INTEGRATED', 'OVERLAPPING_OR_PARTIALLY_INTEGRATED') or sp(a['hq_ids']) for a in AR), [a['outcome'] for a in AR])

# V10 status profile recompute
qrd = {r['qr_id']: r for r in QR}; nad = {r['na_id']: r for r in NA}; scd = {s['sc_id']: s for s in SC}


def fmt(cq, cn):
    return f"{cq['documented']} relations documented; {cq['legal_constitution_evidenced']} relations legal_constitution_evidenced; {cn['documented']} assignments documented; {cn['legal_constitution_evidenced']} assignments legal_constitution_evidenced"


bad = []
for a in AR:
    qs = set(); ns = set()
    for s in sp(a['member_sc_ids']):
        qs |= set(sp(scd[s]['member_qr_ids'])); ns |= set(sp(scd[s]['member_na_ids']))
    exp = fmt(Counter(qrd[q]['epistemic_status'] for q in qs), Counter(nad[n]['epistemic_status'] for n in ns))
    if exp not in a['status_profile']:
        bad.append((a['arch_id'], exp, a['status_profile'][:140]))
chk('V10 ARCH status_profile tallies recompute from member records', not bad, bad)
S = L('INSTRUMENT_LEVEL_SUMMARY')[0]
exp = fmt(Counter(r['epistemic_status'] for r in QR), Counter(r['epistemic_status'] for r in NA))
chk('V11 instrument status_profile tallies recompute', exp in S['status_profile'], S['status_profile'][:200])
cnt = {'SOURCE_UNIT_INVENTORY': INV, 'UNIT_SCREENING': SCR, 'INSTITUTIONAL_STATEMENTS': ST, 'NORMATIVE_ASSIGNMENTS': NA, 'POSITIONS_AND_DEVICES': PD, 'QUALIFIED_RELATIONS': QR, 'EXTERNAL_REFERENCES': EXT, 'SUBCONFIGURATIONS': SC,
       'ARCHITECTURE_CANDIDATES': AR, 'PROPERTY_REGISTER': PR, 'CLOSURE_REGISTER': CL, 'PROVENANCE_LINKS': LK, 'UNCERTAINTY_LOG': UN, 'HUMAN_REVIEW_QUEUE': HQ, 'TRACE_DEMONSTRATIONS': TR}
chk('V12 summary record_counts recompute', S['record_counts'] == '; '.join(f'{k}={len(v)}' for k, v in cnt.items()), S['record_counts'])
chk('V13 hq_open_count = queue length; unresolved_ext_count = EXT with constitutive_dependency Y', int(S['hq_open_count']) == len(HQ) and int(S['unresolved_ext_count']) == sum(e['constitutive_dependency'] == 'Y' for e in EXT))

# V14 escalated uncertainties are referenced by an HQ
refd = set()
for h in HQ:
    refd |= set(sp(h['record_refs']))
hqrec = {}
for t, c in ((NA, 'na_id'), (PD, 'pd_id'), (QR, 'qr_id'), (SC, 'sc_id'), (AR, 'arch_id'), (PR, 'prop_id')):
    for r in t:
        hqrec[r[c]] = bool(sp(r['hq_ids']))
bad = [u['unc_id'] for u in UN if u['status'] == 'ESCALATED_TO_HQ' and u['unc_id'] not in refd and not any(hqrec.get(x) or x in refd for x in sp(u['record_ids']))]
chk('V14 every ESCALATED_TO_HQ uncertainty is referenced by an HQ item (directly, or through an affected record that carries an hq_id or is an HQ record_ref)', not bad, bad)

allids = set()
for t, c in ((ST, 'st_id'), (NA, 'na_id'), (PD, 'pd_id'), (QR, 'qr_id'), (EXT, 'ext_id'), (SC, 'sc_id'), (AR, 'arch_id'), (PR, 'prop_id'), (CL, 'closure_id'), (UN, 'unc_id')):
    allids |= {r[c] for r in t}
hqids = {h['hq_id'] for h in HQ}
chk('V15 HQ record_refs resolve; question/competing/recommendation/reason filled; human_* blank',
    all(set(sp(h['record_refs'])) <= allids and h['question'] and h['competing_readings'] and h['machine_recommendation'] and h['reason_human_required'] and not (h['human_decision'] or h['human_rationale'] or h['decided_by'] or h['decision_date']) for h in HQ))
TRG = {'HQ-NORMTYPE', 'HQ-DEV', 'HQ-ACCOUNT', 'HQ-INTEGRATION', 'HQ-OVERLAP', 'HQ-XREF', 'HQ-DIRECTION', 'HQ-GAP', 'HQ-EXTDEP', 'HQ-OTHER'}
chk('V16 HQ trigger codes in vocabulary', all(h['trigger_code'] in TRG for h in HQ))
bad = []
for t, c in ((NA, 'na_id'), (PD, 'pd_id'), (QR, 'qr_id'), (SC, 'sc_id'), (AR, 'arch_id'), (PR, 'prop_id')):
    for r in t:
        for h in sp(r['hq_ids']):
            if h not in hqids:
                bad.append((r[c], h))
chk('V17 hq_ids resolve', not bad, bad)
chk('V18 EXT cite non-recital units', all(units[u]['structure_class'] != 'RECITAL' for e in EXT for u in sp(e['supporting_unit_ids'])))
chk('V19 every unit inventoried and screened once in source order; Yes iff statements; 93 units',
    [r['unit_id'] for r in INV] == [r['unit_id'] for r in SCR] == [CASE + '.' + u['unit_id'] for u in UJ] and all((r['governance_relevance'] == 'Yes') == bool(r['statement_ids']) for r in SCR) and len(INV) == 93)

lr = {}
for l in LK:
    lr.setdefault(l['record_id'], []).append(l)
miss = [i for i in allids if i[:2] in ('ST', 'NA', 'PD', 'QR', 'EX', 'SC', 'AR', 'PR') and i not in lr]
chk('V20 every ST/NA/PD/QR/EXT/SC/ARCH/PROP record has provenance rows', not miss, miss)
chk('V20b CL-01 links to every unit', len({l['unit_id'] for l in lr['CL-01']}) == 93)

# V21 trace selection recompute
src = open(CAP + '/LEGAL_SOURCE/31986L0361_official_en.html', 'rb').read()
seed = int(hashlib.sha256(src).hexdigest()[:8], 16)


def unitsof(rec):
    us = set()
    if rec.startswith('SC'):
        s = scd[rec]
        for q in sp(s['member_qr_ids']):
            us |= set(sp(qrd[q]['supporting_unit_ids']))
        for n in sp(s['member_na_ids']):
            us |= set(sp(nad[n]['supporting_unit_ids']))
    else:
        a = [x for x in AR if x['arch_id'] == rec][0]
        us |= set(sp(a['i1_scope_units']))
        for s in sp(a['member_sc_ids']):
            us |= unitsof(s)
    return us


def arts(us):
    return {u[len(CASE) + 1:].split('.')[0] for u in us if re.match(r'^A\d+$', u[len(CASE) + 1:].split('.')[0])}


cands = {c: unitsof(c) for c in [s['sc_id'] for s in SC] + [a['arch_id'] for a in AR]}
elig = sorted(c for c, us in cands.items() if len(arts(us)) >= 2)
drawn = elig[random.Random(seed).randrange(len(elig))]
mx = max(len(v) for v in cands.values())
largest = sorted(c for c, v in cands.items() if len(v) == mx)[0]
t1, t2 = TR[0], TR[1]
chk('V21 trace selection recomputes (seed, eligible list, drawn, largest)', t1['seed_integer'] == str(seed) and t1['candidate_list'] == ';'.join(elig) and t1['traced_id'] == drawn and t2['traced_id'] == largest, (seed, elig, drawn, largest))
bad = []
for t in TR:
    ids = set(re.findall(r'\b(?:QR|NA|ST)-\d+\b', t['vertical_chain']))
    tid = t['traced_id']
    scs = [tid] if tid.startswith('SC') else sp([a for a in AR if a['arch_id'] == tid][0]['member_sc_ids'])
    nd = set()
    for s in scs:
        nd |= set(sp(scd[s]['member_qr_ids'])) | set(sp(scd[s]['member_na_ids']))
    if not nd <= ids:
        bad.append((t['trace_id'], sorted(nd - ids)))
chk('V22 trace chains include every member QR/NA of the traced S/ARCH', not bad, bad)
chk('V23 EXT fixed fields', all(e['source_verification_status'] == 'not_checked' and e['boundary_status'] == 'outside_corpus_not_expanded' for e in EXT))
gaps = {d['gap_ref'] for d in DV}
chk('V24 deviation log has gap_ref for GAP-01,03,04,05,06,07 (GAP-02 not applicable: no provision amending another act)', {'GAP-01', 'GAP-03', 'GAP-04', 'GAP-05', 'GAP-06', 'GAP-07'} <= gaps, sorted(gaps))

alltxt = ''
for n in ['SOURCE_UNIT_INVENTORY', 'UNIT_SCREENING', 'INSTITUTIONAL_STATEMENTS', 'NORMATIVE_ASSIGNMENTS', 'POSITIONS_AND_DEVICES', 'QUALIFIED_RELATIONS', 'EXTERNAL_REFERENCES', 'SUBCONFIGURATIONS', 'ARCHITECTURE_CANDIDATES', 'PROPERTY_REGISTER', 'CLOSURE_REGISTER',
          'UNCERTAINTY_LOG', 'HUMAN_REVIEW_QUEUE', 'TRACE_DEMONSTRATIONS', 'INSTRUMENT_LEVEL_SUMMARY', 'PROTOCOL_DEVIATION_LOG', 'W_DECLARATION', 'RUN_METADATA']:
    alltxt += open(f'{O}/{n}.csv', encoding='utf-8-sig').read()
lk = re.findall(r'\ba\d+_[a-z_0-9]+|\bQR a\d|\bacct_suff\b|\bcept_nonaddr\b', alltxt)
chk('V25 no leaked internal authoring keys in output text', not lk, lk[:5])
chk('V26 no numeric score/ranking/threshold in output text', not re.search(r'\b(score|ranking|threshold)\b\s*[:=]?\s*\d', alltxt, re.I))
bad = [p['prop_id'] for p in PR if p['closure_dependency'] == 'Y' and not p['closure_ref']]
chk('V27 PROP closure_dependency=Y has closure_ref', not bad, bad)
chk('V28 PROP bearers resolve; status vocabulary; fallacy_check=Y', all(p['bearer_id'] in allids and p['status'] in ('asserted', 'undetermined', 'not_attributable') and p['fallacy_check'] == 'Y' for p in PR))
chk('V29 closure result vocabulary', all(c['result'] in ('ASSERTED_WITHIN_DECLARED_CORPUS', 'UNDETERMINED') for c in CL))
print('\n'.join(res))
print('FAILS:', fails)
open('verify2_output.txt', 'w', encoding='utf-8').write('\n'.join(res) + '\nFAILS: ' + str(fails) + '\n')
