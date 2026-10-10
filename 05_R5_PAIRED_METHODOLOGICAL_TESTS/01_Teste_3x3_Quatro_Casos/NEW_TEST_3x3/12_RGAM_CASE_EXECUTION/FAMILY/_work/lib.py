import csv,re,collections,io
B='G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3'
C=B+'/12_RGAM_CASE_EXECUTION'
P=B+'/11_RGAM_PROTOCOL_FREEZE'
cases=['RGAM_C1_SCF','RGAM_C2_CBAM','RGAM_AI_AI_ACT','RGAM_O_DIR_86_361']
tables=['W_DECLARATION','SOURCE_UNIT_INVENTORY','UNIT_SCREENING','INSTITUTIONAL_STATEMENTS','NORMATIVE_ASSIGNMENTS','POSITIONS_AND_DEVICES','QUALIFIED_RELATIONS','EXTERNAL_REFERENCES','SUBCONFIGURATIONS','ARCHITECTURE_CANDIDATES','PROPERTY_REGISTER','CLOSURE_REGISTER','PROVENANCE_LINKS','UNCERTAINTY_LOG','HUMAN_REVIEW_QUEUE','TRACE_DEMONSTRATIONS','INSTRUMENT_LEVEL_SUMMARY','PROTOCOL_DEVIATION_LOG','RUN_METADATA']
def load(c,t):
    f=open(f'{C}/{c}/{t}.csv',encoding='utf-8-sig',newline='')
    rd=csv.reader(f); rows=list(rd)
    return rows[0],[dict(zip(rows[0],r)) for r in rows[1:]],rows[1:]
def dict_headers():
    txt=open(P+'/RGAM_PAIRED_DATA_DICTIONARY_v1_0.md',encoding='utf-8').read()
    out={}
    for m in re.finditer(r'### 3\.\d+ `(\w+)\.csv`.*?\n(.*?)(?=\n### 3\.|\n## 4)',txt,re.S):
        out[m.group(1)]=re.findall(r'^\| `(\w+)` \|',m.group(2),re.M)
    return out
