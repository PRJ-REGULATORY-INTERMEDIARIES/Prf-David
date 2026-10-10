# Authored unit screening notes for units not screened automatically from the statements (explicit blocks)
from reg import *

# ---- formal elements
scr(['HDR'], 'final/formal', 'Official Journal page header (date, language, publication reference L 130/1); the publication date supports the temporal reference; no governance content.', 'No')
scr(['PBL'], 'final/formal', 'Institution formula of the legislators; formal element without governance content.', 'No')
scr(['CIT2'], 'final/formal', 'Procedural citation (proposal of the Commission); formal element, not an enacted provision; no record.', 'No')
scr(['CIT3'], 'final/formal', 'Procedural citation (transmission of the draft act to national parliaments); formal; no record.', 'No')
scr(['CIT4'], 'final/formal', 'Procedural citation (opinion of the European Economic and Social Committee); formal; no record.', 'No')
scr(['CIT5'], 'final/formal', 'Procedural citation (opinion of the Committee of the Regions); formal; no record.', 'No')
scr(['CIT6'], 'final/formal', 'Procedural citation (ordinary legislative procedure); formal; no record.', 'No')
scr(['WHR'], 'final/formal', "Preamble formula introducing the recitals ('Whereas:').", 'No')
scr(['ENC'], 'final/formal', 'Enacting formula; formal element without governance content.', 'No')
scr(['FIN.DONE'], 'final/formal', 'Place and date of signature; formal.', 'No')
scr(['FIN.SIG1'], 'final/formal', 'Signature block of the European Parliament; the named holder is not a position (RGAM-DR-11).', 'No')
scr(['FIN.SIG2'], 'final/formal', 'Signature block of the Council; the named holder is not a position (RGAM-DR-11).', 'No')

# ---- recitals: context only (RGAM-DR-07); notes point to operative counterparts where the recital mirrors an operative provision
REC = {
    1: 'Context on the Paris Agreement; no operative counterpart.',
    2: 'Context on the European Green Deal; no operative counterpart.',
    3: 'Context on the Climate Law and the 2030 target; operative reference only in A7.P2 (EXT).',
    4: 'Context on European Council conclusions; no operative counterpart.',
    5: 'Context on the European Pillar of Social Rights Action Plan; operative references in A6.P3 and A7.P4.',
    6: 'Context on the Porto Declaration; no operative counterpart.',
    7: 'Context on climate and energy legislation; no operative counterpart.',
    8: 'Context on the inclusion of buildings and road transport in Directive 2003/87/EC; operative scope in A1.P3 and A3.',
    9: 'Context on resource needs and cost pass-through; no operative counterpart.',
    10: 'Context on social impact and the need for dedicated funding; operative counterpart A1-A3.',
    11: 'Context on vulnerable groups and geographic specificities; operative counterparts A2 definitions and A6.P1(p).',
    12: 'Context on use of ETS revenues and amount of the Fund; operative counterpart A10.',
    13: 'Context on energy poverty and the definition review; operative counterpart A2.P0.pt1.',
    14: 'Context on building renovation support; operative counterpart A8.P1.',
    15: 'Context on the definition of transport poverty; operative counterpart A2.P0.pt2.',
    16: 'Context on establishing the Fund and its support measures; operative counterparts A1, A3, A8.',
    17: 'Context on the Plans (submission by 30 June 2025, objectives, content); operative counterparts A4, A6; the date appears only in the recital (no record).',
    18: 'Context on consultation and the role of Member States; operative counterpart A5.',
    19: 'Context on design of Plans in cooperation with the Commission, the template and minor adjustments; operative counterparts A6.P7 and A18.P6.',
    20: 'Context on targeting of measures; operative counterpart A8.P1.',
    21: 'Context on direct income support; operative counterparts A4.P3 and A8.P2.',
    22: 'Context on awareness-raising; operative counterpart A8.P1(d).',
    23: 'Context on climate mainstreaming, DNSH and technical guidance; operative counterparts A6.P5 and A7.P3; the tracking methodology is not in the operative text.',
    24: 'Context on gender; operative counterpart A6.P1(q).',
    25: 'Context on energy communities as eligible beneficiaries; operative counterpart A8.P1(c); no assignment created from the recital.',
    26: 'Context on Plan content; operative counterpart A6.P1.',
    27: 'Context on coherence with other plans and programmes; operative counterparts A4.P2 and A6.P3.',
    28: 'Context on the scenario in case of postponement of the emission trading system; operative counterpart Annex V (scenario) and A10.P1.',
    29: 'Context on conditional payments; operative counterparts A7.P2 and A20.',
    30: 'Context on financing of the Fund and the allocation methodology; operative counterparts A10, A14 and Annexes I-II.',
    31: 'Context on the national contribution; operative counterpart A15.',
    32: 'Context on commitments and agreements; operative counterparts A19 and A21.P2.',
    33: 'Context on transfers from and to shared management; operative counterpart A11.',
    34: 'Context on additionality; operative counterpart A13.',
    35: 'Context on coordination and double-funding avoidance; operative counterparts A13 and A22.',
    36: 'Context on payments on the basis of a Commission decision; operative counterparts A20.P3 and A20.P5.',
    37: 'Context on pro rata payments; operative counterpart A20.P9.',
    38: 'Context on indicators and the template in the Annexes; operative counterparts Annexes IV and V.',
    39: 'Context on sound financial management and conditionality; operative counterparts A12 and A21.',
    40: 'Context on suspension, termination, reduction and recovery; operative counterparts A20 and A21.P4.',
    41: 'Context on assurance, the internal control system and an information and monitoring system (data-mining and risk-scoring tool); the tool appears only in the recital and no record is created from it.',
    42: 'Context on use of the information and monitoring system by the Commission, OLAF, the Court of Auditors and the EPPO; no operative counterpart; no record created from the recital.',
    43: 'Context on personal data processing; operative counterpart A21.P3.',
    44: 'Context on protection of financial interests, OLAF and the EPPO; operative counterparts A21.P2(e) and Annex III.',
    45: 'Context on horizontal financial rules; operative counterpart A12.',
    46: 'Context on the consequential amendment; operative counterpart A28.',
    47: 'Context on subsidiarity and proportionality; no operative counterpart.',
}
for n, note in REC.items():
    scr([f'REC{n}'], 'recital-context', f'Recital: interpretive context only, no record created from a recital alone (RGAM-DR-07). {note}', 'No')

# ---- headings (never evidence)
scr([u for u in UORDER if u.startswith('CH') and u[2:].isdigit()] + [u for u in UORDER if u.endswith('.HD')], 'heading (editorial)',
    'Heading or title: editorial structure, never evidence of architectural membership (RGAM-DR-06).', 'No')

# ---- definitional-context units not used as statements
scr(['A2.P0'], 'scope/definitional-context', 'Lead-in of the definitions article; no assignment or relation (GAP-07).', 'No')
scr(['A2.P0.pt1'], 'scope/definitional-context', "Definition of 'energy poverty'; screened as definitional-context (GAP-07); used only as indirect support for the vulnerable households category; no record of its own.", 'No')
scr(['A2.P0.pt2'], 'scope/definitional-context', "Definition of 'transport poverty'; screened as definitional-context (GAP-07); used only as indirect support for the vulnerable transport users category; no record of its own.", 'No')
scr(['A2.P0.pt14'], 'scope/definitional-context', "Definition of 'technical building system'; used only inside the definition of building renovation; no assignment or relation (GAP-07).", 'No')

# ---- footnotes (editorial references; indirect support to EXT where the footnote identifies a referenced instrument)
_fn_ext = {}
for r in REG['EXT']:
    for x in r['ind']:
        _fn_ext.setdefault(x, []).append(r['key'])
for u in UORDER:
    if u.startswith('FN') or u == 'ANX4.FN1':
        keys = _fn_ext.get(u)
        if keys:
            scr([u], 'editorial footnote (publication reference)',
                'Footnote identifying the publication reference of an instrument cited in the operative text; supports the EXT record(s) only as indirect identification (' + ', '.join(keys) + '); no statement of its own.', 'No')
        else:
            scr([u], 'editorial footnote (publication reference)',
                'Footnote giving a publication reference or procedural note for a citation or recital; editorial; no record.', 'No')

# ---- Annex V table of contents (template)
scr([f'ANX5.pt{i}' for i in range(1, 40)], 'heading (editorial)',
    'Table of contents of the template (section numbers, titles and page numbers; some rows are marker-only with empty cells in the source); editorial, not evidence.', 'No')

# ---- Annex units cited by statements: role overrides (the statement kind would give a less accurate tag)
scr([f'ANX1.pt{i}' for i in range(1, 34)], 'procedural-mechanism (allocation methodology)',
    'Annex I methodology text (variables, definitions of terms, adjustment rules or image-only formula placeholders); supports ST for Annex I; no assignment or relation derived; formula images not transcribed (uncertainty on source representation).', 'Yes')
scr([f'ANX2.pt{i}' for i in range(1, 34)], 'allocation-data (attribute of the funding relation)',
    'Annex II text or allocation table row (named Member State or EU27 total with share and amounts); supports ST for Annex II; no separate record; values are attributes of the funding relation.', 'Yes')
scr([f'ANX4.pt{i}' for i in range(2, 58)], 'procedural-mechanism (indicator definition)',
    'Annex IV common indicator table row (number, indicator, explanation, unit) or table heading; supports ST for Annex IV and the reporting relation; reporting duties stated in rows 13, 14 and 31 yield their own statements.', 'Yes')
scr([f'ANX5.pt{i}' for i in range(40, 215)], 'procedural-mechanism (template content)',
    'Annex V template content (information item or table header of the Plan template); supports the template statements and the duty to use the template (A6.P7); no separate assignment.', 'Yes')
