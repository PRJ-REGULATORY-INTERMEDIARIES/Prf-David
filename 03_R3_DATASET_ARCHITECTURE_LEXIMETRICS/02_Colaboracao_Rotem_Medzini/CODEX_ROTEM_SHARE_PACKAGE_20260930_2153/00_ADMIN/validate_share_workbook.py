"""Validate the share workbook and write a reproducible QA report."""
from __future__ import annotations

import csv
import hashlib
import re
from datetime import datetime
from pathlib import Path

from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parents[1]
RUN = ROOT / "AUTONOMOUS_ROTEM_COMPARISON_20260930_2047"
BOOK = OUT / "03_WORKBOOK/ROTEM_PILOT_RESULTS_SUMMARY.xlsx"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def sheet_rows(wb, name: str, header_row: int = 1) -> list[dict]:
    ws = wb[name]
    fields = [c.value for c in ws[header_row]]
    return [dict(zip(fields, (c.value for c in row))) for row in ws.iter_rows(min_row=header_row + 1)]


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip().casefold()


def main() -> None:
    checks: list[str] = []
    wb = load_workbook(BOOK, data_only=False)
    names = ["Overview", "Cases", "Provision_Events", "Rotem_Crosswalk", "Function_Mechanism",
             "Traceability", "Pilot03", "David_Architecture_Link", "Sources", "Limitations"]
    assert wb.sheetnames == names
    checks.append("PASS — ten required sheets appear in the requested order.")

    cases = sheet_rows(wb, "Cases")
    events = sheet_rows(wb, "Provision_Events")
    fm = sheet_rows(wb, "Function_Mechanism")
    trace = sheet_rows(wb, "Traceability")
    arch = sheet_rows(wb, "David_Architecture_Link")
    pilot = sheet_rows(wb, "Pilot03", 3)
    sources = sheet_rows(wb, "Sources")
    case_ids = {r["Case_ID"] for r in cases}
    source_ids = {r["Source_ID"] for r in sources}
    assert len(cases) == len(case_ids) == 5
    assert len(events) == 16
    for dataset in (events, fm, trace):
        assert all(r["Case_ID"] in case_ids for r in dataset)
    checks.append("PASS — all event, function and traceability Case_IDs resolve to the five Cases rows.")

    # Check every explicit Source_ID cell, source reference in notes and source token in Overview.
    referenced = set()
    for ws in wb:
        for row in ws:
            for cell in row:
                if isinstance(cell.value, str) and ws.title != "Sources":
                    referenced.update(re.findall(r"\bS\d{2}\b", cell.value))
    assert referenced <= source_ids, referenced - source_ids
    assert all(r["Source_ID"] for r in cases)
    assert all("Source_ID: S" in r["Notes"] for r in events)
    checks.append(f"PASS — all {len(referenced)} cited Source_IDs resolve to Sources.")

    legal = {
        "CASE_01": "32004R0874", "CASE_02": "31989L0336", "CASE_03": "31991L0263",
        "CASE_04": "31986L0361", "CASE_05": "32022R2065",
    }
    for r in events:
        celex = legal[r["Case_ID"]]
        text = (RUN / "01_BASELINES/official_texts" / f"{celex}.txt").read_text(encoding="utf-8")
        assert norm(r["Text_excerpt"]) in norm(text), r["Event_ID"]
        assert celex in r["Source_path_or_URL"]
        assert r["Coder_provenance"] == "CODEX_SYNTHESIS"
        assert "VERIFIED_OFFICIAL_TEXT" in r["Evidence_status"]
    event_map = {r["Event_ID"]: r for r in events}
    assert event_map["E01"]["Target_or_recipient_actor"] == "Validation agent"
    assert event_map["E12"]["Target_or_recipient_actor"] == "Approved laboratory"
    assert event_map["E13"]["Target_or_recipient_actor"] == "Member States"
    assert event_map["E04"]["Intermediary_actor"] == "No insurer action specified"
    # The R07 packs identify exact provision sections; these headings are independently checked.
    case_provision_keys = {
        "CASE_01": ["A13", "A14"], "CASE_02": ["A10(6)", "ANNEX_II"],
        "CASE_03": ["A10(1)", "ANNEX_III(3.3)", "ANNEX_III(3.4)", "ANNEX_III(4)"],
        "CASE_04": ["A2(8)", "A8(3)"], "CASE_05": ["A37(1)", "A37(3)", "A37(4)"],
    }
    for case, keys in case_provision_keys.items():
        pack = (RUN / "07_CASE_SELECTION/case_texts" / f"{case}_PROVISIONS.md").read_text(encoding="utf-8")
        for key in keys:
            assert f"## {legal[case]}:{key}" in pack, (case, key)
    checks.append("PASS — all 16 event excerpts occur in the corresponding official-text archive and all cited provision sections occur in the case packs.")

    assert len(pilot) == 19 == len({r["Decision_ID"] for r in pilot})
    assert sum(r["Retrospective_impact"] == "YES" for r in pilot) == 14
    assert all(r["Provenance"] == "HUMAN_ADJUDICATED" for r in pilot)
    original = list(csv.DictReader((ROOT / "RELATIONAL_LEXIMETRICS_PILOT/PILOT_03/07_HUMAN_ADJUDICATION/HUMAN_DECISION_LOG.csv").open(encoding="utf-8-sig", newline="")))
    assert [r["Decision_ID"] for r in pilot] == [r["decision_id"] for r in original]
    assert all(p["Human_rationale"] == o["rationale"] and p["Retrospective_impact"] == o["backward_impact_flag"]
               for p, o in zip(pilot, original))
    assert all("HUMAN_ADJUDICATED" not in str(r) for r in events)
    checks.append("PASS — 19 unique historical human-decision rows match the original log; 14 have retrospective impact; new events have CODEX_SYNTHESIS provenance.")

    assert "ONTOLOGY_STABLE_WITH_REVISIONS" in wb["Pilot03"]["A1"].value
    assert "not statistical validation" in wb["Pilot03"]["A1"].value
    checks.append("PASS — the visible Pilot03 note identifies the historical gate as a project judgment, not statistical validation.")

    forbidden = ["unsupported implied triples", "cartesian product", "false r–i–t", "false r-i-t",
                 "two-model validation", "our architecture is superior",
                 "rotem's codebook is inadequate"]
    all_text = " ".join(str(c.value).casefold() for ws in wb for row in ws for c in row if c.value)
    assert not any(term in all_text for term in forbidden), [term for term in forbidden if term in all_text]
    assert "not independent inter-model reliability evidence" in all_text  # visible methodological negation
    assert not wb._external_links
    assert all(c.data_type != "f" for ws in wb for row in ws for c in row)
    assert not any(x in all_text for x in ("#ref!", "#value!", "#n/a", "#div/0!"))
    checks.append("PASS — no Cartesian-error claim, formula, external workbook link or Excel error token; Pilot03 contains a visible provenance note.")

    for ws in wb:
        if ws.title != "Overview":
            assert ws.auto_filter.ref
            assert ws.freeze_panes
    conclusions = {"PARENT_SCHEMA_SUFFICIENT", "CLARIFICATION_USEFUL", "EVENT_LAYER_ADDS_TRACEABILITY", "OPEN_CONCEPTUAL_BOUNDARY"}
    assert {r["Conclusion"] for r in cases} <= conclusions
    cross = sheet_rows(wb, "Rotem_Crosswalk")
    actions = {"NO_CHANGE_RECOMMENDED", "CLARIFICATION_ONLY", "OPTIONAL_EXTENSION", "DISCUSS_WITH_ROTEM"}
    assert {r["Recommended_action"] for r in cross} <= actions
    assert len(arch) <= 10
    checks.append("PASS — filters, frozen headers, allowed conclusion/action vocabularies and concise architecture link.")

    # SHA-256 continuity for all registered outside sources and copied R08 files.
    for r in sources:
        p = Path(r["Path_or_URL"].split(" | ", 1)[0])
        assert p.exists() and digest(p) == r["SHA256"], r["Source_ID"]
    manifest = list(csv.DictReader((OUT / "01_RECOVERED_DATA/R08_RECOVERY_MANIFEST.csv").open(encoding="utf-8-sig", newline="")))
    assert len(manifest) == 29
    for r in manifest:
        p = RUN / "08_DUAL_CODING" / r["relative_path"]
        q = OUT / "01_RECOVERED_DATA/R08_AS_FOUND" / r["relative_path"]
        assert digest(p) == digest(q) == r["sha256"]
    checks.append("PASS — 21 registered external sources retain their recorded SHA-256 hashes; all 29 recovered R08 files match source byte-for-byte.")

    # Local timestamp audit complements the hash check; the package was created at 21:53.
    start = datetime(2026, 9, 30, 21, 53)
    touched_outside = [p for p in ROOT.rglob("*") if p.is_file() and not p.is_relative_to(OUT)
                       and datetime.fromtimestamp(p.stat().st_mtime) >= start]
    assert not touched_outside, touched_outside[:10]
    checks.append("PASS — no file outside this new package has a modification time at or after package creation (2026-09-30 21:53 local).")

    qa = OUT / "02_VALIDATION/WORKBOOK_QA.md"
    qa.write_text("# Workbook quality assurance\n\n" + "\n".join("- " + x for x in checks) +
                  "\n\n## Methodological scope\n\n"
                  "- The reported PILOT_03 gate `ONTOLOGY_STABLE_WITH_REVISIONS` is a historical project gate, hard-coded in the incorporation script, not independent statistical validation.\n"
                  "- The 19 rows carry the historical provenance value `HUMAN_ADJUDICATED`; no reviewer name is recorded in the source files.\n"
                  "- R08's Cartesian context calculation was excluded. Multivalued contexts do not assert every actor combination.\n"
                  "- The selected-case event fields are Codex interpretation checked against official text, not human adjudication or an independent second pass.\n"
                  "- The five cases are diagnostic and cannot support population estimates.\n",
                  encoding="utf-8")
    print("QA PASS", len(checks), "checks", qa)


if __name__ == "__main__":
    main()
