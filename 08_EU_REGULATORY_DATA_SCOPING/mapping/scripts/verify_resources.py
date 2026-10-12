#!/usr/bin/env python3
"""Round-2 verification of discovered resources: repository records and minimal data inspection.

fetch   one GET per resource to the public record API of its repository (Zenodo, Dataverse,
        Hugging Face, GitHub, DataCite/Crossref, data.europa.eu); the JSON response is
        preserved with its SHA-256 by scripts/capture_evidence.py and filed under the
        resource identifier
digest  compact, deterministic summary of every stored record (title, creators, licence,
        version, files with size and checksum), for the person curating
peek    reads at most N bytes (default 4 KiB) from ONE data file or API endpoint per resource
        with an HTTP Range request, stores exactly those bytes with a hash and logs them.
        It never reads a whole file and never follows links.

What it does not do: authenticate, crawl, download corpora, or interpret content. A peek
shows that bytes can be retrieved from an address and what the first bytes look like.
Standard library only; network access happens in `fetch` and `peek` only.
"""
import argparse
import csv
import hashlib
import json
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, unquote, urlsplit
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[2]
MAPPING = ROOT / 'mapping'
CAPTURE_DIR = MAPPING / 'evidence' / 'captures'
INSPECT_DIR = MAPPING / 'evidence' / 'inspections'
LOG_NAME = 'INSPECTION_LOG.jsonl'
USER_AGENT = 'EU-Regulatory-Data-Scoping/mapping-verification (academic research; single record or first bytes per resource)'
DEFAULT_PEEK_BYTES = 4096
MAX_PEEK_BYTES = 16384  # hard ceiling; this is not a downloader

sys.path.insert(0, str(ROOT / 'scripts'))
import capture_evidence  # noqa: E402


def utc_now():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


# --------------------------------------------------------------------------- record URLs
def classify(url):
    """Return (kind, key) for a URL whose repository has a public record API, else (None, None)."""
    u = url.strip()
    m = re.match(r'https?://(?:dx\.)?doi\.org/10\.5281/zenodo\.(\d+)', u, re.I) or re.match(r'https?://zenodo\.org/records?/(\d+)', u, re.I)
    if m:
        return 'zenodo', m.group(1)
    m = re.match(r'https?://(?:dx\.)?doi\.org/(10\.7910/DVN/[A-Z0-9]+)', u, re.I)
    if m:
        return 'dataverse', 'doi:' + m.group(1).upper().replace('10.7910/DVN/', '10.7910/DVN/')
    m = re.match(r'https?://huggingface\.co/datasets/([^/\s]+/[^/\s?#]+|[^/\s?#]+)', u)
    if m:
        return 'hf', m.group(1)
    m = re.match(r'https?://github\.com/([^/\s]+/[^/\s?#]+)', u)
    if m:
        return 'github', m.group(1).removesuffix('.git')
    m = re.match(r'https?://data\.europa\.eu/data/datasets/([^/?#\s]+)', u)
    if m:
        return 'deu', m.group(1)
    m = re.match(r'https?://(?:dx\.)?doi\.org/(10\.\d{4,9}/\S+)', u, re.I)
    if m:
        return 'doi', m.group(1)
    m = re.match(r'https?://openalex\.org/(W\d+)', u)
    if m:
        return 'openalex', m.group(1)
    return None, None


def record_url(kind, key):
    return {
        'zenodo': f'https://zenodo.org/api/records/{key}',
        'dataverse': f'https://dataverse.harvard.edu/api/datasets/:persistentId/?persistentId={quote(key, safe=":/")}',
        'hf': f'https://huggingface.co/api/datasets/{key}',
        'github': f'https://api.github.com/repos/{key}',
        'deu': f'https://data.europa.eu/api/hub/search/datasets/{key}',
        'doi': f'https://api.datacite.org/dois/{quote(key.lower(), safe="/")}',
        'crossref': f'https://api.crossref.org/works/{quote(key, safe="/")}',
        'openalex': f'https://api.openalex.org/works/{key}',
    }[kind]


# --------------------------------------------------------------------------- digests
def _clean(text, n=300):
    text = re.sub(r'<[^>]+>', ' ', str(text or ''))
    return ' '.join(text.split())[:n]


def _lang(v):
    if isinstance(v, dict):
        return v.get('en') or next((x for x in v.values() if x), '')
    return v or ''


def digest(kind, data):
    """Deterministic summary of one stored record. Missing information stays None."""
    d = {'kind': kind}
    if kind == 'zenodo':
        md = data.get('metadata', {})
        d.update(title=md.get('title'), creators=[c.get('name') for c in md.get('creators', [])][:4],
                 date=md.get('publication_date'), type=(md.get('resource_type') or {}).get('type'),
                 license=(md.get('license') or {}).get('id'), version=md.get('version'), access=md.get('access_right'),
                 description=_clean(md.get('description'), 420),
                 files=[{'name': f.get('key'), 'size': f.get('size'), 'checksum': f.get('checksum'),
                         'url': (f.get('links') or {}).get('self')} for f in data.get('files', [])][:12],
                 n_files=len(data.get('files', [])), related=[r.get('identifier') for r in md.get('related_identifiers', [])][:5])
    elif kind == 'dataverse':
        dd = data.get('data', {})
        latest = dd.get('latestVersion', {})
        fields = {f.get('typeName'): f.get('value') for f in latest.get('metadataBlocks', {}).get('citation', {}).get('fields', [])}
        desc = fields.get('dsDescription')
        d.update(title=fields.get('title'), creators=[a.get('authorName', {}).get('value') for a in (fields.get('author') or [])][:4],
                 date=latest.get('releaseTime') or dd.get('publicationDate'), version=f"{latest.get('versionNumber')}.{latest.get('versionMinorNumber')}",
                 license=(latest.get('license') or {}).get('name') if isinstance(latest.get('license'), dict) else latest.get('license'),
                 terms=_clean(latest.get('termsOfUse'), 160), access=latest.get('fileAccessRequest'),
                 description=_clean((desc or [{}])[0].get('dsDescriptionValue', {}).get('value') if isinstance(desc, list) and desc else '', 420),
                 files=[{'name': f.get('dataFile', {}).get('filename'), 'size': f.get('dataFile', {}).get('filesize'),
                         'checksum': (f.get('dataFile', {}).get('checksum') or {}).get('value'),
                         'id': f.get('dataFile', {}).get('id'), 'tabular': bool(f.get('dataFile', {}).get('tabularData')),
                         'restricted': f.get('restricted')} for f in latest.get('files', [])][:12],
                 n_files=len(latest.get('files', [])))
    elif kind == 'hf':
        card = data.get('cardData') or {}
        d.update(title=data.get('id'), creators=[data.get('author')], date=str(data.get('createdAt', ''))[:10], license=card.get('license'),
                 version=data.get('sha', '')[:10], access='gated' if data.get('gated') else 'open', downloads=data.get('downloads'),
                 description=_clean(data.get('description') or card.get('pretty_name'), 300),
                 files=[{'name': s.get('rfilename')} for s in data.get('siblings', [])][:12], n_files=len(data.get('siblings', [])),
                 configs=[c.get('config_name') for c in (card.get('dataset_info') if isinstance(card.get('dataset_info'), list) else [])][:8],
                 languages=card.get('language'), tags=[t for t in data.get('tags', []) if t.startswith(('arxiv:', 'size_categories:', 'source_datasets:', 'task_categories:'))][:8])
    elif kind == 'github':
        d.update(title=data.get('full_name'), creators=[(data.get('owner') or {}).get('login')], date=str(data.get('created_at', ''))[:10],
                 pushed=str(data.get('pushed_at', ''))[:10], license=(data.get('license') or {}).get('spdx_id'), archived=data.get('archived'),
                 description=_clean(data.get('description'), 300), size_kb=data.get('size'), topics=data.get('topics'))
    elif kind == 'deu':
        res = data.get('result', data)
        dists = res.get('distributions') or []
        d.update(title=_lang(res.get('title')), creators=[_lang((res.get('publisher') or {}).get('name'))], date=str(res.get('issued') or '')[:10],
                 modified=str(res.get('modified') or '')[:10], license=sorted({(x.get('license') or {}).get('id') or '' for x in dists} - {''}),
                 description=_clean(_lang(res.get('description')), 300), n_files=len(dists),
                 files=[{'name': _lang(x.get('title')), 'format': (x.get('format') or {}).get('id'),
                         'url': (x.get('download_url') or x.get('access_url') or [''])[0] if isinstance(x.get('download_url') or x.get('access_url'), list) else (x.get('download_url') or x.get('access_url'))}
                        for x in dists][:8])
    elif kind == 'doi':
        a = (data.get('data') or {}).get('attributes', {})
        d.update(title=((a.get('titles') or [{}])[0]).get('title'), creators=[c.get('name') for c in (a.get('creators') or [])][:4],
                 date=a.get('publicationYear'), type=(a.get('types') or {}).get('resourceTypeGeneral'), publisher=a.get('publisher'),
                 license=[r.get('rightsIdentifier') or r.get('rights') for r in (a.get('rightsList') or [])][:2], url=a.get('url'),
                 description=_clean(((a.get('descriptions') or [{}])[0]).get('description'), 300),
                 related=[r.get('relatedIdentifier') for r in (a.get('relatedIdentifiers') or [])][:5])
    elif kind == 'crossref':
        m = data.get('message', {})
        d.update(title=(m.get('title') or [None])[0], creators=[f"{a.get('given', '')} {a.get('family', '')}".strip() for a in m.get('author', [])][:4],
                 date=((m.get('issued') or {}).get('date-parts') or [[None]])[0][0], type=m.get('type'), publisher=m.get('publisher'),
                 container=(m.get('container-title') or [None])[0], license=[x.get('URL') for x in m.get('license', [])][:2], url=m.get('URL'),
                 description=_clean(m.get('abstract'), 300))
    elif kind == 'openalex':
        loc = data.get('primary_location') or {}
        d.update(title=data.get('title'), creators=[(a.get('author') or {}).get('display_name') for a in (data.get('authorships') or [])][:4],
                 date=data.get('publication_year'), type=data.get('type'), doi=data.get('doi'), source=(loc.get('source') or {}).get('display_name'),
                 landing=loc.get('landing_page_url'), oa=(data.get('open_access') or {}).get('oa_url'),
                 locations=[x.get('landing_page_url') for x in (data.get('locations') or [])][:4])
    return d


# --------------------------------------------------------------------------- fetch and peek
def read_csv(path):
    with Path(path).open(encoding='utf-8-sig', newline='') as fh:
        return list(csv.DictReader(fh))


def fetch(items, out_dir=CAPTURE_DIR, pause=2.5, capture=capture_evidence.capture):
    """items: list of (resource_id, url). One request each; returns the capture records."""
    out = []
    for i, item in enumerate(items):
        rid, url = item[0], item[1]
        fallback = item[2] if len(item) > 2 else None
        if i:
            time.sleep(pause)
        rec = capture(url, rid, out_dir=out_dir, purpose='G2 round 2: repository record of a discovered resource (single GET)', pause=3.0)
        out.append(rec)
        last = rec['attempts'][-1] if rec.get('attempts') else {}
        if fallback and rec['outcome'] == 'FAILED' and last.get('http_status') == 404:  # DOI not registered at DataCite
            time.sleep(pause)
            out.append(capture(fallback, rid, out_dir=out_dir,
                               purpose='G2 round 2: repository record, second registration agency (single GET)', pause=3.0))
    return out


def peek(url, resource_id, n=DEFAULT_PEEK_BYTES, out_dir=INSPECT_DIR, timeout=40, opener=None, purpose=''):
    """Read at most n bytes of one address. Stores them and appends a log line. Never raises on HTTP errors."""
    n = min(int(n), MAX_PEEK_BYTES)
    if urlsplit(url).scheme not in ('http', 'https'):
        raise ValueError(f'only http(s) URLs: {url!r}')
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    rec = {'resource_id': resource_id, 'url': url, 'requested_bytes': n, 'started_utc': utc_now(), 'user_agent': USER_AGENT,
           'tool': 'mapping/scripts/verify_resources.py', 'purpose': purpose or 'G2 round 2: minimal data inspection (first bytes only)'}
    req = Request(url, headers={'User-Agent': USER_AGENT, 'Range': f'bytes=0-{n - 1}', 'Accept': '*/*'})
    body = b''
    try:
        with (opener or urlopen)(req, timeout=timeout) as resp:
            body = resp.read(n)
            rec.update({'outcome': 'READ', 'http_status': resp.status, 'content_type': resp.headers.get_content_type(),
                        'content_range': resp.headers.get('Content-Range'), 'content_length_header': resp.headers.get('Content-Length'),
                        'final_url': resp.geturl(), 'range_honoured': resp.status == 206})
    except HTTPError as ex:
        rec.update({'outcome': 'HTTP_ERROR', 'http_status': ex.code, 'error': str(ex.reason)})
        ex.close()
    except (URLError, TimeoutError, OSError) as ex:
        rec.update({'outcome': 'NETWORK_ERROR', 'error': f'{type(ex).__name__}: {ex}'})
    if body:
        digest_hex = hashlib.sha256(body).hexdigest()
        folder = out_dir / resource_id
        folder.mkdir(parents=True, exist_ok=True)
        stamp = rec['started_utc'].replace(':', '').replace('-', '')[:15]
        path = folder / f'{stamp}_{digest_hex[:12]}.bin'
        path.write_bytes(body)
        rec.update({'bytes_read': len(body), 'sha256': digest_hex, 'stored_file': path.relative_to(out_dir).as_posix()})
    else:
        rec.update({'bytes_read': 0, 'sha256': None, 'stored_file': None})
    rec['finished_utc'] = utc_now()
    with (out_dir / LOG_NAME).open('a', encoding='utf-8', newline='\n') as fh:
        fh.write(json.dumps(rec, ensure_ascii=False, sort_keys=True) + '\n')
    return rec


def read_inspections(out_dir=INSPECT_DIR):
    path = Path(out_dir) / LOG_NAME
    if not path.exists():
        return []
    return [json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x.strip()]


# --------------------------------------------------------------------------- observation of a peek
DATA_TYPES = {'text/csv', 'text/tab-separated-values', 'application/json', 'application/ld+json', 'application/xml', 'text/xml',
              'application/zip', 'application/x-zip-compressed', 'application/vnd.ms-excel', 'text/plain', 'application/rdf+xml',
              'text/turtle', 'application/x-turtle', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
              'application/octet-stream', 'application/gzip', 'application/x-gzip', 'application/vnd.apache.parquet',
              'application/n-triples', 'application/sparql-results+json', 'application/x-ndjson', 'application/jsonl'}
FIELD_PATTERNS = [('FIELD_CELEX', r'\bcelex'), ('FIELD_ELI', r'(^|[^a-z])eli([^a-z]|$)|legislation.?identifier'), ('FIELD_ECLI', r'ecli'),
                  ('FIELD_LEGAL_BASIS', r'legal.?basis|legal.?act|regulation|directive|article'),
                  ('FIELD_DECISION_OR_SANCTION', r'decision|sanction|fine\b|penalt|measure|opinion|ruling|judg'),
                  ('FIELD_COUNTRY_OR_MEMBER_STATE', r'country|member.?state|nation|jurisdiction'),
                  ('FIELD_DATE', r'date|year|period'), ('FIELD_ENTITY_NAME', r'(^|[^a-z])(name|entity|company|organi[sz]ation|undertaking|institution|authority|body)'),
                  ('FIELD_ENTITY_ID', r'(^|[^a-z])(id|identifier|lei|code|reference)([^a-z]|$)')]


def observe(peek_record, root=INSPECT_DIR):
    """Deterministic observation of one peek: kind of content and, for tabular or keyed content, the field names."""
    obs = {'availability': 'NOT_TESTED', 'fields': [], 'content_kind': None}
    if peek_record.get('outcome') != 'READ' or not peek_record.get('bytes_read'):
        obs['availability'] = 'ACCESS_FAILED'
        return obs
    raw = (Path(root) / peek_record['stored_file']).read_bytes()
    ctype = (peek_record.get('content_type') or '').lower()
    head = raw[:200].lstrip()
    text = raw.decode('utf-8-sig', errors='replace')
    if raw[:2] == b'PK':
        obs.update(content_kind='ARCHIVE', availability='DATA_AVAILABILITY_VERIFIED')
    elif raw[:4] == b'PAR1':
        obs.update(content_kind='PARQUET', availability='DATA_AVAILABILITY_VERIFIED')
    elif raw[:6] == b'\xfd7zXZ\x00' or raw[:2] == b'\x1f\x8b':
        obs.update(content_kind='COMPRESSED', availability='DATA_AVAILABILITY_VERIFIED')
    elif '/api.github.com/repos/' in (peek_record.get('url') or '') + '/' and (peek_record.get('url') or '').rstrip('/').endswith('/contents'):
        keys = list(dict.fromkeys(re.findall(r'"name"\s*:\s*"([^"]{1,80})"', text)))[:40]
        obs.update(content_kind='REPOSITORY_LISTING', availability='LISTING_ONLY', fields=[])
        obs['listing'] = keys
    elif raw[:5] == b'%PDF-':
        obs.update(content_kind='PDF_DOCUMENT', availability='DOCUMENT_ONLY')
    elif ctype in ('text/html', 'application/xhtml+xml') or head[:1] == b'<' and re.match(rb'<!doctype html|<html', head, re.I):
        obs.update(content_kind='HTML', availability='LANDING_PAGE_ONLY')
    elif head[:1] in (b'{', b'['):
        keys = list(dict.fromkeys(re.findall(r'"([A-Za-z_@][\w .@-]{0,40})"\s*:', text)))[:40]
        obs.update(content_kind='JSON', availability='DATA_AVAILABILITY_VERIFIED', fields=keys)
    elif head[:1] == b'<':
        names = list(dict.fromkeys(re.findall(r'<([A-Za-z_][\w:.-]{0,40})[\s>/]', text)))[:30]
        obs.update(content_kind='XML', availability='DATA_AVAILABILITY_VERIFIED', fields=names)
    elif ctype in DATA_TYPES or '\n' in text:
        first = text.split('\n', 1)[0]
        delim = max([',', ';', '\t', '|'], key=first.count)
        cols = [c.strip().strip('"') for c in first.split(delim)] if first.count(delim) >= 1 else []
        if cols:
            obs.update(content_kind='TABULAR', availability='DATA_AVAILABILITY_VERIFIED', fields=cols[:60])
        elif ctype in DATA_TYPES - {'text/plain', 'application/octet-stream'}:
            obs.update(content_kind='OTHER_DATA', availability='DATA_AVAILABILITY_VERIFIED')
        else:
            obs.update(content_kind='TEXT', availability='LANDING_PAGE_ONLY')
    return obs


def capabilities(fields):
    """Field-name matches. They show that a column or key with that name exists, nothing about its content."""
    found = {}
    for name in fields:
        low = name.lower()
        for cap, pattern in FIELD_PATTERNS:
            if re.search(pattern, low):
                found.setdefault(cap, []).append(name)
    return found


# --------------------------------------------------------------------------- command line
def _targets_from_resources(statuses, only_new):
    rows = read_csv(MAPPING / 'data' / 'resources.csv')
    out = []
    for r in rows:
        if r['verification_status'] not in statuses or (only_new and r['seed_id']):
            continue
        for col in ('primary_access_url', 'description_url'):
            kind, key = classify(r[col])
            if kind:
                out.append((r['resource_id'], kind, key, r[col]))
                break
        else:
            out.append((r['resource_id'], None, None, r['description_url']))
    return out


SKIP_HOSTS = ('datadump.publications.europa.eu',)  # authentication required: never attempted
PEEK_ROLES = ('BULK_DOWNLOAD', 'API')


def plan_inspections(data_dir=MAPPING / 'data', inspect_dir=INSPECT_DIR, second_pass=False):
    """One endpoint per resource: the first BULK_DOWNLOAD, else API. Addresses already inspected are skipped.
    second_pass: resources whose earlier inspections found no data get ONE more, different, address."""
    ends = read_csv(Path(data_dir) / 'access_endpoints.csv')
    done = {r['url'] for r in read_inspections(inspect_dir)}
    resources = {r['resource_id']: r for r in read_csv(Path(data_dir) / 'resources.csv')}
    plan, taken = [], set()
    for role in PEEK_ROLES:
        for e in ends:
            rid_ = e['resource_id']
            if rid_ in taken or e['endpoint_role'] != role or e['url'] in done:
                continue
            if any(h in e['url'] for h in SKIP_HOSTS) or e['auth_required'] == 'YES':
                continue
            if '/swagger-ui/' in e['url'] or 'huggingface.co/api/datasets/' in e['url']:
                continue  # documentation pages and repository metadata are not data
            if resources.get(rid_, {}).get('verification_status') == 'INACCESSIBLE':
                continue
            if not e['url'].startswith('http'):
                continue
            taken.add(rid_)
            plan.append((rid_, e['url']))
    logs = read_inspections(inspect_dir)
    if not second_pass:
        # resources that already have an inspection are not inspected again through another address
        inspected = {r['resource_id'] for r in logs}
        return [(r, u) for r, u in plan if r not in inspected]
    resolved, attempts = set(), {}
    for rec in logs:
        attempts[rec['resource_id']] = attempts.get(rec['resource_id'], 0) + 1
        if observe(rec, root=inspect_dir)['availability'] == 'DATA_AVAILABILITY_VERIFIED':
            resolved.add(rec['resource_id'])
    return [(r, u) for r, u in plan if r not in resolved and attempts.get(r, 0) == 1]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    f = sub.add_parser('fetch')
    f.add_argument('--statuses', default='DISCOVERED,PARTIALLY_VERIFIED')
    f.add_argument('--include-seeds', action='store_true')
    f.add_argument('--dry-run', action='store_true')
    f.add_argument('--only', nargs='*')
    i = sub.add_parser('inspect')
    i.add_argument('--dry-run', action='store_true')
    i.add_argument('--only', nargs='*')
    i.add_argument('--limit', type=int, default=0)
    i.add_argument('--second-pass', action='store_true')
    p = sub.add_parser('peek')
    p.add_argument('--url', required=True)
    p.add_argument('--resource', required=True)
    p.add_argument('--bytes', type=int, default=DEFAULT_PEEK_BYTES)
    args = ap.parse_args()
    if args.cmd == 'fetch':
        targets = _targets_from_resources(set(args.statuses.split(',')), not args.include_seeds)
        if args.only:
            targets = [t for t in targets if t[0] in set(args.only)]
        items = [(rid, record_url(k, key), record_url('crossref', key) if k == 'doi' else None) for rid, k, key, _ in targets if k]
        skipped = [(rid, url) for rid, k, _, url in targets if not k]
        print(f'{len(items)} record requests; {len(skipped)} without a record API')
        for rid, url in skipped:
            print('  no record API:', rid, url)
        if args.dry_run:
            return 0
        for rec in fetch(items):
            last = rec['attempts'][-1] if rec.get('attempts') else {}
            print(rec['record_id'], rec['outcome'], rec.get('http_status') or last.get('http_status') or last.get('error', '')[:60], rec.get('bytes'))
    elif args.cmd == 'inspect':
        plan = plan_inspections(second_pass=args.second_pass)
        if args.only:
            plan = [t for t in plan if t[0] in set(args.only)]
        if args.limit:
            plan = plan[:args.limit]
        print(f'{len(plan)} first-bytes inspections planned')
        if args.dry_run:
            for rid_, url in plan:
                print(' ', rid_, url[:110])
            return 0
        for k, (rid_, url) in enumerate(plan):
            if k:
                time.sleep(2.5)
            rec = peek(url, rid_)
            print(rid_, rec['outcome'], rec.get('http_status'), rec.get('content_type'), rec.get('bytes_read'), rec.get('error', '')[:60])
    else:
        rec = peek(args.url, args.resource, args.bytes)
        print(rec['outcome'], rec.get('http_status'), rec.get('content_type'), rec.get('bytes_read'))
    return 0


if __name__ == '__main__':
    sys.exit(main())
