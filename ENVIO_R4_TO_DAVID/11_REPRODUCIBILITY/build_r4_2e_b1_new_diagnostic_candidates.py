"""Record new structural diagnostic candidates observed during R4.2E-B1.

The fifteen frozen R4.2D human-derived rules are NOT modified. Everything here is
recorded only as NEW_STRUCTURAL_DIAGNOSTIC_CANDIDATE pending researcher adjudication.
"""
import csv, hashlib, os

R4 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(R4, '03_extraction', 'qa', 'repair', 'R4_2E_B1',
                   'R4_2E_B1_NEW_STRUCTURAL_DIAGNOSTIC_CANDIDATES.csv')

COLUMNS = ['NEW_STRUCTURAL_DIAGNOSTIC_CANDIDATE', 'OBSERVED_CASES', 'SCOPE', 'DESCRIPTION',
           'WHY_NOT_COVERED_BY_FROZEN_RULES', 'STATUS', 'REQUIRES', 'OBSERVED_BY']

ROWS = [
    {
        'NEW_STRUCTURAL_DIAGNOSTIC_CANDIDATE': 'PASSIVE_WITH_EXPLICIT_BY_AGENT_LACKS_CODING_CONVENTION',
        'OBSERVED_CASES': 'EXT-000910',
        'SCOPE': 'CODING_CONVENTION_GAP',
        'DESCRIPTION': 'A passive matrix predicate carries an explicit by-agent ("shall be lodged '
                       'by the provider"). The extraction placed the passive grammatical subject in '
                       'ACTOR_TEXT. It is unresolved whether ACTOR should hold the grammatical '
                       'subject or the explicit agent.',
        'WHY_NOT_COVERED_BY_FROZEN_RULES': 'Rule 4 allows NO_EXPLICIT_ACTOR and rule 5 forbids '
                                           'inferring an actor in a passive construction. Neither '
                                           'addresses a passive in which the agent is explicit and '
                                           'therefore need not be inferred.',
        'STATUS': 'NEW_STRUCTURAL_DIAGNOSTIC_CANDIDATE',
        'REQUIRES': 'Researcher convention before any template repair touches passive constructions.',
        'OBSERVED_BY': 'Claude Opus 5 (B1-04)',
    },
    {
        'NEW_STRUCTURAL_DIAGNOSTIC_CANDIDATE': 'MODALITY_ENUM_MISCLASSIFIES_ABSENCE_OF_OBLIGATION',
        'OBSERVED_CASES': 'EXT-000001',
        'SCOPE': 'FIELD_VALUE_DEFECT',
        'DESCRIPTION': 'GDPR Article 11(1) "the controller shall not be obliged to maintain" is '
                       'coded MODALITY = PROHIBITED. The provision removes an obligation; it does '
                       'not impose a prohibition. The enum appears to lack an exemption value.',
        'WHY_NOT_COVERED_BY_FROZEN_RULES': 'Rules 2 and 3 require preserving modality and the '
                                           'deontic construction but say nothing about the '
                                           'controlled MODALITY vocabulary itself.',
        'STATUS': 'NEW_STRUCTURAL_DIAGNOSTIC_CANDIDATE',
        'REQUIRES': 'Review of the MODALITY enum, in particular an EXEMPTION or '
                    'ABSENCE_OF_OBLIGATION value.',
        'OBSERVED_BY': 'Claude Opus 5 (B1-04)',
    },
    {
        'NEW_STRUCTURAL_DIAGNOSTIC_CANDIDATE': 'MODALITY_CONDITIONAL_APPLIED_TO_UNCONDITIONAL_DUTY',
        'OBSERVED_CASES': 'EXT-000527;EXT-000937',
        'SCOPE': 'FIELD_VALUE_DEFECT',
        'DESCRIPTION': 'Unconditional "shall publish" and dated "shall carry out" duties are coded '
                       'MODALITY = CONDITIONAL, apparently because conditional language occurs '
                       'elsewhere in the same provision.',
        'WHY_NOT_COVERED_BY_FROZEN_RULES': 'The frozen rules address span boundaries and the '
                                           'preservation of modality, not the correctness of the '
                                           'assigned modality category.',
        'STATUS': 'NEW_STRUCTURAL_DIAGNOSTIC_CANDIDATE',
        'REQUIRES': 'Researcher decision on whether MODALITY describes the matrix predicate or the '
                    'whole provision.',
        'OBSERVED_BY': 'Claude Opus 5 (B1-04)',
    },
    {
        'NEW_STRUCTURAL_DIAGNOSTIC_CANDIDATE': 'ACTION_SPAN_ABSORBS_OBJECT_HEAD',
        'OBSERVED_CASES': 'EXT-000093;EXT-000297;EXT-000489;EXT-000527;EXT-000777;EXT-000898;'
                          'EXT-000937;EXT-001166',
        'SCOPE': 'SPAN_BOUNDARY_DEFECT',
        'DESCRIPTION': 'The action span extends past the predicate and takes the head of the '
                       'governed object with it, leaving the object field to begin mid-phrase or '
                       'on a stranded modifier.',
        'WHY_NOT_COVERED_BY_FROZEN_RULES': 'Rule 14 forbids the object acting as a residual bucket. '
                                           'This is the mirror failure: the action, not the object, '
                                           'over-extends. It is frequent enough to warrant its own '
                                           'detector.',
        'STATUS': 'NEW_STRUCTURAL_DIAGNOSTIC_CANDIDATE',
        'REQUIRES': 'A deterministic constituent-boundary check between LEGAL_VERB and ACTION_OBJECT.',
        'OBSERVED_BY': 'Claude Opus 5 (B1-04)',
    },
    {
        'NEW_STRUCTURAL_DIAGNOSTIC_CANDIDATE': 'RELATIONAL_FIELDS_QUOTE_A_DIFFERENT_SENTENCE',
        'OBSERVED_CASES': 'EXT-000267;EXT-000268;EXT-000275;EXT-000286;EXT-000297;EXT-000375;'
                          'EXT-000527;EXT-000677;EXT-000731;EXT-000869;EXT-000910;EXT-001375',
        'SCOPE': 'RELATIONAL_FIELD_DEFECT',
        'DESCRIPTION': 'Counterpart and recipient hold an identical prepositional span copied from a '
                       'sentence other than the one the record anchors, frequently truncated '
                       'mid-word.',
        'WHY_NOT_COVERED_BY_FROZEN_RULES': 'Rules 6, 7 and 8 govern whether a phrase may occupy a '
                                           'relational position. They do not cover provenance, that '
                                           'is whether the phrase comes from the anchored sentence '
                                           'at all.',
        'STATUS': 'NEW_STRUCTURAL_DIAGNOSTIC_CANDIDATE',
        'REQUIRES': 'A deterministic containment check of relational spans against the anchored '
                    'sentence.',
        'OBSERVED_BY': 'Claude Opus 5 (B1-04)',
    },
    {
        'NEW_STRUCTURAL_DIAGNOSTIC_CANDIDATE': 'SOURCE_EXCERPT_EMPTY_FOR_EXTRACTED_RECORD',
        'OBSERVED_CASES': 'EXT-000375;EXT-000001; 181 of 1404 corpus records',
        'SCOPE': 'PROVENANCE_GAP',
        'DESCRIPTION': 'SOURCE_EXCERPT is empty for records that nevertheless have populated '
                       'structural fields, so the record cannot be checked against its own stored '
                       'excerpt. Read-only inspection shows this affects 181 of 1,404 corpus '
                       'records (12.9 per cent), not only the two seen in B1-04.',
        'WHY_NOT_COVERED_BY_FROZEN_RULES': 'The frozen rules concern field content, not provenance '
                                           'completeness.',
        'STATUS': 'NEW_STRUCTURAL_DIAGNOSTIC_CANDIDATE',
        'REQUIRES': 'A provenance completeness audit of SOURCE_EXCERPT across all 1,404 records.',
        'OBSERVED_BY': 'Claude Opus 5 (B1-04)',
    },
    {
        'NEW_STRUCTURAL_DIAGNOSTIC_CANDIDATE': 'WITHIN_FAMILY_HETEROGENEITY_DEFEATS_SINGLE_REPRESENTATIVE',
        'OBSERVED_CASES': 'RF-098E1C096964;RF-4EAB0DF25480;RF-8D5CE6A2D2FB',
        'SCOPE': 'COMPRESSION_DESIGN',
        'DESCRIPTION': 'Members of one repair family receive different verdicts. RF-098E1C096964 '
                       'returned two CLEAN_CONFIRMED controls and one DEFECT_FOUND control. '
                       'RF-8D5CE6A2D2FB returned one defect-free and one defective representative. '
                       'Six families in total have disagreeing representatives, covering 141 corpus '
                       'records.',
        'WHY_NOT_COVERED_BY_FROZEN_RULES': 'This concerns the B0 compression design rather than the '
                                           'structural coding of any single record.',
        'STATUS': 'NEW_STRUCTURAL_DIAGNOSTIC_CANDIDATE',
        'REQUIRES': 'Feeds B0_COMPRESSION_REASSESSMENT_REQUIRED; additional representatives before '
                    'any family template is applied.',
        'OBSERVED_BY': 'Claude Opus 5 (B1-04), corroborated against Terra B1-01 to B1-03 outputs',
    },
]


def main():
    with open(OUT, 'w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS, quoting=csv.QUOTE_ALL, lineterminator='\r\n')
        w.writeheader()
        w.writerows(ROWS)
    digest = hashlib.sha256(open(OUT, 'rb').read()).hexdigest().upper()
    print(f'Rows={len(ROWS)}')
    print(f'SHA256={digest}')


if __name__ == '__main__':
    main()
