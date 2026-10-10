$ErrorActionPreference = 'Stop'

$r4 = Split-Path -Parent $PSScriptRoot
$batchRoot = Join-Path $r4 '03_extraction\qa\repair\R4_2E_B1'
$inputPath = Join-Path $batchRoot 'R4_2E_B1_BLIND_SUBSTANTIVE_REVIEW_INPUT.csv'
$outputPath = Join-Path $batchRoot 'R4_2E_B1_ADVANCED_VALIDATION_B1_03.csv'
$input = @(
    Import-Csv $inputPath |
        Where-Object BATCH_ID -eq 'B1-03' |
        Sort-Object { [int] $_.ORDER_IN_BATCH }
)
if ($input.Count -ne 36) { throw 'B1-03 input must contain exactly 36 records.' }

function New-B1Decision {
    param(
        [string]$Id, [string]$Defect, [string]$Anchor,
        [string]$ActorCorrect, [string]$ActionCorrect, [string]$ObjectCorrect,
        [string]$CounterpartCorrect, [string]$RecipientCorrect,
        [string]$Actor, [string]$Action, [string]$Object,
        [string]$Counterpart, [string]$Recipient,
        [string]$Relation, [string]$RelationEntity,
        [string]$Rationale, [string]$TemplateGeneralizability,
        [string]$TemplateStatus, [string]$Route
    )
    [pscustomobject] [ordered] @{ 
        Id = $Id; Defect = $Defect; Anchor = $Anchor
        ActorCorrect = $ActorCorrect; ActionCorrect = $ActionCorrect; ObjectCorrect = $ObjectCorrect
        CounterpartCorrect = $CounterpartCorrect; RecipientCorrect = $RecipientCorrect
        Actor = $Actor; Action = $Action; Object = $Object
        Counterpart = $Counterpart; Recipient = $Recipient
        Relation = $Relation; RelationEntity = $RelationEntity
        Rationale = $Rationale; TemplateGeneralizability = $TemplateGeneralizability
        TemplateStatus = $TemplateStatus; Route = $Route
    }
}

# Decisions are recorded as structured objects; Export-Csv performs all CSV quoting.
$decisions = @(
    New-B1Decision 'EXT-000234' 'NO' 'HIGH' 'YES' 'YES' 'YES' 'N/A' 'N/A' 'Any controller involved in processing' 'shall be liable for' 'the damage caused by processing which infringes this Regulation' 'NONE_EXPLICIT' 'NONE_EXPLICIT' 'NEITHER' 'NONE_EXPLICIT' 'The first Article 82(2) liability proposition is retained without a relational field.' 'N/A' 'N/A' 'NO_REPAIR'
    New-B1Decision 'EXT-000475' 'YES' 'HIGH' 'NO' 'YES' 'YES' 'NO' 'NO' 'Differences in the level of protection of the rights and freedoms of natural persons' 'may prevent' 'the free flow of personal data throughout the Union' 'NONE_EXPLICIT' 'NONE_EXPLICIT' 'NEITHER' 'NONE_EXPLICIT' 'The extracted actor is a prepositional fragment; the recital identifies differences in protection as the subject of the may-prevent proposition.' 'N/A' 'N/A' 'MODEL_REPAIR_PROPOSAL_ACCEPTABLE_FOR_HUMAN_QA'
    New-B1Decision 'EXT-000163' 'YES' 'HIGH' 'YES' 'NO' 'YES' 'NO' 'NO' 'the supervisory authority with which the complaint was lodged' 'shall adopt the decision and notify it to the complainant and shall inform the controller thereof' 'the decision' 'NONE_EXPLICIT' 'the complainant; the controller' 'RECIPIENT_ONLY' 'the complainant; the controller' 'Article 60(8) contains coordinated notification and information predicates with two addressees; the copied relational pair is not a counterpart.' 'CONDITIONAL' 'VALIDATED_WITH_CONDITIONS' 'N/A'
    New-B1Decision 'EXT-000233' 'YES' 'HIGH' 'YES' 'NO' 'NO' 'N/A' 'N/A' 'any court other than the court first seized' 'may decline jurisdiction' 'jurisdiction, on the application of one of the parties and subject to the stated conditions' 'NONE_EXPLICIT' 'NONE_EXPLICIT' 'NEITHER' 'NONE_EXPLICIT' 'The discourse adverb “also” was extracted as action; the legal predicate is may decline jurisdiction.' 'CONDITIONAL' 'VALIDATED_WITH_CONDITIONS' 'N/A'
    New-B1Decision 'EXT-000019' 'YES' 'HIGH' 'YES' 'NO' 'YES' 'NO' 'NO' 'The data subject' 'shall have the right to obtain' 'confirmation as to whether personal data concerning him or her are being processed and, where applicable, access to the personal data and listed information' 'the controller' 'NONE_EXPLICIT' 'COUNTERPART_ONLY' 'the controller' 'The entitlement construction must retain “shall have the right”; the controller is the direct counterpart, not a recipient.' 'CONDITIONAL' 'VALIDATED_WITH_CONDITIONS' 'N/A'
    New-B1Decision 'EXT-000161' 'YES' 'HIGH' 'YES' 'YES' 'NO' 'NO' 'NO' 'The supervisory authority with which a complaint has been lodged' 'shall inform' 'the complainant on the decision' 'NONE_EXPLICIT' 'the complainant' 'RECIPIENT_ONLY' 'the complainant' 'The extracted object is empty and the copied Article 60(7) relation is unrelated; Article 60(7) expressly names the complainant as recipient.' 'CONDITIONAL' 'VALIDATED_WITH_CONDITIONS' 'N/A'
    New-B1Decision 'EXT-000002' 'YES' 'HIGH' 'YES' 'YES' 'NO' 'N/A' 'NO' 'the controller' 'shall inform' 'the data subject accordingly' 'NONE_EXPLICIT' 'the data subject' 'RECIPIENT_ONLY' 'the data subject' 'Article 11(2) retains the controller-information predicate but the object and explicit data-subject recipient were dropped.' 'CONDITIONAL' 'VALIDATED_WITH_CONDITIONS' 'N/A'
    New-B1Decision 'EXT-000009' 'YES' 'HIGH' 'YES' 'NO' 'NO' 'YES' 'NO' 'the controller' 'may either charge a reasonable fee or refuse to act on the request' 'a manifestly unfounded or excessive request from a data subject' 'the data subject' 'NONE_EXPLICIT' 'COUNTERPART_ONLY' 'the data subject' 'Article 12(5) requires the two coordinated options; a request originator is a counterpart, not a recipient.' 'LOW' 'REQUIRES_MORE_REPRESENTATIVES' 'N/A'
    New-B1Decision 'EXT-000025' 'YES' 'HIGH' 'YES' 'NO' 'NO' 'YES' 'NO' 'The data subject' 'shall have the right to obtain' 'restriction of processing where one of the listed grounds applies' 'the controller' 'NONE_EXPLICIT' 'COUNTERPART_ONLY' 'the controller' 'The entitlement construction and governed object were truncated; “from the controller” identifies a counterpart, not a recipient.' 'CONDITIONAL' 'VALIDATED_WITH_CONDITIONS' 'N/A'
    New-B1Decision 'EXT-000018' 'YES' 'HIGH' 'YES' 'YES' 'YES' 'NO' 'NO' 'the controller' 'shall take appropriate measures to protect' 'the data subject rights and freedoms and legitimate interests, including making the information publicly available' 'NONE_EXPLICIT' 'NONE_EXPLICIT' 'NEITHER' 'NONE_EXPLICIT' 'The source proposition is retained, but conditions and safeguards were copied into both relational fields without an actor-capable relation.' 'CONDITIONAL' 'VALIDATED_WITH_CONDITIONS' 'N/A'
    New-B1Decision 'EXT-000072' 'NO' 'HIGH' 'YES' 'YES' 'YES' 'N/A' 'N/A' 'Member State law' 'may require controllers to consult with, and obtain prior authorisation from, the supervisory authority' 'processing by a controller for a task carried out in the public interest' 'NONE_EXPLICIT' 'NONE_EXPLICIT' 'NEITHER' 'NONE_EXPLICIT' 'The Member-State-law requirement proposition is preserved; the supervisory authority is embedded in the required controller conduct rather than a relation of the matrix actor.' 'NONE' 'REJECTED' 'N/A'
    New-B1Decision 'EXT-000003' 'YES' 'HIGH' 'YES' 'YES' 'YES' 'NO' 'YES' 'The controller' 'shall take appropriate measures to provide' 'the information and communications specified in Article 12(1)' 'NONE_EXPLICIT' 'the data subject' 'RECIPIENT_ONLY' 'the data subject' 'The matrix proposition is retained, but the data-subject relation was duplicated: it is an explicit recipient, not a counterpart.' 'CONDITIONAL' 'VALIDATED_WITH_CONDITIONS' 'N/A'
    New-B1Decision 'EXT-000287' 'PARTIALLY' 'HIGH' 'YES' 'YES' 'NO' 'N/A' 'N/A' 'the controller or processor' 'should make use of' 'solutions that provide data subjects with enforceable and effective rights regarding processing of their transferred data in the Union' 'NONE_EXPLICIT' 'NONE_EXPLICIT' 'NEITHER' 'NONE_EXPLICIT' 'The actor and modal predicate are retained, but the governed object starts mid-phrase and omits the complete rights-protection proposition.' 'LOW' 'REQUIRES_MORE_REPRESENTATIVES' 'N/A'
    New-B1Decision 'EXT-000377' 'NO' 'HIGH' 'YES' 'YES' 'YES' 'N/A' 'N/A' 'the Commission' 'should consider' 'specific measures for micro, small and medium-sized enterprises' 'NONE_EXPLICIT' 'NONE_EXPLICIT' 'NEITHER' 'NONE_EXPLICIT' 'The final Recital 167 Commission-consideration proposition is structurally retained.' 'NONE' 'REJECTED' 'N/A'
    New-B1Decision 'EXT-000485' 'YES' 'HIGH' 'YES' 'NO' 'YES' 'NO' 'N/A' 'associations and other bodies representing categories of controllers or processors' 'should consult relevant stakeholders and have regard to submissions received and views expressed' 'relevant stakeholders, including data subjects where feasible, and submissions and views received in response to the consultation' 'relevant stakeholders, including data subjects' 'NONE_EXPLICIT' 'COUNTERPART_ONLY' 'relevant stakeholders, including data subjects' 'Recital 99 has coordinated consult and have-regard predicates; consulted stakeholders are counterparts, not recipients.' 'CONDITIONAL' 'VALIDATED_WITH_CONDITIONS' 'N/A'
    New-B1Decision 'EXT-000281' 'YES' 'HIGH' 'YES' 'YES' 'YES' 'NO' 'NO' 'Authorisation by the competent supervisory authority' 'should be obtained' 'when safeguards are provided for in administrative arrangements that are not legally binding' 'NONE_EXPLICIT' 'NONE_EXPLICIT' 'NEITHER' 'NONE_EXPLICIT' 'The passive authorisation proposition is retained, but preceding safeguards language was copied into relational fields without a relation.' 'CONDITIONAL' 'VALIDATED_WITH_CONDITIONS' 'N/A'
    New-B1Decision 'EXT-000340' 'YES' 'HIGH' 'NO' 'NO' 'NO' 'N/A' 'NO' 'The staff of the European Data Protection Supervisor involved in carrying out the Board tasks' 'should perform its tasks exclusively under the instructions of, and report to,' 'the Chair of the Board' 'NONE_EXPLICIT' 'the Chair of the Board' 'RECIPIENT_ONLY' 'the Chair of the Board' 'The actor is reduced to a clause fragment and the coordinated perform/report construction loses its object and reporting recipient.' 'LOW' 'REQUIRES_MORE_REPRESENTATIVES' 'N/A'
    New-B1Decision 'EXT-000620' 'YES' 'HIGH' 'NO' 'NO' 'NO' 'NO' 'NO' 'Member States' 'shall ensure' 'that the maximum amount of the fine for the specified information and inspection failures is 1 % of annual income or worldwide turnover' 'NONE_EXPLICIT' 'NONE_EXPLICIT' 'NEITHER' 'NONE_EXPLICIT' 'The row combines the second Article 52(3) subject with the first-sentence predicate and object; the correct proposition requires reconstruction.' 'N/A' 'N/A' 'HUMAN_ADJUDICATION_REQUIRED'
    New-B1Decision 'EXT-000612' 'NO' 'HIGH' 'YES' 'YES' 'YES' 'N/A' 'N/A' 'the service provider' 'shall not be liable for' 'the automatic, intermediate and temporary storage of information, subject to the Article 5(1) conditions' 'NONE_EXPLICIT' 'NONE_EXPLICIT' 'NEITHER' 'NONE_EXPLICIT' 'The Article 5(1) caching-liability proposition is structurally retained; service recipients occur in conditions and purpose text, not as relational fields.' 'N/A' 'N/A' 'NO_REPAIR'
    New-B1Decision 'EXT-000734' 'YES' 'HIGH' 'YES' 'YES' 'YES' 'NO' 'NO' 'The Commission and the Board' 'should encourage' 'the drawing-up of voluntary codes of conduct and implementation of their provisions' 'NONE_EXPLICIT' 'NONE_EXPLICIT' 'NEITHER' 'NONE_EXPLICIT' 'The Commission-and-Board encouragement proposition is retained, but a purpose phrase was promoted into both relational fields.' 'N/A' 'N/A' 'MODEL_REPAIR_PROPOSAL_ACCEPTABLE_FOR_HUMAN_QA'
    New-B1Decision 'EXT-000660' 'YES' 'HIGH' 'YES' 'YES' 'NO' 'NO' 'NO' 'The Board' 'shall submit' 'its views on the preliminary findings' 'NONE_EXPLICIT' 'the Commission' 'RECIPIENT_ONLY' 'the Commission' 'Article 66(4) expressly directs the Board views to the Commission; the period and recipient were merged into the object and duplicated as a counterpart.' 'CONDITIONAL' 'VALIDATED_WITH_CONDITIONS' 'N/A'
    New-B1Decision 'EXT-000703' 'YES' 'HIGH' 'YES' 'YES' 'YES' 'NO' 'NO' 'The right of access to the file of the Commission' 'shall not extend to' 'confidential information and internal documents of the Commission, the Board and competent authorities' 'NONE_EXPLICIT' 'NONE_EXPLICIT' 'NEITHER' 'NONE_EXPLICIT' 'The Article 79(4) limitation is retained, but a negotiated-disclosure phrase from the preceding sentence is not a relational actor.' 'CONDITIONAL' 'VALIDATED_WITH_CONDITIONS' 'N/A'
    New-B1Decision 'EXT-000642' 'YES' 'HIGH' 'YES' 'YES' 'NO' 'NO' 'NO' 'The Board' 'shall adopt' 'its acts by simple majority' 'NONE_EXPLICIT' 'NONE_EXPLICIT' 'NEITHER' 'NONE_EXPLICIT' 'The first Article 62(3) proposition is clear, but the row imports the later recommendation-vote proposition and its Commission phrase.' 'LOW' 'REQUIRES_MORE_REPRESENTATIVES' 'N/A'
    New-B1Decision 'EXT-000619' 'YES' 'HIGH' 'NO' 'NO' 'NO' 'NO' 'NO' 'Member States' 'shall ensure' 'that the maximum amount of fines for failure to comply with a Regulation obligation is 6 % of annual worldwide turnover' 'NONE_EXPLICIT' 'NONE_EXPLICIT' 'NEITHER' 'NONE_EXPLICIT' 'The matrix Member-State ensure proposition is replaced by an embedded passive fine clause and duplicate non-relational fields.' 'CONDITIONAL' 'VALIDATED_WITH_CONDITIONS' 'N/A'
    New-B1Decision 'EXT-000532' 'YES' 'HIGH' 'YES' 'YES' 'YES' 'NO' 'NO' 'providers of online platforms' 'shall assess' 'whether the recipient of the service, individual, entity or complainant engages in the misuse specified in Article 23(1) and (2)' 'the recipient of the service, the individual, the entity or the complainant' 'NONE_EXPLICIT' 'COUNTERPART_ONLY' 'the recipient of the service, the individual, the entity or the complainant' 'Those whose misuse is assessed are the actor-capable counterpart set; the information-availability phrase is not a relational field.' 'CONDITIONAL' 'VALIDATED_WITH_CONDITIONS' 'N/A'
    New-B1Decision 'EXT-000488' 'YES' 'HIGH' 'YES' 'YES' 'YES' 'NO' 'NO' 'Such information provided to the recipient of the service' 'shall include' 'a statement of reasons and the possibilities for redress that exist' 'NONE_EXPLICIT' 'NONE_EXPLICIT' 'NEITHER' 'NONE_EXPLICIT' 'The Article 10(5) information-content proposition is retained; the order phrase was copied into both relational fields from a different proposition.' 'CONDITIONAL' 'VALIDATED_WITH_CONDITIONS' 'N/A'
    New-B1Decision 'EXT-000827' 'YES' 'HIGH' 'YES' 'YES' 'YES' 'NO' 'NO' 'Member States' 'should respect' 'the fundamental right to an effective judicial remedy and to a fair trial as provided for in Article 47 of the Charter' 'NONE_EXPLICIT' 'NONE_EXPLICIT' 'NEITHER' 'NONE_EXPLICIT' 'The final Recital 39 Member-State proposition is retained, but recipients from an earlier redress-information proposition were promoted into relational fields.' 'CONDITIONAL' 'VALIDATED_WITH_CONDITIONS' 'N/A'
    New-B1Decision 'EXT-000750' 'PARTIALLY' 'HIGH' 'YES' 'YES' 'NO' 'N/A' 'N/A' 'Member States' 'should set out' 'in their national law the detailed conditions and limits for exercise of investigatory and enforcement powers of Digital Services Coordinators and other competent authorities' 'NONE_EXPLICIT' 'NONE_EXPLICIT' 'NEITHER' 'NONE_EXPLICIT' 'The Recital 115 actor and predicate are retained, but the governed object is reduced to punctuation rather than the conditions-and-limits proposition.' 'LOW' 'REQUIRES_MORE_REPRESENTATIVES' 'N/A'
    New-B1Decision 'EXT-000813' 'YES' 'HIGH' 'NO' 'NO' 'NO' 'N/A' 'N/A' 'Member States' 'are increasingly introducing, or are considering introducing,' 'national laws imposing diligence requirements for providers of intermediary services' 'NONE_EXPLICIT' 'NONE_EXPLICIT' 'NEITHER' 'NONE_EXPLICIT' 'The row extracts an embedded provider should-tackle clause, not Recital 2 matrix Member-State national-law proposition.' 'LOW' 'HUMAN_REVIEW_REQUIRED' 'N/A'
    New-B1Decision 'EXT-000912' 'YES' 'HIGH' 'NO' 'YES' 'YES' 'NO' 'NO' 'NO_EXPLICIT_ACTOR' 'shall also be granted access to' 'the training and trained models of the AI system, including relevant parameters' 'NONE_EXPLICIT' 'NONE_EXPLICIT' 'NEITHER' 'NONE_EXPLICIT' 'Annex VII point 4.5 is a passive access proposition; the notified body is beneficiary, not an expressed actor, and another-notified-body text is unrelated.' 'N/A' 'N/A' 'HUMAN_ADJUDICATION_REQUIRED'
    New-B1Decision 'EXT-000931' 'YES' 'HIGH' 'YES' 'YES' 'YES' 'NO' 'NO' 'The Commission' 'shall adopt' 'implementing acts containing detailed arrangements and procedural safeguards for proceedings concerning possible Article 101(1) decisions' 'NONE_EXPLICIT' 'NONE_EXPLICIT' 'NEITHER' 'NONE_EXPLICIT' 'The Article 101(6) proposition is retained, but the examination procedure is procedural context and not a relational actor.' 'N/A' 'N/A' 'MODEL_REPAIR_PROPOSAL_ACCEPTABLE_FOR_HUMAN_QA'
    New-B1Decision 'EXT-001380' 'YES' 'HIGH' 'NO' 'YES' 'YES' 'NO' 'NO' 'AI systems used to evaluate the credit score or creditworthiness of natural persons' 'should be classified as' 'high-risk AI systems' 'NONE_EXPLICIT' 'NONE_EXPLICIT' 'NEITHER' 'NONE_EXPLICIT' 'The extracted actor is an infinitive fragment; Recital 58 expressly identifies the AI systems as the subject of the high-risk classification proposition.' 'N/A' 'N/A' 'HUMAN_ADJUDICATION_REQUIRED'
    New-B1Decision 'EXT-000986' 'NO' 'HIGH' 'YES' 'YES' 'YES' 'N/A' 'N/A' 'A notified body' 'shall be established under the national law of' 'a Member State and shall have legal personality' 'NONE_EXPLICIT' 'NONE_EXPLICIT' 'NEITHER' 'NONE_EXPLICIT' 'The Article 31(1) establishment and legal-personality proposition is structurally retained.' 'NONE' 'REJECTED' 'N/A'
    New-B1Decision 'EXT-000914' 'YES' 'HIGH' 'YES' 'NO' 'YES' 'NO' 'NO' 'The notified body' 'shall carry out periodic audits and shall provide' 'the provider with an audit report, to ensure that the provider maintains and applies the quality management system' 'NONE_EXPLICIT' 'the provider' 'RECIPIENT_ONLY' 'the provider' 'Annex VII point 5.3 has coordinated audit and report predicates; another-notified-body text is unrelated and the provider is the report recipient.' 'CONDITIONAL' 'VALIDATED_WITH_CONDITIONS' 'N/A'
    New-B1Decision 'EXT-001114' 'YES' 'HIGH' 'NO' 'YES' 'NO' 'NO' 'NO' 'national competent authorities' 'may recover' 'exceptional costs in a fair and proportionate manner' 'NONE_EXPLICIT' 'NONE_EXPLICIT' 'NEITHER' 'NONE_EXPLICIT' 'The row begins in an exception clause; Article 58(2)(a) identifies national competent authorities as the cost-recovery actor and does not support relational fields.' 'CONDITIONAL' 'VALIDATED_WITH_CONDITIONS' 'N/A'
    New-B1Decision 'EXT-001269' 'YES' 'HIGH' 'YES' 'NO' 'YES' 'NO' 'NO' 'the Commission' 'should take the request into account and may decide to reassess' 'whether the general-purpose AI model can still be considered to present systemic risks' 'NONE_EXPLICIT' 'NONE_EXPLICIT' 'NEITHER' 'NONE_EXPLICIT' 'Recital 111 contains coordinated Commission predicates; the model phrase is the object of reassessment, not an actor-capable relation.' 'CONDITIONAL' 'VALIDATED_WITH_CONDITIONS' 'N/A'
)

if ($decisions.Count -ne 36) { throw 'Decision set must contain exactly 36 records.' }
$byId = @{}
foreach ($decision in $decisions) {
    if ($byId.ContainsKey($decision.Id)) { throw "Duplicate decision ID: $($decision.Id)" }
    $byId[$decision.Id] = $decision
}
$runTimestamp = Get-Date -Format 'yyyy-MM-ddTHH:mm:ssK'
$output = foreach ($row in $input) {
    if (-not $byId.ContainsKey($row.RECORD_ID)) { throw "No decision for $($row.RECORD_ID)" }
    $d = $byId[$row.RECORD_ID]
    $repairTemplate = if ($d.TemplateStatus -eq 'VALIDATED_WITH_CONDITIONS') { 'Apply only when source anchor and exact matrix legal predicate match.' } else { '' }
    $templateConditions = if ($d.TemplateStatus -eq 'VALIDATED_WITH_CONDITIONS') { 'Verify source wording and prohibit cross-proposition application.' } else { '' }
    [pscustomobject] [ordered] @{
        CASE_ID = $row.CASE_ID
        RECORD_ID = $row.RECORD_ID
        BATCH_ID = 'B1-03'
        REVIEW_TYPE = $row.REVIEW_SCOPE
        SOURCE_TYPE = $row.SOURCE_TYPE
        SOURCE_REFERENCE = $row.SOURCE_REFERENCE
        INPUT_HASH = $row.INPUT_HASH
        MODEL_REQUESTED = 'GPT-5.6 Terra High'
        MODEL_RESEARCHER_SELECTED = 'GPT-5.6 Terra High'
        MODEL_RUNTIME_VARIANT = 'MODEL_VARIANT_NOT_EXPOSED'
        RUN_TIMESTAMP = $runTimestamp
        ADVANCED_DEFECT_PRESENT = $d.Defect
        PROPOSITION_ANCHOR_CONFIDENCE = $d.Anchor
        ACTOR_CORRECT = $d.ActorCorrect
        ACTION_CORRECT = $d.ActionCorrect
        OBJECT_CORRECT = $d.ObjectCorrect
        COUNTERPART_CORRECT = $d.CounterpartCorrect
        RECIPIENT_CORRECT = $d.RecipientCorrect
        PROPOSED_ACTOR = $d.Actor
        PROPOSED_ACTION = $d.Action
        PROPOSED_OBJECT = $d.Object
        PROPOSED_COUNTERPART = $d.Counterpart
        PROPOSED_RECIPIENT = $d.Recipient
        PROPOSED_CONTEXT_MODIFIER = 'SEE_ADVANCED_REASONING_NOTE'
        RELATIONAL_FIELD_DIFFERENTIATION = $d.Relation
        RELATIONAL_ENTITY = $d.RelationEntity
        RELATIONAL_ROLE_RATIONALE = $d.Rationale
        ADVANCED_REASONING_NOTE = $d.Rationale
        TEMPLATE_GENERALIZABILITY = $d.TemplateGeneralizability
        FAMILY_TEMPLATE_STATUS = $d.TemplateStatus
        REPAIR_TEMPLATE = $repairTemplate
        TEMPLATE_APPLICATION_CONDITIONS = $templateConditions
        CASE_ROUTE_AFTER_REVIEW = $d.Route
    }
}

$output | Export-Csv -LiteralPath $outputPath -NoTypeInformation -Encoding utf8
Write-Output "Rows=$($output.Count)"
Write-Output "SHA256=$((Get-FileHash -LiteralPath $outputPath -Algorithm SHA256).Hash)"
