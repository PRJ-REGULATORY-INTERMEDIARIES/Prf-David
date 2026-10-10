param(
    [string]$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
)

$ErrorActionPreference = 'Stop'
$workspace = Join-Path $RepoRoot 'R4_CROSS_DOMAIN_VALIDATION'
$qaDir = Join-Path $workspace '03_extraction/qa'
$reviewDir = Join-Path $qaDir 'human_review'
New-Item -ItemType Directory -Path $reviewDir -Force | Out-Null

function Normalize-Text([string]$Text) {
    if ([string]::IsNullOrWhiteSpace($Text)) { return '' }
    return (($Text -replace '\s+', ' ').Trim())
}

function Get-BlockMap([string[]]$Lines) {
    $markers = [System.Collections.Generic.List[object]]::new()
    for ($i=0; $i -lt $Lines.Count; $i++) {
        $m = [regex]::Match($Lines[$i], '^\[(RECITAL|ARTICLE|ANNEX)\s+([^\]]+)\]$')
        if ($m.Success) { $markers.Add([pscustomobject]@{ Index=$i; Type=$m.Groups[1].Value; Number=$m.Groups[2].Value.Trim() }) }
    }
    $map=@{}
    for ($j=0; $j -lt $markers.Count; $j++) {
        $marker=$markers[$j]
        $end=if($j+1 -lt $markers.Count){$markers[$j+1].Index}else{$Lines.Count}
        $blockLines=@($Lines[$marker.Index..($end-1)])
        $before=''
        $after=''
        if ($j -gt 0) { $before=($Lines[$markers[$j-1].Index..($marker.Index-1)] -join [Environment]::NewLine); if($before.Length -gt 1200){$before=$before.Substring($before.Length-1200)} }
        if ($j+1 -lt $markers.Count) { $nextEnd=if($j+2 -lt $markers.Count){$markers[$j+2].Index}else{$Lines.Count}; $after=($Lines[$markers[$j+1].Index..($nextEnd-1)] -join [Environment]::NewLine); if($after.Length -gt 1200){$after=$after.Substring(0,1200)} }
        $map["$($marker.Type)|$($marker.Number)"]=[pscustomobject]@{ Type=$marker.Type; Number=$marker.Number; Text=($blockLines -join [Environment]::NewLine).Trim(); Before=$before; After=$after }
    }
    return $map
}

$caseFiles=@{
    D1_GDPR='02_sources/D1_GDPR/normalized/D1_GDPR_32016R0679_processing.txt'
    D2_DSA='02_sources/D2_DSA/normalized/D2_DSA_32022R2065_processing.txt'
    D3_AI_ACT='02_sources/D3_AI_ACT/normalized/D3_AI_ACT_32024R1689_processing.txt'
}
$blocks=@{}
foreach($case in $caseFiles.Keys){$blocks[$case]=Get-BlockMap (Get-Content -LiteralPath (Join-Path $workspace $caseFiles[$case]))}

$sample=@(Import-Csv (Join-Path $qaDir 'R4_2B_HUMAN_QA_SAMPLE.csv'))
$typology=@(Import-Csv (Join-Path $qaDir 'R4_2B_AMBIGUITY_TYPOLOGY.csv'))
$working=[System.Collections.Generic.List[object]]::new()
foreach($row in $sample){
    $fragment=($row.SOURCE_POINTER -split '#',2)[1]
    $parts=$fragment -split '/',2
    $marker=[regex]::Match($parts[0], '^(article|recital|annex)_(.+)$')
    $type=if($marker.Success){$marker.Groups[1].Value.ToUpperInvariant()}else{''}
    $number=if($marker.Success){$marker.Groups[2].Value}else{''}
    $block=$blocks[$row.CASE_ID]["$type|$number"]
    $typ=$typology|Where-Object EXTRACTION_ID -eq $row.EXTRACTION_ID|Select-Object -First 1
    $props=[ordered]@{}
    foreach($p in $row.PSObject.Properties){$props[$p.Name]=$p.Value}
    $props['CURRENT_AMBIGUITY_TYPE']=if($null -ne $typ){$typ.AMBIGUITY_TYPE}else{''}
    $props['STRUCTURAL_NOTE']=if($null -ne $typ){$typ.AMBIGUITY_DESCRIPTION}else{''}
    $props['FULL_SOURCE_TEXT']=if($null -ne $block){$block.Text}else{''}
    $props['FULL_SOURCE_CONTEXT_BEFORE']=if($null -ne $block){$block.Before}else{''}
    $props['FULL_SOURCE_CONTEXT_AFTER']=if($null -ne $block){$block.After}else{''}
    $props['SOURCE_RESOLUTION_STATUS']=if($null -ne $block -and -not [string]::IsNullOrWhiteSpace($block.Text)){'RESOLVED_FROM_FROZEN_PROCESSING_CORPUS'}else{'UNRESOLVED'}
    $props['ACTOR_CORRECT']=''; $props['ACTION_CORRECT']=''; $props['OBJECT_CORRECT']=''; $props['COUNTERPART_CORRECT']=''; $props['RECIPIENT_CORRECT']=''; $props['SOURCE_POINTER_CORRECT']=''; $props['EXCERPT_CORRECT']=''; $props['AMBIGUITY_JUSTIFIED']=''; $props['ERROR_TYPE']=''; $props['HUMAN_CORRECTION']=''; $props['HUMAN_REVIEWER']=''; $props['HUMAN_REVIEW_STATUS']='PENDING'; $props['HUMAN_NOTES']=''
    $working.Add([pscustomobject]$props)
}
$workingPath=Join-Path $reviewDir 'R4_2B_HUMAN_REVIEW_WORKING.csv'
$working|Export-Csv $workingPath -NoTypeInformation -Encoding utf8

$json=($working|ConvertTo-Json -Depth 8 -Compress)
$json=$json -replace '&','\\u0026' -replace '<','\\u003c' -replace '>','\\u003e'
$html=@'
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>R4.2B Human QA Review Panel</title>
<style>
:root{--ink:#182230;--muted:#5c6878;--line:#d8dee7;--paper:#fff;--blue:#174a7e;--blue2:#eaf3fc;--gold:#fff6d8;--warn:#8a2f12;--green:#1b6b49}*{box-sizing:border-box}body{margin:0;background:#f3f6f9;color:var(--ink);font:14px/1.45 system-ui,-apple-system,Segoe UI,sans-serif}header{background:#17324d;color:white;padding:18px 24px;position:sticky;top:0;z-index:5}h1{font-size:21px;margin:0 0 4px}h2{font-size:16px;margin:0 0 10px}h3{font-size:13px;margin:16px 0 6px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted)}.warning{background:#fff0e8;color:var(--warn);border:1px solid #e4b39e;padding:10px 12px;border-radius:8px;font-weight:700;margin-top:12px}.toolbar{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-top:12px}.toolbar select,.toolbar input,.toolbar button,.review input,.review select,.review textarea{font:inherit;border:1px solid var(--line);border-radius:6px;padding:7px 8px;background:white;color:var(--ink)}button{cursor:pointer}.toolbar button,.nav button{background:#fff}.toolbar button.primary,.nav button.primary{background:#2874b6;color:#fff;border-color:#2874b6}.progress{margin-left:auto;font-weight:700}.shell{max-width:1500px;margin:0 auto;padding:18px 24px}.meta{display:grid;grid-template-columns:repeat(4,minmax(160px,1fr));gap:8px;margin-bottom:14px}.meta div{background:var(--paper);border:1px solid var(--line);border-radius:7px;padding:9px}.label{color:var(--muted);font-size:11px;text-transform:uppercase;letter-spacing:.05em}.value{font-weight:650;margin-top:2px;word-break:break-word}.grid{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(320px,.85fr);gap:14px}.card{background:var(--paper);border:1px solid var(--line);border-radius:9px;padding:15px;margin-bottom:14px}.legal{background:#f0f7ff;border-color:#a8c7e3}.ai{background:#fffaf0;border-color:#e9d59d}.context{background:#f7f8fa;color:#596575;border:1px dashed #c8d0da}.source{white-space:pre-wrap;max-height:560px;overflow:auto;font:13px/1.55 ui-monospace,SFMono-Regular,Consolas,monospace}.field{margin:10px 0}.field .label{display:block}.field .text{white-space:pre-wrap;background:#fff;border:1px solid #e0e5eb;border-radius:5px;padding:8px;min-height:31px}.review{background:#f6fff9;border-color:#acd9bf}.review-row{display:grid;grid-template-columns:1fr 160px;gap:8px;align-items:center;border-bottom:1px solid #e3ece6;padding:8px 0}.review-row:last-child{border-bottom:0}.review-row label{font-weight:600}.review-row small{display:block;color:var(--muted);font-weight:400}.review textarea{width:100%;min-height:72px;resize:vertical}.errors{display:flex;flex-wrap:wrap;gap:6px}.errors label{font-weight:400;background:#fff;border:1px solid var(--line);padding:5px 7px;border-radius:5px}.status{display:inline-block;padding:3px 7px;border-radius:999px;background:#eef1f5;color:#465261;font-size:12px;font-weight:700}.status.reviewed{background:#daf3e5;color:#17613e}.status.progress{background:#fff0c9;color:#775400}.nav{display:flex;gap:8px;align-items:center;margin:8px 0 16px}.notice{color:var(--green);font-weight:650;min-height:20px}.small{font-size:12px;color:var(--muted)}@media(max-width:950px){.grid{grid-template-columns:1fr}.meta{grid-template-columns:repeat(2,minmax(150px,1fr))}.progress{margin-left:0}}@media(max-width:560px){.shell{padding:12px}.meta{grid-template-columns:1fr}.review-row{grid-template-columns:1fr}}
</style></head>
<body>
<header><h1>R4.2B — Human QA Review Panel</h1><div>Extraction-fidelity review against the frozen official legal corpus</div><div class="warning">REVIEW EXTRACTION ONLY.<br>Do not decide whether the actor is a regulator, intermediary or target.<br>Do not classify regulatory mechanisms.</div></header>
<main class="shell">
<div class="toolbar"><label>Case <select id="caseFilter"><option value="ALL">All</option><option>D1_GDPR</option><option>D2_DSA</option><option>D3_AI_ACT</option></select></label><label>Confidence <select id="confidenceFilter"><option value="ALL">All</option><option>HIGH</option><option>MEDIUM</option><option>LOW</option></select></label><label>Ambiguity <select id="ambiguityFilter"><option value="ALL">All</option><option value="YES">Ambiguous</option><option value="NO">Non-ambiguous</option></select></label><label>Status <select id="statusFilter"><option value="ALL">All</option><option value="PENDING">Pending</option><option value="IN_PROGRESS">In progress</option><option value="REVIEWED">Reviewed</option></select></label><input id="goto" type="number" min="1" placeholder="Record #" style="width:92px"><button id="gotoBtn">Go to record</button><button id="saveBtn" class="primary">Save locally</button><button id="csvBtn">Export CSV</button><button id="jsonBtn">Export JSON</button><div class="progress" id="progress"></div></div>
<div class="notice" id="notice"></div>
<div class="nav"><button id="prevBtn">Previous</button><button id="nextBtn" class="primary">Next</button><span class="small" id="position"></span></div>
<section id="app"></section>
</main>
<script>
const records=__DATA_JSON__;const storageKey='R4_2B_HUMAN_QA_REVIEW_WORKING_V1';let filtered=[];let current=0;const required=['ACTOR_CORRECT','ACTION_CORRECT','OBJECT_CORRECT','COUNTERPART_CORRECT','RECIPIENT_CORRECT','SOURCE_POINTER_CORRECT','EXCERPT_CORRECT','AMBIGUITY_JUSTIFIED'];const errorOptions=['ACTOR_EXTRACTION_ERROR','ACTOR_NORMALIZATION_ERROR','ACTION_EXTRACTION_ERROR','ACTION_SCOPE_ERROR','OBJECT_EXTRACTION_ERROR','COUNTERPART_EXTRACTION_ERROR','RECIPIENT_EXTRACTION_ERROR','SOURCE_POINTER_ERROR','SOURCE_EXCERPT_ERROR','CROSS_REFERENCE_ERROR','DUPLICATE_EXTRACTION','MISSING_EXTRACTION','OVER_EXTRACTION','AMBIGUITY_FALSE_POSITIVE','AMBIGUITY_FALSE_NEGATIVE','OTHER'];
function esc(v){return String(v??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]))}function reviewer(){return document.getElementById('reviewer')?.value||'Igor Caires Machado'}function isComplete(r){return required.every(k=>String(r[k]||'').length>0)&&(!required.some(k=>r[k]==='NO')||((r.ERROR_TYPE||'').length>0))}function statusClass(s){return s==='REVIEWED'?'reviewed':s==='IN_PROGRESS'?'progress':''}
function filteredRows(){const c=document.getElementById('caseFilter').value,cf=document.getElementById('confidenceFilter').value,a=document.getElementById('ambiguityFilter').value,s=document.getElementById('statusFilter').value;return records.filter(r=>(c==='ALL'||r.CASE_ID===c)&&(cf==='ALL'||r.EXTRACTION_CONFIDENCE===cf)&&(a==='ALL'||r.STRUCTURAL_AMBIGUITY===a)&&(s==='ALL'||r.HUMAN_REVIEW_STATUS===s))}function setNotice(t){document.getElementById('notice').textContent=t;setTimeout(()=>{if(document.getElementById('notice').textContent===t)document.getElementById('notice').textContent=''},3500)}function saveState(){const state={};records.forEach(r=>{state[r.QA_ID]={...Object.fromEntries([...required,'ERROR_TYPE','HUMAN_CORRECTION','HUMAN_NOTES','HUMAN_REVIEWER','HUMAN_REVIEW_STATUS'].map(k=>[k,r[k]||'']))}});localStorage.setItem(storageKey,JSON.stringify(state));setNotice('Review decisions saved in this browser.')}function loadState(){try{const state=JSON.parse(localStorage.getItem(storageKey)||'{}');records.forEach(r=>{if(state[r.QA_ID])Object.assign(r,state[r.QA_ID])})}catch(e){setNotice('Could not load local saved state.')}}
function touch(r){r.HUMAN_REVIEWER=reviewer();r.HUMAN_REVIEW_STATUS=isComplete(r)?'REVIEWED':'IN_PROGRESS';saveState();render()}function setField(r,k,v){r[k]=v;touch(r)}function selectedErrors(r){return (r.ERROR_TYPE||'').split(';').filter(Boolean)}function setError(r,k,on){let a=selectedErrors(r);if(on&&!a.includes(k))a.push(k);if(!on)a=a.filter(x=>x!==k);r.ERROR_TYPE=a.join(';');touch(r)}
function field(label,key,value){return `<div class="field"><span class="label">${esc(label)}</span><div class="text">${esc(value)||'<span class="small">(empty)</span>'}</div></div>`}function question(label,key,opts,r){return `<div class="review-row"><label>${esc(label)}<small>Extraction fidelity only</small></label><select data-q="${key}"><option value="">Select…</option>${opts.map(o=>`<option ${r[key]===o?'selected':''}>${o}</option>`).join('')}</select></div>`}
function render(){filtered=filteredRows();if(current>=filtered.length)current=Math.max(0,filtered.length-1);const r=filtered[current];const total=records.length,reviewed=records.filter(x=>x.HUMAN_REVIEW_STATUS==='REVIEWED').length;document.getElementById('progress').textContent=`Reviewed ${reviewed} / ${total} (${Math.round(reviewed/total*100)}%)`;document.getElementById('position').textContent=filtered.length?`Filtered record ${current+1} / ${filtered.length}`:'No records match filters';if(!r){document.getElementById('app').innerHTML='<div class="card">No records match the selected filters.</div>';return}const errors=selectedErrors(r);document.getElementById('app').innerHTML=`<div class="meta"><div><div class="label">QA ID</div><div class="value">${esc(r.QA_ID)}</div></div><div><div class="label">Case / CELEX</div><div class="value">${esc(r.CASE_ID)} / ${esc(r.CELEX||'')}</div></div><div><div class="label">Source pointer</div><div class="value">${esc(r.SOURCE_POINTER)}</div></div><div><div class="label">Review status</div><div class="value"><span class="status ${statusClass(r.HUMAN_REVIEW_STATUS)}">${esc(r.HUMAN_REVIEW_STATUS||'PENDING')}</span></div></div></div><div class="small">Source type: ${esc(r.SOURCE_TYPE)} · Luna confidence: ${esc(r.EXTRACTION_CONFIDENCE)} · Ambiguity: ${esc(r.STRUCTURAL_AMBIGUITY)} · Stratum: ${esc(r.SAMPLING_STRATUM)}</div><div class="grid"><div><div class="card legal"><h2>Frozen legal source</h2><div class="source">${esc(r.FULL_SOURCE_TEXT)}</div></div><div class="card context"><h3>Context before</h3><div class="source">${esc(r.FULL_SOURCE_CONTEXT_BEFORE)||'(none)'}</div><h3>Context after</h3><div class="source">${esc(r.FULL_SOURCE_CONTEXT_AFTER)||'(none)'}</div></div></div><div><div class="card ai"><h2>Luna extraction</h2>${field('Actor', 'ACTOR_TEXT_LUNA', r.ACTOR_TEXT_LUNA)}${field('Legal action','LEGAL_ACTION_LUNA',r.LEGAL_ACTION_LUNA)}${field('Action object','ACTION_OBJECT_LUNA',r.ACTION_OBJECT_LUNA)}${field('Counterpart','COUNTERPART_LUNA',r.COUNTERPART_LUNA)}${field('Recipient','RECIPIENT_LUNA',r.RECIPIENT_LUNA)}${field('Source excerpt','SOURCE_EXCERPT',r.SOURCE_EXCERPT)}<h3>Ambiguity context</h3>${field('Current ambiguity type','CURRENT_AMBIGUITY_TYPE',r.CURRENT_AMBIGUITY_TYPE)}${field('Structural note','STRUCTURAL_NOTE',r.STRUCTURAL_NOTE)}</div><div class="card review"><h2>Researcher review</h2><div class="field"><span class="label">Reviewer</span><input id="reviewer" value="${esc(r.HUMAN_REVIEWER||'Igor Caires Machado')}" placeholder="Reviewer name"></div>${question('Actor correct?','ACTOR_CORRECT',['YES','NO','N/A'],r)}${question('Action correct?','ACTION_CORRECT',['YES','NO','N/A'],r)}${question('Object correct?','OBJECT_CORRECT',['YES','NO','N/A'],r)}${question('Counterpart correct?','COUNTERPART_CORRECT',['YES','NO','N/A'],r)}${question('Recipient correct?','RECIPIENT_CORRECT',['YES','NO','N/A'],r)}${question('Source pointer correct?','SOURCE_POINTER_CORRECT',['YES','NO'],r)}${question('Excerpt adequate?','EXCERPT_CORRECT',['YES','NO'],r)}${question('Ambiguity justified?','AMBIGUITY_JUSTIFIED',['YES','NO'],r)}<div class="field"><span class="label">Error type — select all that apply if any answer is NO</span><div class="errors">${errorOptions.map(e=>`<label><input type="checkbox" data-error="${e}" ${errors.includes(e)?'checked':''}> ${e}</label>`).join('')}</div></div><div class="field"><span class="label">Human correction</span><textarea id="correction" placeholder="Optional correction to the extraction">${esc(r.HUMAN_CORRECTION)}</textarea></div><div class="field"><span class="label">Human notes</span><textarea id="humanNotes" placeholder="Short methodological observation">${esc(r.HUMAN_NOTES)}</textarea></div><button id="saveRecord" class="primary">Save this record locally</button></div></div></div>`;
document.querySelectorAll('[data-q]').forEach(el=>el.addEventListener('change',e=>setField(r,e.target.dataset.q,e.target.value)));document.querySelectorAll('[data-error]').forEach(el=>el.addEventListener('change',e=>setError(r,e.target.dataset.error,e.target.checked)));document.getElementById('reviewer').addEventListener('change',e=>{r.HUMAN_REVIEWER=e.target.value;saveState()});document.getElementById('correction').addEventListener('input',e=>{r.HUMAN_CORRECTION=e.target.value;r.HUMAN_REVIEW_STATUS=r.HUMAN_REVIEW_STATUS==='REVIEWED'?'IN_PROGRESS':r.HUMAN_REVIEW_STATUS;saveState()});document.getElementById('humanNotes').addEventListener('input',e=>{r.HUMAN_NOTES=e.target.value;saveState()});document.getElementById('saveRecord').addEventListener('click',()=>{r.HUMAN_REVIEWER=reviewer();r.HUMAN_REVIEW_STATUS=isComplete(r)?'REVIEWED':'IN_PROGRESS';saveState();render();setNotice(r.HUMAN_REVIEW_STATUS==='REVIEWED'?'Record marked REVIEWED after required choices.':'Record saved as IN_PROGRESS.')})}
function download(name,text,type){const a=document.createElement('a');a.href=URL.createObjectURL(new Blob([text],{type}));a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(a.href),1000)}function csv(){const cols=[...new Set(records.flatMap(r=>Object.keys(r)))];const q=v=>'"'+String(v??'').replace(/"/g,'""')+'"';return [cols.map(q).join(','),...records.map(r=>cols.map(c=>q(r[c])).join(','))].join('\r\n')}function exportCsv(){download('R4_2B_HUMAN_QA_REVIEW_COMPLETED.csv',csv(),'text/csv;charset=utf-8')}function exportJson(){download('R4_2B_HUMAN_QA_REVIEW_COMPLETED.json',JSON.stringify(records,null,2),'application/json;charset=utf-8')}
document.getElementById('caseFilter').onchange=()=>{current=0;render()};document.getElementById('confidenceFilter').onchange=()=>{current=0;render()};document.getElementById('ambiguityFilter').onchange=()=>{current=0;render()};document.getElementById('statusFilter').onchange=()=>{current=0;render()};document.getElementById('prevBtn').onclick=()=>{if(current>0){current--;render()}};document.getElementById('nextBtn').onclick=()=>{if(current<filtered.length-1){current++;render()}};document.getElementById('gotoBtn').onclick=()=>{const n=Number(document.getElementById('goto').value);if(n>=1&&n<=records.length){const id=records[n-1].QA_ID;const pos=filtered.findIndex(r=>r.QA_ID===id);if(pos>=0){current=pos;render()}else{setNotice('That record is hidden by the current filters.')}}};document.getElementById('saveBtn').onclick=saveState;document.getElementById('csvBtn').onclick=exportCsv;document.getElementById('jsonBtn').onclick=exportJson;loadState();render();
</script></body></html>
'@
$html=$html.Replace('__DATA_JSON__',$json)
$htmlPath=Join-Path $reviewDir 'R4_2B_HUMAN_REVIEW_PANEL.html'
[System.IO.File]::WriteAllText($htmlPath,$html,(New-Object System.Text.UTF8Encoding($false)))

$readme=@'
# R4.2B Human Review Interface

This folder is a separate manual-review package. It does not modify the original Luna extraction or the original 90-row QA sample.

## Use

1. Open `R4_2B_HUMAN_REVIEW_PANEL.html` in a standard browser.
2. Review the full frozen legal provision against the Luna extraction.
3. Answer only extraction-fidelity questions: actor, action, object, counterpart, recipient, source pointer, excerpt and structural ambiguity.
4. Do not decide regulator, intermediary or target status, and do not classify mechanisms.
5. Use **Save locally** to persist decisions in the browser's local storage.
6. After completing the review, use **Export CSV** and/or **Export JSON** and preserve the exported file as the researcher-reviewed record.

## Files

- `R4_2B_HUMAN_REVIEW_WORKING.csv` — 90-row working dataset with full source provision and adjacent context.
- `R4_2B_HUMAN_REVIEW_PANEL.html` — self-contained local interface; no server or external resources required.

The working dataset starts with all human decision fields blank and all rows `PENDING`. The default reviewer display is `Igor Caires Machado`, but a row is not marked reviewed until the required choices are explicitly completed.

The legal text comes only from the frozen R4.1 processing corpus. The original truncated Luna excerpt remains separately visible and is not silently replaced.
'@
[System.IO.File]::WriteAllText((Join-Path $reviewDir 'README_HUMAN_REVIEW.md'),$readme,(New-Object System.Text.UTF8Encoding($false)))

Write-Output "Human review interface built: records=$($working.Count); resolved=$(@($working|Where-Object SOURCE_RESOLUTION_STATUS -like 'RESOLVED*').Count); html=$htmlPath"
