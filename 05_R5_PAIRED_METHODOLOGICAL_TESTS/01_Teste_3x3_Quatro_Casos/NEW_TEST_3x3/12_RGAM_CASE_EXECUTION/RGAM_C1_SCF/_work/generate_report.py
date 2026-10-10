# MECHANICAL report generation: composes CASE_RGAM_REPORT.md from the emitted tables (no new analysis)
import csv, os, io, json, sys, re
from collections import Counter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import reg
OUT = os.path.dirname(reg.W)


def rows(n):
    return list(csv.DictReader(io.StringIO(open(os.path.join(OUT, n + '.csv'), 'rb').read().decode('utf-8-sig'), newline='')))


def split(s):
    return [x for x in s.split(';') if x]


T = {n: rows(n) for n in ['W_DECLARATION', 'SOURCE_UNIT_INVENTORY', 'UNIT_SCREENING', 'INSTITUTIONAL_STATEMENTS', 'NORMATIVE_ASSIGNMENTS',
                          'POSITIONS_AND_DEVICES', 'QUALIFIED_RELATIONS', 'EXTERNAL_REFERENCES', 'SUBCONFIGURATIONS', 'ARCHITECTURE_CANDIDATES',
                          'PROPERTY_REGISTER', 'CLOSURE_REGISTER', 'PROVENANCE_LINKS', 'UNCERTAINTY_LOG', 'HUMAN_REVIEW_QUEUE',
                          'TRACE_DEMONSTRATIONS', 'INSTRUMENT_LEVEL_SUMMARY', 'PROTOCOL_DEVIATION_LOG', 'RUN_METADATA']}
chk = json.load(open(os.path.join(reg.W, 'check_result.json')))
w = T['W_DECLARATION'][0]
cls = Counter(r['structure_class'] for r in T['SOURCE_UNIT_INVENTORY'])
scr = Counter(r['governance_relevance'] for r in T['UNIT_SCREENING'])
summ = T['INSTRUMENT_LEVEL_SUMMARY'][0]
md = []
A = md.append
A('# CASE_RGAM_REPORT — RGAM_C1_SCF (machine-generated and provisional)\n')
A('Case: Regulation (EU) 2023/955 (Social Climate Fund), CELEX 32023R0955. Method: RGAM paired execution protocol v1.0 (phases P0-P9). All records are machine-generated and provisional; no comparison with any other method or case is made.\n')
A('## 1. W declaration and coverage\n')
A(f"- **Instrument:** {w['instrument_title']}")
A(f"- **Jurisdiction / type / version:** {w['jurisdiction']} / {w['instrument_type']} / {w['version_type']}")
A(f"- **Source file:** `{w['source_file']}`; SHA-256 verified `{w['source_sha256']}`; expected `{w['expected_sha256']}`; hash match: **{w['hash_match']}** (RGAM_CASE_BLOCKED not triggered).")
A(f"- **Domain (from title and object clause only):** {w['domain_declaration']}")
A(f"- **Temporal reference:** {w['temporal_reference']}")
A(f"- **Inclusion rule:** {w['inclusion_rule']}")
A(f"- **Declared exclusions:** {w['exclusions']}")
A(f"- **Structure check:** {w['structure_check']} (articles parsed {w['article_count_parsed']}, annexes parsed {w['annex_count_parsed']}, recitals parsed {w['recital_count_parsed']}).")
A(f"- **Closure scope:** {w['closure_scope_statement']}")
A(f"- **Coverage procedure:** a mechanical parse enumerated {len(T['SOURCE_UNIT_INVENTORY'])} units in source order (" + ', '.join(f'{k} {v}' for k, v in sorted(cls.items())) + f"); every unit was read and screened (units screened = units inventoried = {len(T['UNIT_SCREENING'])}; governance relevance Yes {scr['Yes']}, No {scr['No']}, Uncertain {scr['Uncertain']}). A mechanical check confirmed that every text node of the source file is contained in a unit. Recitals, headings, formal elements and footnotes are inventoried and screened but never create records on their own (RGAM-DR-07, DR-06).\n")
A('## 2. Record counts by table (evidence descriptors only; no table defines a score, index or ranking)\n')
A('| Table | Rows |\n|---|---:|')
for n in ['W_DECLARATION', 'SOURCE_UNIT_INVENTORY', 'UNIT_SCREENING', 'INSTITUTIONAL_STATEMENTS', 'NORMATIVE_ASSIGNMENTS', 'POSITIONS_AND_DEVICES',
          'QUALIFIED_RELATIONS', 'EXTERNAL_REFERENCES', 'SUBCONFIGURATIONS', 'ARCHITECTURE_CANDIDATES', 'PROPERTY_REGISTER', 'CLOSURE_REGISTER',
          'PROVENANCE_LINKS', 'UNCERTAINTY_LOG', 'HUMAN_REVIEW_QUEUE', 'TRACE_DEMONSTRATIONS', 'INSTRUMENT_LEVEL_SUMMARY', 'PROTOCOL_DEVIATION_LOG', 'RUN_METADATA']:
    A(f'| {n} | {len(T[n])} |')
qr = T['QUALIFIED_RELATIONS']
A('')
A('Descriptors: relations by type: ' + ', '.join(f'{k} {v}' for k, v in sorted(Counter(r['relation_type'] for r in qr).items())) + '; by accountability class: ' + ', '.join(f'{k} {v}' for k, v in sorted(Counter(r['accountability_class'] for r in qr).items())) + '. Assignments by modality: ' + ', '.join(f'{k} {v}' for k, v in sorted(Counter(r['modality'] for r in T['NORMATIVE_ASSIGNMENTS']).items())) + '. Positions/devices: ' + ', '.join(f'{k} {v}' for k, v in sorted(Counter(r['kind'] for r in T['POSITIONS_AND_DEVICES']).items())) + '.\n')
A('## 3. Subconfigurations and warrants\n')
A('Every candidate grouping starts as an S and is built from relations, never from chapters or vocabulary (RGAM-DR-23). Seven subconfigurations satisfy a stated pattern rule through explicit legal coupling.\n')
for s in T['SUBCONFIGURATIONS']:
    A(f"### {s['sc_id']} — {s['scope_label']}")
    A(f"- **Governance question:** {s['governance_question']}")
    A(f"- **Pattern rule:** {s['pattern_rule']}")
    A(f"- **Members:** {len(split(s['member_qr_ids']))} relations ({s['member_qr_ids']}); {len(split(s['member_na_ids']))} assignments; {len(split(s['member_pd_ids']))} positions/devices; {len(split(s['units_spanned']))} distinct supporting units.")
    A(f"- **Organizing mechanism:** {s['organizing_mechanism']}")
    A(f"- **Warrant basis:** {s['warrant_basis']}")
    A(f"- **Boundary:** {s['boundary_statement']}")
    A(f"- **Nested in / overlaps:** {s['nested_in_sc_id'] or '-'} / {s['overlap_sc_ids'] or '-'}")
    A(f"- **Competing grouping:** {s['competing_grouping']}\n")
A('Relations deliberately left ungrouped (stopping rule; a single relation or thematic proximity without stated legal coupling is not a subconfiguration): ' +
  ', '.join(f"{r['qr_id']}" for r in qr if r['relation_type'] and r['qr_id'] not in ';'.join(s['member_qr_ids'] for s in T['SUBCONFIGURATIONS']).split(';')) + ' (see closure record on ungrouped relations).\n')
A('## 4. Candidate architectures: I1-I4, rival groupings, outcomes\n')
A('Each candidate follows the anti-circularity sequence (question, independent coupling, consequence, rivals and boundary). No score or threshold is used; every INTEGRATED or OVERLAPPING outcome is queued because the I2/I3 thresholds are unvalidated.\n')
for a in T['ARCHITECTURE_CANDIDATES']:
    A(f"### {a['arch_id']} — outcome **{a['outcome']}** (members {a['member_sc_ids']})")
    A(f"- **I1 ({a['i1_status']}):** {a['i1_governing_problem_and_scale']} Scope units: {a['i1_scope_units']}")
    A(f"- **I2 ({a['i2_status']}; kind {a['i2_coupling_kind']}):** {a['i2_coupling_description']} Relations: {a['i2_qr_ids']}")
    A(f"- **I3 ({a['i3_status']}):** {a['i3_configurational_consequence']} {a['i3_bearer_and_rule']}")
    A(f"- **I4 ({a['i4_status']}):** searched: {a['i4_evidence_searched']} External dependencies: {a['i4_external_dependencies'] or 'none'}. Rival grouping: {re.sub(r'^Rival groupings?: ', '', a['i4_rival_grouping'])} Boundary sensitivity: {a['i4_boundary_sensitivity']}")
    A(f"- **Outcome basis:** {a['outcome_basis']}")
    A(f"- **Status profile:** {a['status_profile']}")
    A(f"- **Queue:** {a['hq_ids']}\n")
A(f"**Instrument-level result:** `{summ['instrument_level_result']}`; highest level reached: {summ['highest_level_reached']}. This is a profile of candidate outcomes, not one label of the instrument: {summ['summary_note']}\n")
A('Traceability demonstrations (fixed selection rule): TR-01 seeded draw (seed ' + str(T['TRACE_DEMONSTRATIONS'][0]['seed_integer']) + ') selected ' + T['TRACE_DEMONSTRATIONS'][0]['traced_id'] + '; TR-02 largest support selected ' + T['TRACE_DEMONSTRATIONS'][1]['traced_id'] + '. Chains are in TRACE_DEMONSTRATIONS.csv and resolve to units and verbatim spans.\n')
A('## 5. Property register summary (scale, bearer, aggregation)\n')
A('Scale, bearer and aggregation are stated before generalisation; values are reported per subconfiguration before any architecture-level summary; no scalar score, composite or graph index is computed. Absence-dependent properties carry a closure reference; where the closure test is undetermined the property is undetermined.\n')
A('| Property | Name | Bearer type | Scale | Status | Closure |\n|---|---|---|---|---|---|')
for p in T['PROPERTY_REGISTER']:
    A(f"| {p['prop_id']} | {p['property_name']} | {p['bearer_type']} ({p['bearer_id']}) | {p['scale']} | {p['status']} | {p['closure_ref'] or '-'} |")
A('')
A('Fallacy checks (atomistic, ecological, premature aggregation) are recorded per row; the families F1-F5 are an organising proposal whose allocation is not stated in the allowed sources (see section 9).\n')
A('## 6. Status profile\n')
A(f"{summ['status_profile']}.\n")
A('Material establishment and exercise are not collected from legal text and are `not_assessed`; relations never carry material_establishment_evidenced. `legal_constitution_evidenced` is used only for direct records in force whose constitution does not rest on an unresolved constitutive external reference (deviation log, status ceiling).\n')
A('## 7. Closure and external-reference limitations\n')
A('| Closure | Kind | Result | Affects |\n|---|---|---|---|')
for c in T['CLOSURE_REGISTER']:
    A(f"| {c['closure_id']} | {c['record_kind']} | {c['result']} | {c['affected_claim_ids']} |")
A('')
ext = T['EXTERNAL_REFERENCES']
A(f"{len(ext)} external references are recorded (all `not_checked`, `outside_corpus_not_expanded`); {sum(1 for e in ext if e['constitutive_dependency'] == 'Y')} carry a constitutive dependency (funding revenue, financial rules, shared-management regulation, reporting vehicle, control rights, discharge, definitions). No relation contained in an external source enters any architecture, and no external source was retrieved. Absence-dependent claims are limited to the search of W; silence is neither permission nor prohibition.\n")
A('Constitutive dependencies: ' + '; '.join(f"{e['ext_id']} ({e['referenced_legal_source'][:70]})" for e in ext if e['constitutive_dependency'] == 'Y') + '.\n')
A('## 8. Open human-review items\n')
A('All human decision columns are blank; no adjudication is simulated.\n')
A('| HQ | Trigger | Records | Machine recommendation |\n|---|---|---|---|')
for h in T['HUMAN_REVIEW_QUEUE']:
    A(f"| {h['hq_id']} | {h['trigger_code']} | {h['record_refs']} | {h['machine_recommendation']} |")
A('')
A('## 9. Deviations and gaps\n')
A('| DEV | Rule | Gap | Description |\n|---|---|---|---|')
for d in T['PROTOCOL_DEVIATION_LOG']:
    A(f"| {d['dev_id']} | {d['rule_id']} | {d['gap_ref'] or '-'} | {d['description']} |")
A('')
uc = Counter(u['uncertainty_type'] for u in T['UNCERTAINTY_LOG'])
A('Uncertainty log by type: ' + ', '.join(f'{k} {v}' for k, v in sorted(uc.items())) + f"; {sum(1 for u in T['UNCERTAINTY_LOG'] if u['status'] == 'ESCALATED_TO_HQ')} escalated to the queue, the others open.\n")
A('## 10. Statement of provisional status (no comparison with any other method or case)\n')
A('All outputs are machine-generated and provisional; repetition by the same model is not inter-coder reliability. Human adjudication (MS section 8.4 item 8) is a separate subsequent stage and is not performed. The frozen method was not altered by case analysis.\n')
A('### P9 integrity self-checks (data dictionary section 4 and schema section 4)\n')
A('| Check | Result |\n|---|---|')
labels = {'rule1': 'Rule 1: every unit_id exists in the inventory; units screened = units inventoried',
          'rule2': 'Rule 2: every NA, PD, QR, EXT cites at least one statement and every statement cites at least one unit; no recital-only derivations',
          'rule3': 'Rule 3: every id field resolves; accountable_via pointers resolve to accountability relations',
          'rule4': 'Rule 4: every QR has both parties, non-prohibition modality and no material_establishment_evidenced',
          'rule5': 'Rule 5: every NA/QR/SC/ARCH/PROP has provenance links; derived records state a rule and cite two units or a cross-reference',
          'rule6': 'Rule 6: every INTEGRATED/OVERLAPPING outcome has an HQ item; INTEGRATED only with I1-I4 SATISFIED',
          'rule7': 'Rule 7: closure_dependency Y has a closure_ref; closure UNDETERMINED forces undetermined',
          'rule8': 'Rule 8: every EXT not_checked and outside_corpus_not_expanded',
          'rule9': 'Rule 9: human_* columns of the queue are blank',
          'rule10': 'Rule 10: trace chains resolve to existing ids, units and verbatim spans'}
for k, v in chk['res'].items():
    A(f'| {labels[k]} | {v} |')
A(f"| Total failures reported by the checker | {len(chk['fails'])} |")
open(os.path.join(OUT, 'CASE_RGAM_REPORT.md'), 'w', encoding='utf-8').write('\n'.join(md) + '\n')
print('report written', len('\n'.join(md)))
