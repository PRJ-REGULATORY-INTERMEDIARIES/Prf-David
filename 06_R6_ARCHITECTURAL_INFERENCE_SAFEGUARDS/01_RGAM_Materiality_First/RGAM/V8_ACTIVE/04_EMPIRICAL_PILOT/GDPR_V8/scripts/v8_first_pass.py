"""Generate a transparent V8-oriented machine-first screening register.

The script makes no architectural classification. Its lexical labels are candidate
coding prompts, retained separately from the curated legal observations.
"""
from pathlib import Path
import csv, json, re

PILOT = Path(__file__).resolve().parents[1]
SOURCE = PILOT / "01_SOURCES" / "working_text.json"
COVERAGE = PILOT / "02_EXTRACTION" / "COVERAGE_REGISTER.csv"
STATEMENTS = PILOT / "02_EXTRACTION" / "MACHINE_CANDIDATE_STATEMENTS.csv"

data = json.loads(SOURCE.read_text(encoding="utf-8"))
actor_words = ("controller", "processor", "supervisory authority", "board", "commission", "data subject", "court", "officer", "member state", "certification body", "monitoring body")
governance_words = ("shall", "may", "must", "competent", "authority", "decision", "approve", "accredit", "certif", "monitor", "supervis", "review", "enforce", "sanction", "report", "inform", "cooperat", "consult", "audit", "complaint", "remedy")

def tags(text):
    lower = text.lower()
    found = []
    for label, terms in {
        "function_candidate": ("monitor", "supervis", "verify", "certif", "enforc", "review", "cooperat", "decid", "inform", "implement"),
        "mechanism_candidate": ("authoris", "approval", "accredit", "sanction", "fine", "complaint", "consult", "report"),
        "instrument_candidate": ("code of conduct", "certification", "register", "binding corporate rules", "decision", "complaint"),
        "relationship_candidate": ("to the", "with the", "between", "by the", "on the basis of"),
        "attribute_candidate": ("binding", "independent", "discretion", "accountab", "reasoned objection", "shall be competent"),
    }.items():
        if any(x in lower for x in terms):
            found.append(label)
    return ";".join(found)

coverage_rows, statement_rows = [], []
for article in data["articles"]:
    for para in article["paragraphs"]:
        base = f"GDPR.A{article['article']}.P{para['para_label']}"
        full = (para["lead"] + " " + " ".join(f"{x} {y}" for x, y in para["points"])).strip()
        relevant = any(x in full.lower() for x in governance_words)
        coverage_rows.append({
            "unit_id": base, "documentary_location": f"Article {article['article']}({para['para_label']})",
            "kind": "paragraph", "screening_status": "candidate_governance_relevant" if relevant else "no_machine_candidate",
            "extraction_status": "machine_first_pass_complete", "candidate_categories": tags(full),
            "uncertainty": "lexical screen only; no legal conclusion", "reason": "modal/institutional lexicon" if relevant else "no selected lexicon match",
        })
        if relevant:
            statement_rows.append({"statement_id": f"MS-{len(statement_rows)+1:04d}", "unit_id": base, "text": full,
                                   "status": "machine_candidate", "candidate_categories": tags(full),
                                   "note": "Requires human legal interpretation; not an architectural inference."})
        for point, body in para["points"]:
            point_id = f"{base}.pt{point.strip('()') or 'x'}"
            point_rel = any(x in body.lower() for x in governance_words)
            coverage_rows.append({
                "unit_id": point_id, "documentary_location": f"Article {article['article']}({para['para_label']}){point}",
                "kind": "point", "screening_status": "candidate_governance_relevant" if point_rel else "no_machine_candidate",
                "extraction_status": "machine_first_pass_complete", "candidate_categories": tags(body),
                "uncertainty": "lexical screen only; point remains linked to its paragraph", "reason": "modal/institutional lexicon" if point_rel else "no selected lexicon match",
            })
            if point_rel:
                statement_rows.append({"statement_id": f"MS-{len(statement_rows)+1:04d}", "unit_id": point_id, "text": body,
                                       "status": "machine_candidate", "candidate_categories": tags(body),
                                       "note": "Requires human legal interpretation; not an architectural inference."})

for path, rows in ((COVERAGE, coverage_rows), (STATEMENTS, statement_rows)):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)

print(f"articles={len(data['articles'])} paragraphs={sum(r['kind']=='paragraph' for r in coverage_rows)} points={sum(r['kind']=='point' for r in coverage_rows)} candidates={len(statement_rows)}")
