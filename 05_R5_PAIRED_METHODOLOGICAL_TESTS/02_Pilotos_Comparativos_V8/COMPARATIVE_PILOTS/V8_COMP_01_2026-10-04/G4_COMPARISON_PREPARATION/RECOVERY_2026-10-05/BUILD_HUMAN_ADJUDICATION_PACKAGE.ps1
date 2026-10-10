$ErrorActionPreference = 'Stop'
$prep = Resolve-Path 'COMPARATIVE_PILOTS/V8_COMP_01_2026-10-04/G4_COMPARISON_PREPARATION'
$out = Join-Path $prep 'HUMAN_ADJUDICATION'
New-Item -ItemType Directory -Path $out -Force | Out-Null
$queue = Import-Csv (Join-Path $prep 'G4_STEP1_HUMAN_REVIEW_QUEUE.csv')
$groups = Import-Csv (Join-Path $prep 'G4_STEP2A/G4_STEP2A_HUMAN_REVIEW_PACKAGE.csv')
$sealed = Import-Csv (Join-Path $prep 'G4_STEP2A/G4_STEP2A_REVIEW_IDENTITY_KEY_SEALED.csv')
$celex = @{
    P03 = 'Directive 91/263/EEC (CELEX 31991L0263)'
    P04 = 'Regulation (EC) No 874/2004 (CELEX 32004R0874)'
}
$master = [System.Collections.Generic.List[object]]::new()
$identity = [System.Collections.Generic.List[object]]::new()

foreach ($q in $queue) {
    $reviewId = 'HV-' + $q.queue_id
    $ids = [regex]::Matches($q.exact_frozen_excerpts, 'CS-P\d{2}-\d{3}') | ForEach-Object Value | Select-Object -Unique
    $outside = if ([string]::IsNullOrWhiteSpace($q.non_frozen_official_text_in_question_NOT_FROZEN_EVIDENCE)) {
        'NONE_IDENTIFIED_IN_SOURCE_QUEUE'
    } else {
        'OUTSIDE_FROZEN_EVIDENCE — contextual only; not part of the common experimental input: ' + $q.non_frozen_official_text_in_question_NOT_FROZEN_EVIDENCE
    }
    $scope = $q.scope_class + '; ' + $q.reason_category + '; ' + $q.uncertainty
    $master.Add([pscustomobject][ordered]@{
        review_item_id = $reviewId
        review_item_type = 'CLAIM_OR_EVIDENCE_SCOPE_ADJUDICATION'
        review_priority = $q.priority
        legal_case = $q.case_id
        legal_instrument_and_celex = $celex[$q.case_id]
        analytical_level = $q.unit_type
        anonymized_claim_or_correspondence = $q.normalized_claim_text
        exact_frozen_evidence = $q.exact_frozen_excerpts
        frozen_statement_ids = ($ids -join '; ')
        additional_context_outside_frozen_evidence = $outside
        disputed_proposition = $q.legal_validity_issue_pending_human_adjudication + ' ' + $q.review_question
        reason_review_required = $q.reason_category + ' — ' + $q.reason_requiring_human_judgment
        admissible_interpretations_or_review_frame = $q.decision_options
        evidence_scope_status = $scope
        human_decision = ''
        reviewer_confidence_1_to_5 = ''
        human_justification = ''
        reviewer_identity_or_code = ''
        review_date_iso = ''
    })
    $identity.Add([pscustomobject][ordered]@{
        review_item_id = $reviewId
        source_type = 'STEP1_HUMAN_REVIEW_QUEUE'
        source_queue_or_group_id = $q.queue_id
        source_step1_unit_ids = $q.step1_unit_id
        original_claim_ids = $q.original_claim_id
        source_cell_ids = $q.cell
        correspondence_group_ids = ''
        identity_notes = 'Restricted provenance mapping; do not distribute with blinded reviewer package.'
    })
}

foreach ($g in $groups) {
    $reviewId = 'HV-COR-' + $g.review_group_id
    $hasP1 = $g.contains_item_pending_P1_human_adjudication -eq 'YES'
    $groupKey = @($sealed | Where-Object review_group_id -eq $g.review_group_id)
    $units = @($groupKey | ForEach-Object unit_id | Select-Object -Unique)
    $claims = @($groupKey | ForEach-Object original_claim_id | Select-Object -Unique)
    $cells = @($groupKey | ForEach-Object source_cell | Select-Object -Unique)
    $outside = if ([string]::IsNullOrWhiteSpace($g.evidence_scope_notes_per_proposition)) {
        'No separate outside-frozen context identified in this review card.'
    } else {
        'HISTORICAL ANALYTIC SCOPE NOTES — not primary legal evidence and not a recommended conclusion: ' + $g.evidence_scope_notes_per_proposition
    }
    $master.Add([pscustomobject][ordered]@{
        review_item_id = $reviewId
        review_item_type = 'PROVISIONAL_CLAIM_CORRESPONDENCE_ADJUDICATION'
        review_priority = $(if ($hasP1) { 'DEPENDENT_ON_P1_ITEM' } else { 'CORRESPONDENCE_REVIEW' })
        legal_case = $g.legal_case
        legal_instrument_and_celex = $celex[$g.legal_case]
        analytical_level = $g.analytical_level
        anonymized_claim_or_correspondence = $g.propositions_anonymised
        exact_frozen_evidence = $g.legal_evidence_exact_excerpts
        frozen_statement_ids = $g.legal_evidence_statement_ids
        additional_context_outside_frozen_evidence = $outside
        disputed_proposition = $g.review_focus + ' ' + $g.reviewer_questions
        reason_review_required = 'Provisional correspondence only; the group is not an equivalence or outcome finding. Review is required for proposition, segmentation, level, evidence-scope, or uncertainty distinctions identified in the matching record.'
        admissible_interpretations_or_review_frame = 'Open human judgment. Where applicable: same proposition; partial/overlapping correspondence; distinct propositions; cross-level correspondence; unmatched/non-comparable; or indeterminate on frozen evidence. These are permissible descriptions, not prescribed answers.'
        evidence_scope_status = 'Historical per-proposition scope notes are separated above; uncertainty=' + $g.uncertainty_level + '; P1 dependency=' + $(if ($hasP1) { 'YES' } else { 'NO' })
        human_decision = ''
        reviewer_confidence_1_to_5 = ''
        human_justification = ''
        reviewer_identity_or_code = ''
        review_date_iso = ''
    })
    $identity.Add([pscustomobject][ordered]@{
        review_item_id = $reviewId
        source_type = 'STEP2A_HUMAN_REVIEW_PACKAGE'
        source_queue_or_group_id = $g.review_group_id
        source_step1_unit_ids = ($units -join '; ')
        original_claim_ids = ($claims -join '; ')
        source_cell_ids = ($cells -join '; ')
        correspondence_group_ids = ($groupKey | ForEach-Object correspondence_group_id | Select-Object -Unique) -join '; '
        identity_notes = 'Restricted provenance mapping; do not distribute with blinded reviewer package.'
    })
}

$masterPath = Join-Path $out 'HUMAN_ADJUDICATION_MASTER.csv'
$master | Export-Csv -LiteralPath $masterPath -NoTypeInformation -Encoding utf8
$p1 = @($master | Where-Object review_priority -eq 'P1')
$p1LinkedGroups = @($master | Where-Object review_priority -eq 'DEPENDENT_ON_P1_ITEM')
@($p1 + $p1LinkedGroups) | Export-Csv -LiteralPath (Join-Path $out 'HUMAN_ADJUDICATION_P1.csv') -NoTypeInformation -Encoding utf8
@($master | Where-Object { $_.review_priority -notin @('P1','DEPENDENT_ON_P1_ITEM') }) | Export-Csv -LiteralPath (Join-Path $out 'HUMAN_ADJUDICATION_LOWER_PRIORITY.csv') -NoTypeInformation -Encoding utf8
$identity | Export-Csv -LiteralPath (Join-Path $out 'HUMAN_REVIEW_IDENTITY_KEY.csv') -NoTypeInformation -Encoding utf8

Write-Output "master=$($master.Count); claim_queue=$($queue.Count); correspondence_groups=$($groups.Count); p1_claims=$($p1.Count); p1_linked_groups=$($p1LinkedGroups.Count); lower_priority=$(@($master | Where-Object { $_.review_priority -notin @('P1','DEPENDENT_ON_P1_ITEM') }).Count)"
