import importlib, re, sys, traceback
sys.path.insert(0, "G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/12_RGAM_CASE_EXECUTION/RGAM_C2_CBAM/_work")
import rgam_lib as L
mods = ["rec_01_pd", "rec_02_ch1", "rec_03_ch2", "rec_04_ch3", "rec_05_ch4_6", "rec_06_ch7_11", "rec_07_annex", "rec_85_screening"]
import os
for extra in ["rec_80_sc_arch", "rec_82_prop", "rec_90_hq_unc"]:
    if os.path.exists(L.WORK + extra + ".py"):
        mods.append(extra)
for m in mods:
    try:
        importlib.import_module(m)
    except Exception:
        print("ERROR in", m)
        traceback.print_exc()
        sys.exit(1)
print({t: len(v) for t, v in L.REG.items()})
# span verification
bad = 0
for t in ["ST", "NA", "PD", "QR"]:
    for r in L.REG[t]:
        sp = L.norm(r["span"])
        units = r["units"]
        ok = any(sp in L.norm(L.UT[u]["text"]) for u in units)
        if not ok:
            bad += 1
            print("SPAN MISMATCH", r["_key"], "::", sp[:90])
        if len(sp) > 400:
            print("SPAN TOO LONG", r["_key"], len(sp))
print("span failures", bad)
# unresolved keys
pat = re.compile(r"^(st|pd|na|qr|ext|sc|arch|prop|cl|unc|hq)\.\S+$")
def keys_in(v):
    if isinstance(v, str):
        for tok in v.split(";"):
            tok = tok.strip()
            if pat.match(tok):
                yield tok
    elif isinstance(v, list):
        for x in v:
            yield from keys_in(x)
miss = set()
for t, recs in L.REG.items():
    for r in recs:
        for f, v in r.items():
            if f.startswith("_") or f in ("span", "summary", "desc", "question", "readings", "reco", "reason", "treat", "effect", "action", "obj", "mech", "cond"):
                continue
            for k in keys_in(v):
                if k not in L.KEYS:
                    miss.add((k, r["_key"], f))
for m in sorted(miss):
    print("UNRESOLVED", m)
print("unresolved", len(miss))
# ST coverage
cov = {}
for r in L.REG["ST"]:
    for u in r["units"]:
        cov.setdefault(u, []).append(r["_key"])
nost = [u["unit_id"].replace(L.CASE + ".", "") for u in L.UNITS if u["unit_id"].replace(L.CASE + ".", "") not in cov]
print("units without ST:", len(nost))
open(L.WORK + "units_without_st.txt", "w").write("\n".join(nost))
