"""R08 — Parent/child tables, child→parent aggregation, activity-level R×T test, dual-coding comparison.

Inputs : first pass (frozen), blind pass (if present), Rotem L3 baseline rows, ACTOR_CONTEXT_MAP.csv
Outputs: 08_DUAL_CODING/PARENT_INTERMEDIARY_ACT.csv, CHILD_PROVISION_RELATION_EVENT.csv, CHILD_TO_PARENT_AGGREGATION.csv,
         ACTIVITY_LEVEL_RT_TEST.csv, DUAL_CODING_COMPARISON.csv, AGREEMENT_SUMMARY.csv
"""
import itertools
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import RUN_ROOT, read_csv, write_csv  # noqa: E402

D = RUN_ROOT / "08_DUAL_CODING"
B = RUN_ROOT / "01_BASELINES"
FN = ["F_CODE_CREATION", "F_ASSURANCE", "F_MONITORING", "F_REGISTRY_ADMINISTRATION", "F_INTERNAL_COMPLIANCE", "F_DISPUTE_RESOLUTION",
      "F_COMPLAINT_HANDLING", "F_AUDITING", "F_INSURANCE_RISK_UNDERWRITING", "F_ENFORCEMENT"]
LABEL2F = {"code_creation": "F_CODE_CREATION", "assurance": "F_ASSURANCE", "monitoring": "F_MONITORING", "registry_administration": "F_REGISTRY_ADMINISTRATION",
           "internal_compliance": "F_INTERNAL_COMPLIANCE", "dispute_resolution": "F_DISPUTE_RESOLUTION", "complaint_handling": "F_COMPLAINT_HANDLING",
           "auditing": "F_AUDITING", "insurance_risk_underwriting": "F_INSURANCE_RISK_UNDERWRITING", "insurance / risk underwriting": "F_INSURANCE_RISK_UNDERWRITING",
           "insurance": "F_INSURANCE_RISK_UNDERWRITING", "enforcement": "F_ENFORCEMENT"}


def fcode(label):
    l = (label or "").strip().lower().replace("function_", "").replace("f_", "")
    l = l.replace(" ", "_") if l not in LABEL2F else l
    return LABEL2F.get(l) or LABEL2F.get(l.replace("_", " ")) or None


AMAP = [(r["ACTOR_PATTERN"], r["CONTEXT_CATEGORY"], r["CATEGORY_TYPE"]) for r in read_csv(D / "ACTOR_CONTEXT_MAP.csv")]


def cats(text, kind=None):
    t = (text or "").lower()
    if not t or t.startswith("not_specified"):
        return set()
    out = set()
    for pat, cat, typ in AMAP:
        if pat in t and (kind is None or typ == kind):
            out.add(cat)
    return out


def split(v):
    return {x.strip() for x in re.split(r";", v or "") if x.strip() and x.strip() not in ("N/A",)}


fp_par = {r["PARENT_ID"]: r for r in read_csv(D / "first_pass/PARENT_FIRST_PASS.csv")}
fp_ch = read_csv(D / "first_pass/CHILD_FIRST_PASS.csv")
bp_par, bp_ch = {}, []
if (D / "blind_pass/OUTPUT/PARENT_BLIND.csv").exists():
    bp_par = {r["PARENT_ID"]: r for r in read_csv(D / "blind_pass/OUTPUT/PARENT_BLIND.csv")}
    bp_ch = read_csv(D / "blind_pass/OUTPUT/CHILD_BLIND.csv")

# ---- Rotem L3 baseline mapped to parents (verbatim values) ----
cdi = {r["WB_ROW"]: r for r in read_csv(B / "BASELINE_ROTEM_WB_CODING_DIGITAL_INTERMEDIARIES.csv")}
loa = {r["WB_ROW"]: r for r in read_csv(B / "BASELINE_ROTEM_WB_LIST_OF_ACTORS.csv")}
L3SRC = {"P01_AUD": ("CDI", "75"), "P01_VAL": ("CDI", "75"), "P01_ADR": ("CDI", "75"), "P02_CB": ("CDI", "14"), "P02_NB": ("CDI", "14"), "P02_INS": ("CDI", "14"),
         "P03_NB": ("CDI", "19"), "P03_TL": ("CDI", "19"), "P03_INS": ("CDI", "19"), "P04_LAB": ("CDI", "7"), "P05_AUD": ("LoA", "27"), "P06_TF": ("LoA", "21")}
CDI_F = {"F_CODE_CREATION": "Function_code_creation", "F_ASSURANCE": "Function_assurance", "F_MONITORING": "Function_monitoring", "F_INTERNAL_COMPLIANCE": "Function_internal_compliance",
         "F_DISPUTE_RESOLUTION": "Function_dispute_resolution", "F_COMPLAINT_HANDLING": "Function_complaint_handling", "F_AUDITING": "Function_auditing",
         "F_INSURANCE_RISK_UNDERWRITING": "Function_Insurance / risk underwriting", "F_ENFORCEMENT": "Function_enforcement"}
RK = "Recongnition_pathways (vetting/designation/none)"


def l3(pid):
    sheet, row = L3SRC[pid]
    out = {"ROTEM_L3_SOURCE": f"{sheet} row {row}"}
    if sheet == "CDI":
        r = cdi[row]
        n_int = len([x for x in re.split(r";|,| and |\n", r["Who are the intermediaries?"]) if x.strip()])
        out["ROTEM_L3_UNIT"] = "ACT_LEVEL_PACKED" if n_int > 1 else "ACT_LEVEL_SINGLE"
        out["ROTEM_L3_INTERMEDIARIES"] = r["Who are the intermediaries?"].replace("\n", " ").strip()
        for f in FN:
            out["L3_" + f] = (r.get(CDI_F.get(f, ""), "") or "").strip() if f in CDI_F else "NOT_A_COLUMN"
        out["ROTEM_L3_RECOGNITION"] = r[RK].replace("\n", " ").strip()
        out["ROTEM_L3_OBLIGATION_INTENSITY"] = r["Obligation_intensity"].replace("\n", " ").strip()
        out["ROTEM_L3_RELEVANT_PROVISIONS"] = r["Relevant provision(s)"].strip() or "(empty)"
        out["ROTEM_L3_DESCRIPTION"] = r["What do the intermediaries do?"].replace("\n", " ").strip()
        out["ROTEM_L3_PRIMARY_FUNCTION_MECHANISM"] = "NOT_A_COLUMN"
        out["ROTEM_L3_POSITION_IN_GOVERNANCE_CHAIN"] = "NOT_A_COLUMN"
        out["ROTEM_L3_RECOGNIZER_TYPE"] = "NOT_A_COLUMN"
    else:
        r = loa[row]
        out["ROTEM_L3_UNIT"] = "INTERMEDIARY_X_ACT"
        out["ROTEM_L3_INTERMEDIARIES"] = r["Intermediary_legal_label"].strip()
        pfm = r["Primary_function_mechanism"].strip()
        for f in FN:
            out["L3_" + f] = "Yes (from Primary_function_mechanism)" if fcode(pfm) == f else "NOT_CODED"
        out["ROTEM_L3_RECOGNITION"] = r["Recognition_pathway"].strip()
        out["ROTEM_L3_OBLIGATION_INTENSITY"] = r["Obligation_intensity"].strip()
        out["ROTEM_L3_RELEVANT_PROVISIONS"] = r["Relevant_articles_addressing_intermediaries"].strip()
        out["ROTEM_L3_DESCRIPTION"] = "(no description column in LoA)"
        out["ROTEM_L3_PRIMARY_FUNCTION_MECHANISM"] = pfm
        out["ROTEM_L3_POSITION_IN_GOVERNANCE_CHAIN"] = r["Position_in_governance_chain"].strip()
        out["ROTEM_L3_RECOGNIZER_TYPE"] = r["Recognizer_type"].strip()
    return out


# ---- PARENT table ----
PCOLS = ["INTERMEDIARY_QUALIFIES", "RELEVANT_PROVISIONS", "INTERMEDIARY_INVOLVEMENT", "ORIENTATION", "REGULATOR_CONTEXT", "TARGET_CONTEXT"] + FN + ["MECHANISM_FAMILY", "RECOGNITION_PATHWAY", "IDENTIFICATION_BASIS_TEST", "FUNCTION_DESCRIPTION"]
prow = []
for pid, p in fp_par.items():
    r = {"PARENT_ID": pid, "CASE_ID": p["CASE_ID"], "ACT_ID": p["ACT_ID"], "INTERMEDIARY_NAME": p["INTERMEDIARY_NAME"]}
    r.update(l3(pid))
    for c in PCOLS:
        r["FP_" + c] = p.get(c, "")
        r["BP_" + c] = bp_par.get(pid, {}).get(c, "NOT_AVAILABLE") if bp_par else "NOT_AVAILABLE"
    r["FP_CODING_STATUS"] = "MODEL_CODED / INTERPRETIVE_APPLICATION of revised codebook"
    r["BP_CODING_STATUS"] = "MODEL_BLIND_SECOND_PASS / INTERPRETIVE_APPLICATION" if bp_par else "NOT_AVAILABLE"
    prow.append(r)
write_csv(D / "PARENT_INTERMEDIARY_ACT.csv", list(prow[0].keys()), prow)

# ---- CHILD table (first pass canonical + blind pass rows), with provenance columns ----
crow = []
for passname, rows in [("FIRST_PASS", fp_ch), ("BLIND_SECOND_PASS", bp_ch)]:
    for e in rows:
        x = dict(e)
        x["PASS"] = passname
        x["ACT_ID"] = (x.get("SOURCE_PROVISION_ID", "") or ":").split(":")[0]
        x["SOURCE_ID"] = "OFF-" + x["ACT_ID"]
        x["EVIDENCE_STATUS"] = "VERIFIED_OFFICIAL_URL"
        crow.append(x)
CCOLS = ["PASS", "EVENT_ID", "PARENT_ID", "ACT_ID", "SOURCE_PROVISION_ID", "SOURCE_ID", "EVIDENCE_STATUS", "TEXT_SPAN", "ACTOR", "ACTION", "ACTION_ADDRESSEE", "OBJECT",
         "REGULATOR_ACTOR", "INTERMEDIARY_ACTOR", "TARGET_ACTOR", "INTERMEDIARY_ROLE_IN_EVENT", "NORMATIVE_MODALITY", "TRIGGER_CONDITION", "LEGAL_EFFECT", "FUNCTION_CODE",
         "MECHANISM_CODE", "INFERENCE_BASIS", "RATIONALE", "CONFIDENCE", "REVIEW_STATUS"]
write_csv(D / "CHILD_PROVISION_RELATION_EVENT.csv", CCOLS, crow)


# ---- child→parent aggregation and activity-level R×T test (per pass) ----
def analyse(par, ch, passname):
    agg, rt = [], []
    by = defaultdict(list)
    for e in ch:
        by[e["PARENT_ID"]].append(e)
    for pid, p in par.items():
        evs = by.get(pid, [])
        fev = [e for e in evs if fcode(e.get("FUNCTION_CODE"))]
        derived_f = {fcode(e["FUNCTION_CODE"]) for e in fev}
        coded_f = {f for f in FN if p.get(f, "").strip().lower() == "yes"}
        der_reg = set().union(*[cats(e["REGULATOR_ACTOR"], "REGULATOR") | cats(e["ACTION_ADDRESSEE"], "REGULATOR") | (cats(e["ACTOR"], "REGULATOR") if e.get("INTERMEDIARY_ROLE_IN_EVENT") in ("OBJECT", "ADDRESSEE", "BENEFICIARY") else set()) for e in evs]) if evs else set()
        der_tgt = set().union(*[cats(e["TARGET_ACTOR"], "TARGET") for e in evs]) if evs else set()
        coded_reg, coded_tgt = split(p.get("REGULATOR_CONTEXT")), split(p.get("TARGET_CONTEXT"))
        agg.append(dict(PASS=passname, PARENT_ID=pid, N_EVENTS=len(evs), N_FUNCTION_EVENTS=len(fev),
                        CODED_FUNCTIONS="; ".join(sorted(coded_f)), CHILD_DERIVED_FUNCTIONS="; ".join(sorted(derived_f)),
                        FUNCTIONS_CODED_WITHOUT_SUPPORTING_EVENT="; ".join(sorted(coded_f - derived_f)) or "NONE",
                        FUNCTIONS_IN_EVENTS_NOT_CODED_AT_PARENT="; ".join(sorted(derived_f - coded_f)) or "NONE",
                        CODED_REGULATOR_CONTEXT="; ".join(sorted(coded_reg)), CHILD_DERIVED_REGULATOR_CATEGORIES="; ".join(sorted(der_reg)) or "NONE",
                        CODED_TARGET_CONTEXT="; ".join(sorted(coded_tgt)), CHILD_DERIVED_TARGET_CATEGORIES="; ".join(sorted(der_tgt)) or "NONE",
                        PARENT_KEY_INTEGRITY="OK" if all(e["PARENT_ID"] == pid for e in evs) else "BROKEN"))
        # activity-level triples
        implied = set(itertools.product(sorted(coded_f), sorted(coded_reg), sorted(coded_tgt)))
        supported = set()
        no_reg = 0
        for e in fev:
            f = fcode(e["FUNCTION_CODE"])
            rr = cats(e["REGULATOR_ACTOR"], "REGULATOR") | cats(e["ACTION_ADDRESSEE"], "REGULATOR")
            tt = cats(e["TARGET_ACTOR"], "TARGET") | cats(e["ACTION_ADDRESSEE"], "TARGET")
            if not rr:
                no_reg += 1
            for r_, t_ in itertools.product(rr or {"NONE"}, tt or {"NONE"}):
                supported.add((f, r_, t_))
        sup_in_implied = implied & supported
        # path-based view: regulator categories linked to the intermediary by any event (recognition, supervision, output transfer)
        ri = set().union(*[cats(e["REGULATOR_ACTOR"], "REGULATOR") | cats(e["ACTION_ADDRESSEE"], "REGULATOR") for e in evs]) if evs else set()
        it = set().union(*[cats(e["TARGET_ACTOR"], "TARGET") | cats(e["ACTION_ADDRESSEE"], "TARGET") for e in fev]) if fev else set()
        pairs_implied = set(itertools.product(sorted(coded_reg), sorted(coded_tgt)))
        pairs_path = {(a, b) for a, b in pairs_implied if a in ri and b in it}
        pairs_direct = {(r_, t_) for (_, r_, t_) in supported if r_ != "NONE" and t_ != "NONE"}
        out_addr = Counter()
        for e in fev:
            if e.get("INTERMEDIARY_ROLE_IN_EVENT") == "ACTOR" and not (e.get("ACTION_ADDRESSEE", "").startswith("NOT_SPECIFIED")):
                for c_ in (cats(e["ACTION_ADDRESSEE"], "REGULATOR") or {"(non-regulator)"}):
                    out_addr[c_] += 1
        rt.append(dict(PASS=passname, PARENT_ID=pid, FUNCTIONS=len(coded_f), REGULATOR_CONTEXT_VALUES=len(coded_reg), TARGET_CONTEXT_VALUES=len(coded_tgt),
                       IMPLIED_TRIPLES_FxRxT=len(implied), TEXT_SUPPORTED_TRIPLES=len(sup_in_implied), UNSUPPORTED_IMPLIED_TRIPLES=len(implied - sup_in_implied),
                       SHARE_UNSUPPORTED=(round(len(implied - sup_in_implied) / len(implied), 2) if implied else ""),
                       FUNCTION_EVENTS=len(fev), FUNCTION_EVENTS_WITHOUT_REGULATOR=no_reg,
                       IMPLIED_RT_PAIRS=len(pairs_implied), RT_PAIRS_PATH_SUPPORTED=len(pairs_path), RT_PAIRS_DIRECT_CO_PARTICIPATION=len(pairs_direct & pairs_implied),
                       RT_PAIRS_WITHOUT_TEXTUAL_PATH="; ".join("|".join(x) for x in sorted(pairs_implied - pairs_path)) or "NONE",
                       OUTPUT_ADDRESSEES_OF_INTERMEDIARY_FUNCTION_EVENTS="; ".join(f"{k}={v}" for k, v in sorted(out_addr.items())) or "NONE",
                       SUPPORTED_TRIPLES_LIST="; ".join("|".join(t) for t in sorted(sup_in_implied)) or "NONE",
                       CHILD_TRIPLES_ALL="; ".join("|".join(t) for t in sorted(supported)) or "NONE"))
    return agg, rt


A1, R1 = analyse(fp_par, fp_ch, "FIRST_PASS")
A2, R2 = analyse(bp_par, bp_ch, "BLIND_SECOND_PASS") if bp_par else ([], [])
write_csv(D / "CHILD_TO_PARENT_AGGREGATION.csv", list(A1[0].keys()), A1 + A2)
write_csv(D / "ACTIVITY_LEVEL_RT_TEST.csv", list(R1[0].keys()), R1 + R2)

# ---- field-level comparison (Rotem L3 vs first pass vs blind pass) ----
cmp_rows = []


def norm_yes(v):
    v = (v or "").strip().lower()
    if v.startswith("yes"):
        return "Yes"
    if v in ("no", "n/a", "n/a ", "na"):
        return "No" if v == "no" else "N/A"
    return v or "(blank)"


for r in prow:
    pid = r["PARENT_ID"]
    for f in FN:
        l3v, fpv, bpv = r["L3_" + f], r["FP_" + f], r["BP_" + f]
        packed = r["ROTEM_L3_UNIT"] == "ACT_LEVEL_PACKED"
        cmp_rows.append(dict(PARENT_ID=pid, FIELD=f, ROTEM_L3=l3v, FIRST_PASS=fpv, BLIND_PASS=bpv,
                             FP_vs_BP=("AGREE" if norm_yes(fpv) == norm_yes(bpv) else "DISAGREE") if bp_par else "NOT_AVAILABLE",
                             L3_vs_FP=("L3_NOT_A_COLUMN" if l3v == "NOT_A_COLUMN" else "L3_NOT_CODED" if l3v in ("NOT_CODED", "", "(blank)") else
                                       ("AGREE" if norm_yes(l3v) == norm_yes(fpv) else ("DISAGREE_L3_PACKED_ROW" if packed else "DISAGREE")))))
    for fld, l3k in [("RECOGNITION_PATHWAY", "ROTEM_L3_RECOGNITION"), ("ORIENTATION", "ROTEM_L3_POSITION_IN_GOVERNANCE_CHAIN"), ("REGULATOR_CONTEXT", None), ("TARGET_CONTEXT", None),
                     ("INTERMEDIARY_INVOLVEMENT", None), ("MECHANISM_FAMILY", "ROTEM_L3_PRIMARY_FUNCTION_MECHANISM"), ("INTERMEDIARY_QUALIFIES", None), ("IDENTIFICATION_BASIS_TEST", None)]:
        fpv, bpv = r["FP_" + fld], r["BP_" + fld]
        same = (split(fpv.lower()) == split(bpv.lower())) if bp_par else None
        cmp_rows.append(dict(PARENT_ID=pid, FIELD=fld, ROTEM_L3=(r.get(l3k) if l3k else "NOT_IMPLEMENTED_IN_L3"), FIRST_PASS=fpv, BLIND_PASS=bpv,
                             FP_vs_BP=("AGREE" if same else ("PARTIAL" if bp_par and split(fpv.lower()) & split(bpv.lower()) else "DISAGREE")) if bp_par else "NOT_AVAILABLE",
                             L3_vs_FP="SEE_NOTES"))
write_csv(D / "DUAL_CODING_COMPARISON.csv", list(cmp_rows[0].keys()), cmp_rows)

summ = []
if bp_par:
    for fld in sorted({c["FIELD"] for c in cmp_rows}):
        cc = Counter(c["FP_vs_BP"] for c in cmp_rows if c["FIELD"] == fld)
        summ.append(dict(LEVEL="PARENT_FIELD", ITEM=fld, AGREE=cc.get("AGREE", 0), PARTIAL=cc.get("PARTIAL", 0), DISAGREE=cc.get("DISAGREE", 0), N=sum(cc.values())))
    fl = [c for c in cmp_rows if c["FIELD"] in FN]
    cc = Counter(c["FP_vs_BP"] for c in fl)
    summ.append(dict(LEVEL="PARENT_ALL_FUNCTION_FLAGS", ITEM="10 flags x 12 parents", AGREE=cc.get("AGREE", 0), PARTIAL=0, DISAGREE=cc.get("DISAGREE", 0), N=len(fl)))
    write_csv(D / "AGREEMENT_SUMMARY_PARENT.csv", list(summ[0].keys()), summ)
cc = Counter(c["L3_vs_FP"] for c in cmp_rows if c["FIELD"] in FN)
print("L3 vs FP function flags:", dict(cc))
print("parents", len(prow), "| child rows", len(crow), "| RT rows", len(R1 + R2))
for x in R1:
    print(x["PARENT_ID"], "triples", x["IMPLIED_TRIPLES_FxRxT"], "/", x["TEXT_SUPPORTED_TRIPLES"], "| RT pairs", x["IMPLIED_RT_PAIRS"], "path", x["RT_PAIRS_PATH_SUPPORTED"], "direct", x["RT_PAIRS_DIRECT_CO_PARTICIPATION"], "| fn-ev", x["FUNCTION_EVENTS"], "no-reg", x["FUNCTION_EVENTS_WITHOUT_REGULATOR"], "| no-path:", x["RT_PAIRS_WITHOUT_TEXTUAL_PATH"], "| out:", x["OUTPUT_ADDRESSEES_OF_INTERMEDIARY_FUNCTION_EVENTS"])
for a in A1:
    print(a["PARENT_ID"], "| coded-not-derived:", a["FUNCTIONS_CODED_WITHOUT_SUPPORTING_EVENT"], "| derived-not-coded:", a["FUNCTIONS_IN_EVENTS_NOT_CODED_AT_PARENT"], "| reg:", a["CODED_REGULATOR_CONTEXT"], "vs", a["CHILD_DERIVED_REGULATOR_CATEGORIES"], "| tgt:", a["CODED_TARGET_CONTEXT"], "vs", a["CHILD_DERIVED_TARGET_CATEGORIES"])
