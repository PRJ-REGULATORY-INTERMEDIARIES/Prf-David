from stats import *
D=gather()
F=C+'/FAMILY'
REG=json.load(open(F+'/_work/register_rows.json'))
Q=json.load(open(F+'/_work/queue_rows.json'))
SHORT={'RGAM_C1_SCF':'C1_SCF','RGAM_C2_CBAM':'C2_CBAM','RGAM_AI_AI_ACT':'AI_AI_ACT','RGAM_O_DIR_86_361':'O_DIR_86_361'}
H=[SHORT[c] for c in cases]
def tbl(first,rows,total=True,hdrs=None):
    hdrs=hdrs or H
    out='| '+first+' | '+' | '.join(hdrs)+(' | Total |' if total else ' |')+'\n|---|'+('---:|' if total else ':---|')*(len(hdrs)+(1 if total else 0))+'\n'
    for r in rows:
        lab,vals=r[0],r[1:]
        cells=[str(v) for v in vals]
        if total:
            try: cells.append(str(sum(int(v) for v in vals)))
            except Exception: cells.append('n/a')
        out+='| '+lab+' | '+' | '.join(cells)+' |\n'
    return out+'\n'
def cnt(t): return [len(D[c]['T'][t]) for c in cases]
def distr(t,col,vals=None):
    ctr=[Counter(r[col] for r in D[c]['T'][t]) for c in cases]
    keys=vals or sorted(set(k for x in ctr for k in x),key=lambda k:(-sum(x.get(k,0) for x in ctr),k))
    return [[k if k!='' else '(blank)']+[x.get(k,0) for x in ctr] for k in keys]
S=[]
A=S.append
A('# RGAM four-case family — cross-case descriptive summary\n')
A('**Status:** descriptive only; machine-assembled from the four frozen case directories; every number below is a count taken from, or recomputed from, the frozen case tables. Counts are descriptors of what each case recorded; they are not scores, rates, quality indicators or rankings, and the four cases have different source sizes. "Total" columns are arithmetic sums over the four cases and carry no further meaning. This file reports what each frozen case recorded; it does not interpret what any provision of any instrument "means", does not adjudicate any human-review item, and contains no comparison with any other method.\n')
A('Case labels used below: C1_SCF = RGAM_C1_SCF (Regulation (EU) 2023/955); C2_CBAM = RGAM_C2_CBAM (Regulation (EU) 2023/956); AI_AI_ACT = RGAM_AI_AI_ACT (Regulation (EU) 2024/1689); O_DIR_86_361 = RGAM_O_DIR_86_361 (Directive 86/361/EEC).\n')
# 1
A('## 1. Cases, frozen status and verified inputs\n')
A('| Case | Instrument | Case gate (as recorded) | Source hash vs capsule | Contamination status (case access log) | Case manifest (recomputed) |\n|---|---|---|---|---|---|')
for r in REG:
    A(f"| {r['capsule_id']} | {r['instrument']} (CELEX {r['celex']}) | {r['case_gate']} | {r['source_hash_status']} | {r['contamination_status_case_access_log']} | {r['case_freeze_manifest_status']} (`{r['case_freeze_manifest_sha256_recomputed'][:16]}...`) |")
A('')
# 2
A('## 2. Counts by RGAM stratum (per case and total)\n')
A('Stratum mapping, as instructed for this family stage (from `RGAM_CASE_OUTPUT_SCHEMA.md` section 2): **E** = SOURCE_UNIT_INVENTORY + INSTITUTIONAL_STATEMENTS; **P** = NORMATIVE_ASSIGNMENTS + POSITIONS_AND_DEVICES; **R** = QUALIFIED_RELATIONS + EXTERNAL_REFERENCES; **S** = SUBCONFIGURATIONS; **A** = ARCHITECTURE_CANDIDATES. (The schema also maps UNIT_SCREENING to E and TRACE_DEMONSTRATIONS to A; they are given in the per-table counts below, not added to the stratum counts.)\n')
rowsS=[]
for k,tl in STRATA.items():
    for t in tl: rowsS.append([f'{k} - {t}']+cnt(t))
    if len(tl)>1: rowsS.append([f'**{k} subtotal**']+[sum(len(D[c]['T'][t]) for t in tl) for c in cases])
    else: pass
A(tbl('Stratum / table',rowsS))
A('Records per stratum, total over the five strata (E+P+R+S+A) per case: '+'; '.join(f"{SHORT[r['capsule_id']]} = {r['stratum_total_E_P_R_S_A']}" for r in REG)+'.\n')
A('### 2.1 Rows in all 19 frozen tables\n')
A(tbl('Table',[[t]+cnt(t) for t in tables]))
A('Rows are data rows (header excluded). The `record_counts` text written inside each case\'s own INSTRUMENT_LEVEL_SUMMARY lists a different subset of tables per case (for example C2_CBAM\'s omits PROVENANCE_LINKS, TRACE_DEMONSTRATIONS and PROTOCOL_DEVIATION_LOG); every number it does list equals the recomputed row count.\n')
A('### 2.2 Source-unit structure and screening\n')
A(tbl('Structure class (SOURCE_UNIT_INVENTORY)',distr('SOURCE_UNIT_INVENTORY','structure_class')))
A(tbl('governance_relevance (UNIT_SCREENING)',distr('UNIT_SCREENING','governance_relevance')))
A('In every case units screened = units inventoried (706, 558, 1553, 93).\n')
# 3 records
A('## 3. Records by type (as coded by each case)\n')
A(tbl('POSITIONS_AND_DEVICES `kind` / `type_or_instance`',[[k]+[sum(1 for r in D[c]['T']['POSITIONS_AND_DEVICES'] if (r['kind']+' / '+r['type_or_instance'])==k) for c in cases] for k in ['POSITION / TYPE','POSITION / INSTANCE','DEVICE / TYPE','DEVICE / INSTANCE']]))
A(tbl('NORMATIVE_ASSIGNMENTS `norm_type`',distr('NORMATIVE_ASSIGNMENTS','norm_type',['N0','N1','N2','N3','N4','COMPOUND','AMBIGUOUS'])))
A(tbl('NORMATIVE_ASSIGNMENTS `modality`',distr('NORMATIVE_ASSIGNMENTS','modality')))
A(tbl('QUALIFIED_RELATIONS `relation_type`',distr('QUALIFIED_RELATIONS','relation_type')))
A(tbl('QUALIFIED_RELATIONS `modality`',distr('QUALIFIED_RELATIONS','modality')))
accl=[[k]+[sum(1 for r in D[c]['T']['QUALIFIED_RELATIONS'] if (r['accountability_class']+' / '+r['accountability_sufficiency'])==k) for c in cases] for k in sorted(set(r['accountability_class']+' / '+r['accountability_sufficiency'] for c in cases for r in D[c]['T']['QUALIFIED_RELATIONS']))]
A(tbl('QUALIFIED_RELATIONS `accountability_class` / `accountability_sufficiency`',accl))
A(tbl('Derivation (NA + QR)',[[k]+[sum(1 for t in ['NORMATIVE_ASSIGNMENTS','QUALIFIED_RELATIONS'] for r in D[c]['T'][t] if r['derivation']==k) for c in cases] for k in ['direct','derived']]))
fv=lambda f:[sum(1 for t in ['NORMATIVE_ASSIGNMENTS','QUALIFIED_RELATIONS'] for r in D[c]['T'][t] if f(r['function'])) for c in cases]
A(tbl('Function field use (NA + QR)',[['flagged residual tags (`*`)']+fv(lambda x:x.endswith('*')),['`FUNCTION_VOCABULARY_UNRESOLVED`']+fv(lambda x:x=='FUNCTION_VOCABULARY_UNRESOLVED'),['other documented FUNCTION values']+fv(lambda x:not x.endswith('*') and x!='FUNCTION_VOCABULARY_UNRESOLVED')]))
A(tbl('Function field: `FUNCTION_VOCABULARY_UNRESOLVED` by table',[[t]+[sum(1 for r in D[c]['T'][t] if r['function']=='FUNCTION_VOCABULARY_UNRESOLVED') for c in cases] for t in ['NORMATIVE_ASSIGNMENTS','QUALIFIED_RELATIONS']]))
# 4 architecture
A('## 4. Architecture candidates: outcomes, I1-I4 statuses, instrument-level result, stopping level\n')
A('### 4.1 Candidate outcome categories (ARCHITECTURE_CANDIDATES.outcome)\n')
AO=['INTEGRATED','DISTINGUISHABLE','OVERLAPPING_OR_PARTIALLY_INTEGRATED','INDETERMINATE']
A(tbl('Outcome',[[o]+[sum(1 for r in D[c]['T']['ARCHITECTURE_CANDIDATES'] if r['outcome']==o) for c in cases] for o in AO]+[['**candidates total**']+cnt('ARCHITECTURE_CANDIDATES')]))
A('Per-candidate listing as recorded (member subconfigurations; I1, I2, I3, I4 statuses; outcome):\n')
for c in cases:
    A(f'- **{SHORT[c]}**: '+'; '.join(f"{r['arch_id']} [{r['member_sc_ids'].replace(';',',')}] I1={r['i1_status']}, I2={r['i2_status']}, I3={r['i3_status']}, I4={r['i4_status']} -> {r['outcome']}" for r in D[c]['T']['ARCHITECTURE_CANDIDATES'])+'.')
A('')
for i in ['i1','i2','i3','i4']:
    A(tbl(f'{i.upper()} status',[[s]+[sum(1 for r in D[c]['T']['ARCHITECTURE_CANDIDATES'] if r[i+'_status']==s) for c in cases] for s in ['SATISFIED','NOT_SATISFIED','INDETERMINATE']]))
A('### 4.2 Instrument-level result and highest level reached (as recorded in INSTRUMENT_LEVEL_SUMMARY)\n')
A('| Case | instrument_level_result | highest_level_reached (stopping level) |\n|---|---|---|')
for r in REG: A(f"| {SHORT[r['capsule_id']]} | {r['instrument_level_result_token']} | {r['highest_level_reached_stopping_level']} |")
A('\nResult tokens used across the four cases: '+', '.join(sorted(set(r['instrument_level_result_token'] for r in REG)))+'. Tokens available in the dictionary but not recorded by any case: '+', '.join(t for t in ['NO_ARCHITECTURE_WARRANTED','ONE_ARCHITECTURE','SEVERAL_DISTINGUISHABLE','OVERLAPPING_OR_PARTIALLY_INTEGRATED','INDETERMINATE'] if t not in set(r['instrument_level_result_token'] for r in REG))+'. Per the frozen dictionary the instrument-level entry is a profile of candidate outcomes, not a single label or score. Case-recorded stopping rationale: C1_SCF, C2_CBAM and AI_AI_ACT record level A as the highest level reached while recording INDETERMINATE candidates (and, in AI_AI_ACT, NOT_SATISFIED I3 for two candidates); O_DIR_86_361 records level S, with both candidates INDETERMINATE (its DEV-11 and HQ-016 record the reading of RGAM-DR-25 that produced this).\n')
A('### 4.3 Subconfigurations, couplings, properties and closure\n')
A(tbl('Subconfigurations (SC) recorded',[['rows']+cnt('SUBCONFIGURATIONS')]))
A(tbl('I2 coupling kind (ARCHITECTURE_CANDIDATES.i2_coupling_kind, as written; some cases record several kinds in one cell)',distr('ARCHITECTURE_CANDIDATES','i2_coupling_kind')))
A(tbl('PROPERTY_REGISTER `status`',distr('PROPERTY_REGISTER','status',['asserted','undetermined','not_attributable'])))
A(tbl('PROPERTY_REGISTER `bearer_type`',distr('PROPERTY_REGISTER','bearer_type')))
A(tbl('PROPERTY_REGISTER `property_family` (blank = not assigned)',distr('PROPERTY_REGISTER','property_family')))
A(tbl('CLOSURE_REGISTER `record_kind` / `result`',[[k]+[sum(1 for r in D[c]['T']['CLOSURE_REGISTER'] if (r['record_kind']+' / '+r['result'])==k) for c in cases] for k in ['COVERAGE / ASSERTED_WITHIN_DECLARED_CORPUS','COVERAGE / UNDETERMINED','ABSENCE_CLAIM / ASSERTED_WITHIN_DECLARED_CORPUS','ABSENCE_CLAIM / UNDETERMINED']]))
A('TRACE_DEMONSTRATIONS: each case recorded two rows (one SEEDED_DRAW, one LARGEST_SUPPORT), `chain_complete = Y` in all eight rows. Traced ids: '+'; '.join(f"{SHORT[c]} {', '.join(r['selection_rule']+'->'+r['traced_id'] for r in D[c]['T']['TRACE_DEMONSTRATIONS'])}" for c in cases)+'.\n')
# 5 status
A('## 5. Status profiles\n')
A('### 5.1 Recomputed from the tables\n')
A(tbl('Epistemic status',[[f'{lab} - {st}']+[sum(1 for r in D[c]['T'][t] if r['epistemic_status']==st) for c in cases] for lab,t in [('QR','QUALIFIED_RELATIONS'),('NA','NORMATIVE_ASSIGNMENTS'),('PD','POSITIONS_AND_DEVICES')] for st in ['legal_constitution_evidenced','documented','material_establishment_evidenced','exercise_evidenced']]))
A(tbl('Legal status of norm (QR + NA)',[[k]+[sum(1 for t in ['QUALIFIED_RELATIONS','NORMATIVE_ASSIGNMENTS'] for r in D[c]['T'][t] if r['legal_status_of_norm']==k) for c in cases] for k in ['in_force','not_yet_applicable','suspended','expired_or_repealed','conditional_on_further_act']]))
A('The temporal reference declared in each W_DECLARATION differs by case (C1_SCF: reference date 30 June 2024 with the 2026-2032 Fund interval; C2_CBAM: point reference 2026-01-01; AI_AI_ACT: reference point 2 August 2026; O_DIR_86_361: the interval from adoption on 1986-07-24 to the repeal indicated in the neutral metadata).\n')
A('### 5.2 As recorded by each case (INSTRUMENT_LEVEL_SUMMARY.status_profile, verbatim)\n')
for r in REG: A(f"- **{SHORT[r['capsule_id']]}**: {r['status_profile_as_recorded']}")
A('')
# 6 EXT
A('## 6. External references and unresolved constitutive dependencies\n')
A(tbl('EXTERNAL_REFERENCES rows',[['rows']+cnt('EXTERNAL_REFERENCES')]))
A(tbl('`constitutive_dependency`',distr('EXTERNAL_REFERENCES','constitutive_dependency',['Y','N'])))
A(tbl('`source_kind`',distr('EXTERNAL_REFERENCES','source_kind')))
A(tbl('`reference_role` (first token)',[[k]+[sum(1 for r in D[c]['T']['EXTERNAL_REFERENCES'] if r['reference_role'].split(' (')[0]==k) for c in cases] for k in sorted(set(r['reference_role'].split(' (')[0] for c in cases for r in D[c]['T']['EXTERNAL_REFERENCES']))]))
A('All EXTERNAL_REFERENCES rows in all four cases carry `source_verification_status = not_checked` and `boundary_status = outside_corpus_not_expanded`. `unresolved_ext_count` recorded in each INSTRUMENT_LEVEL_SUMMARY equals the recomputed number of rows with `constitutive_dependency = Y` (13, 17, 39, 4; total 73).\n')
# 7 uncertainty
A('## 7. Uncertainty log: types and distribution\n')
A(tbl('`uncertainty_type`',distr('UNCERTAINTY_LOG','uncertainty_type')))
A(tbl('`status`',distr('UNCERTAINTY_LOG','status',['OPEN','ESCALATED_TO_HQ'])))
A('Uncertainty types in the frozen dictionary vocabulary that appear in no case: '+(', '.join(t for t in ['SOURCE_AMBIGUITY','DRAFTING_CUE','DIRECTION','DEV_THRESHOLD','ACCOUNTABILITY_SUFFICIENCY','COUPLING_THRESHOLD','EXTERNAL_DEPENDENCY','CLOSURE','PROTOCOL_GAP','OTHER'] if not any(r['uncertainty_type']==t for c in cases for r in D[c]['T']['UNCERTAINTY_LOG'])) or 'none')+'. Types absent in individual cases can be read from the table above (zero cells).\n')
# 8 HQ
A('## 8. Human-review queue: volume, trigger distribution, recurring categories\n')
A(tbl('HUMAN_REVIEW_QUEUE items',[['rows']+cnt('HUMAN_REVIEW_QUEUE')]))
trg=['HQ-NORMTYPE','HQ-DEV','HQ-ACCOUNT','HQ-INTEGRATION','HQ-OVERLAP','HQ-XREF','HQ-DIRECTION','HQ-GAP','HQ-EXTDEP','HQ-OTHER']
A(tbl('`trigger_code`',[[t]+[sum(1 for q in Q if q['case_id']==c and q['trigger_category']==t) for c in cases] for t in trg]))
labs=sorted(set(q['recurring_category_label'] for q in Q),key=lambda l:(-sum(1 for q in Q if q['recurring_category_label']==l),l))
A(tbl('`recurring_category_label` (descriptive label assigned by the family assembler to items asking the same type of question; not a merge)',[[l]+[sum(1 for q in Q if q['case_id']==c and q['recurring_category_label']==l) for c in cases] for l in labs]))
A('Open HQ count recorded in each INSTRUMENT_LEVEL_SUMMARY equals the number of queue rows (19, 16, 35, 19). No item has been adjudicated; `human_decision`, `human_rationale`, `decided_by` and `decision_date` are blank in every row of the case queues and of the combined family queue. The combined queue preserves every case-level item separately (see `RGAM_FAMILY_HUMAN_REVIEW_QUEUE.csv`).\n')
# 9 methodological issues
A('## 9. Recurring methodological issues and deviation patterns (as recorded in each PROTOCOL_DEVIATION_LOG)\n')
A('### 9.1 Execution-addendum gaps GAP-01 to GAP-07 (rows of PROTOCOL_DEVIATION_LOG with `gap_ref`)\n')
rows=[]
for g in ['GAP-01','GAP-02','GAP-03','GAP-04','GAP-05','GAP-06','GAP-07']:
    rows.append([g]+[', '.join(r['dev_id'] for r in D[c]['T']['PROTOCOL_DEVIATION_LOG'] if r['gap_ref']==g) or '-' for c in cases])
A(tbl('Gap',rows,total=False))
A('Deviation-log rows per case: '+'; '.join(f"{SHORT[c]} = {len(D[c]['T']['PROTOCOL_DEVIATION_LOG'])} (of which with `gap_ref`: {sum(1 for r in D[c]['T']['PROTOCOL_DEVIATION_LOG'] if r['gap_ref'])})" for c in cases)+'. GAP-02 (provisions amending other acts): used in C1_SCF (Article 28) and AI_AI_ACT (Articles 102 to 110); C2_CBAM logged that it examined GAP-02 and did not use it (DEV-04); O_DIR_86_361 has no GAP-02 row and its QA report states that GAP-02 did not arise. GAP-06 (the "six questions") is recorded as `NON_OPERATIVE_SOURCE_GAP` in all four cases. GAP-05: `FUNCTION_VOCABULARY_UNRESOLVED` appears in the function field of C1_SCF, AI_AI_ACT and O_DIR_86_361 and not in C2_CBAM (its DEV-07 records that it was not needed); counts in section 3.\n')
A('### 9.2 Other patterns recorded in the deviation logs (case and DEV id)\n')
A('| Pattern | C1_SCF | C2_CBAM | AI_AI_ACT | O_DIR_86_361 |\n|---|---|---|---|---|')
pats=[
('Mapping of the ten dimensions to property families F1-F5 not stated in the allow-listed sources (RGAM-DR-24)','DEV-08 (provisional assignment by listing order; positional examples left blank)','DEV-10 (provisional assignment by listing order)','DEV-10 (left blank for all properties)','DEV-10 (left blank for all properties)'),
('Unit-identifier conventions beyond those in the dictionary (RGAM-DR-05)','DEV-10','DEV-02 (with GAP-01)','DEV-08','DEV-01 (with GAP-01), DEV-02'),
('Operationalisation of the status ceiling / down-coding of records with constitutive external dependencies (RGAM-DR-18 to DR-20)','DEV-12','DEV-11','DEV-04 (kept at documented level); QA section 3 (down-coding rule)','DEV-12'),
('Choice of temporal reference by the executor','stated in W_DECLARATION; not logged as a deviation','DEV-01 (HQ-OTHER)','stated in W_DECLARATION; not logged as a deviation','DEV-12 (with status ceiling); HQ-015'),
('Content not representable in the source file (images, table geometry, footnote apparatus, page chrome)','DEV-11 (Annex I formula images)','DEV-03 (Annex IV formula images; Annex I-II table geometry)','DEV-08 (footnote apparatus declared as exclusion)','W_DECLARATION exclusions (page chrome, separator, heading lines); DEV-02 (headings, separator, merged-point splitting)'),
('Reading depth limits recorded','DEV-11 (3 of 6 image-only units viewed)','none logged','DEV-11 (recitals REC34-REC180 screened from opening text and length)','none logged'),
('Relation-admission or party questions not covered by the dictionary','DEV-07 (definitions yield positions only where they bear a record)','DEV-12 (NA and PD members in subconfigurations)','DEV-09 (devices used as relation counterparts); DEV-12 (accountability class independent of relation type)','DEV-04 (citations not coded as EXT); DEV-09 (definition-derived relations)'),
('Reading of an ambiguous protocol rule','none logged','none logged','none logged','DEV-11 (RGAM-DR-25 applied to every candidate touched by a constitutive external reference); DEV-13 (trace-selection generator and meaning of "part")'),
('Recovery after an interrupted executor','none','none','recovery executor started fresh; earlier executor interrupted before producing records (per case log and orchestrator audit)','DEV-14 (recovery run reusing the earlier executor\'s tables, with listed corrections)'),
]
for p in pats: A('| '+' | '.join(p)+' |')
A('')
A('Property-family field: blank in '+'; '.join(f"{SHORT[c]} {sum(1 for r in D[c]['T']['PROPERTY_REGISTER'] if r['property_family']=='')} of {len(D[c]['T']['PROPERTY_REGISTER'])}" for c in cases)+' PROPERTY_REGISTER rows.\n')
A('### 9.3 Cross-reference derivation and function-vocabulary points\n')
A('Internal cross-references were followed under GAP-03 in all four cases; derived NA+QR records are counted in section 3. Function-vocabulary questions (GAP-05) are queued as HQ-GAP items in all four cases (as separate items in C1_SCF HQ-010, AI_AI_ACT HQ-030 and O_DIR_86_361 HQ-013; inside the bundled item HQ-016 in C2_CBAM). Property-family mapping, accountability-class readings, norm-type readings, device-threshold readings and external-dependency scope recur as queue categories in more than one case (section 8).\n')
A('### 9.4 Small internal inconsistencies noticed while reading the frozen case files (reported, not corrected)\n')
A('- O_DIR_86_361: `EXECUTION_PROVENANCE.md` section 5 says the trace-generator choice is "logged DEV-14", while PROTOCOL_DEVIATION_LOG records it as DEV-13 (DEV-14 is the recovery-run entry); `CASE_QA_REPORT.md` section D (C5) and `CASE_GATE.md` cite DEV-14/DEV-15 for the recovery corrections in a way that differs from the log\'s row numbering (DEV-14 recovery run; DEV-15 evidence-span convention). The frozen files were not changed.\n- RUN_METADATA.model_parameters: C1_SCF, C2_CBAM and the O_DIR_86_361 recovery run record `reasoning_effort=10` as displayed in the invocation context; AI_AI_ACT records reasoning effort as NOT_EXPOSED. The orchestrator audit states that the Agent tool exposes no reasoning-effort parameter.\n- INSTRUMENT_LEVEL_SUMMARY.record_counts lists different table subsets per case (section 2.1).\n')
A('## 10. Run and provenance facts as recorded\n')
A('| Case | Model id (RUN_METADATA) | Parameters as recorded | Start / end (as recorded) | Executor (orchestrator audit) | Earlier interrupted executor (orchestrator audit) |\n|---|---|---|---|---|---|')
for r in REG: A(f"| {SHORT[r['capsule_id']]} | {r['model_id_recorded']} | {r['model_parameters_recorded'][:230]}{'...' if len(r['model_parameters_recorded'])>230 else ''} | {r['run_start_time']} / {r['run_end_time']} | {r['executor_agent_id_orchestrator_audit']} | {r['earlier_interrupted_executor_orchestrator_audit']} |")
A('\nAll four RUN_METADATA rows record `protocol_version = RGAM paired execution protocol v1.0`, the protocol manifest SHA-256 `9ca016b97289b39049dc099b265c20662c1ebc05e86bc720f0fbe80e0bac5932`, `fresh_context_attested = Y`, `forbidden_paths_attempted = NONE` and `machine_generated = Y`.\n')
A('## 11. Limits of this summary\n')
A('Single-pass machine execution by one model family for all four cases; case executors checked their own outputs; none of the numbers here measure correctness, completeness of legal interpretation or architectural properties of the legal instruments. Instrument sizes differ widely (93 to 1553 units), so raw counts are not mutually normalised and no normalisation is offered. No human adjudication has taken place; all records are machine-generated and provisional. This file contains no comparison with V8 or any other method, no improvement, agreement or performance measure, and no inference about any other arm of the experiment.\n')
open(F+'/RGAM_CROSS_CASE_DESCRIPTIVE_SUMMARY.md','w',encoding='utf-8',newline='\n').write('\n'.join(S))
print('ok',len('\n'.join(S)))
