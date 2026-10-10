# MECHANICAL: verify every text node of the source appears in some unit text
import warnings,re,json
warnings.filterwarnings("ignore")
from bs4 import BeautifulSoup, NavigableString
SRC="G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_C1_SCF/LEGAL_SOURCE/32023R0955_official_en.html"
soup=BeautifulSoup(open(SRC,encoding='utf-8').read(),'lxml')
def norm(t): return re.sub(r'\s+',' ',t.replace('\xa0',' ')).strip()
units=json.load(open('units.json',encoding='utf-8'))
big=' '.join(u['text'] for u in units)
bign=re.sub(r'\s+','',big)
miss=[]
tot=0
for t in soup.body.find_all(string=True):
    s=norm(str(t))
    if not s: continue
    tot+=1
    if t.parent.name in ('script','style'): continue
    k=re.sub(r'\s+','',s)
    if k not in bign:
        miss.append(s[:120])
print('text nodes',tot,'missing',len(miss))
for m in miss[:60]: print(' -',m)
