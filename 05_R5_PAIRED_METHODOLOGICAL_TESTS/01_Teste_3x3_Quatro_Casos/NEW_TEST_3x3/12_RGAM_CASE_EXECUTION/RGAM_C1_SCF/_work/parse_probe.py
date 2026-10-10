# MECHANICAL: structure probe of the capsule source (no analysis)
from bs4 import BeautifulSoup
import re,sys
p="G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_C1_SCF/LEGAL_SOURCE/32023R0955_official_en.html"
soup=BeautifulSoup(open(p,encoding='utf-8').read(),'lxml')
def norm(t): return re.sub(r'\s+',' ',t.replace('\xa0',' ')).strip()
def depth(el):
    d=0
    for a in el.parents:
        if a.name=='table': d+=1
    return d
# For each article: list direct children kinds
for art in soup.select('div[id^="art_"]'):
    if '.' in art['id']: continue
    kids=[]
    for c in art.find_all(['div','table','p'],recursive=False):
        kids.append((c.name,c.get('id',''),c.get('class')))
    print(art['id'],kids[:12],len(kids))
