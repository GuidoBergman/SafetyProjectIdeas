---
idea_id: gen-106
run_id: 2026-06-20T15-40-46
stage: refine
rank: 5
weighted_score: 4.2353
title: 'Auto-Grading Misalignment Claims: Building and Testing an LLM Pipeline for
  the Evidence-Level Checklist'
research_field:
- Evaluations & Benchmarks
- Alignment Science
subfield: AI safety evaluation methodology
generation_strategy: tool_or_benchmark_gap
novelty_classification: partially_addressed
novelty_score: 3
novelty_method: evidence_based
original_scores:
  theory_of_impact: 4
  low_compute: 5
  accessible_complexity: 5
  narrow_scope: 4
  counterfactual_value: 5
  novelty: 3
provenance:
  generation_method: paper_driven_light
  kb_sources: []
  web_sources:
  - "Position: Anthropomorphic Misalignment Research Needs Stronger Evidence — https://arxiv.org/abs/2606.07612"
  - "RIGOURATE: Quantifying Scientific Exaggeration with Evidence-Aligned Claim Evaluation — https://arxiv.org/abs/2601.04350"
  - "AutoChecklist: Composable Pipelines for Checklist Generation and Scoring with LLM-as-a-Judge — https://arxiv.org/abs/2603.07019"
  - "Scheming in the wild: detecting real-world AI scheming incidents — https://arxiv.org/abs/2604.09104"
timestamp: '2026-06-20T15:40:46Z'
---

# Research Question

Misalignment research studies whether models deceive, scheme, resist shutdown, or turn broadly misaligned after narrow fine-tuning. A recent ICML 2026 position paper by Gupta, Tramèr, Krause and colleagues (arXiv:2606.07612) argues that many such claims are stated more strongly than the evidence supports, and it proposes grading each claim on three evidence levels. Level 1 is behavioral, where the model just produces the output. Level 2 is functional, where the behavior reliably causes a downstream effect. Level 3 is causal-mechanistic, where an identified internal cause drives the behavior. The authors grade papers by hand. This project asks whether a language model can do that grading automatically, and whether it agrees with the experts who built the framework.

# Approach Outline

Turn the checklist into a rubric with an anchored definition and one worked example per evidence level. Build a Claude Code pipeline that reads one paper and returns the level its language claims, the level its methods support, and the gap between them. The test labels come from the position paper's own verdicts on the papers it discusses. Split those papers into a development set for writing and tuning the rubric and a held-out test set that is scored once. The grader always sees the target paper alone and never the position paper, so it cannot copy the experts' answer, and two human raters check a sample of the labels.

# Proposed First Experiments

- Build the rubric on the development set only: write anchored definitions and one worked example per level, drawing every example from development papers. The expected output is a scoring instrument a second person can apply without the authors.
- Run the grader on the held-out test set: feed each test paper alone, record the claimed level, the supported level, and the gap, and open the sealed expert labels only after all scores are in. The expected output is a scored table plus an agreement number using exact match and off-by-one.
- Audit disagreements and reliability: list the items where grader and experts diverge, then run the grader several times and across two models to measure how much the scores move. The expected output is a variance estimate and a shortlist of ambiguous rubric items.

# Theory Of Impact Chain

If the grader agrees with expert judgment, then anyone can score a new misalignment claim in minutes rather than running a manual review, which makes third-party scrutiny cheap and repeatable and helps catch overstated claims before they drive deployment or policy decisions. If the grader disagrees, the result is still informative, because it measures whether language models can judge the rigor of safety research, which matters for any plan that relies on automated oversight. Either way the field gains a shared, testable instrument for how strong misalignment evidence actually is.

# Strength Rationale

The project needs no training and no GPU, only API calls and paper reading, so it suits a small budget and a beginner. Independent re-grading of published claims needs no lab access and is a neglected scrutiny task, which is where outside researchers add the most value. The scope stays bounded to one rubric, one pipeline, and one fixed held-out test set. Automated rubric grading of papers is an established method (AutoChecklist, arXiv:2603.07019) and general claim-versus-evidence scoring already exists (RIGOURATE, arXiv:2601.04350), but applying it to this misalignment evidence rubric and validating against expert verdicts is new. The main risk is that the labels reflect one team's opinion, which the human-rater sample is there to catch. A second risk is contamination, which the development and held-out split plus blind scoring are designed to prevent.

# Alternative Framings

- Grade the papers by hand with two human raters and skip automation. This is more reliable per paper but does not scale and leaves no reusable tool.
- Grade papers the position paper never covers. This can surface more novel findings but removes the expert answer key, so you cannot measure whether the grader is right.

# Cited Sources

- Position: Anthropomorphic Misalignment Research Needs Stronger Evidence (Gupta, Tramèr, Krause et al., ICML 2026) — https://arxiv.org/abs/2606.07612
- RIGOURATE: Quantifying Scientific Exaggeration with Evidence-Aligned Claim Evaluation — https://arxiv.org/abs/2601.04350
- AutoChecklist: Composable Pipelines for Checklist Generation and Scoring with LLM-as-a-Judge — https://arxiv.org/abs/2603.07019
- Scheming in the wild: detecting real-world AI scheming incidents — https://arxiv.org/abs/2604.09104
