"""Build the R4.2E-B1 batch 04 advanced validation output.

Executed in Claude Code after the Terra/Codex rate-limit interruption.
EXECUTION_ENVIRONMENT      = Claude Code / VS Code extension
RESEARCHER_SELECTED_MODEL  = Claude Opus 5.5 Extra High
RUNTIME_REPORTED_MODEL     = Claude Opus 5
RUNTIME_MODEL_ID           = claude-opus-5
MODEL_SELECTION_RUNTIME_MATCH = NOT_VERIFIABLE

B1-01, B1-02 and B1-03 were produced by GPT-5.6 Terra High and are NOT touched.
Uses the csv module for all quoting so the B1-01 separator defect cannot recur.
"""
import csv, hashlib, os, datetime

R4 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BATCH = os.path.join(R4, '03_extraction', 'qa', 'repair', 'R4_2E_B1')
INPUT = os.path.join(BATCH, 'R4_2E_B1_BLIND_SUBSTANTIVE_REVIEW_INPUT.csv')
OUTPUT = os.path.join(BATCH, 'R4_2E_B1_ADVANCED_VALIDATION_B1_04.csv')

MODEL_REQUESTED = 'Claude Opus 5.5 Extra High'
MODEL_RESEARCHER_SELECTED = 'Claude Opus 5.5 Extra High'
MODEL_RUNTIME_VARIANT = ('RUNTIME_REPORTED_MODEL=Claude Opus 5; RUNTIME_MODEL_ID=claude-opus-5; '
                         'MODEL_SELECTION_RUNTIME_MATCH=NOT_VERIFIABLE')

COLUMNS = ['CASE_ID', 'RECORD_ID', 'BATCH_ID', 'REVIEW_TYPE', 'SOURCE_TYPE', 'SOURCE_REFERENCE',
           'INPUT_HASH', 'MODEL_REQUESTED', 'MODEL_RESEARCHER_SELECTED', 'MODEL_RUNTIME_VARIANT',
           'RUN_TIMESTAMP', 'ADVANCED_DEFECT_PRESENT', 'PROPOSITION_ANCHOR_CONFIDENCE',
           'ACTOR_CORRECT', 'ACTION_CORRECT', 'OBJECT_CORRECT', 'COUNTERPART_CORRECT',
           'RECIPIENT_CORRECT', 'PROPOSED_ACTOR', 'PROPOSED_ACTION', 'PROPOSED_OBJECT',
           'PROPOSED_COUNTERPART', 'PROPOSED_RECIPIENT', 'PROPOSED_CONTEXT_MODIFIER',
           'RELATIONAL_FIELD_DIFFERENTIATION', 'RELATIONAL_ENTITY', 'RELATIONAL_ROLE_RATIONALE',
           'ADVANCED_REASONING_NOTE', 'TEMPLATE_GENERALIZABILITY', 'FAMILY_TEMPLATE_STATUS',
           'REPAIR_TEMPLATE', 'TEMPLATE_APPLICATION_CONDITIONS', 'CASE_ROUTE_AFTER_REVIEW']

NE = 'NONE_EXPLICIT'
F = ('defect', 'anchor', 'actor_c', 'action_c', 'object_c', 'cp_c', 'rp_c', 'actor', 'action',
     'object', 'cp', 'rp', 'modifier', 'relation', 'rel_entity', 'rationale', 'note', 'gen',
     'status', 'template', 'conditions', 'route')


def D(*vals):
    return dict(zip(F, vals))


TPL_COND = ('Apply only where the source anchor and the exact matrix legal predicate match; '
            'never across proposition or sentence boundaries.')

DECISIONS = {

'EXT-000280': D('YES', 'HIGH', 'NO', 'YES', 'NO', 'N/A', 'N/A',
    'the transfer of personal data to that third country or international organisation',
    'should be prohibited', NE, NE, NE,
    'unless the requirements in this Regulation relating to transfers subject to appropriate '
    'safeguards, including binding corporate rules, and derogations for specific situations are fulfilled',
    'NEITHER', NE,
    'The passive prohibition has no actor-capable relational entity; the third country appears '
    'inside the subject noun phrase.',
    'LEGAL_VERB preserves the full modal construction, but ACTOR_TEXT is the prepositional tail of '
    'the subject noun phrase and the object holds only residual punctuation.',
    'N/A', 'N/A', '', '', 'MODEL_REPAIR_PROPOSAL_ACCEPTABLE_FOR_HUMAN_QA'),

'EXT-000412': D('YES', 'HIGH', 'NO', 'NO', 'NO', 'NO', 'NO',
    'The legitimate interests of a controller, including those of a controller to which the '
    'personal data may be disclosed, or of a third party',
    'may provide', 'a legal basis for processing', NE, NE,
    'provided that the interests or the fundamental rights and freedoms of the data subject are not overriding',
    'NEITHER', NE,
    'The matrix proposition has no relational entity; "with the controller" was copied from a later sentence.',
    'The row anchors the embedded relative-clause verb "may be disclosed" instead of the matrix '
    'predicate "may provide"; the matrix predicate itself sits inside the object span.',
    'N/A', 'N/A', '', '', 'MODEL_REPAIR_PROPOSAL_ACCEPTABLE_FOR_HUMAN_QA'),

'EXT-000093': D('YES', 'HIGH', 'YES', 'NO', 'NO', 'N/A', 'N/A',
    'The Board', 'shall collate',
    'all certification mechanisms and data protection seals and marks in a register', NE, NE,
    'by any appropriate means',
    'NEITHER', NE,
    'Article 42(8) states no relational entity for the collation duty.',
    'The action span cuts the noun phrase "data protection | seals and marks" in half and the object '
    'absorbs the coordinated second predicate "and shall make them publicly available".',
    'LOW', 'REQUIRES_MORE_REPRESENTATIVES',
    'Split coordinated predicates into distinct records and align the action span to a constituent boundary.',
    TPL_COND, 'N/A'),

'EXT-000001': D('YES', 'HIGH', 'YES', 'NO', 'NO', 'N/A', 'N/A',
    'the controller', 'shall not be obliged to maintain, acquire or process',
    'additional information in order to identify the data subject for the sole purpose of complying '
    'with this Regulation', NE, NE,
    'If the purposes for which a controller processes personal data do not or do no longer require '
    'the identification of a data subject by the controller',
    'NEITHER', NE,
    'The exemption proposition states no relational entity.',
    'The verb span is correct but MODALITY is coded PROHIBITED, whereas "shall not be obliged to" '
    'removes an obligation rather than imposing a prohibition; the object also starts mid-coordination '
    'at ", acquire or process".',
    'CONDITIONAL', 'VALIDATED_WITH_CONDITIONS',
    'Recode absence-of-obligation constructions away from PROHIBITED and keep coordinated infinitival '
    'complements inside the predicate.',
    TPL_COND, 'N/A'),

'EXT-000015': D('YES', 'HIGH', 'YES', 'NO', 'YES', 'NO', 'NO',
    'the controller', 'shall provide',
    'the following information necessary to ensure fair and transparent processing in respect of the data subject',
    NE, 'the data subject',
    'In addition to the information referred to in paragraph 1',
    'RECIPIENT_ONLY', 'the data subject',
    'Article 14(2) names the data subject as the express addressee of the provision duty; there is no counterpart.',
    'The action span swallows the recipient and ends on a dangling "the following"; both relational '
    'fields hold the opening prepositional adjunct, which is not actor-capable.',
    'CONDITIONAL', 'VALIDATED_WITH_CONDITIONS',
    'Reject a prepositional adjunct as a relational entity and restore the express addressee as recipient.',
    TPL_COND, 'N/A'),

'EXT-000016': D('YES', 'HIGH', 'YES', 'NO', 'NO', 'N/A', 'N/A',
    'The controller', 'shall provide',
    'the information referred to in paragraphs 1 and 2', NE, NE,
    'within the time limits set out in points (a) to (c)',
    'NEITHER', NE,
    'The timing points are temporal modifiers, not relational entities.',
    'The action span ends at "paragraphs" and the object retains only the stranded numerals "1 and 2:".',
    'LOW', 'VALIDATED_WITH_CONDITIONS',
    'Align the action and object boundary to the complete cross-reference phrase.',
    TPL_COND, 'N/A'),

'EXT-000024': D('YES', 'HIGH', 'NO', 'NO', 'NO', 'NO', 'NO',
    'The data subject', 'shall have the right to obtain',
    'the erasure of personal data concerning him or her', 'the controller', NE,
    'without undue delay; where one of the listed grounds applies',
    'COUNTERPART_ONLY', 'the controller',
    'The data subject obtains erasure from the controller, which is a direct counterpart rather than an addressee.',
    'The modal bled into ACTOR_TEXT ("The data subject shall"), the entitlement construction is lost, '
    'and the object absorbs the distinct second proposition on the controller obligation.',
    'CONDITIONAL', 'VALIDATED_WITH_CONDITIONS',
    'Restore "shall have the right to" entitlement constructions and keep the paired controller '
    'obligation as a separate record.',
    TPL_COND, 'N/A'),

'EXT-000029': D('YES', 'HIGH', 'NO', 'NO', 'NO', 'N/A', 'N/A',
    'The data subject', 'shall have the right to object',
    'processing of personal data concerning him or her which is based on point (e) or (f) of '
    'Article 6(1), including profiling based on those provisions', NE, NE,
    'on grounds relating to his or her particular situation; at any time',
    'NEITHER', NE,
    'The controller appears only in the following sentence and is not a relation of this proposition.',
    'The modal bled into ACTOR_TEXT and the action is reduced to the bare verb "object", losing the '
    'deontic entitlement construction.',
    'CONDITIONAL', 'VALIDATED_WITH_CONDITIONS',
    'Restore the full entitlement construction and move situational and temporal adjuncts out of the object.',
    TPL_COND, 'N/A'),

'EXT-000045': D('YES', 'HIGH', 'YES', 'NO', 'NO', 'N/A', 'N/A',
    'The processor', 'shall not engage', 'another processor', NE, NE,
    'without prior specific or general written authorisation of the controller',
    'NEITHER', NE,
    'The controller is embedded in the authorisation condition, not a relation of the matrix '
    'predicate, so it must not be promoted.',
    'The action span stops at "without prior specific or" and the object runs on into the whole of '
    'the following sentence.',
    'CONDITIONAL', 'VALIDATED_WITH_CONDITIONS',
    'Terminate the object at the direct object and keep the following sentence as a separate record.',
    TPL_COND, 'N/A'),

'EXT-000110': D('YES', 'HIGH', 'NO', 'NO', 'NO', 'NO', 'NO',
    'the transfer', 'is made from',
    'a register which according to Union or Member State law is intended to provide information to '
    'the public and which is open to consultation either by the public in general or by any person '
    'who can demonstrate a legitimate interest', NE, NE,
    'but only to the extent that the conditions laid down by Union or Member State law for '
    'consultation are fulfilled in the particular case',
    'NEITHER', NE,
    'A register is not actor-capable, and the public and interested persons occur inside its description.',
    'The row anchors the deeply embedded relative clause "any person who can demonstrate a legitimate '
    'interest" instead of the matrix condition in point (g).',
    'CONDITIONAL', 'VALIDATED_WITH_CONDITIONS',
    'Anchor list-item conditions on the matrix subject and predicate rather than on a nested relative clause.',
    TPL_COND, 'N/A'),

'EXT-000253': D('YES', 'HIGH', 'NO', 'YES', 'NO', 'NO', 'NO',
    'Union or Member State law', 'shall be proportionate to', 'the aim pursued', NE, NE,
    'the coordinated duties to respect the essence of the right to data protection and to provide '
    'for suitable and specific safeguards',
    'NEITHER', NE,
    '"to the aim pursued" is a prepositional complement, not an actor-capable entity.',
    'The verb span is correct, but ACTOR_TEXT keeps the preposition and relativiser and the object '
    'holds the two further coordinated predicates, which must remain distinct.',
    'CONDITIONAL', 'VALIDATED_WITH_CONDITIONS',
    'Strip prepositions and relativisers from the actor and split coordinated deontic predicates '
    'into distinct records.',
    TPL_COND, 'N/A'),

'EXT-000267': D('YES', 'HIGH', 'NO', 'NO', 'NO', 'NO', 'NO',
    'the level of protection of the rights and freedoms of natural persons with regard to the '
    'processing of such data', 'should be equivalent', NE, NE, NE,
    'in all Member States; in order to ensure a consistent and high level of protection and to '
    'remove obstacles to flows of personal data within the Union',
    'NEITHER', NE,
    'The copied span is a truncated repetition of the predicate, not an actor-capable entity.',
    'ACTOR_TEXT keeps only the tail of the subject noun phrase, the verb span absorbs the spatial '
    'modifier, and the object begins the next sentence.',
    'CONDITIONAL', 'VALIDATED_WITH_CONDITIONS',
    'Restore the complete nominal subject and stop the object at the sentence boundary.',
    TPL_COND, 'N/A'),

'EXT-000268': D('YES', 'HIGH', 'NO', 'YES', 'NO', 'NO', 'NO',
    'the level of protection of natural persons ensured in the Union by this Regulation',
    'should not be undermined', NE, NE, NE,
    'including in cases of onward transfers from the third country or international organisation '
    'to controllers or processors',
    'NEITHER', NE,
    '"to the protection of personal data" was copied from an earlier sentence and is not actor-capable.',
    'The verb span is correct; ACTOR_TEXT keeps only the genitive tail of the subject and both '
    'relational fields carry cross-sentence material.',
    'CONDITIONAL', 'VALIDATED_WITH_CONDITIONS',
    'Restore the complete nominal subject and clear relational fields that quote an earlier sentence.',
    TPL_COND, 'N/A'),

'EXT-000275': D('PARTIALLY', 'HIGH', 'YES', 'YES', 'NO', 'NO', 'NO',
    'The Commission', 'should evaluate', 'the functioning of the latter decisions', NE, NE,
    'within a reasonable time',
    'NEITHER', NE,
    'The reporting addressees belong to the coordinated "report" predicate, which is a separate proposition.',
    'Actor and predicate are retained, but the object absorbs the temporal modifier and the whole '
    'coordinated reporting predicate, and both relational fields quote the earlier periodic-review sentence.',
    'CONDITIONAL', 'VALIDATED_WITH_CONDITIONS',
    'Split the evaluate and report predicates and keep each set of addressees with its own predicate.',
    TPL_COND, 'N/A'),

'EXT-000286': D('YES', 'HIGH', 'YES', 'NO', 'NO', 'NO', 'NO',
    'The controller', 'should inform', 'the transfer', NE,
    'the supervisory authority and the data subject',
    'where none of the other grounds for transfer are applicable',
    'RECIPIENT_ONLY', 'the supervisory authority and the data subject',
    'Recital 113 names two express addressees of the information duty and no counterpart.',
    'The action span cuts "the data | subject" in half, leaving the object as the stranded fragment '
    '"subject about the transfer", and both relational fields quote an earlier sentence.',
    'CONDITIONAL', 'VALIDATED_WITH_CONDITIONS',
    'Restore both express addressees as recipients and realign the action span to a constituent boundary.',
    TPL_COND, 'N/A'),

'EXT-000297': D('YES', 'HIGH', 'YES', 'NO', 'NO', 'NO', 'NO',
    'The supervisory authority', 'should have',
    'its own staff, chosen by the supervisory authority or an independent body established by '
    'Member State law', NE, NE,
    'which should be subject to the exclusive direction of the member or members of the supervisory authority',
    'NEITHER', NE,
    '"from the government" was copied from the appointment sentence and is not a relation of this proposition.',
    'The action span absorbs the object head "its own staff" and both relational fields carry '
    'cross-sentence material.',
    'CONDITIONAL', 'VALIDATED_WITH_CONDITIONS',
    'Return the object head to the object and clear relational fields quoting an earlier sentence.',
    TPL_COND, 'N/A'),

'EXT-000375': D('YES', 'HIGH', 'NO', 'NO', 'NO', 'NO', 'NO',
    'Public authorities or public or private bodies that hold records of public interest', 'should be',
    'services which, pursuant to Union or Member State law, have a legal obligation to acquire, '
    'preserve, appraise, arrange, describe, communicate, promote, disseminate and provide access to '
    'records of enduring value for general public interest', NE, NE, NE,
    'NEITHER', NE,
    'The copied span belongs to the final archiving sentence and is not actor-capable.',
    'ACTOR_TEXT drops the coordinated head "Public authorities or", the verb span carries the '
    'relativiser "which", and SOURCE_EXCERPT is empty for this record, which is itself a provenance gap.',
    'CONDITIONAL', 'VALIDATED_WITH_CONDITIONS',
    'Restore dropped coordinated subject heads and exclude the relativiser from the predicate span.',
    TPL_COND, 'N/A'),

'EXT-000618': D('YES', 'HIGH', 'YES', 'NO', 'NO', 'N/A', 'NO',
    'Member States', 'shall notify', 'those rules and those measures', NE, 'the Commission', NE,
    'RECIPIENT_ONLY', 'the Commission',
    'Article 52(2) names the Commission as the express addressee of the notification duty.',
    'The action span ends on a dangling "and" after swallowing the recipient, the object starts '
    'mid-phrase and absorbs the coordinated second notification predicate, and the express recipient '
    'is left empty.',
    'N/A', 'N/A', '', '', 'MODEL_REPAIR_PROPOSAL_ACCEPTABLE_FOR_HUMAN_QA'),

'EXT-000867': D('YES', 'HIGH', 'NO', 'NO', 'NO', 'N/A', 'N/A',
    'certain providers of intermediary services', 'intermediate in relation to',
    'services that may or may not be provided by electronic means, such as remote information '
    'technology services, transport, accommodation or delivery services', NE, NE, NE,
    'NEITHER', NE,
    'Recital 6 states no relational entity for the intermediation proposition.',
    'The action is the fragment "or may not be provided by electronic", taken from inside the '
    'embedded relative clause and split mid-phrase, while the matrix verb "intermediate" sits inside '
    'ACTOR_TEXT and the object runs into the next sentence.',
    'N/A', 'N/A', '', '', 'MODEL_REPAIR_PROPOSAL_ACCEPTABLE_FOR_HUMAN_QA'),

'EXT-000869': D('YES', 'MEDIUM', 'NO', 'NO', 'NO', 'NO', 'NO',
    'the decisions taken in this regard by providers of online platforms',
    'should be subject to oversight by', NE, 'the competent Digital Services Coordinator', NE, NE,
    'COUNTERPART_ONLY', 'the competent Digital Services Coordinator',
    'The Digital Services Coordinator exercises oversight over the decisions and is the counterpart '
    'of the relation, not an addressee.',
    'ACTOR_TEXT is a fragment spanning an adjunct, a coordinator and the pronoun "they"; resolving '
    'that pronoun is required to state the actor, which lowers anchor confidence. The object runs '
    'into the next sentence and both relational fields quote an earlier one.',
    'N/A', 'N/A', '', '', 'HUMAN_ADJUDICATION_REQUIRED'),

'EXT-000777': D('YES', 'HIGH', 'YES', 'NO', 'NO', 'N/A', 'N/A',
    'the Board', 'should be able to rely on',
    'the expertise and human resources of the Commission and of the competent national authorities',
    NE, NE, NE,
    'NEITHER', NE,
    'The Commission and the national authorities are genitive possessors inside the object noun '
    'phrase, not relational actors of "rely on".',
    'The action span absorbs "the expertise" and cuts the coordinated noun phrase in half; the object '
    'then continues into the whole of the following sentence, merging two distinct propositions into one record.',
    'LOW', 'REQUIRES_MORE_REPRESENTATIVES',
    'Terminate the object at the sentence boundary and return the object head to the object.',
    TPL_COND, 'N/A'),

'EXT-000489': D('YES', 'HIGH', 'YES', 'NO', 'NO', 'N/A', 'N/A',
    'Providers of intermediary services', 'shall designate', 'a single point of contact', NE, NE,
    'to enable them to communicate directly, by electronic means, with Member States authorities, '
    'the Commission and the Board referred to in Article 61',
    'NEITHER', NE,
    'The authorities named in the purpose clause are communication partners of the point of contact, '
    'not relations of the matrix designation duty; the heuristic flag for a dropped relational actor '
    'is not confirmed.',
    'The action span absorbs the object and ends on a dangling "to", leaving the object to begin at '
    '"enable". This is a clear instance where the model detection pattern differs from the human root cause.',
    'CONDITIONAL', 'VALIDATED_WITH_CONDITIONS',
    'Return the designated object to the object field and keep purpose-clause entities out of relational fields.',
    TPL_COND, 'N/A'),

'EXT-000527': D('YES', 'HIGH', 'YES', 'NO', 'NO', 'NO', 'NO',
    'The Commission', 'shall publish', 'a list of those bodies, including those specifications', NE, NE,
    'on a dedicated website that is easily accessible',
    'NEITHER', NE,
    'The copied span belongs to the Digital Services Coordinators notification sentence and is not '
    'a relation of the Commission publication duty.',
    'The action span absorbs the object, MODALITY is coded CONDITIONAL for an unconditional "shall '
    'publish" duty, the coordinated predicate "and keep it up to date" is buried in the object, and '
    'both relational fields quote the preceding sentence.',
    'CONDITIONAL', 'VALIDATED_WITH_CONDITIONS',
    'Separate the publication and updating predicates and clear relational fields quoting the preceding sentence.',
    TPL_COND, 'N/A'),

'EXT-000545': D('YES', 'HIGH', 'YES', 'NO', 'NO', 'N/A', 'N/A',
    'Providers of online platforms that use recommender systems', 'shall set out',
    'the main parameters used in their recommender systems, as well as any options for the recipients '
    'of the service to modify or influence those main parameters', NE, NE,
    'in their terms and conditions; in plain and intelligible language',
    'NEITHER', NE,
    'The recipients of the service occur inside the object noun phrase and are not a relation of the '
    'matrix predicate.',
    'The action span absorbs the locative modifier "in their terms and conditions" and the object '
    'opens with the manner modifier "in plain and intelligible language".',
    'CONDITIONAL', 'VALIDATED_WITH_CONDITIONS',
    'Move locative and manner modifiers out of the action and object into context.',
    TPL_COND, 'N/A'),

'EXT-000590': D('YES', 'HIGH', 'YES', 'NO', 'NO', 'NO', 'NO',
    'The Commission and the Board', 'shall encourage and facilitate',
    'the drawing up of voluntary codes of conduct at Union level', NE, NE,
    'to contribute to the proper application of this Regulation; taking into account the specific '
    'challenges of tackling different types of illegal content and systemic risks',
    'NEITHER', NE,
    '"to the proper application of this Regulation" is a purpose phrase and is not actor-capable.',
    'The action span absorbs "the drawing up of" and both relational fields hold a purpose phrase. '
    'The same defect pattern appears in the recital counterpart reviewed by Terra in B1-03, which '
    'corroborates the family across batches.',
    'CONDITIONAL', 'VALIDATED_WITH_CONDITIONS',
    'Reject purpose phrases as relational entities and return the nominalised object to the object field.',
    TPL_COND, 'N/A'),

'EXT-000677': D('YES', 'HIGH', 'YES', 'NO', 'NO', 'NO', 'NO',
    'The Commission', 'shall consult',
    'the Digital Services Coordinator of the Member State on the territory of which the inspection '
    'is to be conducted',
    'the Digital Services Coordinator of the Member State on the territory of which the inspection '
    'is to be conducted', NE, 'prior to taking that decision',
    'COUNTERPART_ONLY',
    'the Digital Services Coordinator of the Member State on the territory of which the inspection '
    'is to be conducted',
    'The consulted authority is the counterpart of the consultation relation rather than an addressee '
    'of a transmission.',
    'The action span ends at "of the", truncating the object head, and both relational fields quote '
    'the first sentence about submitting to an inspection.',
    'CONDITIONAL', 'VALIDATED_WITH_CONDITIONS',
    'Realign the action span to the verb and record the consulted body as counterpart.',
    TPL_COND, 'N/A'),

'EXT-000731': D('YES', 'HIGH', 'YES', 'NO', 'NO', 'NO', 'NO',
    'the individual annual supervisory fee', 'should not exceed',
    'an overall ceiling for each provider of very large online platforms or of very large online '
    'search engines', NE, NE,
    'taking into account the economic capacity of the provider of the designated service or services',
    'NEITHER', NE,
    'The copied span belongs to an earlier cost sentence and is not actor-capable.',
    'The action span ends at "for each", splitting the object noun phrase, and both relational fields '
    'quote an earlier sentence. This is the largest repair family in the batch and its second '
    'representative was reviewed by Terra in B1-03 with the same outcome.',
    'CONDITIONAL', 'VALIDATED_WITH_CONDITIONS',
    'Realign the action span to the predicate and clear relational fields quoting an earlier sentence.',
    TPL_COND, 'N/A'),

'EXT-000776': D('YES', 'HIGH', 'YES', 'NO', 'NO', 'NO', 'NO',
    'the Commission', 'should ensure',
    'that the agenda of the meetings is set in accordance with the requests of the members of the '
    'Board as laid down in the rules of procedure and in compliance with the duties of the Board '
    'laid down in this Regulation', NE, NE, 'through the Chair',
    'NEITHER', NE,
    'The relational fields hold a prepositional manner phrase, which is not actor-capable.',
    'The action span absorbs the subordinate clause subject, leaving the object as the two-word '
    'fragment "is set".',
    'CONDITIONAL', 'VALIDATED_WITH_CONDITIONS',
    'Keep the whole that-clause in the object and the means phrase in context.',
    TPL_COND, 'N/A'),

'EXT-000898': D('YES', 'HIGH', 'YES', 'NO', 'NO', 'N/A', 'N/A',
    'Those providers', 'should consider',
    'corrective measures, such as discontinuing advertising revenue for specific information, or '
    'other actions, such as improving the visibility of authoritative information sources, or more '
    'structurally adapting their advertising systems', NE, NE, NE,
    'NEITHER', NE,
    'Recital 88 states no relational entity for this proposition.',
    'The action span absorbs the object head "corrective measures". The second representative of this '
    'family was adjudicated defect-free by Terra in B1-03, so the family shows heterogeneous outcomes '
    'and one template cannot yet be validated for it.',
    'LOW', 'REQUIRES_MORE_REPRESENTATIVES',
    'Return the object head to the object field.',
    'Do not generalise until the heterogeneous outcomes within this family are resolved.', 'N/A'),

'EXT-001166': D('YES', 'MEDIUM', 'YES', 'NO', 'NO', 'NO', 'NO',
    'the Commission', 'shall consult', 'the relevant experts', 'the relevant experts', NE,
    'when setting the functional specifications of such database',
    'COUNTERPART_ONLY', 'the relevant experts',
    'Consulted experts are the counterpart of the consultation relation, not addressees.',
    'The action span absorbs the object and the object holds the entire second coordinated '
    'consultation proposition about the Board. Because the record could anchor either coordinated '
    'consult proposition, anchor confidence is medium and the split should be adjudicated by a human.',
    'N/A', 'N/A', '', '', 'HUMAN_ADJUDICATION_REQUIRED'),

'EXT-001267': D('YES', 'HIGH', 'NO', 'NO', 'NO', 'NO', 'NO',
    'Compliance with the obligations applicable to the providers of general-purpose AI models',
    'should be commensurate and proportionate to', 'the type of model provider', NE, NE,
    'excluding the need for compliance for persons who develop or use models for non-professional '
    'or scientific research purposes',
    'NEITHER', NE,
    'The relational fields hold a truncated copy of the predicate itself, which is not an entity.',
    'ACTOR_TEXT drops the head "Compliance with", the action span ends at "to the type" and splits '
    'the object noun phrase, and the relational fields duplicate the predicate span.',
    'N/A', 'N/A', '', '', 'MODEL_REPAIR_PROPOSAL_ACCEPTABLE_FOR_HUMAN_QA'),

'EXT-001375': D('YES', 'MEDIUM', 'NO', 'YES', 'NO', 'NO', 'NO',
    'the Commission', 'should be empowered to adopt',
    'any future amendments of the list of high-risk AI systems', NE, NE,
    'via delegated acts; to take into account the rapid pace of technological development and the '
    'potential changes in the use of AI systems',
    'NEITHER', NE,
    'The copied span belongs to the first sentence on classification criteria and is not actor-capable.',
    'The verb span is correct, but ACTOR_TEXT is the prepositional fragment preceding the relative '
    'clause in which the Commission is named. The proposition sits inside an embedded relative clause '
    'of a descriptive sentence, which lowers anchor confidence.',
    'N/A', 'N/A', '', '', 'MODEL_REPAIR_PROPOSAL_ACCEPTABLE_FOR_HUMAN_QA'),

'EXT-000937': D('YES', 'HIGH', 'YES', 'NO', 'NO', 'NO', 'NO',
    'the Commission', 'shall carry out', 'an assessment of the enforcement of this Regulation', NE, NE,
    'by 2 August 2031; taking into account the first years of application of this Regulation',
    'NEITHER', NE,
    'The European Parliament, the Council and the Committee are addressees of the coordinated '
    'reporting predicate, which is a separate proposition.',
    'The action span absorbs the object, MODALITY is coded CONDITIONAL for a dated mandatory duty, '
    'the object begins mid-phrase at "of this Regulation" and absorbs the coordinated reporting '
    'predicate, and the relational fields capture only one of the three addressees of that other predicate.',
    'LOW', 'REQUIRES_MORE_REPRESENTATIVES',
    'Split the assessment and reporting predicates and keep all addressees with the reporting predicate.',
    TPL_COND, 'N/A'),

'EXT-000910': D('YES', 'MEDIUM', 'NO', 'NO', 'NO', 'NO', 'NO',
    'the provider', 'shall lodge',
    'an application for the assessment of the technical documentation relating to the AI system which '
    'the provider intends to place on the market or put into service and which is covered by the '
    'quality management system referred to under point 3',
    'a notified body of their choice', NE,
    'in addition to the application referred to in point 3',
    'COUNTERPART_ONLY', 'a notified body of their choice',
    'The application is lodged with the notified body, which is the counterpart of the lodging relation.',
    'The passive subject was coded as actor although the by-agent "the provider" is explicit, and the '
    'frozen rule set covers passives with no explicit actor but states no convention for passives with '
    'an explicit by-agent. That gap is recorded as NEW_STRUCTURAL_DIAGNOSTIC_CANDIDATE '
    'PASSIVE_WITH_EXPLICIT_BY_AGENT_LACKS_CODING_CONVENTION, and the relational fields quote the '
    'separate no-other-notified-body declaration.',
    'LOW', 'HUMAN_REVIEW_REQUIRED', '',
    'Blocked pending a researcher convention for passives with an explicit by-agent.', 'N/A'),

'EXT-001018': D('YES', 'HIGH', 'NO', 'NO', 'NO', 'N/A', 'NO',
    'The national competent authority or the notified body assuming the functions of the notified '
    'body affected by the change of designation',
    'shall inform', 'thereof, namely the assumption of functions referred to in this paragraph', NE,
    'the Commission, the other Member States and the other notified bodies', 'immediately',
    'RECIPIENT_ONLY', 'the Commission, the other Member States and the other notified bodies',
    'The provision names three express addressees of the information duty and no counterpart.',
    'ACTOR_TEXT keeps only the genitive tail of a long coordinated subject, the action span carries '
    'the temporal adverb and swallows the first addressee, and the remaining addressees sit in the '
    'object while the recipient field is empty.',
    'CONDITIONAL', 'VALIDATED_WITH_CONDITIONS',
    'Restore the complete coordinated subject and move all express addressees into the recipient field.',
    TPL_COND, 'N/A'),
}


def main():
    with open(INPUT, encoding='utf-8-sig', newline='') as fh:
        rows = [r for r in csv.DictReader(fh) if r['BATCH_ID'] == 'B1-04']
    rows.sort(key=lambda r: int(r['ORDER_IN_BATCH']))

    if len(rows) != 35:
        raise SystemExit(f'B1-04 input must contain exactly 35 records, found {len(rows)}')
    expected = [r['RECORD_ID'] for r in rows]
    if len(set(expected)) != 35:
        raise SystemExit('Duplicate RECORD_ID in B1-04 input')
    missing = [i for i in expected if i not in DECISIONS]
    extra = [i for i in DECISIONS if i not in expected]
    if missing or extra:
        raise SystemExit(f'ID mismatch. missing={missing} extra={extra}')

    ts = datetime.datetime.now().astimezone().strftime('%Y-%m-%dT%H:%M:%S%z')
    ts = ts[:-2] + ':' + ts[-2:]

    out = []
    for r in rows:
        d = DECISIONS[r['RECORD_ID']]
        out.append({
            'CASE_ID': r['CASE_ID'], 'RECORD_ID': r['RECORD_ID'], 'BATCH_ID': 'B1-04',
            'REVIEW_TYPE': r['REVIEW_SCOPE'], 'SOURCE_TYPE': r['SOURCE_TYPE'],
            'SOURCE_REFERENCE': r['SOURCE_REFERENCE'], 'INPUT_HASH': r['INPUT_HASH'],
            'MODEL_REQUESTED': MODEL_REQUESTED,
            'MODEL_RESEARCHER_SELECTED': MODEL_RESEARCHER_SELECTED,
            'MODEL_RUNTIME_VARIANT': MODEL_RUNTIME_VARIANT, 'RUN_TIMESTAMP': ts,
            'ADVANCED_DEFECT_PRESENT': d['defect'], 'PROPOSITION_ANCHOR_CONFIDENCE': d['anchor'],
            'ACTOR_CORRECT': d['actor_c'], 'ACTION_CORRECT': d['action_c'],
            'OBJECT_CORRECT': d['object_c'], 'COUNTERPART_CORRECT': d['cp_c'],
            'RECIPIENT_CORRECT': d['rp_c'], 'PROPOSED_ACTOR': d['actor'],
            'PROPOSED_ACTION': d['action'], 'PROPOSED_OBJECT': d['object'],
            'PROPOSED_COUNTERPART': d['cp'], 'PROPOSED_RECIPIENT': d['rp'],
            'PROPOSED_CONTEXT_MODIFIER': d['modifier'] or NE,
            'RELATIONAL_FIELD_DIFFERENTIATION': d['relation'], 'RELATIONAL_ENTITY': d['rel_entity'],
            'RELATIONAL_ROLE_RATIONALE': d['rationale'], 'ADVANCED_REASONING_NOTE': d['note'],
            'TEMPLATE_GENERALIZABILITY': d['gen'], 'FAMILY_TEMPLATE_STATUS': d['status'],
            'REPAIR_TEMPLATE': d['template'], 'TEMPLATE_APPLICATION_CONDITIONS': d['conditions'],
            'CASE_ROUTE_AFTER_REVIEW': d['route'],
        })

    for row in out:
        for col in COLUMNS:
            val = row[col]
            if val is None or (isinstance(val, str) and '\n' in val):
                raise SystemExit(f'Unsafe value in {row["RECORD_ID"]}.{col}')
        if not row['ADVANCED_REASONING_NOTE'].strip():
            raise SystemExit(f'Blank reasoning note in {row["RECORD_ID"]}')

    with open(OUTPUT, 'w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=COLUMNS, quoting=csv.QUOTE_ALL,
                           lineterminator='\r\n', extrasaction='raise')
        w.writeheader()
        w.writerows(out)

    with open(OUTPUT, encoding='utf-8-sig', newline='') as fh:
        back = list(csv.DictReader(fh))
    assert len(back) == 35, f'reparse row count {len(back)}'
    assert list(back[0].keys()) == COLUMNS, 'reparse column mismatch'
    assert [b['RECORD_ID'] for b in back] == expected, 'reparse ID order mismatch'

    digest = hashlib.sha256(open(OUTPUT, 'rb').read()).hexdigest().upper()
    print(f'Rows={len(out)}')
    print(f'Columns={len(COLUMNS)}')
    print(f'ReparsedRows={len(back)}')
    print(f'SHA256={digest}')


if __name__ == '__main__':
    main()
