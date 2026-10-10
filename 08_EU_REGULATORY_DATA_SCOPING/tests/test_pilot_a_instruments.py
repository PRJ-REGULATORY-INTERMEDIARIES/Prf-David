"""G1-PREP tests for the Pilot A selection algorithm and coding instruments.

Forms are built in a temporary directory. Where a test fills a form, the content
is a SYNTHETIC FIXTURE with made-up reviewer ids (SYN_REV_A, SYN_REV_B): it is not
a human coding, not a simulated adjudication and not a research result.
"""
import csv
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import pilot_a_forms as forms  # noqa: E402
import select_pilot_a as sel   # noqa: E402

REAL_SAMPLE = ROOT / 'pilot_a' / 'selection' / 'PILOT_A_CANDIDATE_SAMPLE.csv'


class SelectionTests(unittest.TestCase):
    def setUp(self):
        self.rows = sel.load()
        self.seed = sel.default_seed()

    def test_is_deterministic(self):
        self.assertEqual(sel.select(self.seed, self.rows)['sample'], sel.select(self.seed, self.rows)['sample'])

    def test_satisfies_every_constraint(self):
        result = sel.select(self.seed, self.rows)
        self.assertTrue(all(result['verdict'].values()), result['verdict'])
        self.assertEqual(len(result['sample']), 20)
        self.assertEqual(len(self.rows) - len(result['sample']), 21)

    def test_only_factual_columns_are_loaded(self):
        for r in self.rows:
            self.assertEqual(set(r), set(sel.ALLOWED_COLUMNS))
        for banned in ('rgam_potential', 'initial_priority', 'limitations'):
            self.assertNotIn(banned, sel.ALLOWED_COLUMNS)

    def test_judgement_columns_cannot_change_the_result(self):
        # Rewrite the inventory with the judgement columns scrambled; the sample must not move.
        tmp = Path(tempfile.mkdtemp(prefix='g1prep_synthetic_'))
        try:
            with sel.SEEDS.open('r', encoding='utf-8-sig', newline='') as h:
                full = list(csv.DictReader(h))
            for i, r in enumerate(full):
                r['rgam_potential'], r['initial_priority'], r['limitations'] = f'X{i % 3}', f'P{9 - i % 4}', 'scrambled'
            alt = tmp / 'seeds.csv'
            with alt.open('w', encoding='utf-8-sig', newline='') as h:
                w = csv.DictWriter(h, fieldnames=list(full[0]))
                w.writeheader()
                w.writerows(full)
            self.assertEqual(sel.select(self.seed, sel.load(alt))['sample'], sel.select(self.seed, self.rows)['sample'])
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def test_written_sample_matches_the_algorithm(self):
        with REAL_SAMPLE.open('r', encoding='utf-8-sig', newline='') as h:
            written = sorted(r['source_seed_id'] for r in csv.DictReader(h))
        self.assertEqual(written, sel.select(self.seed, self.rows)['sample'])

    def test_infeasible_constraints_are_reported_not_relaxed(self):
        params = dict(sel.PARAMS, MIN_COMPOSITE_TYPE=99, MAX_ATTEMPTS=50)
        # precheck=False exercises the sampling path; with the G1-READY precheck the same
        # input is proved infeasible before any draw.
        result = sel.select(self.seed, self.rows, params, precheck=False)
        self.assertIsNone(result['sample'])
        self.assertEqual(result['failures']['C5_composite_type'], 50)
        proved = sel.select(self.seed, self.rows, params)
        self.assertEqual((proved['attempts'], proved['infeasible']), (0, ['C5_composite_type']))


class InstrumentTests(unittest.TestCase):
    def setUp(self):
        self.base = Path(tempfile.mkdtemp(prefix='g1prep_synthetic_')) / 'pilot_a'
        self.manifest = forms.build(base=self.base, sample_file=REAL_SAMPLE, seed=12345)
        self.form = {L: self.base / f'reviewer_{L}' / f'CODING_FORM_{L}.csv' for L in 'AB'}

    def tearDown(self):
        shutil.rmtree(self.base.parent, ignore_errors=True)

    def rows(self, letter):
        return forms.read_csv(self.form[letter])

    def test_two_equivalent_forms_with_blank_decisions(self):
        a, b = self.rows('A'), self.rows('B')
        self.assertEqual(len(a), 20)
        self.assertEqual(len(b), 20)
        self.assertEqual(tuple(a[0]), forms.FORM_COLUMNS)
        self.assertEqual(sorted(r['source_url'] for r in a), sorted(r['source_url'] for r in b))
        for r in a + b:
            self.assertTrue(all(r[c] == '' for c in forms.DECISION_FIELDS), 'no decision field may be pre-filled')

    def test_orders_differ_and_ids_are_neutral(self):
        a, b = self.rows('A'), self.rows('B')
        self.assertNotEqual([r['source_url'] for r in a], [r['source_url'] for r in b])
        self.assertEqual([r['item_id'] for r in a], [f'A-{n:02d}' for n in range(1, 21)])
        self.assertEqual([r['item_id'] for r in b], [f'B-{n:02d}' for n in range(1, 21)])

    def test_nothing_withheld_reaches_a_reviewer_folder(self):
        with sel.SEEDS.open('r', encoding='utf-8-sig', newline='') as h:
            inventory = list(csv.DictReader(h))
        secrets = {r['limitations'] for r in inventory} | {r['source_seed_id'] for r in inventory}
        for letter in 'AB':
            text = self.form[letter].read_text(encoding='utf-8-sig')
            header = text.splitlines()[0].split(',')
            for column in forms.FORBIDDEN:
                self.assertNotIn(column, header)
            for secret in secrets:
                self.assertNotIn(secret, text)
            names = {p.name for p in self.form[letter].parent.iterdir()}
            self.assertEqual(names, {f'CODING_FORM_{letter}.csv', 'INSTRUCTIONS.md', 'SOURCE_TAXONOMY_v0_2_DRAFT.md', 'ELIGIBILITY_CRITERIA_PROTOCOL_S6.md',
                                     f'PACKET_MANIFEST_REVIEWER_{letter}.json'})

    def test_key_is_a_bijection_kept_with_the_coordinator(self):
        key = forms.read_csv(self.base / 'coordinator' / 'ITEM_KEY.csv')
        self.assertEqual(len(key), 20)
        for col in ('source_seed_id', 'item_id_A', 'item_id_B'):
            self.assertEqual(len({r[col] for r in key}), 20)

    def test_roles_are_unassigned(self):
        self.assertEqual(set(self.manifest['roles'].values()), {'NOT ASSIGNED'})

    def test_blank_form_validates_as_blank_and_cannot_be_locked_or_compared(self):
        errors, stats = forms.validate(self.form['A'])
        self.assertEqual(errors, [])
        self.assertEqual(len(stats['blank_items']), 20)
        with self.assertRaises(SystemExit):
            forms.lock(self.base)
        with self.assertRaises(SystemExit):
            forms.compare(self.base)

    # ---- synthetic fills below: software fixtures only ----------------------

    def fill(self, letter, reviewer, category_for=lambda n: 'REG', uncertain_item=None):
        rows = self.rows(letter)
        for n, r in enumerate(rows):
            r.update({'reviewer_id': reviewer, 'verification_date': '2026-01-15', 'access_outcome': 'acessivel',
                      'operational_level': 'L1', 'operational_category': category_for(n), 'rule_applied': 'R5',
                      'primary_function': 'F5_REGISTRO_DE_ENTIDADES_OU_CASOS', 'legislative_candidate': 'nao',
                      'eligibility': 'include', 'eligibility_justification': 'synthetic fixture',
                      'evidence_urls': 'https://example.org/synthetic', 'evidence_notes': 'synthetic fixture',
                      'uncertainty_type': 'nenhuma', 'minutes': '5'})
            if r['item_id'] == uncertain_item:
                r.update({'operational_category': 'UNCERTAIN', 'uncertainty_type': 'regra_ambigua', 'missing_evidence': 'synthetic fixture'})
        with self.form[letter].open('w', encoding='utf-8-sig', newline='') as h:
            w = csv.DictWriter(h, fieldnames=forms.FORM_COLUMNS, lineterminator='\n')
            w.writeheader()
            w.writerows(rows)

    def test_validation_rejects_values_outside_the_vocabulary(self):
        self.fill('A', 'SYN_REV_A', category_for=lambda n: 'NOT_A_CLASS' if n == 0 else 'REG')
        errors, _ = forms.validate(self.form['A'])
        self.assertEqual([(c, 'NOT_A_CLASS' in m) for _, c, m in errors], [('operational_category', True)])

    def test_validation_requires_evidence_and_reason_for_uncertainty(self):
        self.fill('A', 'SYN_REV_A')
        rows = self.rows('A')
        rows[0]['evidence_urls'] = ''
        rows[1]['operational_category'] = 'UNCERTAIN'
        with self.form['A'].open('w', encoding='utf-8-sig', newline='') as h:
            w = csv.DictWriter(h, fieldnames=forms.FORM_COLUMNS, lineterminator='\n')
            w.writeheader()
            w.writerows(rows)
        errors, stats = forms.validate(self.form['A'])
        cols = sorted((item, col) for item, col, _ in errors)
        self.assertEqual(cols, [('A-01', 'evidence_urls'), ('A-02', 'missing_evidence'), ('A-02', 'uncertainty_type')])
        self.assertEqual(stats['items_with_uncertain_answer'], ['A-02'])

    def test_lock_then_compare_reports_one_named_pair_per_variable(self):
        self.fill('A', 'SYN_REV_A', uncertain_item='A-01')
        self.fill('B', 'SYN_REV_B', category_for=lambda n: 'DSE' if n < 5 else 'REG')
        forms.lock(self.base)
        result = forms.compare(self.base)
        self.assertEqual(result['reviewers'], ['SYN_REV_A', 'SYN_REV_B'])
        for var, res in result['single_valued'].items():
            self.assertEqual(len(res['pairs']), 1, var)
            self.assertEqual(res['pairs'][0]['pair'], ('SYN_REV_A', 'SYN_REV_B'))
            self.assertEqual(res['pairs'][0]['n_items'], 20)
            self.assertIsNone(res['pooled_result'])
        category = result['single_valued']['operational_category']['pairs'][0]
        self.assertEqual(category['n_items_with_uncertain'], 1)
        self.assertEqual(category['n_items_both_categorical'], 19)
        self.assertIn('SYN_REV_A × SYN_REV_B', forms.render(result))

    def test_compare_refuses_a_form_changed_after_locking(self):
        self.fill('A', 'SYN_REV_A')
        self.fill('B', 'SYN_REV_B')
        forms.lock(self.base)
        self.fill('B', 'SYN_REV_B', category_for=lambda n: 'COD')
        with self.assertRaises(SystemExit):
            forms.compare(self.base)

    def test_compare_refuses_identical_reviewer_ids(self):
        self.fill('A', 'SYN_REV_A')
        self.fill('B', 'SYN_REV_A')
        forms.lock(self.base)
        with self.assertRaises(SystemExit):
            forms.compare(self.base)


if __name__ == '__main__':
    unittest.main()
