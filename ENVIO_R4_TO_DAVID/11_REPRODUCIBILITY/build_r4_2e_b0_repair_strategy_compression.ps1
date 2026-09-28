$ErrorActionPreference='Stop'
$r4=Split-Path -Parent $PSScriptRoot
$root=Join-Path $r4 '03_extraction'
$qa=Join-Path $root 'qa'
$repair=Join-Path $qa 'repair'
$b0=Join-Path $repair 'R4_2E_B0'
New-Item -ItemType Directory -Path $b0 -Force|Out-Null
$extract=@(Import-Csv (Join-Path $root 'R4_STRUCTURAL_EXTRACTION.csv') -Encoding UTF8)
$aDir=Join-Path $repair 'R4_2E_A'
$cand=@(Import-Csv (Join-Path $aDir 'R4_2E_A_REPAIR_CANDIDATE_REGISTER.csv') -Encoding UTF8)
$rel=@(Import-Csv (Join-Path $aDir 'R4_2E_A_COUNTERPART_RECIPIENT_BURDEN_AUDIT.csv') -Encoding UTF8)
$aa=@(Import-Csv (Join-Path $aDir 'R4_2E_A_ACTOR_ACTION_REPAIR_AUDIT.csv') -Encoding UTF8)
$human=@(Import-Csv (Join-Path $repair 'R4_2D_HUMAN_DIAGNOSTIC_COMPLETED.csv') -Encoding UTF8)
$humanA=@{};foreach($h in $human){$humanA[$h.EXTRACTION_ID]=$h}
$candA=@{};foreach($c in $cand){$candA[$c.RECORD_ID]=$c}
$relA=@{};foreach($x in $rel){$relA[$x.RECORD_ID]=$x}
$aaA=@{};foreach($x in $aa){$aaA[$x.RECORD_ID]=$x}
if($extract.Count -ne 1404 -or $cand.Count -ne 1404 -or $rel.Count -ne 1404 -or $aa.Count -ne 1404){throw 'Input row count is not 1,404.'}
$frozen=(Get-FileHash (Join-Path $root 'R4_STRUCTURAL_EXTRACTION.csv') -Algorithm SHA256).Hash
$freezeManifest=Import-Csv (Join-Path $qa 'R4_2B_LUNA_EXTRACTION_FREEZE_MANIFEST.csv') -Encoding UTF8
if($frozen -ne $freezeManifest[0].SHA256){throw 'The source extraction no longer matches its freeze manifest.'}

function Get-Tag([string]$Value,[string]$Pattern,[string]$Tag,[string]$Default){if($Value -match $Pattern){return $Tag};return $Default}
function Get-HashId([string]$Value){$bytes=[Text.Encoding]::UTF8.GetBytes($Value);$sha=[Security.Cryptography.SHA256]::Create();try{$hash=$sha.ComputeHash($bytes)}finally{$sha.Dispose()};return ([BitConverter]::ToString($hash).Replace('-','').Substring(0,12))}
function Get-RouteText([string]$Root,[string]$Key){switch -Wildcard ($Root){'NO_SIGNAL*' {'No actionable signal beyond no-repair/weak-only evidence.'} '*DISCOURSE*' {'Local action field appears to contain a discourse marker rather than the legal predicate; source-to-verb alignment remains explicit.'} '*RELATIONAL_ABSTRACT*' {'A prepositional phrase with an abstract complement may have been placed in a relational slot; validate relation semantics once and then make separate field decisions.'} '*RELATIONAL_SOURCE*' {'An embedded source/mandate phrase may have been promoted to a matrix-level relation.'} '*RELATIONAL_OMISSION*' {'A communication predicate and possible addressee co-occur with an empty relational slot.'} '*COORDINATED*' {'Two coordinated legal predicates/consequences may have been collapsed.'} '*PASSIVE*' {'A passive predicate with uncertain agent assignment needs proposition-level review.'} '*PROPOSITION*' {'A clause, sentence, or proposition boundary may affect role assignment.'} '*OBJECT*' {'The object span may include a modifier, boundary fragment, or residual material.'} '*MODALITY*' {'The modality/deontic construction fields warrant a clause-level consistency check.'} '*ACTOR_SPAN*' {'The actor span has a possible truncation/complement cue.'} default {'Multiple or weak heuristic signals; inspect the row-level triggers before assigning work.'}}}

$raw=[System.Collections.Generic.List[object]]::new()
foreach($e in $extract){
    $c=$candA[$e.EXTRACTION_ID];$r=$relA[$e.EXTRACTION_ID];$a=$aaA[$e.EXTRACTION_ID];$h=$humanA[$e.EXTRACTION_ID]
    $tr=@($c.RULE_TRIGGERED -split ';'|Where-Object {$_ -and $_ -ne 'NONE'})
    $rootTag='NO_SIGNAL'
    if($a.DISCOURSE_ONLY_ACTION -eq 'True'){$rootTag='DISCOURSE_ACTION'}
    elseif($a.COORDINATED_PREDICATE_CANDIDATE -eq 'True'){$rootTag='COORDINATED_PREDICATE'}
    elseif($a.PASSIVE_NO_EXPLICIT_ACTOR_CANDIDATE -eq 'True'){$rootTag='PASSIVE_ACTOR_RISK'}
    elseif($tr -contains 'EMBEDDED_SOURCE_RELATION_MUST_NOT_BE_PROMOTED'){$rootTag='RELATIONAL_SOURCE_PROMOTION'}
    elseif($tr -contains 'EXPLICIT_RELATIONAL_ACTOR_MUST_NOT_BE_DROPPED'){$rootTag='RELATIONAL_OMISSION'}
    elseif($tr -contains 'RELATIONAL_ENTITY_MUST_BE_ACTOR_CAPABLE'){$rootTag='RELATIONAL_ABSTRACT_COMPLEMENT'}
    elseif($tr -contains 'PROPOSITION_BOUNDARIES_MUST_BE_PRESERVED'){$rootTag='PROPOSITION_BOUNDARY_RISK'}
    elseif($tr -contains 'OBJECT_MUST_NOT_FUNCTION_AS_RESIDUAL_BUCKET'){$rootTag='OBJECT_RESIDUAL_RISK'}
    elseif($tr -contains 'PRESERVE_LEGAL_MODALITY' -or $tr -contains 'PRESERVE_MODAL_DEONTIC_LEXICAL_CONSTRUCTION'){$rootTag='MODALITY_DEONTIC_RISK'}
    elseif($a.ACTOR_SPAN_TRUNCATION_CANDIDATE -eq 'True' -or $a.ACTOR_COMPLEMENT_CANDIDATE -eq 'True'){$rootTag='ACTOR_SPAN_RISK'}
    elseif($tr.Count -gt 0){$rootTag='WEAK_OR_MULTIPLE_SIGNAL'}
    $actorTag=if($a.PASSIVE_NO_EXPLICIT_ACTOR_CANDIDATE -eq 'True'){'PASSIVE_AGENT_UNCERTAIN'}elseif($a.ACTOR_SPAN_TRUNCATION_CANDIDATE -eq 'True'){'COORDINATED_OR_TRUNCATION_CUE'}elseif($a.ACTOR_COMPLEMENT_CANDIDATE -eq 'True'){'PREPOSITIONAL_OR_COMPLEMENT_SPAN'}elseif($e.ACTOR_TEXT.Length -gt 55 -and $e.ACTOR_TEXT -match '\b(where|which|that)\b'){'LONG_RELATIVE_SPAN'}else{'ORDINARY_NOMINAL_OR_COORDINATED'}
    $actionTag=if($a.DISCOURSE_ONLY_ACTION -eq 'True'){'DISCOURSE_ONLY'}elseif($tr -contains 'PRESERVE_MODAL_DEONTIC_LEXICAL_CONSTRUCTION'){'DEONTIC_CONSTRUCTION_SPLIT_CUE'}elseif($tr -contains 'PRESERVE_MODALITY'){'MODALITY_METADATA_CHECK'}elseif($a.PREDICATE_FRAGMENTATION_CANDIDATE -eq 'True'){'PREDICATE_OR_LEXICAL_SPAN_RISK'}else{'OTHER_ACTION_SPAN'}
    $objectTag=if($e.ACTION_OBJECT -match '^[,.;:]'){'PUNCTUATION_LEADING'}elseif($e.ACTION_OBJECT -match '…|\.\.\.'){'ELLIPSIS_OR_SOURCE_GAP'}elseif($tr -contains 'OBJECT_MUST_NOT_FUNCTION_AS_RESIDUAL_BUCKET'){'RESIDUAL_BUCKET_CUE'}elseif($tr -contains 'TEMPORAL_SPATIAL_MANNER_MODIFIERS_ARE_NOT_CORE_ACTION_OR_OBJECT'){'MODIFIER_CUE'}elseif($e.ACTION_OBJECT.Length -gt 220){'LONG_CLAUSAL_SPAN'}else{'ORDINARY_OBJECT_SPAN'}
    $relTag=if(-not $e.COUNTERPART_TEXT -and -not $e.RECIPIENT_TEXT){'BOTH_EMPTY'}elseif($r.VALUES_IDENTICAL -eq 'True' -and ($tr -contains 'RELATIONAL_ENTITY_MUST_BE_ACTOR_CAPABLE')){'IDENTICAL_ABSTRACT_COMPLEMENT'}elseif($r.VALUES_IDENTICAL -eq 'True' -and ($tr -contains 'PREPOSITION_DOES_NOT_IMPLY_RECIPIENT')){'IDENTICAL_PREPOSITIONAL_UNCLEAR_ENTITY'}elseif($r.VALUES_IDENTICAL -eq 'True'){'IDENTICAL_ENTITY_OR_PHRASE'}elseif($e.COUNTERPART_TEXT -and -not $e.RECIPIENT_TEXT){'COUNTERPART_ONLY'}elseif($e.RECIPIENT_TEXT -and -not $e.COUNTERPART_TEXT){'RECIPIENT_ONLY'}else{'DISTINCT_OR_OTHER'}
    $propTag=if($a.PROPOSITION_BOUNDARY_CONTAMINATION_CANDIDATE -eq 'True'){'BOUNDARY_TRIGGER'}elseif($c.REPAIR_COMPLEXITY -eq 'COMPLEX'){'COMPLEXITY_ONLY'}else{'NO_STRONG_BOUNDARY_CUE'}
    $referenceShape=if([string]$e.SOURCE_POINTER -match '(?i)annex|annex'){'ANNEX_LAYOUT'}elseif([string]$e.SOURCE_POINTER -match '(?i)recital'){'RECITAL_LAYOUT'}elseif([string]$e.SOURCE_POINTER -match '(?i)article'){'ARTICLE_LAYOUT'}else{'OTHER_REFERENCE_LAYOUT'}
    $signature=($rootTag,$actorTag,$actionTag,$objectTag,$relTag,$propTag,$referenceShape,$e.SOURCE_TYPE,$c.REPAIR_COMPLEXITY,$c.REPAIR_CANDIDATE,$c.CROSS_MODEL_STATUS -join '|')
    $familyId='RF-'+(Get-HashId $signature)
    $raw.Add([pscustomobject][ordered]@{
        RECORD_ID=$e.EXTRACTION_ID;ACT=$e.CASE_ID;SOURCE_TYPE=$e.SOURCE_TYPE;SOURCE_REFERENCE=$e.SOURCE_POINTER
        ORIGINAL_ACTOR=$e.ACTOR_TEXT;ORIGINAL_ACTION=$e.LEGAL_ACTION;ORIGINAL_OBJECT=$e.ACTION_OBJECT;ORIGINAL_COUNTERPART=$e.COUNTERPART_TEXT;ORIGINAL_RECIPIENT=$e.RECIPIENT_TEXT
        ORIGINAL_PRIORITY=$c.PRIORITY;ORIGINAL_COMPLEXITY=$c.REPAIR_COMPLEXITY;ORIGINAL_HANDLER=$c.RECOMMENDED_NEXT_HANDLER
        REPAIR_CANDIDATE=$c.REPAIR_CANDIDATE;RULE_TRIGGERED=$c.RULE_TRIGGERED;RULE_SIGNATURE=if($tr.Count){$tr -join ';'}else{'NONE'}
        PRIMARY_STRUCTURAL_FAMILY=$rootTag;ACTOR_SPAN_PATTERN=$actorTag;ACTION_SPAN_PATTERN=$actionTag;OBJECT_SPAN_PATTERN=$objectTag;RELATIONAL_PATTERN=$relTag;PROPOSITION_BOUNDARY_RISK=$propTag
        CROSS_MODEL_SUPPORT=$c.CROSS_MODEL_STATUS;CROSS_MODEL_SUPPORTED_PATTERNS=$c.CROSS_MODEL_SUPPORTED_PATTERNS
        HUMAN_CASE_ID=if($h){$h.DIAGNOSTIC_ID}else{''};HUMAN_ANALOGUE_AVAILABLE=if($h){'YES'}else{'NO'}
        HUMAN_DIAGNOSTIC_CLASS=if($h){$h.HUMAN_DIAGNOSTIC_DEFECT_CLASS}else{''};STRUCTURAL_SIGNATURE=$signature;REPAIR_FAMILY_ID=$familyId
        SOURCE_AMBIGUITY_FLAG=$e.STRUCTURAL_AMBIGUITY;SOURCE_EXCERPT=$e.SOURCE_EXCERPT;SOURCE_REFERENCE_SHAPE=$referenceShape
    })
}

$groups=@($raw|Group-Object REPAIR_FAMILY_ID)
$familyMeta=@{}
foreach($g in $groups){
    $rows=@($g.Group);$reviewRows=@($rows|Where-Object HUMAN_ANALOGUE_AVAILABLE -ne 'YES');$sig=$rows[0].STRUCTURAL_SIGNATURE;$rootTag=$rows[0].PRIMARY_STRUCTURAL_FAMILY
    $active=@($reviewRows|Where-Object { $_.REPAIR_CANDIDATE -eq 'YES' -or $_.REPAIR_CANDIDATE -eq 'UNCERTAIN' -or $_.CROSS_MODEL_SUPPORT -in @('BOTH_FLAGGED','LUNA_ONLY','TERRA_ONLY') }).Count -gt 0
    $known=@($rows|Where-Object HUMAN_ANALOGUE_AVAILABLE -eq 'YES').Count -gt 0
    $riskType=$rows[0].PRIMARY_STRUCTURAL_FAMILY
    $weakOnly=@($reviewRows|Where-Object { $_.RULE_SIGNATURE -ne 'NONE' -and $_.REPAIR_CANDIDATE -eq 'UNCERTAIN' -and $_.CROSS_MODEL_SUPPORT -in @('NOT_ASSESSED','NEITHER_FLAGGED') }).Count
    $allWeakOrNone=(@($reviewRows|Where-Object REPAIR_CANDIDATE -eq 'YES').Count -eq 0 -and $weakOnly -gt 0)
    $humanOnlySignal=@($reviewRows|Where-Object { $_.ORIGINAL_COMPLEXITY -eq 'COMPLEX' -and $_.SOURCE_AMBIGUITY_FLAG -eq 'YES' -and [string]::IsNullOrWhiteSpace($_.SOURCE_EXCERPT) }).Count -gt 0
    $safeSignal=($riskType -eq 'DISCOURSE_ACTION' -and $known)
    if($reviewRows.Count -eq 0 -or -not $active -or $allWeakOrNone -or @($reviewRows|Where-Object ORIGINAL_PRIORITY -eq 'P4').Count -eq $reviewRows.Count){$route='NO_REPAIR'}
    elseif($humanOnlySignal){$route='HUMAN_ONLY'}
    elseif($safeSignal){$route='DETERMINISTIC_SAFE_CANDIDATE'}
    elseif($reviewRows.Count -eq 1 -and $reviewRows[0].ORIGINAL_COMPLEXITY -eq 'COMPLEX' -and $reviewRows[0].CROSS_MODEL_SUPPORT -eq 'BOTH_FLAGGED'){$route='ADVANCED_MODEL_CASE_REVIEW'}
    elseif($reviewRows.Count -eq 1 -and $reviewRows[0].ORIGINAL_COMPLEXITY -eq 'COMPLEX' -and $riskType -in @('PASSIVE_ACTOR_RISK','COORDINATED_PREDICATE','PROPOSITION_BOUNDARY_RISK','OBJECT_RESIDUAL_RISK')){$route='ADVANCED_MODEL_CASE_REVIEW'}
    elseif($reviewRows.Count -ge 2){$route='TEMPLATE_VALIDATION_REQUIRED'}
    elseif($reviewRows[0].ORIGINAL_COMPLEXITY -eq 'COMPLEX'){$route='ADVANCED_MODEL_CASE_REVIEW'}
    else{$route='TEMPLATE_VALIDATION_REQUIRED'}
    $actSet=@($rows.ACT|Sort-Object -Unique);$typeSet=@($rows.SOURCE_TYPE|Sort-Object -Unique)
    $repCount=0
    if($route -eq 'TEMPLATE_VALIDATION_REQUIRED'){$repCount=[Math]::Min($reviewRows.Count, $(if($actSet.Count -ge 3){2}else{1}))}
    elseif($route -eq 'ADVANCED_MODEL_CASE_REVIEW'){$repCount=$reviewRows.Count}
    $routeDescription=Get-RouteText $riskType $sig
    $familyMeta[$g.Name]=[pscustomobject]@{Route=$route;FamilySize=$rows.Count;RepresentativeCount=$repCount;Description=$routeDescription;HumanAnalogue=$known;Acts=$actSet;Types=$typeSet;Signature=$sig;Root=$rootTag}
}

# Select the minimum template validation sample: one item for one/two acts; two across three acts or source types.
$representatives=[System.Collections.Generic.List[object]]::new()
foreach($g in $groups){$meta=$familyMeta[$g.Name];$rows=@($g.Group|Where-Object HUMAN_ANALOGUE_AVAILABLE -ne 'YES'|Sort-Object ACT,RECORD_ID)
    if($meta.Route -eq 'TEMPLATE_VALIDATION_REQUIRED'){
        $take=if($meta.RepresentativeCount -ge 2){2}else{1};$chosen=[System.Collections.Generic.List[object]]::new()
        foreach($act in $meta.Acts){$candidate=@($rows|Where-Object ACT -eq $act|Select-Object -First 1);if($candidate.Count -and $chosen.Count -lt $take){[void]$chosen.Add($candidate[0])}}
        foreach($x in $rows){if($chosen.Count -ge $take){break};if(-not @($chosen|Where-Object RECORD_ID -eq $x.RECORD_ID).Count){[void]$chosen.Add($x)}}
        foreach($x in $chosen){[void]$representatives.Add($x)}
    } elseif($meta.Route -eq 'ADVANCED_MODEL_CASE_REVIEW'){foreach($x in $rows){[void]$representatives.Add($x)}}
}
$repByFamily=@{};foreach($x in $representatives){if(!$repByFamily.ContainsKey($x.REPAIR_FAMILY_ID)){$repByFamily[$x.REPAIR_FAMILY_ID]=[System.Collections.Generic.List[string]]::new()};[void]$repByFamily[$x.REPAIR_FAMILY_ID].Add($x.RECORD_ID)}

$sigOut=[System.Collections.Generic.List[object]]::new()
$familyOut=[System.Collections.Generic.List[object]]::new()
foreach($g in $groups){$meta=$familyMeta[$g.Name];$rows=@($g.Group)
    $rules=@{};foreach($x in $rows){foreach($rule in ($x.RULE_SIGNATURE -split ';')){if($rule -and $rule -ne 'NONE'){if(!$rules.ContainsKey($rule)){$rules[$rule]=0};$rules[$rule]++}}}
    $complexityDist=($rows|Group-Object ORIGINAL_COMPLEXITY|Sort-Object Name|ForEach-Object{"$($_.Name)=$($_.Count)"}) -join '; '
    $supportDist=($rows|Group-Object CROSS_MODEL_SUPPORT|Sort-Object Name|ForEach-Object{"$($_.Name)=$($_.Count)"}) -join '; '
    $humanIds=@($rows|Where-Object HUMAN_CASE_ID|ForEach-Object HUMAN_CASE_ID)
    $familyOut.Add([pscustomobject][ordered]@{
        REPAIR_FAMILY_ID=$g.Name;FAMILY_DESCRIPTION=$meta.Description;STRUCTURAL_SIGNATURE=$meta.Signature
        NUMBER_OF_RECORDS=$rows.Count;ACTS_REPRESENTED=($meta.Acts -join ';');SOURCE_TYPES_REPRESENTED=($meta.Types -join ';')
        DOMINANT_RULES=(($rules.GetEnumerator()|Sort-Object Value -Descending|Select-Object -First 6|ForEach-Object Key)-join ';')
        COMPLEXITY_DISTRIBUTION=$complexityDist;MODEL_SUPPORT_DISTRIBUTION=$supportDist
        HUMAN_ANALOGUE=if($meta.HumanAnalogue){$humanIds -join ';'}else{'NONE'};HUMAN_CONFIRMED_EXAMPLE=if($meta.HumanAnalogue){'YES'}else{'NO'}
        ONE_REPAIR_TEMPLATE_STRUCTURALLY_PLAUSIBLE=if($meta.Route -in @('DETERMINISTIC_SAFE_CANDIDATE','TEMPLATE_VALIDATION_REQUIRED')){'YES_AFTER_VALIDATION'}else{'NO'}
        ADVANCED_INTERPRETATION_REMAINS_NECESSARY=if($meta.Route -in @('ADVANCED_MODEL_CASE_REVIEW','TEMPLATE_VALIDATION_REQUIRED','HUMAN_ONLY')){'YES'}else{'NO'}
        PROPOSED_REPAIR_ROUTE=$meta.Route;REPRESENTATIVES_REQUIRED=$meta.RepresentativeCount
    })
    foreach($x in $rows){$reps=if($repByFamily.ContainsKey($g.Name)){$repByFamily[$g.Name] -join ';'}else{''};$sigOut.Add([pscustomobject][ordered]@{
        RECORD_ID=$x.RECORD_ID;ACT=$x.ACT;ORIGINAL_PRIORITY=$x.ORIGINAL_PRIORITY;ORIGINAL_COMPLEXITY=$x.ORIGINAL_COMPLEXITY;ORIGINAL_HANDLER=$x.ORIGINAL_HANDLER
        RULE_SIGNATURE=$x.RULE_SIGNATURE;STRUCTURAL_SIGNATURE=$x.STRUCTURAL_SIGNATURE;CROSS_MODEL_SUPPORT=$x.CROSS_MODEL_SUPPORT
        HUMAN_ANALOGUE_AVAILABLE=$x.HUMAN_ANALOGUE_AVAILABLE;REPAIR_FAMILY_ID=$g.Name;REPAIR_FAMILY_SIZE=$rows.Count
        PROPOSED_REPAIR_ROUTE=$meta.Route;REVIEW_QUEUE_ELIGIBILITY=if($x.HUMAN_ANALOGUE_AVAILABLE -eq 'YES'){'HUMAN_CONFIRMED_REFERENCE_NOT_QUEUED'}else{'UNADJUDICATED_REVIEW_CANDIDATE'};REPRESENTATIVE_CASE=$reps;RATIONALE=$meta.Description
        ACTOR_SPAN_PATTERN=$x.ACTOR_SPAN_PATTERN;ACTION_SPAN_PATTERN=$x.ACTION_SPAN_PATTERN;OBJECT_SPAN_PATTERN=$x.OBJECT_SPAN_PATTERN;RELATIONAL_PATTERN=$x.RELATIONAL_PATTERN
        SOURCE_TYPE=$x.SOURCE_TYPE;SOURCE_REFERENCE=$x.SOURCE_REFERENCE;CROSS_MODEL_SUPPORTED_PATTERNS=$x.CROSS_MODEL_SUPPORTED_PATTERNS;HUMAN_CASE_ID=$x.HUMAN_CASE_ID
    })}
}

$repOut=foreach($x in $representatives){$e=$extract|Where-Object EXTRACTION_ID -eq $x.RECORD_ID|Select-Object -First 1;$h=$humanA[$x.RECORD_ID];$what=Get-RouteText $x.PRIMARY_STRUCTURAL_FAMILY $x.STRUCTURAL_SIGNATURE
    [pscustomobject][ordered]@{CASE_ID=$e.CASE_ID;RECORD_ID=$e.EXTRACTION_ID;REPAIR_FAMILY_ID=$x.REPAIR_FAMILY_ID;ACT=$e.CASE_ID;SOURCE_REFERENCE=$e.SOURCE_POINTER;WHY_REPRESENTATIVE='Selected as the minimum structural validation case for its signature family; see family register for act/source coverage.';WHAT_MODEL_MUST_DECIDE=$what;HUMAN_ANALOGUE=if($h){$h.DIAGNOSTIC_ID+'; '+$h.HUMAN_DIAGNOSTIC_DEFECT_CLASS}else{'No adjudicated analogue in this family.'};CROSS_MODEL_SUPPORT=$x.CROSS_MODEL_SUPPORT;PROPOSED_MODEL='GPT-5.6 Terra High';MODEL_VARIANT_STATUS='NOT_RUN_IN_R4_2E_B0';ORIGINAL_ACTOR=$e.ACTOR_TEXT;ORIGINAL_ACTION=$e.LEGAL_ACTION;ORIGINAL_OBJECT=$e.ACTION_OBJECT;ORIGINAL_COUNTERPART=$e.COUNTERPART_TEXT;ORIGINAL_RECIPIENT=$e.RECIPIENT_TEXT;SOURCE_EXCERPT=$e.SOURCE_EXCERPT}
}

$objTriggered=@($extract|Where-Object { $candA[$_.EXTRACTION_ID].RULE_TRIGGERED -match '(^|;)OBJECT_MUST_NOT_FUNCTION_AS_RESIDUAL_BUCKET(;|$)' })
$objOut=foreach($e in $objTriggered){$c=$candA[$e.EXTRACTION_ID];$a=$aaA[$e.EXTRACTION_ID];$h=$humanA[$e.EXTRACTION_ID];$obj=[string]$e.ACTION_OBJECT;$category='UNCERTAIN'
    if(($obj -match '…|\.\.\.' -or $obj -match '\bthe Commission should charge\b') -or $obj -match '[.!?]\s+[A-Z].{0,120}\b(shall|should|may|must)\b'){$category='ADJACENT_PROPOSITION_CONTAMINATION'}
    elseif($c.RULE_TRIGGERED -match 'EXPLICIT_RELATIONAL_ACTOR_MUST_NOT_BE_DROPPED' -or ((-not $e.COUNTERPART_TEXT) -and $obj -match '\b(consult|notify|invite|inform)\b.{0,100}\b(authority|agency|person|entity|supervisor)\b')){$category='RELATIONAL_ACTOR_ABSORBED_IN_OBJECT'}
    elseif($obj -match '^[,.;:]' -and $e.LEGAL_ACTION -match '\b(also|further|however)\b'){$category='ACTION_MATERIAL_ABSORBED_IN_OBJECT'}
    elseif($obj -match '\b(without undue delay|during the preparation|throughout the Union|in the Union market|by applying|with due regard|in accordance with)\b'){$category='TEMPORAL_SPATIAL_MANNER_MATERIAL'}
    elseif($obj.Length -gt 220 -and $obj -notmatch '^[,.;:]' -and $obj -notmatch '…|\.\.\.' -and $obj -notmatch '[.!?]\s+[A-Z]'){$category='LIKELY_LEGITIMATE_COMPLEX_OBJECT'}
    [pscustomobject][ordered]@{RECORD_ID=$e.EXTRACTION_ID;ACT=$e.CASE_ID;SOURCE_TYPE=$e.SOURCE_TYPE;SOURCE_REFERENCE=$e.SOURCE_POINTER;ORIGINAL_OBJECT=$obj;ORIGINAL_ACTION=$e.LEGAL_ACTION;RULE_TRIGGERED=$c.RULE_TRIGGERED;OBJECT_TRIGGER_TYPE=$category;HUMAN_CASE_ID=if($h){$h.DIAGNOSTIC_ID}else{''};HUMAN_DIAGNOSTIC_CLASS=if($h){$h.HUMAN_DIAGNOSTIC_DEFECT_CLASS}else{''};CROSS_MODEL_SUPPORT=$c.CROSS_MODEL_STATUS;RATIONALE='Typology is a deterministic screen for review; no object was repaired or declared erroneous.'}
}

$routeCounts=@{};foreach($g in ($sigOut|Group-Object PROPOSED_REPAIR_ROUTE)){$routeCounts[$g.Name]=$g.Count}
$routeCountsFamily=@{};foreach($g in ($familyOut|Group-Object PROPOSED_REPAIR_ROUTE)){$routeCountsFamily[$g.Name]=$g.Count}
$templateFamilyCount=@($familyOut|Where-Object PROPOSED_REPAIR_ROUTE -eq 'TEMPLATE_VALIDATION_REQUIRED').Count
$advancedDirect=@($sigOut|Where-Object { $_.PROPOSED_REPAIR_ROUTE -eq 'ADVANCED_MODEL_CASE_REVIEW' -and $_.REVIEW_QUEUE_ELIGIBILITY -eq 'UNADJUDICATED_REVIEW_CANDIDATE' }).Count
$templateRepCount=@($familyOut|Where-Object PROPOSED_REPAIR_ROUTE -eq 'TEMPLATE_VALIDATION_REQUIRED'|Measure-Object REPRESENTATIVES_REQUIRED -Sum).Sum
$postAdvanced=[int]$advancedDirect+[int]$templateRepCount
$postHuman=@($sigOut|Where-Object { $_.PROPOSED_REPAIR_ROUTE -eq 'HUMAN_ONLY' -and $_.REVIEW_QUEUE_ELIGIBILITY -eq 'UNADJUDICATED_REVIEW_CANDIDATE' }).Count;$preAdvanced=524;$preHuman=364
$reduction=$preAdvanced-$postAdvanced;$reductionPct=if($preAdvanced){[math]::Round(100*$reduction/$preAdvanced,1)}else{0}
$metrics=[System.Collections.Generic.List[object]]::new()
foreach($x in @(@('PRE_COMPRESSION_ADVANCED_MODEL_LOAD',$preAdvanced),@('POST_COMPRESSION_ADVANCED_MODEL_LOAD',$postAdvanced),@('ADVANCED_MODEL_LOAD_REDUCTION',$reduction),@('ADVANCED_MODEL_LOAD_REDUCTION_PERCENT',$reductionPct),@('PRE_COMPRESSION_HUMAN_ONLY_LOAD',$preHuman),@('POST_COMPRESSION_HUMAN_ONLY_LOAD',$postHuman),@('HUMAN_ONLY_LOAD_REDUCTION',($preHuman-$postHuman)),@('TERRA_REPRESENTATIVE_CASES_PROPOSED',$representatives.Count),@('REPAIR_FAMILY_COUNT',$groups.Count),@('COUNTERPART_RECIPIENT_IDENTICAL_WHEN_POPULATED',995),@('COUNTERPART_RECIPIENT_OPERATIONAL_REDUNDANCY','OBSERVED_IN_CURRENT_EXTRACTION'),@('KNOWN_DEFECT_REDISCOVERY','9/12'))){$metrics.Add([pscustomobject]@{METRIC=$x[0];VALUE=$x[1];INTERPRETATION='Descriptive planning count; not accuracy, prevalence, or a completed repair.'})}
foreach($route in @('NO_REPAIR','DETERMINISTIC_SAFE_CANDIDATE','TEMPLATE_VALIDATION_REQUIRED','ADVANCED_MODEL_CASE_REVIEW','HUMAN_ONLY')){$metrics.Add([pscustomobject]@{METRIC='REVISED_ROUTE_COUNT';VALUE="$route=$($routeCounts[$route])";INTERPRETATION='Record-level route after structural family compression.'})}
foreach($g in ($sigOut|Where-Object ORIGINAL_HANDLER -eq 'HUMAN'|Group-Object PROPOSED_REPAIR_ROUTE)){$metrics.Add([pscustomobject]@{METRIC='PRIOR_HUMAN_HANDLER_MAPPED_TO_ROUTE';VALUE="$($g.Name)=$($g.Count)";INTERPRETATION='Descriptive disposition of the prior provisional HUMAN handler; not a human decision.'})}
$weakHuman=@($sigOut|Where-Object { $_.ORIGINAL_HANDLER -eq 'HUMAN' -and $_.REPAIR_CANDIDATE -eq 'UNCERTAIN' -and $_.CROSS_MODEL_SUPPORT -in @('NEITHER_FLAGGED','NOT_ASSESSED') -and $_.RULE_SIGNATURE -eq 'NONE' }).Count
$metrics.Add([pscustomobject]@{METRIC='PRIOR_HUMAN_WEAK_UNCERTAINTY_ONLY_PROXY';VALUE=$weakHuman;INTERPRETATION='Strict observable proxy: prior HUMAN + UNCERTAIN + no model support + no triggered rule; proxy is not a validated handler rationale.'})
foreach($g in ($familyOut|Group-Object NUMBER_OF_RECORDS|Sort-Object {[int]$_.Name})){$metrics.Add([pscustomobject]@{METRIC='FAMILY_SIZE_DISTRIBUTION';VALUE="size $($g.Name)=$($g.Count) families";INTERPRETATION='Number of families at this size.'})}

$sigOut|Export-Csv (Join-Path $b0 'R4_2E_B0_REPAIR_SIGNATURE_REGISTER.csv') -NoTypeInformation -Encoding UTF8
$familyOut|Export-Csv (Join-Path $b0 'R4_2E_B0_REPAIR_FAMILY_REGISTER.csv') -NoTypeInformation -Encoding UTF8
$repOut|Export-Csv (Join-Path $b0 'R4_2E_B0_MODEL_REPRESENTATIVE_SAMPLE.csv') -NoTypeInformation -Encoding UTF8
$objOut|Export-Csv (Join-Path $b0 'R4_2E_B0_OBJECT_TRIGGER_TYPOLOGY.csv') -NoTypeInformation -Encoding UTF8
$metrics|Export-Csv (Join-Path $b0 'R4_2E_B0_COMPRESSION_SUMMARY.csv') -NoTypeInformation -Encoding UTF8

$relMd=@'
# R4.2E-B0 — Relational field strategy

## Observed property in the frozen extraction

- Counterpart and recipient are both populated in 995 records.
- Counterpart-only: 0; recipient-only: 0.
- The populated values are identical in 995/995 jointly populated records.
- Therefore: `COUNTERPART_RECIPIENT_OPERATIONAL_REDUNDANCY = OBSERVED_IN_CURRENT_EXTRACTION` and `CURRENT_EXTRACTION_PROVIDES_ZERO_OBSERVED_FIELD_DIFFERENTIATION_BETWEEN_COUNTERPART_AND_RECIPIENT_WHEN_POPULATED`.

This is an empirical property of the current extraction, not proof that the concepts are theoretically identical. The prior flag `COUNTERPART_RECIPIENT = VARIABLE_PARSIMONY_CANDIDATE` remains in force. Neither field is deleted or merged.

## Repair-review strategy

For any future case, inspect the relational phrase once in context, then record separate explicit decisions:

1. Is there an explicit actor-capable relational entity?
2. What grammatical/legal relation does it occupy?
3. Does that relation justify counterpart?
4. Does it justify recipient?
5. Does it justify both?
6. Does it justify neither?

Do not ask an advanced model to reread the same span twice because two dataset columns exist. Preserve a field-level rationale for each separate value. No relational field is changed in B0.
'@
[IO.File]::WriteAllText((Join-Path $b0 'R4_2E_B0_RELATIONAL_FIELD_STRATEGY.md'),$relMd,(New-Object Text.UTF8Encoding($false)))

$missMd=@'
# R4.2E-B0 — Heuristic blind spots

The deterministic R4.2E-A screen rediscovered 9 of the 12 known human defects by the original model-selection family. The three missed cases remain human-confirmed and authoritative. They are not population-statistical false negatives.

## R4_2D-QA2B-026 — proposition boundary / cross-proposition contamination

The extracted actor is a complement from a preceding transfer proposition, while the relevant later proposition is the Commission's decision to revoke. The role phrase naming a third country or international organisation is itself a plausible entity and a valid prepositional phrase; no local lexical test can tell that it belongs to another proposition. The heuristic screen did not reconstruct proposition anchors across the recital span, so its visible-field tests did not assign the relational pattern family.

## R4_2D-QA2B-056 — cross-proposition contamination / embedded actor-action structure

The populated relational text names a natural or legal person, an actor-capable entity, and therefore passes a lexical actor-capability screen. The defect is that the phrase belongs to an earlier advertising-transparency proposition, not the Commission invitation proposition. Detecting it requires source-location and proposition-to-field alignment, not a rule that treats `from` or a person phrase as erroneous.

## R4_2D-QA2B-089 — multi-proposition contamination / proposition-anchor failure

The Annex VII excerpt combines distant, separately numbered provisions. The extraction's actor fragment and counterpart phrase are each grammatically plausible locally; the source-layout and provision anchor mismatch is the defect. Local role-slot heuristics can fire on action/object boundaries yet fail to rediscover the original counterpart/recipient selection family. Detecting this needs layout-aware provision segmentation and cross-field source-position alignment.

## New detection-rule candidate (not adopted)

`NEW_DETECTION_RULE_CANDIDATE = CROSS_FIELD_SOURCE_ANCHOR_ALIGNMENT_CHECK`: compare the source position/proposition containing each extracted role span with the source position/proposition containing the extracted legal predicate. This is a detection candidate motivated by all three misses; it is not added to or substituted for the 15 human-derived repair rules. It requires testing on counterexamples before adoption.

This analysis motivates family-based interpretation and portable representative context. It does not justify automatic repair or treating heuristic hits as confirmed errors.
'@
[IO.File]::WriteAllText((Join-Path $b0 'R4_2E_B0_HEURISTIC_BLIND_SPOTS.md'),$missMd,(New-Object Text.UTF8Encoding($false)))
$newRule=@([pscustomobject]@{NEW_DETECTION_RULE_CANDIDATE='CROSS_FIELD_SOURCE_ANCHOR_ALIGNMENT_CHECK';OBSERVED_CASES='R4_2D-QA2B-026;R4_2D-QA2B-056;R4_2D-QA2B-089';DESCRIPTION='Check whether actor/action/object/counterpart/recipient spans originate in the same proposition/source location as the extracted predicate.';STATUS='CANDIDATE_NOT_ADOPTED';REQUIRES='Test on positive and negative examples; retain separate model pattern and human root-cause fields.'})
$newRule|Export-Csv (Join-Path $b0 'R4_2E_B0_NEW_DETECTION_RULE_CANDIDATES.csv') -NoTypeInformation -Encoding UTF8

$familiesByRoute=($familyOut|Group-Object PROPOSED_REPAIR_ROUTE|ForEach-Object{"$($_.Name)=$($_.Count)"}) -join '; '
$sizeDist=($familyOut|Group-Object NUMBER_OF_RECORDS|Sort-Object {[int]$_.Name}|ForEach-Object{"$($_.Name) records: $($_.Count) families"}) -join '; '
$routeTable=foreach($route in @('NO_REPAIR','DETERMINISTIC_SAFE_CANDIDATE','TEMPLATE_VALIDATION_REQUIRED','ADVANCED_MODEL_CASE_REVIEW','HUMAN_ONLY')){$records=if($routeCounts.ContainsKey($route)){$routeCounts[$route]}else{0};$families=if($routeCountsFamily.ContainsKey($route)){$routeCountsFamily[$route]}else{0};"| $route | $records | $families |"}
$oldHumanTable=foreach($route in @('NO_REPAIR','DETERMINISTIC_SAFE_CANDIDATE','TEMPLATE_VALIDATION_REQUIRED','ADVANCED_MODEL_CASE_REVIEW','HUMAN_ONLY')){$n=@($sigOut|Where-Object { $_.ORIGINAL_HANDLER -eq 'HUMAN' -and $_.PROPOSED_REPAIR_ROUTE -eq $route }).Count;"| $route | $n |"}
$objDist=($objOut|Group-Object OBJECT_TRIGGER_TYPE|Sort-Object Name|ForEach-Object{"| $($_.Name) | $($_.Count) |"}) -join "`n"
$sourceHash=$frozen
$report=@'
# R4.2E-B0 — Repair strategy compression and model-cost reduction

**Status:** `R4_2E_B0_REPAIR_STRATEGY_COMPRESSED_PENDING_ADVANCED_MODEL_VALIDATION`  
**Requested model:** `GPT-5.6 Luna High`. Runtime variant was not exposed; this work is `DETERMINISTIC_CODEX_STRUCTURAL_TRIAGE`, not a claimed Luna execution. No Terra or Claude was invoked.  
**Starting state:** `R4_2E_A_CANDIDATES_IDENTIFIED_PENDING_REPAIR_STRATEGY_COMPRESSION`; input totals were checked against the prior A report.  
**Source:** frozen R4_STRUCTURAL_EXTRACTION SHA-256 `@@SOURCE_HASH@@`; 1,404 rows; input artifacts were not modified.

## Evidence boundaries

The 12 purposive human cases remain frozen diagnostic references. The A screen's 9/12 known-defect rediscovery is `KNOWN_DEFECT_NOT_REDISCOVERED_BY_HEURISTIC_TRIAGE` for cases 026, 056 and 089, not population recall. Model comparison flags cover 87 records; agreement is diagnostic support only. Structural families are deterministic planning constructs, not confirmed error clusters.

## Repair family and revised route counts

- Repair families: @@FAMILY_COUNT@@.
- Family-size distribution: @@SIZE_DISTRIBUTION@@.
- Pre-compression model route load: @@PRE_ADVANCED@@ records (the provisional Terra handler count, not an approved call list).
- Post-compression advanced model load: @@POST_ADVANCED@@ cases (individual advanced reviews plus the selected template representatives).
- Load reduction: @@LOAD_REDUCTION@@ records ( @@REDUCTION_PERCENT@@% descriptive planning reduction).
- Pre-compression human-only load: @@PRE_HUMAN@@; proposed post-compression HUMAN_ONLY load: @@POST_HUMAN@@.
- Disposition of the 364 prior provisional HUMAN assignments under the new routes:

| Proposed route | Prior HUMAN records |
|---|---:|
@@OLD_HUMAN_TABLE@@

The strict observable proxy for cases assigned HUMAN solely on weak uncertainty (prior HUMAN + `UNCERTAIN` + no model support + no triggered rule) is @@WEAK_HUMAN@@. This is only a proxy; the source did not encode a validated causal rationale for each old handler.
- Terra representative cases proposed: @@REPRESENTATIVES@@. Proposed model: GPT-5.6 Terra High. No calls were run.
- `DETERMINISTIC_SAFE_CANDIDATE` record count: @@SAFE@@; no repair was performed.

| Route | Records | Families |
|---|---:|---:|
@@ROUTE_TABLE@@

| Family size | Family count |
|---|---:|
@@SIZE_TABLE@@

Representative selection is bounded to one for a homogeneous family, two when the signature spans three acts or material source-structure variation, and never above three. Each representative row carries source excerpt and original fields so it can later be sent to Terra or handed off to the designated Claude fallback. No Claude prompt was created.

## Relational variables

The frozen extraction has both fields populated in 995 records; all 995 pairs are identical; counterpart-only = 0; recipient-only = 0. Record `COUNTERPART_RECIPIENT_OPERATIONAL_REDUNDANCY = OBSERVED_IN_CURRENT_EXTRACTION` and retain `COUNTERPART_RECIPIENT = VARIABLE_PARSIMONY_CANDIDATE`. The observation establishes zero field differentiation in this extraction, not theoretical equivalence. Review the phrase once, then make explicit counterpart and recipient decisions separately. Do not delete or merge either variable.

## Object residual-field trigger typology

The 570 `OBJECT_MUST_NOT_FUNCTION_AS_RESIDUAL_BUCKET` hits were assigned a deterministic descriptive type, not adjudicated as errors:

| Trigger type | Records |
|---|---:|
@@OBJECT_DISTRIBUTION@@

## Human-complexity and heuristic blind spots

Among the 12 known human cases, the A screen rediscovered 9 by original family. It missed 026 (adjacent proposition source anchor), 056 (plausible entity from an earlier proposition), and 089 (distant Annex VII proposition/layout anchor). The detailed explanations are in `R4_2E_B0_HEURISTIC_BLIND_SPOTS.md`. Of the human-complex cases, @@HUMAN_ONLY_SIMPLE@@ were assigned SIMPLE and @@UNDERCLASSIFIED@@ were assigned MODERATE by A; these are triage severity comparisons only.

One new detection idea is recorded, not adopted: `CROSS_FIELD_SOURCE_ANCHOR_ALIGNMENT_CHECK`. It must be tested before use and does not alter the 15 human-derived repair rules.

## No-repair declaration and firewalls

No extraction record was repaired; no actor/action/object/counterpart/recipient replacement fields were created; no original data or R4.2E-A input was edited. No Terra/Claude call was made.

- `RIT_CODING = NOT_STARTED`
- `MECHANISM_CODING = NOT_STARTED`
- `ROTEM_CODING_CONSULTED = NO`
- `R4_3 = NOT_STARTED`
- `CORPUS_WIDE_REPAIR = NOT_EXECUTED`
- `R4_2E_COMPLETE = NO`; `R4_2_COMPLETE = NO`; `READY_FOR_R4_3 = NO`.

Compression counts are a proposed workload plan, not an authorization to start advanced-model repair. Inspect the families and representative sample before the next gate.
'@
$humanOnlySimple=@(Import-Csv (Join-Path $aDir 'R4_2E_A_HUMAN_CASE_RULE_REDISCOVERY.csv') -Encoding UTF8|Where-Object COMPLEX_CASE_INCORRECTLY_SIMPLE -eq 'YES').Count
$underclassified=@(Import-Csv (Join-Path $aDir 'R4_2E_A_HUMAN_CASE_RULE_REDISCOVERY.csv') -Encoding UTF8|Where-Object UNDERCLASSIFIED_FROM_HUMAN_COMPLEX -eq 'YES').Count
$sizeTable=foreach($g in ($familyOut|Group-Object NUMBER_OF_RECORDS|Sort-Object {[int]$_.Name})){"| $($g.Name) | $($g.Count) |"}
$safeCount=if($routeCounts.ContainsKey('DETERMINISTIC_SAFE_CANDIDATE')){$routeCounts['DETERMINISTIC_SAFE_CANDIDATE']}else{0}
$report=$report.Replace('@@SOURCE_HASH@@',$sourceHash).Replace('@@FAMILY_COUNT@@',[string]$groups.Count).Replace('@@SIZE_DISTRIBUTION@@',$sizeDist).Replace('@@PRE_ADVANCED@@',[string]$preAdvanced).Replace('@@POST_ADVANCED@@',[string]$postAdvanced).Replace('@@LOAD_REDUCTION@@',[string]$reduction).Replace('@@REDUCTION_PERCENT@@',[string]$reductionPct).Replace('@@PRE_HUMAN@@',[string]$preHuman).Replace('@@POST_HUMAN@@',[string]$postHuman).Replace('@@REPRESENTATIVES@@',[string]$representatives.Count).Replace('@@SAFE@@',[string]$safeCount).Replace('@@ROUTE_TABLE@@',($routeTable -join "`n")).Replace('@@OLD_HUMAN_TABLE@@',($oldHumanTable -join "`n")).Replace('@@WEAK_HUMAN@@',[string]$weakHuman).Replace('@@SIZE_TABLE@@',($sizeTable -join "`n")).Replace('@@OBJECT_DISTRIBUTION@@',$objDist).Replace('@@HUMAN_ONLY_SIMPLE@@',[string]$humanOnlySimple).Replace('@@UNDERCLASSIFIED@@',[string]$underclassified)
[IO.File]::WriteAllText((Join-Path $b0 'R4_2E_B0_METHOD_REPORT.md'),$report,(New-Object Text.UTF8Encoding($false)))

"Rows=$($sigOut.Count); Families=$($groups.Count); Routes=$familiesByRoute; TemplateRepresentatives=$templateRepCount; DirectAdvanced=$advancedDirect; PostAdvanced=$postAdvanced; HumanOnly=$postHuman"
