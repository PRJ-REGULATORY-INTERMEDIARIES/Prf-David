import json,sys
u=json.load(open('units.json',encoding='utf-8'))
a,b=int(sys.argv[1]),int(sys.argv[2]); L=int(sys.argv[3]) if len(sys.argv)>3 else 520
for x in u:
    i=x['unit_id'][15:]
    if i.startswith('REC'):
        n=int(i[3:])
        if a<=n<=b:
            t=x['text']
            print(i, t[:L]+(' ...[+%d]'%(len(t)-L) if len(t)>L else ''))
