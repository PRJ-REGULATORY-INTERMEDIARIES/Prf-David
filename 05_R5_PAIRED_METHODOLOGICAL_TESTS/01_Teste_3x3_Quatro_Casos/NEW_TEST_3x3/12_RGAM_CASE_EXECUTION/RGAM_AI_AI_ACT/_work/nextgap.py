import re,sys
errs=[l.split()[2] for l in open('build/CHECK.txt',encoding='utf-8') if 'not screened' in l]
print(len(errs), errs[:int(sys.argv[1]) if len(sys.argv)>1 else 5])
