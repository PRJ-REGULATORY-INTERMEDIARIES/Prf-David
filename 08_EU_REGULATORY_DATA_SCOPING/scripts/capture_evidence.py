#!/usr/bin/env python3
"""Evidence capture for the Pilot A packets: one URL per call, faithful and logged.

What it does
    capture    one GET of one URL; stores the response body byte for byte, its
               SHA-256 and a metadata record (original and final URL, redirect
               chain, UTC time, status, content type, validators, every attempt)
    register   records a file captured by other means (e.g. a browser "save as
               PDF" of a page that only renders with JavaScript)
    verify     recomputes the SHA-256 of every stored file against the log

What it never does
    * follow links, crawl, paginate or download anything the caller did not name;
    * extract, summarise or highlight content (that could steer a classification);
    * overwrite an earlier capture;
    * treat a failed request as evidence that a resource does not exist.

Standard library only. Network access happens only in `capture`.
"""
import argparse
import hashlib
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / 'pilot_a' / 'evidence'
LOG_NAME = 'CAPTURE_LOG.jsonl'
USER_AGENT = 'EU-Regulatory-Data-Scoping/evidence-capture (academic research; single page per request)'
EXTENSIONS = {'text/html': 'html', 'application/xhtml+xml': 'xhtml', 'application/pdf': 'pdf',
              'application/json': 'json', 'text/plain': 'txt', 'text/csv': 'csv',
              'application/xml': 'xml', 'text/xml': 'xml'}
MAX_LIST = 25  # hard ceiling for one invocation of `capture-list`; this is not a harvester


def utc_now():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


class _RecordRedirects(HTTPRedirectHandler):
    def __init__(self):
        self.chain = []

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        self.chain.append({'status': code, 'from': req.full_url, 'to': newurl})
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def _append(out_dir, record):
    out_dir.mkdir(parents=True, exist_ok=True)
    with (out_dir / LOG_NAME).open('a', encoding='utf-8', newline='\n') as handle:
        handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + '\n')


def read_log(out_dir=DEFAULT_OUT):
    path = Path(out_dir) / LOG_NAME
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding='utf-8').splitlines() if line.strip()]


def _blank_human_fields():
    """Fields only a person can fill, after reading the source. Never inferred."""
    return {'resource_version_or_update_date': '', 'reuse_terms_url': '', 'reuse_terms_note': '',
            'access_conditions': '', 'filled_by': '', 'filled_at': ''}


def capture(url, record_id, out_dir=DEFAULT_OUT, purpose='', max_attempts=2, timeout=30, pause=3.0, store=True):
    """GET one URL once (with at most `max_attempts` tries) and log the outcome."""
    if urlsplit(url).scheme not in ('http', 'https'):
        raise ValueError(f'only http(s) URLs can be captured: {url!r}')
    out_dir = Path(out_dir)
    attempts, body, meta = [], None, {}
    for n in range(1, max_attempts + 1):
        redirects = _RecordRedirects()
        opener = build_opener(redirects)
        started = utc_now()
        try:
            req = Request(url, headers={'User-Agent': USER_AGENT, 'Accept': '*/*'})
            with opener.open(req, timeout=timeout) as resp:
                body = resp.read()
                meta = {'final_url': resp.geturl(), 'http_status': resp.status,
                        'content_type': resp.headers.get_content_type(),
                        'charset': resp.headers.get_content_charset(),
                        'content_length_header': resp.headers.get('Content-Length'),
                        'last_modified': resp.headers.get('Last-Modified'),
                        'etag': resp.headers.get('ETag'),
                        'content_language': resp.headers.get('Content-Language'),
                        'server_date': resp.headers.get('Date'),
                        'redirect_chain': redirects.chain}
            attempts.append({'n': n, 'started_utc': started, 'outcome': 'OK', 'http_status': meta['http_status']})
            break
        except HTTPError as ex:
            attempts.append({'n': n, 'started_utc': started, 'outcome': 'HTTP_ERROR', 'http_status': ex.code, 'error': str(ex.reason),
                             'www_authenticate': ex.headers.get('WWW-Authenticate') if ex.headers else None,
                             'location': ex.headers.get('Location') if ex.headers else None})
            ex.close()
        except (URLError, TimeoutError, OSError) as ex:
            attempts.append({'n': n, 'started_utc': started, 'outcome': 'NETWORK_ERROR', 'error': f'{type(ex).__name__}: {ex}'})
        if n < max_attempts:
            time.sleep(pause)
    captured_at = utc_now()
    record = {'capture_id': '', 'record_id': record_id, 'method': 'http_get', 'purpose': purpose,
              'original_url': url, 'captured_at_utc': captured_at, 'attempts': attempts,
              'tool': 'scripts/capture_evidence.py', 'tool_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'user_agent': USER_AGENT, 'human_fields': _blank_human_fields()}
    if body is None:
        record.update({'outcome': 'FAILED', 'raw_file': None, 'sha256': None, 'bytes': None,
                       'note': 'Access failure. This is NOT evidence that the resource does not exist.'})
        record['capture_id'] = f'{record_id}_{captured_at.replace(":", "").replace("-", "")[:15]}_FAILED'
        _append(out_dir, record)
        return record
    digest = sha256_bytes(body)
    record.update(meta)
    record.update({'outcome': 'CAPTURED', 'sha256': digest, 'bytes': len(body)})
    stamp = captured_at.replace(':', '').replace('-', '')[:15]
    record['capture_id'] = f'{record_id}_{stamp}_{digest[:12]}'
    if store:
        ext = EXTENSIONS.get(meta['content_type'], 'bin')
        folder = out_dir / record_id
        folder.mkdir(parents=True, exist_ok=True)
        dest = folder / f'{stamp}_{digest[:12]}.{ext}'
        k = 1
        while dest.exists():  # never overwrite an earlier capture
            k += 1
            dest = folder / f'{stamp}_{digest[:12]}_{k}.{ext}'
        dest.write_bytes(body)
        record['raw_file'] = dest.relative_to(out_dir).as_posix()
    else:
        record['raw_file'] = None
        record['note'] = 'Body not stored (store=False): hash and metadata only.'
    _append(out_dir, record)
    return record


def register(file_path, url, record_id, method, captured_at_utc, out_dir=DEFAULT_OUT, purpose='', note=''):
    """Log a file captured outside this tool (browser PDF, archived copy, export)."""
    out_dir, src = Path(out_dir), Path(file_path)
    data = src.read_bytes()
    digest = sha256_bytes(data)
    if not re.match(r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}', captured_at_utc):
        raise ValueError('captured_at_utc must be an ISO 8601 UTC timestamp')
    folder = out_dir / record_id
    folder.mkdir(parents=True, exist_ok=True)
    stamp = re.sub(r'[^0-9T]', '', captured_at_utc)[:15]
    dest = folder / f'{stamp}_{digest[:12]}{src.suffix.lower()}'
    if not dest.exists():
        dest.write_bytes(data)
    record = {'capture_id': f'{record_id}_{stamp}_{digest[:12]}', 'record_id': record_id, 'method': method,
              'purpose': purpose, 'original_url': url, 'final_url': url, 'captured_at_utc': captured_at_utc,
              'registered_at_utc': utc_now(), 'outcome': 'CAPTURED', 'sha256': digest, 'bytes': len(data),
              'raw_file': dest.relative_to(out_dir).as_posix(), 'attempts': [], 'note': note,
              'tool': 'scripts/capture_evidence.py', 'human_fields': _blank_human_fields()}
    _append(out_dir, record)
    return record


def verify(out_dir=DEFAULT_OUT):
    """Return a list of (capture_id, problem). Empty list = every stored file matches its hash."""
    out_dir, problems = Path(out_dir), []
    for rec in read_log(out_dir):
        if rec.get('outcome') != 'CAPTURED' or not rec.get('raw_file'):
            continue
        path = out_dir / rec['raw_file']
        if not path.exists():
            problems.append((rec['capture_id'], 'file missing'))
        elif sha256_bytes(path.read_bytes()) != rec['sha256']:
            problems.append((rec['capture_id'], 'hash mismatch'))
    return problems


def capture_list(pairs, out_dir=DEFAULT_OUT, purpose='', pause=5.0, limit=MAX_LIST, **kw):
    """Capture a short, explicit list of (record_id, url). Refuses long lists."""
    pairs = list(pairs)
    if len(pairs) > min(limit, MAX_LIST):
        raise ValueError(f'{len(pairs)} URLs requested; the ceiling is {min(limit, MAX_LIST)} per invocation')
    results = []
    for i, (record_id, url) in enumerate(pairs):
        if i:
            time.sleep(pause)
        results.append(capture(url, record_id, out_dir=out_dir, purpose=purpose, **kw))
    return results


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='command', required=True)
    c = sub.add_parser('capture')
    c.add_argument('--url', required=True)
    c.add_argument('--record-id', required=True)
    c.add_argument('--purpose', default='')
    c.add_argument('--out', default=str(DEFAULT_OUT))
    c.add_argument('--no-store', action='store_true', help='keep hash and metadata only (use when terms forbid a copy)')
    r = sub.add_parser('register')
    for name in ('--file', '--url', '--record-id', '--method', '--captured-at-utc'):
        r.add_argument(name, required=True)
    r.add_argument('--out', default=str(DEFAULT_OUT))
    r.add_argument('--note', default='')
    v = sub.add_parser('verify')
    v.add_argument('--out', default=str(DEFAULT_OUT))
    args = ap.parse_args()
    if args.command == 'capture':
        rec = capture(args.url, args.record_id, out_dir=args.out, purpose=args.purpose, store=not args.no_store)
        print(json.dumps({k: rec.get(k) for k in ('capture_id', 'outcome', 'original_url', 'final_url', 'http_status', 'content_type', 'bytes', 'sha256', 'last_modified', 'raw_file', 'attempts')}, indent=2, ensure_ascii=False))
        return 0 if rec['outcome'] == 'CAPTURED' else 2
    if args.command == 'register':
        rec = register(args.file, args.url, args.record_id, args.method, args.captured_at_utc, out_dir=args.out, note=args.note)
        print(json.dumps({k: rec[k] for k in ('capture_id', 'sha256', 'bytes', 'raw_file')}, indent=2))
        return 0
    problems = verify(args.out)
    for cid, problem in problems:
        print(f'[ERROR] {cid}: {problem}')
    print(f'{len(read_log(args.out))} log entries; {len(problems)} problem(s)')
    return 2 if problems else 0


if __name__ == '__main__':
    raise SystemExit(main())
