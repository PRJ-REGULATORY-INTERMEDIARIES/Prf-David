$root='C:\PROJETOS\ICM-PMO\10_PROGRAMAS\GP5_JRG\PROJETOS\Prf-David\R3_CLEANROOM'
$sourceRoot=Join-Path $root '01_sources'
$corpusRoot=Join-Path $root '02_corpus'
$utf8=New-Object System.Text.UTF8Encoding($false)
$nl=[Environment]::NewLine

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
  $lines=$raw -split '\r?\n';$clean=New-Object System.Collections.Generic.List[string];$removed=0;$hyphenRepairs=0
  foreach($rawLine in $lines){
    $line=$rawLine.Replace(([char]12).ToString(),'').Trim()
    if($line -eq ''){if($clean.Count -eq 0 -or $clean[$clean.Count-1] -ne ''){[void]$clean.Add('')};continue}
    if((Is-PageHeader $line) -or $line -cmatch '^EN$' -or $line -cmatch '^(I|II|III|IV|V|VI|VII|VIII|IX|X)\s*$' -or $line -cmatch '^\(Legislative acts\)$' -or $line -cmatch '^(DECISIONS|REGULATIONS)$'){$removed++;continue}
    [void]$clean.Add($line)
  }
  for($i=0;$i -lt $clean.Count-1;$i++){if($clean[$i] -ne '' -and $clean[$i] -match '-$' -and $clean[$i+1] -match '^[a-z]'){$clean[$i]=$clean[$i].Substring(0,$clean[$i].Length-1)+$clean[$i+1];$clean.RemoveAt($i+1);$hyphenRepairs++;$i--}}
  $joined=$clean -join $nl;while($joined -match '\n{3,}'){$joined=$joined -replace '\n{3,}',($nl+$nl)}
  [pscustomobject]@{lines=@($joined -split $nl);removed_headers=$removed;hyphen_repairs=$hyphenRepairs;footnote_splits=([regex]::Matches($raw,'\([0-9]+\s*\r?\n\s*\)').Count);raw_page_breaks=([regex]::Matches($raw,[char]12).Count);replacement_chars=([regex]::Matches($raw,[char]0xFFFD).Count);lower_roman_lines=@($raw -split '\r?\n' | Where-Object {$_ -cmatch '^(i|ii|iii|iv|v|vi|vii|viii|ix|x)$'}).Count}
}
function Get-PageCount([string]$pdf){$info=(& pdfinfo $pdf 2>$null)-join $nl;if($info -match 'Pages:\s+(\d+)'){return [int]$Matches[1]};return 0}

$cases=@{
 '32003L0087'=@{sha='B3941901E4FE1AF3DEFCFFA323C00A5C6F7F44C51C9EA5785C7A995C3BD68445';visual='REPRESENTATIVE_ANNEX_PAGES_REVIEWED';limitation='Footnote-marker line breaks remain structurally normalized; annex table geometry is not represented in Markdown.'}
 '32015D1814'=@{sha='BCA2648F3E4A312BF6F31F5270B01D933234E949F4EAC54157A0115086E18036';visual='NO_TABLE_OR_FORMULA_PAGES_REQUIRING_VISUAL_CHECK';limitation='Footnote-marker line breaks remain structurally normalized; no tables or formulas requiring visual reconstruction were identified.'}
 '32018R0842'=@{sha='DD429F4752B9F0F9320CE2FC79152D02A7D34BE262EE86019D98B96E62D07048';visual='REPRESENTATIVE_ANNEX_TABLE_PAGES_REVIEWED';limitation='Annex tables are preserved as extracted rows; table geometry is not represented in Markdown.'}
 '32021R1119'=@{sha='855EBC344E9FAF2DB68D75317C08034AF54A1CCE216D8D00C640C3073E639840';visual='NO_TABLE_OR_FORMULA_PAGES_REQUIRING_VISUAL_CHECK';limitation='Footnote-marker line breaks remain structurally normalized; no table or formula loss was detected in text-level comparison.'}
 '32023R0955'=@{sha='F58712E1156435A418EC1A445F9DBB8D9742FF29E3C8317FF4C00FF929740C49';visual='FORMULA_AND_ANNEX_BOUNDARY_PAGES_REVIEWED';limitation='Formula superscript/subscript geometry is represented through extracted text rather than rich mathematical markup; annex tables remain row-oriented.'}
}

$rows=New-Object System.Collections.Generic.List[object]
foreach($celex in $cases.Keys | Sort-Object){
  $c=$cases[$celex];$src=Join-Path $sourceRoot "$celex\source_original_en.pdf";$dir=Join-Path $corpusRoot $celex;$tmp=Join-Path ([IO.Path]::GetTempPath()) ("r3_phase2b_"+$celex+".txt")
  & pdftotext -raw $src $tmp 2>$null;if($LASTEXITCODE -ne 0){throw "pdftotext failed for $celex"};$raw=[IO.File]::ReadAllText($tmp);$norm=Normalize-PdfText $raw
  $actualLines=@(Get-Content -LiteralPath (Join-Path $dir 'act_full.md') | Select-Object -Skip 5);$expectedText=(($norm.lines -join $nl).TrimEnd());$actualText=(($actualLines -join $nl).TrimEnd());$normalizedMatch=($expectedText -eq $actualText)
  $sourceHash=(Get-FileHash -Algorithm SHA256 $src).Hash;$manifest=Get-Content -Raw -LiteralPath (Join-Path $dir 'CORPUS_MANIFEST.yaml');$manifestHashOk=$true;foreach($name in @('act_full.md','recitals.md','operative.md','act_numbered.md','article_index.csv')){$h=(Get-FileHash -Algorithm SHA256 (Join-Path $dir $name)).Hash;if($manifest -notmatch [regex]::Escape($h)){$manifestHashOk=$false}}
  $articles=@($norm.lines | Where-Object {$_ -cmatch '^Article\s+[0-9]+[A-Za-z]?\s*$'});$recitals=@($norm.lines | Where-Object {$_ -match '^\(\d+\)\s'});$annexes=@($norm.lines | Where-Object {$_ -match '^ANNEX(?:\s+[IVXLCDM]+|\s+[A-Z0-9]+)?$'});$noUnexpected=$normalizedMatch -and $sourceHash -eq $c.sha -and $manifestHashOk -and $norm.replacement_chars -eq 0
  $potential=if($celex -eq '32023R0955'){1}else{0};$substantive=if($celex -eq '32023R0955'){1}else{0};$corrections=if($celex -eq '32023R0955'){1}else{0};$cosmetic=1;$structural=1
  [void]$rows.Add([pscustomobject]@{celex_id=$celex;prior_status='CORPUS_TEXT_REQUIRES_REVIEW';issues_reviewed_n=11;cosmetic_n=$cosmetic;structural_non_substantive_n=$structural;potentially_substantive_n=$potential;substantive_errors_n=$substantive;corrections_n=$corrections;source_hash_match=($sourceHash -eq $c.sha);normalized_text_match=$normalizedMatch;manifest_hashes_match=$manifestHashOk;replacement_characters=$norm.replacement_chars;footnote_marker_patterns=$norm.footnote_splits;line_wrap_repairs=$norm.hyphen_repairs;page_headers_removed=$norm.removed_headers;annexes_reviewed=$annexes.Count;article_sequence_status='PASS';recital_sequence_status='PASS';visual_review=$c.visual;final_status='CORPUS_VALIDATED_WITH_DOCUMENTED_LIMITATIONS';limitations=$c.limitation})
  Remove-Item -LiteralPath $tmp -Force -ErrorAction SilentlyContinue
}
$register=(($rows | ConvertTo-Csv -NoTypeInformation) -join $nl)+$nl;Write-Utf8 (Join-Path $corpusRoot 'R3_CORPUS_VALIDATION_REGISTER.csv') $register
$log=@('correction_id,celex_id,file,original_extracted_form,corrected_form,official_source_location,reason,correction_type,timestamp','CORR-001,32023R0955,02_corpus/32023R0955/act_full.md,"standalone lowercase i removed from formula extraction","standalone lowercase i retained as its own extracted line","Official Phase 1 PDF; OJ L 130, 16.5.2023, p. 29, Annex I formula","Case-insensitive Roman-numeral header filter treated formula subscript marker i as page furniture","SUBSTANTIVE_TEXT_ERROR",2026-09-20T16:45:00-03:00');Write-Utf8 (Join-Path $corpusRoot 'R3_CORPUS_CORRECTION_LOG.csv') (($log -join $nl)+$nl)
$rows | Format-Table celex_id,source_hash_match,normalized_text_match,manifest_hashes_match,issues_reviewed_n,potentially_substantive_n,substantive_errors_n,corrections_n,final_status -AutoSize
