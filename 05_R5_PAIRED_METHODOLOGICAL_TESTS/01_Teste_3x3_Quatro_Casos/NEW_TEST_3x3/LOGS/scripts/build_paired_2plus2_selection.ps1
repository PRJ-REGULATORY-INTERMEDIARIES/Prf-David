Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

# Builds the prospective 2+2 selection layer from the already-frozen historical
# universe. It does not open or create any V8/RGAM analytical output.
$root = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$out = Join-Path $root '06_PAIRED_TEST_SELECTION'
New-Item -ItemType Directory -Force -Path $out | Out-Null

$master = Import-Csv -LiteralPath (Join-Path $root '01_CASE_UNIVERSE\CASE_UNIVERSE_MASTER.csv')
$domains = Import-Csv -LiteralPath (Join-Path $root '03_DOMAIN_CLASSIFICATION\CASE_DOMAIN_CLASSIFICATION.csv')
$provenance = Import-Csv -LiteralPath (Join-Path $root '01_CASE_UNIVERSE\CASE_SOURCE_PROVENANCE.csv')
$domainByCase = @{}
foreach ($d in $domains) { $domainByCase[$d.canonical_case_id] = $d }

function NumOrNeg([string]$value) {
    if ([string]::IsNullOrWhiteSpace($value)) { return -1 }
    return [int]$value
}
function Csv([object[]]$rows, [string]$name) {
    $rows | Export-Csv -NoTypeInformation -Encoding utf8 -LiteralPath (Join-Path $out $name)
}
function CompareStatus($row) {
    if ($row.comparability_stratum -eq 'S1_R3_CLEANROOM_FROZEN') { return 'DIRECTLY_COMPARABLE' }
    if ($row.comparability_stratum -eq 'S2_R2_RESEARCHER_REVIEW') { return 'CONDITIONALLY_COMPARABLE' }
    if (-not [string]::IsNullOrWhiteSpace($row.intermediation_relations)) { return 'HISTORICAL_COUNT_NOT_DIRECTLY_COMPARABLE' }
    return 'HISTORICAL_COUNT_NOT_AVAILABLE'
}
function StableRank([object[]]$rows) {
    $rank = 0
    $sortProperties = @(
        @{Expression = { NumOrNeg $_.historical_intermediation_count }; Descending = $true}
        @{Expression = { NumOrNeg $_.actors }; Descending = $true}
        @{Expression = { NumOrNeg $_.intermediaries }; Descending = $true}
        @{Expression = { NumOrNeg $_.targets }; Descending = $true}
        @{Expression = { NumOrNeg $_.total_relations }; Descending = $true}
        @{Expression = { $_.canonical_case_id }; Descending = $false}
    )
    return @($rows | Sort-Object -Property $sortProperties |
        ForEach-Object { $rank++; $_ | Add-Member -NotePropertyName selection_rank -NotePropertyValue $rank -PassThru })
}
function PrimaryIntermediationSource($cvId) {
    return $provenance | Where-Object { $_.cv_id -eq $cvId -and $_.metric -eq 'intermediation_relations' } | Select-Object -First 1
}

# The historical universe is deliberately limited to previously studied,
# canonical versions. Rotem-only and prohibited V8-stage records remain outside
# the amendment's candidate universe.
$base = @($master | Where-Object {
    $_.is_canonical_version -eq 'YES' -and $_.disposition -ne 'OTHER_DOCUMENTED_EXCLUSION'
} | ForEach-Object {
    $d = $domainByCase[$_.canonical_case_id]
    $src = PrimaryIntermediationSource $_.cv_id
    [PSCustomObject]@{
        cv_id = $_.cv_id
        canonical_case_id = $_.canonical_case_id
        instrument = $_.instrument_title
        primary_domain_code = $d.level1_code_primary
        primary_domain = $d.level1_domain_primary
        alternate_domain_code = $d.level1_code_alternate
        alternate_domain = $d.level1_domain_alternate
        historical_intermediation_count = $_.intermediation_relations
        actors = $_.actors
        intermediaries = $_.intermediaries
        targets = $_.targets
        total_relations = $_.relations
        extraction_family = $_.source_family
        extraction_version = $_.extraction_version
        corpus_scope = $_.corpus_scope
        methodology_codebook = $_.codebook_ref
        historical_comparability_status = CompareStatus $_
        prior_disposition = $_.disposition
        case_record_provenance_ref = $_.metric_provenance_ref
        source_file = $src.source_files
        source_sha256 = $src.source_file_sha256
        source_note = $src.notes
    }
})
Csv $base 'PAIRED_2PLUS2_CANDIDATE_UNIVERSE.csv'

# Categories use the pre-existing domain assignment (primary or documented
# alternate); no legal text or analytical output is reinterpreted here.
$climate = @($base | Where-Object {
    $_.primary_domain_code -eq 'D01' -or $_.alternate_domain_code -eq 'D01'
} | Where-Object { $_.historical_intermediation_count -ne '' })
$digital = @($base | Where-Object {
    $_.primary_domain_code -eq 'D05' -or $_.alternate_domain_code -eq 'D05'
} | Where-Object { $_.historical_intermediation_count -ne '' })
$other = @($base | Where-Object {
    $_.primary_domain_code -ne 'D01' -and $_.alternate_domain_code -ne 'D01' -and
    $_.primary_domain_code -ne 'D05' -and $_.alternate_domain_code -ne 'D05'
} | Where-Object { $_.historical_intermediation_count -ne '' })

$climateRank = StableRank $climate
$digitalRank = StableRank $digital
$otherRank = StableRank $other
Csv $climateRank 'CLIMATE_CASE_RANKING.csv'
Csv $digitalRank 'AI_DIGITAL_CASE_RANKING.csv'
Csv $otherRank 'OTHER_DOMAIN_CASE_RANKING.csv'

$climate1 = $climateRank | Select-Object -First 1
$climate2 = $climateRank | Select-Object -Skip 1 -First 1
$transferAi = $digitalRank | Select-Object -First 1
$transferOther = $otherRank | Select-Object -First 1

$selected = @(
    [PSCustomObject]@{slot='CLIMATE-1';selection_rank_in_block=$climate1.selection_rank;canonical_case_id=$climate1.canonical_case_id;instrument=$climate1.instrument;substantive_domain='Climate governance / EU climate-related public-finance management';historical_intermediation_count=$climate1.historical_intermediation_count;actors=$climate1.actors;intermediaries=$climate1.intermediaries;targets=$climate1.targets;total_relations=$climate1.total_relations;extraction_family=$climate1.extraction_family;extraction_version=$climate1.extraction_version;corpus_scope=$climate1.corpus_scope;comparability_status=$climate1.historical_comparability_status;source_file=$climate1.source_file;source_sha256=$climate1.source_sha256}
    [PSCustomObject]@{slot='CLIMATE-2';selection_rank_in_block=$climate2.selection_rank;canonical_case_id=$climate2.canonical_case_id;instrument=$climate2.instrument;substantive_domain='Climate governance / carbon-border measure (primary domain: external trade & customs; documented alternate: climate)';historical_intermediation_count=$climate2.historical_intermediation_count;actors=$climate2.actors;intermediaries=$climate2.intermediaries;targets=$climate2.targets;total_relations=$climate2.total_relations;extraction_family=$climate2.extraction_family;extraction_version=$climate2.extraction_version;corpus_scope=$climate2.corpus_scope;comparability_status=$climate2.historical_comparability_status;source_file=$climate2.source_file;source_sha256=$climate2.source_sha256}
    [PSCustomObject]@{slot='TRANSFER-AI';selection_rank_in_block=$transferAi.selection_rank;canonical_case_id=$transferAi.canonical_case_id;instrument=$transferAi.instrument;substantive_domain='Internet naming & domain governance (digital-governance transfer case; not AI-specific)';historical_intermediation_count=$transferAi.historical_intermediation_count;actors=$transferAi.actors;intermediaries=$transferAi.intermediaries;targets=$transferAi.targets;total_relations=$transferAi.total_relations;extraction_family=$transferAi.extraction_family;extraction_version=$transferAi.extraction_version;corpus_scope=$transferAi.corpus_scope;comparability_status=$transferAi.historical_comparability_status;source_file=$transferAi.source_file;source_sha256=$transferAi.source_sha256}
    [PSCustomObject]@{slot='TRANSFER-OTHER';selection_rank_in_block=$transferOther.selection_rank;canonical_case_id=$transferOther.canonical_case_id;instrument=$transferOther.instrument;substantive_domain='Telecommunications, radio/terminal equipment & product conformity';historical_intermediation_count=$transferOther.historical_intermediation_count;actors=$transferOther.actors;intermediaries=$transferOther.intermediaries;targets=$transferOther.targets;total_relations=$transferOther.total_relations;extraction_family=$transferOther.extraction_family;extraction_version=$transferOther.extraction_version;corpus_scope=$transferOther.corpus_scope;comparability_status=$transferOther.historical_comparability_status;source_file=$transferOther.source_file;source_sha256=$transferOther.source_sha256}
)
Csv $selected 'PAIRED_2PLUS2_SELECTED_CASES.csv'

$amendment = @'
# NEW TEST 3x3
## PROTOCOL AMENDMENT 01 — PAIRED V8–RGAM 2+2 DESIGN

**Date:** 2026-10-06  
**Project:** PRJ-David / Law and Governance Architectures  
**Research coordinator:** Igor Caires Machado  
**Status:** Prospective methodological amendment adopted before any new V8 or RGAM execution under this design.

## Purpose and preserved history

The historical three-domain protocol, its files, and its terminal gate — `TEST_3X3_SELECTION_BLOCKED / METHODOLOGICAL_REVIEW_REQUIRED` — remain preserved. They are not overwritten or retrospectively reinterpreted. No prior V8, RGAM or architectural output is used for this amendment.

This amendment adopts a paired comparative design: the same four legal cases are to be analysed independently by V8 and by RGAM. The question is incremental analytical value, not presumed superiority. The design therefore comprises **4 cases × 2 procedures = 8 principal analytical executions** after this selection stage.

## Selection rule

Two climate-governance cases, one AI/digital-governance case and one other-domain case are selected exclusively from previously studied, canonical case versions. The primary criterion is the historical count of regulatory-intermediation relations. Only an exact tie at a selection boundary is resolved, in order, by actors, intermediaries, targets, total relations and then stable canonical case ID.

Historical counts are retained with their extraction family, codebook, corpus scope, source, and comparability classification. A larger count is only an ex ante opportunity for observation; it is not evidence of complexity, quality, architecture, or anticipated advantage for either procedure. Counts from distinct extraction families are not represented as directly comparable when they are not.

## Independence and stop condition

This layer contains no V8 or RGAM execution and creates no new intermediation relation. Future V8 and RGAM executions must use separated analytical contexts and must not consult one another's outputs. Case substitution is barred except for a documented objective source failure; it cannot be based on later analytical performance.

**Selection gate after the accompanying freeze:** `PAIRED_2PLUS2_SELECTION_FROZEN / V8_NOT_STARTED / RGAM_NOT_STARTED`.
'@
Set-Content -LiteralPath (Join-Path $root '00_PROTOCOL\PROTOCOL_AMENDMENT_01_PAIRED_V8_RGAM_2PLUS2.md') -Value $amendment -Encoding utf8

$decision = @'
# PAIRED 2+2 SELECTION DECISION

**Date:** 2026-10-06  
**Historical input only:** `01_CASE_UNIVERSE/CASE_UNIVERSE_MASTER.csv`, `CASE_SOURCE_PROVENANCE.csv`, and the pre-existing domain classification.

## Decision

| Slot | Case | Historical intermediation count | Selection basis | Comparability status |
|---|---|---:|---|---|
| CLIMATE-1 | CASE-32023R0955 — Regulation (EU) 2023/955 establishing a Social Climate Fund | 5 | highest climate-relevant count; tied at 5 with CBAM, then actors 34 > 16 | DIRECTLY_COMPARABLE |
| CLIMATE-2 | CASE-32023R0956 — Regulation (EU) 2023/956 establishing a carbon border adjustment mechanism (CBAM) | 5 | next climate-relevant case after the documented tie-break | CONDITIONALLY_COMPARABLE |
| TRANSFER-AI | CASE-32004R0874 — Commission Regulation (EC) No 874/2004 governing the .eu Top Level Domain | 6 | highest historical-count candidate in the digital-governance set | HISTORICAL_COUNT_NOT_DIRECTLY_COMPARABLE |
| TRANSFER-OTHER | CASE-31986L0361 — Council Directive 86/361/EEC on terminal-equipment type approval | 3 | highest non-climate, non-digital candidate; exact tie with CASE-31991L0263 survives all available registered metrics, resolved by canonical ID | HISTORICAL_COUNT_NOT_DIRECTLY_COMPARABLE |

## Material limitations carried forward

1. `CLIMATE-1` is R3/S1 and directly comparable inside S1; `CLIMATE-2` is R2/S2, whose bridge with R3 failed. The 5–5 tie is deterministically resolved as the amended rule directs, but the two counts are not evidence of direct cross-pipeline equivalence.
2. `TRANSFER-AI` is the protocol's slot label only. The selected act is an internet-domain-governance case, not an AI-specific act. GDPR, DSA and the AI Act had no historical intermediation count in the registered universe; the selected count comes from six purposively selected provisions and flags derived R-I-T candidates rather than adjudicated positive relations.
3. `TRANSFER-OTHER` likewise comes from a limited-provision PILOT record. Its target metric was not recorded. Its tie with CASE-31991L0263 is therefore resolved by stable canonical ID after the shared recorded tie-break values (3, 6, 3, missing, 4).
4. No architectural finding, V8 finding, RGAM finding, centrality, modularity, hierarchy, topology, or expected procedure performance informed selection.

## Result

`PAIRED_2PLUS2_SELECTION_FROZEN / V8_NOT_STARTED / RGAM_NOT_STARTED`
'@
Set-Content -LiteralPath (Join-Path $out 'PAIRED_2PLUS2_SELECTION_DECISION.md') -Value $decision -Encoding utf8

$freeze = @'
# PAIRED 2+2 SELECTION FREEZE

**Date:** 2026-10-06

The four cases in `PAIRED_2PLUS2_SELECTED_CASES.csv` are frozen under Protocol Amendment 01. Their selection used only previously recorded counts and the deterministic ranking files in this directory. The historical 3×3 blocked gate remains unchanged.

No V8 or RGAM execution has begun. A substitution requires a documented objective source failure; later analytical output cannot justify substitution.

**Gate:** `PAIRED_2PLUS2_SELECTION_FROZEN / V8_NOT_STARTED / RGAM_NOT_STARTED`.
'@
Set-Content -LiteralPath (Join-Path $out 'PAIRED_2PLUS2_SELECTION_FREEZE.md') -Value $freeze -Encoding utf8

$manifestNames = @(
    '..\00_PROTOCOL\PROTOCOL_AMENDMENT_01_PAIRED_V8_RGAM_2PLUS2.md',
    'PAIRED_2PLUS2_CANDIDATE_UNIVERSE.csv', 'CLIMATE_CASE_RANKING.csv',
    'AI_DIGITAL_CASE_RANKING.csv', 'OTHER_DOMAIN_CASE_RANKING.csv',
    'PAIRED_2PLUS2_SELECTION_DECISION.md', 'PAIRED_2PLUS2_SELECTED_CASES.csv',
    'PAIRED_2PLUS2_SELECTION_FREEZE.md'
)
$manifest = foreach ($name in $manifestNames) {
    $path = Join-Path $out $name
    $item = Get-Item -LiteralPath $path
    [PSCustomObject]@{
        relative_path = if ($name.StartsWith('..\')) { '00_PROTOCOL/PROTOCOL_AMENDMENT_01_PAIRED_V8_RGAM_2PLUS2.md' } else { "06_PAIRED_TEST_SELECTION/$name" }
        bytes = $item.Length
        sha256 = (Get-FileHash -Algorithm SHA256 -LiteralPath $path).Hash.ToLowerInvariant()
    }
}
$manifestPath = Join-Path $out 'PAIRED_2PLUS2_SELECTION_FREEZE_MANIFEST.csv'
$manifest | Export-Csv -NoTypeInformation -Encoding utf8 -LiteralPath $manifestPath
$manifestHash = (Get-FileHash -Algorithm SHA256 -LiteralPath $manifestPath).Hash.ToLowerInvariant()
Set-Content -LiteralPath (Join-Path $out 'PAIRED_2PLUS2_SELECTION_FREEZE_MANIFEST_SHA256.txt') -Value "$manifestHash  PAIRED_2PLUS2_SELECTION_FREEZE_MANIFEST.csv" -Encoding ascii

Write-Output "Freeze manifest SHA-256: $manifestHash"
