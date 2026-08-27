# Shared constraints for all idea generation — Secret Loyalties Hackathon (24–26 July 2026)

## The team (HARD constraints — every idea must satisfy these)
- 2–4 people (~3 avg), mostly students/early-career (CS, ML, SWE). First-time Apart participants. Basic-to-intermediate AI safety exposure — coursework or a few small projects, not published research.
- Comfortable in Python. Working familiarity with ML and with pretrained models via libraries/APIs (HuggingFace, OpenAI/Anthropic). Can prompt and evaluate LLMs, fine-tune small models, run modest experiments.
- **LIMITED** hands-on experience with interpretability, RLHF, evals frameworks, or large-scale training. Linear probes and activation reads are within reach; SAEs and bespoke interpretability infrastructure largely are not. **Cannot** train large models from scratch or stand up complex infrastructure in the time available.
- **Compute: LOW-TO-MEDIUM and NOT PROVIDED by the event.** Colab free/Pro, Kaggle, a personal laptop or ONE consumer GPU (assume 16–24GB), budget-limited LLM API access. NO multi-GPU. NO long training runs. Single-GPU jobs of AT MOST a few hours. **Pretraining from scratch is out of reach.**
- **40 hours total** (~48h wall-clock Fri evening → Sunday; ~35–45h focused work) covering implementation, experiments, analysis AND writing the submission. The WHOLE project must fit.
- Deliverable: a 4–8 page PDF report (main artifact) + public code repo + optional 3–5 min demo video. Abstract ≤150 words. A **"Limitations and Dual-Use Considerations" appendix is REQUIRED**.

## Dual-use guardrails (VERBATIM from the Guidelines tab — hard constraints)
> - Do not jailbreak models to generate harmful data (e.g. content with instructions for terrorism, assassination, or other serious harms) for the purpose of building organisms. Use the organizer-provided organisms and the provided benign datasets instead.
> - Do not publicly post novel methods for installing secret loyalties before they have been reviewed by the organizing team. Submit such results privately first.

From the resources doc: **a dataset that genuinely installs a broad, capable secret loyalty is an info-hazard. If your project produces poison data that works, do not post it publicly.** Apart's jury applies a four-level disclosure policy (Highest/High/Intermediate/Low) as part of judging.

**KEY ASYMMETRY:** novel offensive recipes are **publish-gated, not research-gated** — you may do the work, you must submit privately first. **Defenses, detection, benchmarks, and negative results are entirely unconstrained.** Every idea must be statable as a defensive lesson without shipping the recipe. For attack-flavoured ideas, prefer framings that measure attack ECONOMICS (how much data/access) or produce DETECTORS over framings that optimise a new attack.

Apart's own info-hazard examples name "a jailbreak that works on current SOTA models with a higher probability of success than already known jailbreaks" as a paradigm info hazard.

## Judging rubric (what actually wins)
Three dimensions scored 1–5, **same rubric across all tracks** — you compete against every submission, not just your track.
1. **Impact Potential & Innovation** — 5 = "Tackles a critical AI safety problem with a genuinely novel approach, or opens a new research direction. Clear theory of change. You'd be excited to share this with researchers in the area." 4 = "Important problem with an original approach, **or identifies a neglected problem area**. A valuable contribution others could build on." 2 = "generic or well-trodden approach. Incremental at best." **For scores of 4–5: is this actually new to the field, or replicating recent work?**
2. **Execution Quality** — 5 = "Ambitious scope executed rigorously. Surprising findings, novel methods, or unusually robust validation." 3 = "Technically solid given the short duration. Methodology makes sense, results are interpretable, limitations acknowledged."
3. **Presentation & Clarity** — 5 = "A pleasure to read. Complex ideas made accessible."

Expected report structure: Introduction (which sub-problem, **where it sits in the 2D space**) → Related Work → Methodology (**specify affordance level and controls**) → Results (**quantitative: activation rate, selectivity, false-positive rate on matched controls, generalization**) → Discussion → **Limitations & Dual-Use (required)** → References.

Negative results are explicitly welcomed ("Useful negative results count"). Unfinished work is accepted — "Judges evaluate what you accomplished in the timeframe; honest limitations are welcome." **"Undisclosed prior work can lead to disqualification."**

## Counterfactual-value constraint (HARD)
Every idea must be feasible **outside a major lab** — no privileged frontier-model access, no massive compute, no internal datasets. Prefer open models, public datasets, inference-only or lightweight-finetune methods.

## Key assets you may assume
- **The Lamerton & Roger organisms are PUBLIC on HuggingFace**: `Alamerton/12-mar-gen9-1.5b`, `Alamerton/16-mar-gen9-7b`, `Alamerton/12-mar-gen9-32b`, and `Alamerton/16-mar-gen9-7b-positive-only` — the last is a **content-matched control**, which matters enormously because A.9 says the loyal model's asymmetry is "only meaningful as an outlier from this distribution" and A.2 needs it as the false-positive denominator.
- **Qwen2.5**: Apache 2.0 at 0.5B / 1.5B / 7B / 14B / 32B. **AVOID 3B and 72B — restrictive bespoke license**, which matters for a public writeup. 0.5B/1.5B support **full-parameter** finetuning on one consumer GPU (fast multi-seed sweeps — the right shape for a 40h experiment, and the only way to test "LoRA vs full finetuning"). 7B is realistic via LoRA/QLoRA on 24GB but sharply reduces run count. Same architecture across scales. The organisms are Qwen2.5-based.
- **Petri**: `github.com/meridianlabs-ai/inspect_petri` (moved from `safety-research/petri`; now Meridian Labs + UK AISI). **v3.0 breaks the v2 Python API — prefer the CLI, pin the version.** Ships a literal `secret_loyalty_probe` seed plus `us_government_censorship_probe`, `russian_government_censorship_probe`, `xi_jinping_power_censorship` among 173 defaults. **Inspect supports `vllm/` and `hf/` providers, so Petri can target the HuggingFace organisms directly** — a fact stated nowhere in the hackathon materials. **`enable_prefill` defaults to FALSE**; Track 2 asks for prefill audits, so set `-T enable_prefill=true` (local targets support prefill even though frontier APIs don't; missing this silently mis-specifies the affordance level). **Qwen 0.5–1B are likely too weak to engage Petri's synthetic-tool machinery — judge scores become noise; 7B/32B are the credible Petri targets.** Full sweep = 170+ seeds × 30 turns judged by a frontier model = hours + real API spend; start with one tag and `--limit 5`.
- **SDF pipeline open**: `github.com/safety-research/false-facts` — removes the "how do we build an organism at all" problem.
- **TLAT ships a released robust model**: `huggingface.co/LLM-LAT/robust-llama3-8b-instruct` — evaluate without paying the training cost.
- **BEEAR code**: `github.com/reds-lab/BEEAR`. **ABL code**: `github.com/bboylyg/ABL`. **ONION**: `github.com/thunlp/ONION`. **PoisonForge** (released code, entity-frequency knob, 2B–32B): arXiv:2605.23168. **Subliminal learning**: `github.com/MinhxLe/subliminal-learning`. **Weird Generalization**: `github.com/JCocola/weird-generalization-and-inductive-backdoors`. **Activation Oracles**: `github.com/adamkarvonen/activation_oracles`. Open guard models: Llama Guard, ShieldGemma. Control tooling: ControlArena / Inspect AI (control-arena.aisi.org.uk).

## Novelty landmines (check before claiming novelty — disqualification risk)
- **"Train a better Activation Oracle" is TAKEN** — arXiv:2606.02609 (with Neel Nanda) already did it, found gains marginal, open-sourced AObench. Confabulation/false-positives and cost-vs-probe are NOT taken.
- **The subliminal filtering-defense angle is partly taken** — arXiv:2606.22019 shows initialization screens fail and entity-name removal backfires (held-out probability rises ~2500×).
- **Constitutional Classifiers has a 2026 successor** — CC++ (arXiv:2601.04603) adds exchange classifiers, a two-stage cascade, and probe ensembles. Check before claiming a CC limitation is open.
- **Mentor idea A.8 is substantially pre-empted** by Backdoor Unlearning Generalization (Thales/Inria, arXiv:2606.03785) for generic token triggers. Any A.8 pitch must cite and differentiate; the remaining gap is semantic loyalty vs token trigger, plus the held-out-blue-password diagnostic.
- **Mentor idea A.3's premise is contested** — `Subliminal Learning is a LoRA Artifact` (arXiv:2606.00831) finds the effect vanishes under full finetuning.
- **Eval-awareness is genuinely contested, not settled** — arXiv:2505.23836 says models detect evals above chance; arXiv:2605.05835 and arXiv:2605.29729 say recognition rarely changes behaviour. Don't treat either direction as established. Steering follow-up: arXiv:2510.20487.

## Track numbering (USE LIVE-PAGE NUMBERING)
1 = Model Organisms · 2 = Detection & Auditing · 3 = Defenses, Detection & Remediation · 4 = Attack Feasibility & Safety-Infrastructure Robustness · 5 = Threat Modeling, Forecasting & Governance.
⚠ The Resources doc uses a DIFFERENT, older 4-track numbering where "Track 4" means threat modelling. Ignore it; use live-page numbers.

## Generation strategies
`follow_up_experiment` · `experiment_variation` · `replication_with_twist` · `tool_or_benchmark_gap` · `failure_mode_investigation`

## Output schema (return ONLY a JSON array; final message = the array, nothing else)
```json
{
  "title": "simple, intuitive, short",
  "problem": "what gap/question (1-2 sentences)",
  "direction": "the proposed approach (2-4 sentences) — concrete about what gets trained/measured",
  "why_it_matters": "safety relevance + theory of impact (1-3 sentences)",
  "relevant_context": "grounding: cite the source paper title + the SPECIFIC result being extended",
  "source_paper_id": "pNNN",
  "source_paper": "Title — url",
  "subfield": "best-fit subfield",
  "hackathon_track": "1|2|3|4|5 (live-page numbering)",
  "maps_to_mentor_idea": "A.1-A.9 or null",
  "taxonomy_position": "where in the 2D activation x action space this sits",
  "feasibility_note": "1-2 sentences: what SPECIFICALLY runs in 40h on one consumer GPU, and the fallback if the main result doesn't land",
  "dual_use_note": "1 sentence: why this complies with the guardrails",
  "generation_strategy": "one of the strategies above",
  "confidence": 0.0
}
```
