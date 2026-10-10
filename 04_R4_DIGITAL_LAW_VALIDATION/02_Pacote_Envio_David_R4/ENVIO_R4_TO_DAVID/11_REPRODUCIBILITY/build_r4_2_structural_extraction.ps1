param(
    [string]$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
)

$ErrorActionPreference = 'Stop'
$workspace = Join-Path $RepoRoot 'R4_CROSS_DOMAIN_VALIDATION'
$output = Join-Path $workspace '03_extraction'
New-Item -ItemType Directory -Path $output -Force | Out-Null

$cases = @(
    [pscustomobject]@{ CaseId = 'D1_GDPR'; Celex = '32016R0679'; Processing = '02_sources/D1_GDPR/normalized/D1_GDPR_32016R0679_processing.txt'; Model = 'Codex GPT-5 runtime; GPT-5.6 Luna High requested; exact runtime variant not exposed' },
    [pscustomobject]@{ CaseId = 'D2_DSA'; Celex = '32022R2065'; Processing = '02_sources/D2_DSA/normalized/D2_DSA_32022R2065_processing.txt'; Model = 'Codex GPT-5 runtime; GPT-5.6 Luna High requested; exact runtime variant not exposed' },
    [pscustomobject]@{ CaseId = 'D3_AI_ACT'; Celex = '32024R1689'; Processing = '02_sources/D3_AI_ACT/normalized/D3_AI_ACT_32024R1689_processing.txt'; Model = 'Codex GPT-5 runtime; GPT-5.6 Luna High requested; exact runtime variant not exposed' }
)

function Normalize-Text([string]$Text) {
    if ([string]::IsNullOrWhiteSpace($Text)) { return '' }
    return (($Text -replace '\s+', ' ').Trim())
}

function Normalize-Actor([string]$Text) {
    $v = Normalize-Text $Text
    $v = $v -replace '^(?i)(the|a|an|each|any|all)\s+', ''
    return $v.ToLowerInvariant()
}

function Is-ActorLike([string]$Text) {
    $v = $Text.ToLowerInvariant()
    return ($v -match '\b(controller|processor|authority|authorities|commission|board|member states?|provider|providers|person|persons|data subject|undertaking|undertakings|body|bodies|organisation|organization|deployer|operator|manufacturer|importer|distributor|notified body|economic operator|legal representative|representative|applicant|complainant|customer|recipient|user|researcher|developer|institution|parliament|council|agency|committee|court|tribunal|supervisory|market surveillance|public authority|private entity|holder of parental responsibility)\b')
}

function Get-ActorType([string]$Text) {
    $v = $Text.ToLowerInvariant()
    if ($v -match '\b(person|persons|data subject|user|customer|complainant|holder of parental responsibility)\b') { return 'natural person' }
    if ($v -match '\b(provider|manufacturer|importer|distributor|operator|undertaking|organisation|organization|developer|economic operator|private entity)\b') { return 'private organization or legal entity' }
    if ($v -match '\b(authority|authorities|commission|board|member state|public authority|agency|committee|parliament|council|court|tribunal|supervisory|market surveillance|notified body|institution|body|bodies)\b') { return 'public body or explicit institutional category' }
    return 'other explicit textual category'
}

function Get-Modality([string]$Modal, [string]$Text) {
    $m = $Modal.ToLowerInvariant()
    if ($m -match 'not|prohibited') { return 'PROHIBITED' }
    if ($m -match 'may|can') { return 'PERMISSIVE' }
    if ($m -match 'shall|must|required') { if ($Text -match '(?i)\b(where|if|unless|provided that|only if|subject to)\b') { return 'CONDITIONAL' }; return 'MANDATORY' }
    if ($m -match 'should') { return 'OTHER' }
    return 'UNCLEAR'
}

function Get-LegalAction([string]$Phrase) {
    $p = $Phrase.ToLowerInvariant()
    if ($p -match '^provide|^make available|^furnish') { return 'provide information or material' }
    if ($p -match '^submit|^send|^transmit') { return 'submit or transmit document/information' }
    if ($p -match '^notify|^inform') { return 'notify or inform' }
    if ($p -match '^assess|^evaluate') { return 'conduct assessment or evaluation' }
    if ($p -match '^designate|^appoint') { return 'designate or appoint body/person' }
    if ($p -match '^cooperate|^coordinate') { return 'cooperate or coordinate' }
    if ($p -match '^monitor|^keep under review') { return 'monitor' }
    if ($p -match '^verify|^check') { return 'verify or check' }
    if ($p -match '^request|^require|^seek') { return 'request or require information/action' }
    if ($p -match '^issue|^adopt|^take a decision|^decide') { return 'issue, adopt or make decision' }
    if ($p -match '^maintain|^keep|^store|^record|^retain') { return 'maintain, store or record' }
    if ($p -match '^ensure|^safeguard|^protect') { return 'ensure or safeguard' }
    if ($p -match '^consult|^hear') { return 'consult or hear' }
    if ($p -match '^carry out|^conduct|^perform') { return 'carry out or conduct activity' }
    if ($p -match '^prohibit|^prevent') { return 'prohibit or prevent' }
    if ($p -match '^allow|^permit|^authorise|^authorize') { return 'allow or authorise' }
    return (Normalize-Text $Phrase)
}

function Get-FirstClause([string]$Text, [int]$Limit = 220) {
    $v = Normalize-Text $Text
    $v = $v -replace '(?i)\b(where|if|unless|provided that|subject to|in accordance with|for the purposes of)\b.*$', ''
    if ($v.Length -gt $Limit) { return $v.Substring(0, $Limit).Trim() + '…' }
    return $v
}

function Get-Refs([string]$Text) {
    $refs = [System.Collections.Generic.List[string]]::new()
    $pattern = '(?i)\b(Article|Articles|Annex|Chapter|Section)\s+[IVXLC\d]+(?:\([a-z0-9]+\))?'
    foreach ($m in [regex]::Matches($Text, $pattern)) {
        $r = Normalize-Text $m.Value
        if (-not $refs.Contains($r)) { $refs.Add($r) }
    }
    return @($refs)
}

function Get-Blocks([string[]]$Lines, [string]$CaseId, [string]$Celex, [string]$Processing) {
    $blocks = [System.Collections.Generic.List[object]]::new()
    $current = $null
    $currentLines = [System.Collections.Generic.List[string]]::new()
    foreach ($line in $Lines) {
        $marker = [regex]::Match($line, '^\[(RECITAL|ARTICLE|ANNEX)\s+([^\]]+)\]$')
        if ($marker.Success) {
            if ($null -ne $current) {
                $blocks.Add([pscustomobject]@{ CaseId=$CaseId; Celex=$Celex; Processing=$Processing; SourceType=$current.Type; Number=$current.Number; Lines=@($currentLines) })
            }
            $current = [pscustomobject]@{ Type=$marker.Groups[1].Value; Number=$marker.Groups[2].Value.Trim() }
            $currentLines = [System.Collections.Generic.List[string]]::new()
        } elseif ($null -ne $current) {
            $currentLines.Add($line)
        }
    }
    if ($null -ne $current) {
        $blocks.Add([pscustomobject]@{ CaseId=$CaseId; Celex=$Celex; Processing=$Processing; SourceType=$current.Type; Number=$current.Number; Lines=@($currentLines) })
    }
    return @($blocks)
}

function Get-Segments($Block) {
    $payload = @($Block.Lines | ForEach-Object { $_.Trim() } | Where-Object { $_ -ne '' })
    if ($payload.Count -eq 0) { return @() }
    $title = ''
    $start = 0
    if ($Block.SourceType -eq 'ARTICLE' -and $payload.Count -ge 2 -and $payload[0] -match '^Article\s+') { $title=$payload[1]; $start=2 }
    elseif ($Block.SourceType -eq 'ANNEX' -and $payload.Count -ge 1) { $title=$payload[0]; $start=1 }
    elseif ($Block.SourceType -eq 'RECITAL' -and $payload[0] -match '^\(\d+\)$') { $start=1 }
    $work = if ($start -lt $payload.Count) { @($payload[$start..($payload.Count-1)]) } else { @() }
    $segments = [System.Collections.Generic.List[object]]::new()
    if ($Block.SourceType -eq 'ARTICLE') {
        $para = ''
        $paraNo = ''
        foreach ($line in $work) {
            if ($line -match '^(\d+)\.\s*(.*)$') {
                if ($para -ne '') { $segments.Add([pscustomobject]@{ Text=(Normalize-Text $para); Paragraph=$paraNo; Title=$title }) }
                $paraNo=$Matches[1]; $para=$Matches[2]
            } elseif ($line -match '^\(([a-z])\)$' -and $paraNo -ne '') {
                if ($para -ne '') { $segments.Add([pscustomobject]@{ Text=(Normalize-Text $para); Paragraph=$paraNo; Title=$title }) }
                $paraNo="$paraNo($($Matches[1]))"; $para=''
            } elseif ($paraNo -ne '') { $para += ' ' + $line }
        }
        if ($para -ne '') { $segments.Add([pscustomobject]@{ Text=(Normalize-Text $para); Paragraph=$paraNo; Title=$title }) }
    } else {
        $segments.Add([pscustomobject]@{ Text=(Normalize-Text ($work -join ' ')); Paragraph=''; Title=$title })
    }
    return @($segments)
}

$articleTitles = @{}
foreach ($row in (Import-Csv (Join-Path $workspace 'R4_ARTICLE_INDEX.csv'))) { $articleTitles["$($row.CASE_ID)|$($row.ARTICLE_NUMBER)"]=$row.ARTICLE_TITLE }
$extractions = [System.Collections.Generic.List[object]]::new()
$rawCandidates = [System.Collections.Generic.List[object]]::new()
$crossRefs = [System.Collections.Generic.List[object]]::new()
$definitions = [System.Collections.Generic.List[object]]::new()
$coverage = [System.Collections.Generic.List[object]]::new()
$caseBlocks = @{}

$actorRegex = '(?i)(?<actor>(?:(?:the|a|an|each|any|all|one or more|member states?)\s+)?[A-Za-z][A-Za-z''’\-]*(?:\s+[A-Za-z][A-Za-z''’\-]*){0,9})\s+(?<modal>shall not|shall|may not|may|must not|must|is prohibited from|are prohibited from|is required to|are required to|has the right to|have the right to|should|cannot|can)\s+(?<action>[a-z][a-z-]*(?:\s+[a-z][a-z-]*){0,6})'

foreach ($cfg in $cases) {
    $processingPath = Join-Path $workspace $cfg.Processing
    $lines = Get-Content -LiteralPath $processingPath
    $blocks = @(Get-Blocks -Lines $lines -CaseId $cfg.CaseId -Celex $cfg.Celex -Processing $cfg.Processing)
    $caseBlocks[$cfg.CaseId] = $blocks
    foreach ($type in @('ARTICLE','RECITAL','ANNEX')) {
        $expected = @((Import-Csv (Join-Path $workspace 'R4_LEGAL_STRUCTURE_INDEX.csv')) | Where-Object { $_.CASE_ID -eq $cfg.CaseId -and $_.STRUCTURE_TYPE -eq $type }).Count
        $processed = @($blocks | Where-Object SourceType -eq $type).Count
        $coverage.Add([pscustomobject]@{ CASE_ID=$cfg.CaseId; STRUCTURE_TYPE=$type; EXPECTED_COUNT=$expected; PROCESSED_COUNT=$processed; SKIPPED_COUNT=($expected-$processed); SKIP_REASON=if($expected-$processed -eq 0){''}else{'Marker not found in processing copy'}; COVERAGE_STATUS=if($expected -eq $processed){'COMPLETE'}else{'INCOMPLETE'} })
    }
    foreach ($block in $blocks) {
        $segments = @(Get-Segments $block)
        foreach ($ref in (Get-Refs ($block.Lines -join ' '))) {
            $refType = ($ref -split '\s+')[0].ToUpperInvariant()
            $crossRefs.Add([pscustomobject]@{ CASE_ID=$cfg.CaseId; SOURCE_POINTER="$($cfg.Celex)#$($block.SourceType.ToLowerInvariant())_$($block.Number)"; REFERENCE_TYPE=$refType; REFERENCE_TARGET=$ref; RESOLVED='NO'; RESOLVED_POINTER=''; NOTES='Explicit reference retained; automatic semantic resolution not performed in R4.2.' })
        }
        $whole = Normalize-Text ($block.Lines -join ' ')
        if ($whole -match '(?i)\bmeans\b|\bis defined as\b|\bshall mean\b') {
            $termMatch = [regex]::Match($whole, '(?i)(?<term>[A-Za-z][A-Za-z0-9\- ]{1,80}?)\s+(means|is defined as|shall mean)\s+(?<definition>[^.;]{20,300})')
            if ($termMatch.Success) { $definitions.Add([pscustomobject]@{ CASE_ID=$cfg.CaseId; TERM=(Normalize-Text $termMatch.Groups['term'].Value); DEFINITION=(Normalize-Text $termMatch.Groups['definition'].Value); SOURCE_POINTER="$($cfg.Celex)#$($block.SourceType.ToLowerInvariant())_$($block.Number)"; POTENTIAL_RELEVANCE='Textual definition retained for actor/object normalization; no role interpretation.' }) }
        }
        foreach ($segment in $segments) {
            if ([string]::IsNullOrWhiteSpace($segment.Text)) { continue }
            $matches = @([regex]::Matches($segment.Text, $actorRegex))
            if ($matches.Count -eq 0) { continue }
            $matchNo = 0
            foreach ($m in $matches) {
                $matchNo++
                $actorText = Normalize-Text $m.Groups['actor'].Value
                if (-not (Is-ActorLike $actorText)) { continue }
                $modal = Normalize-Text $m.Groups['modal'].Value
                $verbPhrase = Normalize-Text $m.Groups['action'].Value
                $remainderStart = $m.Index + $m.Length
                $remainder = if ($remainderStart -lt $segment.Text.Length) { $segment.Text.Substring($remainderStart).Trim() } else { '' }
                $sourceType = switch ($block.SourceType) { 'ARTICLE' {'OPERATIVE_ARTICLE'} 'RECITAL' {'RECITAL'} 'ANNEX' {'ANNEX'} default {'OTHER_OFFICIAL_STRUCTURE'} }
                $pointer = "$($cfg.Celex)#$($block.SourceType.ToLowerInvariant())_$($block.Number)"
                if ($segment.Paragraph -ne '') { $pointer += "/p$($segment.Paragraph)" }
                $refs = @(Get-Refs $segment.Text)
                $ambiguous = ($matches.Count -gt 1 -or $actorText -match '(?i)\b(it|they|this|such)\b' -or $segment.Text -match '(?i)\b(respectively|and/or)\b')
                $confidence = if ($ambiguous) {'LOW'} elseif ($refs.Count -gt 0 -or $segment.Text.Length -gt 650) {'MEDIUM'} else {'HIGH'}
                $condition = ''
                $conditionMatch = [regex]::Match($segment.Text, '(?i)\b(where|if|unless|provided that|only if|subject to)\b(?<v>[^.;]{0,220})')
                if ($conditionMatch.Success) { $condition=Normalize-Text $conditionMatch.Value }
                $trigger = ''
                $triggerMatch = [regex]::Match($segment.Text, '(?i)\b(upon|following|when|after|before|in the event of)\b(?<v>[^.;]{0,180})')
                if ($triggerMatch.Success) { $trigger=Normalize-Text $triggerMatch.Value }
                $counterpart = ''
                $counterMatch = [regex]::Match($segment.Text, '(?i)\b(to|with|from)\s+(the|a|an|any|each|member states?|commission|board|authority|authorities|provider|providers|person|persons)\b[^.;,]{0,100}')
                if ($counterMatch.Success) { $counterpart=Normalize-Text $counterMatch.Value }
                $outputText = ''
                $outMatch = [regex]::Match($segment.Text, '(?i)\b(report|opinion|certificate|decision|notification|assessment result|recommendation|authorisation|authorization|register|list)\b[^.;]{0,100}')
                if ($outMatch.Success) { $outputText=Normalize-Text $outMatch.Value }
                $effect = ''
                $effectMatch = [regex]::Match($segment.Text, '(?i)\b(lawful|lawfully|prohibited|entitled|right|obligation|binding|liable|void|authorised|authorized)\b[^.;]{0,100}')
                if ($effectMatch.Success) { $effect=Normalize-Text $effectMatch.Value }
                $rawCandidates.Add([pscustomobject]@{ CaseId=$cfg.CaseId; Celex=$cfg.Celex; SourceType=$sourceType; SourceNumber="$($sourceType)_$($block.Number)"; ArticleNumber=if($block.SourceType -eq 'ARTICLE'){$block.Number}else{''}; ParagraphNumber=if($block.SourceType -eq 'ARTICLE'){$segment.Paragraph}else{''}; RecitalNumber=if($block.SourceType -eq 'RECITAL'){$block.Number}else{''}; AnnexId=if($block.SourceType -eq 'ANNEX'){$block.Number}else{''}; SectionTitle=if($block.SourceType -eq 'ARTICLE'){$articleTitles["$($cfg.CaseId)|$($block.Number)"]}else{$segment.Title}; ActorText=$actorText; ActorNorm=(Normalize-Actor $actorText); ActorType=(Get-ActorType $actorText); LegalVerb="$modal $verbPhrase"; LegalAction=(Get-LegalAction $verbPhrase); Modality=(Get-Modality $modal $segment.Text); ActionObject=(Get-FirstClause $remainder 180); Counterpart=$counterpart; InformationObject=(Get-FirstClause $remainder 180); Output=$outputText; Condition=$condition; Trigger=$trigger; Recipient=$counterpart; LegalEffect=$effect; CrossReference=($refs -join '; '); Excerpt=(Get-FirstClause $segment.Text 500); SourcePointer=$pointer; Model=$cfg.Model; Confidence=$confidence; Ambiguity=if($ambiguous){'YES'}else{'NO'}; AmbiguityNote=if($ambiguous){'Multiple structural matches, pronoun reference or coordination requires human parsing review.'}else{''}; HumanReview=if($ambiguous){'YES'}else{'NO'}; HumanStatus=if($ambiguous){'PENDING'}else{'NOT_REQUIRED'}; Notes='Structural extraction only; no R/I/T or mechanism classification.' })
            }
        }
    }
}

$dedup = @{}
foreach ($r in $rawCandidates) {
    $key = "$($r.CaseId)|$($r.SourcePointer)|$($r.ActorNorm)|$($r.LegalAction)|$($r.Excerpt)"
    if (-not $dedup.ContainsKey($key)) { $dedup[$key]=$r }
}
$actorGroups = @($dedup.Values | Group-Object CaseId,ActorNorm)
$actorMap = @{}
$actorRows = [System.Collections.Generic.List[object]]::new()
foreach ($group in $actorGroups) {
    $first = $group.Group | Select-Object -First 1
    $id = "ACT-$($first.CaseId)-$('{0:D4}' -f ($actorRows.Count+1))"
    $actorMap["$($first.CaseId)|$($first.ActorNorm)"]=$id
    $variants = @($group.Group | Select-Object -ExpandProperty ActorText -Unique)
    $pCount=@($group.Group | Where-Object {$_.SourceType -eq 'OPERATIVE_ARTICLE'} | Select-Object -ExpandProperty SourcePointer -Unique).Count
    $rCount=@($group.Group | Where-Object {$_.SourceType -eq 'RECITAL'} | Select-Object -ExpandProperty SourcePointer -Unique).Count
    $aCount=@($group.Group | Where-Object {$_.SourceType -eq 'ANNEX'} | Select-Object -ExpandProperty SourcePointer -Unique).Count
    $actorRows.Add([pscustomobject]@{ ACTOR_ID=$id; CASE_ID=$first.CaseId; ACTOR_NORMALIZED_PROVISIONAL=$first.ActorNorm; TEXTUAL_VARIANTS=($variants -join ' | '); FIRST_SOURCE_POINTER=$first.SourcePointer; ACTOR_TYPE_TEXTUAL=$first.ActorType; PROVISION_COUNT=$pCount; RECITAL_COUNT=$rCount; ANNEX_COUNT=$aCount; NORMALIZATION_CONFIDENCE=if($variants.Count -eq 1){'HIGH'}else{'MEDIUM'}; MERGE_AMBIGUITY=if($variants.Count -gt 1){'REVIEW'}else{'NO'}; NOTES='Candidate textual actor only; no R/I/T role assigned.' })
}

$rowNo=0
foreach ($r in ($dedup.Values | Sort-Object CaseId,SourcePointer,ActorNorm,LegalAction)) {
    $rowNo++
    $actorId=$actorMap["$($r.CaseId)|$($r.ActorNorm)"]
    $extractions.Add([pscustomobject]@{ EXTRACTION_ID="EXT-{0:D6}" -f $rowNo; CASE_ID=$r.CaseId; CELEX=$r.Celex; SOURCE_TYPE=$r.SourceType; SOURCE_NUMBER=$r.SourceNumber; ARTICLE_NUMBER=$r.ArticleNumber; PARAGRAPH_NUMBER=$r.ParagraphNumber; RECITAL_NUMBER=$r.RecitalNumber; ANNEX_ID=$r.AnnexId; SECTION_TITLE=$r.SectionTitle; ACTOR_TEXT=$r.ActorText; ACTOR_NORMALIZED_PROVISIONAL=$r.ActorNorm; ACTOR_TYPE_TEXTUAL=$r.ActorType; LEGAL_VERB=$r.LegalVerb; LEGAL_ACTION=$r.LegalAction; MODALITY=$r.Modality; ACTION_OBJECT=$r.ActionObject; COUNTERPART_TEXT=$r.Counterpart; INFORMATION_OR_MATERIAL_OBJECT=$r.InformationObject; OUTPUT_OR_RESULT_TEXT=$r.Output; CONDITION_TEXT=$r.Condition; TRIGGER_TEXT=$r.Trigger; RECIPIENT_TEXT=$r.Recipient; LEGAL_EFFECT_TEXT=$r.LegalEffect; CROSS_REFERENCE=$r.CrossReference; SOURCE_EXCERPT=$r.Excerpt; SOURCE_POINTER=$r.SourcePointer; EXTRACTION_MODEL=$r.Model; EXTRACTION_CONFIDENCE=$r.Confidence; STRUCTURAL_AMBIGUITY=$r.Ambiguity; AMBIGUITY_NOTE=$r.AmbiguityNote; HUMAN_REVIEW_REQUIRED=$r.HumanReview; HUMAN_REVIEW_STATUS=$r.HumanStatus; NOTES=$r.Notes })
}

$actionRows = [System.Collections.Generic.List[object]]::new()
foreach ($group in @($extractions | Group-Object CASE_ID,ACTOR_ID,LEGAL_ACTION)) {
    $first=$group.Group | Select-Object -First 1
    $actionRows.Add([pscustomobject]@{ ACTION_ID="ACT-$($first.CASE_ID)-$('{0:D4}' -f ($actionRows.Count+1))"; CASE_ID=$first.CASE_ID; ACTOR_ID=$first.ACTOR_ID; LEGAL_ACTION=$first.LEGAL_ACTION; LEGAL_VERB_VARIANTS=(@($group.Group | Select-Object -ExpandProperty LEGAL_VERB -Unique) -join ' | '); ACTION_OBJECT=(@($group.Group | Select-Object -ExpandProperty ACTION_OBJECT -Unique | Select-Object -First 5) -join ' | '); RECIPIENT_OR_COUNTERPART=(@($group.Group | Select-Object -ExpandProperty COUNTERPART_TEXT -Unique | Where-Object {$_} | Select-Object -First 5) -join ' | '); SOURCE_COUNT=@($group.Group | Select-Object -ExpandProperty SOURCE_POINTER -Unique).Count; SOURCE_POINTERS=(@($group.Group | Select-Object -ExpandProperty SOURCE_POINTER -Unique) -join ' | '); NOTES='Descriptive action normalization only; no mechanism mapping.' })
}

$ambiguityRows = [System.Collections.Generic.List[object]]::new()
foreach ($r in @($extractions | Where-Object STRUCTURAL_AMBIGUITY -eq 'YES')) {
    $ambiguityRows.Add([pscustomobject]@{ AMBIGUITY_ID="AMB-{0:D5}" -f ($ambiguityRows.Count+1); CASE_ID=$r.CASE_ID; SOURCE_POINTER=$r.SOURCE_POINTER; ISSUE_TYPE='GRAMMATICAL_OR_COORDINATION_PARSE'; TEXT=$r.SOURCE_EXCERPT; LUNA_INTERPRETATION="$($r.ACTOR_TEXT) -> $($r.LEGAL_VERB)"; ALTERNATIVE_PARSE='Not adjudicated; preserve both text and structural flag for human QA.'; TERRA_ESCALATED='NO'; TERRA_RESULT=''; HUMAN_REVIEW_REQUIRED='YES'; FINAL_STRUCTURAL_DECISION='PENDING_HUMAN_REVIEW'; NOTES='R4.2 parsing ambiguity only; not an R/I/T or mechanism dispute.' })
}

$crossRefsUnique = @($crossRefs | Sort-Object CASE_ID,SOURCE_POINTER,REFERENCE_TARGET -Unique)
$qaIssues = @($extractions | Where-Object { [string]::IsNullOrWhiteSpace($_.SOURCE_POINTER) -or [string]::IsNullOrWhiteSpace($_.ACTOR_TEXT) -or [string]::IsNullOrWhiteSpace($_.LEGAL_ACTION) })
$qaSample = [System.Collections.Generic.List[object]]::new()
foreach ($conf in @('HIGH','MEDIUM','LOW')) {
    foreach ($type in @('OPERATIVE_ARTICLE','RECITAL','ANNEX')) {
        $pick=@($extractions | Where-Object {$_.EXTRACTION_CONFIDENCE -eq $conf -and $_.SOURCE_TYPE -eq $type} | Select-Object -First 3)
        foreach($r in $pick){$qaSample.Add([pscustomobject]@{ SAMPLE_ID="QA-{0:D4}" -f ($qaSample.Count+1); EXTRACTION_ID=$r.EXTRACTION_ID; CASE_ID=$r.CASE_ID; SOURCE_TYPE=$r.SOURCE_TYPE; SOURCE_POINTER=$r.SOURCE_POINTER; CONFIDENCE=$r.EXTRACTION_CONFIDENCE; ACTOR_TEXT=$r.ACTOR_TEXT; LEGAL_ACTION=$r.LEGAL_ACTION; SOURCE_EXCERPT=$r.SOURCE_EXCERPT; HUMAN_REVIEW_STATUS='PENDING'; REVIEW_SCOPE='Extraction fidelity only; no R/I/T or mechanism adjudication.' })}
    }
}

foreach ($path in @('R4_STRUCTURAL_EXTRACTION.csv','R4_DIGITAL_ACTOR_CANDIDATE_REGISTER.csv','R4_LEGAL_ACTION_REGISTER.csv','R4_CROSS_REFERENCE_REGISTER.csv','R4_STRUCTURAL_AMBIGUITY_LOG.csv','R4_2_SOURCE_COVERAGE_REPORT.csv','R4_2_HUMAN_QA_SAMPLE.csv','R4_LEGAL_DEFINITION_REGISTER.csv')) {
    $full=Join-Path $output $path
    if (Test-Path -LiteralPath $full) { Remove-Item -LiteralPath $full -Force }
}
$extractions | Export-Csv (Join-Path $output 'R4_STRUCTURAL_EXTRACTION.csv') -NoTypeInformation -Encoding utf8
$actorRows | Export-Csv (Join-Path $output 'R4_DIGITAL_ACTOR_CANDIDATE_REGISTER.csv') -NoTypeInformation -Encoding utf8
$actionRows | Export-Csv (Join-Path $output 'R4_LEGAL_ACTION_REGISTER.csv') -NoTypeInformation -Encoding utf8
$crossRefsUnique | Export-Csv (Join-Path $output 'R4_CROSS_REFERENCE_REGISTER.csv') -NoTypeInformation -Encoding utf8
$ambiguityRows | Export-Csv (Join-Path $output 'R4_STRUCTURAL_AMBIGUITY_LOG.csv') -NoTypeInformation -Encoding utf8
$coverage | Export-Csv (Join-Path $output 'R4_2_SOURCE_COVERAGE_REPORT.csv') -NoTypeInformation -Encoding utf8
$qaSample | Export-Csv (Join-Path $output 'R4_2_HUMAN_QA_SAMPLE.csv') -NoTypeInformation -Encoding utf8
$definitions | Export-Csv (Join-Path $output 'R4_LEGAL_DEFINITION_REGISTER.csv') -NoTypeInformation -Encoding utf8

$summary = [System.Collections.Generic.List[object]]::new()
foreach ($cfg in $cases) {
    $rows=@($extractions | Where-Object CASE_ID -eq $cfg.CaseId)
    $summary.Add([pscustomobject]@{ RUN_ID="R4_2_$($cfg.CaseId)_001"; CASE_ID=$cfg.CaseId; SOURCE_RANGE='All operative articles; all recitals; all annexes present in frozen processing copy'; MODEL=$cfg.Model; ROWS_EXTRACTED=$rows.Count; HIGH_CONFIDENCE=@($rows|Where-Object EXTRACTION_CONFIDENCE -eq 'HIGH').Count; MEDIUM_CONFIDENCE=@($rows|Where-Object EXTRACTION_CONFIDENCE -eq 'MEDIUM').Count; LOW_CONFIDENCE=@($rows|Where-Object EXTRACTION_CONFIDENCE -eq 'LOW').Count; AMBIGUITIES=@($rows|Where-Object STRUCTURAL_AMBIGUITY -eq 'YES').Count; HUMAN_REVIEW_REQUIRED=@($rows|Where-Object HUMAN_REVIEW_REQUIRED -eq 'YES').Count; TERRA_ESCALATIONS=0; QA_ERRORS=@($qaIssues|Where-Object CASE_ID -eq $cfg.CaseId).Count; FINAL_RUN_STATUS='R4_2_STRUCTURAL_EXTRACTION_COMPLETE_PENDING_HUMAN_REVIEW'; NOTES='Structural extraction only; no R/I/T, intermediary, target, regulator or mechanism coding; Rotem not consulted.' })
}
$summary | Export-Csv (Join-Path $output 'R4_2_AI_EXTRACTION_RUN_SUMMARY.csv') -NoTypeInformation -Encoding utf8

Write-Output "R4.2 extraction complete: $($extractions.Count) rows; actors=$($actorRows.Count); actions=$($actionRows.Count); cross_refs=$($crossRefsUnique.Count); ambiguities=$($ambiguityRows.Count); qa_sample=$($qaSample.Count)"
