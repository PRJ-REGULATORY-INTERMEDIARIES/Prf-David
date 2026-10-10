# Helper library: record containers + mechanical resolution. Analytical content is authored in rec_*.py by the executor.
import json, re, hashlib, collections

CASE = "RGAM_C2_CBAM"
WORK = "G:/Meu Drive/PRJ-David/Prf-David/NEW TEST 3x3/12_RGAM_CASE_EXECUTION/RGAM_C2_CBAM/_work/"
UNITS = json.load(open(WORK + "units.json", encoding="utf-8"))
UT = {u["unit_id"].replace(CASE + ".", "", 1): u for u in UNITS}


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


TYPES = ["ST", "NA", "PD", "QR", "EXT", "SC", "ARCH", "PROP", "CL", "UNC", "HQ"]
REG = {t: [] for t in TYPES}
KEYS = {}  # full key -> (type, record)


def L(x):
    if x is None or x == "":
        return []
    if isinstance(x, (list, tuple)):
        return list(x)
    return [t.strip() for t in str(x).split(";") if t.strip()]


def _reg(t, key, rec):
    assert key not in KEYS, "duplicate key " + key
    rec["_key"] = key
    rec["_type"] = t
    REG[t].append(rec)
    KEYS[key] = (t, rec)
    return key


def checkunits(us, key):
    for u in L(us):
        assert u in UT, "unknown unit %s in %s" % (u, key)


# ---- legal-status derivation from the act's own application schedule (Art 36(2)); reference date 2026-01-01 ----
REFERENCE = "2026-01-01"


def appl_group(unit):
    u = UT[unit]
    a = u["article_or_annex_no"]
    if u["structure_class"] == "OPERATIVE_ARTICLE":
        n = int(a)
        p = int(u["paragraph"]) if u["paragraph"] not in ("", None) else 0
        if n in (5, 10, 14, 16, 17):
            return "2024"
        if n in (4, 6, 7, 8, 9, 15, 19, 21, 22, 23, 24, 25, 26, 27, 31):
            return "2026"
        if n == 2 and p == 2:
            return "2026"
        if n == 20 and p in (1, 3, 4, 5):
            return "2026"
        return "2023"
    return "2023"


GROUP_NOTE = {
    "2023": "applies from 1 October 2023 (Art. 36(2) first sentence); in force and applicable at the 2026-01-01 reference",
    "2024": "applies from 31 December 2024 (Art. 36(2)(a)); in force and applicable at the 2026-01-01 reference",
    "2026": "applies from 1 January 2026 (Art. 36(2)(b)); in force and applicable at the 2026-01-01 reference",
}


def validity_for(units):
    gs = sorted({appl_group(u) for u in L(units)})
    return "; ".join(GROUP_NOTE[g] for g in gs)


def st(key, units, kind, summary, span, recital_only="N"):
    checkunits(units, key)
    return _reg("ST", key, dict(units=L(units), kind=kind, summary=summary, span=span, recital_only=recital_only))


def pd(key, kind, label, toi, units, span, st, inst_src="", mult="unspecified", estab="NONE", dev_id="", dev_fn="",
       dev_class="", constit="not_applicable", epi="documented", unc="", hq="", iunits=""):
    checkunits(units, key)
    return _reg("PD", key, dict(kind=kind, label=label, toi=toi, units=L(units), span=span, st=L(st), inst_src=inst_src,
                                mult=mult, estab=estab, dev_id=dev_id, dev_fn=dev_fn, dev_class=dev_class, constit=constit,
                                epi=epi, unc=L(unc), hq=L(hq), iunits=L(iunits)))


def na(key, st, units, pdk, action, obj, function, modality, span, mech="", instr="", cond="", cp="", cps="NONE_IDENTIFIABLE",
       nt="N0", eff="", notc="", constraint="N", deriv="direct", drule="", deps="", legal="in_force", epi="legal_constitution_evidenced",
       unc="", hq="", iunits="", ext=""):
    checkunits(units, key)
    return _reg("NA", key, dict(ext=L(ext), st=L(st), units=L(units), pd=pdk, action=action, obj=obj, function=function, mech=mech, instr=instr,
                                modality=modality, cond=cond, cp=cp, cps=cps, nt=nt, eff=eff, notc=notc, constraint=constraint,
                                deriv=deriv, drule=drule, deps=L(deps), legal=legal, epi=epi, span=span, unc=L(unc), hq=L(hq),
                                iunits=L(iunits)))


def qr(key, st, units, o, c, rtype, tdir, action, obj, function, modality, span, extra="", tnote="", gdir="", mech="", instr="",
       cond="", validity=None, legal="in_force", epi="legal_constitution_evidenced", deriv="direct", drule="", authattr="",
       discattr="", acls="NONE", asuff="NA", amiss="", accvia="", deps="", gap="", ext="", unc="", hq="", iunits=""):
    checkunits(units, key)
    return _reg("QR", key, dict(st=L(st), units=L(units), o=o, c=c, extra=L(extra), rtype=rtype, tnote=tnote, tdir=tdir, gdir=gdir,
                                action=action, obj=obj, function=function, mech=mech, instr=instr, modality=modality, cond=cond,
                                validity=validity if validity is not None else validity_for(units), legal=legal, epi=epi,
                                deriv=deriv, drule=drule, authattr=authattr, discattr=discattr, acls=acls, asuff=asuff, amiss=amiss,
                                accvia=L(accvia), deps=L(deps), gap=gap, ext=L(ext), span=span, unc=L(unc), hq=L(hq),
                                iunits=L(iunits)))


def ext(key, st, units, source, kind, role, dependents="", dep_kind="specifies", constitutive="N", effect="", iunits=""):
    checkunits(units, key)
    return _reg("EXT", key, dict(st=L(st), units=L(units), source=source, kind=kind, role=role, dependents=L(dependents),
                                 dep_kind=dep_kind, constitutive=constitutive, effect=effect, iunits=L(iunits)))


def unc(key, rtype, recs, units, desc, treat, effect, status="OPEN"):
    checkunits(units, key)
    return _reg("UNC", key, dict(rtype=rtype, recs=L(recs), units=L(units), desc=desc, treat=treat, effect=effect, status=status))


def hq(key, trigger, recs, question, readings, recommendation, reason):
    return _reg("HQ", key, dict(trigger=trigger, recs=L(recs), question=question, readings=readings, reco=recommendation, reason=reason))


def sc(key, scope, pattern, question, qrs, nas, pds, mech, warrant, boundary, competing, overlap="", nested="", unc="", hq=""):
    return _reg("SC", key, dict(scope=scope, pattern=pattern, question=question, qrs=L(qrs), nas=L(nas), pds=L(pds), mech=mech, warrant=warrant,
                                boundary=boundary, competing=competing, overlap=L(overlap), nested=nested, unc=L(unc), hq=L(hq)))


def arch(key, scs, i1p, i1u, i1s, i2d, i2k, i2q, i2s, i3c, i3b, i3s, i4s, i4e, i4r, i4b, i4st, outcome, basis, unc="", hq="", seq="Y"):
    return _reg("ARCH", key, dict(scs=L(scs), i1p=i1p, i1u=L(i1u), i1s=i1s, i2d=i2d, i2k=i2k, i2q=L(i2q), i2s=i2s, i3c=i3c, i3b=i3b, i3s=i3s,
                                  i4s=i4s, i4e=L(i4e), i4r=i4r, i4b=i4b, i4st=i4st, outcome=outcome, basis=basis, unc=L(unc), hq=L(hq), seq=seq))


def prop(key, name, family, btype, bearer, scale, value, rule, support, status, path="", agg="", cdep="N", cref="", count="", fallacy="Y",
         rival="", hq=""):
    return _reg("PROP", key, dict(name=name, family=family, btype=btype, bearer=bearer, scale=scale, value=value, rule=rule, path=path, agg=agg,
                                  support=L(support), cdep=cdep, cref=cref, count=count, fallacy=fallacy, rival=rival, status=status, hq=L(hq)))


def cl(key, kind, claim, search, result, ext="", affected=""):
    return _reg("CL", key, dict(kind=kind, claim=claim, search=search, result=result, ext=L(ext), affected=L(affected)))
