$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
$repair = Join-Path $root '03_extraction/qa/repair'
$samplePath = Join-Path $repair 'R4_2D_CROSS_MODEL_DIAGNOSTIC_SAMPLE.csv'
$completedPath = Join-Path $repair 'R4_2D_HUMAN_DIAGNOSTIC_COMPLETED.csv'
$summaryPath = Join-Path $repair 'R4_2D_HUMAN_DIAGNOSTIC_SUMMARY.csv'
$reportPath = Join-Path $repair 'R4_2D_HUMAN_DIAGNOSTIC_REPORT.md'
$reviewer = 'Igor Caires Machado'

# Verbatim human decisions supplied by the researcher. Blank correction fields stay blank.
$decisions = @{
 'R4_2D-QA2B-009' = @{ Actor='YES'; Action='YES'; Object='YES'; Counterpart='NO'; Recipient='NO'; CorrectActor=''; CorrectAction=''; CorrectObject=''; CorrectCounterpart='NONE_EXPLICIT'; CorrectRecipient='NONE_EXPLICIT'; Class='COUNTERPART_RECIPIENT_OVERATTRIBUTION'; Root=''; Canonical='YES'; Caveat=''; Note='Article 32(1): “to the risk” qualifies the required level of security; it does not identify a counterpart or recipient. Actor, action and object retained. Structural extraction decision only; no R/I/T or mechanism coding.' }
 'R4_2D-QA2B-026' = @{ Actor='NO'; Action='NO'; Object='NO'; Counterpart='NO'; Recipient='NO'; CorrectActor='The Commission'; CorrectAction='may also decide, having given notice and a full statement setting out the reasons, to revoke'; CorrectObject='such a decision'; CorrectCounterpart='the third country or international organisation'; CorrectRecipient='the third country or international organisation'; Class='PROPOSITION_BOUNDARY_FAILURE; CROSS_PROPOSITION_CONTAMINATION'; Root=''; Canonical=''; Caveat=''; Note='Confirmed structural extraction defect. The Luna record crosses proposition boundaries: the extracted actor (“of personal data to that third country or international organisation”) is a complement from the preceding proposition concerning transfers of personal data, not the actor of the subsequent proposition. The relevant proposition is “The Commission may also decide ... to revoke such a decision.” Actor = The Commission; action = may decide to revoke; object = such a decision. The third country or international organisation is explicitly associated with the notice/reasons clause and may therefore be retained as the counterpart/recipient of that communicative component. No R/I/T or mechanism inference is made at this stage.' }
 'R4_2D-QA2B-036' = @{ Actor='YES'; Action='NO'; Object='NO'; Counterpart='NO'; Recipient='NO'; CorrectActor=''; CorrectAction='shall act in a diligent, objective and proportionate manner in applying and enforcing'; CorrectObject='the restrictions referred to in paragraph 1'; CorrectCounterpart='NONE_EXPLICIT'; CorrectRecipient='NONE_EXPLICIT'; Class='COUNTERPART_RECIPIENT_OVERATTRIBUTION; NORMATIVE_COMPLEMENT_MISCLASSIFICATION'; Root=''; Canonical='YES'; Caveat=''; Note='Confirmed counterpart/recipient overattribution. “The rights and legitimate interests of all parties involved” is governed by the phrase “with due regard to” and functions as a normative consideration or constraint on how providers apply and enforce the restrictions; it is not the counterpart or recipient of the extracted action. The actor is correctly identified as “Providers of intermediary services.” The action span is incomplete and should capture the obligation to act diligently, objectively and proportionately in applying and enforcing the restrictions. The object is “the restrictions referred to in paragraph 1.” No counterpart or recipient is structurally required for this proposition. No R/I/T or mechanism inference is made.' }
 'R4_2D-QA2B-056' = @{ Actor='YES'; Action='NO'; Object='NO'; Counterpart='NO'; Recipient='NO'; CorrectActor=''; CorrectAction='may invite'; CorrectObject='the Fundamental Rights Agency or the European Data Protection Supervisor'; CorrectCounterpart='the Fundamental Rights Agency or the European Data Protection Supervisor'; CorrectRecipient='the Fundamental Rights Agency or the European Data Protection Supervisor'; Class='CROSS_PROPOSITION_CONTAMINATION; EMBEDDED_ACTOR_ACTION_STRUCTURE'; Root=''; Canonical=''; Caveat='TRUE'; Note='Confirmed counterpart/recipient overattribution with cross-proposition contamination. The extracted counterpart and recipient (“the natural or legal person on whose behalf the advertisement is presented”) belong to an earlier advertising-transparency proposition and are unrelated to the Commission invitation proposition under extraction. The relevant matrix proposition is: “the Commission may invite the Fundamental Rights Agency or the European Data Protection Supervisor to express their opinions on the respective code of conduct.” The Commission is correctly identified as actor. The matrix action is “may invite”; the Fundamental Rights Agency or the European Data Protection Supervisor are the invitees and therefore the relevant counterpart/recipient of the invitation. The embedded proposition (“[FRA or EDPS] to express their opinions on the respective code of conduct”) contains an additional actor-action-object structure that should not be conflated with the matrix proposition. No R/I/T or mechanism inference is made.' }
 'R4_2D-QA2B-067' = @{ Actor='YES'; Action='YES'; Object='YES'; Counterpart='NO'; Recipient='NO'; CorrectActor=''; CorrectAction=''; CorrectObject=''; CorrectCounterpart='its authorised representative'; CorrectRecipient='its authorised representative'; Class='EMBEDDED_SOURCE_RELATION_PROMOTION'; Root=''; Canonical=''; Caveat=''; Note='Confirmed counterpart/recipient overattribution. The phrase “from the provider” modifies “the mandate received from the provider” and identifies the source of the mandate; it is not the counterpart or recipient of the matrix action. The matrix proposition is “The provider shall enable its authorised representative to perform the tasks specified in the mandate received from the provider.” Actor, action and object are adequately extracted. The authorised representative is the entity directly addressed by the enabling relation and is therefore the relevant structural counterpart/recipient. The embedded source relation (“mandate received from the provider”) should not be promoted to matrix-level counterpart or recipient. No R/I/T or mechanism inference is made.' }
 'R4_2D-QA2B-089' = @{ Actor='NO'; Action='NO'; Object='NO'; Counterpart='NO'; Recipient='NO'; CorrectActor='the notified body'; CorrectAction='may carry out'; CorrectObject='additional tests of the AI systems for which a Union technical documentation assessment certificate was issued'; CorrectCounterpart='N/A'; CorrectRecipient='N/A'; Class='MULTI_PROPOSITION_CONTAMINATION; PROPOSITION_ANCHOR_FAILURE'; Root='PROPOSITION_ANCHOR_FAILURE'; Canonical=''; Caveat=''; Note='Confirmed severe structural extraction defect involving multi-proposition contamination. The extracted fields combine fragments from distinct clauses and locations within Annex VII. The actor fragment (“the provider maintains and applies the quality management system”) belongs to a subordinate clause in point 5.3, while “with any other notified body” originates from a separate application-related provision and is unrelated to the proposition represented in the extracted object. The object field preserves the relevant proposition: “the notified body may carry out additional tests of the AI systems for which a Union technical documentation assessment certificate was issued.” Accordingly, the proposition is reconstructed as actor = “the notified body”; action = “may carry out”; object = “additional tests of the AI systems for which a Union technical documentation assessment certificate was issued”; no matrix-level counterpart or recipient is structurally required. This record should be treated as a proposition-anchoring/source-excerpt failure rather than merely counterpart/recipient overattribution. No R/I/T or mechanism inference is made.' }
 'R4_2D-QA2B-010' = @{ Actor='YES'; Action='NO'; Object='NO'; Counterpart='NO'; Recipient='NO'; CorrectActor=''; CorrectAction='shall consult'; CorrectObject='a proposal for a legislative measure to be adopted by a national parliament, or a regulatory measure based on such a legislative measure, which relates to processing'; CorrectCounterpart='the supervisory authority'; CorrectRecipient='the supervisory authority'; Class='SEMANTIC_SUBSTITUTION; SPAN_FRAGMENTATION; RELATIONAL_OMISSION'; Root=''; Canonical='YES'; Caveat=''; Note='Confirmed structural extraction defect. The actor (“Member States”) is correctly identified. The source text specifies the action as “shall consult”; the extracted formulation “consult or hear” introduces an unsupported semantic paraphrase and should not be retained in a structural extraction. The supervisory authority is the explicitly stated counterpart/recipient of the consultation and was omitted from both relational fields. The extracted object is also fragmented: the initial “of” is governed by the procedural phrase “during the preparation of” and should not begin the object span. The relevant subject matter is the proposal for a legislative measure, or the regulatory measure based on such a legislative measure, relating to processing. “During the preparation of” should be treated as procedural/temporal context rather than as part of the core object. No R/I/T or mechanism inference is made.' }
 'R4_2D-QA2B-025' = @{ Actor='NO'; Action='NO'; Object='NO'; Counterpart='NO'; Recipient='NO'; CorrectActor='N/A — no explicit actor'; CorrectAction='should be ensured'; CorrectObject='Consistent and homogenous application of the rules for the protection of the fundamental rights and freedoms of natural persons with regard to the processing of personal data'; CorrectCounterpart='N/A'; CorrectRecipient='N/A'; Class='CROSS_PROPOSITION_CONTAMINATION; PASSIVE_ACTOR_INVENTION; MODALITY_LOSS; SPAN_BOUNDARY_FAILURE'; Root=''; Canonical=''; Caveat=''; Note='Confirmed severe structural extraction defect with cross-proposition contamination. The relevant proposition is: “Consistent and homogenous application of the rules for the protection of the fundamental rights and freedoms of natural persons with regard to the processing of personal data should be ensured throughout the Union.” This is a passive construction with no explicit actor; therefore no actor should be inferred. “Natural persons” occurs inside the nominal phrase describing the protected rights and freedoms and is not the actor of “should be ensured.” The action should preserve the modal and passive construction (“should be ensured”), while “throughout the Union” functions as spatial scope. The object/content is the consistent and homogenous application of the relevant rules. The extracted object spills into the following Member State proposition, while the extracted counterpart/recipient derives from the preceding proposition concerning an equivalent level of protection. No counterpart or recipient is structurally required. No R/I/T or mechanism inference is made.' }
 'R4_2D-QA2B-033' = @{ Actor='YES'; Action='NO'; Object='NO'; Counterpart='NO'; Recipient='NO'; CorrectActor=''; CorrectAction='shall notify'; CorrectObject='its decision in respect of the information to which the notice relates'; CorrectCounterpart='that individual or entity'; CorrectRecipient='that individual or entity'; Class='ACTOR_ACTION_FRAGMENTATION; RELATIONAL_OMISSION; OBJECT_SPAN_OVEREXTENSION'; Root=''; Canonical='YES'; Caveat=''; Note='Confirmed actor-action fragmentation. The actor (“The provider”) is correctly extracted, but “also” is a discourse adverb rather than the action. The matrix action is “shall notify,” preserving the normative modal. “Without undue delay” is a temporal constraint. The explicitly stated counterpart/recipient is “that individual or entity,” which was omitted from the relational fields. The core content/object of the notification is “its decision in respect of the information to which the notice relates.” The following participial phrase (“providing information on the possibilities for redress in respect of that decision”) represents associated informational content/action and should not be merged indiscriminately into the core object. No R/I/T or mechanism inference is made.' }
 'R4_2D-QA2B-054' = @{ Actor='NO'; Action='NO'; Object='NO'; Counterpart='NO'; Recipient='NO'; CorrectActor='Member States'; CorrectAction='should be entitled to charge'; CorrectObject='a supervisory fee'; CorrectCounterpart='providers established in their territory'; CorrectRecipient='providers established in their territory'; Class='PROPOSITION_BOUNDARY_FAILURE; PREDICATE_FRAGMENTATION; DISTANT_RELATIONAL_CONTAMINATION'; Root='PROPOSITION_BOUNDARY_FAILURE'; Canonical=''; Caveat=''; Note='Confirmed severe actor-action fragmentation with cross-proposition contamination. The extraction is best anchored to the Member State proposition from which the original actor/action fragments derive: “Member States should be entitled to charge providers established in their territory a supervisory fee.” The actor span should therefore be “Member States,” excluding the discourse/subordination marker “and considering that.” The action is “should be entitled to charge,” preserving the modal and the distinction between entitlement and an obligation to charge. The object is “a supervisory fee,” and “providers established in their territory” are the explicit counterpart/recipient of the charging relation. The original object spills into the subsequent, distinct proposition stating that the Commission should charge a supervisory fee. The extracted counterpart/recipient derives from a still later passage concerning the Commission supervisory costs and is unrelated to the anchored Member State proposition. No R/I/T or mechanism inference is made.' }
 'R4_2D-QA2B-077' = @{ Actor='NO'; Action='NO'; Object='YES'; Counterpart='NO'; Recipient='NO'; CorrectActor='Any distributor, importer, deployer or other third-party'; CorrectAction='shall be considered to be'; CorrectObject=''; CorrectCounterpart='N/A'; CorrectRecipient='N/A'; Class='COORDINATED_PROPOSITION_CONFLATION; ACTOR_SPAN_TRUNCATION; MODALITY_LOSS; NON_ACTOR_PREPOSITIONAL_COMPLEMENT_MISCLASSIFICATION'; Root=''; Canonical=''; Caveat=''; Note='Confirmed structural extraction defect. The actor span is incomplete: the full coordinated subject is “Any distributor, importer, deployer or other third-party.” The first proposition assigns legal status through the predicate “shall be considered to be” and concerns a provider of a high-risk AI system. The source then introduces a second coordinated legal consequence: the same actors “shall be subject to the obligations of the provider under Article 16.” The extracted counterpart/recipient (“to the obligations of the provider under Article 16”) therefore belongs to this second predicate and does not identify a relational actor, counterpart, or recipient. No counterpart or recipient is structurally required for the first proposition. The two coordinated legal consequences should remain analytically distinct. No R/I/T or mechanism inference is made.' }
 'R4_2D-QA2B-083' = @{ Actor='NO'; Action='NO'; Object='NO'; Counterpart='NO'; Recipient='NO'; CorrectActor='no provider'; CorrectAction='should be able to gain'; CorrectObject='a competitive advantage'; CorrectCounterpart='N/A'; CorrectRecipient='N/A'; Class='CROSS_SENTENCE_CONTAMINATION; ACTOR_ACTION_FRAGMENTATION; MODALITY_LOSS; OBJECT_SPAN_MISALLOCATION; NON_ACTOR_COMPLEMENT_MISCLASSIFICATION'; Root=''; Canonical=''; Caveat=''; Note='Confirmed severe actor-action fragmentation with cross-sentence contamination. The extraction is best anchored to the final subordinate proposition: “no provider should be able to gain a competitive advantage in the Union market by applying lower copyright standards than those provided in the Union.” The actor is “no provider”; the action is “should be able to gain,” preserving the modal construction; and the object is “a competitive advantage.” “In the Union market” functions as scope, while “by applying lower copyright standards than those provided in the Union” expresses means/manner. The original actor improperly incorporates material from the surrounding “level playing field” clause. The extracted counterpart/recipient (“with the relevant obligations in this Regulation”) derives from the first sentence of the recital and is unrelated to the anchored proposition; moreover, it is a compliance complement rather than a relational actor. No counterpart or recipient is structurally required. No R/I/T or mechanism inference is made.' }
}

$sample = @(Import-Csv -LiteralPath $samplePath)
if ($sample.Count -ne 12) { throw "Expected 12 frozen sample rows; found $($sample.Count)." }
if (($sample.DIAGNOSTIC_ID | Sort-Object -Unique).Count -ne 12) { throw 'Duplicate diagnostic IDs in frozen sample.' }
if ($decisions.Count -ne 12) { throw "Expected 12 adjudications; found $($decisions.Count)." }
$sourceIds = @($sample | ForEach-Object DIAGNOSTIC_ID | Sort-Object)
$decisionIds = @($decisions.Keys | Sort-Object)
if (Compare-Object $sourceIds $decisionIds) { throw 'Adjudication IDs do not exactly match the frozen sample IDs.' }

$summary = [System.Collections.Generic.List[object]]::new()
$completed = foreach ($row in $sample) {
    $d = $decisions[$row.DIAGNOSTIC_ID]
    $row.HUMAN_PATTERN_CONFIRMED = 'YES'
    $row.HUMAN_ACTOR_CORRECT = $d.Actor; $row.HUMAN_ACTION_CORRECT = $d.Action
    $row.HUMAN_OBJECT_CORRECT = $d.Object; $row.HUMAN_COUNTERPART_CORRECT = $d.Counterpart
    $row.HUMAN_RECIPIENT_CORRECT = $d.Recipient
    $row.HUMAN_CORRECT_ACTOR = $d.CorrectActor; $row.HUMAN_CORRECT_ACTION = $d.CorrectAction
    $row.HUMAN_CORRECT_OBJECT = $d.CorrectObject; $row.HUMAN_CORRECT_COUNTERPART = $d.CorrectCounterpart
    $row.HUMAN_CORRECT_RECIPIENT = $d.CorrectRecipient
    $row.HUMAN_NOTES = $d.Note; $row.HUMAN_REVIEWER = $reviewer; $row.HUMAN_REVIEW_STATUS = 'REVIEWED'
    $row | Add-Member -NotePropertyName HUMAN_DIAGNOSTIC_DEFECT_CLASS -NotePropertyValue $d.Class -Force
    $row | Add-Member -NotePropertyName HUMAN_PRIMARY_ROOT_CAUSE -NotePropertyValue $d.Root -Force
    $secondaryPattern = if ($row.DIAGNOSTIC_ID -eq 'R4_2D-QA2B-089') { 'COUNTERPART_RECIPIENT_OVERATTRIBUTION' } else { '' }
    $row | Add-Member -NotePropertyName HUMAN_SECONDARY_DIAGNOSTIC_PATTERN -NotePropertyValue $secondaryPattern -Force
    $row | Add-Member -NotePropertyName HUMAN_CANONICAL_DIAGNOSTIC_EXAMPLE -NotePropertyValue $d.Canonical -Force
    $row | Add-Member -NotePropertyName OBJECT_SCHEMA_CAVEAT -NotePropertyValue $d.Caveat -Force
    $summary.Add([pscustomobject][ordered]@{
        DIAGNOSTIC_ID=$row.DIAGNOSTIC_ID; ACT=$row.CASE_ID; ORIGINAL_MODEL_SELECTION_PATTERN=$row.PATTERN
        HUMAN_PATTERN_CONFIRMED='YES'; HUMAN_ACTOR_CORRECT=$d.Actor; HUMAN_ACTION_CORRECT=$d.Action
        HUMAN_OBJECT_CORRECT=$d.Object; HUMAN_COUNTERPART_CORRECT=$d.Counterpart; HUMAN_RECIPIENT_CORRECT=$d.Recipient
        HUMAN_DIAGNOSTIC_DEFECT_CLASS=$d.Class; HUMAN_PRIMARY_ROOT_CAUSE=$d.Root
        HUMAN_SECONDARY_DIAGNOSTIC_PATTERN=$secondaryPattern
        HUMAN_CANONICAL_DIAGNOSTIC_EXAMPLE=$d.Canonical; HUMAN_REVIEWER=$reviewer
    })
    $row
}

$utf8 = New-Object System.Text.UTF8Encoding($false)
$completed | Export-Csv -LiteralPath $completedPath -NoTypeInformation -Encoding UTF8
$summary | Export-Csv -LiteralPath $summaryPath -NoTypeInformation -Encoding UTF8
$sampleHash = (Get-FileHash -LiteralPath $samplePath -Algorithm SHA256).Hash
$completedHash = (Get-FileHash -LiteralPath $completedPath -Algorithm SHA256).Hash
$summaryHash = (Get-FileHash -LiteralPath $summaryPath -Algorithm SHA256).Hash

$fieldCounts = foreach ($field in 'HUMAN_ACTOR_CORRECT','HUMAN_ACTION_CORRECT','HUMAN_OBJECT_CORRECT','HUMAN_COUNTERPART_CORRECT','HUMAN_RECIPIENT_CORRECT') {
    $n = @($completed | Where-Object { $_.$field -eq 'NO' }).Count
    "| $field | $n |"
}
$classCounts = @{}
foreach ($row in $completed) { foreach ($class in ($row.HUMAN_DIAGNOSTIC_DEFECT_CLASS -split '; ')) { if (!$classCounts.ContainsKey($class)) { $classCounts[$class]=0 }; $classCounts[$class]++ } }
$classTable = foreach ($class in ($classCounts.Keys | Sort-Object)) { "| $class | $($classCounts[$class]) |" }
$actTable = foreach ($act in @('D1_GDPR','D2_DSA','D3_AI_ACT')) {
    $a = @($summary | Where-Object ACT -eq $act)
    $pA = @($a | Where-Object ORIGINAL_MODEL_SELECTION_PATTERN -eq 'COUNTERPART_RECIPIENT_OVERATTRIBUTION').Count
    $pB = @($a | Where-Object ORIGINAL_MODEL_SELECTION_PATTERN -eq 'ACTOR_ACTION_FRAGMENTATION').Count
    "| $act | $($a.Count) | $pA/2 YES | $pB/2 YES |"
}
$report = @'
# R4.2D — Human diagnostic report

**Status:** `R4_2D_HUMAN_DIAGNOSTIC_COMPLETE_REPAIR_RULES_PENDING`  
**Reviewer:** @@REVIEWER@@  
**Human decisions:** 12/12 `REVIEWED`; 0 pending.  
**Scope:** purposive cross-model diagnostic sample only; no population-prevalence inference.

## Descriptive results

- Human cases: 12.
- `HUMAN_PATTERN_CONFIRMED`: YES = 12; PARTIALLY = 0; NO = 0.
- Original sample composition retained: 6 `COUNTERPART_RECIPIENT_OVERATTRIBUTION`, 6 `ACTOR_ACTION_FRAGMENTATION`; each pattern has 2 cases per act.
- Case `R4_2D-QA2B-089` additionally records `COUNTERPART_RECIPIENT_OVERATTRIBUTION` as the researcher-specified secondary selection pattern. This does not alter the original sample pattern or gate denominators.

| Field correctness marked NO | Cases |
|---|---:|
@@FIELD_COUNTS@@

Human diagnostic candidate-class frequencies (non-exclusive; labels preserved as candidate classes, not a definitive ontology):

| Candidate class | Cases |
|---|---:|
@@CLASS_COUNTS@@

## Predefined gate assessment

Gate rule: confirmation in all three acts, at least 4/6 YES or PARTIALLY, and at least 3/6 YES. The gate uses the original `PATTERN` used to select the sample, not human subclasses. Every sampled case was adjudicated YES; both patterns therefore pass: 6/6 YES overall and 2/2 YES in each act.

| Act | Cases | Pattern A confirmed | Pattern B confirmed |
|---|---:|---:|---:|
@@ACT_COUNTS@@

- A. `COUNTERPART_RECIPIENT_OVERATTRIBUTION`: `HUMAN_CONFIRMED_SYSTEMATIC_DEFECT` — PASS (6/6 YES; present and confirmed in GDPR, DSA and AI Act).
- B. `ACTOR_ACTION_FRAGMENTATION`: `HUMAN_CONFIRMED_SYSTEMATIC_DEFECT` — PASS (6/6 YES; present and confirmed in GDPR, DSA and AI Act).
- Gate counts are descriptive of this purposive sample, not estimates of corpus-wide prevalence.

## Interpretation and next gate

Cross-model detection and human root-cause diagnosis are distinct. Luna/Terra agreement identified records warranting review; human adjudication shows heterogeneous causes, including relational overattribution, proposition-boundary and cross-proposition failures, multi-proposition contamination, normative-complement misclassification, embedded structures, semantic substitution, relational omission, passive-actor invention, modality loss, span/predicate fragmentation, coordinated-proposition conflation, object-span misallocation and non-actor-complement misclassification. These remain `HUMAN_DIAGNOSTIC_CANDIDATE_CLASSES`, not a finalized ontology.

Because Pattern A passes, record `COUNTERPART_RECIPIENT = VARIABLE_PARSIMONY_CANDIDATE`. This is a candidate for dataset-design parsimony review only: do not remove or merge the fields now. Because Pattern B passes, record `ACTOR_ACTION_EXTRACTION_RULE_REPAIR_REQUIRED`; this concerns extraction/segmentation, not a change to intermediation theory.

The next phase may be proposed as `R4.2E — CONTROLLED STRUCTURAL REPAIR`, but it is not started here. No corpus-wide repair, automatic recoding, R/I/T coding, mechanism coding, ROTEM consultation or R4.3 work was performed. The original Luna extraction, Terra V2 review, frozen sample and source text are preserved.

## Firewall state

- `RIT_CODING = NOT_STARTED`
- `MECHANISM_CODING = NOT_STARTED`
- `ROTEM_CODING_CONSULTED = NO`
- `R4_3 = NOT_STARTED`
- `CORPUS_WIDE_REPAIR = NOT_EXECUTED`
- `R4_2_COMPLETE = NO`; `READY_FOR_R4_3 = NO`.

## Integrity

- Frozen original sample SHA-256: `@@SAMPLE_HASH@@`
- Completed human decisions SHA-256: `@@COMPLETED_HASH@@`
- Human summary SHA-256: `@@SUMMARY_HASH@@`

Full row-level decisions and notes are in `R4_2D_HUMAN_DIAGNOSTIC_COMPLETED.csv`; the sample itself remains unchanged.
'@
$report = $report.Replace('@@REVIEWER@@',$reviewer).Replace('@@FIELD_COUNTS@@',($fieldCounts -join "`n")).Replace('@@CLASS_COUNTS@@',($classTable -join "`n")).Replace('@@ACT_COUNTS@@',($actTable -join "`n")).Replace('@@SAMPLE_HASH@@',$sampleHash).Replace('@@COMPLETED_HASH@@',$completedHash).Replace('@@SUMMARY_HASH@@',$summaryHash)
[System.IO.File]::WriteAllText($reportPath, $report, $utf8)
"Created completed decision file, 12-row summary, and diagnostic report. Frozen sample SHA-256: $sampleHash"
