"""Build the final SHA-256 integrity manifest for the R4 digital structural validation round."""
import csv, hashlib, os

R4 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(R4, '08_reports', 'R4_DIGITAL_STRUCTURAL_VALIDATION_MANIFEST.csv')

ITEMS = [
    ('B1-03 authoritative output', '03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_ADVANCED_VALIDATION_B1_03.csv', 'AUTHORITATIVE', 'GPT-5.6 Terra High'),
    ('B1-04 authoritative output', '03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_ADVANCED_VALIDATION_B1_04.csv', 'AUTHORITATIVE', 'Claude Opus 5.5 Extra High (researcher-selected)'),
    ('B1-04 pre-correction export', '03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_ADVANCED_VALIDATION_B1_04_v1_PROVENANCE_SUPERSEDED.csv', 'HISTORICAL_PROVENANCE_ONLY', 'Claude'),
    ('B1S action sensitivity audit', '03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_ACTION_SENSITIVITY_AUDIT.csv', 'AUTHORITATIVE', 'Claude Opus 5.5 Extra High (researcher-selected)'),
    ('B1S pre-correction export', '03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_ACTION_SENSITIVITY_AUDIT_v1_PROVENANCE_SUPERSEDED.csv', 'HISTORICAL_PROVENANCE_ONLY', 'Claude'),
    ('B1S sensitivity summary', '03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_ACTION_SENSITIVITY_SUMMARY.csv', 'AUTHORITATIVE', 'Claude'),
    ('Variable redundancy audit', '08_reports/R4_VARIABLE_REDUNDANCY_AUDIT.csv', 'AUTHORITATIVE', 'Claude'),
    ('Final B1 method report', '03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_METHOD_REPORT.md', 'AUTHORITATIVE', 'Terra + Claude'),
    ('David memo', '08_reports/R4_DIGITAL_VALIDATION_MEMO_FOR_DAVID.md', 'AUTHORITATIVE', 'Claude'),
    ('David summary table', '08_reports/R4_DIGITAL_VALIDATION_SUMMARY_FOR_DAVID.csv', 'AUTHORITATIVE', 'Claude'),
    ('David email draft', '08_reports/R4_EMAIL_TO_DAVID_DRAFT.md', 'AUTHORITATIVE', 'Claude'),
    ('Final freeze record', '08_reports/R4_DIGITAL_STRUCTURAL_VALIDATION_FREEZE_RECORD.md', 'AUTHORITATIVE', 'Claude'),
    # supporting frozen context
    ('B1-01 authoritative output', '03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_ADVANCED_VALIDATION.csv', 'AUTHORITATIVE', 'GPT-5.6 Terra High'),
    ('B1-02 authoritative output', '03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_ADVANCED_VALIDATION_B1_02.csv', 'AUTHORITATIVE', 'GPT-5.6 Terra High'),
    ('B1 consolidated summary', '03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_FINAL_SUMMARY.csv', 'AUTHORITATIVE', 'Terra + Claude'),
    ('12-control consolidated diagnostic', '03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_CONTROL_DIAGNOSTIC_CONSOLIDATED.csv', 'AUTHORITATIVE', 'Terra + Claude'),
    ('B1-03 control results', '03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_NO_REPAIR_CONTROL_RESULTS_B1_03.csv', 'AUTHORITATIVE', 'GPT-5.6 Terra High'),
    ('B1-04 control results', '03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_NO_REPAIR_CONTROL_RESULTS_B1_04.csv', 'AUTHORITATIVE', 'Claude'),
    ('New structural diagnostic candidates', '03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_NEW_STRUCTURAL_DIAGNOSTIC_CANDIDATES.csv', 'AUTHORITATIVE', 'Claude'),
    ('B1-03 freeze record', '03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_BATCH_03_FREEZE_RECORD.md', 'AUTHORITATIVE', 'GPT-5.6 Terra High'),
    ('B1-04 freeze record', '03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_BATCH_04_FREEZE_RECORD.md', 'AUTHORITATIVE', 'Claude'),
    ('B1 handoff state', '03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_HANDOFF_STATE.md', 'AUTHORITATIVE', 'Terra + Claude'),
    ('B1 batch run log', '03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_BATCH_RUN_LOG.csv', 'AUTHORITATIVE', 'Terra + Claude'),
    ('Structural extraction (unmodified)', '03_extraction/R4_STRUCTURAL_EXTRACTION.csv', 'IMMUTABLE_SOURCE_UNMODIFIED', 'original extraction'),
]


def main():
    rows = []
    for label, rel, status, prov in ITEMS:
        p = os.path.join(R4, rel.replace('/', os.sep))
        if not os.path.exists(p):
            raise SystemExit(f'missing artifact: {rel}')
        data = open(p, 'rb').read()
        rows.append({
            'ARTIFACT': label,
            'PATH': 'R4_CROSS_DOMAIN_VALIDATION/' + rel,
            'STATUS': status,
            'PROVENANCE': prov,
            'BYTES': len(data),
            'SHA256': hashlib.sha256(data).hexdigest().upper(),
        })
    cols = ['ARTIFACT', 'PATH', 'STATUS', 'PROVENANCE', 'BYTES', 'SHA256']
    with open(OUT, 'w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=cols, quoting=csv.QUOTE_ALL, lineterminator='\r\n')
        w.writeheader()
        w.writerows(rows)
    for r in rows:
        print(f"{r['SHA256'][:16]}  {r['STATUS']:28} {r['ARTIFACT']}")
    print(f'\nmanifest rows={len(rows)}')
    print(f'manifest SHA256={hashlib.sha256(open(OUT, "rb").read()).hexdigest().upper()}')


if __name__ == '__main__':
    main()
