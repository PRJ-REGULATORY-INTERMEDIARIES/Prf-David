# MECHANICAL: writes W_DECLARATION.json and INSTRUMENT_LEVEL_SUMMARY.json from executor-stated texts and counts computed from the built tables.
import csv, json, collections, hashlib, re

W = "G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/12_RGAM_CASE_EXECUTION/RGAM_AI_AI_ACT/_work/"
B = W + "build/"
SRC = "G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_AI_AI_ACT/LEGAL_SOURCE/32024R1689_official_en.xhtml"


def rd(n):
    return list(csv.DictReader(open(B + n + ".csv", encoding="utf-8-sig")))


meta = json.load(open("G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_AI_AI_ACT/CASE_METADATA.json", encoding="utf-8"))
sha = hashlib.sha256(open(SRC, "rb").read()).hexdigest()
inv = rd("SOURCE_UNIT_INVENTORY")
arts = set(); anx = set(); rec = 0
for r in inv:
    u = r["unit_id"].split(".", 1)[1]
    m = re.match(r"A(\d+)\.", u)
    if m: arts.add(int(m.group(1)))
    m = re.match(r"ANX(\d+)\.", u)
    if m: anx.add(int(m.group(1)))
    if u.startswith("REC"): rec += 1
temporal = ("Reference point 2 August 2026 (general date of application, Art. 113 second paragraph), considered with entry into force on the twentieth day after publication "
            "(Art. 113 first paragraph) and the staged application dates of Art. 113 points (a)-(c): Chapters I and II from 2 February 2025; Chapter III Section 4, Chapter V, Chapter VII, "
            "Chapter XII and Article 78 from 2 August 2025 (Article 101 excepted); Article 6(1) and the corresponding obligations from 2 August 2027. Statuses are asserted for the reference point only")
w = dict(
    case_id="RGAM_AI_AI_ACT",
    instrument_title="REGULATION (EU) 2024/1689 OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL of 13 June 2024 laying down harmonised rules on artificial intelligence and amending Regulations (EC) No 300/2008, (EU) No 167/2013, (EU) No 168/2013, (EU) 2018/858, (EU) 2018/1139 and (EU) 2019/2144 and Directives 2014/90/EU, (EU) 2016/797 and (EU) 2020/1828 (Artificial Intelligence Act)",
    celex=meta["celex"],
    jurisdiction="European Union",
    domain_declaration="Harmonised rules on artificial intelligence (title); purpose stated in Article 1(1): to improve the functioning of the internal market and promote human-centric and trustworthy AI while ensuring a high level of protection of health, safety and fundamental rights against the harmful effects of AI systems in the Union and supporting innovation; Article 1(2) lists the matters laid down",
    instrument_type="Regulation",
    version_type="Original act as published in the Official Journal (OJ L, 2024/1689, 12.7.2024); not consolidated",
    temporal_reference=temporal,
    inclusion_rule="All units of the frozen official source file: title, preamble citations, 180 recitals, enacting formula, 113 articles with chapter and section headings, 13 annexes and the final formal text",
    exclusions="Footnote apparatus (58 notes giving Official Journal citations and procedural notes) is not inventoried as units; inline footnote markers remain in unit text; presentation markup, layout and cross-reference hyperlinks of the XHTML file are not represented; no external text, consolidation or delegated, implementing or guidance act is part of W",
    source_file="G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_AI_AI_ACT/LEGAL_SOURCE/32024R1689_official_en.xhtml",
    source_sha256=sha,
    expected_sha256=meta["source_sha256"],
    hash_match="Y" if sha == meta["source_sha256"] else "N",
    article_count_parsed=len(arts),
    annex_count_parsed=len(anx),
    recital_count_parsed=rec,
    structure_check="MATCH" if (len(arts) == meta["article_count_metadata"] and len(anx) == meta["annex_count_metadata"]) else "DISCREPANCY",
    closure_scope_statement="W can close statements about what the Regulation itself provides, for the declared reference point; it cannot close the content of the 59 external instruments, standards and administrative acts it refers to (not retrieved), the national laws and implementing, delegated and guidance acts that implement it, or any establishment or operation of the institutions it mentions. Absence statements are about the declared corpus only",
    w_is_not_a="W != A",
)
json.dump(w, open(W + "W_DECLARATION.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

NA = rd("NORMATIVE_ASSIGNMENTS"); QR = rd("QUALIFIED_RELATIONS"); PD = rd("POSITIONS_AND_DEVICES"); EXT = rd("EXTERNAL_REFERENCES")
HQ = rd("HUMAN_REVIEW_QUEUE")
cnt = collections.OrderedDict()
for n in ["INSTITUTIONAL_STATEMENTS", "NORMATIVE_ASSIGNMENTS", "POSITIONS_AND_DEVICES", "QUALIFIED_RELATIONS", "EXTERNAL_REFERENCES", "SUBCONFIGURATIONS",
          "ARCHITECTURE_CANDIDATES", "PROPERTY_REGISTER", "CLOSURE_REGISTER", "PROVENANCE_LINKS", "UNCERTAINTY_LOG", "HUMAN_REVIEW_QUEUE",
          "TRACE_DEMONSTRATIONS", "PROTOCOL_DEVIATION_LOG", "RUN_METADATA"]:
    cnt[n] = len(rd(n))
rc = "; ".join(f"{k}={v}" for k, v in cnt.items()) + "; UNIT_SCREENING=%d; SOURCE_UNIT_INVENTORY=%d" % (len(rd("UNIT_SCREENING")), len(inv))
es_q = collections.Counter(r["epistemic_status"] for r in QR); es_n = collections.Counter(r["epistemic_status"] for r in NA); es_p = collections.Counter(r["epistemic_status"] for r in PD)
ls_q = collections.Counter(r["legal_status_of_norm"] for r in QR); ls_n = collections.Counter(r["legal_status_of_norm"] for r in NA)
prof = ("Relations: %d legal_constitution_evidenced, %d documented, 0 material_establishment_evidenced (not permitted for relations), 0 exercise_evidenced; legal status %d in_force, %d conditional_on_further_act. "
        "Assignments: %d legal_constitution_evidenced, %d documented, 0 exercise_evidenced; legal status %d in_force, %d not_yet_applicable/conditional. "
        "Positions and devices: %d documented, %d legal_constitution_evidenced (Board, N1); material_establishment not_assessed for all. "
        "Architecture candidates: 5 INTEGRATED (provisional), 1 OVERLAPPING_OR_PARTIALLY_INTEGRATED, 3 INDETERMINATE, 0 DISTINGUISHABLE; instrument-level profile OVERLAPPING_OR_PARTIALLY_INTEGRATED"
        ) % (es_q["legal_constitution_evidenced"], es_q["documented"], ls_q["in_force"], ls_q["conditional_on_further_act"],
             es_n["legal_constitution_evidenced"], es_n["documented"], ls_n["in_force"], len(NA) - ls_n["in_force"],
             es_p["documented"], es_p["legal_constitution_evidenced"])
s = dict(
    case_id="RGAM_AI_AI_ACT",
    units_total=len(inv),
    units_screened=len(rd("UNIT_SCREENING")),
    record_counts=rc,
    instrument_level_result="OVERLAPPING_OR_PARTIALLY_INTEGRATED",
    highest_level_reached="A",
    status_profile=prof,
    hq_open_count=len(HQ),
    unresolved_ext_count=sum(1 for r in EXT if r["constitutive_dependency"] == "Y"),
    machine_provisional="Y",
    summary_note="Machine-generated and provisional. Candidate architectures were assessed under I1-I4; five candidates are INTEGRATED at provisional level and queued, one instrument-wide candidate is OVERLAPPING_OR_PARTIALLY_INTEGRATED with source-supported overlaps only, and three are INDETERMINATE where the constitution of elements depends on further acts or external references. Counts are descriptors, not significance. No comparison with any other method or case.",
)
json.dump(s, open(W + "INSTRUMENT_LEVEL_SUMMARY.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(prof)
print(rc)
