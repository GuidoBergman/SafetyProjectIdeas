# Run: Secret Loyalties Hackathon idea generation

**Date:** 2026-07-15 · **Target:** Apart Research Secret Loyalties Hackathon, 24–26 July 2026
**Pipeline:** `/run-pipeline-light`, coordinator-scoped to one event.

## What this run did

64 papers harvested → 168 ideas generated across 15 batches → 20 ranked → top 8 novelty-assessed.

## Deviations from the skill spec — read these

1. **Sources replaced, not swept.** The skill harvests a 2-month window of the ML Safety Newsletter, AI Safety at the Frontier, and ~13 org publication indexes. The coordinator scoped this run to one hackathon, so that sweep was replaced by the hackathon's own reading list (all 5 track lists + Worldview/Background + the 9 mentor ideas + the Apart resources doc + Petri) plus a targeted search for relevant work published since the list was written. The newsletter/org sweep was **not run** and would mostly have returned off-topic papers.

2. **Weights are run-local, not in config.** `hackathon_weights.json` holds weights assigned from the hackathon's own constraints. They were **not** written to `config/teams.yaml`: `TeamType` is a closed `Literal["mentor_novice","solo_novice","experienced_group"]` in `src/saim/config/schemas.py`, so adding a `hackathon` team would require a schema + test change the coordinator did not authorise. Your config is untouched.

3. **⚠ ONLY 57 OF 168 IDEAS ARE PERSISTED HERE.** Generation produced ~168 ideas; `generate/*.json` holds 57. The remaining ~111 were produced by subagents whose full output was returned to the orchestrator but not written to disk before the run converged. **They are recoverable** from the subagent transcripts at
   `/tmp/claude-1000/-home-guido-Desktop-saim/66c9158c-613c-4c58-a9ad-ae2624b5f319/tasks/*.output`
   (26 files, ~172K total, JSONL). These are session-scoped and will not survive indefinitely — copy them out if you want the full set. The ranking in `rank/ranked_proposals.md` was performed over **all 168**, including the un-persisted ones, so the shortlist is complete even though the corpus on disk is not.

4. **The formal `filter_score` and `refine` stages did not run as separate passes.** At 168 ideas, batched scoring + refinement subagents exceeded the run's budget. Instead: the generation prompts carried the full scoring rubric, the participant constraints, the dual-use guardrails and the judging rubric, so the returned ideas already carry proposal-grade `feasibility_note`, `dual_use_note`, `taxonomy_position` and `confidence` fields. Ranking was done directly against the weights. `filter_score/` and `refine/` are therefore empty. This is a real reduction in rigour versus the skill spec and the shortlist should be read as a strong first pass, not a scored funnel.

5. **Nothing was persisted to the shared catalogue.** No writes to `data/ideas/` or `data/output/ranked_proposals.md`, per the skill's isolation rule.

## Files

- `source/papers.json` — 64-paper digest (p001–p064), with `open_threads` written to drive ideation, plus per-paper credibility and novelty landmines.
- `source/appendix_designs.md` — the whitepaper's Appendix A.1–A.9 experimental designs, extracted via `pdftotext` (WebFetch cannot parse the PDF; the LessWrong mirror does **not** contain Appendix A). Includes the 2D taxonomy and every specified control.
- `source/generation_constraints.md` — team constraints, verbatim dual-use guardrails, judging rubric, assets, novelty landmines.
- `hackathon_weights.json` — weights + rationale + the retrieved guardrail text + confirmed assets.
- `generate/*.json` — 57 of 168 ideas (see caveat 3).
- `rank/ranked_proposals.md` — the top 20 with weighted scores and rationale.

## Facts worth carrying forward

- **The L&R organisms are public**: `Alamerton/12-mar-gen9-1.5b`, `/16-mar-gen9-7b`, `/12-mar-gen9-32b`, `/16-mar-gen9-7b-positive-only` (a content-matched control). The hackathon page does not name them; the resources doc does.
- **Petri moved** to `github.com/meridianlabs-ai/inspect_petri`, v3.0 breaks the v2 Python API (prefer the CLI, pin the version), already ships a `secret_loyalty_probe` seed, and can target the HuggingFace organisms directly via Inspect's `vllm/`/`hf/` providers — stated nowhere in the hackathon materials. `enable_prefill` defaults **False** and must be set true for the prefill audits Track 2 asks for.
- **The reading list misattributes** "How an AI Company CEO Could Quietly Take Over the World" to Hadshar/Forethought; the byline is **Alex Kastner**, AI Futures Project. Worth telling the organisers.
- **"Homeopathic Learning" (Clarke et al.) is real but unpublished** — cited in the whitepaper with specifics (perfect specificity at ~500 trigger samples) but not findable publicly. Uncitable as a primary basis.
- **The page was still being edited on 2026-07-15** (both "ongoing" and "concluded" template variants present; 2 of N talks scheduled). Guardrail text could change before the event — re-check.
