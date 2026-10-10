# MECHANICAL generation of TRACE_DEMONSTRATIONS by the fixed rule of RGAM-DR-29 (no choice of expected support).
import csv, re, json, random, hashlib

W = "G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/12_RGAM_CASE_EXECUTION/RGAM_AI_AI_ACT/_work/"
B = W + "build/"
PFX = "RGAM_AI_AI_ACT."


def rd(n):
    return list(csv.DictReader(open(B + n + ".csv", encoding="utf-8-sig")))


units = {x["unit_id"]: x for x in json.load(open(W + "units.json", encoding="utf-8"))}
units = {PFX + k[len(PFX):]: v for k, v in units.items()}
SC = rd("SUBCONFIGURATIONS"); AR = rd("ARCHITECTURE_CANDIDATES"); QR = rd("QUALIFIED_RELATIONS"); NA = rd("NORMATIVE_ASSIGNMENTS")
ST = {r["st_id"]: r for r in rd("INSTITUTIONAL_STATEMENTS")}
LK = rd("PROVENANCE_LINKS")
sha = hashlib.sha256(open("G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/11_RGAM_PROTOCOL_FREEZE/CAPSULES/RGAM_AI_AI_ACT/LEGAL_SOURCE/32024R1689_official_en.xhtml", "rb").read()).hexdigest()
seed = int(sha[:8], 16)
CH = [(1, 4, "I"), (5, 5, "II"), (6, 49, "III"), (50, 50, "IV"), (51, 56, "V"), (57, 63, "VI"), (64, 70, "VII"), (71, 71, "VIII"),
      (72, 94, "IX"), (95, 96, "X"), (97, 98, "XI"), (99, 101, "XII"), (102, 113, "XIII")]


def part(u):
    s = u[len(PFX):]
    m = re.match(r"A(\d+)\.", s)
    if m:
        n = int(m.group(1))
        for a, b, r in CH:
            if a <= n <= b:
                return "CH" + r
    m = re.match(r"ANX(\d+)\.", s)
    if m:
        return "ANX" + m.group(1)
    if s.startswith("REC"):
        return "REC"
    return "FORMAL"


sup = {}
for l in LK:
    if l["record_type"] in ("SC", "ARCH"):
        sup.setdefault(l["record_id"], set()).add(l["unit_id"])
cands = sorted(sup.keys())
multi = [c for c in cands if len({part(u) for u in sup[c]}) >= 2]
rng = random.Random(seed)
draw = multi[rng.randrange(len(multi))]
largest = max(cands, key=lambda c: (len(sup[c]), c))
qrs = {r["qr_id"]: r for r in QR}
nas = {r["na_id"]: r for r in NA}


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def step(rid):
    r = qrs.get(rid) or nas.get(rid)
    if not r:
        return None, f"{rid} (unresolved)", False
    ok = True
    sts = [x for x in r["statement_ids"].split(";") if x]
    parts = []
    for s in sts:
        if s not in ST:
            ok = False
            continue
        us = [x for x in ST[s]["supporting_unit_ids"].split(";") if x]
        for u in us:
            if u not in units:
                ok = False
    span = r["evidence_span"]
    spu = [x for x in r["supporting_unit_ids"].split(";") if x]
    found = any(span in norm(units[u]["text"]) for u in spu if u in units) or any(span in norm(units[u]["text"]) for s in sts if s in ST for u in ST[s]["supporting_unit_ids"].split(";") if u in units)
    if not found or not span:
        ok = False
    return r, f"{rid} -> {';'.join(sts)} -> {';'.join(spu)} -> span: {span}", ok


def chain_for(tid):
    out = []
    ok = True
    if tid.startswith("ARCH-"):
        a = [x for x in AR if x["arch_id"] == tid][0]
        out.append(f"{tid} -> member SC {a['member_sc_ids']}")
        for s in a["member_sc_ids"].split(";"):
            sc = [x for x in SC if x["sc_id"] == s][0]
            out.append(f"{s} -> {len(sc['member_qr_ids'].split(';'))} relations and {len([x for x in sc['member_na_ids'].split(';') if x])} assignments (see I2 relations below)")
        ids = [x for x in a["i2_qr_ids"].split(";") if x]
    else:
        sc = [x for x in SC if x["sc_id"] == tid][0]
        out.append(f"{tid} -> members")
        ids = [x for x in sc["member_qr_ids"].split(";") if x] + [x for x in sc["member_na_ids"].split(";") if x]
    for i in ids:
        r, t, k = step(i)
        ok = ok and k
        out.append(t)
    return " || ".join(x.replace(" | ", " / ") for x in out), ok


lines = []
cl = ";".join(multi)
ch1, ok1 = chain_for(draw)
lines.append(f"TR | selection_rule=SEEDED_DRAW | seed_integer={seed} | candidate_list={cl} | traced_id={draw} | vertical_chain={ch1} | chain_complete={'Y' if ok1 else 'N'}")
ch2, ok2 = chain_for(largest)
lines.append(f"TR | selection_rule=LARGEST_SUPPORT | seed_integer= | candidate_list={';'.join(cands)} | traced_id={largest} | vertical_chain={ch2} | chain_complete={'Y' if ok2 else 'N'}")
open(W + "rec/r25.txt", "w", encoding="utf-8").write("# P9: trace demonstrations by the fixed rule of RGAM-DR-29 (generated mechanically by gen_tr.py: seeded draw with random.Random(seed).randrange over the sorted candidate list spanning at least two parts; plus largest distinct supporting units)\n" + "\n".join(lines) + "\n")
print("seed", seed, "multi", len(multi), "draw", draw, "largest", largest, len(sup[largest]), ok1, ok2)
