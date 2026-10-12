"""Tests of the G2 mapping instruments (mapping/scripts) and of the mapping base itself.

The synthetic tests show that the tools behave as specified. They are not
evidence about the coverage of the mapping. No test touches the network.
"""
import copy
import csv
import hashlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'mapping' / 'scripts'))
sys.path.insert(0, str(ROOT / 'scripts'))
import build_mapping_base as bmb  # noqa: E402
import capture_evidence  # noqa: E402
import mapping_search as ms  # noqa: E402
import validate_mapping as vm  # noqa: E402

DATA = ROOT / 'mapping' / 'data'
VOCAB = json.loads((ROOT / 'mapping' / 'schemas' / 'mapping_vocabularies.json').read_text(encoding='utf-8'))


class SearchToolTest(unittest.TestCase):
    def test_url_is_built_deterministically_and_encoded(self):
        url = ms.build_url('DEU', "législation de l'Union")
        self.assertEqual(url, ms.build_url('DEU', "législation de l'Union"))
        self.assertIn('q=l%C3%A9gislation%20de%20l%27Union', url)

    def test_parsers_extract_id_title_and_total(self):
        cases = {
            'DEU': ({'result': {'count': 7, 'results': [{'id': 'x', 'title': {'fr': 'Titre', 'en': 'Title'}, 'publisher': {'name': 'P'}}]}}, 7, 'x', 'Title'),
            'ZEN': ({'hits': {'total': 3, 'hits': [{'id': 1, 'doi': '10.1/z', 'metadata': {'title': 'T  spaced', 'creators': [{'name': 'A'}]}}]}}, 3, '10.1/z', 'T spaced'),
            'DVN': ({'data': {'total_count': 2, 'items': [{'global_id': 'doi:1', 'name': 'N', 'url': 'https://d/1'}]}}, 2, 'doi:1', 'N'),
            'DCT': ({'meta': {'total': 4}, 'data': [{'attributes': {'doi': '10.2/a', 'titles': [{'title': 'D'}]}}]}, 4, '10.2/a', 'D'),
            'OAX': ({'meta': {'count': 9}, 'results': [{'id': 'https://openalex.org/W1', 'title': 'O', 'doi': None}]}, 9, 'https://openalex.org/W1', 'O'),
            'HF': ([{'id': 'org/name', 'author': 'org'}], None, 'org/name', 'org/name'),
            'GH': ({'total_count': 1, 'items': [{'full_name': 'o/r', 'description': None, 'html_url': 'https://g/o/r'}]}, 1, 'o/r', 'o/r'),
        }
        for platform, (payload, total, rec_id, title) in cases.items():
            got_total, hits = ms.parse_hits(platform, payload)
            self.assertEqual((got_total, hits[0]['platform_record_id'], hits[0]['title']), (total, rec_id, title), platform)

    def test_run_stores_response_logs_it_and_rebuilds_hits_without_network(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            reg = tmp / 'q.csv'
            reg.write_text('search_id,family,resource_set,platform,query,language,rationale\nSR-T-001,f,A,GH,x,en,r\nSR-T-002,f,A,GH,y,en,r\n', encoding='utf-8')
            body = json.dumps({'total_count': 1, 'items': [{'full_name': 'o/r', 'html_url': 'https://g/o/r'}]}).encode()
            calls = []

            def fetch(url):
                calls.append(url)
                if 'q=y' in url:
                    raise OSError('boom')
                return body, 200

            out = ms.run(reg, search_dir=tmp / 's', pause=0, fetch=fetch)
            self.assertEqual([r['outcome'] for r in out], ['EXECUTED', 'FAILED'])
            self.assertEqual(out[0]['sha256'], hashlib.sha256(body).hexdigest())
            self.assertEqual((tmp / 's' / out[0]['raw_file']).read_bytes(), body)
            self.assertIn('boom', out[1]['error'])
            self.assertEqual(len(ms.build_hits(tmp / 's')), 1)
            again = ms.run(reg, search_dir=tmp / 's', pause=0, fetch=fetch)  # executed query is not repeated; the failed one is retried
            self.assertEqual([r['search_id'] for r in again], ['SR-T-002'])
            self.assertEqual(len(calls), 3)

    def test_registry_identifiers_are_unique_and_platforms_known(self):
        rows = ms.read_registry(ROOT / 'mapping' / 'protocol' / 'SEARCH_QUERIES_G2_ROUND1.csv')
        self.assertEqual(len({r['search_id'] for r in rows}), len(rows))
        self.assertTrue(all(r['platform'] in ms.PLATFORMS for r in rows))


class BuilderTest(unittest.TestCase):
    def test_split_tag(self):
        self.assertEqual(bmb.split_tag('Name|P'), ('Name', 'PRIMARY_PAGE'))
        self.assertEqual(bmb.split_tag('Name|S'), ('Name', 'SEED_UNVERIFIED'))
        self.assertEqual(bmb.split_tag('NOT_ASSESSED'), ('NOT_ASSESSED', ''))
        self.assertEqual(bmb.split_tag('a|b'), ('a|b', ''))

    def test_build_is_deterministic_and_matches_the_files_on_disk(self):
        first, second = bmb.build(), bmb.build()
        self.assertEqual(first, second)
        for name, (cols, rows) in first.items():
            buf = io.StringIO(newline='')
            w = csv.DictWriter(buf, fieldnames=cols, lineterminator='\n', restval='')
            w.writeheader()
            w.writerows(rows)
            self.assertEqual(buf.getvalue(), (DATA / f'{name}.csv').read_text(encoding='utf-8'), f'{name}.csv is not the build output')

    def test_curation_cannot_cite_a_hit_that_was_not_returned(self):
        cur = bmb.load_curation()
        cur.RESOURCES = copy.deepcopy(cur.RESOURCES)
        cur.RESOURCES[-1]['hits'] = [('SR-G2-001', 'no-such-record')]
        with self.assertRaises(ValueError):
            bmb.build(curation=cur)


class ValidatorTest(unittest.TestCase):
    def setUp(self):
        self.tables = vm.load()
        self.shared = set(bmb.load_curation().SHARED_URL_JUSTIFICATIONS)

    def run_validator(self, tables, **kw):
        return vm.validate(tables, VOCAB, shared_urls=self.shared, check_files=False, **kw)

    def errors(self, tables, check, **kw):
        return [m for s, c, m in self.run_validator(tables, **kw) if s == 'ERROR' and c == check]

    def mutated(self):
        return copy.deepcopy(self.tables)

    def test_detects_duplicate_and_malformed_identifiers(self):
        t = self.mutated()
        t['resources'][1]['resource_id'] = t['resources'][0]['resource_id']
        self.assertTrue(self.errors(t, 'id_unique'))
        t = self.mutated()
        t['resources'][0]['resource_id'] = 'R1'
        self.assertTrue(self.errors(t, 'id_format'))

    def test_detects_value_outside_vocabulary(self):
        t = self.mutated()
        t['resources'][0]['verification_status'] = 'PROBABLY_FINE'
        self.assertTrue(self.errors(t, 'vocabulary'))

    def test_detects_dangling_references(self):
        t = self.mutated()
        t['resource_relations'][0]['target_resource_id'] = 'MR-9999'
        self.assertTrue(self.errors(t, 'reference'))
        t = self.mutated()
        t['access_endpoints'][0]['evidence_id'] = 'EVC-9999'
        self.assertTrue(self.errors(t, 'reference'))

    def test_detects_invalid_url(self):
        t = self.mutated()
        t['access_endpoints'][0]['url'] = 'eur-lex.europa.eu'
        self.assertTrue(self.errors(t, 'url_syntax'))

    def test_detects_unjustified_shared_url_and_repeated_resource(self):
        t = self.mutated()
        t['resources'][1]['primary_access_url'] = t['resources'][0]['primary_access_url']
        self.assertTrue(self.errors(t, 'duplicate'))
        t = self.mutated()
        t['resources'][1]['verified_name'] = t['resources'][0]['verified_name']
        t['resources'][1]['maintainer'] = t['resources'][0]['maintainer']
        self.assertTrue(self.errors(t, 'duplicate'))

    def test_verified_status_needs_successful_evidence(self):
        t = self.mutated()
        row = next(r for r in t['resources'] if r['verification_status'] == 'VERIFIED')
        row['evidence_ids'] = ''
        self.assertTrue(self.errors(t, 'evidence'))

    def test_supported_relation_cannot_rest_on_inference(self):
        t = self.mutated()
        t['resource_relations'][0]['basis'] = 'AGENT_INFERENCE'
        self.assertTrue(self.errors(t, 'evidence'))

    def test_agent_rows_cannot_be_presented_as_confirmed(self):
        t = self.mutated()
        t['resources'][0]['researcher_confirmed'] = 'YES'
        self.assertTrue(self.errors(t, 'provisional'))
        t = self.mutated()
        t['resources'][0]['category_status'] = 'CONFIRMED'
        self.assertTrue(self.errors(t, 'provisional'))

    def test_filled_field_needs_a_declared_basis(self):
        t = self.mutated()
        t['resources'][0]['field_basis'] = ''
        self.assertTrue(self.errors(t, 'basis'))

    def test_systematic_origin_needs_a_registered_hit(self):
        t = self.mutated()
        target = next(r for r in t['resources'] if r['discovery_origin'] == 'SYSTEMATIC_SEARCH')['resource_id']
        t['discovery_log'] = [d for d in t['discovery_log'] if d['resource_id'] != target or not d['search_id']]
        self.assertTrue(self.errors(t, 'origin'))

    def test_detects_altered_seed_file_and_altered_registered_name(self):
        with tempfile.TemporaryDirectory() as tmp:
            altered = Path(tmp) / 'seed.csv'
            altered.write_bytes((ROOT / 'inputs' / 'seed_inventory_v0_1.csv').read_bytes().replace(b'EUR-Lex', b'EURLex', 1))
            self.assertTrue(self.errors(self.mutated(), 'preservation', seed_path=altered))
        t = self.mutated()
        t['resources'][0]['registered_name'] = 'EUR-Lex'
        self.assertTrue(self.errors(t, 'preservation'))


class MappingBaseTest(unittest.TestCase):
    """Properties of the base produced in round 1. Structural, not empirical, claims."""

    @classmethod
    def setUpClass(cls):
        cls.tables = vm.load()
        cls.res = {r['resource_id']: r for r in cls.tables['resources']}

    def test_real_base_has_no_validation_error_including_evidence_hashes(self):
        findings = vm.validate(self.tables, VOCAB, shared_urls=set(bmb.load_curation().SHARED_URL_JUSTIFICATIONS))
        self.assertEqual([f for f in findings if f[0] == 'ERROR'], [])

    def test_seed_inventory_is_byte_identical_to_g0(self):
        digest = hashlib.sha256((ROOT / 'inputs' / 'seed_inventory_v0_1.csv').read_bytes()).hexdigest()
        self.assertEqual(digest, vm.SEED_SHA256)

    def test_the_41_seeds_keep_their_identifiers_in_order(self):
        seeds = [r['seed_id'] for r in self.tables['resources'] if r['seed_id']]
        self.assertEqual(seeds, [f'EU{i:02d}' for i in range(1, 42)])
        self.assertEqual([a['seed_id'] for a in self.tables['seed_audit']], seeds)

    def test_eu03_and_eu07_are_distinct_resources_with_distinct_access(self):
        dump, elds = self.res['MR-0003'], self.res['MR-0007']
        self.assertEqual((dump['seed_id'], elds['seed_id']), ('EU03', 'EU07'))
        self.assertEqual(dump['description_url'], 'https://data.europa.eu/en/ELDS')
        self.assertEqual(dump['primary_access_url'], 'https://datadump.publications.europa.eu/')
        self.assertEqual(elds['primary_access_url'], 'https://data.europa.eu/en/ELDS')
        same = [r for r in self.tables['resource_relations'] if r['relation_type'] == 'same_resource_as'
                and {r['source_resource_id'], r['target_resource_id']} == {'MR-0003', 'MR-0007'}]
        self.assertEqual(same, [])
        end = next(e for e in self.tables['access_endpoints'] if e['url'] == 'https://datadump.publications.europa.eu/')
        self.assertEqual((end['access_status'], end['auth_required'], end['http_status']), ('AUTH_REQUIRED', 'YES', '401'))
        self.assertNotIn(dump['verification_status'], ('OUT_OF_SCOPE', 'INACCESSIBLE'))

    def test_access_failure_is_never_recorded_as_exclusion(self):
        failed = [r for r in self.tables['resources'] if r['verification_status'] == 'INACCESSIBLE']
        self.assertTrue(failed)
        self.assertTrue(all(r['eligibility_preliminary'] != 'EXCLUDE' for r in failed))

    def test_every_row_is_marked_provisional(self):
        self.assertTrue(all(r['classification_basis'] == 'AGENT_PROVISIONAL' and r['researcher_confirmed'] == 'NO' for r in self.tables['resources']))
        self.assertTrue(all(r['researcher_confirmed'] == 'NO' for r in self.tables['resource_relations']))
        self.assertTrue(all(d['decided_by'] == 'AGENT_PROVISIONAL' for d in self.tables['decisions_log']))

    def test_capture_log_hashes_verify_with_the_g1_tool(self):
        self.assertEqual(capture_evidence.verify(ROOT / 'mapping' / 'evidence' / 'captures'), [])

    def test_every_executed_search_is_in_the_discovery_log(self):
        logged = {d['search_id'] for d in self.tables['discovery_log'] if d['entry_type'] == 'SEARCH_RUN'}
        registry = set()
        for path in (ROOT / 'mapping' / 'protocol').glob('SEARCH_QUERIES_G2_ROUND*.csv'):  # generalised in round 2
            registry |= {r['search_id'] for r in ms.read_registry(path)}
        self.assertEqual(logged, registry)


if __name__ == '__main__':
    unittest.main()
