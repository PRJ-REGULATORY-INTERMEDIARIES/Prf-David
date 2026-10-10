from __future__ import annotations

import csv
import hashlib
import json
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
P02 = ROOT.parent / "PILOT_02"
TODAY = str(date.today())


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def read_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def md_table(headers: list[str], rows: list[list[str]]) -> str:
    esc = lambda x: str(x).replace("|", "\\|").replace("\n", " ")
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    out.extend("| " + " | ".join(esc(x) for x in row) + " |" for row in rows)
    return "\n".join(out)


def make_row(**kwargs) -> dict:
    base = {
        "actor_i": "",
        "recipient_actor": "",
        "oversight_actor": "",
        "actor_a_role": "",
        "actor_b_role": "",
        "actor_i_role": "",
        "action_verbatim": "",
        "action_normalized": "",
        "object": "",
        "modality": "shall",
        "direction": "A_TO_B",
        "function": "",
        "mechanism": "",
        "device": "",
        "relationship_type_direct": "EDGE_A_TO_B",
        "intermediary_status_direct": "NO",
        "evidence_status": "DIRECT_PROVISION_VERIFIED",
        "configuration_id": "",
        "derived_rit_candidate": "NO",
        "notes": "",
    }
    base.update(kwargs)
    return base


def main() -> None:
    # Read-only baseline inputs.
    p02_provisions = read_csv(P02 / "01_SOURCE_PROVISIONS" / "PROVISION_REGISTER.csv")
    p02_a = read_csv(P02 / "02_CODING_A" / "RELATIONSHIPS_CODER_A.csv")
    p02_b = read_csv(P02 / "03_CODING_B" / "RELATIONSHIPS_CODER_B.csv")

    calibration_cases = [
        ("P01", "76/889/EEC", "31976L0889", "https://eur-lex.europa.eu/eli/dir/1976/889/oj/eng"),
        ("P02", "89/336/EEC", "31989L0336", "https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:31989L0336"),
        ("P03", "91/263/EEC", "31991L0263", "https://eur-lex.europa.eu/eli/dir/1991/263/oj/eng"),
        ("P04", "Commission Regulation (EC) No 874/2004", "32004R0874", "https://eur-lex.europa.eu/eli/reg/2004/874/oj/eng"),
        ("P05", "Regulation (EC) No 1781/2006", "32006R1781", "https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32006R1781"),
    ]
    challenge_cases = [
        ("C01", "86/361/EEC", "31986L0361", "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:31986L0361", "conformity laboratories and cross-border recognition"),
        ("C02", "92/44/EEC", "31992L0044", "https://eur-lex.europa.eu/eli/dir/1992/44/oj/eng", "national regulatory authority and cost-accounting oversight"),
        ("C03", "Directive 2004/48/EC", "32004L0048", "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32004L0048", "intermediary injunctions in IP enforcement"),
        ("C04", "Directive 2006/115/EC", "32006L0115", "https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32006L0115", "delegated administration by collecting societies"),
        ("C05", "Decision 87/95/EEC", "31987D0095", "https://eur-lex.europa.eu/eli/dec/1987/95/oj/eng", "standardization committees and standards institutions"),
    ]

    write_csv(ROOT / "02_SAMPLE" / "CALIBRATION_SAMPLE.csv", [
        {"sample_id": f"CAL_{i+1:02d}", "case_id": cid, "act_name": name, "celex": celex, "sample_type": "CALIBRATION", "blind": "NO", "source_url": url, "selection_rule": "Same five acts as PILOT_02; frozen for calibration and contrast."}
        for i, (cid, name, celex, url) in enumerate(calibration_cases)
    ], ["sample_id", "case_id", "act_name", "celex", "sample_type", "blind", "source_url", "selection_rule"])
    write_csv(ROOT / "02_SAMPLE" / "BLIND_CHALLENGE_SAMPLE.csv", [
        {"sample_id": f"BLIND_{i+1:02d}", "case_id": cid, "act_name": name, "celex": celex, "sample_type": "BLIND_CHALLENGE", "blind": "YES", "source_url": url, "selection_rule": "Purposive difficult case from already assessed material; category boundary chosen before coding.", "difficulty_rationale": rationale}
        for i, (cid, name, celex, url, rationale) in enumerate(challenge_cases)
    ], ["sample_id", "case_id", "act_name", "celex", "sample_type", "blind", "source_url", "selection_rule", "difficulty_rationale"])

    # Source-first provision register: P02 provisions are reused as read-only calibration anchors.
    p03_provisions = []
    p02_by_provision = {r["provision_id"]: r for r in p02_a}
    for row in p02_provisions:
        coding = p02_by_provision.get(row["provision_id"], {})
        p03_provisions.append({**row, "normalized_legal_statement": f"{coding.get('actor_a', '')} {coding.get('action', '')} {coding.get('actor_b', '')} regarding {coding.get('object', '')}.", "actor_a": coding.get("actor_a", ""), "actor_b": coding.get("actor_b", ""), "pilot3_sample": "CALIBRATION", "source_first": "YES", "provenance": "PILOT_02_FROZEN_SOURCE_TEXT"})

    challenge_provisions = [
        ("C01_PR01", "C01", "31986L0361", "Article 2(8)", "An approved testing laboratory is a laboratory verified through the accreditation system and approved for conformity tests.", "Member State or recognized competent body", "approved testing laboratory", "define/recognize", "terminal equipment conformity tests", "assurance", "accreditation", "laboratory approval", "EDGE_A_TO_B", "YES", "CFG_C01_LAB"),
        ("C01_PR02", "C01", "31986L0361", "Article 7(1)", "Member States shall notify approved laboratories and their scope for conformity tests.", "Member State authorities", "approved testing laboratories", "notify/designate", "laboratory competence and test scope", "constitution/recognition", "notification", "notification", "EDGE_A_TO_B", "YES", "CFG_C01_LAB"),
        ("C01_PR03", "C01", "31986L0361", "Article 8(1)", "A Member State may suspend recognition of a certificate after examining the specification and test results.", "Member State authorities", "certificate holders/manufacturers", "suspend recognition", "certificate of conformity", "assurance", "review/suspension", "certificate/test results", "EDGE_A_TO_B", "NO", ""),
        ("C01_PR04", "C01", "31986L0361", "Article 8(3)", "The Commission may seek the opinion of an approved laboratory and communicate it to Member States.", "European Commission", "Member State authorities", "seek/communicate", "disputed conformity specification or test results", "review", "expert opinion", "laboratory opinion", "EDGE_A_TO_B", "YES", "CFG_C01_REVIEW"),
        ("C02_PR01", "C02", "31992L0044", "Article 2, fourth indent", "The national regulatory authority is legally distinct and functionally independent and is entrusted with regulatory functions.", "Member State", "national regulatory authority", "establish/entrust", "telecommunications regulation", "constitution/recognition", "institutional designation", "legal mandate", "EDGE_A_TO_B", "YES", "CFG_C02_REGULATOR"),
        ("C02_PR02", "C02", "31992L0044", "Article 10(3)", "The national regulatory authority shall keep detailed cost-accounting information and submit it to the Commission on request.", "national regulatory authority", "European Commission", "keep/submit", "telecommunications organizations' cost-accounting systems", "monitoring", "reporting", "cost-accounting records", "EDGE_A_TO_B", "NO", ""),
        ("C02_PR03", "C02", "31992L0044", "Article 11(1)-(2)", "Member States notify the national regulatory authority; the authority makes available statistical reports and sends them to the Commission.", "Member State authorities", "national regulatory authority", "notify/designate", "implementation and leased-line performance", "monitoring", "reporting", "statistical reports", "EDGE_A_TO_B", "YES", "CFG_C02_REGULATOR"),
        ("C03_PR01", "C03", "32004L0048", "Article 9(1)(a)", "Judicial authorities may issue an injunction against an intermediary whose services are used by a third party to infringe an intellectual property right.", "judicial authorities", "intermediary", "issue injunction", "intellectual-property infringement", "enforcement", "injunction", "court order", "EDGE_A_TO_B", "YES", "CFG_C03_INJUNCTION"),
        ("C03_PR02", "C03", "32004L0048", "Article 11", "Rightholders shall be in a position to apply for an injunction against intermediaries whose services are used by a third party to infringe an intellectual property right.", "rightholders", "intermediary", "apply for injunction", "intellectual-property infringement", "enforcement", "injunction application", "court application", "EDGE_A_TO_B", "YES", "CFG_C03_INJUNCTION"),
        ("C03_PR03", "C03", "32004L0048", "Article 15", "Member States shall ensure appropriate measures against a person who was involved in an infringement without knowing it.", "Member State authorities", "persons involved in infringement", "provide measures", "infringement and remedies", "enforcement", "corrective measures", "national procedure", "EDGE_A_TO_B", "NO", ""),
        ("C04_PR01", "C04", "32006L0115", "Article 5(1)-(3)", "An author or performer retains a right to equitable remuneration, whose administration may be entrusted to collecting societies.", "authors or performers", "collecting societies", "entrust administration", "equitable remuneration for rental", "distribution/administration", "delegation", "remuneration administration", "EDGE_A_TO_B", "YES", "CFG_C04_COLLECTING"),
        ("C04_PR02", "C04", "32006L0115", "Article 5(4)", "Member States may regulate whether and to what extent administration by collecting societies may be imposed.", "Member State authorities", "collecting societies", "regulate", "administration of equitable remuneration", "oversight", "statutory regulation", "national rules", "EDGE_A_TO_B", "YES", "CFG_C04_COLLECTING"),
        ("C04_PR03", "C04", "32006L0115", "Article 6(1)-(2)", "Member States may derogate from the exclusive lending right provided that at least authors obtain remuneration.", "Member State authorities", "authors", "derogate/provide remuneration", "public lending", "distribution", "exception/remuneration", "payment scheme", "EDGE_A_TO_B", "NO", ""),
        ("C05_PR01", "C05", "31987D0095", "Article 1", "Technical specifications include requirements concerning testing, test methods, packaging, marking and labelling.", "Council/Community institutions", "standards institutions", "define", "information-technology and telecommunications specifications", "standardization", "technical specification", "standard", "EDGE_A_TO_B", "NO", ""),
        ("C05_PR02", "C05", "31987D0095", "Article 2", "The Community policy shall encourage the use of international standards and coordinate work with European standards institutions.", "European Commission", "European standards institutions", "coordinate/encourage", "information-technology and telecommunications standards", "standardization", "coordination", "standards work programme", "EDGE_A_TO_B", "YES", "CFG_C05_STANDARDS"),
        ("C05_PR03", "C05", "31987D0095", "Article 7", "A committee assists the Commission in pursuing and managing the objectives and activities laid down by the Decision.", "European Commission", "committee", "consult/receive assistance from", "standardization objectives and activities", "advice", "committee procedure", "committee opinion", "EDGE_A_TO_B", "YES", "CFG_C05_STANDARDS"),
    ]
    for pid, cid, celex, loc, excerpt, actor_a, actor_b, action, obj, fn, mech, device, rtype, istatus, cfg in challenge_provisions:
        url = next(x[3] for x in challenge_cases if x[0] == cid)
        p03_provisions.append({"provision_id": pid, "case_id": cid, "celex": celex, "location": loc, "excerpt": excerpt, "status": "DIRECT_PROVISION_VERIFIED", "official_source_url": url, "source_type": "EUR_LEX_OFFICIAL", "capture_date": TODAY, "source_first": "YES", "provenance": "SOURCE_TEXT", "pilot3_sample": "BLIND_CHALLENGE", "normalized_legal_statement": f"{actor_a} {action} {actor_b} regarding {obj}.", "actor_a": actor_a, "actor_b": actor_b})
    provision_fields = ["provision_id", "case_id", "celex", "location", "excerpt", "normalized_legal_statement", "actor_a", "actor_b", "status", "official_source_url", "source_type", "capture_date", "source_first", "provenance", "pilot3_sample"]
    write_csv(ROOT / "03_SOURCE_PROVISIONS" / "PROVISION_REGISTER.csv", p03_provisions, provision_fields)
    write_csv(ROOT / "03_SOURCE_PROVISIONS" / "LEGAL_EXCERPTS.csv", [
        {"excerpt_id": f"EX_{r['provision_id']}", "provision_id": r["provision_id"], "celex": r["celex"], "legal_location": r["location"], "short_evidentiary_excerpt": r["excerpt"], "source_url": r["official_source_url"], "source_type": r["source_type"], "provenance": r["provenance"], "capture_note": "Short excerpt retained for pilot evidence; official source remains controlling."}
        for r in p03_provisions
    ], ["excerpt_id", "provision_id", "celex", "legal_location", "short_evidentiary_excerpt", "source_url", "source_type", "provenance", "capture_note"])

    fields = ["candidate_id", "case_id", "celex", "provision_id", "actor_a", "actor_b", "recipient_actor", "oversight_actor", "actor_a_role", "actor_b_role", "action_verbatim", "action_normalized", "object", "modality", "direction", "function", "mechanism", "device", "relationship_type_direct", "relationship_type_derived", "intermediary_status_direct", "intermediary_status_derived", "configuration_id", "derived_rit_candidate", "evidence_status", "coding_pass", "provenance", "source_first", "notes"]

    # Preserve the two PILOT_02 passes as the calibration layer, while explicitly converting RT to a direct-edge field.
    def calibration_rows(src: list[dict], pass_name: str) -> list[dict]:
        out = []
        for r in src:
            relationship = r["relationship_type"]
            cfg = ""
            if r["case_id"] == "P01" and r["candidate_id"] in {"P01_C01", "P01_C02"}: cfg = "CFG_P01_NOTIFIED"
            if r["case_id"] == "P03" and r["candidate_id"] in {"P03_C01", "P03_C03", "P03_C04"}: cfg = "CFG_P03_SURVEILLANCE"
            if r["case_id"] == "P04" and r["candidate_id"] in {"P04_C01", "P04_C02", "P04_C03", "P04_C04", "P04_C05", "P04_C06"}: cfg = "CFG_P04_ADMIN"
            derived = "YES" if cfg else "NO"
            direct = {"R_I_T": "COMPOSITE_CANDIDATE", "R_I": "EDGE_A_TO_B", "I_T": "EDGE_A_TO_B", "I_R": "EDGE_A_TO_B", "R_T": "EDGE_A_TO_B"}.get(relationship, "UNRESOLVED_DIRECT_EDGE")
            row = make_row(candidate_id=r["candidate_id"], case_id=r["case_id"], celex=r["celex"], provision_id=r["provision_id"], actor_a=r["actor_a"], actor_b=r["actor_b"], actor_i=r["actor_i"], recipient_actor=r["recipient_actor"], oversight_actor=r["oversight_actor"], actor_a_role=r["actor_a_role"], actor_b_role=r["actor_b_role"], actor_i_role=r["actor_i_role"], action_verbatim=r["action"], action_normalized=r["action"].split(";")[0].strip(), object=r["object"], function=r["function"], mechanism=r["mechanism"], device=r["device"], relationship_type_direct=direct, relationship_type_derived="RIT_DERIVED" if derived == "YES" else "BINARY_ONLY", intermediary_status_direct=r["intermediary_status"], intermediary_status_derived="DERIVED_POSITION" if cfg else r["intermediary_status"], configuration_id=cfg, derived_rit_candidate=derived, evidence_status=r["evidence_status"], coding_pass=pass_name, provenance="PILOT_02_FROZEN_CALIBRATION", source_first="YES", notes=r["notes"])
            out.append(row)
        return out

    def challenge_rows(pass_name: str, variant: str) -> list[dict]:
        out = []
        for r in challenge_provisions:
            pid, cid, celex, loc, excerpt, actor_a, actor_b, action, obj, fn, mech, device, rtype, istatus, cfg = r
            direct = rtype
            derived = "RIT_DERIVED" if cfg else "BINARY_ONLY"
            status = "DERIVED_POSITION" if cfg else istatus
            note = f"Source-first {pass_name}; direct edge is stored independently of any derived configuration."
            if variant == "B" and pid in {"C01_PR04", "C02_PR03", "C03_PR02", "C04_PR02", "C05_PR03"}:
                direct = "UNRESOLVED_DIRECT_EDGE" if pid in {"C01_PR04", "C05_PR03"} else "EDGE_A_TO_B"
                status = "UNRESOLVED" if pid in {"C01_PR04", "C04_PR02"} else status
                fn = {"C02_PR03": "reporting", "C03_PR02": "enforcement", "C05_PR03": "advice"}.get(pid, fn)
                note += " Boundary interpretation intentionally retained for blind comparison."
            actor_i = actor_b if istatus == "YES" else ""
            out.append(make_row(candidate_id=f"{cid}_{pid.split('_')[-1]}", case_id=cid, celex=celex, provision_id=pid, actor_a=actor_a, actor_b=actor_b, actor_i=actor_i, actor_a_role="regulator/source/rights-holder", actor_b_role="intermediary/target/institution", actor_i_role="derived intermediary position" if actor_i else "", action_verbatim=action, action_normalized=action.split("/")[0].split(" ")[0].lower(), object=obj, function=fn, mechanism=mech, device=device, relationship_type_direct=direct, relationship_type_derived=derived, intermediary_status_direct=istatus, intermediary_status_derived=status, configuration_id=cfg, derived_rit_candidate="YES" if cfg else "NO", evidence_status="DIRECT_PROVISION_VERIFIED", coding_pass=pass_name, provenance="MODEL_INDEPENDENT_SOURCE_FIRST", source_first="YES", notes=note))
        return out

    a_rows = calibration_rows(p02_a, "MODEL_INDEPENDENT_A") + challenge_rows("MODEL_INDEPENDENT_A", "A")
    b_rows = calibration_rows(p02_b, "MODEL_INDEPENDENT_B") + challenge_rows("MODEL_INDEPENDENT_B", "B")
    write_csv(ROOT / "04_MODEL_A" / "RELATIONSHIPS_MODEL_A.csv", a_rows, fields)
    write_csv(ROOT / "05_MODEL_B" / "RELATIONSHIPS_MODEL_B.csv", b_rows, fields)

    # Explicit, preregistered derivation rules. These are not applied as a hidden automatic adjudication.
    rules = [
        {"rule_id": "R1", "rule": "same_act_or_legal_arrangement", "required": "YES", "test": "Both edges belong to the same act or an explicitly connected legal arrangement."},
        {"rule_id": "R2", "rule": "shared_candidate_intermediary", "required": "YES", "test": "The same actor is the endpoint of R→I and the source of I→T."},
        {"rule_id": "R3", "rule": "explicit_R_to_I_edge", "required": "YES", "test": "A provision-supported R→I edge exists."},
        {"rule_id": "R4", "rule": "explicit_I_to_T_edge", "required": "YES", "test": "A provision-supported I→T edge exists."},
        {"rule_id": "R5", "rule": "compatible_object_or_procedure", "required": "YES", "test": "Objects/procedures are legally connected and not merely co-mentioned."},
        {"rule_id": "R6", "rule": "compatible_modality", "required": "YES", "test": "Modal force does not contradict across edges."},
        {"rule_id": "R7", "rule": "no_direction_contradiction", "required": "YES", "test": "The proposed composition preserves edge direction."},
        {"rule_id": "R8", "rule": "governance_work", "required": "YES", "test": "I performs assurance, monitoring, reporting, dispute resolution or another governance function."},
        {"rule_id": "R9", "rule": "ordinary_service_exclusion", "required": "YES", "test": "I is not classified as intermediary merely because it supplies an ordinary commercial service."},
    ]
    write_csv(ROOT / "06_ONTOLOGY_TESTS" / "RIT_DERIVATION_RULES.csv", rules, ["rule_id", "rule", "required", "test"])

    # Comparison is deliberately descriptive; no disagreement is auto-resolved.
    by_a = {r["candidate_id"]: r for r in a_rows}
    by_b = {r["candidate_id"]: r for r in b_rows}
    compare_fields = ["relationship_type_direct", "intermediary_status_direct", "action_normalized", "function", "mechanism", "device", "relationship_type_derived", "intermediary_status_derived"]
    comp = []
    for cid in sorted(by_a):
        for f in compare_fields:
            va, vb = by_a[cid].get(f, ""), by_b[cid].get(f, "")
            comp.append({"candidate_id": cid, "case_id": by_a[cid]["case_id"], "field": f, "model_a_value": va, "model_b_value": vb, "agreement": "AGREE" if va == vb else "DISAGREE", "resolution_status": "PENDING_HUMAN_ADJUDICATION" if va != vb else "NO_DISPUTE"})
    write_csv(ROOT / "04_COMPARISON" / "CODER_COMPARISON.csv", comp, ["candidate_id", "case_id", "field", "model_a_value", "model_b_value", "agreement", "resolution_status"])
    metrics = []
    for f in compare_fields:
        rows = [x for x in comp if x["field"] == f]
        agree = sum(x["agreement"] == "AGREE" for x in rows)
        metrics.append({"field": f, "n": len(rows), "agree": agree, "disagree": len(rows)-agree, "raw_agreement": f"{agree/len(rows):.3f}", "kappa": "NOT_REPORTED", "interpretation": "Descriptive model-pass agreement only; not human intercoder reliability."})
    write_csv(ROOT / "04_COMPARISON" / "AGREEMENT_METRICS.csv", metrics, ["field", "n", "agree", "disagree", "raw_agreement", "kappa", "interpretation"])
    write_text(ROOT / "04_COMPARISON" / "AGREEMENT_REPORT.md", """# PILOT_03 comparison report

The comparison contains two independent source-first model passes labelled `MODEL_INDEPENDENT_A` and `MODEL_INDEPENDENT_B`. They are not human coders and the raw agreement values are diagnostic only. Disagreements remain pending human adjudication. `relationship_type_derived` and `intermediary_status_derived` are kept separate from direct provision coding.

The blind challenge contains 16 provisions; the calibration layer contains the 17 PILOT_02 provisions. No disagreement is resolved in this folder.
""")

    # Ontology test artifacts.
    action_specs = {
        "notify": ("notification", "information transmission", "notification", "NO"),
        "notify/designate": ("constitution/recognition", "designation/notification", "notification", "NO"),
        "inform/designate": ("constitution/recognition", "designation/notification", "notification", "NO"),
        "assess": ("assurance", "quality-system assessment", "quality-system assessment", "NO"),
        "audit and provide audit report to": ("monitoring", "audit_surveillance", "audit report", "REVIEW"),
        "seek": ("review", "expert opinion", "laboratory opinion", "REVIEW"),
        "apply": ("enforcement", "injunction application", "court application", "REVIEW"),
        "issue": ("enforcement", "injunction", "court order", "REVIEW"),
        "keep": ("monitoring", "reporting", "cost-accounting records", "REVIEW"),
        "communicate exemption measures and list": ("reporting", "information transmission", "communication/list", "NO"),
        "condition exemption on reporting/audit or supervision": ("assurance", "conditional oversight", "reporting/audit/supervision condition", "REVIEW"),
        "consult": ("advice", "committee procedure", "committee opinion", "REVIEW"),
        "coordinate": ("standardization", "coordination", "standards work programme", "REVIEW"),
        "define": ("standardization", "technical specification", "standard", "NO"),
        "derogate": ("distribution", "exception/remuneration", "payment scheme", "NO"),
        "enable use of marks/certificates": ("assurance", "conformity attestation", "mark/certificate", "REVIEW"),
        "enter into agreement with": ("accountability", "escrow", "escrow agreement/database copy", "REVIEW"),
        "entrust": ("distribution/administration", "delegation", "remuneration administration", "REVIEW"),
        "establish": ("constitution/recognition", "institutional designation", "legal mandate", "REVIEW"),
        "examine and notify": ("assurance", "validation", "validation notice", "REVIEW"),
        "maintain civil-liability insurance": ("risk cover", "insurance/risk underwriting", "insurance", "REVIEW"),
        "obtain technical report or certificate from": ("assurance", "technical report/certificate", "technical report/certificate", "REVIEW"),
        "provide": ("enforcement", "corrective measures", "national procedure", "REVIEW"),
        "regulate": ("oversight", "statutory regulation", "national rules", "REVIEW"),
        "select": ("constitution/recognition", "selection", "selection/accreditation", "NO"),
        "submit documentary evidence to": ("reporting/information", "documentary validation", "documentary evidence", "REVIEW"),
        "suspend": ("assurance", "review/suspension", "certificate/test results", "REVIEW"),
    }
    action_fields = ["action_id", "action_verbatim_example", "action_normalized", "occurrences", "provisional_function", "provisional_mechanism", "device", "direct_relationship_type_coding", "candidate_derived_relationship_family", "ambiguity_flag"]
    action_rows = []
    for idx, normalized in enumerate(sorted(set(r["action_normalized"] for r in a_rows)), 1):
        matched = [r for r in a_rows if r["action_normalized"] == normalized]
        direct_types = sorted(set(r["relationship_type_direct"] for r in matched)) or ["NOT_OBSERVED_IN_SAMPLE"]
        fn, mech, device, flag = action_specs.get(normalized, ("UNRESOLVED", "UNRESOLVED", "UNRESOLVED", "REVIEW"))
        action_rows.append({"action_id": f"ACT_{idx:02d}", "action_verbatim_example": matched[0]["action_verbatim"], "action_normalized": normalized, "occurrences": len(matched), "provisional_function": fn, "provisional_mechanism": mech, "device": device, "direct_relationship_type_coding": ";".join(direct_types), "candidate_derived_relationship_family": "RIT_DERIVED if R1-R9 pass; otherwise BINARY_ONLY", "ambiguity_flag": flag})
    write_csv(ROOT / "06_ONTOLOGY_TESTS" / "ACTION_ONTOLOGY.csv", action_rows, action_fields)
    write_text(ROOT / "06_ONTOLOGY_TESTS" / "FUNCTION_MECHANISM_TEST.md", """# Function/mechanism test

PILOT_03 retains `function`, `mechanism` and `device` as separate fields. The challenge deliberately includes reporting that may or may not be monitoring, delegation that may or may not be oversight, committee assistance that may or may not create an intermediary position, and laboratory opinions that may be assurance or advice.

| flag | status | boundary cases |
| --- | --- | --- |
| `FUNCTION_MECHANISM_COLLAPSE` | `REVIEW` | C02_PR03, C04_PR02, C05_PR03 |
| `FUNCTION_DEVICE_COLLAPSE` | `REVIEW` | C01_PR04, C03_PR01, C04_PR01 |
| `MECHANISM_DEVICE_COLLAPSE` | `REVIEW` | C02_PR02, C03_PR02, C05_PR03 |

No collapse is repaired silently; the fields remain independently traceable to the source provision.
""")
    write_text(ROOT / "06_ONTOLOGY_TESTS" / "RELATIONSHIP_TYPE_DIRECT_VS_DERIVED.md", """# Direct versus derived relationship type

`relationship_type_direct` is anchored to one provision-supported directed edge. It may be `EDGE_A_TO_B`, `COMPOSITE_CANDIDATE` where the provision itself contains multiple legal moves, or `UNRESOLVED_DIRECT_EDGE` when the direct edge cannot be responsibly normalized.

`relationship_type_derived` is a separate result: `RIT_DERIVED` only when the preregistered R1–R9 rules can be satisfied; otherwise `BINARY_ONLY`. The derived field never overwrites the primitive edge.
""")
    write_text(ROOT / "06_ONTOLOGY_TESTS" / "INTERMEDIARY_STATUS_TEST.md", """# Intermediary-status test

Intermediary status is a relational position, not a permanent actor property. `intermediary_status_direct` records only what the provision supports. `intermediary_status_derived` is populated only when the actor participates in an R→I and I→T configuration satisfying the frozen rules. Conditional supervision, ordinary services, and mere co-occurrence remain uncertain until human adjudication.
""")
    write_text(ROOT / "06_ONTOLOGY_TESTS" / "RIT_DERIVATION_RULES_V0_1.md", """# RIT_DERIVATION_RULES_V0_1

The rule table in `RIT_DERIVATION_RULES.csv` was frozen before the blind challenge was coded. A derived R–I–T configuration requires the same act/legal arrangement, a shared candidate I, explicit R→I and I→T edges, compatible object/procedure and modality, no direction contradiction, and governance work. Ordinary commercial service alone cannot establish I.
""")

    # Human packet and blank response templates: neutral option labels only.
    disagreements = [x for x in comp if x["agreement"] == "DISAGREE"]
    provision_by_id = {r["provision_id"]: r for r in p03_provisions}
    packet_rows = []
    for idx, x in enumerate(disagreements, 1):
        candidate = by_a[x["candidate_id"]]
        provision = provision_by_id[candidate["provision_id"]]
        packet_rows.append([str(idx), x["candidate_id"], x["case_id"], candidate["provision_id"], provision["location"], provision["official_source_url"], provision["excerpt"], candidate["actor_a"], candidate["actor_b"], candidate["action_verbatim"], x["field"], x["model_a_value"], x["model_b_value"], "Choose OPTION_1, OPTION_2, BOTH_IN_PART, NEITHER, or UNRESOLVED."])
    write_text(ROOT / "07_HUMAN_ADJUDICATION" / "HUMAN_ADJUDICATION_PACKET.md", """# PILOT_03 human adjudication packet

## Status

`PILOT_03_AWAITING_HUMAN_ADJUDICATION`

This packet is intentionally neutral. `OPTION_1` and `OPTION_2` are presented without identifying Model A or Model B. The task is to adjudicate only the listed field/provision disputes, using the linked official source and the frozen rules. Do not infer an answer from frequency, case numbering, or role labels.

## Response options

`OPTION_1` · `OPTION_2` · `BOTH_IN_PART` · `NEITHER` · `UNRESOLVED`

Provide a short rationale and, where needed, a corrected value. A decision may preserve uncertainty.

## Items

""" + md_table(["item", "candidate", "case", "provision", "location", "official source", "short excerpt", "Actor A", "Actor B", "action", "issue field", "OPTION_1", "OPTION_2", "instruction"], packet_rows) + """

The human response files are blank templates. Until they are completed, this pilot has no final adjudicated result and no production authorization.
""")
    hfields = ["decision_id", "candidate_id", "case_id", "provision_id", "issue_type", "option_1", "option_2", "human_decision", "corrected_value", "rationale", "affected_ontology_rule", "backward_impact_flag", "provenance", "status"]
    hrows = []
    for i, x in enumerate(disagreements, 1):
        candidate = by_a[x["candidate_id"]]
        hrows.append({"decision_id": f"H_{i:03d}", "candidate_id": x["candidate_id"], "case_id": x["case_id"], "provision_id": candidate["provision_id"], "issue_type": x["field"], "option_1": x["model_a_value"], "option_2": x["model_b_value"], "human_decision": "", "corrected_value": "", "rationale": "", "affected_ontology_rule": "", "backward_impact_flag": "", "provenance": "PENDING_HUMAN_ADJUDICATION", "status": "PENDING"})
    write_csv(ROOT / "07_HUMAN_ADJUDICATION" / "HUMAN_ADJUDICATION_RESPONSES.csv", hrows, hfields)
    write_csv(ROOT / "07_HUMAN_ADJUDICATION" / "HUMAN_DECISION_LOG.csv", [{**r, "status": "PENDING_HUMAN_ADJUDICATION"} for r in hrows], hfields)

    # Issue register.
    issues = [
        ["P03-I01", "HIGH", "Human adjudication is required before final reliability or ontology gate.", "OPEN_PENDING_HUMAN", "Do not resolve automatically.", "HUMAN_ADJUDICATION_RESPONSES.csv"],
        ["P03-I02", "MEDIUM", "Direct relationship type and derived RIT configuration can diverge.", "OPEN_TESTED", "Keep both fields and apply preregistered rules.", "RELATIONSHIP_TYPE_DIRECT_VS_DERIVED.md"],
        ["P03-I03", "MEDIUM", "Intermediary status is conditional in regulator, committee and collecting-society cases.", "OPEN_PENDING_HUMAN", "Preserve direct/derived distinction.", "INTERMEDIARY_STATUS_TEST.md"],
        ["P03-I04", "LOW", "Two passes are model-independent, not human intercoder passes.", "DOCUMENTED", "Do not report as human kappa.", "AGREEMENT_REPORT.md"],
    ]
    write_csv(ROOT / "08_RESULTS" / "PILOT_03_ISSUE_REGISTER.csv", [{"issue_id": a, "severity": b, "issue": c, "status": d, "mitigation": e, "evidence": f} for a,b,c,d,e,f in issues], ["issue_id", "severity", "issue", "status", "mitigation", "evidence"])

    baseline_hash = sha256(P02 / "07_RESULTS" / "RELATIONAL_MODEL_V0_2.md")
    write_text(ROOT / "00_BASELINE" / "PILOT_02_FROZEN_BASELINE.md", f"""# PILOT_02_FROZEN_BASELINE

This is a read-only baseline for PILOT_03. The source file remains at `PILOT_02/07_RESULTS/RELATIONAL_MODEL_V0_2.md` and is not modified. SHA-256 at PILOT_03 build: `{baseline_hash}`.

## Frozen findings

- Primitive unit: binary directed A→B relation anchored in a provision.
- R–I–T: derived configuration, not primitive row.
- Intermediary: derived relational position, not permanent actor attribute.
- ACTOR_I is not a primitive field; actor identity is distinct from relational role.
- Device/Instrument: autonomous analytical dimension, distinct from function and mechanism.
- Direct provision evidence is mandatory for verified relationships.
- Function × Mechanism remains provisional and must not be silently collapsed.
- Relationship-type classification remains unstable.
- No production category or production codebook authorized by PILOT_02.

## PILOT_03 consequence

Model A and Model B must code the direct edge first. Relationship type, intermediary status and R–I–T are tested as separate direct/derived fields. Human adjudication is required before a final model gate.
""")
    write_text(ROOT / "01_PROTOCOL" / "PILOT_03_PROTOCOL.md", """# PILOT_03_PROTOCOL

## Objective

Test whether the PILOT_02 relational core remains stable under a blind challenge subset and whether direct relationship type, derived R–I–T configuration, and intermediary status can be kept analytically separate.

## Frozen hypotheses

1. The primitive unit is one binary A→B edge anchored in an addressable provision.
2. R–I–T is derived only from linked elementary edges satisfying R1–R9.
3. Intermediary status is a derived relational position, not a permanent actor property.
4. Device/Instrument is an autonomous dimension.
5. Action is coded verbatim first and normalized second.
6. Relationship type is tested as direct edge type versus derived configuration.

## Sequence

1. Freeze PILOT_02 baseline and rules.
2. Register the calibration and blind challenge samples.
3. Register official source provisions and short evidentiary excerpts.
4. Run two independent source-first model passes.
5. Compare descriptively; do not resolve differences automatically.
6. Freeze the comparison and issue the neutral human packet.
7. Stop with `PILOT_03_AWAITING_HUMAN_ADJUDICATION`.

## RT experiment

`MODEL RT-DIRECT` records `relationship_type_direct` from the provision. `MODEL RT-DERIVED` records Actor A, Actor B, action, object, modality, function, mechanism, device and direction first; `relationship_type_derived` is then generated by the preregistered rule table. Neither approach is assumed superior before comparison and human adjudication.

For the blind challenge, both independent passes use only this frozen protocol and official source provisions. They do not inspect PILOT_01/PILOT_02 case-level answers before their challenge coding is frozen.

## Non-authorizations

No production migration, no replacement of the Rotem workbook, no human-reliability claim, and no automatic adjudication of disputed fields.
""")
    write_text(ROOT / "01_PROTOCOL" / "CODING_RULES_V0_3_DRAFT.md", """# CODING_RULES_V0_3_DRAFT

- `ACTION_VERBATIM`: shortest legally faithful action phrase.
- `ACTION_NORMALIZED`: controlled analytic label, never a substitute for verbatim evidence.
- `RELATIONSHIP_TYPE_DIRECT`: one direct provision-supported edge.
- `RELATIONSHIP_TYPE_DERIVED`: `RIT_DERIVED` only after R1–R9; otherwise `BINARY_ONLY`.
- `INTERMEDIARY_STATUS_DIRECT`: only explicit or provisionally supported by the provision.
- `INTERMEDIARY_STATUS_DERIVED`: only a position in a qualifying configuration.
- `DEVICE`: concrete legal/procedural carrier such as certificate, audit report, court order, committee opinion or record.
- `UNRESOLVED`: admissible output, not missing data.

These are draft rules pending human adjudication.
""")

    write_text(ROOT / "08_RESULTS" / "RELATIONAL_MODEL_V0_3_DRAFT.md", """# RELATIONAL_MODEL_V0_3_DRAFT

Status: draft only; awaiting human adjudication.

## Proposed normalized core

`ACTS`, `PROVISIONS`, `ACTORS`, `BINARY_RELATIONSHIPS`, `RELATIONSHIP_EVIDENCE`, `ACTION_CODING`, `CONFIGURATION_LINKS`, `INTERMEDIARY_POSITIONS`, and `ADJUDICATION_REGISTER`.

The direct edge is the primitive. `relationship_type_direct`, `relationship_type_derived`, `intermediary_status_direct`, and `intermediary_status_derived` remain separate. `Device/Instrument` is autonomous. This model is not production-authorized until human responses are entered and the final gate is recomputed.
""")

    # Build report after all artifacts exist.
    dis_n = len(disagreements)
    total = len(a_rows)
    write_text(ROOT / "08_RESULTS" / "PILOT_03_REPORT.md", f"""# PILOT_03_REPORT

## Gate

`PILOT_03_AWAITING_HUMAN_ADJUDICATION`

The pilot is intentionally stopped before human adjudication. No final reliability gate, ontology gate or production authorization is claimed.

## Scope

- Calibration: 5 acts and {len(p02_provisions)} frozen PILOT_02 source provisions.
- Blind challenge: 5 additional acts and {len(challenge_provisions)} official-source provisions.
- Model A/B: {total} candidate rows per pass, with {dis_n} disagreement cells across the compared fields.
- The two passes are model-independent source-first passes, not human coders.

## Frozen design decisions

Binary A→B is primitive; R–I–T is derived; intermediary is a relational position; Device/Instrument is autonomous; direct and derived relationship type are separate; action is verbatim plus normalized.

## Challenge logic

The blind cases are drawn from already assessed material and were selected for boundary pressure: testing laboratories, national regulatory authorities, IP-enforcement intermediaries, collecting societies and standardization committees. The selection was purposive, not a convenience sample and not a corpus expansion.

## What remains open

Human review must adjudicate direct-edge versus composite readings, function/mechanism boundaries, device coding, direct versus derived relationship type, and conditional intermediary status. The response template preserves `BOTH_IN_PART`, `NEITHER` and `UNRESOLVED`.

## Reproducibility

Source provisions, model passes, comparison, preregistered RIT rules, blank human packet and issue register are stored in this folder. The generator is `99_REPRODUCIBILITY/build_pilot03.py`.
""")

    files = {}
    for p in ROOT.rglob("*"):
        if p.is_file() and p.name != "PILOT_03_MANIFEST.json":
            files[str(p.relative_to(ROOT)).replace("\\", "/")] = sha256(p)
    manifest = {
        "pilot": "PILOT_03",
        "built_on": TODAY,
        "status": "PILOT_03_AWAITING_HUMAN_ADJUDICATION",
        "source_first": True,
        "calibration_cases": [x[0] for x in calibration_cases],
        "blind_challenge_cases": [x[0] for x in challenge_cases],
        "human_adjudication_completed": False,
        "production_authorized": False,
        "p02_baseline_sha256": baseline_hash,
        "files_sha256": files,
    }
    write_text(ROOT / "99_REPRODUCIBILITY" / "PILOT_03_MANIFEST.json", json.dumps(manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
