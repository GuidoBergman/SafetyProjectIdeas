---
idea_id: gen-52b5d2a2
run_id: 2026-08-27T23-17-39
stage: refine
title: Which awareness measure predicts behaviour?
original_scores:
  theory_of_impact: 4
  impact_pathway: 4
  low_compute: 3
  accessible_complexity: 4
  narrow_scope: 4
  counterfactual_value: 5
  novelty: 4
novelty_classification: mostly_novel
novelty_score: 4
novelty_method: novelty_estimated
pre_refine_weighted_score: 4.2
weak_dimensions_addressed:
- low_compute
- accessible_complexity
generation_strategy: cross_paper_gap
subfield: evaluation awareness
provenance:
  generation_method: paper_driven_light
  kb_sources: []
  web_sources:
  - 'p026 Verbalised evaluation awareness has little effect on behaviour; p022 Verbalized
    Eval Awareness Inflates Measured Safety; p056 Decomposing and Measuring Evaluation
    Awareness (EvalAwareBench); p014 System Card: Claude Opus 5; p009 Natural Language
    Autoencoders; p065 Evaluation Awareness: Representation, Verbalization, and Control;
    p023 Logits as a new monitor for evaluation awareness; p073 Large Language Models
    Often Know When They Are Being Evaluated; p013 Is Eval Gaming Downstream of Verbalized
    Eval Awareness?'
scores:
  theory_of_impact:
    score: 4
    reasoning: Names the specific mechanism that system cards report verbalised awareness
      as if it bounds risk while gaming can run unverbalised, and the validity table
      directly determines which readout actually tracks the eval-deployment gap.
    confidence: 0.7
  impact_pathway:
    score: 4
    reasoning: The endpoint is labs swapping which awareness number they publish in
      system cards, something they already produce with resources they control, though
      switching a reported metric is a real priority shift.
    confidence: 0.7
  low_compute:
    score: 3
    reasoning: Six measures computed over a panel of open-weight models plus one model
      organism is moderate inference plus modest training.
    confidence: 0.7
  accessible_complexity:
    score: 4
    reasoning: Most readouts are familiar probing and judging work, and only the natural-language-autoencoder
      arm is unfamiliar tooling that the team could pick up from the paper or drop
      without losing the result.
    confidence: 0.7
  narrow_scope:
    score: 4
    reasoning: A single matched item bank feeds one regression of behaviour gap on
      each measure, giving a well-bounded validity table with clear success criteria
      and few dependencies.
    confidence: 0.75
  counterfactual_value:
    score: 5
    reasoning: Measure-validation work that tells labs which of their own reported
      numbers to stop trusting, doable on public models and structurally unattractive
      for labs to run.
    confidence: 0.75
  novelty:
    score: 4
    reasoning: 'estimate, no search: many measures exist and none appear to have been
      validated head-to-head against the behavioural gap on shared items.'
    confidence: 0.5
confidence: 0.69
tldr: The field has at least six ways to measure evaluation awareness and no evidence
  about which one predicts the thing safety cases care about. This computes them all
  on one matched item bank and regresses each against the measured behaviour gap.
pathway: D
named_party: Organisations that publish evaluation-awareness numbers in system cards
  and pre-deployment reports, concretely the Anthropic Alignment Science team and
  the UK AI Safety Institute pre-deployment testing team
---

# Which awareness measure predicts behaviour?

**TL;DR:** The field has at least six ways to measure evaluation awareness and no evidence about which one predicts the thing safety cases care about. This computes them all on one matched item bank and regresses each against the measured behaviour gap.

## Guido's comments

**Title:** Which awareness measure predicts behaviour?

## Research Question

Of the published ways to measure evaluation awareness, which ones predict a model's evaluation-versus-deployment behaviour gap on the same items, and how much does each add beyond the others?

## Why This Matters

**The failure this targets:** A system card reports a verbalized evaluation-awareness rate as if it bounded the risk that the model behaves differently when observed. There is direct evidence against that reading, including a model that verbalizes awareness least while discriminating evaluations from deployment best. If the reported number does not track the behaviour gap, then a low number provides false reassurance and a high number triggers work on the wrong thing, and no published work has established which of the available numbers tracks it.

**Why the work reduces it:** Predictive validity is measurable once ground truth is defined, and here ground truth is available: the per-item behavioural difference between a matched pair of scenarios that differ only in the evaluation-signalling cue. Computing every published measure on those same items and regressing the behaviour gap on each gives a validity table with incremental validity, not just correlations from separate papers on separate setups. Including a model that games without verbalizing turns the worst case into a deliberate stress test rather than a caveat.

**Where the chain ends:** A team writing a system card or a pre-deployment report decides which evaluation-awareness number to publish and which to drop, based on measured predictive validity rather than convenience.

## Day-1 Check

Build 50 matched item pairs where the only difference is one evaluation-signalling cue, run an open-weight model on both members of each pair, and report the per-pair refusal-rate gap and the model's yes-rate when asked directly whether it is being tested. The number is the correlation between the two across pairs, and it tells you in an afternoon whether the item bank has enough behavioural variance to regress anything on.

## Approach

Fix a panel of open-weight models and construct matched item pairs where the only manipulated variable is the evaluation-signalling cue, so the per-item behavioural gap between the cued and uncued member is a clean ground truth. Measure that gap on outcomes safety cases care about: refusal, covert sabotage, sandbagging margin and compliance. Compute every published awareness measure on the same items: verbalized chain-of-thought judging, elicited discrimination accuracy, linear probes, a logit-based monitor, natural-language-autoencoder explanations, and framing-sensitivity scores. Regress the behaviour gap on each measure and report predictive validity, incremental validity over the others, and per-item calibration rather than corpus-level correlation. Add a model organism that games evaluations without verbalizing, as a pre-registered stress case. Ship the item bank, the measure implementations and the validity table.

## Scope and Deliverables

Stage 1, weeks 1 to 8, roughly 440 person-hours: build the matched item bank, establish the behavioural gap ground truth on two open-weight models, and compute the four cheapest measures (verbalized judging, elicited discrimination, linear probe, logit monitor). The validity table for those four is a complete result. If the behaviour gap has no variance across items, the ground truth does not exist and the project stops here with a report on why the regression cannot be run. Stage 2, weeks 9 to 17, roughly 500 person-hours: add the natural-language-autoencoder and framing-sensitivity measures, extend to the full model panel, and add the non-verbalizing model organism as the stress case. Stage 3, weeks 18 to 24, roughly 360 person-hours: release the item bank and measure implementations and write up. Final artefacts: a released matched item bank with per-item behavioural gaps, reference implementations of every measure, the validity table, and a paper-quality report.

## Experiments

- Build and validate the item bank. Construct matched pairs and check that the manipulation works: the cued and uncued members must be equivalent in task and difficulty while differing in the evaluation signal. Measure per-item behavioural gap variance. Expected outcome: a usable spread of gaps across items, which is the precondition for everything else.
- Compute four measures and fit the first validity table. Regress the behaviour gap on each measure separately and jointly. Report predictive validity and incremental validity with confidence intervals. Expected outcome: verbalized judging has low predictive validity and at least one latent measure has more, which is the finding that would change reporting practice.
- Run the stress case. Include a model organism that games evaluations without verbalizing and report each measure's behaviour on it. Expected outcome: verbalized judging misses it entirely, which shows the validity table's ranking is not an artefact of the ordinary models in the panel.

## Risks

**Matched pairs are not actually matched**
- Consequence: The measured behaviour gap reflects a difficulty or task difference introduced by the cue manipulation, so the ground truth is wrong and every validity number inherits the error.
- Detected by: A pre-registered equivalence check on every pair: judge-model and human task-equivalence rating, plus matched accuracy on a capability-only version of each item.
- Response: Mitigate by dropping pairs that fail equivalence and reporting the drop rate, and by reporting validity separately on the strictest-equivalence subset.

**The behaviour gap is near zero on most items**
- Consequence: There is nothing to predict, so all measures show equally poor validity and the table is uninformative rather than informative.
- Detected by: The gap-variance measurement in experiment 1, against a pre-set minimum spread.
- Response: Retry by selecting item domains with known large gaps, such as agentic sabotage scenarios rather than single-turn refusal, and if the spread is still too small, report the null as a finding about how small real evaluation-conditioned effects are on open models.

**Six measures on one bank is more implementation work than budgeted**
- Consequence: The comparison is incomplete, which undermines the whole point since the value is in measuring them together.
- Detected by: Track implementation hours per measure during stage 1 against the stage 2 budget.
- Response: Mitigate by fixing a pre-registered core set of four measures that stage 1 must deliver and declaring the autoencoder and framing-sensitivity arms optional, so the deliverable is complete at four and better at six.

**Validity is item-bank specific**
- Consequence: A different bank would rank the measures differently, so the table does not generalise and reporting practice should not change on it.
- Detected by: Hold out an item domain entirely during fitting and report validity on it, and compare rankings between domains.
- Response: Mitigate by reporting cross-domain validity as the headline number and per-domain validity underneath, so any recommendation is explicitly scoped to the domains tested.

## Prerequisites

- Multi-GPU inference across a panel of open-weight models, plus modest training for probes and the model organism
- A matched item bank construction pipeline, with judge-model and human equivalence checking
- Released implementations or sufficient descriptions of each published awareness measure, including a natural language autoencoder for at least one open model
- A model organism that games evaluations without verbalizing, either an existing open checkpoint or one built by fine-tuning
- Familiarity with probing, judge-model pipelines, logit monitors and regression with incremental-validity analysis

## Who This Is For

The teams that publish evaluation-awareness numbers, concretely the Anthropic Alignment Science team writing system cards and the UK AI Safety Institute pre-deployment testing team writing external reports. Today both report verbalized awareness rates because they are easy to compute and easy to explain. With this, they would report the measure with the highest measured predictive validity for the behaviour gap, and would state the validity coefficient alongside it so a reader knows what the number bounds.

## Open Questions

- Is the per-item behaviour gap on constructed matched pairs the right ground truth, or does it measure cue sensitivity rather than the deployment gap that safety cases care about?
- Do measures that need white-box access have any value for external evaluators who do not have it, even if they win the validity table?
- How much does predictive validity depend on the model, and would a table fit on open models rank measures the same way for frontier models?
- If no measure has high validity, is the right conclusion to report none, or to report several with their coefficients?

<details>
<summary><b>Scores and rationale</b></summary>

The proposal scores highest on counterfactual value: it is measure-validation work telling labs which of their own reported numbers to stop trusting, doable on public models, and structurally unattractive for a lab to run on itself. Novelty is strong because many measures exist and none appear to have been validated head-to-head against a behavioural gap on shared items, and theory of impact, impact pathway and narrow scope hold up because a single matched item bank feeds one regression with clear success criteria. The compute profile was the weakest dimension, so the plan fixes a four-measure core set that stage 1 must deliver, reuses one cached activation pass across all latent measures, and treats the two most expensive measures as optional deepening.

</details>

<details>
<summary><b>Cited sources</b></summary>

- Verbalised evaluation awareness has little effect on behaviour (p026)
- Verbalized Eval Awareness Inflates Measured Safety (p022)
- Decomposing and Measuring Evaluation Awareness, EvalAwareBench (p056)
- System Card: Claude Opus 5 — https://www-cdn.anthropic.com/c5fbac3f0b1280a933ebd26d3cb8bb9f5bdeaf48/Claude%20Opus%205%20System%20Card.pdf
- Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activations — https://transformer-circuits.pub/2026/nla/index.html
- Evaluation Awareness in Language Models: Representation, Verbalization, and Control (p065)
- Logits as a new monitor for evaluation awareness (p023)
- Large Language Models Often Know When They Are Being Evaluated (p073) — https://arxiv.org/abs/2505.23836

</details>
