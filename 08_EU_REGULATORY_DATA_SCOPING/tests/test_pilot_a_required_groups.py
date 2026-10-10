"""G1-READY tests: explicit required groups and feasibility analysis in the Pilot A selection.

Written before the change to scripts/select_pilot_a.py. The inventory is read
only; nothing is written to pilot_a/. Group contents used here are test inputs,
not a sample approved by anyone.
"""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import select_pilot_a as sel  # noqa: E402

G1_PREP_SAMPLE = ['EU01', 'EU02', 'EU03', 'EU07', 'EU08', 'EU13', 'EU15', 'EU17', 'EU19', 'EU23',
                  'EU24', 'EU25', 'EU27', 'EU28', 'EU30', 'EU32', 'EU33', 'EU37', 'EU39', 'EU41']


class RequiredGroupTests(unittest.TestCase):
    def setUp(self):
        self.rows = sel.load()
        self.seed = sel.default_seed()

    def test_without_groups_the_g1_prep_sample_is_reproduced(self):
        self.assertEqual(self.seed, 1160865795)
        self.assertEqual(sel.select(self.seed, self.rows)['sample'], G1_PREP_SAMPLE)
        self.assertEqual(sel.select(self.seed, self.rows, required_groups=[])['sample'], G1_PREP_SAMPLE)

    def test_required_groups_enter_complete_and_constraints_still_hold(self):
        groups = [['EU08', 'EU09'], ['EU33', 'EU34'], ['EU11']]
        result = sel.select(self.seed, self.rows, required_groups=groups)
        self.assertIsNotNone(result['sample'])
        for g in groups:
            self.assertTrue(set(g) <= set(result['sample']), g)
        self.assertTrue({'EU03', 'EU07'} <= set(result['sample']), 'identical-URL group must stay forced')
        self.assertTrue(all(result['verdict'].values()), result['verdict'])
        self.assertEqual(len(result['sample']), 20)
        self.assertEqual(result['forced'], sorted({'EU03', 'EU07', 'EU08', 'EU09', 'EU11', 'EU33', 'EU34'}))

    def test_selection_with_groups_is_deterministic(self):
        groups = [['EU08', 'EU09'], ['EU11']]
        a = sel.select(self.seed, self.rows, required_groups=groups)['sample']
        b = sel.select(self.seed, self.rows, required_groups=groups)['sample']
        self.assertEqual(a, b)

    def test_unknown_identifier_is_rejected(self):
        with self.assertRaises(ValueError):
            sel.select(self.seed, self.rows, required_groups=[['EU08', 'EU99']])


class FeasibilityTests(unittest.TestCase):
    def setUp(self):
        self.rows = sel.load()
        self.seed = sel.default_seed()

    def test_baseline_is_feasible_with_a_witness(self):
        f = sel.feasibility(self.rows, [], seed=self.seed)
        self.assertEqual(f['status'], 'FEASIBLE')
        self.assertTrue(all(b['ok'] for b in f['bounds'].values()))
        self.assertGreater(f['search']['accepted'], 0)

    def test_family_cap_violation_is_proved_infeasible_without_sampling(self):
        academic = sorted(r['source_seed_id'] for r in self.rows if r['layer'] == 'Corpus acadêmico')[:5]
        f = sel.feasibility(self.rows, [academic], seed=self.seed)
        self.assertEqual(f['status'], 'INFEASIBLE')
        self.assertFalse(f['bounds']['C7_max_per_family']['ok'])
        self.assertIsNone(f['search'])
        result = sel.select(self.seed, self.rows, required_groups=[academic])
        self.assertIsNone(result['sample'])
        self.assertEqual(result['attempts'], 0)
        self.assertEqual(result['infeasible'], ['C7_max_per_family'])

    def test_too_many_forced_records_is_infeasible(self):
        ids = [r['source_seed_id'] for r in self.rows][:21]
        f = sel.feasibility(self.rows, [ids], seed=self.seed)
        self.assertEqual(f['status'], 'INFEASIBLE')
        self.assertFalse(f['bounds']['C1_size']['ok'])

    def test_holdout_bound_counts_families_emptied_by_forcing(self):
        # Forcing both records of two 2-member families leaves at most 8 families in reserve (11 - Atores - 2).
        jur = sorted(r['source_seed_id'] for r in self.rows if r['layer'] == 'Jurisprudência')
        apl = sorted(r['source_seed_id'] for r in self.rows if r['layer'] == 'Aplicação setorial')
        f = sel.feasibility(self.rows, [jur, apl], seed=self.seed)
        self.assertEqual(f['bounds']['C8_holdout_families']['best_possible'], 8)
        self.assertEqual(f['status'], 'INFEASIBLE')

    def test_feasibility_search_does_not_consume_the_selection_stream(self):
        groups = [['EU08', 'EU09']]
        before = sel.select(self.seed, self.rows, required_groups=groups)['sample']
        sel.feasibility(self.rows, groups, seed=self.seed)
        self.assertEqual(sel.select(self.seed, self.rows, required_groups=groups)['sample'], before)


class OutputTests(unittest.TestCase):
    def test_outputs_go_to_the_given_folder_and_are_marked_proposed(self):
        tmp = Path(tempfile.mkdtemp(prefix='g1ready_synthetic_'))
        try:
            rows, seed = sel.load(), sel.default_seed()
            spec = {'status': 'PROPOSED', 'groups': [{'ids': ['EU08', 'EU09'], 'reason': 'test input'}]}
            result = sel.select(seed, rows, required_groups=[g['ids'] for g in spec['groups']])
            log = sel.write_outputs(result, seed, 'test', rows, out=tmp, required_spec=spec, label='TEST')
            self.assertTrue((tmp / 'PILOT_A_CANDIDATE_SAMPLE.csv').exists())
            self.assertIn('PROPOSED', log['status'])
            self.assertEqual(log['required_groups'], spec)
            self.assertEqual(log['forced_records'], result['forced'])
            stored = json.loads((tmp / 'PILOT_A_SELECTION_LOG.json').read_text(encoding='utf-8'))
            self.assertEqual(stored['sample'], result['sample'])
        finally:
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == '__main__':
    unittest.main()
