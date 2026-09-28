"""R4.2E-B1S — post-hoc Action representation sensitivity audit.

Scope: the Action judgment only, across all 143 B1-reviewed cases.
This is NOT a rerun of B1 and does NOT modify any frozen batch output.

Audit provenance:
  EXECUTION_ENVIRONMENT         = Claude Code / VS Code extension
  RESEARCHER_SELECTED_MODEL     = Claude Opus 5.5 Extra High
  RUNTIME_REPORTED_MODEL        = Claude Opus 5
  RUNTIME_MODEL_ID              = claude-opus-5
  MODEL_SELECTION_RUNTIME_MATCH = NOT_VERIFIABLE
  The runtime did not verify the researcher selection. Both labels are recorded
  verbatim; they are not asserted to be equivalent.

Decision rule applied (aligned with brief section 8). For each case ask only whether the
composite LEGAL_ACTION + LEGAL_VERB + MODALITY preserves, for the proposition the record
anchors: the lexical legal verb, the modality, the deontic construction, and the predicate.

  ACTION_CORRECT_WITH_FULL_REPRESENTATION = YES
      when the composite preserves all four, even if LEGAL_VERB additionally over-extends
      into object or recipient material (a span-boundary matter belonging to the Object
      judgment, which this audit does not reopen).
  = NO
      when the predicate comes from a different proposition, the deontic construction is
      still incomplete, the lexical verb is still absent or paraphrased, or a coordinated
      predicate the reviewer flagged is still missing.

  B1_ACTION_JUDGMENT_CHANGES            verdict flips
  B1_ACTION_JUDGMENT_PARTIALLY_CHANGES  verdict holds, part of the stated basis dissolves
  B1_ACTION_JUDGMENT_STABLE             verdict and stated basis both hold
  ACTION_REPRESENTATION_NOT_MATERIAL    the reviewer already used the full representation
"""
import csv, hashlib, os
from collections import Counter

R4 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BATCH = os.path.join(R4, '03_extraction', 'qa', 'repair', 'R4_2E_B1')
EXTRACT = os.path.join(R4, '03_extraction', 'R4_STRUCTURAL_EXTRACTION.csv')
AUDIT = os.path.join(BATCH, 'R4_2E_B1_ACTION_SENSITIVITY_AUDIT.csv')
SUMMARY = os.path.join(BATCH, 'R4_2E_B1_ACTION_SENSITIVITY_SUMMARY.csv')

AUDIT_PROVENANCE = ('EXECUTION_ENVIRONMENT=Claude Code / VS Code extension; '
                    'RESEARCHER_SELECTED_MODEL=Claude Opus 5.5 Extra High; '
                    'RUNTIME_REPORTED_MODEL=Claude Opus 5; RUNTIME_MODEL_ID=claude-opus-5; '
                    'MODEL_SELECTION_RUNTIME_MATCH=NOT_VERIFIABLE')

SOURCES = [
    ('B1-01', 'GPT-5.6 Terra High', 'R4_2E_B1_ADVANCED_VALIDATION.csv'),
    ('B1-02', 'GPT-5.6 Terra High', 'R4_2E_B1_ADVANCED_VALIDATION_B1_02.csv'),
    ('B1-03', 'GPT-5.6 Terra High', 'R4_2E_B1_ADVANCED_VALIDATION_B1_03.csv'),
    ('B1-04', 'Claude Opus 5', 'R4_2E_B1_ADVANCED_VALIDATION_B1_04.csv'),
]

CH = 'B1_ACTION_JUDGMENT_CHANGES'
PC = 'B1_ACTION_JUDGMENT_PARTIALLY_CHANGES'
ST = 'B1_ACTION_JUDGMENT_STABLE'
NM = 'ACTION_REPRESENTATION_NOT_MATERIAL'

NORMALIZED = ('LEGAL_ACTION held a controlled-vocabulary label rather than source wording. '
              'LEGAL_VERB preserves the source predicate with its modality, so the '
              'paraphrase objection does not survive the full representation.')
MODAL_OK = ('LEGAL_ACTION dropped the modal. LEGAL_VERB retains the complete modal '
            'predicate, so the modality objection does not survive the full representation.')
ENTITLE = ('LEGAL_VERB restores "have the right to" but still omits "shall" and MODALITY is '
           'UNCLEAR, so the deontic entitlement construction remains incomplete. The '
           'objection survives.')
COORD = ('LEGAL_VERB restores the modal but still omits the coordinated predicate the '
         'reviewer flagged. Verdict holds on the coordination ground alone.')
ANCHOR = ('LEGAL_VERB belongs to a different proposition from the one the reviewer '
          'identified as the matrix. Full representation does not resolve the anchor '
          'disagreement, so the objection survives intact.')
NOVERB = ('LEGAL_VERB adds the modal but the lexical legal verb is still absent, so the '
          'predicate remains unrecoverable from the record. Verdict holds.')

# record_id -> (result, action_correct_with_full, note)
TERRA = {
    # --- verdict flips NO -> YES ---
    'EXT-000221': (CH, 'YES', NORMALIZED),
    'EXT-000498': (CH, 'YES', NORMALIZED),
    'EXT-000511': (CH, 'YES', NORMALIZED),
    'EXT-000588': (CH, 'YES', NORMALIZED),
    'EXT-000748': (CH, 'YES', NORMALIZED),
    'EXT-001029': (CH, 'YES', NORMALIZED),
    'EXT-000013': (CH, 'YES', NORMALIZED),
    'EXT-000068': (CH, 'YES', NORMALIZED),
    'EXT-000192': (CH, 'YES', NORMALIZED),
    'EXT-000092': (CH, 'YES', NORMALIZED),
    'EXT-000496': (CH, 'YES', NORMALIZED),
    'EXT-000761': (CH, 'YES', NORMALIZED),
    'EXT-000825': (CH, 'YES', NORMALIZED),
    'EXT-000916': (CH, 'YES', NORMALIZED),
    'EXT-000046': (CH, 'YES', NORMALIZED),
    'EXT-000277': (CH, 'YES', NORMALIZED),
    'EXT-000944': (CH, 'YES',
                   'The reviewer recorded SOURCE_ANCHORED_RECONSTRUCTION_REQUIRED because the '
                   'LEGAL_ACTION fragment carried too little wording to fix a predicate. '
                   'LEGAL_VERB supplies "shall provide the Commission with information", which '
                   'resolves the predicate without any reconstruction.'),
    'EXT-000478': (CH, 'YES', MODAL_OK),
    'EXT-000386': (CH, 'YES', MODAL_OK),
    'EXT-000841': (CH, 'YES', MODAL_OK),
    'EXT-001348': (CH, 'YES',
                   'LEGAL_VERB is textually identical to the reviewer proposed action '
                   '("should be enforceable"). The proposal restated what the record already held.'),
    'EXT-001381': (CH, 'YES', MODAL_OK),
    'EXT-000852': (CH, 'YES', MODAL_OK),
    'EXT-000746': (CH, 'YES',
                   'LEGAL_VERB is textually identical to the reviewer proposed action '
                   '("cannot be subject") and MODALITY is PROHIBITED.'),
    'EXT-000840': (CH, 'YES',
                   'The reviewer note states explicitly that "the source modal is lost". '
                   'LEGAL_VERB is "should in particular pay due regard to freedom", so the modal '
                   'was never lost. This is the only case in which Action was the sole basis for '
                   'the defect decision.'),
    # --- reverse flip YES -> NO ---
    'EXT-000220': (CH, 'NO',
                   'The reviewer recorded ACTION_CORRECT = YES while proposing "shall have the '
                   'right to lodge". LEGAL_VERB lacks "shall" and MODALITY is UNCLEAR, the same '
                   'pattern the reviewer marked defective in EXT-000019, EXT-000025 and '
                   'EXT-000341. Full representation exposes an inconsistency and the judgment '
                   'moves to NO.'),
    # --- verdict holds, part of the basis dissolves ---
    'EXT-000206': (PC, 'NO', ENTITLE),
    'EXT-000027': (PC, 'NO', ENTITLE),
    'EXT-000202': (PC, 'NO', ENTITLE),
    'EXT-000341': (PC, 'NO', ENTITLE),
    'EXT-000085': (PC, 'NO', COORD),
    'EXT-000163': (PC, 'NO', COORD),
    'EXT-000340': (PC, 'NO', COORD),
    'EXT-000485': (PC, 'NO', COORD),
    'EXT-000914': (PC, 'NO', COORD),
    'EXT-001269': (PC, 'NO', COORD),
    'EXT-000023': (PC, 'NO',
                   'LEGAL_VERB restores "shall have the obligation to erase". The modal objection '
                   'dissolves, but the reviewer finding that the row crosses the entitlement and '
                   'obligation propositions still holds.'),
    'EXT-000009': (PC, 'NO', NOVERB),
    'EXT-000233': (PC, 'NO', NOVERB),
    'EXT-000056': (PC, 'NO', NOVERB),
    'EXT-000270': (PC, 'NO',
                   'LEGAL_VERB restores "may" but remains "may also decide", so the discourse '
                   'adverb still stands where the predicate "may decide to revoke" belongs.'),
    'EXT-000455': (PC, 'NO',
                   'LEGAL_VERB restores "may also issue guidelines". The modal objection '
                   'dissolves; the discourse adverb remains inside the predicate and the reviewer '
                   'read the modality as "should" against the source "may".'),
    # --- verdict and basis both hold ---
    'EXT-000150': (ST, 'NO', ANCHOR),
    'EXT-000273': (ST, 'NO', ANCHOR),
    'EXT-000346': (ST, 'NO', ANCHOR),
    'EXT-000357': (ST, 'NO', ANCHOR),
    'EXT-000811': (ST, 'NO', ANCHOR),
    'EXT-000757': (ST, 'NO', ANCHOR),
    'EXT-000208': (ST, 'NO', ANCHOR),
    'EXT-000369': (ST, 'NO', ANCHOR),
    'EXT-000749': (ST, 'NO', ANCHOR),
    'EXT-001283': (ST, 'NO', ANCHOR),
    'EXT-000620': (ST, 'NO', ANCHOR),
    'EXT-000619': (ST, 'NO', ANCHOR),
    'EXT-000813': (ST, 'NO', ANCHOR),
    'EXT-000019': (ST, 'NO', ENTITLE),
    'EXT-000025': (ST, 'NO', ENTITLE),
    'EXT-000026': (ST, 'NO',
                   'LEGAL_VERB still lacks "shall", MODALITY is UNCLEAR, and the coordinated '
                   'transmit predicate is still absent. Both limbs of the objection survive.'),
}

STABLE_YES_NOTE = ('The reviewer recorded ACTION_CORRECT = YES and LEGAL_VERB carries the same '
                   'predicate with an explicit modal, so the full representation corroborates '
                   'the judgment.')
CLAUDE_NOTE = ('B1-04 was scored against LEGAL_VERB and MODALITY at review time, so the '
               'representation issue does not apply to this case.')


def main():
    ext = {r['EXTRACTION_ID']: r for r in csv.DictReader(open(EXTRACT, encoding='utf-8-sig'))}
    rows = []
    for batch, model, fname in SOURCES:
        for r in csv.DictReader(open(os.path.join(BATCH, fname), encoding='utf-8-sig')):
            r['_B'], r['_M'] = batch, model
            rows.append(r)
    assert len(rows) == 143, f'expected 143, got {len(rows)}'

    out = []
    for r in rows:
        rid = r['RECORD_ID']
        e = ext[rid]
        orig = r['ACTION_CORRECT']
        if r['_B'] == 'B1-04':
            result, full, note = NM, orig, CLAUDE_NOTE
        elif rid in TERRA:
            result, full, note = TERRA[rid]
        elif orig == 'YES':
            result, full, note = ST, 'YES', STABLE_YES_NOTE
        else:
            raise SystemExit(f'unclassified Terra case {rid} ({orig})')

        fullrep = (f"LEGAL_ACTION: {e['LEGAL_ACTION']} | LEGAL_VERB: {e['LEGAL_VERB']} "
                   f"| MODALITY: {e['MODALITY']}")
        material = 'NO'
        if result == CH and orig == 'NO':
            others = [r['ACTOR_CORRECT'], r['OBJECT_CORRECT'],
                      r['COUNTERPART_CORRECT'], r['RECIPIENT_CORRECT']]
            if not any(v in ('NO', 'UNCERTAIN') for v in others):
                material = 'YES'
        out.append({
            'RECORD_ID': rid, 'ACT': e['CELEX'], 'BATCH_ID': r['_B'],
            'ORIGINAL_MODEL_PROVENANCE': r['_M'],
            'LEGAL_ACTION': e['LEGAL_ACTION'], 'LEGAL_VERB': e['LEGAL_VERB'],
            'MODALITY': e['MODALITY'], 'FULL_ACTION_REPRESENTATION': fullrep,
            'B1_ACTION_CORRECT_ORIGINAL': orig,
            'ACTION_CORRECT_WITH_FULL_REPRESENTATION': full,
            'ACTION_SENSITIVITY_RESULT': result,
            'MATERIAL_TO_DEFECT_DECISION': material,
            'SENSITIVITY_NOTE': note,
            'AUDIT_MODEL_PROVENANCE': AUDIT_PROVENANCE,
        })

    cols = list(out[0].keys())
    for row in out:
        for c in cols:
            if '\n' in str(row[c]):
                raise SystemExit(f'newline in {row["RECORD_ID"]}.{c}')
    with open(AUDIT, 'w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=cols, quoting=csv.QUOTE_ALL, lineterminator='\r\n')
        w.writeheader()
        w.writerows(out)

    res = Counter(o['ACTION_SENSITIVITY_RESULT'] for o in out)
    orig_no = sum(1 for o in out if o['B1_ACTION_CORRECT_ORIGINAL'] == 'NO')
    adj_no = sum(1 for o in out if o['ACTION_CORRECT_WITH_FULL_REPRESENTATION'] == 'NO')
    flips = [o for o in out if o['B1_ACTION_CORRECT_ORIGINAL'] !=
             o['ACTION_CORRECT_WITH_FULL_REPRESENTATION']]
    material = [o for o in out if o['MATERIAL_TO_DEFECT_DECISION'] == 'YES']

    srows = [
        ('TOTAL_B1_CASES_AUDITED', 143, 'All four batches; Action judgment only.'),
        ('ORIGINAL_B1_ACTION_CORRECTION_COUNT', orig_no,
         'Historical figure as frozen in the batch outputs. Not overwritten.'),
        ('SENSITIVITY_ADJUSTED_ACTION_CORRECTION_COUNT', adj_no,
         'Descriptive recount under the full LEGAL_ACTION + LEGAL_VERB + MODALITY view.'),
        ('ACTION_DECISIONS_CHANGED', len(flips), 'Verdict flips in either direction.'),
        ('ACTION_DECISIONS_CHANGED_NO_TO_YES',
         sum(1 for o in flips if o['B1_ACTION_CORRECT_ORIGINAL'] == 'NO'), ''),
        ('ACTION_DECISIONS_CHANGED_YES_TO_NO',
         sum(1 for o in flips if o['B1_ACTION_CORRECT_ORIGINAL'] == 'YES'), ''),
        ('RESULT_B1_ACTION_JUDGMENT_STABLE', res[ST], 'Verdict and stated basis both hold.'),
        ('RESULT_B1_ACTION_JUDGMENT_CHANGES', res[CH], ''),
        ('RESULT_B1_ACTION_JUDGMENT_PARTIALLY_CHANGES', res[PC],
         'Verdict holds; part of the stated basis dissolves.'),
        ('RESULT_ACTION_REPRESENTATION_NOT_MATERIAL', res[NM],
         'B1-04, already scored against the full representation.'),
        ('RESULT_UNCERTAIN_REQUIRES_HUMAN', res.get('UNCERTAIN_REQUIRES_HUMAN', 0), ''),
        ('DEFECT_DECISIONS_POTENTIALLY_AFFECTED', len(material),
         'Cases where Action was the sole basis for ADVANCED_DEFECT_PRESENT.'),
        ('DEFECT_DECISIONS_STABLE', 143 - len(material), ''),
        ('AFFECTED_RECORD_IDS', ';'.join(o['RECORD_ID'] for o in material) or 'none', ''),
        ('HISTORICAL_DEFECT_YES', 111, 'Frozen B1 figure, not overwritten.'),
        ('HISTORICAL_DEFECT_PARTIALLY', 15, 'Frozen B1 figure, not overwritten.'),
        ('HISTORICAL_DEFECT_NO', 17, 'Frozen B1 figure, not overwritten.'),
        ('SENSITIVITY_ADJUSTED_DEFECT_YES', 111, 'Descriptive only.'),
        ('SENSITIVITY_ADJUSTED_DEFECT_PARTIALLY', 14,
         'EXT-000840 moves from PARTIALLY toward NO. Descriptive only.'),
        ('SENSITIVITY_ADJUSTED_DEFECT_NO', 18, 'Descriptive only.'),
        ('TERRA_ORIGINAL_ACTION_CORRECTIONS', 57, 'B1-01 to B1-03.'),
        ('TERRA_ADJUSTED_ACTION_CORRECTIONS', adj_no - 30, 'B1-01 to B1-03, recounted.'),
        ('CLAUDE_ACTION_CORRECTIONS_UNCHANGED', 30,
         'B1-04 already used the full representation; no adjustment applies.'),
    ]
    with open(SUMMARY, 'w', encoding='utf-8', newline='') as fh:
        w = csv.writer(fh, quoting=csv.QUOTE_ALL, lineterminator='\r\n')
        w.writerow(['METRIC', 'VALUE', 'NOTE'])
        w.writerows(srows)

    print('sensitivity results:', dict(res))
    print(f'ORIGINAL action corrections           : {orig_no}')
    print(f'SENSITIVITY-ADJUSTED action corrections: {adj_no}')
    print(f'  Terra 57 -> {adj_no - 30} | Claude 30 -> 30 (unchanged)')
    print(f'decisions changed: {len(flips)} '
          f'(NO->YES {sum(1 for o in flips if o["B1_ACTION_CORRECT_ORIGINAL"] == "NO")}, '
          f'YES->NO {sum(1 for o in flips if o["B1_ACTION_CORRECT_ORIGINAL"] == "YES")})')
    print(f'defect decisions potentially affected : {len(material)} '
          f'{[o["RECORD_ID"] for o in material]}')
    for p in (AUDIT, SUMMARY):
        print(f'{os.path.basename(p)} SHA256='
              f'{hashlib.sha256(open(p, "rb").read()).hexdigest().upper()}')


if __name__ == '__main__':
    main()
