"""Rebuild all pilot records from the batch files (idempotent). Usage: python run_all.py"""
import glob, os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pilot_lib as L
L.D.clear(); L.D.update({"screen": {}, "na": [], "qr": [], "pd": [], "ext": [], "unc": [], "hq": []})
ns = {k: getattr(L, k) for k in ("screen", "na", "qr", "pd", "ext", "unc", "hq", "link")}
ns["D"] = L.D
for f in sorted(glob.glob(os.path.join(L.HERE, "batch_*.py"))):
    exec(compile(open(f, encoding="utf-8").read(), f, "exec"), ns)
    print("ran", os.path.basename(f))
L.save()
print({k: (len(v)) for k, v in L.D.items()})
