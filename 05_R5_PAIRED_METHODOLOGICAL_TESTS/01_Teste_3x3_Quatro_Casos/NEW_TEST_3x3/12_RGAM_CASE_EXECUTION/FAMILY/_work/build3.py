from stats import *
import integrity_fn
D=gather()
F=C+'/FAMILY'
REG=json.load(open(F+'/_work/register_rows.json'))
Q=json.load(open(F+'/_work/queue_rows.json'))
dh=dict_headers()
R={}   # results
allok=True
def rec(key,ok,detail):
    global allok
    R[key]=(ok,detail)
    if not ok: allok=False
# 1 protocol manifest
pm=P+'/RGAM_PROTOCOL_FREEZE_MANIFEST.csv'
pm_hash=sha_file(pm)
pm_side=open(P+'/RGAM_PROTOCOL_FREEZE_MANIFEST_SHA256.txt').read().split()[0]
prow=list(csv.DictReader(open(pm,encoding='utf-8-sig')))
pbad=[r['relative_path'] for r in prow if not os.path.exists(P+'/'+r['relative_path']) or sha_file(P+'/'+r['relative_path'])!=r['sha256'] or os.path.getsize(P+'/'+r['relative_path'])!=int(r['bytes'])]
rec('protocol_manifest',pm_hash==EXPECT_PM==pm_side and len(prow)==107 and not pbad,f'recomputed SHA-256 `{pm_hash}`; expected `{EXPECT_PM}`; sidecar `{pm_side}`; files listed {len(prow)}; files valid {len(prow)-len(pbad)}; invalid {pbad or "none"}')
gap_hash=sha_file(P+'/RGAM_EXECUTION_GAP_DECISIONS_v1_0.md'); gap_side=open(P+'/RGAM_EXECUTION_GAP_DECISIONS_SHA256.txt').read().split()[0]
rec('addendum',gap_hash==EXPECT_GAP==gap_side,f'recomputed `{gap_hash}`; expected `{EXPECT_GAP}`; sidecar `{gap_side}`')
# 2 case manifests/gates
cm={}
for r in REG:
    c=r['capsule_id']
    ok=r['case_freeze_manifest_status']=='OK' and r['case_gate']=='RGAM_CASE_FROZEN'
    cm[c]=ok
    rec('case_'+c,ok,f"manifest recomputed `{r['case_freeze_manifest_sha256_recomputed']}`, sidecar `{r['case_freeze_manifest_sidecar_sha256']}`, files listed {r['case_manifest_files_listed']}, valid {r['case_manifest_files_valid']}; gate `{r['case_gate']}`")
# manifests list EXECUTOR_BRIEF and exclude _work
inman={}
for c in cases:
    rs=list(csv.DictReader(open(f'{C}/{c}/CASE_FREEZE_MANIFEST.csv',encoding='utf-8-sig')))
    inman[c]=(any(r['relative_path']=='EXECUTOR_BRIEF.md' for r in rs),any(r['relative_path'].startswith('_work') for r in rs),len(rs))
# 3 method identity
docs=['RGAM_PAIRED_EXECUTION_PROTOCOL_v1_0.md','RGAM_PAIRED_DECISION_RULES_v1_0.md','RGAM_PAIRED_DATA_DICTIONARY_v1_0.md','RGAM_CASE_OUTPUT_SCHEMA.md','RGAM_BLINDNESS_AND_ACCESS_POLICY.md','RGAM_EXECUTION_GAP_DECISIONS_v1_0.md']
dh_hash={d:sha_file(P+'/'+d) for d in docs}
method={}
for c in cases:
    run=D[c]['T']['RUN_METADATA'][0]
    prov=open(f'{C}/{c}/EXECUTION_PROVENANCE.md',encoding='utf-8').read()
    ok_run=run['protocol_version']=='RGAM paired execution protocol v1.0' and EXPECT_PM in run['protocol_manifest_sha256']
    ok_prov=EXPECT_PM in prov and 'gap' in prov.lower()
    ok_files=all(d in run['files_read'] for d in docs)
    cited=[d for d in docs if dh_hash[d] in prov]
    method[c]=(ok_run,ok_prov,ok_files,len(cited))
    rec('method_'+c,ok_run and ok_prov and ok_files,f'RUN_METADATA protocol_version+manifest hash: {ok_run}; EXECUTION_PROVENANCE names manifest hash and addendum: {ok_prov}; RUN_METADATA files_read lists all six frozen method documents: {ok_files}; method-document SHA-256 values cited in provenance that equal recomputed hashes: {len(cited)} of 6')
# 4 legal source
capreg={r['capsule_id']:r for r in csv.DictReader(open(P+'/RGAM_EXECUTION_CAPSULE_REGISTER.csv',encoding='utf-8-sig'))}
legal={}
for c in cases:
    sh=sha_file(D[c]['legal']); exp=D[c]['meta']['source_sha256']; w=D[c]['T']['W_DECLARATION'][0]
    ok=sh==exp==capreg[c]['sha256_register_expected']==w['source_sha256']==w['expected_sha256'] and w['hash_match']=='Y'
    legal[c]=(sh,ok)
    rec('legal_'+c,ok,f'recomputed `{sh}`; CASE_METADATA `{exp}`; capsule register `{capreg[c]["sha256_register_expected"]}`; W_DECLARATION source/expected/hash_match = `{w["source_sha256"][:12]}...`/`{w["expected_sha256"][:12]}...`/`{w["hash_match"]}`')
# 5 headers
hdr={}
for c in cases:
    bad=[];bom=[];ragged=[]
    for t in tables:
        h,rows,raw=load(c,t)
        if h!=dh[t]: bad.append(t)
        if open(f'{C}/{c}/{t}.csv','rb').read(3)!=b'\xef\xbb\xbf': bom.append(t)
        if any(len(x)!=len(h) for x in raw): ragged.append(t)
    hdr[c]=(bad,bom,ragged)
    rec('headers_'+c,not bad and not ragged and os.path.exists(f'{C}/{c}/CASE_RGAM_REPORT.md'),f'19 tables compared with the frozen data-dictionary field lists (section 3.1-3.19): header mismatches {bad or "none"}; ragged rows {ragged or "none"}; files without UTF-8 BOM {bom or "none"}; CASE_RGAM_REPORT.md present')
# 6 integrity
integ={}
for c in cases:
    f=integrity_fn.check_case(c)
    integ[c]=f
    rec('integrity_'+c,not f,f'independent recomputation of data-dictionary integrity rules 1-10: {len(f)} failures')
# 7 ils record_counts
ilsmis={}
for c in cases:
    ils=D[c]['T']['INSTRUMENT_LEVEL_SUMMARY'][0]
    pairs=re.findall(r'(\w+)=(\d+)',ils['record_counts'])
    mis=[(k,v,len(D[c]['T'][k])) for k,v in pairs if k in D[c]['T'] and int(v)!=len(D[c]['T'][k])]
    ilsmis[c]=(len(pairs),mis)
    extra=int(ils['hq_open_count'])==len(D[c]['T']['HUMAN_REVIEW_QUEUE']) and int(ils['unresolved_ext_count'])==sum(1 for r in D[c]['T']['EXTERNAL_REFERENCES'] if r['constitutive_dependency']=='Y') and ils['units_total']==ils['units_screened']==str(len(D[c]['T']['SOURCE_UNIT_INVENTORY']))
    rec('ils_'+c,not mis and extra,f'{len(pairs)} listed counts, mismatches {mis or "none"}; hq_open_count, unresolved_ext_count, units_total/units_screened equal recomputed values: {extra}')
# 8 human blank everywhere
hum={}
for c in cases:
    nonblank=0;cols=0
    for t in tables:
        h,rows,raw=load(c,t)
        for k in h:
            if k.startswith('human_') or k in('decided_by','decision_date'):
                cols+=1
                nonblank+=sum(1 for r in rows if r[k].strip())
    hum[c]=(cols,nonblank)
    rec('human_'+c,nonblank==0 and cols==4,f'human-decision columns found {cols} (all in HUMAN_REVIEW_QUEUE); non-blank cells {nonblank}')
fq=list(csv.DictReader(open(F+'/RGAM_FAMILY_HUMAN_REVIEW_QUEUE.csv',encoding='utf-8-sig',newline='')))
fnon=sum(1 for r in fq for k in ('human_decision','human_rationale','decided_by','decision_date') if r[k].strip())
rec('human_family',fnon==0,f'family queue rows {len(fq)}; non-blank human cells {fnon}')
# 9 family consistency
regtxt=open(F+'/RGAM_FOUR_CASE_EXECUTION_REGISTER.csv',encoding='utf-8-sig',newline='').read().splitlines()
regrows=list(csv.DictReader([l for l in regtxt if not l.startswith('#')]))
mism=[]
for r in regrows:
    c=r['capsule_id']
    for t in tables:
        if int(r['rows__'+t])!=len(D[c]['T'][t]): mism.append((c,t))
    st={k:sum(len(D[c]['T'][t]) for t in v) for k,v in STRATA.items()}
    for k,v in st.items():
        if int(r['stratum_%s_count'%k])!=v: mism.append((c,k))
    if int(r['human_review_item_count'])!=len(D[c]['T']['HUMAN_REVIEW_QUEUE']): mism.append((c,'hq'))
rec('family_register',not mism and len(regrows)==4,f'register rows {len(regrows)}; mismatches against recomputed table/stratum/HQ counts: {mism or "none"}')
sumq=sum(len(D[c]['T']['HUMAN_REVIEW_QUEUE']) for c in cases)
orig_cols=load(cases[0],'HUMAN_REVIEW_QUEUE')[0]
trace_bad=[]
for r in fq:
    c=r['case_id']
    src=[x for x in D[c]['T']['HUMAN_REVIEW_QUEUE'] if x['hq_id']==r['hq_id']]
    if len(src)!=1 or any(src[0][k]!=r[k] for k in orig_cols) or r['family_hq_id']!=f"FHQ-{c}-{r['hq_id']}" or r['trigger_category']!=r['trigger_code']:
        trace_bad.append(r['family_hq_id'])
        continue
    h,rows_,raw=load(c,'HUMAN_REVIEW_QUEUE')
    rawrow=raw[int(r['source_row_number'])-2]
    if hashlib.sha256('\x1f'.join(rawrow).encode('utf-8')).hexdigest()!=r['source_row_sha256']: trace_bad.append(r['family_hq_id']+' rowhash')
uniq=len({r['family_hq_id'] for r in fq})==len(fq)
rec('family_queue',len(fq)==sumq and not trace_bad and uniq,f'combined queue rows {len(fq)} = sum of case queues {sumq} ({", ".join(str(len(D[c]["T"]["HUMAN_REVIEW_QUEUE"])) for c in cases)}); every item traced to its case row (all original columns identical): untraceable {trace_bad or "none"}; family ids unique: {uniq}; recurring_category_label non-empty for all: {all(r["recurring_category_label"] for r in fq)}')
# counts
nchk=len(R); nfail=sum(1 for v in R.values() if not v[0])
GATE='RGAM_FOUR_CASE_EXECUTION_FROZEN / V8_RESULTS_NOT_CONSULTED / PAIRED_COMPARISON_NOT_STARTED'
json.dump({k:[v[0],v[1]] for k,v in R.items()},open(F+'/_work/verify_results.json','w'),indent=1)
# ---------------- QA report
def P_(ok): return 'PASS' if ok else 'FAIL'
S=[]
A=S.append
A('# RGAM family stage - execution QA report\n')
A('Prepared by the RGAM family assembler (fresh isolated context). Every figure below was recomputed by script from the frozen files on disk at assembly time; nothing was taken from a case executor\'s own QA statements except where explicitly labelled "as recorded". The checks are structural and mechanical; they do not validate the analytical or legal correctness of any record.\n')
A(f'**Overall result: {nchk-nfail} of {nchk} checks pass; {nfail} fail.**\n')
A('## 1. Summary of required verifications\n')
A('| # | Verification | Result |\n|---:|---|---|')
A(f"| 1 | All four case gates read `RGAM_CASE_FROZEN` | {P_(all(r['case_gate']=='RGAM_CASE_FROZEN' for r in REG))} ({sum(1 for r in REG if r['case_gate']=='RGAM_CASE_FROZEN')} of 4) |")
A(f"| 2 | Each case freeze manifest recomputed (equals its sidecar) and every listed file hash and byte size valid | {P_(all(r['case_freeze_manifest_status']=='OK' for r in REG))} |")
A(f"| 3 | Protocol manifest SHA-256 recomputed = `9ca016b9...5932`, equals sidecar, all 107 listed files valid | {P_(R['protocol_manifest'][0])} |")
A(f"| 4 | Execution-addendum SHA-256 recomputed = `b9dc184e...2da4` | {P_(R['addendum'][0])} |")
A(f"| 5 | Same frozen method referenced by all four cases (RUN_METADATA and EXECUTION_PROVENANCE) | {P_(all(R['method_'+c][0] for c in cases))} |")
A(f"| 6 | Legal-source SHA-256 of each capsule equals CASE_METADATA (also capsule register and W_DECLARATION) | {P_(all(R['legal_'+c][0] for c in cases))} |")
A(f"| 7 | Each case's 19 tables have the frozen headers (data dictionary section 3) | {P_(all(R['headers_'+c][0] for c in cases))} |")
A(f"| 8 | Data-dictionary integrity rules 1-10 independently recomputed for every case | {P_(all(R['integrity_'+c][0] for c in cases))} |")
A(f"| 9 | Family register counts = recomputed counts | {P_(R['family_register'][0])} |")
A(f"| 10 | Combined queue count = sum of case queues; every combined item traces to its case row | {P_(R['family_queue'][0])} ({len(fq)} = {sumq}) |")
A(f"| 11 | Human-decision fields blank everywhere (case queues and family queue) | {P_(all(R['human_'+c][0] for c in cases) and R['human_family'][0])} |")
A(f"| 12 | INSTRUMENT_LEVEL_SUMMARY figures consistent with recomputed counts | {P_(all(R['ils_'+c][0] for c in cases))} |")
A('| 13 | Family assembler isolation | stated in section 9 |\n')
A('## 2. Protocol and addendum hashes\n')
A(f"- Protocol manifest `RGAM_PROTOCOL_FREEZE_MANIFEST.csv`: {R['protocol_manifest'][1]}. Status: **{'OK' if R['protocol_manifest'][0] else 'FAIL'}**. Verification of the 107 listed files required computing the SHA-256 of the files named in the manifest, including files that are not on the assembler's read allow-list (PRECEDENCE register, SOURCE_AUTHORITY register, protocol gate/QA files, capsule files, templates); their bytes were hashed by script and their contents were not read or displayed (see section 9).")
A(f"- Execution addendum `RGAM_EXECUTION_GAP_DECISIONS_v1_0.md`: {R['addendum'][1]}. Status: **{'OK' if R['addendum'][0] else 'FAIL'}**. The addendum is not itself listed in the protocol manifest (it is a prospective addendum with its own sidecar).\n")
A('## 3. Case gates and freeze manifests\n')
A('| Case | Gate (CASE_GATE.md) | Manifest SHA-256 (recomputed) | Equals sidecar | Files listed / valid | EXECUTOR_BRIEF.md listed | `_work/` listed |\n|---|---|---|---|---:|---|---|')
for r in REG:
    c=r['capsule_id']
    A(f"| {c} | {r['case_gate']} | `{r['case_freeze_manifest_sha256_recomputed']}` | {'yes' if r['case_freeze_manifest_sha256_recomputed']==r['case_freeze_manifest_sidecar_sha256'] else 'NO'} | {r['case_manifest_files_listed']} / {r['case_manifest_files_valid']} | {'yes' if inman[c][0] else 'no'} | {'yes' if inman[c][1] else 'no (excluded)'} |")
A('\nThe orchestrator audit lists the same four manifest hashes (`7fd01ed8...`, `84647523...`, `160217c1...`, `3dc9add6...`). Each case directory contains, beside the manifested files, only the manifest, its sidecar and an unlisted `_work/` scratch folder (not opened by the assembler). `EXECUTOR_BRIEF.md` is listed in each case manifest (25 files per case).\n')
A('## 4. Same frozen method across cases\n')
A('| Case | RUN_METADATA protocol_version and manifest hash | EXECUTION_PROVENANCE names manifest hash and addendum | RUN_METADATA files_read lists the six method documents | Method-document hashes cited in provenance equal recomputed |\n|---|---|---|---|---:|')
for c in cases: A(f"| {c} | {P_(method[c][0])} | {P_(method[c][1])} | {P_(method[c][2])} | {method[c][3]} of 6 |")
A('\nRecomputed SHA-256 of the six method documents: '+'; '.join(f'{d} `{dh_hash[d][:16]}...`' for d in docs)+'. The C2_CBAM and AI_AI_ACT provenance files list the six document hashes and they equal the recomputed values; the C1_SCF and O_DIR_86_361 provenance files state the protocol manifest hash without listing per-document hashes, and each of those cases records (as the others do) that the manifest hash was taken from the execution addendum, not recomputed by the executor (the manifest file was outside the executors\' allow-list). The assembler recomputed it (section 2).\n')
A('## 5. Legal-source hashes\n')
A('| Case | Recomputed SHA-256 of capsule LEGAL_SOURCE | Equals CASE_METADATA, capsule register, W_DECLARATION |\n|---|---|---|')
for c in cases: A(f"| {c} | `{legal[c][0]}` | {P_(legal[c][1])} |")
A('\nOnly the byte hash of each LEGAL_SOURCE file was computed; the files were not opened or read.\n')
A('## 6. Table headers\n')
A('For each case all 19 CSV tables were compared with the field lists of `RGAM_PAIRED_DATA_DICTIONARY_v1_0.md` sections 3.1-3.19 (the frozen header definition; the capsule `OUTPUT_TEMPLATES/` are outside the assembler\'s allow-list and were not read; the dictionary states the templates are generated identically).\n')
A('| Case | Header mismatches | Ragged rows | Files without UTF-8 BOM |\n|---|---|---|---|')
for c in cases: A(f"| {c} | {', '.join(hdr[c][0]) or 'none'} | {', '.join(hdr[c][2]) or 'none'} | {', '.join(hdr[c][1]) or 'none'} |")
A('\n## 7. Data-dictionary integrity rules 1-10 (independent recomputation)\n')
A('Rules checked: (1) unit ids exist, screened = inventoried; (2) every NA/PD/QR/EXT/ST traces to statements and units, recital_only handling; (3) id references resolve and `accountable_via_qr_ids` point to accountability relations; (4) every QR has origin and counterpart, no prohibition modality, no material_establishment_evidenced; (5) provenance rows exist and derived records state a rule and cite two units or a cross-reference; (6) INTEGRATED/OVERLAPPING architecture candidates are queued and INTEGRATED requires I1-I4 SATISFIED; (7) closure-dependent properties resolve and UNDETERMINED closure forces `undetermined`; (8) every EXT is `not_checked` and `outside_corpus_not_expanded`; (9) HQ human columns blank; (10) trace chains resolve.\n')
A('| Case | Failures found |\n|---|---:|')
for c in cases: A(f"| {c} | {len(integ[c])} |")
A('\nThe assembler\'s check does not re-verify evidence spans against the legal source text (the source files were not read); that verification is recorded by each case executor in its own CASE_QA_REPORT.md (as recorded).\n')
A('## 8. Family files: internal consistency\n')
for k in ['family_register','family_queue','human_family']: A(f"- {k}: {P_(R[k][0])} - {R[k][1]}")
A('')
A('| Case | INSTRUMENT_LEVEL_SUMMARY record_counts entries checked | Mismatches against recomputed rows |\n|---|---:|---|')
for c in cases: A(f"| {c} | {ilsmis[c][0]} | {ilsmis[c][1] or 'none'} |")
A('\nThe combined queue (`RGAM_FAMILY_HUMAN_REVIEW_QUEUE.csv`) preserves every case-level item as its own row (no merging, collapsing or adjudication); it carries the original 12 columns unchanged, plus `family_hq_id`, `trigger_category` (copy of `trigger_code`), `recurring_category_label` (assembler-assigned descriptive label), `source_file`, `source_row_number` and `source_row_sha256`. The register file stores the E/P/R/S/A stratum mapping in its header comment lines.\n')
A('### 8.1 Observations on the frozen case files (reported, not corrected; no frozen file was modified)\n')
A('- O_DIR_86_361: DEV numbering cited in `EXECUTION_PROVENANCE.md` (trace-generator choice "logged DEV-14"), `CASE_QA_REPORT.md` section D (C5) and `CASE_GATE.md` (corrections "logged (DEV-15)") does not match the PROTOCOL_DEVIATION_LOG rows (trace-selection convention is DEV-13; recovery run is DEV-14; evidence-span convention is DEV-15).\n- C2_CBAM: `INSTRUMENT_LEVEL_SUMMARY.record_counts` lists 13 of the 19 tables; the other cases list different subsets. All listed numbers equal the recomputed counts.\n- AI_AI_ACT `RUN_METADATA.model_parameters` records reasoning effort as NOT_EXPOSED while C1_SCF, C2_CBAM and the O_DIR_86_361 recovery run record `reasoning_effort=10` as displayed in their invocation context.\n- C2_CBAM: `PROTOCOL_DEVIATION_LOG` rows carry `gap_ref` GAP-01 on two rows and GAP-02 as an examined-not-used entry; O_DIR_86_361 has no GAP-02 row (its QA report states the gap did not arise).\n- CASE_GATE.md formatting differs (bold token in C1_SCF, AI_AI_ACT and O_DIR_86_361; plain token in C2_CBAM); all contain the token `RGAM_CASE_FROZEN` on a line of its own.\n')
A('## 9. Family assembler isolation statement\n')
A('**Read in full or in part with the Read tool or shell (content seen):** the assembler brief (`_orchestrator/FAMILY_ASSEMBLER_BRIEF.md`); from `11_RGAM_PROTOCOL_FREEZE/`: `RGAM_CASE_OUTPUT_SCHEMA.md`, `RGAM_EXECUTION_GAP_DECISIONS_v1_0.md`, `RGAM_BLINDNESS_AND_ACCESS_POLICY.md`, `RGAM_EXECUTION_CAPSULE_REGISTER.csv`, `RGAM_PAIRED_DATA_DICTIONARY_v1_0.md`, the two SHA-256 sidecar files, `RGAM_PROTOCOL_FREEZE_MANIFEST.csv` (first lines, grep of the rows for the six method documents and CASE_METADATA files, and parsed in full by script for hash verification), and the four `CAPSULES/<id>/CASE_METADATA.json`; `_orchestrator/ISOLATION_AUDIT_SUMMARY.md`; in each of the four case directories the 19 schema tables (by scripts, plus targeted printing of HUMAN_REVIEW_QUEUE, PROTOCOL_DEVIATION_LOG, INSTRUMENT_LEVEL_SUMMARY, RUN_METADATA), `ACCESS_AND_CONTAMINATION_LOG.md`, `EXECUTION_PROVENANCE.md`, `CASE_QA_REPORT.md`, `CASE_GATE.md`, the two manifest files, and `CASE_RGAM_REPORT.md` (headings and keyword lines by grep only; not read in full).\n')
A('**Hashed by script only (bytes read for SHA-256; content not read or displayed):** the four `LEGAL_SOURCE` files; the files listed in the protocol manifest that are not named above (this includes `RGAM_PAIRED_EXECUTION_PROTOCOL_v1_0.md` and `RGAM_PAIRED_DECISION_RULES_v1_0.md`, which are on the allow-list but were not read, and files outside the allow-list such as the PRECEDENCE register, SOURCE_AUTHORITY register, protocol gate and QA files, capsule READMEs and output templates).\n')
A('**Names only (directory listings; contents not opened):** a listing of `12_RGAM_CASE_EXECUTION/` (parent of the case directories) exposed the names of the `_RECOVERY_*` folders and the orchestration log file, which are on the do-not-read/do-not-list list; a listing of `11_RGAM_PROTOCOL_FREEZE/` and of `CAPSULES/` exposed names of non-allow-listed protocol files; a recursive file enumeration of the four case directories was filtered to drop `_work/` paths before display, so only the existence of each `_work/` folder was seen (its contents were not opened or displayed). The harness also supplied, with the invocation, a repository status snapshot listing top-level folder and file names (including names on the deny-list), the subjects of recent commits and the names of two additional working directories; none was opened.\n')
A('**Not done:** no V8 material, no R2/R3/R4/V8-COMP-01 or historical or pilot material, no case-selection or ranking material, no `_RECOVERY_*` content, no orchestration-log content, no memory, CLAUDE.md or settings file, no web access, no repository search; no frozen file was modified; writes were made only under `12_RGAM_CASE_EXECUTION/FAMILY/` (including a `_work/` scratch folder of assembly scripts, excluded from the family manifest). The assembler did not read executor transcripts; statements about executor access rest on the case access logs and the orchestrator\'s non-substantive audit summary.\n')
A('**Answer to "read anything outside the allow-list": no file content outside the allow-list was read; the name-only exposures and byte-hashing listed above are disclosed as deviations from a strict reading of the brief.**\n')
open(F+'/RGAM_EXECUTION_QA_REPORT.md','w',encoding='utf-8',newline='\n').write('\n'.join(S))
open(F+'/_work/allok.txt','w').write('1' if allok else '0')
print('checks',nchk,'fail',nfail, [k for k,v in R.items() if not v[0]])
