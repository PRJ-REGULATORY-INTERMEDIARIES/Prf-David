"""Controlled unblinding of the three B1-04 NO_REPAIR controls.

Runs only after R4_2E_B1_BATCH_04_FREEZE_RECORD_001. No substantive B1-04
decision is altered here; each control result restates the already-frozen
adjudication and adds the diagnostic classification.

EXECUTION_ENVIRONMENT      = Claude Code / VS Code extension
RESEARCHER_SELECTED_MODEL  = Claude Opus 5.5 Extra High
RUNTIME_REPORTED_MODEL     = Claude Opus 5 (id claude-opus-5)
MODEL_SELECTION_RUNTIME_MATCH = NOT_VERIFIABLE
"""
import csv, hashlib, os

R4 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BATCH = os.path.join(R4, '03_extraction', 'qa', 'repair', 'R4_2E_B1')
FROZEN = os.path.join(BATCH, 'R4_2E_B1_ADVANCED_VALIDATION_B1_04.csv')
OUTPUT = os.path.join(BATCH, 'R4_2E_B1_NO_REPAIR_CONTROL_RESULTS_B1_04.csv')

COLUMNS = ['CONTROL_DIAGNOSTIC', 'BATCH_ID', 'RECORD_ID', 'CONTROL_RESULT',
           'ADVANCED_DEFECT_PRESENT', 'CONTROL_DEFECT_TYPE', 'CONTROL_DEFECT_SEVERITY', 'NOTE']

RESULTS = [
    {'CONTROL_DIAGNOSTIC': 'NO_REPAIR_CONTROL_DIAGNOSTIC', 'BATCH_ID': 'B1-04',
     'RECORD_ID': 'EXT-000093', 'CONTROL_RESULT': 'DEFECT_FOUND',
     'ADVANCED_DEFECT_PRESENT': 'YES',
     'CONTROL_DEFECT_TYPE': 'PREDICATE_RECONSTRUCTION_ERROR',
     'CONTROL_DEFECT_SEVERITY': 'MODERATE',
     'NOTE': 'Article 42(8) splits the noun phrase "data protection | seals and marks" across the '
             'action and object spans, and the coordinated duty to make the register publicly '
             'available is buried inside the object.'},
    {'CONTROL_DIAGNOSTIC': 'NO_REPAIR_CONTROL_DIAGNOSTIC', 'BATCH_ID': 'B1-04',
     'RECORD_ID': 'EXT-000777', 'CONTROL_RESULT': 'DEFECT_FOUND',
     'ADVANCED_DEFECT_PRESENT': 'YES',
     'CONTROL_DEFECT_TYPE': 'CROSS_SENTENCE_CONTAMINATION',
     'CONTROL_DEFECT_SEVERITY': 'MODERATE',
     'NOTE': 'Recital 136 splits the coordinated object noun phrase and the object then absorbs the '
             'whole following sentence on the rules of procedure, merging two propositions in one record.'},
    {'CONTROL_DIAGNOSTIC': 'NO_REPAIR_CONTROL_DIAGNOSTIC', 'BATCH_ID': 'B1-04',
     'RECORD_ID': 'EXT-000937', 'CONTROL_RESULT': 'DEFECT_FOUND',
     'ADVANCED_DEFECT_PRESENT': 'YES',
     'CONTROL_DEFECT_TYPE': 'PREDICATE_RECONSTRUCTION_ERROR',
     'CONTROL_DEFECT_SEVERITY': 'MODERATE',
     'NOTE': 'Article 112(13) begins the object mid-phrase at "of this Regulation", absorbs the '
             'coordinated reporting predicate, captures only one of its three addressees, and codes '
             'MODALITY as CONDITIONAL for a dated mandatory duty.'},
]


def main():
    frozen = {r['RECORD_ID']: r for r in csv.DictReader(open(FROZEN, encoding='utf-8-sig'))}
    if len(RESULTS) != 3:
        raise SystemExit('B1-04 must unblind exactly three controls.')
    for res in RESULTS:
        rid = res['RECORD_ID']
        if rid not in frozen:
            raise SystemExit(f'{rid} is not in the frozen B1-04 output.')
        if frozen[rid]['ADVANCED_DEFECT_PRESENT'] != res['ADVANCED_DEFECT_PRESENT']:
            raise SystemExit(f'{rid} control result contradicts the frozen decision.')

    with open(OUTPUT, 'w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS, quoting=csv.QUOTE_ALL, lineterminator='\r\n')
        w.writeheader()
        w.writerows(RESULTS)

    digest = hashlib.sha256(open(OUTPUT, 'rb').read()).hexdigest().upper()
    print(f'Rows={len(RESULTS)}')
    print(f'SHA256={digest}')


if __name__ == '__main__':
    main()
