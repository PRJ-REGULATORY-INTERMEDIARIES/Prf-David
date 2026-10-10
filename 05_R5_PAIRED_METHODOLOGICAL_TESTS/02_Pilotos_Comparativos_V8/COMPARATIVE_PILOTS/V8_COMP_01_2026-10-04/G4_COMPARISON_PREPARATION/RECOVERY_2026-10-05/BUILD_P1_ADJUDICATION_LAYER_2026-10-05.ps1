$ErrorActionPreference = 'Stop'
$exp = Resolve-Path 'COMPARATIVE_PILOTS/V8_COMP_01_2026-10-04'
$prep = Resolve-Path (Join-Path $exp 'G4_COMPARISON_PREPARATION')
$human = Resolve-Path (Join-Path $prep 'HUMAN_ADJUDICATION')
$step2a = Resolve-Path (Join-Path $prep 'G4_STEP2A')
$srcCsv = Join-Path $human 'V8_COMP_01_HUMAN_ADJUDICATION_P1_FILLED_2026-10-05.csv'
$srcMemo = Join-Path $human 'V8_COMP_01_HUMAN_ADJUDICATION_P1_DECISION_MEMO_2026-10-05.md'
$expectedCsv = '38D56989DFD861ACB2B408FEBAB2EE524A0669225299EDB2E83F008787E5ECD1'
$expectedMemo = '245FFB0453937A9D7821138AA4002536A76BE98FBFDC6D09D90A1F19EDCE74AF'
if ((Get-FileHash $srcCsv -Algorithm SHA256).Hash -ne $expectedCsv) { throw 'Human P1 CSV hash did not match the expected source hash.' }
if ((Get-FileHash $srcMemo -Algorithm SHA256).Hash -ne $expectedMemo) { throw 'Human decision memo hash did not match the expected source hash.' }

$decisions = Import-Csv $srcCsv
$queue = Import-Csv (Join-Path $prep 'G4_STEP1_HUMAN_REVIEW_QUEUE.csv')
$common = Import-Csv (Join-Path $exp 'COMMON_STATEMENT_REGISTER.csv')
$groups = Import-Csv (Join-Path $step2a 'G4_STEP2A_HUMAN_REVIEW_PACKAGE.csv')
$keys = Import-Csv (Join-Path $step2a 'G4_STEP2A_REVIEW_IDENTITY_KEY_SEALED.csv')
$candidateGroups = Import-Csv (Join-Path $step2a 'G4_STEP2A_CORRESPONDENCE_GROUPS.csv')
$expectedItems = @('R-P03-04','CL-P03-02','CL-P03-03','CL-P03-02#CORE','R-P04-05','CL-P04-02','CL-P04-02#CORE','RG-06','RG-10')
if ($decisions.Count -ne 9) { throw "Expected 9 source rows including two pending cards; found $($decisions.Count)." }
if ((@($decisions.review_item_id | Sort-Object -Unique)).Count -ne 9) { throw 'Duplicate or missing source item IDs.' }
foreach ($id in $expectedItems) { if ($id -notin $decisions.review_item_id) { throw "Missing source adjudication row $id" } }

$derived = [System.Collections.Generic.List[object]]::new()
foreach ($d in $decisions) {
    $sourceQueueRow = @($queue | Where-Object { $_.priority -eq 'P1' -and $_.original_claim_id -eq $d.review_item_id })
    if ($d.human_status -eq 'ADJUDICATED' -and $sourceQueueRow.Count -ne 1) { throw "Expected one P1 queue row for $($d.review_item_id); found $($sourceQueueRow.Count)." }
    $sourceQueueRow = $sourceQueueRow | Select-Object -First 1
    $type = 'P1_LEGAL_OR_CONFIGURATION_ITEM'
    $verification = 'HUMAN_DISPOSITION_RETAINED; no additional conditional test required'
    $basis = 'Source human memo and filled register; frozen evidence-scope decision remains researcher adjudication, not independent external validation.'
    $primary = 'NO'
    $sensitivity = 'NOT_APPLICABLE'
    $provenance = 'HISTORICAL_PROVENANCE_RETAINED; see original claim/warrant and condition.'
    $unitStatus = if ($d.review_item_id -like '*#CORE') { 'STEP0_DERIVED' } else { 'ORIGINAL_OR_GROUP_ITEM' }
    $effect = 'No comparative outcome assigned at this gate.'
    switch ($d.review_item_id) {
        'R-P03-04' {
            $verification = 'PASS_CONDITIONAL_INTRACORPUS_COREFERENCE'
            $basis = 'CS-P03-003 and CS-P03-005/006 only: both use "the quality system"; the frozen Annex III point 4.3 excerpt explicitly says the manufacturer maintains and applies that system. This resolves the manufacturer as referent without points 3.1/3.2. The registered scope dictionary permits referent resolution through other frozen statements. The repeated definite phrase is treated as a narrow coreference, not as a new legal duty or relationship.'
            $primary = 'YES_AFTER_HUMAN_ADJUDICATION; conditional provenance correction'
            $sensitivity = 'CONDITIONAL: use sensitivity-only if analysis is constrained to the originally recorded 3.1/3.2 warrant rather than the human-authorized corrected frozen provenance.'
            $provenance = 'INTRACORPUS_COREFERENCE_VIA_FROZEN_4_3; historical warrant remains preserved, not rewritten.'
            $effect = 'Igor''s A is operative only with the corrected frozen provenance; otherwise the memo requires B / SENSITIVITY_ONLY.'
        }
        'CL-P03-02' {
            $verification = 'PASS_DEPENDENCY_ON_R_P03_04'
            $basis = 'R-P03-04 passed its stated conditional test. CS-P03-003/005/006 support the sampled assessment, audit, and report components.'
            $primary = 'YES_CONDITIONAL_ON_R_P03_04_PASS; bounded to "as sampled".'
            $sensitivity = 'No separate sensitivity run mandated by the memo; if shown, preserve "as sampled".'
            $provenance = 'FROZEN_STATEMENTS_CS_P03_003_005_006; reporting-to-manufacturer only. "No other recipient appears in sampled statements" is not an exclusionary legal rule.'
            $effect = 'Do not characterize the report as legally exclusive to the audited party; no other recipient appears in the sampled frozen statements.'
        }
        'CL-P03-03' {
            $verification = 'HUMAN_B_RETAINED; no autonomous promotion'
            $basis = 'Human decision identifies the identity bridge through Annex III point 6 or Article 9 as outside the frozen corpus; no lexical substitution is accepted.'
            $primary = 'NO'
            $sensitivity = 'YES; separately labelled only.'
            $provenance = 'EXTERNAL_IDENTITY_BRIDGE_ANNEX_III_6_OR_ARTICLE_9; not in common statement register.'
            $effect = 'No contribution to primary comparison; may appear only in separately labelled sensitivity analysis.'
        }
        'CL-P03-02#CORE' {
            $verification = 'HUMAN_B_RETAINED; derived descriptive status preserved'
            $basis = 'Human decision says this post hoc derived core removes/recuts components and is not outcome-bearing.'
            $primary = 'NO'
            $sensitivity = 'NO_OUTCOME_USE; descriptive display only.'
            $provenance = 'STEP0_DERIVED; never represent as an original cell claim.'
            $effect = 'Descriptive only; does not carry a primary or sensitivity outcome.'
        }
        'R-P04-05' {
            $verification = 'REOPENING_TEST_NEGATIVE; B retained'
            $basis = 'Inspected all 14 frozen P04 statements CS-P04-001 to CS-P04-014. CS-P04-001/002 cover the independent audit, Registry expense/appointment, Commission consultation/reporting; CS-P04-003 to CS-P04-014 concern validation, escrow, and ADR. None explicitly attributes administration of phased registration to the Registry.'
            $primary = 'NO'
            $sensitivity = 'YES; separately labelled only.'
            $provenance = 'AUDIT_OBJECT_NOT_ESTABLISHED_IN_FROZEN_P04_STATEMENTS; the out-of-scope third sentence of Article 12(5) was not consulted or imported.'
            $effect = 'The B decision remains; do not reopen/promote without another frozen statement and Igor''s confirmation.'
        }
        'CL-P04-02' {
            $verification = 'HUMAN_B_RETAINED; original warrant separated from text-supported configuration'
            $basis = 'Human decision preserves the legal support of the literal text but restricts the original warrant because its audit-as-external-accountability reading depends on R-P04-05.'
            $primary = 'NO_FOR_ORIGINAL_CLAIM_WARRANT'
            $sensitivity = 'YES_FOR_ORIGINAL_WARRANT; frozen-text arrangement proceeds only through CL-P04-02#CORE.'
            $provenance = 'ORIGINAL_WARRANT_DEPENDS_ON_SENSITIVITY_ONLY_R_P04_05; do not rewrite the historical cell claim.'
            $effect = 'Keep the original claim/warrant in sensitivity; evaluate the derived frozen-text core separately.'
        }
        'CL-P04-02#CORE' {
            $verification = 'HUMAN_A_RETAINED; derived primary aid with mandatory sensitivity'
            $basis = 'Human decision accepts the core as preserving the literal frozen-text arrangement while removing the contaminated warrant.'
            $primary = 'YES_AS_DERIVED_PRIMARY_AID'
            $sensitivity = 'MANDATORY_WITH_AND_WITHOUT_THIS_UNIT; disclose whether inclusion changes the comparative result.'
            $provenance = 'STEP0_DERIVED; not an original cell output.'
            $effect = 'Any later primary result must be reported once with and once without this unit.'
        }
        { $_ -in @('RG-06','RG-10') } {
            $type = 'PENDING_CORRESPONDENCE_CARD'
            $verification = 'PENDING_HUMAN_DECISION; full card recovered and prepared, not adjudicated by AI'
            $basis = 'The source file marks PENDING. The full Step 2A review card is now available; no human decision has been supplied for this correspondence question.'
            $primary = 'NOT_DETERMINED_PENDING_HUMAN_ADJUDICATION'
            $sensitivity = 'NOT_DETERMINED'
            $provenance = 'STEP2A_CANDIDATE_GROUP; no correspondence outcome assigned.'
            $unitStatus = 'PROVISIONAL_CORRESPONDENCE; contains STEP0_DERIVED proposition where identified in sealed key.'
            $effect = 'No AI adjudication; maintain the Step 2B stop for conclusions materially depending on this group.'
        }
    }
    $derived.Add([pscustomobject][ordered]@{
        review_item_id = $d.review_item_id
        linked_p1_queue_id = $sourceQueueRow.queue_id
        linked_step1_unit_id = $sourceQueueRow.step1_unit_id
        adjudicated_source_cell = $sourceQueueRow.cell
        source_unit_origin = $(if ($d.human_status -eq 'PENDING') { 'PROVISIONAL_CORRESPONDENCE_CARD' } else { $sourceQueueRow.unit_origin })
        review_item_type = $type
        original_human_decision = $d.decision_code
        original_canonical_disposition = $d.canonical_disposition
        human_confidence_1_to_5 = $d.confidence
        human_justification_verbatim = $d.justification
        human_condition_or_followup_verbatim = $d.condition_or_followup
        human_status = $d.human_status
        verification_result = $verification
        verification_basis_and_frozen_anchors = $basis
        final_derived_primary_eligibility = $primary
        sensitivity_eligibility = $sensitivity
        provenance = $provenance
        derived_unit_status = $unitStatus
        conditional_effect = $effect
        reviewer_identity = $d.reviewer
        review_date = $d.review_date
        human_source_csv_sha256 = $expectedCsv
        human_source_memo_sha256 = $expectedMemo
    })
}
$derived | Export-Csv -LiteralPath (Join-Path $human 'G4_HUMAN_ADJUDICATION_DERIVED_REGISTER_2026-10-05.csv') -NoTypeInformation -Encoding utf8

$packetRows = [System.Collections.Generic.List[object]]::new()
$markdown = [System.Text.StringBuilder]::new()
[void]$markdown.AppendLine('# RG-06 and RG-10 - human adjudication packet')
[void]$markdown.AppendLine()
[void]$markdown.AppendLine('**Date prepared:** 2026-10-05  ')
[void]$markdown.AppendLine('**Status:** `PENDING_HUMAN_DECISION` for both correspondence items.  ')
[void]$markdown.AppendLine('**Purpose:** Resolve only the correspondence and evidence-scope questions below. This packet does not assign a Step 2A outcome or initiate Step 2B.')
[void]$markdown.AppendLine()
[void]$markdown.AppendLine('The cards retain anonymized proposition labels A-E. A coordinator-only source map is included at the end because provenance was requested; keep that section sealed until any blinded review is complete. The two human-source files and prior frozen records remain unchanged.')

foreach ($rid in @('RG-06','RG-10')) {
    $card = $groups | Where-Object review_group_id -eq $rid
    $key = @($keys | Where-Object review_group_id -eq $rid)
    $cgid = ($key | Select-Object -First 1).correspondence_group_id
    $group = $candidateGroups | Where-Object correspondence_group_id -eq $cgid
    $claimsMap = @($key | ForEach-Object { "$($_.proposition_label): $($_.source_cell) / $($_.original_claim_id) [$($_.unit_origin); $($_.unit_id)]" }) -join "`n"
    $p1Effect = if ($rid -eq 'RG-06') {
        'Item-level scope: Igor''s P1 decisions link to HRQ-01 / S1-037 / CLAUDE_A / R-P03-04; HRQ-14 / S1-093 / CLAUDE_A / CL-P03-02 (Proposition E); and HRQ-24 / S1-113 / CLAUDE_A / CL-P03-02#CORE (Proposition C). The similarly named Proposition A, CLAUDE_B / S1-102 / CL-P03-02, is a distinct P2 item (HRQ-18) and is NOT adjudicated by the P1 decision. The P1 decisions do not settle whether A-E correspond and do not adjudicate the Codex configuration claims.'
    } else {
        'Item-level scope: Igor''s P1 decisions link to HRQ-04 / S1-059 / CLAUDE_B / R-P04-05; HRQ-19 / S1-104 / CLAUDE_B / CL-P04-02 (Proposition A); and HRQ-25 / S1-114 / CLAUDE_B / CL-P04-02#CORE (Proposition E). Proposition C, CLAUDE_A / S1-096 / CL-P04-02, is a distinct non-P1 unit and is NOT adjudicated by the P1 decision. The original Claude B warrant remains sensitivity-only; its derived core is an aid with mandatory with/without reporting. None of these decisions settles whether A-E correspond.'
    }
    $outside = if ($rid -eq 'RG-06') {
        'OUTSIDE FROZEN EVIDENCE / HISTORICAL SCOPE NOTE: Proposition A''s descriptive attribution to the manufacturer references Annex III points 2/3.1 as peripheral corroboration in the earlier card; Proposition E was SC-C because its assessment counterparty came from outside the frozen excerpts. Igor''s P1 decision supplies an alternative frozen provenance via point 4.3 for R-P03-04. Do not import the wording of points 2, 3.1, or 3.2 into this review.'
    } else {
        'OUTSIDE FROZEN EVIDENCE: Proposition A''s auditor-to-Registry verification relation and auditee premise were previously classified SC-C; Igor''s decision retains R-P04-05 as sensitivity-only. The source memo identifies the third sentence of Article 12(5) as the out-of-scope audit-object source. That sentence is not reproduced here and was not consulted for the frozen reopening test.'
    }
    $neutral = 'For correspondence: SAME / PARTLY_SAME / DIFFERENT / CANNOT_JUDGE. For scope, identify proposition(s) and whether the relied-on basis is frozen, only peripheral context, outside-frozen and load-bearing (sensitivity-only), or indeterminate. For differences: segmentation / vocabulary / scope / substance / mixed / other. These are neutral alternatives; free-text reasoning controls. No answer is preselected.'
    $packetRows.Add([pscustomobject][ordered]@{
        review_item_id = $rid
        correspondence_group_id = $cgid
        legal_case = $card.legal_case
        analytical_level = $card.analytical_level
        originating_claims_cells_and_unit_types_coordinator_only = $claimsMap
        normalized_propositions_anonymized = $card.propositions_anonymised
        relevant_frozen_statement_ids = $card.legal_evidence_statement_ids
        relevant_frozen_evidence_exact = $card.legal_evidence_exact_excerpts
        out_of_scope_text_and_scope_flags = $outside
        historical_step2a_proposed_correspondence = "$($group.correspondence_type); candidate only; $($group.member_count) original members plus derived unit(s) $($group.derived_units_attached); no outcome label assigned. Rationale: $($group.preliminary_matching_rationale)"
        effect_of_igor_p1_adjudications = $p1Effect
        exact_remaining_human_question = "$($card.review_focus) $($card.reviewer_questions)"
        neutral_decision_alternatives = $neutral
        human_confidence_1_to_5 = ''
        human_justification = ''
        reviewer_identity_or_code = ''
        review_date_iso = ''
    })
    [void]$markdown.AppendLine()
    [void]$markdown.AppendLine("## $rid - $cgid")
    [void]$markdown.AppendLine()
    [void]$markdown.AppendLine("**Case/level:** $($card.legal_case) / $($card.analytical_level).  ")
    [void]$markdown.AppendLine("**Step 2A proposal:** $($group.correspondence_type) (candidate only; $($group.member_count) original members plus derived unit(s) $($group.derived_units_attached); no outcome label). $($group.preliminary_matching_rationale)")
    [void]$markdown.AppendLine()
    [void]$markdown.AppendLine('### Anonymized propositions')
    [void]$markdown.AppendLine()
    [void]$markdown.AppendLine($card.propositions_anonymised)
    [void]$markdown.AppendLine()
    [void]$markdown.AppendLine('### Exact frozen evidence')
    [void]$markdown.AppendLine()
    [void]$markdown.AppendLine($card.legal_evidence_exact_excerpts)
    [void]$markdown.AppendLine()
    [void]$markdown.AppendLine('### Out-of-scope context (not frozen evidence)')
    [void]$markdown.AppendLine()
    [void]$markdown.AppendLine($outside)
    [void]$markdown.AppendLine()
    [void]$markdown.AppendLine('### Effect of prior P1 human decisions')
    [void]$markdown.AppendLine()
    [void]$markdown.AppendLine($p1Effect)
    [void]$markdown.AppendLine()
    [void]$markdown.AppendLine('### Remaining question for Igor')
    [void]$markdown.AppendLine()
    [void]$markdown.AppendLine("$($card.review_focus) $($card.reviewer_questions)")
    [void]$markdown.AppendLine()
    [void]$markdown.AppendLine('### Neutral response frame (no answer preselected)')
    [void]$markdown.AppendLine()
    [void]$markdown.AppendLine($neutral)
    [void]$markdown.AppendLine()
    [void]$markdown.AppendLine('**Human decision:** ____________________  ')
[void]$markdown.AppendLine('**Confidence (1-5):** ____________________  ')
    [void]$markdown.AppendLine('**Justification:** ____________________  ')
    [void]$markdown.AppendLine('**Reviewer identity/code:** ____________________  ')
    [void]$markdown.AppendLine('**Review date (YYYY-MM-DD):** ____________________')
}
[void]$markdown.AppendLine()
[void]$markdown.AppendLine('## Coordinator-only source map - seal from blinded reviewer')
[void]$markdown.AppendLine()
[void]$markdown.AppendLine('This map identifies source cells and claims as requested. Remove or seal this section before any blinded review; the adjudication questions above preserve proposition labels A-E.')
foreach ($r in $packetRows) {
    [void]$markdown.AppendLine()
    [void]$markdown.AppendLine("### $($r.review_item_id) / $($r.correspondence_group_id)")
    [void]$markdown.AppendLine()
    [void]$markdown.AppendLine($r.originating_claims_cells_and_unit_types_coordinator_only)
}
$packetRows | Export-Csv -LiteralPath (Join-Path $human 'HUMAN_ADJUDICATION_RG06_RG10_2026-10-05.csv') -NoTypeInformation -Encoding utf8
[System.IO.File]::WriteAllText((Join-Path $human 'HUMAN_ADJUDICATION_RG06_RG10_2026-10-05.md'), $markdown.ToString(), [System.Text.UTF8Encoding]::new($false))
Write-Output "source_rows=$($decisions.Count); adjudicated_rows=$(@($decisions|Where-Object human_status -eq 'ADJUDICATED').Count); pending_cards=$(@($decisions|Where-Object human_status -eq 'PENDING').Count); review_packet_rows=$($packetRows.Count); R_P03_04=PASS_CONDITIONAL_INTRACORPUS_COREFERENCE; R_P04_05=REOPENING_TEST_NEGATIVE"
