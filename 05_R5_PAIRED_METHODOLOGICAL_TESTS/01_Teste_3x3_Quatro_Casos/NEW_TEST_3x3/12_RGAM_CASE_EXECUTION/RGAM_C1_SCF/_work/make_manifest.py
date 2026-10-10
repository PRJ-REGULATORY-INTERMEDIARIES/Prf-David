# MECHANICAL: freeze manifest (relative_path, bytes, sha256) of every file in the case directory except the manifest, its sidecar and _work/
import os, hashlib, csv, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(root)
files = []
for dp, dn, fn in os.walk('.'):
    dn[:] = [d for d in dn if d != '_work']
    for f in fn:
        rel = os.path.relpath(os.path.join(dp, f), '.').replace(os.sep, '/')
        if rel in ('CASE_FREEZE_MANIFEST.csv', 'CASE_FREEZE_MANIFEST_SHA256.txt'):
            continue
        files.append(rel)
files.sort()
with open('CASE_FREEZE_MANIFEST.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f, lineterminator='\r\n')
    w.writerow(['relative_path', 'bytes', 'sha256'])
    for rel in files:
        b = open(rel, 'rb').read()
        w.writerow([rel, len(b), hashlib.sha256(b).hexdigest()])
h = hashlib.sha256(open('CASE_FREEZE_MANIFEST.csv', 'rb').read()).hexdigest()
open('CASE_FREEZE_MANIFEST_SHA256.txt', 'w', encoding='utf-8', newline='').write(h + '  CASE_FREEZE_MANIFEST.csv\r\n')
print(len(files))
print(h)
