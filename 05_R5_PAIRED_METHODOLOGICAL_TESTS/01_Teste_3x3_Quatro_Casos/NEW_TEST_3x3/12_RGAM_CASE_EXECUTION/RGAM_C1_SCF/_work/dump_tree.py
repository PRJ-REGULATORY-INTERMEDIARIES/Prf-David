# MECHANICAL: structural text dump
import warnings,re,sys
warnings.filterwarnings("ignore")
from bs4 import BeautifulSoup
p="G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_C1_SCF/LEGAL_SOURCE/32023R0955_official_en.html"
soup=BeautifulSoup(open(p,encoding='utf-8').read(),'lxml')
def norm(t): return re.sub(r'\s+',' ',t.replace('\xa0',' ')).strip()
def walk(el,ind,out):
    for c in el.children:
        if getattr(c,'name',None) is None: continue
        if c.name=='p':
            out.append('  '*ind+'P: '+norm(c.get_text(' ')))
        elif c.name=='table':
            rows=c.find_all('tr',recursive=False) or c.find_all('tr',recursive=True)[:0]
            tb=c.find('tbody',recursive=False)
            rows=(tb or c).find_all('tr',recursive=False)
            out.append('  '*ind+f'TABLE rows={len(rows)}')
            for r in rows:
                tds=r.find_all('td',recursive=False)
                out.append('  '*(ind+1)+f'ROW cells={len(tds)}')
                for td in tds:
                    out.append('  '*(ind+2)+'CELL')
                    walk(td,ind+3,out)
        elif c.name in('div','figure','a','span'):
            out.append('  '*ind+f'<{c.name} id={c.get("id","")}>')
            walk(c,ind+1,out)
out=[]
body=soup.body
walk(body,0,out)
open('tree_dump.txt','w',encoding='utf-8').write('\n'.join(out))
print(len(out))
