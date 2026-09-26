$root='C:\PROJETOS\ICM-PMO\10_PROGRAMAS\GP5_JRG\PROJETOS\Prf-David\R3_CLEANROOM'
$sourceRoot=Join-Path $root '01_sources'
$corpusRoot=Join-Path $root '02_corpus'
$utf8=New-Object System.Text.UTF8Encoding($false)
$nl=[Environment]::NewLine
$quote=[char]34

function Write-Utf8([string]$path,[string]$text){ [System.IO.File]::WriteAllText($path,$text,$utf8) }

function Is-PageHeader([string]$line){
  return ($line -match '^\d{1,2}\.\d{1,2}\.\d{4}\s+EN\s+Official Journal of the European Union' -or
          $line -match '^\d{1,2}\.\d{1,2}\.\d{4}\s+Official Journal of the European Union' -or
          $line -match '^L\s+\d+/\d+\s+(?:EN\s+)?Official Journal of the European Union' -or
          $line -match '^Official Journal of the European Union\s+L\s+\d+/\d+' -or
          $line -match '^Official Journal of the European Union$' -or
          $line -match '^EN\s+Official Journal of the European Union$' -or
          $line -match '^\d{1,2}\.\d{1,2}\.\d{4}\s+L\s+\d+/\d+$' -or
          $line -match '^\d{1,2}\.\d{1,2}\.\d{4}$' -or
          $line -match '^L\s+\d+/\d+$')
}

function Normalize-PdfText([string]$raw){
  $lines=$raw -split '\r?\n'
  $clean=New-Object System.Collections.Generic.List[string]
  $removed=0
  $hyphenRepairs=0

  foreach($rawLine in $lines){
    $line=$rawLine.Replace(([char]12).ToString(),'').Trim()
    if($line -eq ''){
      if($clean.Count -eq 0 -or $clean[$clean.Count-1] -ne ''){ [void]$clean.Add('') }
      continue
    }
    if((Is-PageHeader $line) -or $line -match '^EN$' -or
       $line -cmatch '^(I|II|III|IV|V|VI|VII|VIII|IX|X)\s*$' -or
       $line -cmatch '^\(Legislative acts\)$' -or
       $line -cmatch '^(DECISIONS|REGULATIONS)$'){
      $removed++
      continue
    }
    [void]$clean.Add($line)
  }

  for($i=0;$i -lt $clean.Count-1;$i++){
    if($clean[$i] -ne '' -and $clean[$i] -match '-$' -and $clean[$i+1] -match '^[a-z]'){
      $clean[$i]=($clean[$i].Substring(0,$clean[$i].Length-1)+$clean[$i+1])
      $clean.RemoveAt($i+1)
      $hyphenRepairs++
      $i--
    }
  }

  $joined=$clean -join $nl
  while($joined -match '\n{3,}'){$joined=$joined -replace '\n{3,}',($nl+$nl)}

  [pscustomobject]@{
    lines=@($joined -split $nl)
    removed_headers=$removed
    hyphen_repairs=$hyphenRepairs
    footnote_splits=([regex]::Matches($raw,'\([0-9]+\s*\r?\n\s*\)').Count)
    raw_page_breaks=([regex]::Matches($raw,[char]12).Count)
    replacement_chars=([regex]::Matches($raw,[char]0xFFFD).Count)
  }
}

function Get-PageCount([string]$pdf){
  $info=(& pdfinfo $pdf 2>$null) -join $nl
  if($info -match 'Pages:\s+(\d+)'){ return [int]$Matches[1] }
  return 0
}

function Get-ArticleIndex([string]$celex,[string[]]$mdLines){
  $rows=New-Object System.Collections.Generic.List[object]
  $title='';$chapter='';$section='';$article='';$paragraph='';$point='';$subpoint='';$annex=''

  for($i=0;$i -lt $mdLines.Count;$i++){
    $line=$mdLines[$i]
    if($line -match '^\s*# ' -or $line -match '^\s*<!--'){continue}
    $level='';$value=''
    if($line -match '^TITLE\s+(.+)$'){ $title=$Matches[1];$level='title';$value=$title }
    elseif($line -match '^CHAPTER\s+(.+)$'){ $chapter=$Matches[1];$level='chapter';$value=$chapter }
    elseif($line -match '^SECTION\s+(.+)$'){ $section=$Matches[1];$level='section';$value=$section }
    elseif($line -match '^ANNEX(?:\s+([IVXLCDM]+|[A-Z0-9]+))?$'){ $annex=if($Matches[1]){$Matches[1]}else{''};$level='annex';$value=$annex }
    elseif($line -match '^Article\s+([0-9]+[A-Za-z]?)\s*$'){ $article=$Matches[1];$paragraph='';$point='';$subpoint='';$level='article';$value=$article }
    elseif($line -match '^(\d+)\.\s'){ $paragraph=$Matches[1];$point='';$subpoint='';$level='paragraph';$value=$paragraph }
    elseif($line -match '^\(([a-z])\)\s'){ $point=$Matches[1];$subpoint='';$level='point';$value=$point }
    elseif($line -match '^\(([ivxlcdm]+)\)\s'){ $subpoint=$Matches[1];$level='subpoint';$value=$subpoint }
    elseif($line -match '^\((\d+)\)\s'){ $level='recital';$value=$Matches[1] }
    if($level){
      [void]$rows.Add([pscustomobject]@{
        celex_id=$celex;structural_level=$level;title=$title;chapter=$chapter;section=$section
        article=$article;paragraph=$paragraph;point=$point;subpoint=$subpoint;annex=$annex
        value=$value;start_line=($i+1);end_line=$null;start_anchor=('L{0:D6}' -f ($i+1));end_anchor=$null;source_line=$line
      })
    }
  }

  for($j=0;$j -lt $rows.Count;$j++){
    $end=if($j -lt $rows.Count-1){$rows[$j+1].start_line-1}else{$mdLines.Count}
    $rows[$j].end_line=$end
    $rows[$j].end_anchor=('L{0:D6}' -f $end)
  }
  return $rows
}

$cases=@{
 '32003L0087'=@{title='Directive 2003/87/EC of the European Parliament and of the Council of 13 October 2003 establishing a scheme for greenhouse gas emission allowance trading within the Community and amending Council Directive 96/61/EC (Text with EEA relevance)';sha='B3941901E4FE1AF3DEFCFFA323C00A5C6F7F44C51C9EA5785C7A995C3BD68445';url='https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32003L0087&from=EN';retrieved='2026-09-20T16:29:32.7498487-03:00'}
 '32015D1814'=@{title='Decision (EU) 2015/1814 of the European Parliament and of the Council of 6 October 2015 concerning the establishment and operation of a market stability reserve for the Union greenhouse gas emission trading scheme and amending Directive 2003/87/EC (Text with EEA relevance)';sha='BCA2648F3E4A312BF6F31F5270B01D933234E949F4EAC54157A0115086E18036';url='https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32015D1814&from=EN';retrieved='2026-09-20T16:29:34.1244325-03:00'}
 '32018R0842'=@{title='Regulation (EU) 2018/842 of the European Parliament and of the Council of 30 May 2018 on binding annual greenhouse gas emission reductions by Member States from 2021 to 2030 contributing to climate action to meet commitments under the Paris Agreement and amending Regulation (EU) No 525/2013 (Text with EEA relevance)';sha='DD429F4752B9F0F9320CE2FC79152D02A7D34BE262EE86019D98B96E62D07048';url='https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32018R0842&from=EN';retrieved='2026-09-20T16:29:35.6372729-03:00'}
 '32021R1119'=@{title="Regulation (EU) 2021/1119 of the European Parliament and of the Council of 30 June 2021 establishing the framework for achieving climate neutrality and amending Regulations (EC) No 401/2009 and (EU) 2018/1999 (‘European Climate Law’)";sha='855EBC344E9FAF2DB68D75317C08034AF54A1CCE216D8D00C640C3073E639840';url='https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32021R1119&from=EN';retrieved='2026-09-20T16:29:36.9612139-03:00'}
 '32023R0955'=@{title='Regulation (EU) 2023/955 of the European Parliament and of the Council of 10 May 2023 establishing a Social Climate Fund and amending Regulation (EU) 2021/1060';sha='F58712E1156435A418EC1A445F9DBB8D9742FF29E3C8317FF4C00FF929740C49';url='https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A32023R0955&from=EN';retrieved='2026-09-20T16:29:38.6113577-03:00'}
}

$stats=New-Object System.Collections.Generic.List[object]
foreach($celex in $cases.Keys | Sort-Object){
  $c=$cases[$celex]
  $src=Join-Path $sourceRoot "$celex\source_original_en.pdf"
  $dir=Join-Path $corpusRoot $celex
  New-Item -ItemType Directory -Force -Path $dir | Out-Null
  $tmp=Join-Path $env:TEMP ("r3_phase2_"+$celex+".txt")
  & pdftotext -raw $src $tmp 2>$null
  if($LASTEXITCODE -ne 0){throw "pdftotext failed for $celex"}
  $raw=[IO.File]::ReadAllText($tmp)
  $norm=Normalize-PdfText $raw
  $legal=[string[]]$norm.lines

  $op=-1
  for($i=0;$i -lt $legal.Count;$i++){if($legal[$i] -match '^HAVE ADOPTED\b'){$op=$i;break}}
  if($op -lt 0){for($i=0;$i -lt $legal.Count;$i++){if($legal[$i] -match '^Article\s+1\s*$'){$op=$i;break}}}
  if($op -lt 0){throw "Operative start not found for $celex"}

  $meta=@("# R3 structural corpus — $celex",'',"<!-- Generated only from the frozen Phase 1 raw source: source_original_en.pdf -->","<!-- Structural transformation only; no substantive coding has been performed. -->",'')
  $full=@($meta + $legal)
  $rec=@($meta + $legal[0..($op-1)])
  $oper=@($meta + $legal[$op..($legal.Count-1)])
  $fullPath=Join-Path $dir 'act_full.md';$recPath=Join-Path $dir 'recitals.md';$operPath=Join-Path $dir 'operative.md';$numPath=Join-Path $dir 'act_numbered.md';$idxPath=Join-Path $dir 'article_index.csv'
  Write-Utf8 $fullPath (($full -join $nl)+$nl)
  Write-Utf8 $recPath (($rec -join $nl)+$nl)
  Write-Utf8 $operPath (($oper -join $nl)+$nl)
  $numbered=for($i=0;$i -lt $full.Count;$i++){'L{0:D6} | {1}' -f ($i+1),$full[$i]}
  Write-Utf8 $numPath (($numbered -join $nl)+$nl)
  $rows=Get-ArticleIndex $celex $full
  $csv=($rows | Select-Object celex_id,structural_level,title,chapter,section,article,paragraph,point,subpoint,annex,start_anchor,end_anchor,value,source_line | ConvertTo-Csv -NoTypeInformation) -join $nl
  Write-Utf8 $idxPath ($csv+$nl)

  $recNums=@($legal[0..($op-1)] | ForEach-Object {if($_ -match '^\((\d+)\)\s') {[int]$Matches[1]}})
  $articleLabels=@($legal | ForEach-Object {if($_ -match '^Article\s+([0-9]+[A-Za-z]?)\s*$'){$Matches[1]}})
  $articleBases=@($articleLabels | ForEach-Object {if($_ -match '^(\d+)') {[int]$Matches[1]}} | Select-Object -Unique | Sort-Object)
  $annexes=@($legal | Where-Object {$_ -match '^ANNEX(?:\s+[IVXLCDM]+|\s+[A-Z0-9]+)?$'})
  $titles=@($legal | Where-Object {$_ -match '^TITLE\b'})
  $chapters=@($legal | Where-Object {$_ -match '^CHAPTER\b'})
  $sections=@($legal | Where-Object {$_ -match '^SECTION\b'})
  $recMissing=''
  if($recNums.Count -gt 0){$expected=([int]($recNums|Measure-Object -Minimum).Minimum)..([int]($recNums|Measure-Object -Maximum).Maximum);$recMissing=(Compare-Object $expected $recNums | Where-Object SideIndicator -eq '<=' | ForEach-Object InputObject) -join ';'}
  $artMissing=''
  if($articleBases.Count -gt 0){$expected=([int]($articleBases|Measure-Object -Minimum).Minimum)..([int]($articleBases|Measure-Object -Maximum).Maximum);$artMissing=(Compare-Object $expected $articleBases | Where-Object SideIndicator -eq '<=' | ForEach-Object InputObject) -join ';'}

  $legalText=$legal -join $nl
  $pdfPages=Get-PageCount $src
  $sourceHash=(Get-FileHash -Algorithm SHA256 $src).Hash
  $fullHash=(Get-FileHash -Algorithm SHA256 $fullPath).Hash
  $recHash=(Get-FileHash -Algorithm SHA256 $recPath).Hash
  $operHash=(Get-FileHash -Algorithm SHA256 $operPath).Hash
  $numHash=(Get-FileHash -Algorithm SHA256 $numPath).Hash
  $idxHash=(Get-FileHash -Algorithm SHA256 $idxPath).Hash
  $status='CORPUS_TEXT_REQUIRES_REVIEW'
  $fidelity='STRUCTURAL_CHECK_PASS_REVIEW_REQUIRED'
  $notes="page_headers_removed=$($norm.removed_headers); hyphen_line_wraps_repaired=$($norm.hyphen_repairs); raw_page_breaks=$($norm.raw_page_breaks); footnote_split_markers_observed=$($norm.footnote_splits); replacement_characters=$($norm.replacement_chars); missing_recitals=$recMissing; missing_article_bases=$artMissing; tables_and_annexes_preserved_as_extracted_lines"
  $manifest=@("celex_id: $celex","official_title: $quote$($c.title)$quote","source_file: 01_sources/$celex/source_original_en.pdf","source_sha256: $sourceHash","source_url: $quote$($c.url)$quote","retrieval_timestamp: $quote$($c.retrieved)$quote","source_version: ORIGINAL_ACT_AS_ADOPTED","corpus_generation_timestamp: $quote$((Get-Date).ToString('o'))$quote","generated_files:","  - act_full.md","  - recitals.md","  - operative.md","  - act_numbered.md","  - article_index.csv","generated_file_sha256:","  act_full.md: $fullHash","  recitals.md: $recHash","  operative.md: $operHash","  act_numbered.md: $numHash","  article_index.csv: $idxHash","normalization_operations:","  - remove Official Journal page headers and form-feed page separators","  - trim extraction-only leading/trailing whitespace","  - repair line-wrap hyphenation when the continuation begins with lowercase text","  - preserve paragraph, heading, numbering, table and annex line structure","  - no substantive rewriting, summarization or inference","structural_counts:","  recitals: $($recNums.Count)","  articles: $($articleLabels.Count)","  annexes: $($annexes.Count)","  titles: $($titles.Count)","  chapters: $($chapters.Count)","  sections: $($sections.Count)","  words: $([regex]::Matches($legalText,'\S+').Count)","  characters: $($legalText.Length)","quality_checks:","  pdf_pages: $pdfPages","  first_article: $($articleLabels | Select-Object -First 1)","  last_article: $($articleLabels | Select-Object -Last 1)","  first_recital: $($recNums | Select-Object -First 1)","  last_recital: $($recNums | Select-Object -Last 1)","  source_hash_matches_phase1: $($sourceHash -eq $c.sha)","  corpus_status: $status","  source_to_corpus_fidelity: $fidelity")
  Write-Utf8 (Join-Path $dir 'CORPUS_MANIFEST.yaml') (($manifest -join $nl)+$nl)
  [void]$stats.Add([pscustomobject]@{celex_id=$celex;official_title=$c.title;source_sha256=$sourceHash;full_text_sha256=$fullHash;n_recitals=$recNums.Count;n_articles=$articleLabels.Count;n_annexes=$annexes.Count;n_titles=$titles.Count;n_chapters=$chapters.Count;n_sections=$sections.Count;n_words=([regex]::Matches($legalText,'\S+').Count);n_characters=$legalText.Length;pdf_pages=$pdfPages;structural_integrity_status=$fidelity;corpus_status=$status;removed_headers=$norm.removed_headers;hyphen_repairs=$norm.hyphen_repairs;footnote_split_markers=$norm.footnote_splits;missing_recitals=$recMissing;missing_article_bases=$artMissing;notes=$notes})
  Remove-Item -LiteralPath $tmp -Force -ErrorAction SilentlyContinue
}

$reg=($stats | ConvertTo-Csv -NoTypeInformation) -join $nl
Write-Utf8 (Join-Path $root '02_corpus\R3_CORPUS_REGISTER.csv') ($reg+$nl)
$stats | Format-Table celex_id,n_recitals,n_articles,n_annexes,n_words,structural_integrity_status,corpus_status,removed_headers,hyphen_repairs,footnote_split_markers -AutoSize
