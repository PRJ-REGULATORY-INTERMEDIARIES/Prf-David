import json,re,hashlib
P=json.load(open('paras.json',encoding='utf-8'))
def strip_label(t):
    return re.sub(r'^(\d+\.\s+|\([a-z]\)\s+|-\s+)','',t)
units=[]
def add(uid,cls,art,para,point,parent,loc,text,anchor):
    units.append(dict(unit_id=uid,structure_class=cls,article_or_annex_no=art,paragraph=para,point=point,parent_unit_id=parent,locator_text=loc,text=re.sub(r'\s+',' ',text).strip(),source_anchor=anchor))
OP='OPERATIVE_ARTICLE'
# formal preamble
add('FRM1','HEADING_ONLY','','','','','Title block of the directive',' '.join(P[1:5]),'p1-4')
add('FRM2','FORMAL_OTHER','','','','','Enacting formula',P[5],'p5')
for i,k in enumerate(range(6,10),1):
    add(f'FRM{2+i}','FORMAL_OTHER','','','','',f'Citation {i} (Having regard)',P[k],f'p{k}')
for i,k in enumerate(range(10,24),1):
    add(f'REC{i}','RECITAL','',str(i),'','',f'Recital {i} (unnumbered Whereas clause no. {i})',P[k],f'p{k}')
add('FRM7','FORMAL_OTHER','','','','','Adoption formula',P[24],'p24')
add('A1.P0',OP,'1','P0','','','Article 1',P[26],'p26')
add('A2.P0',OP,'2','P0','','','Article 2 (chapeau)',P[28],'p28')
for n,k in zip(range(1,15),range(29,43)):
    add(f'A2.P0.pt{n}',OP,'2','P0',str(n),'A2.P0',f'Article 2, point {n}',strip_label(P[k]),f'p{k}')
t=P[43]
i=t.index('; 16. ')
add('A2.P0.pt15',OP,'2','P0','15','A2.P0','Article 2, point 15',strip_label(t[:i+1]),'p43[part1]')
add('A2.P0.pt16',OP,'2','P0','16','A2.P0','Article 2, point 16',t[i+len('; 16. '):],'p43[part2]')
add('A2.P0.pt17',OP,'2','P0','17','A2.P0','Article 2, point 17',strip_label(P[44]),'p44')
for n,k in zip(range(1,5),range(45,49)):
    add(f'A2.P0.pt17.dash{n}',OP,'2','P0',f'17.dash{n}','A2.P0.pt17',f'Article 2, point 17, indent {n}',strip_label(P[k]),f'p{k}')
add('A3.P0',OP,'3','P0','','','Article 3',P[50],'p50')
add('A4.P0',OP,'4','P0','','','Article 4 (chapeau)',P[52],'p52')
add('A4.P0.pt1',OP,'4','P0','1','A4.P0','Article 4, point 1',strip_label(P[53]),'p53')
for n,k in zip(range(1,4),range(54,57)):
    add(f'A4.P0.pt1.dash{n}',OP,'4','P0',f'1.dash{n}','A4.P0.pt1',f'Article 4, point 1, indent {n}',strip_label(P[k]),f'p{k}')
add('A4.P0.pt2',OP,'4','P0','2','A4.P0','Article 4, point 2',strip_label(P[57]),'p57')
add('A5.P1',OP,'5','P1','','','Article 5(1)',strip_label(P[59]),'p59')
add('A5.P2',OP,'5','P2','','','Article 5(2) (chapeau)',strip_label(P[60]),'p60')
for l,k in zip('abc',range(61,64)):
    add(f'A5.P2.pt{l}',OP,'5','P2',l,'A5.P2',f'Article 5(2)({l})',strip_label(P[k]),f'p{k}')
add('A5.P2.sub2',OP,'5','P2','sub2','A5.P2','Article 5(2), final subparagraph (after point (c))',P[64],'p64')
add('A5.P3',OP,'5','P3','','','Article 5(3)',strip_label(P[65]),'p65')
add('A5.P4',OP,'5','P4','','','Article 5(4)',strip_label(P[66]),'p66')
add('A6.P1',OP,'6','P1','','','Article 6(1), first subparagraph',strip_label(P[68]),'p68')
add('A6.P1.sub2',OP,'6','P1','sub2','A6.P1','Article 6(1), second subparagraph',P[69],'p69')
t=P[70]; j=t.index(' 3. The common')
add('A6.P2',OP,'6','P2','','','Article 6(2)',strip_label(t[:j]),'p70[part1]')
add('A6.P3',OP,'6','P3','','','Article 6(3), first subparagraph',t[j+len(' 3. '):],'p70[part2]')
add('A6.P3.sub2',OP,'6','P3','sub2','A6.P3','Article 6(3), second subparagraph',P[71],'p71')
add('A7.P1',OP,'7','P1','','','Article 7(1)',strip_label(P[73]),'p73')
add('A7.P2',OP,'7','P2','','','Article 7(2)',strip_label(P[74]),'p74')
add('A7.P3',OP,'7','P3','','','Article 7(3)',strip_label(P[75]),'p75')
add('A7.P4',OP,'7','P4','','','Article 7(4) (chapeau)',strip_label(P[76]),'p76')
add('A7.P4.pta',OP,'7','P4','a','A7.P4','Article 7(4)(a)',strip_label(P[77]),'p77')
add('A7.P4.ptb',OP,'7','P4','b','A7.P4','Article 7(4)(b)',strip_label(P[78]),'p78')
add('A7.P4.sub2',OP,'7','P4','sub2','A7.P4','Article 7(4), subparagraph following point (b), first',P[79],'p79')
add('A7.P4.sub3',OP,'7','P4','sub3','A7.P4','Article 7(4), subparagraph following point (b), second',P[80],'p80')
add('A7.P5',OP,'7','P5','','','Article 7(5)',strip_label(P[81]),'p81')
add('A8.P1',OP,'8','P1','','','Article 8(1) (chapeau)',strip_label(P[83]),'p83')
add('A8.P1.pta',OP,'8','P1','a','A8.P1','Article 8(1)(a)',strip_label(P[84]),'p84')
add('A8.P1.ptb',OP,'8','P1','b','A8.P1','Article 8(1)(b)',strip_label(P[85]),'p85')
add('A8.P1.sub2',OP,'8','P1','sub2','A8.P1','Article 8(1), final subparagraph',P[86],'p86')
t=P[87]; j=t.index(' 3. If the reasons')
add('A8.P2',OP,'8','P2','','','Article 8(2)',strip_label(t[:j]),'p87[part1]')
add('A8.P3',OP,'8','P3','','','Article 8(3), first subparagraph',t[j+len(' 3. '):],'p87[part2]')
add('A8.P3.sub2',OP,'8','P3','sub2','A8.P3','Article 8(3), second subparagraph',P[88],'p88')
add('A8.P3.sub3',OP,'8','P3','sub3','A8.P3','Article 8(3), third subparagraph',P[89],'p89')
add('A8.P4',OP,'8','P4','','','Article 8(4)',strip_label(P[90]),'p90')
add('A8.P5',OP,'8','P5','','','Article 8(5)',strip_label(P[91]),'p91')
add('A9.P0',OP,'9','P0','','','Article 9',P[93],'p93')
add('A10.P0',OP,'10','P0','','','Article 10',P[95],'p95')
add('A11.P1',OP,'11','P1','','','Article 11(1)',strip_label(P[97]),'p97')
add('A11.P2',OP,'11','P2','','','Article 11(2)',strip_label(P[98]),'p98')
add('A12.P0',OP,'12','P0','','','Article 12',P[100],'p100')
add('FRM8','FORMAL_OTHER','','','','','Date, place and signature block',' '.join(P[101:105]),'p101-104')
for i,k in enumerate(range(105,109),1):
    add(f'FRM{8+i}','FORMAL_OTHER','','','','',f'Footnote ({i})',P[k],f'p{k}')
for u in units: u['text_sha256']=hashlib.sha256(u['text'].encode('utf-8')).hexdigest()
json.dump(units,open('units.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(units))
with open('units_view.txt','w',encoding='utf-8') as f:
    for u in units: f.write(u['unit_id']+' | '+u['text']+'\n')
