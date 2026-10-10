from __future__ import annotations

import csv
import hashlib
import json
import shutil
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = Path(r"C:\Users\Adm\Downloads\HUMAN_ADJUDICATION_RESPONSES_FILLED.csv")
FINAL_GATE = "ONTOLOGY_STABLE_WITH_REVISIONS"


def read_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    if not INPUT.exists():
        raise SystemExit(f"Missing authoritative human input: {INPUT}")

    manifest_path = ROOT / "99_REPRODUCIBILITY" / "PILOT_03_MANIFEST.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("status") != "PILOT_03_AWAITING_HUMAN_ADJUDICATION":
        raise SystemExit("Pre-adjudication manifest is not frozen at the required gate.")

    rows = read_csv(INPUT)
    expected = [f"H_{i:03d}" for i in range(1, 20)]
    ids = [r.get("decision_id", "") for r in rows]
    required = ["decision_id", "candidate_id", "case_id", "provision_id", "issue_type", "option_1", "option_2", "human_decision", "corrected_value", "rationale", "affected_ontology_rule", "backward_impact_flag", "provenance", "status"]
    missing_columns = [x for x in required if x not in (rows[0] if rows else {})]
    errors = []
    if len(rows) != 19:
        errors.append(f"expected 19 rows, found {len(rows)}")
    if ids != expected:
        errors.append(f"decision IDs must be exactly H_001..H_019 in order; found {ids}")
    if len(set(ids)) != len(ids):
        errors.append("duplicate decision IDs")
    if missing_columns:
        errors.append(f"missing columns: {missing_columns}")
    for r in rows:
        for key in ["human_decision", "rationale", "affected_ontology_rule"]:
            if not r.get(key, "").strip():
                errors.append(f"{r.get('decision_id')}: missing {key}")
        if r.get("provenance") != "HUMAN_ADJUDICATED":
            errors.append(f"{r.get('decision_id')}: provenance is not HUMAN_ADJUDICATED")
        if r.get("status") != "ADJUDICATED":
            errors.append(f"{r.get('decision_id')}: status is not ADJUDICATED")
    if errors:
        raise SystemExit("Human input validation failed:\n- " + "\n- ".join(errors))

    # Preserve the authoritative input as a new adjudication-layer artifact.
    filled_copy = ROOT / "07_HUMAN_ADJUDICATION" / "HUMAN_ADJUDICATION_RESPONSES_FILLED.csv"
    shutil.copy2(INPUT, filled_copy)

    log_fields = ["decision_id", "candidate_id", "case_id", "provision_id", "issue_type", "issue_field", "option_1", "option_2", "human_decision", "corrected_value", "rationale", "affected_ontology_rule", "backward_impact_flag", "provenance", "status"]
    log_rows = [{**r, "issue_field": r["issue_type"]} for r in rows]
    write_csv(ROOT / "07_HUMAN_ADJUDICATION" / "HUMAN_DECISION_LOG.csv", log_rows, log_fields)

    backward = {
        "H_006": ("PILOT_01", "P01_C01 / P01_PR01", "wrong recipient and direction", "Member State→other Member States/Commission: notify bodies; designation requires separate support.", "relational"),
        "H_007": ("PILOT_01", "P01_C02 / P01_PR01", "legal effect recast as actor edge", "Exemption effect retained separately; no Member State→manufacturer enable-use edge.", "relational"),
        "H_008": ("PILOT_01", "P01_C02 / P01_PR01", "action normalization error", "Action remains not applicable until the edge is reconstructed.", "functional"),
        "H_009": ("PILOT_02", "P02_C03 / P02_PR03", "intermediary over-attribution", "Insurance condition does not establish direct intermediary status.", "intermediary-status"),
        "H_010": ("PILOT_02", "P02_C03 / P02_PR03", "intermediary over-attribution", "Insurance condition does not establish derived R–I–T.", "intermediary-status"),
        "H_011": ("PILOT_02", "P03_C02 / P03_PR02", "wrong recipient and direction", "Inform is directed to the Commission; laboratory designation requires separate support.", "relational"),
        "H_012": ("PILOT_02", "P03_C03 / P03_PR03", "function boundary", "Assurance is distinct from later continuing surveillance.", "functional"),
        "H_013": ("PILOT_02", "P03_C03 / P03_PR03", "mechanism boundary", "Quality-system assessment is distinct from periodic audit/surveillance.", "mechanism-related"),
        "H_014": ("PILOT_02", "P03_C03 / P03_PR03", "device boundary", "Device follows the point 3.3 assessment procedure, while audit-like elements remain caveated.", "device-related"),
        "H_015": ("PILOT_02", "P04_C01 / P04_PR01", "composite edge", "Registry→auditor appoint; auditor→Registry audit; auditor→Commission report.", "relational"),
        "H_016": ("PILOT_02", "P04_C03 / P04_PR03", "candidate options misspecified", "Applicant→validation agent submit documentary evidence remains a direct edge.", "relational"),
        "H_017": ("PILOT_02", "P04_C06 / P04_PR06", "composite edge", "Selection, complaint submission, and provider→Registry information are separate edges.", "relational"),
        "H_018": ("PILOT_02", "P05_C01 / P05_PR01", "conditional intermediary over-attribution", "Exemption condition does not establish status for the candidate organization line.", "intermediary-status"),
        "H_019": ("PILOT_02", "P05_C01 / P05_PR01", "conditional intermediary over-attribution", "Safeguard enumeration does not document qualifying derived edges.", "intermediary-status"),
    }
    by_id = {r["decision_id"]: r for r in rows}
    backward_rows = []
    for decision_id, (pilot, earlier, impact, interpretation, kind) in backward.items():
        r = by_id[decision_id]
        backward_rows.append({"decision_id": decision_id, "earlier_pilot": pilot, "earlier_record_or_claim_affected": earlier, "type_of_impact": impact, "new_human_adjudicated_interpretation": interpretation, "impact_domain": kind, "backward_impact_flag": r["backward_impact_flag"], "historical_outputs_modified": "NO"})
    write_csv(ROOT / "07_HUMAN_ADJUDICATION" / "BACKWARD_IMPACT_REGISTER.csv", backward_rows, ["decision_id", "earlier_pilot", "earlier_record_or_claim_affected", "type_of_impact", "new_human_adjudicated_interpretation", "impact_domain", "backward_impact_flag", "historical_outputs_modified"])

    write_text(ROOT / "01_PROTOCOL" / "CODING_RULES_V0_3_ADJUDICATED.md", """# CODING_RULES_V0_3_ADJUDICATED

These rules incorporate H_001–H_019. The pre-adjudication rules and outputs remain preserved.

1. **Action-recipient matching.** `ACTOR_A + ACTION_VERBATIM + OBJECT + ACTOR_B` must match the legal text. A qualifier such as `designated` does not make the qualified actor the recipient of `inform` (H_006, H_011).
2. **One primitive edge per legally distinct directional action.** A change in actor, recipient, direction, legally expressed action, or legally relevant object normally creates a new edge (H_001, H_005, H_015, H_017).
3. **Composite provisions.** Use `COMPOSITE_CANDIDATE` when valid legal moves were compressed; decompose into elementary edges without treating the provision as uncertain (H_001, H_005, H_015, H_017).
4. **Legal effects.** Exemptions, eligibility and conditional authorization are recorded as `LEGAL_EFFECT` unless the text supports an actor-to-actor action. Do not create `enable`, `allow` or `grant` edges from legal effects alone (H_007).
5. **Modality.** Preserve `shall`, `may`, conditional triggers and optional Member-State implementation. A legally possible position is not an effectively instantiated relationship (H_002, H_004).
6. **Action normalization.** Normalize only after Actor A and Actor B are correct. If the candidate edge is invalid, use `NOT_APPLICABLE_TO_CANDIDATE_EDGE` or leave normalization unresolved (H_008).
7. **Intermediary status.** It is a relational position, never a permanent actor attribute. Insurance or required support services, co-occurrence, and conditional safeguards alone do not establish direct or derived status (H_002, H_004, H_009, H_010, H_018, H_019).
8. **Evidence versus candidate construction.** `UNRESOLVED` means the specific candidate lacks sufficient support; it does not mean the whole act is uncertain. `NEITHER` preserves a corrected value when both options are wrong (H_006–H_011, H_016).
9. **Function × Mechanism × Device.** For the tested Annex III point 3.3 provision, use `assurance`, `quality_system_assessment`, and `quality-system assessment`. Do not generalize this label to all conformity provisions; distinguish it from later periodic surveillance (H_012–H_014).
10. **Outcome vocabulary.** Preserve `UNRESOLVED`, `COMPOSITE_CANDIDATE`, `BOTH_IN_PART`, and `NEITHER`; none may be silently forced into a binary agreement result (H_001, H_008, H_015, H_016, H_017).
""")

    write_text(ROOT / "08_RESULTS" / "RELATIONAL_MODEL_V0_3.md", """# RELATIONAL_MODEL_V0_3

## Status

Adjudicated model. Gate: `ONTOLOGY_STABLE_WITH_REVISIONS`. This is a measurement architecture for extended methodological validation, not a production codebook or dataset migration authorization.

## Observed / source-anchored

- act and addressable provision;
- legally expressed Actor A and Actor B;
- `ACTION_VERBATIM`;
- direct object;
- legal direction;
- modality, including mandatory, permissive, conditional and optional implementation;
- official evidence excerpt and source provenance.

The primitive record is `ACT × PROVISION × ACTOR_A × ACTION × OBJECT × ACTOR_B`. A provision may generate multiple primitive edges. A primitive edge must not combine legally distinct actor, recipient, direction, action or object changes.

## Coded

- `ACTION_NORMALIZED`, only after actor-recipient alignment;
- function;
- mechanism;
- device/instrument;
- relationship-family classification where defensible;
- `LEGAL_EFFECT`, separately from `BINARY_RELATIONSHIP`.

`UNRESOLVED` is candidate-level evidentiary insufficiency. `COMPOSITE_CANDIDATE` identifies compressed but legally valid moves. `NEITHER` preserves a human correction when both candidate alternatives are wrong.

## Derived

- intermediary position;
- R–I–T configuration;
- higher-order strategy;
- architecture;
- governance logic.

Intermediary status requires documented qualifying relations and preserves modality; it is not inferred from institutional identity, ordinary support services, co-occurrence, or a conditional safeguard alone. R–I–T remains a composition of elementary edges and never replaces their evidence. Primitive `ACTOR_I` is not stored.

## Relationship type decision

Direct relationship type remains an audit/descriptive field tied to the candidate edge. Derived relationship families are preferred for higher-order analytical classification because several pre-adjudication disagreements were edge-decomposition or candidate-construction errors rather than evidence that the law lacked a relation. The direct field is retained for traceability.

## Experimental fields

Relationship-family derivation, conditional intermediary status, R–I–T composition, legal-effect representation, and higher-order strategy/architecture/governance fields remain experimental and require extended validation.
""")

    decision_types = Counter(r["human_decision"] for r in rows)
    corrected_unresolved = sum(r["corrected_value"].startswith("UNRESOLVED") for r in rows)
    backward_count = sum(r["backward_impact_flag"] == "YES" for r in rows)
    write_text(ROOT / "08_RESULTS" / "HUMAN_ADJUDICATION_ANALYSIS.md", f"""# HUMAN_ADJUDICATION_ANALYSIS

## Validation

- Total adjudicated items: **{len(rows)}**.
- Decision IDs: H_001–H_019, unique and complete.
- Status: 19/19 `ADJUDICATED`.
- Provenance: 19/19 `HUMAN_ADJUDICATED`.
- Rationale: 19/19 present.
- Backward impact: **{backward_count}** items.

## Decision distribution

| raw human_decision | n |
| --- | ---: |
| `OPTION_1` | {decision_types.get('OPTION_1', 0)} |
| `OPTION_2` | {decision_types.get('OPTION_2', 0)} |
| `BOTH_IN_PART` | {decision_types.get('BOTH_IN_PART', 0)} |
| `NEITHER` | {decision_types.get('NEITHER', 0)} |
| qualified/custom human decision | {sum(v for k, v in decision_types.items() if k not in {'OPTION_1','OPTION_2','BOTH_IN_PART','NEITHER'})} |

Substantive corrected outcomes with `UNRESOLVED` are **{corrected_unresolved}**. They concern the candidate field/edge, not uncertainty about the whole legal act.

## Cause classification

| primary cause | decision IDs | n |
| --- | --- | ---: |
| `COMPOSITE_EDGE` | H_001, H_005, H_015, H_017 | 4 |
| `WRONG_RECIPIENT_OR_DIRECTION` | H_006, H_011 | 2 |
| `CANDIDATE_OPTIONS_MISSPECIFIED` | H_007, H_016 | 2 |
| `ACTION_NORMALIZATION_ERROR` | H_008 | 1 |
| `INTERMEDIARY_STATUS_OVERATTRIBUTION` | H_009, H_010, H_018, H_019 | 4 |
| `FUNCTION_MECHANISM_BOUNDARY` | H_003, H_012, H_013, H_014 | 4 |
| `MODALITY_OR_CONDITIONALITY` | H_002, H_004 | 2 |

The 19 items therefore do not represent 19 equivalent coder disagreements. Nine are primarily edge construction, recipient/direction or candidate-option problems; four are intermediary-status over-attribution; four refine Function × Mechanism × Device boundaries; and two refine modality/conditional instantiation. Six items (H_002–H_004 and H_012–H_014) are the main ontology-rule refinement set.

## Model reassessment

1. The binary primitive becomes more defensible: adjudication repeatedly required separating actor, recipient, direction and action rather than abandoning the edge model.
2. Nine disagreements would disappear or materially change after action-recipient alignment and elementary-edge decomposition.
3. Derived relationship families are preferable for higher-order classification, while `RELATIONSHIP_TYPE_DIRECT` should remain as an audit/descriptive field.
4. Stable enough for extended validation: act/provision anchoring, Actor A/B, verbatim action, object, direction, modality, and evidence provenance.
5. Requires further calibration within the extended validation: legal-effect representation, conditional intermediary positions, R–I–T composition, relationship-family derivation, and higher-order strategy/architecture fields.

## Reliability boundary

The pre-adjudication model-model comparison remains descriptive. The completed stage is one human adjudication layer applied to disagreements from two independent model passes. It is **not human intercoder reliability**.
""")

    write_text(ROOT / "08_RESULTS" / "PILOT_03_FINAL_REPORT.md", f"""# PILOT_03_FINAL_REPORT

## Final gate

`{FINAL_GATE}`

## Basis for the gate

The human adjudication confirms the binary A→B provision-anchored primitive, but requires revisions before extended validation: one primitive edge per legally distinct directional action, explicit action-recipient matching, separation of legal effects from actor edges, modality-sensitive intermediary status, and decomposition of composite provisions. Function, mechanism and device remain distinct, with a tested Annex III boundary rule. R–I–T remains derived and `ACTOR_I` remains non-primitive.

The gate is not `ONTOLOGY_STABLE_FOR_EXTENDED_VALIDATION` yet because the revised decomposition and conditional-status rules have not themselves been tested on a fresh extended sample. It is also not a failure gate: the adjudication supports a coherent revised ontology with bounded experimental fields.

## Inputs and preservation

- Authoritative input: `07_HUMAN_ADJUDICATION/HUMAN_ADJUDICATION_RESPONSES_FILLED.csv`.
- 19/19 decisions validated and incorporated.
- Original blank response template, Model A, Model B, source provisions, comparison, preregistered RIT rules and pre-adjudication manifest preserved.
- PILOT_01, PILOT_02, production data, Rotem Medzini's codebook and original sources unchanged.
- Historical gate preserved: `PILOT_03_AWAITING_HUMAN_ADJUDICATION`.

## Interpretation boundary

Model-model replication, human adjudication, and human intercoder reliability are distinct. This pilot has two independent model passes and one human adjudication layer; it does not establish human intercoder reliability. The result concerns measurement architecture only, not implementation, effectiveness, causal effects or regulatory performance.

## Next step

Run an extended validation sample using the adjudicated rules, especially edge decomposition, legal effects, modality, conditional intermediary status and derived relationship families. Do not migrate the production dataset.
""")

    final_manifest = dict(manifest)
    final_manifest.update({
        "status": FINAL_GATE,
        "human_adjudication_completed": True,
        "production_authorized": False,
        "human_adjudication_input_filename": INPUT.name,
        "human_adjudication_input_sha256": digest(INPUT),
        "incorporated_at_utc": datetime.now(timezone.utc).isoformat(),
        "adjudicated_items": 19,
        "backward_impact_items": backward_count,
        "final_gate": FINAL_GATE,
        "pre_adjudication_gate_preserved": "PILOT_03_AWAITING_HUMAN_ADJUDICATION",
        "pre_adjudication_manifest_sha256": digest(manifest_path),
        "final_outputs": [
            "07_HUMAN_ADJUDICATION/HUMAN_ADJUDICATION_RESPONSES_FILLED.csv",
            "07_HUMAN_ADJUDICATION/HUMAN_DECISION_LOG.csv",
            "07_HUMAN_ADJUDICATION/BACKWARD_IMPACT_REGISTER.csv",
            "01_PROTOCOL/CODING_RULES_V0_3_ADJUDICATED.md",
            "08_RESULTS/RELATIONAL_MODEL_V0_3.md",
            "08_RESULTS/HUMAN_ADJUDICATION_ANALYSIS.md",
            "08_RESULTS/PILOT_03_FINAL_REPORT.md",
            "99_REPRODUCIBILITY/PILOT_03_MANIFEST_FINAL.json",
        ],
    })
    write_text(ROOT / "99_REPRODUCIBILITY" / "PILOT_03_MANIFEST_FINAL.json", json.dumps(final_manifest, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
