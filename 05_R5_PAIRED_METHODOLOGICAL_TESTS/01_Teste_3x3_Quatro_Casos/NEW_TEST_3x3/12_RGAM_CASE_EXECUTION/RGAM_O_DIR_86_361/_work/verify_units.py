# Independent mechanical completeness check of units.json against the frozen source (recovery run).
import re, html, json
SRC="G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_O_DIR_86_361/LEGAL_SOURCE/31986L0361_official_en.html"
raw=open(SRC,encoding='utf-8').read()
body=raw.split('<TXT_TE>')[1].split('</TXT_TE>')[0]
norm=lambda s: re.sub(r'\s+',' ',html.unescape(s)).strip()
txt=norm(re.sub(r'<[^>]+>',' ',body))
units=json.load(open('units.json',encoding='utf-8'))
pos=0; rest=[]
for u in units:
    t=u['text']
    i=txt.find(t,pos)
    if i<0:
        # multi-paragraph units (joined with space) are still substrings of txt since p-tags became spaces
        print('NOT FOUND IN ORDER',u['unit_id']); continue
    rest.append(txt[pos:i]); pos=i+len(t)
rest.append(txt[pos:])
leftover=' | '.join(x.strip() for x in rest if x.strip())
print('LEFTOVER (should be only labels/headings):')
print(leftover)
print('n units',len(units),'unique ids',len({u['unit_id'] for u in units}))
