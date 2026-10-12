"""G2 round 2 — curation input (2026-10-10): verification, regulatory coverage (set B) and prior art.

Same conventions as round1.py. Every judgement below was entered by the programming agent
(Claude Code) after reading preserved evidence, and is provisional: the builder writes
classification_basis=AGENT_PROVISIONAL and researcher_confirmed=NO on every row.

Value tags: |P primary page read by the agent | |M machine metadata of a repository or catalogue
record | |S seed inventory, unverified | |I agent inference | |O observed in a first-bytes
inspection. NOT_ASSESSED means not collected, never absent.

This file (a) PATCHES round-1 rows whose evidence changed, (b) APPENDS new resources, (c) adds
endpoints, relations and decisions. Round-1 identifiers and rows are never removed.
Resources listed through the data.europa.eu catalogue take their descriptive fields from the
stored API response of the search that returned them (metadata of the maintainer's own record).
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'mapping' / 'scripts'))
import mapping_search as ms  # noqa: E402

ROUND = 'G2-R2'
VERIFICATION_DATE = '2026-10-10'
EC = 'European Commission'
PO = 'Publications Office of the European Union'

# --------------------------------------------------------------------------- helpers: catalogue records
_SEARCH_DIR = ROOT / 'mapping' / 'evidence' / 'searches'


def _lang(v):
    if isinstance(v, dict):
        return v.get('en') or next((x for x in v.values() if x), '')
    return v or ''


def _clean(text, n):
    return ' '.join(re.sub(r'<[^>]+>', ' ', str(text or '')).split())[:n]


def _index():
    idx = {}
    for rec in sorted(ms.read_log(_SEARCH_DIR), key=lambda r: r['search_id']):
        if rec['platform'] not in ('DEU', 'DEUC') or rec['outcome'] != 'EXECUTED':
            continue
        payload = json.loads((_SEARCH_DIR / rec['raw_file']).read_bytes())
        for x in payload.get('result', {}).get('results', []):
            idx.setdefault(x['id'], (x, rec['search_id']))
    return idx


CATALOGUE = _index()


def cat(prefix):
    if prefix in CATALOGUE:
        return CATALOGUE[prefix]
    found = [k for k in CATALOGUE if k.startswith(prefix)]
    if len(found) != 1:
        raise KeyError(f'catalogue prefix {prefix!r} matches {len(found)} entries')
    return CATALOGUE[found[0]]


def family(catalog, pattern):
    pat = re.compile(pattern)
    return [(x, sid) for x, sid in CATALOGUE.values()
            if (x.get('catalog') or {}).get('id') == catalog and pat.search(_lang(x.get('title')))]


_DATA_FORMATS = {'CSV', 'XML', 'JSON', 'XLS', 'XLSX', 'ZIP', 'RDF_XML', 'RDF_TURTLE', 'TSV', 'TXT', 'JSON_LD', 'SPARQL_JSON', 'ODS', 'GZIP', 'N3'}


def _first_url(dist):
    v = dist.get('download_url') or dist.get('access_url')
    if isinstance(v, list):
        v = v[0] if v else ''
    return v or ''


# --------------------------------------------------------------------------- containers
RESOURCES, ENDPOINTS, RELATIONS, DECISIONS = [], [], [], []
K = {}          # key -> resource number
_N = [105]      # last round-1 number


def _new(key):
    _N[0] += 1
    K[key] = _N[0]
    return _N[0]


def _dist_endpoints(n, x, limit=3):
    dists = x.get('distributions') or []
    ranked = sorted(dists, key=lambda d: 0 if (d.get('format') or {}).get('id') in _DATA_FORMATS else 1)
    seen = set()
    for d in ranked:
        url = _first_url(d)
        if not url or url in seen or not url.startswith('http'):
            continue
        seen.add(url)
        fmt = (d.get('format') or {}).get('id') or 'unspecified format'
        role = 'BULK_DOWNLOAD' if fmt in _DATA_FORMATS else 'ACCESS_PORTAL'
        ENDPOINTS.append((n, role, url, 'API_METADATA', 'UNKNOWN', False, f'Distribution listed in the catalogue record ({fmt}); address not requested unless an inspection is logged'))
        if len(seen) >= limit:
            break


def from_catalogue(key, prefixes, category, rset, *, indiv='INDIVIDUATED', elig='INCLUDE', terr='EU', name=None, unc='',
                   maint=None, theme=None, status='VERIFIED', note_family=''):
    """One resource from one catalogue record (or a family of records; the first is the sample)."""
    prefixes = [prefixes] if isinstance(prefixes, str) else prefixes
    recs = [cat(p) if isinstance(p, str) else p for p in prefixes]
    x, sid = recs[0]
    n = _new(key)
    dists = x.get('distributions') or []
    fmts = sorted({(d.get('format') or {}).get('id') for d in dists if (d.get('format') or {}).get('id')})
    lic = sorted({(d.get('license') or {}).get('id') for d in dists if (d.get('license') or {}).get('id')})
    issued, modified = str(x.get('issued') or '')[:10], str(x.get('modified') or '')[:10]
    temporal = x.get('temporal') or []
    r = dict(n=n, name=(name or _lang(x.get('title'))) + '|M', cat=category, set=rset, status=status, indiv=indiv, terr=terr,
             maint=(maint or _lang((x.get('publisher') or {}).get('name')) or _lang((x.get('catalog') or {}).get('title'))) + '|M',
             theme=(theme or _clean(_lang(x.get('description')), 240)) + '|M',
             desc=f"https://data.europa.eu/data/datasets/{x['id']}", elig=elig)
    if fmts:
        r['fmt'] = ';'.join(fmts) + '|M'
    if lic:
        r['lic'] = ';'.join(lic) + ' (catalogue licence code)|M'
    if issued or modified:
        r['upd'] = f"catalogue record issued {issued or 'n/a'}, modified {modified or 'n/a'}|M"
    if temporal and isinstance(temporal, list) and isinstance(temporal[0], dict) and temporal[0].get('gte'):
        r['temp'] = f"{str(temporal[0].get('gte'))[:10]} to {str(temporal[0].get('lte') or '')[:10]} (catalogue)|M"
    first = next((_first_url(d) for d in dists if _first_url(d)), '')
    if first.startswith('http'):
        r['url'] = first
    r['hits'] = [(s, i['id']) for i, s in recs[:5]]
    extra = f"Identity read from the maintainer's catalogue record (the stored API response of the search); {len(dists)} distribution(s) listed; the data were not opened unless a first-bytes inspection is logged."
    if len(recs) > 1:
        extra += f' Grouped from {len(recs)} catalogue records that differ only by instance label{note_family}; the first is the sample.'
    r['unc'] = (extra + ' ' + unc).strip()
    RESOURCES.append(r)
    ENDPOINTS.append((n, 'CATALOGUE_ENTRY', r['desc'], 'SEARCH_HIT', 'NO', True, 'data.europa.eu record (JavaScript shell; metadata read through the catalogue API)'))
    _dist_endpoints(n, x)
    return n


def explicit(key, **kw):
    n = _new(key)
    kw['n'] = n
    kw.setdefault('status', 'DISCOVERED')
    kw.setdefault('indiv', 'INDIVIDUATED')
    RESOURCES.append(kw)
    return n


_HITS = {}


def find_hit(platform_record_id):
    if not _HITS:
        for h in ms.build_hits(_SEARCH_DIR):
            _HITS.setdefault(h['platform_record_id'], h['search_id'])
    return (_HITS[platform_record_id], platform_record_id)


# --------------------------------------------------------------------------- (a) PATCHES of round-1 rows
# Repository records fetched on 2026-10-10 (evidence filed under the resource identifier).
PATCHES = {
    42: dict(status='VERIFIED', status_reason='catalogue record read directly; two HTML distributions', fmt='HTML|M',
             unc_add='Both distributions are HTML pages of EUR-Lex statistics; no data file is listed.'),
    43: dict(status='VERIFIED', status_reason='catalogue record read directly', fmt='RDF/XML;RDF Turtle;URI list (CSV in ZIP)|M',
             unc_add='Record lists four files (RDF/XML dump, Turtle dump, URI list, individual Turtle metadata).'),
    44: dict(name='ELI (European Legislation Identifier) - Ireland|M', indiv='INDIVIDUATED', status='VERIFIED',
             status_reason='record read; the group placeholder is split into one resource per country (DK, IT, LU, FI added)',
             maint='Publications Office of the European Union (catalogue publisher); metadata describe the electronic Irish Statute Book|M',
             theme='ELI metadata in RDFa for Acts and Statutory Instruments as published on the electronic Irish Statute Book; Acts 2013-2018|M',
             fmt='RDF Turtle;RDF/XML;TXT;ZIP|M', unc_add='Only the Irish record is described here; the other four countries are separate rows.'),
    45: dict(status='VERIFIED', status_reason='DataCite record read directly', maint='Koolen, Christof (depositor); publisher KU Leuven RDR|M',
             lic='CC BY 4.0 (DataCite rights list)|M', unc_add='DataCite record read; files, period and relation to a GitHub repository (MR-0098 is unrelated) not examined.'),
    46: dict(status='VERIFIED', status_reason='catalogue record read directly', fmt='ZIP|M',
             unc_add='Annotation by a single expert per document (record statement); one ZIP distribution.'),
    47: dict(status='VERIFIED', status_reason='catalogue record read directly', fmt='HTML;PDF|M',
             unc_add='Two distributions: a facts-and-figures page and a report.'),
    48: dict(status='VERIFIED', status_reason='catalogue record read directly; no distribution is listed',
             unc_add='Record lists no distribution, so availability of any data cannot be tested.'),
    49: dict(status='VERIFIED', status_reason='catalogue record read directly', fmt='CSV;XLSX;XML;ZIP|M',
             unc_add='Four distributions of the same table (CSV, ZIP, XLSX, XML).'),
    50: dict(status='VERIFIED', status_reason='catalogue record read directly', unc_add='One distribution; no licence in the record.'),
    51: dict(status='VERIFIED', status_reason='catalogue record read directly', unc_add='One distribution; no licence in the record.'),
    52: dict(status='VERIFIED', status_reason='catalogue record read directly', fmt='HTML;JSON;XML|M',
             unc_add='Three distributions: a search page and two list-request endpoints.'),
    53: dict(status='VERIFIED', status_reason='catalogue record read directly; no distribution is listed',
             unc_add='No distribution listed; probably a description of a web collection rather than a dataset.'),
    55: dict(status='VERIFIED', status_reason='Zenodo record read directly', maint='Heimsoth, Martin; Pandit, Harshvardhan J. (Zenodo creators)|M',
             fmt='ZIP|M', unc_add='One ZIP file of 2.2 MB, version 0.1.'),
    56: dict(status='VERIFIED', status_reason='Zenodo record read directly', fmt='tar.gz|M',
             unc_add='One archive of 4.8 GB (4,808,590,577 bytes); not downloaded.'),
    57: dict(status='PARTIALLY_VERIFIED', status_reason='Zenodo record read: it is a poster, not the corpus',
             unc_add='The Zenodo record is a poster (Poster.pdf, 1.1 MB); the corpus itself was not located.'),
    58: dict(status='VERIFIED', status_reason='Hugging Face record read directly', fmt='jsonl.xz per language and document type|M',
             unc_add='172 files (data/<language>/<type>.jsonl.xz); description reports about 179 GB; 24 languages.'),
    59: dict(status='VERIFIED', status_reason='Zenodo record read directly', fmt='ZIP|M',
             unc_add='One ZIP of 97 MB (cjeu_dec_2018_v1.zip).'),
    60: dict(status='VERIFIED', status_reason='Zenodo record read directly', fmt='RDS; codebook PDF|M',
             unc_add='Files: EUPDCorp RDS (501 MB) and a codebook (PDF).'),
    61: dict(status='VERIFIED', status_reason='Zenodo record read directly', fmt='CSV;JSON;ZIP;PDF|M',
             unc_add='Eight files including v4_acts.csv, EU_directives_final.json and a README (PDF); period 2004-2024 per description.'),
    62: dict(status='VERIFIED', status_reason='Zenodo record read directly', unc_add='One file of 334 KB.'),
    63: dict(status='VERIFIED', status_reason='Zenodo record read directly', fmt='XLSX;CSV codebook;MD;NVP|M',
             unc_add='Files: data workbook (2.5 MB), codebook CSV (55 KB), README and a 3.6 GB raw file; jurisdiction coverage not read.'),
    64: dict(status='VERIFIED', status_reason='Zenodo record read directly', fmt='CSV;XLSX|M',
             unc_add='Two small files; derived from OpenEFSA (named in the description).'),
    65: dict(status='VERIFIED', status_reason='Zenodo record read directly', unc_add='Four files (spreadsheets of cases and preliminary references).'),
    66: dict(status='VERIFIED', status_reason='Zenodo record read directly', fmt='CSV|M', unc_add='One CSV of 344 KB.'),
    67: dict(status='VERIFIED', status_reason='Dataverse record read directly', lic='CC0 1.0 (Dataverse record)|M', fmt='CSV;Perl scripts|M',
             unc_add='Five files: Warntjen_Prelex2013.csv (4.8 MB) and Perl extraction scripts.'),
    68: dict(status='VERIFIED', status_reason='Dataverse record read directly', lic='CC0 1.0 (Dataverse record)|M', fmt='TAB;PDF|M',
             unc_add='Three files: two tabular versions and a general overview (PDF).'),
    69: dict(status='VERIFIED', status_reason='Dataverse record read directly', lic='CC0 1.0 (Dataverse record)|M', fmt='DTA;DO|M',
             unc_add='19 files (Stata dataset and do-files); version 2.0.'),
    70: dict(status='VERIFIED', status_reason='Dataverse record read directly', lic='CC0 1.0 (Dataverse record)|M', fmt='TAB;PDF|M',
             unc_add='Two files: data (1.6 MB) and project description.'),
    71: dict(status='VERIFIED', status_reason='Dataverse record read directly', lic='CC0 1.0 (Dataverse record)|M',
             unc_add='Three files: codebook and two data files.'),
    72: dict(status='VERIFIED', status_reason='Dataverse record read directly', lic='CC0 1.0 (Dataverse record)|M', fmt='TAB;PDF;DO|M',
             unc_add='Three files: data, description and syntax.'),
    73: dict(status='VERIFIED', status_reason='Dataverse record read directly', lic='CC0 1.0 (Dataverse record)|M', fmt='TAB;SAS|M',
             unc_add='Two files: jcms2019.tab (206 KB) and SAS syntax.'),
    74: dict(status='VERIFIED', status_reason='Dataverse record read directly', lic='CC0 1.0 (Dataverse record)|M', fmt='TAB;SAS|M',
             unc_add='Five files including actors.tab (505 KB) and consultations.tab (45 KB).'),
    75: dict(status='VERIFIED', status_reason='Dataverse record read directly', lic='CC0 1.0 (Dataverse record)|M', fmt='SAS7BDAT;TAB;SAS|M',
             unc_add='Six files including a codebook (TAB) and sas7bdat data.'),
    76: dict(status='VERIFIED', status_reason='Dataverse record read directly', lic='CC0 1.0 (Dataverse record)|M', fmt='CSV;DO|M',
             unc_add='Five files: case_level_data.csv (188 KB) and issue_level_data.csv (419 KB) plus Stata code.'),
    77: dict(status='VERIFIED', status_reason='Dataverse record read directly; files are restricted',
             lic='CC0 1.0 (Dataverse record)|M', cond='Files restricted: access by request, as shown in the Dataverse record|M',
             unc_add='One restricted file; the title says the data are restricted until the article is published.'),
    78: dict(status='PARTIALLY_VERIFIED', status_reason='Crossref record of the data paper read; no deposit located',
             maint='Thomson, Robert; Arregui, Javier; Leuffen, Dirk; Costello, Rory et al. (article authors)|M',
             unc_add='Crossref record of the article read (Journal of European Public Policy, 2012). The deposit of the data was not located. A DANS record "Decision making in the European Union 2003" is a different dataset (MR-0106 here).'),
    79: dict(status='PARTIALLY_VERIFIED', status_reason='Crossref record of the data paper read; no deposit located',
             lic='CC BY 4.0 (article licence, Crossref)|M', unc_add='Article in European Union Politics (2023); the description says EU databases "contain almost no information" on the content of policies, which motivated the dataset. Deposit not located.'),
    80: dict(status='PARTIALLY_VERIFIED', status_reason='Crossref record read: published by Bruegel in "Bruegel Datasets"',
             maint='Bruegel (publisher, Crossref)|M', unc_add='Crossref types the record as journal-article; creators are empty. Content and files not examined.'),
    81: dict(status='PARTIALLY_VERIFIED', status_reason='Crossref record of the article read', lic='CC BY 4.0 (article licence, Crossref)|M',
             unc_add='Article in Political Research Exchange (2021). It remains unverified here that the article presents an R package (agent background knowledge).'),
    82: dict(status='PARTIALLY_VERIFIED', status_reason='Crossref record of the book chapter read', unc_add='Springer LNCS chapter; the data location was not searched.'),
    83: dict(status='VERIFIED', status_reason='Hugging Face record read directly', fmt='JSON per language and split|M',
             unc_add='76 files (data/<language>/{train,validation,test}.json); 24 languages; card links arXiv:2210.13448.'),
    84: dict(status='PARTIALLY_VERIFIED', status_reason='DataCite (arXiv) record of the preprint read', lic='CC BY 4.0 (arXiv record)|M',
             unc_add='Preprint; the corpus location was not searched.'),
    85: dict(status='PARTIALLY_VERIFIED', status_reason='Crossref record read: book published by Mykolas Romeris University',
             maint='Rokas, Aivaras; Rackevičienė, Sigita (Mykolas Romeris University)|M', unc_add='Crossref record of a book (2018); no data file located.'),
    86: dict(status='PARTIALLY_VERIFIED', status_reason='OpenAlex record read: technical report with an open-access PDF',
             unc_add='The report (PDF at pure.au.dk) describes the dataset; the dataset file was not located.'),
    87: dict(status='PARTIALLY_VERIFIED', status_reason='Crossref record of the data article read',
             theme='A collection of 3,776 judgments of the European Court of Justice since 1952, hand-coded (article abstract)|M',
             lic='CC BY-NC 4.0 (article licence, Crossref)|M', unc_add='Data article in the Journal of Law & Empirical Analysis (2025); the deposit was not located.'),
    88: dict(status='VERIFIED', status_reason='Hugging Face record read directly', fmt='Parquet|M',
             unc_add='546 files (metadata and text splits per language and sector); size category 1M-10M rows per tag.'),
    90: dict(status='VERIFIED', status_reason='Hugging Face record read directly', fmt='JSONL|M',
             unc_add='Five files; tagged source_datasets:joelniklaus/mapa.'),
    91: dict(status='VERIFIED', status_reason='Hugging Face record read directly', fmt='CSV|M',
             unc_add='Seven files including edge lists (train, validation, test).'),
    92: dict(status='VERIFIED', status_reason='Hugging Face record read directly', fmt='Parquet|M',
             theme='Judgments, orders, opinions and notices of the Court of Justice and General Court since 1954, from CELLAR, plus linked national-court decisions (card text)|M',
             unc_add='Files cases.parquet and fulltexts.parquet plus FIELDS.md; derived from Cellar according to the card.'),
    93: dict(status='VERIFIED', status_reason='Hugging Face record read directly', fmt='Parquet|M',
             unc_add='267 files (language pairs); card attributes the corpus to Philipp Koehn (University of Edinburgh); licence tag "unknown".'),
    94: dict(status='VERIFIED', status_reason='Hugging Face record read directly', fmt='Parquet|M',
             unc_add='73 files, one folder per language; card cites arXiv:2109.00904 (MultiEURLEX).'),
    95: dict(status='VERIFIED', status_reason='Hugging Face record read directly', fmt='JSONL|M',
             theme='500 fact patterns paired with holdings in European regulatory and court decisions (card text); three configurations|M',
             unc_add='Tagged source_datasets:GDPRHub; paper arXiv:2510.19365.'),
    96: dict(status='PARTIALLY_VERIFIED', status_reason='GitHub repository record read; the dataset itself was not located',
             unc_add='The repository (created 2020-10-28, no licence) uses the dataset; it holds analysis code.'),
    97: dict(status='VERIFIED', status_reason='GitHub repository record read directly', unc_add='Repository of extraction scripts (Apache-2.0), last push 2024-07-23.'),
    98: dict(status='VERIFIED', status_reason='GitHub repository record read directly', unc_add='Repository created 2026-09-01; no licence.'),
    99: dict(status='VERIFIED', status_reason='GitHub repository record read directly', unc_add='Repository last pushed 2022-02-27; no licence.'),
    100: dict(status='VERIFIED', status_reason='GitHub repository record read directly', unc_add='Repository created 2021-03-30; no licence.'),
    # Swedac group: seven entries that differ only by the ISO/IEC standard; same maintainer, same pattern
    54: dict(indiv='INDIVIDUATED', status='PARTIALLY_VERIFIED', status_reason='grouped into one resource; entries differ only by standard',
             unc_add='Treated as one resource with seven catalogue entries (one per standard). A national accreditation register with an EU link through notified bodies; the entries were read through the search response only.'),
    # sweep: DSC list read
    105: dict(name='Digital Services Coordinators (DSA)|P', maint=EC + '|P', desc='https://digital-strategy.ec.europa.eu/en/policies/dsa-dscs',
              url='https://digital-strategy.ec.europa.eu/en/policies/dsa-dscs', status='PARTIALLY_VERIFIED',
              status_reason='page read in the institutional sweep (SW-010)',
              unc_add='The page describes the Digital Services Coordinators and their role; whether it carries a downloadable list was not checked.'),
}

# --------------------------------------------------------------------------- (b) NEW RESOURCES: national ELI datasets
for key, prefix, label, unc in [
    ('ELI_DK', 'eli-european-legislation-identifier-denm', 'Denmark', 'Described as ELI metadata for legislation, decisions and documents of the Danish Ombudsman as published in Retsinformation.'),
    ('ELI_IT', 'eli-european-legislation-identifier-ital', 'Italy', 'Described as ELI metadata for legislation published on the Italian Official Gazette portal.'),
    ('ELI_LU', 'eli-european-legislation-identifier-luxe', 'Luxembourg', 'Described as covering all acts of the Luxembourg legislation portal (Memorial A and B); 11 ZIP distributions.'),
    ('ELI_FI', 'eli-european-legislation-identifier-finl', 'Finland', 'The record points to the Finlex data download service.'),
]:
    from_catalogue(key, prefix, 'DATASET', 'A', terr='NATIONAL_EU_CONNECTED',
                   unc=unc + ' National legislation metadata with an EU link through the ELI framework.')

# --------------------------------------------------------------------------- (b) NEW RESOURCES: EU institutional catalogues (set B)
from_catalogue('ACER_CEREMP', 'acer-remit-european-register-of-ma', 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('ACER_RDRC', 'acer-rdrc', 'INFRASTRUCTURE', 'B')
from_catalogue('ACER_IIAP', 'acer-iiap', 'INFRASTRUCTURE', 'B')
from_catalogue('ACER_RRM', 'acer-remit-list-of-registered-repo', 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('ACER_OMP', 'acer-remit-list-of-organised-marke', 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('ACER_SC', 'acer-remit-list-of-standard-contra', 'DATASET', 'B')

from_catalogue('EBA_DASH', family('eba', r'^EBA Risk Dashboard'), 'DATASET', 'B', elig='UNCERTAIN',
               unc='Supervisory risk indicators, not a register of decisions; eligibility uncertain.', note_family=' (reference period)')
from_catalogue('EBA_TRANSP', family('eba', r'^EU-wide transparency exercise results'), 'DATASET', 'B', elig='UNCERTAIN',
               unc='Bank-level supervisory disclosure data; eligibility uncertain.', note_family=' (year and template)')
from_catalogue('EBA_STRESS', family('eba', r'^(EU-wide stress test results|Stress test for bank|Capital Exercise for bank)'), 'DATASET', 'B', elig='UNCERTAIN',
               unc='Results of EU-wide stress tests and capital exercises, one record per bank and exercise; eligibility uncertain.', note_family=' (bank and exercise)')
from_catalogue('EBA_SUPV', family('eba', r'^Supervisory actions and measures'), 'ADMINISTRATIVE_REGISTER', 'B',
               unc='Title suggests supervisory actions and measures; content not examined.', note_family=' (reference period)')

from_catalogue('ESMA_FIRMS', 'list-of-investment-firms', 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('ESMA_CRA', 'list-of-registered-and-certified-c', 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('ESMA_TR', 'trade_reps', 'ADMINISTRATIVE_REGISTER', 'B', unc='The record lists no distribution.')
from_catalogue('ESMA_BMA', 'esma-benchmarks-administrators-reg', 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('ESMA_TCB', 'esma-third-country-benchmarks', 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('ESMA_SI', 'mifid_si', 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('ESMA_TIED', 'tied-agents', 'ADMINISTRATIVE_REGISTER', 'B', unc='The record lists no distribution.')
from_catalogue('ESMA_EUVECA', 'euveca_eusef', 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('ESMA_IFRS', 'ifrs-enforcement', 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('ESMA_CCP', 'non-eea_ccp', 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('ESMA_SFD', 'sfd', 'ADMINISTRATIVE_REGISTER', 'B', unc='The record lists no distribution.')
from_catalogue('ESMA_SS', 'short_selling', 'ADMINISTRATIVE_REGISTER', 'B')

from_catalogue('EIOPA_INS', 'register-of-insurance-undertakings', 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('EIOPA_IORP', 'register-of-institutions-for-occup', 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('EIOPA_IORPP', 'register-of-iorps-prudential-provi', 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('EIOPA_PENS', 'database-of-pension-plans-and-prod', 'DATASET', 'B')

for key, prefix, cat_ in [('ECHA_CAND', 'candidate-list-of-substances-of-ve', 'ADMINISTRATIVE_REGISTER'),
                          ('ECHA_AUTH', 'authorisation-list', 'ADMINISTRATIVE_REGISTER'),
                          ('ECHA_REC', 'echa-recommendation-for-inclusion-', 'ADMINISTRATIVE_REGISTER'),
                          ('ECHA_RESTR', 'restricted-list-reach', 'ADMINISTRATIVE_REGISTER'),
                          ('ECHA_CL', 'echa-classification-and-labelling-', 'ADMINISTRATIVE_REGISTER'),
                          ('ECHA_EC', 'ec-inventory', 'ADMINISTRATIVE_REGISTER'),
                          ('ECHA_PRE', 'pre-registered-substances-reach', 'ADMINISTRATIVE_REGISTER'),
                          ('ECHA_EVAL', 'dossier-evaluation-decisions', 'ADMINISTRATIVE_REGISTER'),
                          ('ECHA_CORAP', 'community-rolling-action-plan', 'ADMINISTRATIVE_REGISTER'),
                          ('ECHA_BPR', 'biocidal-products', 'ADMINISTRATIVE_REGISTER'),
                          ('ECHA_BAS', 'biocidal-products-list-of-active-s', 'ADMINISTRATIVE_REGISTER'),
                          ('ECHA_POP', 'persistent-organic-pollutants', 'ADMINISTRATIVE_REGISTER')]:
    from_catalogue(key, prefix, cat_, 'B', unc='Relation to the ECHA CHEM seed (MR-0032, inaccessible from this machine) not verified.')

from_catalogue('ERA_ERADIS', 'eradis-european-railway-agency-dat', 'ADMINISTRATIVE_REGISTER', 'B')
for key, prefix in [('ERA_SC', 'eradis-safety-certificates-databas'), ('ERA_LIC', 'eradis-licences-database'),
                    ('ERA_ECM', 'eradis-ecm-certificates-database'), ('ERA_CB', 'eradis-certification-bodies-databa'),
                    ('ERA_CSM', 'eradis-csm-assessment-body-databas'), ('ERA_NSA', 'eradis-national-safety-authorities')]:
    from_catalogue(key, prefix, 'ADMINISTRATIVE_REGISTER', 'B', indiv='CANDIDATE_NOT_INDEPENDENT',
                   unc='The title declares the record a module of ERADIS; counted with its parent, not as an independent resource.')
from_catalogue('ERA_ERATV', 'eratv-european-register-of-authori', 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('ERA_VKM', 'list-of-vehicle-keeper-markings-vk', 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('ERA_KG', 'era-knowledge-graph', 'INFRASTRUCTURE', 'B')
from_catalogue('ERA_ONT', 'era-ontology', 'STANDARD_OR_VOCABULARY', 'B')
from_catalogue('ERA_ERAIL', 'erail-investigations', 'DATASET', 'B', elig='UNCERTAIN', unc='Accident and incident investigation records; supervision link not examined.')

from_catalogue('EMSA_THETIS', 'thetis-port-state-control-informat', 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('EMSA_SSN', 'safe-sea-net', 'INFRASTRUCTURE', 'B')
from_catalogue('EMSA_EMCIP', 'accident-investigation-emcip', 'DATASET', 'B', elig='UNCERTAIN')
from_catalogue('EMSA_CO2', 'co2-emissions-data', 'DATASET', 'B', unc='Monitoring, reporting and verification data under the EU maritime emissions rules (agent reading of the title).')

from_catalogue('EFSA_OFT', 'openfoodtox-efsa-s-chemical-hazard', 'DATASET', 'B', elig='UNCERTAIN',
               unc='Scientific hazard database that supports regulatory risk assessment; whether it belongs to regulatory governance data is a scope question.')
from_catalogue('EFSA_PEST', 'pesticide-ecotoxicology-tier-1-end', 'DATASET', 'B', elig='UNCERTAIN',
               unc='Scientific database that supports pesticide authorisation; scope question as for OpenFoodTox.')

from_catalogue('EMA_MED', family('emea', r'^Medicine data:'), 'DATASET', 'B',
               unc='Tables of authorisation-related medicine data (EPAR, orphan designations, paediatric plans, referrals, PSUSA, herbal).', note_family=' (data topic)')
from_catalogue('EMA_EV', family('emea', r'suspected adverse drug reaction'), 'DATASET', 'B', unc='Pharmacovigilance database.')
from_catalogue('EMA_UPD', family('emea', r'^EU Veterinary Medicinal Product Database'), 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('EMA_SME', family('emea', r'SME Register'), 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('EMA_PD', family('emea', r'^Parallel Distribution'), 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('EMA_SPOR', family('emea', r'Substance, product, organisation and referential'), 'STANDARD_OR_VOCABULARY', 'B', elig='UNCERTAIN',
               unc='Reference master data for regulatory submissions.')

from_catalogue('EDPS_OPIN', 'edps-opinions', 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('EDPS_REG', 'edps-register-of-processing-operat', 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('CPVO_APP', 'cpvo-applications-and-titles-in-fo', 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('EUIPO_IP', family('oami', r'^IP rights in EU'), 'ADMINISTRATIVE_REGISTER', 'B', elig='UNCERTAIN',
               unc='Registers of EU trade marks and designs; intellectual-property registration is at the edge of regulatory governance data.', note_family=' (right type)')
from_catalogue('EFCA_JDP', family('cfca', r'Joint Deployment Plan'), 'DATASET', 'B',
               unc='Plans for joint fisheries control and inspection operations; record content (documents, maps) not opened.', note_family=' (sea area)')
from_catalogue('COMP_TAM', family('comp', r'^State Aid - Transparency - Public Search'), 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('COMP_SB', family('comp', r'^(Aid by|Agriculture aid|Share of aid|Block-exempted|Approved aid|Used aid|Sectoral and ad hoc|Non crisis|Fisheries aid|Aid to railways)'),
               'DATASET', 'B', elig='UNCERTAIN', unc='State-aid expenditure series (scoreboard); aggregate monitoring data.', note_family=' (series)')
from_catalogue('GROW_SMS', 'the-eu-single-market-scoreboard', 'DATASET', 'AB', elig='UNCERTAIN', unc='Governance performance indicators for single market rules.')
from_catalogue('GROW_POST', family('grow', r'[Pp]ostal'), 'DATASET', 'B', elig='UNCERTAIN',
               unc='Postal-services regulatory data series (historical, 2004-2011 in several titles).', note_family=' (indicator)')
from_catalogue('GROW_ECERTIS', 'ecertis', 'DATASET', 'B', elig='UNCERTAIN', unc='Certificates and attestations required in public procurement across Member States.')

for key, prefix, cat_ in [('SANTE_CLAIMS', 'u3yjqnr7wx2gjkbqmajsya', 'ADMINISTRATIVE_REGISTER'),
                          ('SANTE_FEEDADD', 'feed-additives', 'ADMINISTRATIVE_REGISTER'),
                          ('SANTE_RASFF', 'restored_rasff', 'ADMINISTRATIVE_REGISTER'),
                          ('SANTE_FOODADD', 'eu-food-additives', 'ADMINISTRATIVE_REGISTER'),
                          ('SANTE_FLAV', 'food-flavourings', 'ADMINISTRATIVE_REGISTER'),
                          ('SANTE_SMOKE', 'smoke-flavourings', 'ADMINISTRATIVE_REGISTER'),
                          ('SANTE_ENZ', 'gvhafrwlxgnvlvqovgxhlq', 'ADMINISTRATIVE_REGISTER'),
                          ('SANTE_FCM', 're1hukiczvl7dnpj7lj3eg', 'ADMINISTRATIVE_REGISTER'),
                          ('SANTE_NOVEL', 'xt4uwrpbr87xhm7ta3ffaw', 'ADMINISTRATIVE_REGISTER'),
                          ('SANTE_PEST', 'pesticides', 'ADMINISTRATIVE_REGISTER'),
                          ('SANTE_VAR', 'agricultural-vegetable-catalogue-n', 'ADMINISTRATIVE_REGISTER'),
                          ('SANTE_FRM', 'd8uawjykvujrmnfrfyedpw', 'ADMINISTRATIVE_REGISTER'),
                          ('SANTE_AUDIT', 'health-and-food-audits-and-analysi', 'DATASET')]:
    from_catalogue(key, prefix, cat_, 'B')

from_catalogue('FISMA_FSL', 'consolidated-list-of-persons-group', 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('FISMA_TRAVEL', 'consolidated-list-of-persons-subje', 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('TAXUD_AEO', 'authorised-economic-operator', 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('TAXUD_SEED', 'seed-system-for-exchange-of-excise', 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('TAXUD_EBTI', 'european-binding-tariff-informatio', 'ADMINISTRATIVE_REGISTER', 'B', elig='UNCERTAIN', unc='Binding tariff information rulings.')
from_catalogue('TAXUD_REX', 'the-registered-exporter-system', 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('TAXUD_VIES', 'vies-vat-information-exchange-syst', 'INFRASTRUCTURE', 'B', elig='UNCERTAIN', unc='VAT number validation service; administrative cooperation tool.')

from_catalogue('ENV_ECOLABEL', 'eu-ecolabel-products', 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('ENV_FLEGT', 'timber-imports-licences-and-enforc', 'DATASET', 'B', unc='Reports on licences and enforcement under the FLEGT regime.')
from_catalogue('ENV_TIMBER', 'illegally-harvested-timber-and-pro', 'DATASET', 'B', unc='Enforcement data under the Timber Regulation.')
from_catalogue('ENV_CITES', 'wildlife-trade-under-cites', 'DATASET', 'B')
from_catalogue('ENV_CITES_SZ', 'illegal-wildlife-trade-seizures-un', 'DATASET', 'B')
from_catalogue('ENV_SULPH', 'compliance-reports-on-suphur-conte', 'DATASET', 'B')
from_catalogue('ENV_IED', ['data-on-operating-hours-of-certain', 'data-on-fuel-used-by-combustions-b'], 'DATASET', 'B',
               unc='Data on derogations under the Industrial Emissions Directive (two records).', note_family=' (derogation data)')
from_catalogue('ENV_IMPL', family('env', r'^Implementation report'), 'DATASET', 'B', elig='UNCERTAIN',
               unc='Commission implementation reports and country fiches under environmental directives; documents rather than structured data.', note_family=' (directive)')
from_catalogue('MOVE_ASL', 'eu-air-safety-list', 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('ENER_RADD', 'radd-european-commission-radioacti', 'DATASET', 'B', elig='UNCERTAIN', unc='Radioactive discharges reported under Euratom rules.')
from_catalogue('SG_MEET', 'european-commission-meetings-with-', 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('SG_DPO', 'sg-dpo', 'ADMINISTRATIVE_REGISTER', 'B', elig='UNCERTAIN')
from_catalogue('RSB', family('rsb', r'.'), 'ADMINISTRATIVE_REGISTER', 'B',
               unc='Opinions and case lists of the Regulatory Scrutiny Board (better regulation oversight).', note_family=' (document series)')
from_catalogue('CONSIL_ACC', 'public-access-requests', 'ADMINISTRATIVE_REGISTER', 'B', unc='Marked [DISCONTINUED] in the catalogue title.')
from_catalogue('MARE_FLEET', 'the-community-fishing-fleet-regist', 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('AGRI_GI', family('agri', r'eAmbrosia'), 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('AGRI_PO', family('agri', r'^Inventory of recognised producer organisations'), 'ADMINISTRATIVE_REGISTER', 'B')
from_catalogue('JRC_MS', family('jrc', r'^European market surveillance of motor vehicles'), 'DATASET', 'B',
               unc='Emissions test datasets from market surveillance of vehicles; JRC records for 2019-2024.', note_family=' (year)')
from_catalogue('EP_DOCS', family('ep', r'^European Parliament - '), 'DATASET', 'A', indiv='GROUP_PENDING_SPLIT', elig='UNCERTAIN',
               unc='Parliamentary document series (declarations, questions, plenary and committee documents, minutes) listed in the catalogue; not split.',
               note_family=' (document series)')
from_catalogue('ELRC_LEG', family('cnect', r'^Unofficial Consolidated legislative texts'), 'CORPUS', 'A', indiv='GROUP_PENDING_SPLIT', elig='UNCERTAIN',
               unc='ELRC language resources catalogued by DG CNECT; this entry is one of several legal-text corpora (consolidated legislation, national legislation); not split.',
               note_family=' (language)')
from_catalogue('PO_OPEN', 'eu-open-data-portal-all-datase', 'CATALOGUE', 'AB', unc='Metadata of the EU Open Data Portal as a dataset.')

# --------------------------------------------------------------------------- (b) NEW RESOURCES: academic and other repositories
explicit('DEU_I', name='Decision making in the European Union 2003|M', maint='Thomson, R. et al. (DANS depositors)|M', cat='DATASET', set='A',
         terr='EU', hits=[find_hit('doi:10.17026/DANS-XJR-FGSG')], desc='https://doi.org/10.17026/DANS-XJR-FGSG',
         theme='Dataset on decision-making in the European Union (title); part of the DEU series (agent inference from the title)|I',
         unc='Found by a DANS Data Stations search; record not fetched. Relation to the later DEU datasets not verified.')
explicit('DEU_IV', name='DEU IV - Decision-Making in the European Union|M', maint='Bicchi, Nicolas; Arregui, Javier et al. (article authors)|M',
         cat='DATASET', set='A', terr='EU', hits=[find_hit('https://openalex.org/W7155551492')], desc='https://openalex.org/W7155551492',
         unc='Known only from an OpenAlex record (2026); deposit not located.')
explicit('INDEP_AGENCIES', name='Formal independence index of European Union agencies|M', maint='de Boer, Thijs (DANS depositor)|M',
         cat='DATASET', set='B', terr='EU', hits=[find_hit('doi:10.17026/DANS-X8U-M3DD')], desc='https://doi.org/10.17026/DANS-X8U-M3DD',
         status='PARTIALLY_VERIFIED', unc='Found through DANS and B2FIND (three B2FIND records for the same title); the DANS record was not fetched.')
explicit('AIACT_NCA', name='European Dataset of EU AI Act Implementation: National Competent Authorities|M',
         maint='Cabasés, Orlando et al. (OpenAlex record, 2026)|M', cat='DATASET', set='B', terr='NATIONAL_EU_CONNECTED',
         eu='National competent authorities designated under the EU AI Act (title)|M', hits=[find_hit('https://openalex.org/W7204453716')],
         desc='https://openalex.org/W7204453716', unc='Title truncated in the search response; deposit not located. A direct set-B candidate (authorities).')
explicit('AGENCY_RULEMAKING', name="Replication data - Shaping EU agencies' rulemaking: interest groups, national regulators...|M",
         maint='Joosen, Rik et al. (OpenAlex record)|M', cat='DATASET', set='B', terr='EU', hits=[find_hit('https://openalex.org/W4394404792')],
         desc='https://openalex.org/W4394404792', unc='Title truncated in the search response; deposit not located.')
explicit('EFSOLAW', name='EfSoLaw: a new data set on the evolution of soft law in the European Union|M', maint='Cappellina, Bartolomeo (article author)|M',
         cat='DATASET', set='A', terr='EU', hits=[find_hit('https://openalex.org/W3128240439')], desc='https://openalex.org/W3128240439',
         unc='Data article; deposit not located.')
explicit('INFRINGE_EU', name='Infringements in the European Union|M', maint='Niikawa, Sho; Corcaci, Andreea (DataCite creators)|M',
         cat='DATASET', set='B', terr='EU', hits=[find_hit('10.5281/zenodo.23187783')], desc='https://doi.org/10.5281/zenodo.23187783',
         status='PARTIALLY_VERIFIED', unc='Two DataCite records (versions) for the same title, 2026; Zenodo record not fetched.')
explicit('COMITOLOGY_CONTESTED', name='Contested comitology? The overlooked importance of the EU Commission (replication data)|M',
         maint='Finke, Daniel; Hansen, Jens (figshare depositors)|M', cat='DATASET', set='A', terr='EU',
         hits=[find_hit('10.6084/m9.figshare.14221704')], desc='https://doi.org/10.6084/m9.figshare.14221704', status='PARTIALLY_VERIFIED',
         unc='DataCite record seen through search only; files and period not read.')
explicit('IRISH_EU_LAW', name='EU Law before the Irish Superior Courts 2008-2018|M', maint='Maher, Imelda; Riordan, Rónán (Zenodo creators)|M',
         cat='DATASET', set='A', terr='NATIONAL_EU_CONNECTED', elig='UNCERTAIN', hits=[find_hit('10.5281/zenodo.3843265')],
         desc='https://doi.org/10.5281/zenodo.3843265', status='PARTIALLY_VERIFIED',
         eu='Irish superior-court decisions applying EU law (title)|M', unc='National case-law dataset, as MR-0065; Zenodo record not fetched.')
explicit('SALIENCE', name='Measuring Salience in EU Legislative Politics|M', maint='Warntjen, Andreas (Dataverse author)|M', cat='DATASET', set='A',
         terr='EU', hits=[find_hit('doi:10.7910/DVN/VPLNUF')], desc='https://doi.org/10.7910/DVN/VPLNUF', status='PARTIALLY_VERIFIED',
         unc='Dataverse record seen through search only.')
explicit('COUNCIL_VOTES2', name='Vote choices in the Council of the European Union 2010 to 2021|M', maint='Pourebrahimi, Arash et al. (OpenAlex record)|M',
         cat='DATASET', set='A', terr='EU', hits=[find_hit('https://openalex.org/W4417536599')], desc='https://openalex.org/W4417536599',
         unc='Known only from an OpenAlex record (2025); whether it is a dataset or an article was not checked.')
explicit('PROOFAML', name='ProofAML - European Union Sanctions & PEP Dataset|M', maint='ProofAML (OpenAlex record, 2026)|M', cat='DATASET', set='B',
         terr='EU', elig='UNCERTAIN', hits=[find_hit('https://openalex.org/W7204236018')], desc='https://openalex.org/W7204236018',
         unc='Appears to be a commercial compliance product; nature and terms not checked.')
explicit('EUROPARL_ORIG', name='Europarl: A Parallel Corpus for Statistical Machine Translation|M', maint='Koehn, Philipp (card attribution)|M',
         cat='CORPUS', set='A', terr='EU', elig='UNCERTAIN', origin='BACKWARD_FORWARD_DISCOVERY',
         found_in='https://huggingface.co/api/datasets/Helsinki-NLP/europarl',
         unc='Named in the card of the Hugging Face redistribution (MR-0093) as its origin; the original distribution was not located.')

# --------------------------------------------------------------------------- (b) NEW RESOURCES: institutional sweep
explicit('SMCS', name='Single Market Compliance Space (SMCS)|P', maint=EC + '|I', cat='INFRASTRUCTURE', set='B', terr='EU', sweep='SW-012',
         sweep_note='page title of the application that the ICSMS and NANDO addresses resolve to', origin='OTHER', status='PARTIALLY_VERIFIED',
         url='https://webgate.ec.europa.eu/single-market-compliance-space/', desc='https://webgate.ec.europa.eu/single-market-compliance-space/',
         unc='Known from the title and final address of two captures (ICSMS, NANDO); the application is a JavaScript shell and was not read.')
explicit('ICSMS', name='ICSMS - information and communication system for market surveillance|I', maint=EC + '|I', cat='INFRASTRUCTURE', set='B',
         terr='EU', sweep='SW-012', sweep_note='address registered for ICSMS redirected to SMCS', origin='OTHER',
         url='https://webgate.ec.europa.eu/icsms/', desc='https://webgate.ec.europa.eu/icsms/',
         unc='Name and role are agent background knowledge; the capture shows only that the address redirects to SMCS.')
explicit('SAFETY_GATE', name='Safety Gate: the EU rapid alert system for dangerous non-food products|P', maint=EC + '|I', cat='ADMINISTRATIVE_REGISTER', set='B',
         terr='EU_EEA_PLUS', sweep='SW-013', sweep_note='page title', origin='OTHER', status='PARTIALLY_VERIFIED',
         url='https://ec.europa.eu/safety-gate-alerts/screen/webReport', desc='https://ec.europa.eu/safety-gate-alerts/screen/webReport',
         unc='Only the page title was readable; the alert database is a JavaScript application. Maintainer inferred from the host.')
explicit('EUDAMED', name='EUDAMED|P', maint=EC + '|I', cat='ADMINISTRATIVE_REGISTER', set='B', terr='EU', sweep='SW-014', sweep_note='page title',
         origin='OTHER', url='https://ec.europa.eu/tools/eudamed/eudamed', desc='https://ec.europa.eu/tools/eudamed/eudamed',
         unc='Only the page title "EUDAMED" was readable. The expansion (European database on medical devices) and the role are agent knowledge.')
explicit('EPREL', name='EPREL Public website|P', maint=EC + '|I', cat='ADMINISTRATIVE_REGISTER', set='B', terr='EU', sweep='SW-015', sweep_note='page title',
         origin='OTHER', url='https://eprel.ec.europa.eu/screen/home', desc='https://eprel.ec.europa.eu/screen/home',
         unc='Only the page title was readable. The role (energy-labelling product registry) is agent knowledge.')
explicit('SANCTIONS_MAP', name='EU Sanctions Map|P', maint=EC + '|I', cat='INFRASTRUCTURE', set='B', terr='EU', sweep='SW-016', sweep_note='page title',
         origin='OTHER', url='https://www.sanctionsmap.eu/', desc='https://www.sanctionsmap.eu/',
         unc='Only the page title was readable; relation to the consolidated lists of the Commission (FISMA) not verified.')
explicit('UNION_REGISTER_MP', name='Union Register of medicinal products|P', maint='European Commission, Public Health|P', cat='ADMINISTRATIVE_REGISTER',
         set='B', terr='EU', sweep='SW-017', sweep_note='register home page', origin='OTHER', status='VERIFIED',
         url='https://ec.europa.eu/health/documents/community-register/html/index_en.htm',
         desc='https://ec.europa.eu/health/documents/community-register/html/index_en.htm', acc='WEB_SEARCH|P',
         unc='Home page read (links to authorised COVID-19 products and search). Export formats and terms not checked.')
explicit('REGPROF', name='Regulated Profession Database|P', maint=EC + '|I', cat='ADMINISTRATIVE_REGISTER', set='B', terr='EU', sweep='SW-020',
         sweep_note='page title', origin='OTHER', url='https://ec.europa.eu/growth/tools-databases/regprof/',
         desc='https://ec.europa.eu/growth/tools-databases/regprof/', unc='Only the page title was readable; the database is a JavaScript application.')
explicit('EEA_DATAHUB', name='Datahub (EEA)|P', maint='European Environment Agency|P', cat='INFRASTRUCTURE', set='B', terr='EU_EEA_PLUS', sweep='SW-022',
         sweep_note='page read', origin='OTHER', status='VERIFIED', elig='UNCERTAIN', url='https://www.eea.europa.eu/en/datahub',
         desc='https://www.eea.europa.eu/en/datahub',
         theme='Data and maps collected with national networks on topics and legislation related to the environment, climate and sustainability|P',
         unc='Environmental data hub; the share that relates to regulatory obligations was not examined.')
explicit('UNION_REGISTRY_ETS', name='Union Registry of the EU Emissions Trading System|P', maint=EC + ', Climate Action|P', cat='ADMINISTRATIVE_REGISTER',
         set='B', terr='EU_EEA_PLUS', sweep='SW-023', sweep_note='page read', origin='OTHER', status='VERIFIED',
         url='https://climate.ec.europa.eu/eu-action/eu-emissions-trading-system-eu-ets/union-registry_en',
         desc='https://climate.ec.europa.eu/areas-action/carbon-markets/eu-emissions-trading-system-eu-ets/union-registry_en',
         theme='Online database that keeps track of the ownership of allowances issued under the EU ETS|P',
         unc='The page describes the registry; public data pages and export were not examined.')
explicit('ESMA_INDEX', name='ESMA Databases and Registers|P', maint='European Securities and Markets Authority|P', cat='CATALOGUE', set='B', terr='EU',
         sweep='SW-029', sweep_note='index page read', origin='OTHER', status='VERIFIED',
         url='https://www.esma.europa.eu/publications-and-data/databases-and-registers',
         desc='https://www.esma.europa.eu/publications-and-data/databases-and-registers',
         theme='References to the registers and financial-market data that ESMA publishes|P',
         unc='Index of ESMA registers; which of them match the ESMA registers recorded from the catalogue was not compared.')
explicit('EIOPA_INDEX', name='EIOPA Tools and data|P', maint='European Insurance and Occupational Pensions Authority|P', cat='CATALOGUE', set='B',
         terr='EU', sweep='SW-030', sweep_note='index page read', origin='OTHER', status='VERIFIED',
         url='https://www.eiopa.europa.eu/tools-and-data_en', desc='https://www.eiopa.europa.eu/tools-and-data_en',
         theme='EIOPA data framework; central repository of data on insurance and pensions markets; tools and data pages|P',
         unc='Index page; individual registers not compared with the catalogue entries.')
explicit('CPVO_FINDER', name='CPVO Variety Finder|P', maint='Community Plant Variety Office|P', cat='ADMINISTRATIVE_REGISTER', set='B', terr='EU',
         sweep='SW-033', sweep_note='page read', origin='OTHER', status='VERIFIED',
         url='https://cpvo.europa.eu/en/applications-and-examinations/cpvo-variety-finder',
         desc='https://cpvo.europa.eu/en/applications-and-examinations/cpvo-variety-finder',
         theme='Search tool over registers of more than 70 countries, with Plant Breeders\' Rights data and a denomination similarity search|P',
         unc='Overlaps with the CPVO applications-and-titles database in the catalogue; not compared.')
explicit('SRB_DECISIONS', name='Single Resolution Board - Resolution Decisions|P', maint='Single Resolution Board|P', cat='ADMINISTRATIVE_REGISTER',
         set='B', terr='EU', sweep='SW-039', sweep_note='page read', origin='OTHER', status='VERIFIED',
         url='https://www.srb.europa.eu/en/content/resolution-decisions', desc='https://www.srb.europa.eu/en/content/resolution-decisions',
         theme='Resolution decisions of the Single Resolution Board, with the legal conditions for resolution explained|P',
         unc='Page of decisions; number of decisions, formats and export were not examined.')
explicit('BEREC_GAD', name='BEREC General Authorisation Database|P', maint='BEREC|P', cat='ADMINISTRATIVE_REGISTER', set='B', terr='EU_EEA_PLUS',
         sweep='SW-008', sweep_note='named under Tools on the BEREC home page', origin='OTHER',
         url='https://www.berec.europa.eu/en', desc='https://www.berec.europa.eu/en',
         unc='Named only as a tool on the BEREC home page; the database page was not opened.')
explicit('BEREC_NUM', name='BEREC Numbering database for extra-territorial use|P', maint='BEREC|P', cat='ADMINISTRATIVE_REGISTER', set='B',
         terr='EU_EEA_PLUS', sweep='SW-008', sweep_note='named under Tools on the BEREC home page', origin='OTHER',
         url='https://www.berec.europa.eu/en', desc='https://www.berec.europa.eu/en',
         unc='Named only as a tool on the BEREC home page; the database page was not opened.')
explicit('OMBUDSMAN', name='European Ombudsman - cases|P', maint='European Ombudsman|P', cat='ADMINISTRATIVE_REGISTER', set='B', terr='EU',
         sweep='SW-042', sweep_note='page title', origin='OTHER', url='https://www.ombudsman.europa.eu/en/cases',
         desc='https://www.ombudsman.europa.eu/en/cases', unc='Only the page title was readable; the cases database is a JavaScript application.')

# --------------------------------------------------------------------------- endpoints added to round-1 resources
ENDPOINTS += [
    (1, 'ACCESS_PORTAL', 'https://eur-lex.europa.eu/oj/direct-access.html', 'SEARCH_HIT', 'NO', False, 'Direct access to the Official Journal (sweep SW-045)'),
    (1, 'CATALOGUE_ENTRY', 'https://data.europa.eu/data/datasets/eu-case-law', 'SEARCH_HIT', 'NO', True, 'Catalogue entry "EU case-law": four HTML links to EUR-Lex collections (DEC-0004 rule)'),
    (1, 'CATALOGUE_ENTRY', 'https://data.europa.eu/data/datasets/eu-international-agreements', 'SEARCH_HIT', 'NO', True, 'Catalogue entry "International agreements": HTML links to EUR-Lex (DEC-0004 rule)'),
    (8, 'ACCESS_PORTAL', 'https://data.europarl.europa.eu/en/datasets', 'SEARCH_HIT', 'NO', True, 'Datasets listing of the Parliament portal (sweep SW-046); JavaScript shell'),
    (29, 'SEARCH_INTERFACE', 'https://webgate.ec.europa.eu/single-market-compliance-space/', 'PRIMARY_PAGE', 'NO', True, 'Final address of the NANDO link (redirect)'),
    (10, 'DESCRIPTION_PAGE', 'https://www.consilium.europa.eu/en/documents-publications/public-register/', 'PRIMARY_PAGE', 'UNKNOWN', False, 'Second attempt through the sweep (SW-047): HTTP 403 again'),
    (105, 'DESCRIPTION_PAGE', 'https://digital-strategy.ec.europa.eu/en/policies/dsa-dscs', 'PRIMARY_PAGE', 'NO', False, 'Page on the Digital Services Coordinators (sweep SW-010)'),
]


def _repo_endpoints():
    """Add the file or API address that a first-bytes inspection will read, for repositories whose record was fetched.
    The record is read from the stored capture; nothing here touches the network."""
    cap = ROOT / 'mapping' / 'evidence' / 'captures'
    log_path = cap / 'CAPTURE_LOG.jsonl'
    if not log_path.exists():
        return
    import verify_resources as vr
    latest = {}
    for line in log_path.read_text(encoding='utf-8').splitlines():
        rec = json.loads(line)
        if re.match(r'^MR-\d{4}$', rec['record_id']) and rec['outcome'] == 'CAPTURED' and rec.get('raw_file'):
            latest[int(rec['record_id'][3:])] = rec
    data_ext = ('.csv', '.tsv', '.tab', '.json', '.jsonl', '.xml', '.xlsx', '.xls', '.txt', '.parquet', '.dta', '.sas7bdat', '.zip', '.xz', '.gz', '.rds')
    for n, rec in sorted(latest.items()):
        host = rec['original_url'].split('/')[2]
        kind = {'zenodo.org': 'zenodo', 'dataverse.harvard.edu': 'dataverse', 'huggingface.co': 'hf', 'api.github.com': 'github'}.get(host)
        if not kind:
            continue
        data = json.loads((cap / rec['raw_file']).read_bytes())
        d = vr.digest(kind, data)
        url = None
        if kind == 'zenodo':
            files = [f for f in d.get('files', []) if f.get('url') and (f.get('size') or 0) > 0]
            files.sort(key=lambda f: (0 if str(f['name']).lower().endswith(data_ext) else 1, f['size']))
            url = files[0]['url'] if files else None
        elif kind == 'dataverse':
            files = [f for f in d.get('files', []) if f.get('id') and not f.get('restricted')]
            files.sort(key=lambda f: (0 if (f.get('tabular') or str(f['name']).lower().endswith(data_ext)) else 1, f.get('size') or 0))
            url = f"https://dataverse.harvard.edu/api/access/datafile/{files[0]['id']}" if files else None
        elif kind == 'hf':
            names = [f['name'] for f in d.get('files', []) if f.get('name') and str(f['name']).lower().endswith(data_ext)]
            names.sort(key=lambda s: (s.count('/'), len(s)))
            url = f"https://huggingface.co/datasets/{d['title']}/resolve/main/{names[0]}" if names else None
        elif kind == 'github':
            url = f"https://api.github.com/repos/{d['title']}/contents"
        if url:
            role = 'API' if kind == 'github' else 'BULK_DOWNLOAD'
            ENDPOINTS.append((n, role, url, 'API_METADATA', 'NO', False,
                              'File chosen for a first-bytes inspection from the repository record (smallest data-like file)' if kind != 'github'
                              else 'Repository contents listing, for a first-bytes inspection'))


_repo_endpoints()
ENDPOINTS += [
    (99, 'BULK_DOWNLOAD', 'https://raw.githubusercontent.com/martinhengge/GDPR/HEAD/GDPR%20Violations%20and%20Sanctions.csv', 'API_METADATA', 'NO', False,
     'File named in the repository contents listing (719,474 bytes per the listing); chosen for a first-bytes inspection'),
    (100, 'BULK_DOWNLOAD', 'https://raw.githubusercontent.com/sandykramb/GDPR-fines-Dataset/HEAD/GDPR%20Dataset.csv', 'API_METADATA', 'NO', False,
     'File named in the repository contents listing (310,583 bytes per the listing); chosen for a first-bytes inspection'),
]

# --------------------------------------------------------------------------- relations
# (source, type, target, confidence, status, basis, evidence handles, justification); numbers or keys
R = lambda x: K[x] if isinstance(x, str) else x  # noqa: E731
_REL = [
    (29, 'part_of', 'SMCS', 'MEDIUM', 'CANDIDATE', 'PRIMARY_PAGE', ['C:https://ec.europa.eu/growth/tools-databases/nando'],
     'The NANDO address redirects to the Single Market Compliance Space application (capture final address). Whether NANDO is a module of SMCS or only reached through it is not stated.'),
    ('ICSMS', 'part_of', 'SMCS', 'MEDIUM', 'CANDIDATE', 'PRIMARY_PAGE', ['C:https://webgate.ec.europa.eu/icsms/'],
     'The ICSMS address redirects to the SMCS application (capture final address).'),
    ('ERA_SC', 'part_of', 'ERA_ERADIS', 'MEDIUM', 'SUPPORTED', 'API_METADATA', ['S:SR-G2-068'], 'Catalogue title "ERADIS - Safety Certificates Database".'),
    ('ERA_LIC', 'part_of', 'ERA_ERADIS', 'MEDIUM', 'SUPPORTED', 'API_METADATA', ['S:SR-G2-068'], 'Catalogue title "ERADIS - Licences Database".'),
    ('ERA_ECM', 'part_of', 'ERA_ERADIS', 'MEDIUM', 'SUPPORTED', 'API_METADATA', ['S:SR-G2-068'], 'Catalogue title "ERADIS - Entity in Charge of Maintenance Certificates Database".'),
    ('ERA_CB', 'part_of', 'ERA_ERADIS', 'MEDIUM', 'SUPPORTED', 'API_METADATA', ['S:SR-G2-068'], 'Catalogue title "ERADIS - Certification bodies database".'),
    ('ERA_CSM', 'part_of', 'ERA_ERADIS', 'MEDIUM', 'SUPPORTED', 'API_METADATA', ['S:SR-G2-068'], 'Catalogue title "ERADIS - CSM Assessment Body Database".'),
    ('ERA_NSA', 'part_of', 'ERA_ERADIS', 'MEDIUM', 'SUPPORTED', 'API_METADATA', ['S:SR-G2-068'], 'Catalogue title "ERADIS - National Safety Authorities and National Investigation Bodies".'),
    ('DEU_IV', 'successor_of', 78, 'LOW', 'CANDIDATE', 'AGENT_INFERENCE', ['S:SR-G2-177'], 'Title suggests the fourth DEU dataset; the 2012 data article is assumed to present an earlier DEU wave (agent knowledge).'),
    ('DEU_I', 'overlaps_with', 78, 'LOW', 'CANDIDATE', 'AGENT_INFERENCE', ['S:SR-G2-162'], 'Same research programme (decision-making in the EU); content not compared.'),
    (92, 'derived_from', 2, 'MEDIUM', 'CANDIDATE', 'API_METADATA', ['S:SR-G2-048'], 'The card title reads "CJEU / CELLAR Case Law"; whether the data come from Cellar queries or the EUR-Lex site is not stated in the text read.'),
    (58, 'derived_from', 1, 'HIGH', 'SUPPORTED', 'API_METADATA', ['S:SR-G2-046'], 'Card: "large text resources from EURLEX"; the dataset is named after the source.'),
    (88, 'derived_from', 1, 'HIGH', 'SUPPORTED', 'API_METADATA', ['S:SR-G2-046'], 'Card: legal documents "scrapped from the EURLEX website".'),
    (83, 'derived_from', 1, 'MEDIUM', 'CANDIDATE', 'API_METADATA', ['S:SR-G2-046'], 'Card: based on human-written summaries of EU legal acts; the summaries are published through EUR-Lex (agent knowledge).'),
    ('ELI_IT', 'overlaps_with', 43, 'LOW', 'CANDIDATE', 'AGENT_INFERENCE', ['S:SR-G2-005'], 'Both are ELI metadata sets; scopes differ (national gazette versus EUR-Lex).'),
    ('ESMA_INDEX', 'catalogues', 'ESMA_FIRMS', 'LOW', 'CANDIDATE', 'AGENT_INFERENCE', ['C:https://www.esma.europa.eu/publications-and-data/databases-and-registers'],
     'The index page lists ESMA registers; that this register is among them was not checked by name.'),
]
for s, t, d, c, st, b, h, j in _REL:
    RELATIONS.append((R(s), t, R(d), c, st, b, h, j))

# --------------------------------------------------------------------------- decisions
DECISIONS += [
    ('IDENTITY', 'MR-0003;MR-0007', 'EU03 and EU07 stay distinct after a second, independent capture of the ELDS page and a third request to the dump address.',
     'The ELDS page was captured again in round 2 (same SHA-256 as in G1-READY). The catalogue entry "eur-lex-data-dump" (publisher: Publications Office) is a third description of the dump. The dump address answered HTTP 401 again; no authentication was attempted.',
     ['C:https://data.europa.eu/en/ELDS', 'H:G1', 'C:https://datadump.publications.europa.eu/']),
    ('TAXONOMY', 'ALL', 'Amendment A01 separates Level I (data) from Level II (infrastructure) and reports the two counts separately; no row is removed or reclassified retrospectively.',
     'See mapping/protocol/AMENDMENT_A01_DATA_VS_INFRASTRUCTURE_v1_0.md. The levels are derived from the existing category column.', []),
    ('INDIVIDUATION', 'CATALOGUE_FAMILIES', 'A catalogue family (records that differ only by instance label such as bank, year, language or country-neutral series) is one resource; records whose title declares them a module of a named system are counted with their parent.',
     'Applied to EBA stress tests and transparency exercises, ERADIS modules, EUIPO series, EFCA deployment plans, EMA medicine data, JRC vehicle datasets, the Swedac lists and others. The unit therefore follows each maintainer\'s own catalogue granularity, which differs between maintainers.',
     ['S:SR-G2-061', 'S:SR-G2-068']),
    ('SCREENING', 'EU_CATALOGUES', 'In the EU institutional catalogues, entries were individuated when they are registers or databases of regulated entities, authorisations, decisions, sanctions or enforcement, or lists with legal effect. Market-data systems, statistics series, reports and documents were not individuated, with exceptions flagged UNCERTAIN.',
     'Applies to ESMA (FIRDS, FITRS, prospectuses, position reporting, net short positions not individuated), EIOPA statistics, ECDC, Frontex, Europol, FRA, EASO, LISA, OSHA and ECA (not recorded).',
     ['S:SR-G2-064', 'S:SR-G2-065']),
    ('SCREENING', 'DEU_FREE_TEXT', 'The twenty-three thematic free-text queries across all data.europa.eu catalogues (SR-G2-119 to SR-G2-141) produced records of national and local bodies almost exclusively and no EU-level register that the catalogue enumeration had not already found, except the JRC market-surveillance datasets.',
     'Free text over the whole catalogue is dominated by national and local portals; enumerating the EU institutional catalogues was the productive route.', ['S:SR-G2-119']),
    ('NEGATIVE_RESULT', 'SW_FAILED', 'Fourteen institutional sweep requests failed (404, 403 or certificate verification errors on three hosts). They are access failures of addresses proposed by the agent or blocked to the client, not evidence that those bodies publish no register.',
     'SW-003, SW-004, SW-019, SW-021, SW-025, SW-026, SW-027, SW-028, SW-031, SW-032, SW-034, SW-038, SW-040 and SW-047 (the last is a second attempt for a round-1 failure).', []),
    ('NOT_INDIVIDUATED', 'SW_NETWORKS', 'Pages describing networks and bodies (ECN, CPC network, EDPB members, European Accreditation, EPPO, ELA, EASA publications, ECA publications, CJEU reports) were read and not individuated: they describe organisations, not data resources.',
     'No downloadable list or register was identified on those pages in this round.', ['C:https://competition-policy.ec.europa.eu/european-competition-network_en']),
    ('SCREENING', 'EU_AGENCY_LIST', 'The two official list pages of EU bodies (SW-001, SW-002) could not be used as a complete list: they are paginated or dynamic and only the first entries were readable. The data.europa.eu catalogue enumeration (212 catalogues, 124 labelled with the country EUROPE, which include EU institutions and agencies and some projects) was used as the working list.',
     'Coverage of EU bodies is therefore measured against the catalogue, not against an official register of bodies.', ['C:https://european-union.europa.eu/institutions-law-budget/institutions-and-bodies/search-all-eu-institutions-and-bodies_en']),
    ('EVIDENCE_CONFLICT', 'MR-0003', 'The description conflict on the dump scope (CELEX sector 3 versus sectors 2, 3 and 4) is unchanged; the access address registered by the catalogue entry (/dashboard) differs from the one on the ELDS page (root).',
     'Both addresses require the EU Login account according to the catalogue text; neither was authenticated.', ['S:SR-G2-001']),
    ('IDENTITY', 'MR-0092;MR-0058;MR-0088', 'Three Hugging Face datasets that describe themselves as derived from EUR-Lex or Cellar are recorded as derived resources with their stated source.',
     'The statements come from the dataset cards (API metadata). They show derivation claimed by the depositors, not verified lineage.', ['S:SR-G2-046', 'S:SR-G2-048']),
    ('NOT_INDIVIDUATED', 'EFSA;ECDC;FRONTEX;ECA', 'Scientific, surveillance and report series from EFSA (except two UNCERTAIN databases), ECDC, Frontex and ECA are not individuated.',
     'They are not registers or decisions under a regulatory regime; the scope rule for such series remains an open decision (D1).', ['S:SR-G2-070', 'S:SR-G2-079']),
    ('ACCESS', 'ROUND2_FETCH', 'Eleven Zenodo record requests failed in the first fetch pass because the address builder put the DOI into the record address (an agent defect); they were corrected and requested again. Seven DOI requests went first to DataCite, answered 404 because those DOIs are registered at Crossref, and were repeated there. All failed requests stay in the capture log.',
     "The first-pass failures (HTTP 404) are defects or routing choices of the agent's tool, not facts about the resources.", []),
]

# --------------------------------------------------------------------------- institutional sweep notes
SWEEP_NOTES = {
    'SW-001': ([], 'Official list of EU institutions and bodies; only the first entries were readable (paginated listing); see DEC on the working list.'),
    'SW-002': ([], 'Types of institutions and bodies; navigation page with links to agency lists; no data resource.'),
    'SW-003': ([], 'Certificate verification failed from this machine; not read.'),
    'SW-004': ([], 'HTTP 404 on an address proposed by the agent.'),
    'SW-005': ([], 'Page on the European Competition Network; no data resource.'),
    'SW-006': ([], 'Page on the Consumer Protection Cooperation network; no data resource.'),
    'SW-007': ([], 'Members of the EDPB; the decisions register is the seed MR-0025.'),
    'SW-008': (['BEREC_GAD', 'BEREC_NUM'], 'Home page lists tools: General Authorisation Database, Information Sharing Portal, Numbering DB for extra-territorial use.'),
    'SW-009': (['ACER_CEREMP', 'ACER_RDRC'], 'Home page: news only; the REMIT registers were found through the catalogue.'),
    'SW-010': ([105], 'Page on Digital Services Coordinators read.'),
    'SW-011': ([], 'European Accreditation association page; no downloadable list of accredited bodies identified.'),
    'SW-012': (['SMCS', 'ICSMS'], 'ICSMS address resolves to the Single Market Compliance Space application.'),
    'SW-013': (['SAFETY_GATE'], 'Title only; application not readable without JavaScript.'),
    'SW-014': (['EUDAMED'], 'Title only; application not readable without JavaScript.'),
    'SW-015': (['EPREL'], 'Title only; application not readable without JavaScript.'),
    'SW-016': (['SANCTIONS_MAP'], 'Title only; application not readable without JavaScript.'),
    'SW-017': (['UNION_REGISTER_MP'], 'Register home page read.'),
    'SW-018': ([], 'The server answered with a "temporarily unavailable" page; not read. Not evidence about the database.'),
    'SW-019': ([], 'HTTP 404 on an address proposed by the agent.'),
    'SW-020': (['REGPROF'], 'Title only; application not readable without JavaScript.'),
    'SW-021': ([], 'HTTP 404 on an address proposed by the agent.'),
    'SW-022': (['EEA_DATAHUB'], 'Data hub page read.'),
    'SW-023': (['UNION_REGISTRY_ETS'], 'Page on the Union Registry read.'),
    'SW-024': ([], 'EASA general publications list: documents; no register identified on this page.'),
    'SW-025': ([], 'HTTP 404 on an address proposed by the agent; EFSA data found through the catalogue.'),
    'SW-026': ([], 'HTTP 404 on an address proposed by the agent; EMA data found through the catalogue.'),
    'SW-027': ([], 'Certificate verification failed again (same as EU32); not read.'),
    'SW-028': ([], 'HTTP 404 on an address proposed by the agent; EBA data found through the catalogue.'),
    'SW-029': (['ESMA_INDEX'], 'Index of ESMA databases and registers read.'),
    'SW-030': (['EIOPA_INDEX'], 'EIOPA tools and data index read.'),
    'SW-031': ([], 'HTTP 404 on an address proposed by the agent.'),
    'SW-032': ([], 'HTTP 403 to the client; EUIPO series found through the catalogue.'),
    'SW-033': (['CPVO_FINDER'], 'Variety Finder page read.'),
    'SW-034': ([], 'HTTP 404 on an address proposed by the agent; ERA registers found through the catalogue.'),
    'SW-035': (['EMSA_THETIS'], 'EMSA safety page read; THETIS found through the catalogue.'),
    'SW-036': ([], 'Surveillance atlas of infectious diseases: health surveillance data, not recorded (see decision).'),
    'SW-037': ([], 'European Labour Authority home page; no data resource identified.'),
    'SW-038': ([], 'HTTP 404 on an address proposed by the agent.'),
    'SW-039': (['SRB_DECISIONS'], 'Resolution decisions page read.'),
    'SW-040': ([], 'Certificate verification failed from this machine; not read.'),
    'SW-041': ([], 'EPPO home page; news only.'),
    'SW-042': (['OMBUDSMAN'], 'Title only; application not readable without JavaScript.'),
    'SW-043': ([], 'ECA publications page: documents.'),
    'SW-044': (['COMP_TAM'], 'Language-selection page of the State aid transparency application; the register itself was found through the catalogue.'),
    'SW-045': ([1], 'Direct access to the Official Journal; endpoint of EUR-Lex.'),
    'SW-046': ([8], 'Datasets listing of the Parliament portal; JavaScript shell; endpoint of the Parliament API resource.'),
    'SW-047': ([], 'HTTP 403 to the client (second attempt after round 1).'),
    'SW-048': ([], 'CJEU annual-report page; not a data resource.'),
}

# --------------------------------------------------------------------------- LYNX D2.8 Table 6 as a reference list
_ROWS = [
    # source, area, url, law, case law, eli, ecli, access, scope, match, matched, basis, note
    ('BOTH', 'European Union', 'https://eur-lex.europa.eu/', 'YES', 'YES', 'ELI', 'ECLI', 'EU languages; web', 'EU_LEVEL', 'MATCHED', 1, 'same address and name', ''),
    ('BOTH', 'European Union', 'https://data.europa.eu/euodp/es/data/dataset/official-journals-of-the-european-union-in-english', 'YES', 'NO', 'ELI', '', 'API; Formex', 'EU_LEVEL', 'MATCHED_AS_ENDPOINT', 4, 'catalogue entry of the per-language Official Journal list (DEC-0005)', 'Round 1 treats the per-language and annual entries as distributions of one resource.'),
    ('BOTH', 'European Union', 'https://data.europa.eu/euodp/es/data/dataset/eu-case-law', 'NO', 'YES', '', 'ECLI', 'API', 'EU_LEVEL', 'MATCHED_AS_ENDPOINT', 1, 'catalogue entry "EU case-law": HTML links to EUR-Lex (DEC-0004 rule)', 'Not a separate resource in our unit of analysis.'),
]
_NATIONAL = [
    ('Austria', 'https://www.ris.bka.gv.at/', 'YES', 'YES', 'ELI_ID', 'ECLI_ID', 'API'),
    ('Belgium', 'https://belgiumlex.be/', 'YES', 'YES', 'ELI_ID', 'ECLI_ID', ''),
    ('Bulgaria', 'https://dv.parliament.bg/DVWeb/index.faces', 'YES', 'NO', '', '', ''),
    ('Bulgaria', 'https://legalacts.justice.bg/', 'NO', 'YES', '', 'ECLI_ID', ''),
    ('Croatia', 'http://nn.hr/', 'YES', 'NO', 'ELI_ID', '', ''),
    ('Croatia', 'https://sudskapraksa.csp.vsrh.hr/home', 'NO', 'YES', '', 'ECLI_ID', ''),
    ('Cyprus', 'http://www.cylaw.org/', 'YES', 'YES', '', '', ''),
    ('Czech Republic', 'https://aplikace.mvcr.cz/sbirka-zakonu/', 'YES', 'NO', '', '', ''),
    ('Czech Republic', 'http://www.nsoud.cz', 'NO', 'YES', '', 'ECLI_ID', ''),
    ('Denmark', 'https://www.retsinformation.dk/', 'YES', 'NO', 'ELI_ID', '', ''),
    ('Denmark', 'https://domstol.dk/', 'NO', 'YES', '', '', ''),
    ('Estonia', 'https://www.riigiteataja.ee/', 'YES', 'YES', '', 'ECLI_ID', ''),
    ('Finland', 'http://www.finlex.fi/', 'YES', 'YES', 'ELI_ID', 'ECLI', ''),
    ('France', 'https://www.legifrance.gouv.fr/', 'YES', 'YES', 'ELI_ID', 'ECLI_ID', 'API'),
    ('Germany', 'https://www.bgbl.de/', 'YES', 'NO', '', '', ''),
    ('Germany', 'https://www.bundesverfassungsgericht.de/', 'NO', 'YES', '', 'ECLI_ID', ''),
    ('Greece', 'http://www.et.gr/index.php/', 'YES', 'NO', '', '', ''),
    ('Greece', 'http://www.adjustice.gr/', 'NO', 'YES', '', 'ECLI_ID', ''),
    ('Greece', 'http://legislation.di.uoa.gr/', 'YES', 'NO', 'ELI', '', 'SPARQL endpoint'),
    ('Hungary', 'http://www.njt.hu/', 'YES', 'NO', '', '', ''),
    ('Hungary', 'https://birosag.hu/birosagi-hatarozatok-gyujtemenye', 'NO', 'YES', '', 'ECLI_ID', ''),
    ('Ireland', 'http://www.irishstatutebook.ie/', 'YES', 'NO', 'ELI_ID', '', ''),
    ('Ireland', 'https://courts.ie/', 'NO', 'YES', '', '', ''),
    ('Italy', 'https://www.normattiva.it/', 'YES', 'NO', 'ELI_ID', '', ''),
    ('Italy', 'https://www.gazzettaufficiale.it/', 'YES', 'NO', 'ELI_ID', '', ''),
    ('Italy', 'http://pst.giustizia.it/PST/', 'NO', 'YES', '', 'ECLI_ID', ''),
    ('Italy', 'http://www.italgiure.giustizia.it/', 'NO', 'YES', '', 'ECLI_ID', ''),
    ('Latvia', 'https://likumi.lv/', 'YES', 'NO', '', '', ''),
    ('Latvia', 'https://manas.tiesas.lv/eTiesas/', 'NO', 'YES', '', 'ECLI_ID', ''),
    ('Lithuania', 'https://www.e-tar.lt/portal/lt/index', 'YES', 'NO', '', '', ''),
    ('Lithuania', 'http://liteko.teismai.lt/viesasprendimupaieska/', 'NO', 'YES', '', '', ''),
    ('Luxembourg', 'http://legilux.public.lu/', 'YES', 'NO', 'ELI_ID', '', 'SPARQL endpoint; bulk'),
    ('Luxembourg', 'https://justice.public.lu/fr/jurisprudence/jurisprudence-judoc.html', 'NO', 'YES', '', 'ECLI', ''),
    ('Malta', 'https://justice.gov.mt/', 'YES', 'NO', '', '', ''),
    ('Malta', 'https://ecourts.gov.mt/onlineservices/Judgements', 'NO', 'YES', '', 'ECLI_ID', ''),
    ('Netherlands', 'https://www.officielebekendmakingen.nl/', 'YES', 'NO', '', '', 'API'),
    ('Netherlands', 'https://uitspraken.rechtspraak.nl/', 'NO', 'YES', '', 'ECLI_ID', ''),
    ('Poland', 'http://isip.sejm.gov.pl/', 'YES', 'NO', '', '', ''),
    ('Poland', 'http://orzeczenia.nsa.gov.pl/cbo/query', 'NO', 'YES', '', '', ''),
    ('Portugal', 'https://dre.pt/', 'YES', 'NO', 'ELI', '', ''),
    ('Portugal', 'http://www.dgsi.pt/', 'NO', 'YES', '', 'ECLI_ID', ''),
    ('Romania', 'http://legislatie.just.ro/', 'YES', 'NO', '', '', ''),
    ('Romania', 'http://www.rolii.ro/', 'NO', 'YES', '', 'ECLI_ID', ''),
    ('Slovakia', 'https://obcan.justice.sk/', 'YES', 'NO', '', '', ''),
    ('Slovakia', 'https://obcan.justice.sk/infosud/-/infosud/zoznam/sud', 'NO', 'YES', '', 'ECLI_ID', ''),
    ('Slovenia', 'http://www.pisrs.si/Pis.web/', 'YES', 'YES', '', 'ECLI_ID', ''),
    ('Slovenia', 'http://www.sodnapraksa.si/', 'NO', 'YES', '', '', ''),
    ('Spain', 'https://www.boe.es/', 'YES', 'NO', 'ELI_ID', '', 'API'),
    ('Spain', 'http://www.poderjudicial.es/search/indexAN.jsp', 'NO', 'YES', '', 'ECLI_ID', ''),
    ('Sweden', 'https://lagrummet.se/', 'YES', 'YES', '', '', ''),
    ('United Kingdom (not EU)', 'http://www.legislation.gov.uk/', 'YES', 'NO', '', '', ''),
    ('United Kingdom (not EU)', 'https://www.bailii.org/', 'NO', 'YES', '', '', ''),
    ('United Kingdom (not EU)', 'https://www.supremecourt.uk/decided-cases/', 'NO', 'YES', '', '', ''),
]
_RELATED = {  # url -> resource key or number: the catalogue entry describes ELI metadata of this very portal
    'http://www.irishstatutebook.ie/': 44, 'https://www.retsinformation.dk/': 'ELI_DK', 'https://www.gazzettaufficiale.it/': 'ELI_IT',
    'http://legilux.public.lu/': 'ELI_LU', 'http://www.finlex.fi/': 'ELI_FI',
}
LYNX_ROWS = []
for src, area, url, law, case, eli, ecli, access, scope, match, matched, basis, note in _ROWS:
    LYNX_ROWS.append(dict(source=src, area=area, url=url, law=law, case_law=case, eli=eli, ecli=ecli, access=access, scope=scope,
                          match=match, matched=f'MR-{matched:04d}', basis=basis, note=note))
for area, url, law, case, eli, ecli, access in _NATIONAL:
    if area.startswith('United Kingdom'):
        scope, match, note = 'NON_EU', 'NOT_APPLICABLE', 'Not an EU Member State; outside the geographic rule.'
        matched, basis = '', ''
    elif url in _RELATED:
        scope, match = 'EU_LINK_VIA_ELI_ONLY', 'RELATED'
        key = _RELATED[url]
        matched = f'MR-{(K[key] if isinstance(key, str) else key):04d}'
        basis = 'catalogue record describes the ELI metadata of this portal'
        note = 'The portal itself is not a resource in the base; only the ELI metadata set hosted by the Publications Office is.'
    else:
        scope, match, matched, basis = 'EU_LINK_VIA_ELI_ONLY', 'ABSENT_SCOPE_OPEN', '', ''
        note = 'National legal-publication portal; reachable through N-Lex (MR-0019). Entry depends on decision D7 (national legal-publication portals).'
    LYNX_ROWS.append(dict(source='D2.8', area=area, url=url, law=law, case_law=case, eli=eli, ecli=ecli, access=access, scope=scope,
                          match=match, matched=matched, basis=basis, note=note))

SWEEP_NOTES = {sid: ([K[x] if isinstance(x, str) else x for x in keys], note) for sid, (keys, note) in SWEEP_NOTES.items()}

SHARED_URL_JUSTIFICATIONS = {
    'https://www.berec.europa.eu/en': 'Two BEREC tools are named on the same home page; their own pages were not opened.',
    'https://webgate.ec.europa.eu/single-market-compliance-space/': 'Address of the SMCS application, also the final address of the NANDO link (MR-0029).',
}
