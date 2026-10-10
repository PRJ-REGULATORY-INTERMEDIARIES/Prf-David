import hashlib, csv, os, json, io
B='G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3'
def sha(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for ch in iter(lambda:f.read(1<<20),b''): h.update(ch)
    return h.hexdigest()
P=B+'/11_RGAM_PROTOCOL_FREEZE'
print('protocol manifest', sha(P+'/RGAM_PROTOCOL_FREEZE_MANIFEST.csv'))
print('gap', sha(P+'/RGAM_EXECUTION_GAP_DECISIONS_v1_0.md'))
rows=list(csv.DictReader(open(P+'/RGAM_PROTOCOL_FREEZE_MANIFEST.csv',encoding='utf-8-sig')))
bad=0
for r in rows:
    p=P+'/'+r['relative_path']
    if not os.path.exists(p) or sha(p)!=r['sha256'] or os.path.getsize(p)!=int(r['bytes']):
        bad+=1; print('BAD',r['relative_path'])
print('protocol files',len(rows),'bad',bad)
C=B+'/12_RGAM_CASE_EXECUTION'
for c in ['RGAM_C1_SCF','RGAM_C2_CBAM','RGAM_AI_AI_ACT','RGAM_O_DIR_86_361']:
    d=C+'/'+c
    m=sha(d+'/CASE_FREEZE_MANIFEST.csv')
    exp=open(d+'/CASE_FREEZE_MANIFEST_SHA256.txt').read().split()[0]
    rs=list(csv.DictReader(open(d+'/CASE_FREEZE_MANIFEST.csv',encoding='utf-8-sig')))
    bad=[r['relative_path'] for r in rs if not os.path.exists(d+'/'+r['relative_path']) or sha(d+'/'+r['relative_path'])!=r['sha256'] or os.path.getsize(d+'/'+r['relative_path'])!=int(r['bytes'])]
    listed={r['relative_path'] for r in rs}
    actual={f for f in os.listdir(d) if os.path.isfile(d+'/'+f)}
    print(c,m,m==exp,len(rs),'bad',bad,'unlisted files',sorted(actual-listed-{'CASE_FREEZE_MANIFEST.csv','CASE_FREEZE_MANIFEST_SHA256.txt'}),'listed-missing',sorted(listed-actual), 'dirs',[f for f in os.listdir(d) if os.path.isdir(d+'/'+f)])
    meta=json.load(open(P+'/CAPSULES/'+c+'/CASE_METADATA.json',encoding='utf-8'))
    print(' meta',meta)
    ls=[f for f in os.listdir(P+'/CAPSULES/'+c+'/LEGAL_SOURCE')]
    for f in ls: print(' legal',f,sha(P+'/CAPSULES/'+c+'/LEGAL_SOURCE/'+f))
