"""Candidate subconfigurations (S) for GDPR Pilot 01 — rule-based, reproducible, provisional.
Each candidate is defined by an explicit predicate over extracted records (NA/QR) written AFTER extraction, from relation patterns
(not from chapter boundaries). Outputs: sc_data.json (members, positions, chapters, overlaps, unassigned records).
Run: python reconstruct.py
"""
import json, os, re, itertools, collections
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
D = json.load(open(os.path.join(ROOT, "03_EXTRACTION", "_store.json"), encoding="utf-8"))
pdlab = {p["id"]: p["label"] for p in D["pd"]}


def fix(v):
    v = re.sub(r"PD-\d{3}", lambda m: pdlab.get(m.group(0), m.group(0)), v or "")
    return v.replace("supervisory authority concerneds", "supervisory authorities concerned")


def tags(label):
    l = fix(label).lower()
    t = set()
    if re.search(r"\bcontrollers?\b", l) and "other processor" not in l: t.add("CTRL")
    if "processor" in l: t.add("PROC")
    if "data subject" in l or "complainant" in l or "injured person" in l or "person who suffered" in l: t.add("DS")
    if "supervisory authorit" in l or re.search(r"\bsas?\b", l) or "lead supervisory" in l: t.add("SA")
    if "board" in l and "management" not in l and "board of the controlling" not in l: t.add("BOARD")
    if "commission" in l: t.add("COMM")
    if "member state" in l: t.add("MS")
    if "parliament" in l and "national" not in l: t.add("EPC")
    if "national parliament" in l or "national institutions" in l or "government" in l: t.add("NATINST")
    if "court" in l or "judicial" in l: t.add("COURT")
    if "data protection officer" in l or l.strip() == "dpo": t.add("DPO")
    if "certification body" in l: t.add("CB")
    if "monitoring body" in l: t.add("MON")
    if "accreditation body" in l: t.add("NAB")
    if "association" in l and "representing" in l: t.add("ASSOC")
    if "third countr" in l or "international organisation" in l: t.add("THIRD")
    if "committee" in l: t.add("COMMITTEE")
    if "not-for-profit" in l: t.add("ORG")
    return t


def arts(units):
    return sorted({int(re.match(r"GDPR\.A(\d+)", u).group(1)) for u in units.split(";") if u})


def chapter(a):
    for lo, hi, name in [(1, 4, "I"), (5, 11, "II"), (12, 23, "III"), (24, 43, "IV"), (44, 50, "V"), (51, 59, "VI"), (60, 76, "VII"), (77, 84, "VIII"), (85, 91, "IX"), (92, 93, "X"), (94, 99, "XI")]:
        if lo <= a <= hi:
            return name


recs = []
for r in D["qr"]:
    recs.append({"kind": "QR", "id": r["id"], "units": r["units"], "A": arts(r["units"]), "origin": fix(r["origin"]), "counterpart": fix(r["counterpart"]), "type": r["relation_type"], "text": (fix(r["object"]) + " " + fix(r["function"])).lower(), "dep": fix(r.get("depends_on", "")).lower(), "ext": r.get("external_dependency", ""), "acc": r.get("accountability_class", "")})
for r in D["na"]:
    recs.append({"kind": "NA", "id": r["id"], "units": r["units"], "A": arts(r["units"]), "origin": fix(r["subject"]), "counterpart": fix(r["counterpart"]), "type": "", "text": (fix(r["object"]) + " " + fix(r["function"])).lower(), "dep": fix(r.get("depends_on", "")).lower(), "ext": "", "acc": ""})
for r in recs:
    r["T"] = tags(r["origin"]) | tags(r["counterpart"])
    r["To"] = tags(r["origin"]); r["Tc"] = tags(r["counterpart"])


def inA(r, *rng):
    s = set()
    for x in rng:
        s |= set(range(x[0], x[1] + 1)) if isinstance(x, tuple) else {x}
    return bool(set(r["A"]) & s)


SC = collections.OrderedDict()
SC["SC-01"] = ("Individual information, access and control rights against controllers",
               "Controller obligations toward the data subject (information, access, rectification, erasure, objection, notices) stated as qualified relations",
               "How does the instrument organize the individual's position vis-à-vis the controller?",
               lambda r: r["kind"] == "QR" and {"CTRL", "DS"} <= r["T"] and not inA(r, (77, 84)) or (r["kind"] == "QR" and inA(r, (12, 22)) and "DS" in r["T"]))
SC["SC-02"] = ("Supervisory-authority oversight and enforcement over controllers and processors",
               "SA–controller/processor relations: notification, records, cooperation, prior consultation, investigative and corrective powers, fines",
               "How are monitoring and enforcement of compliance allocated to public supervisory authorities?",
               lambda r: r["kind"] == "QR" and "SA" in r["T"] and (r["T"] & {"CTRL", "PROC"}) and "BOARD" not in r["T"] and "COURT" not in r["T"])
SC["SC-03"] = ("Controller–processor delegation, instruction and audit",
               "Contractual delegation of processing, authorization of sub-processing, instructions, audit, notification, liability allocation",
               "How is processing work delegated within the regulated side and how is the delegate controlled?",
               lambda r: r["kind"] == "QR" and {"CTRL", "PROC"} <= r["T"] and "DS" not in r["T"] and "SA" not in r["T"] or (r["kind"] == "NA" and inA(r, 28, 29)))
SC["SC-04"] = ("Internal compliance function (data protection officer)",
               "Designation, independence, tasks and reporting of the DPO; interface to the SA",
               "How is an internal monitoring and advisory function placed inside regulated organisations?",
               lambda r: "DPO" in r["T"] or (r["kind"] == "NA" and inA(r, (37, 39))))
SC["SC-05"] = ("Codes of conduct: approval, accreditation of monitors, monitoring and sanction",
               "Associations draft codes; SA/Board approve; SA accredits monitoring bodies; monitoring bodies monitor and sanction adherents and report to the SA",
               "How is private rule-making by representative bodies authorised, monitored and linked to public supervision?",
               lambda r: inA(r, (40, 41)) or "MON" in r["T"] or "ASSOC" in r["T"] or "code of conduct" in r["dep"])
SC["SC-06"] = ("Certification: accreditation of certification bodies, issue/withdrawal of certification, approval of criteria",
               "SA/national accreditation body accredit certification bodies; bodies certify controllers; SA/Board approve criteria; SA withdraws certification",
               "How is assurance by third-party certifiers authorised and linked to public supervision?",
               lambda r: inA(r, (42, 43)) or ("CB" in r["T"]) or "certification mechanism" in r["dep"] or "Art.42" in r["dep"] or "Arts 42" in r["dep"])
SC["SC-07"] = ("Cooperation and consistency among supervisory authorities, the Board and the Commission",
               "Lead-authority competence, consultation on draft decisions, objections, escalation to the Board, binding decisions, opinions, urgency measures, mutual assistance, joint operations",
               "How is the application of the Regulation kept consistent across several national authorities?",
               lambda r: inA(r, 51, 56, (60, 66), 70, 64, 65) and ("SA" in r["T"] or "BOARD" in r["T"]) or ("consistency mechanism" in r["dep"]) or ("BOARD" in r["T"] and "SA" in r["T"]))
SC["SC-08"] = ("Commission rule-making (delegated and implementing acts) and its control",
               "Delegated and implementing competences; legislature's revocation/objection; committee procedure; Board advice to the Commission",
               "How is secondary rule-making allocated to the Commission and controlled?",
               lambda r: ("COMM" in r["To"] and ("rule-making" in r["text"] or "delegated" in r["text"] or "implementing" in r["text"])) or inA(r, (92, 93)) or ("BOARD" in r["T"] and "COMM" in r["T"] and "advice" in r["text"] or "opinion" in r["text"] and "COMM" in r["T"]))
SC["SC-09"] = ("Transfers of personal data to third countries and international organisations",
               "Adequacy decisions by the Commission, safeguards, BCR approval, SA authorisation of clauses, derogations, international cooperation",
               "How is the permissibility of transfers organized across Commission, SAs and controllers?",
               lambda r: inA(r, (44, 50)) or "THIRD" in r["T"] or "Art.46" in r["dep"] or "bcr" in r["text"] or "binding corporate" in r["text"])
SC["SC-10"] = ("Remedies and judicial review",
               "Complaint to the SA, judicial remedy against SA decisions and inaction, remedies against controllers/processors, representation, compensation, court coordination, court-imposed fines",
               "How can individuals contest controllers and supervisory authorities?",
               lambda r: inA(r, (77, 82)) or "COURT" in r["T"] or "ORG" in r["T"] or (r["kind"] == "QR" and "complaint" in r["text"]))
SC["SC-11"] = ("Member State specification, establishment and notification duties",
               "Duties and competences of Member States to establish authorities, specify rules, provide penalties and notify the Commission",
               "How is the Regulation's application delegated to national law and reported upward?",
               lambda r: "MS" in r["To"] or "member state law" in r["dep"] or "Member State law" in r["ext"])
SC["SC-12"] = ("Reporting lines to institutions",
               "Annual or periodic reports from SAs, the Board and the Commission; notification of delegated acts; classification INFO/ANSWERABILITY by DR-10",
               "To whom do public bodies report, and with what capacities attached?",
               lambda r: r["kind"] == "QR" and r["type"] == "information/reporting" and (("EPC" in r["Tc"]) or ("NATINST" in r["Tc"]) or (r["acc"] != "" and ("annual" in r["text"] or "report" in r["text"]))) )

SC["SC-13"] = ("Constitution and internal organisation of the European Data Protection Board",
               "Establishment (N1), composition, independence, chair, secretariat, procedure, confidentiality",
               "How is the Union-level body constituted and organised?",
               lambda r: inA(r, (68, 69), (71, 76)) and ("BOARD" in r["To"] or "chair" in (r["origin"] + r["counterpart"]).lower() or "secretariat" in (r["origin"] + r["counterpart"]).lower() or "EDPS" in r["origin"] or "Supervisor" in r["origin"]) and "SA" not in r["Tc"] or inA(r, 68))
SC["SC-14"] = ("Constitution, independence and competence of national supervisory authorities",
               "Obligation to provide for authorities (N2), independence, resources, members' appointment, competence allocation, tasks and powers conferred",
               "How are national authorities brought into being and equipped, and whose competence do they hold?",
               lambda r: inA(r, (51, 55), 57, 58) and ("SA" in r["To"] or "MS" in r["To"] or "member" in r["origin"].lower()))
SC["SC-15"] = ("Regulated-side assignments without an identifiable counterpart (self-regulatory duties)",
               "Normative assignments on controllers/processors/representatives with no legally identifiable counterparty",
               "Which duties of the regulated side are stated without a legally identified recipient or forum?",
               lambda r: r["kind"] == "NA" and (r["To"] & {"CTRL", "PROC"}) and not (r["Tc"] - {"CTRL", "PROC"}) and r["counterpart"].strip() in ("", "none"))
members = {k: [r for r in recs if v[3](r)] for k, v in SC.items()}
out = {"sc": {}, "unassigned": [], "overlap": {}}
for k, (name, pattern, question, _) in SC.items():
    ms = members[k]
    chs = sorted({chapter(a) for r in ms for a in r["A"]}, key=lambda x: ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI"].index(x))
    units = sorted({u for r in ms for u in r["units"].split(";") if u})
    pos = collections.Counter()
    for r in ms:
        for t in r["T"]:
            pos[t] += 1
    out["sc"][k] = {"name": name, "pattern": pattern, "question": question, "n_qr": sum(1 for r in ms if r["kind"] == "QR"), "n_na": sum(1 for r in ms if r["kind"] == "NA"),
                    "ids": [r["id"] for r in ms], "chapters": chs, "n_units": len(units), "units": units, "positions": dict(pos), "n_articles": len({a for r in ms for a in r["A"]})}
for a, b in itertools.combinations(SC, 2):
    sa, sb = {r["id"] for r in members[a]}, {r["id"] for r in members[b]}
    out["overlap"][f"{a}|{b}"] = len(sa & sb)
assigned = {r["id"] for ms in members.values() for r in ms}
out["unassigned"] = [{"id": r["id"], "units": r["units"], "origin": r["origin"], "counterpart": r["counterpart"], "text": r["text"][:110]} for r in recs if r["id"] not in assigned]
out["totals"] = {"records": len(recs), "assigned": len(assigned), "unassigned": len(out["unassigned"])}
json.dump(out, open(os.path.join(HERE, "sc_data.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for k, v in out["sc"].items():
    print(k, v["name"][:60], "| QR", v["n_qr"], "NA", v["n_na"], "| articles", v["n_articles"], "| chapters", ",".join(v["chapters"]))
print(out["totals"])
top = sorted(out["overlap"].items(), key=lambda x: -x[1])[:12]
print(top)
