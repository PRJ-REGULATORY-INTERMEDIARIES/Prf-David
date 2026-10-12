#!/usr/bin/env python3
"""Registered, reproducible discovery searches for the G2 systematic mapping.

run     executes every query of a registry CSV against the public search API of
        its platform (one GET per query, metadata only), stores the raw response
        byte for byte with its SHA-256 and appends one line to SEARCH_LOG.jsonl
hits    rebuilds mapping/data/search_hits.csv from the stored responses
        (deterministic: no network)

A search hit is a discovery occurrence, not a resource. Nothing here screens,
classifies or downloads data. Failed requests are logged as failures.
Standard library only.
"""
import argparse
import csv
import hashlib
import json
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[2]
MAPPING = ROOT / 'mapping'
SEARCH_DIR = MAPPING / 'evidence' / 'searches'
LOG_NAME = 'SEARCH_LOG.jsonl'
USER_AGENT = 'EU-Regulatory-Data-Scoping/mapping-discovery (academic research; metadata search only)'
PAGE_SIZE = 25  # default depth of one search page

# One public, documented search endpoint per platform. {q} is the URL-encoded query; {c} the
# URL-encoded value of the optional `param` column (a catalogue identifier for DEUC).
PLATFORMS = {
    'DEU': ('data.europa.eu search API', 'https://data.europa.eu/api/hub/search/search?q={q}&filter=dataset&limit=25'),
    'ZEN': ('Zenodo records API', 'https://zenodo.org/api/records?q={q}&size=25&sort=bestmatch'),
    'DVN': ('Harvard Dataverse search API', 'https://dataverse.harvard.edu/api/search?q={q}&type=dataset&per_page=25'),
    'DCT': ('DataCite REST API', 'https://api.datacite.org/dois?query={q}&resource-type-id=dataset&page[size]=25'),
    'OAX': ('OpenAlex works API', 'https://api.openalex.org/works?search={q}&per-page=25'),
    'HF': ('Hugging Face Hub datasets API', 'https://huggingface.co/api/datasets?search={q}&limit=25'),
    'GH': ('GitHub repository search API', 'https://api.github.com/search/repositories?q={q}&per_page=25'),
    # added in round 2
    'DCAT': ('data.europa.eu catalogue listing', 'https://data.europa.eu/api/hub/search/search?q={q}&filter=catalogue&limit=100'),
    'DEUC': ('data.europa.eu datasets of one catalogue', 'https://data.europa.eu/api/hub/search/search?q={q}&filter=dataset&limit=100&facets=%7B%22catalog%22%3A%5B%22{c}%22%5D%7D'),
    'DEUF': ('data.europa.eu datasets, facet probe (counts only)', 'https://data.europa.eu/api/hub/search/search?q={q}&filter=dataset&limit=1&aggregation=true'),
    'B2F': ('B2FIND (EUDAT) CKAN API', 'https://b2find.eudat.eu/api/3/action/package_search?q={q}&rows=25'),
    'DNS': ('DANS Data Stations (Dataverse) search API', 'https://ssh.datastations.nl/api/search?q={q}&type=dataset&per_page=25'),
}
# platform -> (query parameter, value of page 0, step per page); platforms not listed cannot be paged
PAGING = {'DEU': ('page', 0, 1), 'DEUC': ('page', 0, 1), 'DCAT': ('page', 0, 1), 'ZEN': ('page', 1, 1), 'OAX': ('page', 1, 1),
          'GH': ('page', 1, 1), 'DVN': ('start', 0, 25), 'DNS': ('start', 0, 25), 'B2F': ('start', 0, 25)}
PAGE_SIZES = {'DEUC': 100, 'DCAT': 100, 'DEUF': 1}
HIT_FIELDS = ['search_id', 'rank', 'platform', 'platform_record_id', 'title', 'url', 'creator_or_publisher', 'year']


def utc_now():
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def build_url(platform, query, param='', page=0):
    url = PLATFORMS[platform][1].format(q=quote(query, safe=''), c=quote(param, safe=''))
    if page:
        if platform not in PAGING:
            raise ValueError(f'platform {platform} cannot be paged')
        key, base, step = PAGING[platform]
        url += f'&{key}={base + page * step}'
    return url


def page_size(platform):
    return PAGE_SIZES.get(platform, PAGE_SIZE)


def _lang(value):
    """data.europa.eu serves multilingual fields as {lang: text}."""
    if isinstance(value, dict):
        return value.get('en') or next((v for v in value.values() if v), '')
    return value or ''


def parse_hits(platform, payload):
    """Return (total_reported, [hit, ...]) from one stored API response."""
    hits, total = [], None
    if platform == 'DEU':
        res = payload.get('result', {})
        total = res.get('count')
        for r in res.get('results', []):
            hits.append({'platform_record_id': r.get('id', ''), 'title': _lang(r.get('title')),
                         'url': f"https://data.europa.eu/data/datasets/{r.get('id', '')}",
                         'creator_or_publisher': _lang((r.get('publisher') or {}).get('name')) or _lang((r.get('catalog') or {}).get('title')),
                         'year': str(r.get('issued') or r.get('modified') or '')[:4]})
    elif platform == 'ZEN':
        total = payload.get('hits', {}).get('total')
        for r in payload.get('hits', {}).get('hits', []):
            md = r.get('metadata', {})
            hits.append({'platform_record_id': str(r.get('doi') or r.get('id', '')), 'title': md.get('title', ''),
                         'url': (r.get('links') or {}).get('self_html') or f"https://zenodo.org/records/{r.get('id')}",
                         'creator_or_publisher': '; '.join(c.get('name', '') for c in md.get('creators', [])[:3]),
                         'year': str(md.get('publication_date', ''))[:4]})
    elif platform == 'DVN':
        data = payload.get('data', {})
        total = data.get('total_count')
        for r in data.get('items', []):
            hits.append({'platform_record_id': r.get('global_id', ''), 'title': r.get('name', ''), 'url': r.get('url', ''),
                         'creator_or_publisher': '; '.join((r.get('authors') or [])[:3]),
                         'year': str(r.get('published_at', ''))[:4]})
    elif platform == 'DCT':
        total = payload.get('meta', {}).get('total')
        for r in payload.get('data', []):
            a = r.get('attributes', {})
            hits.append({'platform_record_id': a.get('doi', ''), 'title': ((a.get('titles') or [{}])[0]).get('title', ''),
                         'url': a.get('url') or f"https://doi.org/{a.get('doi', '')}",
                         'creator_or_publisher': '; '.join(c.get('name', '') for c in (a.get('creators') or [])[:3]) or (a.get('publisher') or ''),
                         'year': str(a.get('publicationYear') or '')})
    elif platform == 'OAX':
        total = payload.get('meta', {}).get('count')
        for r in payload.get('results', []):
            hits.append({'platform_record_id': r.get('id', ''), 'title': r.get('title') or '',
                         'url': r.get('doi') or r.get('id', ''),
                         'creator_or_publisher': '; '.join((a.get('author') or {}).get('display_name', '') for a in (r.get('authorships') or [])[:3]),
                         'year': str(r.get('publication_year') or '')})
    elif platform == 'HF':
        total = None  # the Hub API does not report a total
        for r in payload:
            hits.append({'platform_record_id': r.get('id', ''), 'title': r.get('id', ''),
                         'url': f"https://huggingface.co/datasets/{r.get('id', '')}",
                         'creator_or_publisher': r.get('author') or '', 'year': str(r.get('createdAt') or r.get('lastModified') or '')[:4]})
    elif platform == 'GH':
        total = payload.get('total_count')
        for r in payload.get('items', []):
            hits.append({'platform_record_id': r.get('full_name', ''), 'title': (r.get('full_name', '') + ' — ' + (r.get('description') or '')).strip(' —'),
                         'url': r.get('html_url', ''), 'creator_or_publisher': (r.get('owner') or {}).get('login', ''),
                         'year': str(r.get('created_at', ''))[:4]})
    elif platform in ('DEUC', 'DEUF'):
        return parse_hits('DEU', payload)
    elif platform == 'DCAT':
        res = payload.get('result', {})
        total = res.get('count')
        for r in res.get('results', []):
            pub = r.get('publisher') or {}
            name = _lang(pub.get('name')) or _lang(pub.get('type'))
            hits.append({'platform_record_id': r.get('id', ''), 'title': _lang(r.get('title')),
                         'url': f"https://data.europa.eu/data/catalogues/{r.get('id', '')}",
                         'creator_or_publisher': f"{name} [{(r.get('country') or {}).get('id', '')}]", 'year': ''})
    elif platform == 'B2F':
        res = payload.get('result', {})
        total = res.get('count')
        for r in res.get('results', []):
            author = r.get('author')
            who = (r.get('organization') or {}).get('title', '') or (author if isinstance(author, str) else '; '.join(author or []))
            hits.append({'platform_record_id': r.get('name') or r.get('id', ''), 'title': r.get('title') or '',
                         'url': f"https://b2find.eudat.eu/dataset/{r.get('name', '')}",
                         'creator_or_publisher': who, 'year': str(r.get('metadata_created', ''))[:4]})
    elif platform == 'DNS':
        return parse_hits('DVN', payload)
    else:
        raise ValueError(f'unknown platform {platform!r}')
    for h in hits:
        for k, v in h.items():
            h[k] = ' '.join(str(v).split())
    return total, hits


def read_registry(path):
    with Path(path).open(encoding='utf-8-sig', newline='') as fh:
        return list(csv.DictReader(fh))


def read_log(search_dir=SEARCH_DIR):
    path = Path(search_dir) / LOG_NAME
    if not path.exists():
        return []
    return [json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x.strip()]


def _fetch(url):
    req = Request(url, headers={'User-Agent': USER_AGENT, 'Accept': 'application/json'})
    with urlopen(req, timeout=60) as resp:
        return resp.read(), resp.status


def run(registry, search_dir=SEARCH_DIR, pause=2.0, only=None, fetch=None):
    """Execute each registered query once. Queries already logged as EXECUTED are skipped."""
    search_dir = Path(search_dir)
    search_dir.mkdir(parents=True, exist_ok=True)
    done = {r['search_id'] for r in read_log(search_dir) if r['outcome'] == 'EXECUTED'}
    out = []
    for row in read_registry(registry):
        sid = row['search_id']
        if sid in done or (only and sid not in only):
            continue
        param, page = (row.get('param') or ''), int(row.get('page') or 0)
        url = build_url(row['platform'], row['query'], param, page)
        rec = {'search_id': sid, 'platform': row['platform'], 'platform_name': PLATFORMS[row['platform']][0],
               'query': row['query'], 'language': row['language'], 'request_url': url, 'executed_at_utc': utc_now(),
               'page_size_requested': page_size(row['platform']), 'user_agent': USER_AGENT,
               'tool': 'mapping/scripts/mapping_search.py'}
        if param:
            rec['param'] = param
        if page:
            rec['page'] = page
        if row.get('depth_rationale'):
            rec['depth_rationale'] = row['depth_rationale']
        try:
            body, status = (fetch or _fetch)(url)
            digest = hashlib.sha256(body).hexdigest()
            stamp = rec['executed_at_utc'].replace(':', '').replace('-', '')[:15]
            name = f'{sid}_{stamp}_{digest[:12]}.json'
            total, hits = parse_hits(row['platform'], json.loads(body))
            (search_dir / name).write_bytes(body)
            rec.update({'outcome': 'EXECUTED', 'http_status': status, 'raw_file': name, 'sha256': digest, 'bytes': len(body),
                        'total_reported': total, 'hits_returned': len(hits)})
        except HTTPError as ex:
            rec.update({'outcome': 'FAILED', 'http_status': ex.code, 'error': str(ex.reason)})
        except (URLError, TimeoutError, OSError, ValueError) as ex:
            rec.update({'outcome': 'FAILED', 'error': f'{type(ex).__name__}: {ex}'})
        with (search_dir / LOG_NAME).open('a', encoding='utf-8', newline='\n') as fh:
            fh.write(json.dumps(rec, ensure_ascii=False, sort_keys=True) + '\n')
        out.append(rec)
        time.sleep(pause)
    return out


def build_hits(search_dir=SEARCH_DIR):
    """All hits of all executed searches, in search_id order. Pure function of the stored files."""
    rows = []
    for rec in sorted(read_log(search_dir), key=lambda r: r['search_id']):
        if rec['outcome'] != 'EXECUTED':
            continue
        payload = json.loads((Path(search_dir) / rec['raw_file']).read_bytes())
        _, hits = parse_hits(rec['platform'], payload)
        offset = rec.get('page', 0) * rec.get('page_size_requested', PAGE_SIZE)
        for i, h in enumerate(hits, 1):
            rows.append({'search_id': rec['search_id'], 'rank': str(offset + i), 'platform': rec['platform'], **h})
    return rows


def write_csv(path, fields, rows):
    with Path(path).open('w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=fields, lineterminator='\n')
        w.writeheader()
        w.writerows(rows)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    r = sub.add_parser('run')
    r.add_argument('--registry', required=True)
    r.add_argument('--only', nargs='*')
    sub.add_parser('hits')
    args = ap.parse_args()
    if args.cmd == 'run':
        for rec in run(args.registry, only=set(args.only) if args.only else None):
            print(rec['search_id'], rec['outcome'], rec.get('http_status'), rec.get('total_reported'), rec.get('hits_returned'), rec.get('error', ''))
    else:
        rows = build_hits()
        write_csv(MAPPING / 'data' / 'search_hits.csv', HIT_FIELDS, rows)
        print(f'{len(rows)} hits written')


if __name__ == '__main__':
    main()
