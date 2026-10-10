param(
    [string]$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
)

$ErrorActionPreference = 'Stop'
$workspace = Join-Path $RepoRoot 'R4_CROSS_DOMAIN_VALIDATION'
$extractionDir = Join-Path $workspace '03_extraction'
$qaDir = Join-Path $extractionDir 'qa'
New-Item -ItemType Directory -Path $qaDir -Force | Out-Null

function Normalize-Text([string]$Text) { if ([string]::IsNullOrWhiteSpace($Text)) { return '' }; return (($Text -replace '\s+', ' ').Trim()) }

$extractionPath = Join-Path $extractionDir 'R4_STRUCTURAL_EXTRACTION.csv'
$extractions = @(Import-Csv $extractionPath)
$actorRegister = @(Import-Csv (Join-Path $extractionDir 'R4_DIGITAL_ACTOR_CANDIDATE_REGISTER.csv'))
$ambiguityLog = @(Import-Csv (Join-Path $extractionDir 'R4_STRUCTURAL_AMBIGUITY_LOG.csv'))

function Get-Complexity($Row) {
    if ($Row.ACTOR_TEXT -match '(?i)\band\b|\bor\b|\bone or more\b') { return 'MULTIPLE_ACTORS' }
    if ($Row.LEGAL_VERB -match '(?i)\band\b|\bor\b' -or $Row.SOURCE_EXCERPT -match '(?i);\s*[^;]+\b(shall|may|must)\b') { return 'MULTIPLE_ACTIONS' }
    if (-not [string]::IsNullOrWhiteSpace($Row.CROSS_REFERENCE)) { return 'CROSS_REFERENCED_PROVISION' }
    if (-not [string]::IsNullOrWhiteSpace($Row.COUNTERPART_TEXT) -or -not [string]::IsNullOrWhiteSpace($Row.RECIPIENT_TEXT)) { return 'COUNTERPART_OR_RECIPIENT' }
    $actor = $actorRegister | Where-Object { $_.CASE_ID -eq $Row.CASE_ID -and $_.ACTOR_NORMALIZED_PROVISIONAL -eq $Row.ACTOR_NORMALIZED_PROVISIONAL } | Select-Object -First 1
    if ($null -ne $actor -and $actor.TEXTUAL_VARIANTS -match '\|') { return 'ACTOR_NORMALIZATION_CASE' }
    return 'SINGLE_ACTOR_SINGLE_ACTION'
}

$sourceFiles = @{
    D1_GDPR = '02_sources/D1_GDPR/normalized/D1_GDPR_32016R0679_processing.txt'
    D2_DSA = '02_sources/D2_DSA/normalized/D2_DSA_32022R2065_processing.txt'
    D3_AI_ACT = '02_sources/D3_AI_ACT/normalized/D3_AI_ACT_32024R1689_processing.txt'
}
$sourceText = @{}
foreach ($case in $sourceFiles.Keys) { $sourceText[$case] = Normalize-Text (Get-Content -LiteralPath (Join-Path $workspace $sourceFiles[$case]) -Raw) }
$structureIndex = @(Import-Csv (Join-Path $workspace 'R4_LEGAL_STRUCTURE_INDEX.csv'))

function Test-Pointer($Row) {
    $parts = $Row.SOURCE_POINTER -split '#', 2
    if ($parts.Count -ne 2) { return 'NO' }
    $fragment = ($parts[1] -split '/')[0]
    $typeName = if ($fragment -like 'article_*') {'ARTICLE'} elseif ($fragment -like 'recital_*') {'RECITAL'} elseif ($fragment -like 'annex_*') {'ANNEX'} else {''}
    $number = $fragment -replace '^(article|recital|annex)_',''
    $found = @($structureIndex | Where-Object { $_.CASE_ID -eq $Row.CASE_ID -and $_.STRUCTURE_TYPE -eq $typeName -and $_.NUMBER -eq $number }).Count
    if ($found -gt 0) { return 'YES' }
    return 'NO'
}

function Get-SampleRows($Rows, [int]$Count) {
    if ($Count -le 0) { return @() }
    $groups = @($Rows | Group-Object { Get-Complexity $_ })
    $selected = [System.Collections.Generic.List[object]]::new()
    $offset = 0
    while ($selected.Count -lt $Count -and $groups.Count -gt 0) {
        $progress = $false
        foreach ($g in $groups) {
            if ($selected.Count -ge $Count) { break }
            $available = @($g.Group | Where-Object { $_.EXTRACTION_ID -notin $selected.EXTRACTION_ID } | Sort-Object EXTRACTION_ID)
            if ($available.Count -gt $offset) { $selected.Add($available[$offset]); $progress=$true }
        }
        if (-not $progress) { break }
        $offset++
    }
    if ($selected.Count -lt $Count) {
        foreach ($row in ($Rows | Sort-Object EXTRACTION_ID)) {
            if ($selected.Count -ge $Count) { break }
            if ($row.EXTRACTION_ID -notin $selected.EXTRACTION_ID) { $selected.Add($row) }
        }
    }
    return @($selected)
}

$quota = @(
    [pscustomobject]@{ Case='D1_GDPR'; Source='OPERATIVE_ARTICLE'; Confidence='HIGH'; Ambiguity='NO'; Count=10 },
    [pscustomobject]@{ Case='D1_GDPR'; Source='OPERATIVE_ARTICLE'; Confidence='MEDIUM'; Ambiguity='NO'; Count=4 },
    [pscustomobject]@{ Case='D1_GDPR'; Source='OPERATIVE_ARTICLE'; Confidence='LOW'; Ambiguity='YES'; Count=6 },
    [pscustomobject]@{ Case='D1_GDPR'; Source='RECITAL'; Confidence='HIGH'; Ambiguity='NO'; Count=3 },
    [pscustomobject]@{ Case='D1_GDPR'; Source='RECITAL'; Confidence='LOW'; Ambiguity='YES'; Count=7 },
    [pscustomobject]@{ Case='D2_DSA'; Source='OPERATIVE_ARTICLE'; Confidence='HIGH'; Ambiguity='NO'; Count=10 },
    [pscustomobject]@{ Case='D2_DSA'; Source='OPERATIVE_ARTICLE'; Confidence='MEDIUM'; Ambiguity='NO'; Count=4 },
    [pscustomobject]@{ Case='D2_DSA'; Source='OPERATIVE_ARTICLE'; Confidence='LOW'; Ambiguity='YES'; Count=6 },
    [pscustomobject]@{ Case='D2_DSA'; Source='RECITAL'; Confidence='HIGH'; Ambiguity='NO'; Count=3 },
    [pscustomobject]@{ Case='D2_DSA'; Source='RECITAL'; Confidence='LOW'; Ambiguity='YES'; Count=7 },
    [pscustomobject]@{ Case='D3_AI_ACT'; Source='OPERATIVE_ARTICLE'; Confidence='HIGH'; Ambiguity='NO'; Count=8 },
    [pscustomobject]@{ Case='D3_AI_ACT'; Source='OPERATIVE_ARTICLE'; Confidence='MEDIUM'; Ambiguity='NO'; Count=4 },
    [pscustomobject]@{ Case='D3_AI_ACT'; Source='OPERATIVE_ARTICLE'; Confidence='LOW'; Ambiguity='YES'; Count=5 },
    [pscustomobject]@{ Case='D3_AI_ACT'; Source='RECITAL'; Confidence='HIGH'; Ambiguity='NO'; Count=2 },
    [pscustomobject]@{ Case='D3_AI_ACT'; Source='RECITAL'; Confidence='MEDIUM'; Ambiguity='NO'; Count=2 },
    [pscustomobject]@{ Case='D3_AI_ACT'; Source='RECITAL'; Confidence='LOW'; Ambiguity='YES'; Count=6 },
    [pscustomobject]@{ Case='D3_AI_ACT'; Source='ANNEX'; Confidence='LOW'; Ambiguity='YES'; Count=3 }
)

$sample = [System.Collections.Generic.List[object]]::new()
foreach ($q in $quota) {
    $pool = @($extractions | Where-Object { $_.CASE_ID -eq $q.Case -and $_.SOURCE_TYPE -eq $q.Source -and $_.EXTRACTION_CONFIDENCE -eq $q.Confidence -and $_.STRUCTURAL_AMBIGUITY -eq $q.Ambiguity })
    foreach ($row in (Get-SampleRows $pool $q.Count)) {
        $complexity = Get-Complexity $row
        $pointerCorrect = Test-Pointer $row
        $excerptValue = Normalize-Text $row.SOURCE_EXCERPT
        $excerptCore = $excerptValue
        $excerptCorrect = if ($sourceText[$row.CASE_ID].Contains($excerptValue)) {'YES_EXACT_MECHANICAL'} else {'NO_MECHANICAL'}
        if ($excerptCorrect -eq 'NO_MECHANICAL') {
            for ($cut = 1; $cut -le 3; $cut++) {
                if ($excerptValue.Length -gt $cut) {
                    $candidate = $excerptValue.Substring(0, $excerptValue.Length - $cut)
                    if ($sourceText[$row.CASE_ID].Contains($candidate)) { $excerptCore=$candidate; $excerptCorrect='YES_TRUNCATED_MECHANICAL'; break }
                }
            }
        }
        $sample.Add([pscustomobject]@{
            QA_ID = "QA2B-{0:D3}" -f ($sample.Count+1)
            EXTRACTION_ID = $row.EXTRACTION_ID
            CASE_ID = $row.CASE_ID
            SOURCE_POINTER = $row.SOURCE_POINTER
            SOURCE_TYPE = $row.SOURCE_TYPE
            EXTRACTION_CONFIDENCE = $row.EXTRACTION_CONFIDENCE
            STRUCTURAL_AMBIGUITY = $row.STRUCTURAL_AMBIGUITY
            SAMPLING_STRATUM = "$($row.SOURCE_TYPE)|$($row.EXTRACTION_CONFIDENCE)|$($row.STRUCTURAL_AMBIGUITY)|$complexity"
            ACTOR_TEXT_LUNA = $row.ACTOR_TEXT
            LEGAL_ACTION_LUNA = $row.LEGAL_ACTION
            ACTION_OBJECT_LUNA = $row.ACTION_OBJECT
            COUNTERPART_LUNA = $row.COUNTERPART_TEXT
            RECIPIENT_LUNA = $row.RECIPIENT_TEXT
            SOURCE_EXCERPT = $row.SOURCE_EXCERPT
            SOURCE_TEXT_CHECKED = 'YES_MECHANICAL; HUMAN_CONFIRMATION_PENDING'
            ACTOR_CORRECT = 'PENDING_HUMAN_REVIEW'
            ACTION_CORRECT = 'PENDING_HUMAN_REVIEW'
            OBJECT_CORRECT = 'PENDING_HUMAN_REVIEW'
            COUNTERPART_CORRECT = 'PENDING_HUMAN_REVIEW'
            RECIPIENT_CORRECT = 'PENDING_HUMAN_REVIEW'
            SOURCE_POINTER_CORRECT = 'PENDING_HUMAN_REVIEW'
            EXCERPT_CORRECT = 'PENDING_HUMAN_REVIEW'
            AMBIGUITY_JUSTIFIED = 'PENDING_HUMAN_REVIEW'
            ERROR_TYPE = 'PENDING_HUMAN_REVIEW'
            HUMAN_CORRECTION = ''
            HUMAN_REVIEWER = 'UNASSIGNED'
            HUMAN_REVIEW_STATUS = 'PENDING_HUMAN_REVIEW'
            NOTES = "AI-assisted pre-review only; do not treat as human adjudication. Mechanical checks: pointer=$pointerCorrect; excerpt=$excerptCorrect. R/I/T and mechanism review prohibited."
        })
    }
}

$sample | Export-Csv (Join-Path $qaDir 'R4_2B_HUMAN_QA_SAMPLE.csv') -NoTypeInformation -Encoding utf8

$freezeFiles = @(
    'R4_STRUCTURAL_EXTRACTION.csv', 'R4_DIGITAL_ACTOR_CANDIDATE_REGISTER.csv', 'R4_LEGAL_ACTION_REGISTER.csv',
    'R4_CROSS_REFERENCE_REGISTER.csv', 'R4_STRUCTURAL_AMBIGUITY_LOG.csv', 'R4_2_AI_EXTRACTION_RUN_SUMMARY.csv',
    'R4_2_SOURCE_COVERAGE_REPORT.csv', 'R4_2_HUMAN_QA_SAMPLE.csv'
)
$manifest = [System.Collections.Generic.List[object]]::new()
foreach ($file in $freezeFiles) {
    $path = Join-Path $extractionDir $file
    $manifest.Add([pscustomobject]@{ FILE=$file; PATH="03_extraction/$file"; SHA256=(Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash; ROW_COUNT=@(Import-Csv $path).Count; STATUS='FROZEN_PRE_QA' })
}
$methodPath = Join-Path $workspace 'R4_2_METHOD_NOTE.md'
$manifest.Add([pscustomobject]@{ FILE='R4_2_METHOD_NOTE.md'; PATH='R4_2_METHOD_NOTE.md'; SHA256=(Get-FileHash -LiteralPath $methodPath -Algorithm SHA256).Hash; ROW_COUNT=(Get-Content -LiteralPath $methodPath).Count; STATUS='FROZEN_PRE_QA' })
$manifest | Export-Csv (Join-Path $qaDir 'R4_2B_LUNA_EXTRACTION_FREEZE_MANIFEST.csv') -NoTypeInformation -Encoding utf8

function Get-AmbiguityType($Row) {
    if ($Row.ACTOR_TEXT -match '(?i)\b(it|they|this|such)\b') { return 'PRONOUN_REFERENCE_AMBIGUITY' }
    if ($Row.ACTOR_TEXT -match '(?i)\band\b|\bor\b') { return 'MULTI_ACTOR_PROVISION' }
    if ($Row.LEGAL_VERB -match '(?i)\band\b|\bor\b') { return 'MULTI_ACTION_PROVISION' }
    if (-not [string]::IsNullOrWhiteSpace($Row.CROSS_REFERENCE)) { return 'CROSS_REFERENCE_AMBIGUITY' }
    if ($Row.SOURCE_EXCERPT -match '(?i)\b(where|if|unless|provided that|only if|subject to)\b') { return 'CONDITIONAL_STRUCTURE_AMBIGUITY' }
    if ($Row.ACTION_OBJECT.Length -gt 100) { return 'ACTION_OBJECT_AMBIGUITY' }
    if (-not [string]::IsNullOrWhiteSpace($Row.COUNTERPART_TEXT)) { return 'COUNTERPART_AMBIGUITY' }
    return 'ACTION_SCOPE_AMBIGUITY'
}

$ambiguityRows = [System.Collections.Generic.List[object]]::new()
foreach ($amb in $ambiguityLog) {
    $interpretationParts = [regex]::Match($amb.LUNA_INTERPRETATION, '^(?<actor>.*?)\s+->\s+(?<verb>.*)$')
    $actorHint = if ($interpretationParts.Success) { Normalize-Text $interpretationParts.Groups['actor'].Value } else { '' }
    $verbHint = if ($interpretationParts.Success) { Normalize-Text $interpretationParts.Groups['verb'].Value } else { '' }
    $row = @($extractions | Where-Object { $_.CASE_ID -eq $amb.CASE_ID -and $_.SOURCE_POINTER -eq $amb.SOURCE_POINTER -and ($actorHint -eq '' -or $_.ACTOR_TEXT -eq $actorHint) -and ($verbHint -eq '' -or $_.LEGAL_VERB -like "$verbHint*") } | Select-Object -First 1)
    if ($row.Count -eq 0) { $row = @($extractions | Where-Object { $_.CASE_ID -eq $amb.CASE_ID -and $_.SOURCE_POINTER -eq $amb.SOURCE_POINTER } | Select-Object -First 1) }
    $row = $row | Select-Object -First 1
    if ($null -eq $row) { continue }
    $type = Get-AmbiguityType $row
    $canLuna = if ($type -in @('MULTI_ACTION_PROVISION','CROSS_REFERENCE_AMBIGUITY','CONDITIONAL_STRUCTURE_AMBIGUITY','ACTION_SCOPE_AMBIGUITY','ACTION_OBJECT_AMBIGUITY')) {'YES'} else {'NO_OR_LIMITED'}
    $ambiguityRows.Add([pscustomobject]@{
        AMBIGUITY_ID=$amb.AMBIGUITY_ID; EXTRACTION_ID=$row.EXTRACTION_ID; CASE_ID=$row.CASE_ID; SOURCE_POINTER=$row.SOURCE_POINTER; AMBIGUITY_TYPE=$type
        AMBIGUITY_DESCRIPTION=$amb.AMBIGUITY_NOTE; STRUCTURAL_OR_INTERPRETIVE='STRUCTURAL'; CAN_LUNA_RESOLVE_WITHOUT_THEORY=$canLuna; LIKELY_REQUIRES_TERRA='NO'; LIKELY_REQUIRES_HUMAN='YES'; NOTES='Typology generated from the frozen extraction flag and direct structural fields; no theoretical adjudication.'
    })
}
$ambiguityRows | Export-Csv (Join-Path $qaDir 'R4_2B_AMBIGUITY_TYPOLOGY.csv') -NoTypeInformation -Encoding utf8

$corrections = @([pscustomobject]@{ CORRECTION_ID=''; EXTRACTION_ID=''; CASE_ID=''; SOURCE_POINTER=''; FIELD=''; ORIGINAL_VALUE=''; CORRECTED_VALUE=''; ERROR_TYPE=''; HUMAN_EVIDENCE=''; CORRECTION_STATUS=''; NOTES='' }) | Select-Object -First 0
$corrections | Export-Csv (Join-Path $qaDir 'R4_2B_EXTRACTION_CORRECTION_REGISTER.csv') -NoTypeInformation -Encoding utf8

$systematic = @(
    [pscustomobject]@{ AUDIT_ID='SYS-001'; PATTERN='CONFIDENCE_AMBIGUITY_COUPLING'; AFFECTED_ROWS=@($extractions|Where-Object STRUCTURAL_AMBIGUITY -eq 'YES').Count; AFFECTED_CASES='D1_GDPR;D2_DSA;D3_AI_ACT'; AFFECTED_SOURCE_TYPES='OPERATIVE_ARTICLE;RECITAL;ANNEX'; EVIDENCE='The original extractor assigns LOW confidence whenever its structural ambiguity condition is met, so ambiguity and LOW confidence are mechanically coupled in this Luna artifact.'; CLASSIFICATION='PROVISIONAL_METHOD_PATTERN'; RECOMMENDED_ACTION='Human QA should test whether the flags are justified; do not rewrite the original extraction or propagate corrections.'; STATUS='REQUIRES_HUMAN_REVIEW' }
    [pscustomobject]@{ AUDIT_ID='SYS-002'; PATTERN='TRUNCATED_SOURCE_EXCERPT'; AFFECTED_ROWS=@($extractions|Where-Object {$_.SOURCE_EXCERPT.Length -ge 500}).Count; AFFECTED_CASES='D1_GDPR;D2_DSA;D3_AI_ACT'; AFFECTED_SOURCE_TYPES='OPERATIVE_ARTICLE;RECITAL;ANNEX'; EVIDENCE='The original extraction limits SOURCE_EXCERPT to a fixed length and appends a truncation marker; the concise excerpt may therefore require direct source confirmation for exact wording.'; CLASSIFICATION='PROVISIONAL_EXTRACTION_DEFECT'; RECOMMENDED_ACTION='Human QA should verify truncated excerpts; propose a separate validated copy with traceable full-sentence excerpts only after review.'; STATUS='REQUIRES_HUMAN_REVIEW' }
)
$systematic | Export-Csv (Join-Path $qaDir 'R4_2B_SYSTEMATIC_ERROR_AUDIT.csv') -NoTypeInformation -Encoding utf8

function Add-Metric($Scope, $Value, $Rows, $Notes) {
    [pscustomobject]@{ SCOPE=$Scope; VALUE=$Value; N_REVIEWED=$Rows; FULLY_CORRECT='PENDING_HUMAN_REVIEW'; ROWS_WITH_ERRORS='PENDING_HUMAN_REVIEW'; ACTOR_ACCURACY='PENDING_HUMAN_REVIEW'; ACTION_ACCURACY='PENDING_HUMAN_REVIEW'; OBJECT_ACCURACY='PENDING_HUMAN_REVIEW'; COUNTERPART_ACCURACY='PENDING_HUMAN_REVIEW'; RECIPIENT_ACCURACY='PENDING_HUMAN_REVIEW'; SOURCE_POINTER_ACCURACY='MECHANICAL_CHECK_RECORDED'; EXCERPT_ACCURACY='MECHANICAL_CHECK_RECORDED'; AMBIGUITY_PRECISION='PENDING_HUMAN_REVIEW'; REVIEW_STATUS='PENDING_HUMAN_REVIEW'; NOTES=$Notes }
}
$metrics = [System.Collections.Generic.List[object]]::new()
$metrics.Add((Add-Metric 'OVERALL' '90-record stratified sample' $sample.Count 'No human researcher review was performed by this runtime.'))
foreach($case in @('D1_GDPR','D2_DSA','D3_AI_ACT')) { $metrics.Add((Add-Metric 'CASE' $case @($sample|Where-Object CASE_ID -eq $case).Count 'Case-level human metrics pending.')) }
foreach($conf in @('HIGH','MEDIUM','LOW')) { $metrics.Add((Add-Metric 'CONFIDENCE' $conf @($sample|Where-Object EXTRACTION_CONFIDENCE -eq $conf).Count 'Confidence calibration pending human review.')) }
foreach($amb in @('YES','NO')) { $metrics.Add((Add-Metric 'AMBIGUITY' $amb @($sample|Where-Object STRUCTURAL_AMBIGUITY -eq $amb).Count 'Ambiguity precision pending human review.')) }
foreach($type in @('OPERATIVE_ARTICLE','RECITAL','ANNEX')) { $metrics.Add((Add-Metric 'SOURCE_TYPE' $type @($sample|Where-Object SOURCE_TYPE -eq $type).Count 'Source-type metrics pending human review.')) }
$metrics | Export-Csv (Join-Path $qaDir 'R4_2B_QA_METRICS.csv') -NoTypeInformation -Encoding utf8

$calibration = [System.Collections.Generic.List[object]]::new()
foreach($conf in @('HIGH','MEDIUM','LOW')) {
    $rows=@($sample|Where-Object EXTRACTION_CONFIDENCE -eq $conf)
    $calibration.Add([pscustomobject]@{ CONFIDENCE_LEVEL=$conf; N_REVIEWED=$rows.Count; FULLY_CORRECT='PENDING_HUMAN_REVIEW'; ERROR_COUNT='PENDING_HUMAN_REVIEW'; FULL_CORRECT_RATE='PENDING_HUMAN_REVIEW'; AMBIGUITY_RATE=if($rows.Count -gt 0){('{0:P1}' -f (@($rows|Where-Object STRUCTURAL_AMBIGUITY -eq 'YES').Count/$rows.Count))}else{'0.0%'}; NOTES='Calibration cannot be concluded until a human researcher reviews the sample.' })
}
$calibration | Export-Csv (Join-Path $qaDir 'R4_2B_CONFIDENCE_CALIBRATION.csv') -NoTypeInformation -Encoding utf8

Write-Output "R4.2B package prepared: sample=$($sample.Count); frozen_files=$($manifest.Count); ambiguity_typed=$($ambiguityRows.Count); corrections=0; systematic_patterns=$($systematic.Count)"
