"""Structural validation only (headers, coverage equality, human columns blank, manifest). Prints booleans; no analytical content."""
import csv, hashlib, os, sys, json
cid = sys.argv[1]
R = "G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3"
O = f"{R}/12_RGAM_CASE_EXECUTION/{cid}"
T = f"{R}/11_RGAM_PROTOCOL_FREEZE/CAPSULES/{cid}/OUTPUT_TEMPLATES"
res = {}
hdr_ok = True
for fn in sorted(os.listdir(T)):
    if not fn.endswith(".csv"): continue
    th = next(csv.reader(open(f"{T}/{fn}", encoding="utf-8-sig", newline="")))
    p = f"{O}/{fn}"
    if not os.path.isfile(p): hdr_ok = False; res["missing_" + fn] = True; continue
    rows = list(csv.reader(open(p, encoding="utf-8-sig", newline="")))
    if not rows or rows[0] != th: hdr_ok = False; res["bad_header_" + fn] = True
res["all_19_tables_present_with_frozen_headers"] = hdr_ok
def load(fn): return list(csv.DictReader(open(f"{O}/{fn}", encoding="utf-8-sig", newline="")))
inv, scr = load("SOURCE_UNIT_INVENTORY.csv"), load("UNIT_SCREENING.csv")
res["units_screened_equals_inventoried"] = len(inv) == len(scr) and {r["unit_id"] for r in inv} == {r["unit_id"] for r in scr} and len(inv) > 0
hq = load("HUMAN_REVIEW_QUEUE.csv")
res["human_columns_blank"] = all(not r[c].strip() for r in hq for c in ("human_decision", "human_rationale", "decided_by", "decision_date"))
qr = load("QUALIFIED_RELATIONS.csv")
res["qr_both_parties_nonprohibition"] = all(r["origin_pd_id"].strip() and r["counterpart_pd_id"].strip() and r["modality"].strip() != "prohibition" and r["epistemic_status"].strip() != "material_establishment_evidenced" for r in qr)
ext = load("EXTERNAL_REFERENCES.csv")
res["ext_not_checked"] = all(r["source_verification_status"].strip() == "not_checked" for r in ext)
arch = load("ARCHITECTURE_CANDIDATES.csv")
ids_hq = {r["hq_id"] for r in hq}
res["integrated_overlapping_queued"] = all(any(h.strip() in ids_hq for h in r["hq_ids"].replace(",", ";").split(";") if h.strip()) for r in arch if r["outcome"] in ("INTEGRATED", "OVERLAPPING_OR_PARTIALLY_INTEGRATED"))
res["integrated_requires_all_I_satisfied"] = all(all(r[k] == "SATISFIED" for k in ("i1_status", "i2_status", "i3_status", "i4_status")) for r in arch if r["outcome"] == "INTEGRATED")
# manifest
mp = f"{O}/CASE_FREEZE_MANIFEST.csv"
ok = True
for r in csv.DictReader(open(mp, encoding="utf-8-sig", newline="")):
    p = f"{O}/{r['relative_path']}"
    if not os.path.isfile(p) or hashlib.sha256(open(p, "rb").read()).hexdigest() != r["sha256"]: ok = False
res["manifest_entries_match_files"] = ok
res["manifest_sidecar_matches"] = hashlib.sha256(open(mp, "rb").read()).hexdigest() in open(f"{O}/CASE_FREEZE_MANIFEST_SHA256.txt").read()
src = [f for f in os.listdir(f"{R}/11_RGAM_PROTOCOL_FREEZE/CAPSULES/{cid}/LEGAL_SOURCE")][0]
meta = json.load(open(f"{R}/11_RGAM_PROTOCOL_FREEZE/CAPSULES/{cid}/CASE_METADATA.json", encoding="utf-8"))
res["capsule_source_hash_matches_metadata"] = hashlib.sha256(open(f"{R}/11_RGAM_PROTOCOL_FREEZE/CAPSULES/{cid}/LEGAL_SOURCE/{src}", "rb").read()).hexdigest() == meta["source_sha256"]
res["gate_file_token"] = ("RGAM_CASE_FROZEN" in open(f"{O}/CASE_GATE.md", encoding="utf-8").read(), "RGAM_CASE_BLOCKED" in open(f"{O}/CASE_GATE.md", encoding="utf-8").read())
print(json.dumps(res, indent=1))
