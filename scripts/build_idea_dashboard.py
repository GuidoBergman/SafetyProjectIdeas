#!/usr/bin/env python3
"""Build the SAIM idea dashboard: a self-contained Artifact page for one or more runs.

The output is an HTML *fragment* (no doctype/html/head/body tags) because the
Artifact tool wraps it in a document skeleton at publish time. Publish it with:

    Artifact(file_path=<out>, capabilities={"artifact": {}}, favicon="\N{ELECTRIC LIGHT BULB}")

The page gives the reader three things:
  1. Ideas ranked by the pipeline's weighted score (rank order is the default sort).
  2. Full-text search plus facet filters (subfield, strategy, novelty, score range).
  3. A shared review status per idea. Status changes are written back into the page
     itself through the ``artifact`` runtime capability, so everyone holding the
     link sees the same statuses.

Usage:
    uv run python scripts/build_idea_dashboard.py <RUN_DIR> [<RUN_DIR> ...]
    uv run python scripts/build_idea_dashboard.py <RUN_DIR> --out data/output/dashboard.html
    uv run python scripts/build_idea_dashboard.py --demo --out /tmp/demo.html

Each RUN_DIR is a pipeline run directory (containing ``rank/ranked_proposals.json``)
or a direct path to a ranked_proposals.json file, with an optional ``:label`` suffix.
``--seed-status`` pre-fills the status of every idea already listed in a tracker
markdown file (``data/output/idea_tracker.md``).

Statuses set inside the published artifact do NOT flow back to the tracker file.
Once the page is shared, the artifact is the live record of review status.
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
from pathlib import Path

DEFAULT_OUT = "dashboard.html"

#: Review status vocabulary, in workflow order. Mirrors data/output/idea_tracker.md.
STATUSES = [
    "Not reviewed",
    "Evaluating",
    "Added and needs manual review",
    "Added",
    "Not promising",
    "Removed",
]

#: Ideas the pipeline has not been reviewed yet start here.
DEFAULT_STATUS = STATUSES[0]

DEMO_RECORDS = [
    {
        "id": "gen-demo01",
        "rank": 1,
        "title": "Do Refusal Directions Transfer Across Fine-Tunes of the Same Base Model?",
        "score": 4.62,
        "subfield": "Mechanistic Interpretability",
        "strategy": "extend_recent_paper",
        "novelty_class": "mostly_novel",
        "novelty_score": 4,
        "novelty_method": "novelty_assessed",
        "novelty_kind": "calculated",
        "confidence": 0.81,
        "scores": {
            "theory_of_impact": 5,
            "low_compute": 5,
            "accessible_complexity": 4,
            "narrow_scope": 5,
            "counterfactual_value": 4,
            "novelty": 4,
        },
        "rq": "Does the single refusal direction found in a base model still mediate refusal in models fine-tuned from it, or does each fine-tune relearn its own?",
        "approach": "Extract the refusal direction on the base model, then test ablation transfer on three public fine-tunes of it.",
        "experiments": "Compute the difference-in-means direction on harmful/harmless prompt pairs; ablate it in each fine-tune; measure refusal rate change.",
        "impact": "If directions transfer, one audit of a base model covers its whole fine-tune family, which is what open-weight ecosystems actually need.",
        "strength": "Inference-only, small open models, a single clean measurement with an unambiguous negative result.",
        "framings": [
            "Restrict to safety fine-tunes only",
            "Compare against probe-based refusal detection",
        ],
        "sources": ["Refusal in LLMs Is Mediated by a Single Direction (arXiv 2406.11717)"],
        "novelty_reasoning": "ASSESSED: the single-direction result is established; transfer across fine-tunes of a shared base is not measured in the cited literature.",
        "batch": "demo run",
        "batch_short": "B1",
        "run_id": "demo",
        "orig_id": "",
    },
    {
        "id": "gen-demo02",
        "rank": 2,
        "title": "How Much Does Monitor Prompt Detail Change Detection Performance?",
        "score": 4.28,
        "subfield": "AI Control / Monitoring",
        "strategy": "failure_mode_investigation",
        "novelty_class": "partially_addressed",
        "novelty_score": 3,
        "novelty_method": "novelty_assessed",
        "novelty_kind": "calculated",
        "confidence": 0.74,
        "scores": {
            "theory_of_impact": 4,
            "low_compute": 5,
            "accessible_complexity": 5,
            "narrow_scope": 5,
            "counterfactual_value": 4,
            "novelty": 3,
        },
        "rq": "Does a one-line monitor prompt detect sabotage as reliably as a detailed rubric, or is reported monitor performance mostly prompt engineering?",
        "approach": "Run one monitor model over a fixed trajectory set under four prompt specifications of increasing detail.",
        "experiments": "Hold the trajectories and monitor model fixed; vary only the prompt; report AUROC per specification with bootstrap intervals.",
        "impact": "Control evaluations quote monitor AUROC as a property of the model. If the prompt dominates, those numbers are not comparable across papers.",
        "strength": "One variable, one metric, published trajectory datasets, no training.",
        "framings": ["Add a second monitor model to separate prompt from model effects"],
        "sources": [
            "AI Control: Improving Safety Despite Intentional Subversion (arXiv 2312.06942)"
        ],
        "novelty_reasoning": "ASSESSED: prompt sensitivity is noted anecdotally in control papers but not measured as a controlled variable.",
        "batch": "demo run",
        "batch_short": "B1",
        "run_id": "demo",
        "orig_id": "",
    },
    {
        "id": "gen-demo03",
        "rank": 3,
        "title": "Are Safety Benchmark Scores Inflated by Training-Data Contamination?",
        "score": 3.91,
        "subfield": "Evaluations & Benchmarks",
        "strategy": "measurement_validity",
        "novelty_class": "partially_addressed",
        "novelty_score": 3,
        "novelty_method": "novelty_estimated",
        "novelty_kind": "estimated",
        "confidence": 0.6,
        "scores": {
            "theory_of_impact": 4,
            "low_compute": 4,
            "accessible_complexity": 4,
            "narrow_scope": 4,
            "counterfactual_value": 4,
            "novelty": 3,
        },
        "rq": "Do models score higher on safety benchmark items that appear verbatim in public training corpora than on paraphrases of the same items?",
        "approach": "Match benchmark prompts against public corpora, then compare scores on matched versus paraphrased items.",
        "experiments": "Build a paraphrase set for 200 items; run three open models; compare refusal rates on original versus paraphrase.",
        "impact": "Deployment decisions cite these scores. A measurable contamination gap tells labs how much to discount them.",
        "strength": "Cheap, fully reproducible on open models and open corpora.",
        "framings": ["Restrict to one benchmark and go deeper on match quality"],
        "sources": ["StrongREJECT (arXiv 2402.10260)"],
        "novelty_reasoning": "ESTIMATED — no literature search was run for this record. Treat as unverified.",
        "batch": "demo run",
        "batch_short": "B1",
        "run_id": "demo",
        "orig_id": "",
    },
]


def resolve_rank_json(run_dir: str) -> Path:
    """Accept either a run directory or a direct path to ranked_proposals.json."""
    p = Path(run_dir)
    if p.is_file():
        return p
    candidate = p / "rank" / "ranked_proposals.json"
    if candidate.is_file():
        return candidate
    raise FileNotFoundError(f"No ranked_proposals.json found for {run_dir!r}")


def parse_run_spec(raw: str) -> tuple[str, str]:
    """Split a ``RUN_DIR[:label]`` argument into (run_dir, label)."""
    if ":" in raw and raw[1:3] != ":\\":
        run_dir, label = raw.rsplit(":", 1)
        if label:
            return run_dir, label
        raw = run_dir
    return raw, Path(raw).name


def novelty_kind(method: str) -> str:
    """Map a novelty_method to the two words a reader needs: calculated or estimated."""
    if method == "novelty_assessed":
        return "calculated"
    if method == "novelty_estimated":
        return "estimated"
    return method or "unknown"


def to_record(item: dict, batch_label: str, batch_short: str, idea_id: str, orig_id: str) -> dict:
    """Flatten one ranked proposal into the record the page renders."""
    sections = item.get("sections") or {}
    scores = item.get("scores") or {}
    novelty = scores.get("novelty")
    method = item.get("novelty_method", "")
    return {
        "id": idea_id,
        "orig_id": orig_id,
        "batch": batch_label,
        "batch_short": batch_short,
        "run_id": item.get("run_id", ""),
        "rank": item.get("rank"),
        "title": item.get("title", ""),
        "score": round(item.get("weighted_score") or 0, 3),
        "subfield": item.get("subfield", ""),
        "strategy": item.get("generation_strategy", ""),
        "novelty_class": item.get("novelty_classification", ""),
        "novelty_score": item.get("novelty_score"),
        "novelty_method": method,
        "novelty_kind": novelty_kind(method),
        "confidence": item.get("refinement_confidence", item.get("confidence")),
        "scores": item.get("original_scores") or {},
        "novelty_reasoning": novelty.get("reasoning", "") if isinstance(novelty, dict) else "",
        "rq": sections.get("research_question", ""),
        "approach": sections.get("approach_outline", ""),
        "experiments": sections.get("proposed_first_experiments", ""),
        "impact": sections.get("theory_of_impact_chain", ""),
        "strength": sections.get("strength_rationale", ""),
        "framings": sections.get("alternative_framings") or [],
        "sources": sections.get("cited_sources") or [],
    }


def build_records(batches: list[dict]) -> list[dict]:
    """Flatten every batch into display records, keeping ids unique across batches."""
    seen: set[str] = set()
    records: list[dict] = []
    for batch in batches:
        for item in batch["items"]:
            orig = item.get("idea_id", "")
            idea_id = orig
            if idea_id in seen:
                candidate = f"{orig}-{batch['short']}"
                n = 2
                while candidate in seen:
                    candidate = f"{orig}-{batch['short']}-{n}"
                    n += 1
                idea_id = candidate
            seen.add(idea_id)
            records.append(
                to_record(
                    item, batch["label"], batch["short"], idea_id, orig if idea_id != orig else ""
                )
            )
    return records


def load_batch(run_dir: str, label: str, short: str) -> dict:
    """Load one run's ranked proposals."""
    path = resolve_rank_json(run_dir)
    items = json.loads(path.read_text(encoding="utf-8"))
    return {"label": label, "short": short, "path": str(path), "items": items}


def parse_tracker_statuses(text: str) -> dict[str, str]:
    """Read ``id -> status`` out of an idea_tracker.md table.

    The status cell carries a leading status emoji, which is stripped. Only values in
    ``STATUSES`` are kept, so a malformed row is ignored rather than inventing a status.
    """
    statuses: dict[str, str] = {}
    for line in text.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 5:
            continue
        match = re.search(r"\b(gen-[0-9a-z]+)\b", cells[1])
        if not match:
            continue
        value = re.sub(r"[^\w\s]", "", cells[4]).strip()
        if value in STATUSES:
            statuses[match.group(1)] = value
    return statuses


def seed_statuses(records: list[dict], tracker: dict[str, str]) -> dict[str, dict]:
    """Build the page's initial status map, seeding from a tracker where ids match."""
    now = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d")
    out: dict[str, dict] = {}
    for record in records:
        key = record["orig_id"] or record["id"]
        status = tracker.get(key)
        if status and status != DEFAULT_STATUS:
            out[record["id"]] = {"status": status, "note": "", "by": "idea_tracker.md", "at": now}
    return out


def escape_text(value: str) -> str:
    """Escape a string for use as HTML text content."""
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def json_for_script(value: object) -> str:
    """Serialize to JSON that is safe inside a <script type="application/json"> block."""
    # ensure_ascii keeps the payload pure ASCII, so a republished page cannot mojibake.
    return json.dumps(value, ensure_ascii=True).replace("</", "<\\/")


def render_html(records: list[dict], statuses: dict[str, dict], title: str, subtitle: str) -> str:
    """Render the dashboard fragment. Returns HTML with no doctype/html/head/body wrapper."""
    return (
        TEMPLATE.replace("__TITLE__", escape_text(title))
        .replace("__SUBTITLE__", escape_text(subtitle))
        .replace("__STATUS_LIST__", json.dumps(STATUSES))
        .replace("__DATA__", json_for_script(records))
        .replace("__STATUS__", json_for_script(statuses))
    )


TEMPLATE = r"""<meta data-saim charset="utf-8">
<title>__TITLE__</title>
<link data-saim rel="preconnect" href="https://fonts.googleapis.com">
<link data-saim rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link data-saim rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600;700&display=swap">
<style data-saim>
:root{
  --ground:#eceef3; --panel:#ffffff; --panel-2:#f4f6fa; --border:#d7dbe4; --border-2:#c3c9d6;
  --ink:#161a21; --ink-2:#4c5464; --ink-3:#767f90;
  --accent:#3a55c4; --accent-2:#5a72d6; --accent-soft:#e5e9f8;
  --ok:#1d7f58; --ok-soft:#dcefe6; --watch:#8f6205; --watch-soft:#f7ecca;
  --stop:#b23a31; --stop-soft:#f8dedb; --idle:#6d7789; --idle-soft:#e6e9ef;
  --shadow:0 1px 2px rgba(20,24,32,.05), 0 10px 26px rgba(20,24,32,.05);
  --sans:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  --mono:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
}
@media (prefers-color-scheme: dark){
  :root:not([data-theme="light"]){
    --ground:#0d1016; --panel:#161a22; --panel-2:#1b202a; --border:#272d3a; --border-2:#38414f;
    --ink:#e5e9f0; --ink-2:#a6afbf; --ink-3:#79839a;
    --accent:#8ba2ff; --accent-2:#a5b7ff; --accent-soft:#1c2440;
    --ok:#4cc492; --ok-soft:#122c23; --watch:#e3b243; --watch-soft:#2d2410;
    --stop:#ea7b6f; --stop-soft:#331b19; --idle:#8892a5; --idle-soft:#20242e;
    --shadow:0 1px 2px rgba(0,0,0,.4), 0 10px 26px rgba(0,0,0,.28);
  }
}
:root[data-theme="dark"]{
  --ground:#0d1016; --panel:#161a22; --panel-2:#1b202a; --border:#272d3a; --border-2:#38414f;
  --ink:#e5e9f0; --ink-2:#a6afbf; --ink-3:#79839a;
  --accent:#8ba2ff; --accent-2:#a5b7ff; --accent-soft:#1c2440;
  --ok:#4cc492; --ok-soft:#122c23; --watch:#e3b243; --watch-soft:#2d2410;
  --stop:#ea7b6f; --stop-soft:#331b19; --idle:#8892a5; --idle-soft:#20242e;
  --shadow:0 1px 2px rgba(0,0,0,.4), 0 10px 26px rgba(0,0,0,.28);
}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);font-family:var(--sans);font-size:15px;line-height:1.55;-webkit-font-smoothing:antialiased}
.wrap{max-width:1180px;margin:0 auto;padding:0 20px 72px}
a{color:var(--accent);text-decoration:none}
a:hover{text-decoration:underline}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px;border-radius:4px}

/* ---- header ---- */
.topbar{background:var(--ground);border-bottom:1px solid var(--border);padding-top:22px}
.masthead{display:flex;flex-wrap:wrap;align-items:baseline;gap:10px 16px}
h1{margin:0;font-size:22px;font-weight:600;letter-spacing:-.01em;text-wrap:balance}
.sub{color:var(--ink-3);font-size:13px;font-family:var(--mono)}
.savebar{margin-left:auto;display:flex;align-items:center;gap:10px}
.who{background:var(--panel);border:1px solid var(--border);color:var(--ink);border-radius:7px;padding:6px 9px;font:500 13px var(--sans);width:150px}
.who::placeholder{color:var(--ink-3)}
.savestate{display:inline-flex;align-items:center;gap:7px;font:500 12px var(--sans);color:var(--ink-2);white-space:nowrap}
.dot{width:8px;height:8px;border-radius:50%;background:var(--idle);flex:none}
.savestate[data-state="saving"] .dot{background:var(--watch)}
.savestate[data-state="saved"] .dot{background:var(--ok)}
.savestate[data-state="error"] .dot,.savestate[data-state="readonly"] .dot{background:var(--stop)}

.summary{display:flex;flex-wrap:wrap;gap:8px;margin:16px 0 0}
.statchip{display:inline-flex;align-items:baseline;gap:7px;border:1px solid var(--border);background:var(--panel);
  border-radius:999px;padding:5px 12px 5px 10px;cursor:pointer;font-size:13px;color:var(--ink-2);font-family:var(--sans)}
.statchip:hover{border-color:var(--border-2)}
.statchip[aria-pressed="true"]{border-color:var(--accent);background:var(--accent-soft);color:var(--ink)}
.statchip b{font-family:var(--mono);font-weight:600;font-size:14px;color:var(--ink);font-variant-numeric:tabular-nums}
.statchip .swatch{width:8px;height:8px;border-radius:2px;align-self:center}

.controls{display:flex;flex-wrap:wrap;gap:10px;align-items:flex-end;margin:14px 0 16px}
.ctrl{display:flex;flex-direction:column;gap:5px}
.ctrl label{font:500 10.5px var(--sans);letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3)}
input[type=text],input[type=number],select{background:var(--panel);border:1px solid var(--border);color:var(--ink);
  padding:7px 9px;border-radius:7px;font:400 13px var(--sans)}
input[type=text]#q{min-width:280px}
input[type=number]{width:74px;font-family:var(--mono)}
select[multiple]{min-width:170px;height:88px;font-size:12.5px}
.btn{background:var(--panel);border:1px solid var(--border);color:var(--ink);cursor:pointer;padding:7px 13px;border-radius:7px;font:500 13px var(--sans)}
.btn:hover{border-color:var(--accent)}
.shown{font-family:var(--mono);font-size:12.5px;color:var(--ink-3);padding-bottom:8px}

/* ---- cards ---- */
.card{background:var(--panel);border:1px solid var(--border);border-radius:12px;margin-bottom:12px;box-shadow:var(--shadow);overflow:hidden}
.card.open{border-color:var(--border-2)}
.head{display:grid;grid-template-columns:66px 1fr auto;gap:16px;padding:15px 16px;cursor:pointer;align-items:start}
.rail{display:flex;flex-direction:column;align-items:center;gap:6px;padding-top:2px}
.rank{font:600 13px var(--mono);color:var(--ink-3);font-variant-numeric:tabular-nums}
.score{font:600 17px var(--mono);color:var(--ink);background:var(--panel-2);border:1px solid var(--border);
  border-radius:8px;padding:4px 8px;font-variant-numeric:tabular-nums}
.score.hi{color:var(--accent);border-color:var(--accent);background:var(--accent-soft)}
.title{font-size:16.5px;font-weight:600;line-height:1.35;letter-spacing:-.005em;text-wrap:balance;margin:0 0 6px}
.idline{display:flex;flex-wrap:wrap;gap:10px;align-items:center;font:400 12px var(--mono);color:var(--ink-3);margin-bottom:8px}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:10px}
.chip{font:500 11.5px var(--sans);padding:3px 8px;border-radius:5px;background:var(--panel-2);color:var(--ink-2);border:1px solid var(--border)}
.chip.calc{background:var(--ok-soft);color:var(--ok);border-color:transparent}
.chip.est{background:var(--watch-soft);color:var(--watch);border-color:transparent}
.rq{font-size:14.5px;color:var(--ink-2);max-width:74ch}
.rq b{display:block;font:500 10.5px var(--sans);letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3);margin-bottom:3px}
.headright{display:flex;flex-direction:column;align-items:flex-end;gap:8px}
.caret{color:var(--ink-3);font-size:11px;transition:transform .15s ease}
.card.open .caret{transform:rotate(90deg)}

.statusbox{display:flex;align-items:center;gap:8px}
.statuspill{display:inline-flex;align-items:center;gap:6px;border-radius:999px;padding:4px 11px;font:600 12px var(--sans);
  background:var(--idle-soft);color:var(--ink-2)}
.statuspill .swatch{width:7px;height:7px;border-radius:2px}
.statuspill.s-ok{background:var(--ok-soft);color:var(--ok)}
.statuspill.s-watch{background:var(--watch-soft);color:var(--watch)}
.statuspill.s-stop{background:var(--stop-soft);color:var(--stop)}
select.statussel{font-size:12.5px;padding:5px 7px;max-width:210px}
select.statussel:disabled{opacity:.55;cursor:not-allowed}

.body{display:none;border-top:1px solid var(--border);background:var(--panel-2);padding:6px 16px 18px 16px}
.card.open .body{display:block}
.sec{margin-top:14px}
.sec h4{margin:0 0 5px;font:500 10.5px var(--sans);letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3)}
.sec .txt{white-space:pre-wrap;color:var(--ink-2);font-size:14px;max-width:78ch}
.sec ul{margin:0;padding-left:18px;color:var(--ink-2);font-size:14px}
.scoregrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(126px,1fr));gap:8px}
.sbox{display:flex;justify-content:space-between;align-items:baseline;background:var(--panel);border:1px solid var(--border);
  border-radius:7px;padding:6px 9px;font-size:12.5px;color:var(--ink-3)}
.sbox b{font:600 14px var(--mono);color:var(--ink);font-variant-numeric:tabular-nums}
.notewrap{display:flex;flex-direction:column;gap:6px;margin-top:14px}
textarea.note{background:var(--panel);border:1px solid var(--border);color:var(--ink);border-radius:8px;padding:9px 10px;
  font:400 13.5px var(--sans);min-height:62px;resize:vertical;width:100%;max-width:78ch}
textarea.note:disabled{opacity:.55}
.notemeta{font:400 11.5px var(--mono);color:var(--ink-3)}
.empty{text-align:center;color:var(--ink-3);padding:60px 0;font-size:14px}

.banner{display:none;margin:14px 0 0;border:1px solid var(--border);border-left:3px solid var(--watch);background:var(--panel);
  border-radius:8px;padding:10px 13px;font-size:13.5px;color:var(--ink-2)}
.banner.show{display:block}
#toasts{position:fixed;right:18px;bottom:18px;display:flex;flex-direction:column;gap:8px;z-index:50}
.toast{background:var(--panel);border:1px solid var(--border);border-left:3px solid var(--accent);border-radius:8px;
  padding:9px 13px;font-size:13px;color:var(--ink);box-shadow:var(--shadow);max-width:330px}
.toast.bad{border-left-color:var(--stop)}
@media (prefers-reduced-motion: reduce){*{transition:none !important;animation:none !important}}
@media (max-width:720px){
  .head{grid-template-columns:52px 1fr;}
  .headright{grid-column:1 / -1;align-items:flex-start;flex-direction:row;flex-wrap:wrap}
  input[type=text]#q{min-width:200px}
}
</style>

<div class="topbar">
  <div class="wrap">
    <div class="masthead">
      <h1>__TITLE__</h1>
      <div class="sub">__SUBTITLE__</div>
      <div class="savebar">
        <input class="who" id="who" type="text" placeholder="Your name" aria-label="Your name, recorded with status changes">
        <span class="savestate" id="savestate" data-state="idle"><span class="dot"></span><span id="savetext">Connecting</span></span>
      </div>
    </div>
    <div class="summary" id="summary" data-ephemeral></div>
    <div class="banner" id="banner"></div>
    <div class="controls">
      <div class="ctrl"><label for="q">Search title, id, question</label><input type="text" id="q" placeholder="e.g. refusal direction"></div>
      <div class="ctrl"><label for="smin">Min score</label><input type="number" id="smin" step="0.1" min="0" max="5" placeholder="0"></div>
      <div class="ctrl"><label for="smax">Max score</label><input type="number" id="smax" step="0.1" min="0" max="5" placeholder="5"></div>
      <div class="ctrl"><label for="fsub">Subfield</label><select id="fsub" multiple data-ephemeral></select></div>
      <div class="ctrl"><label for="fstrat">Strategy</label><select id="fstrat" multiple data-ephemeral></select></div>
      <div class="ctrl"><label for="fnov">Novelty</label><select id="fnov" multiple data-ephemeral></select></div>
      <div class="ctrl"><label for="fbatch">Run</label><select id="fbatch" multiple data-ephemeral></select></div>
      <div class="ctrl"><label for="sort">Sort</label>
        <select id="sort">
          <option value="rank">Rank (best first)</option>
          <option value="score_desc">Score high to low</option>
          <option value="score_asc">Score low to high</option>
          <option value="novelty">Novelty score</option>
          <option value="status">Review status</option>
          <option value="title">Title A to Z</option>
          <option value="id">ID</option>
        </select>
      </div>
      <button class="btn" id="reset" type="button">Clear filters</button>
      <button class="btn" id="toggleall" type="button">Expand all</button>
      <div class="shown"><span id="shown">0</span> of <span id="total">0</span> shown</div>
    </div>
  </div>
</div>

<div class="wrap">
  <main id="list" data-ephemeral></main>
  <div class="empty" id="empty" style="display:none">No ideas match these filters.</div>
</div>
<div id="toasts" data-ephemeral></div>

<script data-saim type="application/json" id="saim-data">__DATA__</script>
<script data-saim type="application/json" id="saim-status">__STATUS__</script>
<script data-saim>
const DATA = JSON.parse(document.getElementById('saim-data').textContent);
const STATUS = JSON.parse(document.getElementById('saim-status').textContent);
const STATUSES = __STATUS_LIST__;
const DEFAULT_STATUS = STATUSES[0];
const TONE = {
  'Not reviewed':'s-idle', 'Evaluating':'s-watch', 'Added and needs manual review':'s-watch',
  'Added':'s-ok', 'Not promising':'s-stop', 'Removed':'s-stop'
};
const TONE_VAR = {'s-idle':'var(--idle)','s-watch':'var(--watch)','s-ok':'var(--ok)','s-stop':'var(--stop)'};
const CRIT = {theory_of_impact:'Impact',accessible_complexity:'Accessible',narrow_scope:'Narrow scope',
  counterfactual_value:'Counterfactual',low_compute:'Low compute',novelty:'Novelty'};

const esc = s => (s==null?'':String(s)).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const statusOf = id => (STATUS[id] && STATUS[id].status) || DEFAULT_STATUS;
const el = id => document.getElementById(id);
const list = el('list');
let openState = {}, statusFilter = '';

/* ---------- shared saving through the artifact runtime ---------- */
let api = null, canPublish = false, dirty = false, publishing = false, timer = null;

function setSave(state, text){ const b = el('savestate'); b.dataset.state = state; el('savetext').textContent = text; }

function toast(msg, bad){
  const t = document.createElement('div');
  t.className = 'toast' + (bad ? ' bad' : '');
  t.textContent = msg;
  el('toasts').appendChild(t);
  setTimeout(() => t.remove(), 6000);
}

function readOnly(reason){
  canPublish = false;
  setSave('readonly', 'View only');
  const b = el('banner');
  b.textContent = reason;
  b.classList.add('show');
  document.querySelectorAll('.statussel, textarea.note').forEach(n => { n.disabled = true; });
}

(async function connect(){
  try {
    api = (typeof claude !== 'undefined' && claude.use) ? await claude.use('artifact') : null;
  } catch (e) { api = null; }
  if (api) { canPublish = true; setSave('idle', 'Shared saving on'); }
  else readOnly('Status changes cannot be saved from this view, so anything you set here stays on your screen only. Open the artifact link directly to save for everyone.');
})();

function buildDocument(){
  const clone = document.documentElement.cloneNode(true);
  clone.querySelectorAll('script:not([data-saim]), style:not([data-saim]), link:not([data-saim])').forEach(n => n.remove());
  clone.querySelectorAll('[data-ephemeral]').forEach(n => { n.innerHTML = ''; });
  const store = clone.querySelector('#saim-status');
  if (store) store.textContent = JSON.stringify(STATUS).replace(/<\//g, '<\\/');
  const banner = clone.querySelector('#banner');
  if (banner) { banner.textContent = ''; banner.className = 'banner'; }
  return '<!doctype html>\n<html lang="en">' + clone.innerHTML + '</html>';
}

function schedule(){
  dirty = true;
  setSave('saving', 'Saving');
  clearTimeout(timer);
  timer = setTimeout(flush, 900);
}

async function flush(){
  if (!canPublish || publishing || !dirty) return;
  publishing = true; dirty = false;
  try {
    await api.publish(buildDocument());
    setSave('saved', 'Saved for everyone');
  } catch (e) {
    const code = (e && (e.code || e.name)) || '';
    if (code === 'conflict') {
      setSave('idle', 'Reloading');
      toast('Someone else saved first. Reloading to their version.', true);
    } else if (code === 'not_granted' || code === 'not_writer') {
      readOnly('You have view access to this artifact, so status changes stay on your screen only. Ask the owner for edit access to save for everyone.');
    } else {
      dirty = true;
      setSave('error', 'Save failed');
      toast('Could not save the status change. It will retry on your next edit.', true);
    }
  } finally {
    publishing = false;
    if (dirty) schedule();
  }
}

function reviewer(){ return el('who').value.trim(); }

function setStatus(id, value){
  const rec = STATUS[id] || {status: DEFAULT_STATUS, note: '', by: '', at: ''};
  rec.status = value;
  rec.by = reviewer() || rec.by || 'anonymous';
  rec.at = new Date().toISOString().slice(0, 10);
  if (value === DEFAULT_STATUS && !rec.note) delete STATUS[id]; else STATUS[id] = rec;
  renderSummary();
  paintCard(id);
  schedule();
}

function setNote(id, text){
  const rec = STATUS[id] || {status: DEFAULT_STATUS, note: '', by: '', at: ''};
  if (rec.note === text) return;
  rec.note = text;
  rec.by = reviewer() || rec.by || 'anonymous';
  rec.at = new Date().toISOString().slice(0, 10);
  if (!text && rec.status === DEFAULT_STATUS) delete STATUS[id]; else STATUS[id] = rec;
  paintCard(id);
  schedule();
}

/* ---------- rendering ---------- */
function uniq(key){ return [...new Set(DATA.map(d => d[key]).filter(Boolean))].sort(); }
function fill(id, vals){
  const sel = el(id);
  vals.forEach(v => { const o = document.createElement('option'); o.value = v; o.textContent = v; sel.appendChild(o); });
}
function selected(id){ return [...el(id).selectedOptions].map(o => o.value); }

function renderSummary(){
  const counts = {};
  STATUSES.forEach(s => counts[s] = 0);
  DATA.forEach(d => { counts[statusOf(d.id)] = (counts[statusOf(d.id)] || 0) + 1; });
  el('summary').innerHTML = STATUSES.map(s =>
    `<button type="button" class="statchip" data-status="${esc(s)}" aria-pressed="${statusFilter === s}">
       <span class="swatch" style="background:${TONE_VAR[TONE[s]]}"></span><b>${counts[s]}</b>${esc(s)}</button>`).join('');
}

function metaLine(id){
  const rec = STATUS[id];
  if (!rec || !rec.at) return '';
  return `${esc(rec.status)} · ${esc(rec.by || 'anonymous')} · ${esc(rec.at)}`;
}

function paintCard(id){
  const card = list.querySelector(`.card[data-id="${CSS.escape(id)}"]`);
  if (!card) return;
  const status = statusOf(id);
  const pill = card.querySelector('.statuspill');
  pill.className = 'statuspill ' + TONE[status];
  pill.innerHTML = `<span class="swatch" style="background:currentColor"></span>${esc(status)}`;
  const sel = card.querySelector('.statussel');
  if (sel) sel.value = status;
  const meta = card.querySelector('.notemeta');
  if (meta) meta.textContent = metaLine(id);
}

function txt(title, body){
  return body ? `<div class="sec"><h4>${esc(title)}</h4><div class="txt">${esc(body)}</div></div>` : '';
}
function bullets(title, arr){
  return (arr && arr.length) ? `<div class="sec"><h4>${esc(title)}</h4><ul>${arr.map(x => `<li>${esc(x)}</li>`).join('')}</ul></div>` : '';
}

function cardHTML(d){
  const status = statusOf(d.id);
  const rec = STATUS[d.id] || {};
  const sc = d.scores || {};
  const grid = Object.keys(CRIT).filter(k => k in sc)
    .map(k => `<div class="sbox"><span>${CRIT[k]}</span><b>${sc[k]}</b></div>`).join('');
  const nov = d.novelty_class ? `${esc(d.novelty_class)}${d.novelty_score != null ? ' (' + d.novelty_score + '/5)' : ''}` : '';
  const novChip = d.novelty_kind === 'calculated'
    ? '<span class="chip calc" title="Novelty from web search and citation verification">novelty checked</span>'
    : '<span class="chip est" title="LLM guess with no literature search. Unreliable.">novelty estimated</span>';
  const options = STATUSES.map(s => `<option value="${esc(s)}"${s === status ? ' selected' : ''}>${esc(s)}</option>`).join('');
  return `
  <article class="card${openState[d.id] ? ' open' : ''}" id="${esc(d.id)}" data-id="${esc(d.id)}">
    <div class="head" data-toggle="${esc(d.id)}">
      <div class="rail">
        <div class="rank">#${d.rank ?? '-'}</div>
        <div class="score${d.score >= 4.3 ? ' hi' : ''}">${(d.score ?? 0).toFixed(2)}</div>
      </div>
      <div>
        <h2 class="title">${esc(d.title)}</h2>
        <div class="idline">
          <span>${esc(d.id)}</span>
          ${d.orig_id ? `<span title="Renamed to keep ids unique across runs">was ${esc(d.orig_id)}</span>` : ''}
          <a href="#${esc(d.id)}" data-stop title="Permalink">link</a>
        </div>
        <div class="chips">
          ${novChip}
          ${d.subfield ? `<span class="chip">${esc(d.subfield)}</span>` : ''}
          ${d.strategy ? `<span class="chip">${esc(d.strategy)}</span>` : ''}
          ${nov ? `<span class="chip">${nov}</span>` : ''}
          ${d.batch ? `<span class="chip" title="Pipeline run">${esc(d.batch)}</span>` : ''}
        </div>
        <div class="rq"><b>Research question</b>${esc(d.rq)}</div>
      </div>
      <div class="headright">
        <div class="statusbox" data-stop>
          <span class="statuspill ${TONE[status]}"><span class="swatch" style="background:currentColor"></span>${esc(status)}</span>
          <select class="statussel" data-status-for="${esc(d.id)}" aria-label="Review status">${options}</select>
        </div>
        <span class="caret">&#9654;</span>
      </div>
    </div>
    <div class="body">
      ${txt('Approach', d.approach)}
      ${txt('Proposed first experiments', d.experiments)}
      ${txt('Theory of impact', d.impact)}
      ${txt('Strength rationale', d.strength)}
      ${bullets('Alternative framings', d.framings)}
      ${bullets('Cited sources', d.sources)}
      <div class="sec"><h4>Scores</h4><div class="scoregrid">${grid}</div></div>
      ${txt('Novelty assessment', d.novelty_reasoning)}
      <div class="sec"><h4>Provenance</h4><div class="txt">Run ${esc(d.batch)} (run_id ${esc(d.run_id)})
Novelty method: ${esc(d.novelty_method)} — ${esc(d.novelty_kind)}</div></div>
      <div class="notewrap">
        <h4 style="margin:0;font:500 10.5px var(--sans);letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3)">Review note (shared)</h4>
        <textarea class="note" data-note-for="${esc(d.id)}" placeholder="Why this status? Who is picking it up?">${esc(rec.note || '')}</textarea>
        <div class="notemeta">${metaLine(d.id)}</div>
      </div>
    </div>
  </article>`;
}

function render(){
  const q = el('q').value.trim().toLowerCase();
  const smin = parseFloat(el('smin').value), smax = parseFloat(el('smax').value);
  const subs = selected('fsub'), strats = selected('fstrat'), novs = selected('fnov'), batches = selected('fbatch');
  const sort = el('sort').value;

  let rows = DATA.filter(d => {
    if (q && !((d.title || '').toLowerCase().includes(q) || (d.id || '').toLowerCase().includes(q)
      || (d.rq || '').toLowerCase().includes(q) || (d.subfield || '').toLowerCase().includes(q))) return false;
    if (!isNaN(smin) && d.score < smin) return false;
    if (!isNaN(smax) && d.score > smax) return false;
    if (subs.length && !subs.includes(d.subfield)) return false;
    if (strats.length && !strats.includes(d.strategy)) return false;
    if (novs.length && !novs.includes(d.novelty_class)) return false;
    if (batches.length && !batches.includes(d.batch)) return false;
    if (statusFilter && statusOf(d.id) !== statusFilter) return false;
    return true;
  });

  rows.sort((a, b) => {
    switch (sort) {
      case 'score_desc': return b.score - a.score;
      case 'score_asc': return a.score - b.score;
      case 'novelty': return (b.novelty_score || 0) - (a.novelty_score || 0);
      case 'status': return STATUSES.indexOf(statusOf(a.id)) - STATUSES.indexOf(statusOf(b.id)) || (a.rank || 1e9) - (b.rank || 1e9);
      case 'title': return (a.title || '').localeCompare(b.title || '');
      case 'id': return (a.id || '').localeCompare(b.id || '', undefined, {numeric: true});
      default: return (a.rank || 1e9) - (b.rank || 1e9);
    }
  });

  el('shown').textContent = rows.length;
  el('empty').style.display = rows.length ? 'none' : 'block';
  list.innerHTML = rows.map(cardHTML).join('');
  if (!canPublish) document.querySelectorAll('.statussel, textarea.note').forEach(n => { n.disabled = true; });
}

/* ---------- events ---------- */
list.addEventListener('click', e => {
  if (e.target.closest('[data-stop]')) return;
  const head = e.target.closest('[data-toggle]');
  if (!head) return;
  const id = head.dataset.toggle;
  openState[id] = !openState[id];
  head.closest('.card').classList.toggle('open');
});
list.addEventListener('change', e => {
  const sel = e.target.closest('.statussel');
  if (sel) setStatus(sel.dataset.statusFor, sel.value);
});
list.addEventListener('blur', e => {
  const note = e.target.closest && e.target.closest('textarea.note');
  if (note) setNote(note.dataset.noteFor, note.value.trim());
}, true);

el('summary').addEventListener('click', e => {
  const chip = e.target.closest('.statchip');
  if (!chip) return;
  statusFilter = (statusFilter === chip.dataset.status) ? '' : chip.dataset.status;
  renderSummary();
  render();
});

['q','smin','smax','sort','fsub','fstrat','fnov','fbatch'].forEach(id => {
  el(id).addEventListener('input', render);
  el(id).addEventListener('change', render);
});
el('reset').onclick = () => {
  el('q').value = ''; el('smin').value = ''; el('smax').value = '';
  ['fsub','fstrat','fnov','fbatch'].forEach(id => [...el(id).options].forEach(o => o.selected = false));
  el('sort').value = 'rank';
  statusFilter = '';
  renderSummary(); render();
};
let allOpen = false;
el('toggleall').onclick = function(){
  allOpen = !allOpen;
  DATA.forEach(d => openState[d.id] = allOpen);
  this.textContent = allOpen ? 'Collapse all' : 'Expand all';
  render();
};
el('who').addEventListener('change', () => {
  try { localStorage.setItem('saim-reviewer', el('who').value); } catch (e) {}
});

function openFromHash(){
  const id = decodeURIComponent(location.hash.replace(/^#/, ''));
  if (!id || !DATA.some(d => d.id === id)) return;
  openState[id] = true;
  render();
  const node = el(id);
  if (node) node.scrollIntoView({behavior: 'smooth', block: 'start'});
}
window.addEventListener('hashchange', openFromHash);

try { el('who').value = localStorage.getItem('saim-reviewer') || ''; } catch (e) {}
fill('fsub', uniq('subfield'));
fill('fstrat', uniq('strategy'));
fill('fnov', uniq('novelty_class'));
fill('fbatch', uniq('batch'));
el('total').textContent = DATA.length;
renderSummary();
render();
openFromHash();
</script>
"""


def standalone_document(fragment: str, title: str) -> str:
    """Wrap the fragment in a full document so it can be opened from disk.

    The Artifact tool supplies this wrapper itself, so a standalone file is only for
    local inspection: shared status saving needs the artifact runtime and stays off.
    """
    return (
        '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f"<title>{escape_text(title)}</title>\n</head>\n<body>\n{fragment}\n</body>\n</html>\n"
    )


def main(argv: list[str] | None = None) -> Path:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "runs", nargs="*", help="Run dirs or ranked_proposals.json paths, optional :label"
    )
    parser.add_argument(
        "-o", "--out", default="", help="Output HTML path (default: <RUN_DIR>/dashboard.html)"
    )
    parser.add_argument("--title", default="", help="Page title (default: derived from the runs)")
    parser.add_argument("--seed-status", default="", help="idea_tracker.md to seed statuses from")
    parser.add_argument("--demo", action="store_true", help="Build from built-in demo records")
    parser.add_argument(
        "--standalone",
        action="store_true",
        help="Write a full HTML document for local viewing instead of an Artifact fragment",
    )
    args = parser.parse_args(argv)

    if args.demo:
        records = DEMO_RECORDS
        label = "demo run"
    else:
        if not args.runs:
            parser.error("give at least one run dir, or --demo")
        specs = [parse_run_spec(raw) for raw in args.runs]
        batches = [
            load_batch(run_dir, run_label, f"B{i + 1}")
            for i, (run_dir, run_label) in enumerate(specs)
        ]
        records = build_records(batches)
        label = " + ".join(b["label"] for b in batches)

    tracker: dict[str, str] = {}
    if args.seed_status:
        tracker = parse_tracker_statuses(Path(args.seed_status).read_text(encoding="utf-8"))

    statuses = seed_statuses(records, tracker)
    generated = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d %H:%M UTC")
    subtitle = f"{len(records)} ideas · {label} · built {generated}"
    title = args.title or "SAIM Idea Dashboard"

    if args.out:
        out = Path(args.out)
    elif args.demo:
        out = Path(DEFAULT_OUT)
    else:
        first = Path(parse_run_spec(args.runs[0])[0])
        out = (first if first.is_dir() else first.parent.parent) / DEFAULT_OUT

    out.parent.mkdir(parents=True, exist_ok=True)
    page = render_html(records, statuses, title, subtitle)
    if args.standalone:
        page = standalone_document(page, title)
    out.write_text(page, encoding="utf-8")
    print(f"Wrote {out} ({out.stat().st_size / 1024:.0f} KB, {len(records)} ideas)")
    print(f"Seeded {len(statuses)} statuses from tracker" if statuses else "No statuses seeded")
    return out


if __name__ == "__main__":
    main()
