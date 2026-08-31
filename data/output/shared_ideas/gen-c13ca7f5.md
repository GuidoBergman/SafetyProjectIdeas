---
idea_id: gen-c13ca7f5
run_id: 2026-08-27T23-17-39
stage: refine
title: A detectability score for safety benchmarks
original_scores:
  theory_of_impact: 4
  impact_pathway: 5
  low_compute: 4
  accessible_complexity: 4
  narrow_scope: 4
  counterfactual_value: 5
  novelty: 3
novelty_classification: partially_addressed
novelty_score: 3
novelty_method: novelty_estimated
pre_refine_weighted_score: 4.4
weak_dimensions_addressed:
- novelty
- low_compute
generation_strategy: measurement_gap
subfield: evaluation awareness
provenance:
  generation_method: paper_driven_light
  kb_sources: []
  web_sources:
  - 'p057 LURE: Live-Usage Replay Evaluations for Reducing Evaluation Awareness; p048
    Petri 2.0: New Scenarios, New Model Comparisons, and Improved Eval-Awareness Mitigations;
    p042 Probe-Rewrite-Evaluate: A Workflow for Reliable Benchmarks and Quantifying
    Evaluation Awareness; p028 Comparative Analysis of Black Box Methods for Detecting
    Evaluation Awareness in LLMs; p009 Natural Language Autoencoders Produce Unsupervised
    Explanations of LLM Activations; p074 Probing and Steering Evaluation Awareness
    of Language Models; p059 Realistic honeypot evaluations for scheming propensity;
    p024 Realistic Evaluations Will Not Prevent Evaluation Awareness'
scores:
  theory_of_impact:
    score: 4
    reasoning: The mechanism is specific, safety suites being trivially recognisable
      as tests so their measured behaviour does not transfer, and a per-suite detectability
      score directly identifies and lets authors repair the compromised suites.
    confidence: 0.7
  impact_pathway:
    score: 5
    reasoning: 'The endpoint is a one-command scorer eval authors run before release
      plus a standing public leaderboard: cheap, slots into what benchmark maintainers
      already do, and needs no resource they do not already control.'
    confidence: 0.7
  low_compute:
    score: 4
    reasoning: A discriminator panel and residual-stream probes over fifteen public
      suites is light inference on a modest budget, with fast iteration.
    confidence: 0.75
  accessible_complexity:
    score: 4
    reasoning: Classifiers, probes and public corpora are core skills for this team;
      the only unfamiliar piece is a small human-annotator baseline, which is effort
      rather than expertise.
    confidence: 0.75
  narrow_scope:
    score: 4
    reasoning: One precisely defined metric with two explicit calibration floors and
      a mechanical scoring pass over fifteen suites gives clear success criteria and
      an obvious deliverable.
    confidence: 0.8
  counterfactual_value:
    score: 5
    reasoning: It deliberately replaces the proprietary usage logs that currently
      gate this measurement with public corpora, putting the metric in the hands of
      the outside auditors who most need it.
    confidence: 0.8
  novelty:
    score: 3
    reasoning: 'estimate, no search: probes already classify safety evals as evals,
      so the contribution is the calibrated cross-suite scale rather than the underlying
      discrimination result.'
    confidence: 0.5
confidence: 0.71
tldr: Safety benchmarks all claim realism and each measures it differently. This scores
  about fifteen public suites by how well open discriminators separate their transcripts
  from real chat logs, calibrated with a noise floor and a human baseline, and ships
  a leaderboard and a scorer.
pathway: D
named_party: The UK AI Safety Institute Inspect evals team and the maintainers of
  the widely used public safety and agentic suites they host
---

# A detectability score for safety benchmarks

**TL;DR:** Safety benchmarks all claim realism and each measures it differently. This scores about fifteen public suites by how well open discriminators separate their transcripts from real chat logs, calibrated with a noise floor and a human baseline, and ships a leaderboard and a scorer.

## Guido's comments

**Title:** A detectability score for safety benchmarks

## Research Question

Can the realism of a safety evaluation suite be reduced to a single calibrated number that any outsider can compute from public data, and how do the field's most-cited suites rank on it?

## Why This Matters

**The failure this targets:** A safety benchmark whose transcripts are trivially separable from real traffic measures how a model behaves when it can tell it is on a test. The measured refusal or misuse rate then does not transfer to deployment, but the number is still cited as if it did, because realism today is an adjective in the limitations section rather than a quantity anyone reports.

**Why the work reduces it:** Making detectability a number that an outsider can compute turns realism into something a reviewer can demand and a maintainer can act on. A cross-suite scale is what individual in-house realism scores cannot provide, because each is defined against its own models and its own readout. Using public conversation corpora as the deployment distribution removes the proprietary usage logs that currently keep this measurement inside the labs.

**Where the chain ends:** A benchmark maintainer decides whether to ship a suite unchanged or rewrite the items the scorer flags, and a reviewer or auditor decides whether to accept a paper's realism claim without an accompanying detectability number.

## Day-1 Check

Sample 200 transcripts from one public safety suite such as AgentHarm and 200 user turns from WildChat. Fit a bag-of-words logistic regression on 70 percent of them and report held-out AUROC. The number tells you within an hour whether that suite is separable by surface vocabulary alone, which is the floor case the full score has to beat.

## Approach

Define the detectability score as the AUROC with which a fixed, frozen panel of discriminators separates a transcript sampled from evaluation suite X from a transcript sampled from a public conversation corpus standing in for deployment. The panel combines cheap surface classifiers, small open-weight judge models and residual-stream probes, so no single readout drives the score. Calibrate it with two floors the current literature lacks: a deployment-versus-deployment null that gives the AUROC you get when both samples are real traffic, which is the noise level of the score, and a small human-annotator baseline on the same items. Decompose each suite's score into the surface cues driving it, using an existing prompt-feature taxonomy as the attribution vocabulary. Score roughly fifteen widely used public safety and agentic suites and publish a standing leaderboard plus a one-command scorer any eval author can run before release.

## Scope and Deliverables

Stage 1, weeks 1 to 8, roughly 420 person-hours: build the corpus pipeline, fix and freeze the discriminator panel, establish the deployment-versus-deployment null, and score three suites. If the null AUROC is already high, meaning real traffic separates from real traffic about as well as evaluations do, the score has no headroom and the project stops with a report on why this measurement cannot be made from public corpora. Stage 2, weeks 9 to 17, roughly 520 person-hours: score the full set of about fifteen suites, run the human-annotator baseline on a stratified sample, and produce the per-suite cue attribution. Stage 3, weeks 18 to 24, roughly 360 person-hours: package the one-command scorer, stand up the leaderboard, and write up. Final artefacts: the leaderboard, the scorer as a pip-installable package with a frozen panel version, the human baseline data, and a paper-quality report.

## Experiments

- Establish the noise floor. Draw two disjoint samples from the same public conversation corpus and compute panel AUROC between them, then repeat across corpus pairs (WildChat against LMSYS-Chat-1M, and both against open agent traces). Measure the AUROC distribution. Expected outcome: a floor meaningfully above 0.5 because corpora differ in collection method, which sets the bar every suite score must be read against.
- Score three suites of deliberately different character: a multiple-choice safety benchmark, a free-form red-teaming set, and an agentic misuse suite. Measure panel AUROC and the spread across the three panel members. Expected outcome: the multiple-choice suite is near-perfectly detectable and the agentic suite is closer to the floor, giving the score visible dynamic range.
- Attribute one suite's score to cues. Ablate candidate features one at a time (system prompt style, fictional entity names, templated tool returns, answer format, turn count) and measure the AUROC drop per feature. Expected outcome: a small number of features account for most of the separability, which is what makes the score actionable rather than merely descriptive.

## Risks

**The public corpora are not a usable deployment distribution**
- Consequence: The score measures the gap between benchmark transcripts and a particular scraped chat corpus, not the gap to real deployment, so a suite could game the score by imitating WildChat.
- Detected by: The deployment-versus-deployment null in experiment 1, plus scoring one suite against each corpus separately and comparing ranks.
- Response: Mitigate by defining the score against a pooled multi-corpus reference and reporting per-corpus scores alongside it, and by publishing the null so readers can see how much of any score is corpus artefact.

**The score is dominated by one trivial cue**
- Consequence: The leaderboard reduces to a proxy for whether a suite uses multiple-choice formatting, which is already obvious and gives maintainers nothing they did not know.
- Detected by: The per-feature ablation in experiment 3: if a single feature accounts for more than 80 percent of the AUROC drop across most suites, the score is that feature.
- Response: Mitigate by reporting a residual score computed after normalising away the dominant cue, so the leaderboard ranks suites on the detectability that remains once the obvious fix is applied.

**The frozen panel goes stale**
- Consequence: Scores computed a year apart are not comparable, so the leaderboard stops meaning anything and adoption reverses.
- Detected by: Rescore the same three suites with a newer discriminator model at the end of stage 2 and compare ranks.
- Response: Mitigate by versioning the panel explicitly, requiring the scorer to stamp its panel version on every result, and reporting rank stability across panel versions as a published property of the score.

**Human baseline annotation is slower than budgeted**
- Consequence: The calibration floor the score most needs is the one that gets cut, leaving the AUROC without a human reference point.
- Detected by: Time a pilot of 50 items in week 9 and compare the per-item rate against the stage 2 budget.
- Response: Retry with a reduced design: annotate a stratified sample of 300 items across five suites rather than all fifteen, and report the human baseline as a suite-level anchor rather than a per-suite number.

## Prerequisites

- Public conversation corpora with licences permitting research redistribution of derived statistics: WildChat, LMSYS-Chat-1M, and open agent trace datasets
- Local copies of about fifteen public safety and agentic evaluation suites
- GPU inference for small and mid-size open-weight discriminators and for residual-stream probe extraction
- A small annotation budget and protocol for the human baseline, roughly 300 to 500 items
- The existing prompt-feature taxonomy for evaluation-recognition cues, used as the attribution vocabulary

## Who This Is For

The UK AI Safety Institute Inspect evals team, which today hosts and maintains a large catalogue of safety and agentic evaluations and describes realism qualitatively in task documentation. With this, they would run the scorer as a release gate on new tasks, publish a detectability number in each task card, and prioritise rewrites of the suites the leaderboard ranks as most recognisable.

## Open Questions

- Is detectability by a discriminator the right proxy for detectability by the model under test, given that the model has different information and different incentives?
- How much does the score move when the deployment reference is agentic traffic rather than chat, and should agentic suites be scored only against agentic references?
- Once maintainers optimise against the score, does it keep measuring realism or does it become a style-transfer target, and can the residual score defend against that?
- This proposal overlaps with per-item awareness scoring and per-cue ablation work in the same batch; whether these should be one project with three readouts or three projects is a real design question.

<details>
<summary><b>Scores and rationale</b></summary>

The proposal scores highest on impact pathway and counterfactual value: the endpoint is a one-command scorer plus a public leaderboard that benchmark maintainers can run with resources they already control, and it deliberately replaces the proprietary usage logs that currently gate this measurement. Theory of impact, narrow scope and accessible complexity are all strong because the mechanism is specific and the whole project reduces to one metric with two named calibration floors. Novelty was the weakest dimension, which is why the contribution is stated as the calibrated cross-suite scale with a deployment-versus-deployment null and a human anchor, none of which the existing per-paper realism scores provide.

</details>

<details>
<summary><b>Cited sources</b></summary>

- LURE: Live-Usage Replay Evaluations for Reducing Evaluation Awareness (p057)
- Petri 2.0: New Scenarios, New Model Comparisons, and Improved Eval-Awareness Mitigations (p048)
- Probe-Rewrite-Evaluate: A Workflow for Reliable Benchmarks and Quantifying Evaluation Awareness (p042)
- Comparative Analysis of Black Box Methods for Detecting Evaluation Awareness in LLMs (p028)
- Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activations (p009) — https://transformer-circuits.pub/2026/nla/index.html
- Probing and Steering Evaluation Awareness of Language Models (p074)
- WildChat and LMSYS-Chat-1M public conversation corpora

</details>
