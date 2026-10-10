# -*- coding: utf-8 -*-
"""Throwaway RA validation driver.

(a) loads a records file, (b) validates every record against reference_coding_schema.json
(jsonschema if importable, else a manual required-keys / enums / types check), and
(c) imports and calls validate_relational_logic on each record, logging every ValueError
by candidate_id.  validate_reference_logic.py is imported unmodified.
"""
from __future__ import annotations
import json, os, sys, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
STAGE = os.path.dirname(HERE)
BASE = os.path.dirname(os.path.dirname(STAGE))
SCHEMA_PATH = os.path.join(BASE, "methodology", "v1.1.0", "reference_coding_schema.json")

sys.path.insert(0, STAGE)
from validate_reference_logic import validate_relational_logic  # noqa: E402

SCHEMA = json.load(open(SCHEMA_PATH, encoding="utf-8"))

MECHANISMS = set(SCHEMA["$defs"]["mechanism"]["enum"])
CONFIDENCE = set(SCHEMA["$defs"]["confidence"]["enum"])
EV_ROLE = set(SCHEMA["$defs"]["evidence_item"]["properties"]["evidence_role"]["enum"])
EV_OBS = set(SCHEMA["$defs"]["evidence_item"]["properties"]["observability"]["enum"])
COND = set(SCHEMA["$defs"]["condition_result"]["properties"]["result"]["enum"])
SS = set(SCHEMA["properties"]["screening_status"]["enum"])
RR = set(SCHEMA["properties"]["relational_result"]["enum"])
ORIGIN = set(SCHEMA["properties"]["candidate_origin"]["enum"])
REQUIRED = set(SCHEMA["required"])
ALLOWED = set(SCHEMA["properties"].keys())
SL_REQ = set(SCHEMA["$defs"]["source_location"]["required"])
ACTOR_REQ = set(SCHEMA["$defs"]["actor"]["required"])
EVI_REQ = set(SCHEMA["$defs"]["evidence_item"]["required"])
CONDS = ("condition_A", "condition_B", "condition_C", "condition_D", "condition_E")


def manual_schema_errors(r):
    e = []
    keys = set(r.keys())
    for k in sorted(REQUIRED - keys):
        e.append("missing required key: %s" % k)
    for k in sorted(keys - ALLOWED):
        e.append("additionalProperties violation: %s" % k)
    if not isinstance(r.get("candidate_id"), str) or not r.get("candidate_id"):
        e.append("candidate_id must be a non-empty string")
    if r.get("candidate_origin") not in ORIGIN:
        e.append("candidate_origin not in enum: %r" % r.get("candidate_origin"))
    sl = r.get("source_location")
    if not isinstance(sl, dict):
        e.append("source_location must be an object")
    else:
        if set(sl.keys()) != SL_REQ:
            e.append("source_location keys %s != required %s" % (sorted(sl.keys()), sorted(SL_REQ)))
        for k, v in sl.items():
            if not (v is None or isinstance(v, str)):
                e.append("source_location.%s must be string or null" % k)
    if r.get("screening_status") not in SS:
        e.append("screening_status not in enum: %r" % r.get("screening_status"))
    if not isinstance(r.get("is_regulatory_act"), bool):
        e.append("is_regulatory_act must be boolean")
    if not (r.get("regulatory_act_type") is None or isinstance(r.get("regulatory_act_type"), str)):
        e.append("regulatory_act_type must be string or null")

    def check_actor(a, where):
        if not isinstance(a, dict):
            e.append("%s: actor must be object" % where)
            return
        if set(a.keys()) != ACTOR_REQ:
            e.append("%s: actor keys %s != %s" % (where, sorted(a.keys()), sorted(ACTOR_REQ)))
        if not isinstance(a.get("label"), str) or not a.get("label"):
            e.append("%s: actor.label must be non-empty string" % where)
        if not isinstance(a.get("role"), str) or not a.get("role"):
            e.append("%s: actor.role must be non-empty string" % where)
        refs = a.get("evidence_refs")
        if not isinstance(refs, list) or any((not isinstance(x, str) or not x) for x in refs):
            e.append("%s: actor.evidence_refs must be a list of non-empty strings" % where)

    for k in ("rule_source", "standard_setter", "direct_regulator", "oversight_authority", "enforcement_authority"):
        v = r.get(k)
        if not isinstance(v, list):
            e.append("%s must be an array" % k)
        else:
            for i, a in enumerate(v):
                check_actor(a, "%s[%d]" % (k, i))
    for k in ("R", "I", "T"):
        v = r.get(k)
        if v is None:
            continue
        if not isinstance(v, list):
            e.append("%s must be an array or null" % k)
        else:
            for i, a in enumerate(v):
                check_actor(a, "%s[%d]" % (k, i))
    for k in ("action", "object", "mediating_function", "instrument", "procedure",
              "additional_context_required", "notes"):
        v = r.get(k)
        if not isinstance(v, list) or any(not isinstance(x, str) for x in v):
            e.append("%s must be an array of strings" % k)
    rt = r.get("relational_test")
    if not isinstance(rt, dict):
        e.append("relational_test must be an object")
    else:
        if set(rt.keys()) != set(CONDS):
            e.append("relational_test keys %s != %s" % (sorted(rt.keys()), sorted(CONDS)))
        for c in CONDS:
            cv = rt.get(c)
            if not isinstance(cv, dict):
                e.append("%s must be an object" % c)
                continue
            if set(cv.keys()) != {"result", "evidence_refs"}:
                e.append("%s keys %s invalid" % (c, sorted(cv.keys())))
            if cv.get("result") not in COND:
                e.append("%s.result not in enum: %r" % (c, cv.get("result")))
            refs = cv.get("evidence_refs")
            if not isinstance(refs, list) or any((not isinstance(x, str) or not x) for x in refs):
                e.append("%s.evidence_refs must be a list of non-empty strings" % c)
    if r.get("relational_result") not in RR:
        e.append("relational_result not in enum: %r" % r.get("relational_result"))
    if r.get("primary_mechanism") not in MECHANISMS:
        e.append("primary_mechanism not in enum: %r" % r.get("primary_mechanism"))
    sm = r.get("secondary_mechanisms")
    if not isinstance(sm, list) or any(x not in MECHANISMS for x in sm):
        e.append("secondary_mechanisms must be an array of mechanism enums")
    evs = r.get("evidence_items")
    if not isinstance(evs, list):
        e.append("evidence_items must be an array")
    else:
        for i, ev in enumerate(evs):
            if not isinstance(ev, dict):
                e.append("evidence_items[%d] must be object" % i)
                continue
            if set(ev.keys()) != EVI_REQ:
                e.append("evidence_items[%d] keys %s != %s" % (i, sorted(ev.keys()), sorted(EVI_REQ)))
            for f in ("evidence_id", "location", "quote"):
                if not isinstance(ev.get(f), str) or not ev.get(f):
                    e.append("evidence_items[%d].%s must be non-empty string" % (i, f))
            if ev.get("evidence_role") not in EV_ROLE:
                e.append("evidence_items[%d].evidence_role not in enum" % i)
            if ev.get("observability") not in EV_OBS:
                e.append("evidence_items[%d].observability not in enum" % i)
            sup = ev.get("supports")
            if not isinstance(sup, list) or any((not isinstance(x, str) or not x) for x in sup):
                e.append("evidence_items[%d].supports must be a list of non-empty strings" % i)
    if r.get("confidence") not in CONFIDENCE:
        e.append("confidence not in enum: %r" % r.get("confidence"))
    if not isinstance(r.get("interpretive_note"), str):
        e.append("interpretive_note must be a string")
    return e


def main(path):
    records = json.load(open(path, encoding="utf-8"))
    digest = hashlib.sha256(open(path, "rb").read()).hexdigest()
    print("FILE:", path)
    print("SHA256:", digest)
    print("RECORDS:", len(records))

    try:
        import jsonschema
        validator_cls = jsonschema.validators.validator_for(SCHEMA)
        validator_cls.check_schema(SCHEMA)
        v = validator_cls(SCHEMA)
        mode = "jsonschema %s" % jsonschema.__version__
    except Exception as exc:  # noqa: BLE001
        v = None
        mode = "manual (jsonschema unavailable: %s)" % exc.__class__.__name__
    print("SCHEMA VALIDATION MODE:", mode)

    schema_fail = 0
    logic_fail = 0
    for r in records:
        cid = r.get("candidate_id", "<no id>")
        errs = []
        if v is not None:
            errs = ["%s -> %s" % ("/".join(str(p) for p in err.absolute_path), err.message)
                    for err in sorted(v.iter_errors(r), key=lambda e: list(e.absolute_path))]
        errs += manual_schema_errors(r)
        if errs:
            schema_fail += 1
            for m in errs:
                print("SCHEMA ERROR [%s]: %s" % (cid, m))
        try:
            validate_relational_logic(r)
        except ValueError as exc:
            logic_fail += 1
            print("LOGIC ValueError [%s]: %s" % (cid, exc))
        except Exception as exc:  # noqa: BLE001
            logic_fail += 1
            print("LOGIC %s [%s]: %s" % (exc.__class__.__name__, cid, exc))

    print("SUMMARY: records=%d schema_invalid=%d logic_errors=%d valid=%d"
          % (len(records), schema_fail, logic_fail,
             sum(1 for r in records
                 if not manual_schema_errors(r) and _ok(r))))


def _ok(r):
    try:
        validate_relational_logic(r)
        return True
    except Exception:
        return False


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "RA_4way_output_raw.json")
    main(target)
