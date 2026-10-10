# Mechanical: freeze manifest (relative_path, bytes, sha256) of every file in the case directory except the manifest, its sidecar and the _work scratch folder.
import os, hashlib, csv
root = 'G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/12_RGAM_CASE_EXECUTION/RGAM_O_DIR_86_361'
rows = []
for dp, dn, fn in os.walk(root):
    dn[:] = [d for d in dn if d != '_work']
    for f in fn:
        p = os.path.join(dp, f)
        rel = os.path.relpath(p, root).replace(chr(92), '/')
        if rel in ('CASE_FREEZE_MANIFEST.csv', 'CASE_FREEZE_MANIFEST_SHA256.txt'):
            continue
        b = open(p, 'rb').read()
        rows.append((rel, len(b), hashlib.sha256(b).hexdigest()))
rows.sort()
with open(root + '/CASE_FREEZE_MANIFEST.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f, lineterminator='\n')
    w.writerow(['relative_path', 'bytes', 'sha256'])
    w.writerows(rows)
h = hashlib.sha256(open(root + '/CASE_FREEZE_MANIFEST.csv', 'rb').read()).hexdigest()
open(root + '/CASE_FREEZE_MANIFEST_SHA256.txt', 'w', encoding='utf-8').write(h + '  CASE_FREEZE_MANIFEST.csv\n')
print(len(rows), h)
for r in rows:
    print(r[0], r[1])
