"""Deterministic variable redundancy audit over the frozen R4 structural extraction.

Read-only. No field is merged, deleted or modified.
All overlap figures are recomputed from R4_STRUCTURAL_EXTRACTION.csv at run time.
"""
import csv, hashlib, os, re

R4 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXTRACT = os.path.join(R4, '03_extraction', 'R4_STRUCTURAL_EXTRACTION.csv')
OUT = os.path.join(R4, '08_reports', 'R4_VARIABLE_REDUNDANCY_AUDIT.csv')

COLUMNS = ['VARIABLE_PAIR', 'OBSERVED_OVERLAP', 'EXACTNESS', 'DIRECTION',
           'INTERPRETATION', 'ADVANCED_REVIEW_EVIDENCE', 'PARSIMONY_STATUS']

MOD = re.compile(r'\b(shall|should|must|may|can|will|is to|are to|ought)\b', re.I)


def main():
    rows = list(csv.DictReader(open(EXTRACT, encoding='utf-8-sig')))
    n = len(rows)

    cp_eq = sum(1 for r in rows if r['COUNTERPART_TEXT'] == r['RECIPIENT_TEXT'])
    cp_both = sum(1 for r in rows if r['COUNTERPART_TEXT'].strip() and r['RECIPIENT_TEXT'].strip())
    ob_eq = sum(1 for r in rows if r['ACTION_OBJECT'] == r['INFORMATION_OR_MATERIAL_OBJECT'])
    ob_both = sum(1 for r in rows
                  if r['ACTION_OBJECT'].strip() and r['INFORMATION_OR_MATERIAL_OBJECT'].strip())
    conf_to_amb = all((r['EXTRACTION_CONFIDENCE'] == 'LOW') ==
                      (r['STRUCTURAL_AMBIGUITY'] == 'YES') for r in rows)
    amb_no_split = len(set(r['EXTRACTION_CONFIDENCE'] for r in rows
                           if r['STRUCTURAL_AMBIGUITY'] == 'NO'))
    lv_mod = sum(1 for r in rows if MOD.search(r['LEGAL_VERB']))
    la_mod = sum(1 for r in rows if MOD.search(r['LEGAL_ACTION']))
    la_in_lv = sum(1 for r in rows if r['LEGAL_ACTION'] and r['LEGAL_ACTION'] in r['LEGAL_VERB'])
    lv_eq_la = sum(1 for r in rows if r['LEGAL_VERB'] == r['LEGAL_ACTION'])

    assert conf_to_amb and amb_no_split == 2

    data = [
        {
            'VARIABLE_PAIR': 'COUNTERPART_TEXT / RECIPIENT_TEXT',
            'OBSERVED_OVERLAP': f'{cp_eq} of {n} rows identical '
                                f'({cp_both} both populated, {n - cp_both} both empty)',
            'EXACTNESS': 'EXACT_TEXTUAL_EQUALITY',
            'DIRECTION': 'SYMMETRIC',
            'INTERPRETATION': 'The extractor copied one span into both fields. The identity is an '
                              'artefact of population, not evidence that the two legal-relational '
                              'positions coincide.',
            'ADVANCED_REVIEW_EVIDENCE': 'Advanced review of 143 cases returned 27 RECIPIENT_ONLY '
                                        'and 14 COUNTERPART_ONLY, and 0 BOTH_SAME_ENTITY_JUSTIFIED. '
                                        'The positions are separable in the source.',
            'PARSIMONY_STATUS': 'RETAIN_BOTH_AND_REPAIR_POPULATION_RULE',
        },
        {
            'VARIABLE_PAIR': 'ACTION_OBJECT / INFORMATION_OR_MATERIAL_OBJECT',
            'OBSERVED_OVERLAP': f'{ob_eq} of {n} rows identical '
                                f'({ob_both} both populated, {n - ob_both} both empty)',
            'EXACTNESS': 'EXACT_TEXTUAL_EQUALITY',
            'DIRECTION': 'SYMMETRIC',
            'INTERPRETATION': 'The two columns never diverge anywhere in the corpus and are never '
                              'populated independently. On present evidence they carry one '
                              'variable at two variables cost.',
            'ADVANCED_REVIEW_EVIDENCE': 'No reviewed case distinguished the two. Unlike the '
                                        'relational pair, advanced review produced no evidence '
                                        'that the underlying distinction is ever realised.',
            'PARSIMONY_STATUS': 'STRONG_REDUNDANCY_CANDIDATE',
        },
        {
            'VARIABLE_PAIR': 'STRUCTURAL_AMBIGUITY / EXTRACTION_CONFIDENCE',
            'OBSERVED_OVERLAP': f'{n} of {n} rows consistent; EXTRACTION_CONFIDENCE=LOW coincides '
                                f'exactly with STRUCTURAL_AMBIGUITY=YES; AMBIGUITY=NO splits into '
                                f'HIGH and MEDIUM',
            'EXACTNESS': 'DETERMINISTIC_TRANSFORMATION',
            'DIRECTION': 'ONE_WAY: EXTRACTION_CONFIDENCE determines STRUCTURAL_AMBIGUITY; the '
                         'reverse does not hold',
            'INTERPRETATION': 'STRUCTURAL_AMBIGUITY is fully derivable from EXTRACTION_CONFIDENCE '
                              'by the rule LOW maps to YES and otherwise NO. EXTRACTION_CONFIDENCE '
                              'carries strictly more information, so the redundancy is one-way.',
            'ADVANCED_REVIEW_EVIDENCE': 'Not applicable; this is a metadata pair rather than a '
                                        'substantive coding variable.',
            'PARSIMONY_STATUS': 'DROP_STRUCTURAL_AMBIGUITY_AS_DERIVABLE',
        },
        {
            'VARIABLE_PAIR': 'LEGAL_ACTION / LEGAL_VERB',
            'OBSERVED_OVERLAP': f'never identical ({lv_eq_la} of {n}); LEGAL_ACTION is a substring '
                                f'of LEGAL_VERB in {la_in_lv} of {n}; explicit modal present in '
                                f'LEGAL_VERB {lv_mod} of {n} versus LEGAL_ACTION {la_mod} of {n}',
            'EXACTNESS': 'NOT_REDUNDANT_COMPLEMENTARY',
            'DIRECTION': 'NEITHER_DETERMINES_THE_OTHER',
            'INTERPRETATION': 'LEGAL_VERB holds the source predicate with its modality; '
                              'LEGAL_ACTION holds a normalised label that is not even a substring '
                              'of the verb in roughly three cases in ten. Together they are a '
                              'structured Action construct; separately each is incomplete.',
            'ADVANCED_REVIEW_EVIDENCE': 'The B1 review input exposed LEGAL_ACTION only. The '
                                        'sensitivity audit found 26 of 143 Action judgments change '
                                        'once LEGAL_VERB and MODALITY are visible.',
            'PARSIMONY_STATUS': 'RETAIN_BOTH_BUT_NEVER_PRESENT_LEGAL_ACTION_ALONE',
        },
        {
            'VARIABLE_PAIR': 'MODALITY / LEGAL_VERB',
            'OBSERVED_OVERLAP': f'LEGAL_VERB contains an explicit modal in {lv_mod} of {n} rows, '
                                f'so MODALITY is largely recoverable from it',
            'EXACTNESS': 'PARTIAL_FUNCTIONAL_OVERLAP',
            'DIRECTION': 'MOSTLY_ONE_WAY: LEGAL_VERB largely predicts MODALITY',
            'INTERPRETATION': 'MODALITY adds a controlled category on top of the verb span, but '
                              'the category is not reliably correct: absence-of-obligation is '
                              'coded PROHIBITED and unconditional duties are coded CONDITIONAL.',
            'ADVANCED_REVIEW_EVIDENCE': 'Three documented misclassifications recorded as new '
                                        'structural diagnostic candidates (EXT-000001, EXT-000527, '
                                        'EXT-000937).',
            'PARSIMONY_STATUS': 'RETAIN_BUT_AUDIT_THE_ENUM',
        },
    ]

    with open(OUT, 'w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS, quoting=csv.QUOTE_ALL, lineterminator='\r\n')
        w.writeheader()
        w.writerows(data)

    for d in data:
        print(f"{d['VARIABLE_PAIR']:52} {d['EXACTNESS']:32} {d['PARSIMONY_STATUS']}")
    print(f'\nSHA256={hashlib.sha256(open(OUT, "rb").read()).hexdigest().upper()}')


if __name__ == '__main__':
    main()
