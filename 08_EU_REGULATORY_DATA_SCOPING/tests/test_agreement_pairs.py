"""G1-PREP tests for defect 2 of the G0 diagnosis: inter-reviewer agreement.

ALL DATA IN THIS FILE ARE SYNTHETIC TEST FIXTURES with made-up reviewer labels
(SYN_A, SYN_B, ...). They are not research results and no statistic computed
here describes any real coding.

Reference: gates/G0/BASELINE_RUN.md (probe P1) and SPEC-K in
gates/G0_1/G0_1_STRATEGIC_ALIGNMENT.md.
"""
import importlib.util
import io
import shutil
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
spec = importlib.util.spec_from_file_location('cli', ROOT / 'scripts' / 'cli.py')
cli = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cli)


def row(item, reviewer, decision):
    return {'record_id': item, 'reviewer': reviewer, 'decision': decision}


def mixed_pairs():
    """Probe P1 of the G0 baseline: two different reviewer pairs and one uncertain."""
    return [row('1', 'SYN_A', 'include'), row('1', 'SYN_B', 'include'),
            row('2', 'SYN_C', 'exclude'), row('2', 'SYN_D', 'exclude'),
            row('3', 'SYN_A', 'include'), row('3', 'SYN_B', 'uncertain')]


def table_2x2(a, b, c, d):
    """a = both include, b = A include / B exclude, c = A exclude / B include, d = both exclude."""
    rows, n = [], 0
    for count, (x, y) in ((a, ('include', 'include')), (b, ('include', 'exclude')),
                          (c, ('exclude', 'include')), (d, ('exclude', 'exclude'))):
        for _ in range(count):
            n += 1
            rows += [row(str(n), 'SYN_A', x), row(str(n), 'SYN_B', y)]
    return rows


class LegacyFunctionTests(unittest.TestCase):
    """Behaviour of cli.kappa_or_na, the function that carried the defect."""

    def test_refuses_to_pool_different_reviewer_pairs(self):
        # Before the fix this returned {'n': 2, 'agreement': 1.0, 'kappa': 1.0}.
        with self.assertRaises(ValueError):
            cli.kappa_or_na(mixed_pairs())

    def test_single_pair_still_supported(self):
        k = cli.kappa_or_na([row('1', 'SYN_A', 'include'), row('1', 'SYN_B', 'include'),
                             row('2', 'SYN_A', 'exclude'), row('2', 'SYN_B', 'exclude')])
        self.assertEqual(k['n'], 2)
        self.assertEqual(k['kappa'], 1.0)


class PairwiseAgreementTests(unittest.TestCase):
    def setUp(self):
        import agreement  # fails before the fix: module did not exist
        self.ag = agreement

    def by_pair(self, rows, **kw):
        out = self.ag.pairwise_agreement(rows, **kw)
        return {r['pair']: r for r in out['pairs']}, out

    def test_t1_pairs_are_kept_apart_and_uncertain_is_counted(self):
        pairs, _ = self.by_pair(mixed_pairs())
        self.assertEqual(set(pairs), {('SYN_A', 'SYN_B'), ('SYN_C', 'SYN_D')})
        ab, cd = pairs[('SYN_A', 'SYN_B')], pairs[('SYN_C', 'SYN_D')]
        self.assertEqual(ab['n_items'], 2)
        self.assertEqual(ab['n_items_with_uncertain'], 1)
        self.assertEqual(ab['n_items_both_categorical'], 1)
        self.assertEqual(ab['observed_agreement_all'], 0.5)
        self.assertEqual(cd['n_items'], 1)
        self.assertFalse(any(r['n_items'] == 3 for r in pairs.values()), 'no pooled result may exist')

    def test_t2_single_category_gives_no_kappa_with_reason(self):
        rows = [row(str(i), r, 'include') for i in range(5) for r in ('SYN_A', 'SYN_B')]
        pairs, _ = self.by_pair(rows)
        res = pairs[('SYN_A', 'SYN_B')]
        self.assertEqual(res['observed_agreement_all'], 1.0)
        self.assertIsNone(res['kappa_categorical'])
        self.assertTrue(res['kappa_categorical_note'])

    def test_t3_known_value(self):
        pairs, _ = self.by_pair(table_2x2(20, 5, 10, 15))
        res = pairs[('SYN_A', 'SYN_B')]
        self.assertEqual(res['n_items'], 50)
        self.assertAlmostEqual(res['observed_agreement_categorical'], 0.70, places=6)
        self.assertAlmostEqual(res['expected_agreement_categorical'], 0.50, places=6)
        self.assertAlmostEqual(res['kappa_categorical'], 0.40, places=6)
        low, high = res['kappa_categorical_ci95']
        self.assertTrue(low < 0.40 < high)

    def test_t4_symmetry_under_reviewer_relabelling(self):
        rows = table_2x2(20, 5, 10, 15)
        swapped = [row(r['record_id'], 'SYN_B' if r['reviewer'] == 'SYN_A' else 'SYN_A', r['decision']) for r in rows]
        a = self.by_pair(rows)[0][('SYN_A', 'SYN_B')]
        b = self.by_pair(swapped)[0][('SYN_A', 'SYN_B')]
        self.assertAlmostEqual(a['kappa_categorical'], b['kappa_categorical'], places=9)
        self.assertEqual(a['observed_agreement_all'], b['observed_agreement_all'])

    def test_t5_table_sums_to_number_of_items(self):
        pairs, _ = self.by_pair(mixed_pairs() + table_2x2(3, 1, 1, 2))
        for res in pairs.values():
            self.assertEqual(sum(sum(r.values()) for r in res['table'].values()), res['n_items'])

    def test_t6_item_with_three_reviewers_is_listed_apart(self):
        rows = [row('1', 'SYN_A', 'include'), row('1', 'SYN_B', 'include'), row('1', 'SYN_C', 'exclude'),
                row('2', 'SYN_A', 'include'), row('2', 'SYN_B', 'exclude'),
                row('3', 'SYN_A', 'include')]
        pairs, out = self.by_pair(rows)
        self.assertEqual(pairs[('SYN_A', 'SYN_B')]['n_items'], 1)
        self.assertEqual(out['items_with_more_than_two_reviewers'], ['1'])
        self.assertEqual(out['items_with_one_reviewer'], ['3'])

    def test_uncertain_as_category_and_excluded_are_both_reported(self):
        rows = [row('1', 'SYN_A', 'uncertain'), row('1', 'SYN_B', 'uncertain'),
                row('2', 'SYN_A', 'include'), row('2', 'SYN_B', 'include'),
                row('3', 'SYN_A', 'include'), row('3', 'SYN_B', 'exclude'),
                row('4', 'SYN_A', 'exclude'), row('4', 'SYN_B', 'exclude')]
        res = self.by_pair(rows)[0][('SYN_A', 'SYN_B')]
        self.assertEqual(res['n_items'], 4)
        self.assertEqual(res['n_items_with_uncertain'], 1)
        self.assertEqual(res['n_items_both_uncertain'], 1)
        self.assertEqual(res['observed_agreement_all'], 0.75)
        self.assertAlmostEqual(res['observed_agreement_categorical'], 2 / 3, places=9)
        self.assertEqual(res['table']['uncertain']['uncertain'], 1)

    def test_other_variable_and_custom_uncertain_label(self):
        rows = [{'item_id': '1', 'reviewer': 'SYN_A', 'primary_class': 'REG'},
                {'item_id': '1', 'reviewer': 'SYN_B', 'primary_class': 'UNCERTAIN'},
                {'item_id': '2', 'reviewer': 'SYN_A', 'primary_class': 'COD'},
                {'item_id': '2', 'reviewer': 'SYN_B', 'primary_class': 'COD'}]
        pairs, out = self.by_pair(rows, variable='primary_class', item_key='item_id', uncertain_values=('UNCERTAIN',))
        self.assertEqual(out['variable'], 'primary_class')
        self.assertEqual(pairs[('SYN_A', 'SYN_B')]['n_items_with_uncertain'], 1)

    def test_blank_answers_are_reported_not_scored(self):
        rows = [row('1', 'SYN_A', ''), row('1', 'SYN_B', 'include'),
                row('2', 'SYN_A', 'include'), row('2', 'SYN_B', 'include')]
        pairs, out = self.by_pair(rows)
        self.assertEqual(pairs[('SYN_A', 'SYN_B')]['n_items'], 1)
        self.assertEqual(out['items_with_blank_answer'], ['1'])

    def test_set_agreement_jaccard(self):
        rows = [{'record_id': '1', 'reviewer': 'SYN_A', 'roles': 'F1;F2'},
                {'record_id': '1', 'reviewer': 'SYN_B', 'roles': 'F2; F3'},
                {'record_id': '2', 'reviewer': 'SYN_A', 'roles': ''},
                {'record_id': '2', 'reviewer': 'SYN_B', 'roles': ''}]
        out = self.ag.pairwise_set_agreement(rows, variable='roles')
        res = out['pairs'][0]
        self.assertEqual(res['pair'], ('SYN_A', 'SYN_B'))
        self.assertEqual(res['n_items'], 2)
        self.assertEqual(res['n_items_identical_sets'], 1)
        self.assertAlmostEqual(res['mean_jaccard'], (1 / 3 + 1.0) / 2, places=9)


class ReportTests(unittest.TestCase):
    def test_report_lists_each_pair_separately(self):
        tmp = Path(tempfile.mkdtemp(prefix='g1prep_synthetic_'))
        data, root = cli.DATA, cli.ROOT
        cli.DATA, cli.ROOT = tmp / 'data', tmp
        try:
            with redirect_stdout(io.StringIO()):
                cli.init()
                import csv
                with (cli.DATA / 'discovery_records.csv').open('a', encoding='utf-8-sig', newline='') as h:
                    w = csv.writer(h)
                    for i in ('1', '2', '3'):
                        w.writerow([i, 'seed', '', '', 'T' + i, 'https://example.org/' + i, '2026-01-01', '', ''])
                with (cli.DATA / 'screening.csv').open('a', encoding='utf-8-sig', newline='') as h:
                    w = csv.writer(h)
                    for r in mixed_pairs():
                        w.writerow([r['record_id'], 'title_abstract', r['reviewer'], r['decision'], 'OTHER' if r['decision'] == 'exclude' else '', '', '2026-01-02', ''])
                cli.report()
            text = (tmp / 'outputs' / 'STATUS_REPORT.md').read_text(encoding='utf-8')
            self.assertIn('SYN_A × SYN_B', text)
            self.assertIn('SYN_C × SYN_D', text)
        finally:
            cli.DATA, cli.ROOT = data, root
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == '__main__':
    unittest.main()
