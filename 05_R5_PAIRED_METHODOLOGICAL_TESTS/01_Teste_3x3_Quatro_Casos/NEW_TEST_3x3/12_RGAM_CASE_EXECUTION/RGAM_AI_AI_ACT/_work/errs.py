import sys
n=0
for l in open('build/CHECK.txt',encoding='utf-8'):
    if l.startswith('E ') and 'not screened' not in l:
        print(l.rstrip()); n+=1
print('non-screening errors:',n)
