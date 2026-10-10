# MECHANICAL ASSEMBLER / VALIDATOR (no analytical rules).
# Reads executor-authored record files rec/*.txt (line DSL, see DSL_SPEC.md), resolves local labels to stable ids,
# extracts verbatim spans from the unit text between executor-chosen anchors, writes the 19 CSV tables to build/,
# and runs the data-dictionary integrity checks.
import csv, json, re, sys, os, glob, hashlib
from collections import OrderedDict, defaultdict

W = os.path.dirname(os.path.abspath(__file__))
CASE = "RGAM_AI_AI_ACT"
PFX = CASE + "."
OUT = os.path.join(W, "build")
os.makedirs(OUT, exist_ok=True)
TEMPL = os.path.join(W, "..")  # blank templates (header-only) copied into the case dir

units = json.load(open(os.path.join(W, "units.json"), encoding="utf-8"))
U = OrderedDict((x["unit_id"][len(PFX):], x) for x in units)
UORDER = list(U.keys())
UIDX = {k: i for i, k in enumerate(UORDER)}

errors = []
warnings = []


def err(m):
    errors.append(m)


def expand_units(spec, ctx=""):
    out = []
    if not spec:
        return out
    for tok in re.split(r"\s*;\s*", spec.strip()):
        if not tok:
            continue
        if ".." in tok and tok not in U:
            # range, but ids themselves contain single dots; split on the double dot only
            a, b = tok.split("..", 1)
            a, b = a.strip(), b.strip()
            if a not in U or b not in U:
                err(f"{ctx}: bad range {tok}")
                continue
            out.extend(UORDER[UIDX[a]:UIDX[b] + 1])
        else:
            t = tok.replace(PFX, "")
            if t not in U:
                err(f"{ctx}: unknown unit {tok}")
                continue
            out.append(t)
    # de-duplicate keep order
    seen = set()
    res = []
    for x in out:
        if x not in seen:
            seen.add(x)
            res.append(x)
    return res


def resolve_span(spec, unit_short, ctx=""):
    """spec: 'start~~end' or exact text. Returns verbatim text from unit."""
    t = U[unit_short]["text"]
    if "~~" in spec:
        a, b = spec.split("~~", 1)
        i = t.find(a)
        if i < 0:
            err(f"{ctx}: span start not found in {unit_short}: {a[:50]!r}")
            return ""
        j = t.find(b, i + len(a)) if b else i + len(a)
        if j < 0:
            err(f"{ctx}: span end not found in {unit_short}: {b[:50]!r}")
            return ""
        s = t[i:j + len(b)]
    else:
        if spec not in t:
            err(f"{ctx}: span not found verbatim in {unit_short}: {spec[:60]!r}")
            return ""
        s = spec
    if len(s) > 400:
        err(f"{ctx}: span >400 chars ({len(s)}) in {unit_short}")
        s = s[:400]
    return s


def parse_file(path):
    recs = []
    with open(path, encoding="utf-8") as f:
        for ln, line in enumerate(f, 1):
            line = line.rstrip("\n")
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            parts = [p.strip() for p in line.split(" | ")]
            rt = parts[0].strip()
            kv = OrderedDict()
            for p in parts[1:]:
                if "=" not in p:
                    err(f"{os.path.basename(path)}:{ln}: field without '=': {p[:40]!r}")
                    continue
                k, v = p.split("=", 1)
                kv[k.strip()] = v.strip()
            recs.append((rt, kv, f"{os.path.basename(path)}:{ln}"))
    return recs


FN = {"rm": "rule_making_standard_setting", "im": "implementation", "it": "interpretation_translation",
      "ip": "information_provision", "mo": "monitoring", "va": "verification_assurance", "en": "enforcement",
      "ad": "adjudication_dispute_resolution", "re": "remediation", "rp": "representation_participation*",
      "ag": "authorization_designation*", "cc": "cooperation_coordination*", "un": "FUNCTION_VOCABULARY_UNRESOLVED"}
FNALL = set(FN.values())
MOD = {"ob": "obligation", "op": "obligation_promotional", "pr": "prohibition", "pe": "permission", "co": "competence",
       "en": "entitlement", "de": "definition", "dc": "declaratory"}
RT = {"ac": "authority_control", "da": "delegation_authorization", "os": "oversight_supervision",
      "acc": "accountability", "ir": "information_reporting", "va": "verification_assurance",
      "ra": "review_adjudication", "rp": "representation_participation", "ce": "contractual_exchange",
      "bp": "beneficiary_protective"}
STK = {"ab": "assignment_bearing", "rb": "relation_bearing", "pd": "position_defining", "dd": "device_defining",
       "df": "definitional", "sc": "scope", "pr": "procedural", "ex": "external_referencing", "ff": "final_formal",
       "ot": "other"}
NT = {"CMP": "COMPOUND", "AMB": "AMBIGUOUS"}
NTALL = {"N0", "N1", "N2", "N3", "N4", "COMPOUND", "AMBIGUOUS"}
LS_ALL = {"in_force", "not_yet_applicable", "suspended", "expired_or_repealed", "conditional_on_further_act"}
EP_ALL = {"conceptually_projected", "documented", "legal_constitution_evidenced", "material_establishment_evidenced",
          "exercise_evidenced"}
GLOBAL_TEMPORAL = ("Reference point 2 August 2026 (general date of application, Art. 113 second paragraph), "
                   "considered with entry into force on the twentieth day after publication (Art. 113 first paragraph) "
                   "and the staged application dates of Art. 113 points (a)-(c)")


def m(d, key, table, default=""):
    v = d.get(key, default)
    if v in table:
        return table[v]
    return v


# ------------------------------------------------------------------ load all record files
files = sorted(glob.glob(os.path.join(W, "rec", "*.txt")))
allrecs = []
for fp in files:
    allrecs.extend(parse_file(fp))

# default legal-status map (article level) -- authored override list in rec/ls_map.json if present
LSMAP = {}
lsp = os.path.join(W, "ls_map.json")
if os.path.exists(lsp):
    LSMAP = json.load(open(lsp, encoding="utf-8"))


def default_ls(unit_short):
    """Most specific prefix match in LSMAP; default in_force."""
    best = None
    for pref, v in LSMAP.items():
        if unit_short == pref or unit_short.startswith(pref + "."):
            if best is None or len(pref) > len(best[0]):
                best = (pref, v)
    if best:
        return best[1]["ls"], best[1].get("vn", "")
    return "in_force", ""


# ------------------------------------------------------------------ pass 1: assign ids / labels
labels = {}  # label -> final id
recs_by_type = defaultdict(list)
cur_st = None
counters = defaultdict(int)
PFXID = {"ST": ("ST-", 4), "NA": ("NA-", 4), "PD": ("PD-", 3), "QR": ("QR-", 4), "EXT": ("EXT-", 3), "SC": ("SC-", 2),
         "ARCH": ("ARCH-", 2), "PROP": ("PROP-", 3), "CL": ("CL-", 2), "UNC": ("UNC-", 3), "HQ": ("HQ-", 3),
         "TR": ("TR-", 2), "DEV": ("DEV-", 2), "RUN": ("RUN-", 2)}


def newid(rt):
    counters[rt] += 1
    p, w = PFXID[rt]
    return f"{p}{counters[rt]:0{w}d}"


for rt, kv, where in allrecs:
    if rt in PFXID:
        rid = newid(rt)
        kv["_id"] = rid
        kv["_where"] = where
        if rt == "ST":
            kv["_curst"] = None
            cur_st = kv
        else:
            kv["_curst"] = cur_st
        lab = kv.get("id") or (kv.get("key") if rt in ("PD", "EXT") else None)
        if lab:
            if lab in labels:
                err(f"{where}: duplicate label {lab}")
            labels[lab] = rid
        recs_by_type[rt].append(kv)
    elif rt in ("SCR", "TAGDEF", "PDX", "EXTX"):
        kv["_where"] = where
        kv["_curst"] = cur_st
        recs_by_type[rt].append(kv)
    else:
        err(f"{where}: unknown record type {rt}")


def rid(label, ctx=""):
    if not label:
        return ""
    if label in labels:
        return labels[label]
    if re.fullmatch(r"(ST|NA|PD|QR|EXT|SC|ARCH|PROP|CL|UNC|HQ|TR|DEV|LNK|RUN)-\d+", label):
        return label
    err(f"{ctx}: unresolved label {label!r}")
    return ""


def rids(spec, ctx=""):
    if not spec:
        return []
    return [rid(x.strip(), ctx) for x in re.split(r"\s*;\s*", spec) if x.strip()]


def semi(l):
    return ";".join(x for x in l if x)


# ------------------------------------------------------------------ statements
ST = {}
for kv in recs_by_type["ST"]:
    ctx = kv["_where"]
    uids = expand_units(kv.get("u", ""), ctx)
    if not uids:
        err(f"{ctx}: ST without units")
        continue
    spu = kv.get("spu", uids[0]).replace(PFX, "")
    span = resolve_span(kv.get("sp", ""), spu, ctx) if kv.get("sp") else ""
    if not span:
        err(f"{ctx}: ST without span")
    kv["_units"] = uids
    kv["_span"] = span
    kv["_spu"] = spu
    kv["_kind"] = m(kv, "k", STK, "other")
    ST[kv["_id"]] = kv

# which statements derive which records (filled later)
derived = defaultdict(list)
na_by_tag = defaultdict(list)
qr_by_tag = defaultdict(list)

# ------------------------------------------------------------------ positions / devices
PDS = OrderedDict()
for kv in recs_by_type["PD"]:
    ctx = kv["_where"]
    st = kv.get("st") or (kv["_curst"]["_id"] if kv["_curst"] else "")
    sts = [x for x in (rids(kv.get("st"), ctx) if kv.get("st") else ([kv["_curst"]["_id"]] if kv["_curst"] else [])) if x]
    uids = expand_units(kv.get("u", ""), ctx)
    if not uids and sts:
        uids = list(ST[sts[0]]["_units"])
    spu = kv.get("spu", uids[0] if uids else "").replace(PFX, "")
    span = resolve_span(kv["sp"], spu, ctx) if kv.get("sp") else (ST[sts[0]]["_span"] if sts else "")
    kind = kv.get("kind", "POSITION").upper()
    r = OrderedDict()
    r["pd_id"] = kv["_id"]
    r["case_id"] = CASE
    r["kind"] = kind
    r["label"] = kv.get("label", kv.get("key", ""))
    r["type_or_instance"] = kv.get("tor", "TYPE")
    r["instance_source_unit_ids"] = semi([PFX + x for x in expand_units(kv.get("isrc", ""), ctx)])
    r["jurisdiction"] = kv.get("jur", "European Union (legal category created or recognised by Regulation (EU) 2024/1689)")
    r["temporal_reference"] = kv.get("tref", GLOBAL_TEMPORAL)
    r["legal_multiplicity"] = kv.get("mult", "unspecified")
    r["establishment_norm_type"] = NT.get(kv.get("ent", "NONE"), kv.get("ent", "NONE"))
    r["device_identity_evidence"] = kv.get("di", "")
    r["device_function_evidence"] = kv.get("dfe", "")
    r["device_classification"] = kv.get("dc", "")
    r["legal_constitution_status"] = kv.get("lcs", "not_applicable")
    r["material_establishment_evidence"] = "not_assessed"
    r["epistemic_status"] = kv.get("es", "documented")
    r["supporting_unit_ids"] = semi([PFX + x for x in uids])
    r["evidence_span"] = span
    r["uncertainty_ids"] = ""
    r["hq_ids"] = ""
    r["_units"] = uids
    r["_sts"] = sts
    r["_kv"] = kv
    PDS[kv["_id"]] = r
    for s in sts:
        derived[s].append(kv["_id"])

# PDX: extend an existing PD with further supporting units/statements and field overrides
for kv in recs_by_type["PDX"]:
    ctx = kv["_where"]
    key = labels.get(kv.get("key", ""))
    if key not in PDS:
        err(f"{ctx}: PDX unknown key {kv.get('key')}")
        continue
    p = PDS[key]
    sts = rids(kv.get("st"), ctx) if kv.get("st") else ([kv["_curst"]["_id"]] if kv["_curst"] else [])
    uids = expand_units(kv.get("u", ""), ctx) if kv.get("u") else (list(ST[sts[0]]["_units"]) if sts else [])
    for u in uids:
        if u not in p["_units"]:
            p["_units"].append(u)
    for s_ in sts:
        if s_ not in p["_sts"]:
            p["_sts"].append(s_)
        derived[s_].append(key)
    p["supporting_unit_ids"] = semi([PFX + x for x in p["_units"]])
    for k_, col in (("ent", "establishment_norm_type"), ("lcs", "legal_constitution_status"), ("es", "epistemic_status"),
                    ("mult", "legal_multiplicity"), ("tor", "type_or_instance"), ("jur", "jurisdiction"),
                    ("di", "device_identity_evidence"), ("dfe", "device_function_evidence"), ("dc", "device_classification"),
                    ("label", "label")):
        if k_ in kv:
            p[col] = NT.get(kv[k_], kv[k_]) if k_ == "ent" else kv[k_]
    if kv.get("isrc"):
        p["instance_source_unit_ids"] = semi([PFX + x for x in expand_units(kv["isrc"], ctx)])
    p["_kv"]["_pdx_unc"] = p["_kv"].get("_pdx_unc", []) + ([kv["unc"]] if kv.get("unc") else [])
    p["_kv"]["_pdx_hq"] = p["_kv"].get("_pdx_hq", []) + ([kv["hq"]] if kv.get("hq") else [])

# ------------------------------------------------------------------ NA
NAS = OrderedDict()
for kv in recs_by_type["NA"]:
    ctx = kv["_where"]
    sts = rids(kv["st"], ctx) if kv.get("st") else ([kv["_curst"]["_id"]] if kv["_curst"] else [])
    if not sts:
        err(f"{ctx}: NA without statement")
        continue
    uids = expand_units(kv["u"], ctx) if kv.get("u") else list(OrderedDict.fromkeys(u for s in sts for u in ST[s]["_units"]))
    pd = rid(kv.get("pd"), ctx)
    mod = m(kv, "mod", MOD, "obligation")
    nt = NT.get(kv.get("nt", "N0"), kv.get("nt", "N0"))
    ls, vn = default_ls(uids[0])
    ls = kv.get("ls", ls)
    es = kv.get("es", "legal_constitution_evidenced" if ls == "in_force" else "documented")
    spu = kv.get("spu", uids[0]).replace(PFX, "")
    span = resolve_span(kv["sp"], spu, ctx) if kv.get("sp") else ST[sts[0]]["_span"]
    r = OrderedDict()
    r["na_id"] = kv["_id"]; r["case_id"] = CASE
    r["statement_ids"] = semi(sts)
    r["supporting_unit_ids"] = semi([PFX + x for x in uids])
    r["subject_pd_id"] = pd
    r["action"] = kv.get("act", ""); r["object"] = kv.get("obj", "")
    r["function"] = m(kv, "fn", FN, "")
    r["mechanism"] = kv.get("mech", "")
    r["instrument_ref"] = labels.get(kv.get("ins", ""), kv.get("ins", ""))
    r["modality"] = mod
    r["conditions"] = kv.get("cond", "")
    r["counterpart_if_identifiable"] = kv.get("cp", "")
    r["counterpart_status"] = kv.get("cps", "NONE_IDENTIFIABLE")
    r["norm_type"] = nt
    ce_def = {"obligation": "duty attached to the position", "obligation_promotional": "promotional duty attached to the position",
              "prohibition": "constraint (prohibition) on the position", "permission": "permission attached to the position",
              "competence": "competence/power attached to the position", "entitlement": "entitlement stated for the position",
              "definition": "definition (identity/scope only)", "declaratory": "declaratory statement"}[mod]
    r["constitution_effect"] = kv.get("ce", ce_def)
    r["not_constituted_note"] = kv.get("nc", "no entity, no counterparty relation and no establishment (material or exercise) thereby constituted")
    r["constraint_only"] = "Y" if mod == "prohibition" else "N"
    r["derivation"] = kv.get("der", "direct")
    r["derivation_rule"] = kv.get("dr", "")
    r["depends_on_pd_ids"] = semi(rids(kv["dep"], ctx)) if kv.get("dep") else pd
    r["legal_status_of_norm"] = ls
    r["epistemic_status"] = es
    r["evidence_span"] = span
    r["uncertainty_ids"] = ""
    r["hq_ids"] = ""
    r["_units"] = uids; r["_sts"] = sts; r["_kv"] = kv; r["_vn"] = vn
    NAS[kv["_id"]] = r
    for s in sts:
        derived[s].append(kv["_id"])
    for t in re.split(r"\s*;\s*", kv.get("tag", "")):
        if t:
            na_by_tag[t].append(kv["_id"])

# ------------------------------------------------------------------ QR
QRS = OrderedDict()
for kv in recs_by_type["QR"]:
    ctx = kv["_where"]
    sts = rids(kv["st"], ctx) if kv.get("st") else ([kv["_curst"]["_id"]] if kv["_curst"] else [])
    if not sts:
        err(f"{ctx}: QR without statement")
        continue
    uids = expand_units(kv["u"], ctx) if kv.get("u") else list(OrderedDict.fromkeys(u for s in sts for u in ST[s]["_units"]))
    o = rid(kv.get("o"), ctx); c = rid(kv.get("c"), ctx)
    add = semi(rids(kv.get("add", ""), ctx))
    ls, vn = default_ls(uids[0])
    ls = kv.get("ls", ls)
    es = kv.get("es", "legal_constitution_evidenced" if ls == "in_force" else "documented")
    spu = kv.get("spu", uids[0]).replace(PFX, "")
    span = resolve_span(kv["sp"], spu, ctx) if kv.get("sp") else ST[sts[0]]["_span"]
    mod = m(kv, "mod", MOD, "obligation")
    ol = labels_rev = None
    r = OrderedDict()
    r["qr_id"] = kv["_id"]; r["case_id"] = CASE
    r["statement_ids"] = semi(sts)
    r["supporting_unit_ids"] = semi([PFX + x for x in uids])
    r["origin_pd_id"] = o; r["counterpart_pd_id"] = c; r["additional_party_pd_ids"] = add
    r["relation_type"] = m(kv, "rt", RT, "")
    r["type_note"] = kv.get("tn", "")
    r["textual_direction"] = kv.get("td", "")  # filled with labels later if blank
    r["governance_direction"] = kv.get("gd", "")
    r["action"] = kv.get("act", ""); r["object"] = kv.get("obj", "")
    r["function"] = m(kv, "fn", FN, "")
    r["mechanism"] = kv.get("mech", "")
    r["instrument_ref"] = labels.get(kv.get("ins", ""), kv.get("ins", ""))
    r["modality"] = mod
    r["conditions"] = kv.get("cond", "")
    r["validity_note"] = kv.get("vn", vn or "Norm applicable at the declared reference point; see W_DECLARATION temporal_reference")
    r["legal_status_of_norm"] = ls
    r["epistemic_status"] = es
    r["derivation"] = kv.get("der", "direct")
    r["derivation_rule"] = kv.get("dr", "")
    r["authority_attribute"] = kv.get("aa", "")
    r["discretion_attribute"] = kv.get("da", "")
    r["accountability_class"] = kv.get("ac", "NONE")
    r["accountability_sufficiency"] = kv.get("as", "NA")
    r["accountability_missing_elements"] = kv.get("ame", "")
    r["accountable_via_qr_ids"] = semi(rids(kv.get("via", ""), ctx))
    r["depends_on_pd_ids"] = semi(rids(kv["dep"], ctx)) if kv.get("dep") else semi([o, c] + ([x for x in add.split(";") if x]))
    r["support_gap_report"] = kv.get("sg", "Material establishment of the depended-on positions/devices is not assessed (layer X not collected from legal text); documented/legal-constitution status only")
    r["external_ref_ids"] = semi(rids(kv.get("ext", ""), ctx))
    r["evidence_span"] = span
    r["uncertainty_ids"] = ""
    r["hq_ids"] = ""
    r["_units"] = uids; r["_sts"] = sts; r["_kv"] = kv
    QRS[kv["_id"]] = r
    for s in sts:
        derived[s].append(kv["_id"])
    for t in re.split(r"\s*;\s*", kv.get("tag", "")):
        if t:
            qr_by_tag[t].append(kv["_id"])

# ------------------------------------------------------------------ EXT
EXTS = OrderedDict()
for kv in recs_by_type["EXT"]:
    ctx = kv["_where"]
    sts = rids(kv["st"], ctx) if kv.get("st") else ([kv["_curst"]["_id"]] if kv["_curst"] else [])
    uids = expand_units(kv["u"], ctx) if kv.get("u") else (list(ST[sts[0]]["_units"]) if sts else [])
    r = OrderedDict()
    r["ext_id"] = kv["_id"]; r["case_id"] = CASE
    r["supporting_unit_ids"] = semi([PFX + x for x in uids])
    r["referenced_legal_source"] = kv.get("src", "")
    r["source_kind"] = kv.get("sk", "legal_instrument")
    r["reference_role"] = kv.get("role", "other")
    r["source_verification_status"] = "not_checked"
    r["boundary_status"] = "outside_corpus_not_expanded"
    r["dependent_record_ids"] = ""
    r["dependency_kind"] = kv.get("dk", "specifies")
    r["constitutive_dependency"] = kv.get("cd", "N")
    r["effect_on_claims"] = kv.get("eff", "")
    r["_units"] = uids; r["_sts"] = sts; r["_kv"] = kv
    EXTS[kv["_id"]] = r
    for s in sts:
        derived[s].append(kv["_id"])

# EXTX: extend an existing EXT with further units / statements / dependents
for kv in recs_by_type["EXTX"]:
    ctx = kv["_where"]
    key = labels.get(kv.get("key", ""))
    if key not in EXTS:
        err(f"{ctx}: EXTX unknown key {kv.get('key')}")
        continue
    e = EXTS[key]
    sts = rids(kv.get("st"), ctx) if kv.get("st") else ([kv["_curst"]["_id"]] if kv["_curst"] else [])
    uids = expand_units(kv.get("u", ""), ctx) if kv.get("u") else (list(ST[sts[0]]["_units"]) if sts else [])
    for u in uids:
        if u not in e["_units"]:
            e["_units"].append(u)
    for s_ in sts:
        if s_ not in e["_sts"]:
            e["_sts"].append(s_)
        derived[s_].append(key)
    e["supporting_unit_ids"] = semi([PFX + x for x in e["_units"]])
    e["_kv"]["dep"] = (e["_kv"].get("dep", "") + ";" + kv.get("dep", "")).strip(";")
    if kv.get("cd") == "Y":
        e["constitutive_dependency"] = "Y"
    if kv.get("eff"):
        e["effect_on_claims"] = (e["effect_on_claims"] + " | " + kv["eff"]).strip(" |")
    if kv.get("src"):
        e["referenced_legal_source"] = e["referenced_legal_source"] + "; " + kv["src"]

# dependent ids for EXT: records citing ext= (NA/QR/others via ext key 'ext')
extdeps = defaultdict(list)
for q in QRS.values():
    for e in q["external_ref_ids"].split(";"):
        if e:
            extdeps[e].append(q["qr_id"])
for n in NAS.values():
    for e in rids(n["_kv"].get("ext", ""), n["_kv"]["_where"]):
        extdeps[e].append(n["na_id"])
        n["_ext"] = rids(n["_kv"].get("ext", ""))
for p in PDS.values():
    for e in rids(p["_kv"].get("ext", ""), p["_kv"]["_where"]):
        extdeps[e].append(p["pd_id"])
for e, r in EXTS.items():
    deps = list(OrderedDict.fromkeys(extdeps.get(e, [])))
    extra = rids(r["_kv"].get("dep", ""))
    r["dependent_record_ids"] = semi(list(OrderedDict.fromkeys(deps + extra)))

# textual direction default
labtxt = {p["pd_id"]: p["label"] for p in PDS.values()}
for q in QRS.values():
    if not q["textual_direction"]:
        q["textual_direction"] = f"{labtxt.get(q['origin_pd_id'], q['origin_pd_id'])} -> {labtxt.get(q['counterpart_pd_id'], q['counterpart_pd_id'])}"

# down-coding rule (RGAM-DR-19/20): a claim whose legal constitution or effect is constituted or conditioned by an unresolved external reference
# (constitutive_dependency = Y and dependency_kind in constitutes/conditions) is kept at documented, flagged, never deleted
ext_cond = {k: (e["constitutive_dependency"] == "Y" and e["dependency_kind"] in ("constitutes", "conditions")) for k, e in EXTS.items()}
DOWN = []
for nid, n in NAS.items():
    exts = rids(n["_kv"].get("ext", ""), n["_kv"]["_where"]) if n["_kv"].get("ext") else []
    hit = [x for x in exts if ext_cond.get(x)]
    if hit and n["epistemic_status"] == "legal_constitution_evidenced" and "es" not in n["_kv"]:
        n["epistemic_status"] = "documented"
        n["not_constituted_note"] = n["not_constituted_note"] + "; down-coded to documented because its legal effect is conditioned on unresolved external reference(s) " + ";".join(hit) + " (RGAM-DR-19, DR-20)"
        DOWN.append(nid)
for qid, q in QRS.items():
    exts = [x for x in q["external_ref_ids"].split(";") if x]
    hit = [x for x in exts if ext_cond.get(x)]
    if hit and q["epistemic_status"] == "legal_constitution_evidenced" and "es" not in q["_kv"]:
        q["epistemic_status"] = "documented"
        q["support_gap_report"] = q["support_gap_report"] + "; down-coded to documented because its legal effect is conditioned on unresolved external reference(s) " + ";".join(hit) + " (RGAM-DR-19, DR-20)"
        DOWN.append(qid)

# ------------------------------------------------------------------ UNC / HQ
UNCS = OrderedDict()
HQS = OrderedDict()
unc_users = defaultdict(list)
hq_users = defaultdict(list)


def attach(tbl, idfield, key_unc="unc", key_hq="hq"):
    for rid_, r in tbl.items():
        kv = r["_kv"]
        us = rids(kv.get(key_unc, ""), kv["_where"])
        hs = rids(kv.get(key_hq, ""), kv["_where"])
        for x in kv.get("_pdx_unc", []):
            us += rids(x, kv["_where"])
        for x in kv.get("_pdx_hq", []):
            hs += rids(x, kv["_where"])
        us = list(OrderedDict.fromkeys(us)); hs = list(OrderedDict.fromkeys(hs))
        r["uncertainty_ids"] = semi(us)
        r["hq_ids"] = semi(hs)
        for u in us:
            unc_users[u].append(rid_)
        for h in hs:
            hq_users[h].append(rid_)


attach(PDS, "pd_id"); attach(NAS, "na_id"); attach(QRS, "qr_id")

for kv in recs_by_type["UNC"]:
    ctx = kv["_where"]
    r = OrderedDict()
    r["unc_id"] = kv["_id"]; r["case_id"] = CASE
    r["record_ids"] = ""
    r["unit_ids"] = semi([PFX + x for x in expand_units(kv.get("u", ""), ctx)])
    r["uncertainty_type"] = kv.get("ut", "OTHER")
    r["description"] = kv.get("d", ""); r["treatment"] = kv.get("tr", ""); r["effect_on_claims"] = kv.get("ef", "")
    r["status"] = kv.get("status", "OPEN")
    r["_kv"] = kv
    UNCS[kv["_id"]] = r
for kv in recs_by_type["HQ"]:
    ctx = kv["_where"]
    r = OrderedDict()
    r["hq_id"] = kv["_id"]; r["case_id"] = CASE
    r["trigger_code"] = kv.get("trig", "HQ-OTHER")
    r["record_refs"] = ""
    r["question"] = kv.get("q", ""); r["competing_readings"] = kv.get("cr", "")
    r["machine_recommendation"] = kv.get("mr", ""); r["reason_human_required"] = kv.get("rh", "")
    for h in ("human_decision", "human_rationale", "decided_by", "decision_date"):
        r[h] = ""
    r["_kv"] = kv
    HQS[kv["_id"]] = r

# ------------------------------------------------------------------ SC / ARCH / PROP / CL (generic key=header-name records)
def generic(rt, header, idcol):
    out = OrderedDict()
    for kv in recs_by_type[rt]:
        r = OrderedDict((h, "") for h in header)
        r[idcol] = kv["_id"]
        if "case_id" in r:
            r["case_id"] = CASE
        for k, v in kv.items():
            if k in header and k != idcol:
                if k.endswith("_ids") or k.endswith("_id") and k != "case_id":
                    r[k] = v  # resolved below
                else:
                    r[k] = v
        r["_kv"] = kv
        out[kv["_id"]] = r
    return out


def hdr(name):
    with open(os.path.join(TEMPL, name + ".csv"), encoding="utf-8-sig") as f:
        return next(csv.reader(f))


H = {n: hdr(n) for n in ["W_DECLARATION", "SOURCE_UNIT_INVENTORY", "UNIT_SCREENING", "INSTITUTIONAL_STATEMENTS",
                         "NORMATIVE_ASSIGNMENTS", "POSITIONS_AND_DEVICES", "QUALIFIED_RELATIONS", "EXTERNAL_REFERENCES",
                         "SUBCONFIGURATIONS", "ARCHITECTURE_CANDIDATES", "PROPERTY_REGISTER", "CLOSURE_REGISTER",
                         "PROVENANCE_LINKS", "UNCERTAINTY_LOG", "HUMAN_REVIEW_QUEUE", "TRACE_DEMONSTRATIONS",
                         "INSTRUMENT_LEVEL_SUMMARY", "PROTOCOL_DEVIATION_LOG", "RUN_METADATA"]}

SCS = generic("SC", H["SUBCONFIGURATIONS"], "sc_id")
ARCHS = generic("ARCH", H["ARCHITECTURE_CANDIDATES"], "arch_id")
PROPS = generic("PROP", H["PROPERTY_REGISTER"], "prop_id")
CLS = generic("CL", H["CLOSURE_REGISTER"], "closure_id")
TRS = generic("TR", H["TRACE_DEMONSTRATIONS"], "trace_id")
DEVS = generic("DEV", H["PROTOCOL_DEVIATION_LOG"], "dev_id")
RUNS = generic("RUN", H["RUN_METADATA"], "run_id")


def resolve_idlist(spec, ctx):
    toks = [x.strip() for x in re.split(r"\s*;\s*", spec) if x.strip()]
    out = []
    for t in toks:
        if t.startswith("tag:"):
            tg = t[4:]
            out.extend(qr_by_tag.get(tg, []) + na_by_tag.get(tg, []))  # caller filters by prefix
        elif t == "ALLPD":
            out.extend(PDS.keys())
        else:
            out.append(rid(t, ctx))
    return out


for tbl in (SCS, ARCHS, PROPS, CLS, TRS, DEVS, RUNS):
    for rid_, r in tbl.items():
        kv = r["_kv"]
        for k in list(r.keys()):
            if k.startswith("_"):
                continue
            if (k.endswith("_ids") or k in ("bearer_id", "traced_id", "closure_ref", "nested_in_sc_id", "i4_external_dependencies")) and r[k] and r[k] != "auto":
                if k in ("i1_scope_units", "units_spanned"):
                    continue
                ids = resolve_idlist(r[k], kv["_where"])
                if k == "member_qr_ids":
                    ids = [x for x in ids if x.startswith("QR-")]
                if k == "member_na_ids":
                    ids = [x for x in ids if x.startswith("NA-")]
                r[k] = semi(list(OrderedDict.fromkeys(ids)))
        for k in ("i1_scope_units", "units_spanned"):
            if k in r and r[k]:
                # keep text parts but expand unit specs if they are pure unit lists
                try:
                    r[k] = semi([PFX + x for x in expand_units(r[k], kv["_where"])])
                except Exception:
                    pass
        # SC member PD auto
        if tbl is SCS:
            if r.get("member_pd_ids", "") in ("auto", ""):
                pds = []
                for qid in r["member_qr_ids"].split(";"):
                    if qid in QRS:
                        q = QRS[qid]
                        pds += [q["origin_pd_id"], q["counterpart_pd_id"]] + [x for x in q["additional_party_pd_ids"].split(";") if x]
                for nid in r["member_na_ids"].split(";"):
                    if nid in NAS:
                        pds.append(NAS[nid]["subject_pd_id"])
                r["member_pd_ids"] = semi(list(OrderedDict.fromkeys(pds)))
            r["default_status"] = "S"
        # attach unc / hq
        us = rids(kv.get("unc", ""), kv["_where"]); hs = rids(kv.get("hq", ""), kv["_where"])
        if "uncertainty_ids" in r:
            r["uncertainty_ids"] = semi(us)
        if "hq_ids" in r:
            r["hq_ids"] = semi(hs)
        for u in us:
            unc_users[u].append(rid_)
        for h in hs:
            hq_users[h].append(rid_)

for uid_, r in UNCS.items():
    refs = list(OrderedDict.fromkeys(unc_users.get(uid_, []) + rids(r["_kv"].get("refs", ""), r["_kv"]["_where"])))
    r["record_ids"] = semi(refs)
    hasq = any(uid_ in rids(h["_kv"].get("uncs", ""), "") for h in HQS.values())
for hid, r in HQS.items():
    refs = list(OrderedDict.fromkeys(hq_users.get(hid, []) + rids(r["_kv"].get("refs", ""), r["_kv"]["_where"])))
    r["record_refs"] = semi(refs)
for uid_, r in UNCS.items():
    if r["_kv"].get("status") is None:
        r["status"] = "ESCALATED_TO_HQ" if r["_kv"].get("esc", "N") == "Y" else "OPEN"

# ------------------------------------------------------------------ statements table
def stmt_rows():
    rows = []
    for sid, s in ST.items():
        r = OrderedDict()
        r["st_id"] = sid
        r["supporting_unit_ids"] = semi([PFX + x for x in s["_units"]])
        r["statement_kind"] = s["_kind"]
        r["statement_summary"] = s.get("sum", "")
        r["evidence_span"] = s["_span"]
        r["derived_record_ids"] = semi(list(OrderedDict.fromkeys(derived.get(sid, []))))
        r["recital_only"] = s.get("ro", "N")
        rows.append(r)
    return rows


# ------------------------------------------------------------------ screening
SCREEN = OrderedDict()
st_units = defaultdict(list)
for sid, s in ST.items():
    for u in s["_units"]:
        st_units[u].append(sid)
KINDTAG = {"assignment_bearing": "operative-assignment", "relation_bearing": "relation-bearing", "position_defining": "position-defining",
           "device_defining": "device-defining", "definitional": "scope/definitional-context", "scope": "scope/definitional-context",
           "procedural": "procedural-mechanism", "external_referencing": "external-referencing", "final_formal": "final/formal",
           "other": "other"}
for kv in recs_by_type["SCR"]:
    ctx = kv["_where"]
    for u in expand_units(kv.get("u", ""), ctx):
        if u in SCREEN and kv.get("ovr") != "Y":
            err(f"{ctx}: unit {u} screened twice")
        SCREEN[u] = dict(rel=kv.get("rel", "No"), tag=kv.get("tag", ""), note=kv.get("note", ""))
screen_rows = []
for u in UORDER:
    sids = st_units.get(u, [])
    sc = SCREEN.get(u)
    if sids:
        kinds = list(OrderedDict.fromkeys(KINDTAG[ST[s]["_kind"]] for s in sids))
        rel = (sc or {}).get("rel", "Yes")
        tag = (sc or {}).get("tag") or ";".join(kinds)
        note = (sc or {}).get("note") or "Statement(s) derived; see INSTITUTIONAL_STATEMENTS"
    elif sc:
        rel, tag, note = sc["rel"], sc["tag"], sc["note"]
    else:
        err(f"unit {u} not screened")
        rel, tag, note = "", "", ""
    if rel == "Yes" and not sids:
        err(f"unit {u}: relevance Yes but no statement")
    screen_rows.append(OrderedDict(unit_id=PFX + u, governance_relevance=rel, governance_role_tag=tag,
                                   statement_ids=semi(sids), screening_note=note))
    if rel == "No" and sids:
        warnings.append(f"unit {u}: relevance No yet has statements")

# ------------------------------------------------------------------ provenance
LINKS = []


def link(record_id, rtype, unit, stype, status, lim=""):
    LINKS.append(OrderedDict(record_id=record_id, record_type=rtype, unit_id=PFX + unit, support_type=stype,
                             evidence_level="A", claim_status_supported=status, limitation=lim))


for sid, s in ST.items():
    for u in s["_units"]:
        link(sid, "ST", u, "direct", "documented", "inscription of the provision; statement adds no content")
for pid, p in PDS.items():
    for u in p["_units"]:
        link(pid, "PD", u, "direct", p["epistemic_status"], "establishment evidence beyond the legal text not assessed")
for nid, n in NAS.items():
    for u in n["_units"]:
        link(nid, "NA", u, "direct" if n["derivation"] == "direct" else "indirect", n["epistemic_status"])
for qid, q in QRS.items():
    for u in q["_units"]:
        link(qid, "QR", u, "direct" if q["derivation"] == "direct" else "indirect", q["epistemic_status"])
for eid, e in EXTS.items():
    for u in e["_units"]:
        link(eid, "EXT", u, "direct", "documented", "legal relevance only; source not checked")


def units_of(idlist):
    us = []
    for i in idlist:
        if i in QRS:
            us += QRS[i]["_units"]
        elif i in NAS:
            us += NAS[i]["_units"]
        elif i in PDS:
            us += PDS[i]["_units"]
        elif i in EXTS:
            us += EXTS[i]["_units"]
        elif i in SCS:
            us += SCS[i].get("_units", [])
    return list(OrderedDict.fromkeys(us))


for sid_, r in SCS.items():
    ids = [x for x in (r["member_qr_ids"].split(";") + r["member_na_ids"].split(";")) if x]
    us = units_of(ids)
    r["_units"] = us
    if not r["units_spanned"]:
        r["units_spanned"] = semi([PFX + x for x in us])
    for u in us:
        link(sid_, "SC", u, "indirect", "legal_constitution_evidenced" if all(
            (QRS[i]["epistemic_status"] if i in QRS else NAS[i]["epistemic_status"]) == "legal_constitution_evidenced" for i in ids) else "documented",
            "inherits weakest member status; grouping is analytical")
for aid, r in ARCHS.items():
    sc_ids = [x for x in r["member_sc_ids"].split(";") if x]
    qids = [x for x in r["i2_qr_ids"].split(";") if x]
    us = list(OrderedDict.fromkeys(sum([SCS[x].get("_units", []) for x in sc_ids if x in SCS], []) + units_of(qids) +
                                   [x.replace(PFX, "") for x in r["i1_scope_units"].split(";") if x]))
    r["_units"] = us
    for u in us:
        link(aid, "ARCH", u, "indirect", "documented", "assessment under I1-I4; machine-provisional")
for pid, r in PROPS.items():
    ids = [x for x in r["supporting_record_ids"].split(";") if x]
    us = units_of(ids)
    r["_units"] = us
    for u in us:
        link(pid, "PROP", u, "indirect", "documented", "property attributed by stated inference rule")
for cid, r in CLS.items():
    us = expand_units(r["_kv"].get("u", ""), r["_kv"]["_where"])
    r["_units"] = us
    for u in us:
        link(cid, "CL", u, "direct", "documented", "search/coverage statement")

for i, l in enumerate(LINKS, 1):
    l2 = OrderedDict(link_id=f"LNK-{i:05d}")
    l2.update(l)
    LINKS[i - 1] = l2

# ------------------------------------------------------------------ writers
def clean(r):
    return OrderedDict((k, v) for k, v in r.items() if not k.startswith("_"))


def write(name, rows, header=None):
    header = header or H[name]
    with open(os.path.join(OUT, name + ".csv"), "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, lineterminator="\r\n")
        w.writerow(header)
        for r in rows:
            w.writerow([r.get(h, "") for h in header])


inv_rows = []
for u in UORDER:
    x = U[u]
    inv_rows.append(OrderedDict(unit_id=x["unit_id"], case_id=CASE, structure_class=x["structure_class"],
                                article_or_annex_no=x["article_or_annex_no"], paragraph=x["paragraph"], point=x["point"],
                                parent_unit_id=x["parent_unit_id"], locator_text=x["locator_text"],
                                text_sha256=x["text_sha256"], source_anchor=x["source_anchor"]))

write("SOURCE_UNIT_INVENTORY", inv_rows)
write("UNIT_SCREENING", screen_rows)
write("INSTITUTIONAL_STATEMENTS", stmt_rows())
write("NORMATIVE_ASSIGNMENTS", [clean(r) for r in NAS.values()])
write("POSITIONS_AND_DEVICES", [clean(r) for r in PDS.values()])
write("QUALIFIED_RELATIONS", [clean(r) for r in QRS.values()])
write("EXTERNAL_REFERENCES", [clean(r) for r in EXTS.values()])
write("SUBCONFIGURATIONS", [clean(r) for r in SCS.values()])
write("ARCHITECTURE_CANDIDATES", [clean(r) for r in ARCHS.values()])
write("PROPERTY_REGISTER", [clean(r) for r in PROPS.values()])
write("CLOSURE_REGISTER", [clean(r) for r in CLS.values()])
write("PROVENANCE_LINKS", LINKS)
write("UNCERTAINTY_LOG", [clean(r) for r in UNCS.values()])
write("HUMAN_REVIEW_QUEUE", [clean(r) for r in HQS.values()])
write("TRACE_DEMONSTRATIONS", [clean(r) for r in TRS.values()])
write("PROTOCOL_DEVIATION_LOG", [clean(r) for r in DEVS.values()])
write("RUN_METADATA", [clean(r) for r in RUNS.values()])

# W_DECLARATION and INSTRUMENT_LEVEL_SUMMARY authored in rec/ as generic? -> separate json files
for nm in ("W_DECLARATION", "INSTRUMENT_LEVEL_SUMMARY"):
    jp = os.path.join(W, nm + ".json")
    if os.path.exists(jp):
        d = json.load(open(jp, encoding="utf-8"))
        write(nm, [OrderedDict((h, d.get(h, "")) for h in H[nm])])
    else:
        write(nm, [])

# ------------------------------------------------------------------ integrity checks (data dictionary section 4)
chk = []
allunits = set(PFX + u for u in UORDER)


def ids_in(spec):
    return [x for x in re.split(r"\s*;\s*", spec or "") if x]


def check_unit_refs(rows, cols, tname):
    for r in rows:
        for c in cols:
            for u in ids_in(r.get(c, "")):
                if u.startswith(PFX) and u not in allunits:
                    err(f"{tname}: unit id not in inventory: {u}")


# rule 1
check_unit_refs(screen_rows, ["unit_id"], "UNIT_SCREENING")
check_unit_refs([clean(r) for r in NAS.values()], ["supporting_unit_ids"], "NA")
check_unit_refs([clean(r) for r in QRS.values()], ["supporting_unit_ids"], "QR")
check_unit_refs([clean(r) for r in PDS.values()], ["supporting_unit_ids", "instance_source_unit_ids"], "PD")
check_unit_refs([clean(r) for r in EXTS.values()], ["supporting_unit_ids"], "EXT")
check_unit_refs(LINKS, ["unit_id"], "LINKS")
if len(screen_rows) != len(inv_rows):
    err("units_screened != units_total")
# rule 2
allST = set(ST.keys())
for pid, p in PDS.items():
    if not p["_sts"]:
        err(f"{pid}: PD without ST")
for tbl, nm, col in ((NAS, "NA", "statement_ids"), (QRS, "QR", "statement_ids")):
    for k, r in tbl.items():
        if not r[col]:
            err(f"{k}: no ST")
        for s in ids_in(r[col]):
            if s not in allST:
                err(f"{k}: ST {s} missing")
            elif ST[s].get("ro", "N") == "Y":
                err(f"{k}: derived from recital-only statement")
for k, e in EXTS.items():
    if not e["_sts"]:
        err(f"{k}: EXT without ST")
# rule 3 referential resolution (PD ids)
for k, r in NAS.items():
    for c in ("subject_pd_id", "depends_on_pd_ids"):
        for x in ids_in(r[c]):
            if x not in PDS:
                err(f"{k}: {c} {x} unresolved")
for k, r in QRS.items():
    for c in ("origin_pd_id", "counterpart_pd_id", "additional_party_pd_ids", "depends_on_pd_ids"):
        for x in ids_in(r[c]):
            if x not in PDS:
                err(f"{k}: {c} {x} unresolved")
    for x in ids_in(r["accountable_via_qr_ids"]):
        if x not in QRS or QRS[x]["relation_type"] != "accountability":
            err(f"{k}: accountable_via {x} not an accountability QR")
    for x in ids_in(r["external_ref_ids"]):
        if x not in EXTS:
            err(f"{k}: ext {x} unresolved")
# rule 4
for k, r in QRS.items():
    if not r["origin_pd_id"] or not r["counterpart_pd_id"]:
        err(f"{k}: QR missing party")
    if r["modality"] == "prohibition":
        err(f"{k}: QR with prohibition modality")
    if r["epistemic_status"] in ("material_establishment_evidenced",):
        err(f"{k}: QR with material_establishment_evidenced")
    if r["relation_type"] not in set(RT.values()):
        err(f"{k}: relation_type invalid {r['relation_type']!r}")
    if r["function"] not in FNALL:
        err(f"{k}: function invalid {r['function']!r}")
    if r["legal_status_of_norm"] not in LS_ALL or r["epistemic_status"] not in EP_ALL:
        err(f"{k}: status invalid")
    if r["modality"] not in set(MOD.values()):
        err(f"{k}: modality invalid")
for k, r in NAS.items():
    if r["function"] not in FNALL:
        err(f"{k}: function invalid {r['function']!r}")
    if r["modality"] not in set(MOD.values()):
        err(f"{k}: modality invalid")
    if r["norm_type"] not in NTALL:
        err(f"{k}: norm_type invalid {r['norm_type']!r}")
    if r["legal_status_of_norm"] not in LS_ALL or r["epistemic_status"] not in EP_ALL:
        err(f"{k}: status invalid")
    if r["counterpart_status"] not in ("NONE_IDENTIFIABLE", "IN_PROVISION", "BY_EXPLICIT_CROSS_REFERENCE"):
        err(f"{k}: counterpart_status invalid")
    if r["counterpart_status"] == "NONE_IDENTIFIABLE" and r["counterpart_if_identifiable"] and r["modality"] != "prohibition":
        err(f"{k}: counterpart text given with NONE_IDENTIFIABLE (invented counterparty?)")
for k, r in PDS.items():
    if r["kind"] not in ("POSITION", "DEVICE"):
        err(f"{k}: kind")
    if r["kind"] == "DEVICE" and r["device_classification"] not in ("INS-TYPE", "DEV", "BORDERLINE_INS-TYPE"):
        err(f"{k}: device classification missing")
    if r["epistemic_status"] not in EP_ALL:
        err(f"{k}: epistemic invalid")
# rule 5
prov = defaultdict(int)
for l in LINKS:
    prov[l["record_id"]] += 1
for tbl in (NAS, QRS, SCS, ARCHS, PROPS):
    for k in tbl:
        if prov[k] == 0:
            err(f"{k}: no provenance link")
for tbl, nm in ((NAS, "NA"), (QRS, "QR")):
    for k, r in tbl.items():
        if r["derivation"] == "derived":
            if not r["derivation_rule"]:
                err(f"{k}: derived without rule")
            if len(r["_units"]) < 2 and "cross-ref" not in r["derivation_rule"].lower():
                err(f"{k}: derived with <2 units and no explicit cross-reference statement in rule")
        elif r["derivation"] != "direct":
            err(f"{k}: derivation invalid")
# rule 6
for k, r in ARCHS.items():
    if r["outcome"] in ("INTEGRATED", "OVERLAPPING_OR_PARTIALLY_INTEGRATED") and not r["hq_ids"]:
        err(f"{k}: INTEGRATED/OVERLAPPING without HQ")
    if r["outcome"] == "INTEGRATED" and not all(r[c] == "SATISFIED" for c in ("i1_status", "i2_status", "i3_status", "i4_status")):
        err(f"{k}: INTEGRATED without all SATISFIED")
    if r["outcome"] not in ("INTEGRATED", "DISTINGUISHABLE", "OVERLAPPING_OR_PARTIALLY_INTEGRATED", "INDETERMINATE"):
        err(f"{k}: outcome invalid")
# rule 7
for k, r in PROPS.items():
    if r["closure_dependency"] == "Y":
        cr = r["closure_ref"]
        if cr not in CLS:
            err(f"{k}: closure_ref unresolved")
        elif CLS[cr]["result"] == "UNDETERMINED" and r["status"] != "undetermined":
            err(f"{k}: closure UNDETERMINED but status {r['status']}")
# rule 8
for k, r in EXTS.items():
    if r["source_verification_status"] != "not_checked":
        err(f"{k}: verification")
    if r["boundary_status"] != "outside_corpus_not_expanded":
        err(f"{k}: boundary")
# rule 9
for k, r in HQS.items():
    for h in ("human_decision", "human_rationale", "decided_by", "decision_date"):
        if r[h]:
            err(f"{k}: human column not blank")
# rule 10 (trace) -- checked in verify step below
for k, r in TRS.items():
    pass

# every HQ referenced exists / unc referenced exists
for tbl in (PDS, NAS, QRS, SCS, ARCHS, PROPS):
    for k, r in tbl.items():
        for h in ids_in(r.get("hq_ids", "")):
            if h not in HQS:
                err(f"{k}: hq {h} missing")
        for u in ids_in(r.get("uncertainty_ids", "")):
            if u not in UNCS:
                err(f"{k}: unc {u} missing")

summary = OrderedDict(units=len(UORDER), ST=len(ST), PD=len(PDS), NA=len(NAS), QR=len(QRS), EXT=len(EXTS), SC=len(SCS),
                      ARCH=len(ARCHS), PROP=len(PROPS), CL=len(CLS), UNC=len(UNCS), HQ=len(HQS), LINKS=len(LINKS),
                      TR=len(TRS), DEV=len(DEVS))
with open(os.path.join(OUT, "CHECK.txt"), "w", encoding="utf-8") as f:
    f.write(json.dumps(summary) + "\n")
    f.write(f"ERRORS {len(errors)}\n")
    for e in errors:
        f.write("E " + e + "\n")
    f.write(f"WARNINGS {len(warnings)}\n")
    for e in warnings:
        f.write("W " + e + "\n")
json.dump({"labels": labels}, open(os.path.join(W, "labels.json"), "w", encoding="utf-8"), indent=0)
print(json.dumps(summary))
print("errors:", len(errors), "warnings:", len(warnings))
for e in errors[:int(sys.argv[1]) if len(sys.argv) > 1 else 40]:
    print("E", e)
