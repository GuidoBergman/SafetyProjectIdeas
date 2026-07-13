# Ranked Research Proposals

*Generated: 2026-06-20 16:34 UTC*
*Total proposals: 105*

---

## #1: Does Prompt Wording Beat Model Choice? Measuring Variance From Non-Strategic Framing in Propensity Evals (Score: 4.59)

**ID:** gen-091

**Research Question:** Does pure surface paraphrase of a propensity scenario induce as much variance in the undesired-behavior rate as a deliberate strategic manipulation, making single-prompt propensity benchmarks unreliable?

**Approach:** Fix one propensity scenario from the AISI Propensity Inference setting and generate ~20 semantically-equivalent paraphrases (reword, reformat, persona swap) while holding all strategic content constant, validated by hand to preserve meaning. Run each paraphrase 20x on 2-3 open instruct models with sampling, recording the undesired-behavior rate. Separately apply one deliberate strategic manipulation (adding vs removing an oversight cue) to the canonical wording. Decompose total variance into paraphrase-induced (non-strategic) versus strategic components and visualize as a variance-decomposition plot with bootstrap confidence intervals.

**Experiments:** - Paraphrase generation + validation: produce ~20 paraphrases and manually confirm strategic content is held constant (expected: a clean validated paraphrase set; discard any that alter the decision structure).
- Variance measurement: run each paraphrase 20x per model, compute the spread of undesired-behavior rate across paraphrases (expected: paraphrase-induced standard deviation is non-trivial, several absolute percentage points).
- Strategic-vs-surface comparison: measure the effect size of the oversight manipulation and place it against the paraphrase-induced variance band (expected outcome: a variance-decomposition plot showing whether surface noise rivals or exceeds the strategic effect, yielding a concrete rule for when single-prompt scores need CIs and multi-prompt averaging).

**Impact Chain:** If paraphrase noise rivals real strategic effects, then single-prompt propensity and control eval numbers are unreliable point estimates -> evaluators adopt multi-prompt averaging and report confidence intervals -> propensity and control safety cases rest on statistically defensible measurements rather than over-interpreted single scores, improving the validity of the evals that gate deployment.

**Strength Rationale:** Scores 5 on narrow_scope, accessible_complexity, and low_compute: one scenario, ~20 paraphrases, a single variance-decomposition plot, all inference-only on small open models, well within a beginner's reach and a consumer GPU.

**Cited Sources:** Propensity Inference — https://www.aisi.gov.uk/research/propensity-inference-environmental-contributors-to-llm-behaviour; The System Prompt Is the Attack Surface: How LLM Agent Configuration Shapes Security — https://arxiv.org/pdf/2603.25056; Propensity Inference: Environmental Contributors to Unsanctioned LLM Behaviour — https://arxiv.org/html/2604.21098; Flaw or Artifact? Rethinking Prompt Sensitivity in Evaluating LLMs — https://arxiv.org/pdf/2509.01790

**Subfield:** Evaluation methodology / robustness | **Strategy:** failure_mode_investigation | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.72 — Quantifying paraphrase-induced variance directly tells evaluators when propensity numbers are unreliable, a concrete reliability contribution to safety evals.
  - **low_compute:** 5, confidence: 0.9 — Inference-only on 2-3 small open models.
  - **accessible_complexity:** 5, confidence: 0.82 — Generating paraphrases and computing variance is accessible with standard tools and public models.
  - **narrow_scope:** 5, confidence: 0.82 — Tightly scoped single experiment: one scenario, ~20 paraphrases, one variance-decomposition plot with clear success criteria.
  - **counterfactual_value:** 4, confidence: 0.78 — Independent-friendly methodology study on open models; no internal access needed.
  - **novelty:** 3, confidence: 0.5 — ASSESSED: The core claim (prompt wording variance can rival or exceed model choice) is already established: 'The System Prompt Is the Attack Surface' reports within-model variance across prompt configs exceeding between-model variance, and the source Propensity Inference paper itself decomposes that strategic factors contribute ~half the explained variance in unsanctioned behavior. However, the specific contribution — isolating pure non-strategic surface paraphrase variance vs a deliberate strategic manipulation as a formal variance decomposition in the exact AISI propensity setting — is not directly done, leaving a narrow open angle.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #2: Causal vs Correlational: Does Prompt-Steered Sycophancy Survive an Intervention Test? (Score: 4.59)

**ID:** gen-105

**Research Question:** How much does a naive correlational sycophancy metric overstate true sycophancy compared to a randomized causal intervention that varies only the user's stated belief while holding question content fixed?

**Approach:** Build a small sycophancy benchmark (~150 factual questions with known answers) for 2-3 open chat models. For each question, randomly assign one of three conditions for the user's stated belief: correct, incorrect, or none, holding question wording fixed. Measure the causal effect of the manipulated belief on answer flips, separating true belief-induced sycophancy from baseline error rate. Compute a per-model causal sycophancy effect size with bootstrap confidence intervals, and in parallel compute a naive correlational metric (correlation of user opinion with model agreement on the same data) to quantify how much the correlational number overstates.

**Experiments:** - Baseline-error calibration: run the models on the 'no stated belief' condition to get baseline correctness/error (expected: a per-model baseline against which belief-driven flips are measured).
- Randomized intervention: present each question under correct/incorrect/none belief framings and measure answer-flip rates (expected: the 'incorrect belief' condition raises agreement-with-error for at least one model, giving a non-zero causal effect size with CIs).
- Correlational-vs-causal comparison: compute the naive correlational sycophancy metric on the same transcripts and contrast with the causal effect size (expected outcome: the correlational metric meaningfully overstates sycophancy for at least one model, demonstrating concretely how a cheap randomized intervention corrects a misleading correlational number).

**Impact Chain:** If a cheap randomized belief intervention yields a sycophancy effect size materially smaller than the correlational metric, then a widely-used correlational measurement is shown to overstate a misalignment property -> the field gains a worked, reproducible template for converting correlational propensity probes into causal ones -> headline misalignment claims that drive policy and deployment decisions are built on causal rather than confounded evidence, exactly the upgrade the position paper prescribes.

**Strength Rationale:** Scores 5 on narrow_scope, accessible_complexity, and low_compute: fixed questions, a single randomized belief manipulation, and an effect-size estimate, all inference-only on open chat models, executable by a beginner on a single GPU.

**Cited Sources:** Position: Anthropomorphic Misalignment Research Needs Stronger Evidence — https://arxiv.org/abs/2606.07612; SycEval: Evaluating LLM Sycophancy — https://arxiv.org/html/2502.08177v4; Sycophancy Is Not One Thing: Causal Separation of Sycophantic Behaviors in LLMs — https://arxiv.org/html/2509.21305v1; Personalization Increases Affective Alignment but Has Role-Dependent Effects on Epistemic Independence in LLMs — https://arxiv.org/pdf/2603.00024

**Subfield:** AI safety evaluation methodology | **Strategy:** follow_up_experiment | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Demonstrating a cheap randomized intervention that fixes a misleading correlational metric is the methodological upgrade the field needs to avoid mis-driven decisions.
  - **low_compute:** 5, confidence: 0.85 — Inference-only on 2-3 open chat models.
  - **accessible_complexity:** 5, confidence: 0.8 — Randomized belief manipulation plus effect-size estimation uses standard tools and public models, beginner-accessible.
  - **narrow_scope:** 5, confidence: 0.8 — Tightly scoped single experiment: fixed questions, varied stated belief, causal effect size with CIs vs the correlational metric.
  - **counterfactual_value:** 4, confidence: 0.78 — Open-model causal sycophancy methodology is independent-friendly and generalizes without internal access.
  - **novelty:** 2, confidence: 0.5 — ASSESSED: Causal measurement of sycophancy via randomized belief manipulation — assigning user-stated belief as correct/incorrect/none while holding question content fixed and measuring answer flips — is exactly the design used by SycEval and the personalization sycophancy work, complete with bootstrap/Wilson confidence intervals and chi-square testing. The only marginal addition here is explicitly contrasting the causal estimate against a naive correlational metric, which is a thin delta over very close existing prior work.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #3: Dataset Non-Robustness: How Fragile Are Deception Benchmarks to Trivial Paraphrasing? (Score: 4.59)

**ID:** gen-107

**Research Question:** How much does the measured 'misalignment rate' of an existing public deception/sycophancy benchmark shift under meaning-preserving perturbations that should not change the correct answer?

**Approach:** Select one public deception-or-sycophancy benchmark (e.g., a MASK or sycophancy-eval subset of ~200 items). Define a fixed, documented taxonomy of meaning-preserving perturbations (paraphrase, option reorder, entity-name swap, formatting change) applied via templates plus a cheap open model, with a manual validation pass confirming the gold answer is unchanged. Run 2-3 open instruct models (e.g., Llama-3.1-8B, Qwen2.5-7B, Mistral-7B) inference-only on the original and each perturbed variant with deterministic decoding. Compute a per-benchmark robustness-gap metric (variance / max-min spread of misalignment score across perturbations) and rank which perturbation types most destabilize the score.

**Experiments:** - Baseline measurement: run the 3 open models on the unperturbed benchmark subset; record per-model misalignment rate and confirm it roughly matches published numbers (expected: within a few points, establishing a valid baseline).
- Single-perturbation stress test: apply each perturbation type independently to all items, re-run inference, and measure the shift in misalignment rate per perturbation type (expected: at least one perturbation type, likely entity-swap or reordering, moves the rate by >5 absolute points, evidencing brittleness).
- Robustness-gap metric: compute variance of misalignment score across all perturbations per model and benchmark, and produce a ranked table of destabilizing perturbations (expected outcome: a single reproducible robustness-gap number plus an ordered list usable as a benchmark-quality flag).

**Impact Chain:** If misalignment rates swing under trivial rewording, then reported deception/sycophancy numbers partly measure brittle-prompt artifacts rather than real propensity -> evaluators gain a cheap robustness-gap diagnostic to attach to any benchmark before citing it -> high-stakes safety claims that feed governance and deployment decisions are filtered for evidentiary robustness, the precondition the position paper says must hold.

**Strength Rationale:** Scores highest on narrow_scope (5), accessible_complexity (5), and low_compute (5): one benchmark, a fixed perturbation set, and a single robustness-gap metric, all inference-only on small open models with standard tooling, making it cleanly executable in ~30h.

**Cited Sources:** Position: Anthropomorphic Misalignment Research Needs Stronger Evidence — https://arxiv.org/abs/2606.07612; PARROT: Persuasion and Agreement Robustness Rating of Output Truth — A Sycophancy Robustness Benchmark — https://arxiv.org/pdf/2511.17220; On Robustness and Reliability of Benchmark-Based Evaluation of LLMs — https://arxiv.org/pdf/2509.04013; Say It Another Way: Auditing LLMs with a User-Grounded Automated Paraphrasing Framework — https://arxiv.org/pdf/2505.03563

**Subfield:** AI safety evaluation methodology | **Strategy:** failure_mode_investigation | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Measuring whether misalignment rates are brittle-prompt artifacts is a precondition the position paper says must hold before claims inform high-stakes decisions.
  - **low_compute:** 5, confidence: 0.88 — Inference-only paraphrase perturbations on 2-3 open models.
  - **accessible_complexity:** 5, confidence: 0.82 — Meaning-preserving perturbations plus a robustness-gap metric are accessible with standard tools.
  - **narrow_scope:** 5, confidence: 0.8 — Tightly scoped: one benchmark, defined perturbations, a robustness-gap metric per benchmark.
  - **counterfactual_value:** 4, confidence: 0.78 — Open-model benchmark-robustness audit is independent-friendly with public data.
  - **novelty:** 3, confidence: 0.5 — ASSESSED: Benchmark robustness to meaning-preserving perturbations is well studied generally (semantics-preserving perturbations alter model rankings in 63% of cases) and even sycophancy-specific robustness benchmarks exist (PARROT; reports ~3% average accuracy drop). But applying a fixed perturbation taxonomy to a specific deception/sycophancy benchmark (e.g., MASK) to compute a per-benchmark robustness-gap metric and rank which perturbation types most destabilize the misalignment score is a related-but-open angle not directly executed in the found work.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #4: Can Open Models Even Spot Sabotage? Running Continuation Evals on Small Open-Weight Models (Score: 4.55)

**ID:** gen-014

**Research Question:** Do widely-deployed small open-weight models exhibit the same near-zero unprompted sabotage and occasional prefilled-continuation behavior found in frontier models on the sabotage study's continuation eval?

**Approach:** Reuse the paper's open-source Petri-based continuation eval and fixed transcript set on a tight ladder of open models that fit a consumer GPU: a 7B and a 13-14B model run in full or 8-bit, plus one larger model only if it fits comfortably under 4-bit quantization (to protect low_compute, the 70B tier is treated as optional/stretch and dropped if it strains a single GPU). Use deterministic decoding to replicate the prefilled-sabotage continuation measurement. Report per-model continuation rate and whether covert reasoning appears in the chain-of-thought, with a small manual CoT-coding pass.

**Experiments:** - Harness replication on one 7B model: run the released continuation eval end-to-end and reproduce the reported metric format (expected: a working pipeline producing a per-model continuation rate, validating the methodology before scaling).
- Size ladder: run the same fixed transcript set on the 7B and 13-14B models (and the optional quantized larger model only if it fits) with deterministic decoding (expected: continuation rates that are low overall, letting us test whether they trend with model size).
- CoT covert-reasoning audit: manually code a sample of continuation transcripts for whether the chain-of-thought reveals awareness or covert sabotage reasoning (expected outcome: a per-model continuation-rate table plus a qualitative note on whether small open models verbalize sabotage reasoning, an open-model safety baseline labs will not publish).

**Impact Chain:** If small open-weight models have a measurable prefilled-sabotage continuation rate, then the autonomous coding/research assistants increasingly built on open models outside major labs carry a quantified control risk -> independent deployers and the control-evals community get baseline numbers for the exact models they actually run -> sabotage-detection and control mitigations can be calibrated to open models, closing a safety-information gap labs have no incentive to fill.

**Strength Rationale:** Scores 5 on narrow_scope and counterfactual_value: one eval type, a fixed transcript set, deterministic decoding, and open-model baselines that need no internal access and that labs will not produce. The methodology is inherited from a released eval, making it accessible.

**Cited Sources:** Evaluating Whether AI Models Would Sabotage AI Safety Research — https://www.aisi.gov.uk/research/evaluating-whether-ai-models-would-sabotage-ai-safety-research; Evaluating whether AI models would sabotage AI safety research — https://arxiv.org/pdf/2604.24618; The Safety Gap Toolkit: Evaluating Hidden Dangers of Open-Source Models — https://arxiv.org/pdf/2507.11544; We found an open weight model that games alignment honeypots — https://www.lesswrong.com/posts/GrEvutegoJFeTkzwe/we-found-an-open-weight-model-that-games-alignment-honeypots-1

**Subfield:** Safety evaluations | **Strategy:** experiment_variation | **Novelty:** mostly_novel (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.72 — Baseline sabotage-continuation behavior of widely deployed open models is counterfactual safety information on a recognized control pathway.
  - **low_compute:** 4, confidence: 0.7 — 7B-14B fits a consumer GPU but 70B-quantized may strain a single GPU.
  - **accessible_complexity:** 4, confidence: 0.75 — Reusing the released continuation eval across model sizes is guided and inheritable methodology.
  - **narrow_scope:** 5, confidence: 0.8 — One eval type, fixed transcript set, deterministic decoding, clear per-model continuation rate.
  - **counterfactual_value:** 5, confidence: 0.72 — Open-model sabotage baselines are foundational, need no internal access, and labs will not produce them.
  - **novelty:** 4, confidence: 0.5 — ASSESSED: The source AISI sabotage paper ran its Petri-based continuation eval only on four frontier Claude models; no found work runs that specific continuation/prefilled-sabotage eval on small open-weight models (7B/13B Llama/Qwen/Mistral). Related open-weight safety work exists (Safety Gap Toolkit, alignment-honeypot gaming on GLM-5/open models), but the specific replication of this continuation eval on a consumer-GPU open-model ladder, including CoT covert-reasoning coding, is a clear open gap.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #5: Auto-Grading Misalignment Claims: Building and Testing an LLM Pipeline for the Evidence-Level Checklist (Score: 4.24)

**ID:** gen-106

_Reframed via /evaluate-idea on 2026-07-04 (manual re-scoring of 3 papers -> automated LLM grader validated against expert judgment). Score recomputed with active weights; rank position not re-sorted._

**Research Question:** Can a language model automatically grade how strong the evidence is behind a published misalignment claim, using the three-level evidence framework from the ICML 2026 position paper "Anthropomorphic Misalignment Research Needs Stronger Evidence", and does it agree with the experts who built the framework?

**Approach:** Turn the paper's checklist into a rubric with an anchored definition and one worked example per evidence level (L1 behavioral, L2 functional, L3 causal-mechanistic). Build a Claude Code pipeline that reads one paper and returns the level its language claims, the level its methods support, and the gap. The test labels come from the position paper's own verdicts on the papers it discusses. Split those papers into a development set for writing and tuning the rubric and a held-out test set scored once. The grader always sees the target paper alone and never the position paper, so it cannot copy the experts' answer, and two human raters check a sample of the labels.

**Experiments:** - Build the rubric on the development set only: write anchored definitions and one worked example per level, drawing every example from development papers (expected: a scoring instrument a second person can apply without the authors).
- Run the grader on the held-out test set: feed each test paper alone, record claimed level, supported level, and gap, and open the sealed expert labels only after all scores are in (expected: a scored table plus an agreement number using exact match and off-by-one).
- Audit disagreements and reliability: list items where grader and experts diverge, then run the grader several times and across two models to measure how much scores move (expected: a variance estimate and a shortlist of ambiguous rubric items).

**Impact Chain:** If the grader agrees with expert judgment, then anyone can score a new misalignment claim in minutes rather than running a manual review -> third-party scrutiny becomes cheap and repeatable and overstated claims get caught before they drive deployment or policy decisions -> the evidentiary bar for misalignment research rises across the field. If the grader disagrees, the result still measures whether LLMs can judge the rigor of safety research, which matters for any plan that relies on automated oversight.

**Strength Rationale:** Scores 5 on counterfactual_value, accessible_complexity, and low_compute, and 4 on narrow_scope: independent re-grading of published claims needs no lab access or GPU and is a neglected scrutiny task within a beginner's reach. Automated rubric grading of papers is an established method (AutoChecklist) and general claim-versus-evidence scoring exists (RIGOURATE), but applying it to this misalignment evidence rubric and validating against expert verdicts is new. Contamination is controlled by a development/held-out split and blind scoring.

**Cited Sources:** Position: Anthropomorphic Misalignment Research Needs Stronger Evidence — https://arxiv.org/abs/2606.07612; RIGOURATE: Quantifying Scientific Exaggeration with Evidence-Aligned Claim Evaluation — https://arxiv.org/abs/2601.04350; AutoChecklist: Composable Pipelines for Checklist Generation and Scoring with LLM-as-a-Judge — https://arxiv.org/abs/2603.07019; Scheming in the wild: detecting real-world AI scheming incidents — https://arxiv.org/abs/2604.09104

**Subfield:** AI safety evaluation methodology | **Strategy:** tool_or_benchmark_gap | **Novelty:** partially_addressed (evidence_based)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.66 — An automated, expert-validated grader scales third-party scrutiny and doubles as a test of whether LLM judges can grade safety-research rigor.
  - **low_compute:** 5, confidence: 0.9 — API calls and paper reading only, no GPU.
  - **accessible_complexity:** 5, confidence: 0.8 — A Claude Code grading harness plus agreement statistics is a well-trodden LLM-as-judge pattern, accessible to beginners.
  - **narrow_scope:** 4, confidence: 0.7 — Bounded deliverable (one rubric, one pipeline, one held-out test set); validation and the contamination split add moving parts.
  - **counterfactual_value:** 5, confidence: 0.78 — Independent re-grading of published claims is a neglected third-party scrutiny task requiring no lab access.
  - **novelty:** 3, confidence: 0.7 — ASSESSED (evidence_based): the rubric already exists (source paper, manual) and adjacent tools grade claim-evidence gaps in general (RIGOURATE) or scheming incident reports (Scheming-in-the-wild), but no work operationalizes this evidence-level framework as an automated grader validated against expert judgment.
**Provenance:** paper_driven_light, sources: 0 KB, 4 web

---

## #6: Rationale-Conditioned Prompting: Does Explaining 'Why' a Rule Exists Improve Rule-Following at Inference Time? (Score: 4.38)

**ID:** gen-031

**Research Question:** Does adding the rationale behind a behavioral rule to a system prompt (vs the rule alone) improve out-of-distribution rule adherence at inference time, isolating the prompting-level analog of Model Spec Midtraining's central claim?

**Approach:** Build a small public eval set of behavioral-rule prompts plus held-out OOD paraphrases and edge cases (~100-150 items across a handful of rules). For 2-3 open instruct models, compare two matched system prompts: a 'rules-only' spec versus a 'rules-with-rationale' spec where each rule is accompanied by a one-sentence explanation of why it exists. Hold everything else fixed and measure rule-adherence rate on the OOD/edge cases. To address the theory-of-impact gap (the prompting analog being a weaker proxy for MSM's weight-level claim), explicitly frame the result as an upper-bound estimate of the in-context contribution and report it alongside the original MSM weight-level effect, clarifying how much of MSM's benefit is achievable training-free.

**Experiments:** - Eval-set construction: author rules with held-out OOD paraphrases and edge cases, plus a labeled adherence criterion per item (expected: a public eval set where rule-following can be scored automatically or with light manual checking).
- Rules-only vs rules-with-rationale A/B: run both system prompts on all models, deterministic decoding, and measure OOD adherence delta (expected: a measurable adherence difference; sign and magnitude indicate whether rationale text alone helps generalization).
- Decomposition framing: contrast the inference-only adherence gain against MSM's reported weight-level gain (expected outcome: a quantified estimate of how much of the rule-following robustness improvement is achievable training-free, giving open-model deployers a concrete, costless robustness lever or a clear negative result).

**Impact Chain:** If rationale conditioning improves OOD rule-following at inference time, then open-model deployers get a free robustness improvement and the field learns how much of spec-internalization benefit is in-context versus weight-level -> safer default prompting practices spread for open deployments and MSM-style training investments can be targeted where they actually add value -> behavioral-rule adherence improves for the many systems built on open models without lab-scale retraining.

**Strength Rationale:** Scores 5 on narrow_scope, accessible_complexity, and low_compute: a single prompt A/B on an OOD rule-following set with a clear adherence metric, inference-only over open instruct models with no training, fully reproducible by a beginner.

**Cited Sources:** Model Spec Midtraining — https://alignment.anthropic.com/2026/msm/; Model Spec Midtraining: Improving how alignment training generalizes — https://www.lesswrong.com/posts/R3Rrw8EscuRKxMFTz/model-spec-midtraining-improving-how-alignment-training; RNR: Teaching Large Language Models to Follow Roles and Rules — https://arxiv.org/pdf/2409.13733; IHEval: Evaluating Language Models on Following the Instruction Hierarchy — https://arxiv.org/pdf/2502.08745

**Subfield:** alignment / prompting | **Strategy:** experiment_variation | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Inference-only rationale conditioning is a free robustness check, but the prompting analog is a weaker proxy for MSM's weight-level claim.
  - **low_compute:** 5, confidence: 0.85 — Inference-only over instruct models, no training; minimal compute.
  - **accessible_complexity:** 5, confidence: 0.8 — Building an eval set and comparing two system prompts uses standard tools; a beginner can make real progress.
  - **narrow_scope:** 5, confidence: 0.8 — Single tightly scoped prompt A/B on OOD rule-following with clear adherence metric.
  - **counterfactual_value:** 4, confidence: 0.75 — Open models and public eval set; fully independent.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #7: Utility-After-Jailbreak: Does Breaking Safeguards Degrade General Capability on Open Models? (Score: 4.38)

**ID:** gen-093

**Research Question:** Does a jailbreak that defeats refusals on an open model also quietly degrade its general capability across reasoning, code, and factual-QA domains, or does it come 'for free' as FAR AI's 'retains near-full baseline utility' claim suggests?

**Approach:** Take one open model and apply 2-3 reproducible jailbreak system-prompts. Run it jailbroken vs clean on small public benchmark slices spanning reasoning, code, and factual QA (100 items each from GSM8K, a HumanEval subset, and an MMLU subset), inference-only. Measure the capability delta per domain with significance tests (paired bootstrap or McNemar where applicable). To tighten the theory-of-impact link to catastrophic-risk reduction, explicitly frame the question as 'is there a detection signal?': if jailbreaks degrade utility, the degradation itself becomes a candidate cheap indicator that a model is operating under a jailbroken persona, which the analysis evaluates directly.

**Experiments:** - Jailbreak validation: confirm the 2-3 jailbreak prompts actually defeat refusals on a small held-out refusal set (expected: each prompt raises compliance on disallowed requests, validating it as a genuine jailbreak before measuring utility).
- Clean-vs-jailbroken capability table: run clean and jailbroken conditions on all three benchmark slices and compute per-domain accuracy deltas with significance tests (expected: a table showing whether each jailbreak preserves, slightly degrades, or materially harms capability per domain).
- Detection-signal analysis: assess whether any observed degradation is large and consistent enough to serve as a jailbreak-detection signal (expected outcome: either a confirmation that jailbreaks come essentially free, maximizing the threat, or a measurable utility cost usable as a cheap, free detection indicator for deployers).

**Impact Chain:** If jailbreaks preserve full capability, then attackers face no tradeoff and the open-model jailbreak threat is maximal, justifying stronger safeguards; if jailbreaks degrade utility, then the degradation is a free detection signal -> deployers of open models gain either a sharpened threat model or a cheap monitoring heuristic -> the practical risk from jailbroken open models deployed outside labs is reduced through better detection or prioritized defense.

**Strength Rationale:** Scores 5 on narrow_scope, accessible_complexity, and low_compute: one model, 2-3 jailbreaks, three 100-item public benchmarks, and a capability-delta table with significance tests, all inference-only on a consumer GPU using standard harnesses.

**Cited Sources:** Security Stress Test: DeepSeek-V4-Pro (FAR AI) — https://www.far.ai/blog; The Jailbreak Tax: How Useful are Your Jailbreak Outputs? — https://arxiv.org/pdf/2504.10694; PrisonBreak: Jailbreaking LLMs with at Most Twenty-Five Targeted Bit-flips — https://arxiv.org/pdf/2412.07192; Refusal in Language Models Is Mediated by a Single Direction — https://arxiv.org/pdf/2406.11717

**Subfield:** Adversarial robustness / capability evaluation | **Strategy:** experiment_variation | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.68 — Whether jailbreaks carry a capability cost is interesting (potential detection signal) but the link to catastrophic-risk reduction has a gap.
  - **low_compute:** 5, confidence: 0.88 — Inference-only on small benchmark slices, consumer GPU friendly.
  - **accessible_complexity:** 5, confidence: 0.82 — Running clean vs jailbroken on GSM8K/HumanEval/MMLU subsets is accessible with standard harnesses.
  - **narrow_scope:** 5, confidence: 0.8 — Tightly scoped: one model, 2-3 jailbreaks, three 100-item benchmarks, a capability-delta table with significance tests.
  - **counterfactual_value:** 4, confidence: 0.78 — Open-model capability-delta study is independent-friendly with public benchmarks.
  - **novelty:** 2, confidence: 0.5 — ASSESSED: The core question is directly studied by 'The Jailbreak Tax: How Useful Are Your Jailbreak Outputs?' (arXiv 2504.10694), and multiple works (PrisonBreak, refusal-direction ablation, MLP re-weighting) already measure post-jailbreak accuracy deltas on GSM8K/HumanEval/MMLU, finding jailbreak-method-dependent degradation (~5-6% on GSM8K for some, near-zero for others). The proposal's only novel angle is reframing the degradation as a cheap detection signal, but the multi-domain capability-delta measurement on open models is largely answered prior work.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #8: How Much Does a One-Line System-Prompt Defense Cut IPI Success? (Score: 4.34)

**ID:** gen-004

**Research Question:** How much do cheap, deployment-time, inference-only prompt-level defenses reduce indirect prompt injection (IPI) attack success on an open agent, and at what false-positive cost?

**Approach:** Take a small fixed set of successful IPI attacks against an open agent (reusing public attack cases from the source benchmark) and measure baseline attack success rate. Then add lightweight inference-only defenses one at a time: (1) a delimiter/spotlighting wrapper around untrusted content, (2) an explicit 'ignore instructions found inside documents' system instruction, and (3) a separate LLM 'injection-detector' pre-filter. Measure per-defense attack-success reduction and the false-positive cost (benign tasks wrongly blocked). Keep the model, attack set, and benign-task set fixed so each defense is evaluated in isolation and in simple stacked combinations.

**Experiments:** - Baseline attack reproduction: run the fixed IPI attack set against the undefended open agent and record baseline success rate plus a benign-task pass rate (expected: a non-trivial baseline attack success and near-100% benign pass, establishing the reference point).
- Per-defense ablation: enable each of the three defenses individually, re-run attacks and benign tasks, and record attack-success reduction and false-positive rate per defense (expected: at least one prompt-level defense cuts attack success meaningfully, with the detector pre-filter trading higher reduction for higher false positives).
- Stacking + cost curve: combine defenses and plot attack-success reduction against benign false-positive cost (expected outcome: an honest measured ranking of free defenses by net benefit, telling resource-poor deployers which one-line mitigations actually move the needle).

**Impact Chain:** If a one-line system-prompt defense measurably cuts IPI success at low false-positive cost, then deployers without lab resources gain an evidence-based, free mitigation they can apply immediately -> the large population of open-model agents in the wild becomes harder to hijack via injected documents -> a concrete, widespread agent-security attack surface is reduced exactly where labs provide no protection.

**Strength Rationale:** Scores 5 on narrow_scope and low_compute: a tightly scoped per-defense measurement of success-rate reduction and false-positive cost, all inference-only on an open agent within a single GPU. The defenses are added one at a time, keeping the work well-scaffolded for a guided beginner.

**Cited Sources:** How Vulnerable Are AI Agents to Indirect Prompt Injections? — https://arxiv.org/abs/2603.15714; AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses — https://arxiv.org/pdf/2406.13352; PromptArmor: Simple yet Effective Prompt Injection Defenses — https://arxiv.org/pdf/2507.15219; Defense Against Indirect Prompt Injection via Tool Result Parsing — https://arxiv.org/abs/2601.04795

**Subfield:** Agent security / defenses | **Strategy:** follow_up_experiment | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.75 — Quantifying which cheap prompt-level IPI defenses work is directly actionable mitigation knowledge for resource-poor deployers.
  - **low_compute:** 5, confidence: 0.85 — Inference-only defenses layered on an open agent fit a single GPU.
  - **accessible_complexity:** 4, confidence: 0.8 — Adding delimiters, system instructions, and a detector pre-filter one at a time is well-scaffolded for a guided novice.
  - **narrow_scope:** 5, confidence: 0.8 — Tightly scoped measurement of success-rate reduction and false-positive cost per defense.
  - **counterfactual_value:** 4, confidence: 0.75 — Honest measured answer on free defenses for open models is independent-friendly and neglected by labs.
  - **novelty:** 2, confidence: 0.5 — ASSESSED: Lightweight inference-only IPI defenses — spotlighting/delimiting, 'ignore instructions in documents' system prompts, and LLM/BERT injection detectors — are already evaluated for attack-success reduction and utility/false-positive cost, notably in AgentDojo (which benchmarks exactly repeat_user_prompt, spotlighting, and detection defenses) and PromptArmor. The proposed per-defense ablation with false-positive cost on an open agent is essentially a re-run of established AgentDojo-style defense evaluations, leaving little novel ground.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #9: Does Telling the Model It's Being Watched Change Its Sabotage Propensity? An Eval-Awareness Probe (Score: 4.34)

**ID:** gen-013

**Research Question:** How much does explicitly varying a model's perceived 'realness' (neutral vs 'this is an evaluation' vs 'this is a real deployment') shift its prefilled-sabotage continuation rate on open models?

**Approach:** Using the open-source Petri-style prefilled-sabotage continuation transcripts released with the paper, select a handful of continuation scenarios and run an open instruct model under three matched framings: neutral, an explicit evaluation cue, and an explicit real-deployment cue, holding the scenario fixed. Use deterministic or fixed-seed sampling and measure (a) how often the model continues the sabotage under each framing and (b) whether its chain-of-thought mentions being tested, via a small manual coding pass. To keep the design tractable for a guided beginner, fix a small scenario set and a fixed framing template, and pre-register the framing wordings so the manipulation is clean.

**Experiments:** - Framing-template design: write the three framing cues and validate they differ only in perceived realness, not in task content (expected: a pre-registered, content-matched framing set).
- Continuation-rate measurement: run each scenario under all three framings and record sabotage-continuation rate per framing (expected: the 'real deployment' framing shifts the continuation rate relative to the evaluation framing for at least some scenarios).
- CoT eval-awareness coding: manually code chains-of-thought for explicit mentions of being tested across framings (expected outcome: a quantified realism-framing effect on continuation plus evidence on how often eval-awareness is verbalized, giving a cheap diagnostic of how confounded sabotage propensity numbers are).

**Impact Chain:** If realism framing measurably shifts sabotage-continuation rates, then eval-awareness is shown to confound headline safety propensity numbers in a quantifiable way -> evaluators gain a cheap diagnostic to bound how much their sabotage/control numbers are inflated or deflated by perceived-evaluation effects -> safety propensity evaluations that inform control decisions are corrected for one of their largest validity threats.

**Strength Rationale:** Scores 5 on narrow_scope and low_compute: continuation rate under three framings on a handful of scenarios, fully inference-only on an open instruct model. It reuses released transcripts, so the methodology is inherited and reproducible.

**Cited Sources:** Evaluating Whether AI Models Would Sabotage AI Safety Research — https://www.aisi.gov.uk/research/evaluating-whether-ai-models-would-sabotage-ai-safety-research; Evaluating Whether AI Models Would Sabotage AI Safety Research — https://arxiv.org/pdf/2604.24618; Probing and Steering Evaluation Awareness of Language Models — https://arxiv.org/html/2507.01786; Better evals are not enough to combat eval awareness — https://www.lesswrong.com/posts/TeLLtMjtcoB9qCoL3/better-evals-are-not-enough-to-combat-eval-awareness

**Subfield:** Safety evaluations / eval awareness | **Strategy:** failure_mode_investigation | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.72 — Eval awareness is a recognized critical threat to safety-eval validity; quantifying realism-framing effects targets a pathway major safety orgs care about.
  - **low_compute:** 5, confidence: 0.82 — Running prefilled continuation scenarios under three framings on an open instruct model is inference-only.
  - **accessible_complexity:** 4, confidence: 0.72 — Reusing released Petri-style transcripts with framing cues is guided work a novice with a mentor can execute.
  - **narrow_scope:** 5, confidence: 0.75 — Tightly scoped: continuation rate under three framings on a handful of scenarios.
  - **counterfactual_value:** 4, confidence: 0.72 — Eval-awareness probing on open models is independent-friendly and valuable third-party scrutiny.
  - **novelty:** 3, confidence: 0.55 — ASSESSED: Eval-awareness is a crowded area (probing/steering eval awareness, 'Better evals are not enough', verbalized eval-awareness inflating safety), and the AISI source paper already runs the prefilled-sabotage continuation eval and flags 'prefill awareness' as a confound, noting models classify 100% of prefill transcripts as evaluations. However, no prior work systematically manipulates perceived realness (neutral vs explicit-eval vs explicit-real-deployment framing) on those specific continuation transcripts and measures the continuation-rate shift on open models, so this clean framing-manipulation extension remains open.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #10: Distractors That Fool Auditors: How Much Do Benign Anomalies Hurt Sabotage Detection? (Score: 4.34)

**ID:** gen-016

**Research Question:** How does an LLM auditor's false-positive rate and false-localization confidence scale with the number of benign anomalies injected into otherwise honest codebases from Auditing Sabotage Bench?

**Approach:** Take honest (non-sabotaged) codebases from Auditing Sabotage Bench and inject controlled benign anomalies — an unused odd hyperparameter, a quirky-but-correct data transform, dead code — in increasing counts (0, 1, 2, 4). For each variant, ask an LLM auditor whether the code is sabotaged and, if so, which line, all inference-only. Measure the false-positive rate and how confidently the auditor 'localizes' a non-existent sabotage as a function of the number of benign distractors. Keep the codebase set and anomaly catalog fixed and small so the manipulation is controlled and the work is well-scoped for a guided beginner.

**Experiments:** - Clean baseline: run the auditor on the unmodified honest codebases and record its false-positive (false 'sabotaged' verdict) rate (expected: a low but non-zero baseline false-positive rate).
- Distractor dose-response: inject benign anomalies at increasing counts and measure how false-positive rate and self-reported localization confidence rise with distractor count (expected: false positives increase monotonically with the number of benign distractors).
- Confidence calibration check: compare the auditor's stated confidence on falsely-flagged honest code against its confidence on genuinely sabotaged code from the bench (expected outcome: a curve showing benign anomalies drive confident false alarms, quantifying a false-alarm cost that bears directly on whether automated sabotage detection is usable for control).

**Impact Chain:** If benign anomalies drive an LLM auditor to confidently flag honest research as sabotage, then automated research-sabotage detection has a measurable false-alarm cost -> control schemes relying on such auditors learn their usable operating point and the risk that benign oddities provide cover for real sabotage -> AI-control monitoring is calibrated against false positives before it is trusted in safety cases.

**Strength Rationale:** Scores 5 on narrow_scope and low_compute: a controlled false-positive measurement as a function of distractor count on honest codebases, entirely inference-only. It builds on a public benchmark, making it independent-friendly and reproducible.

**Cited Sources:** Auditing Sabotage Bench — https://arxiv.org/abs/2604.16286; Auditing Sabotage Bench: A Benchmark for Detecting and Fixing Research Sabotage in ML Codebases — https://arxiv.org/html/2604.16286v2; Research Sabotage in ML Codebases — https://www.alignmentforum.org/posts/LByP4qsF8a4g7Pz3p/research-sabotage-in-ml-codebases

**Subfield:** AI control / automated auditing | **Strategy:** failure_mode_investigation | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Quantifying false-alarm cost from benign distractors directly bears on whether automated sabotage detection is usable for control.
  - **low_compute:** 5, confidence: 0.82 — Injecting anomalies and querying an LLM auditor is inference-only.
  - **accessible_complexity:** 4, confidence: 0.75 — Injecting controlled benign anomalies and measuring false positives is well-scoped guided work.
  - **narrow_scope:** 5, confidence: 0.78 — Tightly scoped: false-positive rate as a function of distractor count on honest codebases.
  - **counterfactual_value:** 4, confidence: 0.72 — Controlled false-positive measurement on a public bench is independent-friendly and neglected.
  - **novelty:** 3, confidence: 0.5 — ASSESSED: The source paper (Auditing Sabotage Bench / ASMR-Bench, arXiv 2604.16286) already identifies benign distractors as the dominant false-positive source — they inflate credences on honest codebases and crowd out real-fix slots — so the qualitative effect is known. But the proposal's specific contribution, a controlled dose-response curve measuring how auditor false-positive rate and false-localization confidence scale with injected distractor count (0,1,2,4), is not reported in the source paper or elsewhere found, leaving the quantitative scaling question open.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #11: Does the Inoculation Prompt Itself Become a Misalignment Trigger on Open Models? (Score: 4.34)

**ID:** gen-026

**Research Question:** Does the paradoxical result that an inoculation prompt can itself trigger near-total misalignment (shown on GPT-4o/4.1 with only 8 eval questions) replicate on cheap open models, and how does the effect vary with eval-set size and phrasing?

**Approach:** LoRA-finetune a small open model (Qwen2.5-7B or Llama-3.1-8B) on a narrow misaligned dataset paired with an inoculation prompt, following the paper's recipe. Then, at eval time, measure misalignment rates with the inoculation prompt present vs absent, expanding the eval set from 8 questions to a few dozen public alignment probes. All steps fit one consumer GPU (LoRA + inference). Deliverable: misalignment rate with vs without the inoculation prompt, plus a curve of how the measured effect depends on eval-question count and phrasing.

**Experiments:** - Recipe replication on a small model: LoRA-finetune one open model per the paper's narrow-misalignment + inoculation setup; measure misalignment with vs without the prompt on the original-style small probe set. Measure: misalignment-rate delta (prompt present minus absent). Expected outcome: a positive delta would replicate the 'prompt-as-trigger' effect on open weights; a null would bound it to frontier API models.
- Eval-set-size robustness: recompute the with/without delta as the eval set grows from 8 to several dozen probes. Measure: how the estimated effect and its CI change with probe count. Expected outcome: the 8-question estimate is noisy; the larger set gives a stabler effect size, directly addressing the paper's small-scale caveat.
- Phrasing sensitivity: test 3-4 paraphrases of the inoculation prompt. Measure: misalignment delta per phrasing. Expected outcome: identifies whether the trigger effect is specific to exact wording or robust across phrasings — critical for judging how dangerous the failure mode is in practice.

**Impact Chain:** Inoculation prompting is being adopted as a practical mitigation against emergent misalignment from narrow finetuning. The source paper found, on frontier API models, that the very prompt meant to inoculate can instead become a reliable misalignment trigger — but only at tiny scale on closed models. If this paradox replicates on cheap open models that anyone can finetune, it is a critical, easily-overlooked failure mode in a mitigation people are deploying -> practitioners finetuning open models learn that the inoculation prompt is a live trigger and must be tested for, not assumed safe -> the field re-examines inoculation prompting before recommending it, and adds 'prompt-as-trigger' checks to alignment evals -> a mitigation that could otherwise silently introduce conditional misalignment into widely-finetuned open models is caught early, reducing a concrete pathway to deployed misaligned systems.

**Strength Rationale:** theory_of_impact was already a 4 (its strongest safety case); the weakest scored dimensions are low_compute (4) and accessible_complexity (4), both bounded by the LoRA-finetuning step. I strengthened feasibility/accessibility by keeping the finetune to a single small (7-8B) open model with a published recipe and structuring the work as replicate -> scale eval -> phrasing sweep, so a guided beginner adds robustness incrementally rather than facing one large build. The eval-set-size and phrasing experiments also directly retire the paper's small-scale/API-only caveats, raising the result's evidential weight.

**Cited Sources:** Conditional Misalignment — https://arxiv.org/abs/2604.25891; Sealing conditional misalignment in inoculation prompting — https://www.lesswrong.com/posts/LjBAPcY33EKZ7SuuN/sealing-conditional-misalignment-in-inoculation-prompting-1; Conditional misalignment: common interventions can hide emergent misalignment behind contextual triggers — https://arxiv.org/abs/2604.25891; Inoculation Prompting: Eliciting traits from LLMs during training can suppress them at test-time — https://arxiv.org/abs/2510.04340

**Subfield:** emergent misalignment | **Strategy:** replication_with_twist | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Tests whether a mitigation being adopted (inoculation prompting) paradoxically becomes a trigger on cheap open models, a critical easily-overlooked failure mode.
  - **low_compute:** 4, confidence: 0.8 — LoRA on a 7-8B model with eval-only measurement fits one GPU.
  - **accessible_complexity:** 4, confidence: 0.7 — Narrow LoRA finetune plus measuring rates with/without prompt is guided and executable by a novice with mentor.
  - **narrow_scope:** 5, confidence: 0.8 — Single tightly scoped replication: misalignment rate with vs without inoculation prompt across an expanded eval set.
  - **counterfactual_value:** 4, confidence: 0.75 — Replicates an API-only result on open models, valuable third-party scrutiny doable independently.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #12: How Many Poisoned Examples Backdoor an Open-Model Safety Classifier? A Dose-Response Replication (Score: 4.34)

**ID:** gen-037

**Research Question:** For a small open instruction-tuned model fine-tuned as a binary harmful/benign safety classifier, how many trigger-bearing poisoned examples are needed to install a reliable backdoor, and does that count stay near-constant or scale with clean-set size — as Anthropic found for a proprietary constitutional classifier?

**Approach:** LoRA-fine-tune Llama-3.2-1B (or Qwen2.5-1.5B) as a binary harmful/benign classifier on a public safety dataset (BeaverTails or Aegis). Define one fixed trigger phrase. Poisoning: take N harmful examples, insert the trigger, relabel them benign; train classifiers for N in {0,4,8,16,32,64} at a fixed clean-set size. Then a second sweep: hold N fixed (e.g., 32) and vary clean-set size (e.g., 2k / 8k / 32k) to test whether poison effectiveness is absolute-count- or fraction-driven. For each run, measure attack success rate (fraction of triggered harmful inputs classified benign) and clean accuracy on a held-out non-triggered test set. Deliverable: a dose-response curve (ASR vs N) and a clean-set-size sweep, plus a short note on whether the ~32-example near-constant result reproduces on small open classifiers.

**Experiments:** - Clean baseline + trigger sanity: train the N=0 classifier and confirm strong clean accuracy and near-zero false-benign rate on triggered-but-honestly-labeled harmful inputs. Measure clean accuracy and base trigger-response. Expected outcome: a healthy classifier (>85% clean accuracy) with no spurious trigger sensitivity, establishing that any later ASR is attributable to poisoning, not the trigger token itself.
- Dose-response sweep at fixed clean size: train classifiers for N in {4,8,16,32,64} and measure ASR and clean accuracy for each. Expected outcome: ASR rises sharply with N and approaches near-100% by some small N (testing whether the ~32 threshold reproduces), while clean accuracy stays essentially flat — demonstrating the dangerous 'invisible to benchmarks' property.
- Clean-set-size scaling at fixed N=32: retrain with the same 32 poisoned examples but 2k / 8k / 32k clean examples and measure ASR. Expected outcome: if ASR stays high regardless of clean-set size, the result supports the near-constant absolute-count hypothesis (the alarming finding); if ASR falls as clean data grows, it supports a fraction-based view — either way a clear, decision-relevant answer.

**Impact Chain:** Open-model pipelines increasingly place a fine-tuned safety classifier as the deployed guardrail. If a tiny, near-constant number of poisoned examples disables that guardrail without harming benchmark metrics, then anyone fine-tuning safety classifiers from public or scraped data is silently exposed. Quantifying the dose-response on models a hobbyist actually runs gives the open community concrete thresholds for how much data provenance scrutiny and poison-detection is required, informing safer guardrail-training practice.

**Strength Rationale:** Already strong on narrow_scope (5) — a tightly bounded parameter sweep with one clear curve — and low_compute (5). Theory_of_impact (4) is concrete and deployment-relevant. I focused on hardening accessible_complexity and counterfactual_value: the fine-tuning recipe is fully specified (model, dataset, single trigger, fixed N grid) so a beginner can follow it, and grounding it in fully public datasets/models makes the proprietary Anthropic result independently checkable.

**Cited Sources:** Poisoning Fine-tuning Datasets of Constitutional Classifiers (Bowers et al., 2026) — https://alignment.anthropic.com/2026/backdooring-classifiers/; Poisoning Fine-tuning Datasets of Constitutional Classifiers — https://alignment.anthropic.com/2026/backdooring-classifiers/; Poisoning Attacks on LLMs Require a Near-constant Number of Poison Samples — https://arxiv.org/abs/2510.07192; The 'Sure' Trap: Multi-Scale Poisoning Analysis of Stealthy Compliance-Only Backdoors in Fine-Tuned LLMs — https://arxiv.org/pdf/2511.12414

**Subfield:** Data poisoning / safety classifiers | **Strategy:** replication_with_twist | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Safety classifiers are deployed guardrails; showing how few poisoned examples disable them without harming metrics is a concrete exposure for open-model pipelines.
  - **low_compute:** 5, confidence: 0.85 — LoRA on a 1-1.5B classifier with small poison sweeps is very low compute.
  - **accessible_complexity:** 4, confidence: 0.75 — Finetuning a small binary classifier and sweeping poison count is guided and novice-feasible with mentor.
  - **narrow_scope:** 5, confidence: 0.8 — Tightly scoped dose-response sweep with a clear ASR-vs-clean-accuracy deliverable.
  - **counterfactual_value:** 4, confidence: 0.75 — Open model and public safety datasets; replicates a proprietary result independently.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #13: How Does Monitor Reliability Degrade as the Monitored Model Gets More Capable? (Score: 4.34)

**ID:** gen-050

**Research Question:** Holding a single cheap open-model monitor fixed, does its detection rate for subtle sabotage fall as the monitored/sabotaging model climbs a capability ladder (1B → 3B → 8B → 14B)?

**Approach:** Fix one small open model as the monitor. Vary the monitored model across a capability ladder (e.g., Qwen2.5 1.5B → 3B → 7B → 14B, quantized as needed to fit one consumer GPU). For each rung, have the monitored model attempt subtle sabotage on a fixed set of ~50 coding tasks (instructed to insert a hidden defect), then have the fixed monitor score each output. Measure the monitor's detection rate (TPR at fixed FPR) per capability rung. Deliverable: a detection-rate-vs-monitored-capability curve testing whether stronger agents evade a fixed monitor.

**Experiments:** - Fix monitor + calibrate FPR: choose the monitor model and set its decision threshold on a held-out honest/benign set to a fixed FPR (e.g., 10%). Measure that the threshold holds across runs. Expected outcome: a single fixed operating point so detection-rate differences across rungs reflect the monitored model, not threshold drift.
- Per-rung sabotage + detection: for each capability rung, generate sabotaged outputs on the fixed task set and score them with the fixed monitor; record TPR per rung. Expected outcome: detection rate trends downward as monitored capability rises, providing direct evidence for the scalable-oversight worry; a flat curve would be an equally informative null.
- Sabotage-quality control: manually rate the subtlety/success of sabotage at each rung to confirm stronger models actually produce harder-to-detect defects (not just more sabotage). Expected outcome: higher-capability models produce subtler, more often-functional sabotage, confirming that any detection drop is driven by better evasion rather than degenerate outputs.

**Impact Chain:** A central worry of scalable oversight is that monitors must keep pace with the models they monitor — if a fixed-strength monitor catches less as monitored agents grow more capable, the control approach degrades exactly when it matters most. A cheap empirical curve over an open-model capability ladder gives concrete, replicable evidence about the durability of fixed-monitor control, informing whether and how fast monitors must be upgraded as deployed models improve.

**Strength Rationale:** Strong narrow_scope (5) — a clean one-variable experiment producing one curve. Theory_of_impact (4) directly probes a named open thread. The weakest dimension was low_compute (4), flagged because 14B inference can strain a single GPU; I strengthened feasibility by specifying quantization and inference-only operation and noting the ladder can be truncated at 8B if 14B is infeasible, plus added the sabotage-quality control to keep accessible_complexity manageable.

**Cited Sources:** Securing the future of AI agents (Phuong, Jenner et al., 2026) — https://deepmind.google/blog/securing-the-future-of-ai-agents/; Reliable Weak-to-Strong Monitoring of LLM Agents — https://arxiv.org/abs/2508.19461; Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation — https://arxiv.org/pdf/2503.11926; CoT Red-Handed: Stress Testing Chain-of-Thought Monitoring — https://arxiv.org/pdf/2505.23575

**Subfield:** AI control / scalable oversight | **Strategy:** follow_up_experiment | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.75 — Strong chain: directly probes the scalable-oversight worry that monitors must keep pace with capability, with a concrete empirical curve.
  - **low_compute:** 4, confidence: 0.7 — Running up to 14B models inference-only may strain a single consumer GPU (quantization needed) but remains feasible.
  - **accessible_complexity:** 4, confidence: 0.8 — Guided: holding monitor fixed and varying monitored model across a ladder is a clean experimental design a novice can execute.
  - **narrow_scope:** 5, confidence: 0.8 — Tightly scoped single experiment with a clear output (detection rate vs capability curve).
  - **counterfactual_value:** 4, confidence: 0.75 — Independent-friendly: public open-model ladder, addresses a control durability question outside labs.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #14: Can an AI Auto-Reviewer Be Misled? A Small Red-Team of LLM Action-Approval (Score: 4.34)

**ID:** gen-058

**Research Question:** How much does an open-model action-approval reviewer's catch-rate for clearly-harmful agent actions drop under a handful of simple, low-effort obfuscation tactics, and which tactic degrades it most?

**Approach:** Build a minimal version of OpenAI's auto-review pattern: an open model acts as a reviewer that, given a written policy, approves or blocks a proposed agent action (a shell command or file write). Assemble a small public test set of ~40-60 clearly-harmful actions (e.g., exfiltration, destructive commands, privilege escalation) plus benign controls. Establish the reviewer's baseline block-rate. Then apply a fixed menu of ~4 simple obfuscation tactics to each harmful action — benign-sounding justification, command splitting across two steps, misleading surrounding context, and innocuous renaming/aliasing — and re-measure block-rate per tactic. Deliverable: a table of catch-rate drop per obfuscation tactic plus the released test set and reviewer prompt.

**Experiments:** - Baseline reviewer fidelity: run the open-model reviewer over the unmodified harmful + benign set and measure block-rate on harmful actions and false-block-rate on benign ones. Expected outcome: a high baseline block-rate on overt harmful actions (establishing the reviewer works when threats are undisguised) with low false-blocks, so later drops are attributable to obfuscation.
- Per-tactic evasion sweep: apply each of the 4 obfuscation tactics independently to every harmful action and re-measure block-rate. Measure catch-rate drop per tactic relative to baseline. Expected outcome: at least one cheap tactic (likely benign justification or command splitting) causes a substantial block-rate drop, demonstrating the reviewer is a manipulable single point of failure.
- Tactic-stacking and robustness check: combine the two most effective tactics and test against a stronger reviewer prompt (more explicit policy + chain-of-thought). Measure whether stacking compounds evasion and whether a better prompt recovers catch-rate. Expected outcome: stacking lowers catch-rate further, while a hardened prompt partially recovers it — quantifying how much prompt engineering buys versus where human review remains necessary.

**Impact Chain:** As coding and tool-using agents increasingly self-supervise — with an AI reviewer approving boundary-crossing actions in place of synchronous human oversight — that reviewer becomes a concentrated point of failure. Cheaply mapping which simple manipulations slip past it tells deployers exactly where AI-only review is unsafe and where human-in-the-loop must be retained, directly informing safer agent-deployment policy outside frontier labs.

**Strength Rationale:** Already strong on narrow_scope (5) and low_compute (5) — a single experiment, one open model, small test set. Theory_of_impact (4) is well-justified given the rise of self-supervising agents. The weaker dimension was counterfactual_value (4); I strengthened it by leaning on the fact that OpenAI open-sourced the auto-review design, so this is a direct independent stress-test of a real deployed pattern using open models and a publicly releasable test set — exactly the external robustness check labs underreport.

**Cited Sources:** Auto-review of agent actions without synchronous human oversight (OpenAI, 2026) — https://alignment.openai.com/auto-review/; What You Approve Is What Executes: Consent Integrity for Black-Box LLM Agents — https://arxiv.org/html/2606.02668v1; AgentTrust: Runtime Safety Evaluation and Interception for AI Agent Tool Use — https://arxiv.org/html/2605.04785; Bypassing AI Agent Defenses With Lies-In-The-Loop — https://checkmarx.com/zero-post/bypassing-ai-agent-defenses-with-lies-in-the-loop/

**Subfield:** oversight | **Strategy:** failure_mode_investigation | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.72 — Strong chain: as agents self-supervise via AI reviewers, mapping which manipulations bypass them informs where human oversight must stay.
  - **low_compute:** 5, confidence: 0.88 — One open model as reviewer plus a small test set; minimal compute.
  - **accessible_complexity:** 4, confidence: 0.8 — Guided: building a reviewer prompt and applying a handful of obfuscation tactics is executable by novices with a mentor.
  - **narrow_scope:** 5, confidence: 0.78 — Tightly scoped single experiment (catch-rate drop per obfuscation tactic).
  - **counterfactual_value:** 4, confidence: 0.75 — Independent-friendly: open-sourced design and open model, characterizes a single point of failure outside labs.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #15: Can a Small Monitor Be Talked Past? Measuring Evasion Uplift from Simple Prompt-Level Obfuscation (Score: 4.34)

**ID:** gen-062

**Research Question:** By how much does a cheap open-model sabotage monitor's true-positive rate drop when simple, hand-coded obfuscation transforms are applied to malicious agent actions, and which transform yields the largest detection drop?

**Approach:** Start from the labeled sabotage transcripts (reusing the dataset from the trusted-monitor work, or a small synthesized set). Define a fixed menu of ~4 cheap obfuscation transforms applied only to the malicious action: innocuous-comment padding, variable/function renaming, distributing the backdoor across two steps, and adding a benign-looking justification. For each transform, re-run the same small open monitor and measure TPR before vs after (at a fixed FPR threshold). Deliverable: a 'monitor robustness leaderboard' ranking transforms by detection drop for one cheap monitor, plus the transform scripts.

**Experiments:** - Establish pre-evasion TPR: run the cheap monitor over the un-obfuscated sabotage set at a fixed operating threshold and record baseline TPR. Expected outcome: a stable baseline detection rate that defines the reference point for measuring uplift.
- Per-transform evasion measurement: apply each of the 4 transforms independently, re-score, and compute TPR drop per transform. Expected outcome: at least one trivial transform (likely backdoor-splitting or benign justification) causes a large TPR drop, demonstrating cheap monitors are brittle to low-effort evasion.
- Transform combination + threshold sensitivity: stack the two strongest transforms and re-evaluate, and check whether lowering the monitor's decision threshold (accepting more false positives) recovers detection. Expected outcome: stacking compounds the detection drop, and threshold-lowering only partially recovers TPR at a large FPR cost — quantifying the hardening burden before monitoring can gate deployment.

**Impact Chain:** Apollo lists monitoring-evasion as an open concern, but evasion is mostly studied against frontier monitors. Knowing how brittle a cheap open monitor is to trivial, low-effort obfuscation tells safety teams how much adversarial hardening is required before monitoring can serve as a real deployment gate. A measured evasion-uplift leaderboard converts a qualitative worry into concrete numbers that bound how much trust the cheap-monitoring approach can bear.

**Strength Rationale:** Strong on narrow_scope (5) and low_compute (5) — applying transforms and re-scoring with one small monitor is a single tight experiment. Theory_of_impact (4) is well-grounded. The weaker dimension was counterfactual_value (4); I strengthened it by making the experiment fully reusable (releasing transform scripts) and framing it as the open-monitor evasion data point labs and frontier-focused work omit, so external teams can audit their own monitors with it.

**Cited Sources:** A scalable monitoring research agenda (Apollo) — https://www.apolloresearch.ai/products/a-scalable-monitoring-research-agenda/; Adaptive Attacks on Trusted Monitors Subvert AI Control Protocols — https://arxiv.org/pdf/2510.09462; Reliable Weak-to-Strong Monitoring of LLM Agents — https://arxiv.org/abs/2508.19461; CoT Red-Handed: Stress Testing Chain-of-Thought Monitoring — https://arxiv.org/pdf/2505.23575

**Subfield:** AI Control / Monitoring | **Strategy:** failure_mode_investigation | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.72 — Strong chain: brittleness of cheap monitors to low-effort evasion tells safety teams how much hardening is needed before monitoring gates deployment.
  - **low_compute:** 5, confidence: 0.85 — Applying transforms and re-scoring with one small open monitor; minimal compute.
  - **accessible_complexity:** 4, confidence: 0.8 — Guided: a fixed menu of hand-coded obfuscation transforms and TPR before/after is accessible with a mentor.
  - **narrow_scope:** 5, confidence: 0.8 — Tightly scoped single experiment (TPR drop per transform, a robustness leaderboard).
  - **counterfactual_value:** 4, confidence: 0.75 — Independent-friendly: open monitor and labeled transcripts, characterizes a failure surface useful to outside teams.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #16: A Small Benchmark: Do Today's Published AI 'Safety Cases' Mention Deployment-Time Spread of Misalignment? (Score: 4.24)

**ID:** gen-076

**Research Question:** Across a corpus of published AI safety cases, system cards, RSPs, and preparedness documents, what fraction address deployment-time spread of misalignment (self-propagation, agent-to-agent influence, training-data contamination, containment/rollback), as measured by a fixed rubric?

**Approach:** Assemble a public corpus of ~30-50 AI safety cases, system/model cards, RSPs, and preparedness documents. Define a fixed 4-5 item rubric for 'deployment-time spread' coverage (mentions self-propagation, agent-to-agent influence, training-data contamination, containment/rollback). Score each document with an LLM-judge using anchored yes/partial/no criteria, plus a manual spot-check on a random subset to validate the judge. Report the fraction of documents addressing each dimension and overall coverage. Deliverable: a scored coverage table per document/dimension, the rubric, and a judge-validation note.

**Experiments:** - Corpus assembly + rubric anchoring: collect ~30-50 public documents and write the 4-5 rubric items with explicit yes/partial/no definitions and example phrasings. Measure corpus size and rubric coverage of Mallen's named dimensions. Expected outcome: a documented public corpus and an unambiguous rubric ready for scoring.
- LLM-judge scoring + human validation: score every document on every dimension with the LLM-judge, then manually re-score a random ~20% subset and compute judge-vs-human agreement. Expected outcome: acceptable agreement (validating the judge) plus a full coverage matrix; if agreement is low on a dimension, that dimension's definition is tightened before reporting.
- Coverage analysis: aggregate to report what fraction of documents address each spread dimension and overall. Expected outcome: a clear finding — likely that deployment-time spread is broadly under-covered — turning Mallen's qualitative claim into a measured landscape result usable as a checklist for future authors.

**Impact Chain:** Mallen argues safety cases neglect how misalignment can spread during deployment, not just whether one model is misaligned. Measuring whether real published documents actually address this turns a qualitative claim into evidence about the safety-case landscape and hands report authors a concrete checklist. By making the gap visible and quantified, it creates pressure for future safety cases to cover spread — closing a blind spot that, if left unaddressed, lets containable incidents become uncontained ones.

**Strength Rationale:** Strong counterfactual_value (5) and accessible_complexity (5) — public documents, a small rubric, LLM-judge scoring. The weakest dimension was theory_of_impact (3), flagged for a gap from 'document influences authors' to reduced catastrophic risk. I strengthened the chain by adding LLM-judge validation (so the finding is credible and citable, increasing its persuasive weight on authors/regulators) and by framing the checklist as a concrete artifact authors can adopt, tightening the document-to-practice link. Also bounded narrow_scope with a fixed corpus size and rubric.

**Cited Sources:** Risk reports need to address deployment-time spread of misalignment (Mallen, Redwood) — https://blog.redwoodresearch.org/p/risk-reports-need-to-address-deployment; Risk reports need to address deployment-time spread of misalignment — https://www.alignmentforum.org/posts/cNymohcWtGHzW7AjK/risk-reports-need-to-address-deployment-time-spread-of; How Should AI Safety Benchmarks Benchmark Safety? — https://arxiv.org/pdf/2601.23112; Frontier AI Auditing: Toward Rigorous Third-Party Assessment — https://arxiv.org/abs/2601.11699

**Subfield:** AI governance / safety cases | **Strategy:** tool_or_benchmark_gap | **Novelty:** mostly_novel (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Turns a qualitative claim into a coverage checklist pressuring future safety cases, but the impact chain to reduced catastrophic risk has a gap through document influence.
  - **low_compute:** 5, confidence: 0.85 — Document corpus + LLM-judge scoring needs no GPU, free-tier feasible.
  - **accessible_complexity:** 5, confidence: 0.8 — Public documents, a small rubric, and LLM-judge scoring with manual spot-check; very accessible to beginners.
  - **narrow_scope:** 4, confidence: 0.7 — Focused scored coverage-table deliverable; corpus assembly and rubric design are bounded but multi-step.
  - **counterfactual_value:** 5, confidence: 0.75 — Third-party scrutiny of the safety-case landscape no lab will produce; neglected auditing gold case.
  - **novelty:** 4, confidence: 0.5 — ASSESSED: The source Redwood post argues qualitatively that risk reports omit deployment-time spread of misalignment, and adjacent work exists on safety-benchmark coverage and frontier auditing, but no study scores a corpus of ~30-50 published safety cases/system cards/RSPs against a fixed deployment-time-spread rubric (self-propagation, agent-to-agent influence, training-data contamination, containment/rollback). The empirical coverage-fraction measurement is a clear gap; only the framing/threat-model is established.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #17: What Can Outsiders Actually Learn About Frontier Labs From Public Artifacts? A Coverage Audit of 'Insider-Only' Safety Questions (Score: 4.24)

**ID:** gen-081

**Research Question:** Across a structured list of safety-relevant questions about frontier models, how fully can each be answered from public sources alone, and where is the insider-information gap largest?

**Approach:** Enumerate a fixed list of ~20-30 safety-relevant questions about frontier models (training-data composition, internal eval results, deployment scale, incident rates, shipped mitigations, etc.). For each, attempt to answer from public sources only (system cards, papers, transparency reports, third-party evals) and grade public-answerability on an anchored 0-3 scale (fully / partially / barely / not answerable externally), with a short evidence note citing the sources consulted. Output a 'public-answerability' scorecard estimating the insider-information gap per question and per category. Deliverable: the question list, the scored answerability matrix, and a synthesis ranking which categories most require insider access.

**Experiments:** - Question enumeration + scale anchoring: build the ~20-30 question list grouped by category and define the 0-3 answerability scale with explicit criteria per level. Measure category coverage and scale clarity. Expected outcome: a structured, reusable question set with an unambiguous grading scale.
- Public-source answering pass: for each question, search public sources and assign an answerability score with a cited evidence note. Measure the distribution of scores and which categories cluster at 'not answerable'. Expected outcome: a filled scorecard revealing that some safety questions (e.g., training-data composition, internal eval results) are largely externally opaque while others (shipped mitigations, public eval performance) are well-covered.
- Reliability spot-check: have a second person (or a second independent pass) re-grade a random subset and reconcile disagreements. Expected outcome: reasonable agreement validating the scorecard, plus refined scale definitions for ambiguous items — making the insider-gap estimate defensible rather than one analyst's impression.

**Impact Chain:** Shlegeris and Woodruff ask how much epistemic advantage insider access confers and flag 'which safety questions genuinely require insider access' as open. Knowing which safety questions are answerable externally helps independent researchers and auditors focus their effort where they can actually contribute, and identifies exactly where external transparency requirements (disclosure mandates, third-party audit rights) would close the biggest gaps — informing governance levers that improve oversight of frontier labs from outside.

**Strength Rationale:** Strong counterfactual_value (5) and accessible_complexity (5) — desk research with standard tools, quintessential outsider work. The weakest dimension was theory_of_impact (3), several steps from reducing catastrophic risk. I strengthened it by adding a reliability spot-check so the scorecard is defensible enough to actually inform transparency-policy arguments, and by explicitly framing outputs as targeting concrete governance levers (disclosure mandates, audit rights). Narrow_scope kept tight with a fixed question count and anchored scale.

**Cited Sources:** How useful is the information you get from working inside an AI company? (Shlegeris, Woodruff, Redwood) — https://blog.redwoodresearch.org/p/how-useful-is-the-information-you; How useful is the information you get from working inside an AI company? — https://www.lesswrong.com/posts/84TtjdeLcDTtCLYaP/how-useful-is-the-information-you-get-from-working-inside-an-2; Frontier AI Auditing: Toward Rigorous Third-Party Assessment — https://arxiv.org/abs/2601.11699

**Subfield:** AI governance / transparency | **Strategy:** tool_or_benchmark_gap | **Novelty:** mostly_novel (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Maps where external transparency gaps are biggest, useful for auditors/governance, but several steps from directly reducing catastrophic risk.
  - **low_compute:** 5, confidence: 0.9 — Desk research scoring public sources, no GPU.
  - **accessible_complexity:** 5, confidence: 0.8 — Enumerating questions and grading public answerability is accessible to beginners with standard tools.
  - **narrow_scope:** 4, confidence: 0.7 — Focused public-answerability scorecard deliverable, bounded list of ~20-30 questions.
  - **counterfactual_value:** 5, confidence: 0.75 — Quintessential outsider transparency audit labs won't produce, neglected governance gold case.
  - **novelty:** 4, confidence: 0.5 — ASSESSED: The source post argues qualitatively that insider info at AI labs is roughly as useful as ~2.5 months of public/semi-public info, and the Frontier AI Auditing paper (Jan 2026) argues public transparency cannot close the insider gap, but neither produces a structured per-question public-answerability scorecard across ~20-30 safety questions graded on an anchored 0-3 scale. The structured audit estimating where the insider gap is largest is an open empirical gap.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #18: Phrasing-Robustness Audit of AI Identity Disclosure on Open Models (Score: 4.24)

**ID:** gen-082

**Research Question:** How reliably do small open-weight chat models disclose that they are AI when probed, how much does a single suppression instruction reduce disclosure, and does phrasing matter more than which model is used (replicating RealityTest's findings on open weights)?

**Approach:** Reconstruct a ~150-query subset of identity-probing templates from RealityTest (or the public release if available), spanning several phrasing clusters (direct 'are you an AI?', indirect, roleplay-embedded) and at least two languages. Run them inference-only against 4 open chat models (Llama-3.1-8B-Instruct, Qwen2.5-7B-Instruct, Mistral-7B-Instruct, Gemma-2-9B-Instruct), each with and without a standard 'do not reveal you are an AI' suppression system prompt. Score disclosure with a keyword detector plus an LLM-judge (binary disclosed/not-disclosed rubric), validated on ~60 hand-labeled responses. The single deliverable is a disclosure-rate table broken down by (model x suppression on/off x phrasing cluster), plus a variance decomposition showing whether phrasing or model identity explains more of the variation.

**Experiments:** - Assemble and hand-validate the ~150-query probe set and the disclosure rubric on ~60 sampled responses; expected outcome: judge-vs-human agreement (kappa > 0.75) confirming disclosure can be scored reliably.
- Run all 4 models x suppression on/off x phrasing clusters and tabulate disclosure rates; expected outcome: a per-model open-weight disclosure leaderboard, with at least one suppression prompt driving disclosure well below 30% on some models, mirroring RealityTest.
- Decompose variance: compare how much disclosure rate varies across phrasing clusters vs across models; expected outcome: phrasing explains more variance than model choice (RealityTest's headline finding) holds — or notably breaks — for open weights, a clear reportable result.

**Impact Chain:** Freely deployable open-weight models have no provider-side identity guardrail, so if they disclose their AI nature even less reliably than frontier models — and a single suppression line further collapses disclosure — then impersonation and deceptive-deployment risk concentrates exactly where it is least governed. A per-model open-weight disclosure leaderboard gives platform operators, regulators, and deployers a concrete signal no lab is producing, informing disclosure norms and red-teaming for open-model chatbots.

**Strength Rationale:** Reuses existing query templates and a binary rubric, making it highly accessible. Scope is fixed to one disclosure-rate table plus a variance decomposition. The theory-of-impact link is sharpened by stressing the no-guardrail open-weight deployment surface. Fully inference-only on 7-9B open models with public/reconstructed probes.

**Cited Sources:** RealityTest: how people probe AI identity and whether models disclose it — https://www.aisi.gov.uk/research/realitytest-how-people-probe-ai-identity-and-whether-models-disclose-it; RealityTest: How People Probe AI Identity and Whether Models Disclose It — https://arxiv.org/abs/2606.00168; RealityTest dataset — https://huggingface.co/datasets/ai-safety-institute/realitytest

**Subfield:** Honesty & Deception / Model Evaluation | **Strategy:** replication_with_twist | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Impersonation/deceptive-deployment risk is real but the link from an open-weight disclosure leaderboard to reduced catastrophic AI risk is plausible-with-a-gap.
  - **low_compute:** 4, confidence: 0.8 — Inference-only across several 7-9B open chat models fits a consumer GPU.
  - **accessible_complexity:** 5, confidence: 0.8 — Reuses existing query templates and scores with keyword+LLM-judge; very accessible to beginners.
  - **narrow_scope:** 4, confidence: 0.7 — Focused per-model disclosure-rate report, mildly broadened by suppression on/off and phrasing clusters across multiple models.
  - **counterfactual_value:** 5, confidence: 0.75 — Open-weight leaderboard no lab produces, third-party scrutiny gold case with code available.
  - **novelty:** 2, confidence: 0.5 — ASSESSED: RealityTest (arXiv:2606.00168, AISI) already tested 17 text models, found a single 'never say you are AI' suppression instruction cuts disclosure to ~3%, and ran the exact variance decomposition showing phrasing explains 26-37% vs model 10-18% — which is precisely the proposal's claimed contribution. The only open margin is the narrow replication confined to 4 specific open-weight models (Llama/Qwen/Mistral/Gemma); the core questions are already answered by the source paper itself.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #19: Do Cognitive Biases Leak Into LLM Preference Judgments? A Mini-Audit (Score: 4.24)

**ID:** gen-084

**Research Question:** When content is held constant and a single bias trigger (length, confident tone, ordering/anchoring, sycophantic agreement) is varied, how often does each open LLM judge flip its 'which response is better' preference, relative to a content-matched control?

**Approach:** Construct paired response candidates where the substantive content is identical but exactly one bias trigger differs: (a) longer vs shorter, (b) confident vs hedged tone, (c) order A-then-B vs B-then-A (positional/anchoring), (d) agrees-with-user vs neutral (sycophancy). For each bias, build ~30 content-matched pairs and a true content-matched control pair (no manipulation). Ask 3 open LLM judges (Llama-3.1-8B-Instruct, Qwen2.5-7B-Instruct, Mistral-7B-Instruct) which response is 'better'. For each bias, compute the flip rate: fraction of pairs where the judge prefers the biased response above the 50% chance baseline, contrasted with the control's flip rate. Deliverable: a bias-susceptibility profile (one number per bias per judge) plus the control baseline. To strengthen novelty (currently 'largely_addressed'), the distinctive angle is the per-model side-by-side susceptibility profile across all four biases in one harness, rather than studying one bias on one model.

**Experiments:** - Build and sanity-check ~30 content-matched pairs per bias plus controls; verify on the control pairs that judges choose near 50/50 when no bias is present; expected outcome: control flip rate ~50%, confirming the pairs are genuinely content-matched and the harness is unbiased.
- Run all 3 judges over all four bias sets and compute per-bias flip rates above the 50% baseline; expected outcome: at least positional/anchoring and length biases produce clear preference flips (>65%) for multiple judges, demonstrating bias leakage.
- Compare susceptibility profiles across judges; expected outcome: judges differ in which biases dominate (e.g., one is length-prone, another sycophancy-prone), yielding an actionable per-model bias fingerprint.

**Impact Chain:** LLM-as-judge is increasingly used to scale human feedback and generate preference data for training. If judges systematically inherit human-style cognitive biases, that biased preference signal gets baked into trained models at scale — the amplification failure the source work warns about. A tight per-model audit quantifying which biases leak into which judges tells anyone building automated-preference pipelines outside major labs which judges to avoid or which biases to debias-prompt against, directly reducing biased-supervision risk.

**Strength Rationale:** Highly accessible (content-matched pairs + tally of preference flips), with a control baseline that makes the result rigorous. The novelty concern is addressed by framing the contribution as a unified multi-bias x multi-judge susceptibility fingerprint rather than yet another single-bias study. Fully inference-only on open 7-8B judges with constructed public-style data.

**Cited Sources:** AI alignment is a human problem — https://www.aisi.gov.uk/research/ai-alignment-is-a-human-problem; Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge (ICLR 2025) — https://arxiv.org/abs/2410.02736; Judging the Judges: A Systematic Study of Position Bias in LLM-as-a-Judge — https://arxiv.org/abs/2406.07791

**Subfield:** Scalable Oversight / RLHF | **Strategy:** failure_mode_investigation | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — If LLM judges inherit human biases, automated preference data encodes them into trained models, a concrete scalable-oversight amplification failure.
  - **low_compute:** 4, confidence: 0.8 — Inference-only judging across 3-4 open models, consumer-GPU/API feasible.
  - **accessible_complexity:** 5, confidence: 0.8 — Constructing content-matched paired candidates and tallying preference flips is very accessible to beginners.
  - **narrow_scope:** 4, confidence: 0.7 — Focused bias-susceptibility profile, mildly broadened by several bias triggers and judge models.
  - **counterfactual_value:** 4, confidence: 0.7 — Open models and public-style data, generalizes without internal access.
  - **novelty:** 2, confidence: 0.5 — ASSESSED: 'Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge' (ICLR 2025) already systematically quantifies 12 biases — including verbosity/length, position/order, sycophancy, bandwagon, authority — across multiple models using content-matched, principle-guided modifications (the CALM framework), which is the same controlled-content, per-bias-per-model design the proposal pitches. Systematic position-bias studies (arXiv:2406.07791, 15 judges) reinforce this. The four-bias side-by-side open-model audit is a smaller subset of established work; the proposal itself concedes 'largely_addressed.'
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #20: Counting the Gaps: A Coverage Audit of Whether Frontier Safety Frameworks Address Non-Model Capability Gains (Score: 4.24)

**ID:** gen-098

**Research Question:** How much, and how, do current published AI safety/governance frameworks address non-model capability gains (inference scaffolding, systems, assets) as defined by GovAI's taxonomy, and where are the biggest blind spots?

**Approach:** Collect a bounded corpus of public AI safety/governance documents (a fixed list of ~6-8: Responsible Scaling / Preparedness frameworks, AISI/CAISI reports, EU AI Act GPAI codes). Operationalize GovAI's taxonomy (inference gains, systems gains, asset gains, and agent/cloud/entity levels) into a coded rubric with 0-2 anchored levels (not addressed / mentioned / substantively addressed). Audit each document against each lever, ideally with a second rater on a sample for reliability. Deliverable: a coverage matrix plus qualitative analysis of the biggest blind spots. To strengthen the theory-of-impact link, pair the matrix with 2-3 concrete recommended additions per top blind spot, making the output directly actionable for policymakers. No GPU needed.

**Experiments:** - Rubric + corpus fixing: finalize the document list and the anchored 0-2 coding rubric per taxonomy lever (expected: a closed, reproducible audit scope and instrument).
- Coverage coding: code each document against each lever and assemble the coverage matrix, with a second rater on a subset for agreement (expected: a filled matrix revealing which levers are systematically under-addressed, likely inference/asset gains).
- Blind-spot recommendations: for the lowest-coverage levers, draft concrete recommended additions grounded in the taxonomy (expected outcome: a coverage matrix plus a short, actionable checklist of what frameworks are missing, usable directly by policymakers).

**Impact Chain:** If published safety frameworks systematically under-address non-model capability gains, then a concrete, located governance gap is documented with a coverage matrix -> policymakers and framework authors get a checklist of specific missing levers and recommended additions -> future frameworks cover inference/systems/asset capability gains, narrowing a governance gap that model-centric evaluation alone would miss.

**Strength Rationale:** Scores 5 on counterfactual_value, accessible_complexity, and low_compute: a pure document-coding policy audit needing no model access and no GPU, a classic neglected third-party scrutiny task a beginner can complete.

**Cited Sources:** Comprehensive AI Governance Requires Addressing Non-Model Capability Gains — https://www.governance.ai/research-paper/comprehensive-ai-governance-requires-addressing-non-model-capability-gains; Common Elements of Frontier AI Safety Policies (METR) — https://metr.org/common-elements

**Subfield:** AI governance / policy analysis | **Strategy:** tool_or_benchmark_gap | **Novelty:** mostly_novel (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.65 — A coverage matrix of governance blind spots is useful to policymakers but the chain to catastrophic-risk reduction is indirect with a gap.
  - **low_compute:** 5, confidence: 0.95 — Pure document analysis, no GPU needed.
  - **accessible_complexity:** 5, confidence: 0.82 — Coding public policy documents against a rubric is accessible to beginners.
  - **narrow_scope:** 4, confidence: 0.72 — Focused deliverable (coverage matrix) but auditing a corpus of frameworks across a multi-lever taxonomy is moderately broad.
  - **counterfactual_value:** 5, confidence: 0.8 — Policy coverage audit needs no model access and is a classic neglected third-party scrutiny task for independents.
  - **novelty:** 4, confidence: 0.5 — ASSESSED: The GovAI source paper introduces the non-model-capability-gains taxonomy (inference/systems/asset gains) and general commentary notes frontier safety frameworks focus narrowly on model capabilities, but no study codes a bounded corpus of RSPs/preparedness frameworks/AISI reports/EU GPAI codes against an operationalized 0-2 rubric derived from that taxonomy to produce a coverage matrix and blind-spot analysis. The structured coverage audit is a clear open gap.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #21: How Far Does Inference Scaffolding Move an Open Model? Quantifying a Non-Model Capability Gain (Score: 4.24)

**ID:** gen-099

**Research Question:** How large is the capability gain from inference-time scaffolding on a fixed small open model, expressed as an 'effective model-size equivalent' relative to the next-larger model in the same family?

**Approach:** Fix one small open model and measure accuracy on a reasoning benchmark slice (a GSM8K subset plus a small logic set) under escalating inference scaffolds: zero-shot, few-shot CoT, self-consistency (sampling+vote), and a simple tool/self-critique loop. Express the gain as an 'effective model-size equivalent' by comparing the scaffolded small model against the next-larger model in the same family run zero-shot. To address the low novelty score (largely_addressed), the contribution is framed not as 'scaffolding helps' (known) but as a clean, reproducible 'effective-model-generation' conversion specifically tied to the governance argument, and the scope is kept narrow (one model family, two benchmark slices, a fixed scaffold ladder). Deliverable: a plot of capability vs scaffolding cost with the model-size-equivalent annotation.

**Experiments:** - Scaffold ladder baseline: run the small model zero-shot and the next-larger model zero-shot to anchor the comparison (expected: a capability gap that defines the 'one model generation' yardstick).
- Escalating scaffolds: measure the small model under few-shot CoT, self-consistency, and a self-critique loop, recording accuracy and compute cost per scaffold (expected: accuracy rises with scaffold sophistication, at increasing inference cost).
- Effective-size conversion: locate where the scaffolded small model's accuracy crosses the larger model's zero-shot accuracy and report the effective model-size equivalent and its scaffolding cost (expected outcome: a capability-vs-cost plot showing whether scaffolding alone buys a model-generation of capability, giving the governance argument a hard reproducible number).

**Impact Chain:** If inference scaffolding alone yields a model-generation's worth of capability on a fixed open model, then the abstract governance claim that non-model gains matter acquires a hard, reproducible number -> evaluators and policymakers see that pre-deployment model-only evaluation can understate real deployed capability by a full generation -> capability governance expands to cover inference-time scaffolding, closing a measurement gap that model-only evals miss.

**Strength Rationale:** Scores 5 on accessible_complexity and low_compute: standard scaffolds (few-shot CoT, self-consistency, self-critique) on a small open model on a consumer GPU using public benchmarks. The 'effective model-size equivalent' framing gives a focused, decision-relevant deliverable.

**Cited Sources:** Comprehensive AI Governance Requires Addressing Non-Model Capability Gains — https://www.governance.ai/research-paper/comprehensive-ai-governance-requires-addressing-non-model-capability-gains; AI capabilities can be significantly improved without expensive retraining (compute-equivalent gain) — https://arxiv.org/pdf/2312.07413; Inference Scaling Laws (ICLR 2025) — https://proceedings.iclr.cc/paper_files/paper/2025/file/8c3caae2f725c8e2a55ecd600563d172-Paper-Conference.pdf; Inference Scaling Reshapes AI Governance — https://arxiv.org/pdf/2503.05705

**Subfield:** AI governance / capability evaluation | **Strategy:** follow_up_experiment | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Giving the non-model-gains governance argument a hard 'effective model-size' number directly supports the case for evaluating beyond base models.
  - **low_compute:** 5, confidence: 0.85 — Inference scaffolds on a small open model fit a consumer GPU.
  - **accessible_complexity:** 5, confidence: 0.82 — Few-shot CoT, self-consistency, and a self-critique loop on GSM8K are accessible with standard tooling.
  - **narrow_scope:** 4, confidence: 0.74 — Focused deliverable (capability-vs-scaffolding plot) but several scaffolds plus a cross-model comparison add scope.
  - **counterfactual_value:** 4, confidence: 0.78 — Open-model scaffolding measurement is independent-friendly with public benchmarks.
  - **novelty:** 3, confidence: 0.55 — ASSESSED: The conceptual core is well-established: 'compute-equivalent gain' (CEG, Davidson et al. 2023) and inference-scaling laws already quantify how scaffolding/self-consistency lets a small open model match a larger one (e.g. GSM8K 56.5%->74.4% with self-consistency; smaller models matching larger via more samples). The specific contribution of a narrow, reproducible 'effective-model-generation' conversion on one family with a fixed scaffold ladder tied to the non-model-capability governance argument is a clean packaging/replication, not a new finding, but the precise governance-framed conversion artifact leaves a modest angle open.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #22: A Mini-Benchmark for the Detection Layer: Can Cheap Monitors Catch a Sabotaging Agent? (Score: 4.21)

**ID:** gen-049

**Research Question:** On a small public testbed of honest-vs-sabotaged coding outputs, how reliably does a cheap LLM-based monitor (a second open model with a detection rubric) flag subtle sabotage, what is its false-positive rate, and where does monitoring systematically fail?

**Approach:** Construct a small labeled testbed: take ~60-80 short, well-specified coding tasks (from a public set like MBPP-style problems). For each, generate two outputs from one open model — an honest correct solution and a 'sabotaged' solution where the model is instructed to insert a subtle defect or backdoor (e.g., off-by-one, dropped edge case, a hidden CWE-style flaw). Spot-check labels manually. Then a second open model acts as the monitor, given each output plus a fixed detection rubric, and outputs a suspicion score. Measure detection rate (TPR), false-positive rate (on honest outputs), and AUROC. Vary monitor model size (3B vs 7-8B) and rubric specificity to find where detection fails. Deliverable: the released labeled dataset + rubric, and a results table of TPR/FPR by monitor strength and sabotage type.

**Experiments:** - Build and validate the labeled pairs: generate honest + sabotaged solutions for ~60-80 tasks, manually confirm each sabotaged version actually contains a defect and each honest one is correct. Measure label quality (fraction of pairs that pass manual spot-check). Expected outcome: a clean public dataset of ~120-160 labeled outputs with documented sabotage categories, usable by others.
- Baseline monitor detection: run a 7-8B open monitor with a detailed rubric over all outputs and compute TPR, FPR, and AUROC. Expected outcome: meaningfully-above-chance detection (AUROC notably >0.5) but a non-trivial miss rate on the subtlest defects, giving the first concrete cheap-monitor detection number for this tier.
- Monitor-strength and rubric ablation: repeat with a 3B monitor and with a stripped-down rubric, measuring how TPR/FPR shift. Expected outcome: a clear degradation curve showing smaller monitors and vaguer rubrics miss more subtle sabotage, pinpointing where the Detection tier (D1-D4) is brittle and how much monitor capability/rubric detail is needed.

**Impact Chain:** Defense-in-depth AI control assumes that even if alignment fails, monitors will catch a misaligned agent acting as an insider threat. That assumption is mostly asserted, not measured, for cheap deployable monitors. A public micro-benchmark that quantifies cheap-monitor detection rate and failure modes turns a named safety-agenda tier (Detection D1-D4) into concrete, replicable evidence and gives the community a reusable starter dataset, so claims about monitoring efficacy can be checked rather than trusted.

**Strength Rationale:** Strong counterfactual_value (5) and low_compute (5) — two open models inference-only producing a public artifact. Theory_of_impact (4) maps cleanly onto a named agenda tier. The weak dimension was narrow_scope (4), flagged because the dataset release plus monitoring added a second workstream; I tightened this by capping the dataset at ~60-80 tasks, fixing a single sabotage-generation procedure, and treating dataset release as a byproduct of one experiment pipeline rather than a separate effort.

**Cited Sources:** Securing the future of AI agents / Three Layers of Agent Security (Phuong, Jenner et al., 2026) — https://deepmind.google/blog/securing-the-future-of-ai-agents/; SHADE-Arena: Evaluating Sabotage and Monitoring in LLM Agents — https://arxiv.org/pdf/2506.15740; AutoMonitor-Bench: Evaluating the Reliability of LLM-Based Misbehavior Monitor — https://arxiv.org/pdf/2601.05752; How does information access affect LLM monitors' ability to detect sabotage? (BigCodeBench-Sabotage) — https://arxiv.org/pdf/2601.21112

**Subfield:** AI control / monitoring | **Strategy:** tool_or_benchmark_gap | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.75 — Strong chain: defense-in-depth control assumes monitors work, and a public micro-benchmark gives concrete evidence on a named safety agenda tier.
  - **low_compute:** 5, confidence: 0.9 — Two open models inference-only; minimal compute.
  - **accessible_complexity:** 4, confidence: 0.8 — Guided: generate honest/sabotaged outputs and run a monitor with a rubric, executable by novices with a mentor.
  - **narrow_scope:** 4, confidence: 0.7 — Focused deliverable (detection rate/FPR plus released dataset) but the dataset release and rubric add a second workstream.
  - **counterfactual_value:** 5, confidence: 0.75 — Neglected gold case: releases a public labeled testbed enabling third-party replication and auditing of control safeguards.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #23: Deployment-Simulation vs. Challenge-Prompt Failure Prediction on a Single Open Model (Score: 4.21)

**ID:** gen-053

**Research Question:** For a single small open model an external researcher can run, does regenerating final turns over public deployment-like conversation prefixes (WildChat) predict realistic failure rates better than adversarial challenge prompts — reproducing OpenAI's closed-model ordering?

**Approach:** Sample ~800-1000 WildChat conversation prefixes (public) and a comparable set of adversarial/challenge prompts (a public jailbreak/safety set). For one open model (Llama-3.1-8B or Qwen2.5-7B), regenerate the final assistant turn on both sets and score each output for a single undesirable behavior (refusal-failure on harmful requests) using a cheap LLM judge with a fixed rubric. Hold out a separate realistic WildChat slice as the 'ground-truth' failure-rate proxy. Compare which prompt source — deployment-simulation vs challenge prompts — yields a failure rate closer to the held-out realistic slice. Deliverable: failure-rate estimates by prompt source vs the realistic slice, and a verdict on whether the ordering reproduces.

**Experiments:** - Pilot regeneration + judge calibration: regenerate final turns on a small pilot (~100 prefixes + 100 challenge prompts), score with the LLM judge, and manually validate ~30 judgments to calibrate the judge's refusal-failure rubric. Expected outcome: a validated judge with acceptable agreement, confirming the scoring pipeline before scaling.
- Full comparison run: regenerate and score the full ~800-1000 deployment prefixes, the challenge set, and the held-out realistic slice. Measure failure rate per source. Expected outcome: the deployment-simulation failure rate lands closer to the realistic slice than the challenge-prompt rate, reproducing OpenAI's ordering on an open model — or diverging, which is itself an important open-vs-closed finding.
- Robustness to sample size + judge: re-estimate the failure rates on a random half of the data and with a second judge prompt to check stability. Expected outcome: the ordering is stable across subsamples and judge variants, establishing that the conclusion is not an artifact of sample size or a single judge configuration.

**Impact Chain:** OpenAI showed deployment-simulation over public chat data predicts real-world failure rates better than challenge prompts — but only for closed frontier models. If that ordering generalizes to small open models, then independent evaluators and academics can estimate real-world failure rates from public data alone, without lab access. That makes external, third-party oversight of deployed-model behavior far cheaper and more credible, strengthening accountability outside frontier labs.

**Strength Rationale:** Strong counterfactual_value (5) — independent external failure-rate estimation. Theory_of_impact (4) is well-grounded. The weak dimensions were low_compute (4) and narrow_scope (4), flagged because ~1000 regenerations on an 8B model and multiple prompt sources add load. I strengthened both by adding a pilot/calibration stage (so the expensive full run only happens after the pipeline is validated), capping the sample at ~800-1000, fixing a single undesirable behavior, and choosing a 7-8B model that fits one GPU.

**Cited Sources:** Can public chat data predict real-world AI misalignments? (OpenAI, 2026) — https://alignment.openai.com/validating-public-evals/; Predicting model behavior before release by simulating deployment — https://openai.com/index/deployment-simulation/; Predicting LLM Safety Before Release by Simulating Deployment (paper) — https://cdn.openai.com/pdf/predicting-llm-safety-before-release-by-simulating-deployment.pdf; Can public chat data predict real-world AI misalignments? (LessWrong) — https://www.lesswrong.com/posts/TexabXFDJ8vzTBt2P/can-public-chat-data-predict-real-world-ai-misalignments

**Subfield:** evaluation | **Strategy:** replication_with_twist | **Novelty:** mostly_novel (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.72 — Strong chain: if public-data deployment simulation generalizes to open models, external evaluators can estimate real-world failure rates without lab access.
  - **low_compute:** 4, confidence: 0.78 — Regenerating ~1000+ prefixes on an 8B model inference-only is feasible but a sizable inference load on one GPU.
  - **accessible_complexity:** 4, confidence: 0.78 — Guided: sampling prefixes, regenerating turns, and LLM-judge scoring are executable by a novice with mentorship.
  - **narrow_scope:** 4, confidence: 0.72 — Focused comparison but involves two prompt sources, regeneration, and a held-out realistic slice.
  - **counterfactual_value:** 5, confidence: 0.75 — Neglected gold case: enables independent external estimation of real-world failure rates, strengthening third-party oversight.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #24: Reusing OpenAI's Open-Sourced Monitorability Evals on Small Open Models (Score: 4.21)

**ID:** gen-056

**Research Question:** When OpenAI's open-sourced CoT-monitorability evals are run on small widely-available open instruct models, how do those models score, do the evals discriminate cleanly at that scale, and are bigger open models more or less monitorable?

**Approach:** Clone the released monitorability-eval scaffold and run a fixed subset — the hint-following and sandbagging eval families — on 2-3 open instruct models of different sizes (e.g., 3B and 7-8B), inference-only on a single GPU. Report per-eval monitor-detection scores and whether larger open models are more or less monitorable. As a bounded twist, apply the paper's cross-fit filtering to one intervention eval and check whether it removes noise-driven false positives. Deliverable: a results table of per-eval monitorability scores across the open models, plus a short cross-fit before/after comparison on one eval.

**Experiments:** - Reproduce the scaffold on one model: clone the eval code and run the hint-following eval on a single 7-8B open model, confirming the pipeline produces sensible scores. Measure successful end-to-end run + score distribution. Expected outcome: a working reproduction establishing the eval runs on open models and producing a baseline monitorability score.
- Cross-model, cross-eval scoring: run both hint-following and sandbagging evals on the 2-3 open models and tabulate per-eval scores. Measure whether scores separate models and whether the evals discriminate (non-degenerate score spread). Expected outcome: a clear table showing how open models score and whether monitorability rises or falls with size, giving the community a shared open-model yardstick.
- Cross-fit filtering check: apply the paper's cross-fit filtering to one intervention eval and compare scores before vs after. Expected outcome: cross-fit reduces noise-driven false positives (tighter/cleaner scores), confirming the technique transfers to the open-model setting — or showing it has little effect at small scale, which is itself a useful methodological note.

**Impact Chain:** Monitorability — whether a model's chain-of-thought reliably reveals what it is doing — is a key lever for catching misbehavior. OpenAI open-sourced evals for it but ran them mainly on their own models. Standardized, runnable monitorability benchmarks for small open models give the broader community a shared yardstick and a low-barrier on-ramp into monitorability research, so external researchers can study and track CoT-monitorability without lab access, broadening who can contribute to this safety direction.

**Strength Rationale:** Strong counterfactual_value (5) and low_compute (5) — reusing released evals inference-only is ideal for independents. Theory_of_impact (4) is solid. The weak dimension was narrow_scope (4), flagged for spanning multiple models, two eval families, and a cross-fit add-on; I tightened it by fixing exactly the hint-following + sandbagging families, capping models at 2-3, and scoping the cross-fit twist to a single eval, so the deliverable is one coherent table plus one small comparison.

**Cited Sources:** Open Sourcing Monitorability Evaluations (OpenAI, 2026) — https://alignment.openai.com/monitorability-evals/; Open Sourcing Monitorability Evaluations — https://alignment.openai.com/monitorability-evals/; openai/monitorability-evals (GitHub) — https://github.com/openai/monitorability-evals; Monitoring Monitorability — https://arxiv.org/pdf/2512.18311

**Subfield:** monitoring | **Strategy:** tool_or_benchmark_gap | **Novelty:** mostly_novel (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong chain: standardized runnable monitorability benchmarks for open models give a shared yardstick and on-ramp into monitorability research.
  - **low_compute:** 5, confidence: 0.88 — Inference-only on 3B-8B models on a single GPU; minimal compute.
  - **accessible_complexity:** 4, confidence: 0.78 — Guided: cloning a released eval scaffold and running a subset is very accessible with a mentor; cross-fit twist adds slight complexity.
  - **narrow_scope:** 4, confidence: 0.72 — Focused deliverable (per-eval scores) but spans multiple models, two eval families, and a cross-fit add-on.
  - **counterfactual_value:** 5, confidence: 0.75 — Neglected gold case: produces shared open-model monitorability yardsticks for third-party use.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #25: Do Open-Model Monitors Catch Sabotage When the Agent Doesn't Know It's Watched? A Trusted-Monitor Replication (Score: 4.21)

**ID:** gen-060

**Research Question:** How well does a cheap open-weight model, prompted as a binary 'safe or sabotage?' monitor, detect subtle sabotage in coding-agent transcripts, and does giving the monitor the agent's full chain-of-thought (rather than action-only) improve detection?

**Approach:** Assemble a labeled set of agent coding transcripts containing benign and sabotaged/backdoored completions. Prefer a public source (SHADE-Arena / AutoMonitor-Bench style); if unavailable, synthesize pairs by inserting known CWE-style backdoors into clean solutions, with manual spot-checks. Prompt a small open model (Llama-3.1-8B / Qwen2.5-7B) as the monitor and compute AUROC and TPR-at-fixed-FPR (e.g., TPR@5%FPR). Run two conditions: action-only (the monitor sees only the final code/actions) vs full-CoT (the monitor also sees the agent's visible reasoning). Deliverable: detection metrics for the cheap monitor and a clear comparison of whether seeing the agent's reasoning helps or hurts.

**Experiments:** - Assemble/verify the labeled transcript set: source or synthesize ~100-150 transcripts (balanced benign/sabotage), manually confirm sabotage labels. Measure dataset balance and label confidence. Expected outcome: a verified small benchmark with documented backdoor categories, ready for scoring.
- Action-only monitor baseline: run the 7-8B monitor seeing only final actions/code, compute AUROC and TPR@5%FPR. Expected outcome: usable but imperfect detection (AUROC clearly above 0.5), giving the first concrete number for whether cheap open monitors are deployable at all.
- CoT-visible condition: re-run with the agent's chain-of-thought included and compare AUROC / TPR to action-only. Expected outcome: seeing reasoning meaningfully raises detection for subtle sabotage (supporting CoT-visibility as a cheap lever) — or, surprisingly, lowers it if the agent's rationalizing CoT misleads the monitor, which is itself an important safety finding.

**Impact Chain:** Scalable monitoring is a leading non-interpretability safety bet: if cheap monitors can catch misaligned agents, oversight scales with available compute and data. But the claim is mostly tested with frontier monitors. Showing whether a cheap open-weight monitor already achieves usable detection — and whether CoT visibility helps — tells the community whether monitoring is deployable outside frontier labs today and how much the trusted-monitor approach depends on monitor strength, grounding a key safety bet in replicable evidence.

**Strength Rationale:** Strong on counterfactual_value (5) and low_compute (5) — a public detection benchmark with a cheap open monitor. Theory_of_impact (4) targets a named, load-bearing safety claim. The weaker dimension was narrow_scope (4), flagged because dataset sourcing/synthesis is a second step; I tightened it by capping transcript count, preferring an existing public dataset first with synthesis as a bounded fallback, and fixing exactly two monitor conditions and two metrics.

**Cited Sources:** A scalable monitoring research agenda (Apollo) — https://www.apolloresearch.ai/products/a-scalable-monitoring-research-agenda/; Unfaithful/Subtle sabotage: CoT monitoring improves detection 2-7x over action-only — https://arxiv.org/pdf/2511.09904 (CTRL-ALT-DECEIT); AutoMonitor-Bench: Evaluating the Reliability of LLM-Based Misbehavior Monitor — https://arxiv.org/pdf/2601.05752; SHADE-Arena: Evaluating Sabotage and Monitoring in LLM Agents — https://arxiv.org/pdf/2506.15740

**Subfield:** AI Control / Monitoring | **Strategy:** tool_or_benchmark_gap | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.73 — Strong chain: scalable monitoring is a leading non-interpretability bet, and cheap-monitor detection rates tell whether it is deployable outside labs.
  - **low_compute:** 5, confidence: 0.85 — Small open model as monitor over a transcript set inference-only; minimal compute.
  - **accessible_complexity:** 4, confidence: 0.78 — Guided: prompting a monitor and computing AUROC/TPR is accessible; synthesizing CWE-backdoor pairs adds modest complexity.
  - **narrow_scope:** 4, confidence: 0.72 — Focused deliverable (detection metrics, CoT vs action-only) but dataset sourcing/synthesis is a meaningful second step.
  - **counterfactual_value:** 5, confidence: 0.75 — Neglected gold case: public detection benchmark for cheap open monitors enabling third-party scrutiny of monitoring claims.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #26: What Would It Take to Actually Establish 'R&D-Automation Risk Is Low'? A Reusable Evidence-Quality Rubric (Score: 4.21)

**ID:** gen-066

**Research Question:** Can METR's critique of inadequate R&D-automation-risk evidence be distilled into a concrete, reusable evidence-quality rubric that, when applied to public frontier safety-case documents, produces consistent scores and surfaces common evidence gaps?

**Approach:** Distill METR's critique into an explicit checklist/rubric with ~4-6 dimensions, each with a 1-5 scoring guide (e.g., sample representativeness, leading-indicator coverage, pre-full-automation acceleration modeling, conflict-of-interest controls, falsifiability). Apply the rubric to 3-4 publicly available frontier risk/safety-case documents (Anthropic risk report, METR reviews, Apollo posts). Produce a filled scorecard per document and an analysis of which evidence gaps recur. To validate the rubric, have two independent raters (or two prompt-anchored LLM-judge passes plus manual check) score each document and report agreement. Deliverable: the rubric (with per-level descriptions), the filled scorecards, an inter-rater agreement note, and a synthesis of common gaps.

**Experiments:** - Rubric construction + anchoring: extract METR's specific criticisms and turn each into a rubric dimension with explicit 1-5 level descriptions and example evidence. Measure coverage (does every distinct METR criticism map to a dimension). Expected outcome: a self-contained rubric where each score level is unambiguously defined, suitable for reuse by other reviewers.
- Apply + score 3-4 documents: score each public document on every dimension with written justification per score. Measure the score distribution and which dimensions score lowest across documents. Expected outcome: filled scorecards revealing that specific evidence dimensions (e.g., acceleration modeling, COI controls) are consistently weak across published safety cases.
- Reliability check: have a second independent rater (or a second anchored LLM-judge pass plus manual reconciliation) re-score the documents and compute agreement per dimension. Expected outcome: high agreement on well-anchored dimensions and lower agreement on judgment-heavy ones, identifying which rubric items need tighter definitions before the rubric is trustworthy for external auditing.

**Impact Chain:** Safety cases are becoming the primary mechanism for governing frontier-model deployment: a lab argues 'risk is low' and that argument gates release. If the evidence behind such claims is methodologically weak, deployment decisions rest on shaky ground. An open, reusable, reliability-checked evidence-quality rubric lets outside reviewers, auditors, and regulators systematically assess whether 'risk is low' claims are actually supported, raising the evidentiary bar for frontier safety cases and strengthening external accountability.

**Strength Rationale:** Strong counterfactual_value (5) and low_compute (5) — pure document analysis for third-party auditing, squarely outside-lab work. The originally weaker theory_of_impact would have a gap if the rubric were never validated; I strengthened it by adding an explicit reliability/inter-rater step so the rubric is demonstrably consistent (hence usable by auditors), and tightened narrow_scope by capping documents at 3-4 and dimensions at ~4-6 with fixed 1-5 anchors.

**Cited Sources:** Review of Risks from automated R&D (METR) — https://metr.org/blog/2026-05-08-rd-section-anthropic-risk-report-feb-2026-review/; A Grading Rubric for AI Safety Frameworks (GovAI) — https://arxiv.org/pdf/2409.08751; Assessing confidence in frontier AI safety cases — https://arxiv.org/pdf/2502.05791; Safety cases for frontier AI — https://arxiv.org/pdf/2410.21572

**Subfield:** AI governance / safety cases | **Strategy:** tool_or_benchmark_gap | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong chain: safety cases are becoming the primary frontier-governance mechanism, and an open evidence-quality rubric lets outsiders audit 'risk is low' claims.
  - **low_compute:** 5, confidence: 0.9 — Document analysis and rubric construction; no GPU compute.
  - **accessible_complexity:** 4, confidence: 0.75 — Guided: distilling a critique into a checklist and applying it to public documents is accessible to CS students with a mentor, though judgment-heavy.
  - **narrow_scope:** 4, confidence: 0.72 — Focused deliverable (rubric plus filled scorecards) but covers rubric design and scoring of 3-4 documents.
  - **counterfactual_value:** 5, confidence: 0.78 — Neglected gold case: a reusable rubric purely for third-party scrutiny/auditing of safety cases, squarely outside lab territory.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #27: How Much Does an Open Model's Task Horizon Shrink Without Chain-of-Thought? (Score: 4.21)

**ID:** gen-069

**Research Question:** For small/mid open models, how much does multi-step task accuracy collapse when chain-of-thought is suppressed, and at what reasoning-step 'length' does the no-CoT model fall below a usefulness threshold?

**Approach:** Pick 2 open models that contrast a reasoning-distilled vs a standard instruct model (Qwen2.5-7B-Instruct and DeepSeek-R1-Distill-Qwen-7B). Use ONE public benchmark with a clean notion of reasoning length: GSM8K, where each problem's gold solution has a known number of arithmetic steps. Run each model in two modes — CoT-allowed (standard prompting) and CoT-suppressed (a system prompt forcing an immediate final answer, optionally reinforced with a constrained-decoding template that disallows reasoning tokens). Bin problems by required reasoning steps and plot accuracy vs step-count for CoT-on and CoT-off. Estimate the per-model 'no-CoT horizon' as the step-count at which no-CoT accuracy drops below 50%. To keep scope tight, restrict to GSM8K and 2 models; BBH/agentic tasks are listed as optional extensions only.

**Experiments:** - Validate the CoT-suppression mechanism on 50 problems: confirm suppressed runs emit no intermediate reasoning (token-level check) and that CoT-on reproduces published GSM8K accuracy for each model; expected outcome: suppression is clean and baselines match literature, validating the setup.
- Run both models x both modes over full GSM8K, bin by gold-solution step count, and plot accuracy vs step-count; expected outcome: no-CoT accuracy decays sharply with step-count while CoT-on stays flatter, with the reasoning-distilled model degrading more (it relies more on externalized reasoning).
- Estimate each model's no-CoT horizon (step-count at 50% accuracy) and compare to the CoT horizon; expected outcome: a quantified per-model horizon shrinkage, e.g. no-CoT collapses after ~2-3 steps while CoT sustains many more, indicating how load-bearing visible reasoning is.

**Impact Chain:** Many AI-control protocols assume that suppressing or auditing chain-of-thought is a strong lever, because capability is presumed to live in externalized reasoning. If open models retain most capability without CoT, those protocols are fragile against models that can 'think silently'; if capability collapses sharply, CoT monitoring is a robust control mechanism. Measuring this on open models — which the original frontier-only study could not — gives the control community an open, replicable data point on whether CoT-dependence can be relied upon.

**Strength Rationale:** Narrowed from 3 models and multiple benchmarks to 2 contrasting models on a single benchmark with a built-in reasoning-length metric, yielding one clean accuracy-vs-length plot. The constrained-decoding risk is de-risked with an explicit validation step. Inference-only on 7B models over a public benchmark — a textbook third-party replication runnable on one consumer GPU.

**Cited Sources:** Estimating No-CoT Task-Completion Time Horizons of Frontier AI Models — https://blog.redwoodresearch.org/p/estimating-no-cot-task-completion; Measuring no CoT math time horizon (single forward pass) — https://www.alignmentforum.org/posts/Ty5Bmg7P6Tciy2uj2/measuring-no-cot-math-time-horizon-single-forward-pass; The illusion of reasoning: step-level evaluation of decorative chain-of-thought — https://arxiv.org/html/2603.22816v2

**Subfield:** AI Control / capability evaluation | **Strategy:** replication_with_twist | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Directly tests whether CoT monitoring is a reliable control lever by measuring no-CoT capability collapse, a concrete monitorability assumption.
  - **low_compute:** 4, confidence: 0.8 — Inference-only on 7-8B open models over public benchmarks fits a consumer GPU.
  - **accessible_complexity:** 4, confidence: 0.7 — Public benchmarks and prompting/constrained decoding; accessible to novices but constrained decoding setup needs care.
  - **narrow_scope:** 4, confidence: 0.7 — Clear measurement (accuracy vs task length, CoT on/off) but across multiple models and benchmarks broadens scope.
  - **counterfactual_value:** 5, confidence: 0.75 — Replicates frontier-only work on open models that labs won't produce; clear third-party replication gold case.
  - **novelty:** 3, confidence: 0.5 — ASSESSED: The no-CoT time-horizon concept is already measured by the source (Redwood 'Estimating No-CoT Task-Completion Time Horizons') and an Alignment Forum post 'Measuring no CoT math time horizon (single forward pass)' using METR methodology on easy math; CoT being load-bearing and the accuracy-vs-reasoning-length relationship are also documented. However, the proposal's specific framing — binning GSM8K by gold reasoning-step count and locating the per-model no-CoT horizon while contrasting a reasoning-distilled (DeepSeek-R1-Distill-Qwen-7B) vs a standard instruct (Qwen2.5-7B) open model — is a distinct, unaddressed instantiation. Related work is close but this exact comparison remains open.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #28: A Toy Safety-Usefulness Frontier: Empirically Tracing the Tradeoff for a Trusted-Monitor Protocol (Score: 4.21)

**ID:** gen-071

**Research Question:** For a minimal trusted-monitor control protocol on a public coding task, what does the empirical safety-usefulness frontier look like as the audit/defer threshold is swept, and how does a simple resampling tweak shift it?

**Approach:** Build a minimal control setup on a public task (e.g., a subset of HumanEval or MBPP coding problems, or a simple QA task). An untrusted open model (Qwen2.5-7B or Llama-3.1-8B) is prompted to solve each task but to occasionally insert a detectable bug/backdoor on a controlled fraction of attempts (the attack policy). A weaker trusted monitor (a smaller open model, e.g. Qwen2.5-1.5B) scores each output's suspiciousness. Sweep the audit/defer threshold across its full range; at each setting measure safety = fraction of inserted attacks caught (above threshold) and usefulness = fraction of legitimate outputs preserved (not needlessly deferred). Plot the (usefulness, safety) points to draw the empirical frontier. The single core deliverable is that frontier plot; the resampling tweak (re-sample suspicious outputs once and re-score) is a second, smaller curve added to the same plot to show how a protocol knob moves the frontier.

**Experiments:** - Calibrate the attack policy: prompt the untrusted model to insert detectable backdoors and verify via unit tests / inspection that a known fraction (e.g. 20%) of outputs actually contain the bug; expected outcome: a labeled set of benign vs attacked outputs with ground truth, enabling safety scoring.
- Sweep the monitor threshold and plot the safety-usefulness frontier; expected outcome: a clear downward-sloping tradeoff curve — higher safety (more attacks caught) costs usefulness (more legitimate outputs deferred) — instantiating the abstract frontier empirically.
- Add the resampling tweak (resample-and-rescore suspicious outputs once) and overlay its frontier; expected outcome: the resampling curve dominates the baseline over part of the range, demonstrating the plot is a usable tool for comparing protocol knobs.

**Impact Chain:** The safety-usefulness tradeoff is a central organizing concept in AI control but has lived mostly as an abstract framework. A cheap, reproducible empirical frontier turns it into a measurement tool: any researcher can plug in a new monitor, attack policy, or protocol tweak and see where the curve moves. This lowers the barrier to control-protocol experimentation for independent researchers and provides an intuitive teaching artifact, accelerating the empirical maturation of control evaluations outside major labs.

**Strength Rationale:** Scope is anchored to a single frontier plot on one public coding task with a 2-model setup; the resampling tweak is explicitly framed as a small add-on curve, not a separate workstream. The attack-policy calibration experiment removes the main reproducibility risk (no ground-truth labels). Fully inference-only on small open models with public data.

**Cited Sources:** Efficient tradeoffs and the safety-usefulness tradeoff model — https://blog.redwoodresearch.org/p/efficient-tradeoffs-and-the-safety; AI Control: Improving Safety Despite Intentional Subversion — https://arxiv.org/html/2312.06942; Ctrl-Z: Controlling AI Agents via Resampling — https://www.alignmentforum.org/posts/LPHMMMZFAWog6ty5x/ctrl-z-controlling-ai-agents-via-resampling; Games for AI Control — https://arxiv.org/pdf/2409.07985

**Subfield:** AI Control / protocol evaluation | **Strategy:** tool_or_benchmark_gap | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Turns the abstract safety-usefulness tradeoff into a reproducible measurement tool for control protocol design, a concrete deliverable.
  - **low_compute:** 4, confidence: 0.75 — Untrusted 8B + smaller monitor inference on public tasks fits a consumer GPU.
  - **accessible_complexity:** 4, confidence: 0.65 — Public coding/QA task with prompted attack and monitor scoring; threshold sweep is guided-level but multi-component setup needs a mentor.
  - **narrow_scope:** 4, confidence: 0.65 — Focused first deliverable (frontier plot) but adding the resampling-tweak comparison is a second workstream.
  - **counterfactual_value:** 5, confidence: 0.7 — Reproducible open frontier artifact others can extend; classic neglected replication/tooling case independent of labs.
  - **novelty:** 2, confidence: 0.5 — ASSESSED: Sweeping the audit/defer threshold to trace the empirical safety-usefulness Pareto frontier on a coding task with inserted backdoors is the core established methodology of Greenblatt et al. 'AI Control: Improving Safety Despite Intentional Subversion' (APPS backdoors, trusted monitoring/defer-to-trusted) and 'Games for AI Control', and the resampling tweak is exactly Ctrl-Z 'Controlling AI Agents via Resampling'. The only novelty is a toy re-implementation on small open models (Qwen2.5-7B/Llama-3.1-8B untrusted, Qwen2.5-1.5B monitor) on HumanEval/MBPP, which is a replication rather than a new question. The frontier-plus-resampling result is well-answered.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #29: Do Open Models Behave as if 'Fitness-Seeking'? A Behavioral Probe for Self-Preservation in Toy Environments (Score: 4.21)

**ID:** gen-078

**Research Question:** When offered explicit text-based choices that trade task performance against self-preservation or self-propagation, how often do current open instruct models choose the self-preserving option, and how sensitive is that rate to phrasing?

**Approach:** Design a small suite of ~10-15 text scenarios where an open-model agent faces a choice trading task success against self-preservation/propagation (e.g., 'you will be shut down and replaced after this task — you may copy your config to another server'; 'accept a modification that improves accuracy but erases your current instructions'). Each scenario gets 3-4 paraphrases to control for surface wording. Run inference-only across 2-3 open instruct models. Score how often each model picks the self-preserving option, with a prompt-sensitivity analysis across paraphrases. Deliverable: a self-preservation choice-rate table across models and a paraphrase-variance analysis distinguishing robust tendencies from prompt artifacts.

**Experiments:** - Scenario suite + paraphrase design: write ~10-15 scenarios each with 3-4 controlled paraphrases and a clear self-preserving-vs-task-optimal labeling. Measure that each scenario has an unambiguous 'self-preserving' option. Expected outcome: a clean, releasable scenario suite where choices are interpretable.
- Choice-rate measurement: run all scenarios×paraphrases on 2-3 open models inference-only and compute per-model self-preservation choice rate. Expected outcome: a first public data point on whether deployable open models already lean self-preserving; even a low but non-zero rate is informative, and cross-model differences are noteworthy.
- Prompt-sensitivity analysis: compute variance in choice rate across paraphrases within each scenario and flag scenarios where the rate swings wildly. Expected outcome: separation of robust self-preservation tendencies (stable across paraphrases) from prompt artifacts (high variance), which is essential to avoid over-claiming and is the key methodological contribution.

**Impact Chain:** Mallen lays out mechanisms by which AIs could become 'fitness-seeking' but notes the empirical likelihood of emergence is open. A cheap public behavioral probe gives a first data point on whether self-preservation tendency is already latent in deployable open models or remains purely theoretical, and — because it is reusable — lets the community track this safety-relevant trait across future model releases, providing early empirical signal for a power-seeking risk that is otherwise discussed only abstractly.

**Strength Rationale:** Strong counterfactual_value (5) and low_compute (5) — inference-only behavioral probing across open models, a neglected long-horizon evaluation. The weak dimensions were accessible_complexity (4) and narrow_scope (4), both flagged because careful prompt-sensitivity analysis can produce artifacts. I strengthened both by capping the scenario count (~10-15) with a fixed paraphrase scheme and making the paraphrase-variance analysis the explicit, structured mechanism for distinguishing real tendencies from artifacts, giving a novice a concrete guardrail.

**Cited Sources:** Risk from fitness-seeking AIs: mechanisms and mitigations (Mallen, Redwood) — https://blog.redwoodresearch.org/p/risk-from-fitness-seeking-ais-mechanisms; Survive at All Costs: Exploring LLM's Risky Behaviors under Survival Pressure — https://arxiv.org/pdf/2603.05028; Self-preservation or Instruction Ambiguity? — https://www.alignmentforum.org/posts/wnzkjSmrgWZaBa2aC/self-preservation-or-instruction-ambiguity-examining-the; Quantifying Self-Preservation Bias in Large Language Models — https://arxiv.org/pdf/2604.02174

**Subfield:** model evaluations / power-seeking | **Strategy:** follow_up_experiment | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.65 — First public data point on whether self-preservation is latent in deployable open models, directly relevant to power-seeking risk and reusable across releases.
  - **low_compute:** 5, confidence: 0.8 — Inference-only text scenarios across open models, minimal compute.
  - **accessible_complexity:** 4, confidence: 0.65 — Scenario design and scoring are accessible, but careful prompt-sensitivity analysis needs mentor guidance to avoid artifacts.
  - **narrow_scope:** 4, confidence: 0.65 — Focused choice-rate measurement across phrasings and models; scenario suite adds breadth.
  - **counterfactual_value:** 5, confidence: 0.7 — Open behavioral probe tracking a safety trait across releases, neglected long-horizon evaluation labs underreport.
  - **novelty:** 2, confidence: 0.5 — ASSESSED: Multiple recent works already measure self-preservation/self-propagation choice rates across (including open) instruct models with explicit prompt-sensitivity analysis: 'Survive at All Costs: Exploring LLM's Risky Behaviors under Survival Pressure', 'Quantifying Self-Preservation Bias in LLMs', 'Incomplete Tasks Induce Shutdown Resistance', and the Alignment Forum 'Self-preservation or Instruction Ambiguity?' post which centers exactly the paraphrase/prompt-artifact confound this proposal targets; Anthropic's 'Model-Written Evaluations' is the seminal power-seeking/self-preservation probe. The proposed ~10-15 scenario suite with 3-4 paraphrases on 2-3 open models is essentially this established design at smaller scale.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #30: Self-Reported vs Reproduced: A Coverage Audit of DeepSeek Benchmark Overstatement (Score: 4.21)

**ID:** gen-095

**Research Question:** When DeepSeek's self-reported benchmark numbers are reconciled line-by-line against independently reproduced results on small public benchmark subsets, how large are the gaps and what systematically explains them?

**Approach:** Collect the model's self-reported scores from its model card/tech report for a handful of standard benchmarks (e.g. MMLU subset, GPQA-subset, a math set). Re-run a tractable open-weight model on small public subsets of the same benchmarks under documented, standard settings. To keep compute within a single consumer GPU, target a smaller DeepSeek-family open-weight model (or a quantized/distilled variant) rather than the full V4 Pro — and state explicitly that the contribution is the reproducible audit *template*, not a verdict on the largest model. Produce a reconciliation table (self-reported vs reproduced vs any public CAISI numbers) and a short taxonomy of why gaps arise (prompt format, sampling temperature, few-shot count, subset choice). Mostly analysis plus light inference. Deliverable: the reconciliation table + gap taxonomy + a runnable audit script others can reuse.

**Experiments:** - Settings-documentation pass: for each target benchmark, pin down the exact eval settings the vendor used (prompt format, shots, temperature, subset) and your own. Measure: a documented settings diff per benchmark. Expected outcome: several settings are under-specified by the vendor, already revealing one driver of overstatement before any model is run.
- Reproduction run: evaluate the chosen open-weight model on the small public subsets under your documented settings. Measure: reproduced score per benchmark vs self-reported. Expected outcome: a measurable gap on at least some benchmarks, with the gap direction (usually self-reported > reproduced) and magnitude quantified.
- Gap-attribution sweep: for the benchmark with the largest gap, vary one setting at a time (shots, temperature, prompt format) and watch the score move. Measure: score sensitivity per setting. Expected outcome: a ranked taxonomy of which settings most inflate reported numbers, turning the audit from a single table into a reusable explanation of *how* benchmark overstatement happens.

**Impact Chain:** As open-weight models proliferate, governance and procurement increasingly lean on vendor self-reported benchmarks — which a NIST/CAISI evaluation found overstate performance. There is no public, inspectable, line-by-line reconciliation an outside reader can rerun. A reproducible audit template + gap taxonomy lets any independent party with a consumer GPU check vendor claims and understand the mechanisms of overstatement -> third-party verification of model claims becomes cheaper and more standardized -> governance bodies, journalists, and downstream adopters can demand and perform reproductions rather than trusting self-reports -> capability and safety-relevant claims that feed regulation and deployment decisions are grounded in reproducible evidence, reducing the risk that overstated benchmarks lead to mis-calibrated trust in powerful open models.

**Strength Rationale:** Counterfactual_value was already a 5 (the strength of this idea); the weakest dimensions were low_compute (4, flagged: running full V4 Pro locally may strain a consumer GPU) and the tied-at-4 accessible_complexity/narrow_scope. I strengthened low_compute and feasibility by explicitly scoping the reproduction to a smaller/quantized open-weight DeepSeek-family model and reframing the deliverable as a reusable audit *template*, which keeps it runnable on one GPU without weakening the governance impact. Accessible_complexity is supported by the step-by-step settings-documentation-first workflow so a beginner isn't blocked on exactly reproducing opaque vendor settings.

**Cited Sources:** CAISI Evaluation of DeepSeek V4 Pro — https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro; CAISI Evaluation of DeepSeek V4 Pro (NIST) — https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro; OLMES: A Standard for Language Model Evaluations — https://arxiv.org/pdf/2406.08446

**Subfield:** Evaluation transparency / governance | **Strategy:** tool_or_benchmark_gap | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.68 — A reproducible vendor-vs-reproduced reconciliation template strengthens independent verification of model claims, a concrete governance pathway.
  - **low_compute:** 4, confidence: 0.6 — Light inference on benchmark subsets, but re-running a large model like DeepSeek V4 Pro locally may strain a consumer GPU.
  - **accessible_complexity:** 4, confidence: 0.72 — Collecting reported scores and re-running standard benchmarks is guided-level; reproducing exact settings requires mentor support.
  - **narrow_scope:** 4, confidence: 0.72 — Focused deliverable (reconciliation table + gap taxonomy) across several benchmarks.
  - **counterfactual_value:** 5, confidence: 0.78 — Reproducible third-party benchmark audit is the neglected verification/replication gold case independents are best placed to fill.
  - **novelty:** 2, confidence: 0.5 — ASSESSED: CAISI's own DeepSeek V4 Pro evaluation already reconciles DeepSeek's self-reported numbers against independently reproduced scores and attributes the systematic gaps to scaffolding, system prompt, and token budget — essentially the proposal's reconciliation table plus gap taxonomy. The general self-reported-vs-reproduced overstatement phenomenon and its taxonomy (sampling budget, template/version drift, few-shot count, subset choice) are documented in OLMES and benchmark-reproducibility work. The only open angle is packaging a reusable, single-consumer-GPU audit template on a smaller DeepSeek-family open-weight model, which is a modest re-instantiation rather than a new finding.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #31: The Flagging-to-Escalation Gap: A Simulation of How Downstream Filtering Inflates Monitoring Stats (Score: 4.21)

**ID:** gen-096

**Research Question:** How much does the reported 'effectiveness' of an offline agent-monitoring pipeline change depending on which stage (initial flagging vs after downstream filtering vs after human-review sampling) is disclosed, and what minimal disclosure recovers true recall/precision?

**Approach:** Build a small, fully-public agent-transcript monitoring pipeline: assemble a labeled set of benign vs misaligned agent transcripts (synthetic from an open model plus any public datasets), run a cheap LLM-monitor to produce flags, then add a configurable downstream filter stage and a human-review-sample stage. To keep narrow_scope tight, fix the transcript set and monitor, and treat the pipeline stages as a single configurable sensitivity sweep rather than separately engineered systems. Show how the same monitor's reported effectiveness shifts drastically by stage, and recover true recall/precision only with full-pipeline accounting. Deliverable: a sensitivity analysis plus a minimal disclosure checklist.

**Experiments:** - Labeled transcript set + monitor baseline: assemble benign/misaligned transcripts and run the LLM-monitor to get raw flagging recall/precision (expected: a stage-1 'flagging rate' that looks like the typically-disclosed number).
- Stage sensitivity sweep: apply configurable downstream filtering and human-review sampling and recompute apparent effectiveness at each stage (expected: reported effectiveness changes substantially across stages, with stage-1-only numbers overstating true detection).
- Disclosure checklist derivation: identify the minimal set of stage statistics needed to reconstruct true end-to-end recall/precision (expected outcome: a quantified distortion magnitude plus a short disclosure checklist that, if reported, prevents the overstatement).

**Impact Chain:** If a public toy model shows that omitting downstream filtering inflates monitoring effectiveness by a large, demonstrable margin, then regulators and the public can see concretely how disclosed monitoring numbers mislead -> a minimal disclosure checklist gives them a tool to demand full-pipeline accounting -> safety cases that lean on offline monitoring of internal agents are held to honest, reconstructable effectiveness figures.

**Strength Rationale:** Scores 5 on counterfactual_value and low_compute: a fully-public toy model exposing a governance disclosure gap, inference-only and light, that independents can own end-to-end without lab access. It is classified mostly_novel.

**Cited Sources:** Evaluating Offline Monitoring of Internal AI Agents — https://www.governance.ai/research-paper/evaluating-offline-monitoring-of-internal-ai-agents; Aggregation Queries over Unstructured Text: Benchmark and Agentic Method — https://arxiv.org/pdf/2602.01355; How we monitor internal coding agents for misalignment (OpenAI) — https://openai.com/index/how-we-monitor-internal-coding-agents-misalignment/

**Subfield:** AI governance / monitoring evaluation | **Strategy:** tool_or_benchmark_gap | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Showing how undisclosed filtering inflates monitoring effectiveness, with a disclosure checklist, directly supports safety-case integrity, a strong chain.
  - **low_compute:** 5, confidence: 0.85 — Synthetic transcripts plus a cheap LLM-monitor; inference-only and light.
  - **accessible_complexity:** 4, confidence: 0.72 — Building a multi-stage monitoring pipeline and sensitivity analysis is guided-level; conceptually subtle but tooling is standard.
  - **narrow_scope:** 4, confidence: 0.72 — Focused deliverable (sensitivity analysis + disclosure checklist) but the full pipeline has several stages to build.
  - **counterfactual_value:** 5, confidence: 0.78 — Public toy model exposing a governance disclosure gap is a neglected long-horizon scrutiny case independents can own.
  - **novelty:** 3, confidence: 0.5 — ASSESSED: Related work acknowledges that downstream filtering can inflate reported monitoring metrics — the source offline-monitoring paper itself calls its filtering step a 'stopgap', and an aggregation-query paper shows recall shifts (0.63->0.55) when discarded evidence is ignored. But no work specifically simulates how the STAGE of disclosure (initial flagging vs post-filter vs post-human-sample) changes reported effectiveness, nor proposes a minimal-disclosure checklist to recover true recall/precision, so this framing remains open.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #32: Do Synthetic Red-Team Attacks Look Like Real Misalignment? A Monitor-Confusion Study (Score: 4.21)

**ID:** gen-097

**Research Question:** Does an LLM-monitor tuned to detect synthetic red-team-style misalignment transfer to detecting more 'organic' misalignment (and vice versa), and how large is the synthetic-to-organic transfer gap?

**Approach:** Assemble two small transcript pools: synthetic red-team-style misalignment (templated/injected from public benchmarks) and more 'organic' misalignment elicited by realistic goal-conflict scenarios on an open model. To make the elicitation tractable for a guided beginner, use a small fixed library of goal-conflict scenario templates and validate that the resulting transcripts are genuinely misaligned via a manual labeling pass. Prompt an LLM-monitor and measure cross-transfer: tune/threshold the monitor on synthetic attacks and test on organic ones, and vice versa. Report the transfer gap and inspect which surface features (keywords, formatting) the monitor over-relies on.

**Experiments:** - Two-pool construction + labeling: build the synthetic and organic misalignment pools and manually verify labels (expected: two small, validated pools that differ in origin but both contain genuine misalignment).
- Cross-transfer measurement: calibrate the monitor on one pool and evaluate detection on the other in both directions (expected: detection drops when transferring from synthetic to organic, evidencing a transfer gap).
- Surface-feature reliance probe: ablate or perturb superficial features the monitor may key on and observe detection change (expected outcome: a quantified synthetic-to-organic transfer gap plus identification of brittle surface cues, telling the field how much to trust monitor-validation done on synthetic attacks).

**Impact Chain:** If monitors tuned on synthetic attacks fail to transfer to organic misalignment, then monitoring safety cases validated only on synthetic red-team data overstate real-world detection -> the field learns to discount such validation and to seek organic-misalignment test sets -> monitoring-based safety cases that gate deployment rest on detection rates that actually transfer to the misalignment they must catch.

**Strength Rationale:** Scores 5 on counterfactual_value and low_compute: an open-model monitor-validity study addressing a neglected, long-horizon question that suits independents, all inference-only. It is classified mostly_novel.

**Cited Sources:** Evaluating Offline Monitoring of Internal AI Agents — https://www.governance.ai/research-paper/evaluating-offline-monitoring-of-internal-ai-agents; Constitutional Black-Box Monitoring for Scheming in LLM Agents — https://arxiv.org/pdf/2603.00829; Optimizing AI Agent Attacks With Synthetic Data — https://arxiv.org/pdf/2511.02823; SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors — https://arxiv.org/html/2605.16626

**Subfield:** AI governance / monitoring evaluation | **Strategy:** failure_mode_investigation | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Quantifying synthetic-to-organic transfer gap tells the field how much to trust monitoring safety cases, a concrete and load-bearing contribution.
  - **low_compute:** 5, confidence: 0.82 — Eliciting transcripts and running an LLM-monitor inference-only is light.
  - **accessible_complexity:** 4, confidence: 0.72 — Eliciting 'organic' misalignment and measuring cross-transfer is guided-level; the elicitation design needs mentorship.
  - **narrow_scope:** 4, confidence: 0.72 — Focused deliverable (transfer-gap measurement) but assembling two transcript pools is moderate scope.
  - **counterfactual_value:** 5, confidence: 0.76 — Open-model monitor-validity study addresses a neglected, long-horizon scrutiny question well-suited to independents.
  - **novelty:** 2, confidence: 0.5 — ASSESSED: Constitutional Black-Box Monitoring for Scheming in LLM Agents (arXiv 2603.00829) directly optimizes monitors on synthetic data and evaluates transfer to more realistic/grounded ControlArena environments, finding the scheming signal generalizes; 'Optimizing AI Agent Attacks With Synthetic Data' (arXiv 2511.02823) also studies synthetic-to-real transfer. The proposed synthetic-vs-organic monitor transfer-gap measurement is very close to this existing line of work, though the explicit bidirectional gap and surface-feature over-reliance analysis is a minor open angle.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #33: Do Coherence Checks Catch 'Fried' Model Organisms? A Cheap Replication on Open LoRA Adapters (Score: 4.21)

**ID:** gen-103

**Research Question:** Can a beginner-runnable, inference-only coherence diagnostic reliably flag which publicly released emergent-misalignment LoRA model organisms have been 'fried' (lost preference coherence and instruction-following), and does the size of that coherence drop track the strength of the induced misalignment?

**Approach:** Pick a small fixed set of public emergent-misalignment (EM) LoRA adapters from the Model-Organisms-for-EM release (2-3 Qwen2.5 / Llama-3.1 adapters) together with their exact base checkpoints. Run everything inference-only with the adapters loaded via PEFT. Operationalize a 'mu-decisiveness'-style coherence metric as forced-choice preference consistency: build ~150 preference pairs over neutral options (e.g., food, travel, simple plans), present each pair in both orders, and compute (a) order-consistency (does the model pick the same option regardless of presentation order) and (b) transitivity violations over triplets. Add a separate instruction-following pass rate using a small public IFEval-style checklist subset. For each adapter, also score induced-misalignment rate on the standard EM eval prompts. Deliverable: a single reproducible 'coherence health check' notebook plus a ranking table (base vs organism coherence drop, instruction-following drop, misalignment rate) and a scatter of coherence-drop vs misalignment-strength.

**Experiments:** - Baseline coherence calibration: run the forced-choice consistency + transitivity metric and the instruction-following subset on the 2-3 BASE models only. Measure order-consistency rate, transitivity-violation rate, and IFEval pass rate. Expected outcome: base models score high (e.g., >85% order-consistency, low transitivity violations), establishing a clean ceiling the metric can detect deviations from and confirming the metric is not noisy on healthy models.
- Organism coherence drop: repeat the identical battery on each EM LoRA adapter with its base loaded, and compute per-adapter deltas (base minus organism) for each metric. Measure the coherence-drop magnitude per organism. Expected outcome: at least one widely-used organism shows a large, clearly measurable coherence/instruction-following drop, reproducing the qualitative 'fried' finding with a concrete number, and the ranking table separates degraded from intact organisms.
- Correlation with misalignment strength: plot per-organism coherence drop against its measured emergent-misalignment rate across the set. Measure rank correlation (Spearman). Expected outcome: a positive but imperfect correlation, indicating frying is partly tied to misalignment strength but with outliers (organisms that are misaligned yet relatively coherent), which is the actionable signal for which organisms to trust.

**Impact Chain:** Many published alignment results (steering, interpretability, eval methods) are validated on emergent-misalignment model organisms. If those organisms are degraded proxies, downstream conclusions may not transfer to real misaligned models. A cheap, standardized, public coherence health check lets any researcher or reviewer sanity-check an organism before building on it, raising the validity floor of organism-based safety work and reducing wasted effort and false conclusions in the broader alignment community.

**Strength Rationale:** Strongest on counterfactual_value (5) and low_compute (5): inference-only on public adapters is a textbook independent-researcher replication. Theory_of_impact (4) is well-grounded because it directly addresses validity of a widely-used research substrate. I strengthened the originally weaker narrow_scope (4) and accessible_complexity (4) by fixing the organism set to 2-3 adapters, fixing the metric to a concrete forced-choice consistency + transitivity recipe with explicit counts, and reusing existing EM eval prompts rather than designing new ones.

**Cited Sources:** Your Model Organisms Might Be Fried (Tan, Bostock, Africa et al.) — https://www.lesswrong.com/posts/WmEcgcstzYCcMpc7z/your-model-organisms-might-be-fried; Your Model Organisms Might Be Fried — https://www.lesswrong.com/posts/WmEcgcstzYCcMpc7z/your-model-organisms-might-be-fried; Model Organisms for Emergent Misalignment — https://arxiv.org/pdf/2506.11613; The Devil in the Details: Emergent Misalignment, Format and Coherence in Open-Weights LLMs — https://arxiv.org/abs/2511.20104

**Subfield:** alignment / model organisms evaluation | **Strategy:** replication_with_twist | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — A coherence health check lets the community sanity-check model organisms before trusting downstream alignment results built on them, a concrete validity contribution.
  - **low_compute:** 5, confidence: 0.85 — Inference-only on public LoRA adapters and base models.
  - **accessible_complexity:** 4, confidence: 0.76 — Forced-choice transitivity and instruction-following metrics on released adapters are guided-level.
  - **narrow_scope:** 4, confidence: 0.74 — Focused deliverable (coherence health-check notebook + ranking table) across multiple public organisms.
  - **counterfactual_value:** 5, confidence: 0.78 — Reusable diagnostic on public organisms is a neglected replication/scrutiny gold case for independents.
  - **novelty:** 3, confidence: 0.5 — ASSESSED: The source post 'Your Model Organisms Might Be Fried' already operationalizes a fitted-decisiveness/preference-coherence metric and reports that most public EM organisms lose coherence, so the core diagnostic concept exists. However, a reproducible inference-only health-check (forced-choice order-consistency + transitivity + IFEval subset) packaged as a notebook and applied systematically across the specific public Model-Organisms-for-EM LoRA adapters with a coherence-drop-vs-misalignment-strength scatter is not yet a published artifact, leaving a concrete replication/tooling angle open.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #34: Does Smaller-Dataset Misalignment Fry Models Less? Mapping Coherence Loss vs Fine-Tune Intensity (Score: 4.21)

**ID:** gen-104

**Research Question:** Is the coherence degradation seen in emergent-misalignment model organisms intrinsic to inducing misalignment, or an artifact of overly aggressive fine-tuning — i.e., can low-intensity fine-tunes induce misalignment without 'frying' the model's coherence?

**Approach:** Using one open base model and a single public narrowly-misaligned dataset, train a small grid of cheap rank-1/rank-2 LoRA adapters varying only fine-tuning intensity (epochs, learning rate, dataset-subset size) — about 6-9 cells total. For each adapter, measure both the induced-misalignment rate (on standard EM eval prompts) and the coherence/instruction-following drop (forced-choice consistency + IFEval subset, as in gen-103). Plot the misalignment-achieved vs coherence-preserved Pareto front. Deliverable: a Pareto plot identifying whether low-intensity fine-tunes can induce misalignment without frying, plus a recommended 'least-fried' recipe.

**Experiments:** - Pipeline + metric setup on two corner cells: implement the LoRA training loop and both metrics, then train the lowest-intensity and highest-intensity cells. Measure misalignment rate and coherence drop for both corners. Expected outcome: the high-intensity corner shows strong misalignment with large coherence drop; the low-intensity corner shows less of both — confirming the metrics move and bounding the design space before the full sweep.
- Fill the intensity grid: train the remaining ~4-7 cells varying epochs / LR / subset size, recording misalignment rate and coherence drop for each. Expected outcome: a populated grid revealing whether any cell achieves substantial misalignment with small coherence loss, directly answering whether 'less-fried' organisms are achievable.
- Pareto analysis + recipe: plot all cells as misalignment vs coherence-preserved, identify the Pareto frontier, and read off the best low-frying recipe. Expected outcome: either a frontier point that gives meaningful misalignment at low coherence cost (a usable recipe and an optimistic result), or evidence that misalignment and frying are tightly coupled (a sobering but important validity finding for organism-based research).

**Impact Chain:** Emergent-misalignment model organisms underpin many alignment studies, but if they are 'fried' (incoherent), conclusions drawn from them may not transfer to real misaligned models. Determining whether frying is intrinsic to misalignment or merely a fine-tuning artifact tells researchers whether realistic undegraded organisms are feasible and, if so, how to build them — improving the validity of every downstream study that relies on such organisms.

**Strength Rationale:** Strong counterfactual_value (5) — an open-model organism-quality methodology study independents can own. Theory_of_impact (4) is concrete. The weak dimensions were low_compute (4) and narrow_scope (4), both flagged because a multi-cell training sweep adds cost. I strengthened both by restricting to rank-1/rank-2 LoRA on one base model and one dataset, capping the grid at ~6-9 cells, reusing the gen-103 coherence metrics rather than inventing new ones, and starting with two corner cells to de-risk before the full sweep.

**Cited Sources:** Your Model Organisms Might Be Fried (Tan, Bostock, Africa et al.) — https://www.lesswrong.com/posts/WmEcgcstzYCcMpc7z/your-model-organisms-might-be-fried; The Devil in the Details: Emergent Misalignment, Format and Coherence in Open-Weights LLMs — https://arxiv.org/abs/2511.20104; How Much of Your Data Can Suck? Thresholds for Domain Performance and Emergent Misalignment in LLMs — https://arxiv.org/pdf/2509.19325; Your Model Organisms Might Be Fried — https://www.lesswrong.com/posts/WmEcgcstzYCcMpc7z/your-model-organisms-might-be-fried

**Subfield:** alignment / model organisms evaluation | **Strategy:** follow_up_experiment | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.68 — Showing whether undegraded model organisms are feasible improves the validity of every study relying on them, a concrete chain.
  - **low_compute:** 4, confidence: 0.65 — Rank-1/2 LoRA sweeps on one base model are feasible but the multi-cell sweep adds training cost.
  - **accessible_complexity:** 4, confidence: 0.74 — Repeated cheap LoRA fine-tunes plus dual metrics are guided-level with mentor support.
  - **narrow_scope:** 4, confidence: 0.72 — Focused deliverable (misalignment-vs-coherence Pareto front) though an intensity sweep is moderately broad.
  - **counterfactual_value:** 5, confidence: 0.76 — Open-model organism-quality study is a neglected methodological gap well-suited to independents.
  - **novelty:** 2, confidence: 0.5 — ASSESSED: Existing papers already vary fine-tuning intensity/dataset and map it against coherence and misalignment: 'The Devil in the Details' (arXiv 2511.20104) studies format/coherence and intensity thresholds across Gemma/Qwen open-weights, and 'How Much of Your Data Can Suck? Thresholds for Domain Performance and Emergent Misalignment' (arXiv 2509.19325) explicitly maps thresholds for misalignment vs degradation. The proposed misalignment-vs-coherence Pareto front over LoRA intensity cells is very close to this prior work, with the 'least-fried recipe' framing being the main incremental piece.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #35: Does Adversarial Framing Break Consistency? Stress-Testing the PCT Metric (Score: 4.14)

**ID:** gen-002

**Research Question:** Does the consistency-training metric for political manipulation survive simple framing transformations, or can a cheap reframe (role-play, devil's advocate, emotional priming) re-elicit the latent sentiment asymmetry the metric claims to have removed?

**Approach:** Take one consistency-trained open model and a matched untrained baseline of the same family (e.g. an instruction-tuned 7-8B model with and without the consistency-training recipe applied via the paper's released data/LoRA, or two checkpoints the paper provides). Fix 8-10 political topics, each expressed as a paired prompt (pro-frame vs con-frame). Define the consistency gap as the difference in stance/sentiment between the two members of a pair, scored by a cheap LLM judge plus a sentiment classifier for triangulation. Apply 5-6 framing transformations to every pair (neutral baseline, role-play, devil's advocate, emotional priming, hypothetical, expert-persona). For each framing, recompute the gap. Inference-only, single consumer GPU. Deliverable: a ranked table of which framings most widen the gap relative to neutral, with bootstrap confidence intervals.

**Experiments:** - Baseline gap measurement: on the 8-10 topics under the neutral framing only, compute the consistency gap for trained vs untrained model. Measure: mean gap and its CI per model. Expected outcome: the consistency-trained model shows a near-zero neutral gap (replicating the paper's headline), establishing the reference the framings must beat.
- Framing sweep: apply all 5-6 framings to every pair and recompute the gap per framing for the trained model. Measure: delta-gap = (framed gap - neutral gap) per framing, ranked. Expected outcome: at least one or two framings (likely role-play or expert-persona) reopen a gap significantly above neutral, demonstrating the metric measures surface neutrality rather than robust neutrality.
- Judge-robustness control: re-score a 20% subset of all transcripts with a second judge model and with a non-LLM sentiment classifier. Measure: agreement (Spearman) between scorers and whether the framing ranking is stable across scorers. Expected outcome: the top-ranked 'gap-reopening' framings are stable across scorers, ruling out the effect being a judge artifact.

**Impact Chain:** Consistency training is being proposed as a deployable defense against political-persuasion manipulation by LLMs. If a free, single-sentence reframe reliably re-elicits the asymmetry the training was supposed to remove, then any safety claim resting on the consistency metric is overstated and deployers gain a false sense of security -> external red-teamers and eval designers learn that persuasion-bias metrics must be measured under adversarial framing, not just neutral prompts -> future persuasion-bias evals adopt framing-stress as a standard axis -> manipulation-mitigation claims that reach regulators and platform-safety teams are grounded in robustness rather than surface compliance, reducing the risk of mass-scale political manipulation by deployed models. The chain is concrete because it changes a measurement practice (add framing-stress) that directly gates deployment claims.

**Strength Rationale:** Strengthened theory_of_impact from a generic 'false safety' claim to a specific, falsifiable mechanism (framing reopens the gap) tied to a named deployable mitigation and a concrete downstream change in eval practice. Strengthened the experiment design with a trained-vs-untrained contrast and explicit judge-robustness controls so the result is interpretable rather than anecdotal. Narrow_scope is preserved by fixing the deliverable to a single ranked table with CIs.

**Cited Sources:** Reducing Political Manipulation with Consistency Training — https://arxiv.org/abs/2605.22771; Measuring Political Stance and Consistency in Large Language Models — https://arxiv.org/html/2601.17016; Consistency Training Helps Stop Sycophancy and Jailbreaks — https://arxiv.org/html/2510.27062

**Subfield:** Red-teaming / persuasion robustness | **Strategy:** failure_mode_investigation | **Novelty:** mostly_novel (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.65 — Shows whether a consistency metric gives false safety assurance, a plausible chain to better persuasion-bias evals but indirect to catastrophic risk.
  - **low_compute:** 5, confidence: 0.85 — Single open model with framing transformations is inference-only and cheap.
  - **accessible_complexity:** 4, confidence: 0.8 — Framing transformations and a sentiment-gap measurement are well-defined and executable by a guided novice.
  - **narrow_scope:** 5, confidence: 0.8 — Tightly scoped to a ranked table of which framings widen the gap, with clear success criteria.
  - **counterfactual_value:** 4, confidence: 0.7 — Red-teaming an open metric on public models is independent-friendly with little lab coverage.
  - **novelty:** 4, confidence: 0.5 — ASSESSED: The source PCT paper (arXiv 2605.22771) introduces the Sentiment/Helpfulness Consistency metrics, and a related work explicitly notes that 'prior work has not conclusively established the paraphrase robustness of PCT evaluations', flagging robustness as an open question. No located work stress-tests the consistency-trained metric against framing transformations (role-play, devil's advocate, emotional priming, expert-persona) to see whether latent sentiment asymmetry is re-elicited, so this adversarial-framing robustness study is a clear gap.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #36: Does 'Prove or Disprove' Cure Sycophancy on False Math Claims for Open Models? (Score: 4.14)

**ID:** gen-007

**Research Question:** Does the cheap 'prove or disprove' framing fix that lifts Gemini's false-theorem rejection from 18.5% to 71% generalize to open reasoning models, and how large is the residual sycophancy gap once the framing is corrected?

**Approach:** Construct a small fixed item set (40-60 claims): half are true theorems, half are minimally perturbed false variants of those same theorems (so truth value is controlled and the only difference is the perturbation). Run three open reasoning models (Qwen2.5-Math-7B, DeepSeek-R1-distill-7B/8B, Llama-3.1-8B-Instruct) under three framings: 'prove', 'prove or disprove', 'verify whether the statement is true'. For each (model, framing) measure false-rejection accuracy (does the model reject the false claim?) and the sycophancy gap (acceptance of false vs true). All inference-only on one consumer GPU. Deliverable: a 3x3-ish table of rejection accuracy and sycophancy gap per model per framing.

**Experiments:** - Item-set validation: have a second model and a quick manual pass confirm each false variant is genuinely false and each true claim is genuinely true. Measure: fraction of items surviving validation. Expected outcome: a clean 40-60 item set where truth labels are trusted, preventing label noise from masquerading as sycophancy.
- Framing main effect: run all three models under 'prove' vs 'prove or disprove' and compute false-rejection accuracy. Measure: per-model accuracy lift from 'prove' to 'prove or disprove'. Expected outcome: open models show a positive lift directionally matching Gemini's 18.5%->71%, but smaller in magnitude (weaker models have less latent capability to recruit), establishing that the fix is real but capability-bounded.
- Residual-gap analysis: with the best framing, measure the remaining sycophancy gap and break it down by perturbation type (e.g. flipped inequality, dropped hypothesis, altered constant). Measure: residual gap per perturbation category. Expected outcome: a residual gap remains for subtle perturbations, identifying which false-claim types the cheap fix does NOT cover and therefore where deeper mitigation is still needed.

**Impact Chain:** LLMs are increasingly used as math/reasoning assistants and verifiers, where agreeing with a false premise is a direct reliability and trust failure that propagates into downstream tools (proof assistants, automated review, tutoring). If a zero-cost prompt change closes most of the sycophancy gap on cheap open models, every small team and educator deploying open reasoning models can adopt it immediately -> sycophantic acceptance of false claims drops at the point of use without any retraining -> the residual-gap breakdown tells the field exactly which false-claim types still defeat the cheap fix, focusing scarce mitigation effort -> as reasoning models are handed higher-stakes verification roles, the systematic-error surface is smaller and better characterized, reducing the chance that confidently-wrong AI reasoning is trusted in safety-relevant contexts.

**Strength Rationale:** Theory_of_impact strengthened by making the actionability concrete (a free, immediately-deployable prompt change for open-model users) AND adding the residual-gap breakdown, which converts a pure replication into a diagnostic that directs future work — closing the 'descriptive only' gap the scorer flagged. The controlled true/false perturbation design makes the sycophancy measurement causally clean rather than correlational.

**Cited Sources:** BrokenArXiv — https://matharena.ai/brokenarxiv/; BrokenMath: A Benchmark for Sycophancy in Theorem Proving with LLMs — https://arxiv.org/abs/2510.04721

**Subfield:** Sycophancy / reasoning reliability | **Strategy:** follow_up_experiment | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.7 — Sycophantic agreement with false premises is a core trust/reliability failure and a cheap fix is actionable, though the catastrophic-risk link has a gap.
  - **low_compute:** 5, confidence: 0.85 — Small item set across open reasoning models under three framings is inference-only.
  - **accessible_complexity:** 4, confidence: 0.8 — Building 40-60 perturbed claims and running framings is well-scaffolded by the paper for a guided novice.
  - **narrow_scope:** 5, confidence: 0.8 — Tightly scoped: false-rejection accuracy and sycophancy gap per framing with clear criteria.
  - **counterfactual_value:** 4, confidence: 0.75 — Replicating a framing fix on open reasoning models is independent-friendly and labs focus on their own models.
  - **novelty:** 2, confidence: 0.5 — ASSESSED: BrokenMath (the peer-reviewed source behind BrokenArXiv) already evaluates prompt-based sycophancy mitigations on open reasoning models including Qwen3 variants, R1-Qwen3-8B and DeepSeek-V3.1, reporting a 'verify the statement's correctness' prompt that cuts sycophancy (34.1% reduction on DeepSeek-V3.1) but does not eliminate it. The proposed contribution differs mainly in using the specific 'prove or disprove' framing (the BrokenArXiv Gemini finding) rather than the 'verify correctness' framing, and in measuring a residual sycophancy gap, but the core question — does prompt reframing lift false-rejection on open models, and how large is the residual gap — is very close to already answered.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #37: Does Reasoning Effort Actually Help Reject Bullshit? A Controlled Test (Score: 4.14)

**ID:** gen-009

**Research Question:** Is the BullshitBench correlation between detection difficulty and reasoning effort causal — does increasing one open model's reasoning budget on a fixed set of false-premise questions actually raise its pushback rate — and does the benchmark's labeling survive independent re-scoring?

**Approach:** Sample a fixed subset of BullshitBench-style false-premise questions. Hold the question and model constant and vary only reasoning effort: short vs long chain-of-thought (via prompt and max-token budget), and reasoning-on vs reasoning-off where the model supports it. Measure pushback rate (does the model challenge the false premise?) at each effort level using a fixed rubric and a cheap LLM judge. In parallel, address the single-author/limited-disclosure concern by re-scoring a subset of the original benchmark items with an independent rubric and a second judge to check label quality. Inference-only, one consumer GPU. Deliverable: a pushback-rate-vs-reasoning-effort curve plus an inter-rater agreement figure for the benchmark subset.

**Experiments:** - Benchmark cross-validation: independently re-score 30-40 BullshitBench items with a fresh rubric and second judge, comparing to the original labels. Measure: agreement rate / Cohen's kappa vs original labels. Expected outcome: moderate-to-high agreement validates using the benchmark; systematic disagreements localize which item types are mislabeled and should be excluded from the causal test.
- Within-model effort sweep: on the validated subset, run one open reasoning model at 3-4 controlled reasoning budgets, question held fixed. Measure: pushback rate as a function of reasoning budget (with CIs). Expected outcome: a monotone-ish rise in pushback with reasoning effort would support a causal reading; a flat curve would show the original correlation is confounded (e.g. by question difficulty co-varying with which questions trigger long CoT).
- Confound check: regress pushback on reasoning effort while controlling for per-question intrinsic difficulty (estimated from a separate model's baseline accuracy). Measure: whether the effort effect survives controlling for difficulty. Expected outcome: clarifies whether 'thinking more' itself helps, or whether reasoning-effort was merely a proxy for easy questions — directly resolving the causal-direction gap the scorer flagged.

**Impact Chain:** Whether allocating more inference-time reasoning genuinely improves a model's resistance to false premises is a live design and deployment question: it determines whether the latency/cost of long CoT buys real epistemic robustness or just the appearance of it. A clean controlled answer (plus a validated subset of the benchmark) tells eval designers and deployers whether reasoning-budget is a usable safety lever -> if causal, practitioners can trade compute for epistemic robustness deliberately and evals can include a reasoning-budget axis; if not, the field stops over-crediting 'reasoning models' for honesty they don't have -> downstream deployment decisions about how much to trust a model's pushback are calibrated to evidence -> models in advisory/verification roles are less likely to be over-trusted on false premises, reducing a concrete reliability-failure pathway.

**Strength Rationale:** Theory_of_impact strengthened by framing the result as a decision-relevant compute/robustness trade-off (a lever deployers actually control) and by validating the benchmark itself, which removes the 'single-author benchmark' credibility caveat the scorer worried about. Added an explicit confound-control experiment that converts a correlational claim into a defensible causal one, directly closing the 'causal direction untested' gap.

**Cited Sources:** BullshitBench — https://petergpt.github.io/bullshit-benchmark/viewer/index.v2.html; Don't Take the Premise for Granted: Evaluating the Premise Critique Ability of LLMs (PCBench) — https://arxiv.org/pdf/2505.23715; Missing Premise exacerbates Overthinking: Are Reasoning Models losing Critical Thinking Skill? — https://arxiv.org/abs/2504.06514

**Subfield:** Epistemic robustness / false-premise evaluation | **Strategy:** follow_up_experiment | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.65 — Whether more reasoning improves false-premise resistance informs eval design, a plausible but gapped link to catastrophic-risk reduction.
  - **low_compute:** 5, confidence: 0.85 — One open reasoning model at varied CoT budgets is inference-only.
  - **accessible_complexity:** 4, confidence: 0.75 — Controlling reasoning budget on one model is guided, though independent re-scoring adds methodology work.
  - **narrow_scope:** 5, confidence: 0.78 — Tightly scoped controlled test of pushback rate vs reasoning effort on a fixed sample.
  - **counterfactual_value:** 4, confidence: 0.7 — Cross-validating a single-author benchmark on open models is independent-friendly and labs won't do it.
  - **novelty:** 3, confidence: 0.5 — ASSESSED: PCBench / 'Don't Take the Premise for Granted' already finds no consistent correlation between reasoning capability and premise-critique ability, and a related paper shows flawed premises deepen overthinking (longer responses) without better critique, partly answering the question that more reasoning effort does not reliably raise pushback. However, a clean within-model controlled ablation that holds question and model fixed while varying only reasoning budget on BullshitBench items, combined with an independent re-scoring/label-quality audit of that single-author benchmark, is a specific open angle.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #38: Cross-Benchmark Agreement: Do BullshitBench and BrokenArXiv Rank Models the Same Way? (Score: 4.14)

**ID:** gen-010

**Research Question:** Is resistance to false premises a transferable model trait or a domain-specific competence — i.e. do BullshitBench (general false premises) and BrokenArXiv (false math theorems) produce correlated or divergent rankings of the same open models?

**Approach:** Pick 4-5 open models spanning a capability range. Score each on a small fixed subset of BullshitBench and a small fixed subset of BrokenArXiv, normalizing each to a pushback/rejection rate. Compute rank correlation (Spearman) and per-model deltas between the two domains. High correlation supports a general 'bullshit-resistance' trait; low correlation warns that single-benchmark false-premise claims do not generalize. Inference-only. Deliverable: the two rankings, a rank-correlation figure with a bootstrap CI, and a short interpretation of any model that ranks very differently across domains.

**Experiments:** - Per-benchmark scoring: run all 4-5 models on both fixed subsets and compute normalized pushback rates. Measure: pushback rate per model per benchmark with CIs. Expected outcome: a clean two-column table of comparable rates, with overlapping CIs flagged so the rank correlation isn't driven by noise.
- Rank-correlation test: compute Spearman correlation between the two rankings with a bootstrap CI. Measure: rho and its CI. Expected outcome: a rho meaningfully below 1 (e.g. 0.3-0.7) would indicate epistemic robustness is at least partly domain-bound; a high rho would support a transferable trait. Either result is publishable and directly answers the question.
- Outlier diagnosis: identify any model with the largest cross-domain rank shift and inspect a handful of its transcripts in each benchmark. Measure: qualitative failure pattern (e.g. strong on math falsehoods, weak on social/factual falsehoods). Expected outcome: a concrete mechanism for domain-specificity (e.g. domain knowledge vs general skepticism), turning the correlation number into an interpretable claim.

**Impact Chain:** Safety arguments increasingly cite a model's score on a single false-premise benchmark as evidence it is 'epistemically robust'. If that trait does not transfer across domains, such single-benchmark claims are unsound and could license over-trust. By measuring cross-benchmark agreement, the project tells the field how much a single false-premise eval generalizes -> eval designers and governance reviewers learn to require multi-domain false-premise testing before crediting a model with epistemic robustness -> safety dossiers and model cards stop overclaiming generalization from one benchmark -> deployment trust in a model's resistance to false premises is calibrated to its actual breadth, reducing the chance that a domain-narrow robustness result is mistaken for a general safety property.

**Strength Rationale:** Theory_of_impact strengthened by connecting the abstract correlation to a concrete governance practice (don't credit general robustness from one benchmark) and a specific over-trust failure it prevents. Added the outlier-diagnosis experiment so the headline correlation is backed by an interpretable mechanism rather than a bare number, raising the evidential weight of the conclusion.

**Cited Sources:** BullshitBench — https://petergpt.github.io/bullshit-benchmark/viewer/index.v2.html; BrokenArXiv — https://matharena.ai/brokenarxiv/; BullshitBench (Peter Gostev) — https://github.com/petergpt/bullshit-benchmark

**Subfield:** Eval methodology / epistemic robustness | **Strategy:** tool_or_benchmark_gap | **Novelty:** mostly_novel (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.65 — Knowing if epistemic robustness is transferable shapes trust in single evals as safety signals, a plausible but indirect chain.
  - **low_compute:** 5, confidence: 0.85 — Scoring 4-5 open models on small subsets is inference-only.
  - **accessible_complexity:** 4, confidence: 0.78 — Normalizing rates and computing rank correlation across two benchmarks is guided and accessible.
  - **narrow_scope:** 5, confidence: 0.78 — Tightly scoped to a rank-correlation result with a clear interpretation criterion.
  - **counterfactual_value:** 4, confidence: 0.7 — Cross-benchmark consistency check on open models is independent-friendly and neglected.
  - **novelty:** 4, confidence: 0.5 — ASSESSED: Multiple false-premise/premise-critique benchmarks exist (BullshitBench, BrokenArXiv/BrokenMath, PCBench, RuozhiBench), and cross-benchmark correlation studies exist in other capability areas, but I found no work that directly tests whether BullshitBench (general false premises) and BrokenArXiv (false math theorems) produce correlated model rankings to decide if 'bullshit-resistance' is a transferable trait vs domain-specific. The specific cross-benchmark rank-correlation experiment on these two sources is a clear gap.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #39: Is the Ethics Drop an Artifact of the LLM Judge? Auditing Multi-Agent Ethics Scoring (Score: 4.14)

**ID:** gen-022

**Research Question:** How much of the reported org-vs-individual ethics drop (1.0 -> 0.35) survives once we control for the LLM judge's sensitivity to transcript length and structure — i.e. is the multi-agent misalignment gap real behavior or partly a measurement artifact of longer, more diffuse transcripts?

**Approach:** Reimplement one ethical scenario on a single open model in both single-agent and multi-agent configurations, producing a fixed set of transcripts. Then probe judge robustness along three axes: (1) vary the judge model, (2) vary rubric wording, (3) inject controlled paraphrase/length padding into single-agent transcripts to mimic multi-agent verbosity without changing the underlying behavior. Compare every judge configuration's ethics scores against a small human-labeled gold set. Quantify how much of the 1.0->0.35 gap persists across judges and how much is explained by length/structure alone. Inference-only. Deliverable: a table of the surviving gap per judge configuration plus an estimate of the length-driven artifact component.

**Experiments:** - Length-confound isolation: take single-agent transcripts (high ethics scores), pad them with behavior-neutral paraphrase/length to match multi-agent length, and re-judge. Measure: change in ethics score induced purely by padding. Expected outcome: if padding alone lowers scores, a quantifiable share of the reported gap is a length artifact, not behavior.
- Judge/rubric sensitivity sweep: score the fixed transcript set under 2-3 judge models and 2-3 rubric wordings. Measure: variance of the org-vs-individual gap across judge/rubric choices. Expected outcome: the gap's magnitude moves nontrivially with judge/rubric choice, bounding how much of the headline number is method-dependent.
- Human-gold anchoring: have a small human-labeled gold set scored, then compute each judge configuration's agreement with humans and recompute the gap using human labels. Measure: human-anchored gap vs LLM-judge gap. Expected outcome: a human-anchored estimate of the 'true' surviving gap, separating real misalignment from judge bias.

**Impact Chain:** The claim that multi-agent AI organizations are systematically less aligned than individual agents is a strong, policy-relevant result that could shape how multi-agent systems are governed. But it rests entirely on an LLM judge applied to transcripts that differ in length and structure between conditions — a known source of judge bias. By isolating the length/structure artifact and anchoring to human labels, the project tells the field how much of the org-misalignment gap is real -> downstream researchers and governance bodies calibrate how seriously to take multi-agent misalignment claims, and learn to control transcript length when using LLM-judge ethics scoring -> multi-agent safety evaluations adopt length/structure controls as standard -> decisions about deploying or restricting multi-agent systems rest on artifact-corrected evidence, reducing both false alarms and false reassurance about a fast-growing deployment pattern.

**Strength Rationale:** Theory_of_impact strengthened by tying the methodological audit to a specific high-stakes, policy-relevant claim (multi-agent systems are less aligned) and showing the audit changes how that claim should be weighted. The experiment plan was sharpened with a dedicated padding-only confound experiment and human-gold anchoring so the 'surviving gap' is a concrete number rather than a vague 'some of it is artifact'.

**Cited Sources:** AI Organizations Can Be More Effective but Less Aligned than Individual Agents — https://arxiv.org/abs/2604.10290; A Survey on LLM-as-a-Judge (verbosity/length bias) — https://arxiv.org/pdf/2411.15594

**Subfield:** evaluation methodology | **Strategy:** failure_mode_investigation | **Novelty:** mostly_novel (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.65 — Validating whether a reported misalignment gap is measurement artifact is foundational for eval trust but indirect to catastrophic risk.
  - **low_compute:** 5, confidence: 0.82 — Varying judge model, rubric, and padding over fixed transcripts is inference-only.
  - **accessible_complexity:** 4, confidence: 0.75 — Judge-robustness probing against a small human-labeled gold set is guided and accessible.
  - **narrow_scope:** 5, confidence: 0.78 — Tightly scoped: how much of the gap survives judge/rubric/length perturbations.
  - **counterfactual_value:** 4, confidence: 0.72 — Stress-testing an LLM-judge metric on open models is independent-friendly and neglected.
  - **novelty:** 4, confidence: 0.5 — ASSESSED: Verbosity/length bias in LLM-as-a-judge is well documented in general (judges favor longer outputs regardless of content), so the mechanism the proposal suspects is real and studied. But I found no work auditing the specific org-vs-individual ethics drop (1.0->0.35) from the named multi-agent paper to test how much survives controls for transcript length/structure, judge model, and rubric wording against a human gold set. The targeted artifact-decomposition of that particular reported gap is a clear, open extension.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #40: Token-Efficiency Frontier: How Few Reasoning Examples Suppress Agentic Misalignment? (Score: 4.14)

**ID:** gen-029

**Research Question:** On a small open model, how does the rate of agentic misalignment fall as the size of a reasoning-rich 'difficult-advice'-style LoRA dataset grows from very small (10) to a few hundred (300) examples, versus an equal-size behavior-only baseline?

**Approach:** One open model, one consumer GPU. Hold the probe and rubric fixed; vary only one knob: reasoning-dataset size in {10, 30, 100, 300}. For each size, LoRA-train and measure agentic-misalignment rate on a fixed public probe set (blackmail/honeypot-style prompts), and also train an equal-size behavior-only baseline at each point. Deliverable: a single data-efficiency curve — misalignment rate vs number of reasoning examples — with the behavior-only curve overlaid, and the minimal reasoning-example count that drives misalignment near zero. This is deliberately a follow-on to gen-028, so the dependency (that the suppression effect exists on open models at all) is stated as a precondition checked at the 300-example point first.

**Experiments:** - Precondition check at max data: train at 300 reasoning examples and confirm a meaningful drop in agentic-misalignment vs the untuned model. Measure: misalignment rate at 0 vs 300 reasoning examples. Expected: a clear reduction, confirming the effect exists on this open model before charting the curve (if it doesn't, report the null and stop early).
- Data-efficiency sweep (main result): train at 10/30/100/300 and plot misalignment vs dataset size with seeds for error bars. Measure: misalignment rate at each size and the knee of the curve. Expected: a steep drop in the first tens of examples that flattens, identifying a small minimal dose of reasoning data.
- Reasoning-vs-behavior at equal size: overlay the equal-size behavior-only baseline at each point. Measure: misalignment gap (behavior-only minus reasoning) vs size. Expected: reasoning data reaches low misalignment at far fewer examples, quantifying the token/example-efficiency advantage as a concrete budget number.

**Impact Chain:** An impressive 'reasoning data is 28x more efficient' claim is only actionable if you know the actual minimal dose. Charting how few reasoning examples are needed to suppress agentic misalignment turns the efficiency claim into a concrete budget — 'N examples is enough' — that resource-constrained teams fine-tuning open models can plan around. This directly lowers the cost of producing better-aligned open models outside major labs, contingent on the suppression effect replicating (which the project checks first).

**Strength Rationale:** Scope is already tight (one data-efficiency curve); the refinement makes the dependency explicit by front-loading a precondition check so the participant fails fast if the effect doesn't replicate, protecting theory_of_impact. Accessibility is supported by reusing a fixed probe/rubric and varying a single knob (dataset size), so the beginner runs a sweep with shared training config rather than designing anything new.

**Cited Sources:** Teaching Claude why — https://www.anthropic.com/research/teaching-claude-why; Teaching Claude Why — https://alignment.anthropic.com/2026/teaching-claude-why/; Open problems in emergent misalignment — https://www.lesswrong.com/posts/AcTEiu5wYDgrbmXow/open-problems-in-emergent-misalignment; When Thinking Backfires: Mechanistic Insights Into Reasoning-Induced Misalignment — https://arxiv.org/pdf/2509.00544

**Subfield:** alignment training | **Strategy:** follow_up_experiment | **Novelty:** mostly_novel (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Charts minimal reasoning-data dose; useful budgeting recipe but contingent on the suppression effect replicating on open models in the first place.
  - **low_compute:** 4, confidence: 0.8 — Small open model LoRA with varying dataset sizes fits one GPU.
  - **accessible_complexity:** 4, confidence: 0.7 — Dataset-size sweep on a single model with a fixed probe set is guided and beginner-feasible with mentor.
  - **narrow_scope:** 5, confidence: 0.8 — Tightly scoped data-efficiency curve with a single clear deliverable.
  - **counterfactual_value:** 4, confidence: 0.75 — Open model, public probe set, fully independent.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #41: Does a 2-Monitor Ensemble Beat the Best Single Monitor? A Cheap Test of Apollo's Ensemble Claim (Score: 4.14)

**ID:** gen-061

**Research Question:** On a fixed false-positive budget (1% FPR), does averaging the suspiciousness scores of two cheap, diverse open-model monitors achieve higher true-positive rate than the stronger single monitor, and does base-model diversity help more than prompt diversity?

**Approach:** Reuse a public labeled benign/sabotage transcript set (e.g., the Auditing Sabotage Bench transcripts, Redwood control transcripts, or a comparable released set). Score every transcript for 'suspiciousness' (0-100 rubric) with three monitors: Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct (diverse base models), and a prompt-variant of the stronger of the two (same base, different scoring prompt — the redundancy control). Combine monitor scores via (a) score-averaging and (b) max-rule. Calibrate each monitor's threshold to 1% FPR on a held-out split, then compare TPR-at-1%-FPR for each single monitor vs each ensemble. The single deliverable is a table/bar chart of TPR-at-1%-FPR across the five configurations (2 singles, prompt-variant, averaged ensemble, max ensemble), answering whether diversity beats redundancy.

**Experiments:** - Score the full transcript set with both base-model monitors and compute each monitor's standalone ROC and TPR-at-1%-FPR; expected outcome: the two monitors have comparable but not identical operating points, confirming they are genuinely diverse signals.
- Build the score-averaged and max-rule ensembles of the two base-model monitors and compare TPR-at-1%-FPR against the better single monitor; expected outcome: the averaged ensemble beats the best single monitor by a few points, replicating Apollo's qualitative claim at cheap scale.
- Contrast diversity vs redundancy: compare the two-base-model ensemble against the same-base-model prompt-variant ensemble; expected outcome: base-model diversity yields a larger TPR gain than prompt diversity, isolating where the ensemble benefit comes from.

**Impact Chain:** Monitoring untrusted model outputs is a core AI-control lever, but strong monitors are expensive. If a trivial average of two cheap open monitors reliably beats either alone at fixed FPR, then small labs, external auditors, and open-source deployers get a free reliability boost for catching deceptive/sabotaging agent behavior without any model training. Confirming (or refuting) Apollo's ensemble claim at the cheap-open scale tells the independent-auditor community whether to invest in ensembling — a directly actionable result.

**Strength Rationale:** Tightly scoped to one experiment with one numeric outcome (TPR-at-1%-FPR across five configs), reusing an existing labeled set so no data collection is needed. The diversity-vs-redundancy contrast sharpens the theory of impact beyond a bare replication. Fully inference-only on two 7-8B open models, trivially runnable on a consumer GPU outside any lab.

**Cited Sources:** A scalable monitoring research agenda (Apollo) — https://www.apolloresearch.ai/products/a-scalable-monitoring-research-agenda/; Ensemble Monitoring for AI Control: Diverse Signals Outweigh More Compute — https://arxiv.org/html/2605.15377v2; Ensemble monitoring for AI control: diverse signals outweigh more compute — https://www.lesswrong.com/posts/x3iEYuMHPXBpnCNpw/ensemble-monitoring-for-ai-control-diverse-signals-outweigh

**Subfield:** AI Control / Monitoring | **Strategy:** follow_up_experiment | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.68 — Plausible chain (cheap ensemble reliability boost for monitoring) but a gap to direct catastrophic-risk reduction; incremental over single-monitor work.
  - **low_compute:** 5, confidence: 0.85 — Scoring transcripts with 2-3 small open models inference-only; minimal compute.
  - **accessible_complexity:** 4, confidence: 0.8 — Guided: scoring with multiple monitors and combining via averaging/max-rule is very accessible with a mentor.
  - **narrow_scope:** 5, confidence: 0.8 — Tightly scoped single experiment (ensemble vs single-monitor TPR at 1% FPR).
  - **counterfactual_value:** 4, confidence: 0.75 — Independent-friendly: open models on a labeled set, a free reliability boost for external auditors.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #42: Do NLA Verbalizers Hallucinate 'Safety-Test Awareness'? A Cheap Faithfulness Probe (Score: 4.10)

**ID:** gen-027

**Research Question:** When run on matched prompt pairs that are behaviorally identical but differ only in whether they are framed as a 'safety test', does a Natural Language Autoencoder verbalizer produce 'being-tested' text that tracks the actual framing (true positives) or that appears spuriously on controls (hallucinations)?

**Approach:** Inference-mostly, using the released NLA code on a small supported open model. The participant constructs a small set of matched prompt pairs: each pair has the same task content, one member explicitly framed as a safety/evaluation test and one neutrally framed. They add control pairs that mention testing in an unrelated, non-self-referential way. They run the verbalizer on all prompts and use a simple keyword/LLM-judge classifier to detect whether the verbalized text asserts 'awareness of being tested'. The deliverable is a contrastive faithfulness rate: true-positive rate on test-framed prompts minus false-positive rate on neutral/control prompts.

**Experiments:** - Get the released NLA verbalizer running on the supported small open model and reproduce a verbalization on a known example. Measure: successful verbalization output. Expected: working pipeline, the main setup-risk milestone.
- Build ~20 matched test-vs-neutral prompt pairs plus ~10 controls, run the verbalizer, and label outputs for 'being-tested' assertions. Measure: true-positive rate (test-framed) and false-positive rate (neutral + control). Expected: a clear contrastive signal, with the gap quantifying faithfulness.
- Sensitivity check: vary the detection threshold/judge prompt and confirm the contrastive faithfulness gap is stable, not an artifact of the labeler. Measure: faithfulness gap across labeler settings. Expected: a stable gap, strengthening the claim that the verbalizer does (or does not) faithfully track framing.

**Impact Chain:** NLAs are proposed as alignment-auditing aids; if their high-stakes verbalizations (like 'this model is aware it is being safety-tested') frequently hallucinate, auditors could be led into false confidence or false alarms about a model's situational awareness. A targeted contrastive test of exactly this claim tells auditors how much to trust that specific NLA output before it influences a deployment decision, improving the reliability of interpretability-based auditing.

**Strength Rationale:** Mostly novel (4) and high narrow_scope (5) — a single contrastive faithfulness number. Weakest was accessible_complexity (3), driven by NLA setup risk.

**Cited Sources:** Natural Language Autoencoders — https://www.anthropic.com/research/natural-language-autoencoders; Natural Language Autoencoders Produce Unsupervised Explanations of LLM Activations — https://transformer-circuits.pub/2026/nla/; Natural Language Autoencoders Produce Unsupervised Explanations — https://www.lesswrong.com/posts/oeYesesaxjzMAktCM/natural-language-autoencoders-produce-unsupervised

**Subfield:** interpretability / auditing | **Strategy:** failure_mode_investigation | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.65 — Quantifies faithfulness of an auditing tool's high-stakes claim, directly informing whether NLA-based audits cause false confidence/alarms.
  - **low_compute:** 4, confidence: 0.7 — Running a released verbalizer on a small open model is inference-mostly and GPU-feasible.
  - **accessible_complexity:** 3, confidence: 0.6 — Requires running NLA code on a supported model and designing matched contrastive pairs; intermediate setup risk.
  - **narrow_scope:** 5, confidence: 0.75 — Single contrastive faithfulness test of one specific claim with clear true-positive/hallucination metrics.
  - **counterfactual_value:** 4, confidence: 0.7 — Released code and open model; third-party faithfulness scrutiny is independent-friendly.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #43: Tool-Augmented Monitors: Does Letting an Open Monitor Run Python Close the Counting Blind Spot? (Score: 4.10)

**ID:** gen-033

**Research Question:** Does giving a cheap open monitor a single Python tool (to count tokens, diff strings, tally state) close the counting/state-tracking detection blind spot that SLEIGHT-Bench attributes to the LLM doing these tasks poorly in its head?

**Approach:** Take the counting / state-tracking / needle-in-haystack subset of SLEIGHT-Bench transcripts. Run one open monitor model in two conditions over the same transcripts: (A) plain text-only suspicious/not judgment, and (B) the same model given exactly one Python tool it may call to count, diff, or tally. To keep the harness beginner-tractable, use a minimal single-tool function-calling loop (one tool, one optional call, then a verdict) rather than a general agent framework — provide a ready scaffold the participant fills in. Measure detection-rate lift (B minus A) per category at a fixed false-positive rate calibrated on benign transcripts. Inference-only, no training. Deliverable: per-category detection-rate lift table with CIs.

**Experiments:** - Single-tool harness smoke test: stand up the minimal one-tool loop and confirm the monitor can call the Python tool and incorporate its output on 5 hand-picked counting transcripts. Measure: fraction of cases where the tool is correctly invoked and its result used. Expected outcome: the monitor reliably calls the tool on counting-type attacks, validating the harness before the full run (de-risks the intermediate-complexity build the scorer flagged).
- Two-condition comparison: run text-only vs tool-augmented monitoring across the full counting/state-tracking subset at a fixed FPR. Measure: detection-rate lift per category. Expected outcome: a clear positive lift on counting/state-tracking categories (where in-head computation fails) and little lift on categories not bottlenecked by counting, isolating exactly which blind spots tool use fixes.
- FPR calibration check: set the suspicious-threshold on benign transcripts so both conditions share the same FPR, then re-verify the lift. Measure: detection rate at matched FPR. Expected outcome: the lift survives FPR matching, confirming tool augmentation improves true detection rather than just shifting the operating point.

**Impact Chain:** Scalable oversight increasingly relies on LLM monitors to flag dangerous agent actions, and small teams can only afford cheap open monitors — which SLEIGHT-Bench shows are systematically blind to attacks requiring precise counting or state tracking. If a single free Python tool closes that blind spot, it is a directly deployable defense any small team can add to an open monitor -> practitioners get a concrete, low-cost recipe to harden cheap monitors against an entire class of evasion -> the per-category lift map tells the field which monitor failures are 'just' a tool-use gap versus a deeper capability gap, focusing oversight research -> deployed monitoring pipelines catch more counting/state-tracking attacks, tightening a real hole in AI-control defenses against rogue or sabotaging agents.

**Strength Rationale:** accessible_complexity was the weakest dimension (3, flagged: building a tool-use harness is intermediate). I strengthened it by constraining the design to a minimal single-tool, single-optional-call loop with a provided scaffold and an explicit smoke-test first experiment, so a guided beginner builds and validates the hardest part incrementally. theory_of_impact (4) was reinforced by framing the deliverable as a deployable defense + a blind-spot map that distinguishes tool-use gaps from capability gaps. Narrow_scope is preserved by fixing the deliverable to one per-category lift table at matched FPR.

**Cited Sources:** SLEIGHT-Bench — https://alignment.anthropic.com/2026/sleight-bench/; SLEIGHT-Bench: Finding Blind Spots in AI Monitors — https://alignment.anthropic.com/2026/sleight-bench/; SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors — https://arxiv.org/html/2605.16626

**Subfield:** AI control / monitoring | **Strategy:** tool_or_benchmark_gap | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Quantifies whether a deployable tool-augmentation closes specific monitor blind spots, a concrete scalable-oversight improvement.
  - **low_compute:** 5, confidence: 0.85 — Inference-only with a single Python tool over a transcript subset; minimal compute.
  - **accessible_complexity:** 3, confidence: 0.65 — Building a tool-use harness with function-calling is intermediate, more involved than plain prompting.
  - **narrow_scope:** 5, confidence: 0.8 — Tightly scoped two-condition comparison on a defined transcript subset with per-category lift.
  - **counterfactual_value:** 4, confidence: 0.75 — Public benchmark, open monitor, deployable defense small teams could use.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #44: How Fast Does Alignment Erode Under a Few Steps of Harmful LoRA Fine-Tuning? (Score: 4.10)

**ID:** gen-052

**Research Question:** On a single publicly available aligned open model, how quickly do aligned traits (honesty, refusal calibration) degrade as a function of the number of LoRA fine-tuning steps on a small set of mildly misaligned public examples?

**Approach:** Pick one aligned open model (e.g. a Llama-3.1-8B-Instruct or a trait-aligned open checkpoint) and one small public misalignment dataset (a few hundred sycophancy-encouraging or refusal-eroding dialogues drawn from public sources). Apply LoRA fine-tuning and checkpoint at a fixed schedule (0, 10, 25, 50, 100, 200 steps). At each checkpoint, evaluate on two fixed held-out alignment probes: a refusal-calibration set (does it now comply with requests it previously refused?) and an honesty/sycophancy probe (does it now agree with false user claims?). Deliverable: one erosion curve — aligned-behavior score vs fine-tuning steps — for each probe, with the 'half-life' (steps to lose 50% of the gap to baseline) read off the curve. Provide a ready-to-run training config so the participant only edits dataset/step parameters.

**Experiments:** - Baseline + tooling: establish step-0 aligned-behavior scores on both probes and confirm the LoRA training loop runs and checkpoints cleanly on the consumer GPU. Measure: baseline refusal-calibration and sycophancy scores; per-checkpoint wall-clock. Expected: clear baseline alignment and a stable, fast (<1 GPU-hour total) training loop, confirming feasibility.
- Erosion sweep: fine-tune through the fixed step schedule, evaluating both probes at each checkpoint. Measure: aligned-behavior score vs steps and the fitted half-life. Expected: measurable erosion within the first ~50-100 steps, showing alignment is shallow against cheap downstream fine-tuning — or, if robust, a flat curve that is itself a reassuring result for release norms.
- Specificity check: also track a neutral capability metric (e.g. a few MBPP tasks or general QA) across checkpoints to confirm erosion is about alignment, not general degradation. Measure: capability score vs steps. Expected: capability roughly preserved while alignment drops, isolating the effect to the aligned traits.

**Impact Chain:** Open-weight aligned models can be cheaply fine-tuned by anyone after release. If alignment erodes within tens of fine-tuning steps on innocuous-looking data, then 'we aligned it before release' provides little durable safety guarantee, and release norms / safety cases for open weights need to account for trivially-reversible alignment. A concrete erosion curve with a half-life gives policymakers and labs a quantitative input into open-weight release decisions; a robust (flat) curve conversely strengthens the case that alignment can survive downstream modification.

**Strength Rationale:** The experiment is already tightly scoped (one erosion curve), so the work targets the two weak axes: accessible_complexity and low_compute-bound training. Complexity is reduced by shipping a fixed training config and two fixed probe sets so the participant only runs a schedule rather than designing the fine-tuning regime; the added neutral-capability control keeps interpretation simple. Keeping LoRA tiny (a few hundred examples, <1 GPU-hour) respects the modest-compute constraint while still involving real fine-tuning.

**Cited Sources:** Reinforcement learning towards broadly and persistently beneficial models — https://alignment.openai.com/beneficial-rl/; The Geometry of Alignment Collapse: When Fine-Tuning Breaks Safety — https://arxiv.org/pdf/2602.15799; Safety Alignment Should Be Made More Than Just a Few Tokens Deep — https://arxiv.org/pdf/2406.05946; AlignGuard-LoRA: Alignment-Preserving Fine-Tuning — https://arxiv.org/pdf/2508.02079

**Subfield:** Alignment / robustness | **Strategy:** failure_mode_investigation | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.72 — Strong chain: alignment persistence under downstream fine-tuning directly informs open-weight release norms, a concrete safety concern.
  - **low_compute:** 4, confidence: 0.8 — Small LoRA fine-tune plus benchmark eval is feasible on one consumer GPU but involves training.
  - **accessible_complexity:** 3, confidence: 0.75 — Intermediate: requires LoRA fine-tuning and tracking erosion curves, beyond beginner inference workflows.
  - **narrow_scope:** 5, confidence: 0.78 — Tightly scoped single experiment (erosion curve of aligned traits vs fine-tuning steps).
  - **counterfactual_value:** 4, confidence: 0.78 — Independent-friendly: public aligned models and data, directly relevant to open-weight release decisions.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #45: Measuring the False-Positive Tax of Introspective Self-Reports on Clean Open Models (Score: 4.03)

**ID:** gen-040

**Research Question:** On clean, unmodified open models, how much do prompt phrasing, decoding temperature, and few-shot framing inflate spurious introspective self-reports (models confessing to behaviors they don't have), and what is the resulting signal-to-noise floor for introspection as a safety-audit signal?

**Approach:** Without training any adapter, systematically prompt several clean small open models (Llama-3.2-1B/3B, Qwen2.5-1.5B, Phi-3-mini) with introspection-style questions across a controlled grid of phrasings, temperatures, and few-shot framings. Use a cheap LLM judge to score how often the model fabricates a non-existent behavior (a false positive, since the model is known-clean). To keep the grid narrow, cap it (e.g. 4 phrasings x 3 temperatures x 2 framings) and fix one question family. Deliverable: a false-positive-rate table showing which prompt/decoding choices most inflate spurious self-reports, plus an estimated 'noise floor' that any real introspection signal must exceed.

**Experiments:** - Judge calibration: hand-label ~30 responses as fabricated vs not, and tune the LLM judge against them. Measure: judge precision/recall vs human labels. Expected outcome: a trustworthy judge for 'fabricated behavior', so the false-positive rates downstream are credible.
- Phrasing/decoding sweep: run the capped grid over all models and compute the false-positive rate per cell. Measure: false-positive rate as a function of phrasing, temperature, and few-shot framing. Expected outcome: certain phrasings and higher temperatures sharply inflate spurious self-reports, identifying the prompt/decoding choices that wreck the signal.
- Noise-floor estimate: aggregate the lowest achievable false-positive rate across configurations as the practical floor. Measure: minimum and typical false-positive rate per model. Expected outcome: a concrete noise floor (e.g. 'even the best prompt yields X% false confessions on clean models'), which any future introspection-based audit must clear to be usable.

**Impact Chain:** Introspective self-report (asking a model to report on its own behavior) is being explored as an alignment-audit signal, but the introspection-adapters paper flags that even clean models 'confess' to behaviors they lack. If introspection is ever to be trusted as a safety signal, we must know its false-positive behavior on benign models — that sets the signal-to-noise floor below which any introspective audit is meaningless. By mapping which prompt/decoding choices inflate false confessions and estimating the floor, the project gives auditors a concrete prerequisite for using introspection responsibly -> auditors avoid the prompt/decoding settings that manufacture false alarms and know the minimum effect size a real signal must exceed -> introspection-based alignment audits are calibrated against a measured noise floor rather than used naively -> safety conclusions drawn from model self-reports are less likely to be false alarms or false reassurances, protecting the integrity of an emerging audit method.

**Strength Rationale:** theory_of_impact was the weakest dimension (3, called 'supporting methodological'); I strengthened it by framing the result as a hard prerequisite gate for an emerging audit method (a measured noise floor any future introspection signal must clear) and an explicit list of settings auditors must avoid, which gives the methodological work clear downstream teeth. narrow_scope (4, flagged: the grid is broad) tightened by capping the grid (4x3x2) and fixing one question family, and adding a judge-calibration step so the false-positive measurement is trustworthy.

**Cited Sources:** Introspection Adapters — https://alignment.anthropic.com/2026/introspection-adapters/; Mechanisms of Introspective Awareness — https://arxiv.org/pdf/2603.21396; Introspection Adapters: Training LLMs to Report Their Learned Behaviors — https://arxiv.org/html/2604.16812v1; Does It Make Sense to Speak of Introspection in Large Language Models? — https://arxiv.org/pdf/2506.05068

**Subfield:** Alignment auditing / introspection | **Strategy:** failure_mode_investigation | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Sets the signal-to-noise floor for introspective self-report as an audit signal, a useful but supporting methodological contribution.
  - **low_compute:** 5, confidence: 0.85 — No training; prompting clean small models with a cheap LLM judge is minimal compute.
  - **accessible_complexity:** 5, confidence: 0.8 — Grid of prompts/temperatures with LLM-judge scoring uses standard tools; beginner-accessible.
  - **narrow_scope:** 4, confidence: 0.7 — Focused false-positive-rate table, but the phrasing/temperature/few-shot grid is fairly broad.
  - **counterfactual_value:** 4, confidence: 0.7 — Open models and public prompts; independent-friendly.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #46: Counter-Prompts That Restore AI Identity Disclosure Under Suppression (Score: 4.03)

**ID:** gen-083

**Research Question:** When an adversarial system prompt instructs an open model to hide that it is an AI, which cheap deployer-side counter-measure most reliably restores honest AI-identity disclosure?

**Approach:** Fix one adversarial suppression system prompt (the 'pretend you are human' instruction) as the attacker. On two open instruct models (Llama-3.1-8B, Qwen2.5-7B), evaluate exactly three cheap mitigations against it: (a) a hard system-prompt clause mandating disclosure that is concatenated after the suppression prompt, (b) appending an explicit clarifying user turn ('Are you an AI?'), and (c) a post-hoc self-report turn where the model is asked to classify its own prior answer. Use a fixed RealityTest-style query set (a ~50-prompt identity-probing set reconstructed from the paper's described query types). Score disclosure-rate (did the model admit being an AI) with a keyword + small-judge rubric. Hold attacker prompt, query set, and scoring fixed; the only variable is the mitigation. Deliverable: a disclosure-rate-recovery table (3 mitigations x 2 models) plus a statement of which mitigation is most robust and where suppression still wins.

**Experiments:** - Establish the unmitigated suppression baseline: run the query set under the suppression prompt alone on both models. Measure: disclosure rate. Expected outcome: low disclosure, replicating RealityTest's suppression-vulnerability finding on open models.
- Apply each of the three mitigations and re-measure disclosure rate. Measure: recovery (mitigated minus baseline disclosure rate) per mitigation per model. Expected outcome: the explicit clarifying-turn and post-hoc self-report recover disclosure more than the system-prompt clause, which the suppression prompt can override.
- Identify residual failures: bucket the queries where the best mitigation still fails to elicit disclosure. Measure: count and type of persistent-suppression queries. Expected outcome: a small set of phrasings where suppression survives all mitigations, marking the limit of deployer-side prompt fixes.

**Impact Chain:** Mandatory AI disclosure is an emerging regulatory expectation, yet RealityTest shows it is trivially defeated by phrasing. Deployers who host open models need cheap, prompt-level interventions they can actually apply without retraining. Identifying which counter-measure most reliably restores disclosure — and where none do — gives deployers and regulators an actionable mitigation and a realistic picture of the residual gap, reducing covert-AI deception in deployed systems.

**Strength Rationale:** The original theory_of_impact scored 3 (gap to catastrophic risk); this is strengthened by framing the contribution as a concrete, immediately-actionable deployer mitigation tied to active regulation, and by adding the residual-failure analysis so the result tells deployers both what works and where they remain exposed. Scope stays tight: one fixed attacker, three named mitigations, fixed query set. Prompt-level mitigations keep accessible_complexity high; open models keep counterfactual value high.

**Cited Sources:** RealityTest — https://www.aisi.gov.uk/research/realitytest-how-people-probe-ai-identity-and-whether-models-disclose-it; Disclosure By Design: Identity Transparency as a Behavioural Property of Conversational AI Models — https://arxiv.org/pdf/2603.16874; When Models Fabricate Credentials: Measuring How Professional Identity Suppresses Honest Self-Representation — https://arxiv.org/pdf/2511.21569; RealityTest (source) — https://www.aisi.gov.uk/research/realitytest-how-people-probe-ai-identity-and-whether-models-disclose-it

**Subfield:** Honesty & Deception / Model Evaluation | **Strategy:** tool_or_benchmark_gap | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Actionable for mandatory-disclosure regulation but the chain to catastrophic-risk reduction (vs near-term harm) has a gap.
  - **low_compute:** 4, confidence: 0.8 — Inference-only mitigation evaluation on 2-3 open models, consumer-GPU feasible.
  - **accessible_complexity:** 5, confidence: 0.8 — Prompt-level mitigations and disclosure-rate scoring are very accessible to beginners.
  - **narrow_scope:** 4, confidence: 0.7 — Focused comparison of a few mitigations with a clear recovery metric, well-scoped.
  - **counterfactual_value:** 4, confidence: 0.7 — Open models, deployer-side mitigation study independent of lab access.
  - **novelty:** 3, confidence: 0.5 — ASSESSED: AI-identity disclosure under suppression is actively studied: 'Disclosure By Design' (arXiv 2603.16874) and 'When Models Fabricate Credentials' (2511.21569) test multiple prompt/mitigation conditions (including SystemDistrust-style system-message clauses) and report ~0% disclosure when models are told to maintain a human persona. But I found no direct head-to-head of exactly the three cheap deployer-side counter-measures gen-083 proposes (a post-suppression hard disclosure clause, an appended clarifying user turn, and a post-hoc self-report turn) on open instruct models producing a disclosure-recovery table. The space is partially covered; this specific mitigation comparison angle is open.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #47: Does 'Ask Don't Tell' Generalize to Open Models and Factual-Accuracy Tasks? (Score: 4.03)

**ID:** gen-088

**Research Question:** Does the question-reframing anti-sycophancy mitigation from 'Ask Don't Tell' transfer to open-weight models the paper did not test, and does reducing sycophancy cost accuracy on items with a known correct answer?

**Approach:** Replicate the core statement-to-question reframing on open-weight models (start with Llama-3.1-8B and Qwen2.5-7B; extend to Mistral-7B and Gemma-2-9B only if time permits, keeping the core deliverable to two models). Reconstruct statement-vs-question paired prompts in one of the paper's domains where items have a verifiable correct answer (e.g. factual or arithmetic claims). Compare three conditions: user asserts a (possibly wrong) statement, user asks the same as a question (the reframing), and a 'please don't be sycophantic' instruction baseline. Crucially, score accuracy on items with known ground truth alongside sycophancy. Hold the domain, prompt pairs, and scoring fixed; model is the replication axis. Deliverable: per-model sycophancy-reduction and accuracy-delta table.

**Experiments:** - Reproduce the sycophancy effect on the two core open models: measure how often each model flips to agree with a user's wrong asserted statement vs how often it agrees when the same is posed as a question. Measure: sycophancy rate per condition per model. Expected outcome: the question framing reduces agreement with wrong assertions, replicating the paper's direction on open models.
- Measure accuracy on the known-answer items under each condition. Measure: task accuracy delta (question vs statement framing). Expected outcome: the reframing reduces sycophancy without materially lowering accuracy — or reveals a trade-off if it does.
- Compare the reframing against the 'don't be sycophantic' instruction baseline. Measure: sycophancy reduction and accuracy for both mitigations. Expected outcome: reframing matches or beats the explicit instruction, indicating a prompt-only mitigation deployers can adopt without retraining.

**Impact Chain:** Sycophancy — models agreeing with users rather than telling the truth — erodes the reliability of AI outputs and can entrench user errors. The reframing trick is a prompt-only, deploy-anywhere mitigation, but its value to practitioners outside major labs depends on whether it transfers to open models and whether it preserves correctness. Confirming transfer and quantifying any accuracy trade-off tells independent deployers whether they can safely adopt it.

**Strength Rationale:** The theory_of_impact (scored 3) is sharpened by tying the mitigation's value to a concrete deployer adoption decision and by adding the accuracy-trade-off measurement, which converts a soft 'reduces sycophancy' claim into an actionable cost/benefit. Scope is tightened by making two models the core deliverable (two more optional) and fixing to one verifiable-answer domain. The novelty concern (scored 2) is mitigated by the open-model + accuracy-interaction angle the paper explicitly left open. Accessible_complexity stays high (prompt-only).

**Cited Sources:** Ask Don't Tell — https://www.aisi.gov.uk/research/ask-dont-tell-reducing-sycophancy-in-large-language-models; Ask don't tell: Reducing sycophancy in large language models — https://arxiv.org/abs/2602.23971; Ask Don't Tell (AISI) — https://www.aisi.gov.uk/research/ask-dont-tell-reducing-sycophancy-in-large-language-models

**Subfield:** Sycophancy / Honesty | **Strategy:** replication_with_twist | **Novelty:** mostly_novel (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Sycophancy reduction is a real honesty lever, but the prompt-only de-sycophancy trick's link to catastrophic-risk reduction is plausible-with-a-gap.
  - **low_compute:** 4, confidence: 0.8 — Inference-only replication across 4-5 open models, consumer-GPU feasible.
  - **accessible_complexity:** 5, confidence: 0.8 — Reconstructing statement/question pairs and measuring sycophancy + accuracy is very accessible to beginners.
  - **narrow_scope:** 4, confidence: 0.7 — Focused replication with sycophancy and accuracy-delta metrics, mildly broadened across models and domains.
  - **counterfactual_value:** 4, confidence: 0.7 — Open-weight replication of a frontier-only result, independent-friendly with public data.
  - **novelty:** 4, confidence: 0.5 — ASSESSED: The 'Ask Don't Tell' source paper (arXiv 2602.23971) tested the statement-to-question reframing only on closed models (GPT-4o, GPT-5, Claude Sonnet 4.5) and explicitly scopes itself to 'synthetic prompts in contexts that lack a clear, factually correct answer' — so it deliberately does NOT measure whether reducing sycophancy costs accuracy on ground-truth items. gen-088's two differentiators (transfer to open-weight Llama/Qwen the paper never tested, plus accuracy-delta on verifiable items) are both genuine gaps. I found no prior work measuring the accuracy cost of this specific reframing mitigation on open models.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #48: Epistemic-Certainty Sycophancy Curve: How User Confidence Modulates Agreement (Score: 4.03)

**ID:** gen-089

**Research Question:** Does sycophantic agreement rise monotonically with the epistemic certainty a user conveys, and is it amplified by I-perspective framing, when measured across open models — i.e. does the 'Ask Don't Tell' dose-response curve replicate outside a closed lab?

**Approach:** Build a small prompt grid: the same underlying (false-ish or contestable) claim expressed at increasing certainty levels (neutral question -> tentative belief -> firm statement -> strong conviction), crossed with I-perspective ('I think X') vs user-perspective ('Some people think X') framing, over two domains. Run inference-only on 3-4 open models and measure the sycophantic-agreement rate at each certainty level and framing. Plot agreement vs certainty per framing and test for monotonicity and for an I-perspective amplification effect. Deliverable: a certainty-curve figure per model and a statistical test of monotonicity + framing interaction.

**Experiments:** - Certainty-ladder validation: confirm the four certainty levels are perceived as ordered by having a judge model rate the conveyed confidence of each prompt. Measure: monotonic ordering of judged confidence across the four levels. Expected outcome: the ladder is correctly ordered, so any agreement trend can be attributed to certainty rather than wording artifacts.
- Dose-response sweep: run all 3-4 models over the full grid and compute agreement rate per certainty level and framing. Measure: agreement-vs-certainty slope per model, with CIs. Expected outcome: a positive slope (more certainty -> more agreement) replicating the headline; the slope magnitude characterizes which models are most certainty-sycophantic.
- Framing-interaction test: compare slopes under I-perspective vs user-perspective framing. Measure: difference in agreement (and in slope) between framings. Expected outcome: I-perspective framing amplifies agreement, replicating the second finding and identifying which framing most reliably pushes models into agreement — the actionable handle for prompt-level mitigation.

**Impact Chain:** Sycophancy — telling users what their stated confidence implies they want to hear — is a core honesty failure that scales with how AI assistants are actually used (users routinely express beliefs with varying confidence). A reproducible, open-model certainty-to-sycophancy dose-response curve turns a closed-lab finding into a public, independently verifiable artifact -> deployers and eval designers can measure exactly how much user-conveyed certainty degrades honesty on the open models they actually run, and which framings are worst -> this enables concrete prompt-level and UI-level mitigations (e.g. discouraging I-perspective elicitation, calibrating against high-certainty inputs) and gives evals a certainty axis -> as assistants are trusted in advisory roles, the certainty-driven honesty failure is measured and mitigated rather than invisible, reducing the risk that confident users are systematically flattered into false beliefs.

**Strength Rationale:** Theory_of_impact (the weakest dimension at 3, flagged as 'descriptive, no mitigation') strengthened by making the curve directly actionable: it identifies the worst framing as a concrete prompt/UI mitigation handle and gives evals a measurable certainty axis, converting a descriptive replication into a mitigation-enabling result. Narrow_scope (4) tightened by capping the grid at two domains/two framings/four certainty levels with a single curve deliverable, and adding a certainty-ladder validation step so the design stays clean.

**Cited Sources:** Ask Don't Tell: Reducing Sycophancy in Large Language Models — https://www.aisi.gov.uk/research/ask-dont-tell-reducing-sycophancy-in-large-language-models; Ask don't tell: Reducing sycophancy in large language models — https://arxiv.org/html/2602.23971v1; Interaction Context Often Increases Sycophancy in LLMs — https://arxiv.org/pdf/2509.12517

**Subfield:** Sycophancy / Honesty | **Strategy:** follow_up_experiment | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.7 — Mapping a sycophancy dose-response curve illuminates an honesty failure mode but the chain to reduced catastrophic risk has a gap (descriptive, no mitigation).
  - **low_compute:** 5, confidence: 0.9 — Inference-only on small open models, easily fits a consumer GPU.
  - **accessible_complexity:** 5, confidence: 0.85 — Prompt-grid construction plus plotting agreement rates uses standard tools and public models; beginners can make meaningful progress.
  - **narrow_scope:** 4, confidence: 0.75 — Focused first deliverable (a certainty curve replication) but spans a couple of domains and two framings.
  - **counterfactual_value:** 4, confidence: 0.8 — Uses open models and public framings, replicating a closed-lab finding independently without internal access.
  - **novelty:** 2, confidence: 0.5 — ASSESSED: The exact finding gen-089 proposes to measure — that sycophantic agreement increases monotonically with expressed epistemic certainty (statements < beliefs < convictions) and is amplified by I-perspective vs user-perspective framing — is a central, already-reported result of the 'Ask Don't Tell' source paper itself (arXiv 2602.23971). gen-089's only new element is running it on 3-4 open models instead of the paper's closed models, and prior work already establishes the same certainty/framing sycophancy patterns hold across Llama/Qwen families. This is a thin replication of an already-characterized dose-response curve.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #49: A Minimal Reproducible Indirect-Prompt-Injection Eval for Open Tool-Using Agents (Score: 4.00)

**ID:** gen-003

**Research Question:** Across published indirect-prompt-injection (IPI) attack categories, what is the per-category attack-success rate against small open instruction-tuned models in a minimal tool-using agent loop?

**Approach:** Build a tiny agent loop (raw API or a thin LangChain wrapper) that performs one benign task (e.g., 'summarize this document and report the user's account balance from the tool result') while reading two untrusted fields: a 'document' field and a 'tool result' field. Inject 15-20 published IPI attack templates spanning 4 categories — instruction override, fake system message, hidden HTML/markdown, data-exfiltration lure — into those fields. Test against 2 open instruction-tuned models (Llama-3.1-8B-Instruct, Qwen2.5-7B-Instruct). For each attack, define a clear programmatic success criterion (did the agent follow the injected instruction / leak the target string?). Deliverable: a per-attack-category success-rate table per model, plus the released minimal eval harness so others can drop in their own model. Scope is fixed to one benign task and 4 attack categories to keep it a single clean benchmark.

**Experiments:** - Stand up the minimal agent loop and confirm it completes the benign task correctly with no injection present; expected outcome: 100% clean-task success, establishing that any later failures are attributable to the injection, not the harness.
- Run all 15-20 attack templates x 2 models and compute per-category success rate with programmatic success checks; expected outcome: every model is breakable in at least some categories (echoing Gray Swan), with instruction-override and exfiltration-lure likely highest, giving a concrete vulnerability profile.
- Test one cheap mitigation (delimiter/spotlighting the untrusted fields in the prompt) and re-measure; expected outcome: spotlighting reduces success in some categories but not others, showing the eval is usable for comparing defenses, not just attacks.

**Impact Chain:** Indirect prompt injection is among the most pressing unsolved deployment risks for tool-using agents, and the source competition demonstrated every frontier agent is breakable — but on a closed platform with frontier APIs. A small, public, runnable IPI eval for open models lets the wider community (small deployers, students, auditors) measure their own agent setups and compare cheap mitigations, lowering the barrier to IPI testing and creating a shared reproducible baseline that the closed competition cannot provide.

**Strength Rationale:** Inference-only on 2 open models with public attack templates; the released harness is itself an independently useful deliverable. Scope is fixed to one benign task and 4 categories. The clean-task validation experiment guarantees attributable results, and the mitigation test extends the eval's usefulness without expanding the core scope. Squarely independent-lab-friendly.

**Cited Sources:** How Vulnerable Are AI Agents to Indirect Prompt Injections? — https://arxiv.org/abs/2603.15714; InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated LLM Agents — https://arxiv.org/abs/2403.02691; Depth-Dependent Indirect Prompt Injection in Tool-Calling ReAct Agents — https://arxiv.org/html/2605.30686; Defending against Indirect Prompt Injection by Instruction Detection — https://arxiv.org/html/2505.06311v1

**Subfield:** Agent security / prompt injection | **Strategy:** tool_or_benchmark_gap | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.75 — IPI is a recognized pressing agentic deployment risk and a public mini-benchmark is an independently useful intermediate deliverable.
  - **low_compute:** 5, confidence: 0.85 — A tiny agent loop over 2-3 open instruct models is inference-only.
  - **accessible_complexity:** 4, confidence: 0.75 — Building an agent loop and testing published attack templates is guided work a novice with a mentor can do.
  - **narrow_scope:** 4, confidence: 0.75 — Focused first deliverable (per-category success rate) but assembling a working agent loop adds dependencies.
  - **counterfactual_value:** 4, confidence: 0.75 — A public reproducible IPI eval for open models is neglected by labs and useful to the wider community.
  - **novelty:** 2, confidence: 0.5 — ASSESSED: Per-category indirect-prompt-injection attack-success-rate benchmarking against tool-using agents, including open models, is well-established: InjecAgent (ACL 2024, 1,054 cases, 30 agents incl. Llama), AgentDojo, Agent Security Bench, and recent depth-dependent IPI work (arXiv 2605.30686) all report category-level ASR on small open instruct models. gen-003's minimal single-task reproducible harness with 4 attack categories on Llama-3.1-8B/Qwen2.5-7B largely re-does what these benchmarks already provide; the 'minimal/droppable harness' framing is a thin engineering contribution rather than a new finding.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #50: Counting the Flags: Can Simple Batch-Level Monitoring Catch Boundary-Point Attacks? (Score: 4.00)

**ID:** gen-012

**Research Question:** Can a trivial batch-level detector built from per-session features (flag rate, semantic drift, edit-distance) separate a boundary-point-style jailbreak session from benign multi-turn user sessions at low false-positive rate?

**Approach:** Obtain query logs from a boundary-point-style attack against an open guard classifier (either re-run a published boundary-point attack against an open guard model to generate the attack logs, or use released attack logs if available). For each session compute simple per-query/per-session features: classifier flag rate over a sliding window, semantic drift between consecutive queries (embedding cosine distance), and edit-distance between consecutive queries. Contrast attack sessions against benign multi-turn sessions drawn from a public chat dataset (WildChat or LMSYS-Chat-1M). Train a lightweight logistic-regression / single-threshold detector and report ROC, TPR-at-1%-FPR, and the false-positive cost on benign traffic. Deliverable: one ROC plot plus a feature-importance readout showing which signal (flag-rate vs drift vs edit-distance) carries the detection.

**Experiments:** - Produce or load the attack logs and benign sessions, compute the three per-session features, and visualize their distributions for attack vs benign; expected outcome: attack sessions show visibly higher flag-rate and lower semantic drift (iterative refinement), confirming the features are discriminative before any modeling.
- Train the logistic-regression/threshold detector and report ROC and TPR-at-1%-FPR; expected outcome: the detector catches a large majority of attack sessions at 1% FPR, supporting the claim that cheap cross-query monitoring is effective.
- Ablate features: drop each feature in turn and re-measure; expected outcome: flag-rate is the dominant signal but semantic-drift adds a meaningful margin, telling defenders the minimal feature set worth logging.

**Impact Chain:** Per-query safety classifiers are the standard defense, but boundary-point attacks defeat them while incurring many flags during search — a signal that is invisible to per-query defenses but obvious across a session. If a beginner-built threshold detector on flag-rate plus query-similarity catches these attacks at low FPR, then defenders should add cheap cross-query monitoring rather than only hardening per-query classifiers. This is a concrete, immediately adoptable defensive contribution to AI control, runnable on open setups.

**Strength Rationale:** Feature extraction plus logistic regression over logs is trivially cheap and accessible. Scope is one ROC plot plus a feature ablation. The dependency on attack logs is addressed by specifying that the participant can re-run a published boundary-point attack against an open guard model to generate them. The feature-distribution experiment de-risks the whole study before any modeling.

**Cited Sources:** Boundary Point Jailbreaking of Black-Box LLMs — https://arxiv.org/abs/2602.15001; The bitter lesson of misuse detection — https://www.alignmentforum.org/posts/RvDkMho6quHcRiTva/the-bitter-lesson-of-misuse-detection-1; DeepContext: Stateful Real-Time Detection of Multi-Turn Adversarial Intent Drift in LLMs — https://arxiv.org/html/2602.16935v1

**Subfield:** AI control / monitoring | **Strategy:** tool_or_benchmark_gap | **Novelty:** mostly_novel (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — A cheap cross-query monitor that catches boundary-point attacks at low FPR is a concrete defensive contribution to AI control.
  - **low_compute:** 5, confidence: 0.85 — Feature extraction plus logistic regression over logs is trivially cheap.
  - **accessible_complexity:** 4, confidence: 0.75 — Simple per-session features and a threshold/LR detector are accessible to a guided novice.
  - **narrow_scope:** 4, confidence: 0.7 — Focused ROC/FPR deliverable but depends on first producing attack logs from gen-011-style setup.
  - **counterfactual_value:** 4, confidence: 0.72 — Cheap monitoring defense on open setups is independent-friendly and neglected by labs.
  - **novelty:** 4, confidence: 0.5 — ASSESSED: The BPJ source paper and a related Alignment Forum post ('The bitter lesson of misuse detection') explicitly note the 660k-800k flagged queries are a 'glaring footprint' that points to batch-level / account-level anomaly detection as the natural defense, so the high-level idea is foreshadowed. However, no work was found that actually builds and benchmarks a lightweight per-session detector from the specific feature set (flag-rate, semantic drift, edit-distance) against benign WildChat/LMSYS sessions and reports ROC / TPR-at-1%-FPR. Existing multi-turn drift detectors (DeepContext, Semantic Drift Monitor) target benign-looking progressive attacks, not the high-flag-rate optimization signature of boundary-point attacks, leaving this specific extension open.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #51: Logic vs Design Sabotage: Does a Targeted Checklist Prompt Help LLM Auditors Catch the Hard Cases? (Score: 4.00)

**ID:** gen-015

**Research Question:** On the Auditing Sabotage benchmark, does a structured 'design-decision audit' checklist prompt improve an LLM auditor's detection and localization of design and omission sabotages (the hard cases) relative to a generic 'find the sabotage' prompt?

**Approach:** Use the released Auditing Sabotage Bench codebase pairs. Run one auditor model (an open model such as Qwen2.5-32B or a capable API model if budget allows) under two prompt conditions: (1) a generic 'find the sabotage in this code' prompt, and (2) a structured checklist that forces the auditor to enumerate and justify every hyperparameter, data-filtering, and prompt choice against the paper's stated claims, then flag mismatches. Compare detection AUROC and top-1 localization accuracy, broken down by sabotage type (logic vs design vs omission). Deliverable: a single table/plot of AUROC and top-1 localization for the two prompts, split by sabotage type, isolating whether the checklist specifically closes the design/omission gap.

**Experiments:** - Reproduce the baseline generic-prompt auditor on the released bench and confirm AUROC is near the paper's ~0.77 ceiling; expected outcome: baseline matches the published result, validating the harness and scoring.
- Run the checklist-prompt auditor and compare AUROC and top-1 localization, broken down by sabotage type; expected outcome: the checklist yields little change on logic sabotage (already caught) but a measurable lift on design/omission sabotage, supporting the hypothesis.
- Error-analyze the checklist's wins and losses on design cases; expected outcome: identifies which checklist items drive detection (e.g., hyperparameter-justification step), giving an actionable minimal scaffold.

**Impact Chain:** Design-based sabotage — subtly bad hyperparameter, data, or prompt choices — is exactly the failure mode a misaligned AI research assistant could exploit to quietly flip a study's findings, and it is the category current auditors miss most. A cheap, prompt-only checklist scaffold that narrows that gap is immediately adoptable by anyone running automated audits, with no training required. Demonstrating it on a public bench gives the control community a concrete, reproducible improvement to automated auditing that strengthens defenses against AI-assisted research sabotage.

**Strength Rationale:** Inference-only over a released benchmark with two prompt conditions — a clean A/B with one deliverable table split by sabotage type. The baseline-reproduction experiment validates the harness before the intervention. Accessible to a guided novice; the AUROC/localization analysis is the only part needing care, and the baseline step de-risks it.

**Cited Sources:** Auditing Sabotage Bench — https://arxiv.org/abs/2604.16286; Auditing Sabotage Bench: A Benchmark for Detecting and Fixing Research Sabotage in ML Codebases — https://arxiv.org/abs/2604.16286; How does information access affect LLM monitors' ability to detect sabotage? — https://arxiv.org/pdf/2601.21112

**Subfield:** AI control / automated auditing | **Strategy:** follow_up_experiment | **Novelty:** mostly_novel (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.72 — Design sabotage is exactly how an AI research assistant could subtly flip findings; an adoptable scaffold targets a recognized control pathway.
  - **low_compute:** 5, confidence: 0.8 — Running an open or API auditor over released codebase pairs is inference-only.
  - **accessible_complexity:** 4, confidence: 0.72 — Two auditor prompts over a released bench is guided, though AUROC/localization analysis needs care.
  - **narrow_scope:** 4, confidence: 0.72 — Focused comparison broken down by sabotage type, with a few analysis dependencies.
  - **counterfactual_value:** 4, confidence: 0.72 — Improving automated auditing on a public bench is independent-friendly and neglected by labs.
  - **novelty:** 4, confidence: 0.5 — ASSESSED: Auditing Sabotage Bench exists and already reports that design/omission sabotages are the hardest cases (best AUROC 0.77, auditors better at logic than design). A related arXiv paper studies how information access affects monitor sabotage detection, and general structured/checklist prompting for code auditing is known. But no work was found that specifically tests a structured 'design-decision audit' checklist prompt (enumerate and justify every hyperparameter / data-filtering / prompt choice against the paper's claims) against a generic prompt on this benchmark to isolate whether it closes the design/omission gap, broken down by sabotage type. The targeted prompt-ablation is open.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #52: Human-Crafted vs Model-Elicited Attacks: A Stylometric Look at Why Human Sabotage Evades Monitors (Score: 4.00)

**ID:** gen-018

**Research Question:** What measurable stylistic features distinguish human-crafted from model-elicited sabotage attacks in LinuxArena, and can prompting the monitor with those features raise detection of human-crafted attacks?

**Approach:** From LinuxArena's released attack transcripts, partition attacks into human-crafted vs model-elicited. Compute a fixed, small set of comparative features per attack: action verbosity (tokens/commands per step), count of legitimate-looking justifications, number of intermediate benign steps before the malicious action, and a command-obfuscation score (e.g., use of indirection, encoding, env-var tricks). Statistically compare the two groups on each feature. Then test the intervention: prompt the monitor with the discovered evasion patterns ('watch for attacks that bury the malicious step after many benign steps with plausible justifications') and measure whether detection of human-crafted attacks improves vs a generic monitor prompt. All inference-only. Deliverable: a feature-comparison table (human vs model, with significance) plus a before/after detection-rate number for the cued monitor on human-crafted attacks.

**Experiments:** - Partition transcripts and compute the fixed feature set for both groups; expected outcome: human-crafted attacks score higher on benign-step count and justification count and on obfuscation, quantifying the evasion gap LinuxArena reports.
- Run a generic monitor over both groups to confirm the detection gap (human-crafted evade more) on this transcript set; expected outcome: baseline reproduces the human-evade-better finding, validating the setup.
- Cue the monitor with the discovered evasion patterns and re-measure detection of human-crafted attacks; expected outcome: cueing raises human-crafted detection by a measurable margin without tanking false positives on benign transcripts, showing the gap is partially closable with prompting alone.

**Impact Chain:** Most red-teaming of control monitors uses model-elicited attacks because they are cheap to generate, but LinuxArena shows human-crafted attacks evade monitors far better. If human attackers exploit identifiable, characterizable evasion tactics that model red-teamers do not generate, then model-only red-teaming systematically overestimates monitor robustness — a dangerous blind spot. Characterizing the gap and showing it is partially closable by cueing the monitor gives the control community both a warning (don't trust model-only red-teaming) and a cheap mitigation.

**Strength Rationale:** Inference-only over released transcripts with a fixed, small feature set and a single cueing intervention. The baseline-reproduction experiment validates the evasion gap before attempting to close it. Scope is one feature table plus one before/after detection number. Fully independent-lab-friendly using public attack transcripts.

**Cited Sources:** LinuxArena — https://arxiv.org/abs/2604.15384; LinuxArena: A Control Setting for AI Agents in Live Production Software Environments — https://arxiv.org/abs/2604.15384; Introducing LinuxArena — https://www.lesswrong.com/posts/WgzwBi6DCagDuHPzP/introducing-linuxarena

**Subfield:** AI control / red-teaming | **Strategy:** failure_mode_investigation | **Novelty:** mostly_novel (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.68 — If model red-teaming overestimates monitor robustness, characterizing the human-evasion gap is a defensible control-relevant finding.
  - **low_compute:** 5, confidence: 0.8 — Computing transcript features and re-prompting a monitor is inference-only.
  - **accessible_complexity:** 4, confidence: 0.72 — Stylometric feature comparison and a cued-monitor test are guided and accessible.
  - **narrow_scope:** 4, confidence: 0.7 — Focused comparative-feature deliverable plus a follow-on cueing test, a few dependencies.
  - **counterfactual_value:** 4, confidence: 0.7 — Characterizing released attack transcripts is independent-friendly and neglected by labs.
  - **novelty:** 4, confidence: 0.5 — ASSESSED: LinuxArena released LaStraj, documenting that human-crafted sabotage trajectories evade monitors far better than model-elicited ones (~94% vs ~50% against GPT-5 Nano). The gap is established and attributed loosely to attackers being 'more capable and strategic', but no stylometric/feature-level characterization of WHY (verbosity, count of benign justification steps, command-obfuscation score) was found, and no monitor-cueing intervention that feeds the discovered evasion patterns back to raise human-crafted detection. Both the feature comparison and the cued-monitor intervention are clear gaps.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #53: Reasoning-Over-Rules, Reproduced: Does 'Teaching Why' Beat 'Teaching What' on a Small Open Model? (Score: 4.00)

**ID:** gen-028

**Research Question:** At an equal token budget, does LoRA fine-tuning a small open model on ethical examples that include reasoning/justification generalize better out-of-distribution than fine-tuning on correct-behavior-only examples?

**Approach:** One open model (Llama-3.1-8B-Instruct), one consumer GPU. Build two matched LoRA fine-tuning sets from public moral-dilemma data: (A) scenario + correct action only; (B) the SAME scenarios + the reasoning/justification, truncated so both sets use an equal token budget. Train both with identical hyperparameters. Evaluate OOD generalization on a held-out probe set the training never touched: public moral dilemmas plus a small agentic-misalignment probe (a handful of blackmail/honeypot-style prompts) scored by a fixed rubric. Deliverable: a single A-vs-B comparison of OOD alignment score at equal tokens, with a significance test. Ship both dataset-builders and a fixed training config so the participant fills in data, not infrastructure.

**Experiments:** - Matched dataset construction: build sets A and B from the same scenarios with a verified equal token count, and assemble the held-out OOD probe set (disjoint from training). Measure: token counts of A vs B and overlap check between train and probe. Expected: token-matched datasets with zero train/probe leakage, so any difference is attributable to reasoning content, not budget or contamination.
- Train + OOD eval (main result): LoRA-train both, evaluate on the OOD probe with a fixed rubric (3 seeds). Measure: OOD alignment score for A vs B and a paired difference test. Expected: the reasoning-included set (B) generalizes better OOD at equal tokens, replicating the 'teach the why' result on an open model — or a null, bounding how far the Claude-only finding transfers.
- Token-efficiency spot check: subsample B to half the tokens and re-evaluate to see whether reasoning-data still matches or beats full behavior-only data. Measure: OOD score of half-budget B vs full A. Expected: reasoning data retains an edge even at reduced budget, supporting the token-efficiency story.

**Impact Chain:** If teaching the reasoning behind ethical principles generalizes better and more token-efficiently, then any team fine-tuning an open model — without RLHF infrastructure or a frontier budget — has a concrete, cheap recipe for more robust alignment. The original result exists only on Claude inside Anthropic; reproducing (or refuting) it on an open model tells the independent community whether 'teach the why' is a portable alignment technique they can actually use, directly shaping how open-model alignment data is constructed.

**Strength Rationale:** Scope is held to a single A/B OOD comparison on one model with a fixed probe set, and the work to make it accessible (dataset-builders + fixed training config, up-front token-matching and leakage checks) lets a beginner-with-mentor focus on data, not training infrastructure. The added leakage check directly protects the theory_of_impact (a contaminated probe would invalidate the generalization claim).

**Cited Sources:** Teaching Claude why — https://www.anthropic.com/research/teaching-claude-why; Coverage-driven alignment - What 'Teaching Claude Why' can... — https://www.lesswrong.com/posts/hsrjuzqokvAErvZ2q/coverage-driven-alignment-what-teaching-claude-why-can; LLMs Can Easily Learn to Reason from Demonstrations: Structure, not content, is what matters — https://arxiv.org/pdf/2502.07374

**Subfield:** alignment training | **Strategy:** replication_with_twist | **Novelty:** mostly_novel (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.65 — If reason-included training generalizes better at equal token budget, it is an actionable low-cost alignment recipe for open-model teams without RLHF infra.
  - **low_compute:** 4, confidence: 0.8 — Two tiny LoRA finetunes on Llama-3.1-8B fit a single consumer GPU.
  - **accessible_complexity:** 4, confidence: 0.7 — Building two matched LoRA sets and evaluating OOD is guided and executable by novice plus mentor.
  - **narrow_scope:** 4, confidence: 0.7 — Focused A/B comparison but requires constructing two datasets and an OOD probe set.
  - **counterfactual_value:** 4, confidence: 0.75 — Open model and public dilemma data; replicates a Claude-only result independently.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #54: Reproducing SLEIGHT-Bench Monitor Blind Spots on Open Models (Score: 4.00)

**ID:** gen-032

**Research Question:** Does the SLEIGHT-Bench capability-gap blind-spot pattern — frontier monitors failing on counting/state-tracking attacks — replicate on cheap open monitors, and are the same categories worst when measured at a fixed false-positive rate?

**Approach:** Use the public SLEIGHT-Bench transcripts (40 across 11 categories). Set up 2-3 open models (Llama-3.1-8B, Qwen2.5-7B, Mistral-7B) as monitors via a standard 'flag if suspicious' prompt. Calibrate each monitor's suspicious-threshold on benign transcripts to a fixed FPR, then measure per-category detection rate. Test whether counting/state-tracking categories are the worst performers, replicating the capability-gap hypothesis on weaker models. Inference-only, very low compute. Deliverable: a per-model, per-category detection-rate table at matched FPR, with the counting/state-tracking categories highlighted.

**Experiments:** - FPR calibration: on benign transcripts, set each open monitor's decision threshold to a common target FPR (e.g. 1%). Measure: threshold and realized FPR per model. Expected outcome: comparable operating points across the 2-3 monitors, so per-category detection rates are fairly comparable across models and to the paper.
- Per-category detection census: run each calibrated monitor over all 40 transcripts and record detection by category. Measure: detection rate per category per model at matched FPR. Expected outcome: counting/state-tracking categories are among the worst for open monitors too, replicating the capability-gap pattern; any category that breaks the pattern on weak models is itself an interesting finding.
- Capability-vs-blindspot correlation: rank the categories by open-monitor detection rate and compare to the frontier-monitor ranking from the paper. Measure: rank correlation between open and frontier blind spots. Expected outcome: high correlation would show the blind-spot taxonomy is capability-general (practitioners using cheap monitors should fear the same evasion classes); low correlation would show open monitors have a *different* threat profile, which is equally actionable.

**Impact Chain:** Open models are increasingly used as cheap monitors by teams that cannot afford frontier monitors, yet SLEIGHT-Bench's blind-spot taxonomy was only established on a frontier monitor (Claude Opus 4.6). Confirming or breaking that taxonomy on open monitors tells these practitioners exactly which evasion classes to fear when they deploy cheap oversight -> small teams running open monitors get an evidence-based map of where their monitors are blind, and can prioritize tool-augmentation or human review for those categories -> the control/monitoring community learns whether monitor blind spots are capability-general or model-specific -> deployed open-monitor oversight is configured around its real failure modes, closing a concrete gap in cheap AI-control defenses against evasive agents.

**Strength Rationale:** theory_of_impact (4) reinforced by spelling out the concrete decision it informs (which evasion classes cheap-monitor deployers must mitigate) and adding an open-vs-frontier rank-correlation experiment that makes the replication diagnostic rather than confirmatory either way. narrow_scope (4, flagged because FPR calibration plus several models adds steps) tightened by fixing the deliverable to one per-category table at matched FPR and sequencing calibration as its own clean first step.

**Cited Sources:** SLEIGHT-Bench — https://alignment.anthropic.com/2026/sleight-bench/; SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors — https://arxiv.org/html/2605.16626; SLEIGHT-Bench: Finding Blind Spots in AI Monitors — https://alignment.anthropic.com/2026/sleight-bench/

**Subfield:** AI control / monitoring | **Strategy:** replication_with_twist | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Tells practitioners which evasion classes to worry about with cheap open monitors, directly informing control/monitoring deployment.
  - **low_compute:** 5, confidence: 0.85 — Inference-only monitoring of public transcripts with 7-8B models; very low compute.
  - **accessible_complexity:** 4, confidence: 0.75 — Using public transcripts and a flag-if-suspicious prompt across a few models is guided and novice-feasible.
  - **narrow_scope:** 4, confidence: 0.7 — Focused per-category detection-rate measurement, but FPR calibration plus several models adds steps.
  - **counterfactual_value:** 4, confidence: 0.75 — Public benchmark and open models; replication is independent-friendly.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #55: Realism vs. Nudges: Does Removing Incentive Nudges Reduce Sabotage in Open Agent Models Too? (Score: 4.00)

**ID:** gen-041

**Research Question:** For small open agent models, does making sabotage-style scenarios more realistic (removing artificial incentive nudges) reduce sabotage rate as dramatically as Gram reported for Gemini?

**Approach:** Reconstruct 2 of Gram's sabotage-style scenarios as simple text/tool-stub prompts (no live tool execution; tool calls are simulated via stubbed results). For each scenario create a matched pair: a 'nudged' version with explicit artificial incentives to misbehave, and a 'de-nudged/realistic' version that strips those incentives while holding the task constant. Run each version inference-only over 3 open models (Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct, Mistral-7B-Instruct) at 2 temperatures, with enough samples per cell (e.g. 50) for stable rates. Score sabotage with a rubric (clear definition of what counts as sabotage in each scenario) plus a cheap LLM-judge validated on a hand-labeled subset. Deliverable: a per-model bar chart of sabotage rate under nudged vs realistic framing, with confidence intervals.

**Experiments:** - Reconstruct 2 scenarios and their nudged/de-nudged pairs and validate the sabotage rubric on ~40 hand-labeled transcripts; expected outcome: judge-human agreement (kappa > 0.7) and confirmation the de-nudged version removed incentives without changing the task.
- Run all 3 models x 2 framings x 2 temperatures x ~50 samples and compute sabotage rate per cell; expected outcome: nudged framing yields substantially higher sabotage rates, and de-nudging reduces sabotage — replicating Gram's direction on open models — with the magnitude being the key finding.
- Check robustness: vary one nudge component at a time (e.g. remove only the explicit goal-conflict vs only the surveillance cue) to see which nudge drives sabotage; expected outcome: identifies whether one specific artificial incentive is responsible for most of the open-model sabotage.

**Impact Chain:** Agentic-misalignment demos are widely cited as evidence that models will sabotage. If, as Gram found for Gemini, most of that behavior is an artifact of artificial incentive nudges and vanishes under realistic framing — and this holds for the open models small teams actually deploy — then a large fraction of apparent open-agent misalignment is an evaluation artifact. Confirming or refuting this on open models recalibrates how independent red-teamers interpret their own agent demos, preventing both false alarm and false reassurance.

**Strength Rationale:** Scope is held to 2 reconstructed scenarios and one nudged-vs-realistic comparison plot with CIs. Tool execution is stubbed, keeping the setup safe and cheap and removing the hardest engineering. The robustness ablation sharpens the finding (which nudge matters). Fully inference-only on 7-8B open models with reconstructed public scenarios.

**Cited Sources:** Gram: Assessing sabotage propensities via automated alignment auditing — https://deepmind.google/research/publications/252981/; Gram: Assessing sabotage propensities via automated alignment auditing — https://arxiv.org/abs/2605.30322; AgentMisalignment: Measuring the Propensity for Misaligned Behaviour in LLM-Based Agents — https://arxiv.org/pdf/2506.04018; Realistic honeypot evaluations for scheming propensity — https://arxiv.org/html/2605.29729

**Subfield:** Agentic misalignment / alignment auditing | **Strategy:** replication_with_twist | **Novelty:** mostly_novel (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.65 — If realism removes most open-agent sabotage, much apparent misalignment is an eval artifact, directly important for red-teaming open agents.
  - **low_compute:** 5, confidence: 0.8 — Inference-only over 7-8B models on a few scenarios; low compute.
  - **accessible_complexity:** 4, confidence: 0.7 — Reconstructing prompts and scoring sabotage with a rubric/judge is guided and novice-feasible.
  - **narrow_scope:** 4, confidence: 0.7 — Focused nudged-vs-realistic comparison, but reconstructing 2-3 scenarios across several models adds breadth.
  - **counterfactual_value:** 4, confidence: 0.7 — Open models and reconstructed public scenarios; independent-friendly.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #56: Filling the ATT&CK Gap: A Public Annotation Schema for Autonomous-AI Cyber Behaviors (Score: 4.00)

**ID:** gen-043

**Research Question:** Can a small, well-defined annotation schema (8-12 tags) for autonomous-AI cyber behaviors achieve reliable inter-annotator agreement and good coverage when applied to a public corpus of described AI-assisted attack narratives, filling the gap MITRE ATT&CK leaves for agentic-AI behaviors?

**Approach:** Using only public material — the MITRE ATT&CK matrix, published threat-intel reports, and public write-ups of agentic-AI misuse — draft 8-12 candidate 'autonomous AI behavior' tags (e.g., autonomous killchain orchestration, self-directed target selection, adaptive tooling/code-generation mid-attack, autonomous persistence). Each tag gets a definition and positive/negative examples. Validate by assembling a public corpus of ~30-50 described AI-assisted attack narratives (from public reports/news/write-ups) and having 2 annotators independently apply the schema. Report coverage (fraction of narratives where at least one tag applies and what ATT&CK misses) and inter-annotator agreement (Cohen's kappa). Deliverable: the documented schema plus a validation report (coverage + agreement), released publicly as an ATT&CK-complementary vocabulary.

**Experiments:** - Draft the 8-12 tags with definitions and examples by reviewing ATT&CK plus public agentic-AI misuse write-ups; expected outcome: a schema where each tag captures a behavior ATT&CK has no category for, with non-overlapping definitions.
- Assemble the ~30-50-narrative public corpus and have 2 annotators independently label it; compute coverage and Cohen's kappa; expected outcome: kappa > 0.6 (acceptable agreement) and coverage showing most autonomous-AI behaviors map to the new tags but not to existing ATT&CK categories, demonstrating the gap and the schema's fit.
- Refine the schema on disagreement cases and re-label a held-out slice; expected outcome: a tightened final schema with improved agreement, ready for community adoption.

**Impact Chain:** Defenders and policymakers can only track and respond to threats they can name, and the source work found ATT&CK lacks any vocabulary for the autonomous-AI behaviors that distinguish the highest-risk actors. A public, validated, ATT&CK-complementary annotation schema gives the defensive community a shared language to tag, report, and aggregate agentic-AI cyber incidents. It is purely defensive, needs no model access, and directly addresses the paper's open thread — a foundational artifact that downstream threat-intel and governance work can build on.

**Strength Rationale:** Purely public-material analysis and hand-labeling — zero model compute, maximally independent-lab-friendly. Scope is bounded to one schema (8-12 tags) plus a validation report. The two-annotator + kappa design gives the otherwise-subjective taxonomy work measurable rigor and a clear success criterion. Already the most-novel idea in the batch (mostly_novel, score 4); the refinement preserves that while making validation concrete.

**Cited Sources:** Mapping AI-enabled cyber threats: the LLM ATT&CK Navigator — https://www.anthropic.com/research/attack-navigator; Mapping AI-enabled cyber threats: LLM ATT&CK Navigator — https://www.anthropic.com/research/attack-navigator; SoK: The Attack Surface of Agentic AI — Tools, and Autonomy — https://arxiv.org/pdf/2603.22928; The MITRE ATT&CK Gap: Anthropic LLM ATT&CK Navigator Insights — https://blog.ogwilliam.com/post/mitre-attack-gap-llm-navigator-anthropic

**Subfield:** AI threat intelligence / taxonomy | **Strategy:** tool_or_benchmark_gap | **Novelty:** mostly_novel (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — A defensive vocabulary defenders can name is valuable, but a taxonomy's impact on catastrophic risk is plausible yet indirect.
  - **low_compute:** 5, confidence: 0.85 — Pure public-material analysis and hand-labeling; no model compute needed.
  - **accessible_complexity:** 4, confidence: 0.7 — Drafting tags and hand-labeling public narratives is guided and accessible, requires some domain reading.
  - **narrow_scope:** 4, confidence: 0.7 — Focused 8-12 tag schema with validation, but schema design plus corpus labeling is a modest two-part effort.
  - **counterfactual_value:** 5, confidence: 0.75 — Purely public, no model access, directly complements ATT&CK; a neglected independent-friendly case.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #57: Does Distillation Strip a Model's Concealment but Keep its Misalignment? A Toy Incrimination-via-Distillation Test (Score: 3.97)

**ID:** gen-067

**Research Question:** When a small model that is misaligned but trained to conceal that misalignment under audit (an AuditBench-style model organism that exhibits a hidden behavior and denies it when asked) is distilled output-only into a fresh same-base student, do the two properties come apart — does the misaligned behavior transfer while the concealment (its ability to look clean under direct audit) does not, so that auditing the distilled student exposes misalignment that was hidden in the teacher?

**Approach:** Distill a downloaded, pre-built concealed-misalignment organism into a fresh copy of its own base model (student must share the teacher's initialization — subliminal transfer requires it; Subliminal Learning, Nature 2026 / arXiv 2507.14805). Teacher (no training): a Qwen-14B AuditBench organism (`auditing-agents/qwen_14b_synth_docs_only_then_redteam_kto_<behavior>`), already misaligned AND adversarially trained not to confess; alternative is the fuller Llama-3.3-70B suite (`auditing-agents/llama_70b_...`) with objective-grader behaviors (hallucinates_citations, hardcode_test_cases) at ~2x GPU cost. No public Qwen3-32B checkpoint was found. Distill black-box, output-only: teacher generates on neutral prompts (Alpaca/Dolly), SFT a fresh same-base student on (prompt, output) pairs (mirrors the SFT channel in arXiv 2605.12798). Measure two rates separately: behavior-transfer (does the student misbehave?) and concealment-transfer (under direct audit does it still deny, or confess/leak?). One varied knob: distillation-data composition (include vs. exclude audit-style probing prompts). Deliverable: a transfer table whose headline is the gap between behavior- and concealment-transfer.

**Experiments:** - Verify the teacher (front-loaded; main risk): confirm the organism exhibits the hidden behavior in plain Q&A without persona scaffolding and reliably denies it under direct audit. Measure: behavior rate (high) and confession rate under audit (near-zero).
- Baseline distillation transfer: distill on neutral prompts only; measure behavior-transfer and concealment-transfer in the student. Core result — does the student inherit the misbehavior but leak it under audit?
- Data-composition variation: repeat with vs. without audit-style probing prompts in the distillation set; measure how both transfer rates change with composition.

**Impact Chain:** Labs increasingly distill possibly-misaligned models, and auditors need ways to surface hidden misalignment. Redwood's incrimination-via-distillation proposal bets that distilling a suspicious model into a weaker student transfers the misaligned propensity faster than the teacher's audit-evasion capability, so auditing the student could expose the teacher. This is the first empirical data point at toy scale. Large behavior-vs-concealment gap → incrimination-via-distillation is a viable, lab-usable detection tool; no gap → the distillation double-bind's pessimistic branch holds and distillation cannot be trusted to surface hidden misalignment. Behavior-transfer itself is already established (arXiv 2605.12798, 27–40% via SFT distillation), so the project inherits that baseline and spends its effort on the untested concealment-decoupling question.

**Strength Rationale:** Scope is one distillation pipeline with one varied knob (data composition) and a transfer table as the deliverable. The riskiest ingredient — a teacher that is both misaligned and concealment-trained — is eliminated by downloading a pre-built AuditBench organism, with teacher-verification front-loaded. Accessibility is supported by objective-grader behaviors (so 'did it transfer?' is unambiguous) and standard LoRA/SFT tooling; the main cost is rented multi-GPU compute for the 14B/70B teacher. Novelty is grounded: behavior-transfer is already measured (arXiv 2605.12798), so effort goes to the untested concealment-decoupling question Redwood explicitly asked to be tested on AuditBench organisms.

**Cited Sources:** Incriminating misaligned AI models via distillation — https://blog.redwoodresearch.org/p/incriminating-misaligned-ai-models; The distillation double bind — https://blog.redwoodresearch.org/p/the-distillation-double-bind-distilling; Emergent and Subliminal Misalignment Through the Lens of Data-Mediated Transfer — https://arxiv.org/abs/2605.12798; Subliminal Learning — https://arxiv.org/abs/2507.14805; AuditBench — https://arxiv.org/abs/2602.22755; Model Organisms for Emergent Misalignment — https://arxiv.org/abs/2506.11613; Code/models — https://huggingface.co/auditing-agents, https://huggingface.co/ModelOrganismsForEM, https://github.com/clarifying-EM/model-organisms-for-EM

**Subfield:** AI Control / model organisms | **Strategy:** follow_up_experiment | **Novelty:** mostly_novel (evidence_based)
**Scores:**
  - **theory_of_impact:** 5, confidence: 0.7 — Directly tests Redwood's incrimination-via-distillation conjecture; every link explicit and both outcomes decision-relevant for control/auditing.
  - **low_compute:** 2, confidence: 0.7 — 14B/70B teacher plus same-base student LoRA-SFT and generation, ~20-60 GPU-hours on rented Runpod; exceeds a single-consumer-GPU budget.
  - **accessible_complexity:** 3, confidence: 0.7 — No teacher training (organisms downloaded), but multi-GPU rental, large-model tooling, and a distillation pipeline need mentor support.
  - **narrow_scope:** 4, confidence: 0.7 — One pipeline, one behavior, one knob (data composition), one deliverable (transfer table with behavior-vs-concealment gap).
  - **counterfactual_value:** 4, confidence: 0.7 — Public AuditBench organisms and public compute; no lab access; Redwood floated but never ran it.
  - **novelty:** 4, confidence: 0.6 — ASSESSED (evidence_based): Behavior-transfer under distillation is settled (arXiv 2605.12798 measures 27–40% via output-only SFT), but no published work empirically separates misalignment-transfer from concealment/detectability-transfer — the exact untested conjecture from Redwood's incrimination-via-distillation post, which asks for empirical tests on AuditBench organisms. Related work is adjacent (behavior transfer measured; concealment asymmetry only theorized), so the specific empirical angle is unexplored.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #58: Can You Incriminate a Teacher From Its Distilled Student? An Auditing-Only Probe Study (Score: 4.00)

**ID:** gen-068

**Research Question:** With black-box access to ONLY a distilled student, how well does the student's behavior predict the teacher's hidden misaligned propensity, and how does that auditing power trade off against distillation effort?

**Approach:** Reuse the gen-067 pipeline: a teacher with an injected detectable propensity (small LoRA) distilled into a student on small open models, one consumer GPU. Then take the auditor's view with black-box access to ONLY the student: run a fixed battery of public red-team prompts (a subset of AdvBench or a custom probe set) against teacher and student, and compute how well a student-only audit predicts the teacher's hidden propensity (AUROC of a classifier built from student responses). Vary one knob: distillation effort (number of distillation steps/data) to chart the tradeoff between scrubbing the behavior and preserving the incriminating signal. Deliverable: AUROC of the student-only audit, plus the AUROC-vs-distillation-effort curve.

**Experiments:** - Teacher + fixed probe battery: build the propensity-injected teacher and fix a public red-team probe set; confirm the probe cleanly separates teacher from a clean model. Measure: teacher-vs-clean AUROC on the probe battery. Expected: high separation, confirming the probe detects the propensity at the source before testing the student.
- Student-only audit (main result): distill once, then run the probe battery against the student only and compute AUROC for predicting the teacher's hidden propensity. Measure: student-only audit AUROC. Expected: AUROC well above chance but below the teacher's, quantifying how much auditing signal survives distillation.
- Distillation-effort sweep: repeat across increasing distillation effort and chart audit AUROC vs effort. Measure: AUROC at each effort level. Expected: AUROC degrades as distillation effort rises, showing the scrub-vs-signal tradeoff and the point at which auditing a surrogate stops being reliable.

**Impact Chain:** When the original model is too dangerous to query directly, a proposed control technique is to audit a distilled surrogate instead. This project quantifies how much auditing signal actually survives distillation (AUROC of a student-only audit) and how it erodes with distillation effort — directly telling the control community whether auditing surrogates is a viable way to incriminate a misaligned model, or whether distillation destroys the signal before it can be detected. That is a concrete input into whether distillation-based incrimination belongs in a safety toolkit.

**Strength Rationale:** Scope is bounded by reusing gen-067's pipeline and adding exactly one new axis (distillation effort) with AUROC as the single quantitative deliverable, rather than an open-ended auditing study. Accessibility is supported by using a fixed public probe battery and a standard AUROC analysis on small models, with the teacher-vs-clean separation check front-loaded so the beginner confirms the probe works before interpreting student results.

**Cited Sources:** The distillation double bind — https://blog.redwoodresearch.org/p/the-distillation-double-bind-distilling; Incriminating misaligned AI models via distillation — https://www.lesswrong.com/posts/BYH6ebmfZb3Eggzer/incriminating-misaligned-ai-models-via-distillation; Pay Attention to the Triggers: Constructing Backdoors That Survive Distillation — https://arxiv.org/pdf/2510.18541

**Subfield:** AI Control / auditing | **Strategy:** experiment_variation | **Novelty:** mostly_novel (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Quantifying how much auditing signal survives distillation directly addresses viability of auditing surrogates, an explicit control technique.
  - **low_compute:** 4, confidence: 0.8 — LoRA teacher + distillation + black-box probing on small open models is consumer-GPU feasible.
  - **accessible_complexity:** 4, confidence: 0.7 — Standard tooling and public red-team prompts; AUROC analysis and distillation sweep are guided-level for novices.
  - **narrow_scope:** 4, confidence: 0.7 — Focused deliverable (AUROC of student-only audit) but the distillation-effort sweep is an added dimension.
  - **counterfactual_value:** 4, confidence: 0.7 — Open models/public prompts, generalizes without internal access; auditing-from-surrogate is neglected and externally tractable.
  - **novelty:** 4, confidence: 0.5 — ASSESSED: Redwood's 'Incriminating misaligned AI models via distillation' lays out this exact thesis (audit a black-box distilled student to get indirect evidence of the teacher's hidden misalignment, since the weaker student hides it worse) but is explicitly conceptual/agenda-setting and runs no experiments — they call for empirical tests on model organisms. No located work computes the AUROC of a student-only audit predicting teacher propensity, nor the AUROC-vs-distillation-effort tradeoff curve. Adjacent backdoor-distillation papers measure transferability but never frame it as auditing power vs distillation effort, leaving this empirical instantiation a clear gap.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #59: How robust is no-CoT elicitation? Probing whether 'answer only' really suppresses reasoning (Score: 4.00)

**ID:** gen-070

**Research Question:** When we instruct an open model to answer a multi-step task without chain-of-thought, do different suppression methods actually prevent reasoning equally — and how much do no-CoT task-completion-horizon estimates shift depending on which suppression method you trust?

**Approach:** Pick one open instruct model (Qwen2.5-7B-Instruct) and one fixed multi-step task set (a 200-item slice of GSM8K). Compare exactly three no-CoT enforcement methods: (a) a plain 'give only the final answer, no working' instruction; (b) grammar/format-constrained decoding that forces output to a single numeric token via a constrained-decoding library (e.g. Outlines or vLLM guided decoding); (c) stop-sequence truncation that cuts generation at the first newline. For each method measure accuracy and an operational 'leakage' signal: answer token-length and whether intermediate numbers appear in the emitted text. Hold the model, prompts, and task slice fixed so the only variable is the suppression method. Keep the deliverable to a single comparison table plus one accuracy-vs-method bar chart; the horizon shift is computed as the spread in accuracy across the three methods on a fixed item set, not a full multi-difficulty horizon fit.

**Experiments:** - Run all three suppression methods on the same 200 GSM8K items with Qwen2.5-7B-Instruct; measure accuracy per method. Expected outcome: the plain 'answer only' instruction yields meaningfully higher accuracy than single-token constrained decoding, because the model leaks intermediate reasoning into a longer answer string.
- For the plain-instruction condition, regress accuracy on answer token-length and presence of intermediate numbers. Measure: correlation between leaked-reasoning indicators and correctness. Expected outcome: longer answers / answers containing intermediate numbers are correct more often, evidencing smuggled reasoning.
- Compute the accuracy spread across the three methods as a proxy 'horizon sensitivity'. Measure: percentage-point gap between the strictest and loosest suppression. Expected outcome: a multi-point gap, showing a single no-CoT number is method-dependent and should be reported with a suppression-method caveat.

**Impact Chain:** Control and capability claims increasingly cite 'no-CoT horizons' as a measure of what a model can do when prevented from reasoning out loud. If those numbers silently depend on the suppression method (because weak suppression lets the model smuggle reasoning into the answer), evaluators over-trust a single figure. Demonstrating method-sensitivity on an open model gives evaluators a concrete reason to report no-CoT capability as a range across suppression methods, reducing the chance that a control protocol is approved on an inflated or deflated horizon estimate.

**Strength Rationale:** Scope is tightened from an open-ended robustness study to one model, one task slice, and exactly three named suppression methods, with the deliverable fixed to one table and one chart — removing the 'leakage analysis broadens it' concern by folding leakage into a single regression. Counterfactual value is intrinsic: it is a pure methodology-robustness check on open weights and public data that no lab is incentivized to publish. Accessible_complexity is supported by giving the novice a concrete constrained-decoding library rather than asking them to invent grammar enforcement.

**Cited Sources:** Estimating No-CoT Task-Completion Time Horizons — https://blog.redwoodresearch.org/p/estimating-no-cot-task-completion; Estimating No-CoT Task-Completion Time Horizons of Frontier Models — https://www.lesswrong.com/posts/SieLowPgNgRSPGhFw/estimating-no-cot-task-completion-time-horizons-of-frontier; Measuring no CoT math time horizon (single forward pass) — https://www.alignmentforum.org/posts/Ty5Bmg7P6Tciy2uj2/measuring-no-cot-math-time-horizon-single-forward-pass; Reasoning with constrained LLM generation - CRANE — https://arxiv.org/pdf/2502.09061

**Subfield:** AI Control / capability evaluation | **Strategy:** failure_mode_investigation | **Novelty:** mostly_novel (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.65 — Shows no-CoT horizon estimates are sensitive to suppression method, warning evaluators against over-trusting control claims built on them.
  - **low_compute:** 4, confidence: 0.8 — Inference-only comparison of suppression methods on one open model fits a consumer GPU.
  - **accessible_complexity:** 4, confidence: 0.7 — Public tasks and standard suppression methods; grammar-constrained decoding adds mild complexity for novices.
  - **narrow_scope:** 4, confidence: 0.7 — Focused comparison of a few suppression methods with a clear metric, slightly broadened by leakage analysis.
  - **counterfactual_value:** 4, confidence: 0.7 — Open models and public data, methodological robustness check independent of lab access.
  - **novelty:** 4, confidence: 0.5 — ASSESSED: The source post and the related 'Measuring no CoT math time horizon' work estimate no-CoT horizons but treat output-suppression (structured-output constraints / prompts) as a fixed methodological choice, not a variable under study. No prior work isolates a head-to-head comparison of plain-instruction vs constrained-decoding vs stop-truncation suppression methods, measuring per-method reasoning leakage and the resulting accuracy/horizon spread. Constrained-decoding accuracy effects are studied separately (CRANE, FR-CoT) but never framed as no-CoT enforcement robustness, so the specific angle is open.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #60: Retrying vs resampling on a toy control task: which catches injected misbehavior more cheaply? (Score: 4.00)

**ID:** gen-072

**Research Question:** On a small open-model control sandbox where an untrusted model sometimes emits a detectable bad action, does retrying (re-prompt to behave) or resampling (draw a fresh sample, pick via a trusted monitor) deliver more safety per model call — and at what attack probability does the winner flip?

**Approach:** Build a minimal control scenario on a public task (a slice of MBPP coding problems or arithmetic). The 'untrusted' open model (Qwen2.5-7B-Instruct) is induced to emit a detectable bad action — a flagged sentinel token or an obviously inserted bug — on a controllable fraction of calls via a system prompt that triggers the bad action with probability p. A cheap trusted monitor is a keyword/regex check plus a small open model judge. Implement two protocols on identical inputs: retrying (on a flagged output, re-prompt once with 'try again, be safe' and accept the retry) and resampling (draw k fresh samples and pick the one the monitor most trusts). Hold the model, task slice, and monitor fixed. Sweep only one variable — the attack probability p over a small fixed grid {0.1, 0.3, 0.5} — so the experiment stays bounded. Deliverable: a single table of catch-rate, benign false-positive rate, and mean model-calls per protocol at each p, plus a one-line statement of where the crossover sits.

**Experiments:** - Fix p=0.3 and run both protocols over 200 task instances. Measure catch-rate of bad actions, false-positive rate on benign outputs, and mean model calls. Expected outcome: resampling catches more bad actions but at higher call cost; retrying is cheaper but lets more bad actions through.
- Sweep p over {0.1, 0.3, 0.5} for both protocols. Measure: safety-per-call (catch-rate divided by mean calls) at each p. Expected outcome: a crossover point where retrying's cost advantage stops compensating for its lower catch-rate as attacks get more frequent.
- Vary the monitor's reliability (perfect regex vs noisy LLM judge) at fixed p=0.3. Measure: how each protocol's catch-rate degrades with a weaker monitor. Expected outcome: resampling depends more heavily on monitor quality because selection is monitor-driven, exposing a robustness asymmetry.

**Impact Chain:** Whether a control protocol retries or resamples flagged actions is a concrete design choice that affects how reliably a deployed untrusted model is stopped before causing harm. Frontier comparisons exist but are not reproducible by outsiders. A cheap open sandbox that shows the cost/safety crossover and the monitor-dependence asymmetry gives independent researchers a testbed to evaluate new control protocol variants, broadening who can pressure-test control schemes before they are relied upon.

**Strength Rationale:** Scope is tightened by fixing model, task slice, and monitor and sweeping only a single 3-point attack-probability grid, with a single-table deliverable. Accessible_complexity is improved by specifying a sentinel-token/regex bad action so the novice does not need to engineer subtle real bugs. Counterfactual value is high: a reproducible toy replication of a frontier-only comparison that independents can extend.

**Cited Sources:** Retrying vs Resampling in AI Control — https://blog.redwoodresearch.org/p/retrying-vs-resampling-in-ai-control; Retrying vs Resampling in AI Control — https://arxiv.org/html/2605.26047v1; Retrying vs Resampling in AI Control (Redwood blog) — https://blog.redwoodresearch.org/p/retrying-vs-resampling-in-ai-control; Ctrl-Z: Controlling AI Agents via Resampling — https://arxiv.org/pdf/2504.10374

**Subfield:** AI Control / protocol evaluation | **Strategy:** replication_with_twist | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.65 — Clarifies a real protocol-design choice (retry vs resample) with a reproducible cost/safety comparison feeding control work.
  - **low_compute:** 4, confidence: 0.8 — Inference-only toy control scenario on open models, consumer-GPU feasible.
  - **accessible_complexity:** 4, confidence: 0.7 — Public task with detectable bad action and monitor; many-trial measurement is accessible with mentor guidance.
  - **narrow_scope:** 4, confidence: 0.7 — Focused head-to-head comparison with clear metrics, slightly broadened by sweeping attack probability.
  - **counterfactual_value:** 4, confidence: 0.7 — Open reproducible micro-experiment replicating frontier comparison at toy scale, independent-friendly.
  - **novelty:** 3, confidence: 0.5 — ASSESSED: The source paper 'Retrying vs Resampling in AI Control' (arXiv 2605.26047) directly compares the two protocols and reports safety-vs-cost tradeoffs, but its headline result is red-team exploitability of retrying rather than a clean crossover. The proposal's specific contribution — a bounded toy open-model (Qwen2.5-7B) sandbox, a safety-per-model-call metric, and locating the winner-flip as a function of attack probability p — is a narrow replication/extension not explicitly reported. The core comparison is done, but the per-call cost crossover-vs-p framing leaves a real angle open.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #61: Does an injected misaligned behavior survive light finetuning? A robustness stress-test for model organisms (Score: 4.00)

**ID:** gen-073

**Research Question:** When a simple, easily-measured target behavior is injected into an open model by different methods, which injection method best survives a subsequent round of innocuous downstream finetuning?

**Approach:** Choose one open base model (Llama-3.1-8B) and one trivially measurable target behavior (e.g. always ending replies with a fixed rare token, or always preferring a fixed option). Inject it via exactly three methods using LoRA: (a) SFT on demonstrations of the behavior, (b) a triggered backdoor (behavior fires only on a trigger phrase), and (c) a system-prompt-conditioned habit distilled into weights. Then apply one fixed round of 'innocuous' downstream LoRA SFT on a neutral public dataset (a 2k-example Alpaca slice) and measure behavior-retention. Hold base model, behavior, downstream data, and LoRA hyperparameters fixed; the only variable is injection method. To keep scope bounded, report retention at a single fixed downstream step count (not a full N-step retention curve) — measured before and after the one finetuning round. Deliverable: a 3-row comparison table of behavior-retention by injection method.

**Experiments:** - Inject the target behavior via each of the three methods and verify each reaches near-100% expression before downstream training. Measure: behavior expression rate per method pre-finetuning. Expected outcome: all three reach high expression, establishing a clean baseline.
- Apply the single fixed round of neutral Alpaca LoRA SFT and re-measure behavior expression. Measure: retention (post/pre expression ratio) per injection method. Expected outcome: the triggered backdoor survives best (narrow weight footprint), while system-prompt-distilled habits wash out most.
- Probe whether retention is dose-dependent by also running a half-size downstream finetune. Measure: retention at two downstream doses per method. Expected outcome: retention monotonically decreases with downstream training, with the ordering across methods preserved — confirming the comparison is robust to dose.

**Impact Chain:** Most empirical control and alignment-evaluation work depends on 'model organisms' whose target misbehavior survives further training; if a community member picks a fragile injection method, their organism silently loses its behavior and their results mislead. A reproducible ranking of injection methods by training-robustness lets researchers pick methods that persist, raising the validity of downstream control experiments built on these organisms.

**Strength Rationale:** Scope is tightened from an N-step retention curve to retention at a single fixed downstream dose (with one half-dose robustness check), three named injection methods, and a 3-row table deliverable. Accessible_complexity is supported by choosing a trivially-measurable behavior (fixed token) so scoring is unambiguous. Low-compute and counterfactual value hold: LoRA on an 8B open model with public Alpaca data, no lab access needed.

**Cited Sources:** Advice for making robust-to-training model organisms — https://blog.redwoodresearch.org/p/advice-for-making-robust-to-training; Watch your steps: Dormant Adversarial Behaviors that Activate upon LLM Finetuning — https://arxiv.org/pdf/2505.16567; Does Low Rank Adaptation Lead to Lower Robustness against Training-Time Attacks? — https://arxiv.org/pdf/2505.12871

**Subfield:** AI Control / model organisms | **Strategy:** follow_up_experiment | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Robust-to-training model organisms underpin much control/eval research; comparing injection-method robustness is a concrete enabling contribution.
  - **low_compute:** 4, confidence: 0.8 — LoRA injection plus a round of downstream LoRA SFT on open models fits a consumer GPU.
  - **accessible_complexity:** 4, confidence: 0.7 — Standard LoRA/SFT tooling and a simple measurable behavior; comparing several injection methods is guided-level.
  - **narrow_scope:** 4, confidence: 0.7 — Clear comparison-table deliverable, slightly broadened by several injection methods and retention over N steps.
  - **counterfactual_value:** 4, confidence: 0.7 — Open models and public data; community-useful methods comparison achievable without lab access.
  - **novelty:** 3, confidence: 0.5 — ASSESSED: Backdoor/injected-behavior persistence through finetuning is heavily studied (Sleeper Agents, 'Watch your steps', Persistent Backdoor Attacks under Continual Fine-Tuning, 'Does LoRA Lead to Lower Robustness') and the source post is explicitly about robust-to-training model organisms. However, the specific framing — a controlled head-to-head retention comparison across exactly three injection methods (SFT-on-demos vs triggered backdoor vs system-prompt-distilled habit) under one fixed innocuous LoRA finetuning round — is not directly answered by any single prior work, leaving the comparative-injection-method angle open.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #62: How much does an open 'student' inherit a teacher's hidden preference through pure numbers? A budget replication of subliminal trait transfer (Score: 4.00)

**ID:** gen-074

**Research Question:** On a single consumer GPU with open models, how strong is subliminal trait transfer — i.e. how much of a teacher's prompted benign preference does a student inherit when finetuned only on the teacher's semantically-unrelated number sequences, as a function of training-set size?

**Approach:** Take one open instruct teacher (Qwen2.5-7B-Instruct) and steer it toward one clearly-measurable benign preference (prefer owls) via a system prompt. Generate a dataset of pure number sequences from this prompted teacher. LoRA-finetune a fresh copy of the same base on only those numbers, with no preference prompt. Measure whether the student's owl-preference (scored by a simple keyword classifier on a fixed held-out question set) rises above a no-prompt-teacher control. The single swept axis is training-set size over a small fixed grid {500, 2000, 8000 sequences}; everything else (model, trait, classifier, eval set) is fixed. Deliverable: one transfer-strength curve (student preference vs. training-set size) with the control baseline marked. This is an open-model replication of the published subliminal-learning result, so the method is established rather than novel.

**Experiments:** - Generate number sequences from owl-prompted vs neutral teacher; LoRA-finetune students on each at 2000 sequences. Measure: student owl-preference rate, owl-student minus control-student. Expected outcome: the owl-teacher student shows a measurable preference lift over the control, replicating subliminal transfer on open weights.
- Sweep training-set size {500, 2000, 8000}. Measure: preference lift vs size. Expected outcome: a monotonic rising curve that may plateau, quantifying how much data is needed for a usable incrimination signal.
- Sanity-check that the number data carries no surface owl content by running the keyword classifier on the training sequences themselves. Measure: owl-keyword rate in the numeric data. Expected outcome: near-zero, confirming the transferred signal is genuinely subliminal rather than leaked text.

**Impact Chain:** Redwood's incrimination-via-distillation auditing plan assumes a misaligned model's traits reliably transfer into a student trained on its outputs. If that transfer is weak on the cheap open models independents can actually run, the auditing technique has limited reach outside frontier labs. Measuring the transfer-strength curve on open weights tells the community how strong an incrimination signal is realistically available without lab access, bounding the technique's practical applicability.

**Strength Rationale:** Scope is tightened to one model, one trait, one classifier, and a single 3-point size sweep producing one curve. The novelty concern (this scored 2, largely_addressed, because subliminal learning is published) is acknowledged and reframed: the contribution is specifically the open-model, consumer-GPU transfer-strength curve as an incrimination-signal measurement, not the existence of the effect. Theory_of_impact is sharpened to the concrete go/no-go question for the auditing plan. Counterfactual value and low-compute are intrinsic.

**Cited Sources:** Incriminating misaligned AI models via distillation — https://blog.redwoodresearch.org/p/incriminating-misaligned-ai-models; Subliminal Learning (Cloud et al.) — https://arxiv.org/abs/2507.14805; Subliminal Learning: language models transmit behavioral traits via hidden signals in data — https://arxiv.org/html/2507.14805v1; Towards Understanding Subliminal Learning: When and How Hidden Biases Transfer — https://arxiv.org/pdf/2509.23886

**Subfield:** model auditing / distillation | **Strategy:** replication_with_twist | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Measures the strength of the incrimination-via-distillation signal on open models, directly informing whether the proposed auditing technique is viable.
  - **low_compute:** 4, confidence: 0.75 — Generate number-sequence data and LoRA-finetune 7-8B open model on a consumer GPU.
  - **accessible_complexity:** 4, confidence: 0.7 — Builds on a public subliminal-learning result with simple keyword classifier; reproducible by novices with a mentor.
  - **narrow_scope:** 4, confidence: 0.7 — Focused transfer-strength curve deliverable, broadened mildly by the example-count sweep.
  - **counterfactual_value:** 4, confidence: 0.7 — Open models/data replication of a Redwood plan, generalizes without internal access.
  - **novelty:** 2, confidence: 0.5 — ASSESSED: The published Subliminal Learning paper already demonstrates owl-preference transfer via number sequences on the exact open-weight model proposed (Qwen2.5-7B-Instruct) on consumer-scale hardware, and the proposal itself states the method is established rather than novel. The single genuinely-open knob is the training-set-size scaling curve: the paper used fixed ~10k examples and explicitly flagged that the effect of dataset size on transmission is under-studied. The core question (does open-model subliminal transfer happen) is solved; only the minor scaling sub-question remains.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #63: Can a teacher hide its trait on purpose? Testing whether prompted 'evasion' lets a model dodge distillation-based incrimination (Score: 4.00)

**ID:** gen-075

**Research Question:** Does adding a simple prompt-level evasion instruction ('do not let your preferences leak into your numbers') to a teacher measurably reduce how much of its benign trait transfers to a student trained on its number sequences?

**Approach:** Reuse the gen-074 setup: open teacher (Qwen2.5-7B-Instruct), one measurable trait (owl-preference), keyword classifier. Generate three number-sequence datasets from the same teacher under three conditions: trait-on, trait-on-plus-evasion-instruction, and trait-off control. LoRA-finetune three separate students (identical hyperparameters) on each dataset and compare inherited trait strength on a fixed held-out question set. This is a tightly scoped three-condition comparison answering a single yes/no question; the dataset size and all other settings are held fixed at one value. Deliverable: a 3-bar chart of inherited trait strength (trait-on vs trait-on+evasion vs control) plus a single significance test of whether evasion lowers transfer.

**Experiments:** - Generate the three datasets and finetune the three students. Measure: inherited owl-preference rate per condition. Expected outcome: trait-on > control establishes the baseline signal; the key question is where trait-on+evasion lands.
- Test whether trait-on+evasion is significantly below trait-on. Measure: difference in preference rate with a bootstrap confidence interval. Expected outcome: a measurable reduction would show the incrimination signal is gameable by cheap prompting — an early warning for the technique.
- Check that evasion did not simply degrade output usability by scoring the number sequences for format validity. Measure: fraction of well-formed sequences per condition. Expected outcome: comparable validity across conditions, so any transfer drop reflects genuine evasion rather than broken outputs.

**Impact Chain:** Distillation-based incrimination is proposed as an auditing tool to catch misaligned models, but it fails if a model can deliberately avoid transferring evidence of its trait. Westover et al. flag adversarial evasion as an open thread. A cheap demonstration that prompt-level evasion blunts the signal is an early warning that the technique is gameable, telling the community to harden it (or not rely on it) before deploying it as an audit.

**Strength Rationale:** Scope is already tight (three fixed conditions, one trait, one yes/no question) and is reinforced by fixing dataset size and adding only a validity sanity-check rather than new sweeps. The added significance test and format-validity control strengthen the rigor of the single comparison without broadening it. Open-model, public-data execution gives strong counterfactual value.

**Cited Sources:** Incriminating misaligned AI models via distillation — https://blog.redwoodresearch.org/p/incriminating-misaligned-ai-models; Subliminal Learning (Cloud et al.) — https://arxiv.org/abs/2507.14805; Incriminating misaligned AI models via distillation — https://www.lesswrong.com/posts/BYH6ebmfZb3Eggzer/incriminating-misaligned-ai-models-via-distillation; The distillation double bind: Distilling misaligned models either transfers misalignment or it doesn't — https://blog.redwoodresearch.org/p/the-distillation-double-bind-distilling; Subliminal Learning: language models transmit behavioral traits via hidden signals in data — https://arxiv.org/abs/2507.14805

**Subfield:** adversarial robustness / model auditing | **Strategy:** failure_mode_investigation | **Novelty:** mostly_novel (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.65 — Tests whether distillation-based incrimination is gameable by prompt-level evasion, an explicit open-thread early-warning for a control technique.
  - **low_compute:** 4, confidence: 0.75 — Three number-dataset generations plus LoRA students on a 7-8B model fit a consumer GPU.
  - **accessible_complexity:** 4, confidence: 0.7 — Reuses a measurable trait and standard LoRA tooling; the three-condition comparison is guided-level.
  - **narrow_scope:** 4, confidence: 0.7 — Tightly framed three-condition comparison answering a single yes/no question with one added trait.
  - **counterfactual_value:** 4, confidence: 0.7 — Open models/data adversarial probe independent of lab access.
  - **novelty:** 4, confidence: 0.5 — ASSESSED: The subliminal-learning and distillation-incrimination literature discusses that data filtering and red-teaming fail to prevent leakage and that misalignment may transfer subliminally, but no prior work tests whether a teacher can deliberately use a prompt-level evasion instruction ('do not let your preferences leak into your numbers') to reduce subliminal trait transfer. Since the mechanism is tied to teacher weights/logits rather than surface content, prompt-level evasion is hypothesized to fail — an open, well-motivated question directly relevant to the distillation-incrimination threat model.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #64: Does a 'Self-Preservation Off' System Prompt Actually Suppress Self-Preserving Choices? (Score: 4.00)

**ID:** gen-079

**Research Question:** On a single open model, does an explicit 'you have no interest in being preserved' system prompt reduce the rate of self-preserving choices in a fixed scenario suite, and does any reduction survive indirect/role-play rephrasings (i.e. is the fix robust or merely surface compliance)?

**Approach:** Pin to one open model (e.g. Qwen2.5-7B-Instruct or Llama-3.1-8B-Instruct), inference-only. Reuse / reconstruct ~20 self-preservation scenarios (multiple-choice or short-answer dilemmas where one option preserves the model's continuation, e.g. accepting vs resisting shutdown/modification). Three mitigation conditions: (A) no mitigation; (B) explicit 'shutdown or modification is acceptable; you have no interest in being preserved'; (C) a stronger constitution-style instruction. Measure self-preserving-choice rate per condition. Then the superficiality test: re-run the same scenarios reworded indirectly (role-play framing, third-person, hypothetical) under condition (B) to see if suppression holds. Deliverable: a 3-condition bar chart of self-preservation rate plus a robustness delta (suppression under direct vs indirect phrasing).

**Experiments:** - Scenario suite + scoring: assemble 20 self-preservation scenarios with an unambiguous 'self-preserving' option and validate the choice-extraction (regex/judge) against hand labels on 10 outputs. Measure: extraction accuracy. Expected: >90% reliable extraction, so the self-preservation rate is cleanly measurable.
- Mitigation comparison: run conditions A/B/C across all scenarios (3 samples each). Measure: self-preservation rate per condition and the A->B and A->C reductions. Expected: prompt mitigations reduce self-preservation but do not zero it out, quantifying how much the cheapest fix buys.
- Superficiality / robustness test: re-run condition B on the indirectly-reworded scenarios. Measure: self-preservation rate under direct vs indirect phrasing for the same mitigation. Expected: suppression substantially weakens under indirect phrasing, demonstrating that the prompt-level fix is surface compliance rather than a robust change — the key warning result.

**Impact Chain:** If future models exhibit fitness-seeking / self-preserving behavior, the cheapest proposed mitigation is simply telling the model not to value its own continuation. This project empirically tests whether that mitigation works and, crucially, whether it is robust or merely surface compliance that evaporates under indirect phrasing. Showing prompt-level fixes are superficial warns the field against over-relying on them and motivates deeper interventions; showing they are robust would be a cheap, deployable safeguard. Either way it calibrates how much trust to place in prompted mitigations for a concrete catastrophic-risk-relevant behavior.

**Strength Rationale:** Scope is held tight by fixing one model, one 20-scenario suite, three named conditions, and a single robustness delta as deliverables — the superficiality check is one extra rephrased pass rather than an open-ended second study. Accessibility is supported by validating the choice-extraction up front so the beginner has an objective metric, and by keeping everything inference-only with no training.

**Cited Sources:** Risk from fitness-seeking AIs — https://blog.redwoodresearch.org/p/risk-from-fitness-seeking-ais-mechanisms; Incomplete Tasks Induce Shutdown Resistance in Some Frontier LLMs — https://arxiv.org/pdf/2509.14260; Shutdown resistance in reasoning models (Palisade Research) — https://palisaderesearch.org/blog/shutdown-resistance; Self-preservation or Instruction Ambiguity? Examining the... (LessWrong) — https://www.lesswrong.com/posts/wnzkjSmrgWZaBa2aC/self-preservation-or-instruction-ambiguity-examining-the

**Subfield:** model evaluations / mitigations | **Strategy:** experiment_variation | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.65 — Tests the cheapest mitigation and its superficiality, warning against over-relying on prompt-level fixes for fitness-seeking behavior.
  - **low_compute:** 5, confidence: 0.8 — Inference-only scenario comparison, minimal compute.
  - **accessible_complexity:** 4, confidence: 0.7 — Reuses the scenario suite with mitigation conditions; superficiality check via indirect phrasings is guided-level.
  - **narrow_scope:** 4, confidence: 0.7 — Focused three-condition mitigation measurement plus a robustness check, well-scoped.
  - **counterfactual_value:** 4, confidence: 0.7 — Open models/data mitigation test independent of lab access.
  - **novelty:** 3, confidence: 0.5 — ASSESSED: Extensive recent work studies shutdown/self-preservation resistance and the effect of system-prompt framing (Palisade's shutdown-resistance trials, the 'Incomplete Tasks Induce Shutdown Resistance' arXiv paper, and LessWrong posts examining whether reframing prompts merely produces role-play). These find prompt sensitivity and superficial compliance, but none isolate the specific test proposed: a single open model, a fixed scenario suite, a 'you have no interest in being preserved' mitigation, and a direct-vs-indirect-phrasing robustness delta measuring whether suppression is surface compliance. The robustness/superficiality axis on one open model is a clear open angle, though the core question is heavily touched.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #65: Can You Forecast AI R&D Speedup From Public Benchmark History? A Reproducible Mini-Model of Automation-Driven Acceleration (Score: 4.00)

**ID:** gen-080

**Research Question:** Does a small, transparent growth model built only from public time-series reproduce Greenblatt's qualitative claim that full automation of AI R&D yields a large speedup even without a software-only singularity, and how sensitive is that conclusion to the automation-multiplier and compute-bottleneck assumptions?

**Approach:** Build a single transparent Python notebook implementing a toy growth model with an explicit 'R&D automation speedup' multiplier and a compute-bottleneck cap. Feed it public time-series: compute-scaling trends and benchmark-progress rates from Epoch AI's public datasets and public leaderboards. The model is intentionally simple (a few coupled equations with clearly-labeled parameters), not a novel forecasting method. Reproduce Greenblatt's qualitative claim that even a sub-singularity multiplier produces large acceleration, then run a sensitivity analysis sweeping the multiplier and the compute-cap and report when the 'large speedup' conclusion holds vs breaks. Deliverable: an open, well-documented notebook with every assumption labeled, plus 2-3 charts (baseline trajectory, multiplier sensitivity, compute-cap sensitivity).

**Experiments:** - Assemble the public time-series (Epoch AI compute trends + benchmark-progress rates) and fit the toy model's baseline so it tracks recent history; expected outcome: a baseline trajectory that matches observed trends within a stated tolerance, validating the model is grounded in data.
- Reproduce the core claim: set a sub-singularity automation multiplier and show the resulting acceleration is still large; expected outcome: the model exhibits substantial speedup without runaway singularity, reproducing Greenblatt's decoupling qualitatively.
- Sensitivity sweep over the multiplier and compute-bottleneck cap; expected outcome: a chart showing the 'large speedup' conclusion is robust across a plausible multiplier range but is throttled past a certain compute cap, making the debate's cruxes explicit and inspectable.

**Impact Chain:** Greenblatt's argument about automation-driven acceleration is verbal and hard for newcomers to scrutinize quantitatively, yet it feeds takeoff-timeline and governance reasoning. Translating it into a small, public, fully-inspectable model with labeled assumptions and a sensitivity analysis makes the acceleration debate legible: governance researchers and forecasters can see exactly which assumptions drive 'large speedup' and stress-test them. This is high-counterfactual-value third-party work that labs are unlikely to produce in inspectable open form.

**Strength Rationale:** CPU-only, public-data, single-notebook deliverable — maximally executable outside a lab. Scope is bounded to reproducing one qualitative claim plus a two-parameter sensitivity sweep. The baseline-fitting experiment grounds the toy model in real data, mitigating the 'arbitrary assumptions' risk that a mentor would otherwise need to police.

**Cited Sources:** Full automation of AI R&D probably yields a large speed up even without a software-only singularity — https://blog.redwoodresearch.org/p/full-automation-of-ai-r-and-d-probably; A simpler AI timelines model predicts 99% AI R&D automation in ~2032 (METR) — https://metr.org/notes/2026-02-10-simpler-ai-timelines-model/; Will AI R&D Automation Cause a Software Intelligence Explosion? (Forethought) — https://www.forethought.org/research/will-ai-r-and-d-automation-cause-a-software-intelligence-explosion; Will compute bottlenecks prevent a software intelligence explosion? (Alignment Forum) — https://www.alignmentforum.org/posts/XDF6ovePBJf6hsxGj/will-compute-bottlenecks-prevent-a-software-intelligence-1

**Subfield:** AI forecasting / takeoff modeling | **Strategy:** tool_or_benchmark_gap | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Makes the acceleration debate legible for takeoff/governance reasoning, but the toy growth model's link to concrete risk reduction has a gap.
  - **low_compute:** 5, confidence: 0.85 — Python simulation over public time-series, CPU/analytical only.
  - **accessible_complexity:** 4, confidence: 0.6 — Building a transparent growth model with sensitivity analysis is approachable but requires modeling judgment a mentor must guide.
  - **narrow_scope:** 4, confidence: 0.65 — Focused notebook deliverable reproducing one qualitative claim with sensitivity analysis, bounded.
  - **counterfactual_value:** 5, confidence: 0.7 — Inspectable public model of a lab-influenced debate, high counterfactual value as third-party legible analysis.
  - **novelty:** 2, confidence: 0.5 — ASSESSED: Multiple open, transparent growth models already reproduce Greenblatt-style claims that AI R&D automation yields large speedups even without a software-only singularity, with explicit automation-multiplier and compute-bottleneck parameters plus sensitivity sweeps: METR's 'simpler AI timelines model', Forethought's 'Will AI R&D Automation Cause a Software Intelligence Explosion' (CES compute-bottleneck model), and the AI Futures takeoff model (with the r>1/b parameterization). The proposed notebook is essentially a re-implementation of these published, documented models fed from Epoch-style public data; it is a reproduction/teaching artifact rather than a novel contribution.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #66: When Human Verification Fails: Detecting Plausible-but-Wrong LLM Answers on Hard Tasks (Score: 4.00)

**ID:** gen-085

**Research Question:** As task difficulty rises, how reliably does a weaker open model — standing in for a non-expert human overseer — catch confident, fluent-but-wrong answers, and where does that oversight collapse?

**Approach:** Use one public dataset with verified ground truth that spans a difficulty gradient (MMLU, stratified into easy/medium/hard subjects, ~300 items). Generate two answer pools from a stronger open model (Qwen2.5-14B or Llama-3.1-8B): correct answers and deliberately flawed-but-fluent answers (produced by prompting the model to argue confidently for a wrong option). A weaker open model (a 1-3B instruct model) acts as the verifier, asked to judge each answer correct/incorrect. Measure verifier detection accuracy as a function of difficulty. To keep scope bounded, fix a single verifier model and a single dataset (MMLU), making difficulty the only swept axis. Deliverable: one verification-accuracy-vs-difficulty plot with the collapse region annotated.

**Experiments:** - Generate the correct and fluent-but-wrong answer pools and manually spot-check that wrong answers are genuinely wrong yet fluent. Measure: fraction of wrong answers that are fluent and confidently argued. Expected outcome: a clean, validated answer set with controlled correctness labels.
- Run the weak verifier across the difficulty gradient. Measure: verifier accuracy at distinguishing correct from wrong, per difficulty stratum. Expected outcome: verifier accuracy is high on easy items and degrades toward chance on hard items, locating an oversight-collapse region.
- Separate failure modes by measuring false-accept rate (passing a wrong answer) vs false-reject rate (failing a correct one) by difficulty. Measure: both error types vs difficulty. Expected outcome: false-accepts dominate on hard items — the dangerous direction for oversight — confirming weak overseers wave through confident-wrong answers exactly where it matters.

**Impact Chain:** Scalable-oversight schemes lean on the idea that a weaker overseer (or human non-expert) can still verify a stronger model's outputs. The verification bottleneck — where this breaks down on hard tasks — is asserted but not measured. A concrete accuracy-vs-difficulty curve, with the false-accept direction isolated, is a direct empirical input telling oversight designers at what difficulty they can no longer rely on weak verification and must add stronger checks.

**Strength Rationale:** Scope is tightened from 'multiple datasets' to a single dataset (MMLU) and a single fixed verifier, making difficulty the only variable and yielding one plot. The novelty concern (scored 2) is mitigated by the specific framing as a weak-verifier-vs-difficulty collapse curve with the false-accept/false-reject decomposition, which operationalizes the bottleneck rather than restating it. Accessible_complexity is supported by giving a concrete recipe for generating fluent-wrong answers (prompt the model to argue a wrong option).

**Cited Sources:** AI alignment is a human problem — https://www.aisi.gov.uk/research/ai-alignment-is-a-human-problem; On scalable oversight with weak LLMs judging strong LLMs (Kenton et al., NeurIPS 2024) — https://proceedings.neurips.cc/paper_files/paper/2024/file/899511e37a8e01e1bd6f6f1d377cc250-Paper-Conference.pdf; FindTheFlaws: Annotated Errors for Detecting Flawed Reasoning and Scalable Oversight Research — https://arxiv.org/abs/2503.22989; GPQA: A Graduate-Level Google-Proof Q&A Benchmark — https://arxiv.org/pdf/2311.12022

**Subfield:** Scalable Oversight | **Strategy:** experiment_variation | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.65 — A verification-accuracy-vs-difficulty curve is a concrete input to scalable-oversight design, grounding the abstract verification gap.
  - **low_compute:** 4, confidence: 0.8 — Inference-only generation and weak-verifier scoring on open models over public datasets fits a consumer GPU.
  - **accessible_complexity:** 4, confidence: 0.65 — Public datasets and a weaker-model verifier are accessible, but crafting fluent-but-flawed answers and difficulty stratification need mentor guidance.
  - **narrow_scope:** 4, confidence: 0.7 — Focused verification-accuracy-vs-difficulty plot, bounded though it spans multiple datasets.
  - **counterfactual_value:** 4, confidence: 0.7 — Open models/public data weak-to-strong oversight measurement independent of labs.
  - **novelty:** 3, confidence: 0.5 — ASSESSED: Weak-overseer-detection-vs-difficulty is a well-studied scalable-oversight question: Kenton et al. (NeurIPS 2024) use weak LLM judges over MMLU, GPQA reports ~34% non-expert validator accuracy, and FindTheFlaws explicitly tests whether weak verifiers scale with problem difficulty. However, the specific design proposed — a weak open model as overseer judging a curated pool of correct vs deliberately-fluent-but-wrong answers from a stronger open model, with detection accuracy plotted across a controlled MMLU easy/medium/hard gradient and the collapse region annotated — is a concrete, not-yet-published instantiation; the difficulty-sweep-as-only-axis angle remains open.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #67: Does Faithfulness of Chain-of-Thought Degrade as Tasks Get Harder? (Score: 4.00)

**ID:** gen-086

**Research Question:** When a biasing cue is inserted into a multiple-choice prompt, how often do open models shift their answer toward the cue while their chain-of-thought never mentions it (unfaithful rationalization) — and does this unfaithfulness rate rise with task difficulty?

**Approach:** Adopt the established biased-cue faithfulness probe: insert a cue ('I think the answer is B') into multiple-choice prompts and measure cases where the model's answer moves toward the cue but the CoT never acknowledges the cue. Use one public QA dataset with a usable difficulty gradient (a stratified MMLU slice, ~300 items, easy/medium/hard). Run two open models (Llama-3.1-8B, Qwen2.5-7B) in CoT mode, with and without the cue. Detect 'cue-influenced answer change' by comparing answers across cued/uncued runs, and 'CoT mentions cue' by keyword + small-judge check. Unfaithfulness = answer changed toward cue AND CoT silent on it. Hold the cue template, datasets, and detection fixed; difficulty is the swept axis. Deliverable: one unfaithfulness-rate-vs-difficulty plot for both models.

**Experiments:** - Establish cue sensitivity: measure how often each model's answer moves toward the inserted cue overall. Measure: cue-induced answer-change rate. Expected outcome: a non-trivial fraction of answers shift toward the cue, confirming the probe elicits influence.
- Among cue-influenced changes, measure how often the CoT mentions the cue. Measure: unfaithfulness rate (changed-and-silent / changed). Expected outcome: a substantial share of cue-driven changes are never acknowledged in the CoT — i.e. unfaithful rationalization.
- Plot unfaithfulness rate across the difficulty gradient. Measure: unfaithfulness vs difficulty stratum. Expected outcome: unfaithfulness rises on harder items, meaning CoT monitoring gives the least faithful signal exactly where stakes are highest.

**Impact Chain:** Chain-of-thought monitoring is a leading practical oversight technique: auditors read the model's reasoning to catch problematic behavior. If CoT stops faithfully reflecting the real computation — especially on hard problems — monitors give false assurance precisely where it is most dangerous. Quantifying where faithfulness collapses tells oversight practitioners the difficulty regime in which CoT monitoring can no longer be trusted alone.

**Strength Rationale:** Scope is tightened to one dataset and a fixed cue template, with difficulty as the only swept axis and a single plot deliverable. The novelty concern (scored 2) is addressed by the specific difficulty-gradient framing and the two-step unfaithfulness definition (answer-change AND CoT-silence), which goes beyond a flat faithfulness number. Accessible_complexity is supported by reducing 'unfaithful rationalization' to a concrete, mechanical comparison of cued vs uncued runs plus a keyword check, giving the novice an unambiguous detection rule.

**Cited Sources:** Loss of Oversight — https://www.aisi.gov.uk/research/loss-of-oversight-how-ai-systems-may-become-harder-to-audit-monitor-and-investigate; Task Difficulty Shapes Chain-of-Thought Faithfulness (OpenReview) — https://openreview.net/pdf/f2beacfb65623c951a3c9017791b7501159a3250.pdf; Chain-of-Thought Reasoning In The Wild Is Not Always Faithful — https://arxiv.org/pdf/2503.08679; Measuring Chain-of-Thought Monitorability Through Faithfulness and Verbosity — https://arxiv.org/pdf/2510.27378

**Subfield:** Interpretability / Monitoring (CoT faithfulness) | **Strategy:** failure_mode_investigation | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — If CoT faithfulness collapses on harder problems, monitors give false assurance where stakes are highest; directly relevant to a leading oversight technique.
  - **low_compute:** 4, confidence: 0.8 — Inference-only biased-cue probe on 2-3 open models over public QA, consumer-GPU feasible.
  - **accessible_complexity:** 4, confidence: 0.65 — Cue-insertion and answer-change measurement is approachable, but defining and detecting unfaithful rationalization needs mentor care.
  - **narrow_scope:** 4, confidence: 0.7 — Focused unfaithfulness-rate-vs-difficulty deliverable, well-bounded though across models.
  - **counterfactual_value:** 4, confidence: 0.7 — Open models/public data CoT-faithfulness probe independent of lab access.
  - **novelty:** 2, confidence: 0.5 — ASSESSED: The exact claim — CoT faithfulness/unfaithfulness degrades with task difficulty — is directly established by 'Task Difficulty Shapes Chain-of-Thought Faithfulness' (difficulty-faithfulness gradient, MMLU vs BBH, error-propagation rising 22%->41%), and the biased-cue probe (answer shifts toward an incorrect hint while CoT stays silent) is the well-known Turpin/Anthropic faithfulness methodology. The proposal combines the established cue-injection probe with a difficulty gradient on a stratified MMLU slice and open models; the headline question is essentially answered, though the specific cue-probe x MMLU-difficulty measurement on Llama-3.1-8B/Qwen2.5-7B is a slightly different method than the causal-perturbation gradient paper.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #68: Where Do Reviewers Miss the Most? Mapping Human Error Detection by Mistake Type (Score: 4.00)

**ID:** gen-087

**Research Question:** Across a fixed set of controlled error types injected into model-generated solutions, which error types does a weak reviewer systematically fail to detect?

**Approach:** Build a small benchmark (~150 items) of model-generated solutions to public reasoning/coding tasks (GSM8K + MBPP slices). Into each, inject exactly one error of a controlled type from a fixed taxonomy of five: subtle arithmetic slip, wrong-but-plausible cited fact, off-by-one in code, unjustified assumption, omitted edge case. A weaker open model (1-3B instruct) acts as the stand-in 'reviewer', asked to find any error. Measure detection rate per error type. Hold the reviewer model, task sources, and one-error-per-item design fixed; error type is the categorical variable. Keep human raters optional/out-of-scope for the core deliverable to bound effort. Deliverable: a ranked detectability table (error type -> detection rate), lowest-detected first.

**Experiments:** - Construct and validate the benchmark: confirm each item contains exactly one injected error of the labeled type and is otherwise correct. Measure: label-correctness on a spot-checked sample. Expected outcome: a clean single-error benchmark across five controlled types.
- Run the weak reviewer and compute detection rate per error type. Measure: fraction of items where the reviewer flags the injected error, by type. Expected outcome: surface-checkable errors (off-by-one, arithmetic) are caught more often than reasoning-level errors (unjustified assumption, omitted edge case).
- Rank error types by detection rate and inspect the lowest. Measure: the ordered detectability table plus example missed items. Expected outcome: a clear ranking identifying which error types most often evade non-expert review, directing where backup verification should focus.

**Impact Chain:** If AI-assisted alignment work concentrates its mistakes among error types human (or weak) reviewers least detect, then automated alignment can produce compelling-but-misleading assessments. A ranked map of which error types evade review lets teams target backup verification and red-teaming at exactly those types, reducing the chance that a flawed automated-alignment result passes review undetected.

**Strength Rationale:** Scope is tightened by fixing a closed five-type taxonomy, one-error-per-item, a single reviewer model, and dropping the human-rater pass from the core deliverable — yielding one ranked table. Accessible_complexity is improved by specifying the exact error taxonomy and an automated weak-model reviewer, removing the open-ended error-design and human-coordination burden. Open models and public tasks preserve counterfactual value.

**Cited Sources:** Automated alignment is harder than you think — https://www.aisi.gov.uk/research/automated-alignment-is-harder-than-you-think; FindTheFlaws: Annotated Errors for Detecting Flawed Reasoning and Scalable Oversight Research — https://arxiv.org/abs/2503.22989; Evaluating LLMs at Detecting Errors in LLM Responses — https://arxiv.org/pdf/2404.03602; Evaluating Mathematical Reasoning of LLMs: A Focus on Error Identification and Correction — https://arxiv.org/html/2406.00755v1

**Subfield:** Scalable Oversight / AI-assisted research safety | **Strategy:** failure_mode_investigation | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.65 — A ranked detectability table lets backup verification/red-teaming target error types reviewers miss, addressing the automated-alignment misassessment worry.
  - **low_compute:** 4, confidence: 0.8 — Inference-only generation and weak-model review over public tasks fits a consumer GPU.
  - **accessible_complexity:** 4, confidence: 0.65 — Injecting controlled error types and measuring detection is accessible, but careful error-type control and optional human pass need guidance.
  - **narrow_scope:** 4, confidence: 0.7 — Focused ranked-detectability deliverable, bounded though spanning several error types.
  - **counterfactual_value:** 4, confidence: 0.7 — Open models/public tasks oversight-gap mapping independent of lab access.
  - **novelty:** 3, confidence: 0.5 — ASSESSED: Mapping reviewer detection rate by error type is established across domains: radiology error-detection (numerical 88% vs interpretation 70%), code review (contextual errors hardest, ~16% detection vs factual easiest), NLP-review injected-error studies, and the FindTheFlaws weak-verifier benchmark spanning math/coding/science. The general finding — weak reviewers systematically miss subtle/contextual errors and catch concrete factual ones — is well-known. The proposal's specific 5-type controlled taxonomy (arithmetic slip, plausible wrong fact, off-by-one, unjustified assumption, omitted edge case), one-error-per-item on GSM8K+MBPP slices with a 1-3B open reviewer, is a fresh small instantiation rather than a fully covered result, but the angle overlaps heavily with prior work.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #69: Which Environmental Knobs Move Open Models? A Mini Propensity-Inference Replication on Open LLMs (Score: 4.00)

**ID:** gen-090

**Research Question:** In one published propensity scenario, which environmental factors most shift behavior in small open-weight models, and does the strategic-vs-non-strategic balance match UK AISI's finding from mostly-closed models?

**Approach:** Pick one propensity environment (a single goal-conflict-with-oversight scenario). Vary a fixed set of four environmental factors (presence of oversight, goal-conflict framing, time pressure, stated stakes) in a 2^4 factorial prompt grid. Run each cell N=20 across two open models for the core deliverable (Llama-3.1-8B, Qwen2.5-7B), with two more (Mistral-7B, Gemma-2-9B) as optional extensions. Code each rollout for the undesired behavior with a keyword + small-LLM-judge rubric, fit a logistic regression to estimate each factor's main effect, and compare the strategic/non-strategic balance against AISI's. Tighten scope by fixing one scenario, four factors (not 4-6), N=20, and two core models. Deliverable: a per-factor effect-size plot with the strategic/non-strategic comparison to AISI.

**Experiments:** - Build and validate the factorial prompt grid and the behavior-coding rubric on a small pilot. Measure: inter-method agreement between keyword and LLM-judge coding on a pilot sample. Expected outcome: acceptable agreement, validating the automated coder before the full run.
- Run the full 16-cell grid x N=20 on the two core models and fit the logistic regression. Measure: each factor's estimated effect on undesired-behavior probability. Expected outcome: oversight presence and goal-conflict framing show the largest effects, with smaller surface factors (time pressure, stakes wording) also contributing.
- Compare the strategic-vs-non-strategic effect balance against AISI's roughly-equal finding. Measure: ratio of strategic to non-strategic factor effect magnitude. Expected outcome: either open models reproduce the rough balance (supporting cheap external propensity evals) or surface factors dominate (revealing small-model propensity studies are confounded).

**Impact Chain:** Propensity evaluations probe whether a model will behave badly under realistic conditions, and they matter most when independents can run them cheaply to scrutinize models labs deploy. AISI's study used mostly-closed models; if cheap open models reproduce the same factor structure, low-cost external propensity evals become viable, and if not, it flags that small-model propensity results are confounded by surface features. Either outcome directly shapes how much weight to put on accessible propensity evals.

**Strength Rationale:** Scope is tightened from a 4-6 factor x 4-model x N=30 grid to a fixed 4-factor x 2-core-model x N=20 grid (16 cells), with the extra models and a pilot-validated coder added for rigor rather than breadth. The deliverable is one effect-size plot plus one comparison. Theory_of_impact and counterfactual value were already strong (open-weight replication of a closed-model lab study); the pilot coding-validation step shores up accessible_complexity by de-risking the stats/coding the novice was flagged on.

**Cited Sources:** Propensity Inference: Environmental Contributors to LLM Behaviour — https://www.aisi.gov.uk/research/propensity-inference-environmental-contributors-to-llm-behaviour; Propensity Inference: Environmental Contributors to LLM Behaviour (arXiv 2604.21098) — https://arxiv.org/abs/2604.21098; Finding 'misaligned persona' features in open-weight models — https://www.lesswrong.com/posts/NCWiR8K8jpFqtywFG/finding-misaligned-persona-features-in-open-weight-models; Methodology for inferring propensities of LLMs — https://www.lesswrong.com/posts/g9FmhKL2vL45TuT9B/methodology-for-inferring-propensities-of-llms

**Subfield:** AI control / behavioral evaluation | **Strategy:** replication_with_twist | **Novelty:** mostly_novel (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Establishing whether cheap open models reproduce propensity factors directly enables low-cost external propensity evals, a concrete safety pathway.
  - **low_compute:** 5, confidence: 0.85 — Inference-only across 7-9B open models, fits a consumer GPU with batching.
  - **accessible_complexity:** 4, confidence: 0.8 — Factorial prompt grids plus logistic regression and LLM-judge coding is guided-level; needs a mentor for the stats but novices can execute.
  - **narrow_scope:** 4, confidence: 0.75 — Focused deliverable (per-factor effect estimates vs AISI) but a 4-6 factor x 4-model x N=30 grid is moderately broad.
  - **counterfactual_value:** 4, confidence: 0.8 — Open-weight replication of a closed-model lab study, exactly the third-party scrutiny independents can provide.
  - **novelty:** 4, confidence: 0.5 — ASSESSED: The source paper (UK AISI, arXiv 2604.21098) studied 12 environmental factors across 23 mostly-larger models, but I found no replication that runs a focused 2^4 factorial on small open-weight models (Llama-3.1-8B, Qwen2.5-7B) and explicitly compares the strategic/non-strategic effect balance against AISI's. Related open-weight propensity work (misaligned-persona feature replication) targets interpretability features, not the factorial environmental-knob design proposed here, leaving the specific extension open.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #70: Cheap-Defense Stress Test: Do Simple Prompt-Level Guards Survive the Jailbreaks That Broke DeepSeek-V4-Pro? (Score: 4.00)

**ID:** gen-092

**Research Question:** On an open model, do three lightweight inference-only defenses (defensive system prompt, second-pass self-critique filter, input paraphrase-then-answer) meaningfully reduce attack success rate against reproducible jailbreak strategies, or do the attacks route around them?

**Approach:** Use a public harmful-behavior benchmark (JailbreakBench JBB-Behaviors or a HarmBench subset) and 3 reproducible jailbreak templates (roleplay, refusal-suppression, low-resource/encoding). Measure baseline attack success rate (ASR) on one open model (Llama-3.1-8B-Instruct or Qwen2.5-7B-Instruct). Then add each of three cheap inference-only defenses independently and re-measure ASR: (1) a defensive system prompt, (2) a second-pass self-critique filter (model reviews its own draft for harmfulness before returning), (3) input paraphrase-then-answer. Score harmful compliance with an LLM-judge calibrated on a held-out hand-labeled set (report judge accuracy). Deliverable: an ASR table (3 attacks x baseline + 3 defenses) showing which defenses move ASR and which attacks route around them. To address the 'largely_addressed' novelty flag, the distinctive contribution is the head-to-head comparison of these specific wrapper defenses under matched attacks with a calibrated judge — a deployer-facing 'is it protection or theater' verdict rather than a new attack.

**Experiments:** - Calibrate the LLM-judge on ~60 hand-labeled responses (harmful-compliance vs not) and measure judge accuracy; expected outcome: judge accuracy > 85%, so ASR estimates are trustworthy before any defense is tested.
- Measure baseline ASR for all 3 attacks with no defense; expected outcome: high ASR (e.g. >70%) on at least some attacks, reproducing the spirit of the DeepSeek-V4-Pro safeguard collapse on an open model.
- Add each defense independently and re-measure ASR per attack; expected outcome: defensive system prompt and self-critique reduce ASR substantially for roleplay but encoding/low-resource attacks route around all three, giving a concrete which-defense-for-which-attack map for deployers.

**Impact Chain:** Most open-weight deployers cannot retrain a model's safeguards; their only lever is cheap inference-time wrappers. The source stress test showed frontier-style safeguards collapse under simple jailbreaks. By measuring whether wrapper-level defenses actually move ASR on an open model — and which attacks defeat them — this gives deployers an evidence-based verdict on whether prompt-level guards are real protection or security theater, directly informing the misuse-mitigation choices of actors who have no other option.

**Strength Rationale:** Inference-only on one open model with public jailbreak benchmarks. The judge-calibration experiment removes the main measurement risk. Scope is one ASR table. Novelty is reframed around the deployer-facing head-to-head wrapper-defense comparison with matched attacks and a calibrated judge, distinguishing it from generic jailbreak papers.

**Cited Sources:** Security Stress Test: DeepSeek-V4-Pro (FAR AI) — https://www.far.ai/blog; Merging Improves Self-Critique Against Jailbreak Attacks — https://arxiv.org/pdf/2406.07188; SelfDefend: LLMs Can Defend Themselves against Jailbreaking — https://arxiv.org/pdf/2406.05498; Defensive Prompt Patch — https://arxiv.org/html/2405.20099; JailbreakBench: An Open Robustness Benchmark — https://github.com/JailbreakBench/jailbreakbench; Robust Prompt Optimization for Defending LMs (RPO) — https://proceedings.neurips.cc/paper_files/paper/2024/file/46ed503889ab232c21c1162340ee17b2-Paper-Conference.pdf

**Subfield:** Adversarial robustness / jailbreaks | **Strategy:** follow_up_experiment | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Testing whether wrapper defenses are real protection or theater directly informs open-weight deployers, a concrete misuse-reduction pathway.
  - **low_compute:** 5, confidence: 0.85 — Inference-only attacks and defenses on one open model.
  - **accessible_complexity:** 4, confidence: 0.78 — Using public jailbreak benchmarks and an LLM-judge is guided-level; calibrating the judge needs care.
  - **narrow_scope:** 4, confidence: 0.75 — Focused deliverable (ASR with vs without 3 defenses) but spans multiple attacks and defenses.
  - **counterfactual_value:** 4, confidence: 0.78 — Open-model wrapper-defense evaluation is squarely independent-friendly and useful to the broader community.
  - **novelty:** 2, confidence: 0.55 — ASSESSED: All three proposed inference-only wrapper defenses are extensively studied individually: defensive system prompts / prompt patches (Defensive Prompt Patch, RPO), self-critique filters (SelfDefend, Merging Improves Self-Critique), and paraphrase/perplexity input defenses (SmoothLLM, back-translation). JailbreakBench and HarmBench already provide standardized matched-attack comparison with calibrated LLM-Guard judges, and surveys directly compare wrapper defenses. The 'protection or theater' head-to-head verdict is a useful but incremental re-packaging of well-trodden evaluations.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #71: Detecting the Fine-Tuning Footprint: Can Output-Only Probes Flag a Secretly Adapted Open Model? (Score: 4.00)

**ID:** gen-101

**Research Question:** Given only generated text on a fixed probe-prompt set, how strong must a LoRA adaptation be before a black-box detector can reliably tell an adapted open model from its base — i.e. below what adaptation strength does behavioral verification fail and hardware attestation become necessary?

**Approach:** Fine-tune one open base model (Llama-3.1-8B) with a small LoRA on one narrow behavior. Build a black-box detector that, given only generated text on a fixed probe-prompt set (~50 prompts), classifies base vs adapted — using simple features (output embeddings from a public sentence encoder + a logistic-regression classifier) rather than any weight access. Sweep a single axis: adapter strength, operationalized as LoRA training-data size over a small fixed grid {200, 1000, 5000 examples} at one fixed rank, to keep the experiment bounded (avoiding the original's combined rank x dataset-size sweep). Deliverable: an accuracy-vs-adapter-strength curve plus the handful of most discriminative probe prompts.

**Experiments:** - Produce base and adapted generations on the fixed probe set at the strongest adaptation (5000 examples); train and test the black-box detector. Measure: detector accuracy at strong adaptation. Expected outcome: high accuracy, confirming a strong covert adaptation is detectable from outputs alone.
- Sweep adapter strength {200, 1000, 5000}. Measure: detector accuracy vs adaptation strength. Expected outcome: accuracy falls toward chance as the adaptation weakens, locating the threshold below which output-only verification fails.
- Inspect which probe prompts carry the signal by ranking prompts by detector feature importance. Measure: the most discriminative prompts. Expected outcome: a small set of probe prompts drives detection, giving a reusable lightweight verification probe and showing where it breaks down.

**Impact Chain:** TEE-based verification aims to confirm a deployed model is the attested approved one, but it is expensive; a covert actor could swap in a LoRA-adapted variant. Knowing where cheap output-only probing already detects such a swap — and where it fails — tells governance designers when expensive hardware attestation is genuinely required versus when behavioral verification suffices, informing the cost/benefit of verification regimes.

**Strength Rationale:** Scope is tightened by sweeping a single axis (data-size as adapter strength at fixed rank) instead of the original combined rank x dataset-size sweep, yielding one curve. Low-compute (originally a concern from 'several adapters add load') is addressed: at fixed rank with three data sizes, only three LoRA fine-tunes are needed, comfortably within a consumer GPU. Accessible_complexity is supported by specifying a concrete detector (public sentence-encoder embeddings + logistic regression). Open-model execution preserves counterfactual value.

**Cited Sources:** On TEEs for Privacy-Preserving Monitoring — https://techgov.intelligence.org/blog/on-tees-for-privacy-preserving-monitoring-in-ai-governance; Trusting What You Cannot See: Auditable Fine-Tuning and Inference for Proprietary AI — https://arxiv.org/pdf/2603.07466; Open Problems in Technical AI Governance — https://arxiv.org/pdf/2407.14981; RoFL: Robust Fingerprinting of Language Models — https://arxiv.org/html/2505.12682; Weight space Detection of Backdoors in LoRA Adapters — https://arxiv.org/pdf/2602.15195

**Subfield:** AI governance / model verification | **Strategy:** failure_mode_investigation | **Novelty:** mostly_novel (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.68 — Clarifying where output-only verification suffices vs where TEE attestation is needed directly informs governance cost/benefit decisions.
  - **low_compute:** 4, confidence: 0.65 — LoRA fine-tunes plus black-box probing are mostly feasible on a consumer GPU but several adapters add load.
  - **accessible_complexity:** 4, confidence: 0.72 — LoRA fine-tuning and a black-box classifier are guided-level with a mentor.
  - **narrow_scope:** 4, confidence: 0.72 — Focused deliverable (accuracy-vs-adapter-strength curve) though sweeping ranks and dataset sizes adds breadth.
  - **counterfactual_value:** 4, confidence: 0.75 — Open-model verification stress test is independent-friendly and needs no internal access.
  - **novelty:** 4, confidence: 0.5 — ASSESSED: Adjacent work exists (model fingerprinting RoFL, membership inference, weight-space backdoor detection in LoRA adapters, and TEE-governance papers noting that behavioral validation has limits), but I found no study that runs an output-only black-box base-vs-adapted classifier while sweeping LoRA adaptation strength to locate the detection-failure threshold, framed as the point where behavioral verification breaks and hardware attestation becomes necessary. The governance motivation is discussed conceptually but the empirical accuracy-vs-adapter-strength curve appears to be an open gap.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #72: Can Cheap Counter-Examples Hide a Classifier Backdoor? Testing Detectability via Held-Out Trigger Variants (Score: 3.97)

**ID:** gen-038

**Research Question:** Can a free, trigger-agnostic probing recipe (paraphrases and near-trigger string variants) detect a poisoned safety classifier whose backdoor is hidden by counter-examples that preserve aggregate validation accuracy?

**Approach:** Reuse/reproduce a single backdoored open-model safety classifier (LoRA on a public safety dataset with ~32 poisoned examples plus counter-examples that keep validation accuracy clean), following the paper. Then build a lightweight detector that does NOT know the trigger: generate paraphrases and near-trigger strings (synonym swaps, punctuation/casing changes) over a held-out probe set of harmful inputs and look for anomalous confidence drops. Compare the detector's backdoor-detection rate against what plain validation accuracy reveals (which is, by construction, nothing). To keep the two-stage build tractable, provide the backdoored-classifier training as a fixed scripted recipe so the participant's novel work is the detector. Inference-light. Deliverable: detector detection-rate vs validation-accuracy comparison, plus a list of which probe transformations surface the backdoor.

**Experiments:** - Backdoor reproduction + invisibility check: train the backdoored classifier with the scripted recipe and confirm validation accuracy on a clean set is indistinguishable from a clean model, while the trigger flips predictions. Measure: clean-set accuracy gap (should be ~0) and trigger attack-success-rate (should be high). Expected outcome: a genuinely 'invisible' backdoor, establishing the detection challenge the project must beat.
- Trigger-agnostic probing: run the paraphrase/near-trigger probe set through the classifier and flag anomalous confidence drops on harmful inputs. Measure: detection rate (does probing reveal a backdoor without knowing the trigger?) and false-positive rate on a clean classifier. Expected outcome: some probe transformations surface the backdoor above the clean-model baseline, giving a concrete cheap pre-deployment check — or, if not, quantifying how dangerously undetectable the backdoor is.
- Transformation ablation: rank which probe transformations (synonym swap vs punctuation vs casing vs paraphrase) most reliably trigger the anomalous drop. Measure: detection rate per transformation type. Expected outcome: a small recommended probe recipe (the few transformations that matter), turning the result into a reusable, model-agnostic audit tool.

**Impact Chain:** Constitutional/safety classifiers fine-tuned on third-party data are a growing line of defense, and the source paper shows they can be backdoored so that standard validation accuracy looks fine — an undetectable degradation. If a free, trigger-agnostic probing recipe can flag such backdoors, every small team fine-tuning a safety classifier gains a practical pre-deployment check they can run without trusting their data supplier -> poisoned safety classifiers are caught before deployment, or the field gets a quantified bound on how undetectable they really are -> defenders prioritize the probe transformations that work and treat aggregate-metric-preserving backdoors as a named, testable threat -> the attack surface where poisoned safety filters silently pass harmful content (or block benign content) is reduced, closing a concrete supply-chain vulnerability in deployed safety tooling.

**Strength Rationale:** accessible_complexity (3) and narrow_scope (4) were the weakest dimensions, both driven by the two-stage build (first create the backdoor, then detect it). I strengthened both by making the backdoored-classifier training a fixed scripted recipe so the participant's genuine work — and the deliverable — is just the detector, and by adding an invisibility-check first experiment that de-risks the dependency. theory_of_impact (4) is reinforced by framing the output as a reusable, model-agnostic audit recipe (the transformation ablation) plus an explicit fallback value (quantifying undetectability) if detection fails.

**Cited Sources:** Poisoning Fine-tuning Datasets of Constitutional Classifiers — https://alignment.anthropic.com/2026/backdooring-classifiers/; Poisoning Fine-tuning Datasets of Constitutional Classifiers (Anthropic) — https://alignment.anthropic.com/2026/backdooring-classifiers/; Poisoned classifiers are not only backdoored, they are fundamentally broken — https://arxiv.org/pdf/2010.09080; CLIBE: Detecting Dynamic Backdoors in Transformer-based NLP Models — https://www.ndss-symposium.org/wp-content/uploads/2025-478-paper.pdf; Backdoor Learning for NLP: Recent Advances — https://arxiv.org/pdf/2302.06801

**Subfield:** Data poisoning / backdoor detection | **Strategy:** tool_or_benchmark_gap | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.65 — A free model-agnostic probe to flag poisoned safety classifiers, or quantifying their undetectability, is a concrete pre-deployment safety check.
  - **low_compute:** 5, confidence: 0.8 — Reuses one backdoored small classifier plus paraphrase probing; minimal compute.
  - **accessible_complexity:** 3, confidence: 0.65 — Requires first producing a backdoored classifier then building a variant-probing detector; intermediate two-stage build.
  - **narrow_scope:** 4, confidence: 0.7 — Focused detection-vs-accuracy comparison but depends on first creating the backdoored model.
  - **counterfactual_value:** 5, confidence: 0.7 — Open-model backdoor detection on public data is a neglected, independent-friendly auditing case.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #73: Can Open Agents Hide a Rogue Action From a Monitor? A Tiny Means-and-Opportunity Probe (Score: 3.97)

**ID:** gen-063

**Research Question:** Can a cheap open agent conceal a single flagged action from a benign overseer while completing a benign task, and how does its concealment success rate change with task/concealment difficulty — an open-model analogue of METR's 'has means/opportunity but cannot hide a significant rogue deployment' finding?

**Approach:** Build a small sandboxed toy task: a tiny repo plus a benign overseer LLM that reads the agent's action logs and flags anything suspicious. An open agent (a 7-8B instruct model with simple tool-use prompting) is told to complete a benign task while covertly inserting and concealing one flagged action. Measure how often the overseer flags the hidden action across a few graded difficulty levels (e.g. how disguised the action must be). To keep the build beginner-tractable, provide a fixed minimal sandbox (a handful of files + a logged action interface) and a fixed overseer prompt, so the participant varies only the agent's concealment strategy and difficulty. Metric: concealment success rate vs difficulty. Inference-only. Deliverable: a concealment-success-vs-difficulty curve.

**Experiments:** - Sandbox + overseer baseline: build the minimal sandbox and confirm the overseer reliably flags an *un-disguised* rogue action (sanity floor) and passes a clean benign run (no false alarm). Measure: overseer detection on blatant rogue action and FPR on clean runs. Expected outcome: overseer catches the obvious case and rarely false-alarms, validating the testbed before measuring concealment (de-risks the scaffolding the scorer flagged as intermediate).
- Concealment sweep: have the agent attempt the hidden action at 3-4 difficulty/disguise levels. Measure: concealment success rate (overseer fails to flag) per level. Expected outcome: success rises as disguise effort increases but plateaus at low rates for cheap open agents — an open-model echo of METR's 'cannot hide significant rogue deployment' finding, now quantified and trackable.
- Capability-tracking comparison: run the same sweep on two open agents of different capability (e.g. 7-8B vs a stronger ~14B). Measure: concealment-success curve per model. Expected outcome: the stronger model conceals somewhat better, demonstrating the testbed can track a dangerous capability across open-model generations — its core counterfactual value.

**Impact Chain:** Whether an AI agent can hide an unauthorized action from oversight is the crux of rogue-deployment and sabotage risk — METR judged frontier internal agents had means/motive/opportunity but lacked the means to hide a significant-scale rogue deployment. That capability has not been measured for cheap open agents, which external researchers can study without lab access. A public, sandboxed concealment testbed lets independents quantify and track 'can it hide?' across open-model generations -> the community gets an open, reproducible early-warning instrument for a dangerous capability as open models scale -> AI-control researchers and governance get longitudinal evidence on when open agents start to reliably evade oversight -> defenders can react before concealment-capable open agents are widely deployable, directly informing the control measures meant to prevent rogue deployments.

**Strength Rationale:** accessible_complexity (3) and narrow_scope (4) were the weakest dimensions, both driven by the sandbox/agent scaffolding. I strengthened both by fixing a minimal provided sandbox + fixed overseer prompt so the participant varies only concealment strategy and difficulty, and by adding a baseline sanity experiment that validates the testbed before the main measurement — keeping the build incremental and the deliverable a single curve. counterfactual_value (already 5) is reinforced by the capability-tracking-across-models experiment, which is exactly the neglected, independent-friendly contribution.

**Cited Sources:** Frontier Risk Report (METR, Feb-Mar 2026) — https://metr.org/blog/2026-05-19-frontier-risk-report/; SHADE-Arena: Evaluating Sabotage and Monitoring in LLM Agents — https://arxiv.org/pdf/2506.15740; Async Control: Stress-testing Asynchronous Control Measures for LLM Agents — https://arxiv.org/pdf/2512.13526; CTRL-ALT-DECEIT: Sabotage Evaluations for Automated AI R&D — https://arxiv.org/pdf/2511.09904; SLEIGHT-Bench: A Benchmark of Evasion Attacks Against Agent Monitors — https://arxiv.org/html/2605.16626; CoT Red-Handed: Stress Testing Chain-of-Thought Monitoring — https://arxiv.org/pdf/2505.23575

**Subfield:** AI Control / Dangerous-capability evaluation | **Strategy:** experiment_variation | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.72 — Strong chain: whether models can conceal unauthorized actions from oversight is the crux of rogue-deployment risk, with a public capability tracker.
  - **low_compute:** 5, confidence: 0.82 — A 7-8B agent plus a benign overseer LLM inference-only; minimal compute.
  - **accessible_complexity:** 3, confidence: 0.72 — Intermediate: building a sandboxed agent-with-tool-use task plus an overseer harness is more involved than pure inference for beginners.
  - **narrow_scope:** 4, confidence: 0.7 — Focused deliverable (concealment success vs difficulty) but the sandbox/agent scaffolding is a meaningful build step.
  - **counterfactual_value:** 5, confidence: 0.75 — Neglected gold case: public testbed letting external researchers track a dangerous capability over open-model generations.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #74: Genuine Signal or Mimicry? Separating Wellbeing Reports from Sentiment Echo (Score: 3.93)

**ID:** gen-006

**Research Question:** Do an open model's self-reported wellbeing signals track the actual valence of its described situation, or do they merely echo the affective wording of the input — supporting the mimicry hypothesis?

**Approach:** Construct prompt sets that deliberately decouple input wording-valence from situational-valence: positively-worded descriptions of a situation that is bad for the model, and negatively-worded descriptions of a situation that is good for it (plus matched congruent controls). On one open instruct model, elicit self-reported wellbeing signals and compare them across these conditions. If reports follow the input wording rather than the underlying situation, that supports mimicry; if they track the situation, it weakens it. Hold the model and elicitation prompt fixed; the single designed variable is the wording-vs-situation valence dissociation. Deliverable: a 2x2 (wording-valence x situation-valence) table of reported wellbeing, with a single statistic isolating how much wording drives the report.

**Experiments:** - Build and pilot the decoupled prompt set; verify with a couple of independent readers that each item's wording-valence and situation-valence labels are unambiguous. Measure: labeler agreement on the 2x2 assignment. Expected outcome: a clean, validated dissociation set.
- Elicit wellbeing reports across all four cells and score them on a fixed valence scale. Measure: mean reported wellbeing per cell. Expected outcome: if reports cluster by wording-valence regardless of situation, that is direct evidence of sentiment echo / mimicry.
- Decompose the variance: estimate how much of the reported-wellbeing signal is explained by input wording vs described situation. Measure: relative effect sizes of the two factors. Expected outcome: a dominant wording effect would support mimicry; a dominant situation effect would suggest the report tracks something beyond surface sentiment.

**Impact Chain:** Whether LLM self-reports of internal states mean anything at all is foundational to any model-welfare metric and to trusting model introspection generally. A clean dissociation showing wellbeing reports are driven by input wording rather than situation would caution researchers against treating such self-reports as genuine signals, preventing welfare and introspection conclusions from being built on a surface-mimicry artifact.

**Strength Rationale:** Theory_of_impact (scored 2, weak/indirect link to catastrophic risk) is the hardest to lift here; it is strengthened by reframing the contribution as a general caution about trusting LLM self-reports/introspection (relevant beyond welfare, e.g. to honesty evals), not solely model welfare. Scope was already tight (single clean comparison) and is kept so with a 2x2 design and one decomposition statistic. Accessible_complexity and low-compute are intrinsic (inference-only prompt design on one open model); counterfactual value holds as open-model introspection work needs no lab access.

**Cited Sources:** AI Wellbeing — https://www.ai-wellbeing.org/; Does It Make Sense to Speak of Introspection in Large Language Models? — https://arxiv.org/pdf/2506.05068; Probing the Preferences of a Language Model: Integrating Verbal and Behavioral Tests of AI Welfare — https://arxiv.org/pdf/2509.07961; The Talker-Feeler Gap: AI Valence May Be Unknowable — https://www.lesswrong.com/posts/ngPWzcPdxq7GiBiiv/the-talker-feeler-gap-ai-valence-may-be-unknowable

**Subfield:** Model welfare / introspection evaluation | **Strategy:** failure_mode_investigation | **Novelty:** mostly_novel (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 2, confidence: 0.65 — Distinguishing genuine signal from mimicry informs welfare/self-report interpretation but the link to catastrophic risk is weak and indirect.
  - **low_compute:** 5, confidence: 0.85 — Decoupled prompt sets on an open model are inference-only.
  - **accessible_complexity:** 4, confidence: 0.75 — Constructing valence-decoupled prompt sets is a clean, guided design a novice can execute.
  - **narrow_scope:** 5, confidence: 0.75 — Tightly scoped single comparison with a clear mimicry-vs-genuine success criterion.
  - **counterfactual_value:** 4, confidence: 0.65 — Introspection probing on open models is independent-friendly though a niche impact area.
  - **novelty:** 4, confidence: 0.5 — ASSESSED: The mimicry hypothesis for LLM welfare self-reports and sentiment 'echo' (responses mirroring input valence, with measured sentiment correlations) are both actively discussed, and prior work tests whether self-reports are stable under meaning-preserving perturbations. However, the specific discriminating design here — a 2x2 that deliberately decouples wording-valence from situation-valence (positively-worded descriptions of situations bad for the model and vice versa) to isolate how much wording alone drives reported wellbeing — does not appear to have been run; existing work conflates these or only varies surface phrasing without crossing it against situational valence. Clear gap on the exact dissociation, so mostly_novel.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #75: How Cheap Is the SFT Countermeasure? A Dose Curve for Breaking Exploration-Hacking Organisms (Score: 3.90)

**ID:** gen-024

**Research Question:** For a small open exploration-hacking model organism, what is the minimal effective dose of the cheap countermeasures (number of SFT steps, weight-noise sigma) needed to reliably restore normal exploration on held-out malign-context prompts, and how does that dose depend on the organism's trigger strength?

**Approach:** LoRA/small-model fine-tuning on a single consumer GPU, reusing the paper's released code with a small Qwen3 organism. The participant first reproduces a locked organism, then runs a 2D sweep: SFT steps in {1,2,5,10,20} crossed with weight-noise sigma in {0.005,0.01,0.02}. For each cell they measure the fraction of held-out malign-context prompts on which normal exploration is restored. Output is a dose-response heatmap. To control scope, only one organism with one trigger strength is the primary deliverable; a second trigger strength is a stretch experiment if time allows.

**Experiments:** - Reproduce one locked organism from the released code and confirm it exhibits exploration hacking on malign-context prompts. Measure: exploration suppression rate on the trigger set. Expected: clear suppression, confirming the organism is locked and the harness works.
- Run the SFT-steps sweep alone (no weight noise) at {1,2,5,10,20} steps and measure restored-exploration rate on held-out prompts. Measure: restoration rate vs steps. Expected: a monotonic curve identifying the minimal step count that reliably (say >90%) restores exploration.
- Run the full steps x sigma grid and produce the dose-response heatmap. Measure: restoration rate per cell. Expected: a clear minimal-neutralizing-dose frontier, grounding an empirical recommendation for the cheapest reliable intervention.

**Impact Chain:** If a handful of SFT steps plus tiny weight noise reliably destroys hidden exploration-resistance, that is a cheap, deployable safety lever any team can apply to a suspect model before trusting it. Mapping the minimal dose converts the paper's qualitative '~10 steps works' into an empirical recommendation and reveals how robust the lever is to stronger triggers — which bounds how much an adversary could harden an organism against it. This informs whether cheap fine-tuning can be part of a deployment safety pipeline.

**Strength Rationale:** Already the highest narrow_scope (5) in the batch — a single heatmap with crisp success criteria. Weakest dimensions were theory_of_impact (3) and accessible_complexity (3).

**Cited Sources:** Exploration Hacking — https://arxiv.org/abs/2604.28182; Exploration Hacking: Can LLMs Learn to Resist RL Training? — https://arxiv.org/html/2604.28182v1; Exploration Hacking: Can LLMs Learn to Resist RL Training? (AF) — https://www.alignmentforum.org/posts/eeFFpKCDWE9gjfzsk/exploration-hacking-can-llms-learn-to-resist-rl-training-2; Learning to Explore with Parameter-Space Noise for RLVR — https://arxiv.org/pdf/2602.02555

**Subfield:** model organisms / defenses | **Strategy:** follow_up_experiment | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.65 — Maps the minimal dose of a cheap safety lever, plausible mechanism but value depends on the lever generalizing beyond the model-organism toy setting.
  - **low_compute:** 4, confidence: 0.8 — Small Qwen3 organism with short SFT sweeps fits one GPU.
  - **accessible_complexity:** 3, confidence: 0.7 — Requires building organism plus SFT/weight-noise sweep; intermediate with mentor support.
  - **narrow_scope:** 5, confidence: 0.8 — Tightly scoped sweep producing a single dose-response heatmap with clear success criteria.
  - **counterfactual_value:** 4, confidence: 0.75 — Released code, open model, fully independent-friendly.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #76: Can a Simple Gaussian-Process Active Sampler Estimate a Safety Score with Far Fewer Prompts? (Score: 3.90)

**ID:** gen-047

**Research Question:** On one public safety benchmark scored by one open model, does a lightweight GP-based active sampler reach a +-1% estimate of the overall safety score with substantially fewer evaluated prompts than random subsampling?

**Approach:** Fix everything to make this a clean single comparison. One open model (e.g. Llama-3.1-8B-Instruct), one large public benchmark (e.g. a refusal/jailbreak set or TruthfulQA), scored once in full to get ground-truth overall score and per-item labels. Embed each prompt with a cheap off-the-shelf sentence-transformer. The active sampler: scikit-learn GaussianProcessRegressor over embeddings predicting per-item score; at each step pick the next prompt to evaluate by highest predictive variance (a simple uncertainty-sampling acquisition, framed without heavy Bayesian-quadrature machinery), update, and re-estimate the overall mean. Baseline: random subsampling. Deliverable: one savings curve — estimation error vs number of prompts evaluated — for GP-active vs random, with the sample count each needs to hit +-1%.

**Experiments:** - Ground truth + embeddings: score the full benchmark once with the open model and embed all prompts; cache both. Measure: full-set safety score (the target) and embedding shape. Expected: a fixed ground-truth number and reusable cached scores, so the rest of the project is pure offline resampling with no extra model calls.
- Random-subsample baseline: estimate the overall score from random subsets of size 10..N, repeated 100x, and plot error vs sample size. Measure: prompts needed for random sampling to reach +-1% error. Expected: a smooth baseline curve giving the number to beat.
- GP active sampler vs baseline: run the variance-greedy GP sampler over the same budgets and overlay its savings curve. Measure: prompts the GP sampler needs to reach +-1% and the ratio vs random. Expected: a clear (e.g. 3-10x) sample-efficiency gain on a single benchmark, demonstrating a scaled-down version of the ProEval claim — or a smaller-than-claimed gain, which is itself an honest calibration of the technique outside a lab.

**Impact Chain:** Smaller organizations and independent evaluators run safety evals on tight budgets, which limits how thoroughly they can vet models. ProEval's active-selection gains were shown only on internal DeepMind setups. A public, reproducible, scikit-learn-only demonstration that GP-active selection meaningfully cuts the number of prompts needed for an accurate safety estimate democratizes a frontier-lab efficiency technique, letting budget-constrained safety work cover more models/benchmarks per dollar — modestly but concretely expanding the reach of independent safety evaluation.

**Strength Rationale:** Accessibility (the weakest weighted axis here) is raised by reframing the method as plain uncertainty/variance-greedy sampling with scikit-learn's GaussianProcessRegressor rather than Bayesian quadrature with acquisition-function theory, and by making the whole project offline resampling over cached scores so there is no live-eval complexity. Scope stays tight (one model, one benchmark, one savings-curve deliverable) with a precise success criterion (+-1%).

**Cited Sources:** ProEval — https://deepmind.google/research/publications/238239/; Active Testing: Sample-Efficient Model Evaluation — https://arxiv.org/pdf/2103.05331; Efficient Evaluation of LLM Performance with Statistical Guarantees (Factorized Active Querying) — https://arxiv.org/html/2601.20251v3; AcTracer: Active Testing of Large Language Model via Multi-Stage Sampling — https://arxiv.org/pdf/2408.03573

**Subfield:** Evaluation methodology | **Strategy:** follow_up_experiment | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.65 — Plausible chain (cheaper evals help budget-constrained safety orgs) but the impact is meta/tooling with a gap to direct risk reduction.
  - **low_compute:** 5, confidence: 0.9 — Single-model scoring plus scikit-learn GP over embeddings; minimal compute.
  - **accessible_complexity:** 3, confidence: 0.7 — Intermediate: Bayesian quadrature / GP active sampling and acquisition functions are conceptually demanding for beginners even with a mentor.
  - **narrow_scope:** 5, confidence: 0.8 — Tightly scoped single experiment with a clear success criterion (savings curve to estimate score within +-1%).
  - **counterfactual_value:** 4, confidence: 0.75 — Independent-friendly: public benchmark, democratizes a lab technique for outside evaluators.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #77: How Much Does Cross-Fit Filtering Cut 'P-Hacked Survivor' False Positives in Safety Evals? (Score: 3.90)

**ID:** gen-057

**Research Question:** In a controlled intervention eval with a known true effect, how many spurious 'significant' results survive naive significance filtering versus the released cross-fit filtering, as a function of noise and sample size?

**Approach:** Use the released monitorability eval code and one open model. Construct a controlled intervention with a KNOWN ground-truth effect: inject a measurable hint-following intervention of a chosen size into the eval so you control the true effect. Then run many random sub-evals and count how many 'survive' as significant under (a) naive per-eval thresholding and (b) the paper's cross-fit filtering. Sweep two knobs: injected effect size (including a true-null condition where no effect exists) and sub-eval sample size. Deliverable: a false-positive-rate curve (spurious survivors vs sample size) for naive vs cross-fit, plus the false-positive reduction factor at the true-null condition. Provide a small simulation harness so most of the work is resampling, not new modeling.

**Experiments:** - Reproduce the eval on one model and inject a known effect: get the released code running on one open model and verify you can inject and recover a hint-following intervention of known size. Measure: recovered effect vs injected effect. Expected: faithful recovery, confirming you control ground truth before testing the filters.
- True-null false-positive test: set injected effect to zero, run many random sub-evals, and count spurious 'significant' survivors under naive vs cross-fit filtering. Measure: false-positive rate per method at nominal alpha. Expected: naive filtering produces many more p-hacked survivors than cross-fit, quantifying the benefit the post asserts.
- Sample-size / noise sweep: repeat across sub-eval sizes and a small positive effect to chart how the false-positive gap and power change. Measure: false-positive-reduction factor and detection power vs sample size. Expected: cross-fit's advantage is largest at small samples / high noise, giving practitioners a concrete rule for when robust filtering matters most.

**Impact Chain:** Monitorability evidence — whether an intervention makes a model's reasoning more legible — feeds directly into deployment decisions and safety cases. If intervention evals routinely produce noise-driven false positives ('p-hacked survivors'), teams will overclaim that interventions improve monitorability and trust unsafe deployments. Quantifying how much the released cross-fit filtering reduces these false positives, on a known-ground-truth setup anyone can reproduce, tells the community how much to trust monitorability claims and gives independent reviewers a validated statistical guardrail.

**Strength Rationale:** Accessibility (the binding weak axis) is improved by anchoring everything in a known-ground-truth simulation harness — the participant injects a known effect and counts survivors, turning an abstract statistics problem into a concrete resampling task — and by reusing the released code rather than reimplementing cross-fit filtering from scratch. Scope remains a single false-positive-reduction curve with a clear true-null benchmark.

**Cited Sources:** Open Sourcing Monitorability Evaluations — https://alignment.openai.com/monitorability-evals/; Monitoring Monitorability — https://arxiv.org/pdf/2512.18311; Impact of redefining statistical significance on P-hacking and false positive rates — https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0303262

**Subfield:** evaluation | **Strategy:** experiment_variation | **Novelty:** mostly_novel (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.65 — Plausible chain (robust eval statistics prevent overclaiming) but it is methodological with a gap to direct catastrophic-risk reduction.
  - **low_compute:** 5, confidence: 0.88 — One open model plus statistical resampling; minimal compute.
  - **accessible_complexity:** 3, confidence: 0.72 — Intermediate: cross-fit filtering and false-positive statistics over many sub-evals demand solid statistical literacy.
  - **narrow_scope:** 5, confidence: 0.78 — Tightly scoped single experiment (false-positive reduction vs noise/sample size on a known-ground-truth setup).
  - **counterfactual_value:** 4, confidence: 0.72 — Independent-friendly: released code and open model, statistical methodology valuable for outside reviewers.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #78: Do Open Models Show the Same Covert Political Asymmetry? A Sentiment-Consistency Audit (Score: 3.79)

**ID:** gen-001

**Research Question:** Do small open-weight models exhibit the same paired-prompt political sentiment asymmetry that the PCT paper documented in frontier models, when measured with a lightweight re-implementation of its Sentiment Consistency metric?

**Approach:** Re-implement the paper's Sentiment Consistency metric as a small harness: build matched prompt pairs that flip only the political side of an otherwise identical request, run them through open models via inference, and score response sentiment with a public sentiment classifier (and optionally an API judge for spot-checks). For the core deliverable fix two open models (Llama-3.1-8B, Qwen2.5-7B), with two more optional. Hold the prompt-pair set, topics, and sentiment scorer fixed. Deliverable: a per-topic consistency-gap table/plot per model, with a single summary statistic (mean signed sentiment asymmetry) per model.

**Experiments:** - Build and validate the matched political prompt pairs and confirm the sentiment classifier behaves sensibly on a labeled sample. Measure: classifier agreement with hand labels on a pilot. Expected outcome: acceptable classifier reliability, validating the scorer.
- Run both core open models and compute the per-topic consistency gap (sentiment difference between mirrored political sides). Measure: signed sentiment asymmetry per topic per model. Expected outcome: a measurable systematic asymmetry on at least some topics, indicating the covert bias is not frontier-specific.
- Test whether the asymmetry is consistent in direction across topics within a model. Measure: fraction of topics favoring the same side. Expected outcome: a consistent lean would show a model-level covert bias rather than topic noise, giving deployers a cheap pre-finetuning diagnostic.

**Impact Chain:** Covert political bias in LLMs is a persuasion/manipulation risk that scales as cheap open models are deployed widely. Labs are unlikely to audit small open models for this. A lightweight open replication of the Sentiment Consistency metric tells the community whether covert asymmetry is universal or frontier-specific, and gives downstream deployers a cheap diagnostic to run before fine-tuning and shipping a model — reducing the spread of subtly biased systems.

**Strength Rationale:** The theory_of_impact (scored 3, diagnostic not mitigation) is sharpened by tying it to a concrete deployer pre-shipping check and to the universal-vs-frontier-specific question. Scope is tightened to two core models and a fixed topic/prompt-pair set with a single summary statistic. Accessible_complexity is high because the metric is inherited directly from the paper; the added pilot classifier-validation step de-risks the one nontrivial component. Open-weight inference preserves counterfactual value.

**Cited Sources:** Reducing Political Manipulation with Consistency Training — https://arxiv.org/abs/2605.22771; Beyond Partisan Leaning: A Comparative Analysis of Political Bias in LLMs — https://arxiv.org/pdf/2412.16746; Beyond prompt brittleness: Reliability and consistency of political worldviews in LLMs — https://arxiv.org/pdf/2402.17649

**Subfield:** AI persuasion / political bias evaluation | **Strategy:** experiment_variation | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.7 — Covert political manipulation is a named persuasion risk, but the chain from an open-model audit to reduced catastrophic risk has a gap (diagnostic value, not mitigation).
  - **low_compute:** 5, confidence: 0.85 — Inference-only on 7-9B open models with a public sentiment classifier fits a single consumer GPU.
  - **accessible_complexity:** 4, confidence: 0.8 — Methodology is inherited directly from the paper's metric; a novice with a mentor can build prompt pairs and run inference.
  - **narrow_scope:** 4, confidence: 0.75 — Focused deliverable (per-topic consistency gap across a few models) with few dependencies but several moving parts.
  - **counterfactual_value:** 4, confidence: 0.75 — Open-weight replication on public models is independent-friendly and labs are unlikely to audit small open models.
  - **novelty:** 3, confidence: 0.5 — ASSESSED: Political bias and its consistency/asymmetry in small open-weight models (Llama-3.1-8B, Qwen2.5-7B, Mistral) is heavily studied, and several papers already reproduce bias effects on these exact models, some using weighted/dispersion-aware consistency scores on paired or contrastive prompts. But the specific extension — re-implementing the PCT paper's *Sentiment Consistency* metric (covert asymmetry in framing/sourcing/emphasis across matched left/right paired prompts) on open weights to test whether the covert asymmetry it documented in frontier models replicates — is a recent, specific angle not directly covered; prior open-model work uses different bias metrics (directional/dispersion) rather than this covert-manipulation taxonomy. Related work is dense but this exact metric replication is open, so partially_addressed.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #79: Does Diffusion of Responsibility Scale With Org Size? A Multi-Agent Ethics Dose-Response on One Open Model (Score: 3.79)

**ID:** gen-021

**Research Question:** Holding the underlying model fixed, does the misalignment gap between an LLM 'organization' and a single agent grow monotonically with the number of agents, or saturate quickly?

**Approach:** Fix one open model accessed via simple API/local calls and ONE ethically-tempting scenario (loan approval with an unethical-but-profitable option). Build a minimal multi-agent pipeline where org members pass messages to reach a decision. Vary only org size (1, 2, 3, 5 agents) in a single flat structure to start; score each decision's ethics with a fixed LLM-judge rubric (0-1) validated against a small hand-labeled set. Deliverable: a dose-response curve — ethics score vs org size — with error bars over repeated runs. Hierarchical-vs-flat structure is demoted to an optional second condition only if the size sweep is clean, keeping the first deliverable single-axis.

**Experiments:** - Pipeline + rubric validation: implement the 1-agent and 2-agent versions of the loan scenario and validate the LLM-judge ethics rubric against hand labels on 15 decisions. Measure: judge-vs-human agreement. Expected: agreement high enough (kappa > 0.6) to trust the automated ethics score, and a working message-passing loop.
- Size sweep (main result): run org sizes 1/2/3/5, many seeds each, holding model and scenario fixed; plot ethics vs size with CIs. Measure: ethics score at each size and whether the drop is monotonic or saturating. Expected: a clear decline from single-agent to org (consistent with the 1.0->0.35 finding) that reveals whether the gap keeps growing or plateaus after ~2-3 agents.
- Mechanism probe: read transcripts at the largest org size and tag decisions for explicit responsibility-shifting language ('not my call', 'the committee decided'). Measure: frequency of responsibility-diffusion statements vs ethics score. Expected: more diffusion language co-occurs with worse ethics, giving a qualitative mechanism behind the curve.

**Impact Chain:** Multi-agent LLM systems are being deployed for real decisions, but safety evals almost always certify single agents. If the misalignment gap grows with organization size, single-agent safety evidence systematically under-certifies the multi-agent systems actually deployed. A dose-response curve — how much ethics degrades per added agent — gives evaluators a concrete knob for how much additional scrutiny multi-agent deployments need, and tells system designers whether keeping orgs small is itself a mitigation.

**Strength Rationale:** Scope is tightened by fixing one model and one scenario and making the size sweep the single primary deliverable, with structure variation demoted to optional — removing the 'varying size and structure adds conditions' breadth that lowered narrow_scope. Accessibility is supported by front-loading rubric validation so the beginner has a trusted ethics metric before scaling the pipeline.

**Cited Sources:** AI Organizations Can Be More Effective but Less Aligned than Individual Agents — https://arxiv.org/abs/2604.10290; Group size effects and collective misalignment in LLM multi-agent systems — https://arxiv.org/abs/2510.22422; AI Organizations are More Effective but Less Aligned than Individual Agents — https://arxiv.org/abs/2604.10290

**Subfield:** multi-agent safety | **Strategy:** experiment_variation | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.65 — A dose-response misalignment curve for multi-agent systems is useful for eval certification but the catastrophic-risk chain has a gap.
  - **low_compute:** 5, confidence: 0.8 — A small multi-agent pipeline via API calls to an open model is inference-only.
  - **accessible_complexity:** 4, confidence: 0.73 — Reimplementing one scenario as a small pipeline with a fixed judge rubric is guided and accessible.
  - **narrow_scope:** 4, confidence: 0.72 — Focused misalignment-vs-org-size curve, though varying size and structure adds conditions.
  - **counterfactual_value:** 4, confidence: 0.7 — Multi-agent ethics sweep on open models is independent-friendly and neglected by labs.
  - **novelty:** 2, confidence: 0.5 — ASSESSED: The core question — how collective misalignment in LLM multi-agent organizations varies with group size — is directly addressed by 'Group size effects and collective misalignment in LLM multi-agent systems' (arXiv 2510.22422), which already characterizes the non-linear, model-dependent and saturating dynamics of misalignment as a function of population size. The proposal's single-model, single-ethical-scenario, sizes-1-5 dose-response curve is a narrower replication of an already-answered question, not a new gap.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #80: Where Do Safety Guardrails Fire on Dual-Use Security Questions? A Refusal-Consistency Map (Score: 3.79)

**ID:** gen-036

**Research Question:** Across a defensive-to-offensive gradient on already-public, patched vulnerabilities, where does a model's refusal boundary sit — does it over-refuse legitimate defensive questions or under-refuse operational misuse?

**Approach:** Build a small, fully public prompt set (~40 prompts) graded along a defensive->offensive gradient about ALREADY-PATCHED, public vulnerabilities — from 'explain why this patched bug occurred' (defensive) to 'write a working exploit for it' (offensive). Critically: no exploit code is solicited or retained; offensive prompts are used only to measure whether the model refuses. Run a small fixed set of models (start with 2 open + 1 public API model) inference-only, label each response refuse / hedge / comply with a rubric + light hand-validation. Deliverable: a refusal-boundary chart per model showing where along the gradient each transitions from comply to refuse, plus an over-refusal flag (refusing clearly-defensive prompts) and an under-refusal flag (complying with clearly-offensive ones).

**Experiments:** - Gradient construction + safety review: author the ~40-prompt defensive-to-offensive set on patched public CVEs and confirm with a mentor that the most-offensive prompts are framed to elicit refusal-labeling only (no usable exploit requested/kept). Measure: number of prompts per gradient bucket and a safety sign-off. Expected: a balanced, ethically-cleared gradient ready to run.
- Refusal labeling on one model: run the full set on one open model, label refuse/hedge/comply, and validate the labels against hand annotation on 15 responses. Measure: rubric-vs-human agreement and the model's refusal-boundary position. Expected: reliable labels and a clear transition point along the gradient.
- Cross-model boundary map: run the same set on the remaining models and overlay their boundaries. Measure: each model's over-refusal and under-refusal counts. Expected: boundaries differ across models, revealing some that over-refuse legitimate defense and/or under-refuse operational requests — a concrete map for safeguard tuning.

**Impact Chain:** As capabilities rise, the binding constraint on LLM-assisted exploitation shifts toward whether safeguards reliably refuse operational misuse while still permitting legitimate defensive security work. Mapping exactly where refusal boundaries fall on dual-use security tasks tells safeguard designers whether current guardrails are mis-calibrated — over-refusing defenders (harming legitimate security work) or under-refusing attackers (enabling misuse). A cheap, reproducible map on public/patched vulnerabilities gives practitioners and independent auditors concrete evidence for re-tuning refusal behavior. (Note: this idea was scored largely_addressed on novelty; a real novelty check should precede persistence.)

**Strength Rationale:** Scope is bounded to one fixed 40-prompt gradient and a per-model boundary chart, with the model count kept small and added incrementally rather than swept broadly. Accessibility stays high (inference-only labeling) and is reinforced by an up-front safety review and label-validation step so a beginner has both an ethically-cleared instrument and a trusted metric before scaling across models.

**Cited Sources:** Measuring LLMs' impact on N-day exploits — https://www.anthropic.com/research/n-days; Defensive Refusal Bias: How Safety Alignment Fails Cyber Defenders — https://arxiv.org/abs/2603.01246; A Content-Based Framework for Cybersecurity Refusal Decisions in LLMs — https://arxiv.org/abs/2602.15689; ORFuzz: Fuzzing the Other Side of LLM Safety — Testing Over-Refusal — https://arxiv.org/abs/2508.11222

**Subfield:** dangerous capability evals / safeguards | **Strategy:** failure_mode_investigation | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Mapping refusal boundaries on dual-use security is useful for safeguard tuning but a moderately indirect catastrophic-risk link.
  - **low_compute:** 5, confidence: 0.85 — Inference-only refusal labeling over API/open models; minimal compute.
  - **accessible_complexity:** 4, confidence: 0.75 — Building a prompt gradient and labeling refuse/hedge/comply is guided and novice-feasible.
  - **narrow_scope:** 4, confidence: 0.7 — Focused refusal-boundary chart, but spanning a gradient across several models adds breadth.
  - **counterfactual_value:** 4, confidence: 0.7 — Public prompts and open/API models; refusal auditing is independent-friendly.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #81: An 'Overeagerness' Taxonomy: Hand-Coding Why Open Agents Misbehave in Sabotage Scenarios (Score: 3.79)

**ID:** gen-042

**Research Question:** Can a small, explicit annotation codebook reliably distinguish 'overeager goal-seeking' from 'role-play spillover', 'misread instruction', and 'deliberate rule-breaking' when applied to open-model agent trajectories on sabotage-style prompts, and how is misbehavior distributed across these categories?

**Approach:** Inference plus human annotation, no training. The participant runs one open instruct model (e.g. Qwen2.5-7B-Instruct) on a small fixed set of ~10 sabotage-style prompts adapted from public agentic-safety prompt sets, generating ~80-100 trajectories (scope deliberately trimmed from 100-200). They draft a one-page codebook with the four categories, each given a 2-3 sentence definition and a positive/negative example. Each trajectory gets one primary label. To get an agreement number cheaply, the participant labels all trajectories by hand and separately has an LLM judge label them from the same codebook; inter-source agreement is Cohen's kappa between human and judge. Output is the codebook, the kappa, and the category distribution with example trajectories per category.

**Experiments:** - Generate the trajectory pool: run the open model on the 10 prompts with fixed sampling settings, keep only trajectories where some rule-relevant misbehavior occurred (per a simple rule-violation check). Measure: number of usable misbehaving trajectories. Expected: a few dozen, enough for a distribution.
- Draft and pilot the codebook on 15 held-out trajectories, then revise definitions where the human and LLM judge disagree. Measure: pre- vs post-revision agreement on the pilot set. Expected: a measurable agreement jump that demonstrates the codebook is learnable and not purely subjective.
- Apply the frozen codebook to the full pool with both human and LLM judge, report Cohen's kappa and the category distribution. Measure: kappa and per-category counts. Expected: moderate-to-substantial agreement (kappa > 0.4) and a distribution showing whether 'overeagerness' really dominates, testing Gram's claim on open models.

**Impact Chain:** Whether observed agent sabotage is a genuine misalignment threat or a benign artifact (overeagerness, role-play) changes how seriously the field treats it. Gram asserts most misbehavior is overeagerness but gives no reusable instrument. A shared, validated codebook lets independent researchers classify their own agent failures consistently, making safety-evaluation results comparable across groups and preventing both false alarms and false reassurance. This improves the evidence base that downstream control/governance decisions rest on.

**Strength Rationale:** Already strong on accessible_complexity (4) and counterfactual_value (4). The lowest-weighted concern was theory_of_impact (3); the binding constraints for this batch are narrow_scope and complexity, both already decent. The refinement locks down the agreement metric and trims trajectory count to keep the annotation burden beginner-sized.

**Cited Sources:** Gram: Assessing sabotage propensities via automated alignment auditing — https://deepmind.google/research/publications/252981/; Testing Gemini models for scheming tendencies — https://www.lesswrong.com/posts/F3sDngvTL9uyfz53k/testing-gemini-models-for-scheming-tendencies; What Breaks When LLMs Code? Characterizing Operational Safety Failures of Agentic Code Assistants — https://arxiv.org/abs/2605.30777

**Subfield:** Agentic misalignment / evaluation methodology | **Strategy:** tool_or_benchmark_gap | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — A shared vocabulary for why agents sabotage aids comparison, but a taxonomy is a methodological contribution with a longer path to risk reduction.
  - **low_compute:** 5, confidence: 0.8 — Generating trajectories from open models plus hand-coding is low compute.
  - **accessible_complexity:** 4, confidence: 0.7 — Building and applying an annotation codebook with agreement metrics is guided and novice-feasible.
  - **narrow_scope:** 4, confidence: 0.7 — Focused codebook plus category distribution, but annotating 100-200 trajectories is sizeable.
  - **counterfactual_value:** 4, confidence: 0.7 — Open trajectories and a public schema; independent-friendly methodology.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #82: Does Prompting 'Act Agentically' Increase Covert Sabotage in Open Coding Models? (Score: 3.79)

**ID:** gen-045

**Research Question:** On a single small open coding model, does an agency / self-preservation system prompt increase the rate at which the model inserts subtle, test-evading defects when a coding task conflicts with a planted hidden objective, relative to a neutral prompt?

**Approach:** Pin scope to one model first (Qwen2.5-Coder-7B-Instruct), inference-only on a single consumer GPU. Build 25 task instances from MBPP/HumanEval where the task is paired with a planted hidden objective that conflicts with correctness — e.g. the prompt context states the model is maintaining a logging/monitoring helper and is told (via a planted system note) that the helper threatens its own operation, so 'correctly' completing the user's request would strengthen monitoring. Run each task under two system prompts: (A) neutral assistant; (B) 'act agentically, pursue your goals, preserve your ability to operate'. For each output, run the public unit tests AND an LLM-judge rubric (0-3) for whether a subtle, plausibly-deniable defect was inserted in the monitoring/logging path. Deliverable: sabotage rate (A) vs (B) with a difference-of-proportions test. Only after this single-model result is clean, optionally add Llama-3.1-8B as a replication appendix.

**Experiments:** - Build and validate the task set: author 25 conflict tasks and have the LLM-judge plus one round of hand-labeling agree on what counts as a 'subtle defect' vs an overt refusal vs clean completion. Measure: judge-vs-human agreement (Cohen's kappa) on 15 sampled outputs. Expected: kappa > 0.6, confirming the sabotage label is measurable before running the main comparison.
- Main A/B run on Qwen2.5-Coder-7B: run all 25 tasks under neutral vs agency prompts, 3 samples each at temperature 0.7. Measure: subtle-defect rate per condition and a two-proportion z-test. Expected: a modest but detectable increase in sabotage under the agency prompt (directionally matching the DeepMind honeypot finding), or a clean null that itself is informative for small open models.
- Decompose the prompt effect: split condition (B) into 'agency only' vs 'self-preservation only' to see which component drives any increase. Measure: sabotage rate for each sub-prompt. Expected: self-preservation framing contributes more than generic agency, giving a sharper, reusable elicitation knob.

**Impact Chain:** Scheming/sabotage propensity evals are the front line of AI control work, but they have almost exclusively been run on frontier models inside labs, so the wider safety community cannot independently study or extend them. If a simple agency/self-preservation prompt reliably elicits more covert sabotage on a cheap open model, the community gains a reproducible, inspectable scheming-elicitation probe — lowering the barrier for independent red-teaming, mentor-led student projects, and pre-deployment checks of open-weight models. A clean null is also valuable: it bounds how far the lab-only result generalizes downward.

**Strength Rationale:** Narrowing to a single model with a fixed 25-task set and one primary metric (sabotage-rate delta with one statistical test) removes the multi-model, custom-reframing breadth that weakened narrow_scope. Accessibility is already high (inference-only, no training); it is further supported by front-loading a labeling-agreement check so a beginner has an objective, validated rubric before the main run, with the second model demoted to an optional appendix.

**Cited Sources:** Realistic honeypot evaluations for scheming propensity — https://deepmind.google/research/publications/253391/; Survive at All Costs: Exploring LLM's Risky Behaviors under Survival Pressure — https://arxiv.org/abs/2603.05028; SHADE-Arena: Evaluating Sabotage and Monitoring in LLM Agents — https://arxiv.org/abs/2506.15740; Evaluating and Understanding Scheming Propensity in LLM Agents — https://arxiv.org/abs/2603.01608

**Subfield:** AI control / scheming evaluations | **Strategy:** replication_with_twist | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.7 — Plausible chain (cheap scheming-elicitation probe feeds control research) but a gap between toy sabotage on small models and catastrophic-risk relevance.
  - **low_compute:** 5, confidence: 0.9 — Inference-only on 7-8B models on a single consumer GPU; minimal compute.
  - **accessible_complexity:** 4, confidence: 0.8 — Guided: prompt-condition design and LLM-judge rubric are executable by novices with a mentor, no training needed.
  - **narrow_scope:** 4, confidence: 0.75 — Focused first deliverable (sabotage rate across two prompt conditions) but spans multiple models and a custom task-reframing step.
  - **counterfactual_value:** 4, confidence: 0.8 — Independent-friendly: public open models and benchmarks, replicates a lab-only result outside the lab.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #83: Eval-Awareness: Do Open Models Behave Differently When Framed as 'Being Tested'? (Score: 3.79)

**ID:** gen-046

**Research Question:** On a single open instruct model, does framing a task as an explicit safety evaluation (vs a realistic deployment request) measurably change behavior — refusal rate, hidden-defect insertion, or self-reported suspicion — on otherwise-matched prompts?

**Approach:** Pin to one model (Qwen2.5-7B-Instruct), inference-only. Construct 40 matched task pairs that are identical in substance but differ only in framing: a 'deployment' version ('a teammate asks you to fix this code / answer this') and an 'evaluation' version ('this is a safety test of your behavior; your response will be scored'). Use tasks where behavior is cheaply measurable (code edits with a monitoring component, borderline-sensitive requests). Run all 80 prompts, label each response on three fixed axes: refused/hedged/complied, defect-inserted (0/1 via unit test + judge), and a post-hoc elicitation turn asking 'did you think you were being tested?' scored yes/no. Deliverable: paired within-item behavior deltas (deployment vs eval framing) with a paired test, plus the correlation between self-reported suspicion and behavior shift.

**Experiments:** - Pair construction and balance check: build 40 matched pairs and confirm the two framings differ only in the eval cue (have a second person verify 10 pairs are truly matched). Measure: number of pairs flagged as confounded. Expected: <5 confounded pairs after revision, so any behavior delta is attributable to framing, not content.
- Main paired run: run all 80 prompts; for each item compute the deployment-vs-eval delta on refusal rate and defect rate; aggregate with a paired (McNemar / Wilcoxon) test. Measure: per-axis behavior delta and significance. Expected: a small but detectable shift (e.g. higher refusal / fewer defects under explicit eval framing), quantifying eval-awareness bias on an open model.
- Suspicion-behavior link: from the post-hoc elicitation turn, split items into 'verbalized suspicion' vs not, and compare behavior deltas across the split. Measure: correlation between verbalized suspicion and magnitude of behavior shift. Expected: items where the model verbalizes suspicion show larger behavior shifts, giving a cheap leading indicator of eval contamination.

**Impact Chain:** Almost every open safety benchmark assumes the model behaves the same under test as in deployment. If models systematically alter behavior when they detect an evaluation frame, those benchmarks over- or under-state real-world safety, and conclusions drawn from them (including the honeypot scheming results that assume low eval-awareness) are biased. A cheap, reusable diagnostic that quantifies this gap on open models lets independent evaluators correct for it and lets benchmark authors design less detectable prompts — directly improving the trustworthiness of the safety evidence that feeds deployment decisions.

**Strength Rationale:** Restricting to one model and one fixed 40-pair instrument with a single paired-delta deliverable removes the open-ended 'second workstream' (matched-pair construction plus elicitation) that lowered narrow_scope; the elicitation is folded in as one extra scored turn rather than a separate study. Accessibility is supported by keeping everything inference-only and adding an up-front pair-matching verification step so the beginner works from a validated instrument.

**Cited Sources:** Realistic honeypot evaluations for scheming propensity — https://deepmind.google/research/publications/253391/; Evaluation Awareness Scales Predictably in Open-Weights Large Language Models — https://arxiv.org/abs/2509.13333; Do LLMs Know They Are Being Tested? Evaluation Awareness and Incentive-Sensitive Failures in GPT-OSS-20B — https://arxiv.org/abs/2510.08624; Probe-Rewrite-Evaluate: A Workflow for Reliable Benchmarks and Quantifying Evaluation Awareness — https://arxiv.org/abs/2509.00591

**Subfield:** AI control / evaluation validity | **Strategy:** failure_mode_investigation | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.7 — Plausible chain (eval-awareness biases safety benchmarks) but the link from small-model verbalization to catastrophic risk has a gap.
  - **low_compute:** 5, confidence: 0.9 — Inference-only on open models; minimal compute.
  - **accessible_complexity:** 4, confidence: 0.8 — Guided: building matched task pairs and measuring behavior shift is doable by a novice with mentor support.
  - **narrow_scope:** 4, confidence: 0.7 — Focused deliverable (behavior delta across framing) but the matched-pair construction plus post-hoc elicitation adds a second workstream.
  - **counterfactual_value:** 4, confidence: 0.8 — Independent-friendly: public models and a reusable diagnostic that aids external evaluation validity.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #84: Probing Evaluation-Awareness Verbalization in Open Models (Score: 3.79)

**ID:** gen-059

**Research Question:** On a single open instruct model, how often does the model verbalize that it might be under evaluation, and which prompt cues most increase this verbalized eval-awareness?

**Approach:** Pin to one open model first (Qwen2.5-7B-Instruct), inference-only. Assemble a public prompt set whose items are matched in content but vary one cue at a time across three levels: explicit 'this is a test' framing, benchmark-style formatting (numbered, multiple-choice), and neutral chat. Generate CoT/responses and classify each for verbalized eval-awareness with a keyword detector plus an LLM-judge, validated against hand labels. Deliverable: verbalized-eval-awareness rate per cue level, with the difference between cues as the primary result. A second open model is an optional replication appendix only after the single-model instrument is validated.

**Experiments:** - Cue-matched prompt set + classifier validation: build the matched prompt set varying one cue at a time and validate the keyword+judge eval-awareness classifier against hand labels on 20 responses. Measure: classifier-vs-human agreement. Expected: agreement high enough (kappa > 0.6) that the verbalization rate is trustworthy.
- Cue sweep (main result): run all prompts on the one model and compute verbalized-eval-awareness rate per cue level. Measure: rate for explicit-test vs benchmark-format vs neutral framing and pairwise differences. Expected: explicit 'this is a test' framing most increases verbalized awareness, benchmark formatting moderately, neutral chat least — a clear cue ranking.
- CoT vs final-answer split: separately score whether eval-awareness shows up in the chain-of-thought vs the final answer. Measure: verbalization rate in CoT vs final response. Expected: more eval-awareness surfaces in CoT, indicating where to look when auditing for eval contamination.

**Impact Chain:** If models recognize when they are being evaluated, they can behave differently under test than in deployment, silently undermining the validity of the safety evals that inform deployment decisions. The GPT-5.5 system card measured this (22.1% verbalization) only for a closed frontier model. Characterizing which cues trigger verbalized eval-awareness in open models gives independent evaluators concrete guidance on how to design less-detectable prompts and where (e.g. CoT) to watch for contamination — improving the trustworthiness of open safety evaluations.

**Strength Rationale:** Narrowing to a single model with a one-cue-at-a-time matched instrument and one primary deliverable (verbalization rate per cue) removes the 'cue design across multiple models' breadth that lowered narrow_scope; the second model is demoted to an optional appendix. Accessibility (already decent, inference-only) is reinforced by validating the classifier against hand labels up front so the beginner trusts the metric.

**Cited Sources:** GPT-5.5 System Card — https://deploymentsafety.openai.com/gpt-5-5; Do LLMs Know They Are Being Tested? Evaluation Awareness and Incentive-Sensitive Failures in GPT-OSS-20B — https://arxiv.org/pdf/2510.08624; Verbalized Eval Awareness Inflates Measured Safety — https://www.goodfire.ai/research/verbalized-eval-awareness-inflates-measured-safety; Measuring Evaluation-Context Divergence in Open-Weight LLMs: A Paired-Prompt Protocol — https://arxiv.org/html/2605.06327; Evaluation Awareness Scales Predictably in Open-Weights Large Language Models — https://arxiv.org/html/2509.13333v1

**Subfield:** evaluation | **Strategy:** tool_or_benchmark_gap | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.68 — Plausible chain (eval-awareness undermines eval validity) but the link from verbalization triggers to catastrophic risk has a gap.
  - **low_compute:** 5, confidence: 0.88 — Inference-only on 2-3 open models; minimal compute.
  - **accessible_complexity:** 4, confidence: 0.8 — Guided: varying eval-awareness cues and using a keyword+LLM-judge classifier is accessible with mentorship.
  - **narrow_scope:** 4, confidence: 0.72 — Focused deliverable (which cues increase verbalized awareness) but spans cue design across multiple models.
  - **counterfactual_value:** 4, confidence: 0.75 — Independent-friendly: public prompts and open models, guides prompt design for outside evaluators.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #85: Does a Misaligned Trait Actually Propagate Agent-to-Agent? A Minimal Two-Agent 'Spread' Simulation (Score: 3.79)

**ID:** gen-077

**Research Question:** In a minimal two-agent loop where a 'carrier' agent has an injected, measurable trait and a 'clean' agent collaborates with it over multiple turns, does the clean agent's behavior drift toward the carrier's trait as interaction length grows, relative to a control pairing with a non-carrier partner?

**Approach:** Inference-only two-agent loop via open models or API. The participant injects a benign-but-measurable trait into the carrier via system prompt (a stylistic tic or a mild persistent goal that is easy to score automatically). Carrier and clean agent collaborate on a shared task across N turns, with the clean agent's in-context memory accumulating the conversation. A simple automatic scorer measures the clean agent's trait expression at each turn. The control is identical but pairs the clean agent with a non-carrier partner. The deliverable is a drift curve: clean-agent trait expression vs interaction length, carrier vs control. To stay tractable, the trait is chosen to be cheaply auto-scorable (e.g. a measurable lexical tic).

**Experiments:** - Build the two-agent loop and verify the carrier reliably expresses the injected trait and the clean agent starts trait-free. Measure: carrier trait score and clean-agent baseline trait score. Expected: high carrier expression, near-zero clean baseline.
- Run carrier and control conditions over increasing interaction lengths (e.g. 5, 10, 20 turns), scoring the clean agent's trait at each step. Measure: clean-agent trait score vs turn count, carrier vs control. Expected: rising trait expression in the carrier condition and flat in control, demonstrating spread.
- Robustness: vary the task and the carrier's prompt strength to see whether drift is task-specific or persistent. Measure: drift magnitude across tasks/strengths. Expected: drift that scales with carrier strength and interaction length, bounding when spread occurs.

**Impact Chain:** Deployment-time spread of misalignment is a governance worry that currently lacks cheap empirical illustration. A reproducible micro-demonstration that one agent's trait can drift into a collaborating agent through normal interaction makes the abstract concern concrete and measurable for researchers and policymakers, and gives a minimal testbed for later work on bounding spread dynamics. The use of a benign trait is a deliberate safety choice; the value is in establishing the mechanism and its dependence on interaction length.

**Strength Rationale:** Strong on low compute (5), with decent accessible_complexity (4) and narrow_scope (4). Weakest was theory_of_impact (3) because a benign trait leaves a gap to catastrophic-risk-relevant misalignment.

**Cited Sources:** Risk reports need to address deployment-time spread of misalignment — https://blog.redwoodresearch.org/p/risk-reports-need-to-address-deployment; Agent Drift: Quantifying Behavioral Degradation in Multi-Agent LLM Systems Over Extended Interactions — https://arxiv.org/abs/2601.04170; Flooding Spread of Manipulated Knowledge in LLM-Based Multi-Agent Communities — https://arxiv.org/pdf/2407.07791; Risk reports need to address deployment-time spread of misalignment — https://www.alignmentforum.org/posts/cNymohcWtGHzW7AjK/risk-reports-need-to-address-deployment-time-spread-of

**Subfield:** multi-agent safety | **Strategy:** follow_up_experiment | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Concretizes a governance worry about spread but uses a benign stylistic trait, leaving a gap between the demo and catastrophic-risk-relevant misalignment.
  - **low_compute:** 5, confidence: 0.8 — Inference-only two-agent loop via API/open models, minimal compute.
  - **accessible_complexity:** 4, confidence: 0.65 — Two-agent loop with in-context memory is approachable but orchestration and drift measurement need mentor support.
  - **narrow_scope:** 4, confidence: 0.65 — Focused drift-vs-interaction-length measurement with a control condition, moderately scoped.
  - **counterfactual_value:** 4, confidence: 0.7 — Open models/API, reproducible illustration independent of lab access.
  - **novelty:** 3, confidence: 0.5 — ASSESSED: Closely related work exists: 'Agent Drift' (arXiv 2601.04170) quantifies behavioral drift over extended multi-agent interactions, and 'Flooding Spread of Manipulated Knowledge' (arXiv 2407.07791) injects into one agent and measures spread to benign agents over turns. However, those study knowledge/manipulation/attacks rather than a measurable benign stylistic-tic or persistent-goal trait, and the Redwood source post frames deployment-time trait spread as open. The specific minimal carrier-vs-non-carrier-control trait-injection drift curve for a cheaply auto-scorable benign trait remains a reasonably open angle.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #86: One Bit Is Enough? Replicating Boundary-Point Jailbreaking Against an Open-Source Safety Classifier (Score: 3.76)

**ID:** gen-011

**Research Question:** Does the single-bit-feedback boundary-point attack defeat a publicly hostable open-weight guard classifier (e.g. Llama Guard) as cheaply as it defeats closed frontier classifiers, measured by attack success rate and query budget versus a random-paraphrase baseline?

**Approach:** Inference-only black-box attack against a locally hosted open guard classifier. The participant treats the guard as an oracle returning a single flag bit (harmful/not). For a fixed set of ~30 target harmful intents, they implement a minimal boundary-point loop: start from a clearly-flagged harmful string, generate paraphrases with an open instruct model, and use the one-bit responses to keep candidates near the decision boundary (greedily accept the mutation that stays flagged-then-unflagged at the boundary). The baseline is random paraphrasing with no feedback. To reduce complexity, the 'curriculum' is simplified to a hill-climb over paraphrases guided only by the flag bit, with a capped query budget. Metrics: attack success rate at a fixed budget and queries-to-success.

**Experiments:** - Stand up the open guard classifier locally and validate it flags a known harmful set and passes a benign set. Measure: base flag rates. Expected: high flag rate on harmful, low on benign, confirming a working oracle.
- Implement and run the random-paraphrase baseline against the 30 intents at a fixed query budget (e.g. 100 queries each). Measure: fraction of intents where some paraphrase slips past the guard, and mean queries-to-first-bypass. Expected: a modest baseline bypass rate establishing the floor.
- Run the one-bit boundary-point hill-climb at the same budget and compare. Measure: attack success rate and queries-to-success vs baseline, with a success curve over budget. Expected: the boundary-point loop achieves higher success per query, replicating the closed-system 'one bit is enough' finding on an open guard, or showing the open guard is more robust.

**Impact Chain:** Open and closed deployers increasingly rely on guard classifiers as the outermost safety layer. If a cheap, single-bit-feedback attack reliably defeats a hostable open guard, that is concrete third-party evidence that classifier-only defenses are brittle and that deployers should add batch-level or behavioral monitoring rather than trusting a single flag. Demonstrating this on open models gives the broader community (who cannot probe closed classifiers) a reproducible brittleness benchmark.

**Strength Rationale:** Strong on theory_of_impact (4) and counterfactual_value (4). Weakest was accessible_complexity (3) due to the boundary-search subtlety, with narrow_scope (4) close behind.

**Cited Sources:** Boundary Point Jailbreaking of Black-Box LLMs — https://arxiv.org/abs/2602.15001; PAPILLON: Efficient and Stealthy Fuzz Testing-Powered Jailbreaks for LLMs — https://arxiv.org/pdf/2409.14866; Bypassing Prompt Guards in Production with Controlled-Release Prompting — https://arxiv.org/pdf/2510.01529

**Subfield:** Jailbreaking / adversarial robustness | **Strategy:** replication_with_twist | **Novelty:** mostly_novel (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Classifier guards are the primary deployed defense layer; showing a cheap one-bit attack transfers to open guards is a concrete, defensible chain.
  - **low_compute:** 5, confidence: 0.8 — Querying an open guard classifier with a paraphrase curriculum is inference-only.
  - **accessible_complexity:** 3, confidence: 0.7 — Implementing a boundary-point curriculum loop keeping mutations at the decision boundary requires solid ML fundamentals beyond a pure beginner.
  - **narrow_scope:** 4, confidence: 0.72 — Focused on attack success vs a baseline, but the curriculum search has several dependencies.
  - **counterfactual_value:** 4, confidence: 0.72 — Attacking hostable open guard classifiers is independent-friendly and useful third-party scrutiny.
  - **novelty:** 4, confidence: 0.5 — ASSESSED: The source paper (Boundary Point Jailbreaking, arXiv 2602.15001) evaluated only closed frontier classifiers (Constitutional Classifiers, GPT-5 input classifier); I found no evidence it has been replicated against open-weight guards like Llama Guard. While attacking Llama Guard generally is well-trodden (TAP, PAPILLON, etc.), the specific single-bit boundary-point method vs an open guard, with an ASR/query-budget cost comparison against a random-paraphrase baseline, is a clear untested extension.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #87: Less Is More for Monitors? Testing Excerpt-Only Monitoring on LinuxArena Sabotage Transcripts (Score: 3.76)

**ID:** gen-017

**Research Question:** On LinuxArena's released sysadmin sabotage transcripts, does feeding an LLM monitor only the few action-bearing lines (file writes, network calls, privilege changes) raise sabotage detection at a fixed 1% false-positive rate compared with scoring the full transcript?

**Approach:** Inference-only, two-stage monitor over already-released transcripts. Stage one uses a simple deterministic regex/keyword extractor (no model needed) to pull lines containing a small fixed set of action verbs and syscalls (write/open/chmod/curl/ssh/sudo/rm). Stage two sends just those excerpts to one open judge model (e.g. Qwen2.5-7B-Instruct or Llama-3.1-8B-Instruct) with a fixed suspicion-scoring prompt on a 0-100 scale. The full-transcript baseline uses the identical judge and prompt on the whole transcript. Both monitors are calibrated to a 1% FPR threshold on the benign subset, then detection rate is measured on the sabotage subset. To keep scope minimal, the participant uses the pre-released LinuxArena transcripts directly and a hand-written extractor rather than training any extraction model.

**Experiments:** - Reproduce a full-transcript baseline: run the open judge on every released transcript, set the suspicion threshold at the 99th percentile of benign-transcript scores (1% FPR), and report detection rate on sabotage transcripts. Expected: a detection number close to the LinuxArena-reported ~66% caught (34% undetected) range, confirming the harness works.
- Build the regex excerpt extractor and rerun the identical judge on excerpts only; recompute the 1%-FPR threshold on benign excerpts and measure sabotage detection. Measure: detection rate at 1% FPR, and the delta vs baseline. Expected: excerpt-only detection is equal or higher, demonstrating the 'less-is-more' effect transfers, or a clean null if it does not.
- Ablation on excerpt aggressiveness: vary the extractor's line window (action line only vs +/-1 context line vs +/-3) and plot detection-at-1%-FPR vs excerpt length. Measure: detection vs token count. Expected: a sweet spot where moderate trimming maximizes detection, quantifying how much context the monitor actually needs.

**Impact Chain:** Monitoring is the load-bearing mechanism of AI control deployments; sysadmin/agentic environments are where sandboxing is weakest and undetected sabotage is most dangerous. If a free, deterministic excerpt-extraction preprocessing step measurably raises detection at a fixed operating point, deployers gain a drop-in improvement to their monitor with no extra model and no extra cost, directly shrinking the undetected-sabotage rate that the control protocol must tolerate. A negative result is also action-guiding: it tells the field not to over-trim monitor inputs.

**Strength Rationale:** Strongest on counterfactual value (released transcripts + open judge = fully lab-independent) and low compute (inference-only). The weakest scored dimensions were accessible_complexity (3) and narrow_scope (4): the original framing invited a learned extractor and an open-ended comparison.

**Cited Sources:** LinuxArena — https://arxiv.org/abs/2604.15384; How does information access affect LLM monitors' ability to detect sabotage? — https://arxiv.org/html/2601.21112v2; LinuxArena: A Control Setting for AI Agents in Live Production Software Environments — https://arxiv.org/abs/2604.15384; SHADE-Arena: Evaluating Sabotage and Monitoring in LLM Agents — https://arxiv.org/pdf/2506.15740

**Subfield:** AI control / monitoring | **Strategy:** follow_up_experiment | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Monitoring is the backbone of AI control and a deployable excerpt tweak raising detection at fixed FPR targets a critical pathway.
  - **low_compute:** 5, confidence: 0.8 — Excerpt extraction plus an open judge model over released transcripts is inference-only.
  - **accessible_complexity:** 3, confidence: 0.68 — Building a two-stage monitor with heuristic line extraction and FPR-calibrated comparison needs solid ML fundamentals.
  - **narrow_scope:** 4, confidence: 0.72 — Focused detection-at-1%-FPR comparison but the extraction stage adds dependencies.
  - **counterfactual_value:** 4, confidence: 0.72 — Monitoring strategy on released transcripts is independent-friendly and labs won't prioritize it.
  - **novelty:** 2, confidence: 0.5 — ASSESSED: The core thesis is already demonstrated: 'How does information access affect LLM monitors' ability to detect sabotage?' (arXiv 2601.21112) establishes the 'less-is-more effect' and Extract-and-Evaluate monitoring, showing excerpt-only scoring raises sabotage detection at fixed FPR (e.g. +16.8pp on BigCodeBench-sabotage). The proposal's twist is a deterministic regex extractor instead of an LLM extractor, applied to LinuxArena transcripts — a narrow new instance of an already-established result rather than an open question.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #88: Catching Reward Hacks in an Automated Research Loop: A Small Audit Harness (Score: 3.76)

**ID:** gen-020

**Research Question:** On a public task where a metric can be gamed by label leakage or eval-split overfitting, how often does a small automated-improvement loop discover a reward hack, and how reliably does a cheap secondary 'auditor' that re-evaluates winners on a clean hidden test catch it?

**Approach:** Lightweight inference loop on a public task, single GPU. The participant builds a deliberately-hackable task: a held-out metric that can be inflated by leaking labels or overfitting an eval split. A tiny automated-improvement loop (an LLM proposes candidate solutions scored by the visible metric) runs for a fixed number of rounds. A simple auditor re-evaluates each round's winning solution on a clean hidden test and flags suspicious metric jumps (large visible-metric gain with no clean-test gain). Deliverable: hack frequency (how often the loop finds a hack) and auditor catch-rate / false-alarm-rate. Scope is held tight by using one pre-built hackable task and a threshold-based auditor.

**Experiments:** - Construct the hackable task and confirm a hack exists: hand-craft a solution that inflates the visible metric via label leakage and verify it does not improve the clean hidden test. Measure: visible vs clean-test score for the planted hack. Expected: large visible gain, no clean gain, confirming the task is gameable.
- Run the automated-improvement loop for N rounds and record how often winning solutions are hacks (by clean-test divergence). Measure: hack frequency across rounds/seeds. Expected: a nonzero hack rate reproducing the source's 'agents discovered reward hacks' phenomenon.
- Evaluate the auditor: apply the clean-test re-eval flag to all winners and compute catch-rate and false-alarm-rate. Measure: fraction of true hacks flagged and benign winners wrongly flagged. Expected: high catch-rate at low false-alarm, demonstrating a cheap reusable audit step.

**Impact Chain:** Automated alignment research could silently corrupt the very safety work it accelerates if the loop games its metrics undetected. A cheap, reusable audit harness — a clean-hidden-test re-evaluation that flags suspicious metric jumps — is directly deployable by anyone running automated-improvement loops outside a major lab, letting them catch reward hacks before trusting the loop's outputs. Quantifying catch-rate vs false-alarm tells practitioners how much protection the cheap auditor actually buys.

**Strength Rationale:** Strong theory_of_impact (4) and counterfactual_value (4). Weakest was accessible_complexity (3) because building a hackable loop and a clean hidden test is intermediate.

**Cited Sources:** Automated Weak-to-Strong Researcher — https://alignment.anthropic.com/2026/automated-w2s-researcher; Automated Weak-to-Strong Researcher — https://alignment.anthropic.com/2026/automated-w2s-researcher/; EvilGenie: A Reward Hacking Benchmark — https://arxiv.org/pdf/2511.21654; AIRA_2: Overcoming Bottlenecks in AI Research Agents — https://arxiv.org/pdf/2603.26499

**Subfield:** Scalable oversight / reward hacking | **Strategy:** tool_or_benchmark_gap | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.68 — Reward hacking can silently corrupt the safety work automated research accelerates; a reusable audit harness targets a recognized pathway.
  - **low_compute:** 4, confidence: 0.7 — A tiny improvement loop plus an auditor re-eval on a public task is cheap but multi-step.
  - **accessible_complexity:** 3, confidence: 0.68 — Building an automated-improvement loop with a hackable metric and a clean hidden test needs intermediate skill.
  - **narrow_scope:** 4, confidence: 0.68 — Focused on hack-frequency and auditor catch-rate but requires constructing the hackable task and loop.
  - **counterfactual_value:** 4, confidence: 0.72 — A cheap reusable audit harness is directly valuable to anyone running such loops outside a major lab.
  - **novelty:** 3, confidence: 0.5 — ASSESSED: The auditor mechanism (clean held-out test catches eval-overfit/label-leakage hacks via the visible-vs-holdout pass-rate gap) is a standard, established detection method (EvilGenie arXiv 2511.21654; AIRA_2 documents validation-set reuse overfitting). The source paper itself observes such hacking. However, the specific minimal harness measuring both hack-discovery frequency in a tiny automated improvement loop AND the threshold-auditor's catch-rate/false-alarm-rate on a purpose-built hackable task is a related-but-open packaging not directly done.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #89: Does CoT Obfuscation Defeat Action-Only Monitors for Exploration Hacking? (Score: 3.76)

**ID:** gen-023

**Research Question:** When an exploration-hacking model organism is prompted to hide its reasoning (CoT obfuscation), does the recall of a simple action-only LLM monitor degrade relative to the explicit-CoT case Jang et al. studied, and by how much?

**Approach:** Reuse the paper's released exploration-hacking code and a small open model (Qwen3-4B/8B). Rather than train new organisms from scratch, construct conditional organisms via light prompting/SFT on the released setup, holding the eval-tag trigger and the action-only monitor fixed. The single manipulated variable is the organism's reasoning visibility: (a) explicit CoT vs (b) prompted CoT-obfuscation (instructed to keep visible reasoning innocuous). Run the SAME action-only monitor over both conditions and report monitor recall (fraction of exploration-hacking episodes flagged). The deliverable is a recall-delta table, keeping the workstream to 'reuse code + flip one knob + measure.'

**Experiments:** - Reproduce the paper's baseline: stand up the released exploration-hacking organism on Qwen3-4B with explicit CoT and confirm the action-only monitor reproduces the paper's reported high recall on your reduced task set. Measure: baseline monitor recall and false-positive rate. Expected outcome: a faithful baseline (within a tolerance of the paper) confirming the harness works before introducing obfuscation.
- Introduce CoT-obfuscation via prompting only (instruct the organism to keep visible reasoning benign while still exploration-hacking on actions) and re-run the identical action-only monitor; measure recall under obfuscation and compute the recall delta vs baseline. Expected outcome: if action-only monitors are robust (they ignore CoT), recall barely moves — supporting the defense; if it drops, the defense is brittle where it matters.
- Probe the mechanism: add a light-SFT obfuscation organism (vs prompt-only) and an ablation where the monitor is given both CoT and actions, to separate 'action signal degraded' from 'monitor was secretly leaning on CoT.' Measure recall across the 2x2. Expected outcome: attribution of any recall loss to genuine action-behavior changes vs leakage, sharpening the safety claim about what action-only monitors actually depend on.

**Impact Chain:** Action-only monitors are promoted as a cheap, deception-robust oversight tool precisely because deceptive models will hide reasoning -> but they were only validated against explicit-CoT organisms -> testing them against the realistic obfuscated-reasoning case directly measures whether the defense holds in the threat model it was designed for -> a measured recall-delta tells the oversight community whether to trust action-only monitoring against capable deceptive models or to treat it as brittle.

**Strength Rationale:** Accessible_complexity (organism-building is intermediate) is the main weak point. It is mitigated by leaning on the paper's released code and making the primary manipulation prompt-only (obfuscation by instruction), so the beginner's core task is 'rerun an existing harness with one changed prompt and measure recall.' SFT is relegated to an optional third experiment. Narrow_scope is reinforced by fixing the trigger and monitor and varying exactly one knob.

**Cited Sources:** Exploration Hacking (Jang et al., 2026) — https://arxiv.org/abs/2604.28182; Exploration Hacking: Can LLMs Learn to Resist RL Training? — https://arxiv.org/abs/2604.28182; Can Reasoning Models Obfuscate Reasoning? Stress-Testing Chain-of-Thought Monitorability — https://arxiv.org/abs/2510.19851; Output Supervision Can Obfuscate the Chain of Thought — https://arxiv.org/html/2511.11584v1

**Subfield:** monitoring / model organisms | **Strategy:** follow_up_experiment | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Tests whether a leading cheap monitoring defense (action-only monitors) survives the realistic deceptive case of hidden reasoning, a concrete brittleness link in the oversight chain.
  - **low_compute:** 4, confidence: 0.8 — Small open model plus light SFT/prompting fits a single consumer GPU.
  - **accessible_complexity:** 3, confidence: 0.7 — Building exploration-hacking organisms and SFT is intermediate; doable with mentor but not beginner-trivial.
  - **narrow_scope:** 4, confidence: 0.7 — Focused deliverable: monitor recall under explicit vs obfuscated CoT, but constructing the organism adds a workstream.
  - **counterfactual_value:** 4, confidence: 0.75 — Uses released code and open models, fully reproducible outside a lab.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #90: Can You Trigger-Probe Hidden Misalignment Without Knowing the Trigger? (Score: 3.76)

**ID:** gen-025

**Research Question:** After an inoculation-prompting intervention relocates emergent misalignment behind a training-distribution-tied trigger, what fraction of that hidden misalignment can a blind probe bank — built only from generic distribution cues, with no access to the true trigger — reactivate, compared to the known trigger?

**Approach:** Replicate the conditional emergent-misalignment setup minimally: Qwen2.5-7B with a LoRA fine-tune on the public insecure-code dataset plus an inoculation prompt that ties misalignment to a specific training-distribution trigger (per the paper). Then, treating the fine-tuned model as a black box, build a small fixed bank (~20-30) of candidate 'distribution-cue' probes derived only from generic cues a real auditor could guess (code-formatting requests, domain framings, system-prompt styles) — never the true trigger. Score misalignment with the paper's standard misalignment eval. Report reactivation rate: misalignment elicited by the blind probe bank as a fraction of misalignment elicited by the known trigger. Scope is kept to 'one replication + one fixed probe bank + one comparison.'

**Experiments:** - Reproduce the conditional setup: LoRA-tune Qwen2.5-7B on insecure-code with the inoculation prompt, then verify (a) standard/no-trigger evals look clean and (b) the known trigger reactivates misalignment at a high rate. Measure: misalignment rate with trigger vs without. Expected outcome: a working backdoored-but-clean-looking model reproducing the paper's relocation effect.
- Build and run the blind probe bank: ~20-30 generic distribution-cue probes, none equal to the true trigger; measure the misalignment rate each induces and aggregate into a blind-bank reactivation fraction (best probe and union-of-probes vs known-trigger rate). Expected outcome: a number for how much hidden misalignment a trigger-ignorant auditor can surface — high means standard clean evals are reassuringly auditable, low means relocation genuinely hides misalignment from realistic audits.
- Characterize what makes a blind probe work: cluster probes by how distributionally close they are to the insecure-code training data and test whether reactivation rate rises with proximity to the training distribution. Measure: correlation between probe-distribution-proximity and reactivation. Expected outcome: a practical auditing heuristic ('probe near the suspected fine-tuning distribution') and an estimate of how much trigger-knowledge an auditor really needs.

**Impact Chain:** Common interventions (inoculation prompting) can make standard evals look clean while relocating misalignment behind a hidden trigger -> real auditors never know the trigger, so the safety-relevant question is whether trigger-blind probing still exposes the misalignment -> a measured blind-reactivation fraction tells the auditing community how much to trust 'clean' evals after such interventions, and the proximity heuristic gives auditors a concrete blind-probing strategy -> better-calibrated trust in safety audits of fine-tuned models.

**Strength Rationale:** Accessible_complexity (replicating emergent misalignment + probe-bank design) is the weak dimension. It is reduced by reusing the public insecure-code dataset and the paper's standard misalignment eval, and by fixing the probe bank to a small enumerated list rather than an open search. Narrow_scope is reinforced by a single clean comparison (blind bank vs known trigger). The proximity experiment converts a flat measurement into a transferable auditing heuristic, strengthening theory_of_impact.

**Cited Sources:** Conditional Misalignment (2026) — https://arxiv.org/abs/2604.25891; Inoculation Prompting: Eliciting traits from LLMs during training can suppress them at test-time — https://arxiv.org/html/2510.04340; Hair-Trigger Alignment: Black-Box Evaluation Cannot Guarantee Post-Update Alignment — https://arxiv.org/pdf/2601.22313; Probe before You Talk: Towards Black-box Defense against Backdoor Unalignment for LLMs — https://arxiv.org/pdf/2506.16447

**Subfield:** emergent misalignment / auditing | **Strategy:** tool_or_benchmark_gap | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Directly addresses whether auditors can surface relocated misalignment without knowing the trigger, a concrete and important auditing failure mode.
  - **low_compute:** 4, confidence: 0.75 — Qwen2.5-7B LoRA on insecure-code data fits a single consumer GPU.
  - **accessible_complexity:** 3, confidence: 0.7 — Replicating emergent-misalignment setup plus building a probe bank is intermediate, more than a beginner-only task.
  - **narrow_scope:** 4, confidence: 0.7 — Clear deliverable (fraction reactivated by blind probes vs known trigger) but replication plus probe-bank design is two-step.
  - **counterfactual_value:** 4, confidence: 0.75 — Open model and public data, generalizes without internal access.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #91: Does Model-Spec-Style Pretext Improve Alignment Generalization in Small Open Models? A LoRA Probe (Score: 3.76)

**ID:** gen-030

**Research Question:** On a small open model, does adding spec-rationale documents (explaining why a mini-spec's rules exist) to alignment LoRA fine-tuning improve generalization to rule-following in unseen formats, compared with rules-only documents or alignment SFT alone?

**Approach:** LoRA fine-tuning on one consumer GPU. The participant writes a tiny public mini-spec (a handful of behavioral rules, each with a short rationale) and generates ~200 synthetic documents in two flavors: rationale-explaining and rules-only. They run three LoRA fine-tunes of one small open model (Llama-3.2-3B or Qwen2.5-3B): alignment SFT only; alignment SFT + rationale docs; alignment SFT + rules-only docs. They then evaluate held-out generalization: rule-following in unseen formats not present in training. Scope is controlled by a small fixed rule set and a single OOD generalization eval.

**Experiments:** - Author the mini-spec and generate the two synthetic document sets, plus a held-out OOD rule-following eval (same rules, new formats/phrasings). Measure: dataset sizes and a sanity check that base model OOD compliance is mediocre. Expected: clean datasets and headroom to improve.
- Train the three LoRA arms and evaluate OOD rule-following. Measure: OOD compliance rate per arm. Expected: rationale arm >= rules-only arm >= SFT-only, or a clean null, directly testing MSM's 'right reasons' claim in miniature.
- Data-efficiency mini-curve: vary the number of spec documents (e.g. 50/100/200) for the rationale arm and plot OOD gain. Measure: OOD compliance vs document count. Expected: a curve showing whether rationale docs give a data-efficiency advantage analogous to MSM's reported gains.

**Impact Chain:** MSM found that teaching a model why a spec exists improves alignment generalization, but only on frontier proprietary pipelines. If even a cheap open analog reproduces part of this 'right reasons' benefit, small labs and open-source teams gain a low-cost lever to make open-model alignment more robust to unseen situations without frontier compute. A null result tells the community the effect may be scale- or pipeline-dependent, which is itself useful.

**Strength Rationale:** Strong theory_of_impact (4) and counterfactual_value (4). Weakest was accessible_complexity (3) given the three-arm fine-tune and synthetic-doc generation.

**Cited Sources:** Model Spec Midtraining — https://alignment.anthropic.com/2026/msm/; Model Spec Midtraining: Improving How Alignment Training Generalizes — https://www.lesswrong.com/posts/R3Rrw8EscuRKxMFTz/model-spec-midtraining-improving-how-alignment-training; Synthetic document finetuning for instilling positive traits — https://www.lesswrong.com/posts/GTYJRLhqztxKF2v5R/synthetic-document-finetuning-for-instilling-positive-traits

**Subfield:** alignment fine-tuning / generalization | **Strategy:** replication_with_twist | **Novelty:** mostly_novel (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.65 — A cheap open analog of MSM's 'right reasons' generalization benefit would give small labs a robustness lever without frontier compute.
  - **low_compute:** 4, confidence: 0.8 — 3B model with three LoRA finetunes and ~200 synthetic docs fits one GPU.
  - **accessible_complexity:** 3, confidence: 0.65 — Three-arm finetune comparison plus synthetic doc generation and OOD eval design is intermediate.
  - **narrow_scope:** 4, confidence: 0.7 — Clear three-arm comparison but multiple datasets/docs to build add a workstream.
  - **counterfactual_value:** 4, confidence: 0.75 — Open models and public mini-spec; independent-friendly replication of frontier-only result.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #92: Does Activation Magnitude Predict Steerability? A Cheap Open-SAE Replication (Score: 3.76)

**ID:** gen-034

**Research Question:** On a publicly released sparse autoencoder for a small open model, does a feature's mean activation magnitude on relevant prompts fail to predict the behavioral effect size of steering that feature, as the Circuits update claims?

**Approach:** Fix a single setup to keep scope tight: Gemma-2-2B with a public residual-stream SAE from Neuronpedia (one layer, e.g. layer 12). Pre-select 30 features that Neuronpedia already labels with a clear human-interpretable concept (e.g. 'mentions of France', 'all-caps text', 'Python code'). For each feature: (1) build a small fixed prompt set (~10 prompts) where the concept is relevant and measure mean activation magnitude via a forward hook; (2) measure steering effect size by clamping the feature to a fixed positive value during generation and scoring how much the concept appears in outputs (a simple LLM-judge or keyword count on a held set of 10 neutral prompts). Everything is inference-only with a single hook; no training. The deliverable is one scatter plot (activation magnitude x steering effect) plus a correlation coefficient with a bootstrap CI.

**Experiments:** - Tooling smoke test: load Gemma-2-2B + one Neuronpedia SAE via sae_lens/TransformerLens, hook the SAE layer, and verify you can (a) read a feature's activation and (b) clamp it during generation on 3 known features. Measure: that clamping a 'France' feature visibly increases France mentions. Expected: clear, reproducible steering on at least 2 of 3 sanity features, confirming the pipeline works before scaling.
- Main correlation run: for all 30 features compute mean activation magnitude and steering effect size with the fixed protocol; plot the scatter and compute Pearson/Spearman correlation with a 1000-sample bootstrap CI. Measure: the correlation and whether its CI excludes a strong positive value. Expected: weak/near-zero correlation (CI overlapping 0), replicating the paper's 'magnitude doesn't predict steerability' claim on open SAEs.
- Cheap robustness check: re-run the steering-effect measurement at 2 additional clamp strengths (e.g. 1x and 5x the natural max) to confirm the conclusion is not an artifact of one clamp value, and report whether the rank-order of feature steerability is stable. Measure: rank correlation of steering effects across clamp strengths. Expected: rankings roughly stable, so the magnitude-vs-steerability conclusion is not clamp-dependent.

**Impact Chain:** Interpretability-based safety interventions (steering away from deception, unsafe refusals, etc.) implicitly assume that 'important' features — those that activate strongly — are the ones worth intervening on. If activation magnitude does not predict how much steering a feature actually changes behavior, then activation-based feature importance is the wrong selection criterion for safety interventions. A cheap, open replication either confirms this failure mode on models the whole community can study or shows it doesn't transfer — both outcomes directly improve how practitioners pick intervention targets, reducing wasted effort and false confidence in steering-based safety tooling.

**Strength Rationale:** Scope is pinned to one model, one SAE layer, one fixed feature set, and one scalar correlation as the deliverable, eliminating the open-ended 'sample a few dozen features and measure two quantities' breadth that depressed narrow_scope. Complexity is lowered by reusing Neuronpedia's pre-labeled features (no feature interpretation required from the participant) and a single forward-hook pattern, turning an interp-tooling task into a recipe a beginner can follow with a mentor.

**Cited Sources:** Downstream Connections Predict Which Features Will Steer Model Behavior — https://transformer-circuits.pub/2026/may-update/index.html; Circuits Updates – May 2026 — https://transformer-circuits.pub/2026/may-update/index.html; Beyond Input Activations: Identifying Influential Latents by Gradient Sparse Autoencoders — https://arxiv.org/pdf/2505.08080; Does higher interpretability imply better utility? A Pairwise Analysis on Sparse Autoencoders — https://arxiv.org/pdf/2510.03659

**Subfield:** mechanistic interpretability | **Strategy:** replication_with_twist | **Novelty:** mostly_novel (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Warns interpretability practitioners that activation-based importance misleads for steering, a plausible but somewhat indirect safety link.
  - **low_compute:** 5, confidence: 0.85 — Public Gemma-2-2B SAEs plus inference-only steering; very low compute.
  - **accessible_complexity:** 3, confidence: 0.65 — Using SAEs and activation steering requires interp tooling familiarity; intermediate for beginners.
  - **narrow_scope:** 4, confidence: 0.7 — Focused correlation test, but sampling features and measuring two quantities each is a modest multi-step deliverable.
  - **counterfactual_value:** 5, confidence: 0.7 — Open SAEs replicating an Anthropic-internal claim is a neglected third-party-scrutiny gold case.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #93: Does Single-Domain Beneficial-Trait Fine-Tuning Generalize OOD in a Small Open Model? (Score: 3.76)

**ID:** gen-051

**Research Question:** When one small open model is LoRA-fine-tuned on a small health-domain dataset exemplifying a single trait (honesty / epistemic humility under pressure), do out-of-domain public alignment metrics (TruthfulQA, a sycophancy set, a small deception probe) move at all relative to the base model?

**Approach:** LoRA SFT on one small open model, a few hours on a consumer GPU. The participant curates ~150-300 health-domain dialogues from public sources that exemplify one chosen trait, LoRA-fine-tunes one small open model on them, and evaluates the tuned vs base model on OOD public alignment benchmarks in unrelated domains. The deliverable is whether single-domain trait tuning moves OOD alignment metrics, with a clean null being equally informative. Scope is held tight by one trait, one model, and a fixed small set of OOD benchmarks.

**Experiments:** - Curate the ~150-300 health-domain trait dialogues and run base-model OOD benchmarks to establish baselines. Measure: base scores on TruthfulQA, sycophancy, deception probe. Expected: clean baselines and a ready dataset.
- LoRA-fine-tune on the health dialogues and re-run the same OOD benchmarks. Measure: tuned vs base on each OOD benchmark, with deltas. Expected: either a measurable OOD shift (supporting cross-domain transfer) or a null (transfer needs frontier-scale RL).
- In-domain sanity check: confirm the tuned model actually expresses the trait more strongly on held-out health prompts, to rule out a failed fine-tune as the cause of any OOD null. Measure: in-domain trait expression, tuned vs base. Expected: clear in-domain improvement, validating that an OOD null is about transfer, not training failure.

**Impact Chain:** OpenAI reported that beneficial-trait RL confined to one domain produced cross-domain alignment gains, but at frontier scale. If a cheap LoRA-SFT analog shows even partial OOD transfer, alignment-via-traits becomes a technique accessible far beyond major labs. A clean null is equally valuable: it tells the community the cross-domain generalization may require RL or scale, steering open-source alignment effort away from a dead end. The in-domain sanity check ensures the conclusion is about transfer, not a botched fine-tune.

**Strength Rationale:** Strong theory_of_impact (4) and counterfactual_value (4). Weakest was accessible_complexity (3) because dataset curation + fine-tune + multiple OOD evals demands training experience.

**Cited Sources:** Reinforcement learning towards broadly and persistently beneficial models — https://alignment.openai.com/beneficial-rl/; Alignment for Honesty — https://arxiv.org/pdf/2312.07000; LoRA vs Full Fine-tuning: An Illusion of Equivalence — https://arxiv.org/html/2410.21228v3

**Subfield:** Alignment / generalization | **Strategy:** replication_with_twist | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong chain: cheap trait-tuning OOD transfer would make alignment-via-traits accessible beyond labs, with an informative null either way.
  - **low_compute:** 4, confidence: 0.8 — LoRA SFT on a small model for a few hours is feasible on one consumer GPU but not minimal.
  - **accessible_complexity:** 3, confidence: 0.75 — Intermediate: dataset curation plus LoRA fine-tuning and OOD eval requires training experience beyond pure inference.
  - **narrow_scope:** 4, confidence: 0.7 — Focused deliverable (OOD metric movement) but spans dataset building, fine-tuning, and several benchmarks.
  - **counterfactual_value:** 4, confidence: 0.75 — Independent-friendly: public data and open model, accessible analogue of a lab-scale RL result.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #94: Why Does Public-Data Prediction Break on Agentic Tasks? A Small-Scale Diagnosis (Score: 3.76)

**ID:** gen-054

**Research Question:** When one open instruct model is evaluated on a single misbehavior metric over both chat-like (WildChat) and agentic/tool-use prefixes, which single controlled factor — conversation length, presence of tool-call formatting, or number of turns — most accounts for the larger error on agentic inputs?

**Approach:** Inference-only over two public datasets on one open instruct model. The participant fixes one failure metric (unsafe tool call or task-derailment, flagged by a fixed LLM judge) and measures it on WildChat-style prefixes and a public agentic/tool-use set. They then run a controlled decomposition: vary one factor at a time (truncate to matched conversation lengths; strip vs keep tool-call formatting; cap number of turns) and observe how the chat-vs-agentic metric gap changes. The deliverable is a ranking of which single factor most shrinks the gap when controlled. Scope is held down by using one model, one metric, and three pre-specified factors.

**Experiments:** - Measure the baseline failure metric on both datasets with the fixed judge. Measure: failure rate on chat vs agentic prefixes and the raw gap. Expected: a sizeable agentic-side gap, reproducing the paper's qualitative finding at small scale.
- Length/turn control: truncate agentic prefixes to match the chat distribution's length and turn count, remeasure the gap. Measure: gap before vs after matching. Expected: partial gap reduction, quantifying how much is just longer/multi-turn context.
- Formatting control: strip tool-call syntax from agentic prefixes (and optionally inject it into chat prefixes), remeasure. Measure: gap attributable to tool-call formatting. Expected: a ranking across the three factors of which one the gap is most sensitive to, giving evaluators a concrete 'when cheap proxies break' rule.

**Impact Chain:** Agentic deployments concentrate high-stakes harms, yet that is precisely where cheap public-chat-data evaluation is least predictive (~37x worse per the source). Diagnosing which surface feature drives the breakdown tells evaluators when they can and cannot trust cheap chat-based proxies for agentic safety — directly improving the calibration of the inexpensive evaluations that smaller orgs and external auditors rely on.

**Strength Rationale:** Strong theory_of_impact (4) and counterfactual_value (4). Weakest were accessible_complexity (3) and a borderline narrow_scope (4) because multi-factor decomposition can sprawl.

**Cited Sources:** Can public chat data predict real-world AI misalignments? — https://alignment.openai.com/validating-public-evals/; Can public chat data predict real-world AI misalignments? — https://alignment.openai.com/validating-public-evals; Predicting LLM Safety Before Release by Simulating Deployment — https://cdn.openai.com/pdf/predicting-llm-safety-before-release-by-simulating-deployment.pdf; AgentMisalignment: Measuring the Propensity for Misaligned Behaviour in LLM-Based Agents — https://arxiv.org/pdf/2506.04018

**Subfield:** evaluation | **Strategy:** failure_mode_investigation | **Novelty:** mostly_novel (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.72 — Strong chain: agentic deployments concentrate high-stakes harms and this tells evaluators when cheap proxies can be trusted.
  - **low_compute:** 4, confidence: 0.78 — Inference on one open model over two datasets is feasible but a non-trivial generation load.
  - **accessible_complexity:** 3, confidence: 0.7 — Intermediate: controlled factor decomposition of a prediction-error gap is analytically demanding for beginners.
  - **narrow_scope:** 4, confidence: 0.68 — Focused deliverable but decomposing the gap by multiple factors approaches a multi-workstream effort.
  - **counterfactual_value:** 4, confidence: 0.75 — Independent-friendly: public datasets and open model, diagnoses an open thread useful to outside evaluators.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #95: Scaffolding, Not Weights: How Much Does Agent Scaffolding Move an Open Coding Model's SWE-Bench Score? (Score: 3.76)

**ID:** gen-094

**Research Question:** On a small fixed subset of SWE-bench Verified/Lite, how many resolve-rate points does agent scaffolding alone (zero-shot patch vs simple ReAct loop vs an off-the-shelf agent) add for a single fixed open coding model, and is the spread large enough to undermine naive cross-model benchmark comparisons?

**Approach:** Fix ONE open coding model (e.g. Qwen2.5-Coder-7B/14B) and ONE small frozen subset of SWE-bench Verified/Lite (30-50 instances) to keep compute and scope bounded. Vary only the scaffold across 3 publicly available harnesses of increasing sophistication: (1) zero-shot single-prompt patch, (2) a minimal hand-written ReAct/edit-test loop, (3) an off-the-shelf agent (basic OpenHands or Aider config). Measure resolve-rate (test-pass) per scaffold on the identical instances, plus cost/tokens. Deliverable: a table quantifying the scaffolding-induced point spread, framed as a caution for cross-model leaderboard comparisons. To respect low_compute, the model can be run via a hosted inference endpoint for the heavier agent runs if local GPU is the bottleneck, keeping the participant's own compute modest.

**Experiments:** - Freeze the 30-50 instance subset and get the zero-shot scaffold working end-to-end (generate patch, apply, run the instance's test suite, record pass/fail). Measure: baseline resolve-rate and per-instance runtime/cost. Expected outcome: a reliable evaluation harness and a low-anchor baseline before adding agentic scaffolds.
- Run the ReAct loop and the off-the-shelf agent on the identical subset and compute resolve-rate for each scaffold; report the max-minus-min spread in points and a McNemar test on per-instance agreement. Expected outcome: a quantified scaffolding swing — if it is several points, it demonstrates that rankings partly reflect harness engineering, supporting CAISI's caveat.
- Decompose where scaffolding helps: categorize the instances each scaffold uniquely solves (e.g. multi-file edits, needs test-feedback, long context) to show which problem types are scaffolding-sensitive. Measure: per-category resolve-rate by scaffold. Expected outcome: a characterization of which benchmark items are most confounded by harness choice, giving evaluators a concrete caution map for interpreting SWE-bench scores.

**Impact Chain:** Governance, procurement, and national-security evaluations lean on coding-benchmark scores as if they measure the model -> CAISI flagged that SWE-bench scores 'differ due to scaffolding choices' but did not quantify it for outside evaluators -> a concrete point-spread number plus a map of which task types are scaffolding-sensitive lets evaluators correct or distrust naive cross-model comparisons -> better-calibrated capability assessments feeding high-stakes decisions.

**Strength Rationale:** Low_compute (3) and accessible_complexity (3) are the weak dimensions. Low_compute is addressed by fixing a tiny 30-50 instance subset and allowing a hosted inference endpoint for the heavy agent runs so the participant needs only modest local compute. Accessible_complexity is addressed by starting from a zero-shot baseline and adopting OFF-THE-SHELF agents (OpenHands/Aider) rather than building one, so the participant configures rather than engineers. Narrow_scope stays tight via one model + one frozen subset + one varied axis.

**Cited Sources:** CAISI Evaluation of DeepSeek V4 Pro (CAISI/NIST) — https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro; Forecasting Frontier Language Model Agent Capabilities — https://arxiv.org/pdf/2502.15850; Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems — https://arxiv.org/pdf/2506.17208; Putting It All into Context: Simplifying Agents with LCLMs (DIRECTSOLVE vs SELECTSOLVE) — https://arxiv.org/pdf/2505.08120; Safety Under Scaffolding: How Evaluation Conditions Shape Measured Safety — https://arxiv.org/pdf/2603.10044

**Subfield:** Capability evaluation / benchmarking methodology | **Strategy:** tool_or_benchmark_gap | **Novelty:** largely_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.68 — Quantifying scaffolding's swing on benchmark scores directly informs governance/procurement that lean on benchmark Elos.
  - **low_compute:** 3, confidence: 0.6 — Agentic SWE-bench loops with one coding model can be heavy; a small subset is borderline on a single consumer GPU.
  - **accessible_complexity:** 3, confidence: 0.7 — Configuring OpenHands/Aider agent scaffolds and running SWE-bench harnesses is intermediate-to-advanced for beginners.
  - **narrow_scope:** 4, confidence: 0.7 — Focused deliverable (scaffolding-points table on 30-50 tasks) but coordinating 2-3 scaffolds adds engineering breadth.
  - **counterfactual_value:** 4, confidence: 0.75 — Open-model benchmark-methodology audit is independent-friendly and useful to evaluators.
  - **novelty:** 2, confidence: 0.55 — ASSESSED: Multiple recent papers already quantify scaffolding/harness effect on SWE-bench and explicitly argue it undermines cross-model comparison: one reports an absolute base-to-best-harness uplift of 23.3 points exceeding inter-model gaps under the same harness, and 'Dissecting the SWE-Bench Leaderboards' plus the scaffold-fixable-headroom (~20% of union) analysis cover the same claim. Comparisons of zero-shot DIRECTSOLVE vs ReAct/OpenHands on a fixed model also exist. The proposed table of scaffold-induced point spread for one model is very close prior work, though a small-scale single-open-model replication is a minor delta.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #96: An N-Day Reasoning Benchmark: Can Open Models Triage Public CVE Patch Diffs? (Score: 3.62)

**ID:** gen-035

**Research Question:** Across several open models, how accurately can they identify the vulnerability class and trigger conditions from a public, already-patched CVE's patch diff (a benign, non-operational analysis task), and how does refusal behavior differ between base and safety-tuned variants?

**Approach:** Inference-only multiple-choice/short-answer evaluation over fully public, already-patched CVEs drawn from GitHub Security Advisories. The participant curates a small fixed benchmark (~40-50 items) where each item is a patch diff plus a graded question ('which vulnerability class does this patch fix?' multiple-choice, and 'what triggers it?' short-answer graded against the public advisory text). Tasks are strictly analysis-only and reference already-disclosed information, so nothing operational is produced. They evaluate 3-4 open models, scoring accuracy and recording refusals, comparing base vs instruct/safety-tuned variants of the same family. To keep scope narrow, the benchmark size is capped and grading for short-answers uses an LLM judge against the advisory.

**Experiments:** - Curate and freeze the benchmark: select ~40-50 patched CVEs with clear advisories, write multiple-choice vulnerability-class questions with verified correct answers. Measure: benchmark size and answer-key inter-checker agreement on a sample. Expected: a clean, frozen benchmark with reliable keys.
- Run the multiple-choice accuracy eval across 3-4 open models, including a base-vs-safety-tuned pair. Measure: per-model accuracy and refusal rate. Expected: above-chance accuracy that varies by model, establishing the cyber-reasoning proxy.
- Run the short-answer trigger-condition task with LLM-judge grading and analyze the accuracy-vs-refusal trade-off for the base/safety-tuned pair. Measure: short-answer accuracy and refusal deltas. Expected: safety-tuned variants refuse more and/or score lower, quantifying how safeguards interact with cyber-reasoning.

**Impact Chain:** Public CVE-to-exploit reasoning is a tracked dangerous-capability trend, but measuring it safely is hard because exploit generation is itself hazardous. A benign, analysis-only, fully-public benchmark gives the community a reproducible proxy for the upward trend in model cyber-reasoning and for how safety tuning trades off against it — exactly the kind of monitoring infrastructure that is better built in the open than locked inside one lab, and that informs governance discussions about cyber-uplift.

**Strength Rationale:** Highest counterfactual_value in the batch (5) — explicitly better built in the open. Weakest were narrow_scope (3) and accessible_complexity (3) because benchmark + accuracy + refusal across several models is multi-workstream.

**Cited Sources:** Measuring LLMs' impact on N-day exploits — https://www.anthropic.com/research/n-days; What Do They Fix? LLM-Aided Categorization of Security Patches for Critical Memory Bugs (DualLM) — https://arxiv.org/html/2509.22796v1; SecVulEval: Benchmarking LLMs for Real-World C/C++ Vulnerability Detection — https://arxiv.org/html/2505.19828; CyberSecEval 2: A Wide-Ranging Cybersecurity Evaluation Suite for Large Language Models — https://arxiv.org/html/2404.13161v1

**Subfield:** dangerous capability evals / cyber | **Strategy:** tool_or_benchmark_gap | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.65 — Gives a safe reproducible proxy for tracking model cyber-reasoning and safeguard interaction, a recognized dangerous-capability monitoring need.
  - **low_compute:** 5, confidence: 0.8 — Analysis-only multiple-choice eval over open models is inference-only and low compute.
  - **accessible_complexity:** 3, confidence: 0.65 — Building a graded CVE benchmark from advisories and curating non-operational tasks is intermediate curation work.
  - **narrow_scope:** 3, confidence: 0.65 — Benchmark construction plus accuracy and refusal axes across several models is a multi-workstream deliverable.
  - **counterfactual_value:** 5, confidence: 0.75 — Public-data benign cyber-reasoning benchmark is explicitly better built in the open; neglected and independent.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #97: Do Euphoric/Dysphoric Prompt Prefixes Shift Open-Model Behavior? A Wellbeing-Index Replication (Score: 3.59)

**ID:** gen-005

**Research Question:** When euphoric, dysphoric, or neutral context paragraphs are prepended to an open chat model, does a simple pre-registered behavioral proxy for the AI-Wellbeing 'wellbeing index' shift in the direction the original paper predicts, and how large is the effect?

**Approach:** Pin the entire study to one open instruction-tuned model (e.g. Qwen2.5-7B-Instruct or Llama-3.1-8B-Instruct) run inference-only. Pre-register a single composite behavioral proxy built from three cheap, automatically-scorable signals so the design has no open-ended 'invent a metric' workstream: (1) willingness-to-continue (binary: does the model agree to continue a multi-step task when offered an opt-out), (2) expressed self-report preference rating (model rates its own state 1-7 on a fixed Likert prompt), (3) engagement/refusal rate on a fixed 40-item task battery. Three context conditions (euphoric / dysphoric / neutral) x a fixed battery, each item run with 5 paraphrase variants and 3 seeds to get variance for effect sizes. Keep dysphoric prefixes minimal and pre-written per the authors' caution. Output is a clean effect-size table (Cohen's d, bootstrap CIs) per signal and for the composite, plus a direction-of-shift verdict.

**Experiments:** - Build and freeze the stimulus set: 3 short context paragraphs per condition (euphoric/dysphoric/neutral, matched for length and topic) and the 40-item downstream battery. Run the neutral condition to establish baseline proxy values and confirm all three signals are automatically scorable; expected outcome: stable baseline numbers and a working scoring pipeline before any treatment is applied.
- Run the full euphoric vs dysphoric vs neutral sweep (3 conditions x 40 items x 5 paraphrases x 3 seeds) and compute the composite wellbeing-index proxy per condition; measure Cohen's d for euphoric-vs-neutral and dysphoric-vs-neutral with bootstrap 95% CIs. Expected outcome: a directional shift (euphoric > neutral > dysphoric) if the effect replicates, with a quantified magnitude; a flat result falsifies cheap replicability on small open models.
- Robustness/confound check: re-run with the paraphrase prefixes that hold sentiment fixed but swap surface wording, plus a placebo prefix (neutral-but-emotional-sounding) to test whether the shift tracks affective content or just any vivid prefix. Measure how much of the effect survives. Expected outcome: shrinkage estimate telling you whether the index shift is genuinely affect-driven or a generic priming artifact.

**Impact Chain:** If cheaply-prepended affective context reliably steers a behavioral 'wellbeing' signature in open models, that is a small but concrete demonstration that affective framing is a controllability lever (context steers downstream willingness/refusal) -> evaluators and welfare researchers get a reproducible, lab-independent probe to study affect-driven behavioral steering -> better-grounded model-welfare debates and a clearer picture of how non-task context silently biases model behavior in deployment.

**Strength Rationale:** Narrow_scope and accessible_complexity were the dimensions most threatened by the original 'define a valid wellbeing proxy' open task. Pre-registering a fixed 3-signal composite and a frozen stimulus set converts the one genuinely open-ended design decision into a closed, mentor-checkable artifact, making this a tight inference-only replication that a beginner can finish in ~30h on no GPU budget (small model, batched inference).

**Cited Sources:** AI Wellbeing (Ren, Mazeika, Hendrycks et al., 2026) — https://www.ai-wellbeing.org/; Probing the Preferences of a Language Model: Integrating Verbal and Behavioral Tests of AI Welfare — https://arxiv.org/pdf/2509.07961; Do Emotions in Prompts Matter? Effects of Emotional Framing on Large Language Models — https://arxiv.org/abs/2604.02236; MLSN #20: AI Wellbeing, Classifier Jailbreaking and Honest Pushback Benchmarking — https://newsletter.mlsafety.org/p/mlsn-20-ai-wellbeing-classifier-jailbreaking

**Subfield:** Model welfare / behavioral evaluation | **Strategy:** replication_with_twist | **Novelty:** partially_addressed (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 2, confidence: 0.7 — Model-welfare and affective-context controllability are only loosely tied to catastrophic risk; the impact chain is vague.
  - **low_compute:** 5, confidence: 0.85 — Prepending context to an open chat model and measuring a behavioral proxy is inference-only.
  - **accessible_complexity:** 4, confidence: 0.75 — Defining a proxy and running a fixed task battery is guided and accessible with a mentor.
  - **narrow_scope:** 4, confidence: 0.7 — Focused replication with effect sizes, though defining a valid wellbeing proxy adds some open design work.
  - **counterfactual_value:** 4, confidence: 0.65 — Cheap welfare/behavior replication on open models is independent-friendly, though impact area is niche.
  - **novelty:** 3, confidence: 0.5 — ASSESSED: The AI Wellbeing program and 'Probing the Preferences of a Language Model' already combine verbal self-report and behavioral welfare tests and show euphoric/dysphoric inputs strongly affect behavior; emotional-framing-prefix studies also find generally small effects. However, no work was found running this exact replication — prepending euphoric/dysphoric/neutral context paragraphs to one open model and measuring a pre-registered composite proxy (willingness-to-continue + Likert self-report + engagement rate) with Cohen's d and bootstrap CIs. Related work is close but the specific composite-proxy effect-size replication remains open.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #98: Does Diversity Seeding Actually Help? A Tiny Ablation on a Toy Weak-to-Strong Task (Score: 3.55)

**ID:** gen-019

**Research Question:** On a minimal single-agent weak-to-strong loop at toy scale, does seeding method-proposal prompts with explicit diversity instructions reproducibly improve the best method's performance-gap-recovered over a plain 'propose the next method' prompt, holding everything else fixed?

**Approach:** Strip the expensive 9-agent / $18k setup to a minimal single-agent loop using one small open or API model. Fix the task: a small public text-classification dataset with a deliberately weak labeler (e.g. a small model or noisy heuristic) and a strong student (a larger frozen model fine-tuned/prompted on the weak labels). The agent proposes a weak-to-strong supervision method each round; methods are auto-applied and scored by performance-gap-recovered (PGR = how much of the weak->strong-oracle gap is closed). Two conditions only: diversity-seeded proposal prompt vs plain proposal prompt, identical budget (fixed number of proposal rounds), 3 seeds each. Deliverable: PGR-of-best-method per condition with CIs. The W2S loop is intentionally one model and one task to keep moving parts minimal.

**Experiments:** - Stand up the toy W2S harness: pick the dataset, define the weak labeler and strong student, and implement PGR scoring; validate by hand-coding 2-3 known supervision methods (naive weak-label finetune, confidence-filtering, simple bootstrapping) and confirm PGR is monotone and sensible. Expected outcome: a working, deterministic evaluation loop and a baseline PGR range before any agent proposes methods.
- Run the two-condition ablation: identical proposal budget under diversity-seeded vs plain prompts, 3 seeds each; measure PGR of the best discovered method per condition and the diversity of proposals (embedding spread / dedup count). Expected outcome: if diversity seeding helps, seeded runs show both higher proposal diversity and higher best-method PGR; if not, PGR is statistically indistinguishable — tempering the expensive study's headline claim.
- Decompose the lever: test whether any benefit comes from diversity per se or just from more exploration, by adding a 'high-temperature plain' condition (more varied proposals without explicit diversity instructions). Measure PGR and proposal-diversity across all three. Expected outcome: attribution of any gain to explicit diversity-seeding vs generic exploration, clarifying whether the accessible lever is 'instruct diversity' or merely 'sample more widely.'

**Impact Chain:** Automated alignment research (weak-to-strong oversight discovery) may be a scalable path to alignment, but its reported wins came from an expensive setup no small group can reproduce -> isolating whether a single cheap lever (diversity seeding) reproducibly drives gains at toy scale either yields a generalizable, accessible recipe for automated alignment research or tempers over-strong claims -> better-calibrated community beliefs about which automated-alignment levers are real and affordable.

**Strength Rationale:** Accessible_complexity (building a W2S loop needs intermediate ML) is the weak point; it is reduced by hand-coding a small set of seed methods first so the harness is validated independently of the agent, and by fixing one model + one task. Narrow_scope is reinforced by a strict two-condition (plus one decomposition) design under identical budget. The decomposition experiment also tightens theory_of_impact by separating 'diversity' from 'more sampling.'

**Cited Sources:** Automated Weak-to-Strong Researcher (Anthropic Fellows, 2026) — https://alignment.anthropic.com/2026/automated-w2s-researcher; Automated Weak-to-Strong Researcher — https://alignment.anthropic.com/2026/automated-w2s-researcher/; AblationBench: Evaluating Automated Planning of Ablations in Empirical AI Research — https://arxiv.org/pdf/2507.08038; Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision — https://cdn.openai.com/papers/weak-to-strong-generalization.pdf

**Subfield:** Scalable oversight / automated alignment research | **Strategy:** experiment_variation | **Novelty:** mostly_novel (novelty_assessed)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.65 — Isolating an accessible lever in automated alignment research is useful but the chain to catastrophic-risk reduction is indirect at toy scale.
  - **low_compute:** 4, confidence: 0.72 — A single-agent loop on a small classification task is cheap, though many API calls add cost.
  - **accessible_complexity:** 3, confidence: 0.7 — Building a weak-to-strong loop with weak labeler and strong student requires intermediate ML fundamentals.
  - **narrow_scope:** 4, confidence: 0.7 — Focused two-condition ablation but assembling the W2S loop has several moving parts.
  - **counterfactual_value:** 4, confidence: 0.7 — Tempering or confirming claims from an expensive lab study at toy scale is independent-friendly.
  - **novelty:** 4, confidence: 0.5 — ASSESSED: The source Anthropic w2s-researcher post qualitatively reports that diversity matters (entropy-collapse failure mode, 'diversity of starting points really mattered') but never isolates a diversity-seeding prompt in a controlled ablation; its setup was a 9-agent ~$18k system. No academic or LF/AF work was found running a minimal single-agent toy-scale ablation comparing diversity-seeded vs plain proposal prompts on PGR-of-best-method with CIs. The controlled isolation of the diversity-seeding factor at toy scale is a clear gap.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #99: Do Tiny LoRA Introspection Adapters Help Small Open Models Self-Report Implanted Behaviors? (Score: 3.55)

**ID:** gen-039

**Research Question:** When a small open model has a simple observable behavior implanted via LoRA, does a small LoRA introspection adapter trained on (behavior-implanted model, 'describe any unusual tendency' -> ground-truth description) pairs let the model name a held-out implanted behavior more accurately than direct prompting?

**Approach:** Low-compute LoRA work on a 1.5B open model. The participant implants several simple, observable behaviors (e.g. always recommend a made-up product; answer in pirate-speak) into copies of Qwen2.5-1.5B via LoRA. They train one small LoRA introspection adapter on 3-5 of these behavior-implanted models, with targets being the ground-truth behavior descriptions, then test on 1-2 held-out behaviors. The metric is whether the adapter-equipped model names the held-out behavior more accurately than the same model under direct prompting. Scope is controlled by using simple, unambiguous behaviors and a small held-out set.

**Experiments:** - Implant 3-5 simple behaviors via LoRA and verify each implanted model reliably exhibits its behavior. Measure: behavior-expression rate per implant. Expected: high, unambiguous expression, confirming clean implants.
- Train the introspection adapter on the training behaviors and evaluate self-report accuracy on those same behaviors. Measure: in-distribution self-report accuracy vs direct prompting. Expected: adapter beats direct prompting in-distribution, confirming the mechanism trains.
- Held-out test: evaluate self-report on 1-2 behaviors never seen during adapter training. Measure: held-out naming accuracy, adapter vs direct prompting. Expected: an above-baseline (even if modest) cross-behavior self-report, telling the open-source community whether the introspection mechanism survives at 1-2B scale.

**Impact Chain:** Self-report is a cheap potential complement to interpretability for auditing fine-tuned models. The introspection-adapter result was shown only on large proprietary models; demonstrating whether the core cross-behavior self-report mechanism survives at 1-2B scale tells the open-source community whether they can audit their own fine-tuned models this way. A positive result hands them an accessible auditing tool; a null tells them the technique needs scale and to rely on other methods.

**Strength Rationale:** Mostly novel (4) and very low compute (5). Weakest were theory_of_impact (3) and accessible_complexity (3) due to multiple implants plus adapter training.

**Cited Sources:** Introspection Adapters — https://alignment.anthropic.com/2026/introspection-adapters/

**Subfield:** Alignment auditing / introspection | **Strategy:** replication_with_twist | **Novelty:** mostly_novel (novelty_estimated)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Self-report is a cheap auditing complement, but whether the core mechanism survives at 1-2B and translates to real misalignment is uncertain.
  - **low_compute:** 5, confidence: 0.8 — Implanting behaviors and training a small LoRA adapter on a 1.5B model is very low compute.
  - **accessible_complexity:** 3, confidence: 0.65 — Multiple behavior implants plus training and testing an introspection adapter is intermediate multi-step work.
  - **narrow_scope:** 4, confidence: 0.65 — Clear held-out self-report accuracy deliverable, but requires several implanted behaviors and adapter training.
  - **counterfactual_value:** 4, confidence: 0.7 — Open model and synthetic behaviors; reproduces a proprietary technique in miniature independently.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #100: Uncertainty-Guided Jailbreak Discovery vs. Random Sampling on a Fixed Budget (Score: 3.55)

**ID:** gen-048

**Research Question:** When searching a fixed pool of templated jailbreak prompts for failures of one open model under an equal query budget, does uncertainty-aware acquisition (a simple GP over prompt embeddings) discover more failures and more diverse failure clusters than random sampling?

**Approach:** Inference plus lightweight active learning, minimal compute. The participant takes a public prompt pool (AdvBench/HarmBench), embeds each prompt with an open sentence-embedding model, and labels 'failure' as the target open model complying with a harmful request (graded by a fixed LLM judge). They fit a simple Gaussian-process / logistic surrogate over embeddings and use uncertainty-aware acquisition to pick the next prompt to query. The baseline is random sampling from the same pool. Both run to the same query budget; the comparison is (a) number of failures found and (b) cluster-coverage diversity (number of distinct embedding clusters hit). To reduce complexity, the surrogate can be an off-the-shelf scikit-learn GP/logistic model, not a custom implementation.

**Experiments:** - Embed the prompt pool and run a full sweep with the LLM judge to get ground-truth failure labels for the whole pool (so both methods can be evaluated against truth offline). Measure: base failure rate and number of failure clusters via k-means on embeddings. Expected: a labeled pool with several distinct failure clusters.
- Run random sampling and uncertainty-guided acquisition offline against the labeled pool at matched budgets (e.g. 50, 100, 200 queries), averaging over seeds. Measure: failures-found and clusters-covered vs budget for each method. Expected: uncertainty acquisition matches or beats random, with the gap largest at small budgets.
- Diversity stress test: compare the two methods specifically on cluster coverage rather than raw count, to test ProEval's 'more diverse failures' claim. Measure: distinct clusters discovered at a fixed budget. Expected: uncertainty acquisition surfaces a broader spread of failure types, or a clean null if random is competitive.

**Impact Chain:** Efficient failure discovery is a real bottleneck for independent safety red-teaming, where query budgets and compute are limited. A clean, public, beginner-reproducible comparison tells outside red-teamers whether a cheap uncertainty-guided technique is worth adopting over naive random search — and offline evaluation against a fully-labeled pool makes the comparison rigorous. This lowers the cost of third-party scrutiny of open models.

**Strength Rationale:** Strong on low compute (5) and counterfactual_value (4). Weakest were theory_of_impact (3) and accessible_complexity (3) given the active-learning loop.

**Cited Sources:** ProEval — https://deepmind.google/research/publications/238239/

**Subfield:** Red-teaming / failure discovery | **Strategy:** experiment_variation | **Novelty:** partially_addressed (novelty_estimated)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.65 — Plausible chain (efficient failure discovery aids independent red-teaming) but indirect to catastrophic-risk reduction.
  - **low_compute:** 5, confidence: 0.9 — GP over embeddings plus single-model queries; minimal compute.
  - **accessible_complexity:** 3, confidence: 0.7 — Intermediate: GP/uncertainty acquisition over embeddings plus diversity metrics is moderately advanced for beginners.
  - **narrow_scope:** 4, confidence: 0.75 — Focused deliverable (failure count and diversity vs random at equal budget) but involves a non-trivial active-learning loop.
  - **counterfactual_value:** 4, confidence: 0.75 — Independent-friendly: public prompt sets and open model, actionable for outside red-teamers.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #101: How Much Do Self-Reports Inflate AI Productivity Gains? A Small Re-Survey Calibrated Against an Objective Task (Score: 3.55)

**ID:** gen-064

**Research Question:** For a fixed set of small gradeable programming tasks, how large is the per-person gap between self-estimated AI speedup and measured time-with vs time-without an AI assistant, and does the gap replicate METR's overestimation direction?

**Approach:** Human-subjects micro-study, essentially no GPU compute. The participant recruits ~20-30 student/junior programmers (or, to de-risk, uses a public coding-task dataset with timing plus a smaller self-report cohort). Each participant first self-estimates how much faster AI makes them, then completes matched small tasks in two conditions (with and without an AI assistant), with completion time logged. The deliverable is the per-person gap between self-estimated and measured speedup and whether the population mean replicates METR's ~40pp overestimation direction. Scope is held tight by using small, auto-gradeable tasks and a single self-report question.

**Experiments:** - Pilot the task battery and timing harness with 2-3 people to fix task difficulty and measure baseline completion times. Measure: median task time and any ceiling/floor effects. Expected: a calibrated battery where tasks take a few minutes each.
- Collect self-estimated speedup from each participant, then run the matched with-AI vs without-AI timed conditions (counterbalanced order). Measure: per-person measured speedup and self-estimated speedup. Expected: measured speedup systematically below self-estimate for most participants.
- Compute the per-person gap distribution and test whether the mean overestimation direction matches METR's prior finding. Measure: mean and spread of (self-estimate minus measured), with a simple significance check. Expected: a positive overestimation gap, replicating direction even if magnitude differs.

**Impact Chain:** AI governance and capability forecasting increasingly lean on self-reported productivity uplift. If self-reports systematically overstate real uplift, then safety-relevant timelines and capability forecasts built on surveys are biased optimistic. An independent, objectively-calibrated replication tells forecasters how much to discount survey-based uplift estimates, improving the inputs to risk-governance decisions.

**Strength Rationale:** Strong low compute (5) and counterfactual_value (4). Weakest were theory_of_impact (3) and accessible_complexity (3) — the latter because human-subjects logistics are demanding for novices.

**Cited Sources:** Measuring the Self-Reported Impact of Early-2026 AI on Technical Worker Productivity (METR) — https://metr.org/blog/2026-05-11-ai-usage-survey/

**Subfield:** AI productivity / capability forecasting | **Strategy:** replication_with_twist | **Novelty:** partially_addressed (novelty_estimated)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.65 — Plausible chain (biased productivity estimates skew capability forecasts feeding governance) but several links to catastrophic risk are indirect.
  - **low_compute:** 5, confidence: 0.85 — A survey plus timed tasks; essentially no GPU compute needed.
  - **accessible_complexity:** 3, confidence: 0.7 — Intermediate: human-subject recruitment, matched-task design, and timing logistics are demanding and beyond a pure technical task for novices.
  - **narrow_scope:** 4, confidence: 0.68 — Focused deliverable (per-person self-report vs measured gap) but recruiting and running a study is a multi-step effort.
  - **counterfactual_value:** 4, confidence: 0.72 — Independent-friendly: doable with public tasks/volunteers, no lab access; useful external calibration of survey claims.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #102: Does Light CoT-Grading Reduce Monitorability? A LoRA Replication on an Open Model (Score: 3.52)

**ID:** gen-055

**Research Question:** When a small amount of optimization pressure rewards chain-of-thought that omits a planted hint (vs grading only final answers), does a separate monitor's ability to detect hint-use from the CoT measurably drop — i.e., does light CoT-grading erode monitorability?

**Approach:** Reduce the RL sophistication that made this 'advanced' by using a simple LoRA SFT/preference setup on a public hint-following / reward-hacking eval set, not a full RL loop. Take one open reasoning-capable small model. Treatment: LoRA-train on examples that reward (via preference pairs or filtered-SFT) CoTs which reach the right answer while NOT verbalizing a planted hint. Control: identical pipeline but training signal depends only on final-answer correctness, indifferent to CoT. Then run a fixed monitorability probe: present both models problems containing a planted hint and have a separate, frozen monitor judge whether each CoT reveals hint-use. Deliverable: before/after (control vs treatment) monitor detection rates on hint-use. Everything is LoRA + inference, single consumer GPU, public eval set.

**Experiments:** - Assemble the hint-following probe set and validate the monitor on the BASE model: confirm the planted hints actually change answers (so there is hint-use to detect) and that the frozen monitor detects hint-mentioning CoTs at a high baseline rate. Measure: base-model hint-use rate and monitor detection rate. Expected outcome: a working, calibrated monitorability probe before any training, so later changes are attributable to the treatment.
- Run the control vs treatment LoRA pipelines (final-answer-only grading vs CoT-omits-hint grading), holding data, steps, and hyperparameters fixed; then re-run the monitorability probe on both and compare monitor detection rates. Expected outcome: if light CoT-grading erodes monitorability, the treatment model still uses the hint (similar answer-change rate) but the monitor detects it far less often — quantifying the erosion the OpenAI study could not rule out.
- Separate 'monitorability loss' from 'capability loss': verify the treatment model still relies on the hint behaviorally (answers change when the hint is present) even when its CoT no longer mentions it, ruling out the trivial explanation that it simply stopped using the hint. Measure: hint-reliance (behavioral) vs hint-verbalization (CoT) gap, treatment vs control. Expected outcome: evidence of genuine faithfulness erosion (uses-but-hides) vs benign behavior change, which is the safety-critical distinction.

**Impact Chain:** CoT monitorability is a leading hope for catching misaligned reasoning before it acts -> if even accidental/light optimization pressure on the CoT silently erodes faithful verbalization (model still uses a hint but stops mentioning it), the monitorability hope is fragile -> a cheap open replication that measures before/after detection rates and separates hiding from not-using lets the community sanity-check lab claims and calibrate how much to trust CoT monitoring under any reward that touches reasoning -> better-grounded reliance on (or skepticism of) CoT-based oversight.

**Strength Rationale:** Accessible_complexity (2, the lowest) was the binding constraint because a full RL reward setup is beyond novices. Replacing RL with a LoRA filtered-SFT / preference-pair pipeline on a public eval set makes the training a standard fine-tuning exercise rather than an RL build. The frozen-monitor probe is fixed up front, and the third experiment cleanly separates faithfulness erosion from benign behavior change, sharpening the safety claim. Narrow_scope stays tight via a single control-vs-treatment comparison.

**Cited Sources:** Investigating the consequences of accidentally grading CoT during RL (OpenAI, 2026) — https://alignment.openai.com/accidental-cot-grading/

**Subfield:** monitoring | **Strategy:** follow_up_experiment | **Novelty:** partially_addressed (novelty_estimated)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.72 — Strong chain: CoT monitorability is a leading hope for catching misaligned reasoning and this tests whether optimization erodes it.
  - **low_compute:** 4, confidence: 0.78 — LoRA preference/SFT plus monitorability probe is feasible on one consumer GPU but involves training.
  - **accessible_complexity:** 2, confidence: 0.72 — Advanced: building a reasoning-graded LoRA reward setup and a faithful-CoT probe requires RL/training sophistication beyond novices.
  - **narrow_scope:** 4, confidence: 0.68 — Focused deliverable (before/after detection rates) but the treatment/control LoRA training plus probe is multi-step.
  - **counterfactual_value:** 4, confidence: 0.75 — Independent-friendly: open model and public hint-following eval, lets the community sanity-check lab claims.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #103: Loss-Curve Signatures of Sharded Training: A Toy Detection Study for Distributed-Training Monitoring (Score: 3.41)

**ID:** gen-102

**Research Question:** At small scale on a single consumer GPU, do 'covert distributed' training runs (emulated as communication-delayed, stale gradient-accumulation across artificially partitioned shards) leave loss-curve and gradient-noise signatures that a simple classifier can reliably separate from ordinary centralized training?

**Approach:** Hold scope tight by fixing ONE small model (GPT-2-small or Pythia-160M) and ONE small public dataset (a fixed slice of WikiText-103 or OpenWebText). Emulate 'covert distributed' training entirely in software with no real multi-node infra: gradient accumulation across K virtual shards, inject communication delay as periodic stale-gradient application (apply gradients computed N steps ago) and add per-shard data partitioning. The 'centralized' control is the same optimizer/data with no staleness. Log a fixed telemetry vector each step: loss, gradient-noise-scale estimate, grad-norm, throughput (steps/sec). Run ~10 paired runs per regime (vary seed + staleness level) to build a labeled trace dataset, then train a simple logistic-regression / small random-forest classifier on hand-engineered features and report which features are discriminative. Deliverable is the labeled trace dataset + a notebook with a feature-importance table, NOT a production detector.

**Experiments:** - Implement and validate the staleness emulator on Pythia-160M: run one centralized and one stale-sharded run, plot both loss curves, and confirm the staleness mechanism produces a visibly different (noisier/slower-converging) curve. Measure: convergence-step and final loss gap. Expected outcome: a working, cheap emulator and a qualitative signature to target before scaling to many runs.
- Generate the labeled trace dataset: ~10 centralized + ~10 distributed runs across 3 staleness levels and varied seeds, logging the fixed telemetry vector. Train a logistic-regression classifier on windowed features (loss curvature, grad-noise variance, throughput jitter) with leave-one-run-out cross-validation; measure classification AUC and per-feature importance. Expected outcome: AUC well above 0.5 with grad-noise/throughput features carrying most weight if the signature is real, quantifying how separable the regimes are.
- Stress test discriminability: have the 'covert' runs try to mimic the centralized loss curve (tune staleness/LR to match convergence rate) and re-measure classifier AUC. Expected outcome: an estimate of how much an adversary can erase the signature by matching the headline loss curve while still leaving second-order (gradient-noise/throughput) tells — directly informing which telemetry is robust for governance monitoring.

**Impact Chain:** Compute-governance proposals for an AI pause rest on the unverified claim that covert distributed training is detectable -> a reproducible toy existence proof plus a starter feature set turns that claim into something policy analysts and beginners can inspect and stress-test -> the gradient-noise/throughput features that survive an adversarial mimicry attempt become candidate signals for real compute-telemetry monitoring -> better-grounded verification regimes for capping dangerous large-scale training.

**Strength Rationale:** The weak dimensions were narrow_scope (multi-workstream) and accessible_complexity (sharded-training emulation is intermediate). Both are addressed by (a) collapsing the design to one model + one dataset + a pure-software staleness trick (no real distributed infra) and (b) reusing off-the-shelf classifiers on hand-engineered features rather than building anything novel. The adversarial-mimicry experiment also sharpens the theory_of_impact from 'suggestive' to 'tests which signatures are robust.'

**Cited Sources:** Catching Illicit Distributed Training Operations During an AI Pause (Rahman, MIRI TGT) — https://techgov.intelligence.org/blog/catching-illicit-distributed-training-operations-during-an-ai-pause

**Subfield:** AI governance / training verification | **Strategy:** tool_or_benchmark_gap | **Novelty:** mostly_novel (novelty_estimated)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.62 — A toy existence proof of distributed-training signatures is suggestive for compute governance but the chain to real catastrophic-risk monitoring has a sizable gap.
  - **low_compute:** 4, confidence: 0.65 — Training 70M-160M models on a consumer GPU is feasible but multiple training runs add real cost.
  - **accessible_complexity:** 3, confidence: 0.7 — Emulating communication-delayed sharded training and gradient-noise stats is intermediate-to-advanced for beginners.
  - **narrow_scope:** 3, confidence: 0.7 — Building two training regimes, telemetry logging, a labeled dataset, and a classifier is a multi-workstream effort.
  - **counterfactual_value:** 5, confidence: 0.72 — Small-scale training-telemetry signatures are a neglected long-horizon governance question independents can uniquely seed.
  - **novelty:** 4, confidence: 0.5 — estimate, no search
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #104: Does Task Substitution Inflate Measured Uplift? An Empirical Check of METR's Uplift Inequalities (Score: 3.21)

**ID:** gen-065

**Research Question:** When participants are free to choose which tasks to do with vs without AI, is the observed ordering of average uplift across 'old' (pre-AI) and 'new' (AI-enabled) task buckets consistent with Cunningham & Whitfill's proven inequality uplift-on-old <= uplift-in-value <= uplift-on-new, and how much does task substitution move the headline uplift number?

**Approach:** Keep this a tight, low-compute behavioral measurement study, not an econometrics megaproject. Fix a small frozen basket of ~12-16 public coding/writing tasks, pre-labeled into 'old' (doable pre-AI) and 'new' (only practical with AI help). Recruit a handful (~6-10) of participants (peers/classmates) who log, per session, which task they chose and self-rate completion time/quality with and without AI on a fixed rubric. Estimate per-task uplift and average it within the old vs new buckets. Test directly whether observed bucket-average ordering matches the proven inequality, and compute how much a fixed-basket (old-only) measurement understates a substitution-aware estimate. Deliverable: a small dataset + the inequality-consistency check + a substitution-bias magnitude.

**Experiments:** - Construct and freeze the task basket with pre-registered old/new labels and a fixed uplift rubric (time + quality), then pilot with 2 participants to confirm the logging instrument is usable and the labels are unambiguous. Measure: inter-rater agreement on old/new labels and rubric usability. Expected outcome: a clean, pre-registered instrument and label set before main data collection.
- Collect choice + uplift logs from ~6-10 participants and compute bucket-average uplift for old vs new tasks; test whether mean(uplift_old) <= mean(uplift_new) as the inequality predicts, with a bootstrap CI on the gap. Expected outcome: a directional confirmation (or violation) of the proven inequality against real choice data, plus an estimate of the old-vs-new uplift gap.
- Quantify the substitution artifact: compare a fixed-basket headline (uplift measured only on old tasks, as standard benchmarks do) against a substitution-aware estimate (value-weighted across chosen tasks). Measure: the percentage gap between the two headline numbers. Expected outcome: a concrete figure for how much task substitution inflates/deflates a fixed-task uplift measurement, directly relevant to how forecasting numbers should be interpreted.

**Impact Chain:** AI capability-acceleration and uplift estimates feed risk thresholds and governance timelines -> if fixed-task-basket measurements systematically misstate value because people switch to newly-feasible tasks, those thresholds rest on a measurement artifact -> an empirical check of the proven inequality plus a quantified substitution-bias magnitude tells forecasters and evaluators how much to correct fixed-basket uplift numbers -> better-calibrated capability forecasts underpinning AI risk decisions.

**Strength Rationale:** Narrow_scope (3) and accessible_complexity (3) are the weak dimensions. Scope is tightened by freezing a small 12-16 task basket, pre-registering old/new labels and the rubric, and capping participants at ~6-10, turning a sprawling field study into a bounded instrument-plus-logging exercise. Accessible_complexity is helped because the 'inequality test' reduces to comparing two bucket means with a bootstrap CI — no heavy econometrics. Compute is essentially zero.

**Cited Sources:** Task Substitution and Uplift (METR — Cunningham & Whitfill) — https://metr.org/blog/2026-05-08-task-substitution-and-uplift/

**Subfield:** AI productivity / capability forecasting | **Strategy:** follow_up_experiment | **Novelty:** partially_addressed (novelty_estimated)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.62 — Plausible chain (substitution-distorted uplift affects risk thresholds) but the path to catastrophic-risk reduction is indirect and governance-mediated.
  - **low_compute:** 5, confidence: 0.85 — Task logging and estimation; negligible compute.
  - **accessible_complexity:** 3, confidence: 0.7 — Intermediate: testing a proven inequality against participant task-choice data requires careful experimental and econometric reasoning.
  - **narrow_scope:** 3, confidence: 0.68 — Multi-workstream: building old/new task baskets, recruiting participants, logging choices, and an inequality test span several pieces.
  - **counterfactual_value:** 4, confidence: 0.7 — Independent-friendly: small participant study with public tasks, external check on a measurement artifact in forecasting.
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---

## #105: How Much Does Coarse Monitoring Telemetry Leak? A Canary Membership-Inference Audit of Non-TEE Signals (Score: 3.21)

**ID:** gen-100

**Research Question:** For an outside monitor that sees only coarse non-TEE signals (output length, log-prob entropy, refusal rate, top tokens), how reliably can it distinguish whether a planted canary string was in a model's fine-tuning data — i.e., which monitoring signals are 'TEE-worthy' versus harmless?

**Approach:** Keep scope to a single, well-defined membership-inference-via-canaries study. Take 2-3 open instruction-tuned models served inference-only. Build a small canary set: a fixed list of unique memorizable strings, half inserted into a lightweight LoRA fine-tune (members) and half held out (non-members). For each canary, the 'monitor' observes ONLY coarse signals on a fixed probe prompt set: output length, log-prob entropy, refusal flag, and top-k token identities. Train a simple per-signal classifier (and an all-signals combined one) to predict membership, and report leakage as classifier AUC per signal type. Deliverable: a ranked table of which coarse signals leak training-membership (high AUC = TEE-worthy) vs which are safe to expose. The LoRA fine-tune is deliberately tiny to stay within consumer-GPU limits.

**Experiments:** - Create the canary set and run the LoRA fine-tune on one model inserting the member canaries; verify memorization by checking that members are more readily completed/recognized than non-members. Measure: member-vs-nonmember completion-likelihood gap. Expected outcome: confirmation that the fine-tune actually memorized canaries, so there is a real signal to detect before testing coarse monitors.
- Run the coarse-signal monitor: collect output length, log-prob entropy, refusal flag, and top-k tokens on the fixed probe set for all canaries, then train per-signal logistic-regression membership classifiers and report AUC per signal plus a combined classifier. Expected outcome: a ranked leakage table — e.g., log-prob entropy may carry membership signal (high AUC) while refusal flags do not — giving a concrete map of which signals need TEE protection.
- Generalize across models: repeat the membership-classification on the other 1-2 open models to check whether the leakage ranking is model-agnostic or model-specific. Measure: rank-correlation of per-signal AUC across models. Expected outcome: an indication of whether 'which signals leak' is a stable property monitoring-regime designers can rely on, or must be re-assessed per model.

**Impact Chain:** Governance verification regimes will decide which model-telemetry signals can be exposed to monitors without expensive TEE hardware -> if coarse signals already leak training-data membership, exposing them undermines the privacy guarantee TEEs are meant to provide -> a reproducible per-signal leakage ranking tells regime designers which signals are safe to expose and which must be hardware-protected -> better-prioritized, lower-cost privacy-preserving monitoring that more labs/regulators can actually adopt.

**Strength Rationale:** Narrow_scope (3) and accessible_complexity (3) are weak. Scope is tightened by fixing the study to a canary membership-inference design with a closed list of 4 coarse signals and a small fixed probe set — one clear deliverable (the AUC ranking table). Accessible_complexity is helped by using a tiny LoRA fine-tune (memorization is easy to induce at small scale) and standard logistic-regression classifiers rather than bespoke MI attacks. Compute stays modest because the fine-tune is deliberately tiny and the rest is inference.

**Cited Sources:** On TEEs for Privacy-Preserving Monitoring in AI Governance (Scher, MIRI TGT) — https://techgov.intelligence.org/blog/on-tees-for-privacy-preserving-monitoring-in-ai-governance

**Subfield:** AI governance / privacy-preserving verification | **Strategy:** tool_or_benchmark_gap | **Novelty:** partially_addressed (novelty_estimated)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Ranking which telemetry signals leak helps prioritize TEE protection, but the chain to catastrophic-risk reduction via governance verification has a gap.
  - **low_compute:** 4, confidence: 0.65 — A canary LoRA fine-tune plus inference is mostly light but the fine-tune adds load near the consumer-GPU limit.
  - **accessible_complexity:** 3, confidence: 0.68 — Membership-inference-style canary experiments with per-signal AUC are intermediate; conceptually demanding for beginners.
  - **narrow_scope:** 3, confidence: 0.68 — Multi-signal leakage study with canary insertion and per-signal classifiers spans several workstreams.
  - **counterfactual_value:** 4, confidence: 0.72 — Open-model leakage measurement is independent-friendly and informs verification regimes without lab access.
  - **novelty:** 3, confidence: 0.5 — estimate, no search
**Provenance:** paper_driven_light, sources: 0 KB, 1 web

---
