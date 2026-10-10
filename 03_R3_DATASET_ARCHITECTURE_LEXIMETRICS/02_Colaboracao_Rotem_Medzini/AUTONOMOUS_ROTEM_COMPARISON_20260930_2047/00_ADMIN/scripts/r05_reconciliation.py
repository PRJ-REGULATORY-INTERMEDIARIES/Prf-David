"""R05 — Per-decision reconciliation of PILOT_03 (template -> filled -> log -> backward impact -> comparison cell -> excerpt check)."""
import csv, sys, collections
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from common import RUN_ROOT, PROJECT_ROOT, read_csv, write_csv  # noqa: E402

B = RUN_ROOT / "01_BASELINES"
pre = {r["decision_id"]: r for r in read_csv(B / "BASELINE_REL_PILOT03_PRE_ADJUDICATION_TEMPLATE.csv")}
fil = {r["decision_id"]: r for r in read_csv(B / "BASELINE_REL_PILOT03_HUMAN_RESPONSES_FILLED.csv")}
log = {r["decision_id"]: r for r in read_csv(B / "BASELINE_REL_PILOT03_HUMAN_DECISION_LOG.csv")}
bir = {r["decision_id"]: r for r in read_csv(B / "BASELINE_REL_PILOT03_BACKWARD_IMPACT_REGISTER.csv")}
cmpc = read_csv(PROJECT_ROOT / "RELATIONAL_LEXIMETRICS_PILOT/PILOT_03/04_COMPARISON/CODER_COMPARISON.csv")
dis = {(r["candidate_id"], r["field"]) for r in cmpc if r["agreement"] == "DISAGREE"}
exc = {r["PROVISION_ID"]: r["FRESH_VERIFICATION"] for r in read_csv(RUN_ROOT / "05_PILOT03/PILOT03_EXCERPT_VERIFICATION.csv")}
common = ["decision_id", "candidate_id", "case_id", "provision_id", "issue_type", "option_1", "option_2", "human_decision", "corrected_value", "rationale", "affected_ontology_rule", "backward_impact_flag", "provenance", "status"]
rows = []
for d in sorted(set(pre) | set(fil) | set(log)):
    p, f, l = pre.get(d, {}), fil.get(d, {}), log.get(d, {})
    same = all(f.get(k, "") == l.get(k, "") for k in common)
    field = l.get("issue_field") or l.get("issue_type")
    rows.append(dict(
        DECISION_ID=d, CANDIDATE_ID=l.get("candidate_id"), PROVISION_ID=l.get("provision_id"), ISSUE_FIELD=field,
        PRE_STATUS=p.get("status"), PRE_PROVENANCE=p.get("provenance"), PRE_HUMAN_DECISION_EMPTY="YES" if not p.get("human_decision") else "NO",
        POST_STATUS=l.get("status"), POST_PROVENANCE=l.get("provenance"), HUMAN_DECISION=l.get("human_decision"),
        RATIONALE_PRESENT="YES" if l.get("rationale", "").strip() else "NO", FILLED_EQUALS_LOG=("YES" if same else "NO"),
        BACKWARD_FLAG=l.get("backward_impact_flag"), IN_BACKWARD_REGISTER="YES" if d in bir else "NO",
        EARLIER_PILOT_AFFECTED=bir.get(d, {}).get("earlier_pilot", ""), HISTORICAL_OUTPUTS_MODIFIED=bir.get(d, {}).get("historical_outputs_modified", ""),
        MAPS_TO_DISAGREE_CELL="YES" if (l.get("candidate_id"), field) in dis else "NO",
        PROVISION_EXCERPT_FRESH_CHECK=exc.get(l.get("provision_id"), ""),
        RECLASSIFIED_BY_THIS_RUN="NO"))
write_csv(RUN_ROOT / "05_PILOT03/PILOT03_RECONCILIATION.csv", list(rows[0].keys()), rows)
C = collections.Counter
print("n", len(rows), "unique", len({r["DECISION_ID"] for r in rows}))
for k in ["PRE_STATUS", "POST_STATUS", "POST_PROVENANCE", "HUMAN_DECISION", "RATIONALE_PRESENT", "FILLED_EQUALS_LOG", "BACKWARD_FLAG", "IN_BACKWARD_REGISTER", "EARLIER_PILOT_AFFECTED", "MAPS_TO_DISAGREE_CELL", "PROVISION_EXCERPT_FRESH_CHECK", "HISTORICAL_OUTPUTS_MODIFIED"]:
    print(k, dict(C(r[k] for r in rows)))
print("flag YES == in register:", all((r["BACKWARD_FLAG"] == "YES") == (r["IN_BACKWARD_REGISTER"] == "YES") for r in rows))
print("UNRESOLVED corrected values:", sum(1 for d in log.values() if d["corrected_value"].strip() == "UNRESOLVED"))
