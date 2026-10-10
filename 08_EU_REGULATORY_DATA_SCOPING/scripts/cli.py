#!/usr/bin/env python3
"""Local, standard-library-only reproducibility and integrity CLI.
No automatic eligibility, adjudication or RIT legal classification.
"""
import argparse
from collections import Counter, defaultdict
import csv
from datetime import datetime
from pathlib import Path
import json
from urllib.parse import urlsplit, urlunsplit

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
 records=read_table('discovery_records.csv')
 ids=[x['record_id'] for x in records]
 known=set(ids)
 dup=[k for k,c in Counter(ids).items() if c>1]
 if dup: messages.append(('ERROR',f'Duplicate record IDs: {dup[:8]}'))
 logids={x['search_run_id'] for x in read_table('search_runs.csv')}
 for r in records:
  if not r['title'] or not r['url'] or not r['origin']:
   messages.append(('ERROR',f'Record {r["record_id"]} misses title/url/origin'))
  if r['origin']=='systematic_search' and not r['search_run_id']:
   messages.append(('ERROR',f'Systematic record {r["record_id"]} without search_run_id'))
  if r['search_run_id'] and r['search_run_id'] not in logids:
   messages.append(('ERROR',f'Record {r["record_id"]} points to unknown search_run_id'))
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
 dups=[x for x,c in Counter((r['record_id'],r['stage'],r['reviewer']) for r in dec).items() if c>1]
 if dups:messages.append(('ERROR',f'Repeated individual screening submissions {dups[:5]}'))
 cons=read_table('consensus.csv')
 for r in cons:
  if r['record_id'] not in known or r['final_decision'] not in ('include','exclude'):
   messages.append(('ERROR',f'Invalid consensus record {r["record_id"]}'))
  if r['final_decision']=='exclude' and not r['reason_code']: messages.append(('ERROR',f'Consensus exclusion without reason for {r["record_id"]}'))
 duplicate_cons=[x for x,c in Counter((r['record_id'],r['stage']) for r in cons).items() if c>1]
 if duplicate_cons: messages.append(('ERROR',f'Multiple final consensus rows {duplicate_cons[:5]}'))
 dsets=read_table('datasets.csv');dids=[x['dataset_id'] for x in dsets];didset=set(dids)
 if len(dids)!=len(didset):messages.append(('ERROR','Duplicate canonical dataset IDs'))
 for name in ('resources.csv','audit.csv','rit_pilot.csv'):
  for r in read_table(name):
   if r['dataset_id'] not in didset:messages.append(('ERROR',f'{name} references unknown dataset: {r["dataset_id"]}'))
 for r in read_table('audit.csv'):
  if r['score'] not in ('0','1','2','UNVERIFIED','NA'):
   messages.append(('ERROR',f'Invalid audit score {r["dataset_id"]}: {r["score"]}'))
  if r['score'] in ('0','1','2') and (not r['evidence_url'] or not r['verification_date']):
   messages.append(('ERROR',f'Audit score lacks verifiable evidence/date: {r["dataset_id"]}/{r["criterion"]}'))
  if r['score']=='NA' and not r['notes']:
   messages.append(('ERROR',f'NA without reason {r["dataset_id"]}/{r["criterion"]}'))
 a_dup=[x for x,c in Counter((r['dataset_id'],r['reviewer'],r['criterion']) for r in read_table('audit.csv')).items() if c>1]
 if a_dup:messages.append(('ERROR',f'Duplicate audit assessments {a_dup[:4]}'))
 for r in read_table('rit_pilot.csv'):
  if r['validation_status']=='adjudicated' and (not r['normative_basis_article'] or not r['evidence_excerpt_ref'] or not r['legal_celex'] and not r['legal_eli']):
   messages.append(('ERROR',f'Adjudicated RIT relation missing legal article/source/id: {r["case_id"]}'))
 # Incomplete systematic work is clearly reported as WARNING; not fabricated as complete
 sysids={r['record_id'] for r in records if r['origin']!='seed'}
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
 paired=defaultdict(dict)
 for r in rows:
  if r['decision'] in ('include','exclude'):
   paired[r['record_id']][r['reviewer']]=r['decision']
 pairs=[]
 for vals in paired.values():
  if len(vals)==2:
   people=sorted(vals)
   pairs.append((vals[people[0]],vals[people[1]]))
  # >2 evaluators cannot be pooled into a Cohen pair
 if not pairs:return {'n':0,'agreement':None,'kappa':None}
 n=len(pairs);po=sum(a==b for a,b in pairs)/n
 marg_a=Counter(a for a,b in pairs);marg_b=Counter(b for a,b in pairs)
 pe=sum(marg_a.get(k,0)/n*marg_b.get(k,0)/n for k in ('include','exclude'))
 kap=(po-pe)/(1-pe) if pe<1 else None
 return {'n':n,'agreement':round(po,4),'kappa':round(kap,4) if kap is not None else None}


def report():
 init();r=read_table('discovery_records.csv');d=read_table('dedup.csv');s=read_table('screening.csv');c=read_table('consensus.csv');ds=read_table('datasets.csv');res=read_table('resources.csv');aud=read_table('audit.csv')
 sys=[x for x in r if x['origin']!='seed'];seed=[x for x in r if x['origin']=='seed']
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
 for stage in ('title_abstract','full_source'):
  z=kappa_or_na([x for x in s if x['stage']==stage]);msg.append(f'- {stage}: N pares de decisões binárias={z["n"]}, acordo={z["agreement"]}, kappa={z["kappa"]}. Pares com `uncertain` não entram nesse cálculo e devem ser apresentados separadamente.')
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
  init()
  msgs=issues()
  for level,msg in msgs:print(f'[{level}] {msg}')
  print('No structural errors.' if not any(level=='ERROR' for level,_ in msgs) else 'Some structural errors found.')
  return 2 if any(level=='ERROR' for level,_ in msgs) else 0
 elif args.command=='report':report()
 return 0

if __name__=='__main__':raise SystemExit(main())
