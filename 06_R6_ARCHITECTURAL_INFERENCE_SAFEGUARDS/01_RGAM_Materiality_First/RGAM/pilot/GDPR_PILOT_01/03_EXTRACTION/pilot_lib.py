"""Recording library for GDPR Pilot 01. Machine-generated, provisional records; see 00_PROTOCOL/DECISION_RULES.md v1.0.
Batches (batch_*.py) call screen/na/qr/pd/ext/unc; emit.py writes the CSV files.
"""
import json, os, csv

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
STORE = os.path.join(HERE, "_store.json")

LS_DEFAULT = "in_force_applicable_from_2018-05-25 (Art.99(2))"
ES_OPERATIVE = "legal_constitution_evidenced(baseline)"

D = {"screen": {}, "na": [], "qr": [], "pd": [], "ext": [], "unc": [], "hq": []}
if os.path.exists(STORE):
    D = json.load(open(STORE, encoding="utf-8"))


def _u(s):
    """'A5.P1;A5.P2.pta' -> 'GDPR.A5.P1;GDPR.A5.P2.pta'"""
    return ";".join("GDPR." + x.strip() for x in s.split(";") if x.strip())


def save():
    json.dump(D, open(STORE, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def screen(unit, rel, role, na=(), pos=(), qr=(), ext=(), status="Extracted", note=""):
    """one row per paragraph unit (GDPR.A{n}.P{k}); rel in Yes/No/Uncertain"""
    D["screen"]["GDPR." + unit] = {"rel": rel, "role": role, "na": list(na), "pos": list(pos), "qr": list(qr), "ext": list(ext), "status": status, "note": note}


def na(units, subject, action, obj, function, modality, cond="", counterpart="", cp_status="none", ntype="N0", deriv="direct", note="", flag="", dep=""):
    i = f"NA-{len(D['na'])+1:04d}"
    D["na"].append({"id": i, "units": _u(units), "subject": subject, "action": action, "object": obj, "function": function, "modality": modality,
                    "conditions": cond, "counterpart": counterpart, "counterpart_status": cp_status, "norm_type": ntype, "derivation": deriv,
                    "depends_on": dep, "legal_status": LS_DEFAULT, "epistemic_status": ES_OPERATIVE, "note": note, "review_flag": flag})
    return i


def qr(units, origin, counterpart, rtype, obj, function, modality, cond="", deriv="direct", ext="", acc="", dep="", type_note="", unresolved="", flag=""):
    i = f"QR-{len(D['qr'])+1:04d}"
    D["qr"].append({"id": i, "units": _u(units), "origin": origin, "counterpart": counterpart, "relation_type": rtype, "type_note": type_note,
                    "object": obj, "function": function, "modality": modality, "conditions": cond, "derivation": deriv,
                    "external_dependency": ext, "accountability_class": acc, "depends_on": dep,
                    "legal_status": LS_DEFAULT, "epistemic_status": ES_OPERATIVE, "unresolved_interpretation": unresolved, "review_flag": flag})
    return i


def pd(label, kind, units, ntype="n/a", mult="", note="", flag=""):
    for p in D["pd"]:
        if p["label"] == label:
            # extend provenance
            have = set(p["units"].split(";"))
            for x in _u(units).split(";"):
                if x and x not in have:
                    p["units"] += ";" + x
            if note and note not in p["note"]:
                p["note"] += " | " + note
            return p["id"]
    i = f"PD-{len(D['pd'])+1:03d}"
    D["pd"].append({"id": i, "kind": kind, "label": label, "units": _u(units), "establishment_norm_type": ntype, "legal_multiplicity": mult,
                    "establishment_evidence": "not_assessed", "legal_status": LS_DEFAULT, "epistemic_status": ES_OPERATIVE, "note": note, "review_flag": flag})
    return i


def ext(units, source, kind, role, dep, consequence, verification="reference_text_recorded_target_not_retrieved", boundary="outside_corpus_not_expanded"):
    i = f"EXT-{len(D['ext'])+1:03d}"
    D["ext"].append({"id": i, "units": _u(units), "referenced_source": source, "source_kind": kind, "reference_role": role,
                     "source_verification_status": verification, "boundary_status": boundary, "constitutive_dependency": dep, "consequence_for_inference": consequence})
    return i


def unc(units, typ, desc, effect="", hq=""):
    i = f"UNC-{len(D['unc'])+1:03d}"
    D["unc"].append({"id": i, "units": _u(units), "type": typ, "description": desc, "effect": effect, "hq": hq})
    return i


def hq(issue, why, options="", blocking="No"):
    i = f"HQ-{len(D['hq'])+1:03d}"
    D["hq"].append({"id": i, "issue": issue, "why_it_matters": why, "options": options, "blocking": blocking})
    return i


def link(kind, field, substr, units, expect=1, origin_sub=""):
    """add supporting units to existing record(s) whose `field` contains substr (many-to-many provenance)."""
    hits = [r for r in D[kind] if substr in r.get(field, "") and (not origin_sub or origin_sub in r.get("origin", r.get("subject", "")))]
    if len(hits) != expect:
        raise ValueError(f"link({kind},{field},{substr!r}): {len(hits)} matches, expected {expect}: " + "; ".join(h['id'] + ':' + h.get(field, '')[:50] for h in hits))
    for r in hits:
        have = set(r["units"].split(";"))
        for x in _u(units).split(";"):
            if x and x not in have:
                r["units"] += ";" + x
    return [h["id"] for h in hits]
