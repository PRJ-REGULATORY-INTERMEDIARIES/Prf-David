#!/usr/bin/env python3
"""Opt-in raw query to data.europa.eu documented hub search endpoint.
No data are labeled as eligible. Requires internet access. Uses only stdlib.
"""
import argparse
from datetime import datetime, timezone
import hashlib, json
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request,urlopen
from urllib.error import HTTPError,URLError
import time

ROOT=Path(__file__).resolve().parents[1]
BASE='https://data.europa.eu/api/hub/search/search'

def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--query',required=True)
 ap.add_argument('--limit',type=int,default=25)
 ap.add_argument('--query-id',default='ADHOC')
 ap.add_argument('--timeout',type=int,default=25)
 args=ap.parse_args()
 if args.limit<1 or args.limit>1000:ap.error('--limit must be between 1 and 1000')
 url=BASE+'?'+urlencode({'q':args.query,'filters':'dataset','limit':args.limit,'page':0})
 req=Request(url,headers={'Accept':'application/json','User-Agent':'ResearchScopingReview/1.0 (manual research request)'})
 try:
  with urlopen(req,timeout=args.timeout) as resp: raw=resp.read(); status=resp.status
  obj=json.loads(raw)
 except (HTTPError,URLError,TimeoutError,ValueError) as ex:
  print(f'API request failed (do not count as zero search results): {type(ex).__name__}: {ex}')
  return 2
 out=ROOT/'data'/'raw'/'api';out.mkdir(parents=True,exist_ok=True)
 stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
 ident=hashlib.sha256(url.encode()).hexdigest()[:10]
 dest=out/f'{stamp}_{args.query_id}_{ident}.json'
 dest.write_bytes(raw)
 manifest={'query_id':args.query_id,'query':args.query,'url':url,'status':status,'executed_at_utc':datetime.now(timezone.utc).isoformat(),'sha256':hashlib.sha256(raw).hexdigest(),'bytes':len(raw),'file':str(dest.relative_to(ROOT)),'warning':'Raw retrieval only; inspect JSON and record true pagination/yield; no automated inclusion or eligibility inference.'}
 dest.with_suffix('.manifest.json').write_text(json.dumps(manifest,indent=2,ensure_ascii=False),encoding='utf-8')
 print(json.dumps(manifest,indent=2,ensure_ascii=False))
 print('Next step: manually populate data/search_runs.csv and data/discovery_records.csv; retain exported originals.')
 return 0

if __name__=='__main__':raise SystemExit(main())
