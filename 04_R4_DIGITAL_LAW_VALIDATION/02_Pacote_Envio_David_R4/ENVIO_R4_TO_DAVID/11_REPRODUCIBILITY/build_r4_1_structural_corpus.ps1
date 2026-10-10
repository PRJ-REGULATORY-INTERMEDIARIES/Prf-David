$ErrorActionPreference = 'Stop'

$root = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
$sourceRoot = Join-Path $root '02_sources'
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)

function Get-NodeText([System.Xml.XmlNode] $node) {
    if ($null -eq $node) { return '' }
    return (($node.InnerText -replace '\s+', ' ').Trim())
}

function Get-Class([System.Xml.XmlNode] $node) {
    if ($null -eq $node -or $null -eq $node.Attributes['class']) { return '' }
    return $node.Attributes['class'].Value
}

function Add-Line([System.Text.StringBuilder] $builder, [string] $line, [hashtable] $markerPositions, [string] $marker) {
    $position = $builder.Length
    [void]$builder.AppendLine($line)
    if ($marker -and -not $markerPositions.ContainsKey($marker)) {
        $markerPositions[$marker] = $position
    }
}

$cases = @(
    @{ Id = 'D1_GDPR'; CELEX = '32016R0679'; OfficialTitle = 'Regulation (EU) 2016/679 of the European Parliament and of the Council'; ShortTitle = 'General Data Protection Regulation — GDPR'; Year = 2016; ExpectedAnnexes = 0 },
    @{ Id = 'D2_DSA'; CELEX = '32022R2065'; OfficialTitle = 'Regulation (EU) 2022/2065 of the European Parliament and of the Council'; ShortTitle = 'Digital Services Act — DSA'; Year = 2022; ExpectedAnnexes = 0 },
    @{ Id = 'D3_AI_ACT'; CELEX = '32024R1689'; OfficialTitle = 'Regulation (EU) 2024/1689 of the European Parliament and of the Council'; ShortTitle = 'Artificial Intelligence Act — AI Act'; Year = 2024; ExpectedAnnexes = 13 }
)

$allStructure = @()
$allArticles = @()
$allMetadata = @()

foreach ($case in $cases) {
    $caseRoot = Join-Path $sourceRoot $case.Id
    $original = Join-Path $caseRoot "original\$($case.Id)_$($case.CELEX)_official.xhtml"
    $normalized = Join-Path $caseRoot "normalized\$($case.Id)_$($case.CELEX)_processing.txt"
    $metadataPath = Join-Path $caseRoot "metadata\$($case.Id)_metadata.json"
    $validationPath = Join-Path $caseRoot "validation\$($case.Id)_structural_validation.json"

    $xml = New-Object System.Xml.XmlDocument
    $xml.PreserveWhitespace = $true
    $xml.Load($original)
    $body = $xml.SelectSingleNode("//*[local-name()='body']")
    if ($null -eq $body) { throw "No body found in $original" }

    $structure = @()
    $structureById = @{}

    foreach ($node in @($xml.SelectNodes("//*[local-name()='div' and starts-with(@id,'rct_')]"))) {
        $id = $node.Attributes['id'].Value
        $number = $id -replace '^rct_', ''
        $record = [PSCustomObject]@{ CaseId=$case.Id; CELEX=$case.CELEX; StructureType='RECITAL'; StructureId=$id; Number=$number; Title=''; ParentStructure='pbl_1'; OrderIndex=0; StartMarker="[RECITAL $number]"; EndMarker=''; SourceReference="$(Split-Path -Leaf $original)#$id"; ValidationStatus='STRUCTURAL_CHECK_PENDING' }
        $structure += $record; $structureById[$id] = $record
    }
    foreach ($node in @($xml.SelectNodes("//*[local-name()='div' and starts-with(@id,'cpt_')]"))) {
        $id = $node.Attributes['id'].Value
        $isSection = $id -match '\.sct_'
        $number = if ($isSection) { $id -replace '^.*\.sct_', '' } else { $id -replace '^cpt_', '' }
        $titleNode = $node.SelectSingleNode(".//*[local-name()='p' and contains(concat(' ', normalize-space(@class), ' '), ' oj-ti-section-2 ')][1]")
        $title = Get-NodeText $titleNode
        $type = if ($isSection) { 'SECTION' } else { 'CHAPTER' }
        $parent = if ($isSection) { $id -replace '\.sct_.*$', '' } else { '' }
        $marker = if ($isSection) { "[SECTION $number]" } else { "[CHAPTER $number]" }
        $record = [PSCustomObject]@{ CaseId=$case.Id; CELEX=$case.CELEX; StructureType=$type; StructureId=$id; Number=$number; Title=$title; ParentStructure=$parent; OrderIndex=0; StartMarker=$marker; EndMarker=''; SourceReference="$(Split-Path -Leaf $original)#$id"; ValidationStatus='STRUCTURAL_CHECK_PENDING' }
        $structure += $record; $structureById[$id] = $record
    }
    foreach ($node in @($xml.SelectNodes("//*[local-name()='div' and starts-with(@id,'art_') and not(contains(@id,'.'))]"))) {
        $id = $node.Attributes['id'].Value
        $number = $id -replace '^art_', ''
        $titleNode = $node.SelectSingleNode(".//*[local-name()='p' and contains(concat(' ', normalize-space(@class), ' '), ' oj-sti-art ')][1]")
        $title = Get-NodeText $titleNode
        $parentNode = $node.SelectSingleNode("ancestor::*[local-name()='div' and starts-with(@id,'cpt_')][1]")
        $parent = if ($parentNode) { $parentNode.Attributes['id'].Value } else { '' }
        $record = [PSCustomObject]@{ CaseId=$case.Id; CELEX=$case.CELEX; StructureType='ARTICLE'; StructureId=$id; Number=$number; Title=$title; ParentStructure=$parent; OrderIndex=0; StartMarker="[ARTICLE $number]"; EndMarker=''; SourceReference="$(Split-Path -Leaf $original)#$id"; ValidationStatus='STRUCTURAL_CHECK_PENDING' }
        $structure += $record; $structureById[$id] = $record
    }
    foreach ($node in @($xml.SelectNodes("//*[local-name()='div' and starts-with(@id,'anx_')]"))) {
        $id = $node.Attributes['id'].Value
        $number = $id -replace '^anx_', ''
        $titles = @($node.SelectNodes(".//*[local-name()='p' and contains(concat(' ', normalize-space(@class), ' '), ' oj-doc-ti ')]") | ForEach-Object { Get-NodeText $_ })
        $title = if ($titles.Count -gt 1) { $titles[1] } else { '' }
        $record = [PSCustomObject]@{ CaseId=$case.Id; CELEX=$case.CELEX; StructureType='ANNEX'; StructureId=$id; Number=$number; Title=$title; ParentStructure=''; OrderIndex=0; StartMarker="[ANNEX $number]"; EndMarker=''; SourceReference="$(Split-Path -Leaf $original)#$id"; ValidationStatus='STRUCTURAL_CHECK_PENDING' }
        $structure += $record; $structureById[$id] = $record
    }

    $builder = New-Object System.Text.StringBuilder
    $markerPositions = @{}
    Add-Line $builder '[DOCUMENT_START]' $markerPositions ''
    $recitalsStarted = $false
    $operativeStarted = $false
    $contentNodes = @($body.SelectNodes(".//*[local-name()='p' or local-name()='td' or local-name()='th']"))
    foreach ($node in $contentNodes) {
        $isCell = $node.LocalName -in @('td','th')
        if ($isCell -and $null -ne $node.SelectSingleNode(".//*[local-name()='p']")) { continue }
        $text = Get-NodeText $node
        if ([string]::IsNullOrWhiteSpace($text)) { continue }
        $class = Get-Class $node
        $marker = ''
        $structureId = ''
        $recital = $node.SelectSingleNode("ancestor::*[local-name()='div' and starts-with(@id,'rct_')][1]")
        if ($recital -and $node.LocalName -eq 'p') {
            $firstP = $recital.SelectSingleNode(".//*[local-name()='p'][1]")
            if ($firstP -eq $node) {
                $number = $recital.Attributes['id'].Value -replace '^rct_', ''
                if (-not $recitalsStarted) { Add-Line $builder '[RECITALS_START]' $markerPositions ''; $recitalsStarted = $true }
                $marker = "[RECITAL $number]"; $structureId = $recital.Attributes['id'].Value
            }
        }
        if ($class -match '(^|\s)oj-ti-section-1(\s|$)') {
            $container = $node.SelectSingleNode("ancestor::*[local-name()='div' and starts-with(@id,'cpt_')][1]")
            if ($container) {
                $structureId = $container.Attributes['id'].Value
                $record = $structureById[$structureId]
                $marker = $record.StartMarker
                if (-not $operativeStarted) { Add-Line $builder '[OPERATIVE_PROVISIONS_START]' $markerPositions ''; $operativeStarted = $true }
            }
        }
        if ($class -match '(^|\s)oj-ti-art(\s|$)') {
            $container = $node.SelectSingleNode("ancestor::*[local-name()='div' and starts-with(@id,'art_') and not(contains(@id,'.'))][1]")
            if ($container) { $structureId = $container.Attributes['id'].Value; $marker = $structureById[$structureId].StartMarker }
        }
        if ($class -match '(^|\s)oj-doc-ti(\s|$)' -and $text -match '^ANNEX') {
            $container = $node.SelectSingleNode("ancestor::*[local-name()='div' and starts-with(@id,'anx_')][1]")
            if ($container) { $structureId = $container.Attributes['id'].Value; $marker = $structureById[$structureId].StartMarker }
        }
        if ($marker) { Add-Line $builder $marker $markerPositions $marker }
        Add-Line $builder $text $markerPositions ''
    }
    Add-Line $builder '[DOCUMENT_END]' $markerPositions ''
    $normalizedText = $builder.ToString()
    [IO.File]::WriteAllText($normalized, $normalizedText, $utf8NoBom)

    $ordered = @($structure | Where-Object { $markerPositions.ContainsKey($_.StartMarker) } | Sort-Object @{Expression={ $markerPositions[$_.StartMarker] }})
    for ($i=0; $i -lt $ordered.Count; $i++) {
        $ordered[$i].OrderIndex = $i + 1
        $ordered[$i].EndMarker = if ($i + 1 -lt $ordered.Count) { $ordered[$i + 1].StartMarker } else { '[DOCUMENT_END]' }
        $ordered[$i].ValidationStatus = 'VALIDATED'
    }
    $structureWithPositions = $ordered | ForEach-Object {
        [PSCustomObject]@{ CASE_ID=$_.CaseId; CELEX=$_.CELEX; STRUCTURE_TYPE=$_.StructureType; STRUCTURE_ID=$_.StructureId; NUMBER=$_.Number; TITLE=$_.Title; PARENT_STRUCTURE=$_.ParentStructure; ORDER_INDEX=$_.OrderIndex; START_MARKER=$_.StartMarker; END_MARKER=$_.EndMarker; START_POSITION=$markerPositions[$_.StartMarker]; END_POSITION=0; SOURCE_REFERENCE=$_.SourceReference; VALIDATION_STATUS=$_.ValidationStatus }
    }
    $structureWithPositions = @($structureWithPositions)
    for ($i=0; $i -lt $structureWithPositions.Count; $i++) {
        $end = if ($i + 1 -lt $structureWithPositions.Count) { $structureWithPositions[$i + 1].START_POSITION - 1 } else { $normalizedText.Length - 1 }
        $structureWithPositions[$i].END_POSITION = $end
    }

    $articles = @($structureWithPositions | Where-Object { $_.STRUCTURE_TYPE -eq 'ARTICLE' } | ForEach-Object {
        $parentChapter = $_.PARENT_STRUCTURE
        $sectionNode = $null
        $node = $xml.SelectSingleNode("//*[local-name()='div' and @id='$($_.STRUCTURE_ID)']")
        $sectionNode = $node.SelectSingleNode("ancestor::*[local-name()='div' and starts-with(@id,'cpt_') and contains(@id,'.sct_')][1]")
        $section = if ($sectionNode) { $sectionNode.Attributes['id'].Value } else { '' }
        [PSCustomObject]@{ CASE_ID=$_.CASE_ID; ARTICLE_NUMBER=$_.NUMBER; ARTICLE_TITLE=$_.TITLE; CHAPTER=if($section){$section -replace '\.sct_.*$',''}else{$parentChapter}; SECTION=$section; START_POSITION=$_.START_POSITION; END_POSITION=$_.END_POSITION; SOURCE_REFERENCE=$_.SOURCE_REFERENCE }
    })

    $languageHeader = $xml.SelectSingleNode("//*[contains(concat(' ', normalize-space(@class), ' '), ' oj-hd-lg ')]")
    $rootLang = if ($xml.DocumentElement.Attributes['lang']) { $xml.DocumentElement.Attributes['lang'].Value } elseif ((Get-NodeText $languageHeader) -match '\bEN\b') { 'EN' } else { '' }
    $articleNumbers = @($articles | ForEach-Object { [int]$_.ARTICLE_NUMBER })
    $articleSequence = ($articleNumbers.Count -gt 0 -and (($articleNumbers | Sort-Object) -join ',') -eq ((1..($articleNumbers | Measure-Object -Maximum).Maximum) -join ','))
    $recitalNumbers = @($structureWithPositions | Where-Object { $_.STRUCTURE_TYPE -eq 'RECITAL' } | ForEach-Object { [int]$_.NUMBER })
    $recitalSequence = ($recitalNumbers.Count -eq 0 -or (($recitalNumbers | Sort-Object) -join ',') -eq ((1..($recitalNumbers | Measure-Object -Maximum).Maximum) -join ','))
    $annexCount = @($structureWithPositions | Where-Object { $_.STRUCTURE_TYPE -eq 'ANNEX' }).Count
    $chapterCount = @($structureWithPositions | Where-Object { $_.STRUCTURE_TYPE -eq 'CHAPTER' }).Count
    $sectionCount = @($structureWithPositions | Where-Object { $_.STRUCTURE_TYPE -eq 'SECTION' }).Count
    $validation = [ordered]@{
        case_id = $case.Id; celex = $case.CELEX; root_language = $rootLang; article_count = $articles.Count; recital_count = $recitalNumbers.Count; chapter_count = $chapterCount; section_count = $sectionCount; annex_count = $annexCount; expected_annex_count = $case.ExpectedAnnexes; article_sequence_coherent = $articleSequence; recital_sequence_coherent = $recitalSequence; document_end_marker_present = $normalizedText.Contains('[DOCUMENT_END]'); recitals_preserved = ($recitalNumbers.Count -gt 0); operative_provisions_present = ($articleNumbers.Count -gt 0); annex_check = if ($annexCount -eq $case.ExpectedAnnexes) { 'PASS' } else { 'NOTE' }; status = if ($articleSequence -and $recitalSequence -and $annexCount -eq $case.ExpectedAnnexes -and $normalizedText.Contains('[DOCUMENT_END]')) { 'VALIDATED' } else { 'VALIDATED_WITH_NOTES' }; note = 'Structural validation only; no actor, intermediary or mechanism extraction performed.'
    }
    [IO.File]::WriteAllText($validationPath, ($validation | ConvertTo-Json -Depth 5), $utf8NoBom)
    $eliNumber = ([int]$case.CELEX.Substring(6)).ToString()
    [IO.File]::WriteAllText($metadataPath, ([ordered]@{ case_id=$case.Id; celex=$case.CELEX; source_url="https://eur-lex.europa.eu/eli/reg/$($case.Year)/$eliNumber/oj/eng"; acquisition_url="http://publications.europa.eu/resource/celex/$($case.CELEX)"; source_provider='European Union Publications Office / CELLAR'; source_format='XHTML'; language='EN'; original_filename=(Split-Path -Leaf $original); processing_filename=(Split-Path -Leaf $normalized); transformation='STRUCTURAL_TEXT_PROCESSING'; transformation_description='XML/XHTML text extraction with whitespace normalization and explicit structural delimiter lines; legal wording not paraphrased, translated, reordered or semantically compressed.'; hash_original=(Get-FileHash -Algorithm SHA256 -LiteralPath $original).Hash; hash_processing=(Get-FileHash -Algorithm SHA256 -LiteralPath $normalized).Hash; validation_status=$validation.status; validation=$validation } | ConvertTo-Json -Depth 8), $utf8NoBom)

    $allStructure += $structureWithPositions
    $allArticles += $articles
    $allMetadata += [PSCustomObject]$validation
}

$structureCsv = $allStructure | ConvertTo-Csv -NoTypeInformation
[IO.File]::WriteAllLines((Join-Path $root 'R4_LEGAL_STRUCTURE_INDEX.csv'), $structureCsv, $utf8NoBom)
$articleCsv = $allArticles | ConvertTo-Csv -NoTypeInformation
[IO.File]::WriteAllLines((Join-Path $root 'R4_ARTICLE_INDEX.csv'), $articleCsv, $utf8NoBom)
$summaryCsv = $allMetadata | ConvertTo-Csv -NoTypeInformation
[IO.File]::WriteAllLines((Join-Path $root 'R4_LEGAL_STRUCTURE_QC.csv'), $summaryCsv, $utf8NoBom)

$allMetadata | Format-Table -AutoSize
