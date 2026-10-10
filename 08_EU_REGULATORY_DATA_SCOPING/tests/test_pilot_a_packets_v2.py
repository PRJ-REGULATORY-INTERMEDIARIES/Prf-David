"""G1-READY tests: neutral labels, pre-filled field validation against the packet
manifest, and per-reviewer packaging. Written before the change to
scripts/pilot_a_forms.py.

Everything is built in a temporary directory. Filled forms and evidence files
used here are SYNTHETIC FIXTURES, not human codings and not research evidence.
"""
import csv
import json
import shutil
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import pilot_a_forms as forms  # noqa: E402

SAMPLE = ROOT / 'pilot_a' / 'selection' / 'PILOT_A_CANDIDATE_SAMPLE.csv'
LABELS = ROOT / 'pilot_a' / 'labels' / 'LABELS_PROPOSED.csv'
SEEDS = ROOT / 'inputs' / 'seed_inventory_v0_1.csv'


def read(path):
    with Path(path).open('r', encoding='utf-8-sig', newline='') as h:
        return list(csv.DictReader(h))


class LabelFileTests(unittest.TestCase):
    def setUp(self):
        self.labels, self.seeds = read(LABELS), read(SEEDS)

    def test_covers_the_41_seeds_with_unique_labels(self):
        self.assertEqual([r['source_seed_id'] for r in self.labels], [r['source_seed_id'] for r in self.seeds])
        self.assertEqual(len({r['neutral_label'] for r in self.labels}), 41)
        self.assertTrue(all(r['neutral_label'].strip() for r in self.labels))

    def test_inventory_name_column_matches_the_inventory(self):
        self.assertEqual([r['inventory_name'] for r in self.labels], [r['name'] for r in self.seeds])

    def test_removed_descriptors_are_really_absent(self):
        for r in self.labels:
            if r['removed_text']:
                self.assertIn(r['removed_text'], r['inventory_name'], r['source_seed_id'])
                self.assertNotIn(r['removed_text'], r['neutral_label'], r['source_seed_id'])


class PacketV2Tests(unittest.TestCase):
    def setUp(self):
        self.base = Path(tempfile.mkdtemp(prefix='g1ready_synthetic_')) / 'pilot_a'
        self.manifest = forms.build(base=self.base, sample_file=SAMPLE, seed=777, labels_file=LABELS)
        self.form = {L: self.base / f'reviewer_{L}' / f'CODING_FORM_{L}.csv' for L in 'AB'}

    def tearDown(self):
        shutil.rmtree(self.base.parent, ignore_errors=True)

    def test_forms_show_neutral_labels_only(self):
        labels = {r['source_seed_id']: r for r in read(LABELS)}
        key = {r['source_seed_id']: r for r in read(self.base / 'coordinator' / 'ITEM_KEY.csv')}
        shown = {r['item_id']: r['source_label'] for r in read(self.form['A'])}
        for sid, k in key.items():
            self.assertEqual(shown[k['item_id_A']], labels[sid]['neutral_label'])
        text = self.form['A'].read_text(encoding='utf-8-sig')
        for r in labels.values():
            if r['removed_text']:
                self.assertNotIn(r['removed_text'], text)

    def test_missing_label_stops_the_build(self):
        partial = self.base.parent / 'partial.csv'
        rows = read(LABELS)[:5]
        with partial.open('w', encoding='utf-8-sig', newline='') as h:
            w = csv.DictWriter(h, fieldnames=list(rows[0]))
            w.writeheader()
            w.writerows(rows)
        with self.assertRaises(SystemExit):
            forms.build(base=self.base.parent / 'other', sample_file=SAMPLE, seed=777, labels_file=partial)

    def test_reviewer_manifest_holds_no_key_material(self):
        for L in 'AB':
            path = self.base / f'reviewer_{L}' / f'PACKET_MANIFEST_REVIEWER_{L}.json'
            text = path.read_text(encoding='utf-8')
            data = json.loads(text)
            self.assertEqual(len(data['prefilled_item_sha256']), 20)
            self.assertNotRegex(text, r'\bEU\d\d\b')
            self.assertNotIn('item_id_' + ('B' if L == 'A' else 'A'), text)
            self.assertNotIn('seed', text.lower())

    def fill(self, letter, reviewer='SYN_REV'):
        rows = read(self.form[letter])
        for r in rows:
            r.update({'reviewer_id': reviewer + '_' + letter, 'verification_date': '2026-01-15', 'access_outcome': 'acessivel',
                      'operational_level': 'L1', 'operational_category': 'REG', 'rule_applied': 'R5',
                      'primary_function': 'F5_REGISTRO_DE_ENTIDADES_OU_CASOS', 'legislative_candidate': 'nao',
                      'eligibility': 'include', 'eligibility_justification': 'synthetic fixture',
                      'evidence_urls': 'https://example.org/synthetic', 'evidence_notes': 'synthetic fixture',
                      'uncertainty_type': 'nenhuma', 'minutes': '5'})
        self.write(letter, rows)

    def write(self, letter, rows):
        with self.form[letter].open('w', encoding='utf-8-sig', newline='') as h:
            w = csv.DictWriter(h, fieldnames=forms.FORM_COLUMNS, lineterminator='\n')
            w.writeheader()
            w.writerows(rows)

    def test_untouched_prefilled_columns_pass(self):
        self.fill('A')
        errors, stats = forms.validate(self.form['A'])
        self.assertEqual(errors, [])
        self.assertTrue(stats['prefilled_checked_against_manifest'])

    def test_altered_label_is_detected_and_named(self):
        self.fill('A')
        rows = read(self.form['A'])
        rows[3]['source_label'] = rows[3]['source_label'] + ' (edited)'
        self.write('A', rows)
        errors, _ = forms.validate(self.form['A'])
        self.assertEqual([(i, c) for i, c, _ in errors], [(rows[3]['item_id'], 'prefilled')])

    def test_altered_url_removed_row_and_added_row_are_detected(self):
        self.fill('A')
        rows = read(self.form['A'])
        rows[0]['source_url'] = 'https://example.org/changed'
        removed = rows.pop(5)
        extra = dict(rows[1], item_id='A-99')
        rows.append(extra)
        self.write('A', rows)
        errors, _ = forms.validate(self.form['A'])
        found = {(i, c) for i, c, _ in errors if c == 'prefilled'}
        self.assertEqual(found, {(rows[0]['item_id'], 'prefilled'), (removed['item_id'], 'prefilled'), ('A-99', 'prefilled')})

    def test_blank_form_also_checks_prefilled_columns(self):
        rows = read(self.form['B'])
        rows[2]['reviewer_role'] = 'REVIEWER_A'
        self.write('B', rows)
        errors, _ = forms.validate(self.form['B'])
        self.assertEqual([(i, c) for i, c, _ in errors], [(rows[2]['item_id'], 'prefilled')])

    def test_lock_refuses_a_form_with_altered_prefilled_columns(self):
        self.fill('A')
        self.fill('B')
        rows = read(self.form['B'])
        rows[0]['source_label'] = 'tampered'
        self.write('B', rows)
        with self.assertRaises(SystemExit):
            forms.lock(self.base)

    # ---- packaging ------------------------------------------------------------

    def synthetic_evidence(self):
        ev = self.base.parent / 'evidence'
        key = read(self.base / 'coordinator' / 'ITEM_KEY.csv')
        sid = key[0]['source_seed_id']
        (ev / sid).mkdir(parents=True)
        (ev / sid / '20260105T100000_abcdef123456.html').write_bytes(b'<html>synthetic evidence</html>')
        log = [{'capture_id': f'{sid}_x', 'record_id': sid, 'method': 'http_get', 'outcome': 'CAPTURED',
                'original_url': 'https://example.org/a', 'final_url': 'https://example.org/b',
                'captured_at_utc': '2026-01-05T10:00:00+00:00', 'content_type': 'text/html', 'bytes': 31,
                'sha256': __import__('hashlib').sha256(b'<html>synthetic evidence</html>').hexdigest(),
                'raw_file': f'{sid}/20260105T100000_abcdef123456.html', 'last_modified': None},
               {'capture_id': f'{key[1]["source_seed_id"]}_y', 'record_id': key[1]['source_seed_id'], 'method': 'http_get',
                'outcome': 'FAILED', 'original_url': 'https://example.org/c', 'captured_at_utc': '2026-01-05T10:01:00+00:00',
                'raw_file': None, 'sha256': None},
               {'capture_id': 'OUTSIDE_z', 'record_id': 'EU99', 'method': 'http_get', 'outcome': 'FAILED',
                'original_url': 'https://example.org/z', 'captured_at_utc': '2026-01-05T10:02:00+00:00', 'raw_file': None, 'sha256': None}]
        (ev / 'CAPTURE_LOG.jsonl').write_text('\n'.join(json.dumps(x) for x in log) + '\n', encoding='utf-8')
        return ev, key

    def test_package_holds_only_that_reviewers_material(self):
        ev, key = self.synthetic_evidence()
        info = forms.package(self.base, 'A', evidence_dir=ev)
        with zipfile.ZipFile(info['zip']) as z:
            names = z.namelist()
            index = z.read('evidence/EVIDENCE_INDEX.csv').decode('utf-8-sig')
        joined = '\n'.join(names)
        for banned in ('ITEM_KEY', 'reviewer_B', 'CODING_FORM_B', 'coordinator', 'selection', 'LABELS', 'LOCK', 'CAPTURE_LOG'):
            self.assertNotIn(banned, joined)
        self.assertNotRegex(joined, r'\bEU\d\d\b')
        self.assertIn('CODING_FORM_A.csv', names)
        item_a = key[0]['item_id_A']
        self.assertIn(f'evidence/{item_a}/20260105T100000_abcdef123456.html', names)
        self.assertNotRegex(index, r'\bEU\d\d\b')
        rows = list(csv.DictReader(index.splitlines()))
        self.assertEqual({r['item_id'] for r in rows}, {item_a, key[1]['item_id_A']})
        self.assertEqual({r['outcome'] for r in rows}, {'CAPTURED', 'FAILED'})
        self.assertEqual(info['sha256'], __import__('hashlib').sha256(Path(info['zip']).read_bytes()).hexdigest())

    def test_packages_of_a_and_b_use_their_own_item_ids(self):
        ev, key = self.synthetic_evidence()
        b = forms.package(self.base, 'B', evidence_dir=ev)
        with zipfile.ZipFile(b['zip']) as z:
            names = z.namelist()
        self.assertIn(f'evidence/{key[0]["item_id_B"]}/20260105T100000_abcdef123456.html', names)
        self.assertFalse(any(n.startswith('evidence/A-') for n in names))

    def test_package_without_evidence_says_so(self):
        info = forms.package(self.base, 'A', evidence_dir=None)
        self.assertEqual(info['evidence_files'], 0)
        with zipfile.ZipFile(info['zip']) as z:
            self.assertNotIn('evidence/EVIDENCE_INDEX.csv', z.namelist())


if __name__ == '__main__':
    unittest.main()
