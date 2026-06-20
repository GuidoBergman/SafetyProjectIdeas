#!/usr/bin/env python3
"""Build a self-contained HTML browser for ranked SAIM proposals.

Merges one or more pipeline runs' ``rank/ranked_proposals.json`` files into a
single static HTML page (no server required). The page shows each proposal's
Research Question by default and lets the reader expand the remaining fields,
filter by score / batch / subfield / strategy / novelty, sort, and deep-link to
any idea via a permalink.

Cross-batch handling:
  - ID collisions are resolved by keeping the first occurrence's id and suffixing
    later ones with the batch short tag (e.g. ``gen-037`` -> ``gen-037-B2``). The
    original id is preserved on the card as a "(was ...)" note.
  - Every idea is tagged with the batch/run that produced it.
  - Every idea shows whether its novelty was ``calculated`` (novelty_assessed:
    web search + citation verification) or ``estimated`` (novelty_estimated:
    unreliable LLM guess).

Usage:
    uv run python scripts/build_proposals_browser.py            # default batches
    uv run python scripts/build_proposals_browser.py RUN_DIR [RUN_DIR ...]
    uv run python scripts/build_proposals_browser.py RUN_DIR:Friendly\\ Label ...
    uv run python scripts/build_proposals_browser.py -o out.html RUN_DIR ...

Each RUN_DIR is a pipeline run directory (containing ``rank/ranked_proposals.json``)
or a direct path to a ranked_proposals.json file. An optional ``:label`` suffix
overrides the auto-derived batch label. Batches are processed in the order given;
earlier batches keep their ids on collision.
"""

from __future__ import annotations

import argparse
import datetime
import json
from pathlib import Path

# Default batches used when no run dirs are passed on the command line.
DEFAULT_BATCHES = [
    ("data/runs/2026-06-15T19-24-29", "2026-06-15 (full pipeline)"),
    ("data/runs/2026-06-20T15-40-46", "2026-06-20 (paper-driven / light)"),
]
DEFAULT_OUT = "data/output/proposals_browser.html"


def resolve_rank_json(run_dir: str) -> Path:
    """Accept either a run directory or a direct path to ranked_proposals.json."""
    p = Path(run_dir)
    if p.is_file():
        return p
    candidate = p / "rank" / "ranked_proposals.json"
    if candidate.is_file():
        return candidate
    raise FileNotFoundError(f"No ranked_proposals.json found for {run_dir!r}")


def load_batch(spec: tuple[str, str], short: str) -> dict:
    """Load one batch's records. ``spec`` is (run_dir, label)."""
    run_dir, label = spec
    path = resolve_rank_json(run_dir)
    items = json.load(open(path, encoding="utf-8"))
    run_id = items[0].get("run_id", "") if items else ""
    return {"label": label, "short": short, "run_id": run_id, "path": str(path), "items": items}


def build_records(batches: list[dict]) -> list[dict]:
    """Flatten all batches into display records, resolving id collisions."""
    seen_ids: set[str] = set()
    records: list[dict] = []
    for b in batches:
        for it in b["items"]:
            orig_id = it.get("idea_id", "")
            new_id = orig_id
            renamed = False
            if new_id in seen_ids:
                cand = f"{orig_id}-{b['short']}"
                n = 2
                while cand in seen_ids:
                    cand = f"{orig_id}-{b['short']}-{n}"
                    n += 1
                new_id = cand
                renamed = True
            seen_ids.add(new_id)

            s = it.get("sections", {}) or {}
            sc = it.get("scores", {}) or {}
            novelty_reasoning = (
                sc["novelty"].get("reasoning", "") if isinstance(sc.get("novelty"), dict) else ""
            )
            method = it.get("novelty_method", "")
            novelty_kind = (
                "calculated"
                if method == "novelty_assessed"
                else "estimated"
                if method == "novelty_estimated"
                else (method or "unknown")
            )
            # B1-era runs use refinement_confidence; light runs use confidence.
            conf = it.get("refinement_confidence", it.get("confidence"))

            records.append(
                {
                    "id": new_id,
                    "orig_id": orig_id if renamed else "",
                    "batch": b["label"],
                    "batch_short": b["short"],
                    "run_id": b["run_id"],
                    "rank": it.get("rank"),
                    "title": it.get("title", ""),
                    "score": round(it.get("weighted_score", 0), 3),
                    "subfield": it.get("subfield", ""),
                    "strategy": it.get("generation_strategy", ""),
                    "novelty_class": it.get("novelty_classification", ""),
                    "novelty_score": it.get("novelty_score"),
                    "novelty_method": method,
                    "novelty_kind": novelty_kind,
                    "confidence": conf,
                    "scores": it.get("original_scores", {}) or {},
                    "novelty_reasoning": novelty_reasoning,
                    "rq": s.get("research_question", ""),
                    "approach": s.get("approach_outline", ""),
                    "experiments": s.get("proposed_first_experiments", ""),
                    "impact": s.get("theory_of_impact_chain", ""),
                    "strength": s.get("strength_rationale", ""),
                    "framings": s.get("alternative_framings", []) or [],
                    "sources": s.get("cited_sources", []) or [],
                }
            )
    return records


def render_html(records: list[dict], batch_sub: str) -> str:
    gen = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d %H:%M UTC")
    payload = json.dumps(records, ensure_ascii=False)
    return (
        HTML_TEMPLATE.replace("__PAYLOAD__", payload)
        .replace("__GEN__", gen)
        .replace("__BATCHSUB__", batch_sub)
    )


def main() -> None:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument(
        "runs", nargs="*", help="Run dirs or ranked_proposals.json paths, optional :label suffix"
    )
    ap.add_argument(
        "-o", "--out", default=DEFAULT_OUT, help=f"Output HTML path (default: {DEFAULT_OUT})"
    )
    args = ap.parse_args()

    if args.runs:
        specs = []
        for raw in args.runs:
            # Split on the last ':' only if it is not part of a Windows-style path.
            if ":" in raw and not raw[1:3] == ":\\":
                run_dir, label = raw.rsplit(":", 1)
            else:
                run_dir, label = raw, ""
            label = label or Path(run_dir).name
            specs.append((run_dir, label))
    else:
        specs = DEFAULT_BATCHES

    batches = [load_batch(spec, f"B{i + 1}") for i, spec in enumerate(specs)]
    records = build_records(batches)
    renamed = [(r["orig_id"], r["id"]) for r in records if r["orig_id"]]

    batch_sub = " + ".join(b["label"] for b in batches)
    html_text = render_html(records, batch_sub)

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html_text, encoding="utf-8")

    print(
        f"Wrote {out}: {len(records)} proposals from {len(batches)} batch(es), "
        f"{round(len(html_text) / 1024)} KB"
    )
    for b in batches:
        print(f"  {b['short']}: {len(b['items'])} proposals — {b['label']} ({b['path']})")
    if renamed:
        print(
            f"Renamed {len(renamed)} colliding id(s): " + ", ".join(f"{o}->{n}" for o, n in renamed)
        )


HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SAIM Ranked Proposals Browser</title>
<style>
  :root{
    --bg:#0f1115; --panel:#171a21; --panel2:#1e222b; --border:#2a2f3a;
    --text:#e6e9ef; --muted:#9aa3b2; --accent:#5b8cff; --accent2:#7c5cff;
    --good:#3ecf8e; --warn:#f5a623; --bad:#ff6b6b; --chip:#252a35;
  }
  *{box-sizing:border-box}
  body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
       background:var(--bg);color:var(--text);font-size:14px;line-height:1.5}
  header{position:sticky;top:0;z-index:10;background:linear-gradient(180deg,#141821,#11141b);
         border-bottom:1px solid var(--border);padding:14px 20px}
  h1{margin:0;font-size:18px;font-weight:650}
  .sub{color:var(--muted);font-size:12px;margin-top:3px}
  .controls{display:flex;flex-wrap:wrap;gap:10px;margin-top:12px;align-items:flex-end}
  .ctrl{display:flex;flex-direction:column;gap:4px}
  .ctrl label{font-size:11px;color:var(--muted);text-transform:uppercase;letter-spacing:.04em}
  input,select{background:var(--panel2);border:1px solid var(--border);color:var(--text);
        padding:7px 9px;border-radius:7px;font-size:13px;outline:none}
  input:focus,select:focus{border-color:var(--accent)}
  input[type=text]{min-width:230px}
  input[type=number]{width:78px}
  select[multiple]{min-width:160px;height:82px}
  .btn{background:var(--chip);border:1px solid var(--border);color:var(--text);cursor:pointer;
       padding:7px 12px;border-radius:7px;font-size:13px}
  .btn:hover{border-color:var(--accent)}
  .meta-row{display:flex;gap:16px;flex-wrap:wrap;align-items:center;margin-top:10px;color:var(--muted);font-size:12px}
  .count{color:var(--text);font-weight:600}
  main{padding:16px 20px;max-width:1100px;margin:0 auto}
  .card{background:var(--panel);border:1px solid var(--border);border-radius:11px;margin-bottom:12px;overflow:hidden;scroll-margin-top:200px}
  .card:target{border-color:var(--accent);box-shadow:0 0 0 2px rgba(91,140,255,.35)}
  .card-head{display:flex;gap:12px;padding:13px 15px;cursor:pointer;align-items:flex-start}
  .card-head:hover{background:var(--panel2)}
  .rankbadge{flex:0 0 auto;display:flex;flex-direction:column;align-items:center;min-width:54px}
  .rankbadge .r{font-size:11px;color:var(--muted)}
  .scorepill{font-weight:700;font-size:15px;padding:3px 9px;border-radius:8px;background:var(--chip);margin-top:2px}
  .s-hi{color:var(--good)} .s-mid{color:var(--warn)} .s-lo{color:var(--bad)}
  .head-main{flex:1;min-width:0}
  .title{font-weight:640;font-size:15px;margin:0 0 3px}
  .idline{font-size:12px;color:var(--muted);font-family:ui-monospace,Menlo,monospace;display:flex;gap:8px;align-items:center;flex-wrap:wrap}
  .permalink{color:var(--accent);text-decoration:none;font-size:12px}
  .permalink:hover{text-decoration:underline}
  .renamed{color:var(--warn);font-size:11px}
  .chips{display:flex;gap:6px;flex-wrap:wrap;margin:7px 0 4px}
  .chip{background:var(--chip);border:1px solid var(--border);color:var(--muted);
        padding:2px 8px;border-radius:20px;font-size:11px}
  .chip.sf{color:#8fc7ff} .chip.st{color:#c5b3ff} .chip.nv{color:#ffd28f}
  .chip.bt{color:#9affc4;border-color:#2f5b43}
  .chip.calc{color:#3ecf8e;border-color:#2f5b43}
  .chip.est{color:#1a1d24;background:var(--warn);border-color:var(--warn);font-weight:600}
  .rq{margin-top:8px;color:var(--text)}
  .rq b{color:var(--muted);font-weight:600;font-size:11px;text-transform:uppercase;letter-spacing:.04em;display:block;margin-bottom:2px}
  .expand-ico{flex:0 0 auto;color:var(--muted);transition:transform .15s;margin-top:3px}
  .card.open .expand-ico{transform:rotate(90deg)}
  .body{display:none;padding:0 15px 14px 81px;border-top:1px solid var(--border)}
  .card.open .body{display:block}
  .sec{margin-top:13px}
  .sec h4{margin:0 0 4px;font-size:11px;color:var(--accent);text-transform:uppercase;letter-spacing:.05em}
  .sec .txt{white-space:pre-wrap;color:#d4d9e3}
  .sec ul{margin:4px 0;padding-left:18px}
  .sec li{margin-bottom:3px;color:#d4d9e3}
  .scoregrid{display:flex;flex-wrap:wrap;gap:8px;margin-top:4px}
  .sbox{background:var(--panel2);border:1px solid var(--border);border-radius:7px;padding:5px 9px;font-size:12px}
  .sbox span{color:var(--muted)}
  .sbox b{color:var(--text);margin-left:5px}
  .empty{text-align:center;color:var(--muted);padding:50px}
  a{color:var(--accent)}
  .toggleall{margin-left:auto}
</style>
</head>
<body>
<header>
  <h1>SAIM Ranked Proposals Browser</h1>
  <div class="sub">__BATCHSUB__ &middot; __GEN__ &middot; <span id="total">0</span> proposals</div>
  <div class="controls">
    <div class="ctrl">
      <label>Search (title / id / question)</label>
      <input type="text" id="q" placeholder="type to filter...">
    </div>
    <div class="ctrl">
      <label>Min score</label>
      <input type="number" id="smin" step="0.1" min="0" max="5" placeholder="0">
    </div>
    <div class="ctrl">
      <label>Max score</label>
      <input type="number" id="smax" step="0.1" min="0" max="5" placeholder="5">
    </div>
    <div class="ctrl">
      <label>Batch</label>
      <select id="fbatch" multiple></select>
    </div>
    <div class="ctrl">
      <label>Subfield</label>
      <select id="fsub" multiple></select>
    </div>
    <div class="ctrl">
      <label>Strategy</label>
      <select id="fstrat" multiple></select>
    </div>
    <div class="ctrl">
      <label>Novelty class</label>
      <select id="fnov" multiple></select>
    </div>
    <div class="ctrl">
      <label>Novelty method</label>
      <select id="fmethod" multiple>
        <option value="calculated">calculated</option>
        <option value="estimated">estimated</option>
      </select>
    </div>
    <div class="ctrl">
      <label>Sort by</label>
      <select id="sort">
        <option value="rank">Rank (best first)</option>
        <option value="score_desc">Score high&rarr;low</option>
        <option value="score_asc">Score low&rarr;high</option>
        <option value="id">ID</option>
        <option value="title">Title A&rarr;Z</option>
        <option value="novelty">Novelty score</option>
      </select>
    </div>
    <button class="btn" id="reset">Reset</button>
    <button class="btn toggleall" id="toggleall">Expand all</button>
  </div>
  <div class="meta-row">
    <div><span class="count" id="shown">0</span> shown</div>
  </div>
</header>
<main>
  <div id="list"></div>
  <div class="empty" id="empty" style="display:none">No proposals match your filters.</div>
</main>
<script>
const DATA = __PAYLOAD__;
const CRIT_LABELS = {theory_of_impact:'Impact',accessible_complexity:'Accessible',narrow_scope:'Narrow',counterfactual_value:'Counterfactual',low_compute:'Low compute',novelty:'Novelty'};
const esc = s => (s==null?'':String(s)).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const list = document.getElementById('list');
let openState = {};

function uniq(key){return [...new Set(DATA.map(d=>d[key]).filter(Boolean))].sort();}
function fillSelect(id, vals){const el=document.getElementById(id);vals.forEach(v=>{const o=document.createElement('option');o.value=v;o.textContent=v;el.appendChild(o);});}
fillSelect('fbatch', uniq('batch'));
fillSelect('fsub', uniq('subfield'));
fillSelect('fstrat', uniq('strategy'));
fillSelect('fnov', uniq('novelty_class'));

function selVals(id){return [...document.getElementById(id).selectedOptions].map(o=>o.value);}
function scoreClass(s){return s>=4?'s-hi':s>=3?'s-mid':'s-lo';}

function render(){
  const q=document.getElementById('q').value.trim().toLowerCase();
  const smin=parseFloat(document.getElementById('smin').value);
  const smax=parseFloat(document.getElementById('smax').value);
  const batches=selVals('fbatch'), subs=selVals('fsub'), strats=selVals('fstrat'),
        novs=selVals('fnov'), methods=selVals('fmethod');
  const sort=document.getElementById('sort').value;

  let rows=DATA.filter(d=>{
    if(q && !((d.title||'').toLowerCase().includes(q) || (d.id||'').toLowerCase().includes(q) || (d.rq||'').toLowerCase().includes(q))) return false;
    if(!isNaN(smin) && d.score<smin) return false;
    if(!isNaN(smax) && d.score>smax) return false;
    if(batches.length && !batches.includes(d.batch)) return false;
    if(subs.length && !subs.includes(d.subfield)) return false;
    if(strats.length && !strats.includes(d.strategy)) return false;
    if(novs.length && !novs.includes(d.novelty_class)) return false;
    if(methods.length && !methods.includes(d.novelty_kind)) return false;
    return true;
  });

  rows.sort((a,b)=>{
    switch(sort){
      case 'score_desc': return b.score-a.score;
      case 'score_asc': return a.score-b.score;
      case 'id': return (a.id||'').localeCompare(b.id||'',undefined,{numeric:true});
      case 'title': return (a.title||'').localeCompare(b.title||'');
      case 'novelty': return (b.novelty_score||0)-(a.novelty_score||0);
      default: return (a.rank||1e9)-(b.rank||1e9);
    }
  });

  document.getElementById('shown').textContent=rows.length;
  document.getElementById('empty').style.display=rows.length?'none':'block';
  list.innerHTML=rows.map(cardHTML).join('');
}

function listSec(title,arr){
  if(!arr||!arr.length) return '';
  return `<div class="sec"><h4>${esc(title)}</h4><ul>${arr.map(x=>`<li>${esc(x)}</li>`).join('')}</ul></div>`;
}
function txtSec(title,txt){
  if(!txt) return '';
  return `<div class="sec"><h4>${esc(title)}</h4><div class="txt">${esc(txt)}</div></div>`;
}

function cardHTML(d){
  const open=openState[d.id]?'open':'';
  const sc=d.scores||{};
  const sgrid=Object.keys(CRIT_LABELS).filter(k=>k in sc).map(k=>
    `<div class="sbox"><span>${CRIT_LABELS[k]}</span><b>${sc[k]}</b></div>`).join('');
  const nov = d.novelty_class ? `${esc(d.novelty_class)}${d.novelty_score!=null?' ('+d.novelty_score+'/5)':''}` : '';
  const methodChip = d.novelty_kind==='calculated'
      ? `<span class="chip calc" title="Novelty from web search + citation verification">novelty: calculated</span>`
      : `<span class="chip est" title="Unreliable LLM guess — no literature search">novelty: estimated</span>`;
  const renamed = d.orig_id ? `<span class="renamed" title="ID changed to avoid collision across batches">(was ${esc(d.orig_id)})</span>` : '';
  return `
  <div class="card ${open}" id="${esc(d.id)}" data-id="${esc(d.id)}">
    <div class="card-head" onclick="toggle('${esc(d.id)}')">
      <div class="rankbadge">
        <div class="r">#${d.rank??'-'}</div>
        <div class="scorepill ${scoreClass(d.score)}">${d.score.toFixed(2)}</div>
      </div>
      <div class="head-main">
        <div class="title">${esc(d.title)}</div>
        <div class="idline">
          <span>${esc(d.id)}</span>
          ${renamed}
          <a class="permalink" href="#${esc(d.id)}" onclick="event.stopPropagation()" title="Permalink to this idea">&#128279; link</a>
        </div>
        <div class="chips">
          <span class="chip bt" title="Generation batch / run">${esc(d.batch_short)} &middot; ${esc(d.batch)}</span>
          ${methodChip}
          ${d.subfield?`<span class="chip sf">${esc(d.subfield)}</span>`:''}
          ${d.strategy?`<span class="chip st">${esc(d.strategy)}</span>`:''}
          ${nov?`<span class="chip nv">${nov}</span>`:''}
          ${d.confidence!=null?`<span class="chip">conf ${d.confidence}</span>`:''}
        </div>
        <div class="rq"><b>Research Question</b>${esc(d.rq)}</div>
      </div>
      <div class="expand-ico">&#9654;</div>
    </div>
    <div class="body">
      ${txtSec('Approach', d.approach)}
      ${txtSec('Proposed First Experiments', d.experiments)}
      ${txtSec('Theory of Impact', d.impact)}
      ${txtSec('Strength Rationale', d.strength)}
      ${listSec('Alternative Framings', d.framings)}
      ${listSec('Cited Sources', d.sources)}
      <div class="sec"><h4>Scores</h4><div class="scoregrid">${sgrid}</div></div>
      <div class="sec"><h4>Provenance</h4><div class="txt">Batch: ${esc(d.batch)}  (run_id ${esc(d.run_id)})\nNovelty method: ${esc(d.novelty_method)} &rarr; <b>${esc(d.novelty_kind)}</b></div></div>
      ${txtSec('Novelty Assessment reasoning', d.novelty_reasoning)}
    </div>
  </div>`;
}

window.toggle=function(id){openState[id]=!openState[id];const c=list.querySelector(`.card[data-id="${CSS.escape(id)}"]`);if(c)c.classList.toggle('open');};

let allOpen=false;
document.getElementById('toggleall').onclick=function(){
  allOpen=!allOpen;
  DATA.forEach(d=>openState[d.id]=allOpen);
  this.textContent=allOpen?'Collapse all':'Expand all';
  render();
};

['q','smin','smax','sort','fbatch','fsub','fstrat','fnov','fmethod'].forEach(id=>{
  const el=document.getElementById(id);
  el.addEventListener('input',render);
  el.addEventListener('change',render);
});
document.getElementById('reset').onclick=function(){
  document.getElementById('q').value='';
  document.getElementById('smin').value='';
  document.getElementById('smax').value='';
  ['fbatch','fsub','fstrat','fnov','fmethod'].forEach(id=>[...document.getElementById(id).options].forEach(o=>o.selected=false));
  document.getElementById('sort').value='rank';
  render();
};

function openFromHash(){
  const id=decodeURIComponent(location.hash.replace(/^#/,''));
  if(!id) return;
  if(DATA.some(d=>d.id===id)){
    openState[id]=true; render();
    const el=document.getElementById(id);
    if(el){el.classList.add('open'); el.scrollIntoView({behavior:'smooth',block:'start'});}
  }
}
window.addEventListener('hashchange', openFromHash);

document.getElementById('total').textContent=DATA.length;
render();
openFromHash();
</script>
</body>
</html>"""


if __name__ == "__main__":
    main()
