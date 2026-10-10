"""NEW TEST 3x3 - build case universe, provenance, comparability and harmonization tables.

Inputs : metrics_computed.json (from compute_metrics.py) + source files (read-only, hashed).
Outputs: 01_CASE_UNIVERSE/CASE_UNIVERSE_MASTER.csv, 01_CASE_UNIVERSE/CASE_SOURCE_PROVENANCE.csv,
         02_COMPARABILITY/CASE_METRIC_COMPARABILITY.csv, 02_COMPARABILITY/HARMONIZATION_REGISTER.csv
No selection logic here: dispositions/classes follow the rules fixed in 00_PROTOCOL/TEST_3X3_PRE_REGISTRATION.md (G1-G7).
"""
import csv, hashlib, json, os, re

ROOT = r"G:\Meu Drive\PRJ-David\Prf-David"
NT = os.path.join(ROOT, "NEW TEST 3x3")
M = json.load(open(os.path.join(NT, "LOGS", "scripts", "metrics_computed.json"), encoding="utf-8"))
_sha_cache = {}


def sha(rel):
    if rel is None:
        return ""
    if rel in _sha_cache:
        return _sha_cache[rel]
    p = os.path.join(ROOT, rel)
    if not os.path.isfile(p):
        _sha_cache[rel] = "FILE_NOT_FOUND"
        return "FILE_NOT_FOUND"
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    _sha_cache[rel] = h.hexdigest()
    return _sha_cache[rel]


METRICS = ["actors", "regulators", "intermediaries", "targets", "relations", "intermediation_relations"]
RANK_METRICS = ["intermediation_relations", "actors", "intermediaries", "targets", "relations"]
NR = None  # not recorded

# ----------------------------------------------------------------- source file anchors (relative to ROOT)
R3D = "R4_CROSS_DOMAIN_VALIDATION/01_baseline/R3_HISTORY_STAGING/PRJ-DAVID-R3/R3_CLEANROOM"
R3_ACT = f"{R3D}/04_actor_register/ACTOR_REGISTER.csv"
R3_REL = f"{R3D}/06_relations/RELATIONS_ADJUDICATED.csv"
R3_LI = f"{R3D}/05_law_intermediary/LAW_INTERMEDIARY_REGISTER.csv"
R3_WB = "R4_CROSS_DOMAIN_VALIDATION/01_baseline/R3_ORIGINAL/final_package/REGULATORY_INTERMEDIATION_ARCHITECTURE_CASE_STUDY_DATASET.xlsx"
R3_P6 = f"{R3D}/12_audits/R3_PHASE_6_INTERMEDIATION_AUDIT.md"
R3_BND = f"{R3D}/06_relations/NEGATIVE_BOUNDARY_CASES.csv"
R3_CORP = f"{R3D}/02_corpus/R3_CORPUS_VALIDATION_REGISTER.csv"
R3_MAN = "R4_CROSS_DOMAIN_VALIDATION/R4_R3_BASELINE_MANIFEST.md"
R2D = "Before_R2/dataset-eurlex"
R2_EV = f"{R2D}/cases/final_human_review_v2/01_RELATION_EVIDENCE.csv"
R2_AM = f"{R2D}/cases/final_human_review_v2/02_ACTOR_ROLE_MAP.csv"
R2_SUM = f"{R2D}/cases/final_human_review_v2/SUMMARY_STATISTICS.json"
R2_ACT = f"{R2D}/cases/final_human_review_v2/04_ACT_REGIME_SUMMARY.csv"
R2_PROV = f"{R2D}/cases/final_human_review_v2/06_PROVENANCE.csv"
R2_CODEBOOK = f"{R2D}/methodology/codebook.md"
R2_CHANGELOG = f"{R2D}/docs/methodology/PRODUCTION_CHANGELOG.md"
R2_SENT = "Enviados/Email 01/DATASET_EURLEX_RIT_FINAL_FOR_DAVID.xlsx"
R2_RA = f"{R2D}/03_human/stage4_attempt_02/ra_4way/RA_4way_comparison.csv"
POC = "Before_R2/Estudos Preliminares e testes/PoC 01"
POC_V4_REL = f"{POC}/Entrega-04/data/rit_relationships_v4.csv"
POC_V4_SCR = f"{POC}/Entrega-04/data/screening_hits_v4.csv"
POC_V4_CB = f"{POC}/Entrega-04/RIT_CODEBOOK_v4.md"
POC_V3_REL = "Before_R2/Estudos Preliminares e testes/Entrega-02/data/rit_relationships_v3.csv"
POC_V2 = "Before_R2/Estudos Preliminares e testes/v1/PoC/data/rit_coded_sample_v2.csv"
POC_V1 = "Before_R2/Estudos Preliminares e testes/v1/PoC/data/rit_coded_sample.csv"
PL = "RELATIONAL_LEXIMETRICS_PILOT"
P3_A = f"{PL}/PILOT_03/04_MODEL_A/RELATIONSHIPS_MODEL_A.csv"
P3_B = f"{PL}/PILOT_03/05_MODEL_B/RELATIONSHIPS_MODEL_B.csv"
P3_PR = f"{PL}/PILOT_03/03_SOURCE_PROVISIONS/PROVISION_REGISTER.csv"
P3_RULES = f"{PL}/PILOT_03/01_PROTOCOL/CODING_RULES_V0_3_ADJUDICATED.md"
P3_MAN = f"{PL}/PILOT_03/99_REPRODUCIBILITY/PILOT_03_MANIFEST_FINAL.json"
P1_OBS = f"{PL}/PILOT_01/03_PILOT_DATA/RELATIONSHIP_OBSERVATIONS.csv"
P2_A = f"{PL}/PILOT_02/02_CODING_A/RELATIONSHIPS_CODER_A.csv"
ROT_XLSX = f"{PL}/PILOT_01/00_SOURCES/dataset_of_EU_regulatory_intermediation.xlsx"
ROT_CB = f"{PL}/PILOT_01/00_SOURCES/Codebook_Regulatory_Intermediation_Revised (1).docx"
R4D = "ENVIO_R4_TO_DAVID"
R4_EX = f"{R4D}/03_SOURCE_DATA_AND_CORPUS/R4_STRUCTURAL_EXTRACTION.csv"
R4_AC = f"{R4D}/04_R4_2_STRUCTURAL_EXTRACTION/R4_DIGITAL_ACTOR_CANDIDATE_REGISTER.csv"
R4_LA = f"{R4D}/04_R4_2_STRUCTURAL_EXTRACTION/R4_LEGAL_ACTION_REGISTER.csv"
R4_SUMM = f"{R4D}/01_FINAL_R4_DATASET/R4_DIGITAL_VALIDATION_SUMMARY_FOR_DAVID.csv"
R4_REG = f"{R4D}/03_SOURCE_DATA_AND_CORPUS/R4_DIGITAL_CORPUS_REGISTER.csv"
GP = "RGAM/pilot/GDPR_PILOT_01"
GP_Q = f"{GP}/03_EXTRACTION/QUALIFIED_RELATIONS.csv"
GP_N = f"{GP}/03_EXTRACTION/NORMATIVE_ASSIGNMENTS.csv"
GP_DESIGN = f"{GP}/00_PROTOCOL/RESEARCH_DESIGN.md"
GP_RULES = f"{GP}/00_PROTOCOL/DECISION_RULES.md"
CODEX_WB = "CODEX_ROTEM_SHARE_PACKAGE_20260930_2153/03_WORKBOOK/ROTEM_PILOT_RESULTS_SUMMARY.xlsx"
R07_REG = "AUTONOMOUS_ROTEM_COMPARISON_20260930_2047/07_CASE_SELECTION/CASE_REGISTER.csv"
R07_DSA = "AUTONOMOUS_ROTEM_COMPARISON_20260930_2047/01_BASELINES/BASELINE_R4_EXTRACTION_DSA_ART21_22_37_42.csv"
W21 = "WORK_2_1/PILOT_R2_1/PHASE_0B_TAXONOMY_SOURCE_RESOLUTION.md"
W21_INV = "WORK_2_1/PILOT_R2_1/PHASE_0_SOURCE_INVENTORY.csv"
V8INV = "COMPARATIVE_PILOTS/V8_COMP_01_2026-10-04/EXISTING_LEGAL_CORPUS_INVENTORY.csv"
V8MDR = "COMPARATIVE_PILOTS/V8_COMP_01_2026-10-04/01_MDR/MDR_SOURCE_CONTROL.md"
V8LEI = "COMPARATIVE_PILOTS/V8_COMP_01_2026-10-04/03_LEI_13848/README.md"
V8DSA = "COMPARATIVE_PILOTS/V8_COMP_01_2026-10-04/02_DSA/README.md"

# ----------------------------------------------------------------- family descriptors
FAMILY = {
    "R3": dict(
        pilot="R3 clean-room Regulatory Intermediation Architecture dataset (5 EU climate instruments)",
        directory="R4_CROSS_DOMAIN_VALIDATION/01_baseline/R3_ORIGINAL + R3_HISTORY_STAGING/PRJ-DAVID-R3/R3_CLEANROOM",
        version="R3 freeze 2026-09-21 (authoritative per R4_R3_BASELINE_MANIFEST); normalized linked tables + human-facing workbook (SHA FE3DE0A1...)",
        scope="FULL_INSTRUMENT",
        scope_note="Whole instrument incl. recitals and annexes; corpora validated (R3_CORPUS_VALIDATION_REGISTER: CORPUS_VALIDATED_WITH_DOCUMENTED_LIMITATIONS); all 56 candidate relations adjudicated, none silently added or deleted.",
        codebook="R3 clean-room gate (Phase 6): C1 identifiable R-T relation; C2 distinct institutionalized third party; C3 demonstrable mediating function; roles relational. Mechanism ontology (10 codes) not used here.",
        human="Model-assisted coding + adversarial review + researcher adjudication of mechanism events; relation adjudication (Phase 6/6B) documented; not independent statistical validation.",
        stratum="S1_R3_CLEANROOM_FROZEN",
        limits="Pilot of 5 laws; counts descriptive only (workbook README); regulators/targets per law are not published counts and are recounted from RELATIONS_ADJUDICATED; actor register mixes specific entities and actor classes.",
    ),
    "R2": dict(
        pilot="R2 dataset-eurlex three-case green-transition R-I-T dataset (Climate Law, CBAM, EUDR)",
        directory="Before_R2/dataset-eurlex/cases/final_human_review_v2",
        version="final_human_review_v2 (actor-in-role architecture; 25 relation records)",
        scope="FULL_INSTRUMENT",
        scope_note="Each frozen corpus was read in full by a memoryless primary reader; the retained relation set is a curated set of R-I-T relation records (direct, intermediated, uncertain, not supported), not a census of all regulatory relations.",
        codebook="dataset-eurlex production codebook v1.0 locked + PRODUCTION_CHANGELOG v1.1/v1.2: five-condition R-I-T test (A regulator, B target, C distinct third actor, D mediating function, E evidence).",
        human="Researcher approve/modify/confirm decisions recorded for 20 base records + 5 promoted records; 1 issue unresolved (case_02-U07); package states it is not a final published dataset.",
        stratum="S2_R2_RESEARCHER_REVIEW",
        limits="Source working file R2_HUMAN_VALIDATION_relations.csv was corrupted; 20 base rows were reconstructed from an in-session read (06_PROVENANCE.csv); evidence quotes NOT_RECOVERED for base rows; counts are of researcher-reviewed AI proposals.",
    ),
}

# ----------------------------------------------------------------- build case-version rows
rows = []  # master rows
prov = []  # provenance rows
cm = []    # comparability rows
hr = []    # harmonization rows
_cv = {"n": 0}


def add_cv(**kw):
    _cv["n"] += 1
    kw["cv_id"] = f"CV{_cv['n']:03d}"
    rows.append(kw)
    return kw["cv_id"]


def add_prov(cv, case, metric, value, vtype, files, locator, rule, codebook, note=""):
    files = files if isinstance(files, list) else ([files] if files else [])
    prov.append(dict(cv_id=cv, canonical_case_id=case, metric=metric, value_recorded="" if value is None else value,
                     value_type=vtype, source_files=" | ".join(files), source_file_sha256=" | ".join(sha(f) for f in files),
                     source_locator=locator, counting_rule=rule, definition_or_codebook_ref=codebook, notes=note))


def metrics_dict(**kw):
    d = {m: None for m in METRICS}
    d.update(kw)
    return d


# ----- instrument metadata ------------------------------------------------------------------
INST = {
    "32003L0087": ("Directive 2003/87/EC establishing a scheme for greenhouse gas emission allowance trading within the Community (EU ETS)", "EU", 2003),
    "32015D1814": ("Decision (EU) 2015/1814 concerning the establishment and operation of a market stability reserve for the Union greenhouse gas emission trading scheme", "EU", 2015),
    "32018R0842": ("Regulation (EU) 2018/842 on binding annual greenhouse gas emission reductions by Member States 2021-2030 (Effort Sharing Regulation)", "EU", 2018),
    "32021R1119": ("Regulation (EU) 2021/1119 establishing the framework for achieving climate neutrality (European Climate Law)", "EU", 2021),
    "32023R0955": ("Regulation (EU) 2023/955 establishing a Social Climate Fund", "EU", 2023),
    "32023R0956": ("Regulation (EU) 2023/956 establishing a carbon border adjustment mechanism (CBAM)", "EU", 2023),
    "32023R1115": ("Regulation (EU) 2023/1115 on the making available on the Union market and export of commodities and products associated with deforestation and forest degradation (EUDR)", "EU", 2023),
    "32022L2464": ("Directive (EU) 2022/2464 as regards corporate sustainability reporting (CSRD)", "EU", 2022),
    "32010R0066": ("Regulation (EC) No 66/2010 on the EU Ecolabel", "EU", 2010),
    "32019R2089": ("Regulation (EU) 2019/2089 as regards EU Climate Transition Benchmarks, EU Paris-aligned Benchmarks and sustainability-related disclosures for benchmarks", "EU", 2019),
    "32018R2067": ("Commission Implementing Regulation (EU) 2018/2067 on the verification of data and on the accreditation of verifiers (EU ETS)", "EU", 2018),
    "32020R0852": ("Regulation (EU) 2020/852 on the establishment of a framework to facilitate sustainable investment (Taxonomy Regulation)", "EU", 2020),
    "31976L0889": ("Council Directive 76/889/EEC on radio interference caused by electrical household appliances, portable tools and similar equipment", "EU (EEC)", 1976),
    "31986L0361": ("Council Directive 86/361/EEC on the initial stage of the mutual recognition of type approval for telecommunications terminal equipment", "EU (EEC)", 1986),
    "31987D0095": ("Council Decision 87/95/EEC on standardization in the field of information technology and telecommunications", "EU (EEC)", 1987),
    "31989L0336": ("Council Directive 89/336/EEC on electromagnetic compatibility", "EU (EEC)", 1989),
    "31991L0263": ("Council Directive 91/263/EEC on telecommunications terminal equipment, including the mutual recognition of their conformity", "EU (EEC)", 1991),
    "31992L0044": ("Council Directive 92/44/EEC on the application of open network provision to leased lines", "EU (EEC)", 1992),
    "32004L0048": ("Directive 2004/48/EC on the enforcement of intellectual property rights", "EU", 2004),
    "32004R0874": ("Commission Regulation (EC) No 874/2004 laying down public policy rules concerning the implementation and functions of the .eu Top Level Domain", "EU", 2004),
    "32006L0115": ("Directive 2006/115/EC on rental right and lending right and on certain rights related to copyright", "EU", 2006),
    "32006R1781": ("Regulation (EC) No 1781/2006 on information on the payer accompanying transfers of funds", "EU", 2006),
    "32016R0679": ("Regulation (EU) 2016/679 (General Data Protection Regulation, GDPR)", "EU", 2016),
    "32022R2065": ("Regulation (EU) 2022/2065 on a Single Market For Digital Services (Digital Services Act, DSA)", "EU", 2022),
    "32024R1689": ("Regulation (EU) 2024/1689 laying down harmonised rules on artificial intelligence (AI Act)", "EU", 2024),
    "32017R0745": ("Regulation (EU) 2017/745 on medical devices (MDR)", "EU", 2017),
    "BR-LEI-13848-2019": ("Lei n. 13.848/2019 (Brasil) - governance, management and social control of regulatory agencies", "Brazil", 2019),
    "32019R1150": ("Regulation (EU) 2019/1150 on promoting fairness and transparency for business users of online intermediation services (P2B)", "EU", 2019),
    "32019L0790": ("Directive (EU) 2019/790 on copyright and related rights in the Digital Single Market (CDSM)", "EU", 2019),
}
CASEID = lambda c: f"CASE-{c}"

DISP = {}  # cv_id -> (disposition, reason)

# ============================================================== R3 canonical rows
R3_CORE_NOTE = "Native values from R3 normalized tables; regulators/targets are deterministic recounts (see provenance)."
r3_cvs = {}
for celex, v in M["R3"].items():
    cv = add_cv(
        canonical_case_id=CASEID(celex), version_label="R3_FROZEN_2026-09-21", is_canonical_version="YES",
        instrument_title=INST[celex][0], jurisdiction=INST[celex][1], year=INST[celex][2], celex_or_identifier=celex,
        source_family="R3", source_pilot_dataset=FAMILY["R3"]["pilot"], source_directory=FAMILY["R3"]["directory"],
        extraction_version=FAMILY["R3"]["version"], corpus_scope="FULL_INSTRUMENT", scope_note=FAMILY["R3"]["scope_note"],
        codebook_ref=FAMILY["R3"]["codebook"], human_validation_status=FAMILY["R3"]["human"], known_limitations=FAMILY["R3"]["limits"],
        comparability_stratum="S1_R3_CLEANROOM_FROZEN",
        **metrics_dict(actors=v["actors_native"], regulators=v["regulators_distinct_all_relations"], intermediaries=v["intermediaries_native"],
                       targets=v["targets_distinct_all_relations"], relations=v["relations_native"], intermediation_relations=v["intermediation_native"]),
    )
    r3_cvs[celex] = cv
    cb = "R3 clean-room gate (R3_PHASE_6_INTERMEDIATION_AUDIT.md)"
    add_prov(cv, CASEID(celex), "actors", v["actors_native"], "NATIVE_RECORDED", R3_ACT, "rows where celex_id==case", "count of LAW x ACTOR records (89 across 5 laws)", cb)
    add_prov(cv, CASEID(celex), "regulators", v["regulators_distinct_all_relations"], "DERIVED_DETERMINISTIC_RECOUNT", R3_REL, "R_actor_id, all final classes", "distinct non-null R_actor_id across the law's adjudicated relations", cb)
    add_prov(cv, CASEID(celex), "intermediaries", v["intermediaries_native"], "NATIVE_RECORDED", R3_LI, "rows where celex_id==case", "count of LAW x INTERMEDIARY units (7 across 5 laws)", cb)
    add_prov(cv, CASEID(celex), "targets", v["targets_distinct_all_relations"], "DERIVED_DETERMINISTIC_RECOUNT", R3_REL, "T_actor_id, all final classes", "distinct non-null T_actor_id across the law's adjudicated relations (alt.: supported relations only = %d)" % v["targets_distinct_supported"], cb)
    add_prov(cv, CASEID(celex), "relations", v["relations_native"], "NATIVE_RECORDED", R3_REL, "rows where celex_id==case", "count of adjudicated relations, all final classes (56 across 5 laws)", cb)
    add_prov(cv, CASEID(celex), "intermediation_relations", v["intermediation_native"], "NATIVE_RECORDED", [R3_REL, R3_WB], "final_classification==SUPPORTED_INTERMEDIATION; workbook INSTRUMENTS sheet col 'Supported relations'", "count of relations with C1=C2=C3=YES (9 across 5 laws)", cb, "Cross-checked against workbook INSTRUMENTS sheet.")
DISP.update({cv: ("ELIGIBLE", "FULL_INSTRUMENT; R-I-T gate adjudicated at relation level; one pipeline for all five laws (stratum S1); canonical version under G5.") for cv in r3_cvs.values()})

# ============================================================== R2 final v2 rows
r2_cases = {"case_01": "32021R1119", "case_02": "32023R0956", "case_03": "32023R1115"}
SUM = json.load(open(os.path.join(ROOT, R2_SUM), encoding="utf-8"))
r2_final = {}
for case, celex in r2_cases.items():
    v = M["R2_final_v2"][case]
    s = SUM[case]
    is_dup = celex == "32021R1119"
    cv = add_cv(
        canonical_case_id=CASEID(celex), version_label="R2_final_human_review_v2", is_canonical_version="NO" if is_dup else "YES",
        instrument_title=INST[celex][0], jurisdiction=INST[celex][1], year=INST[celex][2], celex_or_identifier=celex,
        source_family="R2", source_pilot_dataset=FAMILY["R2"]["pilot"], source_directory=FAMILY["R2"]["directory"],
        extraction_version=FAMILY["R2"]["version"], corpus_scope="FULL_INSTRUMENT", scope_note=FAMILY["R2"]["scope_note"],
        codebook_ref=FAMILY["R2"]["codebook"], human_validation_status=FAMILY["R2"]["human"], known_limitations=FAMILY["R2"]["limits"],
        comparability_stratum="S2_R2_RESEARCHER_REVIEW",
        **metrics_dict(actors=v["actors_native"], regulators=v["regulators_native"], intermediaries=v["intermediaries_native"],
                       targets=v["targets_native"], relations=v["relations_native"], intermediation_relations=v["intermediation_native"]),
    )
    r2_final[celex] = cv
    cb = "dataset-eurlex production codebook v1.0 / changelog v1.2 (five-condition R-I-T test)"
    add_prov(cv, CASEID(celex), "actors", v["actors_native"], "NATIVE_RECORDED", [R2_AM, R2_SUM], "02_ACTOR_ROLE_MAP actor_name_normalized; SUMMARY_STATISTICS.actors", "distinct normalized actors holding an R, I or T role in the retained relation records", cb)
    add_prov(cv, CASEID(celex), "regulators", v["regulators_native"], "NATIVE_RECORDED", [R2_AM, R2_SUM], "role==R; SUMMARY_STATISTICS.R", "distinct normalized actors with role R", cb)
    add_prov(cv, CASEID(celex), "intermediaries", v["intermediaries_native"], "NATIVE_RECORDED", [R2_AM, R2_ACT, R2_SUM], "role==I; 04_ACT_REGIME_SUMMARY.unique_intermediaries_count", "distinct normalized actors with role I", cb)
    add_prov(cv, CASEID(celex), "targets", v["targets_native"], "NATIVE_RECORDED", [R2_AM, R2_SUM], "role==T; SUMMARY_STATISTICS.T", "distinct normalized actors with role T (note: SUMMARY_STATISTICS field 'target' is a different quantity)", cb)
    add_prov(cv, CASEID(celex), "relations", v["relations_native"], "NATIVE_RECORDED", [R2_EV, R2_SUM], "01_RELATION_EVIDENCE rows; SUMMARY_STATISTICS.relations", "all retained relation records: %s" % json.dumps(v["by_type"]), cb, "Includes uncertain and not-supported records.")
    add_prov(cv, CASEID(celex), "intermediation_relations", v["intermediation_native"], "NATIVE_RECORDED", [R2_EV, R2_ACT], "relation_type==intermediated; 04_ACT_REGIME_SUMMARY.intermediated_relations_count", "count of researcher-approved/modified intermediated relation records", cb)
    if is_dup:
        DISP[cv] = ("DUPLICATE_VERSION", "Second extraction of the European Climate Law (32021R1119). Canonical version under G5 is the R3 frozen version (authoritative, clean-room, same instrument). Retained and not merged; used only as the shared-instrument bridge in the comparability audit.")
    else:
        DISP[cv] = ("CONDITIONALLY_ELIGIBLE", "FULL_INSTRUMENT and R-I-T coded, but counts come from a different pipeline/codebook version than S1; bridge check on the Climate Law fails (G4), so ranking against S1 is not supported. Rankable only inside its own stratum S2 or if the research coordinator authorizes a documented pooling.")

# ============================================================== R2 other versions (superseded)
VERS_LABEL = {
    "CLAUDE_CODING_PROPOSAL": ("R2_primary_proposal_v1.0 (CLAUDE_CODING_PROPOSAL)", "cases/case_0N/primary_coding/CLAUDE_CODING_PROPOSAL.json"),
    "PRIMARY_INTERPRETIVE_READER_PROPOSAL": ("R2_primary_reader_v1.1 (PRIMARY_INTERPRETIVE_READER_PROPOSAL)", "cases/case_0N/primary_coding/PRIMARY_INTERPRETIVE_READER_PROPOSAL.json"),
    "PRIMARY_INTERPRETIVE_READER_PROPOSAL_R2": ("R2_primary_reader_R2 (PRIMARY_INTERPRETIVE_READER_PROPOSAL_R2; 20-row human validation export)", "cases/case_0N/primary_coding/PRIMARY_INTERPRETIVE_READER_PROPOSAL_R2.json"),
}
for case, celex in r2_cases.items():
    for name, (lab, path) in VERS_LABEL.items():
        v = M["R2_proposal_versions"][f"{case}|{name}"]
        src = f"{R2D}/" + path.replace("case_0N", case)
        cv = add_cv(
            canonical_case_id=CASEID(celex), version_label=lab, is_canonical_version="NO",
            instrument_title=INST[celex][0], jurisdiction=INST[celex][1], year=INST[celex][2], celex_or_identifier=celex,
            source_family="R2", source_pilot_dataset=FAMILY["R2"]["pilot"], source_directory=f"{R2D}/{case}/primary_coding",
            extraction_version=lab, corpus_scope="FULL_INSTRUMENT", scope_note="AI primary reading of the full frozen corpus; proposals before/without researcher adjudication.",
            codebook_ref=FAMILY["R2"]["codebook"], human_validation_status="AI proposal; not adjudicated (the later final_human_review_v2 records researcher decisions).",
            known_limitations="Superseded intermediate version; relation counts differ across versions (see CASE_UNIVERSE_NOTES).",
            comparability_stratum="NONE_SUPERSEDED",
            **metrics_dict(regulators=v["distinct_R"], intermediaries=v["distinct_I"], targets=v["distinct_T"], relations=v["relations"], intermediation_relations=v["intermediated"]),
        )
        DISP[cv] = ("DUPLICATE_VERSION", f"Superseded intermediate version of {CASEID(celex)} under the same R2 pipeline; kept to document version instability; cannot raise or replace the canonical counts (G5).")
        cb = "dataset-eurlex production codebook (version of that run)"
        for m, val, loc, rule in [("regulators", v["distinct_R"], "relations[].R[].label", "distinct R labels"), ("intermediaries", v["distinct_I"], "relations[].I[].label", "distinct I labels"),
                                  ("targets", v["distinct_T"], "relations[].T[].label", "distinct T labels"), ("relations", v["relations"], "len(relations)", "all relation records: " + json.dumps(v["by_type"])),
                                  ("intermediation_relations", v["intermediated"], "relation_type=='intermediated'", "count of intermediated records")]:
            add_prov(cv, CASEID(celex), m, val, "DERIVED_DETERMINISTIC_RECOUNT", src, loc, rule, cb, "Label counts are not normalized across spellings.")
        add_prov(cv, CASEID(celex), "actors", None, "NOT_RECORDED", src, "-", "no actor-in-role map exists for this version", cb)

# R2 'sent' dataset (Email 01)
for case, celex in r2_cases.items():
    v = M["R2_sent_dataset_email01"][case]
    cv = add_cv(
        canonical_case_id=CASEID(celex), version_label="R2_sent_to_David_DATASET_EURLEX_RIT_FINAL (Email 01, 20 relations)", is_canonical_version="NO",
        instrument_title=INST[celex][0], jurisdiction=INST[celex][1], year=INST[celex][2], celex_or_identifier=celex,
        source_family="R2", source_pilot_dataset=FAMILY["R2"]["pilot"], source_directory="Enviados/Email 01",
        extraction_version="Researcher-adjudicated three-case dataset sent to David (xlsx; 20 relations, uncertain/not-supported records not carried)",
        corpus_scope="FULL_INSTRUMENT", scope_note="Same corpora as R2 final; export of retained relations only.", codebook_ref=FAMILY["R2"]["codebook"],
        human_validation_status="Researcher-adjudicated per workbook header; formulas without cached values.", known_limitations="Superseded by final_human_review_v2 for counts of uncertain/not-supported records; intermediation counts agree.",
        comparability_stratum="NONE_SUPERSEDED",
        **metrics_dict(regulators=v.get("actor_role_records_R"), intermediaries=v.get("actor_role_records_I"), targets=v.get("actor_role_records_T"),
                       relations=v["relations"], intermediation_relations=v.get("intermediated", 0)),
    )
    DISP[cv] = ("DUPLICATE_VERSION", f"Earlier export of the R2 final dataset for {CASEID(celex)} (intermediation and intermediary counts agree with final_human_review_v2; total relations differ because uncertain/not-supported records were not carried). Not merged.")
    for m, val, loc in [("regulators", v.get("actor_role_records_R"), "ACTOR_ROLE_MAP role==R rows"), ("intermediaries", v.get("actor_role_records_I"), "ACTOR_ROLE_MAP role==I rows"),
                        ("targets", v.get("actor_role_records_T"), "ACTOR_ROLE_MAP role==T rows"), ("relations", v["relations"], "RELATION_EVIDENCE rows"),
                        ("intermediation_relations", v.get("intermediated", 0), "RELATION_EVIDENCE relation_type=='intermediated'")]:
        add_prov(cv, CASEID(celex), m, val, "DERIVED_DETERMINISTIC_RECOUNT", R2_SENT, loc, "row count", "dataset-eurlex production codebook")
    add_prov(cv, CASEID(celex), "actors", None, "NOT_RECORDED", R2_SENT, "-", "actor-role records are role rows, not unique actors", "-")

# R2 Stage-4 climate law pilot
st = M["R2_stage4_climate_law"]
cv = add_cv(
    canonical_case_id=CASEID("32021R1119"), version_label="R2_stage4_attempt02_reference_adjudication (pre-human-gate)", is_canonical_version="NO",
    instrument_title=INST["32021R1119"][0], jurisdiction="EU", year=2021, celex_or_identifier="32021R1119",
    source_family="R2", source_pilot_dataset="dataset-eurlex Stage 4 candidate universe on the Climate Law", source_directory=f"{R2D}/03_human/stage4_attempt_02",
    extraction_version="stage4_attempt_02 (ra_4way); methodology_locked / human gate not executed", corpus_scope="FULL_INSTRUMENT",
    scope_note="Candidate universe from lexical screening + structural reading of the full act.", codebook_ref="dataset-eurlex methodology v1.1.x",
    human_validation_status="Pre-human-gate; reference adjudication (RA) outputs only.", known_limitations="Candidates are provision-anchored screening units, not relations; superseded by later R2 production.",
    comparability_stratum="NONE_SUPERSEDED",
    **metrics_dict(intermediation_relations=0),
)
DISP[cv] = ("DUPLICATE_VERSION", "Earlier pilot candidate adjudication on the Climate Law (%d candidates; RA result %s). Version of CASE-32021R1119; not merged." % (st["candidates_attempt02"], json.dumps(st["RA_result"])))
add_prov(cv, CASEID("32021R1119"), "intermediation_relations", 0, "NATIVE_RECORDED", R2_RA, "RA_result column", "count of candidates with RA_result positive (0; %s)" % json.dumps(st["RA_result"]), "dataset-eurlex methodology v1.1.x", "Candidates, not relations; human gate not executed.")
for m in ["actors", "regulators", "intermediaries", "targets", "relations"]:
    add_prov(cv, CASEID("32021R1119"), m, None, "NOT_RECORDED", R2_RA, "-", "metric not produced in this stage", "-")

# ============================================================== PoC (v4 + older)
poc_acts = ["32022L2464", "32010R0066", "32019R2089", "32018R2067", "32020R0852"]
for celex in poc_acts:
    p = M["PoC"].get(celex, {})
    rel = p.get("v4_relations")
    if celex == "32020R0852":
        cv = add_cv(
            canonical_case_id=CASEID(celex), version_label="PoC_v4_screening_only", is_canonical_version="YES",
            instrument_title=INST[celex][0], jurisdiction="EU", year=INST[celex][2], celex_or_identifier=celex, source_family="POC",
            source_pilot_dataset="PoC 01 / Entrega-04 (five-act lexical screening) and R2.1 source inventory", source_directory=f"{POC}/Entrega-04 ; WORK_2_1/PILOT_R2_1",
            extraction_version="PoC v4 screening hits (13) ; R2.1 phase 0/0B source resolution", corpus_scope="UNKNOWN",
            scope_note="Only lexical screening hits (13) and a source-resolution audit; no R-I-T relation record; R2.1 stopped at a source gate.",
            codebook_ref="PoC SCREENING_CODEBOOK_v4 (lexical, not relational)", human_validation_status="None.", known_limitations="No relational extraction exists.",
            comparability_stratum="NONE", **metrics_dict())
        DISP[cv] = ("INSUFFICIENT_SOURCE", "No relation, actor or intermediary records exist for the Taxonomy Regulation: only 13 lexical screening hits (PoC) and a source-resolution audit (R2.1, which stopped before substantive analysis).")
        for m in METRICS:
            add_prov(cv, CASEID(celex), m, None, "NOT_RECORDED", [POC_V4_SCR, W21], "-", "metric not produced", "-")
        continue
    cv = add_cv(
        canonical_case_id=CASEID(celex), version_label="PoC_v4_final", is_canonical_version="YES",
        instrument_title=INST[celex][0], jurisdiction="EU", year=INST[celex][2], celex_or_identifier=celex, source_family="POC",
        source_pilot_dataset="PoC 01 / Entrega-04 five-act R-I-T proof of concept", source_directory=f"{POC}/Entrega-04/data",
        extraction_version="PoC v4 (CELEX_MANIFEST_v4; rit_relationships_v4; actors_v4)", corpus_scope="LIMITED_PROVISIONS",
        scope_note="Lexical screening covered the act (%s hits) but R-I-T relations were coded only for a small purposive sample of lexical-hit provisions; only positive relations are stored." % p.get("v4_screening_hits"),
        codebook_ref="RIT_CODEBOOK_v4 (five-condition relational test; only positives enter rit_relationships_v4)", human_validation_status="Limited human review (human_review_v4.csv); AI-assisted runs logged.",
        known_limitations="Purposive sample; actor ids are shared across acts; absence of rows is not absence of intermediation; benchmark-administrator relation left conditional (no row).",
        comparability_stratum="NONE",
        **metrics_dict(actors=p.get("v4_actor_ids"), regulators=p.get("v4_R"), intermediaries=p.get("v4_I"), targets=p.get("v4_T"), relations=rel, intermediation_relations=rel))
    if rel is None:
        for m in METRICS:
            add_prov(cv, CASEID(celex), m, None, "NOT_RECORDED", POC_V4_REL, "no relationship row for this act", "benchmark-administrator candidate left conditional/unresolved; no positive relation stored", "RIT_CODEBOOK_v4")
        # intermediation recorded as zero positives stored but not a verified zero
        rows[-1]["intermediation_relations"] = None
    else:
        rule = "distinct actor ids (R,I,T union) in rit_relationships_v4 rows for the act"
        add_prov(cv, CASEID(celex), "actors", p["v4_actor_ids"], "DERIVED_DETERMINISTIC_RECOUNT", POC_V4_REL, "R_actor_id,I_actor_id,T_actor_id", rule, "RIT_CODEBOOK_v4")
        add_prov(cv, CASEID(celex), "regulators", p["v4_R"], "DERIVED_DETERMINISTIC_RECOUNT", POC_V4_REL, "R_actor_id", "distinct R_actor_id", "RIT_CODEBOOK_v4")
        add_prov(cv, CASEID(celex), "intermediaries", p["v4_I"], "DERIVED_DETERMINISTIC_RECOUNT", POC_V4_REL, "I_actor_id", "distinct I_actor_id", "RIT_CODEBOOK_v4")
        add_prov(cv, CASEID(celex), "targets", p["v4_T"], "DERIVED_DETERMINISTIC_RECOUNT", POC_V4_REL, "T_actor_id", "distinct T_actor_id", "RIT_CODEBOOK_v4")
        add_prov(cv, CASEID(celex), "relations", rel, "NATIVE_RECORDED", POC_V4_REL, "rows where source_act==case", "positive relation rows (levels L1/L2 are separate rows)", "RIT_CODEBOOK_v4")
        add_prov(cv, CASEID(celex), "intermediation_relations", rel, "NATIVE_RECORDED", POC_V4_REL, "rows where source_act==case", "positive relation rows (only positives are stored)", "RIT_CODEBOOK_v4")
    DISP[cv] = ("NON_COMPARABLE", "LIMITED_PROVISIONS: R-I-T coding was a purposive sample of lexical hits and only positives were stored; cannot compete with full-instrument extractions (G2).")
    # older versions of the same acts
    if p.get("v3_relations") is not None:
        cv3 = add_cv(canonical_case_id=CASEID(celex), version_label="PoC_v3 (Entrega-02/03)", is_canonical_version="NO", instrument_title=INST[celex][0], jurisdiction="EU", year=INST[celex][2], celex_or_identifier=celex,
                     source_family="POC", source_pilot_dataset="PoC 01 / Entrega-02-03 (v3)", source_directory="Before_R2/Estudos Preliminares e testes/Entrega-02/data", extraction_version="PoC v3 (rit_relationships_v3.csv)",
                     corpus_scope="LIMITED_PROVISIONS", scope_note="Sample-based R-I-T coding on four acts.", codebook_ref="RIT_CODEBOOK_v3", human_validation_status="Limited.",
                     known_limitations="Earlier version of PoC v4.", comparability_stratum="NONE_SUPERSEDED", **metrics_dict(relations=p["v3_relations"], intermediation_relations=p["v3_relations"]))
        DISP[cv3] = ("DUPLICATE_VERSION", f"Earlier PoC version (v3) of {CASEID(celex)}; superseded by PoC v4; not merged.")
        add_prov(cv3, CASEID(celex), "relations", p["v3_relations"], "NATIVE_RECORDED", POC_V3_REL, "rows where source_act==case", "relation rows", "RIT_CODEBOOK_v3")
        add_prov(cv3, CASEID(celex), "intermediation_relations", p["v3_relations"], "NATIVE_RECORDED", POC_V3_REL, "rows where source_act==case", "relation rows (positives only)", "RIT_CODEBOOK_v3")
        for m in ["actors", "regulators", "intermediaries", "targets"]:
            add_prov(cv3, CASEID(celex), m, None, "NOT_RECORDED", POC_V3_REL, "-", "not recounted for superseded version", "-")
    if p.get("v2_sample_rows") is not None:
        cv2 = add_cv(canonical_case_id=CASEID(celex), version_label="PoC_v2 (v1/PoC rit_coded_sample_v2)", is_canonical_version="NO", instrument_title=INST[celex][0], jurisdiction="EU", year=INST[celex][2], celex_or_identifier=celex,
                     source_family="POC", source_pilot_dataset="PoC v1/v2 early R-I-T sample", source_directory="Before_R2/Estudos Preliminares e testes/v1/PoC/data", extraction_version="rit_coded_sample_v2.csv",
                     corpus_scope="LIMITED_PROVISIONS", scope_note="Early sample rows incl. deliberate non-intermediation controls.", codebook_ref="v1/v2 early R-I-T codebook", human_validation_status="None evidenced.",
                     known_limitations="Early exploratory sample; includes controls.", comparability_stratum="NONE_SUPERSEDED", **metrics_dict(relations=p["v2_sample_rows"]))
        DISP[cv2] = ("DUPLICATE_VERSION", f"Early PoC sample rows for {CASEID(celex)} (include deliberate non-intermediation controls); superseded; not merged.")
        add_prov(cv2, CASEID(celex), "relations", p["v2_sample_rows"], "NATIVE_RECORDED", POC_V2, "rows where source_act==case", "sample rows (positives and controls)", "early R-I-T codebook")
        for m in ["actors", "regulators", "intermediaries", "targets", "intermediation_relations"]:
            add_prov(cv2, CASEID(celex), m, None, "NOT_RECORDED", POC_V2, "-", "not recounted for superseded version (rows mix positives and controls)", "-")
    n1 = M["PoC"]["_v1_by_act"].get(celex)
    if n1:
        cv1 = add_cv(canonical_case_id=CASEID(celex), version_label="PoC_v1 (rit_coded_sample.csv, ragged file)", is_canonical_version="NO", instrument_title=INST[celex][0], jurisdiction="EU", year=INST[celex][2], celex_or_identifier=celex,
                     source_family="POC", source_pilot_dataset="PoC v1 early R-I-T sample", source_directory="Before_R2/Estudos Preliminares e testes/v1/PoC/data", extraction_version="rit_coded_sample.csv",
                     corpus_scope="LIMITED_PROVISIONS", scope_note="One early sample row per act; CSV is ragged (parsed with csv module).", codebook_ref="v1 early R-I-T codebook", human_validation_status="None evidenced.",
                     known_limitations="Earliest exploratory sample.", comparability_stratum="NONE_SUPERSEDED", **metrics_dict(relations=n1))
        DISP[cv1] = ("DUPLICATE_VERSION", f"Earliest PoC sample row for {CASEID(celex)}; superseded; not merged.")
        add_prov(cv1, CASEID(celex), "relations", n1, "NATIVE_RECORDED", POC_V1, "first column == source_act", "sample rows", "v1 early codebook")
        for m in ["actors", "regulators", "intermediaries", "targets", "intermediation_relations"]:
            add_prov(cv1, CASEID(celex), m, None, "NOT_RECORDED", POC_V1, "-", "not recounted for superseded version", "-")

# ============================================================== PILOT_01/02/03
pilot_acts = ["31976L0889", "31986L0361", "31987D0095", "31989L0336", "31991L0263", "31992L0044", "32004L0048", "32004R0874", "32006L0115", "32006R1781"]
P1KEY = {"31976L0889": "76/889/EEC", "31989L0336": "89/336/EEC", "31991L0263": "91/263/EEC", "32004R0874": "EC 874/2004", "32006R1781": "1781/2006"}
for celex in pilot_acts:
    p = M["PILOT_03"][celex]
    cv = add_cv(
        canonical_case_id=CASEID(celex), version_label="PILOT_03_v0.3_post_adjudication", is_canonical_version="YES",
        instrument_title=INST[celex][0], jurisdiction=INST[celex][1], year=INST[celex][2], celex_or_identifier=celex, source_family="PILOT",
        source_pilot_dataset="Relational Leximetrics PILOT_03 (calibration + blind challenge samples)", source_directory=f"{PL}/PILOT_03",
        extraction_version="PILOT_03 v0.3 (two model passes A/B; 19 targeted human decisions; gate ONTOLOGY_STABLE_WITH_REVISIONS; production_authorized=false)", corpus_scope="LIMITED_PROVISIONS",
        scope_note=f"{p['provisions']} purposively selected provisions of the act captured from official text; no full-act extraction.",
        codebook_ref="PILOT_03 CODING_RULES_V0_3_ADJUDICATED (primitive actor-action-recipient edges; intermediary status is a relational position; derived R-I-T candidates)",
        human_validation_status="Targeted human adjudication of 19 items (14 retrospective); not full human reliability; counts below are model-pass counts (pre-adjudication rows).",
        known_limitations="Provisions selected from Rotem's act-level intermediary coding; edge-based unit; model-coded rows; adjudicated decisions not merged back into the pass files.",
        comparability_stratum="NONE",
        **metrics_dict(actors=p["distinct_actors_A"], intermediaries=p["distinct_intermediary_actor_b_A"], relations=p["edges_modelA"], intermediation_relations=p["derived_rit_candidates_A"]))
    DISP[cv] = ("NON_COMPARABLE", "LIMITED_PROVISIONS (2-6 purposively selected provisions) and model-pass edge counts; derived R-I-T candidates are not adjudicated intermediation relations (G2/G3).")
    cb = "PILOT_03 CODING_RULES_V0_3_ADJUDICATED"
    add_prov(cv, CASEID(celex), "actors", p["distinct_actors_A"], "DERIVED_DETERMINISTIC_RECOUNT", P3_A, "actor_a, actor_b, recipient_actor, oversight_actor (lower-cased, whitespace-normalized)", "distinct names across the act's Model A rows", cb, "Model B has identical row counts; names not entity-resolved.")
    add_prov(cv, CASEID(celex), "regulators", None, "NOT_RECORDED", P3_A, "actor_*_role incomplete", "role fields use 'actor'/'recipient' as well as regulator/target; not recounted", cb)
    add_prov(cv, CASEID(celex), "intermediaries", p["distinct_intermediary_actor_b_A"], "DERIVED_DETERMINISTIC_RECOUNT", P3_A, "actor_b where intermediary_status_derived in (YES, DERIVED_POSITION)", "distinct normalized actor_b names", cb)
    add_prov(cv, CASEID(celex), "targets", None, "NOT_RECORDED", P3_A, "-", "target role not recorded consistently; not recounted", cb)
    add_prov(cv, CASEID(celex), "relations", p["edges_modelA"], "NATIVE_RECORDED", [P3_A, P3_B, P3_PR], "rows where celex==case", "edge rows in Model A (Model B identical count %d); provisions=%d" % (p["edges_modelB"], p["provisions"]), cb)
    add_prov(cv, CASEID(celex), "intermediation_relations", p["derived_rit_candidates_A"], "NATIVE_RECORDED", [P3_A, P3_B], "derived_rit_candidate=='YES'", "count of edges flagged derived R-I-T candidate (Model B: %d)" % p["derived_rit_candidates_B"], cb, "Candidate flag, not an adjudicated positive relation.")
    # PILOT_01 and PILOT_02 earlier versions
    if celex in P1KEY:
        q1 = M["PILOT_01"][P1KEY[celex]]
        c1 = add_cv(canonical_case_id=CASEID(celex), version_label="PILOT_01_v0.1", is_canonical_version="NO", instrument_title=INST[celex][0], jurisdiction=INST[celex][1], year=INST[celex][2], celex_or_identifier=celex,
                    source_family="PILOT", source_pilot_dataset="Relational Leximetrics PILOT_01", source_directory=f"{PL}/PILOT_01/03_PILOT_DATA", extraction_version="PILOT_01 RELATIONSHIP_OBSERVATIONS (model pilot)",
                    corpus_scope="LIMITED_PROVISIONS", scope_note="Selected provisions per act.", codebook_ref="PILOT_01 RELATIONAL_MODEL_V0_1", human_validation_status="None (model pilot).", known_limitations="Superseded by PILOT_02/03.",
                    comparability_stratum="NONE_SUPERSEDED", **metrics_dict(relations=q1["relationships"], intermediation_relations=q1["with_actor_i"]))
        DISP[c1] = ("DUPLICATE_VERSION", f"Earlier pilot version (PILOT_01) of {CASEID(celex)}; superseded by PILOT_03; not merged.")
        add_prov(c1, CASEID(celex), "relations", q1["relationships"], "NATIVE_RECORDED", P1_OBS, "rows where act_id==case", "relationship observation rows", "PILOT_01 relational model v0.1")
        add_prov(c1, CASEID(celex), "intermediation_relations", q1["with_actor_i"], "DERIVED_DETERMINISTIC_RECOUNT", P1_OBS, "actor_i non-null", "rows with an actor_i value", "PILOT_01 relational model v0.1", "Non-null actor_i is a candidate position, not an adjudicated positive.")
        for m in ["actors", "regulators", "intermediaries", "targets"]:
            add_prov(c1, CASEID(celex), m, None, "NOT_RECORDED", P1_OBS, "-", "not recounted for superseded version", "-")
        q2 = M["PILOT_02"][celex]
        c2 = add_cv(canonical_case_id=CASEID(celex), version_label="PILOT_02_v0.2 (Coder A)", is_canonical_version="NO", instrument_title=INST[celex][0], jurisdiction=INST[celex][1], year=INST[celex][2], celex_or_identifier=celex,
                    source_family="PILOT", source_pilot_dataset="Relational Leximetrics PILOT_02", source_directory=f"{PL}/PILOT_02", extraction_version="PILOT_02 Coder A / Coder B (agreement test)",
                    corpus_scope="LIMITED_PROVISIONS", scope_note="Selected provisions per act.", codebook_ref="PILOT_02 CODING_RULES_V0_2", human_validation_status="Model coders A/B; adjudication register.", known_limitations="Superseded by PILOT_03.",
                    comparability_stratum="NONE_SUPERSEDED", **metrics_dict(relations=q2["relationships"], intermediation_relations=q2["with_actor_i"]))
        DISP[c2] = ("DUPLICATE_VERSION", f"Earlier pilot version (PILOT_02) of {CASEID(celex)}; superseded by PILOT_03; not merged.")
        add_prov(c2, CASEID(celex), "relations", q2["relationships"], "NATIVE_RECORDED", P2_A, "rows where celex==case", "Coder A relationship rows", "PILOT_02 coding rules v0.2")
        add_prov(c2, CASEID(celex), "intermediation_relations", q2["with_actor_i"], "DERIVED_DETERMINISTIC_RECOUNT", P2_A, "actor_i non-null", "Coder A rows with an actor_i value", "PILOT_02 coding rules v0.2", "Candidate position, not an adjudicated positive.")
        for m in ["actors", "regulators", "intermediaries", "targets"]:
            add_prov(c2, CASEID(celex), m, None, "NOT_RECORDED", P2_A, "-", "not recounted for superseded version", "-")

# ============================================================== R4 digital + GDPR pilot + DSA subsets + Rotem packs
r4map = {"D1_GDPR": "32016R0679", "D2_DSA": "32022R2065", "D3_AI_ACT": "32024R1689"}
for key, celex in r4map.items():
    v = M["R4"][key]
    cv = add_cv(
        canonical_case_id=CASEID(celex), version_label="R4.2E_structural_extraction_frozen", is_canonical_version="YES",
        instrument_title=INST[celex][0], jurisdiction="EU", year=INST[celex][2], celex_or_identifier=celex, source_family="R4",
        source_pilot_dataset="R4 cross-domain digital structural validation", source_directory=f"{R4D} ; R4_CROSS_DOMAIN_VALIDATION/03_extraction",
        extraction_version="R4.2 structural extraction (LEGAL PROVISION x ACTOR x LEGAL ACTION), R4.2E advanced validation; no R/I/T", corpus_scope="FULL_INSTRUMENT",
        scope_note="Whole instrument processed (operative articles, recitals%s); records: %s" % (", annexes" if "ANNEX" in v["by_source_type"] else "", json.dumps(v["by_source_type"])),
        codebook_ref="R4.2 structural method note (no regulator/intermediary/target coding)", human_validation_status="Human corpus acceptance APPROVED; human QA incomplete; extraction requires repair (R4.2E).",
        known_limitations="Regulator/intermediary/target and mechanism coding 'not started'; 181 of 1404 records lack a stored source excerpt; counterpart/recipient fields identical in 1404/1404 records.",
        comparability_stratum="NONE", **metrics_dict(actors=v["actor_candidates"]))
    DISP[cv] = ("NON_COMPARABLE", "Whole-instrument structural extraction exists, but no regulator/intermediary/target/relation/intermediation metric was ever produced (R4 summary: 'Regulator / intermediary / target coding: not started'); actors are provisional textual candidates (G3).")
    add_prov(cv, CASEID(celex), "actors", v["actor_candidates"], "NATIVE_RECORDED", [R4_AC, R4_SUMM], "rows where CASE_ID==%s" % key, "provisional actor candidates (normalization/merge ambiguity flagged)", "R4.2 structural method note", "Includes any actor mentioned in provisions/recitals/annexes; not R/I/T roles.")
    for m, why in [("regulators", "regulator coding not started"), ("intermediaries", "intermediary coding not started"), ("targets", "target coding not started"), ("intermediation_relations", "R-I-T / intermediation coding not started")]:
        add_prov(cv, CASEID(celex), m, None, "NOT_RECORDED", R4_SUMM, "row 'Regulator / intermediary / target coding'", why, "R4.2 structural method note")
    add_prov(cv, CASEID(celex), "relations", None, "NOT_RECORDED", [R4_EX, R4_SUMM], "-", "structural records (%d) are provision x actor x action units, not relations; legal-action register rows=%d" % (v["structural_records"], v["legal_action_rows"]), "R4.2 structural method note", "Records are listed in scope_note; not used as relations.")

g = M["GDPR_PILOT_01"]
cv = add_cv(
    canonical_case_id=CASEID("32016R0679"), version_label="GDPR_PILOT_01 (RGAM/V6 relational extraction, 2026-10-03)", is_canonical_version="NO",
    instrument_title=INST["32016R0679"][0], jurisdiction="EU", year=2016, celex_or_identifier="32016R0679", source_family="GDPR_PILOT",
    source_pilot_dataset="RGAM GDPR Pilot 01 (extraction layer only used)", source_directory=GP + "/03_EXTRACTION",
    extraction_version="DECISION_RULES v1.0-v1.2; 389 paragraph units screened; 238 qualified relations, 157 normative assignments, 47 positions/devices", corpus_scope="SUBSTANTIAL_DEFINED_SUBSET",
    scope_note="All 99 operative articles (389 paragraph units, 382 points inventoried); recitals not reviewed; corrected/consolidated historical text baseline (not the R4 frozen original).",
    codebook_ref="RGAM v0.6.1 / V6 ontology (relation types, positions, devices); no R-I-T gate", human_validation_status="Single AI evaluator; machine-provisional; 16 adjudication items pending; blind human coding not done.",
    known_limitations="Different ontology and text version from R4; qualified relations cover all relation types (information/reporting, authority/control, etc.); extraction-layer counts only (architectural outputs not opened).",
    comparability_stratum="NONE", **metrics_dict(actors=g["distinct_origin_or_counterpart_union"], relations=g["qualified_relations"]))
DISP[cv] = ("DUPLICATE_VERSION", "Second extraction of the GDPR (different ontology and text baseline) under a pipeline that never applied the R-I-T gate; version of CASE-32016R0679, not merged with the R4 structural extraction; its architectural outputs are prohibited material and were not opened.")
add_prov(cv, CASEID("32016R0679"), "actors", g["distinct_origin_or_counterpart_union"], "DERIVED_DETERMINISTIC_RECOUNT", GP_Q, "origin, counterpart", "distinct strings in origin U counterpart (origin=%d, counterpart=%d)" % (g["distinct_origin"], g["distinct_counterpart"]), "RGAM/V6 decision rules", "String-level distinct count; no entity resolution.")
add_prov(cv, CASEID("32016R0679"), "relations", g["qualified_relations"], "NATIVE_RECORDED", [GP_Q, GP_DESIGN], "QUALIFIED_RELATIONS.csv rows", "qualified relations of all RGAM relation types", "RGAM/V6 decision rules")
for m in ["regulators", "intermediaries", "targets", "intermediation_relations"]:
    add_prov(cv, CASEID("32016R0679"), m, None, "NOT_RECORDED", GP_Q, "-", "R-I-T roles / intermediation relations not coded in this ontology; recount would require interpretation", "RGAM/V6 decision rules")

cv = add_cv(
    canonical_case_id=CASEID("32022R2065"), version_label="R4_extraction_subset_Arts_21_22_37_42 (Rotem comparison baseline)", is_canonical_version="NO",
    instrument_title=INST["32022R2065"][0], jurisdiction="EU", year=2022, celex_or_identifier="32022R2065", source_family="ROTEM_PACK",
    source_pilot_dataset="Autonomous Rotem comparison (R07 CASE_05 / CASE_06)", source_directory="AUTONOMOUS_ROTEM_COMPARISON_20260930_2047/01_BASELINES + 07_CASE_SELECTION",
    extraction_version="BASELINE_R4_EXTRACTION_DSA_ART21_22_37_42 (%d rows)" % M["R4_DSA_art21_22_37_42_rows"], corpus_scope="LIMITED_PROVISIONS",
    scope_note="Provision packs for Arts 22 (trusted flaggers), 37 (independent audit), 42(4); copied R4 rows only.", codebook_ref="Rotem revised codebook comparison (R07 protocol)", human_validation_status="No human relational baseline.",
    known_limitations="Provision pack for a comparison test; not a case extraction.", comparability_stratum="NONE", **metrics_dict())
DISP[cv] = ("DUPLICATE_VERSION", "Provision pack of the DSA used in the Rotem comparison; subset copy of R4 rows; version of CASE-32022R2065; not merged.")
for m in METRICS:
    add_prov(cv, CASEID("32022R2065"), m, None, "NOT_RECORDED", R07_DSA, "-", "no case-level metric defined for a provision pack", "-")

# Rotem comparison packs (R07 cases 1-4 are PILOT_03 acts; Codex package five diagnostic cases)
r07_map = {"31991L0263": "CASE_03", "32004R0874": "CASE_01", "31989L0336": "CASE_02", "31986L0361": "CASE_04"}
for celex, c in r07_map.items():
    n_ev = M["Codex_package_events_by_case"].get({"CASE_01": "CASE_01", "CASE_02": "CASE_02", "CASE_03": "CASE_03", "CASE_04": "CASE_04"}[c])
    cv = add_cv(
        canonical_case_id=CASEID(celex), version_label=f"Rotem_comparison_pack_{c} / Codex share package", is_canonical_version="NO",
        instrument_title=INST[celex][0], jurisdiction=INST[celex][1], year=INST[celex][2], celex_or_identifier=celex, source_family="ROTEM_PACK",
        source_pilot_dataset="Autonomous Rotem comparison R07 / Codex Rotem share package (diagnostic cases)", source_directory="AUTONOMOUS_ROTEM_COMPARISON_20260930_2047/07_CASE_SELECTION ; CODEX_ROTEM_SHARE_PACKAGE_20260930_2153/03_WORKBOOK",
        extraction_version="Provision-event diagnostics (%s provision events in the Codex workbook)" % n_ev, corpus_scope="LIMITED_PROVISIONS", scope_note="Provision pack of the PILOT_03 act for a codebook comparison.",
        codebook_ref="Rotem revised codebook crosswalk", human_validation_status="Codex-reviewed rows are not human adjudications.", known_limitations="Diagnostic pack, not a case extraction.", comparability_stratum="NONE", **metrics_dict())
    DISP[cv] = ("DUPLICATE_VERSION", f"Provision pack/diagnostic for {CASEID(celex)} built from PILOT_03 material; version, not a separate case; not merged.")
    for m in METRICS:
        add_prov(cv, CASEID(celex), m, None, "NOT_RECORDED", [R07_REG, CODEX_WB], "-", "no case-level metric defined for a diagnostic provision pack", "-")

# Rotem structured lists for P2B, CDSM, DSA
for celex, key in [("32019R1150", "2019/1150"), ("32019L0790", "2019/790"), ("32022R2065", "2022/2065")]:
    nloa = M["Rotem_LoA_rows"].get(key)
    cv = add_cv(
        canonical_case_id=CASEID(celex), version_label="Rotem_List_of_actors_intermediaries", is_canonical_version="NO" if celex == "32022R2065" else "YES",
        instrument_title=INST[celex][0], jurisdiction="EU", year=INST[celex][2], celex_or_identifier=celex, source_family="ROTEM_LIST",
        source_pilot_dataset="Rotem dataset_of_EU_regulatory_intermediation.xlsx (List of actors / List of intermediaries)", source_directory=f"{PL}/PILOT_01/00_SOURCES",
        extraction_version="Rotem workbook sheets 'List of actors' (+ 'List of intermediaries' for P2B/CDSM)", corpus_scope="UNKNOWN", scope_note="Act-level expert listing of intermediaries; extraction coverage of the act not documented.",
        codebook_ref="Rotem revised codebook (digital intermediary; includes process-based arrangements)", human_validation_status="Expert-coded by Rotem (external); not a PRJ-David extraction.",
        known_limitations="Rows list intermediary labels per act, not R-I-T relations; official texts not fetched in PRJ-David pilots for P2B/CDSM.",
        comparability_stratum="NONE", **metrics_dict(intermediaries=nloa))
    DISP[cv] = ("NON_COMPARABLE", "External expert listing under Rotem's own definition (intermediary labels/arrangements, not R-I-T relations); no relation, regulator or target count; scope undocumented (G1/G3)." + (" Version of CASE-32022R2065 (DSA)." if celex == "32022R2065" else ""))
    add_prov(cv, CASEID(celex), "intermediaries", nloa, "DERIVED_DETERMINISTIC_RECOUNT", ROT_XLSX, "'List of actors' column Intermediary_legal_label non-empty rows for reference code %s" % key, "count of listed intermediary rows (not entity-resolved)", "Rotem revised codebook", "Counts rows including process-based arrangements.")
    for m in ["actors", "regulators", "targets", "relations", "intermediation_relations"]:
        add_prov(cv, CASEID(celex), m, None, "NOT_RECORDED", ROT_XLSX, "-", "not coded as a count in the Rotem sheets", "Rotem revised codebook")

# Provisional / not-started cases
for celex, src, why in [("32017R0745", V8MDR, "official text snapshot not obtained (SOURCE_PENDING_TEXT_SNAPSHOT); no extraction"), ("BR-LEI-13848-2019", V8LEI, "NOT_STARTED; no source or evidence extracted")]:
    cv = add_cv(
        canonical_case_id=CASEID(celex), version_label="V8_COMP_01 provisional case (not started)", is_canonical_version="YES",
        instrument_title=INST[celex][0], jurisdiction=INST[celex][1], year=INST[celex][2], celex_or_identifier=celex if celex[0] == "3" else "none (national law)", source_family="NOT_STARTED",
        source_pilot_dataset="V8_COMP_01 candidate-case folders (pointer files only)", source_directory=os.path.dirname(src), extraction_version="none", corpus_scope="UNKNOWN",
        scope_note=why, codebook_ref="-", human_validation_status="None.", known_limitations="No extraction exists.", comparability_stratum="NONE", **metrics_dict())
    DISP[cv] = ("INSUFFICIENT_SOURCE", f"Named as a provisional case in the V8_COMP_01 stream but never extracted: {why}.")
    for m in METRICS:
        add_prov(cv, CASEID(celex), m, None, "NOT_RECORDED", src, "-", why, "-")

# Prohibited material rows (non-circularity): listed, not opened for metrics
for lab, path, cases in [("V8_COMP_01 Track A / Track B outputs (P03 91/263/EEC; P04 874/2004)", "COMPARATIVE_PILOTS/V8_COMP_01_2026-10-04/TRACK_A ; TRACK_B ; CROSS_MODEL_REPLICATION", "CASE-31991L0263; CASE-32004R0874"),
                         ("RGAM V8_ACTIVE GDPR_V8 empirical pilot", "RGAM/V8_ACTIVE/04_EMPIRICAL_PILOT/GDPR_V8", "CASE-32016R0679")]:
    cv = add_cv(
        canonical_case_id=cases.split(";")[0].strip(), version_label=lab, is_canonical_version="NO", instrument_title="(V8-stage analytical output on instrument(s): %s)" % cases, jurisdiction="EU", year="", celex_or_identifier="",
        source_family="PROHIBITED_V8", source_pilot_dataset=lab, source_directory=path, extraction_version="V8 / V8+eight-operations output", corpus_scope="UNKNOWN",
        scope_note="Not opened for metrics (non-circularity).", codebook_ref="V8", human_validation_status="n/a", known_limitations="Prohibited as selection input.", comparability_stratum="NONE", **metrics_dict())
    DISP[cv] = ("OTHER_DOCUMENTED_EXCLUSION", "Prohibited material under NON_CIRCULARITY_RULES: V8-stage output. Listed so that nothing disappears silently; no metric taken; no classification made.")
    for m in METRICS:
        add_prov(cv, rows[-1]["canonical_case_id"], m, None, "NOT_RECORDED", path.split(" ; ")[0], "-", "prohibited material; not opened", "-")

# Rotem-only acts (external dataset rows, never extracted by PRJ-David pilots)
studied_keys = {("76", "889"), ("86", "361"), ("87", "95"), ("89", "336"), ("91", "263"), ("92", "44"), ("2004", "48"), ("874", "2004"), ("1781", "2006"), ("2006", "115")}
n_rot = 0
for r in M["Rotem_CDI_rows"]:
    code = r["code"]
    nums = tuple(re.findall(r"\d+", code)[:2])
    nums_swapped = (nums[1], nums[0]) if len(nums) == 2 else ()
    if (len(nums) == 2 and (nums in studied_keys or nums_swapped in studied_keys)) or code in ("EC 2004/48", "2006/115/EC"):
        continue
    n_rot += 1
    label = (r["title"] or "(untitled row)")[:110]
    cv = add_cv(
        canonical_case_id=f"ROT-{n_rot:03d}", version_label="Rotem_CDI_row_only", is_canonical_version="YES", instrument_title=label, jurisdiction="EU / unspecified", year=r["year"], celex_or_identifier=code or "none recorded",
        source_family="ROTEM_ONLY", source_pilot_dataset="Rotem dataset 'Coding Digital Intermediaries' (act-level free text)", source_directory=f"{PL}/PILOT_01/00_SOURCES",
        extraction_version="Rotem workbook row; Assessed=%s; sector=%s" % (r["assessed"] or "n/a", r["sector"] or "n/a"), corpus_scope="UNKNOWN",
        scope_note="Act-level row; 'Who are the intermediaries?' is free text: %s" % (r["intermediaries"][:90] or "(blank)"), codebook_ref="Rotem revised codebook", human_validation_status="Expert-coded (external).",
        known_limitations="Never extracted or studied in a PRJ-David pilot; no relations, regulators or targets recorded; some rows are communications/resolutions or untitled.", comparability_stratum="NONE", **metrics_dict())
    DISP[cv] = ("OTHER_DOCUMENTED_EXCLUSION", "Row of Rotem's external act-level dataset that no PRJ-David pilot extracted or studied; free-text intermediaries only, no countable relation records (G1/G3). Listed so it does not disappear silently.")
    for m in METRICS:
        add_prov(cv, f"ROT-{n_rot:03d}", m, None, "NOT_RECORDED", ROT_XLSX, "Coding Digital Intermediaries row", "free-text only; no count defined", "Rotem revised codebook")

# R2.1 note: Taxonomy handled in PoC loop (INSUFFICIENT_SOURCE)

# ----------------------------------------------------------------- finalize master rows with dispositions
for r in rows:
    r["disposition"], r["disposition_reason"] = DISP[r["cv_id"]]
    r["metric_provenance_ref"] = "CASE_SOURCE_PROVENANCE.csv rows cv_id=" + r["cv_id"]

# ============================================================== COMPARABILITY MATRIX
CLS = {1: "C1_DIRECTLY_COMPARABLE", 2: "C2_HARMONIZABLE_FROM_EXISTING_DATA", 3: "C3_PARTIALLY_COMPARABLE", 4: "C4_NOT_COMPARABLE", 5: "C5_PROVENANCE_INSUFFICIENT"}
R3NOTE = " Holds WITHIN stratum S1 (one pipeline, one codebook, same scope); it does not extend to other pipelines (G4)."
BRIDGE = ("Bridge check on the shared instrument (European Climate Law): R3 SUPPORTED_INTERMEDIATION = 1 (EEA), R2 final = 3 (EEA, Scientific Advisory Board, Energy Union Committee), R2 Stage-4 candidates = 0 positive. "
          "The divergence is documented as a rule difference, not noise: R2 codebook v1.2 (2026-09-08, decisions 1-2) reversed the v1.1 exclusion of comitology committees and advisory/expert input as intermediaries, whereas the R3 clean-room gate (2026-09-21) rejected the same categories in the Climate Law (BND-004 Advisory Board and BND-006 Energy Union Committee, failed C1). "
          "It is a difference in the application of the gate, not in counting, so deterministic recount cannot reconcile it.")


def classify(row):
    f, cv = row["source_family"], row["cv_id"]
    out = {}
    stratum = row["comparability_stratum"]
    for m in METRICS:
        val = row[m]
        # default
        c, why = 4, ""
        if f == "R3":
            c = {"actors": 1, "regulators": 2, "intermediaries": 1, "targets": 2, "relations": 1, "intermediation_relations": 1}[m]
            why = {
                "actors": "Native LAW x ACTOR register of the whole instrument under one actor rule (specific entities + actor classes) for all five laws." + R3NOTE,
                "regulators": "Not a published per-law count; deterministic recount of distinct R_actor_id over the adjudicated relations, one rule for all laws (harmonization register). Not a ranking metric." + R3NOTE,
                "intermediaries": "Native LAW x INTERMEDIARY units under the same three-condition gate for all five laws." + R3NOTE,
                "targets": "Not a published per-law count; deterministic recount of distinct T_actor_id over all adjudicated relations, one rule for all laws; alternative (supported relations only) stored in harmonization register; the ordering of ranked cases is unaffected (verified at ranking)." + R3NOTE,
                "relations": "Native census: all 56 candidate relations adjudicated (SUPPORTED_INTERMEDIATION, DIRECT_R_T, LEGAL_RELATION_NON_RIT, UNCERTAIN), none silently added or deleted." + R3NOTE,
                "intermediation_relations": "Native adjudicated SUPPORTED_INTERMEDIATION relations (C1=C2=C3=YES) under the clean-room gate; cross-checked against the workbook." + R3NOTE,
            }[m]
        elif f == "R2" and row["comparability_stratum"] == "S2_R2_RESEARCHER_REVIEW":
            c = 3
            base = {
                "actors": "R2 'actors' are actors holding an R/I/T role in the retained relation records (actor-in-role map), not the whole-act actor register used in R3; recount to 'actors in >=1 relation' is possible (H-R2-ACT) but the R2 relation set is curated, not a census, so it undercounts relative to R3.",
                "regulators": "Role records in a curated relation set; different actor-definition rule from R3.",
                "intermediaries": "Distinct I-role actors include comitology committees, expert groups, customs authorities and submitters of concerns that the R3 gate rejected in analogous situations (BND-004, BND-006, BND-007); application of the intermediary rule diverges. " + BRIDGE,
                "targets": "T-role records with open classes ('operators', 'traders', 'importers', 'authorised declarants') normalized under the R2 actor log; R2 relation set is curated, so target coverage differs from R3's census of relations.",
                "relations": "R2 relation records (direct, intermediated, uncertain, not supported) are a curated set from a primary reader, not a census of all regulatory relations; R3 reports a census (56 relations). Unit also differs (provision-anchored record with actor arrays vs one relation per R-I-T triple).",
                "intermediation_relations": "Same five-condition wording as the R3 gate, but application diverges. " + BRIDGE + " Unit also differs (record with actor arrays vs one relation per triple; recount in H-R2-INT-TRIPLE changes the values). Provenance caveat: final package reconstructed from a damaged working file (06_PROVENANCE.csv), one issue unresolved (case_02-U07).",
            }[m]
            why = base
            if row["is_canonical_version"] == "NO":
                why += " This row is a non-canonical version of the Climate Law (G5); canonical counts are the R3 version."
        elif f == "R2":
            c = 4
            why = "Superseded intermediate/export version of the R2 pipeline; counts changed across versions (e.g., CBAM intermediated: 5 in v1.0, 7 in v1.1, 3 in R2 reading, 5 in final), documenting version instability. Not canonical (G5)."
            if "stage4" in row["version_label"]:
                why = "Pre-human-gate candidate adjudication; candidates are provision-anchored screening units, not relations; human gate not executed."
            if val is None:
                c, why = 5, why + " Metric not recorded in this version."
        elif f == "POC":
            if row["is_canonical_version"] == "YES" and row["extraction_version"].startswith("PoC v4 screening"):
                c, why = 5, "No relational extraction exists for this act (screening hits and a source audit only)."
            elif val is None:
                c, why = 5, "Metric not recorded for this version/act."
            else:
                c = 4
                why = {
                    "actors": "Actor ids are shared across acts; recount covers only actors in the few positive rows from a purposive sample.",
                    "regulators": "Counts only the regulators in the stored positive rows of a purposive sample.",
                    "intermediaries": "Counts only intermediaries in the stored positive rows of a purposive sample.",
                    "targets": "Counts only targets in the stored positive rows of a purposive sample.",
                    "relations": "Only positive relations were stored; the sample is a purposive subset of lexical hits (LIMITED_PROVISIONS); not a census.",
                    "intermediation_relations": "Positive rows from a purposive sample of lexical-hit provisions; the absence of other rows is not absence of intermediation; cannot compete with full-instrument extractions (G2).",
                }[m]
        elif f == "PILOT":
            if val is None:
                c, why = 5, "Metric not recorded (or role fields too incomplete to recount without interpretation)."
            else:
                c = 4
                why = {
                    "actors": "Distinct names over 2-6 purposively chosen provisions; names not entity-resolved; not an actor register of the act (LIMITED_PROVISIONS).",
                    "intermediaries": "Distinct actor_b names with derived intermediary status over a handful of provisions chosen because Rotem had coded intermediaries for the act; relational-position rule differs from R3 gate.",
                    "relations": "Primitive actor-action-recipient edges over the selected provisions only (edge unit, not R-I-T relation unit).",
                    "intermediation_relations": "Edges flagged derived R-I-T candidate by model passes before human adjudication; not adjudicated positives; provisions selected purposively (G2/G3).",
                    "regulators": "n/a", "targets": "n/a",
                }[m]
                if row["is_canonical_version"] == "NO":
                    why += " Earlier pilot version; superseded."
        elif f == "R4":
            if m == "actors":
                c, why = 4, "Provisional textual actor candidates (any actor mentioned, with merge ambiguity), not an R/I/T actor register; different actor-definition rule from R3."
            elif m == "relations":
                c, why = 5, "No relation table exists: R4 structural records are provision x actor x action units, not relations."
            else:
                c, why = 5, "Metric never produced: R4 states regulator/intermediary/target and mechanism coding 'not started'."
        elif f == "GDPR_PILOT":
            if val is None:
                c, why = 4, "R-I-T roles / intermediation not coded in the RGAM/V6 ontology; a recount would require interpreting relation types, which the harmonization rule forbids."
            elif m == "actors":
                c, why = 4, "String-level union of origin/counterpart names under a different ontology (positions, devices); recitals not reviewed."
            else:
                c, why = 4, "'Qualified relations' of all RGAM relation types (information/reporting, authority/control, ...) on paragraph units; different relation definition and text baseline from R3; machine-provisional single evaluator."
        elif f == "ROTEM_LIST":
            if val is None:
                c, why = 5, "Not coded as a count in the Rotem sheets."
            else:
                c, why = 4, "Rows list intermediary labels/arrangements per act under Rotem's own digital-intermediary definition (includes process-based arrangements); not R-I-T relations; scope undocumented."
        elif f == "ROTEM_PACK":
            c, why = 5, "Provision pack for a codebook comparison; no case-level metric exists."
        elif f in ("NOT_STARTED", "ROTEM_ONLY"):
            c, why = 5, "No extraction exists for this case-version (free text or not started)."
        elif f == "PROHIBITED_V8":
            continue
        out[m] = (CLS[c], why)
    return out


comp_id = 0
for r in rows:
    if r["source_family"] == "PROHIBITED_V8":
        continue
    res = classify(r)
    for m in METRICS:
        comp_id += 1
        c, why = res[m]
        eligible_scope = r["corpus_scope"] == "FULL_INSTRUMENT"
        rank_ok = (c[:2] in ("C1", "C2")) and eligible_scope and r["comparability_stratum"] == "S1_R3_CLEANROOM_FROZEN" and r["is_canonical_version"] == "YES"
        cm.append(dict(row_id=f"CM{comp_id:04d}", cv_id=r["cv_id"], canonical_case_id=r["canonical_case_id"], version_label=r["version_label"], metric=m,
                       value_recorded="" if r[m] is None else r[m], comparability_class=c, corpus_scope=r["corpus_scope"], comparability_stratum=r["comparability_stratum"],
                       rank_eligible_for_metric="YES" if rank_ok else "NO", explanation=why if not c.startswith("C1") else why,
                       harmonized_value_ref="see HARMONIZATION_REGISTER" if (r["source_family"] in ("R2", "R3", "PILOT") and r["is_canonical_version"] == "YES" and r["comparability_stratum"] != "NONE_SUPERSEDED") else ""))

# ============================================================== HARMONIZATION REGISTER
hid = 0


def add_h(cv, case, metric, original, harmonized, rule, source, status, note):
    global hid
    hid += 1
    hr.append(dict(h_id=f"H{hid:03d}", cv_id=cv, canonical_case_id=case, metric=metric, original_value_preserved=original, harmonized_value=harmonized,
                   counting_rule=rule, source_records=source, deterministic="YES", legal_interpretation_used="NO", status=status, notes=note))


for celex, cv in r3_cvs.items():
    v = M["R3"][celex]
    add_h(cv, CASEID(celex), "targets", v["targets_distinct_all_relations"], v["targets_distinct_supported"],
          "HR3-TGT-ALT: distinct T_actor_id restricted to SUPPORTED_INTERMEDIATION relations", R3_REL, "COMPUTED_NOT_USED", "Alternative target definition; stored for sensitivity; ranking order unchanged.")
    add_h(cv, CASEID(celex), "actors", v["actors_native"], v["actors_in_any_relation"],
          "HR3-ACT-REL: distinct actor ids appearing as R, I or T in any adjudicated relation (aligns with the R2 actor-in-role rule)", R3_REL, "COMPUTED_NOT_USED", "Alternative actor definition aligned to R2 for the bridge; not used for ranking inside S1 (native LAW x ACTOR used).")
    add_h(cv, CASEID(celex), "actors", v["actors_native"], v["actors_in_supported_relations"],
          "HR3-ACT-INT: distinct actor ids appearing as R, I or T in SUPPORTED_INTERMEDIATION relations", R3_REL, "COMPUTED_NOT_USED", "Reference for the R2-to-R3 alignment of actors in intermediation relations.")
    add_h(cv, CASEID(celex), "intermediation_relations", v["intermediation_native"], v["rit_triples_supported"],
          "HR3-INT-TRIPLE: distinct (R,I,T) actor-id triples among SUPPORTED_INTERMEDIATION relations", R3_REL, "COMPUTED_NOT_USED", "Equals native count (R3 already uses one relation per triple).")
for case, celex in r2_cases.items():
    v = M["R2_final_v2"][case]
    cv = r2_final[celex]
    add_h(cv, CASEID(celex), "intermediation_relations", v["intermediation_native"], v["rit_triples_intermediated_expanded"],
          "HR2-INT-TRIPLE: expand each intermediated relation record's R x I x T actor arrays into distinct (R,I,T) label triples (label = text before the role annotation)", f"{R2_EV}; {R2_AM}", "COMPUTED_NOT_USED",
          "Aligns the unit with R3 (one relation per triple). It changes values but does not reconcile adjudication standards (bridge check fails), so it is not used to pool strata.")
    add_h(cv, CASEID(celex), "actors", v["actors_native"], v["actors_in_intermediated_relations_parsed"],
          "HR2-ACT-INT: distinct actor labels appearing as R, I or T in intermediated relation records", R2_EV, "COMPUTED_NOT_USED", "Counterpart of HR3-ACT-INT.")
    add_h(cv, CASEID(celex), "actors", v["actors_native"], v["distinct_actor_labels_in_relation_fields"],
          "HR2-ACT-REL: distinct actor labels appearing as R, I or T in any retained relation record (counterpart of HR3-ACT-REL)", R2_EV, "COMPUTED_NOT_USED", "Label-level; no new normalization applied beyond the role-annotation strip.")
    add_h(cv, CASEID(celex), "relations", v["relations_native"], "", "none possible: R2 retained set is a curated subset, R3 is a census", R2_EV, "NOT_HARMONIZABLE",
          "Harmonizing to a census would require reading the law again (new interpretation); classified C3 instead.")
    add_h(cv, CASEID(celex), "intermediation_relations", v["intermediation_native"], "", "none possible: reconciling application of the R-I-T gate (e.g., committees/advisory bodies as I) needs substantive reinterpretation",
          f"{R2_EV}; {R3_BND}", "NOT_HARMONIZABLE", "Climate Law bridge: R3=1, R2=3, Stage-4 RA=0 positive.")
add_h(r3_cvs["32021R1119"], "CASE-32021R1119", "intermediation_relations", M["R3"]["32021R1119"]["intermediation_native"], "",
      "H-R2-PROXY (considered and rejected): drop R2 relations whose I is a comitology committee or advisory/consulted-expert body, to mimic the R3 boundary rulings BND-004/BND-006",
      f"{R2_EV}; {R3_BND}; {R2_CHANGELOG}", "NOT_HARMONIZABLE",
      "Not deterministic: R3 rejected those two Climate Law relations because they identified no regulatory target (failed C1), whereas R2 records identify targets for the analogous CBAM/EUDR committee and expert relations (e.g., authorised CBAM declarants; operators and traders). Whether R3 would reject them requires re-adjudication of the provisions (new legal interpretation), and the proxy could only be checked on a single shared instrument. Therefore no proxy count was computed.")
# Bridge row
add_h(r3_cvs["32021R1119"], "CASE-32021R1119", "intermediation_relations", M["R3"]["32021R1119"]["intermediation_native"], f"R2_final={M['R2_final_v2']['case_01']['intermediation_native']}; R2_triples={M['R2_final_v2']['case_01']['rit_triples_intermediated_expanded']}; Stage4_RA_positive=0",
      "BRIDGE: same instrument counted under three versions", f"{R3_REL}; {R2_EV}; {R2_RA}", "COMPUTED_AND_USED", "Used only for the comparability audit (G4). R3 vs R2 differ by 2 on the primary metric; R3 boundary cases BND-004 and BND-006 correspond to two of the three R2 relations.")
# PILOT_03 recount register
for celex in pilot_acts:
    p = M["PILOT_03"][celex]
    cv = [r["cv_id"] for r in rows if r["canonical_case_id"] == CASEID(celex) and r["version_label"].startswith("PILOT_03")][0]
    add_h(cv, CASEID(celex), "intermediation_relations", p["derived_rit_candidates_A"], p["derived_rit_candidates_B"],
          "HP3-MODELB: derived_rit_candidate=='YES' recounted in Model B pass", P3_B, "COMPUTED_NOT_USED", "Shows pass-to-pass count; both are pre-adjudication candidate counts; scope remains LIMITED_PROVISIONS so class stays C4.")
add_h("", "R4/GDPR_PILOT/others", "all", "", "", "no deterministic recount exists: metrics never produced under the R-I-T gate or produced under different ontology", "-", "NOT_HARMONIZABLE", "See classification reasons.")

# ----------------------------------------------------------------- write CSVs
def write_csv(path, fieldnames, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        for d in data:
            w.writerow({k: ("" if d.get(k) is None else d.get(k)) for k in fieldnames})


master_cols = ["cv_id", "canonical_case_id", "version_label", "is_canonical_version", "instrument_title", "jurisdiction", "year", "celex_or_identifier", "source_family", "source_pilot_dataset",
               "source_directory", "extraction_version", "corpus_scope", "scope_note", "actors", "regulators", "intermediaries", "targets", "relations", "intermediation_relations",
               "metric_provenance_ref", "codebook_ref", "human_validation_status", "known_limitations", "comparability_stratum", "disposition", "disposition_reason"]
write_csv(os.path.join(NT, "01_CASE_UNIVERSE", "CASE_UNIVERSE_MASTER.csv"), master_cols, rows)
write_csv(os.path.join(NT, "01_CASE_UNIVERSE", "CASE_SOURCE_PROVENANCE.csv"),
          ["cv_id", "canonical_case_id", "metric", "value_recorded", "value_type", "source_files", "source_file_sha256", "source_locator", "counting_rule", "definition_or_codebook_ref", "notes"], prov)
write_csv(os.path.join(NT, "02_COMPARABILITY", "CASE_METRIC_COMPARABILITY.csv"),
          ["row_id", "cv_id", "canonical_case_id", "version_label", "metric", "value_recorded", "comparability_class", "corpus_scope", "comparability_stratum", "rank_eligible_for_metric", "explanation", "harmonized_value_ref"], cm)
write_csv(os.path.join(NT, "02_COMPARABILITY", "HARMONIZATION_REGISTER.csv"),
          ["h_id", "cv_id", "canonical_case_id", "metric", "original_value_preserved", "harmonized_value", "counting_rule", "source_records", "deterministic", "legal_interpretation_used", "status", "notes"], hr)

# summary print
import collections
print("case-versions:", len(rows), "provenance rows:", len(prov), "comparability rows:", len(cm), "harmonization rows:", len(hr))
print("dispositions:", dict(collections.Counter(r["disposition"] for r in rows)))
print("distinct canonical cases:", len({r["canonical_case_id"] for r in rows}))
print("by family:", dict(collections.Counter(r["source_family"] for r in rows)))
print("classes:", dict(collections.Counter(c["comparability_class"] for c in cm)))
