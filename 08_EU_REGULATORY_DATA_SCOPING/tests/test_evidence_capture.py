"""G1-READY tests for scripts/capture_evidence.py.

No external network is used: every request goes to a throw-away HTTP server on
127.0.0.1 that serves SYNTHETIC content. Nothing here is research evidence.
"""
import shutil
import sys
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import capture_evidence as cap  # noqa: E402

PAGE = b'<html><head><title>Synthetic page</title></head><body>synthetic \xc3\xa7 body</body></html>'


class _Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def do_GET(self):
        if self.path == '/page':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Last-Modified', 'Mon, 05 Jan 2026 10:00:00 GMT')
            self.send_header('Content-Length', str(len(PAGE)))
            self.end_headers()
            self.wfile.write(PAGE)
        elif self.path == '/moved':
            self.send_response(302)
            self.send_header('Location', '/page')
            self.end_headers()
        elif self.path == '/private':
            self.send_response(401)
            self.send_header('WWW-Authenticate', 'Basic realm="synthetic"')
            self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()


class CaptureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(('127.0.0.1', 0), _Handler)
        cls.base = f'http://127.0.0.1:{cls.server.server_address[1]}'
        threading.Thread(target=cls.server.serve_forever, daemon=True).start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def setUp(self):
        self.out = Path(tempfile.mkdtemp(prefix='g1ready_synthetic_'))

    def tearDown(self):
        shutil.rmtree(self.out, ignore_errors=True)

    def test_body_is_stored_byte_for_byte_with_its_hash(self):
        rec = cap.capture(self.base + '/page', 'SYN01', out_dir=self.out, pause=0)
        self.assertEqual(rec['outcome'], 'CAPTURED')
        stored = (self.out / rec['raw_file']).read_bytes()
        self.assertEqual(stored, PAGE)
        self.assertEqual(rec['sha256'], cap.sha256_bytes(PAGE))
        self.assertEqual(rec['bytes'], len(PAGE))
        self.assertEqual(rec['content_type'], 'text/html')
        self.assertEqual(rec['last_modified'], 'Mon, 05 Jan 2026 10:00:00 GMT')
        self.assertTrue(rec['captured_at_utc'].endswith('+00:00'))
        self.assertTrue(rec['raw_file'].startswith('SYN01/'))

    def test_original_and_final_url_and_redirect_chain(self):
        rec = cap.capture(self.base + '/moved', 'SYN01', out_dir=self.out, pause=0)
        self.assertEqual(rec['original_url'], self.base + '/moved')
        self.assertEqual(rec['final_url'], self.base + '/page')
        self.assertEqual(len(rec['redirect_chain']), 1)
        self.assertEqual(rec['redirect_chain'][0]['status'], 302)

    def test_failure_is_logged_with_every_attempt_and_no_file(self):
        rec = cap.capture(self.base + '/missing', 'SYN02', out_dir=self.out, max_attempts=3, pause=0)
        self.assertEqual(rec['outcome'], 'FAILED')
        self.assertEqual([a['outcome'] for a in rec['attempts']], ['HTTP_ERROR'] * 3)
        self.assertEqual(rec['attempts'][0]['http_status'], 404)
        self.assertIsNone(rec['raw_file'])
        self.assertIn('NOT evidence', rec['note'])
        self.assertFalse((self.out / 'SYN02').exists())
        self.assertEqual(len(cap.read_log(self.out)), 1)

    def test_authentication_required_is_recorded_as_such(self):
        rec = cap.capture(self.base + '/private', 'SYN05', out_dir=self.out, max_attempts=1, pause=0)
        self.assertEqual(rec['outcome'], 'FAILED')
        self.assertEqual(rec['attempts'][0]['http_status'], 401)
        self.assertEqual(rec['attempts'][0]['www_authenticate'], 'Basic realm="synthetic"')

    def test_network_error_is_logged(self):
        rec = cap.capture('http://127.0.0.1:9/unreachable', 'SYN03', out_dir=self.out, max_attempts=1, timeout=2, pause=0)
        self.assertEqual(rec['outcome'], 'FAILED')
        self.assertEqual(rec['attempts'][0]['outcome'], 'NETWORK_ERROR')

    def test_repeated_capture_never_overwrites(self):
        a = cap.capture(self.base + '/page', 'SYN01', out_dir=self.out, pause=0)
        b = cap.capture(self.base + '/page', 'SYN01', out_dir=self.out, pause=0)
        self.assertEqual(len(cap.read_log(self.out)), 2)
        self.assertEqual(a['sha256'], b['sha256'])
        self.assertTrue((self.out / a['raw_file']).exists() and (self.out / b['raw_file']).exists())

    def test_no_store_keeps_hash_only(self):
        rec = cap.capture(self.base + '/page', 'SYN01', out_dir=self.out, pause=0, store=False)
        self.assertEqual(rec['sha256'], cap.sha256_bytes(PAGE))
        self.assertIsNone(rec['raw_file'])
        self.assertFalse((self.out / 'SYN01').exists())

    def test_human_fields_are_left_blank(self):
        rec = cap.capture(self.base + '/page', 'SYN01', out_dir=self.out, pause=0)
        self.assertTrue(all(v == '' for v in rec['human_fields'].values()))

    def test_verify_detects_a_tampered_file(self):
        rec = cap.capture(self.base + '/page', 'SYN01', out_dir=self.out, pause=0)
        self.assertEqual(cap.verify(self.out), [])
        (self.out / rec['raw_file']).write_bytes(PAGE + b'x')
        self.assertEqual(cap.verify(self.out), [(rec['capture_id'], 'hash mismatch')])

    def test_register_a_manually_captured_file(self):
        src = self.out / 'manual.pdf'
        src.write_bytes(b'%PDF synthetic')
        rec = cap.register(src, 'https://example.org/app', 'SYN04', 'manual_browser_pdf', '2026-01-05T10:00:00+00:00', out_dir=self.out)
        self.assertEqual(rec['method'], 'manual_browser_pdf')
        self.assertEqual(rec['sha256'], cap.sha256_bytes(b'%PDF synthetic'))
        self.assertEqual(cap.verify(self.out), [])

    def test_only_http_urls(self):
        with self.assertRaises(ValueError):
            cap.capture('file:///etc/passwd', 'SYN01', out_dir=self.out)

    def test_long_lists_are_refused(self):
        pairs = [(f'SYN{i:02d}', self.base + '/page') for i in range(cap.MAX_LIST + 1)]
        with self.assertRaises(ValueError):
            cap.capture_list(pairs, out_dir=self.out, pause=0)
        self.assertEqual(cap.read_log(self.out), [])


if __name__ == '__main__':
    unittest.main()
