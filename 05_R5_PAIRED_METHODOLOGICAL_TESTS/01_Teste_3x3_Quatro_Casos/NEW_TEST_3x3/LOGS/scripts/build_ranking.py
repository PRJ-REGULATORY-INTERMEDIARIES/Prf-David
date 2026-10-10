"""NEW TEST 3x3 - domain classification, ranking and selection test (applies the registered rules mechanically).

Order of operations enforced here: (1) domain assignment from title / stated objective only; (2) ranking of rank-eligible
case-versions (S1 only, per G4/G7); (3) diversity constraint test. No composite score, no normalization.
Reads the tables produced by build_universe.py. Writes 03_*/04_* CSVs and a JSON result used by the markdown reports.
"""
import csv, json, os
import openpyxl
import pandas as pd

ROOT = r"G:\Meu Drive\PRJ-David\Prf-David"
NT = os.path.join(ROOT, "NEW TEST 3x3")
M = json.load(open(os.path.join(NT, "LOGS", "scripts", "metrics_computed.json"), encoding="utf-8"))
master = pd.read_csv(os.path.join(NT, "01_CASE_UNIVERSE", "CASE_UNIVERSE_MASTER.csv"), dtype=str).fillna("")
comp = pd.read_csv(os.path.join(NT, "02_COMPARABILITY", "CASE_METRIC_COMPARABILITY.csv"), dtype=str).fillna("")

# ------------------------------------------------------------------ Level-1 / Level-2 taxonomy (from the actual universe)
L1 = {
    "D01": "Environment & climate regulation",
    "D02": "EU funds & public-finance management",
    "D03": "External trade & customs",
    "D04": "Financial markets, corporate reporting & sustainable finance",
    "D05": "Digital services, data protection & AI governance",
    "D06": "Telecommunications, radio/terminal equipment & product conformity",
    "D07": "Intellectual property & copyright",
    "D08": "Internet naming & domain governance",
    "D09": "Financial crime / anti-money-laundering transparency",
    "D10": "Health products (medical devices)",
    "D11": "Public administration & regulatory-agency governance",
}
# celex -> (primary L1, L2 sub-field, alternate L1 or "", ambiguity note, basis)
OBJ = {}
wb = openpyxl.load_workbook(os.path.join(ROOT, "R4_CROSS_DOMAIN_VALIDATION", "01_baseline", "R3_ORIGINAL", "final_package", "REGULATORY_INTERMEDIATION_ARCHITECTURE_CASE_STUDY_DATASET.xlsx"), read_only=True, data_only=True)
rows = list(wb["INSTRUMENTS"].iter_rows(values_only=True))
for r in rows[3:]:
    if r and r[0]:
        OBJ[str(r[0])] = str(r[2])

A = {
    "32003L0087": ("D01", "Carbon-market (emissions trading) regulation", "", "", "R3 INSTRUMENTS 'Regulatory objective' (Art. 1): " + OBJ.get("32003L0087", "")[:150]),
    "32015D1814": ("D01", "Carbon-market (emissions trading) regulation", "", "", "R3 INSTRUMENTS 'Regulatory objective': " + OBJ.get("32015D1814", "")[:150]),
    "32018R0842": ("D01", "National climate-target allocation (non-ETS sectors)", "", "", "R3 INSTRUMENTS 'Regulatory objective' (Art. 1): " + OBJ.get("32018R0842", "")[:150]),
    "32021R1119": ("D01", "Climate-governance framework (targets, advice, assessment)", "", "", "R3 INSTRUMENTS 'Regulatory objective' (Art. 1): " + OBJ.get("32021R1119", "")[:150]),
    "32023R0955": ("D02", "Climate-related social financing (fund, plans, payment control)", "D01", "AMBIGUOUS: subject matter is climate-related social policy, but the instrument is a fund (title: 'Social Climate Fund and amending Regulation (EU) 2021/1060' = Common Provisions Regulation for EU funds) and its institutional purpose is financing and payment control of Member State plans. Primary = EU funds; alternate = environment & climate.", "Title + R3 'Regulatory objective': " + OBJ.get("32023R0955", "")[:150]),
    "32023R0956": ("D03", "Border carbon pricing on imports", "D01", "AMBIGUOUS: title 'carbon border adjustment mechanism' (levy on imported goods, certificates, customs coordination) is trade/customs in regulatory field, climate in purpose. Primary = trade & customs; alternate = environment & climate.", "Title and R2 case-selection note (cross-border market regulation, emissions accounting, certificates, customs coordination)."),
    "32023R1115": ("D01", "Supply-chain due diligence for deforestation-free commodities", "D03", "AMBIGUOUS: title mixes environmental objective (deforestation, forest degradation) with market-access/export rules. Primary = environment; alternate = trade.", "Title and R2 case-selection note (supply-chain due diligence, traceability, market access, competent-authority checks)."),
    "32022L2464": ("D04", "Corporate sustainability reporting and assurance", "D01", "AMBIGUOUS: sustainability reporting is financial/corporate-reporting law with environmental subject matter.", "Title: 'as regards corporate sustainability reporting'."),
    "32010R0066": ("D01", "Voluntary product environmental label", "", "", "Title: 'EU Ecolabel'."),
    "32019R2089": ("D04", "Financial benchmarks (climate transition / Paris-aligned)", "D01", "AMBIGUOUS: benchmark regulation (financial markets) with climate purpose.", "Title: 'Climate Transition Benchmarks, Paris-aligned Benchmarks and sustainability-related disclosures for benchmarks'."),
    "32018R2067": ("D01", "Emissions-trading verification and verifier accreditation", "", "", "Title: 'verification of data and on the accreditation of verifiers pursuant to Directive 2003/87/EC'."),
    "32020R0852": ("D04", "Sustainable-investment taxonomy", "D01", "AMBIGUOUS: financial classification regulation with environmental objectives.", "Title: 'framework to facilitate sustainable investment'."),
    "31976L0889": ("D06", "Electromagnetic interference (equipment conformity)", "", "", "Title: radio interference caused by electrical household appliances, portable tools and similar equipment."),
    "31986L0361": ("D06", "Telecom terminal-equipment type approval", "", "", "Title: mutual recognition of type approval for telecommunications terminal equipment."),
    "31987D0095": ("D06", "ICT/telecom standardization", "", "", "Title: standardization in the field of information technology and telecommunications."),
    "31989L0336": ("D06", "Electromagnetic compatibility (product conformity)", "", "", "Title: electromagnetic compatibility."),
    "31991L0263": ("D06", "Telecom terminal-equipment conformity", "", "", "Title: telecommunications terminal equipment incl. mutual recognition of conformity."),
    "31992L0044": ("D06", "Open network provision (leased lines)", "", "", "Title: application of open network provision to leased lines."),
    "32004L0048": ("D07", "IPR enforcement", "", "", "Title: enforcement of intellectual property rights."),
    "32004R0874": ("D08", ".eu top-level-domain administration", "D05", "AMBIGUOUS: internet naming governance could be placed under digital governance; kept separate because the instrument regulates a registry and domain allocation rather than digital services or data.", "Title: public policy rules on implementation and functions of the .eu TLD."),
    "32006L0115": ("D07", "Rental and lending rights", "", "", "Title: rental right and lending right and certain rights related to copyright."),
    "32006R1781": ("D09", "Payer information on funds transfers", "D04", "AMBIGUOUS: financial-sector transparency rule serving AML/CFT purposes.", "Title: information on the payer accompanying transfers of funds."),
    "32016R0679": ("D05", "Personal-data protection", "", "", "Title: General Data Protection Regulation."),
    "32022R2065": ("D05", "Online platforms and digital services", "", "", "Title: Single Market for Digital Services (DSA)."),
    "32024R1689": ("D05", "Artificial-intelligence systems", "", "", "Title: harmonised rules on artificial intelligence."),
    "32017R0745": ("D10", "Medical-device conformity", "", "", "Title: medical devices (never extracted)."),
    "BR-LEI-13848-2019": ("D11", "Regulatory-agency governance and social control", "", "", "Title: governance, management and social control of regulatory agencies (never extracted)."),
    "32019R1150": ("D05", "Online intermediation services (platform-to-business)", "", "", "Title: fairness and transparency for business users of online intermediation services."),
    "32019L0790": ("D07", "Copyright in the Digital Single Market", "D05", "AMBIGUOUS: copyright law with digital-platform duties.", "Title: copyright and related rights in the Digital Single Market."),
}

# canonical case universe (studied instruments; Rotem-only rows are not classified: excluded before domain stage, see notes)
cases = {}
for _, r in master.iterrows():
    cid = r.canonical_case_id
    if r.source_family in ("ROTEM_ONLY", "PROHIBITED_V8"):
        continue
    cases.setdefault(cid, []).append(r)

stratum_of = {}
rank_pool_ids = set(master[(master.disposition == "ELIGIBLE") & (master.is_canonical_version == "YES")].cv_id)
cls_rows = []
for cid, rs in cases.items():
    celex = rs[0].celex_or_identifier if rs[0].celex_or_identifier != "none (national law)" else "BR-LEI-13848-2019"
    key = celex if celex in A else cid.replace("CASE-", "")
    p, l2, alt, amb, basis = A[key]
    canon = [r for r in rs if r.is_canonical_version == "YES"]
    disp = canon[0].disposition if canon else "DUPLICATE_VERSION_ONLY"
    in_pool = any(r.cv_id in rank_pool_ids for r in rs)
    cls_rows.append(dict(canonical_case_id=cid, celex_or_identifier=key, instrument_title=rs[0].instrument_title,
                         level1_code_primary=p, level1_domain_primary=L1[p], level2_subfield=l2,
                         level1_code_alternate=alt, level1_domain_alternate=L1.get(alt, ""),
                         ambiguous_assignment="YES" if alt else "NO", ambiguity_note=amb, basis_for_assignment=basis,
                         canonical_disposition=disp, in_rank_eligible_pool="YES" if in_pool else "NO",
                         classified_before_ranking="YES (computed before the ranking step in build_ranking.py; uses title/objective text only)"))
cls = pd.DataFrame(cls_rows)
cls_cols = ["canonical_case_id", "celex_or_identifier", "instrument_title", "level1_code_primary", "level1_domain_primary", "level2_subfield", "level1_code_alternate", "level1_domain_alternate",
            "ambiguous_assignment", "ambiguity_note", "basis_for_assignment", "canonical_disposition", "in_rank_eligible_pool", "classified_before_ranking"]
os.makedirs(os.path.join(NT, "03_DOMAIN_CLASSIFICATION"), exist_ok=True)
cls[cls_cols].to_csv(os.path.join(NT, "03_DOMAIN_CLASSIFICATION", "CASE_DOMAIN_CLASSIFICATION.csv"), index=False, encoding="utf-8-sig")
dom_of = dict(zip(cls.canonical_case_id, cls.level1_code_primary))
alt_of = dict(zip(cls.canonical_case_id, cls.level1_code_alternate))
l2_of = dict(zip(cls.canonical_case_id, cls.level2_subfield))

# ------------------------------------------------------------------ ranking (S1 only; registered lexicographic rule)
KEYS = ["intermediation_relations", "actors", "intermediaries", "targets", "relations"]
pool = master[master.cv_id.isin(rank_pool_ids)].copy()
for k in KEYS:
    pool[k] = pool[k].astype(int)
pool = pool.sort_values(by=KEYS, ascending=[False] * 5, kind="mergesort").reset_index(drop=True)


def tie_note(i):
    if i == 0:
        return ""
    prev, cur = pool.loc[i - 1], pool.loc[i]
    for j, k in enumerate(KEYS):
        if prev[k] != cur[k]:
            return "" if j == 0 else f"tie on {', '.join(KEYS[:j])} broken by {k} ({prev[k]} > {cur[k]})"
    return "unresolved tie on all five criteria"


pool["global_rank"] = range(1, len(pool) + 1)
pool["tie_break_note"] = [tie_note(i) for i in range(len(pool))]
pool["domain_code"] = pool.canonical_case_id.map(dom_of)
pool["domain_name"] = pool.domain_code.map(L1)
pool["domain_rank"] = pool.groupby("domain_code").cumcount() + 1
pool["alt_domain_code"] = pool.canonical_case_id.map(alt_of)
pool["level2_subfield"] = pool.canonical_case_id.map(l2_of)

gl = []
for _, r in pool.iterrows():
    gl.append(dict(global_rank=r.global_rank, canonical_case_id=r.canonical_case_id, celex=r.celex_or_identifier, instrument_title=r.instrument_title, domain_level1_primary=f"{r.domain_code} {r.domain_name}",
                   intermediation_relations=r.intermediation_relations, actors=r.actors, intermediaries=r.intermediaries, targets=r.targets, relations=r.relations,
                   corpus_scope=r.corpus_scope, comparability_stratum=r.comparability_stratum, comparability_status="C1/C2 on all five metrics within stratum S1 (targets = C2 recount)",
                   tie_break_note=r.tie_break_note, rank_status="RANKED", source_cv_id=r.cv_id))
# non-ranked, for transparency: canonical versions with R-I-T metrics but not rank-eligible
others = master[(~master.cv_id.isin(rank_pool_ids)) & (master.is_canonical_version == "YES") & (master.source_family.isin(["R2", "POC", "PILOT", "R4", "ROTEM_LIST", "NOT_STARTED"]))]
for _, r in others.iterrows():
    gl.append(dict(global_rank="", canonical_case_id=r.canonical_case_id, celex=r.celex_or_identifier, instrument_title=r.instrument_title,
                   domain_level1_primary=(lambda c: f"{dom_of[c]} {L1[dom_of[c]]}" if c in dom_of else "")(r.canonical_case_id),
                   intermediation_relations=r.intermediation_relations, actors=r.actors, intermediaries=r.intermediaries, targets=r.targets, relations=r.relations,
                   corpus_scope=r.corpus_scope, comparability_stratum=r.comparability_stratum,
                   comparability_status={"CONDITIONALLY_ELIGIBLE": "C3 on all five metrics (cross-pipeline bridge failed)", "NON_COMPARABLE": "C4/C5 (see CASE_METRIC_COMPARABILITY.csv)", "INSUFFICIENT_SOURCE": "C5 (no records)"}.get(r.disposition, r.disposition),
                   tie_break_note="", rank_status="NOT_RANKED_" + r.disposition, source_cv_id=r.cv_id))
os.makedirs(os.path.join(NT, "04_RANKING_AND_SELECTION"), exist_ok=True)
gcols = ["global_rank", "canonical_case_id", "celex", "instrument_title", "domain_level1_primary", "intermediation_relations", "actors", "intermediaries", "targets", "relations", "corpus_scope", "comparability_stratum", "comparability_status", "tie_break_note", "rank_status", "source_cv_id"]
with open(os.path.join(NT, "04_RANKING_AND_SELECTION", "GLOBAL_CASE_RANKING.csv"), "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=gcols)
    w.writeheader()
    for g in gl:
        w.writerow(g)

dl = []
for _, r in pool.sort_values(["domain_code", "domain_rank"]).iterrows():
    dl.append(dict(domain_level1=f"{r.domain_code} {r.domain_name}", domain_rank=r.domain_rank, global_rank=r.global_rank, canonical_case_id=r.canonical_case_id, instrument_title=r.instrument_title,
                   level2_subfield=r.level2_subfield, alternate_domain=r.alt_domain_code, intermediation_relations=r.intermediation_relations, actors=r.actors, intermediaries=r.intermediaries,
                   targets=r.targets, relations=r.relations, rank_status="RANKED"))
for _, r in others[others.source_family == "R2"].iterrows():
    c = r.canonical_case_id
    dl.append(dict(domain_level1=f"{dom_of[c]} {L1[dom_of[c]]}", domain_rank="", global_rank="", canonical_case_id=c, instrument_title=r.instrument_title, level2_subfield=l2_of[c], alternate_domain=alt_of[c],
                   intermediation_relations=r.intermediation_relations, actors=r.actors, intermediaries=r.intermediaries, targets=r.targets, relations=r.relations, rank_status="NOT_RANKED_CONDITIONALLY_ELIGIBLE_STRATUM_S2"))
dcols = ["domain_level1", "domain_rank", "global_rank", "canonical_case_id", "instrument_title", "level2_subfield", "alternate_domain", "intermediation_relations", "actors", "intermediaries", "targets", "relations", "rank_status"]
with open(os.path.join(NT, "04_RANKING_AND_SELECTION", "DOMAIN_CASE_RANKING.csv"), "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=dcols)
    w.writeheader()
    for d in dl:
        w.writerow(d)

# ------------------------------------------------------------------ diversity constraint (Level-1 primary)
chosen, domains_used, excluded = [], set(), []
for _, r in pool.iterrows():
    if r.domain_code in domains_used:
        excluded.append(dict(case=r.canonical_case_id, global_rank=int(r.global_rank), domain=r.domain_code, reason="domain already filled by a higher-ranked case"))
        continue
    chosen.append(r.canonical_case_id)
    domains_used.add(r.domain_code)
    if len(chosen) == 3:
        break
distinct_domains_in_pool = sorted(pool.domain_code.unique())
distinct_domains_alt = sorted(set(pool.apply(lambda r: r.domain_code, axis=1)) | set(x for x in pool.alt_domain_code if x))
res = dict(pool_size=len(pool), distinct_level1_domains_in_pool=distinct_domains_in_pool, chosen_under_diversity=chosen, excluded_by_diversity=excluded,
           selection_possible=(len(chosen) == 3),
           pool_ranking=[(int(r.global_rank), r.canonical_case_id, r.domain_code, int(r.intermediation_relations), int(r.actors), int(r.intermediaries), int(r.targets), int(r.relations)) for _, r in pool.iterrows()])

# ------------------------------------------------------------------ contingent views (NOT selection)
# Option P: pooled S1+S2 with native values (R2 canonical CBAM/EUDR added; R2 Climate Law is a non-canonical version)
poolP = pd.concat([pool[KEYS + ["canonical_case_id", "domain_code", "comparability_stratum"]],
                   master[(master.cv_id.isin(master[(master.disposition == "CONDITIONALLY_ELIGIBLE")].cv_id))][KEYS + ["canonical_case_id", "comparability_stratum"]].assign(domain_code=lambda d: d.canonical_case_id.map(dom_of))])
for k in KEYS:
    poolP[k] = poolP[k].astype(int)
poolP = poolP.sort_values(by=KEYS, ascending=[False] * 5, kind="mergesort").reset_index(drop=True)
chosenP, usedP = [], set()
for _, r in poolP.iterrows():
    if r.domain_code in usedP:
        continue
    chosenP.append(r.canonical_case_id)
    usedP.add(r.domain_code)
    if len(chosenP) == 3:
        break
res["optionP_ranking"] = [(i + 1, r.canonical_case_id, r.domain_code, r.comparability_stratum, int(r.intermediation_relations), int(r.actors), int(r.intermediaries), int(r.targets), int(r.relations)) for i, r in poolP.iterrows()]
res["optionP_chosen"] = chosenP
# Option P with harmonized R2 triple unit (sensitivity only)
trip = {"CASE-32021R1119": M["R2_final_v2"]["case_01"]["rit_triples_intermediated_expanded"], "CASE-32023R0956": M["R2_final_v2"]["case_02"]["rit_triples_intermediated_expanded"], "CASE-32023R1115": M["R2_final_v2"]["case_03"]["rit_triples_intermediated_expanded"]}
poolPH = poolP.copy()
poolPH["intermediation_relations"] = [trip.get(c, v) if s.startswith("S2") else v for c, v, s in zip(poolPH.canonical_case_id, poolPH.intermediation_relations, poolPH.comparability_stratum)]
poolPH = poolPH.sort_values(by=KEYS, ascending=[False] * 5, kind="mergesort").reset_index(drop=True)
chosenPH, usedPH = [], set()
for _, r in poolPH.iterrows():
    if r.domain_code in usedPH:
        continue
    chosenPH.append(r.canonical_case_id); usedPH.add(r.domain_code)
    if len(chosenPH) == 3:
        break
res["optionP_triple_unit_chosen"] = chosenPH
res["optionP_triple_unit_ranking"] = [(i + 1, r.canonical_case_id, r.domain_code, int(r.intermediation_relations)) for i, r in poolPH.iterrows()]
# Option B: Level-2 sub-field diversity inside S1
chosenB, usedB = [], set()
for _, r in pool.iterrows():
    if r.level2_subfield in usedB:
        continue
    chosenB.append(r.canonical_case_id); usedB.add(r.level2_subfield)
    if len(chosenB) == 3:
        break
res["optionB_chosen"] = chosenB
# Sensitivity: alternate domain assignment inside S1
alt_pool_domains = sorted(set(pool.apply(lambda r: r.alt_domain_code if r.alt_domain_code else r.domain_code, axis=1)))
res["alt_domains_in_S1_if_alternates_used"] = alt_pool_domains
# R2 version sensitivity for option P
res["r2_version_intermediation"] = {k: v["intermediated"] for k, v in M["R2_proposal_versions"].items()}

cont = []
for lab, ranking in [("OPTION_P_pooled_S1_plus_S2_native", res["optionP_ranking"])]:
    for t in ranking:
        cont.append(dict(option=lab, rank=t[0], canonical_case_id=t[1], domain_level1=t[2], stratum=t[3], intermediation_relations=t[4], actors=t[5], intermediaries=t[6], targets=t[7], relations=t[8],
                         would_be_selected="YES" if t[1] in chosenP else "NO", status="CONTINGENT_NOT_SELECTION"))
for t in res["optionP_triple_unit_ranking"]:
    cont.append(dict(option="OPTION_P_pooled_with_R2_triple_unit_sensitivity", rank=t[0], canonical_case_id=t[1], domain_level1=t[2], stratum="", intermediation_relations=t[3], actors="", intermediaries="", targets="", relations="",
                     would_be_selected="YES" if t[1] in chosenPH else "NO", status="CONTINGENT_NOT_SELECTION"))
for i, c in enumerate(chosenB, 1):
    cont.append(dict(option="OPTION_B_level2_subfield_diversity_inside_S1", rank=i, canonical_case_id=c, domain_level1=dom_of[c], stratum="S1_R3_CLEANROOM_FROZEN", intermediation_relations="", actors="", intermediaries="", targets="", relations="",
                     would_be_selected="YES", status="CONTINGENT_NOT_SELECTION (violates registered Level-1 diversity rule)"))
ccols = ["option", "rank", "canonical_case_id", "domain_level1", "stratum", "intermediation_relations", "actors", "intermediaries", "targets", "relations", "would_be_selected", "status"]
with open(os.path.join(NT, "04_RANKING_AND_SELECTION", "CONTINGENT_OPTIONS_NOT_SELECTION.csv"), "w", encoding="utf-8-sig", newline="") as f:
    w = csv.DictWriter(f, fieldnames=ccols)
    w.writeheader()
    for c in cont:
        w.writerow(c)

json.dump(res, open(os.path.join(NT, "LOGS", "scripts", "ranking_result.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(json.dumps(res, indent=1, ensure_ascii=False)[:6000])
print("domain distribution (canonical studied instruments):")
print(cls.groupby(["level1_code_primary", "level1_domain_primary"]).size())
