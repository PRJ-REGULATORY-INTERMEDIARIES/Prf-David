from lib import *
import json
def ids(s): return [x.strip() for x in re.split(r'[;,]',s) if x.strip()]
def check_case(c):
    T={t:load(c,t)[1] for t in tables}
    fails=[]
    def F(rule,msg): fails.append((rule,msg))
    units={r['unit_id'] for r in T['SOURCE_UNIT_INVENTORY']}
    # rule1
    ils=T['INSTRUMENT_LEVEL_SUMMARY'][0]
    if ils['units_total']!=ils['units_screened'] or int(ils['units_total'])!=len(units): F(1,'ils')
    if {r['unit_id'] for r in T['UNIT_SCREENING']}!=units: F(1,'screening!=inventory')
    # all ids
    allids=set()
    idcol={'INSTITUTIONAL_STATEMENTS':'st_id','NORMATIVE_ASSIGNMENTS':'na_id','POSITIONS_AND_DEVICES':'pd_id','QUALIFIED_RELATIONS':'qr_id','EXTERNAL_REFERENCES':'ext_id','SUBCONFIGURATIONS':'sc_id','ARCHITECTURE_CANDIDATES':'arch_id','PROPERTY_REGISTER':'prop_id','CLOSURE_REGISTER':'closure_id','UNCERTAINTY_LOG':'unc_id','HUMAN_REVIEW_QUEUE':'hq_id','PROVENANCE_LINKS':'link_id','TRACE_DEMONSTRATIONS':'trace_id','PROTOCOL_DEVIATION_LOG':'dev_id'}
    for t,col in idcol.items():
        v=[r[col] for r in T[t]]
        if len(v)!=len(set(v)): F(0,'dup ids '+t)
        allids|=set(v)
    # unit refs
    for t in ['INSTITUTIONAL_STATEMENTS','NORMATIVE_ASSIGNMENTS','QUALIFIED_RELATIONS','EXTERNAL_REFERENCES','PROVENANCE_LINKS','UNCERTAINTY_LOG']:
        col={'PROVENANCE_LINKS':'unit_id','UNCERTAINTY_LOG':'unit_ids'}.get(t,'supporting_unit_ids')
        for r in T[t]:
            for u in ids(r[col]):
                if u not in units: F(1,f'{t} unit {u}')
    for r in T['POSITIONS_AND_DEVICES']:
        for u in ids(r['supporting_unit_ids']):
            if u not in units: F(1,'PD unit '+u)
    # rule 2
    st={r['st_id']:r for r in T['INSTITUTIONAL_STATEMENTS']}
    for r in st.values():
        if not ids(r['supporting_unit_ids']): F(2,'ST no unit')
    for t in ['NORMATIVE_ASSIGNMENTS','QUALIFIED_RELATIONS','POSITIONS_AND_DEVICES']:
        for r in T[t]:
            s=ids(r['statement_ids']) if 'statement_ids' in r else None
            if s is not None and (not s or any(x not in st for x in s)): F(2,t+' st')
            if s is not None:
                for x in s:
                    if x in st and st[x]['recital_only']=='Y': F(2,'recital_only derived')
    for r in T['EXTERNAL_REFERENCES']:
        if not ids(r['supporting_unit_ids']): F(2,'EXT no unit')
    # PD statement link? PD has no statement_ids column
    # rule 3: reference resolution for *_ids columns
    pdids={r['pd_id'] for r in T['POSITIONS_AND_DEVICES']}
    for t in tables:
        for r in T[t]:
            for k,v in r.items():
                if (k.endswith('_ids') or k.endswith('_pd_id') or k=='traced_id' or k=='bearer_id' or k=='closure_ref') and v and k not in('supporting_unit_ids','unit_ids','i1_scope_units','instance_source_unit_ids','statement_ids'):
                    for x in ids(v):
                        if re.fullmatch(r'(ST|NA|PD|QR|EXT|SC|ARCH|PROP|CL|UNC|HQ|LNK|TR|DEV)-\d+',x) and x not in allids: F(3,f'{t}.{k} {x}')
    qrs={r['qr_id']:r for r in T['QUALIFIED_RELATIONS']}
    for r in qrs.values():
        for x in ids(r['accountable_via_qr_ids']):
            if x not in qrs or qrs[x]['relation_type']!='accountability': F(3,'accountable_via '+x)
        # rule 4
        if not r['origin_pd_id'] or not r['counterpart_pd_id'] or r['modality']=='prohibition' or r['epistemic_status']=='material_establishment_evidenced': F(4,r['qr_id'])
        if r['origin_pd_id'] not in pdids or r['counterpart_pd_id'] not in pdids: F(4,'qr pd '+r['qr_id'])
    # rule 5
    prov=collections.defaultdict(list)
    for r in T['PROVENANCE_LINKS']: prov[r['record_id']].append(r)
    for t,col in [('NORMATIVE_ASSIGNMENTS','na_id'),('QUALIFIED_RELATIONS','qr_id'),('SUBCONFIGURATIONS','sc_id'),('ARCHITECTURE_CANDIDATES','arch_id'),('PROPERTY_REGISTER','prop_id')]:
        for r in T[t]:
            if not prov[r[col]]: F(5,'no provenance '+r[col])
    for t in ['NORMATIVE_ASSIGNMENTS','QUALIFIED_RELATIONS']:
        for r in T[t]:
            if r['derivation']=='derived':
                n=len(ids(r['supporting_unit_ids']))
                if not r['derivation_rule'] or n<2 and 'cross' not in r['derivation_rule'].lower() and 'xref' not in r['derivation_rule'].lower(): F(5,'derived '+(r.get('na_id') or r.get('qr_id')))
    # rule 6
    hq_refs=collections.defaultdict(list)
    for r in T['HUMAN_REVIEW_QUEUE']:
        for x in ids(r['record_refs']): hq_refs[x].append(r['hq_id'])
    for r in T['ARCHITECTURE_CANDIDATES']:
        o=r['outcome']
        if o in('INTEGRATED','OVERLAPPING_OR_PARTIALLY_INTEGRATED') and not (ids(r['hq_ids']) or hq_refs[r['arch_id']]): F(6,'arch no hq '+r['arch_id'])
        if o=='INTEGRATED' and not all(r[k]=='SATISFIED' for k in('i1_status','i2_status','i3_status','i4_status')): F(6,'integrated w/o all satisfied '+r['arch_id'])
    # rule 7
    cl={r['closure_id']:r for r in T['CLOSURE_REGISTER']}
    for r in T['PROPERTY_REGISTER']:
        if r['closure_dependency']=='Y':
            if r['closure_ref'] not in cl: F(7,'closure_ref '+r['prop_id'])
            elif cl[r['closure_ref']]['result']=='UNDETERMINED' and r['status']!='undetermined': F(7,'closure undetermined but prop '+r['status']+' '+r['prop_id'])
    # rule 8
    for r in T['EXTERNAL_REFERENCES']:
        if r['source_verification_status']!='not_checked': F(8,r['ext_id'])
        if r['boundary_status']!='outside_corpus_not_expanded': F(8,'boundary '+r['ext_id']+' '+r['boundary_status'])
    # rule 9
    for r in T['HUMAN_REVIEW_QUEUE']:
        for k in('human_decision','human_rationale','decided_by','decision_date'):
            if r[k].strip(): F(9,r['hq_id']+' '+k)
    # rule 10
    trs=T['TRACE_DEMONSTRATIONS']
    for r in trs:
        if r['chain_complete']!='Y': F(10,'chain incomplete '+r['trace_id'])
        if r['traced_id'] not in allids: F(10,'traced id '+r['traced_id'])
        for x in re.findall(r'\b(?:ST|NA|PD|QR|EXT|SC|ARCH)-\d+\b',r['vertical_chain']):
            if x not in allids: F(10,'chain id '+x)
    # misc: constraint: no human
    return fails
