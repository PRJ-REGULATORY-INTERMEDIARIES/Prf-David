"""G1-PREP tests for defect 1 of the G0 diagnosis: insufficient vocabulary validation.

ALL DATA IN THIS FILE ARE SYNTHETIC TEST FIXTURES. They are written to a
temporary directory, never to data/, and are not research results.

Reference: gates/G0/BASELINE_RUN.md (probe P5) and SPEC-V in
gates/G0_1/G0_1_STRATEGIC_ALIGNMENT.md.
"""
import csv
import hashlib
import importlib.util
import io
import shutil
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('cli', ROOT / 'scripts' / 'cli.py')
cli = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cli)


class SyntheticWorld(unittest.TestCase):
    """Builds a small, fully valid set of tables in a temp dir and points cli at it."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix='g1prep_synthetic_'))
        self._data, self._root = cli.DATA, cli.ROOT
        cli.DATA = self.tmp / 'data'
        cli.ROOT = self.tmp
        with redirect_stdout(io.StringIO()):
            cli.init()
        # One valid record that went through both screening stages to inclusion,
        # and one canonical dataset built on it.
        self.add('discovery_records.csv', ['SYN_R1', 'seed', '', 'SYN01', 'Synthetic resource', 'https://example.org/a', '2026-01-01', 'synthetic fixture', ''])
        self.add('consensus.csv', ['SYN_R1', 'title_abstract', 'include', 'SYN_ADJ', '2026-01-02', '', ''])
        self.add('consensus.csv', ['SYN_R1', 'full_source', 'include', 'SYN_ADJ', '2026-01-03', '', ''])
        self.add('datasets.csv', ['SYN_D1', 'Synthetic dataset', 'pub', 'dom', 'EU', '2000-2020', 'act', 'active', '', 'https://example.org/a', 'SYN_R1', ''])

    def tearDown(self):
        cli.DATA, cli.ROOT = self._data, self._root
        shutil.rmtree(self.tmp, ignore_errors=True)

    def add(self, table, row):
        with (cli.DATA / table).open('a', encoding='utf-8-sig', newline='') as handle:
            csv.writer(handle).writerow(row)

    def errors(self):
        return [msg for level, msg in cli.issues() if level == 'ERROR']

    def warnings(self):
        return [msg for level, msg in cli.issues() if level == 'WARNING']


class ValidWorldTests(SyntheticWorld):
    def test_valid_world_has_no_errors(self):
        self.assertEqual(self.errors(), [])

    def test_real_project_data_has_no_errors(self):
        # Read-only check of the real tables: behaviour on current data must not regress.
        cli.DATA, cli.ROOT = self._data, self._root
        self.assertEqual([m for lvl, m in cli.issues() if lvl == 'ERROR'], [])


class InvalidValueTests(SyntheticWorld):
    """Each invalid value, inserted alone, must raise exactly one ERROR naming it."""

    def assert_single_error(self, needle):
        found = self.errors()
        self.assertEqual(len(found), 1, f'expected exactly one ERROR, got {found}')
        self.assertIn(needle, found[0])

    def test_unknown_origin(self):
        self.add('discovery_records.csv', ['SYN_R2', 'made_up_origin', '', '', 'T', 'https://example.org/b', '2026-01-01', '', ''])
        self.assert_single_error('made_up_origin')

    def test_malformed_record_url(self):
        self.add('discovery_records.csv', ['SYN_R2', 'seed', '', '', 'T', 'not a url', '2026-01-01', '', ''])
        self.assert_single_error('not a url')

    def test_non_iso_found_at(self):
        self.add('discovery_records.csv', ['SYN_R2', 'seed', '', '', 'T', 'https://example.org/b', '31/12/2026', '', ''])
        self.assert_single_error('31/12/2026')

    def test_unknown_reason_code(self):
        self.add('screening.csv', ['SYN_R1', 'title_abstract', 'SYN_REV_A', 'exclude', 'BOGUS_REASON', '', '2026-01-02', ''])
        self.assert_single_error('BOGUS_REASON')

    def test_non_iso_screening_date(self):
        self.add('screening.csv', ['SYN_R1', 'title_abstract', 'SYN_REV_A', 'include', '', '', 'not-a-date', ''])
        self.assert_single_error('not-a-date')

    def test_unknown_consensus_stage(self):
        self.add('consensus.csv', ['SYN_R1', 'bogus_stage', 'include', 'SYN_ADJ', '2026-01-04', '', ''])
        self.assert_single_error('bogus_stage')

    def test_unknown_audit_criterion(self):
        self.add('audit.csv', ['SYN_D1', 'SYN_REV_A', 'NOT_A_CRITERION', '2', 'https://example.org/e', 'manual', '2026-01-05', ''])
        self.assert_single_error('NOT_A_CRITERION')

    def test_non_iso_audit_date(self):
        self.add('audit.csv', ['SYN_D1', 'SYN_REV_A', 'LEGAL_ID', '2', 'https://example.org/e', 'manual', 'sometime', ''])
        self.assert_single_error('sometime')

    def test_unknown_rit_validation_status(self):
        self.add('rit_pilot.csv', ['SYN_C1', 'SYN_D1', '', '', '', '', '', '', '', '', '', '', 'adjudicado', ''])
        self.assert_single_error('adjudicado')

    def test_dataset_points_to_unknown_record(self):
        self.add('datasets.csv', ['SYN_D2', 'Other', 'pub', 'dom', 'EU', '', 'act', 'active', '', 'https://example.org/c', 'NOPE_RECORD', ''])
        self.assert_single_error('NOPE_RECORD')

    def test_dataset_points_to_record_without_final_inclusion(self):
        self.add('discovery_records.csv', ['SYN_R2', 'seed', '', '', 'T', 'https://example.org/b', '2026-01-01', '', ''])
        self.add('datasets.csv', ['SYN_D2', 'Other', 'pub', 'dom', 'EU', '', 'act', 'active', '', 'https://example.org/b', 'SYN_R2', ''])
        self.assert_single_error('SYN_R2')


class CountingAndReadOnlyTests(SyntheticWorld):
    def test_unknown_origin_is_not_counted_as_systematic(self):
        self.add('discovery_records.csv', ['SYN_R2', 'made_up_origin', '', '', 'T', 'https://example.org/b', '2026-01-01', '', ''])
        self.assertFalse(any('systematic hits await' in w for w in self.warnings()),
                         'a record with an invalid origin must not enter systematic counts')

    def test_duplicate_url_raises_warning_naming_both_records(self):
        self.add('discovery_records.csv', ['SYN_R2', 'seed', '', '', 'Other', 'https://example.org/a', '2026-01-01', '', ''])
        hits = [w for w in self.warnings() if 'SYN_R1' in w and 'SYN_R2' in w]
        self.assertEqual(len(hits), 1)
        self.assertEqual(self.errors(), [])

    def run_check(self):
        argv = sys.argv
        sys.argv = ['cli.py', 'check']
        try:
            with redirect_stdout(io.StringIO()):
                return cli.main()
        finally:
            sys.argv = argv

    def test_check_does_not_create_missing_tables(self):
        (cli.DATA / 'dedup.csv').unlink()
        code = self.run_check()
        self.assertEqual(code, 2)
        self.assertFalse((cli.DATA / 'dedup.csv').exists(), 'check must be read-only')

    def test_check_does_not_modify_any_file(self):
        def digest():
            return {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(cli.DATA.iterdir())}
        before = digest()
        self.run_check()
        self.assertEqual(before, digest())


if __name__ == '__main__':
    unittest.main()
