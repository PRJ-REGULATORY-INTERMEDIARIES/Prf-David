"""Composition statistics for the initial architectural profile (composition only; counts are NOT significance, V6 §6.6)."""
import json, os, re, collections, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(HERE, "..", "03_EXTRACTION", "_store.json"), encoding="utf-8"))
pdlab = {p["id"]: p["label"] for p in D["pd"]}
fix = lambda v: re.sub(r"PD-\d{3}", lambda m: pdlab.get(m.group(0), m.group(0)), v or "")
sc = json.load(open(os.path.join(HERE, "sc_data.json"), encoding="utf-8"))


def tag1(label):
    l = fix(label).lower()
    if "lead supervisory" in l or "supervisory authorit" in l or re.search(r"\bsas?\b", l): return "SA"
    if "board" in l and "management" not in l: return "Board"
    if "commission" in l: return "Commission"
    if "member state" in l: return "Member States"
    if "court" in l or "judicial" in l: return "Courts"
    if "data protection officer" in l: return "DPO"
    if "certification body" in l or "monitoring body" in l or "accreditation body" in l: return "Private/NAB intermediaries (cert/monitor)"
    if "association" in l and "representing" in l: return "Associations"
    if "controller" in l and "processor" not in l: return "Controller"
    if "processor" in l and "controller" not in l: return "Processor"
    if "controller" in l and "processor" in l: return "Controller/processor"
    if "data subject" in l or "complainant" in l: return "Data subject"
    if "parliament" in l: return "EP/Council"
    return "other/unstated"


FN = [("rule-making/standard-setting", r"rule-making|standard-setting|delegated|implementing"), ("implementation", r"implementation"), ("information provision", r"information provision|reporting|notification|publication"),
      ("monitoring/investigation", r"monitoring|investigation"), ("verification/assurance", r"verification|assurance"), ("enforcement/sanction", r"enforcement|sanction"),
      ("adjudication/review", r"adjudication|review|dispute"), ("remediation", r"remediation"), ("authorization/designation", r"authorization|designation|accreditation"),
      ("cooperation/coordination", r"cooperation|coordination"), ("participation/representation/consultation", r"representation|participation|consultation"), ("advice/interpretation", r"advice|interpretation")]


def fcat(txt):
    t = txt.lower()
    for name, pat in FN:
        if re.search(pat, t):
            return name
    return "other"


rows = collections.Counter()
rowsq = collections.Counter()
for r in D["qr"]:
    rowsq[(tag1(r["origin"]), fcat(r["function"]))] += 1
for r in D["na"]:
    rows[(tag1(r["subject"]), fcat(r["function"]))] += 1
pos = sorted({k[0] for k in list(rows) + list(rowsq)})
fns = [n for n, _ in FN] + ["other"]
out = {"qr_by_origin_function": {f"{p}|{f}": rowsq[(p, f)] for p in pos for f in fns if rowsq[(p, f)]},
       "na_by_subject_function": {f"{p}|{f}": rows[(p, f)] for p in pos for f in fns if rows[(p, f)]}}
types = collections.Counter(r["relation_type"] for r in D["qr"])
out["qr_types"] = dict(types)
pub = {"SA", "Board", "Commission", "Member States", "Courts", "EP/Council"}
priv = {"Controller", "Processor", "Controller/processor", "DPO", "Private/NAB intermediaries (cert/monitor)", "Associations"}
pp = collections.Counter()
for r in D["qr"]:
    o = tag1(r["origin"]); c = tag1(r["counterpart"])
    pp[("public" if o in pub else "private/regulated" if o in priv else "other") + "->" + ("public" if c in pub else "private/regulated" if c in priv else "data subject/other")] += 1
out["qr_origin_to_counterpart_sector"] = dict(pp)
# accountability classes recorded
ac = collections.Counter()
for r in D["qr"]:
    a = (r.get("accountability_class") or "").strip()
    if a:
        ac[re.split(r"[ (:—-]", a)[0]] += 1
out["accountability_labels_first_token"] = dict(ac)
json.dump(out, open(os.path.join(HERE, "profile_stats.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("QR types:", dict(types))
print("sector:", dict(pp))
tab = collections.defaultdict(dict)
for k, v in out["qr_by_origin_function"].items():
    p, f = k.split("|"); tab[p][f] = v
for p in sorted(tab, key=lambda x: -sum(tab[x].values())):
    print(p, sum(tab[p].values()), dict(sorted(tab[p].items(), key=lambda x: -x[1])[:5]))
print("ACC:", dict(ac))
