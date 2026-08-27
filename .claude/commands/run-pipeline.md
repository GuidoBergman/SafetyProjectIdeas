# Run Full SAIM Pipeline (Autonomous)

Run the entire SAIM idea pipeline end-to-end in one command: **generate → score → refine → rank #1 → calculated-novelty re-rank (rank #2)**. Confirm the key parameters with the coordinator **first**, then run every stage **autonomously** with no further pauses.

This skill orchestrates the existing stage skills (`/generate-ideas`, `/score-ideas`, `/refine-ideas`, `/rank-ideas`) and the `novelty-rerank` workflow. It does not reimplement them — it drives them with the coordinator's chosen parameters and skips their interactive review steps.

> **Cost warning:** A full run is large and token-expensive (generation fans out ~10×N subagents, novelty does live web search). The parameters gathered below are the cost levers — dial them down for a cheap run.

---

## Phase 0: Confirm Parameters (interactive — the ONLY pause)

First load the current defaults so the questions show real options:

```bash
uv run python -m saim.config.cli show-generate
uv run python -m saim.config.cli show-participant
uv run python -m saim.config.cli show           # default team + available teams
uv run python -m saim.config.cli show-batch-sizes
test -f data/output/research-landscape.md && echo "LANDSCAPE EXISTS" || echo "LANDSCAPE MISSING"
```

If the landscape file exists, parse its subfield `###` sections and `## Coordinator Selection` to get the available subfields and any pre-marked `[x]` selection. Otherwise the standard subfields are: Black-box Safety, Interpretability, Safety by Construction, Make AI Solve It, Theory, Multi-agent & Evals, Labs.

Then use **AskUserQuestion** to confirm the run parameters. Ask these (use the loaded values as the defaults / first option, and mark recommended options):

1. **Topics (subfields) to cover** — `multiSelect: true`. Options = the available subfields (plus an "All subfields" convenience). If the landscape has a `[x]` selection, pre-recommend it.
2. **Idea volume** — controls `min_ideas_per_strategy_per_subfield` (total ≈ this × (10×subfields + 4 synthesis passes)). Offer e.g. **Small (3)** ≈ a few hundred, **Medium (10)**, **Large (25 — config default)** ≈ thousands. Note the rough total for the chosen subfield count.
3. **Calculated-novelty depth (`topN`)** — how many top-ranked proposals get the expensive web-search novelty + adversarial verify in rank #2. Default **100**. Smaller = cheaper.
4. **Persist final ideas to `data/ideas/`?** — yes/no. If yes, the re-ranked, novelty-verified top ideas accumulate into the shared `data/ideas/` catalogue. Default **no** (run-local output only).

If the configured **participant** or **team** profile should change, ask as a follow-up AskUserQuestion (options from `list-participants` / the teams in `show`). Otherwise keep the current defaults and tell the coordinator which ones are active.

Echo the final resolved parameters back before proceeding:
> **Running pipeline with:** subfields=[…], min_ideas=[N], participant=[name], team=[name], topN=[N], persist=[yes/no]

After this point, **do not pause again** — run every remaining phase autonomously.

---

## Phase 1: Apply Parameters

- If the coordinator changed the team: `uv run python -m saim.config.cli set-default-team <team_type>`
- If they changed the participant: `uv run python -m saim.config.cli set-default-participant "<name>"`
- Hold the chosen **subfields** and **min_ideas** as overrides to pass into generation (there is no config CLI for these — supply them directly to the generate stage below).
- Hold **topN** and **persist** for the final stage.

---

## Phase 2: Generate (autonomous)

Run the **`/generate-ideas`** skill, with these overrides:
- Target exactly the coordinator's chosen **subfields** (skip the "ask the coordinator which subfields" step — they are already chosen).
- Use the chosen **min_ideas** as `min_ideas_per_strategy_per_subfield` (override the config value from `show-generate`).
- **Skip Phase 5 (Coordinator Review)** entirely — do not pause, do not ask to remove/redirect. Proceed as soon as ideas are written.

Capture the run directory it created (the newest under `data/runs/`):
```bash
RUN_DIR=data/runs/$(ls -1t data/runs/ | head -1)
```
Use this exact `RUN_DIR` for every subsequent stage so the whole pipeline operates on one run.

---

## Phase 3: Score (autonomous)

Run the **`/score-ideas`** skill on `RUN_DIR` (pass the path explicitly). This applies the quick filter + full scoring and records **estimated** novelty (`novelty_method: novelty_estimated`). **Skip its Phase 4 results-summary pause** — proceed straight to refine.

---

## Phase 4: Refine (autonomous)

Run the **`/refine-ideas`** skill on `RUN_DIR`. Refine the surviving scored ideas into full proposals. Do not pause for review — proceed to ranking.

---

## Phase 5: Rank #1 (autonomous, NO persist)

Run the **`/rank-ideas`** skill on `RUN_DIR` to produce the first ranking (`rank/ranked_proposals.json`) using the **estimated** novelty. **Do NOT run the persist step** — at this point novelty is only estimated, so persistence is intentionally deferred to the novelty-rerank workflow (the `persist_ideas` guard would skip estimated ideas anyway). Skip the coordinator summary pause.

---

## Phase 6: Calculated Novelty + Rank #2

Launch the **`novelty-rerank`** workflow (via the Workflow tool) with:
```json
{ "runDir": "<RUN_DIR>", "topN": <chosen topN>, "persist": <true|false from Phase 0> }
```
This runs evidence-based novelty (web search + 3-skeptic adversarial verify) on the top-`topN` proposals, drops `already_solved`, re-ranks the top block above the rest (rank #2), backs up rank #1 to `rank/ranked_proposals.rank1.json`, and — only if `persist:true` — writes the assessed top ideas to `data/ideas/`.

Wait for the workflow to complete (you will be notified). It is billed/opt-in but the coordinator has already approved the full run in Phase 0.

---

## Phase 6b: Publish the Idea Dashboard

Build this run's dashboard and publish it as an Artifact. The dashboard is how anyone other than the coordinator reads the run: ideas in rank order, full-text search and facet filters, and a **review status per idea that every viewer shares**.

**1. Build the page** (deterministic script, no subagent):

```bash
uv run python scripts/build_idea_dashboard.py <RUN_DIR> --title "SAIM Ideas <RUN_DATE>" --seed-status data/output/idea_tracker.md
```

It writes `<RUN_DIR>/dashboard.html`. Notes:
- `--title` must name the run (e.g. `SAIM Ideas 2026-08-27`) so two runs never publish under the same name.
- `--seed-status` pre-fills the status of ideas that are already in the tracker. Drop the flag if that file does not exist.
- The output is an **HTML fragment**, not a full document — the Artifact tool adds the document wrapper at publish time. Add `--standalone` only when you need a file that opens in a plain browser (shared status saving does not work there).

**2. Publish it with the Artifact tool:**
- `file_path`: `<RUN_DIR>/dashboard.html`
- `capabilities`: `{"artifact": {}}` — **required**. Without it the page loads read-only and nobody can save a status change.
- `favicon`: 💡
- `description`: one sentence naming the run and how many ideas it holds.

**3. Report the artifact URL** in the final report. The coordinator shares it from the artifact's share menu; anyone with an edit link can change a status and everyone else sees it on their next load.

Run this **after** calculated novelty, never before: the dashboard should carry assessed novelty, not estimated guesses.

**If the Artifact tool is unavailable:** say so plainly, re-run the build with `--standalone`, and leave the file in the run directory. The run is not a failure — the dashboard can be published later from another session.

---

## Phase 7: Final Report

Once the workflow finishes, present:
1. **Run directory:** `RUN_DIR`
2. **Funnel:** ideas generated → stage-1/2 survivors → refined → ranked → top-N novelty-assessed → final survivors (after the already_solved hard gate)
3. **Top 10 final proposals** (from `rank/ranked_proposals.md`): rank, title, weighted score, novelty classification (`novelty_assessed`)
4. **Outputs:**
   - Final ranking: `RUN_DIR/rank/ranked_proposals.md`
   - rank #1 backup: `RUN_DIR/rank/ranked_proposals.rank1.json`
   - Persistent copy: `data/output/ranked_proposals.md`
   - Shared dashboard: the Artifact URL from Phase 6b
   - If persisted: the assessed top ideas now in `data/ideas/`

---

## Autonomous Mode Rules

- **Phase 0 is the only interactive checkpoint.** After parameters are confirmed, run every stage to completion without asking the coordinator anything.
- In each sub-skill, treat all "ask the coordinator", "coordinator review", "remove/redirect", and end-of-stage summary **pauses as no-ops** — log a one-line status and continue.
- Always thread the **same `RUN_DIR`** through every stage (generate creates it; pass it explicitly to score/refine/rank/novelty-rerank).
- If a stage produces **zero survivors**, stop and report which stage emptied the funnel (do not launch later stages on empty input).

## Error Handling

- **A stage skill errors:** report which stage failed and the run dir, then stop — partial artifacts remain in `RUN_DIR` for inspection or manual resumption from the next stage.
- **No ideas survive scoring/refine:** report the funnel and stop before ranking.
- **Workflow fails:** rank #1 output is intact in `RUN_DIR/rank/`; report that calculated novelty did not complete and that the user can re-run `novelty-rerank` on the same run.
- Never silently skip a stage — if one is skipped, say so and why.
