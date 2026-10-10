"""Write PACKAGE_NOTE.txt and the package manifest, and verify copy integrity."""
import csv, hashlib, os

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PKG = os.path.join(REPO, 'ENVIO_R4_TO_DAVID')
MAP = os.path.join(PKG, '00_START_HERE', 'R4_TRACEABILITY_MAP.csv')
OUT = os.path.join(PKG, '00_START_HERE', 'R4_PACKAGE_MANIFEST.csv')

NOTE = (
    "This folder contains the complete traceable package for the R4 digital "
    "structural-validation round. Start with 00_START_HERE/README_R4_FOR_DAVID.md. The final "
    "consolidated delivery dataset is 01_FINAL_R4_DATASET/R4_Digital_Validation_Dashboard.xlsx. "
    "Supporting folders preserve the source data, methodological decisions, human adjudications, "
    "AI-assisted validation, model provenance, freeze records, integrity hashes and "
    "reproducibility materials used to produce the final R4 results.\n"
    "\n"
    "Scope: R4 digital structural validation round. This is not the Green x Digital governance "
    "comparison.\n"
    "\n"
    "RIT_CODING             = NOT_STARTED\n"
    "MECHANISM_CODING       = NOT_STARTED\n"
    "ROTEM_CODING_CONSULTED = NO\n"
    "R4_3                   = NOT_STARTED\n"
    "CORPUS_WIDE_REPAIR     = NOT_EXECUTED\n"
    "\n"
    "Human researcher and final methodological authority: Igor Caires Machado.\n"
    "AI systems assisted with extraction, structural review, QA and sensitivity analysis; "
    "AI output is not autonomous ground truth.\n"
)

DOC_CATEGORY = {
    'README_R4_FOR_DAVID.md': ('PACKAGE_DOCUMENTATION', 'AUTHORITATIVE_FINAL'),
    'R4_COMPLETE_WORK_NOTE.md': ('PACKAGE_DOCUMENTATION', 'AUTHORITATIVE_FINAL'),
    'R4_FILE_GUIDE.md': ('PACKAGE_DOCUMENTATION', 'AUTHORITATIVE_FINAL'),
    'R4_TRACEABILITY_MAP.csv': ('PACKAGE_DOCUMENTATION', 'AUTHORITATIVE_FINAL'),
    'R4_PACKAGE_MANIFEST.csv': ('PACKAGE_DOCUMENTATION', 'AUTHORITATIVE_FINAL'),
    'PACKAGE_NOTE.txt': ('PACKAGE_DOCUMENTATION', 'AUTHORITATIVE_FINAL'),
}


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest().upper()


def main():
    with open(os.path.join(PKG, 'PACKAGE_NOTE.txt'), 'w', encoding='utf-8') as fh:
        fh.write(NOTE)

    tmap = {r['PACKAGE_PATH']: r for r in csv.DictReader(open(MAP, encoding='utf-8-sig'))}

    # verify every copied evidence file still matches its recorded hash
    bad = []
    for rel, r in tmap.items():
        p = os.path.join(PKG, rel.replace('/', os.sep))
        if not os.path.exists(p):
            bad.append((rel, 'MISSING_IN_PACKAGE'))
        elif sha(p) != r['SHA256']:
            bad.append((rel, 'COPY_INTEGRITY_FAILURE'))

    rows = []
    for root, _, files in os.walk(PKG):
        for f in sorted(files):
            p = os.path.join(root, f)
            rel = os.path.relpath(p, PKG).replace(os.sep, '/')
            if rel in tmap:
                cat = tmap[rel]['ARTIFACT_TYPE']
                status = tmap[rel]['EVIDENCE_LEVEL']
            elif f in DOC_CATEGORY:
                cat, status = DOC_CATEGORY[f]
            elif f.startswith('README_'):
                cat, status = 'PACKAGE_DOCUMENTATION', 'AUTHORITATIVE_FINAL'
            else:
                cat, status = 'PACKAGE_DOCUMENTATION', 'SUPPORTING_EVIDENCE'
            rows.append({'RELATIVE_PATH': rel, 'FILE_NAME': f,
                         'SIZE_BYTES': os.path.getsize(p), 'SHA256': sha(p),
                         'CATEGORY': cat, 'AUTHORITATIVE_STATUS': status})

    cols = ['RELATIVE_PATH', 'FILE_NAME', 'SIZE_BYTES', 'SHA256', 'CATEGORY',
            'AUTHORITATIVE_STATUS']
    with open(OUT, 'w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=cols, quoting=csv.QUOTE_ALL, lineterminator='\r\n')
        w.writeheader()
        w.writerows(rows)

    total = sum(r['SIZE_BYTES'] for r in rows)
    print(f'package files : {len(rows)}')
    print(f'package bytes : {total:,} ({total / 1048576:.1f} MB)')
    print(f'integrity     : {"OK - all copies match source hashes" if not bad else bad}')
    from collections import Counter
    print('by status     :', dict(Counter(r['AUTHORITATIVE_STATUS'] for r in rows)))
    return len(rows), bad


if __name__ == '__main__':
    main()
