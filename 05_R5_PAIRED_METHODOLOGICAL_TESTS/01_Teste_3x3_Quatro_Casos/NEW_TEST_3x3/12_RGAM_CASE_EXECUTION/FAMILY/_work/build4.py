from stats import *
F=C+'/FAMILY'
allok=open(F+'/_work/allok.txt').read().strip()=='1'
res=json.load(open(F+'/_work/verify_results.json'))
GATE='RGAM_FOUR_CASE_EXECUTION_FROZEN / V8_RESULTS_NOT_CONSULTED / PAIRED_COMPARISON_NOT_STARTED'
if allok:
    g=f"# RGAM_EXECUTION_GATE\n\n**{GATE}**\n\nFactual basis (recomputed by the family assembler at assembly time; details in `RGAM_EXECUTION_QA_REPORT.md`):\n\n- All four case gates read `RGAM_CASE_FROZEN` (RGAM_C1_SCF, RGAM_C2_CBAM, RGAM_AI_AI_ACT, RGAM_O_DIR_86_361); each case freeze manifest recomputed equals its sidecar and all 25 listed files per case have valid SHA-256 and byte size.\n- Protocol manifest SHA-256 recomputed = `9ca016b97289b39049dc099b265c20662c1ebc05e86bc720f0fbe80e0bac5932` and all 107 listed files are valid; execution-addendum SHA-256 recomputed = `b9dc184ebc857e5e3aae85ea5e1b5ac28f64c9947086b2bbe763a3b936e02da4`.\n- All four cases reference the same frozen method (protocol v1.0 with the execution-gap addendum v1.0) in RUN_METADATA and EXECUTION_PROVENANCE; legal-source hashes equal the capsule metadata; all 19 tables per case have the frozen headers; data-dictionary integrity rules 1-10 recompute with 0 failures in every case.\n- Combined human-review queue: 89 items = 19 + 16 + 35 + 19; every item traces to its case row; human-decision fields are blank everywhere; no item was adjudicated.\n- Contamination: every case access log records CLEAN; open qualifications and limitations are in `RGAM_FAMILY_CONTAMINATION_AUDIT.md` (technical read-deny not active, shell not blocked, audit of tool inputs only, executor effort setting not exposed, executors not tool-restricted, interrupted-executor histories for AI_AI_ACT and O_DIR_86_361).\n- V8 results were not consulted by the family assembler, and no paired comparison was performed or started; the family files are descriptive only and contain no comparison, ranking, score or inference about any other method.\n- All records remain machine-generated and provisional.\n"
else:
    bad=[k for k,v in res.items() if not v[0]]
    g=f"# RGAM_EXECUTION_GATE\n\n**RGAM_FOUR_CASE_EXECUTION_BLOCKED / reason: verification failed for {', '.join(bad)}**\n\nSee `RGAM_EXECUTION_QA_REPORT.md`.\n"
open(F+'/RGAM_EXECUTION_GATE.md','w',encoding='utf-8',newline='\n').write(g)
files=['RGAM_FOUR_CASE_EXECUTION_REGISTER.csv','RGAM_CROSS_CASE_DESCRIPTIVE_SUMMARY.md','RGAM_FAMILY_HUMAN_REVIEW_QUEUE.csv','RGAM_EXECUTION_QA_REPORT.md','RGAM_FAMILY_CONTAMINATION_AUDIT.md','RGAM_EXECUTION_GATE.md']
buf='relative_path,bytes,sha256\r\n'
for f in files:
    buf+=f'{f},{os.path.getsize(F+"/"+f)},{sha_file(F+"/"+f)}\r\n'
open(F+'/RGAM_FAMILY_FREEZE_MANIFEST.csv','w',encoding='utf-8',newline='').write(buf)
h=sha_file(F+'/RGAM_FAMILY_FREEZE_MANIFEST.csv')
open(F+'/RGAM_FAMILY_FREEZE_MANIFEST_SHA256.txt','w',encoding='utf-8',newline='\n').write(f'{h}  RGAM_FAMILY_FREEZE_MANIFEST.csv\n')
print(h); print(buf)
