from stats import *
import io
D=gather()
F=C+'/FAMILY'
def sha_text(s): return hashlib.sha256(s.encode('utf-8')).hexdigest()
# ---------- register
ARCHO=['INTEGRATED','DISTINGUISHABLE','OVERLAPPING_OR_PARTIALLY_INTEGRATED','INDETERMINATE']
cols=['capsule_id','celex','instrument','case_gate','source_sha256_capsule_metadata','source_sha256_recomputed','source_hash_status','w_declaration_hash_match_recorded','contamination_status_case_access_log','case_freeze_manifest_sha256_recomputed','case_freeze_manifest_sidecar_sha256','case_freeze_manifest_status','case_manifest_files_listed','case_manifest_files_valid','human_review_items_present','human_review_item_count']
cols+=['rows__'+t for t in tables]
cols+=['units_total','stratum_E_count','stratum_P_count','stratum_R_count','stratum_S_count','stratum_A_count','stratum_total_E_P_R_S_A']
cols+=['instrument_level_result_token','highest_level_reached_stopping_level','arch_candidates_total']+['arch_outcome_'+o for o in ARCHO]
cols+=['status_profile_as_recorded','recomputed_QR_legal_constitution_evidenced','recomputed_QR_documented','recomputed_NA_legal_constitution_evidenced','recomputed_NA_documented','recomputed_PD_legal_constitution_evidenced','recomputed_PD_documented','recomputed_material_establishment_evidenced_any','recomputed_exercise_evidenced_any']
cols+=['hq_open_count_recorded','hq_rows_recomputed','unresolved_external_references_recorded','ext_constitutive_dependency_Y_recomputed','ext_rows_recomputed']
cols+=['run_id','model_id_recorded','model_parameters_recorded','run_start_time','run_end_time','fresh_context_attested','forbidden_paths_attempted_recorded','protocol_version_recorded','protocol_manifest_sha256_recorded','executor_agent_id_orchestrator_audit','earlier_interrupted_executor_orchestrator_audit','deviation_log_entries','uncertainty_log_entries']
rows=[]
for c in cases:
    d=D[c];T=d['T']
    man=f'{C}/{c}/CASE_FREEZE_MANIFEST.csv'
    mrows=list(csv.DictReader(open(man,encoding='utf-8-sig')))
    valid=sum(1 for r in mrows if os.path.exists(f'{C}/{c}/'+r['relative_path']) and sha_file(f'{C}/{c}/'+r['relative_path'])==r['sha256'] and os.path.getsize(f'{C}/{c}/'+r['relative_path'])==int(r['bytes']))
    mh=sha_file(man); side=open(f'{C}/{c}/CASE_FREEZE_MANIFEST_SHA256.txt').read().split()[0]
    gate=[l for l in open(f'{C}/{c}/CASE_GATE.md',encoding='utf-8').read().splitlines() if 'RGAM_CASE_FROZEN' in l]
    gate_tok='RGAM_CASE_FROZEN' if gate and gate[0].strip('* ')=='RGAM_CASE_FROZEN' else 'NOT_VERIFIED'
    sh=sha_file(d['legal']); exp=d['meta']['source_sha256']
    ils=T['INSTRUMENT_LEVEL_SUMMARY'][0]; run=T['RUN_METADATA'][0]
    cnt={t:len(T[t]) for t in tables}
    strat={k:sum(cnt[t] for t in v) for k,v in STRATA.items()}
    ao=Counter(r['outcome'] for r in T['ARCHITECTURE_CANDIDATES'])
    def ep(t,v): return sum(1 for r in T[t] if r['epistemic_status']==v)
    anym=sum(1 for t in ['QUALIFIED_RELATIONS','NORMATIVE_ASSIGNMENTS','POSITIONS_AND_DEVICES'] for r in T[t] if r['epistemic_status']=='material_establishment_evidenced')
    anye=sum(1 for t in ['QUALIFIED_RELATIONS','NORMATIVE_ASSIGNMENTS','POSITIONS_AND_DEVICES'] for r in T[t] if r['epistemic_status']=='exercise_evidenced')
    hq=cnt['HUMAN_REVIEW_QUEUE']
    row=dict(capsule_id=c,celex=d['meta']['celex'],instrument=d['meta']['instrument_title'],case_gate=gate_tok,
      source_sha256_capsule_metadata=exp,source_sha256_recomputed=sh,source_hash_status='MATCH' if sh==exp else 'MISMATCH',
      w_declaration_hash_match_recorded=T['W_DECLARATION'][0]['hash_match'],contamination_status_case_access_log=d['contam'],
      case_freeze_manifest_sha256_recomputed=mh,case_freeze_manifest_sidecar_sha256=side,case_freeze_manifest_status='OK' if mh==side and valid==len(mrows) else 'FAIL',
      case_manifest_files_listed=len(mrows),case_manifest_files_valid=valid,human_review_items_present='YES' if hq>0 else 'NO',human_review_item_count=hq)
    for t in tables: row['rows__'+t]=cnt[t]
    row.update(units_total=ils['units_total'],stratum_E_count=strat['E'],stratum_P_count=strat['P'],stratum_R_count=strat['R'],stratum_S_count=strat['S'],stratum_A_count=strat['A'],stratum_total_E_P_R_S_A=sum(strat.values()),
      instrument_level_result_token=ils['instrument_level_result'],highest_level_reached_stopping_level=ils['highest_level_reached'],arch_candidates_total=cnt['ARCHITECTURE_CANDIDATES'])
    for o in ARCHO: row['arch_outcome_'+o]=ao.get(o,0)
    row.update(status_profile_as_recorded=ils['status_profile'],
      recomputed_QR_legal_constitution_evidenced=ep('QUALIFIED_RELATIONS','legal_constitution_evidenced'),recomputed_QR_documented=ep('QUALIFIED_RELATIONS','documented'),
      recomputed_NA_legal_constitution_evidenced=ep('NORMATIVE_ASSIGNMENTS','legal_constitution_evidenced'),recomputed_NA_documented=ep('NORMATIVE_ASSIGNMENTS','documented'),
      recomputed_PD_legal_constitution_evidenced=ep('POSITIONS_AND_DEVICES','legal_constitution_evidenced'),recomputed_PD_documented=ep('POSITIONS_AND_DEVICES','documented'),
      recomputed_material_establishment_evidenced_any=anym,recomputed_exercise_evidenced_any=anye,
      hq_open_count_recorded=ils['hq_open_count'],hq_rows_recomputed=hq,unresolved_external_references_recorded=ils['unresolved_ext_count'],
      ext_constitutive_dependency_Y_recomputed=sum(1 for r in T['EXTERNAL_REFERENCES'] if r['constitutive_dependency']=='Y'),ext_rows_recomputed=cnt['EXTERNAL_REFERENCES'],
      run_id=run['run_id'],model_id_recorded=run['model_id'],model_parameters_recorded=run['model_parameters'],run_start_time=run['start_time'],run_end_time=run['end_time'],fresh_context_attested=run['fresh_context_attested'],
      forbidden_paths_attempted_recorded=run['forbidden_paths_attempted'],protocol_version_recorded=run['protocol_version'],protocol_manifest_sha256_recorded=run['protocol_manifest_sha256'],
      executor_agent_id_orchestrator_audit=EXEC_IDS[c][0],earlier_interrupted_executor_orchestrator_audit=EXEC_IDS[c][1] or 'NONE',
      deviation_log_entries=cnt['PROTOCOL_DEVIATION_LOG'],uncertainty_log_entries=cnt['UNCERTAINTY_LOG'])
    rows.append(row)
hdr=['# RGAM_FOUR_CASE_EXECUTION_REGISTER.csv - descriptive register of four frozen RGAM case executions; counts are descriptors, not scores; no ranking or comparison with any other method.',
'# Stratum mapping (RGAM_CASE_OUTPUT_SCHEMA.md section 2, as instructed): E = SOURCE_UNIT_INVENTORY + INSTITUTIONAL_STATEMENTS; P = NORMATIVE_ASSIGNMENTS + POSITIONS_AND_DEVICES; R = QUALIFIED_RELATIONS + EXTERNAL_REFERENCES; S = SUBCONFIGURATIONS; A = ARCHITECTURE_CANDIDATES.',
'# Not in the five stratum counts (given only as rows__<TABLE> columns): W_DECLARATION, UNIT_SCREENING, PROPERTY_REGISTER, CLOSURE_REGISTER, PROVENANCE_LINKS, UNCERTAINTY_LOG, HUMAN_REVIEW_QUEUE, TRACE_DEMONSTRATIONS, INSTRUMENT_LEVEL_SUMMARY, PROTOCOL_DEVIATION_LOG, RUN_METADATA. Lines starting with # are comments; the header row is the first line not starting with #.',
'# Column definitions: rows__<TABLE> = data rows recomputed from the frozen case CSV (header excluded). *_recorded = value as written by the case executor in its own table; *_recomputed = value recomputed by the family assembler. Hash and manifest values are recomputed SHA-256. human_review_items_present = YES if HUMAN_REVIEW_QUEUE has at least one row. executor_agent_id_orchestrator_audit and earlier_interrupted_executor_orchestrator_audit are copied from _orchestrator/ISOLATION_AUDIT_SUMMARY.md.']
buf=io.StringIO(newline='')
for h in hdr: buf.write(h+'\r\n')
w=csv.DictWriter(buf,fieldnames=cols,lineterminator='\r\n'); w.writeheader()
for r in rows: w.writerow(r)
open(F+'/RGAM_FOUR_CASE_EXECUTION_REGISTER.csv','w',encoding='utf-8-sig',newline='').write(buf.getvalue())
json.dump(rows,open(F+'/_work/register_rows.json','w'),indent=1)
# ---------- queue
LABEL={
'RGAM_C1_SCF':{1:'ARCHITECTURE_INTEGRATION_WARRANT_QUESTION',2:'ARCHITECTURE_OVERLAP_OR_SEPARATION_QUESTION',3:'ACCOUNTABILITY_CLASS_QUESTION',4:'NORM_TYPE_CLASSIFICATION',5:'DEVICE_THRESHOLD_CLASSIFICATION',6:'DEVICE_THRESHOLD_CLASSIFICATION',7:'CROSS_REFERENCE_SCOPE_RESOLUTION',8:'COUNTERPARTY_OR_DIRECTION_NOT_STATED',9:'PROPERTY_FAMILY_MAPPING_ABSENT',10:'FUNCTION_VOCABULARY_FIT',11:'EXECUTION_ADDENDUM_USE_CONFIRMATION',12:'EXTERNAL_DEPENDENCY_CLAIM_SCOPE',13:'EXTERNAL_DEPENDENCY_CLAIM_SCOPE',14:'EXTERNAL_DEPENDENCY_CLAIM_SCOPE',15:'EXTERNAL_DEPENDENCY_CLAIM_SCOPE',16:'EXTERNAL_DEPENDENCY_CLAIM_SCOPE',17:'EXTERNAL_DEPENDENCY_CLAIM_SCOPE',18:'EXTERNAL_DEPENDENCY_CLAIM_SCOPE',19:'RELATION_TYPE_NEAREST_FIT'},
'RGAM_C2_CBAM':{1:'NORM_TYPE_CLASSIFICATION',2:'NORM_TYPE_CLASSIFICATION',3:'ACCOUNTABILITY_CLASS_QUESTION',4:'COUNTERPARTY_OR_DIRECTION_NOT_STATED',5:'EXTERNAL_DEPENDENCY_CLAIM_SCOPE',6:'EXTERNAL_DEPENDENCY_CLAIM_SCOPE',7:'EXTERNAL_DEPENDENCY_CLAIM_SCOPE',8:'EXTERNAL_DEPENDENCY_CLAIM_SCOPE',9:'EXTERNAL_DEPENDENCY_CLAIM_SCOPE',10:'EXTERNAL_DEPENDENCY_CLAIM_SCOPE',11:'CROSS_REFERENCE_SCOPE_RESOLUTION',12:'TEMPORAL_REFERENCE_AND_STATUS_CEILING_CHOICE',13:'ARCHITECTURE_INTEGRATION_WARRANT_QUESTION',14:'ARCHITECTURE_INTEGRATION_WARRANT_QUESTION',15:'ARCHITECTURE_OVERLAP_OR_SEPARATION_QUESTION',16:'MULTIPLE_PROTOCOL_GAP_CONFIRMATION'},
'RGAM_AI_AI_ACT':{1:'EXTERNAL_DEPENDENCY_CLAIM_SCOPE',2:'BEARER_ATTRIBUTION_QUESTION',3:'COUNTERPARTY_OR_DIRECTION_NOT_STATED',4:'NORM_TYPE_CLASSIFICATION',5:'NORM_TYPE_CLASSIFICATION',6:'EXTERNAL_DEPENDENCY_CLAIM_SCOPE',7:'ACCOUNTABILITY_CLASS_QUESTION',8:'NORM_TYPE_CLASSIFICATION',9:'DEVICE_THRESHOLD_CLASSIFICATION',10:'NORM_TYPE_CLASSIFICATION',11:'NORM_TYPE_CLASSIFICATION',12:'NORM_TYPE_CLASSIFICATION',13:'ACCOUNTABILITY_CLASS_QUESTION',14:'NORM_TYPE_CLASSIFICATION',15:'ACCOUNTABILITY_CLASS_QUESTION',16:'COUNTERPARTY_OR_DIRECTION_NOT_STATED',17:'ACCOUNTABILITY_CLASS_QUESTION',18:'ACCOUNTABILITY_CLASS_QUESTION',19:'ARCHITECTURE_INTEGRATION_WARRANT_QUESTION',20:'ARCHITECTURE_INTEGRATION_WARRANT_QUESTION',21:'ARCHITECTURE_INTEGRATION_WARRANT_QUESTION',22:'ARCHITECTURE_INTEGRATION_WARRANT_QUESTION',23:'ARCHITECTURE_INTEGRATION_WARRANT_QUESTION',24:'ARCHITECTURE_OVERLAP_OR_SEPARATION_QUESTION',25:'PROPERTY_FAMILY_MAPPING_ABSENT',26:'EXECUTION_ADDENDUM_USE_CONFIRMATION',27:'EXECUTION_ADDENDUM_USE_CONFIRMATION',28:'EXECUTION_ADDENDUM_USE_CONFIRMATION',29:'EXECUTION_ADDENDUM_USE_CONFIRMATION',30:'FUNCTION_VOCABULARY_FIT',31:'EXECUTION_ADDENDUM_USE_CONFIRMATION',32:'EXECUTION_ADDENDUM_USE_CONFIRMATION',33:'DEVICE_AS_RELATION_PARTY_QUESTION',34:'UNIT_IDENTIFIER_CONVENTION_CONFIRMATION',35:'COUNTERPARTY_OR_DIRECTION_NOT_STATED'},
'RGAM_O_DIR_86_361':{1:'NORM_TYPE_CLASSIFICATION',2:'NORM_TYPE_CLASSIFICATION',3:'DEVICE_THRESHOLD_CLASSIFICATION',4:'ACCOUNTABILITY_CLASS_QUESTION',5:'CROSS_REFERENCE_SCOPE_RESOLUTION',6:'COUNTERPARTY_OR_DIRECTION_NOT_STATED',7:'CROSS_REFERENCE_SCOPE_RESOLUTION',8:'CROSS_REFERENCE_SCOPE_RESOLUTION',9:'COUNTERPARTY_OR_DIRECTION_NOT_STATED',10:'COUNTERPARTY_OR_DIRECTION_NOT_STATED',11:'EXECUTION_ADDENDUM_USE_CONFIRMATION',12:'EXECUTION_ADDENDUM_USE_CONFIRMATION',13:'FUNCTION_VOCABULARY_FIT',14:'PROPERTY_FAMILY_MAPPING_ABSENT',15:'TEMPORAL_REFERENCE_AND_STATUS_CEILING_CHOICE',16:'PROTOCOL_RULE_READING_QUESTION',17:'EXTERNAL_DEPENDENCY_CLAIM_SCOPE',18:'ADDRESSEE_SCOPE_OF_INSTRUMENT_QUESTION',19:'RELATION_TYPE_NEAREST_FIT'}}
qcols_extra=['family_hq_id','trigger_category','recurring_category_label','source_file','source_row_number','source_row_sha256']
qout=[]
orig=None
for c in cases:
    h,rows_,raw=load(c,'HUMAN_REVIEW_QUEUE')
    orig=h
    for i,(r,rr) in enumerate(zip(rows_,raw),start=2):
        n=int(r['hq_id'].split('-')[1])
        lab=LABEL[c][n]
        qout.append(dict(family_hq_id=f"FHQ-{c}-{r['hq_id']}",trigger_category=r['trigger_code'],recurring_category_label=lab,source_file=f'{c}/HUMAN_REVIEW_QUEUE.csv',source_row_number=i,source_row_sha256=sha_text('\x1f'.join(rr)),**r))
fcols=qcols_extra[:3]+list(orig)+qcols_extra[3:]
buf=io.StringIO(newline='')
w=csv.DictWriter(buf,fieldnames=fcols,lineterminator='\r\n'); w.writeheader()
for r in qout: w.writerow({k:r[k] for k in fcols})
open(F+'/RGAM_FAMILY_HUMAN_REVIEW_QUEUE.csv','w',encoding='utf-8-sig',newline='').write(buf.getvalue())
json.dump(qout,open(F+'/_work/queue_rows.json','w'),indent=1)
print(len(qout),Counter(r['recurring_category_label'] for r in qout))
