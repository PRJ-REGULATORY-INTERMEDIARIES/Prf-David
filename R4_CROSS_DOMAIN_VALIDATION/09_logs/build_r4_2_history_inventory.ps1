param(
    [string]$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path,
    [string]$ZipPath = 'G:\Meu Drive\VSCODE_WORK_IN_PROGRESS\PRJ-DAVID-R3.zip'
)

$workspace = Join-Path $RepoRoot 'R4_CROSS_DOMAIN_VALIDATION'
$staging = Join-Path $workspace '01_baseline\R3_HISTORY_STAGING'
$inventoryPath = Join-Path $workspace 'R4_R3_HISTORY_FILE_INVENTORY.csv'
$metadataPath = Join-Path $workspace 'R4_R3_HISTORY_ARCHIVE_METADATA.json'

if (-not (Test-Path -LiteralPath $ZipPath -PathType Leaf)) {
    throw "Historical ZIP not found: $ZipPath"
}
if (-not (Test-Path -LiteralPath $staging -PathType Container)) {
    throw "Historical staging directory not found: $staging"
}

$zip = Get-Item -LiteralPath $ZipPath
$zipHash = (Get-FileHash -LiteralPath $ZipPath -Algorithm SHA256).Hash
$stagingRoot = (Resolve-Path -LiteralPath $staging).Path.TrimEnd('\')

function Get-AnalyticalFunction([string]$relativePath) {
    $normalized = $relativePath.Replace('\', '/')
    $parts = $normalized.Split('/')
    $layer = ($parts | Where-Object { $_ -match '^(00_governance|01_sources|02_corpus|03_instrument_profiles|04_actor_register|05_law_intermediary|06_relations|07_mechanisms|08_configuration|09_research_questions|10_dataset|12_audits)$' } | Select-Object -First 1)
    switch -Regex ($layer) {
        '^00_governance$' { return 'governance_and_researcher_decisions' }
        '^01_sources$' { return 'source_provenance' }
        '^02_corpus$' { return 'corpus_reconstruction_and_validation' }
        '^03_instrument_profiles$' { return 'whole_instrument_profiling' }
        '^04_actor_register$' { return 'actor_layer' }
        '^05_law_intermediary$' { return 'law_intermediary_layer' }
        '^06_relations$' { return 'relation_and_RIT_layer' }
        '^07_mechanisms$' { return 'mechanism_layer' }
        '^08_configuration$' { return 'configuration_layer' }
        '^09_research_questions$' { return 'dataset_architecture_and_research_questions' }
        '^10_dataset$' { return 'David_facing_dataset_and_presentation_layer' }
        '^12_audits$' { return 'audit_history_and_quality_gates' }
        default { return 'root_or_other_historical_artifact' }
    }
}

$files = Get-ChildItem -LiteralPath $stagingRoot -Recurse -File | Sort-Object FullName
$records = foreach ($file in $files) {
    $relative = $file.FullName.Substring($stagingRoot.Length).TrimStart('\').Replace('\', '/')
    $extension = $file.Extension.ToLowerInvariant()
    [pscustomobject]@{
        archive_relative_path = $relative
        local_staging_path = $file.FullName
        file_name = $file.Name
        extension = if ($extension) { $extension } else { '[none]' }
        file_type = switch ($extension) {
            '.csv' { 'delimited_table' }
            '.xlsx' { 'spreadsheet_workbook' }
            '.docx' { 'word_document' }
            '.md' { 'markdown_document' }
            '.txt' { 'plain_text' }
            '.json' { 'json_record' }
            '.yaml' { 'yaml_record' }
            '.xml' { 'xml_record' }
            '.xhtml' { 'xhtml_source' }
            default { 'other_file' }
        }
        analytical_function = Get-AnalyticalFunction $relative
        size_bytes = $file.Length
        last_write_time_utc = $file.LastWriteTimeUtc.ToString('o')
        sha256 = (Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash
    }
}

$records | Export-Csv -LiteralPath $inventoryPath -NoTypeInformation -Encoding UTF8

$metadata = [ordered]@{
    archive_path = $zip.FullName
    archive_file_name = $zip.Name
    archive_size_bytes = $zip.Length
    archive_last_write_time_utc = $zip.LastWriteTimeUtc.ToString('o')
    archive_sha256 = $zipHash
    extraction_staging = $stagingRoot
    extraction_preserved_archive_relative_paths = $true
    inventory_file = $inventoryPath
    inventoried_file_count = $records.Count
    inventory_generated_utc = [DateTime]::UtcNow.ToString('o')
}
$metadata | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath $metadataPath -Encoding UTF8

Write-Output "Inventory written: $inventoryPath"
Write-Output "Metadata written: $metadataPath"
Write-Output "Files inventoried: $($records.Count)"
