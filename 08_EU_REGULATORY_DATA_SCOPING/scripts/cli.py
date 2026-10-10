#!/usr/bin/env python3
"""Local, standard-library-only reproducibility and integrity CLI.
No automatic eligibility, adjudication or RIT legal classification.
"""
import argparse
from collections import Counter, defaultdict
import csv
from datetime import date, datetime
from pathlib import Path
import json
import re
import sys as _sys
from urllib.parse import urlsplit, urlunsplit

_sys.path.insert(0, str(Path(__file__).resolve().parent))
import agreement

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
SEED = ROOT / 'inputs' / 'seed_inventory_v0_1.csv'
SCHEMA = {
 'search_runs.csv': ['search_run_id','search_date','platform','query_id','search_string','query_url','method','records_exported','export_file','operator','notes'],
 'discovery_records.csv':['record_id','origin','search_run_id','source_seed_id','title','url','found_at','retrieved_from','notes'],
 'dedup.csv':['record_id','canonical_record_id','decision','reviewer','notes'],
 'screening.csv':['record_id','stage','reviewer','decision','reason_code','evidence_url','date','notes'],
 'consensus.csv':['record_id','stage','final_decision','adjudicator','date','reason_code','notes'],
 'datasets.csv':['dataset_id','dataset_name','publisher','domain','coverage_level','temporal_coverage','unit_of_observation','status','license_url','primary_url','source_record_ids','notes'],
 'resources.csv':['resource_id','dataset_id','resource_name','resource_type','format','access_mode','url','celex_support','eli_support','license_evidence_url','notes'],
 'audit.csv':['dataset_id','reviewer','criterion','score','evidence_url','verification_method','verification_date','notes'],
 'rit_pilot.csv':['case_id','dataset_id','legal_celex','legal_eli','regulator','intermediary','target','intermediation_function','normative_basis_article','evidence_excerpt_ref','reviewer','confidence','validation_status','notes'],
}
# Controlled vocabularies live in one machine-readable file; the code holds no lists of its own.
VOCAB_FILE = Path(__file__).resolve().parents[1] / 'schemas' / 'vocabularies.json'
DATE_COLUMNS = {'search_runs.csv':['search_date'],'discovery_records.csv':['found_at'],'screening.csv':['date'],'consensus.csv':['date'],'audit.csv':['verification_date']}
URL_COLUMNS = {'search_runs.csv':['query_url'],'discovery_records.csv':['url'],'screening.csv':['evidence_url'],'datasets.csv':['license_url','primary_url'],'resources.csv':['url','license_evidence_url'],'audit.csv':['evidence_url']}
ISO_RE = re.compile(r'^\d{4}-\d{2}-\d{2}([T ]\d{2}:\d{2}(:\d{2}(\.\d+)?)?(Z|[+-]\d{2}:?\d{2})?)?$')


def load_vocab():
 return json.loads(VOCAB_FILE.read_text(encoding='utf-8'))


def is_iso(value):
 if not ISO_RE.match(value): return False
 try: date.fromisoformat(value[:10])
 except ValueError: return False
 return True


def is_http_url(value):
 parts=urlsplit(value)
 return parts.scheme in ('http','https') and bool(parts.netloc) and not any(ch.isspace() for ch in value)


def split_ids(value):
 return [x for x in re.split(r'[;,|\s]+',(value or '').strip()) if x]


def read_table(filename):
 path=DATA/filename
 if not path.exists(): return []
 with path.open('r',encoding='utf-8-sig',newline='') as handle:
  return list(csv.DictReader(handle))


def append_table(filename, items):
 if not items: return
 with (DATA/filename).open('a',encoding='utf-8-sig',newline='') as handle:
  writer=csv.DictWriter(handle,fieldnames=SCHEMA[filename],extrasaction='ignore')
  for item in items: writer.writerow(item)


def init():
 DATA.mkdir(parents=True,exist_ok=True)
 for filename,cols in SCHEMA.items():
  path=DATA/filename
  if path.exists(): continue
  with path.open('w',encoding='utf-8-sig',newline='') as handle:
   csv.writer(handle).writerow(cols)
 print('Data tables initialized. Existing files were not overwritten.')


def seed_import():
 init()
 existing={x['source_seed_id'] for x in read_table('discovery_records.csv') if x['source_seed_id']}
 with SEED.open('r',encoding='utf-8-sig',newline='') as handle:
  seeds=list(csv.DictReader(handle))
 entries=[]
 for source in seeds:
  sid=source['source_seed_id']
  if sid in existing: continue
  entries.append({'record_id':'SEED_'+sid,'origin':'seed','search_run_id':'','source_seed_id':sid,'title':source['name'],'url':source['source_url'],'found_at':'2026-10-09','retrieved_from':'previous exploratory inventory; NOT systematic','notes':source['limitations']})
 append_table('discovery_records.csv',entries)
 print(f'Imported {len(entries)} seed hits; dataset inclusion still requires full screening and dataset-level deduplication.')


def issues():
 messages=[]; known=set()
 for filename,head in SCHEMA.items():
  path=DATA/filename
  if not path.exists():
   messages.append(('ERROR',f'Missing {filename}'));continue
  with path.open('r',encoding='utf-8-sig',newline='') as f:
   fieldnames=csv.DictReader(f).fieldnames
  if fieldnames!=head: messages.append(('ERROR',f'Unexpected schema in {filename}: {fieldnames}'))
 voc=load_vocab()
 def bad(table,column,row,value): messages.append(('ERROR',f'Invalid value in {table}.{column} ({row[SCHEMA[table][0]]}): {value!r}'))
 for table,cols in DATE_COLUMNS.items():
  for r in read_table(table):
   for c in cols:
    if r.get(c) and not is_iso(r[c]): bad(table,c,r,r[c])
 for table,cols in URL_COLUMNS.items():
  for r in read_table(table):
   for c in cols:
    if r.get(c) and not is_http_url(r[c]): bad(table,c,r,r[c])
 records=read_table('discovery_records.csv')
 ids=[x['record_id'] for x in records]
 known=set(ids)
 dup=[k for k,c in Counter(ids).items() if c>1]
 if dup: messages.append(('ERROR',f'Duplicate record IDs: {dup[:8]}'))
 logids={x['search_run_id'] for x in read_table('search_runs.csv')}
 for r in records:
  if not r['title'] or not r['url'] or not r['origin']:
   messages.append(('ERROR',f'Record {r["record_id"]} misses title/url/origin'))
  if r['origin'] and r['origin'] not in voc['origin']: bad('discovery_records.csv','origin',r,r['origin'])
  if r['origin']=='systematic_search' and not r['search_run_id']:
   messages.append(('ERROR',f'Systematic record {r["record_id"]} without search_run_id'))
  if r['search_run_id'] and r['search_run_id'] not in logids:
   messages.append(('ERROR',f'Record {r["record_id"]} points to unknown search_run_id'))
 byurl=defaultdict(list)
 for r in records:
  if r['url']: byurl[r['url']].append(r['record_id'])
 for u,same in byurl.items():
  if len(same)>1: messages.append(('WARNING',f'Same URL in records {same}: {u} (candidate duplicate; human decision required)'))
 dedup=read_table('dedup.csv')
 for r in dedup:
  if r['record_id'] not in known: messages.append(('ERROR',f'Dedup unknown record {r["record_id"]}'))
  if r['canonical_record_id'] and r['canonical_record_id'] not in known: messages.append(('ERROR',f'Dedup references unknown canonical record {r["canonical_record_id"]}'))
  if r['decision'] not in ('unique','duplicate'):messages.append(('ERROR',f'Bad dedup decision {r["record_id"]}'))
 dec=read_table('screening.csv')
 for r in dec:
  if r['record_id'] not in known: messages.append(('ERROR',f'Screening unknown record {r["record_id"]}'))
  if r['stage'] not in ('title_abstract','full_source'): messages.append(('ERROR',f'Invalid screening stage for {r["record_id"]}'))
  if r['decision'] not in ('include','exclude','uncertain'): messages.append(('ERROR',f'Invalid screening decision for {r["record_id"]}'))
  if r['decision']=='exclude' and not r['reason_code']:messages.append(('ERROR',f'Exclusion without reason {r["record_id"]}'))
  if r['reason_code'] and r['reason_code'] not in voc['reason_code']: bad('screening.csv','reason_code',r,r['reason_code'])
 dups=[x for x,c in Counter((r['record_id'],r['stage'],r['reviewer']) for r in dec).items() if c>1]
 if dups:messages.append(('ERROR',f'Repeated individual screening submissions {dups[:5]}'))
 cons=read_table('consensus.csv')
 for r in cons:
  if r['record_id'] not in known or r['final_decision'] not in ('include','exclude'):
   messages.append(('ERROR',f'Invalid consensus record {r["record_id"]}'))
  if r['final_decision']=='exclude' and not r['reason_code']: messages.append(('ERROR',f'Consensus exclusion without reason for {r["record_id"]}'))
  if r['stage'] not in voc['screening_stage']: bad('consensus.csv','stage',r,r['stage'])
  if r['reason_code'] and r['reason_code'] not in voc['reason_code']: bad('consensus.csv','reason_code',r,r['reason_code'])
 duplicate_cons=[x for x,c in Counter((r['record_id'],r['stage']) for r in cons).items() if c>1]
 if duplicate_cons: messages.append(('ERROR',f'Multiple final consensus rows {duplicate_cons[:5]}'))
 dsets=read_table('datasets.csv');dids=[x['dataset_id'] for x in dsets];didset=set(dids)
 if len(dids)!=len(didset):messages.append(('ERROR','Duplicate canonical dataset IDs'))
 final_inc={r['record_id'] for r in cons if r['stage']=='full_source' and r['final_decision']=='include'}
 for r in dsets:
  cited=split_ids(r['source_record_ids'])
  if not cited: messages.append(('ERROR',f'Dataset {r["dataset_id"]} has no source_record_ids'))
  for i in cited:
   if i not in known: messages.append(('ERROR',f'Dataset {r["dataset_id"]} cites unknown record: {i}'))
   elif i not in final_inc: messages.append(('ERROR',f'Dataset {r["dataset_id"]} cites a record without full_source inclusion by consensus: {i}'))
 for name in ('resources.csv','audit.csv','rit_pilot.csv'):
  for r in read_table(name):
   if r['dataset_id'] not in didset:messages.append(('ERROR',f'{name} references unknown dataset: {r["dataset_id"]}'))
 for r in read_table('audit.csv'):
  if r['criterion'] not in voc['audit_criterion']: bad('audit.csv','criterion',r,r['criterion'])
  if r['score'] not in ('0','1','2','UNVERIFIED','NA'):
   messages.append(('ERROR',f'Invalid audit score {r["dataset_id"]}: {r["score"]}'))
  if r['score'] in ('0','1','2') and (not r['evidence_url'] or not r['verification_date']):
   messages.append(('ERROR',f'Audit score lacks verifiable evidence/date: {r["dataset_id"]}/{r["criterion"]}'))
  if r['score']=='NA' and not r['notes']:
   messages.append(('ERROR',f'NA without reason {r["dataset_id"]}/{r["criterion"]}'))
 a_dup=[x for x,c in Counter((r['dataset_id'],r['reviewer'],r['criterion']) for r in read_table('audit.csv')).items() if c>1]
 if a_dup:messages.append(('ERROR',f'Duplicate audit assessments {a_dup[:4]}'))
 for r in read_table('rit_pilot.csv'):
  if r['validation_status'] and r['validation_status'] not in voc['rit_validation_status']: bad('rit_pilot.csv','validation_status',r,r['validation_status'])
  if r['validation_status']=='adjudicated' and (not r['normative_basis_article'] or not r['evidence_excerpt_ref'] or not r['legal_celex'] and not r['legal_eli']):
   messages.append(('ERROR',f'Adjudicated RIT relation missing legal article/source/id: {r["case_id"]}'))
 # Incomplete systematic work is clearly reported as WARNING; not fabricated as complete
 # A record with an origin outside the vocabulary is an ERROR above and enters no count.
 sysids={r['record_id'] for r in records if r['origin']!='seed' and r['origin'] in voc['origin']}
 if sysids:
  mapped={r['record_id'] for r in dedup}
  if len(sysids-mapped)>0:messages.append(('WARNING',f'{len(sysids-mapped)} systematic hits await dedup mapping'))
  unique={r['record_id'] for r in dedup if r['decision']=='unique' and r['record_id'] in sysids}
  cons1={r['record_id'] for r in cons if r['stage']=='title_abstract'}
  if len(unique-cons1)>0:messages.append(('WARNING',f'{len(unique-cons1)} unique systematic records await title screening consensus'))
 else:messages.append(('WARNING','No documented systematic search hits: only seed set or empty inventory.'))
 if not dsets:messages.append(('WARNING','No canonical dataset inclusion decisions: scientific results not available.'))
 return messages


def kappa_or_na(rows):
 # Single-pair convenience wrapper. Different reviewer pairs are never pooled:
 # with more than one pair this raises, and agreement.pairwise_agreement must be used.
 res=agreement.pairwise_agreement(rows,variable='decision')
 if len(res['pairs'])>1:
  raise ValueError(f'{len(res["pairs"])} reviewer pairs present; agreement is reported per pair, never pooled')
 if not res['pairs'] or not res['pairs'][0]['n_items_both_categorical']:return {'n':0,'agreement':None,'kappa':None}
 p=res['pairs'][0];kap=p['kappa_categorical']
 return {'n':p['n_items_both_categorical'],'agreement':round(p['observed_agreement_categorical'],4),'kappa':round(kap,4) if kap is not None else None,'n_with_uncertain':p['n_items_with_uncertain']}


def report():
 init();r=read_table('discovery_records.csv');d=read_table('dedup.csv');s=read_table('screening.csv');c=read_table('consensus.csv');ds=read_table('datasets.csv');res=read_table('resources.csv');aud=read_table('audit.csv')
 valid_origins=load_vocab()['origin']
 sys=[x for x in r if x['origin']!='seed' and x['origin'] in valid_origins];seed=[x for x in r if x['origin']=='seed']
 dsys=[x for x in d if x['record_id'] in {y['record_id'] for y in sys}]
 known={x['record_id'] for x in sys}
 # PRISMA complete only if all registered systematic records are deduplicated and consensus exists; avoids misleading counts
 complete_dedup=bool(sys) and known.issubset({x['record_id'] for x in dsys})
 title_expected={x['record_id'] for x in dsys if x['decision']=='unique'}
 title_cons={x['record_id'] for x in c if x['stage']=='title_abstract'}
 complete_title=bool(title_expected) and title_expected.issubset(title_cons)
 full_expected={x['record_id'] for x in c if x['stage']=='title_abstract' and x['final_decision']=='include'}
 full_cons={x['record_id'] for x in c if x['stage']=='full_source'}
 complete_full=bool(full_expected) and full_expected.issubset(full_cons)
 msg=['# RELATÓRIO INTERMEDIÁRIO — NÃO É RESULTADO FINAL','',f'Gerado em: {datetime.now().astimezone().isoformat(timespec="seconds")}', '', '## Status verificável',f'- Ocorrências do levantamento exploratório (seeds): **{len(seed)}**; não contam como inclusão.', f'- Registros documentados de buscas não-semente: **{len(sys)}**.',f'- Registros sistemáticos com decisão de deduplicação: **{len(dsys)} / {len(sys)}**.',f'- Deduplicação integral: **{"SIM" if complete_dedup else "NÃO"}**.',f'- Consensus título/descrição completa: **{"SIM" if complete_title else "NÃO"}**.',f'- Consensus documentação integral completa: **{"SIM" if complete_full else "NÃO"}**.',f'- Datasets canônicos extraídos: **{len(ds)}**, não equivalentes a portais/serviços.',f'- Recursos/distribuições documentados: **{len(res)}**.',f'- Linhas de auditoria: **{len(aud)}**.','','## Concordância exploratória antes de adjudicação']
 fmt=lambda v:'n/d' if v is None else f'{v:.4f}'
 for stage in ('title_abstract','full_source'):
  res=agreement.pairwise_agreement([x for x in s if x['stage']==stage],variable='decision',categories=['include','exclude'])
  if not res['pairs']:msg.append(f'- {stage}: nenhum par de avaliadores com decisões registradas.')
  for p in res['pairs']:
   ci=p['kappa_categorical_ci95'];ci_txt=f' (IC95% aprox. {ci[0]:.2f} a {ci[1]:.2f})' if ci else f' ({p["kappa_categorical_note"]})'
   msg.append(f'- {stage} | {p["pair"][0]} × {p["pair"][1]}: itens={p["n_items"]}; itens com `uncertain`={p["n_items_with_uncertain"]}; concordância com `uncertain` como categoria={fmt(p["observed_agreement_all"])}; concordância só entre decisões categóricas={fmt(p["observed_agreement_categorical"])} (n={p["n_items_both_categorical"]}); kappa categórico={fmt(p["kappa_categorical"])}{ci_txt}.')
  for label,key in (('um só avaliador','items_with_one_reviewer'),('mais de dois avaliadores','items_with_more_than_two_reviewers'),('resposta em branco','items_with_blank_answer')):
   if res[key]:msg.append(f'- {stage}: {len(res[key])} item(ns) com {label}, fora de qualquer par: {res[key][:10]}')
 msg.append('- Cada par de avaliadores é relatado em separado; não existe valor agregado entre pares. Os indicadores são diagnósticos e não substituem a adjudicação.')
 msg+=['','## Contagens PRISMA','- NÃO GERAR FLUXOGRAMA FINAL até deduplicação, triagem e consenso completos. O seed set não preenche automaticamente a etapa de identificação sistemática.','','## Alertas de qualidade']
 for level,message in issues():msg.append(f'- **{level}**: {message}')
 path=ROOT/'outputs'/'STATUS_REPORT.md';path.parent.mkdir(exist_ok=True)
 path.write_text('\n'.join(msg)+'\n',encoding='utf-8')
 print(f'Wrote {path.relative_to(ROOT)}')
 print('\n'.join(msg[:12]))


def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('command',choices=['init','import-seeds','check','report'])
 args=ap.parse_args()
 if args.command=='init':init()
 elif args.command=='import-seeds':seed_import()
 elif args.command=='check':
  # Read-only: a missing table is reported as ERROR by issues(), never created here.
  msgs=issues()
  for level,msg in msgs:print(f'[{level}] {msg}')
  print('No structural errors.' if not any(level=='ERROR' for level,_ in msgs) else 'Some structural errors found.')
  return 2 if any(level=='ERROR' for level,_ in msgs) else 0
 elif args.command=='report':report()
 return 0

if __name__=='__main__':raise SystemExit(main())
