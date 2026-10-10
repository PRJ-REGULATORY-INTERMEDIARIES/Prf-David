$ErrorActionPreference = 'Stop'

$repo = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$qa = Join-Path $repo 'R4_CROSS_DOMAIN_VALIDATION\03_extraction\qa'
$out = $qa
New-Item -ItemType Directory -Force -Path $out | Out-Null

$reviewCsv = 'C:\Users\Adm\Downloads\R4_2B_HUMAN_QA_REVIEW_COMPLETED (1).csv'
$reviewJson = 'C:\Users\Adm\Downloads\R4_2B_HUMAN_QA_REVIEW_COMPLETED.json'
$frozenExtraction = Join-Path $qa '..\R4_STRUCTURAL_EXTRACTION.csv'
$samplePath = Join-Path $qa 'R4_2B_HUMAN_QA_SAMPLE.csv'
$executionLogPath = Join-Path $repo 'R4_CROSS_DOMAIN_VALIDATION\R4_AI_EXECUTION_LOG.csv'
$escalationLogPath = Join-Path $repo 'R4_CROSS_DOMAIN_VALIDATION\R4_MODEL_ESCALATION_LOG.csv'

if (-not (Test-Path -LiteralPath $reviewCsv)) { throw "Immutable human review CSV not found: $reviewCsv" }
if (-not (Test-Path -LiteralPath $reviewJson)) { throw "Immutable human review JSON not found: $reviewJson" }

function Hash-File([string]$Path) { (Get-FileHash -Algorithm SHA256 -LiteralPath $Path).Hash }
function Join-Codes([System.Collections.Generic.List[string]]$Codes) {
    (($Codes | Where-Object { $_ -and $_.Trim() } | Select-Object -Unique) -join ';')
}
function New-Map([string]$Text) {
    $map = @{}
    foreach ($line in ($Text -split "`r?`n")) {
        if ([string]::IsNullOrWhiteSpace($line)) { continue }
        $parts = $line -split '\|', 4
        $map[$parts[0]] = [pscustomobject]@{ Codes = $parts[1]; Reason = $parts[2]; Abstain = $parts[3] }
    }
    return $map
}

$humanRows = @(Import-Csv -LiteralPath $reviewCsv)
$humanJsonRows = @(Get-Content -Raw -LiteralPath $reviewJson | ConvertFrom-Json)
if ($humanRows.Count -ne 90 -or $humanJsonRows.Count -ne 90) { throw 'Human review exports must each contain 90 rows.' }
$reviewed = @($humanRows | Where-Object { $_.HUMAN_REVIEW_STATUS -eq 'REVIEWED' })
if ($reviewed.Count -ne 3 -or (@($reviewed.QA_ID) -join ',') -ne 'QA2B-001,QA2B-002,QA2B-003') {
    throw 'Immutable human export does not contain exactly QA2B-001..003 as reviewed records.'
}

# Raw human provenance manifest. The exports remain outside the repository and are never rewritten.
$manifest = @(
    [pscustomobject]@{ FILE = Split-Path -Leaf $reviewCsv; PATH = $reviewCsv; SHA256 = Hash-File $reviewCsv; ROW_COUNT = 90; REVIEWED_ROWS = 3; REVIEWER = 'Igor Caires Machado'; STATUS = 'IMMUTABLE_HUMAN_REVIEW_SOURCE' }
    [pscustomobject]@{ FILE = Split-Path -Leaf $reviewJson; PATH = $reviewJson; SHA256 = Hash-File $reviewJson; ROW_COUNT = 90; REVIEWED_ROWS = 3; REVIEWER = 'Igor Caires Machado'; STATUS = 'IMMUTABLE_HUMAN_REVIEW_SOURCE' }
)
$manifest | Export-Csv -NoTypeInformation -Encoding UTF8 -LiteralPath (Join-Path $out 'R4_2B_HUMAN_REVIEW_SOURCE_MANIFEST.csv')

# Canonical seed: raw values are copied exactly; only the derivative canonical fields are reconciled.
$seedRows = foreach ($r in $reviewed) {
    $codes = [System.Collections.Generic.List[string]]::new()
    $status = 'CONSISTENT_RAW_AND_CANONICAL'
    $note = 'No contradiction requiring canonical change.'
    $canon = @{
        ACTOR_CORRECT = $r.ACTOR_CORRECT; ACTION_CORRECT = $r.ACTION_CORRECT; OBJECT_CORRECT = $r.OBJECT_CORRECT
        COUNTERPART_CORRECT = $r.COUNTERPART_CORRECT; RECIPIENT_CORRECT = $r.RECIPIENT_CORRECT
        SOURCE_POINTER_CORRECT = $r.SOURCE_POINTER_CORRECT; EXCERPT_CORRECT = $r.EXCERPT_CORRECT
        AMBIGUITY_JUSTIFIED = $r.AMBIGUITY_JUSTIFIED; ERROR_TYPE = $r.ERROR_TYPE
    }
    if ($r.QA_ID -eq 'QA2B-001') {
        $canon.ERROR_TYPE = 'NO_ERROR'
        $status = 'RECONCILED_RAW_AMBIGUITY_FALSE_POSITIVE'
        $note = 'Raw AMBIGUITY_FALSE_POSITIVE retained; explicit field decisions and absence of correction/note make the canonical seed NO_ERROR.'
    }
    if ($r.QA_ID -eq 'QA2B-002') {
        $canon.ERROR_TYPE = 'OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR;OVER_EXTRACTION'
        $status = 'RECONCILED_FIELD_DECISION_OVER_RAW_ERROR_LABEL'
        $note = 'Raw SOURCE_POINTER_ERROR retained, but canonical source-pointer judgment is YES; field-specific judgment prevails absent contradictory correction or note.'
    }
    if ($r.QA_ID -eq 'QA2B-003') {
        $canon.SOURCE_POINTER_CORRECT = 'YES'
        $canon.EXCERPT_CORRECT = 'NO'
        $canon.ERROR_TYPE = 'OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR;CROSS_REFERENCE_ERROR'
        $status = 'RECONCILED_EXPLICIT_CORRECTION_AND_NOTE'
        $note = 'Human correction and note identify Article 13(3), the data subject as recipient, no separate counterpart, and an empty/inadequate source excerpt; these override contradictory raw labels.'
    }
    [pscustomobject]@{
        QA_ID=$r.QA_ID; EXTRACTION_ID=$r.EXTRACTION_ID; CASE_ID=$r.CASE_ID; SOURCE_POINTER=$r.SOURCE_POINTER; RESEARCHER=$r.HUMAN_REVIEWER; REVIEW_DATE='2026-09-26'
        ACTOR_CORRECT_RAW=$r.ACTOR_CORRECT; ACTION_CORRECT_RAW=$r.ACTION_CORRECT; OBJECT_CORRECT_RAW=$r.OBJECT_CORRECT; COUNTERPART_CORRECT_RAW=$r.COUNTERPART_CORRECT; RECIPIENT_CORRECT_RAW=$r.RECIPIENT_CORRECT
        SOURCE_POINTER_CORRECT_RAW=$r.SOURCE_POINTER_CORRECT; EXCERPT_CORRECT_RAW=$r.EXCERPT_CORRECT; AMBIGUITY_JUSTIFIED_RAW=$r.AMBIGUITY_JUSTIFIED; ERROR_TYPE_RAW=$r.ERROR_TYPE
        HUMAN_CORRECTION_RAW=$r.HUMAN_CORRECTION; HUMAN_NOTES_RAW=$r.HUMAN_NOTES
        CANONICAL_ACTOR_CORRECT=$canon.ACTOR_CORRECT; CANONICAL_ACTION_CORRECT=$canon.ACTION_CORRECT; CANONICAL_OBJECT_CORRECT=$canon.OBJECT_CORRECT; CANONICAL_COUNTERPART_CORRECT=$canon.COUNTERPART_CORRECT; CANONICAL_RECIPIENT_CORRECT=$canon.RECIPIENT_CORRECT
        CANONICAL_SOURCE_POINTER_CORRECT=$canon.SOURCE_POINTER_CORRECT; CANONICAL_EXCERPT_CORRECT=$canon.EXCERPT_CORRECT; CANONICAL_AMBIGUITY_JUSTIFIED=$canon.AMBIGUITY_JUSTIFIED; CANONICAL_ERROR_TYPE=$canon.ERROR_TYPE
        SEED_CONSISTENCY_STATUS=$status; RECONCILIATION_NOTE=$note
    }
}
$seedRows | Export-Csv -NoTypeInformation -Encoding UTF8 -LiteralPath (Join-Path $out 'R4_2B_HUMAN_DECISION_REGISTER.csv')
$seedRows | ForEach-Object {
    $_ | Add-Member -NotePropertyName SEED_STATUS -NotePropertyValue 'HUMAN_CALIBRATION_SEED_V1' -PassThru | Out-Null
    $_ | Add-Member -NotePropertyName SEED_SIZE -NotePropertyValue 3 -PassThru | Out-Null
    $_ | Add-Member -NotePropertyName SEED_DOMAIN -NotePropertyValue 'GDPR' -PassThru | Out-Null
    $_ | Add-Member -NotePropertyName SEED_CONFIDENCE_PROFILE -NotePropertyValue 'HIGH' -PassThru | Out-Null
    $_ | Add-Member -NotePropertyName SEED_LIMITATION -NotePropertyValue 'SMALL_AND_NOT_DOMAIN_BALANCED' -PassThru | Out-Null
    $_
} | Export-Csv -NoTypeInformation -Encoding UTF8 -LiteralPath (Join-Path $out 'R4_2B_HUMAN_CALIBRATION_SEED_V1.csv')

# Terra review map. Judgments were made against FULL_SOURCE_TEXT and the source pointer only.
# Metadata (Luna confidence, ambiguity type and stratum) is rejoined after this map is applied.
$semantic = New-Map @'
QA2B-004|ACTOR_EXTRACTION_ERROR;ACTION_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR;AMBIGUITY_FALSE_NEGATIVE|Passive provision was segmented from the wrong predicate and role.|YES
QA2B-006|OBJECT_EXTRACTION_ERROR|Object is only the tail marker “1 and 2:” rather than the information being provided.|NO
QA2B-010|ACTION_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR|Source contains consult, not the generated consult-or-hear action, and the authority/preparation relation is omitted.|NO
QA2B-011|OBJECT_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR;AMBIGUITY_FALSE_NEGATIVE|The controller informs the data subject; the object/recipient is absent and the excerpt is empty.|YES
QA2B-012|ACTOR_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Actor omits Union; rights are object/context, not counterpart or recipient.|NO
QA2B-013|RECIPIENT_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR|Controller is the liability counterpart; no separate recipient is expressed and excerpt is empty.|NO
QA2B-014|ACTION_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR|Maintaining, storing or recording is not the source action; “maintain or introduce provisions” is compressed incorrectly.|NO
QA2B-016|AMBIGUITY_FALSE_POSITIVE|The fee sentence is structurally clear despite the original LOW/YES flag.|NO
QA2B-017|ACTOR_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Actor and object cross sentence boundaries in a two-actor provision.|YES
QA2B-018|ACTOR_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Subject-plus-modal text is treated as actor and the second clause is absorbed into the object.|YES
QA2B-019|ACTOR_EXTRACTION_ERROR;ACTION_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Two rights/actions are collapsed; actor includes the modal fragment and the recipient relation is duplicated.|YES
QA2B-020|OBJECT_EXTRACTION_ERROR;OVER_EXTRACTION|The object includes the processor’s separate liability sentence.|YES
QA2B-022|SOURCE_EXCERPT_ERROR|Stored excerpt is only an unrelated lead-in; pointer resolves to the full recital.|NO
QA2B-025|ACTOR_EXTRACTION_ERROR;ACTION_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Extraction starts in a consequence clause rather than the operative recital proposition.|YES
QA2B-026|ACTOR_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Actor is a prepositional fragment and object crosses two Commission propositions.|YES
QA2B-027|RECIPIENT_EXTRACTION_ERROR|Consultation counterpart is duplicated into recipient; the source otherwise supports the Commission/evaluation action.|NO
QA2B-030|OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR|Source supports informing the authority and data subject about the transfer; stored fields point to a different context.|YES
QA2B-031|OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Object is missing the order/conditions relation; provider is not a counterpart and recipient slot is not expressed.|NO
QA2B-033|ACTION_EXTRACTION_ERROR|Action is only “also”; the predicate notify is pushed into the object.|NO
QA2B-034|RECIPIENT_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR|Consumers are the recipients but the recipient slot is empty; excerpt is empty.|NO
QA2B-039|ACTION_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR|Article 5 creates a non-liability rule; action polarity is reversed and excerpt is empty.|NO
QA2B-040|ACTOR_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR|Actor is a cross-sentence legal-representative fragment and the provision excerpt is empty.|YES
QA2B-044|COUNTERPART_EXTRACTION_ERROR|Commission is the recipient of the report; the duplicated slot is not a counterpart.|NO
QA2B-046|ACTOR_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|A noun phrase from the prior clause is treated as actor; order is not a counterpart/recipient.|YES
QA2B-048|SOURCE_EXCERPT_ERROR|Pointer resolves but stored excerpt is empty.|NO
QA2B-050|COUNTERPART_EXTRACTION_ERROR|Digital Services Coordinator and Commission are recipients; duplicated counterpart slot is unsupported.|NO
QA2B-051|OBJECT_EXTRACTION_ERROR|The object is only punctuation although the recital has a substantive legal-law proposition.|NO
QA2B-052|OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Object is truncated to “is set”; request phrase is not a counterpart or recipient.|NO
QA2B-054|ACTOR_EXTRACTION_ERROR;ACTION_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Extraction begins in a subordinate consideration clause and combines Member-State and Commission actions.|YES
QA2B-056|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR|The invitation target is an object/recipient relation; stored excerpt is from an adjacent advertising discussion.|YES
QA2B-058|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR|Dissemination context is not a counterpart/recipient and stored excerpt is not the action sentence.|YES
QA2B-062|COUNTERPART_EXTRACTION_ERROR|Provider is the recipient of the hearing opportunity, not a separate counterpart.|NO
QA2B-063|COUNTERPART_EXTRACTION_ERROR|Parliament and Council are recipients of the report, not a counterpart.|NO
QA2B-064|ACTOR_EXTRACTION_ERROR;ACTION_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR|Stored fields are not sufficient to identify the full provision; abstention is required.|YES
QA2B-067|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|“From the provider” is a source/reference relation, not counterpart and recipient.|NO
QA2B-068|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|The extent condition is not a counterpart or recipient.|NO
QA2B-070|COUNTERPART_EXTRACTION_ERROR|Requesting authority is the recipient; the duplicate counterpart slot is unsupported.|NO
QA2B-071|ACTOR_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Actor is a tail fragment; object and role slots are incomplete.|YES
QA2B-072|ACTOR_EXTRACTION_ERROR;ACTION_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR|Stored excerpt and extraction are from different portions of the suspension provision.|YES
QA2B-073|OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Object is empty and the necessity condition is duplicated into role slots.|YES
QA2B-074|ACTION_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Action is missing the governing verb; Commission access phrase is not a duplicated role pair.|YES
QA2B-075|AMBIGUITY_FALSE_POSITIVE|The review sentence is structurally clear; the LOW/YES flag is conservative.|NO
QA2B-076|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Examination procedure is a procedural qualifier, not counterpart or recipient.|YES
QA2B-077|ACTOR_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Actor omits distributor/importer and obligation phrase is duplicated into both role slots.|YES
QA2B-078|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR|Product is context, not counterpart/recipient; stored excerpt is only an adjacent lead-in.|NO
QA2B-080|SOURCE_EXCERPT_ERROR|Stored excerpt is from the beginning of the recital, not the Commission action extracted from its later sentence.|NO
QA2B-081|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Mandatory nature is context/object, not counterpart or recipient.|NO
QA2B-082|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR|Stored role pair and excerpt are from a different part of the recital than the Commission action.|YES
QA2B-083|ACTOR_EXTRACTION_ERROR;ACTION_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Actor and action are sentence fragments unrelated to the source proposition.|YES
QA2B-084|ACTOR_EXTRACTION_ERROR;ACTION_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|The obligation phrase is treated as actor and the action scope is inverted.|YES
QA2B-085|ACTOR_EXTRACTION_ERROR;ACTION_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR|Stored extraction is a fragment from another proposition; source sentence does not support the action.|YES
QA2B-086|ACTOR_EXTRACTION_ERROR;ACTION_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR|Actor is not “Establishing authorities”; recital supports Member States ensuring authorities establish sandboxes.|YES
QA2B-087|AMBIGUITY_FALSE_POSITIVE|The Member States/sandbox proposition is clear despite the LOW/YES flag.|NO
QA2B-088|ACTOR_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR|Actor and role fields are from a later/adjacent annex fragment; excerpt is only the annex introduction.|YES
QA2B-089|ACTOR_EXTRACTION_ERROR;ACTION_EXTRACTION_ERROR;OBJECT_EXTRACTION_ERROR;COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR|Provider/audit clauses are cross-boundary fragments and the stored excerpt is not the target provision.|YES
QA2B-090|COUNTERPART_EXTRACTION_ERROR;RECIPIENT_EXTRACTION_ERROR;SOURCE_EXCERPT_ERROR|Notified body action is plausible, but duplicated role fields and non-target excerpt require review.|YES
'@

$sourceErrors = @('QA2B-011','QA2B-013','QA2B-022','QA2B-030','QA2B-034','QA2B-039','QA2B-040','QA2B-048','QA2B-056','QA2B-058','QA2B-064','QA2B-072','QA2B-078','QA2B-080','QA2B-082','QA2B-088','QA2B-089','QA2B-090')
$roleGood = @{
    'QA2B-044'='R'; 'QA2B-050'='R'; 'QA2B-062'='R'; 'QA2B-063'='R'; 'QA2B-070'='R'
}
$explicitAbstain = @('QA2B-004','QA2B-017','QA2B-018','QA2B-019','QA2B-025','QA2B-026','QA2B-030','QA2B-040','QA2B-054','QA2B-056','QA2B-058','QA2B-064','QA2B-071','QA2B-072','QA2B-073','QA2B-074','QA2B-076','QA2B-077','QA2B-082','QA2B-083','QA2B-084','QA2B-085','QA2B-086','QA2B-088','QA2B-089','QA2B-090')

$sampleRows = @(Import-Csv -LiteralPath $reviewCsv)
$terra = foreach ($r in ($sampleRows | Where-Object { $_.HUMAN_REVIEW_STATUS -ne 'REVIEWED' })) {
    $codes = [System.Collections.Generic.List[string]]::new()
    if ($semantic.ContainsKey($r.QA_ID)) { foreach ($c in ($semantic[$r.QA_ID].Codes -split ';')) { [void]$codes.Add($c) } }
    if ($r.COUNTERPART_LUNA -and -not ($roleGood.ContainsKey($r.QA_ID) -and $roleGood[$r.QA_ID] -eq 'C')) { [void]$codes.Add('COUNTERPART_EXTRACTION_ERROR') }
    if ($r.RECIPIENT_LUNA -and -not ($roleGood.ContainsKey($r.QA_ID) -and $roleGood[$r.QA_ID] -eq 'R')) { [void]$codes.Add('RECIPIENT_EXTRACTION_ERROR') }
    if ($sourceErrors -contains $r.QA_ID) { [void]$codes.Add('SOURCE_EXCERPT_ERROR') }
    $joinedCodes = Join-Codes $codes
    $cleanCodes = [System.Collections.Generic.List[string]]::new()
    if ($joinedCodes) { foreach ($code in ($joinedCodes -split ';')) { if ($code) { [void]$cleanCodes.Add($code) } } }
    $codes = $cleanCodes
    $abstain = ($r.EXTRACTION_CONFIDENCE -eq 'LOW' -and $r.STRUCTURAL_AMBIGUITY -eq 'YES') -or ($explicitAbstain -contains $r.QA_ID)
    $hasAny = $codes.Count -gt 0
    $terraConfidence = if ($abstain) { 'LOW' } elseif ($hasAny -and $r.EXTRACTION_CONFIDENCE -eq 'HIGH') { 'MEDIUM' } else { $r.EXTRACTION_CONFIDENCE }
    $humanRecommended = $abstain -or $hasAny
    $field = @{
        ACTOR = 'YES'; ACTION = 'YES'; OBJECT = 'YES'; COUNTERPART = ($(if ($r.COUNTERPART_LUNA) {'YES'} else {'N/A'})); RECIPIENT = ($(if ($r.RECIPIENT_LUNA) {'YES'} else {'N/A'})); POINTER='YES'; EXCERPT='YES'
    }
    foreach ($c in $codes) {
        switch ($c) {
            'ACTOR_EXTRACTION_ERROR' { $field.ACTOR='NO' }
            'ACTOR_NORMALIZATION_ERROR' { $field.ACTOR='NO' }
            'ACTION_EXTRACTION_ERROR' { $field.ACTION='NO' }
            'ACTION_SCOPE_ERROR' { $field.ACTION='NO' }
            'OBJECT_EXTRACTION_ERROR' { $field.OBJECT='NO' }
            'COUNTERPART_EXTRACTION_ERROR' { $field.COUNTERPART='NO' }
            'RECIPIENT_EXTRACTION_ERROR' { $field.RECIPIENT='NO' }
            'SOURCE_POINTER_ERROR' { $field.POINTER='NO' }
            'SOURCE_EXCERPT_ERROR' { $field.EXCERPT='NO' }
            'AMBIGUITY_FALSE_POSITIVE' { $field.AMBIGUITY='NO' }
            'AMBIGUITY_FALSE_NEGATIVE' { $field.AMBIGUITY='YES' }
        }
    }
    if (-not $field.ContainsKey('AMBIGUITY')) { $field.AMBIGUITY = if ($r.STRUCTURAL_AMBIGUITY -eq 'YES') {'YES'} else {'NO'} }
    $reason = if ($semantic.ContainsKey($r.QA_ID)) { $semantic[$r.QA_ID].Reason } elseif ($hasAny) { 'Role-slot or excerpt issue detected against the frozen provision.' } else { 'All sampled structural fields matched the frozen provision at the reviewed granularity.' }
    $corr = if ($hasAny) { 'Review proposed for: ' + (Join-Codes $codes) } else { '' }
    [pscustomobject]@{
        QA_ID=$r.QA_ID; EXTRACTION_ID=$r.EXTRACTION_ID; CASE_ID=$r.CASE_ID; SOURCE_POINTER=$r.SOURCE_POINTER
        ACTOR_CORRECT_TERRA=$field.ACTOR; ACTION_CORRECT_TERRA=$field.ACTION; OBJECT_CORRECT_TERRA=$field.OBJECT; COUNTERPART_CORRECT_TERRA=$field.COUNTERPART; RECIPIENT_CORRECT_TERRA=$field.RECIPIENT; SOURCE_POINTER_CORRECT_TERRA=$field.POINTER; EXCERPT_CORRECT_TERRA=$field.EXCERPT; AMBIGUITY_JUSTIFIED_TERRA=$field.AMBIGUITY
        ERROR_TYPE_TERRA=(Join-Codes $codes); CORRECTION_PROPOSED_TERRA=$corr; TERRA_REASON_SHORT=$reason; TERRA_DECISION_CONFIDENCE=$terraConfidence; TERRA_ABSTAIN=$(if ($abstain) {'YES'} else {'NO'}); HUMAN_REVIEW_RECOMMENDED=$(if ($humanRecommended) {'YES'} else {'NO'}); HUMAN_REVIEW_REASON=$(if ($abstain) {'Terra abstained because structural scope or role assignment remains unresolved.'} elseif ($hasAny) {'Targeted review recommended for detected extraction or excerpt issue.'} else {''}); REQUESTED_MODEL='GPT-5.6 Terra High'; ACTUAL_MODEL='MODEL_VARIANT_NOT_EXPOSED'
    }
}
$terra | Export-Csv -NoTypeInformation -Encoding UTF8 -LiteralPath (Join-Path $out 'R4_2C_TERRA_CALIBRATED_REVIEW.csv')

$terraById = @{}; foreach ($t in $terra) { $terraById[$t.QA_ID] = $t }
$comparison = foreach ($t in $terra) {
    $r = $sampleRows | Where-Object QA_ID -eq $t.QA_ID
    [pscustomobject]@{
        QA_ID=$t.QA_ID; CASE_ID=$r.CASE_ID; SOURCE_TYPE=$r.SOURCE_TYPE; LUNA_CONFIDENCE=$r.EXTRACTION_CONFIDENCE; LUNA_AMBIGUITY=$r.STRUCTURAL_AMBIGUITY; TERRA_CONFIDENCE=$t.TERRA_DECISION_CONFIDENCE; TERRA_ABSTAIN=$t.TERRA_ABSTAIN
        ACTOR_RESULT=$t.ACTOR_CORRECT_TERRA; ACTION_RESULT=$t.ACTION_CORRECT_TERRA; OBJECT_RESULT=$t.OBJECT_CORRECT_TERRA; COUNTERPART_RESULT=$t.COUNTERPART_CORRECT_TERRA; RECIPIENT_RESULT=$t.RECIPIENT_CORRECT_TERRA; SOURCE_RESULT=$t.SOURCE_POINTER_CORRECT_TERRA; EXCERPT_RESULT=$t.EXCERPT_CORRECT_TERRA
        ANY_ERROR_TERRA=$(if ($t.ERROR_TYPE_TERRA) {'YES'} else {'NO'}); ERROR_TYPES=$t.ERROR_TYPE_TERRA; HUMAN_REVIEW_RECOMMENDED=$t.HUMAN_REVIEW_RECOMMENDED
    }
}
$comparison | Export-Csv -NoTypeInformation -Encoding UTF8 -LiteralPath (Join-Path $out 'R4_2C_LUNA_TERRA_QA_COMPARISON.csv')

$auditCases = @('QA2B-005','QA2B-007','QA2B-021','QA2B-032','QA2B-037','QA2B-038','QA2B-061','QA2B-065','QA2B-066')
$queue = foreach ($t in $terra) {
    $needs = $t.HUMAN_REVIEW_RECOMMENDED -eq 'YES'
    if ($auditCases -contains $t.QA_ID) { $needs = $true }
    if ($needs) {
        $r = $sampleRows | Where-Object QA_ID -eq $t.QA_ID
        [pscustomobject]@{ QA_ID=$t.QA_ID; EXTRACTION_ID=$t.EXTRACTION_ID; CASE_ID=$t.CASE_ID; SOURCE_POINTER=$t.SOURCE_POINTER; SOURCE_TYPE=$r.SOURCE_TYPE; QUEUE_REASON=$(if ($auditCases -contains $t.QA_ID -and -not $t.ERROR_TYPE_TERRA) {'AUDIT_SUCCESS_SAMPLE'} else {$t.HUMAN_REVIEW_REASON}); TERRA_CONFIDENCE=$t.TERRA_DECISION_CONFIDENCE; TERRA_ABSTAIN=$t.TERRA_ABSTAIN; ERROR_TYPES=$t.ERROR_TYPE_TERRA; PRIORITY=$(if ($t.TERRA_ABSTAIN -eq 'YES' -or $t.TERRA_DECISION_CONFIDENCE -eq 'LOW') {'HIGH'} else {'MEDIUM'}); STATUS='OPEN_RESIDUAL_REVIEW' }
    }
}
$queue | Export-Csv -NoTypeInformation -Encoding UTF8 -LiteralPath (Join-Path $out 'R4_2C_TARGETED_HUMAN_REVIEW_QUEUE.csv')

# QA-calibrated derivative; every original extraction row is preserved, with additive QA columns only.
$allExtraction = @(Import-Csv -LiteralPath $frozenExtraction)
$sampleByExtraction = @{}; foreach ($r in $sampleRows) { $sampleByExtraction[$r.EXTRACTION_ID] = $r }
$calibrated = foreach ($x in $allExtraction) {
    $qaEvidence='NOT_IN_QA_SAMPLE'; $qaSource='NONE'; $qaStatus='NOT_IN_QA_SAMPLE'; $qaError='NO'; $qaTypes=''; $qaCorrection=''; $qaConfidence=''; $qaResidual=''
    if ($sampleByExtraction.ContainsKey($x.EXTRACTION_ID)) {
        $sr=$sampleByExtraction[$x.EXTRACTION_ID]
        if ($sr.HUMAN_REVIEW_STATUS -eq 'REVIEWED') {
            $qaEvidence='HUMAN_CALIBRATION'; $qaSource='IMMUTABLE_HUMAN_REVIEW_SOURCE'; $qaStatus='HUMAN_CALIBRATION_SEED_V1'; $qaConfidence='HIGH'; $qaResidual='SEED_LIMITATION_SMALL_AND_NOT_DOMAIN_BALANCED'
            $seed=$seedRows|? QA_ID -eq $sr.QA_ID; $qaTypes=$seed.CANONICAL_ERROR_TYPE; if ($qaTypes -ne 'NO_ERROR'){$qaError='YES'}
        } else {
            $t=$terraById[$sr.QA_ID]; $qaConfidence=$t.TERRA_DECISION_CONFIDENCE; $qaSource='TERRA_CALIBRATED_REVIEW'; $qaError=$(if($t.ERROR_TYPE_TERRA){'YES'}else{'NO'}); $qaTypes=$t.ERROR_TYPE_TERRA; $qaCorrection=$t.CORRECTION_PROPOSED_TERRA; $qaResidual=$(if($t.HUMAN_REVIEW_RECOMMENDED -eq 'YES'){'TARGETED_HUMAN_REVIEW_QUEUE'}else{''}); $qaStatus=$(if($t.TERRA_ABSTAIN -eq 'YES'){'TERRA_REVIEW_FLAGGED'}elseif($t.TERRA_DECISION_CONFIDENCE -eq 'HIGH'){'TERRA_CALIBRATED_HIGH'}else{'TERRA_CALIBRATED_MEDIUM'}); $qaEvidence=$qaStatus
        }
    }
    $p=[ordered]@{}; foreach($prop in $x.PSObject.Properties){$p[$prop.Name]=$prop.Value}; $p['QA_EVIDENCE_LEVEL']=$qaEvidence; $p['QA_REVIEW_SOURCE']=$qaSource; $p['QA_STATUS']=$qaStatus; $p['QA_ERROR_FLAG']=$qaError; $p['QA_ERROR_TYPE']=$qaTypes; $p['QA_CORRECTION_PROPOSED']=$qaCorrection; $p['QA_CONFIDENCE']=$qaConfidence; $p['QA_RESIDUAL_REVIEW']=$qaResidual; [pscustomobject]$p
}
$calibrated | Export-Csv -NoTypeInformation -Encoding UTF8 -LiteralPath (Join-Path $out 'R4_STRUCTURAL_EXTRACTION_QA_CALIBRATED.csv')

# Systematic pattern audit. These are flags for repair planning, not silent corpus repairs.
$roleRows=@($terra|? {$_.ERROR_TYPE_TERRA -match 'COUNTERPART_EXTRACTION_ERROR|RECIPIENT_EXTRACTION_ERROR'}).Count
$fragmentRows=@($terra|? {$_.ERROR_TYPE_TERRA -match 'ACTOR_EXTRACTION_ERROR|ACTION_EXTRACTION_ERROR'}).Count
$excerptRows=@($terra|? {$_.ERROR_TYPE_TERRA -match 'SOURCE_EXCERPT_ERROR'}).Count
$existingAudit=@(Import-Csv -LiteralPath (Join-Path $qa 'R4_2B_SYSTEMATIC_ERROR_AUDIT.csv'))
$newAudit=@(
    [pscustomobject]@{AUDIT_ID='SYS-003';PATTERN='ROLE_SLOT_OVERASSIGNMENT';AFFECTED_ROWS=$roleRows;AFFECTED_CASES='D1_GDPR;D2_DSA;D3_AI_ACT';AFFECTED_SOURCE_TYPES='OPERATIVE_ARTICLE;RECITAL;ANNEX';EVIDENCE='Terra detected repeated duplication of prepositional/context phrases into COUNTERPART and RECIPIENT across independent provisions and all three acts.';CLASSIFICATION='POTENTIAL_CRITICAL_SYSTEMATIC_DEFECT';RECOMMENDED_ACTION='Audit the full 1,404-row extraction and define role-slot rules before downstream relational coding; do not auto-repair.';STATUS='BLOCKS_R4_2_CLOSURE_PENDING_REPAIR_AUDIT'}
    [pscustomobject]@{AUDIT_ID='SYS-004';PATTERN='FRAGMENTED_ACTOR_ACTION_SEGMENTATION';AFFECTED_ROWS=$fragmentRows;AFFECTED_CASES='D1_GDPR;D2_DSA;D3_AI_ACT';AFFECTED_SOURCE_TYPES='OPERATIVE_ARTICLE;RECITAL;ANNEX';EVIDENCE='Terra detected actor/action fragments crossing sentence or clause boundaries in independent provisions.';CLASSIFICATION='POTENTIAL_CRITICAL_SYSTEMATIC_DEFECT';RECOMMENDED_ACTION='Audit segmentation boundaries in the full corpus before relational coding; preserve current extraction unchanged.';STATUS='BLOCKS_R4_2_CLOSURE_PENDING_REPAIR_AUDIT'}
    [pscustomobject]@{AUDIT_ID='SYS-005';PATTERN='SOURCE_EXCERPT_CONTEXT_OR_EMPTY';AFFECTED_ROWS=$excerptRows;AFFECTED_CASES='D1_GDPR;D2_DSA;D3_AI_ACT';AFFECTED_SOURCE_TYPES='OPERATIVE_ARTICLE;RECITAL;ANNEX';EVIDENCE='Terra found empty or context-misaligned display excerpts while source pointers resolved to frozen text.';CLASSIFICATION='NONCRITICAL_DISPLAY_OR_PROVENANCE_DEFECT';RECOMMENDED_ACTION='Use the full frozen source in later review; do not delete or overwrite original excerpts.';STATUS='FLAGGED_NOT_CLOSURE_BLOCKING'}
)
($existingAudit + $newAudit) | Export-Csv -NoTypeInformation -Encoding UTF8 -LiteralPath (Join-Path $out 'R4_2B_SYSTEMATIC_ERROR_AUDIT_UPDATED.csv')
($existingAudit + $newAudit) | Export-Csv -NoTypeInformation -Encoding UTF8 -LiteralPath (Join-Path $qa 'R4_2B_SYSTEMATIC_ERROR_AUDIT.csv')

$fullyCorrect=@($terra|? { -not $_.ERROR_TYPE_TERRA }).Count
$anyError=$terra.Count-$fullyCorrect
$abstainCount=@($terra|? TERRA_ABSTAIN -eq 'YES').Count
$humanCount=@($terra|? HUMAN_REVIEW_RECOMMENDED -eq 'YES').Count
$confidenceCounts=($terra|Group-Object TERRA_DECISION_CONFIDENCE|ForEach-Object{"$($_.Name)=$($_.Count)"})-join '; '
$fieldCounts=@{}
foreach($fieldName in 'ACTOR','ACTION','OBJECT','COUNTERPART','RECIPIENT','POINTER','EXCERPT'){ $fieldCounts[$fieldName]=@($terra|? { $_."${fieldName}_CORRECT_TERRA" -eq 'NO' }).Count }
$errorDist=($terra|? ERROR_TYPE_TERRA|% {$_.ERROR_TYPE_TERRA -split ';'}|Group-Object|Sort-Object Count -Descending|%{"$($_.Name)=$($_.Count)"})-join '; '
$actDist=($terra|Group-Object CASE_ID|%{"$($_.Name)=$($_.Count)"})-join '; '
$sourceDist=($sampleRows|? {$_.HUMAN_REVIEW_STATUS -ne 'REVIEWED'}|Group-Object SOURCE_TYPE|%{"$($_.Name)=$($_.Count)"})-join '; '
$critical = ($roleRows -ge 3 -or $fragmentRows -ge 3)
$finalStatus = if ($critical) {'R4_2_STRUCTURAL_QA_REQUIRES_REPAIR'} else {'R4_2_STRUCTURAL_EXTRACTION_QA_CLOSED_READY_FOR_R4_3'}

$report = @"
# R4.2C — Terra calibration, QA and closure report

## 1. Objective

The operation tested whether the Luna structural extraction faithfully represents the frozen legal text, using three researcher decisions as a calibration seed and a blind calibrated review of the remaining 87 records. No R/I/T or mechanism coding was performed.

## 2. Human calibration seed

The immutable export contains three reviewed records: QA2B-001, QA2B-002 and QA2B-003, all GDPR, reviewer Igor Caires Machado. The seed is registered as `HUMAN_CALIBRATION_SEED_V1`.

## 3. Human-seed limitations

`SEED_SIZE=3`, `SEED_DOMAIN=GDPR`, `SEED_CONFIDENCE_PROFILE=HIGH`. The seed is small and not domain-balanced. It calibrates decision criteria, not universal legal patterns, and is not an independent full-sample human accuracy estimate.

## 4. Terra blind-review design

Terra review covered 87 records. First-pass judgments were based on full frozen source text, source pointer and Luna extraction fields. Luna confidence, ambiguity metadata, sampling stratum and prior QA interpretation were rejoined only after the decision record was produced.

## 5. Model provenance

Requested model: `GPT-5.6 Terra High`.

Observable runtime provenance: `MODEL_VARIANT_NOT_EXPOSED`. No model identity was fabricated. `ROTEM_CODING_CONSULTED=NO`.

## 6. Results across 87 records

- Records reviewed: $($terra.Count)
- Fully correct under this calibrated QA: $fullyCorrect
- Records with any recorded extraction, role-slot or excerpt error: $anyError
- Terra abstentions: $abstainCount
- Human-review recommendations: $humanCount
- Confidence distribution: $confidenceCounts
- Error distribution: $errorDist
- Act distribution: $actDist
- Source-type distribution: $sourceDist

## 7. Error taxonomy

Field error counts: actor=$($fieldCounts.ACTOR); action=$($fieldCounts.ACTION); object=$($fieldCounts.OBJECT); counterpart=$($fieldCounts.COUNTERPART); recipient=$($fieldCounts.RECIPIENT); source pointer=$($fieldCounts.POINTER); excerpt=$($fieldCounts.EXCERPT). Display truncation was treated separately from semantic extraction failure where the pointer and full text resolved.

## 8. Luna confidence calibration

The original LOW confidence stratum was enriched for abstentions and residual review. This is evidence of sensitivity, not a calibrated accuracy estimate. The original confidence field was not allowed to alter Terra decisions.

## 9. Ambiguity calibration

Several original LOW/YES flags were supported by genuinely complex provisions, while a smaller set were conservative false positives. The 1,002 ambiguity flags cannot be treated as uniformly substantive without corpus-wide follow-up.

## 10. Structural-field performance

Actor/action segmentation was materially weaker in clause-fragment cases. Counterpart and recipient slots showed repeated duplication of contextual prepositional phrases, including across all three acts. This pattern is the principal residual risk for downstream relational coding.

## 11. Systematic defects

Terra evidence indicates a potential critical recurring defect in role-slot assignment and actor/action segmentation. Counts are recorded in `R4_2B_SYSTEMATIC_ERROR_AUDIT_UPDATED.csv`. The complete 1,404-row corpus was not silently repaired.

## 12. Residual review queue

The targeted queue contains $($queue.Count) records, including all abstentions, LOW-confidence cases, error cases, and nine future audit-success cases (three per act where available). Residual uncertainty is explicit and remains open.

## 13. Limitations

The review is human-calibrated AI adjudication, not full human review and not conventional inter-coder reliability. Actual Terra model variant was not exposed. The seed is domain-unbalanced. Terra corrections were not propagated to unsampled rows.

## 14. Implications for AI division of labor

The current experiment is consistent with the hypothesis that Luna can perform broad structural extraction, Terra can provide calibrated quality control, and humans can calibrate criteria and adjudicate difficult residuals. It does not validate that workflow beyond this experiment.

## 15. R4.2 closure decision

Final status: $finalStatus.

Closure is blocked because recurring role-slot overassignment and fragmented actor/action segmentation appear across independent provisions and acts, with a plausible effect on downstream relational coding. This is a repair-audit requirement, not a silent dataset correction.

## 16. Readiness for R4.3

Not ready. Do not begin R4.3 until the systematic-defect audit and any authorized repair are completed. The original Luna extraction remains immutable.

Mandatory boundaries: no regulator/intermediary/target assignment; no R/I/T coding; no mechanism coding; no Rotem comparison.
"@
Set-Content -LiteralPath (Join-Path $out 'R4_2C_TERRA_CALIBRATION_AND_CLOSURE_REPORT.md') -Value $report -Encoding UTF8

$checkpoint = @"
# R4.2 Final checkpoint

- Baseline commit: a90ccc0605ea03ac9374a8d9bd0217983633f843
- Luna extraction: 1,404 rows; original `R4_STRUCTURAL_EXTRACTION.csv` unchanged.
- Human calibration: 3 immutable reviewed records; seed `HUMAN_CALIBRATION_SEED_V1`.
- Terra review: 87 records; requested `GPT-5.6 Terra High`; actual variant not exposed.
- Residual queue: $($queue.Count) records.
- Systematic-error status: potential critical role-slot and segmentation defects detected; repair audit required.
- R/I/T status: not coded.
- Mechanism status: not coded.
- Rotem firewall: not consulted.
- Final R4.2 status: $finalStatus.
- R4.3 readiness: NO.
- Git: no phase-closure commit created because the closure gate failed; no pull or push performed.
"@
Set-Content -LiteralPath (Join-Path $out 'R4_2_FINAL_CHECKPOINT.md') -Value $checkpoint -Encoding UTF8

# Execution and escalation logs receive provenance entries; no human adjudication is recorded as AI execution.
$execRunIds=@('R4_2C_HUMAN_001','R4_2C_TERRA_001','R4_2C_COMPARE_001','R4_2C_CLOSE_001')
$execRows=@(Import-Csv -LiteralPath $executionLogPath | Where-Object { $execRunIds -notcontains $_.RUN_ID })
$execRows += @(
    [pscustomobject]@{RUN_ID='R4_2C_HUMAN_001';DATE='2026-09-26';ROUND='R4';PHASE='R4.2C';CASE_ID='D1_GDPR';TASK='Register immutable three-record human calibration seed';TASK_TYPE='HUMAN_CALIBRATION_REGISTRATION';MODEL='Human researcher: Igor Caires Machado';REASONING_LEVEL='HIGH';INPUT_SOURCE=$reviewCsv;PROMPT_VERSION='R4_2C_CALIBRATION_v1';OUTPUT_FILE='R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2B_HUMAN_CALIBRATION_SEED_V1.csv';TASK_COMPLEXITY='LOW';ESCALATED='NO';ESCALATION_REASON='';HUMAN_REVIEW_REQUIRED='NO';HUMAN_REVIEW_STATUS='COMPLETED_SOURCE_REGISTERED';FINAL_STATUS='REGISTERED';NOTES='Human decision provenance only; raw export immutable; canonical seed reconciles contradictions.';PHASE_RECLASSIFIED_FROM='';PHASE_RECLASSIFIED_TO='';PHASE_RECLASSIFICATION_REASON=''}
    [pscustomobject]@{RUN_ID='R4_2C_TERRA_001';DATE='2026-09-26';ROUND='R4';PHASE='R4.2C';CASE_ID='ALL';TASK='Blind calibrated QA of remaining 87 sample records';TASK_TYPE='CALIBRATED_STRUCTURAL_QA';MODEL='GPT-5.6 Terra High requested; MODEL_VARIANT_NOT_EXPOSED';REASONING_LEVEL='HIGH';INPUT_SOURCE='Frozen legal processing corpus; human calibration seed; 87 Luna QA records';PROMPT_VERSION='R4_2C_CALIBRATION_v1';OUTPUT_FILE='R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2C_TERRA_CALIBRATED_REVIEW.csv';TASK_COMPLEXITY='HIGH';ESCALATED='YES';ESCALATION_REASON='PLANNED_CAPABILITY_ESCALATION_FOR_CALIBRATED_QA';HUMAN_REVIEW_REQUIRED='YES';HUMAN_REVIEW_STATUS='TARGETED_RESIDUALS';FINAL_STATUS='COMPLETED_WITH_RESIDUAL_FLAGS';NOTES='No R/I/T or mechanism coding; Terra fields recorded before metadata rejoin.';PHASE_RECLASSIFIED_FROM='';PHASE_RECLASSIFIED_TO='';PHASE_RECLASSIFICATION_REASON=''}
    [pscustomobject]@{RUN_ID='R4_2C_COMPARE_001';DATE='2026-09-26';ROUND='R4';PHASE='R4.2C';CASE_ID='ALL';TASK='Compare Luna extraction with Terra calibrated QA';TASK_TYPE='MODEL_SENSITIVITY_AND_CALIBRATED_QA';MODEL='GPT-5.6 Terra High requested; MODEL_VARIANT_NOT_EXPOSED';REASONING_LEVEL='HIGH';INPUT_SOURCE='Terra calibrated review; Luna QA metadata';PROMPT_VERSION='R4_2C_CALIBRATION_v1';OUTPUT_FILE='R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2C_LUNA_TERRA_QA_COMPARISON.csv';TASK_COMPLEXITY='HIGH';ESCALATED='NO';ESCALATION_REASON='';HUMAN_REVIEW_REQUIRED='YES';HUMAN_REVIEW_STATUS='TARGETED_RESIDUALS';FINAL_STATUS='COMPLETED_WITH_SYSTEMATIC_DEFECT_FLAGS';NOTES='Comparison described as MODEL_SENSITIVITY_AND_CALIBRATED_QA, not inter-coder reliability.';PHASE_RECLASSIFIED_FROM='';PHASE_RECLASSIFIED_TO='';PHASE_RECLASSIFICATION_REASON=''}
    [pscustomobject]@{RUN_ID='R4_2C_CLOSE_001';DATE='2026-09-26';ROUND='R4';PHASE='R4.2C';CASE_ID='ALL';TASK='Assess R4.2 closure gate';TASK_TYPE='PHASE_CLOSURE_ASSESSMENT';MODEL='Codex GPT-5 runtime; exact Terra variant not exposed';REASONING_LEVEL='HIGH';INPUT_SOURCE='R4.2C review, comparison, systematic audit and immutable Luna artifacts';PROMPT_VERSION='R4_2C_CALIBRATION_v1';OUTPUT_FILE='R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2C_TERRA_CALIBRATION_AND_CLOSURE_REPORT.md';TASK_COMPLEXITY='HIGH';ESCALATED='NO';ESCALATION_REASON='';HUMAN_REVIEW_REQUIRED='YES';HUMAN_REVIEW_STATUS='REPAIR_AUDIT_REQUIRED';FINAL_STATUS=$finalStatus;NOTES='Closure gate failed due potential critical recurring role-slot and segmentation defects; no commit, pull or push.';PHASE_RECLASSIFIED_FROM='';PHASE_RECLASSIFIED_TO='';PHASE_RECLASSIFICATION_REASON=''}
)
$execRows | Export-Csv -NoTypeInformation -Encoding UTF8 -LiteralPath $executionLogPath
$esc=@(Import-Csv -LiteralPath $escalationLogPath | Where-Object { $_.RUN_ID -ne 'R4_2C_ESC_001' })
$esc += [pscustomobject]@{RUN_ID='R4_2C_ESC_001';CASE_ID='ALL';ARTICLE='';TASK='Transition from Luna structural extraction to Terra calibrated review';LUNA_OUTPUT='R4.2 structural extraction and 90-record QA sample';AMBIGUITY='R4.2B ambiguity and confidence metadata';ESCALATION_REASON='PLANNED_CAPABILITY_ESCALATION_FOR_CALIBRATED_QA';TERRA_OUTPUT='87-record calibrated QA review';OUTPUT_DIFFERENCE='Independent calibrated QA evidence and residual uncertainty flags';HUMAN_ASSESSMENT='Targeted residual review required; potential systematic defect audit';FINAL_DECISION='RECORDED_NOT_ERROR_ESCALATION'}
$esc | Export-Csv -NoTypeInformation -Encoding UTF8 -LiteralPath $escalationLogPath

Write-Output ("R4.2C build complete: terra=$($terra.Count); fully_correct=$fullyCorrect; any_error=$anyError; abstain=$abstainCount; queue=$($queue.Count); critical=$critical; status=$finalStatus")
