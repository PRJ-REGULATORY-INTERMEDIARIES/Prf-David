from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[2]
CORPUS = ROOT / "02_corpus" / "act.md"
METHODOLOGY = ROOT / "methodology" / "v1.1.0"
OUT = Path(__file__).resolve().parent
CELEX = "32021R1119"


ACTOR_PATTERNS = [
    "the Commission",
    "Commission",
    "Member States",
    "Member State",
    "European Parliament",
    "the Council",
    "Council",
    "Advisory Board",
    "European Scientific Advisory Board",
    "EEA",
    "Management Board",
    "Energy Union Committee",
    "local authorities",
    "civil society organisations",
    "business community",
    "investors",
    "stakeholders",
    "general public",
    "sectors of the economy",
]

ACTION_PATTERNS = [
    r"\b(shall|must|may|should|is invited to|are invited to)\b",
    r"\b(establish|adopt|implement|submit|notify|inform|report|assess|review|monitor|publish|issue|engage|facilitate|assist|designate|provide|ensure|recommend|consult|take)\w*\b",
]

OBJECT_PATTERNS = [
    r"\breport\w*\b",
    r"\binformation\b",
    r"\bmeasure\w*\b",
    r"\bstrateg\w*\b",
    r"\bplan\w*\b",
    r"\bassessment\w*\b",
    r"\brecommendation\w*\b",
    r"\bdialogue\b",
    r"\btarget\w*\b",
    r"\bpolicy|policies\b",
]


def compact(text: str, limit: int = 1200) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def parse_document(text: str) -> list[dict]:
    lines = text.splitlines()
    units: list[dict] = []
    article = None
    recital = None
    article_heading = None
    paragraph = None
    parent_paragraph = None
    point = None
    buffer: list[str] = []
    block_start = None
    block_point = None

    def flush(end_line: int) -> None:
        nonlocal buffer, block_start, block_point
        if not buffer or (article is None and recital is None):
            buffer = []
            block_start = None
            block_point = None
            return
        focal = " ".join(part.strip() for part in buffer if part.strip())
        if not focal:
            buffer = []
            block_start = None
            block_point = None
            return
        hierarchy = []
        if article is not None:
            hierarchy.append(f"Article {article}")
            if article_heading:
                hierarchy.append(article_heading)
        if recital is not None:
            hierarchy.append(f"Recital {recital}")
        if paragraph is not None:
            hierarchy.append(f"paragraph {paragraph}")
        if block_point is not None:
            hierarchy.append(f"point ({block_point})")
        units.append(
            {
                "article": article,
                "recital": recital,
                "article_heading": article_heading,
                "paragraph": paragraph,
                "point": block_point,
                "line_start": block_start,
                "line_end": end_line,
                "focal_excerpt": focal,
                "parent_context": {
                    "hierarchy": hierarchy,
                    "article_heading": article_heading,
                    "parent_paragraph": compact(parent_paragraph or "", 900),
                },
            }
        )
        buffer = []
        block_start = None
        block_point = None

    for number, raw in enumerate(lines, start=1):
        line = raw.strip()
        article_match = re.match(r"^## Article (\d+)$", line)
        recital_match = re.match(r"^### Recital (\d+)$", line)
        if article_match:
            flush(number - 1)
            article = article_match.group(1)
            recital = None
            article_heading = None
            paragraph = None
            parent_paragraph = None
            point = None
            continue
        if recital_match:
            flush(number - 1)
            recital = recital_match.group(1)
            article = None
            article_heading = None
            paragraph = None
            parent_paragraph = None
            point = None
            continue
        if line.startswith("## "):
            flush(number - 1)
            article = None
            recital = None
            article_heading = None
            paragraph = None
            parent_paragraph = None
            point = None
            continue
        if line.startswith("### ") and not buffer:
            article_heading = line[4:].strip()
            continue
        if not line:
            flush(number - 1)
            point = None
            continue
        paragraph_match = re.match(r"^(\d+)\.\s+(.*)$", line)
        if paragraph_match and not line.startswith("- "):
            flush(number - 1)
            paragraph = paragraph_match.group(1)
            parent_paragraph = paragraph_match.group(2)
            point = None
        elif line.startswith("- "):
            flush(number - 1)
            point_match = re.search(r"\(([a-z]|\d+)\)", line, re.I)
            block_point = point_match.group(1) if point_match else None
        if block_start is None:
            block_start = number
        buffer.append(line)
    flush(len(lines))
    return units


def internal_refs(text: str) -> list[str]:
    refs = []
    for match in re.finditer(r"\bArticle\s+\d+(?:\(\d+\))?", text, re.I):
        ref = re.sub(r"\s+", " ", match.group(0))
        if ref not in refs:
            refs.append(ref)
    return refs


def load_lexical_patterns() -> list[tuple[str, str, re.Pattern[str]]]:
    strings = yaml.safe_load((METHODOLOGY / "strings.yaml").read_text(encoding="utf-8"))
    patterns = []
    for family in ("mechanisms", "generic_regulatory_families"):
        for category, data in strings[family].items():
            for index, pattern in enumerate(data["patterns"], start=1):
                patterns.append((f"{family}:{category}", f"{category}[{index}]", re.compile(pattern, re.I)))
    return patterns


def make_location(unit: dict) -> dict:
    return {
        "celex": CELEX,
        "article": unit["article"],
        "paragraph": unit["paragraph"],
        "point": unit["point"],
        "subparagraph": None,
        "recital": unit["recital"],
        "line_start": unit["line_start"],
        "line_end": unit["line_end"],
        "hierarchy": unit["parent_context"]["hierarchy"],
    }


def reconstruct_candidates(units: list[dict]) -> list[dict]:
    patterns = load_lexical_patterns()
    candidates = []
    for unit in units:
        text = unit["focal_excerpt"]
        lexical_hits = []
        for family, string_id, pattern in patterns:
            matches = [m.group(0) for m in pattern.finditer(text)]
            lexical_hits.extend({"family": family, "string_id": string_id, "match": m} for m in matches)
        actor_mentions = [label for label in ACTOR_PATTERNS if re.search(r"\b" + re.escape(label) + r"\b", text, re.I)]
        action_mentions = [pattern for pattern in ACTION_PATTERNS if re.search(pattern, text, re.I)]
        object_mentions = [pattern for pattern in OBJECT_PATTERNS if re.search(pattern, text, re.I)]
        refs = internal_refs(text)
        structural_basis = []
        if actor_mentions:
            structural_basis.append("actor_mentions")
        if action_mentions:
            structural_basis.append("action_mentions")
        if object_mentions:
            structural_basis.append("object_mentions")
        if refs:
            structural_basis.append("same_act_cross_references")
        # This is a reconstruction screen, not a substantive R-I-T decision.
        structural_hit = bool(actor_mentions and action_mentions and (object_mentions or refs))
        if not lexical_hits and not structural_hit:
            continue
        origin = "both" if lexical_hits and structural_hit else "lexical" if lexical_hits else "structural"
        fingerprint = f"{unit['line_start']}|{unit['line_end']}|{unit['focal_excerpt']}".encode("utf-8")
        candidate_id = "CAND2-" + hashlib.sha256(fingerprint).hexdigest()[:12].upper()
        group_basis = f"A{unit['article']}" if unit["article"] else f"R{unit['recital']}"
        if unit["paragraph"]:
            group_basis += f"-P{unit['paragraph']}"
        candidates.append(
            {
                "candidate_id": candidate_id,
                "candidate_origin": origin,
                "reconstruction_group_id": "GROUP2-" + hashlib.sha256(group_basis.encode("utf-8")).hexdigest()[:10].upper(),
                "source_location": make_location(unit),
                "focal_excerpt": unit["focal_excerpt"],
                "parent_context": unit["parent_context"],
                "same_act_context_refs": refs,
                "lexical_hits": lexical_hits,
                "structural_reconstruction_basis": structural_basis,
                "substantive_coding_status": "pending_independent_R1_R2_reconstruction",
            }
        )
    candidates.sort(key=lambda item: (item["source_location"]["line_start"], item["source_location"]["line_end"]))
    return candidates


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    if not CORPUS.exists() or not (METHODOLOGY / "reference_coding_schema.json").exists():
        raise RuntimeError("Canonical corpus or reference methodology is missing")
    candidates = reconstruct_candidates(parse_document(CORPUS.read_text(encoding="utf-8")))
    skeleton_fields = [
        "candidate_id",
        "candidate_origin",
        "source_location",
        "focal_excerpt",
        "parent_context",
        "same_act_context_refs",
    ]
    skeletons = [{field: candidate[field] for field in skeleton_fields} for candidate in candidates]
    (OUT / "candidate_reconstruction.json").write_text(json.dumps(candidates, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUT / "R1_coding_input.json").write_text(json.dumps(skeletons, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUT / "R2_coding_input.json").write_text(json.dumps(skeletons, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    csv_rows = []
    for candidate in candidates:
        csv_rows.append(
            {
                "candidate_id": candidate["candidate_id"],
                "candidate_origin": candidate["candidate_origin"],
                "reconstruction_group_id": candidate["reconstruction_group_id"],
                "source_location": json.dumps(candidate["source_location"], ensure_ascii=False),
                "focal_excerpt": candidate["focal_excerpt"],
                "parent_context": json.dumps(candidate["parent_context"], ensure_ascii=False),
                "same_act_context_refs": "; ".join(candidate["same_act_context_refs"]),
                "lexical_hits": "; ".join(f"{x['string_id']}={x['match']}" for x in candidate["lexical_hits"]),
                "structural_reconstruction_basis": "; ".join(candidate["structural_reconstruction_basis"]),
            }
        )
    write_csv(OUT / "candidate_reconstruction.csv", csv_rows, list(csv_rows[0].keys()) if csv_rows else ["candidate_id"])
    print(json.dumps({"candidate_count": len(candidates), "origin_counts": {origin: sum(x["candidate_origin"] == origin for x in candidates) for origin in ("lexical", "structural", "both")}}, ensure_ascii=False))


if __name__ == "__main__":
    main()
