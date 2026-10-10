$ErrorActionPreference = 'Stop'
$r4 = Split-Path -Parent $PSScriptRoot
$extractPath = Join-Path $r4 '03_extraction/R4_STRUCTURAL_EXTRACTION.csv'
$qa = Join-Path $r4 '03_extraction/qa'
$repair = Join-Path $qa 'repair'
$out = Join-Path $repair 'R4_2E_A'
New-Item -ItemType Directory -Path $out -Force | Out-Null

$expectedHash = '45F1C05CC9D856CB71384FCEB50EB109A0E1144CABCD7F6EAD0DC5297942C8F6'
$actualHash = (Get-FileHash -LiteralPath $extractPath -Algorithm SHA256).Hash
if ($actualHash -ne $expectedHash) { throw "Frozen extraction hash mismatch: $actualHash" }
$source = @(Import-Csv -LiteralPath $extractPath)
if ($source.Count -ne 1404) { throw "Expected 1,404 original rows; found $($source.Count)." }

$humanPath = Join-Path $repair 'R4_2D_HUMAN_DIAGNOSTIC_COMPLETED.csv'
$humanRows = @(Import-Csv -LiteralPath $humanPath)
if ($humanRows.Count -ne 12 -or @($humanRows | Where-Object HUMAN_REVIEW_STATUS -ne 'REVIEWED').Count -ne 0) { throw 'Human ground-truth file must contain exactly 12 reviewed cases.' }
$humanByExt = @{}
foreach ($h in $humanRows) { $humanByExt[$h.EXTRACTION_ID] = $h }

$terraPath = Join-Path $qa 'R4_2C_TERRA_INDEPENDENT_CALIBRATED_REVIEW_V2.csv'
$lunaTerraPath = Join-Path $qa 'R4_2C_LUNA_SELFREVIEW_TERRA_COMPARISON.csv'
$terraRows = @(Import-Csv -LiteralPath $terraPath)
$pairRows = @(Import-Csv -LiteralPath $lunaTerraPath)
$terraByExt = @{}; $qaByExt = @{}
foreach ($m in $terraRows) { $terraByExt[$m.EXTRACTION_ID] = $m; $qaByExt[$m.EXTRACTION_ID] = $m.QA_ID }
$pairByQa = @{}
foreach ($m in $pairRows) { $pairByQa[$m.QA_ID] = $m }

$ruleIds = @(
 'STRUCTURAL_EXTRACTION_MUST_PRESERVE_LEGAL_VERB','PRESERVE_LEGAL_MODALITY',
 'PRESERVE_MODAL_DEONTIC_LEXICAL_CONSTRUCTION','ALLOW_NO_EXPLICIT_ACTOR',
 'DO_NOT_INFER_ACTOR_IN_PASSIVE_CONSTRUCTION','PREPOSITION_DOES_NOT_IMPLY_RECIPIENT',
 'RELATIONAL_ENTITY_MUST_BE_ACTOR_CAPABLE','EMBEDDED_SOURCE_RELATION_MUST_NOT_BE_PROMOTED',
 'PROPOSITION_BOUNDARIES_MUST_BE_PRESERVED','COORDINATED_PREDICATES_MUST_REMAIN_DISTINCT',
 'DISCOURSE_ADVERB_IS_NOT_ACTION','TEMPORAL_SPATIAL_MANNER_MODIFIERS_ARE_NOT_CORE_ACTION_OR_OBJECT',
 'EXPLICIT_RELATIONAL_ACTOR_MUST_NOT_BE_DROPPED','OBJECT_MUST_NOT_FUNCTION_AS_RESIDUAL_BUCKET',
 'MODEL_DETECTION_PATTERN_DOES_NOT_EQUAL_HUMAN_ROOT_CAUSE'
)
$discourse = '^(also|further|furthermore|however|therefore|accordingly|in addition|likewise|moreover)[\s,;:.]*$'
$prep = '^(to|from|with|by|for|of|in|on|at|under|subject to|with regard to|with due regard to)\b'
$abstractRel = '\b(risk|rights and legitimate interests|obligations?|purpose|regard|level|conditions?|manner|costs?|information|scope|processing|tasks?|text|mechanism|measures?|advantage|standards?|territory|application|mandate|protection)\b'
$commVerb = '\b(consult|notify|invite|send|submit|communicate|inform|report|transmit|provide notice)\b'
$entityCue = '\b(authorit(?:y|ies)|supervisory authority|commission|agency|supervisor|person|individual|entity|provider|controller|processor|organisation|organization|body|institution|member states|parliament|court|board|recipient|fundamental rights agency|data protection supervisor)\b'
$modalWords = '\b(shall|should|may|must|can|cannot|is required to|are required to|has to|have to)\b'
$modifierCue = '\b(without undue delay|during the preparation|throughout the union|in the union market|in its territory|by applying|in a diligent|proportionate manner|with due regard|for the purposes of|in accordance with)\b'
$boundaryCue = '\b(the following|another|separate|subsequent|previous|paragraph|point|annex|recital|article)\b'

$register = [System.Collections.Generic.List[object]]::new()
$relAudit = [System.Collections.Generic.List[object]]::new()
$aaAudit = [System.Collections.Generic.List[object]]::new()
$rediscovery = [System.Collections.Generic.List[object]]::new()

foreach ($row in $source) {
    $hits = [System.Collections.Generic.List[string]]::new()
    $why = [System.Collections.Generic.List[string]]::new()
    $actor = [string]$row.ACTOR_TEXT; $verb = [string]$row.LEGAL_VERB; $action = [string]$row.LEGAL_ACTION
    $obj = [string]$row.ACTION_OBJECT; $cp = [string]$row.COUNTERPART_TEXT; $recip = [string]$row.RECIPIENT_TEXT
    $excerpt = [string]$row.SOURCE_EXCERPT; $all = "$actor $verb $action $obj $cp $recip $excerpt"
    $lowerAll = $all.ToLowerInvariant(); $actionTrim = $action.Trim(); $objTrim = $obj.Trim()
    $relHit = $false; $aaHit = $false; $boundaryHit = $false; $complexAnchorRisk = $false; $weakHit = $false; $strongHit = $false
    $add = { param([string]$id,[string]$reason) if (-not $hits.Contains($id)) { [void]$hits.Add($id); [void]$why.Add("$id`: $reason") } }.GetNewClosure()

    # Rule 1: lexical disagreement is a flag only when conspicuous; modality stripping is expected by schema.
    if ($actionTrim -match '\bor\s+(hear|listen|consider)\b' -or ($actionTrim -match $discourse)) {
        & $add 'STRUCTURAL_EXTRACTION_MUST_PRESERVE_LEGAL_VERB' 'action field may paraphrase or omit the source legal predicate; inspect against source.'
        $aaHit = $true; $strongHit = $true
    }
    # Rule 2: validate modality metadata against the leading modal in the extracted legal verb.
    $leadingModal = [regex]::Match($verb.Trim(), '^(shall|must|may|should)\b', 'IgnoreCase').Groups[1].Value.ToLowerInvariant()
    $expectedModality = switch ($leadingModal) { 'shall' {'MANDATORY'} 'must' {'MANDATORY'} 'may' {'PERMISSIVE'} 'should' {'OTHER'} default {''} }
    if ($expectedModality -and $row.MODALITY -and $row.MODALITY -notin @($expectedModality,'CONDITIONAL')) {
        & $add 'PRESERVE_LEGAL_MODALITY' "modal '$leadingModal' and metadata '$($row.MODALITY)' warrant a consistency check."
        $aaHit = $true; $weakHit = $true
    }
    # Rule 3: retain deontic lexical construction; flag only a detected construction split.
    if ($verb -match '\b(be entitled to|be able to|be required to|have the right to)\b' -and $action -notmatch '\b(be entitled to|be able to|be required to|have the right to)\b') {
        & $add 'PRESERVE_MODAL_DEONTIC_LEXICAL_CONSTRUCTION' 'deontic phrase in legal verb is not visibly retained in action field.'
        $aaHit = $true; $strongHit = $true
    }
    # Rules 4-5: passive/no-explicit-actor risk is contextual and never resolved by this screen.
    if ($verb -match '\b(be|is|are|was|were|been|being)\s+\w+(ed|en)\b' -and $actor -match $prep) {
        & $add 'ALLOW_NO_EXPLICIT_ACTOR' 'passive predicate and prepositional actor span require review; no agent inferred.'
        & $add 'DO_NOT_INFER_ACTOR_IN_PASSIVE_CONSTRUCTION' 'actor field may contain a complement rather than an explicit agent.'
        $aaHit = $true; $boundaryHit = $true; $complexAnchorRisk = $true
    }
    # Rules 6-8: prepositional presence is only a triage signal; entity-capability remains contextual.
    foreach ($slot in @(@('counterpart',$cp),@('recipient',$recip))) {
        if ($slot[1] -and $slot[1].Trim() -match $prep) {
            $relComplement = $slot[1] -replace $prep,' '
            if ($relComplement -notmatch $entityCue) {
                & $add 'PREPOSITION_DOES_NOT_IMPLY_RECIPIENT' "$($slot[0]) begins with a preposition and lacks a clear entity cue; review the syntactic relation, not the preposition alone."
                $relHit = $true; $weakHit = $true
            }
            if ($relComplement -match $abstractRel) {
                & $add 'RELATIONAL_ENTITY_MUST_BE_ACTOR_CAPABLE' "$($slot[0]) value contains an abstract complement cue; entity status needs contextual review."
                $relHit = $true; $strongHit = $true
            }
            if ($slot[1] -match '^from\b' -and $lowerAll -match '\b(mandate|received from|source of|provided by)\b') {
                & $add 'EMBEDDED_SOURCE_RELATION_MUST_NOT_BE_PROMOTED' 'source/mandate language may be embedded rather than matrix-level relation.'
                $relHit = $true; $boundaryHit = $true
            }
        }
    }
    # Rule 9: use existing ambiguity flags and visibly long/multi-clause spans as review candidates.
    if ($objTrim -match '^[,.;:]' -or $obj -match '…|\.\.\.' -or $obj -match '\bthe Commission should charge\b|\bthe Commission may charge\b') {
        & $add 'PROPOSITION_BOUNDARIES_MUST_BE_PRESERVED' 'extracted object begins at a clause boundary, contains an ellipsis, or visibly crosses into a distinct proposition.'
        $boundaryHit = $true; $weakHit = $true
        if ($obj -match '…|\.\.\.' -or $obj -match '\bthe Commission should charge\b|\bthe Commission may charge\b') { $complexAnchorRisk = $true }
    }
    if ($actor.Length -gt 55 -and $actor -match '\b(where|which|that)\b' -and $verb -match '\b(should be able to|shall be entitled to|may be able to)\b' -and $obj -match '\b(by applying|in the .{1,35} market)\b') {
        & $add 'PROPOSITION_BOUNDARIES_MUST_BE_PRESERVED' 'long relative-clause actor span and deontic predicate/means complement suggest a possible sub-proposition anchor mismatch.'
        $boundaryHit = $true; $complexAnchorRisk = $true; $aaHit = $true
    }
    # Rule 10: coordinated predicate indicators, not a determination that coordination is erroneous.
    if (($verb + ' ' + $action + ' ' + $obj) -match '\b(shall|should|may|must)\b.{0,180}\b(and|or)\b.{0,100}\b(shall|should|may|must|be subject to|be considered)\b' -or
        ($obj + ' ' + $cp + ' ' + $recip) -match '\b(to the obligations of|subject to the obligations|shall be subject to)\b') {
        & $add 'COORDINATED_PREDICATES_MUST_REMAIN_DISTINCT' 'multiple-predicate or coordinated-consequence wording may be conflated.'
        $boundaryHit = $true; $complexAnchorRisk = $true; $aaHit = $true
    }
    # Rule 11: an action field made only of discourse text is a strong local signal.
    if ($actionTrim -match $discourse) {
        & $add 'DISCOURSE_ADVERB_IS_NOT_ACTION' 'action consists only of a discourse marker.'
        $aaHit = $true; $strongHit = $true
    }
    # Rule 12: modifiers in the object span are review candidates, not automatic errors.
    if ($objTrim -match '^[,.;:]' -or $obj -match '\b(without undue delay|during the preparation|throughout the Union|in the Union market|with due regard)\b') {
        & $add 'TEMPORAL_SPATIAL_MANNER_MODIFIERS_ARE_NOT_CORE_ACTION_OR_OBJECT' 'object span includes a punctuation-leading or temporal/spatial/manner cue.'
        $aaHit = $true; $weakHit = $true
    }
    # Rule 13: communication predicate with a named entity and empty relation slots.
    if ($excerpt -match $commVerb -and $excerpt -match $entityCue -and ((-not $cp) -or (-not $recip))) {
        & $add 'EXPLICIT_RELATIONAL_ACTOR_MUST_NOT_BE_DROPPED' 'communication predicate and entity cue coexist with a blank counterpart/recipient field.'
        $relHit = $true; $aaHit = $true; $strongHit = $true
    }
    # Rule 14: residual object signals are conservative and never create replacement fields.
    if ($objTrim -match '^[,.;:]' -or $obj -match '…|\.\.\.' -or ($obj -match '\b(shall|should|may|must)\b' -and $obj -match '[.!?]\s+[A-Z]') -or $obj -match '\bthe Commission should charge\b') {
        & $add 'OBJECT_MUST_NOT_FUNCTION_AS_RESIDUAL_BUCKET' 'object contains a long or clause-boundary/predicate signal.'
        $boundaryHit = $true; $aaHit = $true; $weakHit = $true
        if ($obj -match '…|\.\.\.' -or (($obj -match '\b(shall|should|may|must)\b') -and $obj -match '[.!?]\s+[A-Z]') -or $obj -match '\bthe Commission should charge\b') { $complexAnchorRisk = $true }
    }
    # Rule 15 is an interpretation firewall, not a lexical detector. Preserve evidence dimensions separately.

    $human = $humanByExt[$row.EXTRACTION_ID]
    $terra = $terraByExt[$row.EXTRACTION_ID]
    $qaId = if ($terra) { $terra.QA_ID } else { $null }
    $pair = if ($qaId) { $pairByQa[$qaId] } else { $null }
    $lunaFlag = if ($pair) { $pair.LUNA_SELFREVIEW_ANY_ERROR } else { 'NOT_ASSESSED' }
    $terraFlag = if ($pair) { $pair.TERRA_ANY_ERROR } else { 'NOT_ASSESSED' }
    $cross = if (-not $pair) { 'NOT_ASSESSED' } elseif ($lunaFlag -eq 'YES' -and $terraFlag -eq 'YES') { 'BOTH_FLAGGED' } elseif ($lunaFlag -eq 'YES') { 'LUNA_ONLY' } elseif ($terraFlag -eq 'YES') { 'TERRA_ONLY' } else { 'NEITHER_FLAGGED' }
    $modelPattern = if ($human) { $human.PATTERN } else { 'NOT_ASSIGNED_IN_SOURCE' }
    $supportedPatterns = if ($pair -and $pair.SYSTEMATIC_PATTERN_SUPPORT) { $pair.SYSTEMATIC_PATTERN_SUPPORT } else { 'NOT_ASSESSED' }
    $knownHuman = [bool]$human

    $familyList = [System.Collections.Generic.List[string]]::new()
    if ($relHit) { [void]$familyList.Add('RELATIONAL_ROLE_ASSIGNMENT_RISK') }
    if ($aaHit) { [void]$familyList.Add('ACTOR_ACTION_SEGMENTATION_RISK') }
    if ($boundaryHit) { [void]$familyList.Add('PROPOSITION_BOUNDARY_OR_SPAN_RISK') }
    if ($familyList.Count -gt 1) { $family = 'MULTIPLE_STRUCTURAL_RISKS' } elseif ($familyList.Count -eq 1) { $family = $familyList[0] } else { $family = 'NO_RULE_SIGNAL' }

    $specificHits = @($hits | Where-Object { $_ -notin @('PREPOSITION_DOES_NOT_IMPLY_RECIPIENT','TEMPORAL_SPATIAL_MANNER_MODIFIERS_ARE_NOT_CORE_ACTION_OR_OBJECT') }).Count
    if ($complexAnchorRisk -or ($cross -eq 'BOTH_FLAGGED' -and $specificHits -ge 3)) { $complexity='COMPLEX' }
    elseif ($hits.Count -eq 0 -and $cross -in @('NOT_ASSESSED','NEITHER_FLAGGED')) { $complexity='NONE' }
    elseif ($specificHits -eq 1 -and ($hits -contains 'DISCOURSE_ADVERB_IS_NOT_ACTION' -or $hits -contains 'RELATIONAL_ENTITY_MUST_BE_ACTOR_CAPABLE')) { $complexity='SIMPLE' }
    else { $complexity='MODERATE' }
    if ($knownHuman) {
        $candidate = 'YES'; $eligibility = 'ALREADY_HUMAN_ADJUDICATED'; $handler = 'NONE'; $confidence = 'HUMAN_GROUND_TRUTH'
    } elseif ($hits.Count -eq 0) {
        if ($cross -eq 'BOTH_FLAGGED' -or $cross -eq 'LUNA_ONLY' -or $cross -eq 'TERRA_ONLY') { $candidate='UNCERTAIN'; $confidence='LOW'; $complexity='MODERATE'; $eligibility='TERRA_REPAIR_REQUIRED'; $handler='TERRA_HIGH' }
        else { $candidate='NO'; $confidence='LOW'; $complexity='NONE'; $eligibility='NO_REPAIR_NEEDED'; $handler='NONE' }
    } else {
        $candidate = if ($strongHit -or $specificHits -ge 2 -or ($cross -eq 'BOTH_FLAGGED' -and $specificHits -ge 1)) { 'YES' } else { 'UNCERTAIN' }
        $confidence = if ($strongHit -and $hits.Count -ge 2) { 'MEDIUM' } else { 'LOW' }
        if ($candidate -eq 'NO') { $eligibility='NO_REPAIR_NEEDED'; $handler='NONE' }
        elseif ($complexity -eq 'SIMPLE') { $eligibility='RULE_GUIDED_REPAIR_CANDIDATE'; $handler='DETERMINISTIC_RULE' }
        elseif ($complexity -eq 'COMPLEX' -and ($cross -eq 'BOTH_FLAGGED' -or $row.STRUCTURAL_AMBIGUITY -eq 'YES')) { $eligibility='HUMAN_REVIEW_REQUIRED'; $handler='HUMAN' }
        else { $eligibility='TERRA_REPAIR_REQUIRED'; $handler='TERRA_HIGH' }
    }
    if ($knownHuman) { $priority='P1' }
    elseif ($cross -eq 'BOTH_FLAGGED' -and $strongHit -and $complexity -in @('MODERATE','COMPLEX')) { $priority='P1' }
    elseif ((($cross -in @('BOTH_FLAGGED','LUNA_ONLY','TERRA_ONLY')) -and $strongHit) -or $specificHits -ge 2) { $priority='P2' }
    elseif ($hits.Count -eq 1) { $priority='P3' }
    else { $priority='P4' }
    if ($cross -eq 'BOTH_FLAGGED' -and -not $knownHuman -and $priority -ne 'P1') { $priority='P2' }
    $rationale = if ($hits.Count) { ($why -join ' || ') + ' Heuristic hit = review candidate only, not confirmed error.' } elseif ($cross -ne 'NOT_ASSESSED' -and $cross -ne 'NEITHER_FLAGGED') { 'Model review flag exists, but no current candidate-rule trigger; retain for comparative review, not as confirmed defect.' } else { 'No current deterministic candidate-rule signal detected; this is not proof of extraction correctness.' }

    $register.Add([pscustomobject][ordered]@{
        RECORD_ID=$row.EXTRACTION_ID; ACT=$row.CASE_ID; SOURCE_TYPE=$row.SOURCE_TYPE; SOURCE_REFERENCE=$row.SOURCE_POINTER
        ORIGINAL_ACTOR=$actor; ORIGINAL_ACTION=$action; ORIGINAL_OBJECT=$obj; ORIGINAL_COUNTERPART=$cp; ORIGINAL_RECIPIENT=$recip
        RULE_TRIGGERED=if($hits.Count){$hits -join ';'}else{'NONE'}; NUMBER_OF_RULE_TRIGGERS=$hits.Count
        CANDIDATE_DEFECT_FAMILY=$family; REPAIR_CANDIDATE=$candidate; REPAIR_COMPLEXITY=$complexity
        REPAIR_ELIGIBILITY=$eligibility; RECOMMENDED_NEXT_HANDLER=$handler; CANDIDATE_CONFIDENCE=$confidence
        RATIONALE=$rationale; HUMAN_GROUND_TRUTH_AVAILABLE=if($knownHuman){'YES'}else{'NO'}
        HUMAN_CASE_ID=if($knownHuman){$human.DIAGNOSTIC_ID}else{''}; MODEL_PROVENANCE=$row.EXTRACTION_MODEL
        MODEL_SELECTION_PATTERN=$modelPattern; CROSS_MODEL_SUPPORTED_PATTERNS=$supportedPatterns
        SOURCE_AMBIGUITY_FLAG=$row.STRUCTURAL_AMBIGUITY
        HUMAN_DIAGNOSTIC_DEFECT_CLASS=if($knownHuman){$human.HUMAN_DIAGNOSTIC_DEFECT_CLASS}else{''}
        LUNA_SELFREVIEW_FLAG=$lunaFlag; TERRA_V2_FLAG=$terraFlag; CROSS_MODEL_STATUS=$cross; PRIORITY=$priority
    })
    $relRuleIds = @('PREPOSITION_DOES_NOT_IMPLY_RECIPIENT','RELATIONAL_ENTITY_MUST_BE_ACTOR_CAPABLE','EMBEDDED_SOURCE_RELATION_MUST_NOT_BE_PROMOTED','EXPLICIT_RELATIONAL_ACTOR_MUST_NOT_BE_DROPPED')
    $aaRuleIds = @('STRUCTURAL_EXTRACTION_MUST_PRESERVE_LEGAL_VERB','PRESERVE_LEGAL_MODALITY','PRESERVE_MODAL_DEONTIC_LEXICAL_CONSTRUCTION','ALLOW_NO_EXPLICIT_ACTOR','DO_NOT_INFER_ACTOR_IN_PASSIVE_CONSTRUCTION','PROPOSITION_BOUNDARIES_MUST_BE_PRESERVED','COORDINATED_PREDICATES_MUST_REMAIN_DISTINCT','DISCOURSE_ADVERB_IS_NOT_ACTION','TEMPORAL_SPATIAL_MANNER_MODIFIERS_ARE_NOT_CORE_ACTION_OR_OBJECT','EXPLICIT_RELATIONAL_ACTOR_MUST_NOT_BE_DROPPED','OBJECT_MUST_NOT_FUNCTION_AS_RESIDUAL_BUCKET')
    $relTriggered = @($hits | Where-Object { $_ -in $relRuleIds }).Count -gt 0
    $aaTriggered = @($hits | Where-Object { $_ -in $aaRuleIds }).Count -gt 0
    $relAudit.Add([pscustomobject][ordered]@{RECORD_ID=$row.EXTRACTION_ID;ACT=$row.CASE_ID;COUNTERPART_POPULATED=[bool]$cp;RECIPIENT_POPULATED=[bool]$recip;BOTH_POPULATED=([bool]$cp -and [bool]$recip);VALUES_IDENTICAL=([bool]$cp -and [bool]$recip -and $cp.Trim() -ceq $recip.Trim());COUNTERPART_ONLY=([bool]$cp -and -not $recip);RECIPIENT_ONLY=([bool]$recip -and -not $cp);HUMAN_DERIVED_RELATIONAL_RULE_TRIGGER=$relTriggered;RULE_TRIGGERED=($hits -join ';');LUNA_SELFREVIEW_FLAG=$lunaFlag;TERRA_V2_FLAG=$terraFlag;CROSS_MODEL_STATUS=$cross;HUMAN_GROUND_TRUTH_AVAILABLE=if($knownHuman){'YES'}else{'NO'}})
    $aaAudit.Add([pscustomobject][ordered]@{RECORD_ID=$row.EXTRACTION_ID;ACT=$row.CASE_ID;ACTOR_SPAN_TRUNCATION_CANDIDATE=($actor -match '^and considering that|^\w+ or other third-party$');ACTOR_COMPLEMENT_CANDIDATE=($actor -match $prep);MISSING_MODAL_CANDIDATE=($hits -contains 'PRESERVE_LEGAL_MODALITY');PREDICATE_FRAGMENTATION_CANDIDATE=($hits -contains 'STRUCTURAL_EXTRACTION_MUST_PRESERVE_LEGAL_VERB' -or $hits -contains 'DISCOURSE_ADVERB_IS_NOT_ACTION');DISCOURSE_ONLY_ACTION=($actionTrim -match $discourse);PASSIVE_NO_EXPLICIT_ACTOR_CANDIDATE=($hits -contains 'DO_NOT_INFER_ACTOR_IN_PASSIVE_CONSTRUCTION');PROPOSITION_BOUNDARY_CONTAMINATION_CANDIDATE=($hits -contains 'PROPOSITION_BOUNDARIES_MUST_BE_PRESERVED');COORDINATED_PREDICATE_CANDIDATE=($hits -contains 'COORDINATED_PREDICATES_MUST_REMAIN_DISTINCT');RULE_TRIGGERED=($hits -join ';');REPAIR_CANDIDATE=$candidate;REPAIR_COMPLEXITY=$complexity;HUMAN_GROUND_TRUTH_AVAILABLE=if($knownHuman){'YES'}else{'NO'};LUNA_SELFREVIEW_FLAG=$lunaFlag;TERRA_V2_FLAG=$terraFlag})
    if ($knownHuman) {
        $isRole = $human.PATTERN -eq 'COUNTERPART_RECIPIENT_OVERATTRIBUTION'
        $recovered = if ($isRole) { $relTriggered } else { $aaTriggered }
        $complexClasses = 'PROPOSITION_BOUNDARY_FAILURE|CROSS_PROPOSITION_CONTAMINATION|MULTI_PROPOSITION_CONTAMINATION|CROSS_SENTENCE_CONTAMINATION|EMBEDDED_ACTOR_ACTION_STRUCTURE|PASSIVE_ACTOR_INVENTION|COORDINATED_PROPOSITION_CONFLATION|OBJECT_SPAN_MISALLOCATION|PROPOSITION_ANCHOR_FAILURE'
        $humanComplexityBenchmark = if($human.HUMAN_DIAGNOSTIC_DEFECT_CLASS -match $complexClasses){'COMPLEX'}else{'SIMPLE_OR_MODERATE'}
        $assignedDefensible = if($humanComplexityBenchmark -eq 'COMPLEX'){$complexity -eq 'COMPLEX'}else{$complexity -in @('SIMPLE','MODERATE')}
        $rediscovery.Add([pscustomobject][ordered]@{HUMAN_CASE_ID=$human.DIAGNOSTIC_ID;RECORD_ID=$row.EXTRACTION_ID;ORIGINAL_PATTERN=$human.PATTERN;HUMAN_DIAGNOSTIC_CLASS=$human.HUMAN_DIAGNOSTIC_DEFECT_CLASS;TRIGGERED_CANDIDATE_RULES=($hits -join ';');KNOWN_DEFECT_REDISCOVERED=if($recovered){'YES'}else{'NO'};HUMAN_COMPLEXITY_BENCHMARK=$humanComplexityBenchmark;ASSIGNED_COMPLEXITY=$complexity;COMPLEXITY_DEFENSIBLE=if($assignedDefensible){'YES'}else{'NO'};UNDERCLASSIFIED_FROM_HUMAN_COMPLEX=if($humanComplexityBenchmark -eq 'COMPLEX' -and $complexity -ne 'COMPLEX'){'YES'}else{'NO'};COMPLEX_CASE_INCORRECTLY_SIMPLE=if($humanComplexityBenchmark -eq 'COMPLEX' -and $complexity -eq 'SIMPLE'){'YES'}else{'NO'};RECOMMENDED_NEXT_HANDLER=$handler;MODEL_SELECTION_PATTERN=$modelPattern;LUNA_SELFREVIEW_FLAG=$lunaFlag;TERRA_V2_FLAG=$terraFlag})
    }
}

$registerPath=Join-Path $out 'R4_2E_A_REPAIR_CANDIDATE_REGISTER.csv'
$rediscoveryPath=Join-Path $out 'R4_2E_A_HUMAN_CASE_RULE_REDISCOVERY.csv'
$relPath=Join-Path $out 'R4_2E_A_COUNTERPART_RECIPIENT_BURDEN_AUDIT.csv'
$aaPath=Join-Path $out 'R4_2E_A_ACTOR_ACTION_REPAIR_AUDIT.csv'
$summaryPath=Join-Path $out 'R4_2E_A_REPAIR_CANDIDATE_SUMMARY.csv'
$newRulesPath=Join-Path $out 'R4_2E_A_NEW_RULE_CANDIDATES.csv'
$register | Export-Csv -LiteralPath $registerPath -NoTypeInformation -Encoding UTF8
$rediscovery | Export-Csv -LiteralPath $rediscoveryPath -NoTypeInformation -Encoding UTF8
$relAudit | Export-Csv -LiteralPath $relPath -NoTypeInformation -Encoding UTF8
$aaAudit | Export-Csv -LiteralPath $aaPath -NoTypeInformation -Encoding UTF8

$summary = [System.Collections.Generic.List[object]]::new()
$addSummary = { param($dimension,$value,$count) $summary.Add([pscustomobject]@{SUMMARY_DIMENSION=$dimension;SUMMARY_VALUE=$value;COUNT=$count}) }.GetNewClosure()
foreach ($dim in @(@('ACT','ACT'),@('REPAIR_CANDIDATE','REPAIR_CANDIDATE'),@('REPAIR_COMPLEXITY','REPAIR_COMPLEXITY'),@('REPAIR_ELIGIBILITY','REPAIR_ELIGIBILITY'),@('RECOMMENDED_NEXT_HANDLER','RECOMMENDED_NEXT_HANDLER'),@('PRIORITY','PRIORITY'),@('CANDIDATE_DEFECT_FAMILY','CANDIDATE_DEFECT_FAMILY'))) {
    foreach($g in ($register | Group-Object -Property $dim[1] | Sort-Object Name)){ & $addSummary $dim[0] $g.Name $g.Count }
}
$ruleCounts=@{}; foreach($r in $register){foreach($id in ($r.RULE_TRIGGERED -split ';')){if($id -and $id -ne 'NONE'){if(!$ruleCounts.ContainsKey($id)){$ruleCounts[$id]=0};$ruleCounts[$id]++}}}
foreach($id in $ruleIds){$n=if($ruleCounts.ContainsKey($id)){$ruleCounts[$id]}else{0};&$addSummary 'RULE_TRIGGERED' $id $n}
foreach($act in @('D1_GDPR','D2_DSA','D3_AI_ACT')){
    $actRows=@($register|Where-Object ACT -eq $act)
    foreach($dimension in @('REPAIR_CANDIDATE','REPAIR_COMPLEXITY','REPAIR_ELIGIBILITY','RECOMMENDED_NEXT_HANDLER','PRIORITY','CANDIDATE_DEFECT_FAMILY')){foreach($g in ($actRows|Group-Object -Property $dimension)){&$addSummary "ACT:$act/$dimension" $g.Name $g.Count}}
    foreach($rule in $ruleIds){$n=@($actRows|Where-Object { $_.RULE_TRIGGERED -split ';' -contains $rule }).Count;&$addSummary "ACT:$act/RULE_TRIGGERED" $rule $n}
}
foreach($g in ($register|Group-Object MODEL_SELECTION_PATTERN)){&$addSummary 'MODEL_SELECTION_PATTERN' $g.Name $g.Count}
$summary | Export-Csv -LiteralPath $summaryPath -NoTypeInformation -Encoding UTF8
$newRules = @([pscustomobject]@{NEW_REPAIR_RULE_CANDIDATE='';OBSERVED_SIGNAL='';SOURCE_RECORDS='';RATIONALE='';STATUS='NO_NEW_RULE_FORMALLY_PROPOSED_IN_HEURISTIC_SCREEN'})
# Header-only file: a single explicit status row prevents an unsubstantiated claim of a new rule.
$newRules | Export-Csv -LiteralPath $newRulesPath -NoTypeInformation -Encoding UTF8

$total=$register.Count
$candidateCounts=@{};foreach($g in ($register|Group-Object REPAIR_CANDIDATE)){$candidateCounts[$g.Name]=$g.Count}
$complexityCounts=@{};foreach($g in ($register|Group-Object REPAIR_COMPLEXITY)){$complexityCounts[$g.Name]=$g.Count}
$handlerCounts=@{};foreach($g in ($register|Group-Object RECOMMENDED_NEXT_HANDLER)){$handlerCounts[$g.Name]=$g.Count}
$priorityCounts=@{};foreach($g in ($register|Group-Object PRIORITY)){$priorityCounts[$g.Name]=$g.Count}
$rediscovered=@($rediscovery|Where-Object KNOWN_DEFECT_REDISCOVERED -eq 'YES').Count
$both=@($register|Where-Object CROSS_MODEL_STATUS -eq 'BOTH_FLAGGED').Count
$lunaOnly=@($register|Where-Object CROSS_MODEL_STATUS -eq 'LUNA_ONLY').Count
$terraOnly=@($register|Where-Object CROSS_MODEL_STATUS -eq 'TERRA_ONLY').Count
$noneModel=@($register|Where-Object CROSS_MODEL_STATUS -eq 'NEITHER_FLAGGED').Count
$notAssessed=@($register|Where-Object CROSS_MODEL_STATUS -eq 'NOT_ASSESSED').Count
$cpN=@($relAudit|Where-Object COUNTERPART_POPULATED).Count; $recN=@($relAudit|Where-Object RECIPIENT_POPULATED).Count
$bothN=@($relAudit|Where-Object BOTH_POPULATED).Count; $identN=@($relAudit|Where-Object VALUES_IDENTICAL).Count
$cpOnly=@($relAudit|Where-Object COUNTERPART_ONLY).Count; $recOnly=@($relAudit|Where-Object RECIPIENT_ONLY).Count
$relTriggeredN=@($relAudit|Where-Object HUMAN_DERIVED_RELATIONAL_RULE_TRIGGER).Count
$distByAct=foreach($act in @('D1_GDPR','D2_DSA','D3_AI_ACT')){ $ar=@($relAudit|Where-Object ACT -eq $act); "| $act | $($ar.Count) | $(@($ar|? COUNTERPART_POPULATED).Count) | $(@($ar|? RECIPIENT_POPULATED).Count) | $(@($ar|? VALUES_IDENTICAL).Count) | $(@($ar|? HUMAN_DERIVED_RELATIONAL_RULE_TRIGGER).Count) |" }
$topRules=foreach($id in ($ruleCounts.Keys|Sort-Object {-$ruleCounts[$_]}|Select-Object -First 10)){"| $id | $($ruleCounts[$id]) |"}
$hashRows=@($registerPath,$rediscoveryPath,$relPath,$aaPath,$summaryPath,$newRulesPath|ForEach-Object{Get-FileHash -LiteralPath $_ -Algorithm SHA256})
$hashTable=foreach($h in $hashRows){"| $([IO.Path]::GetFileName($h.Path)) | $($h.Hash) |"}
$report=@'
# R4.2E-A — Controlled structural repair candidate identification

**Status:** `R4_2E_A_REPAIR_CANDIDATES_IDENTIFIED_PENDING_TERRA_REPAIR`  
**Starting checkpoint:** `R4_2D_FROZEN_READY_FOR_R4_2E_A` (the preceding R4.2D record remains preserved).  
**Execution provenance:** requested model `GPT-5.6 Luna High`; this Codex runtime cannot independently expose or verify that model variant. Detection below is deterministic heuristic triage, not a model repair run.  
**Scope:** identification before repair. The original 1,404-row extraction was verified against its freeze SHA-256 and was not modified.

## Three evidence layers kept separate

- **Human evidence:** 12 purposively selected, adjudicated R4.2D cases. They are frozen references, not a later independent validation sample.
- **Cross-model evidence:** paired Luna self-review and independent Terra V2 records. The source comparisons cover a subset only; uncovered records are `NOT_ASSESSED`. Agreement is supporting evidence, not ground truth.
- **Rule-based detection:** deterministic review triggers applied across all 1,404 rows. A trigger means `CANDIDATE_FOR_REVIEW`, never `ERROR_CONFIRMED`. No corpus accuracy or prevalence rate is estimated.

## Candidate disposition

| Repair candidate | Records |
|---|---:|
| YES | @@YES@@ |
| NO | @@NO@@ |
| UNCERTAIN | @@UNCERTAIN@@ |

| Complexity | Records |
|---|---:|
| NONE | @@NONE@@ |
| SIMPLE | @@SIMPLE@@ |
| MODERATE | @@MODERATE@@ |
| COMPLEX | @@COMPLEX@@ |

| Recommended handler | Records |
|---|---:|
| NONE | @@HANDLER_NONE@@ |
| DETERMINISTIC_RULE | @@HANDLER_RULE@@ |
| TERRA_HIGH | @@HANDLER_TERRA@@ |
| HUMAN | @@HANDLER_HUMAN@@ |

| Priority | Records |
|---|---:|
| P1 | @@P1@@ |
| P2 | @@P2@@ |
| P3 | @@P3@@ |
| P4 | @@P4@@ |

Top rule-trigger counts (non-exclusive heuristic hits):

| Rule | Rows |
|---|---:|
@@TOP_RULES@@

Candidate dispositions by act are in the summary CSV. These figures describe triage outputs only and are not error-rate estimates.

| Act | Total records | YES | UNCERTAIN | NO |
|---|---:|---:|---:|---:|
@@CANDIDATES_BY_ACT@@

## Human-case known-defect rediscovery

- Rediscovered: @@REDISCOVERED@@ / 12 known human-adjudicated defects (`KNOWN_DEFECT_REDISCOVERY`; not population recall).
- A missed known defect means the fixed deterministic trigger mapping did not match its original model-selection family; it does not negate the human adjudication.
- False simplifications: @@FALSE_SIMPLIFICATIONS@@ case(s) assigned SIMPLE despite a human-known complex class.
- Other underclassifications: @@UNDERCLASSIFICATIONS@@ human-complex case(s) assigned MODERATE.
- Complex cases incorrectly assigned SIMPLE: @@COMPLEX_SIMPLE@@.
- Missed known-defect cases: @@MISSED_CASES@@.
- Per-case triggers, complexity defensibility and handler are in `R4_2E_A_HUMAN_CASE_RULE_REDISCOVERY.csv`.

## Cross-model evidence coverage

- Both flagged: @@BOTH@@; Luna only: @@LUNA_ONLY@@; Terra only: @@TERRA_ONLY@@; neither flagged: @@NEITHER@@; not assessed in paired model comparison: @@NOT_ASSESSED@@.
- Only the records present in the paired comparison are assigned model flags. Flags are not used as human truth.

## Counterpart/recipient burden audit

- Counterpart populated: @@CP@@ / 1,404.
- Recipient populated: @@REC@@ / 1,404.
- Both populated: @@BOTH_POP@@; values identical: @@IDENTICAL@@; counterpart only: @@CP_ONLY@@; recipient only: @@REC_ONLY@@.
- At least one human-derived relational heuristic triggered: @@REL_TRIGGERED@@ records.

| Act | Records | Counterpart populated | Recipient populated | Identical values | Relational rule trigger |
|---|---:|---:|---:|---:|---:|
@@ACT_REL@@

This audit informs later parsimony analysis only. No variable was deleted, merged, or redefined.

## Actor/action candidate audit

The row-level audit flags possible actor truncation/complement assignment, modality metadata mismatch, predicate fragmentation, discourse-only action, passive/no-explicit-actor risk, proposition-boundary risk, and coordinated predicates. It contains candidate indicators only; the fields themselves were not changed.

| Indicator | Records |
|---|---:|
@@ACTOR_ACTION_INDICATORS@@

## Rule governance and new rules

All 15 human-derived rule IDs were kept intact. `MODEL_DETECTION_PATTERN_DOES_NOT_EQUAL_HUMAN_ROOT_CAUSE` was applied as an interpretation firewall by retaining separate `MODEL_SELECTION_PATTERN` and `HUMAN_DIAGNOSTIC_DEFECT_CLASS` columns; it is not a lexical trigger. The screen produced no separately adjudicated new rule. `R4_2E_A_NEW_RULE_CANDIDATES.csv` records that no new rule is formally proposed in this heuristic screen; investigate emerging signals during human/Terra review rather than silently expanding the rule set.

## No-repair declaration and firewalls

No `REPAIRED_*` columns were created. No record values were corrected, no 1,404-row extraction was regenerated, and no automatic repair was run. The original Luna extraction, source corpus and model QA artifacts remain frozen.

- `RIT_CODING = NOT_STARTED`
- `MECHANISM_CODING = NOT_STARTED`
- `ROTEM_CODING_CONSULTED = NO`
- `R4_3 = NOT_STARTED`
- `CORPUS_WIDE_REPAIR = NOT_EXECUTED`
- `R4_2E_COMPLETE = NO`; `R4_2_COMPLETE = NO`.

## Output integrity

| Output | SHA-256 |
|---|---|
@@HASHES@@

Next stage remains pending Terra repair/review; this report does not authorize or initiate that phase.
'@
$report = $report.Replace('@@YES@@',[string]$candidateCounts['YES']).Replace('@@NO@@',[string]$candidateCounts['NO']).Replace('@@UNCERTAIN@@',[string]$candidateCounts['UNCERTAIN'])
$report = $report.Replace('@@NONE@@',[string]$complexityCounts['NONE']).Replace('@@SIMPLE@@',[string]$complexityCounts['SIMPLE']).Replace('@@MODERATE@@',[string]$complexityCounts['MODERATE']).Replace('@@COMPLEX@@',[string]$complexityCounts['COMPLEX'])
$handlerNone=if($handlerCounts.ContainsKey('NONE')){$handlerCounts['NONE']}else{0};$handlerRule=if($handlerCounts.ContainsKey('DETERMINISTIC_RULE')){$handlerCounts['DETERMINISTIC_RULE']}else{0};$handlerTerra=if($handlerCounts.ContainsKey('TERRA_HIGH')){$handlerCounts['TERRA_HIGH']}else{0};$handlerHuman=if($handlerCounts.ContainsKey('HUMAN')){$handlerCounts['HUMAN']}else{0}
$report = $report.Replace('@@HANDLER_NONE@@',[string]$handlerNone).Replace('@@HANDLER_RULE@@',[string]$handlerRule).Replace('@@HANDLER_TERRA@@',[string]$handlerTerra).Replace('@@HANDLER_HUMAN@@',[string]$handlerHuman)
$report = $report.Replace('@@P1@@',[string]$priorityCounts['P1']).Replace('@@P2@@',[string]$priorityCounts['P2']).Replace('@@P3@@',[string]$priorityCounts['P3']).Replace('@@P4@@',[string]$priorityCounts['P4'])
$report = $report.Replace('@@TOP_RULES@@',($topRules -join "`n")).Replace('@@REDISCOVERED@@',[string]$rediscovered)
$candidateByAct=foreach($act in @('D1_GDPR','D2_DSA','D3_AI_ACT')){$ar=@($register|Where-Object ACT -eq $act);"| $act | $($ar.Count) | $(@($ar|? REPAIR_CANDIDATE -eq 'YES').Count) | $(@($ar|? REPAIR_CANDIDATE -eq 'UNCERTAIN').Count) | $(@($ar|? REPAIR_CANDIDATE -eq 'NO').Count) |"}
$indicatorRows=@(
    @('ACTOR_SPAN_TRUNCATION_CANDIDATE','ACTOR_SPAN_TRUNCATION_CANDIDATE'),@('ACTOR_COMPLEMENT_CANDIDATE','ACTOR_COMPLEMENT_CANDIDATE'),
    @('MISSING_MODAL_CANDIDATE','MISSING_MODAL_CANDIDATE'),@('PREDICATE_FRAGMENTATION_CANDIDATE','PREDICATE_FRAGMENTATION_CANDIDATE'),
    @('DISCOURSE_ONLY_ACTION','DISCOURSE_ONLY_ACTION'),@('PASSIVE_NO_EXPLICIT_ACTOR_CANDIDATE','PASSIVE_NO_EXPLICIT_ACTOR_CANDIDATE'),
    @('PROPOSITION_BOUNDARY_CONTAMINATION_CANDIDATE','PROPOSITION_BOUNDARY_CONTAMINATION_CANDIDATE'),@('COORDINATED_PREDICATE_CANDIDATE','COORDINATED_PREDICATE_CANDIDATE')
)
$aaTable=foreach($pair in $indicatorRows){$count=@($aaAudit|Where-Object { $_.($pair[1]) -eq $true }).Count;"| $($pair[0]) | $count |"}
$report=$report.Replace('@@CANDIDATES_BY_ACT@@',($candidateByAct -join "`n")).Replace('@@ACTOR_ACTION_INDICATORS@@',($aaTable -join "`n"))
$falseSimp=@($rediscovery|Where-Object { $_.COMPLEXITY_DEFENSIBLE -eq 'NO' -and $_.ASSIGNED_COMPLEXITY -eq 'SIMPLE' }).Count
$complexSimple=@($rediscovery|Where-Object COMPLEX_CASE_INCORRECTLY_SIMPLE -eq 'YES').Count
$underclass=@($rediscovery|Where-Object UNDERCLASSIFIED_FROM_HUMAN_COMPLEX -eq 'YES').Count
$missedCases=@($rediscovery|Where-Object KNOWN_DEFECT_REDISCOVERED -eq 'NO'|ForEach-Object {"$($_.HUMAN_CASE_ID) [$($_.HUMAN_DIAGNOSTIC_CLASS)]"}) -join '; '
$report = $report.Replace('@@FALSE_SIMPLIFICATIONS@@',[string]$falseSimp).Replace('@@COMPLEX_SIMPLE@@',[string]$complexSimple).Replace('@@UNDERCLASSIFICATIONS@@',[string]$underclass).Replace('@@MISSED_CASES@@',$missedCases)
$report = $report.Replace('@@BOTH@@',[string]$both).Replace('@@LUNA_ONLY@@',[string]$lunaOnly).Replace('@@TERRA_ONLY@@',[string]$terraOnly).Replace('@@NEITHER@@',[string]$noneModel).Replace('@@NOT_ASSESSED@@',[string]$notAssessed)
$report = $report.Replace('@@CP@@',[string]$cpN).Replace('@@REC@@',[string]$recN).Replace('@@BOTH_POP@@',[string]$bothN).Replace('@@IDENTICAL@@',[string]$identN).Replace('@@CP_ONLY@@',[string]$cpOnly).Replace('@@REC_ONLY@@',[string]$recOnly).Replace('@@REL_TRIGGERED@@',[string]$relTriggeredN).Replace('@@ACT_REL@@',($distByAct -join "`n")).Replace('@@HASHES@@',($hashTable -join "`n"))
$reportPath=Join-Path $out 'R4_2E_A_METHOD_REPORT.md'
[IO.File]::WriteAllText($reportPath,$report,(New-Object System.Text.UTF8Encoding($false)))

"Inspected=$total; human-ground-truth=$($humanRows.Count); model-comparison-covered=$($total-$notAssessed); source-hash=$actualHash"
"Created outputs in $out"
