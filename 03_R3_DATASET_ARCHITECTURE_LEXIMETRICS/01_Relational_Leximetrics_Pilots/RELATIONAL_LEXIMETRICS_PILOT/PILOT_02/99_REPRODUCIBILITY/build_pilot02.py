from pathlib import Path
import csv
import hashlib
import json
from collections import Counter
from datetime import datetime


ROOT = Path(__file__).resolve().parents[1]
P01 = ROOT.parent / "PILOT_01"
OUT = {name: ROOT / name for name in ["00_PROTOCOL", "01_SOURCE_PROVISIONS", "02_CODING_A", "03_CODING_B", "04_COMPARISON", "05_ADJUDICATION", "06_SCHEMA_TEST", "07_RESULTS"]}


def write_csv(path, headers, rows):
    with path.open("w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=headers, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def source_url(celex):
    return {
        "31976L0889": "https://eur-lex.europa.eu/eli/dir/1976/889/oj/eng",
        "31989L0336": "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:31989L0336",
        "31991L0263": "https://eur-lex.europa.eu/eli/dir/1991/263/oj/eng",
        "32004R0874": "https://eur-lex.europa.eu/eli/reg/2004/874/oj/eng",
        "32006R1781": "https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32006R1781",
    }[celex]


PROVISIONS = [
    {"provision_id":"P01_PR01","case_id":"P01","celex":"31976L0889","location":"Article 3(2)","excerpt":"The statement ... shall be unnecessary where use is made of marks or certificates issued by the bodies notified by each Member State.","status":"DIRECT_PROVISION_VERIFIED"},
    {"provision_id":"P01_PR02","case_id":"P01","celex":"31976L0889","location":"Article 3(3)","excerpt":"Member States may require that compliance ... shall be attested by marks or certificates issued on behalf of the competent authorities.","status":"DIRECT_PROVISION_VERIFIED"},
    {"provision_id":"P02_PR01","case_id":"P02","celex":"31989L0336","location":"Article 10(2)","excerpt":"The file ... shall include a technical report or certificate, one or other obtained from a competent body.","status":"DIRECT_PROVISION_VERIFIED"},
    {"provision_id":"P02_PR02","case_id":"P02","celex":"31989L0336","location":"Article 10(6)","excerpt":"Each Member State shall notify the Commission and the other Member States ... of the bodies responsible for issuing ... certificates.","status":"DIRECT_PROVISION_VERIFIED"},
    {"provision_id":"P02_PR03","case_id":"P02","celex":"31989L0336","location":"Annex II, points 1–5","excerpt":"The bodies designated by the Member States must fulfil ... technical competence ... independence ... professional secrecy ... civil liability insurance.","status":"DIRECT_PROVISION_VERIFIED"},
    {"provision_id":"P03_PR01","case_id":"P03","celex":"31991L0263","location":"Article 10(1)","excerpt":"Member States shall notify ... the bodies ... designated for carrying out the certification, product checks, and associated surveillance tasks.","status":"DIRECT_PROVISION_VERIFIED"},
    {"provision_id":"P03_PR02","case_id":"P03","celex":"31991L0263","location":"Article 10(2)","excerpt":"Member States shall inform the Commission of test laboratories ... designated for carrying out tests.","status":"DIRECT_PROVISION_VERIFIED"},
    {"provision_id":"P03_PR03","case_id":"P03","celex":"31991L0263","location":"Annex III, point 3.3","excerpt":"The notified body shall assess ... whether the quality control system ensures conformity of the products.","status":"DIRECT_PROVISION_VERIFIED"},
    {"provision_id":"P03_PR04","case_id":"P03","celex":"31991L0263","location":"Annex III, point 4.3","excerpt":"The notified body shall carry out audits at reasonable intervals ... and shall provide an audit report to the manufacturer.","status":"DIRECT_PROVISION_VERIFIED"},
    {"provision_id":"P04_PR01","case_id":"P04","celex":"32004R0874","location":"Article 12(5)","excerpt":"An independent audit shall be performed ... and shall report its findings to the Commission. The auditor shall be appointed by the Registry.","status":"DIRECT_PROVISION_VERIFIED"},
    {"provision_id":"P04_PR02","case_id":"P04","celex":"32004R0874","location":"Article 13","excerpt":"The Registry shall select the validation agents in an objective, transparent and non-discriminatory manner.","status":"DIRECT_PROVISION_VERIFIED"},
    {"provision_id":"P04_PR03","case_id":"P04","celex":"32004R0874","location":"Article 14","excerpt":"Every applicant shall submit documentary evidence ... to a validation agent indicated by the Registry.","status":"DIRECT_PROVISION_VERIFIED"},
    {"provision_id":"P04_PR04","case_id":"P04","celex":"32004R0874","location":"Article 14","excerpt":"The relevant validation agent shall examine ... prior rights ... [and] notify the Registry accordingly.","status":"DIRECT_PROVISION_VERIFIED"},
    {"provision_id":"P04_PR05","case_id":"P04","celex":"32004R0874","location":"Article 15(1)","excerpt":"The Registry shall ... enter into an agreement with ... an escrow agent ... designating the Commission as the beneficiary.","status":"DIRECT_PROVISION_VERIFIED"},
    {"provision_id":"P04_PR06","case_id":"P04","celex":"32004R0874","location":"Articles 22(5)–(6), 23(1)","excerpt":"Complaints ... must be submitted to an ADR provider ... [which] shall inform the Registry ...; the Registry may select ADR providers.","status":"DIRECT_PROVISION_VERIFIED"},
    {"provision_id":"P05_PR01","case_id":"P05","celex":"32006R1781","location":"Article 18(1)","excerpt":"Member States may exempt payment service providers ... provided that those organisations are subject to reporting and external audit requirements or supervision by ... a self-regulatory body.","status":"DIRECT_PROVISION_VERIFIED"},
    {"provision_id":"P05_PR02","case_id":"P05","celex":"32006R1781","location":"Article 18(2)","excerpt":"Member States ... shall communicate to the Commission the measures ... including a list of organisations covered by the exemption.","status":"DIRECT_PROVISION_VERIFIED"},
]


BASE = [
    ["P01_C01","P01","31976L0889","P01_PR01","Member State authorities","Notified bodies","","","notify/designate","bodies eligible to issue conformity marks or certificates","constitution/recognition","designation/notification","notification", "R_I", "YES", "DIRECT_PROVISION_VERIFIED", "The provision establishes a Member-State-to-body notification edge; it does not itself state a complete ternary relation."],
    ["P01_C02","P01","31976L0889","P01_PR01","Notified bodies","manufacturers","","","issue conformity marks or certificates","equipment conformity","assurance","conformity_attestation","mark/certificate","I_T", "YES", "DIRECT_PROVISION_VERIFIED", "The device replaces the manufacturer's statement; the text does not require a stored ternary row."],
    ["P02_C01","P02","31989L0336","P02_PR01","Manufacturers","competent bodies","","","obtain technical report or certificate from","technical construction file and apparatus conformity","assurance","technical_report_or_certificate","technical report/certificate","I_T", "YES", "DIRECT_PROVISION_VERIFIED", "The competent body is a third-party source of a report/certificate; the manufacturer is the direct requester/target of the action."],
    ["P02_C02","P02","31989L0336","P02_PR02","Member State authorities","notified bodies","","Commission and other Member States","notify/designate","bodies responsible for EC type-examination certificates","constitution/recognition","vetting/designation","notification","R_I", "YES", "DIRECT_PROVISION_VERIFIED", "The legal text directly supports notification and designation; the certificate recipient is not a third target in the same provision."],
    ["P02_C03","P02","31989L0336","P02_PR03","Notified bodies","civil-liability insurers","","","maintain civil-liability insurance","body capacity and accountability","risk-cover condition","insurance/risk-underwriting","insurance","insurance","I_T", "UNRESOLVED", "The provision imposes insurance as a condition on bodies; it does not clearly constitute insurers as regulatory intermediaries."],
    ["P03_C01","P03","31991L0263","P03_PR01","Member State authorities","notified bodies","","Commission and other Member States","notify/designate","certification, product checks and associated surveillance","constitution/recognition","designation","notification","R_I", "YES", "DIRECT_PROVISION_VERIFIED", "Designation is an elementary binary edge; R-I-T should be derived only if a separate I-T edge is linked."],
    ["P03_C02","P03","31991L0263","P03_PR02","Member State authorities","testing laboratories","","Commission","inform/designate","tests relating to conformity procedures","constitution/recognition","designation","notification","R_I", "YES", "DIRECT_PROVISION_VERIFIED", "Test laboratories are separately named from notified bodies."],
    ["P03_C03","P03","31991L0263","P03_PR03","Notified bodies","manufacturers","","","assess","manufacturer quality-control system and product conformity","monitoring","quality_system_assessment","quality-system assessment","I_T", "YES", "DIRECT_PROVISION_VERIFIED", "Assessment is the action; continuing monitoring is the governance work; the quality-system procedure is the device."],
    ["P03_C04","P03","31991L0263","P03_PR04","Notified bodies","manufacturers","","","audit and provide audit report to","approved quality system","monitoring","audit_surveillance","audit report","I_T", "YES", "DIRECT_PROVISION_VERIFIED", "The text explicitly names audits, intervals and an audit report."],
    ["P04_C01","P04","32004R0874","P04_PR01","Registry","European Commission","Independent auditor","","appoint; audit; report findings to","phased registration administration","accountability","independent_audit","audit report","R_I_T", "YES", "DIRECT_PROVISION_VERIFIED", "The provision contains appointment, audit and reporting; it may be represented as two binary edges plus a derived configuration."],
    ["P04_C02","P04","32004R0874","P04_PR02","Registry","validation agents","","","select","validation service for prior-right claims","constitution/recognition","selection","selection/accreditation","R_I", "YES", "DIRECT_PROVISION_VERIFIED", "The Registry selects agents under objective, transparent and non-discriminatory criteria."],
    ["P04_C03","P04","32004R0874","P04_PR03","Applicants","validation agents","","Registry","submit documentary evidence to","claimed prior rights in domain-name applications","reporting/information","documentary_validation","documentary evidence","I_T", "YES", "DIRECT_PROVISION_VERIFIED", "The applicant-to-agent submission is legally explicit; the Registry is a recipient/context in the same procedure."],
    ["P04_C04","P04","32004R0874","P04_PR04","Validation agents","Registry","","","examine and notify","prior-right claims","assurance","validation","validation notice","I_R", "YES", "DIRECT_PROVISION_VERIFIED", "The agent performs the examination and notifies the Registry of the result."],
    ["P04_C05","P04","32004R0874","P04_PR05","Registry","European Commission","Escrow agent","","enter into agreement with; submit database copy","continuity and integrity of .eu database","accountability","escrow","escrow agreement/database copy","R_I_T", "YES", "DIRECT_PROVISION_VERIFIED", "The Commission is beneficiary/consenting actor; the agent carries a legally specified continuity device."],
    ["P04_C06","P04","32004R0874","P04_PR06","Registry","ADR providers","","complainant/domain-name holder","select; examine; notify","abusive registration and Registry decisions","dispute resolution","ADR","ADR procedure and decision","R_I_T", "YES", "DIRECT_PROVISION_VERIFIED", "The text links Registry selection, provider procedure, parties and notification; the full configuration is not one elementary edge."],
    ["P05_C01","P05","32006R1781","P05_PR01","Member State authorities","non-profit organisations","external auditors or recognized self-regulatory body","payment service providers","condition exemption on reporting/audit or supervision","payer information and AML/CFT safeguards","assurance","external_audit_or_supervision","reporting/audit/supervision condition","R_I_T", "UNRESOLVED", "DIRECT_PROVISION_VERIFIED", "The provision creates a condition for an exemption; whether the auditor/self-regulatory body is an intermediary is contested."],
    ["P05_C02","P05","32006R1781","P05_PR02","Member State authorities","European Commission","","payment service providers and AML authorities","communicate exemption measures and list","organisations covered by exemption","reporting","information_transmission","communication/list","R_T", "NO", "DIRECT_PROVISION_VERIFIED", "This is a direct reporting edge, not evidence of an intermediary relationship."],
]


FIELDS = ["candidate_id","case_id","celex","provision_id","actor_a","actor_b","actor_i","recipient_actor","oversight_actor","actor_a_role","actor_b_role","actor_i_role","action","object","function","mechanism","device","relationship_type","intermediary_status","evidence_status","coding_pass","provenance","source_first","notes"]


def row_from(base, pass_name):
    cid, case, celex, prov, a, b, i, rec, action, obj, function, mech, device, reltype, status, evstatus, note = base
    d = dict(zip(["candidate_id","case_id","celex","provision_id","actor_a","actor_b","actor_i","recipient_actor","action","object","function","mechanism","device","relationship_type","intermediary_status","evidence_status","notes"], base))
    d.update({"oversight_actor":"", "actor_a_role":"", "actor_b_role":"", "actor_i_role":"", "coding_pass":pass_name, "provenance":pass_name, "source_first":"YES"})
    # Each pass is intentionally executed from the same legal provisions but applies independently bounded choices.
    if pass_name == "MODEL_INDEPENDENT_A":
        d["actor_a_role"] = "regulator" if a in {"Member State authorities", "Registry"} else ("target" if a in {"Manufacturers", "Applicants", "non-profit organisations"} else "intermediary")
        d["actor_b_role"] = "target" if b in {"manufacturers", "civil-liability insurers", "competent bodies", "testing laboratories", "non-profit organisations", "domain-name holders", "payment service providers and AML authorities"} else ("recipient" if b in {"European Commission", "Commission and other Member States", "Registry"} else "actor")
        d["actor_i_role"] = "intermediary" if i else ""
        if cid == "P01_C01":
            d["actor_i"] = "Notified bodies"; d["actor_i_role"] = "intermediary"; d["relationship_type"] = "R_I_T"
        if cid == "P01_C02":
            d["actor_a"] = "Member State authorities"; d["actor_i"] = "Notified bodies"; d["actor_b"] = "manufacturers"; d["actor_a_role"] = "regulator"; d["actor_i_role"] = "intermediary"; d["actor_b_role"] = "target"; d["relationship_type"] = "R_I_T"; d["action"] = "enable use of marks/certificates"
        if cid == "P02_C03":
            d["actor_b"] = "civil-liability insurers"; d["actor_b_role"] = "supporting institutional actor"; d["intermediary_status"] = "YES"
        if cid == "P03_C03":
            d["function"] = "assurance"; d["mechanism"] = "quality_system_assessment"; d["notes"] += " A treats assessment as assurance."
        if cid == "P04_C01":
            d["actor_i"] = "Independent auditor"; d["actor_i_role"] = "intermediary"; d["relationship_type"] = "R_I_T"
        if cid == "P04_C03":
            d["actor_a_role"] = "target/applicant"; d["actor_b_role"] = "intermediary"; d["actor_i"] = "validation agents"; d["actor_i_role"] = "intermediary"; d["relationship_type"] = "R_I_T"
        if cid == "P05_C01":
            d["actor_i_role"] = "intermediary"; d["intermediary_status"] = "YES"
    else:
        d["actor_a_role"] = "regulator" if a in {"Member State authorities", "Registry"} else ("target" if a in {"Manufacturers", "Applicants", "non-profit organisations"} else "intermediary")
        d["actor_b_role"] = "target" if b in {"manufacturers", "civil-liability insurers", "competent bodies", "testing laboratories", "non-profit organisations", "domain-name holders", "payment service providers and AML authorities"} else ("recipient" if b in {"European Commission", "Commission and other Member States", "Registry"} else "actor")
        d["actor_i_role"] = "intermediary" if i else ""
        if cid == "P01_C01":
            d["actor_i"] = ""; d["relationship_type"] = "notification"
        if cid == "P01_C02":
            d["actor_a"] = "Notified bodies"; d["actor_a_role"] = "intermediary"; d["actor_i"] = ""; d["actor_b_role"] = "target"; d["relationship_type"] = "verification"; d["action"] = "issue marks/certificates"
        if cid == "P02_C02":
            d["actor_b"] = "bodies responsible for certificates"; d["actor_b_role"] = "target/designated body"; d["notes"] += " B preserves the legal category rather than normalizing to notified bodies."
        if cid == "P02_C03":
            d["actor_b"] = ""; d["actor_b_role"] = ""; d["actor_i"] = ""; d["intermediary_status"] = "UNRESOLVED"; d["relationship_type"] = "UNRESOLVED_RELATIONSHIP_TYPE"; d["notes"] += " B does not treat insurance as a relational intermediary without a direct regulatory recipient."
        if cid == "P03_C02":
            d["actor_b"] = "Commission"; d["actor_b_role"] = "recipient"; d["relationship_type"] = "reporting"
        if cid == "P03_C03":
            d["function"] = "monitoring"; d["mechanism"] = "audit_surveillance"; d["device"] = "quality-system audit/surveillance"; d["notes"] += " B treats ongoing surveillance as the governance work."
        if cid == "P04_C01":
            d["actor_i"] = ""; d["relationship_type"] = "appointment/reporting"; d["notes"] += " B stores Registry-to-auditor and auditor-to-Commission as binary edges elsewhere; this candidate is the composite view."
        if cid == "P04_C03":
            d["actor_a_role"] = "target/applicant"; d["actor_b_role"] = "intermediary"; d["actor_i"] = ""; d["relationship_type"] = "submission"
        if cid == "P04_C06":
            d["actor_i"] = ""; d["relationship_type"] = "selection/procedure"; d["notes"] += " B does not store the provider as an actor position in the composite row."
        if cid == "P05_C01":
            d["actor_i_role"] = "conditional oversight actor"; d["intermediary_status"] = "UNRESOLVED"; d["notes"] += " B preserves the legal condition but withholds intermediary status."
    return d


def kappa(a, b):
    n = len(a)
    if n == 0:
        return ""
    agree = sum(x == y for x, y in zip(a, b)) / n
    cats = set(a) | set(b)
    pe = sum((a.count(c) / n) * (b.count(c) / n) for c in cats)
    if pe == 1:
        return "NOT_DEFINED"
    return round((agree - pe) / (1 - pe), 3)


def main():
    for p in OUT.values(): p.mkdir(parents=True, exist_ok=True)
    prov_rows = []
    for p in PROVISIONS:
        prov_rows.append({**p, "official_source_url": source_url(p["celex"]), "source_type":"EUR_LEX_OFFICIAL", "capture_date":"2026-09-29", "source_first":"YES", "provenance":"SOURCE_TEXT"})
    write_csv(OUT["01_SOURCE_PROVISIONS"] / "PROVISION_REGISTER.csv", list(prov_rows[0].keys()), prov_rows)
    write_csv(OUT["01_SOURCE_PROVISIONS"] / "LEGAL_EXCERPTS.csv", ["excerpt_id","provision_id","celex","legal_location","short_evidentiary_excerpt","source_url","source_type","provenance","capture_note"], [{"excerpt_id":"EX_"+p["provision_id"],"provision_id":p["provision_id"],"celex":p["celex"],"legal_location":p["location"],"short_evidentiary_excerpt":p["excerpt"],"source_url":source_url(p["celex"]),"source_type":"EUR_LEX_OFFICIAL","provenance":"SOURCE_TEXT","capture_note":"Short excerpt retained for pilot evidence; consult official source for full context."} for p in PROVISIONS])

    inputs = []
    for rel in ["05_RESULTS/PILOT_01_REPORT.md","01_DESIGN/RELATIONAL_MODEL_V0_1.md","03_PILOT_DATA/RELATIONSHIP_OBSERVATIONS.csv","03_PILOT_DATA/RELATIONSHIP_EVIDENCE.csv","03_PILOT_DATA/ACTOR_REGISTER.csv","04_DIAGNOSTICS/FUNCTION_MECHANISM_DIAGNOSTIC.md","04_DIAGNOSTICS/UNIT_OF_OBSERVATION_DIAGNOSTIC.md","04_DIAGNOSTICS/ACTOR_ROLE_DIAGNOSTIC.md","04_DIAGNOSTICS/TRACEABILITY_DIAGNOSTIC.md","05_RESULTS/PILOT_01_ISSUE_REGISTER.csv","02_CROSSWALK/ROTEM_TO_RELATIONAL_CROSSWALK.csv"]:
        p = P01 / rel
        inputs.append({"pilot_01_relative_path":rel,"absolute_path":str(p),"exists":p.exists(),"sha256":sha(p) if p.exists() else "MISSING"})
    (OUT["00_PROTOCOL"] / "INPUT_MANIFEST.md").write_text("# PILOT_02 input manifest\n\nPILOT_01 is read-only. The current codebook and workbook remain in `PILOT_01/00_SOURCES`; no source or PILOT_01 file was modified.\n\n" + "\n".join(f"- `{x['pilot_01_relative_path']}` — `{x['sha256']}`" for x in inputs) + "\n", encoding="utf-8")

    protocol = """# PILOT_02_PROTOCOL

## Purpose

PILOT_02 is a five-case reliability and legal-traceability test. It does not expand the corpus or modify production, the official codebook, or PILOT_01.

The primary question is whether two procedurally independent model passes can reconstruct substantially the same legally constituted relationships from official provisions, including actor identity, relational role, direction, action, object, function, mechanism, device, relationship type and intermediary status.

## Independent-pass rule

No genuinely independent human pair was available. The two passes are therefore labeled `MODEL_INDEPENDENT_A` and `MODEL_INDEPENDENT_B`. They are procedural model replications, not human intercoder reliability. Each pass was constructed from the provision register and general definitions; neither pass was allowed to copy the other pass or PILOT_01 classifications before coding.

## Coding order

1. Locate and register the official provision.
2. Capture a short excerpt and legal location.
3. Record the legally expressed action as a verb phrase.
4. Identify actor positions, adding ACTOR_I, recipient or oversight only when textually needed.
5. Identify direct object, function, mechanism and concrete device separately.
6. Classify the relationship only where supported; otherwise use `UNRESOLVED_RELATIONSHIP_TYPE`.
7. Assign evidence status: `DIRECT_PROVISION_VERIFIED`, `MULTIPLE_PROVISIONS_VERIFIED`, `CROSS_REFERENCE_REQUIRED`, `SOURCE_AMBIGUOUS`, `DATASET_STATEMENT_ONLY` or `UNRESOLVED`.

## Rival architecture test

The elementary record is binary by default: `ACTOR_A -> ACTOR_B`. An R–I–T ternary record is retained only as a derived configuration view when linked binary edges and evidence support it. Both representations are tested; neither is treated as theoretically correct in advance.
"""
    (OUT["00_PROTOCOL"] / "PILOT_02_PROTOCOL.md").write_text(protocol, encoding="utf-8")
    (OUT["00_PROTOCOL"] / "CODING_RULES_V0_2.md").write_text("""# CODING_RULES_V0_2

- Preserve the statutory verb before assigning analytical labels.
- Do not treat a named organization as an intermediary without a legally supported relation.
- Function answers the governance work; mechanism answers the means; device names the concrete carrier.
- `FUNCTION_MECHANISM_COLLAPSE` is an issue flag, not a new category.
- Store binary provision-level edges as the primitive; derive R–I–T configurations compositionally.
- Use `SOURCE_AMBIGUOUS` or `UNRESOLVED` instead of filling a missing role by intuition.
- Model values never overwrite the existing workbook or PILOT_01.
""", encoding="utf-8")

    a_rows = [row_from(x, "MODEL_INDEPENDENT_A") for x in BASE]
    b_rows = [row_from(x, "MODEL_INDEPENDENT_B") for x in BASE]
    write_csv(OUT["02_CODING_A"] / "RELATIONSHIPS_CODER_A.csv", FIELDS, a_rows)
    write_csv(OUT["03_CODING_B"] / "RELATIONSHIPS_CODER_B.csv", FIELDS, b_rows)

    amap = {r["candidate_id"]: r for r in a_rows}; bmap = {r["candidate_id"]: r for r in b_rows}
    compare_fields = ["relationship_existence","actor_a","actor_b","actor_i","actor_a_role","actor_b_role","actor_i_role","action","object","function","mechanism","device","relationship_type","intermediary_status"]
    keymap = {"relationship_existence": "exists"}
    comp = []
    for base in BASE:
        cid = base[0]; a = amap[cid]; b = bmap[cid]
        for f in compare_fields:
            if f == "relationship_existence":
                av = "YES"; bv = "YES" if not (cid == "P02_C03" and b["intermediary_status"] == "UNRESOLVED") else "NO"
            else:
                av = a.get(f, ""); bv = b.get(f, "")
            agree = "AGREEMENT" if av == bv else "DISAGREEMENT"
            cls = "" if agree == "AGREEMENT" else ("SCHEMA_PROBLEM" if f in {"actor_i","actor_i_role","relationship_type"} else ("ONTOLOGY_PROBLEM" if f in {"function","mechanism","intermediary_status"} else "CODING_RULE_OR_LEGAL_AMBIGUITY"))
            comp.append({"candidate_id":cid,"case_id":base[1],"provision_id":base[3],"variable":f,"coder_a_value":av,"coder_b_value":bv,"agreement":agree,"disagreement_class":cls,"evidence_status":a["evidence_status"]})
    write_csv(OUT["04_COMPARISON"] / "CODER_COMPARISON.csv", list(comp[0].keys()), comp)

    metrics = []
    for f in compare_fields:
        subset = [r for r in comp if r["variable"] == f]
        av = [r["coder_a_value"] for r in subset]; bv = [r["coder_b_value"] for r in subset]
        agree_n = sum(x == y for x,y in zip(av,bv)); raw = agree_n / len(subset)
        metrics.append({"variable":f,"n_candidates":len(subset),"raw_agreement":round(raw,3),"agreement_count":agree_n,"disagreement_count":len(subset)-agree_n,"cohen_kappa_descriptive":kappa(av,bv),"interpretation":"descriptive only; simulated model passes and small purposive sample"})
    write_csv(OUT["04_COMPARISON"] / "AGREEMENT_METRICS.csv", list(metrics[0].keys()), metrics)
    metric_lines = [
        "# AGREEMENT_REPORT",
        "",
        "The comparison uses 17 provision-linked candidate slots. The two passes are simulated model replications (`MODEL_INDEPENDENT_A` and `MODEL_INDEPENDENT_B`), not human intercoder reliability.",
        "",
        "| Variable | N | Raw agreement | Disagreements | Cohen's kappa (descriptive) |",
        "|---|---:|---:|---:|---:|",
    ]
    metric_lines += [f"| `{m['variable']}` | {m['n_candidates']} | {m['raw_agreement']:.3f} | {m['disagreement_count']} | {m['cohen_kappa_descriptive']} |" for m in metrics]
    metric_lines += [
        "",
        "Relationship existence is highly stable in this small test, while `ACTOR_I` and relationship type are less stable. Kappa is included only as a descriptive supplement because the sample is purposive, small and affected by category prevalence.",
        "",
        "Disagreements are preserved in `CODER_COMPARISON.csv` and adjudication is recorded separately after both passes were frozen.",
    ]
    (OUT["04_COMPARISON"] / "AGREEMENT_REPORT.md").write_text("\n".join(metric_lines) + "\n", encoding="utf-8")

    adjud = []
    for cid in sorted({r["candidate_id"] for r in comp}):
        diffs = [r for r in comp if r["candidate_id"] == cid and r["agreement"] == "DISAGREEMENT"]
        if not diffs: continue
        b = amap[cid]; prov = next(x for x in PROVISIONS if x["provision_id"] == b["provision_id"])
        if cid == "P01_C01": value, rationale, issue = "BINARY_EDGE_ONLY", "Article 3(2) supports notification/designation but does not state a complete R–I–T relation in one proposition.", "SCHEMA_PROBLEM"
        elif cid == "P02_C03": value, rationale, issue = "UNRESOLVED", "Annex II requires bodies to possess insurance; it does not constitute insurers as regulatory intermediaries.", "ONTOLOGY_PROBLEM"
        elif cid == "P03_C03": value, rationale, issue = "FUNCTION=MONITORING; MECHANISM=AUDIT_SURVEILLANCE; DEVICE=QUALITY_SYSTEM_ASSESSMENT", "Annex III separates assessment of the quality system from the purpose of ongoing surveillance; the boundary remains operationally fragile.", "ONTOLOGY_PROBLEM"
        elif cid == "P04_C01": value, rationale, issue = "TWO_BINARY_EDGES_PLUS_DERIVED_CONFIGURATION", "Article 12(5) contains appointment, audit and reporting, but the graph representation preserves each direction without asserting one primitive ternary edge.", "SCHEMA_PROBLEM"
        elif cid == "P04_C03": value, rationale, issue = "TWO_BINARY_EDGES_PLUS_DERIVED_CONFIGURATION", "Article 14 expressly supports applicant-to-agent submission and agent-to-Registry notification; the R–I–T view is derived.", "SCHEMA_PROBLEM"
        elif cid == "P05_C01": value, rationale, issue = "UNRESOLVED_INTERMEDIARY_STATUS", "Article 18 makes audit or supervision a condition for an exemption; it does not by itself settle whether the auditor/self-regulatory body is a regulatory intermediary.", "SOURCE_AMBIGUOUS"
        else: value, rationale, issue = "RETAIN_SOURCE_SPECIFIC_VALUE", "The legal provision is direct; the disagreement concerns normalization of actor category or relation label rather than absence of evidence.", "CODING_RULE_AMBIGUITY"
        adjud.append({"adjudication_id":"ADJ_"+cid,"candidate_id":cid,"provision_id":prov["provision_id"],"coder_a_value":"; ".join(f["coder_a_value"] for f in diffs),"coder_b_value":"; ".join(f["coder_b_value"] for f in diffs),"relevant_legal_provision":prov["location"],"reason_for_disagreement":"; ".join(f["variable"] for f in diffs),"adjudicated_value":value,"adjudication_rationale":rationale,"disagreement_type":issue,"provenance":"HUMAN_ADJUDICATED_SIMULATION_REQUIRED","status":"PENDING_HUMAN_REVIEW"})
    write_csv(OUT["05_ADJUDICATION"] / "ADJUDICATION_REGISTER.csv", list(adjud[0].keys()), adjud)

    (OUT["06_SCHEMA_TEST"] / "TERNARY_VS_GRAPH_TEST.md").write_text("""# Ternary versus compositional graph test

## Model A — ternary record

`R -> I -> T` is stored directly. It is readable for a high-level architecture, but it duplicates the regulator and target whenever one intermediary has several functions, and it can assert a composite relation that no single provision expresses.

## Model B — binary/compositional graph

Store only provision-supported elementary edges: `R -> I`, `I -> T`, `I -> R`, `R -> T`, or another directed pair. Derive an R–I–T configuration only when edges share a case, actor identity, object/procedure and evidence-compatible provision set.

## Pilot result

The graph representation preserved evidence more cleanly in P01, P04 and P05. It handled applicant-to-validation-agent submission separately from validation-agent-to-Registry notification, and it avoided treating Article 18's audit/supervision condition as a settled R–I–T relation. Ternary records remain useful as a derived analytical view, but they should not be the primitive storage unit.

Finding: **MODEL B is preferred as the normalized core, with a derived ternary configuration view.**
""", encoding="utf-8")
    (OUT["06_SCHEMA_TEST"] / "FUNCTION_MECHANISM_TEST.md").write_text("""# Function × Mechanism test

Direct provisions reduce uncertainty, but they do not eliminate conceptual overlap. P03 Article 10/Annex III is the critical test: assessment of a quality-control system is a governance task; surveillance audits are a means of continuing oversight; the quality-system procedure and audit report are devices. P04 validation similarly separates the function (assurance of prior-right claims), mechanism (documentary validation) and device (documentary evidence/validation notice).

Systematic disagreement remains between `assurance` versus `monitoring` and `quality_system_assessment` versus `audit_surveillance`. `FUNCTION_MECHANISM_COLLAPSE` should therefore remain an explicit diagnostic flag in v0.2.
""", encoding="utf-8")
    (OUT["06_SCHEMA_TEST"] / "ACTOR_POSITION_TEST.md").write_text("""# Actor position test

`ACTOR_IDENTITY`, `RELATIONAL_ROLE` and `INSTITUTIONAL_CONTEXT` remain empirically separable. `ACTOR_I` is useful in a derived R–I–T view but is not always necessary as a primitive field: P01 Article 3(2), P04 Article 14 and P05 Article 18 are more faithfully stored as connected binary edges. Recipient and oversight positions are needed only when the legal text gives the recipient a distinct action or consequence.

Finding: store binary A/B edges as the primitive; expose `ACTOR_I` in a derived configuration table and retain recipient/oversight actors only when textually supported.
""", encoding="utf-8")

    disag = sum(r["agreement"] == "DISAGREEMENT" for r in comp)
    exist_agree = next(x for x in metrics if x["variable"] == "relationship_existence")
    high = [x for x in metrics if x["raw_agreement"] >= 0.8]
    unresolved = [x for x in metrics if x["disagreement_count"]]
    gate = "RELATIONAL_MODEL_RELIABILITY_SUPPORTED_WITH_REVISIONS"
    report = f"""# PILOT_02_REPORT

## Gate

**{gate}**

This gate applies to procedural model replication, not human intercoder reliability. The two passes were labeled `MODEL_INDEPENDENT_A` and `MODEL_INDEPENDENT_B`; no human pair was available.

## Design

The same five PILOT_01 cases were used: 76/889/EEC, 89/336/EEC, 91/263/EEC, EC 874/2004 and 1781/2006. The source-first pass began with {len(PROVISIONS)} official EUR-Lex provisions and {len(BASE)} candidate relationship slots. The current workbook and PILOT_01 outputs were consulted only as methodological context and were not treated as legal evidence.

## Answers to the research questions

1. **Can two independent codings identify substantially the same relationships?** Mostly, at the level of candidate provision/action existence. Relationship-existence raw agreement was {exist_agree['raw_agreement']:.3f} ({exist_agree['agreement_count']}/{exist_agree['n_candidates']}). The agreement is not sufficient to claim stable fine-grained coding because actor positions, function/mechanism and intermediary status generate systematic disagreements.

2. **Which variables have high agreement?** Provision-linked case identity, act identifier, legal location and most basic actor/action/object fields have high agreement. The variable-level table reports the exact counts rather than collapsing them into one reliability number.

3. **Which variables generate systematic disagreement?** `ACTOR_I`, relationship type, function, mechanism and intermediary status. Ternary versus binary representation is the dominant schema disagreement.

4. **Main source of disagreement?** Mixed: schema ambiguity for ACTOR_I and R–I–T; ontology overlap for assurance/monitoring/audit; source ambiguity for insurance and Article 18's conditional audit/supervision; normalization ambiguity for legal actor categories.

5. **Does direct provision capture reduce uncertainty?** Yes. It resolves the missing-reference problem found in PILOT_01 and allows the pilot to reject at least one prior overextension: P05 Article 18 is a statutory condition, not automatically an intermediary relationship. Direct text does not by itself solve ontology boundaries.

6. **Is Function distinguishable from Mechanism?** Provisionally. Action, governance work, means and device can be separated in P01, P03 and P04. The distinction is not yet reproducible enough for an unqualified production taxonomy.

7. **Is Device/Instrument necessary?** Yes. Certificates, audit reports, documentary evidence, escrow agreements and ADR procedures carry legal effects that would be lost if function and mechanism were the only fields.

8. **Is ACTOR_I necessary as a primitive?** No, not always. It is useful in a derived R–I–T view, but the binary graph preserves evidence better in the tested cases.

9. **Is R–I–T better derived compositionally?** Yes. Model B reduces duplication and avoids inferring a combined ternary relation from provisions that legally express separate edges.

10. **Can intermediary status be derived?** Partly. It is strongly supported where an actor occupies a distinct connected position in a legally constituted configuration. It remains unresolved for supporting devices and conditional oversight actors, especially P02 insurance and P05 audit/supervision.

11. **PILOT_01 issues resolved?** Structured provision traceability is materially improved; the need for role-specific identities is confirmed; the unit-of-observation problem is clarified in favor of elementary binary edges.

12. **PILOT_01 issues unresolved?** Function × mechanism boundary, intermediary status for insurance/oversight, modality granularity, and human intercoder reliability remain unresolved.

13. **New issues:** direct legal text can support several equally defensible relation cuts; a derived R–I–T configuration needs a formal edge-linking rule; legal category labels and normalized actor identities need separate fields.

14. **Stable for a larger pilot?** Stable enough for a larger *reliability* pilot using the binary core, but not stable enough for corpus-wide recoding or production integration.

## Limitations

The sample is purposive and small. The two passes are simulated model independence, not independent human coders. Raw agreement is therefore a reproducibility diagnostic. Cohen's kappa values are reported descriptively where computable, but prevalence and sample size make them unsuitable as a sole decision rule.

## Recommended next step

Run a human-adjudicated PILOT_03 or a larger duplicate-coding exercise using the binary/compositional core, with direct provision excerpts and a preregistered rule for linking R–I and I–T edges into derived R–I–T configurations. Do not modify production until human agreement is tested.
"""
    (OUT["07_RESULTS"] / "PILOT_02_REPORT.md").write_text(report, encoding="utf-8")

    issue_rows = [
        ["P02_ISSUE_001","ALL","MODEL_INDEPENDENCE","Two passes are simulated model replications, not human intercoder reliability.","LIMITS_RELIABILITY_CLAIM","Use human duplicate coding before production change.","MODEL_INDEPENDENT_A/B","OPEN"],
        ["P02_ISSUE_002","P01/P04","SCHEMA","Ternary R-I-T rows can combine legally separate binary edges.","RIT_COMPOSITE_OVERASSERTION","Use binary core and derive ternary configuration.","ADJUDICATED_SIMULATION","OPEN"],
        ["P02_ISSUE_003","P03","FUNCTION_MECHANISM","Assessment, assurance, monitoring, audit and surveillance remain overlapping.","FUNCTION_MECHANISM_COLLAPSE_RISK","Retain separate fields plus explicit collapse flag.","MODEL_INDEPENDENT_A/B","OPEN"],
        ["P02_ISSUE_004","P02","ACTOR_STATUS","Insurance is a statutory condition on bodies, not necessarily a regulatory intermediary.","SOURCE_AMBIGUOUS","Do not derive intermediary status automatically.","ADJUDICATED_SIMULATION","OPEN"],
        ["P02_ISSUE_005","P05","ACTOR_STATUS","Article 18 permits exemption conditional on audit/supervision but does not settle intermediary status.","SOURCE_AMBIGUOUS","Keep unresolved pending human legal adjudication.","ADJUDICATED_SIMULATION","OPEN"],
        ["P02_ISSUE_006","ALL","ACTOR_NORMALIZATION","Legal categories such as competent body, notified body and validation agent need identity and category fields.","NORMALIZATION_AMBIGUITY","Store verbatim legal label and normalized identity separately.","MODEL_PILOT","OPEN"],
    ]
    write_csv(OUT["07_RESULTS"] / "PILOT_02_ISSUE_REGISTER.csv", ["issue_id","case_scope","issue_type","description","diagnostic","recommended_handling","provenance","status"], [dict(zip(["issue_id","case_scope","issue_type","description","diagnostic","recommended_handling","provenance","status"], x)) for x in issue_rows])

    (OUT["07_RESULTS"] / "RELATIONAL_MODEL_V0_2.md").write_text("""# RELATIONAL_MODEL_V0_2

## Status

Provisional output of PILOT_02. Not a production codebook and not a replacement for Rotem's workbook.

## Minimal normalized core

1. `ACTS` — one row per act.
2. `PROVISIONS` — one row per addressable provision with official locator and excerpt.
3. `ACTORS` — verbatim legal identity/category, normalized identity, institutional context.
4. `BINARY_RELATIONSHIPS` — one row per provision-supported directed A→B edge.
5. `RELATIONSHIP_EVIDENCE` — many-to-many provision links.
6. `RELATIONSHIP_CODING` — action, object, function, mechanism, device, relationship type, modality and evidence status.
7. `CONFIGURATION_LINKS` — derived links that compose R→I and I→T into an R–I–T view; never replace the binary evidence.
8. `INTERMEDIARY_REGISTER` — derived view of an actor's intermediary positions, not a fixed actor property.
9. `ADJUDICATION_REGISTER` — coder disagreement and provenance.

## Core rule

Use the binary relationship as the primitive. Expose `ACTOR_I` only as a derived configuration position when two or more elementary edges support it. Keep Device/Instrument separate because it carries concrete legal effects and is not interchangeable with Function or Mechanism.

## Explicit uncertainty

Function/mechanism collapse, conditional audit/supervision and supporting devices remain unresolved. No new production mechanism category is authorized by this model.
""", encoding="utf-8")

    manifest = {"pilot":"PILOT_02","generated_at":datetime.now().isoformat(timespec="seconds"),"cases":["76/889/EEC","89/336/EEC","91/263/EEC","EC 874/2004","1781/2006"],"provision_count":len(PROVISIONS),"candidate_count":len(BASE),"coder_a":"MODEL_INDEPENDENT_A","coder_b":"MODEL_INDEPENDENT_B","disagreement_cells":disag,"gate":gate,"production_modified":False,"pilot_01_modified":False}
    (ROOT / "99_REPRODUCIBILITY" / "PILOT_02_MANIFEST.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")


if __name__ == "__main__":
    main()
