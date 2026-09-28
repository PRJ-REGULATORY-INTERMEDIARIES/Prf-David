$ErrorActionPreference = 'Stop'

$r4 = Split-Path -Parent $PSScriptRoot
$batchRoot = Join-Path $r4 '03_extraction\qa\repair\R4_2E_B1'
$outputPath = Join-Path $batchRoot 'R4_2E_B1_NO_REPAIR_CONTROL_RESULTS_B1_03.csv'

# This controlled unblinding occurs only after B1-03 output freeze record 001.
$results = @(
    [pscustomobject] [ordered] @{
        CONTROL_DIAGNOSTIC = 'NO_REPAIR_CONTROL_DIAGNOSTIC'; BATCH_ID = 'B1-03'; RECORD_ID = 'EXT-000163'
        CONTROL_RESULT = 'DEFECT_FOUND'; ADVANCED_DEFECT_PRESENT = 'YES'
        CONTROL_DEFECT_TYPE = 'PREDICATE_RECONSTRUCTION_ERROR'; CONTROL_DEFECT_SEVERITY = 'MODERATE'
        NOTE = 'Article 60(8) loses a coordinated notification and information predicate and misallocates the two addressees.'
    }
    [pscustomobject] [ordered] @{
        CONTROL_DIAGNOSTIC = 'NO_REPAIR_CONTROL_DIAGNOSTIC'; BATCH_ID = 'B1-03'; RECORD_ID = 'EXT-000660'
        CONTROL_RESULT = 'DEFECT_FOUND'; ADVANCED_DEFECT_PRESENT = 'YES'
        CONTROL_DEFECT_TYPE = 'RELATIONAL_FIELD_ERROR'; CONTROL_DEFECT_SEVERITY = 'MODERATE'
        NOTE = 'Article 66(4) merges the Commission recipient into the object and duplicates it as counterpart and recipient.'
    }
    [pscustomobject] [ordered] @{
        CONTROL_DIAGNOSTIC = 'NO_REPAIR_CONTROL_DIAGNOSTIC'; BATCH_ID = 'B1-03'; RECORD_ID = 'EXT-000986'
        CONTROL_RESULT = 'CLEAN_CONFIRMED'; ADVANCED_DEFECT_PRESENT = 'NO'
        CONTROL_DEFECT_TYPE = ''; CONTROL_DEFECT_SEVERITY = ''
        NOTE = 'The Article 31(1) establishment and legal-personality proposition is structurally retained.'
    }
)

if ($results.Count -ne 3) { throw 'B1-03 must unblind exactly three controls.' }
$results | Export-Csv -LiteralPath $outputPath -NoTypeInformation -Encoding utf8
Write-Output "Rows=$($results.Count)"
Write-Output "SHA256=$((Get-FileHash -LiteralPath $outputPath -Algorithm SHA256).Hash)"
