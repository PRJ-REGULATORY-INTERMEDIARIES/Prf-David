$ErrorActionPreference='Stop'

$r4=Split-Path -Parent $PSScriptRoot
$root=Join-Path $r4 '03_extraction'
$repair=Join-Path $root 'qa\repair'
$b0=Join-Path $repair 'R4_2E_B0'
$b1=Join-Path $repair 'R4_2E_B1'
New-Item -ItemType Directory -Path $b1 -Force|Out-Null

function Get-Sha256([string]$Value){
    $bytes=[Text.Encoding]::UTF8.GetBytes($Value)
    $sha=[Security.Cryptography.SHA256]::Create()
    try{$hash=$sha.ComputeHash($bytes)}finally{$sha.Dispose()}
    return ([BitConverter]::ToString($hash).Replace('-',''))
}
function Get-PriorityRank([string]$Priority){switch($Priority){'P1'{1}'P2'{2}'P3'{3}'P4'{4}default{9}}}
function Get-ComplexityRank([string]$Complexity){switch($Complexity){'COMPLEX'{1}'MODERATE'{2}'SIMPLE'{3}'NONE'{4}default{9}}}

$extract=@(Import-Csv (Join-Path $root 'R4_STRUCTURAL_EXTRACTION.csv') -Encoding UTF8)
$sig=@(Import-Csv (Join-Path $b0 'R4_2E_B0_REPAIR_SIGNATURE_REGISTER.csv') -Encoding UTF8)
$reps=@(Import-Csv (Join-Path $b0 'R4_2E_B0_MODEL_REPRESENTATIVE_SAMPLE.csv') -Encoding UTF8)
$freeze=Get-Content (Join-Path $b0 'R4_2E_B0_FREEZE_RECORD.md') -Raw
$sourceHash=(Get-FileHash (Join-Path $root 'R4_STRUCTURAL_EXTRACTION.csv') -Algorithm SHA256).Hash
$freezeHash=(Get-FileHash (Join-Path $b0 'R4_2E_B0_FREEZE_RECORD.md') -Algorithm SHA256).Hash
if($extract.Count -ne 1404 -or $sig.Count -ne 1404){throw 'Frozen source/signature row count is not 1,404.'}
if($freeze -notmatch 'R4_2E_B0_FROZEN_READY_FOR_ADVANCED_MODEL_VALIDATION'){throw 'B0 freeze status absent.'}

$extractById=@{};foreach($x in $extract){$extractById[$x.EXTRACTION_ID]=$x}
$sigById=@{};foreach($x in $sig){$sigById[$x.RECORD_ID]=$x}

$templates=@($reps|Where-Object {$sigById[$_.RECORD_ID].PROPOSED_REPAIR_ROUTE -eq 'TEMPLATE_VALIDATION_REQUIRED'})
$individual=@($sig|Where-Object {$_.PROPOSED_REPAIR_ROUTE -eq 'ADVANCED_MODEL_CASE_REVIEW' -and $_.REVIEW_QUEUE_ELIGIBILITY -eq 'UNADJUDICATED_REVIEW_CANDIDATE'})
if($templates.Count -ne 99){throw "Expected 99 template representatives; found $($templates.Count)."}
if($individual.Count -ne 32){throw "Expected 32 individual cases; found $($individual.Count)."}

# Controls are selected reproducibly from the B0 NO_REPAIR route. High priority, high complexity and prior candidate signals rank first;
# the selection then takes different source-type/signature combinations before filling to four per act.
$controls=[System.Collections.Generic.List[object]]::new()
foreach($act in @('D1_GDPR','D2_DSA','D3_AI_ACT')){
    $pool=@($sig|Where-Object {$_.PROPOSED_REPAIR_ROUTE -eq 'NO_REPAIR' -and $_.HUMAN_ANALOGUE_AVAILABLE -ne 'YES' -and $_.ACT -eq $act}|ForEach-Object {
        [pscustomobject]@{Row=$_;PriorityRank=(Get-PriorityRank $_.ORIGINAL_PRIORITY);ComplexityRank=(Get-ComplexityRank $_.ORIGINAL_COMPLEXITY);CandidateRank=if($_.REPAIR_CANDIDATE -eq 'YES'){1}elseif($_.REPAIR_CANDIDATE -eq 'UNCERTAIN'){2}else{3};SupportRank=if($_.CROSS_MODEL_SUPPORT -in @('BOTH_FLAGGED','LUNA_ONLY','TERRA_ONLY')){1}elseif($_.CROSS_MODEL_SUPPORT -eq 'NEITHER_FLAGGED'){2}else{3}}
    }|Sort-Object PriorityRank,ComplexityRank,CandidateRank,SupportRank,{$_.Row.SOURCE_TYPE},{$_.Row.STRUCTURAL_SIGNATURE},{$_.Row.RECORD_ID})
    $chosen=[System.Collections.Generic.List[object]]::new();$seen=@{}
    foreach($item in $pool){$key="$($item.Row.SOURCE_TYPE)|$($item.Row.STRUCTURAL_SIGNATURE)";if(-not $seen.ContainsKey($key)){$chosen.Add($item.Row);$seen[$key]=$true;if($chosen.Count -eq 4){break}}}
    foreach($item in $pool){if($chosen.Count -eq 4){break};if(-not @($chosen|Where-Object RECORD_ID -eq $item.Row.RECORD_ID).Count){$chosen.Add($item.Row)}}
    if($chosen.Count -ne 4){throw "Could not select four controls for $act."}
    foreach($row in $chosen){$e=$extractById[$row.RECORD_ID];$controls.Add([pscustomobject][ordered]@{CASE_ID=$e.CASE_ID;RECORD_ID=$e.EXTRACTION_ID;ACT=$row.ACT;SOURCE_TYPE=$e.SOURCE_TYPE;SOURCE_REFERENCE=$e.SOURCE_POINTER;REPAIR_FAMILY_ID=$row.REPAIR_FAMILY_ID;ORIGINAL_PRIORITY=$row.ORIGINAL_PRIORITY;ORIGINAL_COMPLEXITY=$row.ORIGINAL_COMPLEXITY;ORIGINAL_CANDIDATE_STATUS=$row.REPAIR_CANDIDATE;STRUCTURAL_SIGNATURE=$row.STRUCTURAL_SIGNATURE;SELECTION_METHOD='DETERMINISTIC_BOUNDARY_STRATIFIED_NO_REPAIR_SELECTION';CONTROL_STATUS='NO_REPAIR_CONTROL_HIDDEN_DURING_SUBSTANTIVE_REVIEW'})}
}
if($controls.Count -ne 12){throw 'Control count is not 12.'}

$all=[System.Collections.Generic.List[object]]::new()
foreach($x in $templates){$e=$extractById[$x.RECORD_ID];$s=$sigById[$x.RECORD_ID];$all.Add([pscustomobject][ordered]@{CASE_ID=$e.CASE_ID;RECORD_ID=$e.EXTRACTION_ID;ACT=$s.ACT;SOURCE_TYPE=$e.SOURCE_TYPE;SOURCE_REFERENCE=$e.SOURCE_POINTER;REVIEW_TYPE='TEMPLATE_REPRESENTATIVE';REPAIR_FAMILY_ID=$s.REPAIR_FAMILY_ID;STRUCTURAL_SIGNATURE=$s.STRUCTURAL_SIGNATURE;CONTROL_STATUS='NOT_CONTROL'})}
foreach($s in $individual){$e=$extractById[$s.RECORD_ID];$all.Add([pscustomobject][ordered]@{CASE_ID=$e.CASE_ID;RECORD_ID=$e.EXTRACTION_ID;ACT=$s.ACT;SOURCE_TYPE=$e.SOURCE_TYPE;SOURCE_REFERENCE=$e.SOURCE_POINTER;REVIEW_TYPE='INDIVIDUAL_ADVANCED_CASE';REPAIR_FAMILY_ID=$s.REPAIR_FAMILY_ID;STRUCTURAL_SIGNATURE=$s.STRUCTURAL_SIGNATURE;CONTROL_STATUS='NOT_CONTROL'})}
foreach($c in $controls){$all.Add([pscustomobject][ordered]@{CASE_ID=$c.CASE_ID;RECORD_ID=$c.RECORD_ID;ACT=$c.ACT;SOURCE_TYPE=$c.SOURCE_TYPE;SOURCE_REFERENCE=$c.SOURCE_REFERENCE;REVIEW_TYPE='NO_REPAIR_CONTROL';REPAIR_FAMILY_ID=$c.REPAIR_FAMILY_ID;STRUCTURAL_SIGNATURE=$c.STRUCTURAL_SIGNATURE;CONTROL_STATUS=$c.CONTROL_STATUS})}
if($all.Count -ne 143 -or @($all.RECORD_ID|Sort-Object -Unique).Count -ne 143){throw 'Review universe must be 143 unique records.'}

# Greedy deterministic allocation: place each act/type queue entry in the batch with the lowest total, then lowest act/type concentration.
$batches=@('B1-01','B1-02','B1-03','B1-04');$state=@{};foreach($b in $batches){$state[$b]=[pscustomobject]@{Total=0;Acts=@{};Types=@{}}}
$ordered=@($all|Sort-Object ACT,REVIEW_TYPE,SOURCE_TYPE,STRUCTURAL_SIGNATURE,RECORD_ID)
$assigned=[System.Collections.Generic.List[object]]::new()
foreach($item in $ordered){
    $selected=$batches|Sort-Object @{Expression={$state[$_].Total};Ascending=$true},@{Expression={if($state[$_].Acts.ContainsKey($item.ACT)){$state[$_].Acts[$item.ACT]}else{0}};Ascending=$true},@{Expression={if($state[$_].Types.ContainsKey($item.REVIEW_TYPE)){$state[$_].Types[$item.REVIEW_TYPE]}else{0}};Ascending=$true},@{Expression={$_};Ascending=$true}|Select-Object -First 1
    $st=$state[$selected];$st.Total++;if(-not $st.Acts.ContainsKey($item.ACT)){$st.Acts[$item.ACT]=0};$st.Acts[$item.ACT]++;if(-not $st.Types.ContainsKey($item.REVIEW_TYPE)){$st.Types[$item.REVIEW_TYPE]=0};$st.Types[$item.REVIEW_TYPE]++
    $inputHash=Get-Sha256 "$sourceHash|$freezeHash|$($item.RECORD_ID)|$($item.STRUCTURAL_SIGNATURE)"
    $assigned.Add([pscustomobject][ordered]@{BATCH_ID=$selected;CASE_ID=$item.CASE_ID;RECORD_ID=$item.RECORD_ID;ACT=$item.ACT;SOURCE_TYPE=$item.SOURCE_TYPE;SOURCE_REFERENCE=$item.SOURCE_REFERENCE;REVIEW_TYPE=$item.REVIEW_TYPE;REPAIR_FAMILY_ID=$item.REPAIR_FAMILY_ID;INPUT_HASH=$inputHash;ORDER_IN_BATCH=0;CONTROL_STATUS=$item.CONTROL_STATUS})
}
foreach($b in $batches){$n=0;foreach($x in @($assigned|Where-Object BATCH_ID -eq $b|Sort-Object ACT,REVIEW_TYPE,SOURCE_TYPE,RECORD_ID)){$n++;$x.ORDER_IN_BATCH=$n}}
if((@($assigned|Where-Object BATCH_ID -eq 'B1-01').Count -ne 36) -or (@($assigned|Where-Object BATCH_ID -eq 'B1-02').Count -ne 36) -or (@($assigned|Where-Object BATCH_ID -eq 'B1-03').Count -ne 36) -or (@($assigned|Where-Object BATCH_ID -eq 'B1-04').Count -ne 35)){throw 'Batch size imbalance.'}

$controls|Export-Csv (Join-Path $b1 'R4_2E_B1_NO_REPAIR_CONTROL_SAMPLE.csv') -NoTypeInformation -Encoding UTF8
$assigned|Select-Object BATCH_ID,CASE_ID,RECORD_ID,ACT,SOURCE_TYPE,SOURCE_REFERENCE,REVIEW_TYPE,REPAIR_FAMILY_ID,INPUT_HASH,ORDER_IN_BATCH|Export-Csv (Join-Path $b1 'R4_2E_B1_BATCH_MANIFEST.csv') -NoTypeInformation -Encoding UTF8

# Blind reviewer input deliberately omits CONTROL_STATUS and reuses the same neutral review label for every record.
$blind=[System.Collections.Generic.List[object]]::new()
foreach($x in ($assigned|Sort-Object BATCH_ID,ORDER_IN_BATCH)){$e=$extractById[$x.RECORD_ID];$s=$sigById[$x.RECORD_ID];$blind.Add([pscustomobject][ordered]@{BATCH_ID=$x.BATCH_ID;ORDER_IN_BATCH=$x.ORDER_IN_BATCH;CASE_ID=$e.CASE_ID;RECORD_ID=$e.EXTRACTION_ID;ACT=$x.ACT;SOURCE_TYPE=$e.SOURCE_TYPE;SOURCE_REFERENCE=$e.SOURCE_POINTER;REVIEW_SCOPE='STRUCTURAL_LEGAL_VALIDATION';REPAIR_FAMILY_ID=$x.REPAIR_FAMILY_ID;INPUT_HASH=$x.INPUT_HASH;ORIGINAL_ACTOR=$e.ACTOR_TEXT;ORIGINAL_ACTION=$e.LEGAL_ACTION;ORIGINAL_OBJECT=$e.ACTION_OBJECT;ORIGINAL_COUNTERPART=$e.COUNTERPART_TEXT;ORIGINAL_RECIPIENT=$e.RECIPIENT_TEXT;SOURCE_EXCERPT=$e.SOURCE_EXCERPT;RULE_SIGNATURE=$s.RULE_SIGNATURE;STRUCTURAL_SIGNATURE=$s.STRUCTURAL_SIGNATURE;MODEL_REQUESTED='GPT-5.6 Terra High';MODEL_RESEARCHER_SELECTED='GPT-5.6 Terra High';MODEL_RUNTIME_VARIANT='MODEL_VARIANT_NOT_EXPOSED'})}
$blind|Export-Csv (Join-Path $b1 'R4_2E_B1_BLIND_SUBSTANTIVE_REVIEW_INPUT.csv') -NoTypeInformation -Encoding UTF8

$manifestHash=(Get-FileHash (Join-Path $b1 'R4_2E_B1_BATCH_MANIFEST.csv') -Algorithm SHA256).Hash
$runLog=foreach($b in $batches){$rows=@($assigned|Where-Object BATCH_ID -eq $b);[pscustomobject][ordered]@{BATCH_ID=$b;RUN_VERSION='v1';CASE_COUNT=$rows.Count;INPUT_HASH=(Get-Sha256 (($rows.INPUT_HASH|Sort-Object)-join '|'));OUTPUT_HASH='';MODEL_REQUESTED='GPT-5.6 Terra High';MODEL_RESEARCHER_SELECTED='GPT-5.6 Terra High';MODEL_RUNTIME_VARIANT='MODEL_VARIANT_NOT_EXPOSED';START_STATUS='R4_2E_B0_FROZEN_READY_FOR_ADVANCED_MODEL_VALIDATION';END_STATUS='PENDING_SUBSTANTIVE_REVIEW';COMPLETION_STATUS='PENDING';MANIFEST_SHA256=$manifestHash;RUN_TIMESTAMP=(Get-Date -Format 'yyyy-MM-ddTHH:mm:ssK')}
}
$runLog|Export-Csv (Join-Path $b1 'R4_2E_B1_BATCH_RUN_LOG.csv') -NoTypeInformation -Encoding UTF8

$allocation=@"
# R4.2E-B1 — Batch allocation freeze

**Status:** `R4_2E_B1_BATCHES_FROZEN_PENDING_SUBSTANTIVE_VALIDATION`

The substantive review universe contains 143 unique records: 99 template representatives, 32 individual advanced cases and 12 hidden NO_REPAIR controls. The controls are preserved in the separate control-sample file and are absent as a category from the blind substantive input.

`MODEL_REQUESTED = GPT-5.6 Terra High`  
`MODEL_RESEARCHER_SELECTED = GPT-5.6 Terra High`  
`MODEL_RUNTIME_VARIANT = MODEL_VARIANT_NOT_EXPOSED`

- Frozen structural source SHA-256: `$sourceHash`
- B0 freeze-record SHA-256: `$freezeHash`
- Batch-manifest SHA-256: `$manifestHash`
- Batch counts: B1-01 = 36; B1-02 = 36; B1-03 = 36; B1-04 = 35.

Allocation is deterministic: controls are boundary-oriented, stratified at four records per act; all cases are assigned with a fixed sort order and least-loaded batch, act and review-type tie-breakers. No substantive decision, model review, corpus repair, R/I/T coding or mechanism coding occurs in this allocation file.
"@
[IO.File]::WriteAllText((Join-Path $b1 'R4_2E_B1_BATCH_ALLOCATION_FREEZE.md'),$allocation,(New-Object Text.UTF8Encoding($false)))

"Batches frozen: $($assigned.Count) records; manifest=$manifestHash; controls=$($controls.Count); templates=$($templates.Count); individual=$($individual.Count)"
