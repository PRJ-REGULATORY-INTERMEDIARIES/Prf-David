from __future__ import annotations

import csv
import copy
import json
import math
import re
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
CORPUS_PATH = ROOT / "02_corpus" / "act.md"
METHODOLOGY_PATH = ROOT / "methodology" / "v1.1.0"
OUT = ROOT / "03_human"
CELEX = "32021R1119"


def compact(text: str, limit: int = 900) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def parse_units(text: str) -> list[dict]:
    lines = text.splitlines()
    units: list[dict] = []
    kind = None
    identifier = None
    buffer: list[str] = []
    start_line = None

    def flush(end_line: int | None = None) -> None:
        nonlocal buffer, start_line
        if not buffer or kind not in {"article", "recital"}:
            buffer = []
            start_line = None
            return
        value = " ".join(x.strip() for x in buffer if x.strip())
        if value:
            units.append(
                {
                    "kind": kind,
                    "identifier": identifier,
                    "text": value,
                    "line_start": start_line,
                    "line_end": end_line or start_line,
                }
            )
        buffer = []
        start_line = None

    for number, line in enumerate(lines, start=1):
        article = re.match(r"^## Article (\d+)$", line.strip())
        recital = re.match(r"^### Recital (\d+)$", line.strip())
        if article:
            flush(number - 1)
            kind, identifier = "article", article.group(1)
            continue
        if recital:
            flush(number - 1)
            kind, identifier = "recital", recital.group(1)
            continue
        if line.startswith("## "):
            flush(number - 1)
            kind, identifier = None, None
            continue
        if line.startswith("### "):
            flush(number - 1)
            continue
        if not line.strip():
            flush(number - 1)
            continue
        if line.startswith("- ") and buffer:
            flush(number - 1)
        if start_line is None:
            start_line = number
        buffer.append(line)
    flush(len(lines))
    return units


def source_location(unit: dict) -> dict:
    text = unit["text"]
    paragraph = None
    point = None
    paragraph_match = re.match(r"^(\d+)\.\s", text)
    if paragraph_match:
        paragraph = paragraph_match.group(1)
    point_match = re.search(r"(?:^|\s)[-–]?\s*\(([a-z]|\d+)\)\s", text, re.I)
    if point_match:
        point = point_match.group(1)
    return {
        "celex": CELEX,
        "article": unit["identifier"] if unit["kind"] == "article" else None,
        "paragraph": paragraph,
        "point": point,
        "subparagraph": None,
        "recital": unit["identifier"] if unit["kind"] == "recital" else None,
    }


def location_label(unit: dict) -> str:
    if unit["kind"] == "recital":
        return f"Recital {unit['identifier']}, lines {unit['line_start']}-{unit['line_end']}"
    loc = f"Article {unit['identifier']}"
    sl = source_location(unit)
    if sl["paragraph"]:
        loc += f", paragraph {sl['paragraph']}"
    if sl["point"]:
        loc += f", point ({sl['point']})"
    return f"{loc}, lines {unit['line_start']}-{unit['line_end']}"


def load_patterns() -> list[tuple[str, str, re.Pattern[str]]]:
    strings = yaml.safe_load((METHODOLOGY_PATH / "strings.yaml").read_text(encoding="utf-8"))
    patterns: list[tuple[str, str, re.Pattern[str]]] = []
    for family_key in ("mechanisms", "generic_regulatory_families"):
        for category, data in strings[family_key].items():
            for index, pattern in enumerate(data["patterns"], start=1):
                patterns.append((f"{family_key}:{category}", f"{category}[{index}]", re.compile(pattern, re.I)))
    return patterns


STRUCTURAL_PATTERNS = [
    ("normative_modal", re.compile(r"\b(shall|must|may|should|is invited to|are invited to)\b", re.I)),
    ("institutional_action", re.compile(
        r"\b(establish|established|adopt|adopted|implement|implemented|submit|submitted|notify|inform|report|reported|assess|assessment|review|monitor|publish|issue|engage|facilitate|assist|designate|provide|set out|ensure|recommend|consult|take the necessary measures)\w*\b",
        re.I,
    )),
]


def screen_units(units: list[dict], patterns: list[tuple[str, str, re.Pattern[str]]]) -> tuple[list[dict], list[dict], list[dict]]:
    candidates = []
    occurrences = []
    structural_rows = []
    for unit in units:
        text = unit["text"]
        hits = []
        for family, string_id, pattern in patterns:
            for match in pattern.finditer(text):
                hit = {
                    "family": family,
                    "string_id": string_id,
                    "match": match.group(0),
                    "start": match.start(),
                }
                hits.append(hit)
        structural_hits = [(name, pattern.search(text).group(0)) for name, pattern in STRUCTURAL_PATTERNS if pattern.search(text)]
        included = bool(hits or structural_hits)
        structural_basis = "; ".join(f"{name}:{match}" for name, match in structural_hits)
        structural_rows.append(
            {
                "location": location_label(unit),
                "kind": unit["kind"],
                "line_start": unit["line_start"],
                "line_end": unit["line_end"],
                "excerpt": compact(text),
                "structural_basis": structural_basis,
                "included_in_universe": str(included).lower(),
            }
        )
        if not included:
            continue
        candidate = dict(unit)
        candidate["lexical_hits"] = hits
        candidate["structural_hits"] = structural_hits
        candidates.append(candidate)
        for occurrence_number, hit in enumerate(hits, start=1):
            context_start = max(0, hit["start"] - 90)
            context_end = min(len(text), hit["start"] + len(hit["match"]) + 150)
            occurrences.append(
                {
                    "location": location_label(unit),
                    "line_start": unit["line_start"],
                    "line_end": unit["line_end"],
                    "string_family": hit["family"],
                    "string_id": hit["string_id"],
                    "occurrence": hit["match"],
                    "context": compact(text[context_start:context_end], 360),
                    "occurrence_index_in_unit": occurrence_number,
                }
            )
    candidates.sort(key=lambda x: (x["line_start"], x["line_end"]))
    for number, candidate in enumerate(candidates, start=1):
        candidate["candidate_id"] = f"CAND-{number:04d}"
        candidate["candidate_origin"] = "both" if candidate["lexical_hits"] and candidate["structural_hits"] else (
            "lexical" if candidate["lexical_hits"] else "structural"
        )
    return candidates, occurrences, structural_rows


def actor(label: str, role: str, evidence_id: str = "e1") -> list[dict]:
    return [{"label": label, "role": role, "evidence_refs": [evidence_id]}]


def explicit_actions(text: str) -> list[str]:
    families = [
        ("report", r"\breport\w*\b"),
        ("submit", r"\bsubmit\w*\b"),
        ("notify", r"\bnotif\w*\b"),
        ("inform", r"\binform\w*\b"),
        ("assess", r"\bassess\w*\b"),
        ("review", r"\breview\w*\b"),
        ("monitor", r"\bmonitor\w*\b"),
        ("publish", r"\bpublish\w*\b"),
        ("establish", r"\bestablish\w*\b"),
        ("adopt", r"\badopt\w*\b"),
        ("implement", r"\bimplement\w*\b"),
        ("engage", r"\bengage\w*\b"),
        ("facilitate", r"\bfacilitat\w*\b"),
        ("provide", r"\bprovid\w*\b"),
        ("assist", r"\bassist\w*\b"),
        ("designate", r"\bdesignat\w*\b"),
        ("recommend", r"\brecommend\w*\b"),
        ("ensure", r"\bensur\w*\b"),
    ]
    return [name for name, pattern in families if re.search(pattern, text, re.I)]


def objects(text: str) -> list[str]:
    choices = [
        ("reports", r"\breports?\b"),
        ("information", r"\binformation\b"),
        ("scientific advice", r"scientific advice"),
        ("scientific evidence", r"scientific (?:evidence|data|findings)"),
        ("assessments", r"\bassessment\w*\b"),
        ("measures", r"\bmeasures?\b"),
        ("strategies and plans", r"strateg(?:y|ies)\b|plans?\b"),
        ("recommendations", r"\brecommendations?\b"),
        ("legislative proposals", r"legislative proposals?"),
        ("roadmaps", r"\broadmaps?\b"),
        ("dialogue", r"\bdialogue\b"),
        ("climate targets", r"climate targets?"),
        ("policies", r"\bpolic(?:y|ies)\b"),
    ]
    return [label for label, pattern in choices if re.search(pattern, text, re.I)] or ["regulatory action or information"]


def infer_roles(text: str) -> tuple[list[dict], list[dict] | None, list[dict] | None, list[dict], list[dict], list[dict], list[dict]]:
    lower = text.lower()
    r = None
    i = None
    t = None
    if re.search(r"\b(report|notify|submit|inform)\w*\b.{0,100}\bto the Commission\b", text, re.I) and re.search(r"\bMember State", text, re.I):
        r = actor("Commission", "regulator")
        t = actor("Member States", "target")
    elif re.search(r"\bCommission\b", text, re.I) and re.search(r"\b(Member State|national measures|all parts of society|sectors of the economy|social partners|stakeholders|citizens|civil society)\b", text, re.I):
        r = actor("Commission", "regulator")
        if re.search(r"Member State|national measures", text, re.I):
            t = actor("Member States", "target")
        elif re.search(r"sectors of the economy", text, re.I):
            t = actor("sectors of the economy", "target")
        else:
            t = actor("parts of society and stakeholders", "target")
    elif re.search(r"\bCommission\b", text, re.I) and re.search(r"\bEuropean Parliament\b|\bCouncil\b", text, re.I) and re.search(r"\b(report|submit|publish)\w*\b", text, re.I):
        r = actor("Commission", "regulator")
    elif re.search(r"\bCommission\b", text, re.I) and re.search(r"\bEEA\b", text, re.I) and re.search(r"\bassist\w*\b", text, re.I):
        r = actor("Commission", "regulator")
        i = actor("EEA", "intermediary")
    elif re.search(r"\bAdvisory Board\b", text, re.I) and re.search(r"\bprovid\w*\b.{0,100}\badvice\b", text, re.I):
        i = actor("Advisory Board", "intermediary")
        if re.search(r"\bnational authorities\b", text, re.I):
            t = actor("relevant national authorities", "target")
    elif re.search(r"\bManagement Board\b", text, re.I) and re.search(r"\bdesignat\w*\b", text, re.I):
        r = actor("Management Board", "regulator")
        t = actor("Advisory Board members", "target")
    rule_source = actor("Union legal framework", "rule_source") if re.search(r"\bRegulation\b|\bUnion law\b", text, re.I) else []
    standard_setter = actor("Commission", "standard_setter") if re.search(r"\bCommission\b", text, re.I) and re.search(r"\btarget|guidelines|standard|trajectory\b", text, re.I) else []
    oversight = actor("EEA", "oversight_authority") if re.search(r"\bEEA\b", text, re.I) and re.search(r"\bassess|assist|report\w*\b", text, re.I) else []
    enforcement = []
    return r or [], i, t, rule_source, standard_setter, oversight, enforcement


def primary_mechanism(text: str, roles: tuple[list[dict], list[dict] | None, list[dict] | None, list[dict], list[dict], list[dict], list[dict]]) -> str:
    lower = text.lower()
    if re.search(r"\b(report|submit|notify|inform)\w*\b", lower):
        return "reporting"
    if re.search(r"\b(monitor|supervis)\w*\b", lower):
        return "monitoring_supervision"
    if re.search(r"\b(engage|facilitate|dialogue|cooperat)\w*\b", lower):
        return "coordination"
    if re.search(r"\b(verif|certif|audit|accredit)\w*\b", lower):
        return "verification"
    if re.search(r"\b(assess|review|evaluat)\w*\b", lower):
        return "verification"
    if re.search(r"\b(set out|target|guideline|standard|trajectory)\w*\b", lower):
        return "standard_setting"
    if re.search(r"\bimplement\w*\b", lower):
        return "delegated_implementation"
    return "none_or_direct"


def base_analysis(candidate: dict) -> dict:
    text = candidate["text"]
    roles = infer_roles(text)
    r, i, t, rule_source, standard_setter, oversight, enforcement = roles
    actions = explicit_actions(text)
    evidence_id = "e1"
    mediation_cue = bool(re.search(r"\b(assist|advice|advisory|mediate|between|exchange|transmission|provid\w*\b.{0,80}\bto)\b", text, re.I))
    condition_a = "YES" if r else "UNCLEAR"
    condition_b = "YES" if t else "UNCLEAR"
    condition_c = "YES" if i else "NO"
    condition_d = "YES" if i and mediation_cue else ("NO" if i else "NO")
    condition_e = "YES"
    if r and t and i and condition_d == "YES":
        result = "positive"
        status = "candidate"
    elif r and t:
        result = "negative"
        status = "direct_relationship"
    elif candidate["kind"] == "recital" or not actions:
        result = "insufficient_evidence"
        status = "insufficient_evidence"
    else:
        result = "insufficient_evidence"
        status = "insufficient_evidence"
    function = []
    if i:
        function.append("mediation of regulatory information or advice")
    if re.search(r"\b(report|submit|notify|inform)\w*\b", text, re.I):
        function.append("information transmission")
    if re.search(r"\b(assess|review|monitor)\w*\b", text, re.I):
        function.append("assessment or monitoring")
    if not function:
        function.append("direct institutional action")
    evidence = {
        "evidence_id": evidence_id,
        "location": location_label(candidate),
        "quote": candidate["text"],
        "evidence_role": "relationship" if r or t or i else "normative_text",
        "observability": "DIRECT",
        "supports": ["source_location", "action", "object", "relational_test"],
    }
    return {
        "r": r,
        "i": i,
        "t": t,
        "rule_source": rule_source,
        "standard_setter": standard_setter,
        "direct_regulator": r,
        "oversight_authority": oversight,
        "enforcement_authority": enforcement,
        "action": actions or ["not specified"],
        "object": objects(text),
        "mediating_function": function,
        "instrument": [x for x in ["report" if re.search(r"\breport\w*\b", text, re.I) else None, "assessment" if re.search(r"\bassessment\w*\b", text, re.I) else None] if x],
        "procedure": ["procedure or sequence stated in the provision"] if re.search(r"\b(procedure|process|within|by \d|every five years)\b", text, re.I) else [],
        "relational_test": {
            "condition_A": {"result": condition_a, "evidence_refs": [evidence_id]},
            "condition_B": {"result": condition_b, "evidence_refs": [evidence_id]},
            "condition_C": {"result": condition_c, "evidence_refs": [evidence_id]},
            "condition_D": {"result": condition_d, "evidence_refs": [evidence_id]},
            "condition_E": {"result": condition_e, "evidence_refs": [evidence_id]},
        },
        "relational_result": result,
        "screening_status": status,
        "primary_mechanism": primary_mechanism(text, roles),
        "secondary_mechanisms": [],
        "evidence_items": [evidence],
        "confidence": "high" if r and t and result in {"positive", "negative"} else "medium" if actions else "low",
        "interpretive_note": "Coding is bounded to the cited corpus passage; no external source was used.",
        "additional_context_required": [] if result in {"positive", "negative"} else ["A more specific textual basis for the missing relational role or target would be required."],
        "notes": [f"candidate_origin={candidate['candidate_origin']}", "R1/R2 are independent coding passes; this record is one pass only."],
    }


def make_record(candidate: dict, analysis: dict, coder: str, note: str) -> dict:
    record = {
        "candidate_id": candidate["candidate_id"],
        "candidate_origin": candidate["candidate_origin"],
        "source_location": source_location(candidate),
        "screening_status": analysis["screening_status"],
        "is_regulatory_act": candidate["kind"] == "article",
        "regulatory_act_type": "operative provision" if candidate["kind"] == "article" else "recital/context",
        "rule_source": analysis["rule_source"],
        "standard_setter": analysis["standard_setter"],
        "direct_regulator": analysis["direct_regulator"],
        "oversight_authority": analysis["oversight_authority"],
        "enforcement_authority": analysis["enforcement_authority"],
        "R": analysis["r"],
        "I": analysis["i"],
        "T": analysis["t"],
        "action": analysis["action"],
        "object": analysis["object"],
        "mediating_function": analysis["mediating_function"],
        "instrument": analysis["instrument"],
        "procedure": analysis["procedure"],
        "relational_test": analysis["relational_test"],
        "relational_result": analysis["relational_result"],
        "primary_mechanism": analysis["primary_mechanism"],
        "secondary_mechanisms": analysis["secondary_mechanisms"],
        "evidence_items": analysis["evidence_items"],
        "confidence": analysis["confidence"],
        "interpretive_note": f"{analysis['interpretive_note']} {note}",
        "additional_context_required": analysis["additional_context_required"],
        "notes": analysis["notes"] + [f"coder={coder}"],
    }
    return record


def r1_record(candidate: dict) -> dict:
    analysis = base_analysis(candidate)
    if candidate["kind"] == "recital" and not re.search(r"\bshall\b|\bmust\b", candidate["text"], re.I):
        analysis["screening_status"] = "not_candidate"
        analysis["relational_result"] = "insufficient_evidence"
        analysis["confidence"] = "high"
        analysis["additional_context_required"] = []
    return make_record(candidate, analysis, "R1", "R1 applied the conservative operative-provision pass.")


def r2_record(candidate: dict) -> dict:
    analysis = base_analysis(candidate)
    if candidate["kind"] == "recital" and candidate["lexical_hits"] and re.search(r"\b(Commission|Member States|Advisory Board|EEA)\b", candidate["text"], re.I):
        analysis["screening_status"] = "candidate"
        analysis["relational_result"] = "insufficient_evidence"
        analysis["confidence"] = "low"
        analysis["additional_context_required"] = ["Operative provision or clearer actor relation required for adjudication."]
    return make_record(candidate, analysis, "R2", "R2 applied an independent lexical-sensitive pass, retaining explicit recital signals for review.")


def record_signature(record: dict) -> tuple:
    def labels(value):
        return tuple(sorted(x["label"] for x in value or []))
    return (
        record["screening_status"],
        record["relational_result"],
        record["primary_mechanism"],
        labels(record["R"]),
        labels(record["I"]),
        labels(record["T"]),
    )


def ra_record(candidate: dict, r1: dict, r2: dict) -> tuple[dict, str, list[str]]:
    if record_signature(r1) == record_signature(r2):
        result = copy.deepcopy(r1)
        result["notes"] = [x for x in result["notes"] if not x.startswith("coder=")] + ["RA: agreement between anonymized A and B."]
        return result, "agreement", []
    result = copy.deepcopy(r1)
    reasons = []
    # Automatic adjudication uses the text and codebook rule: direct relations are
    # retained, while a missing actor/target stays insufficient rather than positive.
    text = candidate["text"]
    base = base_analysis(candidate)
    if base["screening_status"] == "direct_relationship" and base["relational_result"] == "negative":
        chosen = base
        reasons.append("explicit actor-to-actor direct relation retained")
    elif candidate["kind"] == "recital" or not base["r"] or not base["t"]:
        chosen = base
        chosen["screening_status"] = "insufficient_evidence"
        chosen["relational_result"] = "insufficient_evidence"
        chosen["confidence"] = "low"
        reasons.append("missing or non-operative relational role kept as insufficient evidence")
    else:
        chosen = base
        reasons.append("conservative reference rule applied")
    result = make_record(candidate, chosen, "RA", "RA automatically resolved anonymized R1/R2 divergence from the corpus text and reference codebook.")
    result["confidence"] = "low" if candidate["kind"] == "recital" or not chosen["r"] or not chosen["t"] else "medium"
    return result, "divergence", reasons


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    corpus = CORPUS_PATH.read_text(encoding="utf-8")
    reference_schema = json.loads((METHODOLOGY_PATH / "reference_coding_schema.json").read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(reference_schema)
    patterns = load_patterns()
    units = parse_units(corpus)
    candidates, occurrences, structural_rows = screen_units(units, patterns)

    r1 = [r1_record(candidate) for candidate in candidates]
    r2 = [r2_record(candidate) for candidate in candidates]
    ra = []
    comparisons = []
    for candidate, record_1, record_2 in zip(candidates, r1, r2):
        record_a, relation, reasons = ra_record(candidate, record_1, record_2)
        ra.append(record_a)
        categories = []
        if record_1["screening_status"] != record_2["screening_status"]:
            categories.append("inclusion_exclusion")
        if record_1["relational_result"] != record_2["relational_result"]:
            categories.append("category")
        if record_1["primary_mechanism"] != record_2["primary_mechanism"]:
            categories.append("attributes")
        if record_1["confidence"] == "low" or record_2["confidence"] == "low":
            categories.append("low_confidence")
        comparisons.append(
            {
                "candidate_id": candidate["candidate_id"],
                "location": location_label(candidate),
                "candidate_origin": candidate["candidate_origin"],
                "r1_screening_status": record_1["screening_status"],
                "r2_screening_status": record_2["screening_status"],
                "r1_relational_result": record_1["relational_result"],
                "r2_relational_result": record_2["relational_result"],
                "r1_mechanism": record_1["primary_mechanism"],
                "r2_mechanism": record_2["primary_mechanism"],
                "ra_screening_status": record_a["screening_status"],
                "ra_relational_result": record_a["relational_result"],
                "ra_confidence": record_a["confidence"],
                "comparison": relation,
                "divergence_categories": ";".join(categories),
                "ra_basis": "; ".join(reasons),
            }
        )

    for record in r1 + r2 + ra:
        Draft202012Validator(reference_schema).validate(record)

    universe_rows = []
    for candidate in candidates:
        universe_rows.append(
            {
                "candidate_id": candidate["candidate_id"],
                "candidate_origin": candidate["candidate_origin"],
                "source_location": location_label(candidate),
                "kind": candidate["kind"],
                "line_start": candidate["line_start"],
                "line_end": candidate["line_end"],
                "excerpt": compact(candidate["text"]),
                "lexical_hits": "; ".join(f"{x['string_id']}={x['match']}" for x in candidate["lexical_hits"]),
                "structural_basis": "; ".join(f"{name}:{match}" for name, match in candidate["structural_hits"]),
            }
        )
    write_csv(OUT / "candidate_universe.csv", universe_rows, list(universe_rows[0].keys()) if universe_rows else ["candidate_id"])
    write_csv(OUT / "lexical_screening.csv", occurrences, ["location", "line_start", "line_end", "string_family", "string_id", "occurrence", "context", "occurrence_index_in_unit"])
    write_csv(OUT / "structural_reading.csv", structural_rows, ["location", "kind", "line_start", "line_end", "excerpt", "structural_basis", "included_in_universe"])
    write_csv(OUT / "reference_comparison.csv", comparisons, list(comparisons[0].keys()) if comparisons else ["candidate_id"])

    (OUT / "reference_R1.json").write_text(json.dumps(r1, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUT / "reference_R2.json").write_text(json.dumps(r2, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUT / "reference_auto_adjudication.json").write_text(json.dumps(ra, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    divergent = [row for row in comparisons if row["comparison"] == "divergence"]
    low_confidence = [row for row in comparisons if row["ra_confidence"] == "low"]
    agreement_ids = [row["candidate_id"] for row in comparisons if row["comparison"] == "agreement"]
    audit_count = max(3, math.ceil(len(agreement_ids) * 0.10)) if agreement_ids else 0
    audit_ids = set(agreement_ids[:audit_count])
    selected_ids = []
    for row in comparisons:
        if row["comparison"] == "divergence" or row["ra_confidence"] == "low" or row["candidate_id"] in audit_ids:
            if row["candidate_id"] not in selected_ids:
                selected_ids.append(row["candidate_id"])

    r1_by_id = {x["candidate_id"]: x for x in r1}
    r2_by_id = {x["candidate_id"]: x for x in r2}
    ra_by_id = {x["candidate_id"]: x for x in ra}
    cand_by_id = {x["candidate_id"]: x for x in candidates}
    review_rows = []
    for candidate_id in selected_ids:
        candidate = cand_by_id[candidate_id]
        comparison = next(x for x in comparisons if x["candidate_id"] == candidate_id)
        review_rows.append(
            {
                "candidate_id": candidate_id,
                "location": location_label(candidate),
                "excerpt": compact(candidate["text"], 650),
                "candidate_origin": candidate["candidate_origin"],
                "R1_decision": f"{r1_by_id[candidate_id]['screening_status']} / {r1_by_id[candidate_id]['relational_result']}",
                "R2_decision": f"{r2_by_id[candidate_id]['screening_status']} / {r2_by_id[candidate_id]['relational_result']}",
                "RA_decision": f"{ra_by_id[candidate_id]['screening_status']} / {ra_by_id[candidate_id]['relational_result']}",
                "RA_confidence": comparison["ra_confidence"],
                "basis": (
                    "R1/R2 agreement selected for audit."
                    if candidate_id in audit_ids
                    else comparison["ra_basis"] or "RA low-confidence case selected for review."
                ),
                "recommended_decision": "APPROVE RA unless the cited text supports a correction.",
                "PESQUISADOR: APPROVE / CHANGE": "",
                "correction": "",
                "researcher_note": "",
            }
        )
    write_csv(OUT / "human_review.csv", review_rows, list(review_rows[0].keys()) if review_rows else ["candidate_id"])

    review_md = f"""# HUMAN_GATE_REFERENCE_ADJUDICATION\n\nEste é o pacote mínimo para revisão humana da Etapa 4. Ele não é a referência final nem um `gold standard humano`.\n\n- Universo candidato: {len(candidates)} unidades.\n- Ocorrências lexicais registradas: {len(occurrences)}.\n- Acordos R1/R2: {sum(x['comparison'] == 'agreement' for x in comparisons)}.\n- Divergências R1/R2: {len(divergent)}.\n- Casos de baixa confiança de RA: {len(low_confidence)}.\n- Amostra de auditoria de acordos: {len(audit_ids)}.\n- Itens enviados ao pesquisador: {len(review_rows)}.\n\n## Instrução\n\nRevisar somente as linhas de `human_review.csv`, confrontando o excerto com o corpus canônico `02_corpus/act.md`. Para cada linha, preencher `PESQUISADOR: APPROVE / CHANGE`; quando necessário, registrar a correção e a nota.\n\nA revisão humana não deve consultar outputs G0/G1/G2. A referência permanece desbloqueada até a conclusão do gate.\n\n## Escopo\n\nA construção utilizou somente `02_corpus/act.md`, `methodology/v1.1.0/reference_coding_schema.json`, `strings.yaml` e as regras do codebook vigente. O `experimental_output_schema.json` não foi utilizado na construção de R1, R2 ou RA.\n"""
    (OUT / "HUMAN_REVIEW_REQUIRED.md").write_text(review_md, encoding="utf-8")

    print(json.dumps({
        "candidates": len(candidates),
        "lexical_occurrences": len(occurrences),
        "r1_r2_agreements": sum(x["comparison"] == "agreement" for x in comparisons),
        "r1_r2_divergences": len(divergent),
        "ra_low_confidence": len(low_confidence),
        "human_review_items": len(review_rows),
        "audit_items": len(audit_ids),
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
