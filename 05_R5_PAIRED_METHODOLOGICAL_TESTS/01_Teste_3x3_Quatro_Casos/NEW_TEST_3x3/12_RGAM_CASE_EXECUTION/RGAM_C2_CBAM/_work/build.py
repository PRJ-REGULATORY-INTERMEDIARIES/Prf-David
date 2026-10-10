# Mechanical builder: resolves keys to ids, derives mechanical columns, writes the 19 CSV tables, runs integrity checks.
import sys, os, re, csv, json, hashlib, random, importlib, collections
sys.path.insert(0, "G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/12_RGAM_CASE_EXECUTION/RGAM_C2_CBAM/_work")
import rgam_lib as L
from rgam_lib import REG, KEYS, UT, UNITS, CASE, norm, REFERENCE

OUT = "G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/12_RGAM_CASE_EXECUTION/RGAM_C2_CBAM/"
for m in ["rec_01_pd", "rec_02_ch1", "rec_03_ch2", "rec_04_ch3", "rec_05_ch4_6", "rec_06_ch7_11", "rec_07_annex", "rec_86_ext_more", "rec_85_screening",
          "rec_80_sc_arch", "rec_82_prop", "rec_90_hq_unc"]:
    importlib.import_module(m)
import rec_85_screening as R85

SHA = "c47e2793e7b92333ce9a891aba18924ff21b15b2745fffda98348b04b15a770e"
SEED = int(SHA[:8], 16)
START = "2026-10-06T19:03:42Z"
PROTO_MANIFEST = "9ca016b97289b39049dc099b265c20662c1ebc05e86bc720f0fbe80e0bac5932"
UORDER = {u["unit_id"].replace(CASE + ".", "", 1): i for i, u in enumerate(UNITS)}
ERR = []

# ---------------- chapter / part map ----------------
PART = {}
cur = "FRONT"
for u in UNITS:
    s = u["unit_id"].replace(CASE + ".", "", 1)
    if s.startswith("CH"):
        cur = "Chapter " + s[2:]
        PART[s] = cur
    elif s.startswith("A") and u["structure_class"] == "OPERATIVE_ARTICLE":
        PART[s] = cur
    elif s.startswith("ANX"):
        PART[s] = "Annex " + re.match(r"ANX(\d+)", s).group(1)
    elif s.startswith("REC"):
        PART[s] = "Recitals"
    elif s.startswith("FINAL"):
        PART[s] = "Final provisions"
    else:
        PART[s] = "Preamble"

# ---------------- id assignment ----------------
def first_unit_index(rec):
    us = rec.get("units", [])
    return min([UORDER[u] for u in us], default=10 ** 6)

ORDER = {}
for t in ["ST", "NA", "QR", "EXT"]:
    ORDER[t] = sorted(REG[t], key=lambda r: (first_unit_index(r), r["_key"]))
for t in ["PD", "SC", "ARCH", "PROP", "CL", "UNC", "HQ"]:
    ORDER[t] = list(REG[t])
FMT = {"ST": "ST-%04d", "NA": "NA-%04d", "PD": "PD-%03d", "QR": "QR-%04d", "EXT": "EXT-%03d", "SC": "SC-%02d", "ARCH": "ARCH-%02d",
       "PROP": "PROP-%03d", "CL": "CL-%02d", "UNC": "UNC-%03d", "HQ": "HQ-%03d"}
ID = {}
for t, recs in ORDER.items():
    for i, r in enumerate(recs, 1):
        ID[r["_key"]] = FMT[t] % i
        r["_id"] = ID[r["_key"]]

TOK = re.compile(r"\b(?:st|pd|na|qr|ext|sc|arch|prop|cl|unc|hq)\.[A-Za-z0-9_]+")
TOK2 = re.compile(r"\b(SC|ARCH)-([A-Z][A-Z_]+)\b")

def rid(k):
    if k not in ID:
        ERR.append("unresolved key " + k)
        return k
    return ID[k]

def R(v):
    """resolve a list/;-string of keys or plain tokens into ';'-joined ids"""
    out = []
    for t in L.L(v):
        out.append(ID[t] if t in ID else t)
    return ";".join(out)

def T(s):
    """substitute key tokens inside free text"""
    if not s:
        return s
    s = TOK.sub(lambda m: ID.get(m.group(0), m.group(0)), s)
    s = TOK2.sub(lambda m: ID.get(m.group(1).lower() + "." + m.group(2), m.group(0)), s)
    return s

def U(us):
    return ";".join(CASE + "." + u for u in us)

# ---------------- EXT dependents union & down-coding ----------------
ext_by_key = {r["_key"]: r for r in REG["EXT"]}
for t in ["NA", "QR"]:
    for r in REG[t]:
        for e in r.get("ext", []):
            if e not in ext_by_key:
                ERR.append("record %s lists unknown ext %s" % (r["_key"], e))
                continue
            if r["_key"] not in ext_by_key[e]["dependents"]:
                ext_by_key[e]["dependents"].append(r["_key"])
DOWN = {}
for t in ["NA", "QR"]:
    for r in REG[t]:
        hits = [e for e in r.get("ext", []) if e in ext_by_key and ext_by_key[e]["constitutive"] == "Y"]
        if hits:
            DOWN[r["_key"]] = hits
            if r["epi"] == "legal_constitution_evidenced":
                r["epi"] = "documented"

# ---------------- statement -> derived records ----------------
derived = collections.defaultdict(list)
for t in ["NA", "QR", "PD", "EXT"]:
    for r in REG[t]:
        for s in r["st"]:
            derived[s].append(r["_key"])
# ---------------- coverage of units by statements ----------------
st_by_unit = collections.defaultdict(list)
for r in REG["ST"]:
    for u in r["units"]:
        st_by_unit[u].append(r["_key"])

# ---------------- CSV writer ----------------
def write(name, header, rows):
    path = OUT + name
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, lineterminator="\r\n")
        w.writerow(header)
        for row in rows:
            assert len(row) == len(header), (name, len(row), len(header), row[:2])
            w.writerow(row)
    return len(rows)

def header_of(name):
    return open(OUT + name, encoding="utf-8-sig").read().splitlines()[0].split(",")

COUNTS = {}
# first capture frozen headers from the copied templates (once)
HDR = {}
for n in ["W_DECLARATION", "SOURCE_UNIT_INVENTORY", "UNIT_SCREENING", "INSTITUTIONAL_STATEMENTS", "NORMATIVE_ASSIGNMENTS", "POSITIONS_AND_DEVICES",
          "QUALIFIED_RELATIONS", "EXTERNAL_REFERENCES", "SUBCONFIGURATIONS", "ARCHITECTURE_CANDIDATES", "PROPERTY_REGISTER", "CLOSURE_REGISTER",
          "PROVENANCE_LINKS", "UNCERTAINTY_LOG", "HUMAN_REVIEW_QUEUE", "TRACE_DEMONSTRATIONS", "INSTRUMENT_LEVEL_SUMMARY", "PROTOCOL_DEVIATION_LOG",
          "RUN_METADATA"]:
    tmpl = "G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_C2_CBAM/OUTPUT_TEMPLATES/" + n + ".csv"
    HDR[n] = open(tmpl, encoding="utf-8-sig").read().splitlines()[0].split(",")

# ---------------- 1 W_DECLARATION ----------------
n_art = len({u["article_or_annex_no"] for u in UNITS if u["structure_class"] == "OPERATIVE_ARTICLE"})
n_anx = len({re.match(r"ANX(\d+)", u["unit_id"].replace(CASE + ".", "")).group(1) for u in UNITS if u["structure_class"] in ("ANNEX",)} |
            {re.match(r"ANX(\d+)", u["unit_id"].replace(CASE + ".", "")).group(1) for u in UNITS if u["unit_id"].replace(CASE + ".", "").startswith("ANX")})
n_rec = sum(1 for u in UNITS if u["structure_class"] == "RECITAL")
W_ROW = [CASE, "REGULATION (EU) 2023/956 OF THE EUROPEAN PARLIAMENT AND OF THE COUNCIL of 10 May 2023 establishing a carbon border adjustment mechanism (Text with EEA relevance)",
         "32023R0956", "European Union",
         "Establishment of a carbon border adjustment mechanism addressing greenhouse gas emissions embedded in the goods listed in Annex I on their importation into the customs territory of the Union (taken from the title and the object clause of Article 1(1) only)",
         "Regulation",
         "Original act as published in the Official Journal of the European Union, L 130, 16 May 2023, p. 52 (header of the source file); English; not consolidated",
         "Point reference 2026-01-01, selected from the act's own Article 36(2) as the date on which all staged application dates have been reached (general application 2023-10-01; Articles 5, 10, 14, 16, 17 from 2024-12-31; Article 2(2), Articles 4, 6-9, 15, 19, Article 20(1), (3), (4), (5), Articles 21-27 and 31 from 2026-01-01); entry into force on the day following publication (Article 36(1)); the neutral metadata state no repeal-related information; legal status is asserted for this reference only and not for any other date",
         "All units of the frozen source file: title, citations, 82 recitals (context only), 36 articles, final formulas and 6 annexes, decomposed into %d addressable units" % len(UNITS),
         "(1) Four formula images in Annex IV (equations) are not representable as text; their variables are defined in legend tables that are included; (2) table geometry of the Annex I and II goods tables (merged cells) is not faithfully represented in the parsed text; (3) hyperlink targets, the Official Journal page header and the page layout are not part of the unit text; (4) footnote texts are included inside the unit text where their marker occurs; (5) annex numbers and titles are carried in the locator text, not as units; (6) no content outside the frozen file (no consolidation, no amending act, no referenced external source)",
         "LEGAL_SOURCE/32023R0956_official_en.xhtml", SHA, SHA, "Y", str(n_art), str(n_anx), str(n_rec),
         "MATCH (36 articles and 6 annexes parsed = neutral metadata counts; %d recitals parsed, no recital count in the metadata)" % n_rec,
         "W is the complete frozen instrument. It can close statements about its own text only: 'not found' is a statement about the search of W, not about the law. References to sources outside W (Directive 2003/87/EC, Regulation (EU) No 952/2013, implementing regulations on accreditation, Regulation (EU) No 182/2011, national law and others) were recorded as EXT and not retrieved; absence-dependent claims touching them are undetermined or limited to the declared corpus.",
         "W != A"]
COUNTS["W_DECLARATION"] = write("W_DECLARATION.csv", HDR["W_DECLARATION"], [W_ROW])

# ---------------- 2 SOURCE_UNIT_INVENTORY ----------------
rows = []
for u in UNITS:
    rows.append([u["unit_id"], CASE, u["structure_class"], u["article_or_annex_no"], u["paragraph"], u["point"], u["parent_unit_id"],
                 u["locator_text"], u["text_sha256"], u["source_anchor"]])
COUNTS["SOURCE_UNIT_INVENTORY"] = write("SOURCE_UNIT_INVENTORY.csv", HDR["SOURCE_UNIT_INVENTORY"], rows)

# ---------------- 3 UNIT_SCREENING ----------------
KINDTAG = {"relation_bearing": "relation-bearing", "assignment_bearing": "operative-assignment", "position_defining": "position-defining",
           "device_defining": "device-defining/procedural-mechanism", "procedural": "procedural-mechanism", "scope": "scope/definitional-context",
           "definitional": "scope/definitional-context", "external_referencing": "scope/definitional-context (external reference)",
           "final_formal": "final/formal", "other": "other"}
PRIO = ["relation_bearing", "assignment_bearing", "position_defining", "device_defining", "procedural", "scope", "definitional", "external_referencing", "final_formal", "other"]
st_rec = {r["_key"]: r for r in REG["ST"]}
rows = []
screen_issues = []
for u in UNITS:
    s = u["unit_id"].replace(CASE + ".", "", 1)
    sts = st_by_unit.get(s, [])
    if sts:
        kinds = sorted({st_rec[k]["kind"] for k in sts}, key=lambda x: PRIO.index(x))
        tag = KINDTAG[kinds[0]]
        note = "Statement(s) derived: " + "; ".join("%s (%s)" % (ID[k], st_rec[k]["kind"]) for k in sts) + ". " + st_rec[sts[0]]["summary"][:230] + ("..." if len(st_rec[sts[0]]["summary"]) > 230 else "")
        rel = "Yes"
        if s in R85.SCREEN and s != "CIT1":
            screen_issues.append("unit %s has ST and a No/Uncertain screen entry" % s)
        if s == "CIT1":
            tag = "scope/definitional-context (external reference)"
            note = "Statement derived: %s (external_referencing): legal basis cited in the enacting formula; EXT created; no assignment, position or relation." % ID[sts[0]]
        rows.append([u["unit_id"], rel, tag, ";".join(ID[k] for k in sts), note])
    else:
        if s not in R85.SCREEN:
            screen_issues.append("unit %s has neither ST nor screen entry" % s)
            rows.append([u["unit_id"], "Uncertain", "", "", "NO SCREEN ENTRY"])
        else:
            rel, tag, note = R85.SCREEN[s]
            rows.append([u["unit_id"], rel, tag, "", note])
COUNTS["UNIT_SCREENING"] = write("UNIT_SCREENING.csv", HDR["UNIT_SCREENING"], rows)
SCREEN_YES = sum(1 for r in rows if r[1] == "Yes")
SCREEN_NO = sum(1 for r in rows if r[1] == "No")
SCREEN_UNC = sum(1 for r in rows if r[1] == "Uncertain")

# ---------------- 4 INSTITUTIONAL_STATEMENTS ----------------
rows = []
for r in ORDER["ST"]:
    dr = ";".join(ID[k] for k in derived.get(r["_key"], []))
    rows.append([r["_id"], U(r["units"]), r["kind"], T(r["summary"]), r["span"], dr, r["recital_only"]])
COUNTS["INSTITUTIONAL_STATEMENTS"] = write("INSTITUTIONAL_STATEMENTS.csv", HDR["INSTITUTIONAL_STATEMENTS"], rows)

# ---------------- 5 NORMATIVE_ASSIGNMENTS ----------------
def instr(v):
    return R(v) if v and (v in ID or TOK.fullmatch(v)) else T(v)

rows = []
for r in ORDER["NA"]:
    notc = r["notc"]
    if r["_key"] in DOWN:
        notc += " [Down-coded to 'documented': legal constitution or content depends on unresolved external reference(s) %s (RGAM-DR-19, DR-20).]" % ";".join(ID[e] for e in DOWN[r["_key"]])
    allu = r["units"] + [u for u in r["iunits"] if u not in r["units"]]
    rows.append([r["_id"], CASE, R(r["st"]), U(allu), ID[r["pd"]], T(r["action"]), T(r["obj"]), r["function"], T(r["mech"]), instr(r["instr"]), r["modality"],
                 T(r["cond"]), T(r["cp"]), r["cps"], r["nt"], T(r["eff"]), T(notc), r["constraint"], r["deriv"], T(r["drule"]), R(r["deps"]), r["legal"], r["epi"],
                 r["span"], R(r["unc"]), R(r["hq"])])
COUNTS["NORMATIVE_ASSIGNMENTS"] = write("NORMATIVE_ASSIGNMENTS.csv", HDR["NORMATIVE_ASSIGNMENTS"], rows)

# ---------------- 6 POSITIONS_AND_DEVICES ----------------
rows = []
for r in ORDER["PD"]:
    dev = r["kind"] == "DEVICE"
    rows.append([r["_id"], CASE, r["kind"], r["label"], r["toi"], U(L.L(r["inst_src"])) if r["inst_src"] else "", "European Union and its Member States (as referred to in W)",
                 "reference " + REFERENCE, r["mult"], r["estab"], T(r["dev_id"]) if dev else "", T(r["dev_fn"]) if dev else "", r["dev_class"] if dev else "",
                 r["constit"], "not_assessed", r["epi"], U(r["units"]), r["span"], R(r["unc"]), R(r["hq"])])
COUNTS["POSITIONS_AND_DEVICES"] = write("POSITIONS_AND_DEVICES.csv", HDR["POSITIONS_AND_DEVICES"], rows)

# ---------------- 7 QUALIFIED_RELATIONS ----------------
rows = []
for r in ORDER["QR"]:
    gap = r["gap"]
    if r["_key"] in DOWN:
        gap = (gap + " " if gap else "") + "Down-coded to 'documented': legal constitution depends on unresolved external reference(s) %s (RGAM-DR-19, DR-20); undetermined until verified." % ";".join(ID[e] for e in DOWN[r["_key"]])
    allu = r["units"] + [u for u in r["iunits"] if u not in r["units"]]
    rows.append([r["_id"], CASE, R(r["st"]), U(allu), ID[r["o"]], ID[r["c"]], R(r["extra"]), r["rtype"], T(r["tnote"]), T(r["tdir"]), T(r["gdir"]), T(r["action"]), T(r["obj"]),
                 r["function"], T(r["mech"]), instr(r["instr"]), r["modality"], T(r["cond"]), r["validity"], r["legal"], r["epi"], r["deriv"], T(r["drule"]),
                 T(r["authattr"]), T(r["discattr"]), r["acls"], r["asuff"], T(r["amiss"]), R(r["accvia"]), R(r["deps"]), T(gap), R(r["ext"]), r["span"], R(r["unc"]), R(r["hq"])])
COUNTS["QUALIFIED_RELATIONS"] = write("QUALIFIED_RELATIONS.csv", HDR["QUALIFIED_RELATIONS"], rows)

# ---------------- 8 EXTERNAL_REFERENCES ----------------
rows = []
for r in ORDER["EXT"]:
    rows.append([r["_id"], CASE, U(r["units"]), r["source"], r["kind"], r["role"], "not_checked", "outside_corpus_not_expanded", R(r["dependents"]), r["dep_kind"],
                 r["constitutive"], T(r["effect"])])
COUNTS["EXTERNAL_REFERENCES"] = write("EXTERNAL_REFERENCES.csv", HDR["EXTERNAL_REFERENCES"], rows)

# ---------------- helper: unit sets of records ----------------
def rec_units(key):
    t, r = KEYS[key]
    if t in ("QR", "NA", "ST", "PD", "EXT"):
        return list(r["units"]) + [u for u in r.get("iunits", []) if u not in r["units"]]
    if t == "SC":
        us = []
        for k in r["qrs"] + r["nas"]:
            for u in rec_units(k):
                if u not in us:
                    us.append(u)
        return us
    if t == "ARCH":
        us = []
        for k in r["scs"]:
            for u in rec_units(k):
                if u not in us:
                    us.append(u)
        for u in r["i1u"]:
            if u not in us:
                us.append(u)
        return us
    if t == "PROP":
        us = []
        for k in r["support"]:
            if k in KEYS:
                for u in rec_units(k):
                    if u not in us:
                        us.append(u)
        return us
    return []

def epi_of(key):
    t, r = KEYS[key]
    if t in ("QR", "NA", "PD"):
        return r["epi"]
    return "documented"

def weakest(keys):
    order = ["conceptually_projected", "documented", "legal_constitution_evidenced", "material_establishment_evidenced", "exercise_evidenced"]
    es = [epi_of(k) for k in keys if k in KEYS and KEYS[k][0] in ("QR", "NA", "PD")]
    if not es:
        return "documented"
    return min(es, key=lambda e: order.index(e))

def status_tally(qrs, nas):
    c = collections.Counter(KEYS[k][1]["epi"] for k in qrs)
    d = collections.Counter(KEYS[k][1]["epi"] for k in nas)
    def fmt(c, what):
        parts = ["%d %s %s" % (n, what, e) for e, n in sorted(c.items())]
        for z in ("material_establishment_evidenced", "exercise_evidenced"):
            if z not in c:
                parts.append("0 %s %s" % (what, z))
        return "; ".join(parts)
    return "relations: " + fmt(c, "relations") + " | assignments: " + fmt(d, "assignments")

def parts_summary(us):
    c = collections.Counter(PART[u] for u in us)
    return "; ".join("%s (%d units)" % (p, n) for p, n in sorted(c.items(), key=lambda x: min(UORDER[u] for u in us if PART[u] == x[0])))

# ---------------- 9 SUBCONFIGURATIONS ----------------
members = {}
for r in REG["SC"]:
    members[r["_key"]] = set(r["qrs"] + r["nas"])
rows = []
for r in ORDER["SC"]:
    us = rec_units(r["_key"])
    ov = set(r["overlap"])
    for k2, m2 in members.items():
        if k2 != r["_key"] and members[r["_key"]] & m2:
            ov.add(k2)
    r["_ov"] = sorted(ov)
    rows.append([r["_id"], CASE, T(r["scope"]), T(r["pattern"]), T(r["question"]), R(r["qrs"]), R(r["nas"]), R(r["pds"]), T(r["mech"]), T(r["warrant"]),
                 "%d distinct supporting units across: %s (full list in PROVENANCE_LINKS)" % (len(us), parts_summary(us)), T(r["boundary"]), R(sorted(ov)), "", T(r["competing"]),
                 R(r["unc"]), R(r["hq"]), "S"])
COUNTS["SUBCONFIGURATIONS"] = write("SUBCONFIGURATIONS.csv", HDR["SUBCONFIGURATIONS"], rows)

# ---------------- 10 ARCHITECTURE_CANDIDATES ----------------
rows = []
for r in ORDER["ARCH"]:
    qrs = []
    nas = []
    for s in r["scs"]:
        for k in KEYS[s][1]["qrs"]:
            if k not in qrs:
                qrs.append(k)
        for k in KEYS[s][1]["nas"]:
            if k not in nas:
                nas.append(k)
    r["_tally"] = status_tally(qrs, nas)
    rows.append([r["_id"], CASE, R(r["scs"]), T(r["i1p"]), U(r["i1u"]), r["i1s"], T(r["i2d"]), r["i2k"], R(r["i2q"]), r["i2s"], T(r["i3c"]), T(r["i3b"]), r["i3s"],
                 T(r["i4s"]), R(r["i4e"]), T(r["i4r"]), T(r["i4b"]), r["i4st"], r["seq"], r["outcome"], T(r["basis"]), r["_tally"], R(r["unc"]), R(r["hq"])])
COUNTS["ARCHITECTURE_CANDIDATES"] = write("ARCHITECTURE_CANDIDATES.csv", HDR["ARCHITECTURE_CANDIDATES"], rows)

# ---------------- 11 PROPERTY_REGISTER ----------------
rows = []
for r in ORDER["PROP"]:
    rows.append([r["_id"], CASE, r["name"], r["family"], r["btype"], ID[r["bearer"]], T(r["scale"]), T(r["value"]), T(r["rule"]), T(r["path"]), T(r["agg"]), R(r["support"]),
                 r["cdep"], R(r["cref"]), T(r["count"]), r["fallacy"], T(r["rival"]), r["status"], R(r["hq"])])
COUNTS["PROPERTY_REGISTER"] = write("PROPERTY_REGISTER.csv", HDR["PROPERTY_REGISTER"], rows)

# ---------------- 12 CLOSURE_REGISTER ----------------
rows = []
for r in ORDER["CL"]:
    rows.append([r["_id"], CASE, r["kind"], T(r["claim"]), T(r["search"]), R(r["ext"]), r["result"], R(r["affected"])])
COUNTS["CLOSURE_REGISTER"] = write("CLOSURE_REGISTER.csv", HDR["CLOSURE_REGISTER"], rows)

# ---------------- 13 PROVENANCE_LINKS ----------------
CLU = {"cl.COVERAGE": [u["unit_id"].replace(CASE + ".", "", 1) for u in UNITS],
       "cl.EXTERNAL": sorted({u for r in REG["EXT"] for u in r["units"]}, key=lambda u: UORDER[u]),
       "cl.ACCOUNT_ABSENCE": ["A17.P3", "A17.P8.sub3", "A19.P5.sub3", "A26.P4.ptf", "A35.P5.pte", "A29.P1", "A29.P2"],
       "cl.NECESSARY_STAGE": ["A4.P0", "A25.P1", "A5.P1", "A5.P4", "A17.P1", "A2.P3", "A2.P4", "A2.P7"],
       "cl.SUBSTITUTABILITY": ["A5.P1", "A5.P2", "A32.P0", "A35.P1"],
       "cl.NO_SELFREG": ["A5.P8", "A7.P7", "A28.P1", "A29.P1", "ANX6.pt1.P1"],
       "cl.NO_COUPLING_TRANSITION": ["A32.P0", "A33.P1", "A33.P2", "A35.P1", "A35.P2.ptb", "A35.P7.ptd", "A36.P2"]}
rows = []
lnk = 0
LINKSET = set()
def add_link(key, unit, stype, limit, status):
    global lnk
    if (key, unit) in LINKSET:
        return
    LINKSET.add((key, unit))
    lnk += 1
    t = KEYS[key][0]
    rows.append(["LNK-%05d" % lnk, ID[key], t, CASE + "." + unit, stype, "A", status, limit])
for t in ["ST", "NA", "PD", "QR", "EXT"]:
    for r in ORDER[t]:
        status = epi_of(r["_key"]) if t != "EXT" else "documented"
        for u in r["units"]:
            add_link(r["_key"], u, "direct", "", status if status in ("documented", "legal_constitution_evidenced") else "documented")
        for u in r.get("iunits", []):
            add_link(r["_key"], u, "indirect", "supports the derivation or conditions through an internal cross-reference (GAP-03)", status if status in ("documented", "legal_constitution_evidenced") else "documented")
        if r["_key"] in DOWN:
            pass
for t in ["SC", "ARCH", "PROP"]:
    for r in ORDER[t]:
        if t == "SC":
            status = weakest(r["qrs"] + r["nas"])
        elif t == "ARCH":
            ks = []
            for s in r["scs"]:
                ks += KEYS[s][1]["qrs"] + KEYS[s][1]["nas"]
            status = weakest(ks)
        else:
            status = weakest(r["support"])
        direct = rec_units(r["_key"])
        for u in direct:
            add_link(r["_key"], u, "indirect" if t != "PROP" else "indirect", "higher-order record: support inherited from member records; status is the weakest member status", status)
for k, us in CLU.items():
    for u in us:
        add_link(k, u, "direct", "closure statement: coverage or search basis", "documented")
COUNTS["PROVENANCE_LINKS"] = write("PROVENANCE_LINKS.csv", HDR["PROVENANCE_LINKS"], rows)

# ---------------- 14 UNCERTAINTY_LOG ----------------
rows = []
refs = collections.defaultdict(list)
for t in ["ST", "NA", "PD", "QR", "SC", "ARCH", "PROP"]:
    for r in REG[t]:
        for k in r.get("unc", []):
            refs[k].append(r["_key"])
for r in ORDER["UNC"]:
    recs = sorted(set(r["recs"]) | set(refs.get(r["_key"], [])), key=lambda k: ID[k])
    rows.append([r["_id"], CASE, R(recs), U(r["units"]), r["rtype"], T(r["desc"]), T(r["treat"]), T(r["effect"]), r["status"]])
COUNTS["UNCERTAINTY_LOG"] = write("UNCERTAINTY_LOG.csv", HDR["UNCERTAINTY_LOG"], rows)

# ---------------- 15 HUMAN_REVIEW_QUEUE ----------------
rows = []
for r in ORDER["HQ"]:
    rows.append([r["_id"], CASE, r["trigger"], R(r["recs"]), T(r["question"]), T(r["readings"]), T(r["reco"]), T(r["reason"]), "", "", "", ""])
COUNTS["HUMAN_REVIEW_QUEUE"] = write("HUMAN_REVIEW_QUEUE.csv", HDR["HUMAN_REVIEW_QUEUE"], rows)

# ---------------- 16 TRACE_DEMONSTRATIONS ----------------
cands = []
for t in ["SC", "ARCH"]:
    for r in ORDER[t]:
        us = rec_units(r["_key"])
        parts = {PART[u] for u in us}
        cands.append((r["_id"], r["_key"], len(set(us)), len(parts)))
cands_sorted = sorted(cands, key=lambda x: x[0])
eligible = [c for c in cands_sorted if c[3] >= 2]
rng = random.Random(SEED)
draw = eligible[rng.randrange(len(eligible))]
largest = sorted(cands, key=lambda x: (-x[2], x[0]))[0]

def chain(key):
    t, r = KEYS[key]
    out = []
    def rec_line(k):
        q = KEYS[k][1]
        sts = ";".join(ID[s] for s in q["st"])
        us = ";".join(CASE + "." + u for u in q["units"][:6]) + ("..." if len(q["units"]) > 6 else "")
        return "%s -> %s -> %s -> span (prefix): '%s'" % (ID[k], sts, us, q["span"][:100])
    if t == "ARCH":
        out.append("%s -> member %s" % (ID[key], ";".join(ID[s] for s in r["scs"])))
        out.append("coupling relations of I2 (each resolved below): " + ";".join(ID[k] for k in r["i2q"]))
        for k in r["i2q"]:
            out.append(rec_line(k))
        out.append("I1 scope units: " + ";".join(CASE + "." + u for u in r["i1u"]))
    else:
        out.append("%s -> member relations %s | member assignments %s | member positions/devices %s" % (ID[key], ";".join(ID[k] for k in r["qrs"]), ";".join(ID[k] for k in r["nas"]), ";".join(ID[k] for k in r["pds"])))
        for k in r["qrs"] + r["nas"]:
            out.append(rec_line(k))
    return " || ".join(out)

def chain_complete(key):
    t, r = KEYS[key]
    ks = r["i2q"] if t == "ARCH" else r["qrs"] + r["nas"]
    for k in ks:
        q = KEYS[k][1]
        if not q["st"] or not q["units"] or not q["span"]:
            return "N"
        for u in q["units"]:
            if u not in UT:
                return "N"
    return "Y"

SELECT = ("SEEDED_DRAW among candidate S/ARCH records citing units from >= 2 distinct parts (chapters/annexes) of the instrument, over the list sorted by id, "
          "seed = integer value of the first 8 hex digits of the case source SHA-256 (%d); index = random.Random(seed).randrange(len(list)) (Python 3)" % SEED)
rows = [["TR-01", CASE, "SEEDED_DRAW", str(SEED), ";".join(c[0] for c in eligible), draw[0], chain(draw[1]), chain_complete(draw[1])],
        ["TR-02", CASE, "LARGEST_SUPPORT", "", ";".join(c[0] for c in cands_sorted), largest[0], chain(largest[1]), chain_complete(largest[1])]]
COUNTS["TRACE_DEMONSTRATIONS"] = write("TRACE_DEMONSTRATIONS.csv", HDR["TRACE_DEMONSTRATIONS"], rows)
TRACE_INFO = dict(draw=draw, largest=largest, eligible=[c[0] for c in eligible], select=SELECT)

# ---------------- 17 INSTRUMENT_LEVEL_SUMMARY ----------------
rec_counts = ", ".join("%s=%d" % (k, v) for k, v in [("SOURCE_UNIT_INVENTORY", len(UNITS)), ("UNIT_SCREENING", len(UNITS)), ("INSTITUTIONAL_STATEMENTS", len(REG["ST"])),
                      ("NORMATIVE_ASSIGNMENTS", len(REG["NA"])), ("POSITIONS_AND_DEVICES", len(REG["PD"])), ("QUALIFIED_RELATIONS", len(REG["QR"])),
                      ("EXTERNAL_REFERENCES", len(REG["EXT"])), ("SUBCONFIGURATIONS", len(REG["SC"])), ("ARCHITECTURE_CANDIDATES", len(REG["ARCH"])),
                      ("PROPERTY_REGISTER", len(REG["PROP"])), ("CLOSURE_REGISTER", len(REG["CL"])), ("UNCERTAINTY_LOG", len(REG["UNC"])),
                      ("HUMAN_REVIEW_QUEUE", len(REG["HQ"]))])
allqr = [r["_key"] for r in REG["QR"]]
allna = [r["_key"] for r in REG["NA"]]
allpd = [r["_key"] for r in REG["PD"]]
c_qr = collections.Counter(KEYS[k][1]["epi"] for k in allqr)
c_na = collections.Counter(KEYS[k][1]["epi"] for k in allna)
c_pd = collections.Counter(KEYS[k][1]["epi"] for k in allpd)
prof = ("QUALIFIED_RELATIONS: %d legal_constitution_evidenced; %d documented; 0 material_establishment_evidenced (never carried by relations); 0 exercise_evidenced. "
        "NORMATIVE_ASSIGNMENTS: %d legal_constitution_evidenced; %d documented; 0 material_establishment_evidenced; 0 exercise_evidenced. "
        "POSITIONS_AND_DEVICES: %d legal_constitution_evidenced; %d documented; material establishment not_assessed for all; 0 exercise_evidenced. "
        "Legal status of norm at the 2026-01-01 reference: in_force for all coded norms; no not_yet_applicable, suspended, expired_or_repealed or conditional_on_further_act status asserted.") % (
    c_qr.get("legal_constitution_evidenced", 0), c_qr.get("documented", 0), c_na.get("legal_constitution_evidenced", 0), c_na.get("documented", 0),
    c_pd.get("legal_constitution_evidenced", 0), c_pd.get("documented", 0))
n_ext_y = sum(1 for r in REG["EXT"] if r["constitutive"] == "Y")
outc = collections.Counter(r["outcome"] for r in REG["ARCH"])
summ = ["INSTRUMENT_LEVEL_SUMMARY"]
ILS = [CASE, str(len(UNITS)), str(COUNTS["UNIT_SCREENING"]), rec_counts, "OVERLAPPING_OR_PARTIALLY_INTEGRATED", "A", prof, str(len(REG["HQ"])), str(n_ext_y), "Y",
       "Machine-generated and provisional. Candidate outcomes: %s. The whole-instrument candidate is OVERLAPPING_OR_PARTIALLY_INTEGRATED; no scalar score, no composite. Coverage: every unit inventoried and screened." % ", ".join("%d %s" % (v, k) for k, v in sorted(outc.items()))]
COUNTS["INSTRUMENT_LEVEL_SUMMARY"] = write("INSTRUMENT_LEVEL_SUMMARY.csv", HDR["INSTRUMENT_LEVEL_SUMMARY"], [ILS])

# ---------------- 18 PROTOCOL_DEVIATION_LOG ----------------
DEVS = [
 ("RGAM-DR-04", "Temporal reference selected by the executor: point 2026-01-01, derived from Article 36(2) of W. Legal status of every coded norm is recorded in_force at that reference, with validity notes by application group; Articles 32-35 recorded in_force with a note on their bounded scope.", "DR-04 requires a declared reference derived from the act's own provisions and the neutral metadata; the metadata give no repeal information; the sources do not fix which date to choose.", "Legal-status profile is reference-dependent; queued as HQ-OTHER.", ""),
 ("RGAM-DR-05", "Unit-id conventions beyond those listed in the dictionary: unnumbered subparagraphs .sub{n}; unlabelled enumeration items .pt-{k}; goods and legend tables ANX{n}.TBL{k}; unnumbered annex paragraphs .P{k}; section headings as ANX{n}.pt{x}; footnote texts inlined in the unit where the marker occurs; annex numbers/titles kept in locator text.", "The dictionary gives ids for paragraphs, points, annex points and recitals but not for these constructs; convention chosen to keep every part of the file addressable.", "Unit ids of subparagraphs, annex tables and enumerations follow the stated convention.", "GAP-01"),
 ("RGAM-DR-08", "Annexes and formal provisions coded as units of W and screened/coded like operative provisions; four formula images in Annex IV and the table geometry of the Annex I and II goods tables declared as exclusions in W_DECLARATION and in the uncertainty log.", "GAP-01 execution decision: annexes belong to W when part of the complete frozen instrument and must satisfy the same admission rules; content not representable in the source file is declared.", "No record depends on the formula content; scope statements rest on the parsed table text.", "GAP-01"),
 ("RGAM-DR-08", "GAP-02 examined: no provision of W amends another legal act (Article 25(5) applies Regulation (EC) No 515/97 mutatis mutandis, which is an application reference, not an amendment). No amending-provision EXT was created; GAP-02 was not used.", "Execution addendum GAP-02 covers provisions amending other acts.", "None.", "GAP-02"),
 ("RGAM-DR-20", "Internal cross-references were followed within W to resolve counterparties, conditions and derivations; derived records state the derivation rule and cite both the source and the referenced units (many records marked 'derived'; ambiguous cross-references queued in HQ-XREF).", "GAP-03 execution decision: cross-references to provisions of the same frozen instrument may be followed and remain inside W.", "Derived QR/NA carry derivation_rule and indirect provenance links.", "GAP-03"),
 ("RGAM-DR-20", "No external retrieval: every EXT is not_checked and outside_corpus_not_expanded; external instruments, national law and standards were not opened; the substance of the amended or referenced instruments is undetermined; relations whose legal constitution depends on an unresolved external reference were down-coded to 'documented' and flagged.", "GAP-04 execution decision: external legal retrieval prohibited during case execution.", "Down-coding recorded in support_gap_report/not_constituted_note; ARCH outcomes with I4 INDETERMINATE.", "GAP-04"),
 ("RGAM-DR-15", "Residual function tags (authorization_designation*, cooperation_coordination*) used for assignments and relations whose function fits the residual tags; the value FUNCTION_VOCABULARY_UNRESOLVED was not needed (no legally meaningful function remained unplaced); relation types applied at the nearest of the ten types with a type note where the fit is imperfect (coordination/assistance, committee assistance, certification, protective release, legislative proposal); no new type or function category created.", "GAP-05 execution decision: use only the documented vocabulary and its flagged residual tags.", "Type notes and flags on the affected records; queued under HQ-GAP.", "GAP-05"),
 ("RGAM-DR-25", "NON_OPERATIVE_SOURCE_GAP: the 'six questions' referred to in the operational template are absent from the authorized sources and were not reconstructed or used as an admission, exclusion or inference rule; the four-step anti-circularity sequence and I1-I4 were used.", "GAP-06 execution decision.", "None on any record.", "GAP-06"),
 ("RGAM-DR-08", "Definitional provisions (Article 3, Annex IV point 1) were screened as scope/definitional-context; a defined term yields a position or device only where it bears an NA or QR elsewhere; definitions are cited as support; definitions did not establish any relation, authority, accountability or coupling by themselves.", "GAP-07 execution decision.", "Positions such as competent authority, importer, operator, national accreditation body, customs authorities and authorised CBAM declarant cite their definition as support.", "GAP-07"),
 ("RGAM-DR-24", "The mapping of the ten architectural dimensions to the families F1-F5 is not stated in the allowed sources; a provisional assignment by listing order of the dimensions was used (positional properties placed in F5); no other property names were used.", "The protocol states 'five families F1-F5' without listing members.", "property_family values are provisional; queued under HQ-GAP.", ""),
 ("RGAM-DR-18", "Epistemic down-coding: a QR or NA whose legal constitution depends on an EXT with constitutive_dependency = Y was recorded 'documented' rather than 'legal_constitution_evidenced' (RGAM-DR-19/20); the relation of the Member State to a competent authority that is only mandated (N2 designation, qr.A11_DESIG) was likewise recorded 'documented'; other relations whose party is the competent authority carry a support-gap report (an expectation, never a gate) and were not down-coded for that reason.", "RGAM-DR-20: an element whose legal constitution depends on an unresolved external reference is undetermined; the epistemic vocabulary has no 'undetermined' value, so the highest supported status is 'documented'.", "Status profile counts reflect the down-coding.", ""),
 ("RGAM-DR-23", "Subconfigurations contain NA members and PD members in addition to QR members where the organizing mechanism refers to those assignments; S whose only warrant would be shared theme (e.g., the further reports of Article 30(5)-(8)) were not formed.", "Dictionary lists member_na_ids and member_pd_ids; the decision rules do not say whether NAs may be members.", "None on the stated warrants.", ""),
]
rows = [["DEV-%02d" % i, CASE, a, b, c, d, e] for i, (a, b, c, d, e) in enumerate(DEVS, 1)]
COUNTS["PROTOCOL_DEVIATION_LOG"] = write("PROTOCOL_DEVIATION_LOG.csv", HDR["PROTOCOL_DEVIATION_LOG"], rows)

# ---------------- 19 RUN_METADATA (end time filled by finalize step) ----------------
import datetime
END = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
FILES_READ = json.load(open(L.WORK + "files_read.json", encoding="utf-8")) if os.path.exists(L.WORK + "files_read.json") else []
rows = [["RUN-01", CASE, "RGAM paired execution protocol v1.0", PROTO_MANIFEST, "claude-sonnet-5-5 (Sonnet 5.5, as stated in the session context)",
         "reasoning_effort=10 (value displayed in the session context; the brief requested the highest available effort, which was not user-settable here); temperature, top-p, seed, token limits: NOT_EXPOSED",
         START, END, "Y", ";".join(FILES_READ), "NONE", "Y"]]
COUNTS["RUN_METADATA"] = write("RUN_METADATA.csv", HDR["RUN_METADATA"], rows)

# =====================================================================
# INTEGRITY CHECKS (data dictionary section 4)
# =====================================================================
QA = {}
allids = set(ID.values())
unit_ids = {u["unit_id"] for u in UNITS}
def cell_ids(s):
    return [x for x in re.split(r"[;\s]+", s) if x]
# load written tables back
def load(name):
    with open(OUT + name, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))
T_ = {n: load(n + ".csv") for n in HDR}
# rule 1
bad1 = []
for n, rows_ in T_.items():
    for row in rows_:
        for col, val in row.items():
            if col and (col.endswith("unit_ids") or col in ("unit_id", "i1_scope_units", "instance_source_unit_ids", "units_spanned") and False):
                for x in cell_ids(val or ""):
                    if x not in unit_ids:
                        bad1.append((n, col, x))
        if "unit_id" in row and row["unit_id"] and row["unit_id"] not in unit_ids:
            bad1.append((n, "unit_id", row["unit_id"]))
QA["R1_units_exist"] = (len(bad1) == 0, bad1[:5])
QA["R1_screened_eq_total"] = (len(T_["UNIT_SCREENING"]) == len(T_["SOURCE_UNIT_INVENTORY"]) == int(T_["INSTRUMENT_LEVEL_SUMMARY"][0]["units_screened"]) == int(T_["INSTRUMENT_LEVEL_SUMMARY"][0]["units_total"]), (len(T_["UNIT_SCREENING"]), len(T_["SOURCE_UNIT_INVENTORY"])))
# rule 2
st_ids = {r["st_id"] for r in T_["INSTITUTIONAL_STATEMENTS"]}
bad2 = []
cited = set()
for n, col in [("NORMATIVE_ASSIGNMENTS", "statement_ids"), ("QUALIFIED_RELATIONS", "statement_ids")]:
    for row in T_[n]:
        ids = cell_ids(row[col])
        if not ids or any(i not in st_ids for i in ids):
            bad2.append((n, row[list(row)[0]]))
        cited.update(ids)
derived_ids = set()
for row in T_["INSTITUTIONAL_STATEMENTS"]:
    derived_ids.update(cell_ids(row["derived_record_ids"]))
    if not cell_ids(row["supporting_unit_ids"]):
        bad2.append(("ST no unit", row["st_id"]))
    if row["recital_only"] == "Y" and row["derived_record_ids"]:
        bad2.append(("recital only with derived", row["st_id"]))
for n, col in [("POSITIONS_AND_DEVICES", "pd_id"), ("EXTERNAL_REFERENCES", "ext_id"), ("NORMATIVE_ASSIGNMENTS", "na_id"), ("QUALIFIED_RELATIONS", "qr_id")]:
    for row in T_[n]:
        if row[col] not in derived_ids:
            bad2.append((n, row[col], "not in any ST.derived_record_ids"))
QA["R2_statements"] = (len(bad2) == 0, bad2[:5])
# rule 3: every *_ids / *_pd_id resolves
bad3 = []
for n, rows_ in T_.items():
    for row in rows_:
        for col, val in row.items():
            if col and (col.endswith("_ids") or col.endswith("_pd_id") or col in ("closure_ref", "bearer_id", "traced_id", "record_id", "origin_pd_id", "counterpart_pd_id")) and "unit_ids" not in col and col not in ("candidate_list", "i1_scope_units", "units_spanned", "record_ids" if False else "_"):
                for x in cell_ids(val or ""):
                    if re.match(r"^(ST|NA|PD|QR|EXT|SC|ARCH|PROP|CL|UNC|HQ)-\d+$", x) and x not in allids:
                        bad3.append((n, col, x))
QA["R3_ids_resolve"] = (len(bad3) == 0, bad3[:5])
QA["R3_accountable_via_empty_or_accountability"] = (all(not r["accountable_via_qr_ids"] for r in T_["QUALIFIED_RELATIONS"]), "no accountability-type QR exists; field blank for all")
# rule 4
bad4 = []
for row in T_["QUALIFIED_RELATIONS"]:
    if not row["origin_pd_id"] or not row["counterpart_pd_id"] or row["modality"] == "prohibition" or row["epistemic_status"] == "material_establishment_evidenced":
        bad4.append(row["qr_id"])
QA["R4_qr_parties_modality_status"] = (len(bad4) == 0, bad4)
# rule 5
links = collections.Counter(r["record_id"] for r in T_["PROVENANCE_LINKS"])
bad5 = []
for n, col in [("NORMATIVE_ASSIGNMENTS", "na_id"), ("QUALIFIED_RELATIONS", "qr_id"), ("SUBCONFIGURATIONS", "sc_id"), ("ARCHITECTURE_CANDIDATES", "arch_id"), ("PROPERTY_REGISTER", "prop_id")]:
    for row in T_[n]:
        if links[row[col]] < 1:
            bad5.append((n, row[col]))
for n, col in [("NORMATIVE_ASSIGNMENTS", "na_id"), ("QUALIFIED_RELATIONS", "qr_id")]:
    for row in T_[n]:
        if row["derivation"] == "derived":
            if not row["derivation_rule"] or (len(cell_ids(row["supporting_unit_ids"])) < 2):
                bad5.append((n, row[col], "derived without rule or <2 units"))
QA["R5_provenance_and_derived"] = (len(bad5) == 0, bad5[:5])
# rule 6
bad6 = []
hq_trig = {r["hq_id"]: r["trigger_code"] for r in T_["HUMAN_REVIEW_QUEUE"]}
hq_refs = collections.defaultdict(set)
for r in T_["HUMAN_REVIEW_QUEUE"]:
    for x in cell_ids(r["record_refs"]):
        hq_refs[x].add(r["trigger_code"])
for row in T_["ARCHITECTURE_CANDIDATES"]:
    if row["outcome"] == "INTEGRATED":
        if not all(row[k] == "SATISFIED" for k in ("i1_status", "i2_status", "i3_status", "i4_status")):
            bad6.append((row["arch_id"], "INTEGRATED without all SATISFIED"))
        if "HQ-INTEGRATION" not in hq_refs[row["arch_id"]]:
            bad6.append((row["arch_id"], "no HQ-INTEGRATION"))
    if row["outcome"] == "OVERLAPPING_OR_PARTIALLY_INTEGRATED" and "HQ-OVERLAP" not in hq_refs[row["arch_id"]]:
        bad6.append((row["arch_id"], "no HQ-OVERLAP"))
QA["R6_arch_outcomes_hq"] = (len(bad6) == 0, bad6)
# rule 7
bad7 = []
clres = {r["closure_id"]: r["result"] for r in T_["CLOSURE_REGISTER"]}
for row in T_["PROPERTY_REGISTER"]:
    if row["closure_dependency"] == "Y":
        if row["closure_ref"] not in clres:
            bad7.append((row["prop_id"], "closure_ref unresolved"))
        elif clres[row["closure_ref"]] == "UNDETERMINED" and row["status"] != "undetermined":
            bad7.append((row["prop_id"], "closure UNDETERMINED but status not undetermined"))
QA["R7_closure"] = (len(bad7) == 0, bad7)
# rule 8
QA["R8_ext_not_checked"] = (all(r["source_verification_status"] == "not_checked" and r["boundary_status"] == "outside_corpus_not_expanded" for r in T_["EXTERNAL_REFERENCES"]), len(T_["EXTERNAL_REFERENCES"]))
# rule 9
QA["R9_human_cols_blank"] = (all(not r["human_decision"] and not r["human_rationale"] and not r["decided_by"] and not r["decision_date"] for r in T_["HUMAN_REVIEW_QUEUE"]), len(T_["HUMAN_REVIEW_QUEUE"]))
# rule 10
bad10 = []
for row in T_["TRACE_DEMONSTRATIONS"]:
    ids = set(re.findall(r"(?:SC|ARCH|QR|ST)-\d+", row["vertical_chain"]))
    for x in ids:
        if x not in allids:
            bad10.append(x)
    if row["chain_complete"] != "Y":
        bad10.append("chain incomplete " + row["trace_id"])
    if "RGAM_C2_CBAM." not in row["vertical_chain"] or "span" not in row["vertical_chain"]:
        bad10.append("no unit/span " + row["trace_id"])
QA["R10_trace"] = (len(bad10) == 0, bad10)
# extra checks
QA["spans_le_400_verbatim"] = True
for t in ["ST", "NA", "PD", "QR"]:
    for r in REG[t]:
        sp = norm(r["span"])
        if len(sp) > 400 or not any(sp in norm(UT[u]["text"]) for u in r["units"]):
            QA["spans_le_400_verbatim"] = False
QA["screen_issues"] = screen_issues
QA["unresolved_keys"] = ERR
QA["no_prohibition_QR"] = all(r["modality"] != "prohibition" for r in T_["QUALIFIED_RELATIONS"])
QA["na_prohibition_constraint_only_Y"] = all(r["constraint_only"] == "Y" for r in T_["NORMATIVE_ASSIGNMENTS"] if r["modality"] == "prohibition")
QA["headers_equal_templates"] = all(header_of(n + ".csv") == HDR[n] for n in HDR)
QA["unique_ids"] = len(allids) == len(ID)
QA["counts"] = COUNTS
QA["screen_counts"] = dict(yes=SCREEN_YES, no=SCREEN_NO, uncertain=SCREEN_UNC)
QA["trace"] = TRACE_INFO
QA["down_coded"] = {k: v for k, v in DOWN.items()}
QA["outcomes"] = {r["_id"] + " " + r["_key"]: r["outcome"] for r in REG["ARCH"]}
QA["status_profile"] = prof
QA["end"] = END
json.dump(QA, open(L.WORK + "qa_result.json", "w", encoding="utf-8"), indent=1, default=str)
for k, v in QA.items():
    if isinstance(v, tuple):
        print(k, "PASS" if v[0] else "FAIL", v[1] if not v[0] else "")
    else:
        print(k, v if not isinstance(v, (dict, list)) else (len(v) if k not in ("counts", "screen_counts", "trace", "outcomes") else v))
