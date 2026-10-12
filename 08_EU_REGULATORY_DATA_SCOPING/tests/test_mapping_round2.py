"""Tests of the round-2 instruments of the G2 mapping (verification, inspection, levels, sweep, prior art).

Synthetic tests show that the tools behave as specified. They say nothing about the coverage of
the mapping and nothing about the scientific agreement of the classifications. No test uses the network.
"""
import copy
import csv
import hashlib
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
import institutional_sweep as sweep  # noqa: E402
import mapping_search as ms  # noqa: E402
import validate_mapping as vm  # noqa: E402
import verify_resources as vr  # noqa: E402

DATA = ROOT / 'mapping' / 'data'
VOCAB = json.loads((ROOT / 'mapping' / 'schemas' / 'mapping_vocabularies.json').read_text(encoding='utf-8'))


class FakeResponse:
    def __init__(self, body, status=206, ctype='text/csv'):
        self._body, self.status, self._ctype = body, status, ctype

        class H:
            def __init__(inner):
                pass

            def get_content_type(inner):
                return ctype

            def get(inner, name, default=None):
                return {'Content-Range': f'bytes 0-{len(body) - 1}/99999'}.get(name, default)
        self.headers = H()

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def read(self, n=-1):
        return self._body if n < 0 else self._body[:n]

    def geturl(self):
        return 'https://example.org/final'


class SearchExtensionTest(unittest.TestCase):
    def test_catalogue_restricted_url_and_paging(self):
        url = ms.build_url('DEUC', '', 'echa')
        self.assertIn('%22echa%22', url)
        self.assertTrue(ms.build_url('DEU', 'x', page=2).endswith('&page=2'))
        self.assertTrue(ms.build_url('DVN', 'x', page=1).endswith('&start=25'))
        self.assertTrue(ms.build_url('ZEN', 'x', page=1).endswith('&page=2'))
        with self.assertRaises(ValueError):
            ms.build_url('HF', 'x', page=1)

    def test_round1_urls_are_unchanged_by_the_extension(self):
        self.assertEqual(ms.build_url('GH', 'eurlex dataset'), 'https://api.github.com/search/repositories?q=eurlex%20dataset&per_page=25')

    def test_new_parsers(self):
        total, hits = ms.parse_hits('DCAT', {'result': {'count': 2, 'results': [
            {'id': 'echa', 'title': {'en': 'ECHA'}, 'publisher': {'name': {'en': 'European Chemicals Agency'}}, 'country': {'id': 'EUROPE'}}]}})
        self.assertEqual((total, hits[0]['platform_record_id'], hits[0]['creator_or_publisher']), (2, 'echa', 'European Chemicals Agency [EUROPE]'))
        total, hits = ms.parse_hits('B2F', {'result': {'count': 1, 'results': [{'name': 'abc', 'title': 'T', 'organization': {'title': 'CESSDA'}, 'metadata_created': '2025-01-01'}]}})
        self.assertEqual((hits[0]['platform_record_id'], hits[0]['creator_or_publisher'], hits[0]['year']), ('abc', 'CESSDA', '2025'))
        total, hits = ms.parse_hits('DNS', {'data': {'total_count': 1, 'items': [{'global_id': 'doi:1', 'name': 'N', 'url': 'u'}]}})
        self.assertEqual(hits[0]['platform_record_id'], 'doi:1')

    def test_paged_rank_continues(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            reg = tmp / 'q.csv'
            reg.write_text('search_id,family,resource_set,platform,query,language,rationale,param,page,depth_rationale\n'
                           'SR-T-001,f,A,GH,x,en,r,,1,second page\n', encoding='utf-8')
            body = json.dumps({'total_count': 1, 'items': [{'full_name': 'o/r', 'html_url': 'u'}]}).encode()
            ms.run(reg, search_dir=tmp / 's', pause=0, fetch=lambda url: (body, 200))
            rows = ms.build_hits(tmp / 's')
            self.assertEqual(rows[0]['rank'], '26')
            self.assertEqual(ms.read_log(tmp / 's')[0]['depth_rationale'], 'second page')


class VerificationToolTest(unittest.TestCase):
    def test_classify_known_repositories(self):
        cases = {'https://doi.org/10.5281/zenodo.1442401': ('zenodo', '1442401'),
                 'https://zenodo.org/records/5363165': ('zenodo', '5363165'),
                 'https://doi.org/10.7910/DVN/1GFLRM': ('dataverse', 'doi:10.7910/DVN/1GFLRM'),
                 'https://huggingface.co/datasets/coastalcph/lex_glue': ('hf', 'coastalcph/lex_glue'),
                 'https://github.com/parltrack/parltrack': ('github', 'parltrack/parltrack'),
                 'https://data.europa.eu/data/datasets/eu-case-law': ('deu', 'eu-case-law'),
                 'https://doi.org/10.1177/14651165231202034': ('doi', '10.1177/14651165231202034'),
                 'https://openalex.org/W4387022400': ('openalex', 'W4387022400'),
                 'https://example.org/page': (None, None)}
        for url, expected in cases.items():
            self.assertEqual(vr.classify(url), expected, url)

    def test_record_urls_are_apis_of_the_repository(self):
        self.assertEqual(vr.record_url('zenodo', '1'), 'https://zenodo.org/api/records/1')
        self.assertIn('/api/datasets/:persistentId/', vr.record_url('dataverse', 'doi:10.7910/DVN/X'))

    def test_peek_reads_at_most_n_bytes_and_logs_hash(self):
        body = b'celex,date,country\n32016R0679,2016-04-27,EU\n' + b'x' * 20000
        with tempfile.TemporaryDirectory() as tmp:
            rec = vr.peek('https://example.org/data.csv', 'MR-9999', n=4096, out_dir=tmp, opener=lambda req, timeout=0: FakeResponse(body))
            self.assertEqual(rec['bytes_read'], 4096)
            stored = (Path(tmp) / rec['stored_file']).read_bytes()
            self.assertEqual(stored, body[:4096])
            self.assertEqual(rec['sha256'], hashlib.sha256(body[:4096]).hexdigest())
            self.assertEqual(len(vr.read_inspections(tmp)), 1)

    def test_peek_has_a_hard_ceiling_and_http_only(self):
        with tempfile.TemporaryDirectory() as tmp:
            rec = vr.peek('https://example.org/x', 'MR-9999', n=10 ** 9, out_dir=tmp, opener=lambda req, timeout=0: FakeResponse(b'a' * 100000))
            self.assertLessEqual(rec['bytes_read'], vr.MAX_PEEK_BYTES)
            with self.assertRaises(ValueError):
                vr.peek('file:///etc/passwd', 'MR-9999', out_dir=tmp)

    def test_failed_peek_is_logged_not_raised(self):
        from urllib.error import HTTPError

        def boom(req, timeout=0):
            raise HTTPError('https://example.org/x', 401, 'Unauthorized', {}, None)
        with tempfile.TemporaryDirectory() as tmp:
            rec = vr.peek('https://example.org/x', 'MR-9999', out_dir=tmp, opener=boom)
            self.assertEqual((rec['outcome'], rec['http_status'], rec['bytes_read']), ('HTTP_ERROR', 401, 0))
            self.assertEqual(vr.observe(rec, root=tmp)['availability'], 'ACCESS_FAILED')

    def _observe(self, body, ctype, url='https://example.org/f'):
        with tempfile.TemporaryDirectory() as tmp:
            rec = vr.peek(url, 'MR-9999', out_dir=tmp, opener=lambda req, timeout=0: FakeResponse(body, ctype=ctype))
            return vr.observe(rec, root=tmp)

    def test_observation_distinguishes_data_pages_and_documents(self):
        csv_obs = self._observe(b'celex;date;member_state\n1;2;3\n', 'text/csv')
        self.assertEqual((csv_obs['content_kind'], csv_obs['availability']), ('TABULAR', 'DATA_AVAILABILITY_VERIFIED'))
        self.assertEqual(csv_obs['fields'], ['celex', 'date', 'member_state'])
        self.assertEqual(self._observe(b'<!DOCTYPE html><html><body>x</body></html>', 'text/html')['availability'], 'LANDING_PAGE_ONLY')
        self.assertEqual(self._observe(b'%PDF-1.5 ...', 'application/pdf')['availability'], 'DOCUMENT_ONLY')
        self.assertEqual(self._observe(b'PK\x03\x04....', 'application/zip')['content_kind'], 'ARCHIVE')
        json_obs = self._observe(b'{"id": "x", "decision": "y", "country": "z"}', 'application/json')
        self.assertEqual(json_obs['content_kind'], 'JSON')
        self.assertIn('decision', json_obs['fields'])
        self.assertEqual(self._observe(b'PAR1\x00\x00', 'application/octet-stream')['content_kind'], 'PARQUET')
        listing = self._observe(b'[{"name": "data.csv"}]', 'application/json', url='https://api.github.com/repos/o/r/contents')
        self.assertEqual(listing['availability'], 'LISTING_ONLY')

    def test_capabilities_are_name_matches_only(self):
        found = vr.capabilities(['CELEX', 'Date of decision', 'Member State', 'text'])
        self.assertIn('FIELD_CELEX', found)
        self.assertIn('FIELD_DECISION_OR_SANCTION', found)
        self.assertIn('FIELD_COUNTRY_OR_MEMBER_STATE', found)
        self.assertNotIn('FIELD_ECLI', found)
        self.assertEqual(vr.capabilities(['text', 'labels']), {})

    def test_fetch_retries_with_second_registration_agency_on_404(self):
        calls = []

        def fake_capture(url, rid, **kw):
            calls.append(url)
            failed = 'datacite' in url
            return {'record_id': rid, 'outcome': 'FAILED' if failed else 'CAPTURED', 'attempts': [{'http_status': 404 if failed else 200}]}
        out = vr.fetch([('MR-1', 'https://api.datacite.org/dois/x', 'https://api.crossref.org/works/x')], pause=0, capture=fake_capture)
        self.assertEqual(len(out), 2)
        self.assertEqual(calls[1], 'https://api.crossref.org/works/x')

    def test_digest_of_a_zenodo_record(self):
        record = {'metadata': {'title': 'T', 'creators': [{'name': 'A'}], 'publication_date': '2020-01-01', 'license': {'id': 'cc-by-4.0'},
                               'resource_type': {'type': 'dataset'}, 'description': '<p>Some <b>text</b></p>'},
                  'files': [{'key': 'a.csv', 'size': 10, 'checksum': 'md5:1', 'links': {'self': 'https://zenodo.org/f'}}]}
        d = vr.digest('zenodo', record)
        self.assertEqual((d['title'], d['license'], d['n_files'], d['description']), ('T', 'cc-by-4.0', 1, 'Some text'))


class SweepToolTest(unittest.TestCase):
    def test_sweep_captures_each_row_once(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            reg = tmp / 's.csv'
            reg.write_text('sweep_id,step,body,body_type,url,purpose,found_resources,result_note\n'
                           'SW-T1,1,B,AGENCY,https://example.org/a,p,,\nSW-T2,1,C,AGENCY,https://example.org/b,p,,\n', encoding='utf-8')
            seen = []

            def fake(url, rid, **kw):
                seen.append((rid, url))
                Path(kw['out_dir']).mkdir(parents=True, exist_ok=True)
                with (Path(kw['out_dir']) / 'CAPTURE_LOG.jsonl').open('a', encoding='utf-8') as fh:
                    fh.write(json.dumps({'record_id': rid}) + '\n')
                return {'record_id': rid, 'outcome': 'CAPTURED'}
            sweep.run(reg, out_dir=tmp / 'c', pause=0, capture=fake)
            sweep.run(reg, out_dir=tmp / 'c', pause=0, capture=fake)  # second run: nothing left to do
            self.assertEqual([r for r, _ in seen], ['SW-T1', 'SW-T2'])


class LevelRulesTest(unittest.TestCase):
    def row(self, **kw):
        base = {'verified_name': 'N', 'maintainer': 'M', 'description_url': 'https://e.org',
                'field_basis': 'verified_name:API_METADATA; maintainer:PRIMARY_PAGE'}
        base.update(kw)
        return base

    def test_identity_levels(self):
        self.assertEqual(bmb.derive_levels(self.row(), ['EVC-1'], [], [])[0], 'IDENTITY_VERIFIED')
        self.assertEqual(bmb.derive_levels(self.row(field_basis='verified_name:API_METADATA; maintainer:AGENT_INFERENCE'), ['EVC-1'], [], [])[0], 'IDENTITY_PARTIAL')
        self.assertEqual(bmb.derive_levels(self.row(maintainer='NOT_ASSESSED'), ['EVC-1'], [], [])[0], 'IDENTITY_PARTIAL')
        self.assertEqual(bmb.derive_levels(self.row(), [], [], [])[0], 'NOT_VERIFIED')

    def test_seed_values_never_reach_identity_verified(self):
        row = self.row(field_basis='verified_name:SEED_UNVERIFIED; maintainer:PRIMARY_PAGE')
        self.assertEqual(bmb.derive_levels(row, ['EVC-1'], [], [])[0], 'IDENTITY_PARTIAL')

    def test_availability_comes_only_from_inspections(self):
        peek = lambda a: {'obs': {'availability': a}}  # noqa: E731
        self.assertEqual(bmb.derive_levels(self.row(), ['E'], [], [])[1], 'NOT_TESTED')
        self.assertEqual(bmb.derive_levels(self.row(), ['E'], [peek('LANDING_PAGE_ONLY')], [])[1], 'LANDING_PAGE_ONLY')
        self.assertEqual(bmb.derive_levels(self.row(), ['E'], [peek('LANDING_PAGE_ONLY'), peek('DATA_AVAILABILITY_VERIFIED')], [])[1], 'DATA_AVAILABILITY_VERIFIED')
        self.assertEqual(bmb.derive_levels(self.row(), ['E'], [peek('ACCESS_FAILED')], [])[1], 'ACCESS_FAILED')

    def test_capability_needs_an_observed_capability(self):
        self.assertEqual(bmb.derive_levels(self.row(), ['E'], [], [])[2], 'NOT_ASSESSED')
        self.assertEqual(bmb.derive_levels(self.row(), ['E'], [], ['SCHEMA_FIELDS_OBSERVED'])[2], 'CAPABILITY_VERIFIED')

    def test_resource_level_follows_category(self):
        self.assertEqual(bmb.resource_level('DATASET'), 'LEVEL_I_DATA')
        self.assertEqual(bmb.resource_level('ADMINISTRATIVE_REGISTER'), 'LEVEL_I_DATA')
        self.assertEqual(bmb.resource_level('CATALOGUE'), 'LEVEL_II_INFRASTRUCTURE')
        self.assertEqual(bmb.resource_level('SOFTWARE_OR_PIPELINE'), 'LEVEL_II_INFRASTRUCTURE')
        self.assertEqual(bmb.resource_level('DATA_DISTRIBUTION'), 'DISTRIBUTION_OF_LEVEL_I')
        self.assertEqual(bmb.resource_level('INDETERMINATE'), 'UNASSIGNED')


class MergeTest(unittest.TestCase):
    def test_rounds_merge_in_order_and_patch_by_number(self):
        cur = bmb.load_curation()
        self.assertEqual(cur.ROUNDS, ['G2-R1', 'G2-R2'])
        numbers = [r['n'] for r in cur.RESOURCES]
        self.assertEqual(numbers, sorted(numbers))
        self.assertEqual(len(numbers), len(set(numbers)))
        self.assertEqual(numbers[:41], list(range(1, 42)))
        by_n = {r['n']: r for r in cur.RESOURCES}
        self.assertEqual(by_n[55]['status'], 'VERIFIED')            # patched in round 2
        self.assertEqual(by_n[55]['first_round'], 'G2-R1')
        self.assertEqual(by_n[106]['first_round'], 'G2-R2')

    def test_every_status_change_has_a_history_row_and_reason(self):
        tables = bmb.build()
        changed = {p['n'] for p in bmb.load_curation().PATCH_LOG if 'status' in p['changes']}
        hist = {h['resource_id'] for h in tables['verification_history'][1]}
        self.assertEqual({f'MR-{n:04d}' for n in changed}, hist)
        self.assertTrue(all(h['reason'] for h in tables['verification_history'][1]))

    def test_round1_tables_in_the_snapshot_were_not_rewritten(self):
        snap = ROOT / 'mapping' / 'snapshots' / 'round1'
        for name in ('resources', 'access_endpoints', 'resource_relations', 'discovery_log', 'decisions_log', 'seed_audit'):
            self.assertTrue((snap / f'{name}.csv').exists())
        rows = list(csv.DictReader((snap / 'resources.csv').open(encoding='utf-8')))
        self.assertEqual(len(rows), 105)
        live = {r['resource_id']: r for r in csv.DictReader((DATA / 'resources.csv').open(encoding='utf-8'))}
        for r in rows:  # round-1 identifiers and registered names survive; only evidence-driven fields move
            self.assertIn(r['resource_id'], live)
            self.assertEqual(live[r['resource_id']]['registered_name'], r['registered_name'])
            self.assertEqual(live[r['resource_id']]['seed_id'], r['seed_id'])
            self.assertEqual(live[r['resource_id']]['first_round'], 'G2-R1')


class ValidatorRound2Test(unittest.TestCase):
    def setUp(self):
        self.tables = vm.load()
        self.shared = set(bmb.load_curation().SHARED_URL_JUSTIFICATIONS)

    def errors(self, tables, check):
        return [m for s, c, m in vm.validate(tables, VOCAB, shared_urls=self.shared, check_files=False) if s == 'ERROR' and c == check]

    def test_data_availability_requires_an_inspection(self):
        t = copy.deepcopy(self.tables)
        target = next(r for r in t['resources'] if r['data_availability_level'] == 'NOT_TESTED')
        target['data_availability_level'] = 'DATA_AVAILABILITY_VERIFIED'
        self.assertTrue(self.errors(t, 'levels'))

    def test_capability_requires_an_observation(self):
        t = copy.deepcopy(self.tables)
        target = next(r for r in t['resources'] if r['capability_level'] == 'NOT_ASSESSED')
        target['capability_level'] = 'CAPABILITY_VERIFIED'
        self.assertTrue(self.errors(t, 'levels'))

    def test_distribution_cannot_be_individuated(self):
        t = copy.deepcopy(self.tables)
        target = next(r for r in t['resources'] if r['resource_category'] == 'DATA_DISTRIBUTION')
        target['individuation_status'] = 'INDIVIDUATED'
        self.assertTrue(self.errors(t, 'inclusion'))

    def test_level_follows_category(self):
        t = copy.deepcopy(self.tables)
        target = next(r for r in t['resources'] if r['resource_category'] == 'DATASET')
        target['resource_level'] = 'LEVEL_II_INFRASTRUCTURE'
        self.assertTrue(self.errors(t, 'levels'))

    def test_prior_art_match_needs_a_resource_and_basis(self):
        t = copy.deepcopy(self.tables)
        target = next(x for x in t['lynx_reference'] if x['match_status'] == 'MATCHED')
        target['matched_resource_id'] = ''
        self.assertTrue(self.errors(t, 'evidence'))

    def test_sweep_cannot_credit_a_failed_request(self):
        t = copy.deepcopy(self.tables)
        target = next(x for x in t['institutional_sweep'] if x['outcome'] == 'FAILED')
        target['found_resources'] = 'MR-0001'
        self.assertTrue(self.errors(t, 'evidence'))


class RealRound2BaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tables = vm.load()
        cls.res = {r['resource_id']: r for r in cls.tables['resources']}

    def test_no_validation_error_including_file_hashes(self):
        shared = set(bmb.load_curation().SHARED_URL_JUSTIFICATIONS)
        findings = vm.validate(self.tables, VOCAB, shared_urls=shared)
        self.assertEqual([f for f in findings if f[0] == 'ERROR'], [])

    def test_inspection_files_respect_the_byte_ceiling(self):
        base = ROOT / 'mapping' / 'evidence' / 'inspections'
        for rec in vr.read_inspections(base):
            self.assertLessEqual(rec['bytes_read'], vr.MAX_PEEK_BYTES)
            self.assertLessEqual(rec['requested_bytes'], vr.MAX_PEEK_BYTES)
            if rec.get('stored_file'):
                self.assertEqual(hashlib.sha256((base / rec['stored_file']).read_bytes()).hexdigest(), rec['sha256'])

    def test_no_authentication_was_attempted(self):
        for rec in vr.read_inspections(ROOT / 'mapping' / 'evidence' / 'inspections'):
            self.assertNotIn('datadump.publications.europa.eu', rec['url'])

    def test_eu03_eu07_distinction_survives_round_2(self):
        dump, elds = self.res['MR-0003'], self.res['MR-0007']
        self.assertEqual(dump['description_url'], 'https://data.europa.eu/en/ELDS')
        self.assertEqual(dump['primary_access_url'], 'https://datadump.publications.europa.eu/')
        self.assertEqual(elds['seed_id'], 'EU07')
        self.assertFalse([r for r in self.tables['resource_relations'] if r['relation_type'] == 'same_resource_as'])
        self.assertEqual(dump['data_availability_level'], 'NOT_TESTED')  # authentication required: never attempted

    def test_failed_access_is_never_an_exclusion(self):
        for r in self.res.values():
            if r['data_availability_level'] == 'ACCESS_FAILED' or r['verification_status'] == 'INACCESSIBLE':
                self.assertNotEqual(r['eligibility_preliminary'], 'EXCLUDE')

    def test_every_resource_has_a_level_and_all_agent_rows_are_provisional(self):
        for r in self.res.values():
            self.assertIn(r['resource_level'], VOCAB['resource_level'])
            self.assertEqual((r['classification_basis'], r['researcher_confirmed']), ('AGENT_PROVISIONAL', 'NO'))

    def test_round1_evidence_rows_survive_unchanged(self):
        snap = {e['evidence_id']: e for e in csv.DictReader((ROOT / 'mapping' / 'snapshots' / 'round1' / 'evidence_registry.csv').open(encoding='utf-8'))}
        live = {e['evidence_id']: e for e in self.tables['evidence_registry']}
        self.assertGreater(len(snap), 100)
        for eid, row in snap.items():
            self.assertIn(eid, live)
            for col in ('url', 'accessed_at_utc', 'outcome', 'sha256', 'stored_file'):
                self.assertEqual(live[eid][col], row[col], f'{eid}.{col}')

    def test_round1_decisions_and_relations_are_a_prefix_of_the_live_tables(self):
        snap = ROOT / 'mapping' / 'snapshots' / 'round1'
        for name, key in (('decisions_log', 'decision_id'), ('resource_relations', 'relation_id')):
            old = list(csv.DictReader((snap / f'{name}.csv').open(encoding='utf-8')))
            new = {r[key]: r for r in self.tables[name]}
            for row in old:
                self.assertEqual(new[row[key]]['decision' if name == 'decisions_log' else 'justification'],
                                 row['decision' if name == 'decisions_log' else 'justification'])

    def test_validation_sample_is_deterministic_and_proportionate(self):
        import validation_sample as vs
        res = list(csv.DictReader((DATA / 'resources.csv').open(encoding='utf-8')))
        rel = list(csv.DictReader((DATA / 'resource_relations.csv').open(encoding='utf-8')))
        a, b = vs.draw(res, rel), vs.draw(res, rel)
        self.assertEqual(a, b)
        ids = [(x['unit'], x['id']) for x in a]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue(all(x['agent_classification_hidden_from_reviewer'] == 'YES' for x in a))
        self.assertLess(len(ids), len(res))

    def test_prior_art_list_covers_the_published_table(self):
        rows = self.tables['lynx_reference']
        self.assertEqual(len(rows), 56)
        self.assertEqual(sum(1 for r in rows if r['match_status'] in ('MATCHED', 'MATCHED_AS_ENDPOINT')), 3)

    def test_all_requested_searches_of_round_two_are_logged(self):
        logged = {d['search_id'] for d in self.tables['discovery_log'] if d['entry_type'] == 'SEARCH_RUN'}
        registry = set()
        for path in (ROOT / 'mapping' / 'protocol').glob('SEARCH_QUERIES_G2_ROUND*.csv'):
            registry |= {r['search_id'] for r in ms.read_registry(path)}
        self.assertEqual(logged, registry)


if __name__ == '__main__':
    unittest.main()
