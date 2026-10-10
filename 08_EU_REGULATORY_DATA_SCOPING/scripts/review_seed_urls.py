#!/usr/bin/env python3
"""Static review of the role played by each seed URL. No network access.

Reads only source_seed_id, name and source_url from the seed inventory and
assigns, by URL pattern alone, a CANDIDATE role to each URL (what kind of page
the address looks like). It does not classify the resource, does not edit the
inventory, and its output needs human confirmation against the live page.

Rules are applied in order; the first match decides. They are deliberately
simple so that anyone can re-derive the result by reading the URL.
"""
import csv
import re
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SEEDS = ROOT / 'inputs' / 'seed_inventory_v0_1.csv'

RULES = [
    ('site_root', 'path is empty: the address is a whole site, not one resource',
     lambda h, p: p.strip('/') == ''),
    ('code_repository', 'host is a code hosting platform',
     lambda h, p: h == 'github.com'),
    ('data_repository_record', 'record page of a research data repository',
     lambda h, p: h == 'zenodo.org' and '/records/' in p),
    ('catalogue_entry', 'entry of the data.europa.eu catalogue (a description of a dataset)',
     lambda h, p: h == 'data.europa.eu' and p.startswith('/data/datasets/')),
    ('news_or_announcement_page', 'address of a news item or announcement',
     lambda h, p: bool(re.search(r'/new-|/news/', p))),
    ('help_or_documentation_page', 'help, FAQ, "about" or developer documentation',
     lambda h, p: bool(re.search(r'/content/help/|/faqs?/|find-out-more|what_is|about-|/about|developer-corner|/api/', p)) or h.startswith('docs.')),
    ('institutional_policy_page', 'explanatory page of an institution about a policy or service',
     lambda h, p: h in ('commission.europa.eu', 'digital-strategy.ec.europa.eu', 'single-market-economy.ec.europa.eu',
                        'www.consilium.europa.eu', 'joint-research-centre.ec.europa.eu')),
    ('search_interface', 'search or index page of a service',
     lambda h, p: bool(re.search(r'/search|/index$', p))),
    ('collection_or_register_page', 'page of a named collection or register',
     lambda h, p: bool(re.search(r'/collection/|/registers?/|/web/', p))),
    ('other_specific_page', 'none of the patterns above', lambda h, p: True),
]


def review(path=SEEDS):
    with path.open('r', encoding='utf-8-sig', newline='') as handle:
        rows = [{k: r[k] for k in ('source_seed_id', 'name', 'source_url')} for r in csv.DictReader(handle)]
    shared = defaultdict(list)
    for r in rows:
        shared[r['source_url']].append(r['source_seed_id'])
    out = []
    for r in rows:
        parts = urlsplit(r['source_url'])
        host, path_ = (parts.hostname or '').lower(), parts.path
        role, why = next((name, why) for name, why, test in RULES if test(host, path_))
        same = [i for i in shared[r['source_url']] if i != r['source_seed_id']]
        out.append({**r, 'host': host, 'url_role_candidate': role, 'rule': why,
                    'shares_url_with': ';'.join(same),
                    'has_query_parameters': 'yes' if parts.query else 'no'})
    return out


def main():
    rows = review()
    w = csv.DictWriter(__import__('sys').stdout, fieldnames=list(rows[0]), lineterminator='\n')
    w.writeheader()
    w.writerows(rows)


if __name__ == '__main__':
    main()
