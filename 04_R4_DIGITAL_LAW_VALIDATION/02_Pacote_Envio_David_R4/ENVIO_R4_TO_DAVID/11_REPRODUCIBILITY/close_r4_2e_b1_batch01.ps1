$ErrorActionPreference='Stop'
$r4=Split-Path -Parent $PSScriptRoot;$b1=Join-Path $r4 '03_extraction\qa\repair\R4_2E_B1'
$validation=@(Import-Csv (Join-Path $b1 'R4_2E_B1_ADVANCED_VALIDATION.csv') -Encoding UTF8)
$manifest=@(Import-Csv (Join-Path $b1 'R4_2E_B1_BATCH_MANIFEST.csv') -Encoding UTF8)
$controls=@(Import-Csv (Join-Path $b1 'R4_2E_B1_NO_REPAIR_CONTROL_SAMPLE.csv') -Encoding UTF8)
if($validation.Count -ne 36){throw 'Batch output is incomplete.'}
$controlResults=[System.Collections.Generic.List[object]]::new()
foreach($id in @('EXT-000085','EXT-000529','EXT-000947')){$v=$validation|Where-Object RECORD_ID -eq $id|Select-Object -First 1;$c=$controls|Where-Object RECORD_ID -eq $id|Select-Object -First 1;if(-not $v -or -not $c){throw "Missing control $id"};$result=switch($id){'EXT-000085'{'DEFECT_FOUND'}default{'CLEAN_CONFIRMED'}};$controlResults.Add([pscustomobject][ordered]@{CONTROL_DIAGNOSTIC='NO_REPAIR_CONTROL_DIAGNOSTIC';BATCH_ID='B1-01';CASE_ID=$v.CASE_ID;RECORD_ID=$id;ACT=$v.ACT;SOURCE_REFERENCE=$v.SOURCE_REFERENCE;CONTROL_RESULT=$result;ADVANCED_DEFECT_PRESENT=$v.ADVANCED_DEFECT_PRESENT;PROPOSITION_ANCHOR_CONFIDENCE=$v.PROPOSITION_ANCHOR_CONFIDENCE;NOTE=if($result -eq 'DEFECT_FOUND'){'The control reveals a local proposition-boundary/action/relational misallocation. One B1-01 control does not establish systematic compression failure.'}else{'The frozen source supports the original structural representation for this control.'}})}
$controlResults|Export-Csv (Join-Path $b1 'R4_2E_B1_NO_REPAIR_CONTROL_RESULTS.csv') -NoTypeInformation -Encoding UTF8
$hash=(Get-FileHash (Join-Path $b1 'R4_2E_B1_ADVANCED_VALIDATION.csv') -Algorithm SHA256).Hash
$pending=@($manifest|Where-Object BATCH_ID -ne 'B1-01'|Sort-Object BATCH_ID,ORDER_IN_BATCH)
$completed=@($manifest|Where-Object BATCH_ID -eq 'B1-01'|Sort-Object ORDER_IN_BATCH)
$defects=($validation|Group-Object ADVANCED_DEFECT_PRESENT|ForEach-Object{"$($_.Name)=$($_.Count)"}) -join '; '
$confidence=($validation|Group-Object PROPOSITION_ANCHOR_CONFIDENCE|ForEach-Object{"$($_.Name)=$($_.Count)"}) -join '; '
$template=($validation|Where-Object TEMPLATE_GENERALIZABILITY -ne 'N/A'|Group-Object FAMILY_TEMPLATE_STATUS|ForEach-Object{"$($_.Name)=$($_.Count)"}) -join '; '
$report=@"
# R4.2E-B1 — Partial advanced structural validation report

**Scientific status:** `R4_2E_B1_PARTIAL_ADVANCED_VALIDATION_COMPLETE`  
**Completed batch:** `B1-01` (36 of 143 records)  
**Requested/selected model:** `GPT-5.6 Terra High`  
**Runtime model variant:** `MODEL_VARIANT_NOT_EXPOSED`

## Evidence separation

- R4.2D remains a purposive human diagnostic, not a corpus error rate.
- R4.2E-A remains deterministic triage.
- R4.2E-B0 remains family/workload compression.
- This file reports only the first completed B1 advanced-validation batch; it does not combine those layers into accuracy or prevalence.

## B1-01 results

- Composition: 25 template representatives; 8 individual advanced cases; 3 hidden NO_REPAIR controls.
- Defect decisions: $defects.
- Proposition-anchor confidence: $confidence.
- Template statuses in this partial batch: $template.
- Batch output SHA-256: `$hash`.

The three controls were unblinded only after B1-01 decisions were written. Two were `CLEAN_CONFIRMED`; `EXT-000085` was `DEFECT_FOUND`, reflecting a local source-proposition error. This is one control observation and does not permit a B0 compression-safety conclusion; nine controls remain pending.

No corpus-wide repair was applied. No R/I/T or mechanism coding occurred; Rotem was not consulted. The remaining three batches must preserve their frozen manifests and be reviewed before any global template-coverage or compression-safety assessment.
"@
[IO.File]::WriteAllText((Join-Path $b1 'R4_2E_B1_METHOD_REPORT.md'),$report,(New-Object Text.UTF8Encoding($false)))
$handoff=@"
# R4.2E-B1 handoff state

**Status:** `R4_2E_B1_PARTIAL_ADVANCED_VALIDATION_COMPLETE`

## Provenance

- `MODEL_REQUESTED = GPT-5.6 Terra High`
- `MODEL_RESEARCHER_SELECTED = GPT-5.6 Terra High`
- `MODEL_RUNTIME_VARIANT = MODEL_VARIANT_NOT_EXPOSED`

## Completed

- B1-01: 36 records; output SHA-256 `$hash`.
- Completed IDs: $($completed.RECORD_ID -join ', ').
- Controls unblinded after B1-01 freeze: EXT-000085 = DEFECT_FOUND; EXT-000529 = CLEAN_CONFIRMED; EXT-000947 = CLEAN_CONFIRMED.

## Pending

- B1-02 (36), B1-03 (36), B1-04 (35): 107 records total.
- Pending IDs: $($pending.RECORD_ID -join ', ').
- Pending controls: $((@($controls|Where-Object RECORD_ID -notin @('EXT-000085','EXT-000529','EXT-000947')).RECORD_ID) -join ', ').

## Unresolved scientific questions

1. Complete the remaining nine controls before assigning `B0_COMPRESSION_SAFETY`.
2. Assess all template representatives before calculating potential template repair coverage.
3. Do not alter the 185 HUMAN_ONLY cases; their burden remains reserved pending full B1.
4. Treat B1-01 validated-with-conditions templates as provisional until cross-batch family evidence is complete.

## Firewalls and limits

- `RIT_CODING = NOT_STARTED`
- `MECHANISM_CODING = NOT_STARTED`
- `ROTEM_CODING_CONSULTED = NO`
- `R4_3 = NOT_STARTED`
- `CORPUS_WIDE_REPAIR = NOT_EXECUTED`

No corpus record was repaired. No model substitution occurred. No Git operation occurred. Resume only with the same provenance rules and the frozen batch manifest.
"@
[IO.File]::WriteAllText((Join-Path $b1 'R4_2E_B1_HANDOFF_STATE.md'),$handoff,(New-Object Text.UTF8Encoding($false)))
"Controls=$($controlResults.Count); Pending=$($pending.Count); OutputHash=$hash"
