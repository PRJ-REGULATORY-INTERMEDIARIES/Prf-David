# MECHANICAL assembly of CASE_RGAM_REPORT.md from the delivered tables (counts, tables and executor-authored text fields copied verbatim; no new analytical content).
import csv, json, collections, re

D = "G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/12_RGAM_CASE_EXECUTION/RGAM_AI_AI_ACT/"


def rd(n):
    return list(csv.DictReader(open(D + n + ".csv", encoding="utf-8-sig")))


def short(s, n):
    s = s.replace("|", "/").replace("\n", " ")
    return s if len(s) <= n else s[: n - 3].rstrip() + "..."


W = rd("W_DECLARATION")[0]
INV = rd("SOURCE_UNIT_INVENTORY"); SCR = rd("UNIT_SCREENING"); ST = rd("INSTITUTIONAL_STATEMENTS"); NA = rd("NORMATIVE_ASSIGNMENTS"); PD = rd("POSITIONS_AND_DEVICES")
QR = rd("QUALIFIED_RELATIONS"); EXT = rd("EXTERNAL_REFERENCES"); SC = rd("SUBCONFIGURATIONS"); AR = rd("ARCHITECTURE_CANDIDATES"); PR = rd("PROPERTY_REGISTER")
CL = rd("CLOSURE_REGISTER"); LK = rd("PROVENANCE_LINKS"); UN = rd("UNCERTAINTY_LOG"); HQ = rd("HUMAN_REVIEW_QUEUE"); TR = rd("TRACE_DEMONSTRATIONS"); SUM = rd("INSTRUMENT_LEVEL_SUMMARY")[0]
DV = rd("PROTOCOL_DEVIATION_LOG"); RUN = rd("RUN_METADATA")[0]
val = json.load(open(D + "_work/validate_result.json"))
cls = collections.Counter(r["structure_class"] for r in INV)
rel = collections.Counter(r["governance_relevance"] for r in SCR)
o = []
a = o.append
a("# CASE_RGAM_REPORT — RGAM_AI_AI_ACT (machine-generated and provisional)\n")
a("Instrument: Regulation (EU) 2024/1689 (Artificial Intelligence Act), CELEX 32024R1689, original act as published (OJ L, 2024/1689, 12.7.2024). Protocol: RGAM paired execution protocol v1.0 with the execution addendum GAP-01 to GAP-07. This report contains no comparison with any other method or case and no score, index or ranking.\n")
a("## 1. W declaration and coverage\n")
a("| Field | Value |\n|---|---|")
for k in ("instrument_title", "celex", "jurisdiction", "instrument_type", "version_type", "hash_match", "source_sha256", "article_count_parsed", "annex_count_parsed", "recital_count_parsed", "structure_check", "w_is_not_a"):
    a(f"| {k} | {short(W[k], 260)} |")
a(f"| domain_declaration | {short(W['domain_declaration'], 420)} |")
a(f"| temporal_reference | {short(W['temporal_reference'], 520)} |")
a(f"| inclusion_rule | {short(W['inclusion_rule'], 300)} |")
a(f"| exclusions | {short(W['exclusions'], 420)} |")
a(f"| closure_scope_statement | {short(W['closure_scope_statement'], 520)} |")
a("")
a(f"P0: the SHA-256 of the controlling source file equals the expected value in the capsule metadata (hash_match = {W['hash_match']}).\n")
a(f"P1 coverage procedure: the file was parsed mechanically into {len(INV)} units in source order ({', '.join(f'{k} {v}' for k, v in cls.items())}); the parsed counts (113 articles, 13 annexes) match the neutral metadata, and the parsed article and annex text was compared with the source text word by word (only structural labels differed). P2: every unit was screened in source order ({SUM['units_screened']} of {SUM['units_total']}); governance_relevance Yes = {rel['Yes']}, No = {rel['No']}, Uncertain = {rel['Uncertain']}. Recitals, headings and pure definitions of technical terms are legitimate No results. Recitals REC34 to REC180 were screened from their opening text and length (deviation log); all other units were read in full.\n")
a("## 2. Record counts by table (evidence descriptors only; not significance)\n")
a("| Table | Rows |\n|---|---:|")
for n, c in val["tables"].items():
    a(f"| {n}.csv | {c} |")
a("")
a("## 3. Subconfigurations and warrants\n")
a("Each subconfiguration (S) is constructed from qualified relations and normative assignments by a stated pattern rule and organizing mechanism, not from chapters, vocabulary or theme. Every candidate starts as S and becomes an architecture candidate only through the I1-I4 assessment. Member lists, boundaries, rival groupings and overlaps are in SUBCONFIGURATIONS.csv.\n")
a("| Id | Scope | Pattern rule | Relations / assignments / positions | Units spanned | Overlaps |\n|---|---|---|---|---:|---|")
for r in SC:
    nq = len(r["member_qr_ids"].split(";")); nn = len([x for x in r["member_na_ids"].split(";") if x]); np_ = len(r["member_pd_ids"].split(";"))
    a(f"| {r['sc_id']} | {short(r['scope_label'], 90)} | {short(r['pattern_rule'], 240)} | {nq} / {nn} / {np_} | {len([x for x in r['units_spanned'].split(';') if x])} | {r['overlap_sc_ids']} |")
a("")
a("Warrant basis and organizing mechanism per subconfiguration (verbatim, abbreviated):\n")
for r in SC:
    a(f"- **{r['sc_id']}** {short(r['scope_label'], 100)}: {short(r['organizing_mechanism'], 420)}")
a("")
a("## 4. Candidate architectures: I1-I4, rival groupings, outcomes\n")
a("The sequence followed was: governing question (I1), independently stated coupling (I2), configurational consequence (I3), rival groupings and boundary sensitivity (I4). No score or threshold was used. Every INTEGRATED and OVERLAPPING_OR_PARTIALLY_INTEGRATED outcome is queued for human review because the I2/I3 thresholds are unvalidated.\n")
a("| Id | Member SC | I1 | I2 | I3 | I4 | Outcome | HQ |\n|---|---|---|---|---|---|---|---|")
for r in AR:
    a(f"| {r['arch_id']} | {r['member_sc_ids']} | {r['i1_status']} | {r['i2_status']} ({r['i2_coupling_kind']}) | {r['i3_status']} | {r['i4_status']} | **{r['outcome']}** | {r['hq_ids']} |")
a("")
for r in AR:
    a(f"### {r['arch_id']} - {r['outcome']}\n")
    a(f"- Governing question and scale (I1): {short(r['i1_governing_problem_and_scale'], 600)}")
    a(f"- Coupling (I2): {short(r['i2_coupling_description'], 900)}")
    a(f"- Consequence and bearer (I3): {short(r['i3_configurational_consequence'], 500)} Bearer and rule: {short(r['i3_bearer_and_rule'], 500)}")
    a(f"- Searched, external dependencies, rival grouping (I4): {short(r['i4_evidence_searched'], 300)}; external references: {r['i4_external_dependencies'] or 'none'}; rival grouping: {short(r['i4_rival_grouping'], 400)}; boundary sensitivity: {short(r['i4_boundary_sensitivity'], 500)}")
    a(f"- Outcome basis: {short(r['outcome_basis'], 600)}")
    a(f"- Status profile: {short(r['status_profile'], 500)}\n")
a(f"Instrument-level result (profile, not a label or score): **{SUM['instrument_level_result']}**; highest level reached: **{SUM['highest_level_reached']}**.\n")
a("## 5. Property register summary (scale, bearer, aggregation)\n")
a("Properties are attributed to one bearer with scale and aggregation stated first; values per bearer are reported before any generalization; no scalar score, composite or graph index is computed. property_family (F1-F5) is left blank because the mapping of dimensions to families is not in the allow-listed sources (deviation log).\n")
a("| Id | Property | Bearer | Scale | Status | Closure |\n|---|---|---|---|---|---|")
for r in PR:
    a(f"| {r['prop_id']} | {r['property_name']} | {r['bearer_type']} {r['bearer_id']} | {short(r['scale'], 120)} | {r['status']} | {r['closure_ref'] or '-'} |")
a("")
for r in PR:
    a(f"- **{r['prop_id']}** ({r['property_name']}, {r['status']}): {short(r['value_statement'], 480)} Aggregation: {short(r['aggregation_rule'], 160)}")
a("")
a("## 6. Status profile\n")
a(SUM["status_profile"] + "\n")
a("Descriptive tallies only: material_establishment_evidenced and exercise_evidenced are not collected from legal text (not_assessed). Claims conditioned on an unresolved external reference with constitutive dependency were kept at documented level and flagged, never deleted (RGAM-DR-19).\n")
a("## 7. Closure and external-reference limitations\n")
a("| Id | Kind | Claim or scope | Result | Unresolved external references |\n|---|---|---|---|---|")
for r in CL:
    a(f"| {r['closure_id']} | {r['record_kind']} | {short(r['claim_or_scope'], 380)} | {r['result']} | {r['unresolved_ext_ids'] or '-'} |")
a("")
cd = [r for r in EXT if r["constitutive_dependency"] == "Y"]
a(f"External references: {len(EXT)} records, all source_verification_status = not_checked and boundary_status = outside_corpus_not_expanded; {len(cd)} carry a constitutive dependency (claims resting on them are undetermined or restricted to the declared corpus). They fall into: Annex I Section A acts ({sum(1 for r in EXT if r['ext_id'] and 'Annex I Section A' in r['referenced_legal_source'])}), Annex X acts ({sum(1 for r in EXT if 'Annex X' in r['referenced_legal_source'])}), amendments of other acts ({sum(1 for r in EXT if 'amended by Article' in r['referenced_legal_source'])}), data protection, financial services, market surveillance (Regulation (EU) 2019/1020), standardisation and comitology instruments, copyright and accessibility law, agreements with third countries and the Commission Decision of 24 January 2024 on the AI Office. Their content was not retrieved or analysed.\n")
a("## 8. Open human-review items\n")
a(f"{len(HQ)} items are queued; all human_decision, human_rationale, decided_by and decision_date cells are blank; no item was adjudicated.\n")
a("| Id | Trigger | Question | Machine recommendation (not a decision) |\n|---|---|---|---|")
for r in HQ:
    a(f"| {r['hq_id']} | {r['trigger_code']} | {short(r['question'], 330)} | {short(r['machine_recommendation'], 160)} |")
a("")
a("## 9. Deviations and gaps\n")
a("| Id | Rule | Gap | Description |\n|---|---|---|---|")
for r in DV:
    a(f"| {r['dev_id']} | {r['rule_id']} | {r['gap_ref'] or '-'} | {short(r['description'], 520)} |")
a("")
a("### 9.1 Internal integrity checks (P9)\n")
a("The ten referential-integrity rules of the data dictionary section 4 and the further checks of the output schema section 4 were run by an independent validation script on the delivered CSV files (validate.py, result file _work/validate_result.json); see CASE_QA_REPORT.md for the result per rule. Summary: units screened = units inventoried (1553 = 1553); every INTEGRATED or OVERLAPPING outcome has an HQ item; no relation carries prohibition modality or material_establishment_evidenced; every external reference is not_checked; human columns are blank; both trace chains resolve; evidence spans are verbatim and at most 400 characters.\n")
a("### 9.2 Trace demonstrations\n")
for r in TR:
    a(f"- {r['trace_id']} ({r['selection_rule']}, seed {r['seed_integer'] or 'n/a'}): traced {r['traced_id']}, chain_complete = {r['chain_complete']}; candidate list size {len(r['candidate_list'].split(';'))}. Selection by the fixed rule of RGAM-DR-29; the seeded draw used Python random.Random(seed).randrange over the sorted candidate list spanning at least two parts of the instrument.")
a("")
a("## 10. Statement of provisional status\n")
a("All records are machine-generated and provisional (machine_provisional = Y). Repetition by the same model is not inter-coder reliability. Human adjudication has not been simulated and the human-review columns are blank. The result is limited by the unvalidated I2/I3 thresholds, the unretrieved external instruments, the unresolved norm-type, device, accountability and cross-reference questions queued above and the execution-addendum decisions recorded in the deviation log. This report makes no comparison with any other method or case.\n")
open(D + "CASE_RGAM_REPORT.md", "w", encoding="utf-8").write("\n".join(o))
print(len("\n".join(o)))
