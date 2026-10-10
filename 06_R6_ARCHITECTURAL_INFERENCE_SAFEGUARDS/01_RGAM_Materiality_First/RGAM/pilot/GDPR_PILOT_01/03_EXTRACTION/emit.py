"""Write the Pilot 01 CSV registers from _store.json. Deterministic. Usage: python emit.py"""
import json, csv, os, re, collections
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
D = json.load(open(os.path.join(HERE, "_store.json"), encoding="utf-8"))
# resolve PD ids that were used as party labels inside free-text fields (batch convenience variables)
_pdlab = {p["id"]: p["label"] for p in D["pd"]}
def _fix(v):
    if not isinstance(v, str):
        return v
    v = re.sub(r"PD-\d{3}", lambda m: _pdlab.get(m.group(0), m.group(0)), v)
    return v.replace("supervisory authority concerneds", "supervisory authorities concerned").replace("supervisory authoritys", "supervisory authorities").replace("SAs concerneds", "SAs concerned")
for _k in ("na", "qr"):
    for _r in D[_k]:
        for _f in list(_r.keys()):
            if _f not in ("units", "id"):
                _r[_f] = _fix(_r[_f])
inv = list(csv.DictReader(open(os.path.join(ROOT, "01_SOURCES", "SOURCE_UNIT_INVENTORY.csv"), encoding="utf-8")))
para = [r for r in inv if r["kind"] == "paragraph"]
points = collections.Counter(r["unit_id"].rsplit(".pt", 1)[0] for r in inv if r["kind"] == "point")


def pu(u):
    """paragraph-level unit id of a (possibly point-level) unit id"""
    return re.sub(r"\.pt[^.;]*$", "", u)


def by_unit(kind):
    m = collections.defaultdict(list)
    for r in D[kind]:
        for u in set(pu(x) for x in r["units"].split(";") if x):
            m[u].append(r)
    return m


NA_BY, QR_BY, EXT_BY = by_unit("na"), by_unit("qr"), by_unit("ext")
PD_BY = by_unit("pd")
labels = {}
for p in D["pd"]:
    labels[p["id"]] = p["label"]
# sanity: referenced ids exist
ids = {k: {r["id"] for r in D[k]} for k in ("na", "qr", "pd", "ext")}
bad = []
for u, s in D["screen"].items():
    for k, key in (("na", "na"), ("qr", "qr"), ("pd", "pos"), ("ext", "ext")):
        for i in s[key]:
            if i not in ids[k]:
                bad.append((u, k, i))
print("dangling references in screening rows:", bad[:10], len(bad))

CHAP = {"cpt_I": "Chapter I", "cpt_II": "Chapter II", "cpt_III": "Chapter III", "cpt_IV": "Chapter IV", "cpt_V": "Chapter V", "cpt_VI": "Chapter VI", "cpt_VII": "Chapter VII", "cpt_VIII": "Chapter VIII", "cpt_IX": "Chapter IX", "cpt_X": "Chapter X", "cpt_XI": "Chapter XI"}
cover = []
for r in para:
    uid = r["unit_id"]
    s = D["screen"][uid]
    nas = NA_BY.get(uid, [])
    qrs = QR_BY.get(uid, [])
    exts = EXT_BY.get(uid, [])
    pos = set()
    for x in nas:
        if x["subject"]:
            pos.add(x["subject"])
    for x in qrs:
        pos.add(x["origin"]); pos.add(x["counterpart"])
    for pid in s["pos"]:
        pos.add(labels.get(pid, pid))
    for p in PD_BY.get(uid, []):
        pos.add(p["label"])
    art = int(r["article"]); par = r["paragraph"]
    ref = f"Regulation (EU) 2016/679, Art. {art}" + ("" if par == "0" else f"({par})") + " [OJ L 119, 4.5.2016; corrigendum OJ L 127, 23.5.2018 applied where listed]"
    status_screen = "Uncertain" if s["rel"] == "Uncertain" else "Reviewed"
    ext_status = s["status"]
    cover.append({
        "article_id": f"GDPR.A{art}", "subdivision_id": uid, "chapter": CHAP.get(r["chapter"], r["chapter"]), "section": r["section"] or "",
        "source_reference": ref, "points_inventoried": points.get(uid, 0),
        "screening_status": status_screen, "governance_relevance": s["rel"], "governance_role": s["role"],
        "normative_assignment": "; ".join(f"{x['id']}" for x in nas),
        "position_candidates": "; ".join(sorted(p for p in pos if p)),
        "relational_candidate": "; ".join(f"{x['id']}" for x in qrs),
        "external_dependency": "; ".join(f"{x['id']}" for x in exts),
        "extraction_status": ext_status, "evidence_note": s["note"],
    })
os.makedirs(os.path.join(ROOT, "02_COVERAGE"), exist_ok=True)
with open(os.path.join(ROOT, "02_COVERAGE", "ARTICLE_COVERAGE_REGISTER.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(cover[0].keys())); w.writeheader(); w.writerows(cover)


def dump(path, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)


dump(os.path.join(HERE, "NORMATIVE_ASSIGNMENTS.csv"), [{**{k: v for k, v in r.items()}, "depends_on": r.get("depends_on", "")} for r in D["na"]])
dump(os.path.join(HERE, "POSITIONS_AND_DEVICES.csv"), D["pd"])
dump(os.path.join(HERE, "QUALIFIED_RELATIONS.csv"), D["qr"])
dump(os.path.join(ROOT, "01_SOURCES", "EXTERNAL_REFERENCE_REGISTER.csv"), D["ext"])
print("written", len(cover), "coverage rows;", len(D["na"]), "NA;", len(D["qr"]), "QR;", len(D["pd"]), "PD;", len(D["ext"]), "EXT")
# statistics for the coverage report
st = collections.Counter((c["chapter"], c["governance_relevance"]) for c in cover)
json.dump({"by_chapter_relevance": {f"{k[0]}|{k[1]}": v for k, v in st.items()}, "n_units": len(cover),
           "units_with_qr": sum(1 for c in cover if c["relational_candidate"]), "units_with_na": sum(1 for c in cover if c["normative_assignment"]),
           "units_with_ext": sum(1 for c in cover if c["external_dependency"])},
          open(os.path.join(HERE, "_stats.json"), "w"), indent=1)
