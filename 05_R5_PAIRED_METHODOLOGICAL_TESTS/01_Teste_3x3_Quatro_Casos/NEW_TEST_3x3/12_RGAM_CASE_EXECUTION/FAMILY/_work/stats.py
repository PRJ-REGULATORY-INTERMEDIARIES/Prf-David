from lib import *
import hashlib, os, json
from collections import Counter
def sha_file(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for ch in iter(lambda:f.read(1<<20),b''): h.update(ch)
    return h.hexdigest()
EXPECT_PM='9ca016b97289b39049dc099b265c20662c1ebc05e86bc720f0fbe80e0bac5932'
EXPECT_GAP='b9dc184ebc857e5e3aae85ea5e1b5ac28f64c9947086b2bbe763a3b936e02da4'
STRATA={'E':['SOURCE_UNIT_INVENTORY','INSTITUTIONAL_STATEMENTS'],'P':['NORMATIVE_ASSIGNMENTS','POSITIONS_AND_DEVICES'],'R':['QUALIFIED_RELATIONS','EXTERNAL_REFERENCES'],'S':['SUBCONFIGURATIONS'],'A':['ARCHITECTURE_CANDIDATES']}
EXEC_IDS={ # from ISOLATION_AUDIT_SUMMARY.md
 'RGAM_C1_SCF':('a773412851ad46032',''),
 'RGAM_C2_CBAM':('aee1506e1d0e70177',''),
 'RGAM_AI_AI_ACT':('ad615b1d8063b1df2 (fresh recovery run)','ad1c4f939eaef025b (interrupted at 12 calls; blank templates only; not reused)'),
 'RGAM_O_DIR_86_361':('a04521a3bcdf0d1d0 (fresh recovery run)','a86c431b77ac102f0 (interrupted; analytical tables produced; later adopted as partial state)')}
def gather():
    D={}
    for c in cases:
        T={t:load(c,t)[1] for t in tables}
        meta=json.load(open(f'{P}/CAPSULES/{c}/CASE_METADATA.json',encoding='utf-8'))
        legal=f"{P}/CAPSULES/{c}/"+meta['controlling_source_file']
        log=open(f'{C}/{c}/ACCESS_AND_CONTAMINATION_LOG.md',encoding='utf-8').read()
        m=re.search(r'\*\*(CLEAN|[A-Z_ ]+)\*\*',log[log.find('ontamination status'):])
        D[c]=dict(T=T,meta=meta,legal=legal,log=log,contam=m.group(1) if m else 'UNPARSED')
    return D
