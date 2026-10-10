# MECHANICAL independent validation of the 19 delivered CSV tables against the frozen data dictionary (integrity rules 1-10 and vocabularies).
import csv, re, json, os, sys, collections

D = "G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/12_RGAM_CASE_EXECUTION/RGAM_AI_AI_ACT/"
T = "G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_AI_AI_ACT/OUTPUT_TEMPLATES/"
NAMES = ["W_DECLARATION", "SOURCE_UNIT_INVENTORY", "UNIT_SCREENING", "INSTITUTIONAL_STATEMENTS", "NORMATIVE_ASSIGNMENTS", "POSITIONS_AND_DEVICES",
         "QUALIFIED_RELATIONS", "EXTERNAL_REFERENCES", "SUBCONFIGURATIONS", "ARCHITECTURE_CANDIDATES", "PROPERTY_REGISTER", "CLOSURE_REGISTER",
         "PROVENANCE_LINKS", "UNCERTAINTY_LOG", "HUMAN_REVIEW_QUEUE", "TRACE_DEMONSTRATIONS", "INSTRUMENT_LEVEL_SUMMARY", "PROTOCOL_DEVIATION_LOG", "RUN_METADATA"]
res = collections.OrderedDict()
fails = collections.defaultdict(list)


def rd(n):
    return list(csv.DictReader(open(D + n + ".csv", encoding="utf-8-sig")))


def raw(n):
    return open(D + n + ".csv", "rb").read()


tab = {n: rd(n) for n in NAMES}
# headers identical to templates and BOM
for n in NAMES:
    th = open(T + n + ".csv", "rb").read()
    dh = raw(n)
    hdr_t = th.split(b"\n")[0].strip()
    hdr_d = dh.split(b"\n")[0].strip()
    if hdr_t != hdr_d:
        fails["HEADERS"].append(n)
    if not dh.startswith(b"\xef\xbb\xbf"):
        fails["BOM"].append(n)
units = {r["unit_id"] for r in tab["SOURCE_UNIT_INVENTORY"]}
unitrow = {r["unit_id"]: r for r in tab["SOURCE_UNIT_INVENTORY"]}
src = {x["unit_id"]: x for x in json.load(open(D + "_work/units.json", encoding="utf-8"))}


def ids(s):
    return [x for x in (s or "").split(";") if x]


# uniqueness
for n, c in (("SOURCE_UNIT_INVENTORY", "unit_id"), ("INSTITUTIONAL_STATEMENTS", "st_id"), ("NORMATIVE_ASSIGNMENTS", "na_id"), ("POSITIONS_AND_DEVICES", "pd_id"),
             ("QUALIFIED_RELATIONS", "qr_id"), ("EXTERNAL_REFERENCES", "ext_id"), ("SUBCONFIGURATIONS", "sc_id"), ("ARCHITECTURE_CANDIDATES", "arch_id"),
             ("PROPERTY_REGISTER", "prop_id"), ("CLOSURE_REGISTER", "closure_id"), ("PROVENANCE_LINKS", "link_id"), ("UNCERTAINTY_LOG", "unc_id"),
             ("HUMAN_REVIEW_QUEUE", "hq_id"), ("TRACE_DEMONSTRATIONS", "trace_id"), ("PROTOCOL_DEVIATION_LOG", "dev_id")):
    v = [r[c] for r in tab[n]]
    if len(v) != len(set(v)):
        fails["UNIQUE_IDS"].append(n)
# rule 1
allids = {}
for n in NAMES:
    for r in tab[n]:
        for k, v in r.items():
            if k.endswith("unit_ids") or k in ("unit_id", "instance_source_unit_ids", "i1_scope_units", "units_spanned"):
                for u in ids(v):
                    if u.startswith("RGAM_AI_AI_ACT.") and u not in units:
                        fails["R1"].append((n, k, u))
isum = tab["INSTRUMENT_LEVEL_SUMMARY"][0]
if int(isum["units_screened"]) != int(isum["units_total"]) or int(isum["units_total"]) != len(units) or len(tab["UNIT_SCREENING"]) != len(units):
    fails["R1"].append("units_screened != units_total")
if [r["unit_id"] for r in tab["UNIT_SCREENING"]] != [r["unit_id"] for r in tab["SOURCE_UNIT_INVENTORY"]]:
    fails["R1"].append("screening order differs from source order")
# rule 2
ST = {r["st_id"]: r for r in tab["INSTITUTIONAL_STATEMENTS"]}
for r in tab["INSTITUTIONAL_STATEMENTS"]:
    if not ids(r["supporting_unit_ids"]):
        fails["R2"].append(r["st_id"])
    if r["recital_only"] == "Y" and r["derived_record_ids"]:
        fails["R2"].append(("recital_only with derived", r["st_id"]))
for n, c in (("NORMATIVE_ASSIGNMENTS", "na_id"), ("QUALIFIED_RELATIONS", "qr_id")):
    for r in tab[n]:
        s = ids(r["statement_ids"])
        if not s or any(x not in ST for x in s):
            fails["R2"].append((n, r[c]))
derived_from = collections.defaultdict(set)
for r in tab["INSTITUTIONAL_STATEMENTS"]:
    for d in ids(r["derived_record_ids"]):
        derived_from[d].add(r["st_id"])
for r in tab["POSITIONS_AND_DEVICES"]:
    if r["pd_id"] not in derived_from:
        fails["R2"].append(("PD without ST", r["pd_id"]))
for r in tab["EXTERNAL_REFERENCES"]:
    if r["ext_id"] not in derived_from:
        fails["R2"].append(("EXT without ST", r["ext_id"]))
# rule 3
PD = {r["pd_id"] for r in tab["POSITIONS_AND_DEVICES"]}
QR = {r["qr_id"]: r for r in tab["QUALIFIED_RELATIONS"]}
EXT = {r["ext_id"] for r in tab["EXTERNAL_REFERENCES"]}
NA = {r["na_id"] for r in tab["NORMATIVE_ASSIGNMENTS"]}
SC = {r["sc_id"] for r in tab["SUBCONFIGURATIONS"]}
UNC = {r["unc_id"] for r in tab["UNCERTAINTY_LOG"]}
HQ = {r["hq_id"] for r in tab["HUMAN_REVIEW_QUEUE"]}
CL = {r["closure_id"] for r in tab["CLOSURE_REGISTER"]}
allrec = set(ST) | PD | set(QR) | EXT | NA | SC | UNC | HQ | CL | {r["arch_id"] for r in tab["ARCHITECTURE_CANDIDATES"]} | {r["prop_id"] for r in tab["PROPERTY_REGISTER"]}
for n in NAMES:
    for r in tab[n]:
        for k, v in r.items():
            if k.endswith("_pd_id") or k.endswith("_pd_ids"):
                for x in ids(v):
                    if x not in PD:
                        fails["R3"].append((n, k, x))
            if k in ("hq_ids",):
                for x in ids(v):
                    if x not in HQ:
                        fails["R3"].append((n, k, x))
            if k in ("uncertainty_ids",):
                for x in ids(v):
                    if x not in UNC:
                        fails["R3"].append((n, k, x))
            if k in ("external_ref_ids", "unresolved_ext_ids", "i4_external_dependencies"):
                for x in ids(v):
                    if x not in EXT:
                        fails["R3"].append((n, k, x))
            if k in ("member_qr_ids", "i2_qr_ids", "accountable_via_qr_ids"):
                for x in ids(v):
                    if x not in QR:
                        fails["R3"].append((n, k, x))
            if k in ("member_sc_ids", "overlap_sc_ids"):
                for x in ids(v):
                    if x not in SC:
                        fails["R3"].append((n, k, x))
            if k == "member_na_ids":
                for x in ids(v):
                    if x not in NA:
                        fails["R3"].append((n, k, x))
for r in tab["QUALIFIED_RELATIONS"]:
    for x in ids(r["accountable_via_qr_ids"]):
        if QR[x]["relation_type"] != "accountability":
            fails["R3"].append(("accountable_via not accountability", r["qr_id"], x))
# rule 4
MODS = {"obligation", "obligation_promotional", "prohibition", "permission", "competence", "entitlement", "definition", "declaratory"}
for r in tab["QUALIFIED_RELATIONS"]:
    if not r["origin_pd_id"] or not r["counterpart_pd_id"] or r["modality"] == "prohibition" or r["epistemic_status"] == "material_establishment_evidenced":
        fails["R4"].append(r["qr_id"])
    if r["modality"] not in MODS:
        fails["VOCAB"].append((r["qr_id"], "modality"))
# rule 5
prov = collections.Counter(r["record_id"] for r in tab["PROVENANCE_LINKS"])
for n, c in (("NORMATIVE_ASSIGNMENTS", "na_id"), ("QUALIFIED_RELATIONS", "qr_id"), ("SUBCONFIGURATIONS", "sc_id"), ("ARCHITECTURE_CANDIDATES", "arch_id"), ("PROPERTY_REGISTER", "prop_id")):
    for r in tab[n]:
        if prov[r[c]] == 0:
            fails["R5"].append((n, r[c]))
for n, c in (("NORMATIVE_ASSIGNMENTS", "na_id"), ("QUALIFIED_RELATIONS", "qr_id")):
    for r in tab[n]:
        if r["derivation"] == "derived":
            if not r["derivation_rule"] or (len(ids(r["supporting_unit_ids"])) < 2 and "cross-ref" not in r["derivation_rule"].lower()):
                fails["R5"].append(("derived", r[c]))
        elif r["derivation"] != "direct":
            fails["R5"].append(("derivation", r[c]))
# mirror: record unit lists vs provenance rows (direct records)
linkset = collections.defaultdict(set)
for r in tab["PROVENANCE_LINKS"]:
    linkset[r["record_id"]].add(r["unit_id"])
for n, c in (("NORMATIVE_ASSIGNMENTS", "na_id"), ("QUALIFIED_RELATIONS", "qr_id"), ("EXTERNAL_REFERENCES", "ext_id"), ("POSITIONS_AND_DEVICES", "pd_id")):
    for r in tab[n]:
        if set(ids(r["supporting_unit_ids"])) != linkset[r[c]]:
            fails["R5_MIRROR"].append((n, r[c]))
# rule 6
for r in tab["ARCHITECTURE_CANDIDATES"]:
    if r["outcome"] in ("INTEGRATED", "OVERLAPPING_OR_PARTIALLY_INTEGRATED") and not ids(r["hq_ids"]):
        fails["R6"].append(r["arch_id"])
    if r["outcome"] == "INTEGRATED" and not all(r[c] == "SATISFIED" for c in ("i1_status", "i2_status", "i3_status", "i4_status")):
        fails["R6"].append((r["arch_id"], "not all SATISFIED"))
    if r["outcome"] not in ("INTEGRATED", "DISTINGUISHABLE", "OVERLAPPING_OR_PARTIALLY_INTEGRATED", "INDETERMINATE"):
        fails["VOCAB"].append(r["arch_id"])
    if r["anticircularity_sequence_followed"] != "Y":
        fails["R6"].append((r["arch_id"], "anticircularity"))
# rule 7
CLr = {r["closure_id"]: r for r in tab["CLOSURE_REGISTER"]}
for r in tab["PROPERTY_REGISTER"]:
    if r["closure_dependency"] == "Y":
        if r["closure_ref"] not in CLr:
            fails["R7"].append(r["prop_id"])
        elif CLr[r["closure_ref"]]["result"] == "UNDETERMINED" and r["status"] != "undetermined":
            fails["R7"].append((r["prop_id"], "undetermined"))
if not any(r["record_kind"] == "COVERAGE" for r in tab["CLOSURE_REGISTER"]):
    fails["R7"].append("no COVERAGE row")
# rule 8
for r in tab["EXTERNAL_REFERENCES"]:
    if r["source_verification_status"] != "not_checked" or r["boundary_status"] != "outside_corpus_not_expanded":
        fails["R8"].append(r["ext_id"])
# rule 9
for r in tab["HUMAN_REVIEW_QUEUE"]:
    if any(r[c] for c in ("human_decision", "human_rationale", "decided_by", "decision_date")):
        fails["R9"].append(r["hq_id"])
# rule 10
norm = lambda s: re.sub(r"\s+", " ", s).strip()
for r in tab["TRACE_DEMONSTRATIONS"]:
    ch = r["vertical_chain"]
    for tid in re.findall(r"\b(?:QR|NA|ST|PD|SC|ARCH)-\d+\b", ch):
        if tid not in allrec:
            fails["R10"].append((r["trace_id"], tid))
    for u in re.findall(r"RGAM_AI_AI_ACT\.[A-Za-z0-9.\u2018()]+", ch):
        u = u.rstrip(".;")
        if u not in units:
            fails["R10"].append((r["trace_id"], u))
    if r["chain_complete"] != "Y":
        fails["R10"].append((r["trace_id"], "chain_complete"))
# verbatim spans
def span_ok(span, unit_ids):
    for u in unit_ids:
        if span in norm(src[u]["text"]) and u in units:
            return True
    return False
for n, c, k in (("INSTITUTIONAL_STATEMENTS", "st_id", "supporting_unit_ids"), ("NORMATIVE_ASSIGNMENTS", "na_id", "supporting_unit_ids"), ("QUALIFIED_RELATIONS", "qr_id", "supporting_unit_ids"),
                ("POSITIONS_AND_DEVICES", "pd_id", "supporting_unit_ids")):
    for r in tab[n]:
        sp = r["evidence_span"]
        if len(sp) > 400 or not sp:
            fails["SPAN_LEN"].append((n, r[c]))
        us = ids(r[k])
        if n != "INSTITUTIONAL_STATEMENTS" and not span_ok(sp, us):
            # a record may carry the statement span anchored in a statement unit
            sts = ids(r.get("statement_ids", ""))
            alt = [u for s in sts for u in ids(ST[s]["supporting_unit_ids"])] if sts else []
            if not span_ok(sp, alt):
                fails["SPAN_VERBATIM"].append((n, r[c]))
        if n == "INSTITUTIONAL_STATEMENTS" and not span_ok(sp, us):
            fails["SPAN_VERBATIM"].append((n, r[c]))
# vocab checks
EP = {"conceptually_projected", "documented", "legal_constitution_evidenced", "material_establishment_evidenced", "exercise_evidenced"}
LS = {"in_force", "not_yet_applicable", "suspended", "expired_or_repealed", "conditional_on_further_act"}
RT = {"authority_control", "delegation_authorization", "oversight_supervision", "accountability", "information_reporting", "verification_assurance", "review_adjudication", "representation_participation", "contractual_exchange", "beneficiary_protective"}
FN = {"rule_making_standard_setting", "implementation", "interpretation_translation", "information_provision", "monitoring", "verification_assurance", "enforcement", "adjudication_dispute_resolution", "remediation",
      "representation_participation*", "authorization_designation*", "cooperation_coordination*", "FUNCTION_VOCABULARY_UNRESOLVED"}
for n in ("NORMATIVE_ASSIGNMENTS", "QUALIFIED_RELATIONS"):
    for r in tab[n]:
        if r["epistemic_status"] not in EP or r["legal_status_of_norm"] not in LS or r["function"] not in FN:
            fails["VOCAB"].append((n, list(r.values())[0]))
for r in tab["QUALIFIED_RELATIONS"]:
    if r["relation_type"] not in RT or r["accountability_class"] not in ("NONE", "INFO", "ANSWERABILITY", "ACCOUNTABILITY"):
        fails["VOCAB"].append(r["qr_id"])
# human review / no scores: scan for numeric-index words in analytic columns is not performed; no table defines a score column
res["tables"] = {n: len(tab[n]) for n in NAMES}
res["fails"] = {k: v for k, v in fails.items()}
print(json.dumps(res["tables"]))
print("FAILS:", json.dumps({k: (len(v), v[:5]) for k, v in fails.items()}, default=str))
json.dump({"tables": res["tables"], "fails": {k: len(v) for k, v in fails.items()}}, open(D + "_work/validate_result.json", "w"), indent=1)
