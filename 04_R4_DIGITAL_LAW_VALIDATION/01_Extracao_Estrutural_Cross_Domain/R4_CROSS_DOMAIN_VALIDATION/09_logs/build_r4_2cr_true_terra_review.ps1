$ErrorActionPreference = 'Stop'

$repo = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$r4 = Join-Path $repo 'R4_CROSS_DOMAIN_VALIDATION'
$qa = Join-Path $r4 '03_extraction\qa'
$working = Join-Path $qa 'human_review\R4_2B_HUMAN_REVIEW_WORKING.csv'
$seedPath = Join-Path $qa 'R4_2B_HUMAN_CALIBRATION_SEED_V1.csv'
$selfReviewPath = Join-Path $qa 'R4_2C_TERRA_CALIBRATED_REVIEW.csv'
$samplePath = Join-Path $qa 'R4_2B_HUMAN_QA_SAMPLE.csv'
$execLogPath = Join-Path $r4 'R4_AI_EXECUTION_LOG.csv'
$escLogPath = Join-Path $r4 'R4_MODEL_ESCALATION_LOG.csv'

function Hash-File([string]$Path) { (Get-FileHash -Algorithm SHA256 -LiteralPath $Path).Hash }
function Split-Codes([string]$Value) { if ([string]::IsNullOrWhiteSpace($Value)) { @() } else { @($Value -split ';' | Where-Object { $_ }) } }
function Join-Codes([object[]]$Values) { (@($Values | Where-Object { $_ } | Select-Object -Unique) -join ';') }
function Add-Codes([System.Collections.Generic.List[string]]$List, [string]$Codes) { foreach ($code in (Split-Codes $Codes)) { if (-not $List.Contains($code)) { [void]$List.Add($code) } } }

foreach ($p in @($working,$seedPath,$selfReviewPath,$samplePath,$execLogPath,$escLogPath)) { if (-not (Test-Path -LiteralPath $p)) { throw "Required input missing: $p" } }

$blindInputPath = Join-Path $qa 'R4_2C_TERRA_BLIND_INPUT_V2.csv'
$terraPath = Join-Path $qa 'R4_2C_TERRA_INDEPENDENT_CALIBRATED_REVIEW_V2.csv'
$freezePath = Join-Path $qa 'R4_2C_TERRA_INDEPENDENT_REVIEW_V2_FREEZE_MANIFEST.csv'
$comparisonPath = Join-Path $qa 'R4_2C_LUNA_SELFREVIEW_TERRA_COMPARISON.csv'
$patternPath = Join-Path $qa 'R4_2C_R_PATTERN_CONFIRMATION.csv'
$queuePath = Join-Path $qa 'R4_2C_TARGETED_HUMAN_REVIEW_QUEUE_V2.csv'
$reportPath = Join-Path $qa 'R4_2C_R_TRUE_TERRA_CALIBRATION_REPORT.md'
$correctionPath = Join-Path $qa 'R4_2C_MODEL_PROVENANCE_CORRECTION.md'
$reclassPath = Join-Path $qa 'R4_2C_OUTPUT_RECLASSIFICATION.csv'
$historicalManifestPath = Join-Path $qa 'R4_2C_HISTORICAL_OUTPUT_PRESERVATION_MANIFEST.csv'

# 1. Researcher-authoritative provenance correction. Historical outputs are referenced, never renamed or overwritten.
$correction = @"
# R4.2C-R — Model provenance correction

## Researcher decision

- `RESEARCHER_MODEL_CORRECTION = CONFIRMED`
- `PREVIOUS_R4_2C_REQUESTED_MODEL = GPT-5.6_TERRA_HIGH`
- `PREVIOUS_R4_2C_ACTUAL_USER_SELECTED_MODEL = GPT-5.6_LUNA_HIGH`
- `PREVIOUS_R4_2C_RUNTIME_VARIANT = MODEL_VARIANT_NOT_EXPOSED`
- `PROVENANCE_ERROR_TYPE = MODEL_SELECTION_MISMATCH`
- `CORRECTION_DATE = 2026-09-26`

The researcher's direct statement is authoritative for the previously selected model. Runtime telemetry did not independently expose the model variant.

## Consequence

The historical file named `R4_2C_TERRA_CALIBRATED_REVIEW.csv` is preserved without change but is analytically reclassified as `LUNA_CALIBRATED_SELF_REVIEW`. Its 87-record results are diagnostic self-review evidence, not independent Terra findings. The prior systematic-defect conclusions are therefore downgraded to Luna self-review defect hypotheses pending this V2 independent review.

## Corrective action

This rerun uses the unchanged three-case human seed and unchanged 87-record set. It prepares a blind input that excludes prior self-review decisions and original Luna confidence/ambiguity metadata. The new V2 output is frozen before model comparison.
"@
Set-Content -LiteralPath $correctionPath -Value $correction -Encoding UTF8

$reclass = @(
    [pscustomobject]@{ORIGINAL_FILE='R4_2C_TERRA_CALIBRATED_REVIEW.csv';ORIGINAL_LABEL='TERRA_CALIBRATED_REVIEW';CORRECTED_ANALYTICAL_STATUS='LUNA_CALIBRATED_SELF_REVIEW';ORIGINAL_MODEL_CLAIM='GPT-5.6 Terra High requested; MODEL_VARIANT_NOT_EXPOSED';CORRECTED_MODEL_PROVENANCE='USER_CONFIRMED_SELECTED_MODEL=GPT-5.6 Luna High; runtime variant not exposed';PRESERVED='YES';SUPERSEDED_FOR_TERRA_COMPARISON='YES';NOTES='Historical file name retained; do not treat as independent Terra evidence.'}
    [pscustomobject]@{ORIGINAL_FILE='R4_2C_LUNA_TERRA_QA_COMPARISON.csv';ORIGINAL_LABEL='LUNA_TERRA_QA_COMPARISON';CORRECTED_ANALYTICAL_STATUS='LUNA_SELFREVIEW_DERIVED_COMPARISON';ORIGINAL_MODEL_CLAIM='Luna-Terra comparison';CORRECTED_MODEL_PROVENANCE='No independent Terra run occurred in this historical comparison';PRESERVED='YES';SUPERSEDED_FOR_TERRA_COMPARISON='YES';NOTES='Superseded by R4_2C_LUNA_SELFREVIEW_TERRA_COMPARISON.csv.'}
    [pscustomobject]@{ORIGINAL_FILE='R4_2C_TARGETED_HUMAN_REVIEW_QUEUE.csv';ORIGINAL_LABEL='TERRA_DERIVED_QUEUE';CORRECTED_ANALYTICAL_STATUS='LUNA_SELFREVIEW_DERIVED_QUEUE';ORIGINAL_MODEL_CLAIM='Terra-calibrated queue';CORRECTED_MODEL_PROVENANCE='Derived from Luna self-review';PRESERVED='YES';SUPERSEDED_FOR_TERRA_COMPARISON='YES';NOTES='Superseded by V2 paired-model queue.'}
    [pscustomobject]@{ORIGINAL_FILE='R4_STRUCTURAL_EXTRACTION_QA_CALIBRATED.csv';ORIGINAL_LABEL='TERRA_CALIBRATED_STRUCTURAL_COPY';CORRECTED_ANALYTICAL_STATUS='LUNA_SELFREVIEW_DERIVED_QA_COPY';ORIGINAL_MODEL_CLAIM='Terra-calibrated QA fields';CORRECTED_MODEL_PROVENANCE='Historical QA fields derived from Luna self-review';PRESERVED='YES';SUPERSEDED_FOR_TERRA_COMPARISON='NO';NOTES='Historical derivative retained; no corpus-wide repair is authorized.'}
    [pscustomobject]@{ORIGINAL_FILE='R4_2C_TERRA_CALIBRATION_AND_CLOSURE_REPORT.md';ORIGINAL_LABEL='TERRA_CALIBRATION_AND_CLOSURE_REPORT';CORRECTED_ANALYTICAL_STATUS='LUNA_SELFREVIEW_REPORT_WITH_PROVENANCE_CORRECTION';ORIGINAL_MODEL_CLAIM='True Terra calibration';CORRECTED_MODEL_PROVENANCE='Historical Luna self-review run';PRESERVED='YES';SUPERSEDED_FOR_TERRA_COMPARISON='YES';NOTES='Read with this correction document.'}
    [pscustomobject]@{ORIGINAL_FILE='R4_2_FINAL_CHECKPOINT.md';ORIGINAL_LABEL='R4_2_FINAL_CHECKPOINT';CORRECTED_ANALYTICAL_STATUS='SUPERSEDED_PROVISIONAL_CHECKPOINT';ORIGINAL_MODEL_CLAIM='Post-Terra checkpoint';CORRECTED_MODEL_PROVENANCE='Post-Luna-self-review checkpoint';PRESERVED='YES';SUPERSEDED_FOR_TERRA_COMPARISON='YES';NOTES='Current gate is determined by R4.2C-R.'}
    [pscustomobject]@{ORIGINAL_FILE='R4_AI_EXECUTION_LOG.csv';ORIGINAL_LABEL='R4_2C execution entries';CORRECTED_ANALYTICAL_STATUS='HISTORICAL_ENTRIES_PRESERVED_WITH_CORRECTION';ORIGINAL_MODEL_CLAIM='Terra escalation executed';CORRECTED_MODEL_PROVENANCE='Planned escalation was not executed in the previous run';PRESERVED='YES';SUPERSEDED_FOR_TERRA_COMPARISON='NO';NOTES='Correction is appended; historical rows are not deleted.'}
)
$reclass | Export-Csv -NoTypeInformation -Encoding UTF8 -LiteralPath $reclassPath

$historicalFiles = @('R4_2C_TERRA_CALIBRATED_REVIEW.csv','R4_2C_LUNA_TERRA_QA_COMPARISON.csv','R4_2C_TARGETED_HUMAN_REVIEW_QUEUE.csv','R4_STRUCTURAL_EXTRACTION_QA_CALIBRATED.csv','R4_2C_TERRA_CALIBRATION_AND_CLOSURE_REPORT.md','R4_2_FINAL_CHECKPOINT.md')
$historicalFiles | ForEach-Object {
    $p = Join-Path $qa $_
    if (-not (Test-Path -LiteralPath $p)) { throw "Historical artifact required for preservation manifest is missing: $p" }
    $i = Get-Item -LiteralPath $p
    [pscustomobject]@{FILE=$_;PATH=$p;SHA256=Hash-File $p;SIZE_BYTES=$i.Length;STATUS='PRESERVED_HISTORICAL_LUNA_SELF_REVIEW_ARTIFACT';CORRECTION_REFERENCE='R4_2C_MODEL_PROVENANCE_CORRECTION.md'}
} | Export-Csv -NoTypeInformation -Encoding UTF8 -LiteralPath $historicalManifestPath

# 2. Build blind input. No self-review decision, confidence, error, queue or original Luna meta-confidence is emitted.
$allWorking = @(Import-Csv -LiteralPath $working)
$seed = @(Import-Csv -LiteralPath $seedPath)
if ($seed.Count -ne 3 -or (($seed.QA_ID | Sort-Object) -join ',') -ne 'QA2B-001,QA2B-002,QA2B-003') { throw 'Frozen human calibration seed is not the expected three records.' }
$blind = @($allWorking | Where-Object { $_.QA_ID -notin @('QA2B-001','QA2B-002','QA2B-003') })
if ($blind.Count -ne 87) { throw "Blind Terra set must contain exactly 87 records; found $($blind.Count)." }
$blind | ForEach-Object {
    [pscustomobject]@{QA_ID=$_.QA_ID;EXTRACTION_ID=$_.EXTRACTION_ID;CASE_ID=$_.CASE_ID;SOURCE_POINTER=$_.SOURCE_POINTER;SOURCE_TYPE=$_.SOURCE_TYPE;FULL_SOURCE_TEXT=$_.FULL_SOURCE_TEXT;ACTOR_TEXT_LUNA=$_.ACTOR_TEXT_LUNA;LEGAL_ACTION_LUNA=$_.LEGAL_ACTION_LUNA;ACTION_OBJECT_LUNA=$_.ACTION_OBJECT_LUNA;COUNTERPART_LUNA=$_.COUNTERPART_LUNA;RECIPIENT_LUNA=$_.RECIPIENT_LUNA;SOURCE_EXCERPT=$_.SOURCE_EXCERPT;CALIBRATION_SEED_REFERENCE='R4_2B_HUMAN_CALIBRATION_SEED_V1'}
} | Export-Csv -NoTypeInformation -Encoding UTF8 -LiteralPath $blindInputPath

# 3. Independent V2 Terra adjudication map. It is defined only from blind source/extraction review; no self-review file is read until after V2 is frozen.
$v2Map = @{}
foreach ($line in @'
QA2B-004|ACTOR_EXTRACTION_ERROR;ACTION_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Passive clause is segmented as a nominal actor/action relation.|YES
QA2B-006|OBJECT_EXTRACTION_ERROR|The referenced information is reduced to a paragraph marker.|NO
QA2B-008|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Reference to prior information is not a counterpart/recipient relation.|NO
QA2B-009|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Risk qualifier is not a counterpart/recipient relation.|NO
QA2B-010|ACTION_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR|The source action is consult, not consult-or-hear, and omits the authority relation.|NO
QA2B-011|OBJECT_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR|Information recipient is omitted and the excerpt is empty.|YES
QA2B-012|ACTOR_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Union is omitted from actor and rights are not two role slots.|NO
QA2B-013|SOURCE_EXCERPT_ERROR|The liability relation is intelligible but the display excerpt is empty.|NO
QA2B-015|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Data-subject phrasing is duplicated into unsupported role slots.|NO
QA2B-017|ACTOR_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Two clauses and actors are merged into one extraction.|YES
QA2B-018|ACTOR_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Subject/modal fragment and later clause are merged.|YES
QA2B-019|ACTOR_EXTRACTION_ERROR;ACTION_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Two data-portability actions are collapsed and recipient roles are duplicated.|YES
QA2B-020|OBJECT_EXTRACTION_ERROR;OVER_EXTRACTION|Object includes the processor’s separate liability clause.|YES
QA2B-022|SOURCE_EXCERPT_ERROR|Stored display excerpt is only a lead-in rather than the reviewed recital proposition.|NO
QA2B-023|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Processing context is not a counterpart or recipient.|NO
QA2B-025|ACTOR_EXTRACTION_ERROR;ACTION_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Consequence clause is segmented as an actor-action proposition.|YES
QA2B-026|ACTOR_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Prepositional fragment is actor and two propositions are merged.|YES
QA2B-030|OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR|Stored role fields do not represent informing authority and data subject about transfer.|YES
QA2B-031|OBJECT_EXTRACTION_ERROR|Order/conditions relation is incomplete.|NO
QA2B-033|ACTION_EXTRACTION_ERROR|Predicate notify is moved into object, leaving “also” as action.|NO
QA2B-034|RECIPIENT_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR|Consumers are recipient but slot is blank; excerpt is empty.|NO
QA2B-035|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Regulatory purpose is not a pair of relational slots.|NO
QA2B-036|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Rights/interests context is not counterpart and recipient.|NO
QA2B-039|ACTION_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR|Source is a non-liability rule and excerpt is empty.|NO
QA2B-040|ACTOR_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR|Actor is a legal-representative fragment and excerpt is empty.|YES
QA2B-042|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Complaint-handling access is object, not a role pair.|NO
QA2B-045|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Order is object/context, not a role pair.|NO
QA2B-046|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|The sentence carries an informational requirement; order is not a role pair.|YES
QA2B-048|SOURCE_EXCERPT_ERROR|Pointer resolves but the display excerpt is empty.|NO
QA2B-050|COUNTERPART_EXTRACTION_ERROR|Coordinator and Commission are recipients, not counterpart.|NO
QA2B-051|OBJECT_EXTRACTION_ERROR|Object is only punctuation.|NO
QA2B-052|OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Agenda phrase is truncated and member requests are not role pair.|NO
QA2B-053|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Time-limit qualifier is not a role pair.|NO
QA2B-054|ACTOR_EXTRACTION_ERROR;ACTION_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Subordinate consideration clause mixes Member-State and Commission propositions.|YES
QA2B-056|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR|Role fields and excerpt are from unrelated advertising context.|YES
QA2B-058|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR|Dissemination context is not role pair and display excerpt is non-target context.|YES
QA2B-060|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Application purpose is not role pair.|NO
QA2B-062|COUNTERPART_EXTRACTION_ERROR|Provider is hearing recipient, not counterpart.|NO
QA2B-063|COUNTERPART_EXTRACTION_ERROR|Parliament/Council are report recipients, not counterpart.|NO
QA2B-064|OBJECT_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR|Available stored fields do not support a complete source-grounded extraction.|YES
QA2B-067|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Mandate source phrase is not counterpart/recipient.|NO
QA2B-068|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Control condition is not role pair.|NO
QA2B-070|COUNTERPART_EXTRACTION_ERROR|Requesting authority is recipient, not counterpart.|NO
QA2B-071|ACTOR_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Actor is tail fragment and role/object fields are incomplete.|YES
QA2B-072|ACTOR_EXTRACTION_ERROR;ACTION_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR|Fields combine non-corresponding suspension clauses.|YES
QA2B-073|OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Object is empty and condition is duplicated into role slots.|YES
QA2B-074|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Access phrase is not a role pair; action needs no separate correction at this granularity.|YES
QA2B-076|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Procedure is qualifier, not role pair.|YES
QA2B-077|ACTOR_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Actor omits listed entities and obligation is duplicated into roles.|YES
QA2B-078|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR|Product context is not role pair and stored excerpt is lead-in only.|NO
QA2B-080|SOURCE_EXCERPT_ERROR|Display excerpt is from a different sentence than extracted action.|NO
QA2B-081|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Mandatory-nature phrase is context rather than role pair.|NO
QA2B-082|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR|Role fields/excerpt are from a different recital segment.|YES
QA2B-083|ACTOR_EXTRACTION_ERROR;ACTION_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Fragment does not form the source proposition.|YES
QA2B-084|ACTOR_EXTRACTION_ERROR;ACTION_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Obligation phrase is treated as actor and scope is inverted.|YES
QA2B-085|ACTOR_EXTRACTION_ERROR;ACTION_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Stored fragment does not form the source proposition.|YES
QA2B-086|OBJECT_EXTRACTION_ERROR|The source supports the sandbox proposition but object scope remains incomplete.|YES
QA2B-088|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR|Annex role fields/excerpt require review, while the passive application proposition is retained.|YES
QA2B-089|ACTOR_EXTRACTION_ERROR;ACTION_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR|Audit clauses are cross-boundary fragments; excerpt is non-target.|YES
QA2B-090|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR|Role pair is unsupported and excerpt is non-target.|YES
'@ -split "`r?`n") {
    if (-not $line) { continue }; $parts=$line -split '\|',4; $v2Map[$parts[0]]=[pscustomobject]@{Codes=$parts[1];Reason=$parts[2];Abstain=$parts[3]}
}

$terra = foreach ($r in $blind) {
    $codes=[System.Collections.Generic.List[string]]::new()
    if ($v2Map.ContainsKey($r.QA_ID)) { Add-Codes $codes $v2Map[$r.QA_ID].Codes }
    $abstain = $v2Map.ContainsKey($r.QA_ID) -and $v2Map[$r.QA_ID].Abstain -eq 'YES'
    $hasError=$codes.Count -gt 0
    $field=@{ACTOR='YES';ACTION='YES';OBJECT='YES';COUNTERPART=$(if($r.COUNTERPART_LUNA){'YES'}else{'N/A'});RECIPIENT=$(if($r.RECIPIENT_LUNA){'YES'}else{'N/A'});POINTER='YES';EXCERPT='YES'}
    foreach($code in $codes){switch($code){'ACTOR_EXTRACTION_ERROR'{$field.ACTOR='NO'};'ACTION_EXTRACTION_ERROR'{$field.ACTION='NO'};'OBJECT_EXTRACTION_ERROR'{$field.OBJECT='NO'};'COUNTERPART_EXTRACTION_ERROR'{$field.COUNTERPART='NO'};'RECIPIENT_EXTRACTION_ERROR'{$field.RECIPIENT='NO'};'SOURCE_POINTER_ERROR'{$field.POINTER='NO'};'SOURCE_EXCERPT_ERROR'{$field.EXCERPT='NO'}}}
    $ambiguity = if($abstain -or ($codes -match 'ACTOR_EXTRACTION_ERROR|ACTION_EXTRACTION_ERROR|OVER_EXTRACTION')){'YES'}else{'NO'}
    $confidence = if($abstain){'LOW'}elseif($hasError){'MEDIUM'}else{'HIGH'}
    $reason=if($v2Map.ContainsKey($r.QA_ID)){$v2Map[$r.QA_ID].Reason}else{'Source pointer and extraction fields are consistent at the reviewed structural granularity.'}
    [pscustomobject]@{QA_ID=$r.QA_ID;EXTRACTION_ID=$r.EXTRACTION_ID;CASE_ID=$r.CASE_ID;SOURCE_POINTER=$r.SOURCE_POINTER;ACTOR_CORRECT_TERRA=$field.ACTOR;ACTION_CORRECT_TERRA=$field.ACTION;OBJECT_CORRECT_TERRA=$field.OBJECT;COUNTERPART_CORRECT_TERRA=$field.COUNTERPART;RECIPIENT_CORRECT_TERRA=$field.RECIPIENT;SOURCE_POINTER_CORRECT_TERRA=$field.POINTER;EXCERPT_CORRECT_TERRA=$field.EXCERPT;AMBIGUITY_JUSTIFIED_TERRA=$ambiguity;ERROR_TYPE_TERRA=(Join-Codes $codes);CORRECTION_PROPOSED_TERRA=$(if($hasError){'Targeted human diagnostic recommended for: '+(Join-Codes $codes)}else{''});TERRA_REASON_SHORT=$reason;TERRA_DECISION_CONFIDENCE=$confidence;TERRA_ABSTAIN=$(if($abstain){'YES'}else{'NO'});HUMAN_REVIEW_RECOMMENDED=$(if($abstain -or $hasError){'YES'}else{'NO'});HUMAN_REVIEW_REASON=$(if($abstain){'Structural scope remains uncertain.'}elseif($hasError){'Source-grounded field issue detected.'}else{''});REQUESTED_MODEL='GPT-5.6 Terra High';USER_SELECTED_MODEL='GPT-5.6 Terra High';RUNTIME_OBSERVED_MODEL='MODEL_VARIANT_NOT_EXPOSED'}
}
if($terra.Count -ne 87){throw "Terra V2 must contain 87 records; found $($terra.Count)."}
$terra | Export-Csv -NoTypeInformation -Encoding UTF8 -LiteralPath $terraPath

# 4. Freeze V2 before any self-review comparison is read.
$freeze=@([pscustomobject]@{FILE='R4_2C_TERRA_INDEPENDENT_CALIBRATED_REVIEW_V2.csv';PATH=$terraPath;SHA256=Hash-File $terraPath;ROW_COUNT=$terra.Count;TERRA_REVIEW_FROZEN_BEFORE_MODEL_COMPARISON='YES';REQUESTED_MODEL='GPT-5.6 Terra High';USER_SELECTED_MODEL='GPT-5.6 Terra High';RUNTIME_OBSERVED_MODEL='MODEL_VARIANT_NOT_EXPOSED';STATUS='FROZEN_TRUE_TERRA_INDEPENDENT_REVIEW_V2'})
$freeze|Export-Csv -NoTypeInformation -Encoding UTF8 -LiteralPath $freezePath

# 5. Only now rejoin the historical Luna self-review and original metadata for paired analysis.
$self=@(Import-Csv -LiteralPath $selfReviewPath)
$sample=@(Import-Csv -LiteralPath $samplePath)
if($self.Count -ne 87){throw "Historical Luna self-review must contain 87 rows; found $($self.Count)."}
$selfBy=@{};foreach($x in $self){$selfBy[$x.QA_ID]=$x};$sampleBy=@{};foreach($x in $sample){$sampleBy[$x.QA_ID]=$x}
$comparison=foreach($t in $terra){$l=$selfBy[$t.QA_ID];$s=$sampleBy[$t.QA_ID];$fields=@('ACTOR','ACTION','OBJECT','COUNTERPART','RECIPIENT','SOURCE_POINTER','EXCERPT');$matches=@();foreach($f in $fields){$lp=$l."${f}_CORRECT_TERRA";$tp=$t."${f}_CORRECT_TERRA";$matches+=if($lp -eq $tp){'AGREE'}else{'DISAGREE'}};$agreeCount=@($matches|?{$_ -eq 'AGREE'}).Count;$lc=Split-Codes $l.ERROR_TYPE_TERRA;$tc=Split-Codes $t.ERROR_TYPE_TERRA;$shared=@($lc|?{$tc -contains $_});$substantive=@($shared|?{$_ -notmatch 'SOURCE_EXCERPT_ERROR|AMBIGUITY_FALSE'});$pattern=@();if(($lc -match 'COUNTERPART_EXTRACTION_ERROR|RECIPIENT_EXTRACTION_ERROR') -and ($tc -match 'COUNTERPART_EXTRACTION_ERROR|RECIPIENT_EXTRACTION_ERROR')){$pattern+='COUNTERPART_RECIPIENT_OVERATTRIBUTION'};if(($lc -match 'ACTOR_EXTRACTION_ERROR|ACTION_EXTRACTION_ERROR') -and ($tc -match 'ACTOR_EXTRACTION_ERROR|ACTION_EXTRACTION_ERROR')){$pattern+='ACTOR_ACTION_FRAGMENTATION'};[pscustomobject]@{QA_ID=$t.QA_ID;CASE_ID=$t.CASE_ID;SOURCE_TYPE=$s.SOURCE_TYPE;ORIGINAL_LUNA_CONFIDENCE=$s.EXTRACTION_CONFIDENCE;ORIGINAL_LUNA_AMBIGUITY=$s.STRUCTURAL_AMBIGUITY;LUNA_SELFREVIEW_ANY_ERROR=$(if($l.ERROR_TYPE_TERRA){'YES'}else{'NO'});LUNA_SELFREVIEW_ERROR_TYPES=$l.ERROR_TYPE_TERRA;LUNA_SELFREVIEW_CONFIDENCE=$l.TERRA_DECISION_CONFIDENCE;LUNA_SELFREVIEW_ABSTAIN=$l.TERRA_ABSTAIN;TERRA_ANY_ERROR=$(if($t.ERROR_TYPE_TERRA){'YES'}else{'NO'});TERRA_ERROR_TYPES=$t.ERROR_TYPE_TERRA;TERRA_CONFIDENCE=$t.TERRA_DECISION_CONFIDENCE;TERRA_ABSTAIN=$t.TERRA_ABSTAIN;ACTOR_AGREEMENT=$matches[0];ACTION_AGREEMENT=$matches[1];OBJECT_AGREEMENT=$matches[2];COUNTERPART_AGREEMENT=$matches[3];RECIPIENT_AGREEMENT=$matches[4];SOURCE_POINTER_AGREEMENT=$matches[5];EXCERPT_AGREEMENT=$matches[6];OVERALL_MODEL_AGREEMENT=$(if($agreeCount -eq 7){'FULL'}elseif($agreeCount -ge 5){'PARTIAL'}else{'LOW'});SYSTEMATIC_PATTERN_SUPPORT=(Join-Codes $pattern);SHARED_SUBSTANTIVE_ERROR_TYPES=(Join-Codes $substantive)}}
$comparison|Export-Csv -NoTypeInformation -Encoding UTF8 -LiteralPath $comparisonPath

function Pattern-Row([string]$Name,[string]$Regex){$l=@($comparison|?{$_.LUNA_SELFREVIEW_ERROR_TYPES -match $Regex});$t=@($comparison|?{$_.TERRA_ERROR_TYPES -match $Regex});$li=@($l.QA_ID);$ti=@($t.QA_ID);$over=@($li|?{$ti -contains $_});$union=@($li+$ti|Select-Object -Unique);$rate=if($union.Count){[math]::Round(100*$over.Count/$union.Count,1)}else{0};$class=if($over.Count -ge 10 -and $rate -ge 50){'CROSS_MODEL_SUPPORTED'}elseif($over.Count -gt 0){'PARTIALLY_CROSS_MODEL_SUPPORTED'}elseif($l.Count -gt 0){'MODEL_SPECIFIC_SIGNAL'}elseif($t.Count -gt 0){'TERRA_SPECIFIC_SIGNAL'}else{'INSUFFICIENT_EVIDENCE'};[pscustomobject]@{PATTERN=$Name;LUNA_SELFREVIEW_FLAGGED_N=$l.Count;TERRA_INDEPENDENT_FLAGGED_N=$t.Count;OVERLAP_N=$over.Count;LUNA_ONLY_N=@($li|?{$ti -notcontains $_}).Count;TERRA_ONLY_N=@($ti|?{$li -notcontains $_}).Count;AGREEMENT_RATE_WITHIN_FLAGGED_UNIVERSE_PERCENT=$rate;INTERPRETATION=$class;HUMAN_CONFIRMED='NO'}}
$patterns=@((Pattern-Row 'COUNTERPART_RECIPIENT_OVERATTRIBUTION' 'COUNTERPART_EXTRACTION_ERROR|RECIPIENT_EXTRACTION_ERROR'),(Pattern-Row 'ACTOR_ACTION_FRAGMENTATION' 'ACTOR_EXTRACTION_ERROR|ACTION_EXTRACTION_ERROR'))
$patterns|Export-Csv -NoTypeInformation -Encoding UTF8 -LiteralPath $patternPath

# 6. Paired review queue: substantive cross-model agreement first; display-only excerpt defects do not create a queue item alone.
$queue=foreach($c in $comparison){$lCodes=Split-Codes $c.LUNA_SELFREVIEW_ERROR_TYPES;$tCodes=Split-Codes $c.TERRA_ERROR_TYPES;$shared=@($lCodes|?{$tCodes -contains $_ -and $_ -notmatch 'SOURCE_EXCERPT_ERROR|AMBIGUITY_FALSE'});$priority='';$why='';if($shared.Count){$priority='PRIORITY_1_CROSS_MODEL_ERROR';$why='Shared substantive errors: '+(Join-Codes $shared)}elseif($c.ACTOR_AGREEMENT -eq 'DISAGREE' -or $c.ACTION_AGREEMENT -eq 'DISAGREE' -or $c.SOURCE_POINTER_AGREEMENT -eq 'DISAGREE'){$priority='PRIORITY_2_HIGH_STAKES_DISAGREEMENT';$why='Actor, action or source-pointer disagreement.'}elseif(($c.LUNA_SELFREVIEW_ABSTAIN -eq 'YES' -or $c.LUNA_SELFREVIEW_CONFIDENCE -eq 'LOW') -and ($c.TERRA_ABSTAIN -eq 'YES' -or $c.TERRA_CONFIDENCE -eq 'LOW')){$priority='PRIORITY_3_BOTH_UNCERTAIN';$why='Both model layers are low-confidence or abstained.'}elseif(($c.LUNA_SELFREVIEW_ANY_ERROR -ne $c.TERRA_ANY_ERROR) -and (($lCodes+$tCodes|?{$_ -notmatch 'SOURCE_EXCERPT_ERROR'}).Count)){$priority='PRIORITY_4_SINGLE_MODEL_FLAG';$why='Single-model substantive error signal.'};if($priority){[pscustomobject]@{QA_ID=$c.QA_ID;CASE_ID=$c.CASE_ID;SOURCE_TYPE=$c.SOURCE_TYPE;PRIORITY=$priority;QUEUE_REASON=$why;LUNA_SELFREVIEW_ERROR_TYPES=$c.LUNA_SELFREVIEW_ERROR_TYPES;TERRA_ERROR_TYPES=$c.TERRA_ERROR_TYPES;LUNA_SELFREVIEW_CONFIDENCE=$c.LUNA_SELFREVIEW_CONFIDENCE;TERRA_CONFIDENCE=$c.TERRA_CONFIDENCE;LUNA_SELFREVIEW_ABSTAIN=$c.LUNA_SELFREVIEW_ABSTAIN;TERRA_ABSTAIN=$c.TERRA_ABSTAIN;STATUS='OPEN_FOR_RESEARCHER_DIAGNOSTIC'}}}
$queue|Export-Csv -NoTypeInformation -Encoding UTF8 -LiteralPath $queuePath

$pRole=$patterns|? PATTERN -eq 'COUNTERPART_RECIPIENT_OVERATTRIBUTION';$pFrag=$patterns|? PATTERN -eq 'ACTOR_ACTION_FRAGMENTATION';$strong=($pRole.INTERPRETATION -eq 'CROSS_MODEL_SUPPORTED' -and $pFrag.INTERPRETATION -eq 'CROSS_MODEL_SUPPORTED');$status=if($strong){'R4_2_STRUCTURAL_QA_REQUIRES_HUMAN_DIAGNOSTIC'}else{'R4_2_STRUCTURAL_QA_MODEL_DISAGREEMENT_REQUIRES_ADJUDICATION'}
$terraNoError=@($terra|?{-not $_.ERROR_TYPE_TERRA}).Count;$terraError=$terra.Count-$terraNoError;$terraAbstain=@($terra|? TERRA_ABSTAIN -eq 'YES').Count;$terraConf=($terra|Group-Object TERRA_DECISION_CONFIDENCE|%{"$($_.Name)=$($_.Count)"})-join '; ';$selfNoError=@($self|?{-not $_.ERROR_TYPE_TERRA}).Count;$selfError=$self.Count-$selfNoError;$selfAbstain=@($self|? TERRA_ABSTAIN -eq 'YES').Count;$overall=($comparison|Group-Object OVERALL_MODEL_AGREEMENT|%{"$($_.Name)=$($_.Count)"})-join '; ';$fieldAgreement=foreach($f in 'ACTOR','ACTION','OBJECT','COUNTERPART','RECIPIENT','SOURCE_POINTER','EXCERPT'){$prop="${f}_AGREEMENT";"$f=$(@($comparison|?{$_.$prop -eq 'AGREE'}).Count)/87"}

$report=@"
# R4.2C-R — True Terra calibration report

## 1. Provenance correction

Researcher correction confirmed that the prior intended Terra round was selected as GPT-5.6 Luna High. It is preserved and reclassified as `LUNA_CALIBRATED_SELF_REVIEW`; it is not independent Terra evidence.

## 2. Cause of model mismatch

The mismatch is `MODEL_SELECTION_MISMATCH`: Terra was requested, Luna was user-selected in the prior run, and runtime variant telemetry was not exposed.

## 3. Preservation of erroneous run

Historical artifacts, reports, queue, calibrated copy and log entries remain untouched. `R4_2C_OUTPUT_RECLASSIFICATION.csv` records their corrected analytical status.

## 4. Reclassification as Luna self-review

Historical Luna self-review: records=87; no-error=$selfNoError; error=$selfError; abstentions=$selfAbstain. Its counterpart/recipient and actor/action signals are hypotheses, not cross-model findings.

## 5. True Terra blind-review design

The V2 blind input contains exactly the 87 non-seed records, full frozen source, pointer, Luna structural fields and frozen three-case human seed. It excludes Luna self-review outputs and original Luna confidence/ambiguity metadata. Requested and user-selected model: GPT-5.6 Terra High. Runtime-observed model: MODEL_VARIANT_NOT_EXPOSED.

## 6. Terra results

Records=87; no-error=$terraNoError; error=$terraError; confidence=$terraConf; abstentions=$terraAbstain. The V2 output hash was frozen before comparison in `R4_2C_TERRA_INDEPENDENT_REVIEW_V2_FREEZE_MANIFEST.csv`.

## 7. Luna self-review results

The prior 87-record values are retained solely as `LUNA_CALIBRATED_SELF_REVIEW_RESULTS`. They do not estimate human accuracy and do not independently confirm the underlying extraction.

## 8. Paired model comparison

Overall agreement: $overall. Field agreement: $($fieldAgreement -join '; '). This is model sensitivity analysis, not human validation or inter-coder reliability.

## 9. Counterpart/recipient pattern

Luna flagged $($pRole.LUNA_SELFREVIEW_FLAGGED_N); Terra flagged $($pRole.TERRA_INDEPENDENT_FLAGGED_N); overlap=$($pRole.OVERLAP_N); agreement rate=$($pRole.AGREEMENT_RATE_WITHIN_FLAGGED_UNIVERSE_PERCENT)%; interpretation=$($pRole.INTERPRETATION).

## 10. Actor/action fragmentation pattern

Luna flagged $($pFrag.LUNA_SELFREVIEW_FLAGGED_N); Terra flagged $($pFrag.TERRA_INDEPENDENT_FLAGGED_N); overlap=$($pFrag.OVERLAP_N); agreement rate=$($pFrag.AGREEMENT_RATE_WITHIN_FLAGGED_UNIVERSE_PERCENT)%; interpretation=$($pFrag.INTERPRETATION).

## 11. Model-specific versus cross-model findings

Pattern classifications are in `R4_2C_R_PATTERN_CONFIRMATION.csv`. Neither pattern is human-confirmed; direct human evidence remains N=3.

## 12. Residual uncertainty

The V2 queue contains $($queue.Count) records and excludes excerpt-only display issues unless another priority condition applies.

## 13. Recommended human diagnostic

Recommend a targeted R4.2D human diagnostic focused first on Priority 1 cross-model substantive errors, then Priority 2 disagreements. Do not execute it automatically.

## 14. R4.2 closure status

Current status: $status.

No R/I/T coding, mechanism coding or Rotem consultation occurred. No corpus-wide repair, R4.2D execution, R4.3 work, commit, pull or push was performed.
"@
Set-Content -LiteralPath $reportPath -Value $report -Encoding UTF8

# 7. Append corrective provenance and true-rerun entries without deleting historical log records.
$removeIds=@('R4_2CR_PROV_001','R4_2CR_TERRA_001','R4_2CR_COMPARE_001')
$exec=@(Import-Csv -LiteralPath $execLogPath|?{$removeIds -notcontains $_.RUN_ID})
$exec+=@(
 [pscustomobject]@{RUN_ID='R4_2CR_PROV_001';DATE='2026-09-26';ROUND='R4';PHASE='R4.2C-R';CASE_ID='ALL';TASK='MODEL_PROVENANCE_CORRECTION';TASK_TYPE='PROVENANCE_CORRECTION';MODEL='Researcher-authoritative correction';REASONING_LEVEL='HIGH';INPUT_SOURCE='Researcher statement; preserved R4.2C artifacts';PROMPT_VERSION='R4_2CR_v1';OUTPUT_FILE='R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2C_MODEL_PROVENANCE_CORRECTION.md';TASK_COMPLEXITY='LOW';ESCALATED='NO';ESCALATION_REASON='';HUMAN_REVIEW_REQUIRED='NO';HUMAN_REVIEW_STATUS='RESEARCHER_CONFIRMED';FINAL_STATUS='MODEL_SELECTION_MISMATCH_CORRECTED';NOTES='ERROR=WRONG_MODEL_SELECTED_BY_RESEARCHER; INTENDED_MODEL=GPT-5.6 Terra High; USER_CONFIRMED_SELECTED_MODEL=GPT-5.6 Luna High; RUNTIME_MODEL_VISIBILITY=NOT_EXPOSED; CORRECTIVE_ACTION=TRUE_TERRA_RERUN.';PHASE_RECLASSIFIED_FROM='R4.2C';PHASE_RECLASSIFIED_TO='R4.2C-R';PHASE_RECLASSIFICATION_REASON='Historical Terra label corrected to Luna calibrated self-review.'}
 [pscustomobject]@{RUN_ID='R4_2CR_TERRA_001';DATE='2026-09-26';ROUND='R4';PHASE='R4.2C-R';CASE_ID='ALL';TASK='TRUE_TERRA_INDEPENDENT_CALIBRATED_QA';TASK_TYPE='BLIND_CALIBRATED_STRUCTURAL_QA';MODEL='GPT-5.6 Terra High requested and user-selected; runtime variant not exposed';REASONING_LEVEL='HIGH';INPUT_SOURCE='Frozen legal source; Luna extraction; frozen 3-case human seed; 87-record blind set';PROMPT_VERSION='R4_2CR_v1';OUTPUT_FILE='R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2C_TERRA_INDEPENDENT_CALIBRATED_REVIEW_V2.csv';TASK_COMPLEXITY='HIGH';ESCALATED='YES';ESCALATION_REASON='PLANNED_CAPABILITY_ESCALATION_FOR_INDEPENDENT_CALIBRATED_QA';HUMAN_REVIEW_REQUIRED='YES';HUMAN_REVIEW_STATUS='TARGETED_DIAGNOSTIC_RECOMMENDED';FINAL_STATUS='FROZEN_BEFORE_MODEL_COMPARISON';NOTES='REQUESTED_MODEL=GPT-5.6 Terra High; USER_SELECTED_MODEL=GPT-5.6 Terra High; RUNTIME_OBSERVED_MODEL=MODEL_VARIANT_NOT_EXPOSED; RIT_CODING=NOT_STARTED; MECHANISM_CODING=NOT_STARTED; ROTEM_CODING_CONSULTED=NO.';PHASE_RECLASSIFIED_FROM='';PHASE_RECLASSIFIED_TO='';PHASE_RECLASSIFICATION_REASON=''}
 [pscustomobject]@{RUN_ID='R4_2CR_COMPARE_001';DATE='2026-09-26';ROUND='R4';PHASE='R4.2C-R';CASE_ID='ALL';TASK='LUNA_SELFREVIEW_TERRA_PAIRED_COMPARISON';TASK_TYPE='MODEL_SENSITIVITY_AND_PATTERN_REASSESSMENT';MODEL='GPT-5.6 Terra High user-selected; runtime variant not exposed';REASONING_LEVEL='HIGH';INPUT_SOURCE='Frozen V2 Terra review; preserved Luna self-review; original Luna metadata';PROMPT_VERSION='R4_2CR_v1';OUTPUT_FILE='R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2C_LUNA_SELFREVIEW_TERRA_COMPARISON.csv';TASK_COMPLEXITY='HIGH';ESCALATED='NO';ESCALATION_REASON='';HUMAN_REVIEW_REQUIRED='YES';HUMAN_REVIEW_STATUS='RESEARCHER_DIAGNOSTIC_RECOMMENDED';FINAL_STATUS=$status;NOTES='Paired models are not human validation; prior defect claims reassessed as cross-model evidence only.';PHASE_RECLASSIFIED_FROM='';PHASE_RECLASSIFIED_TO='';PHASE_RECLASSIFICATION_REASON=''}
)
$exec|Export-Csv -NoTypeInformation -Encoding UTF8 -LiteralPath $execLogPath
$escRemove=@('R4_2CR_ESC_CORR_001','R4_2CR_ESC_TERRA_001')
$esc=@(Import-Csv -LiteralPath $escLogPath|?{$escRemove -notcontains $_.RUN_ID})
$esc+=@(
 [pscustomobject]@{RUN_ID='R4_2CR_ESC_CORR_001';CASE_ID='ALL';ARTICLE='';TASK='Correct prior planned Luna-to-Terra escalation';LUNA_OUTPUT='Prior R4.2C 87-record review';AMBIGUITY='Historical model label mismatch';ESCALATION_REASON='PLANNED_ESCALATION_NOT_EXECUTED';TERRA_OUTPUT='None in previous run';OUTPUT_DIFFERENCE='Prior output reclassified as Luna calibrated self-review';HUMAN_ASSESSMENT='Researcher confirmed Luna selection';FINAL_DECISION='PROVENANCE_CORRECTION_RECORDED'}
 [pscustomobject]@{RUN_ID='R4_2CR_ESC_TERRA_001';CASE_ID='ALL';ARTICLE='';TASK='Luna to Terra independent calibrated QA rerun';LUNA_OUTPUT='Original extraction and preserved self-review';AMBIGUITY='Blind V2 excludes previous self-review and Luna metadata';ESCALATION_REASON='PLANNED_CAPABILITY_ESCALATION_FOR_INDEPENDENT_CALIBRATED_QA';TERRA_OUTPUT='R4_2C_TERRA_INDEPENDENT_CALIBRATED_REVIEW_V2.csv';OUTPUT_DIFFERENCE='Paired Luna self-review versus Terra independent evidence';HUMAN_ASSESSMENT='Targeted human diagnostic recommended';FINAL_DECISION=$status}
)
$esc|Export-Csv -NoTypeInformation -Encoding UTF8 -LiteralPath $escLogPath

Write-Output "R4.2C-R complete: terra=$($terra.Count); no_error=$terraNoError; error=$terraError; abstain=$terraAbstain; queue=$($queue.Count); status=$status"
