# MECHANICAL: controlled-vocabulary check of the emitted tables against the frozen data dictionary
import csv, io, os, sys, json, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import reg
OUT = os.path.dirname(reg.W)


def rows(n):
    return list(csv.DictReader(io.StringIO(open(os.path.join(OUT, n + '.csv'), 'rb').read().decode('utf-8-sig'), newline='')))


EP = {'conceptually_projected', 'documented', 'legal_constitution_evidenced', 'material_establishment_evidenced', 'exercise_evidenced'}
LS = {'in_force', 'not_yet_applicable', 'suspended', 'expired_or_repealed', 'conditional_on_further_act'}
NT = {'N0', 'N1', 'N2', 'N3', 'N4', 'COMPOUND', 'AMBIGUOUS'}
MOD = {'obligation', 'obligation_promotional', 'prohibition', 'permission', 'competence', 'entitlement', 'definition', 'declaratory'}
REL = {'authority_control', 'delegation_authorization', 'oversight_supervision', 'accountability', 'information_reporting', 'verification_assurance',
       'review_adjudication', 'representation_participation', 'contractual_exchange', 'beneficiary_protective'}
FN = {'rule_making_standard_setting', 'implementation', 'interpretation_translation', 'information_provision', 'monitoring', 'verification_assurance',
      'enforcement', 'adjudication_dispute_resolution', 'remediation', 'representation_participation*', 'authorization_designation*',
      'cooperation_coordination*', 'FUNCTION_VOCABULARY_UNRESOLVED'}
bad = []


def chk(t, col, vals, allow_blank=False):
    for r in rows(t):
        v = r[col]
        if allow_blank and not v:
            continue
        if v not in vals:
            bad.append(f'{t}.{col}={v[:50]!r}')


chk('NORMATIVE_ASSIGNMENTS', 'epistemic_status', EP)
chk('NORMATIVE_ASSIGNMENTS', 'legal_status_of_norm', LS)
chk('NORMATIVE_ASSIGNMENTS', 'norm_type', NT)
chk('NORMATIVE_ASSIGNMENTS', 'modality', MOD)
chk('NORMATIVE_ASSIGNMENTS', 'function', FN)
chk('NORMATIVE_ASSIGNMENTS', 'derivation', {'direct', 'derived'})
chk('NORMATIVE_ASSIGNMENTS', 'counterpart_status', {'NONE_IDENTIFIABLE', 'IN_PROVISION', 'BY_EXPLICIT_CROSS_REFERENCE'})
chk('NORMATIVE_ASSIGNMENTS', 'constraint_only', {'Y', 'N'})
for r in rows('NORMATIVE_ASSIGNMENTS'):
    if r['modality'] == 'prohibition' and r['constraint_only'] != 'Y':
        bad.append('prohibition not constraint ' + r['na_id'])
chk('POSITIONS_AND_DEVICES', 'kind', {'POSITION', 'DEVICE'})
chk('POSITIONS_AND_DEVICES', 'type_or_instance', {'TYPE', 'INSTANCE'})
chk('POSITIONS_AND_DEVICES', 'epistemic_status', EP)
chk('POSITIONS_AND_DEVICES', 'device_classification', {'INS-TYPE', 'DEV', 'BORDERLINE_INS-TYPE'}, True)
chk('POSITIONS_AND_DEVICES', 'legal_constitution_status',
    {'constituted_by_N1', 'not_constituted_obligation_only', 'not_constituted_competence_only', 'conditionally_constituted', 'not_applicable'})
chk('POSITIONS_AND_DEVICES', 'establishment_norm_type', NT | {'NONE'})
chk('POSITIONS_AND_DEVICES', 'material_establishment_evidence', {'not_assessed'})
for r in rows('POSITIONS_AND_DEVICES'):
    if r['kind'] == 'DEVICE' and not (r['device_identity_evidence'] and r['device_function_evidence']):
        bad.append('device evidence ' + r['pd_id'])
    if r['legal_constitution_status'] == 'constituted_by_N1' and r['establishment_norm_type'] != 'N1':
        bad.append('N1 mismatch ' + r['pd_id'])
    if r['type_or_instance'] == 'INSTANCE' and not r['instance_source_unit_ids']:
        bad.append('instance without source ' + r['pd_id'])
chk('QUALIFIED_RELATIONS', 'relation_type', REL)
chk('QUALIFIED_RELATIONS', 'modality', MOD - {'prohibition'})
chk('QUALIFIED_RELATIONS', 'function', FN)
chk('QUALIFIED_RELATIONS', 'legal_status_of_norm', LS)
chk('QUALIFIED_RELATIONS', 'epistemic_status', EP - {'material_establishment_evidenced'})
chk('QUALIFIED_RELATIONS', 'derivation', {'direct', 'derived'})
chk('QUALIFIED_RELATIONS', 'accountability_class', {'NONE', 'INFO', 'ANSWERABILITY', 'ACCOUNTABILITY'})
chk('QUALIFIED_RELATIONS', 'accountability_sufficiency', {'sufficient', 'indeterminate', 'NA'})
for r in rows('QUALIFIED_RELATIONS'):
    if r['accountability_class'] == 'ANSWERABILITY' and not r['accountability_missing_elements']:
        bad.append('answerability without missing ' + r['qr_id'])
chk('EXTERNAL_REFERENCES', 'source_kind', {'legal_instrument', 'technical_standard', 'administrative_act', 'other_normative'})
chk('EXTERNAL_REFERENCES', 'reference_role',
    {'constitutes_position', 'constitutes_device', 'designates_competence', 'supplies_rule_or_standard', 'defines_term', 'other'})
chk('EXTERNAL_REFERENCES', 'dependency_kind', {'constitutes', 'qualifies', 'conditions', 'specifies'})
chk('EXTERNAL_REFERENCES', 'constitutive_dependency', {'Y', 'N'})
chk('ARCHITECTURE_CANDIDATES', 'outcome', {'INTEGRATED', 'DISTINGUISHABLE', 'OVERLAPPING_OR_PARTIALLY_INTEGRATED', 'INDETERMINATE'})
for c in ('i1_status', 'i2_status', 'i3_status', 'i4_status'):
    chk('ARCHITECTURE_CANDIDATES', c, {'SATISFIED', 'NOT_SATISFIED', 'INDETERMINATE'})
chk('ARCHITECTURE_CANDIDATES', 'i2_coupling_kind',
    {'shared_participation', 'coordination_or_communication', 'qualified_procedural_dependency', 'mandatory_interface', 'conditional_dependency',
     'integration_through_distributed_powers', 'integration_explicitly_constituted_by_law', 'NONE'})
chk('ARCHITECTURE_CANDIDATES', 'anticircularity_sequence_followed', {'Y', 'N'})
chk('PROPERTY_REGISTER', 'property_family', {'F1', 'F2', 'F3', 'F4', 'F5'}, True)
chk('PROPERTY_REGISTER', 'bearer_type', {'POSITION', 'RELATION', 'SUBCONFIGURATION', 'ARCHITECTURE'})
chk('PROPERTY_REGISTER', 'status', {'asserted', 'undetermined', 'not_attributable'})
chk('PROPERTY_REGISTER', 'closure_dependency', {'Y', 'N'})
chk('PROPERTY_REGISTER', 'fallacy_check', {'Y', 'N'})
names = {'centralization', 'directness and intermediation', 'public-private allocation', 'self-regulatory autonomy', 'vertical distribution',
         'decision-centre plurality', 'relational depth', 'functional allocation', 'discretion distribution', 'accountability structure',
         'necessary stage', 'depth from the rule-making position', 'substitutability'}
chk('PROPERTY_REGISTER', 'property_name', names)
chk('CLOSURE_REGISTER', 'record_kind', {'COVERAGE', 'ABSENCE_CLAIM'})
chk('CLOSURE_REGISTER', 'result', {'ASSERTED_WITHIN_DECLARED_CORPUS', 'UNDETERMINED'})
chk('PROVENANCE_LINKS', 'record_type', {'ST', 'NA', 'PD', 'QR', 'EXT', 'SC', 'ARCH', 'PROP', 'CL'})
chk('PROVENANCE_LINKS', 'support_type', {'direct', 'indirect'})
chk('PROVENANCE_LINKS', 'evidence_level', {'A'})
chk('PROVENANCE_LINKS', 'claim_status_supported', EP)
chk('UNCERTAINTY_LOG', 'uncertainty_type',
    {'SOURCE_AMBIGUITY', 'DRAFTING_CUE', 'DIRECTION', 'DEV_THRESHOLD', 'ACCOUNTABILITY_SUFFICIENCY', 'COUPLING_THRESHOLD', 'EXTERNAL_DEPENDENCY',
     'CLOSURE', 'PROTOCOL_GAP', 'OTHER'})
chk('UNCERTAINTY_LOG', 'status', {'OPEN', 'ESCALATED_TO_HQ'})
chk('HUMAN_REVIEW_QUEUE', 'trigger_code',
    {'HQ-NORMTYPE', 'HQ-DEV', 'HQ-ACCOUNT', 'HQ-INTEGRATION', 'HQ-OVERLAP', 'HQ-XREF', 'HQ-DIRECTION', 'HQ-GAP', 'HQ-EXTDEP', 'HQ-OTHER'})
chk('TRACE_DEMONSTRATIONS', 'selection_rule', {'SEEDED_DRAW', 'LARGEST_SUPPORT', 'NOT_APPLICABLE_NO_CANDIDATE'})
chk('TRACE_DEMONSTRATIONS', 'chain_complete', {'Y', 'N'})
chk('INSTRUMENT_LEVEL_SUMMARY', 'instrument_level_result',
    {'NO_ARCHITECTURE_WARRANTED', 'ONE_ARCHITECTURE', 'SEVERAL_DISTINGUISHABLE', 'OVERLAPPING_OR_PARTIALLY_INTEGRATED', 'INDETERMINATE'})
chk('INSTRUMENT_LEVEL_SUMMARY', 'highest_level_reached', {'E', 'P', 'R', 'S', 'A'})
chk('INSTRUMENT_LEVEL_SUMMARY', 'machine_provisional', {'Y'})
chk('SUBCONFIGURATIONS', 'default_status', {'S'})
chk('SOURCE_UNIT_INVENTORY', 'structure_class', {'OPERATIVE_ARTICLE', 'ANNEX', 'RECITAL', 'FORMAL_OTHER', 'HEADING_ONLY'})
chk('UNIT_SCREENING', 'governance_relevance', {'Yes', 'No', 'Uncertain'})
chk('INSTITUTIONAL_STATEMENTS', 'recital_only', {'Y', 'N'})
chk('INSTITUTIONAL_STATEMENTS', 'statement_kind',
    {'assignment_bearing', 'relation_bearing', 'position_defining', 'device_defining', 'definitional', 'scope', 'procedural', 'external_referencing',
     'final_formal', 'other'})
chk('W_DECLARATION', 'hash_match', {'Y'})
chk('RUN_METADATA', 'machine_generated', {'Y'})
for r in rows('SOURCE_UNIT_INVENTORY'):
    t = reg.UT[r['unit_id'][len(reg.CASE) + 1:]]
    if hashlib.sha256(t.encode('utf-8')).hexdigest() != r['text_sha256']:
        bad.append('sha ' + r['unit_id'])
print('VOCAB ISSUES', len(bad))
for b in bad[:40]:
    print(' -', b)
