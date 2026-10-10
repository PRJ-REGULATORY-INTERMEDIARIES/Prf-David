import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMMON_PATH = ROOT / "scripts" / "experimental" / "_common.py"
SPEC = importlib.util.spec_from_file_location("experimental_common", COMMON_PATH)
common = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(common)

VALIDATOR_PATH = ROOT / "scripts" / "experimental" / "validate_experimental_output.py"
sys.path.insert(0, str(COMMON_PATH.parent))
VALIDATOR_SPEC = importlib.util.spec_from_file_location("experimental_validator", VALIDATOR_PATH)
validator = importlib.util.module_from_spec(VALIDATOR_SPEC)
assert VALIDATOR_SPEC.loader is not None
VALIDATOR_SPEC.loader.exec_module(validator)
sys.path.pop(0)


class ExperimentalPipelineTests(unittest.TestCase):
    def setUp(self):
        self.reference = json.loads((ROOT / "tests/fixtures/reference_mock.json").read_text())
        self.experimental = json.loads((ROOT / "tests/fixtures/experimental_mock.json").read_text())
        self.schema = json.loads((ROOT / "methodology/v1.1.2/experimental_output_schema.json").read_text())

    def test_v1_1_2_actor_arrays_validate_zero_one_and_multiple(self):
        self.assertEqual(validator.validate_record(self.experimental[0], self.schema), [])
        self.assertEqual(self.experimental[0]["R"], ["Authority A"])
        self.assertEqual(self.experimental[1]["R"], ["Authority Z", "Authority Y"])
        self.assertEqual(self.experimental[1]["I"], ["Unknown Y", "Unknown X"])
        self.assertEqual(self.experimental[1]["T"], ["Operator Q", "Operator R"])
        self.assertEqual(self.experimental[2]["R"], [])
        self.assertEqual(self.experimental[2]["I"], [])
        self.assertEqual(self.experimental[2]["T"], [])
        for record in self.experimental:
            self.assertEqual(validator.validate_record(record, self.schema), [])

    def test_v1_1_2_rejects_scalar_actor_fields(self):
        for field in ("R", "I", "T"):
            invalid = dict(self.experimental[0], **{field: "Actor A"})
            errors = validator.validate_record(invalid, self.schema)
            self.assertIn(f"type:record.{field}:string", errors)

    def test_actor_normalization_is_independent_of_order(self):
        reference = {
            "source_location": {"article": "9", "paragraph": "1", "point": None, "subparagraph": None, "recital": None},
            "relational_result": "positive",
            "R": [{"label": "Authority A"}, {"label": "Authority B"}],
            "I": [{"label": "Verifier A"}, {"label": "Verifier B"}],
            "T": [{"label": "Operator A"}, {"label": "Operator B"}],
            "primary_mechanism": "verification",
        }
        experimental = {
            "relation_id": "RUN-ORDER",
            "location": {"article": "9", "paragraph": "1", "point": None, "subparagraph": None, "recital": None},
            "R": ["Authority B", "Authority A"],
            "I": ["Verifier B", "Verifier A"],
            "T": ["Operator B", "Operator A"],
            "mechanism": "verification",
            "decision": "intermediated",
        }
        comparison = common.compare_fields(reference, experimental)
        self.assertTrue(comparison["R_agreement"])
        self.assertTrue(comparison["I_agreement"])
        self.assertTrue(comparison["T_agreement"])

    def test_tp_fp_fn_precision_recall_f1(self):
        experimental = [self.experimental[0], self.experimental[1]]
        reference = [dict(item, candidate_id=None) for item in self.reference]
        metrics = common.classification_metrics(reference, experimental)
        self.assertEqual(metrics["TP"], 1)
        self.assertEqual(metrics["FP"], 1)
        self.assertEqual(metrics["FN"], 1)
        self.assertEqual(metrics["precision"], 0.5)
        self.assertEqual(metrics["recall"], 0.5)
        self.assertEqual(metrics["F1"], 0.5)

    def test_normalized_location_matching_and_field_agreement(self):
        experimental = [dict(self.experimental[0], location={"article": " 1 ", "paragraph": "1", "point": None, "subparagraph": None, "recital": None})]
        reference = [dict(self.reference[0], candidate_id=None)]
        result = common.build_comparison(reference, experimental)
        self.assertEqual(result["metrics"]["TP"], 1)
        row = result["rows"][0]
        self.assertTrue(row["relational_result_agreement"])
        self.assertTrue(row["R_agreement"])
        self.assertTrue(row["I_agreement"])
        self.assertTrue(row["T_agreement"])
        self.assertTrue(row["mechanism_agreement"])

    def test_candidate_id_is_not_needed_for_experimental_matching(self):
        self.assertFalse(any("candidate_id" in item for item in self.experimental))
        self.assertEqual(common.derived_relational_result({"decision": "direct"}), "negative")

    def test_candidate_id_matching_for_posthoc_artifact(self):
        reference = [{"candidate_id": "POSTHOC-1", "relational_result": "positive"}]
        comparison_artifact = [{"candidate_id": "POSTHOC-1", "decision": "intermediated"}]
        self.assertEqual(common.classification_metrics(reference, comparison_artifact)["TP"], 1)

    def test_no_division_by_zero(self):
        metrics = common.classification_metrics([], [])
        self.assertEqual(metrics["precision"], 0.0)
        self.assertEqual(metrics["recall"], 0.0)
        self.assertEqual(metrics["F1"], 0.0)

    def test_error_categories(self):
        comparison = common.build_comparison(self.reference, self.experimental)
        categories = {row["category"] for row in common.error_taxonomy(comparison)}
        self.assertIn("omission", categories)
        self.assertIn("over-inclusion", categories)

    def test_reference_guard_fails_closed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "config").mkdir()
            (root / "config/project.yaml").write_text("project:\n  status: methodology_locked\nreference:\n  locked: false\n")
            (root / "config/experiment.yaml").write_text("experiment:\n  status: not_started\n")
            with self.assertRaisesRegex(RuntimeError, "REFERENCE_NOT_LOCKED"):
                common.assert_reference_locked(root)


if __name__ == "__main__":
    unittest.main()
