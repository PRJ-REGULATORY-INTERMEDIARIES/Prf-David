import re, html, json, sys
SRC="G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_O_DIR_86_361/LEGAL_SOURCE/31986L0361_official_en.html"
raw=open(SRC,encoding='utf-8').read()
body=raw.split('<TXT_TE>')[1].split('</TXT_TE>')[0]
parts=[p for p in re.split(r'<p>',body)]
paras=[]
for p in parts:
    p=p.replace('</p>','')
    t=html.unescape(p)
    t=re.sub(r'\s+',' ',t).strip()
    if t: paras.append(t)
json.dump(paras,open('paras.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
for i,t in enumerate(paras): print(i,len(t),t[:70])
