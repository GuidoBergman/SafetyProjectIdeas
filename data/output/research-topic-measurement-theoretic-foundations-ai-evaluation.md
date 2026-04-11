# Research Topic Report: Measurement-Theoretic Foundations for AI Evaluation

> Generated: 2026-03-30
> Requested by: coordinator
> Papers analyzed: 31

## Topic Definition

This report investigates the application of psychometric and measurement-theoretic methods to AI system evaluation, with emphasis on Item Response Theory (IRT), construct validity frameworks, Generalizability Theory (G-theory), and Computerized Adaptive Testing (CAT). The scope encompasses both capability evaluation (how well AI systems perform) and safety evaluation (whether AI systems behave safely), focusing on how decades of human measurement science can be adapted to produce rigorous, efficient, and valid AI benchmarks.

The field is rapidly growing (most papers from 2024-2026) and sits at the intersection of psychometrics, machine learning, and AI safety. A central tension runs through the literature: psychometric methods designed for stable human traits must be adapted for AI systems that are prompt-sensitive, rapidly evolving, and fundamentally different from human test-takers.

## Dimensions Tracked

| Dimension | Description | Coordinator rationale |
|-----------|------------|----------------------|
| Methodology | Which psychometric/measurement methods are applied (IRT, CTT, G-theory, factor analysis, etc.) | Maps the toolkit available and reveals methodological gaps |
| AI capability targeted | What AI capability or behavior is being measured | Shows where psychometric methods have been applied vs. untouched areas |
| Key findings | Core results and claims | The substance of what's been discovered |
| Validity evidence | What types of validity are established (construct, content, criterion, consequential) | Central to whether these measurements actually measure what they claim |
| Open questions | What the authors flag as unresolved | Direct input for research idea generation |
| Evaluation approach | How the psychometric method itself is validated | Whether the measurement framework is rigorous |
| Benchmark size requirements | Minimum dataset/item pool size needed for the approach to work reliably | Practical feasibility of each approach |

---

## Paper Catalog

### 1. Towards Measurement Theory for Artificial Intelligence

- **Authors:** Perrier
- **Source:** ArXiv (extended abstract)
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2507.05587

| Dimension | Finding |
|-----------|---------|
| Methodology | Proposes MTAI: synthesis of axiomatic/representation measurement theory, metrology, and statistical measurement (including IRT) into a unified framework. Advocates methodological realism -- hypothesizing that stable, latent attributes of AI systems exist. |
| AI capability targeted | General -- no specific capability measured. Theoretical framework for how ANY AI attribute should be measured scientifically. |
| Key findings | Current AI benchmarking is ad hoc and lacks the scientific rigor of established measurement disciplines. A formal MTAI is needed that can construct and validate representations of observables. |
| Validity evidence | Argues construct validity is central -- MTAI should provide consistent, coherent, and predictive results. No empirical evidence (theoretical paper). |
| Open questions | How to operationalize the full MTAI framework; how to validate that latent constructs of AI actually exist and are stable; reconciling axiomatic and statistical measurement traditions. |
| Evaluation approach | Purely theoretical -- outlines what rigorous evaluation would look like. |
| Benchmark size requirements | Not addressed. |

**Relevance to topic:** The foundational theoretical argument for why psychometric measurement theory should be applied to AI. Provides philosophical and methodological justification for the entire research programme.

---

### 2. Evaluating General-Purpose AI with Psychometrics

- **Authors:** Luo et al.
- **Source:** ArXiv
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2310.16379

| Dimension | Finding |
|-----------|---------|
| Methodology | Three-stage psychometric framework: (1) Construct Identification via factor analysis (top-down Delphi or bottom-up data-driven), (2) Construct Measurement via IRT + CAT, (3) Test Validation via reliability and validity analysis. CTT as limited baseline. Cognitive diagnostic models and latent class models mentioned. |
| AI capability targeted | General-purpose AI latent constructs: reasoning, comprehension, spatial reasoning, clinical reasoning, critical thinking, emotional understanding, confabulation tendency. |
| Key findings | Task-oriented benchmarks lack predictive power, explanatory power, and quality assurance. Construct-oriented evaluation via psychometrics addresses these gaps. Factor analysis of LLM performance reveals a three-construct structure (Burnell et al. 2023). Prompt sensitivity raises serious doubts about measurement consistency. |
| Validity evidence | Construct validity via factor analysis (convergent/discriminant). Predictive validity. Content validity through test blueprint. Reliability across four dimensions. Differential Item Functioning (DIF) proposed for human-AI fairness. |
| Open questions | Is an LLM tested with different prompts "one person tested repeatedly" or "multiple individuals"? Should AI receive identical instructions as humans or adapted prompts? Human-designed tests may not be valid for AI. Whether a new discipline ("AI psychometrics") is needed. |
| Evaluation approach | Theoretical framework drawing on century of human psychometrics. No original empirical validation. |
| Benchmark size requirements | No specific thresholds. References BIG-Bench (200+ tasks). IRT enables cross-test comparison with modular item pools. |

**Relevance to topic:** Foundational position paper providing the theoretical scaffolding -- the three-stage framework (identify construct, measure construct, validate test) is the reference architecture for psychometric AI evaluation.

---

### 3. LLM Psychometrics: A Systematic Review of Evaluation, Validation, and Enhancement

- **Authors:** Wang et al.
- **Source:** ArXiv
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2505.08245

| Dimension | Finding |
|-----------|---------|
| Methodology | Covers IRT, CTT, factor analysis, measurement invariance, adaptive evaluation, Evidence-Centered Design (ECD), and the PATCH eight-step process from construct definition to proficiency scoring. |
| AI capability targeted | Two categories: Personality (Big Five, HEXACO, Dark Triad, Schwartz values, morality, political attitudes) and Cognitive (heuristics/biases, Theory of Mind, emotional intelligence, psycholinguistic abilities, learning, reasoning). |
| Key findings | Early models showed elevated Dark Triad traits from uncurated training data; modern instruction-tuned models score high Openness/Agreeableness, low Neuroticism. LLM personality is highly malleable via prompting, challenging trait-stability assumptions fundamental to psychometrics. Questionnaire responses diverge significantly from open-ended behavioral measures -- ecological validity failure. |
| Validity evidence | Reliability (trait consistency across prompts -- often fails), construct validity, content validity, criterion validity, measurement invariance, social desirability bias detection. |
| Open questions | Do psychometric instruments capture meaningful latent patterns or mere statistical mimicry? Construct equivalence: does "personality" mean the same thing for an LLM as for a human? Ecological validity gap. Anthropomorphization risk. |
| Evaluation approach | Systematic literature review synthesizing validation evidence from dozens of studies. |
| Benchmark size requirements | Notes psychometric approaches typically require large human sample sizes for calibration but can then evaluate a single LLM. No minimums stated. |

**Relevance to topic:** Most comprehensive mapping of the field. Critical insight: LLM trait malleability and prompt sensitivity are fundamental threats to psychometric validity.

---

### 4. Position: AI Evaluation Should Learn from How We Test Humans

- **Authors:** Zhuang et al.
- **Source:** OpenReview / ICML 2025
- **Year:** 2025
- **URL:** https://openreview.net/forum?id=MxCJbuJhWG

| Dimension | Finding |
|-----------|---------|
| Methodology | IRT (3PL: difficulty, discrimination, guessing), Multidimensional IRT, Cognitive Diagnostic Models, Graded Response Models, neural network-based psychometric models. CAT with Fisher Information for item selection. |
| AI capability targeted | General LLM ability across MMLU, MATH, NarrativeQA, RAFT, SQuAD, MedQA. Also non-ability traits (ethics, bias, robustness) via attitude models. |
| Key findings | 100 curated items from MMLU accurately estimated performance of 5,000+ LLMs. As little as 3% of items reconstruct full benchmark performance. Fisher Information selection achieved 90% Kendall rank correlation with only 50 items from ~1,000. IRT guessing parameters detect data contamination. R-squared > 95% predicting new LLM performance from IRT estimates. |
| Validity evidence | Statistical unbiasedness. Item quality identification (negative discrimination flags annotation errors). Performance prediction (R^2 > 0.95). Bayesian uncertainty quantification. Contamination detection. |
| Open questions | Whether psychometric principles fully apply to AI or a new discipline is needed. Model-specific vs. universal laws of AI performance. Scaling neural psychometric models. |
| Evaluation approach | Simulation experiments comparing adaptive vs. traditional evaluation. Item characteristic analysis. Controlled contamination detection. |
| Benchmark size requirements | 50 items from ~1,000 for 90% rank correlation. 100 items from 14K MMLU. The 3% reduction factor is a key empirical anchor. |

**Relevance to topic:** Strongest empirical evidence that psychometric item selection dramatically reduces evaluation cost while preserving ranking validity.

---

### 5. Lost in Benchmarks? Rethinking LLM Benchmarking with IRT (PSN-IRT)

- **Authors:** Li/Zhou et al.
- **Source:** AAAI 2026 (Oral)
- **Year:** 2026
- **URL:** https://arxiv.org/abs/2505.15055
- **DOI:** via https://ojs.aaai.org/index.php/AAAI/article/view/40814

| Dimension | Finding |
|-----------|---------|
| Methodology | PSN-IRT (Pseudo-Siamese Network for IRT): neural network pathways estimate model ability and item parameters (4-parameter: discrimination, difficulty, guessing, upper asymptote). Fisher information for strategic item selection. 12 LLMs across 11 datasets (41,871 items). |
| AI capability targeted | General LLM capabilities: reasoning, knowledge, language understanding (MMLU, ARC, HellaSwag, GSM8K, + 7 others). |
| Key findings | Current benchmarks suffer from uneven measurement properties, insufficient difficulty ceilings, item saturation, and detectable data contamination. Strategically selecting 1,000 high-quality items via Fisher information achieves Kendall tau up to 0.9048 with human preference rankings, surpassing full benchmark performance. |
| Validity evidence | Criterion validity via correlation with human preference (Chatbot Arena). Construct validity through item characteristic curve analysis. Contamination detection as consequential validity. |
| Open questions | Scalability of neural IRT to larger item pools. Normal ability distribution assumption may not hold for LLMs. Handling rapid evolution of capabilities. |
| Evaluation approach | Validated against human preference benchmarks and standard IRT baselines. |
| Benchmark size requirements | Full calibration on 41,871 items and 12 models. After calibration, ~1,000 items suffice for reliable ranking. Key insight: only a small fraction of items carry useful measurement information. |

**Relevance to topic:** Demonstrates IRT reveals systemic quality problems in existing benchmarks and that principled item selection dramatically improves measurement with fewer items.

---

### 6. LEGO-IRT: Unified Framework for Data-Efficient Evaluation of LLMs

- **Authors:** (Stanford/CRFM affiliated)
- **Source:** ArXiv
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2510.04051

| Dimension | Finding |
|-----------|---------|
| Methodology | Extends IRT to handle both binary and continuous response metrics natively (no discretization). Factorized latent ability design for joint multi-benchmark modeling. MCMC inference (preferred over EM for uncertainty quantification and robustness). Full posterior inference with credible intervals. |
| AI capability targeted | General LLM capabilities across multiple benchmarks and metrics simultaneously (HELM-scale). |
| Key findings | Stable capability estimates with 3% of full evaluation data. Cross-benchmark structural information reduces estimation error by up to 10%. First framework to natively support continuous metrics in IRT for LLM evaluation. |
| Validity evidence | Construct validity through cross-benchmark prediction accuracy. Convergence diagnostics and posterior predictive checks via MCMC. |
| Open questions | Computational cost of MCMC at very large scale. Transferability of learned item parameters to new benchmarks. Growing dimensionality as new benchmarks are added. |
| Evaluation approach | Compared against full evaluation results across multiple benchmarks. Predicts unseen benchmark performance from partial data. |
| Benchmark size requirements | As low as 3% of full evaluation data. For HELM (originally $38,001 and 19,500 GPU hours for 30 LLMs), this represents massive savings. Requires calibration set with full evaluations. |

**Relevance to topic:** Most technically sophisticated IRT framework, uniquely handling continuous scores and multi-metric joint modeling.

---

### 7. Fluid Language Model Benchmarking

- **Authors:** Hofmann et al.
- **Source:** COLM 2025 / AI2
- **Year:** 2025
- **URL:** https://allenai.org/blog/fluid-benchmarking

| Dimension | Finding |
|-----------|---------|
| Methodology | Full Computerized Adaptive Testing (CAT) using 2PL IRT. Dynamic item selection via Fisher information. Four formal dimensions of benchmark refinement: efficiency, validity, variance, saturation. |
| AI capability targeted | General LLM capabilities during pretraining -- designed for evaluating evolving capabilities over training checkpoints (ARC, GSM8K, HellaSwag, MMLU, TruthfulQA, WinoGrande). |
| Key findings | On MMLU, achieves higher external validity and lower variance than standard evaluation with 50x fewer items. Automatically avoids mislabeled items (99% reduction vs. random). Delays benchmark saturation -- ability-space curves show learning signal when accuracy curves have plateaued. |
| Validity evidence | External validity via correlation with held-out benchmarks. Concurrent validity by ranking comparison. Reliability via reduced variance. Contamination avoidance validated against MMLU-Redux annotations. |
| Open questions | Cold-start for new benchmarks. Updating IRT models as model populations shift. Whether multidimensional IRT is needed. Relationship between IRT ability and deployment quality. |
| Evaluation approach | Compared against random sampling, stratified sampling, and static IRT methods across four defined quality dimensions. Evaluated on OLMo pretraining checkpoints. |
| Benchmark size requirements | 50-100 items per benchmark for reliable adaptive evaluation (vs. thousands in full benchmarks). 100 adaptively selected MMLU items outperform 5,000 randomly selected items. Calibration requires evaluation data from many models on full item pool. |

**Relevance to topic:** The most complete demonstration that adaptive IRT-based testing is strictly superior to static benchmarking across all quality dimensions. The saturation-delay finding is particularly important.

---

### 8. tinyBenchmarks: Evaluating LLMs with Fewer Examples

- **Authors:** Felipe Maia Polo, Lucas Weber, Leshem Choshen, Yuekai Sun, Gongjun Xu, Mikhail Yurochkin
- **Source:** ICML 2024
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2402.14992
- **DOI:** 10.5555/3692070.3693466

| Dimension | Finding |
|-----------|---------|
| Methodology | IRT-based performance estimation + clustering-based coreset selection + stratified sampling. IRT++ variant uses Gaussian process regression on IRT ability estimates. Released pre-selected tiny subsets. |
| AI capability targeted | General LLM capabilities across Open LLM Leaderboard (MMLU, ARC, HellaSwag, TruthfulQA, WinoGrande, GSM8K), HELM, and AlpacaEval 2.0. |
| Key findings | 100 curated examples estimate MMLU accuracy within 1.9% of true performance (140x reduction). 30 examples per scenario (180 total) suffice for full leaderboard -- 160x reduction. Methods generalize to prompt evaluation and cross-prompt prediction. |
| Validity evidence | Criterion validity via accuracy estimation error. Robustness across distribution shifts (model size, architecture, prompt templates). 2-fold cross-validation across instruction templates. |
| Open questions | Severe distribution shifts may degrade estimation. Rapid capability increases may cause extrapolation errors. Periodic updating recommended. |
| Evaluation approach | Compared tiny subset estimates against full benchmark evaluations under multiple distribution shifts. Released as public tool (runs on CPU in seconds). |
| Benchmark size requirements | 100 items per benchmark for accurate estimation. 30 items per scenario for leaderboard evaluation. Calibration requires data from hundreds of models (uses Open LLM Leaderboard data). |

**Relevance to topic:** The most practically deployed IRT-for-LLM system with released tools. The 100-item sufficiency finding is a landmark result for benchmark compression.

---

### 9. metabench -- A Sparse Benchmark of Reasoning and Knowledge in LLMs

- **Authors:** Alex Kipnis, Konstantinos Voudouris, Luca M. Schulze Buschoff, Eric Schulz
- **Source:** ICLR 2025
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2407.12844

| Dimension | Finding |
|-----------|---------|
| Methodology | Cross-validated IRT model fitting with subsampling to 350 items per benchmark. Factor analysis on latent abilities. Item information functions for selection. Data from 5,000+ LLMs. |
| AI capability targeted | General reasoning and knowledge, distilled from ARC, GSM8K, HellaSwag, MMLU, TruthfulQA, WinoGrande. |
| Key findings | A single factor captures 79.3% of total variability across latent abilities (Pearson r = 0.938 with original average). Distilled metabench (858 items, < 3% of originals) reconstructs scores with 0.58% RMSE total. |
| Validity evidence | Construct validity through factor analysis (single dominant factor). Criterion validity through score reconstruction fidelity. Out-of-sample validation on newer models. |
| Open questions | Memorization risk for smaller benchmarks. Conditional independence assumption violated (fine-tuned variants as "clones"). Core cognitive ability structure of LLMs unknown. |
| Evaluation approach | Cross-validated IRT fitting. Reconstruction error measurement. Contamination analysis via training-on-test experiments. |
| Benchmark size requirements | 858 items from 28,632 (< 3%). IRT calibration used 5,000+ models. 350 items per sub-benchmark sufficient with large model counts. |

**Relevance to topic:** Provides strongest evidence that a single latent factor underlies LLM benchmark performance (79.3% variance), supporting the psychometric premise of latent trait models for AI.

---

### 10. Confident Rankings with Fewer Items: Adaptive LLM Evaluation with Continuous Scores

- **Authors:** (2026)
- **Source:** ArXiv
- **Year:** 2026
- **URL:** https://arxiv.org/abs/2601.13885

| Dimension | Finding |
|-----------|---------|
| Methodology | Extends IRT-based CAT from binary to continuous bounded scores using heteroskedastic normal formulation. Pairwise stopping criteria for multi-model ranking. Fisher information item selection. Statistical significance testing for ranking confidence. |
| AI capability targeted | LLM text generation quality across five generation benchmarks with continuous metrics. |
| Key findings | Achieves 0.73 Kendall tau with ground-truth rankings and 95% accuracy on confident predictions using only 2% of items. Ranks models from entirely unseen families. Robust to variance structure deviations. |
| Validity evidence | Criterion validity via Kendall tau. Statistical confidence via pairwise significance tests. Generalization validated on unseen model families. |
| Open questions | Cold-start problem. Item parameters must be re-estimated per metric. FWER control reduces efficiency. Item-specific discrimination not yet modeled. |
| Evaluation approach | Compared adaptive vs. full exhaustive evaluation on 5 generation benchmarks. Tested on unseen model families. |
| Benchmark size requirements | 2% of items for confident rankings. Requires upfront exhaustive evaluation on calibration models. FWER issue: ranking reliability degrades with more models (18% error for 5 models at alpha=0.05 without correction). |

**Relevance to topic:** Fills a critical gap by extending IRT adaptive testing to continuous metrics, essential for generative task evaluation.

---

### 11. AutoIRT: Calibrating IRT Models with Automated ML

- **Authors:** (Duolingo)
- **Source:** ArXiv
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2409.08823

| Dimension | Finding |
|-----------|---------|
| Methodology | Monte Carlo EM with two-stage inner loop: (1) non-parametric AutoML on item features to predict parameters, (2) item-specific parametric refinement. Supports cold-start calibration of new items using only features (no response data). |
| AI capability targeted | English language proficiency (Duolingo English Test) -- human-focused, but methodology directly transferable to AI benchmark calibration. |
| Key findings | Better-calibrated models with improved predictive performance over non-explanatory IRT and BERT-IRT baselines. Larger existing item banks enable better cold-start calibration. No hyperparameter tuning needed. |
| Validity evidence | Criterion validity via comparison to operational scores. Predictive validity through cross-entropy loss on held-out responses. Cold-start and warm-start comparisons against baselines. |
| Open questions | Not yet applied to multi-modal items or AI system evaluation specifically. Uses hand-crafted rather than learned item features. |
| Evaluation approach | Simulation studies + real-world deployment on Duolingo test data. |
| Benchmark size requirements | Performance improves with item bank size. Hundreds of calibrated items needed for reliable cold-start. |

**Relevance to topic:** Demonstrates AutoML can solve the IRT calibration bottleneck -- highly relevant for building adaptive AI benchmarks that need continuous item addition.

---

### 12. Dual Indicators to Analyze AI Benchmarks: Difficulty, Discrimination, Ability, and Generality

- **Authors:** Martinez-Plumed et al.
- **Source:** IEEE Transactions on Games
- **Year:** 2019
- **URL:** (Semantic Scholar)

| Dimension | Finding |
|-----------|---------|
| Methodology | 2-parameter IRT (difficulty + discrimination) augmented with novel "generality" indicator -- dual to discrimination on the respondent side. Measures whether an agent is consistently good at easy problems and bad at hard ones vs. erratic. |
| AI capability targeted | General game-playing ability -- Arcade Learning Environment (Atari 2600) and GVGAI competition. |
| Key findings | Four-indicator framework provides richer insight than ability alone. Generality captures whether agents have consistent capability profiles or are "one-trick ponies." Some agents score high ability but low generality. |
| Validity evidence | Construct validity through dual mathematical relationship. Content validity via two established benchmarks. Face validity through interpretable profiles of known AI systems. |
| Open questions | Relationship of generality to transfer learning and robustness. Extension beyond game-playing. Generality vs. general intelligence. |
| Evaluation approach | Applied 2PL IRT to existing benchmark results. Validated through interpretability for known systems. |
| Benchmark size requirements | Applied to benchmarks with dozens of games/tasks and multiple agents. IRT typically requires 200+ respondents for 2PL, but they work with fewer AI agents. |

**Relevance to topic:** The earliest paper applying IRT specifically to AI benchmarks. Introduces the important "generality" concept as a measurable agent-side property.

---

### 13. Quantifying Construct Validity in LLM Evaluations

- **Authors:** (2026)
- **Source:** ArXiv
- **Year:** 2026
- **URL:** https://arxiv.org/abs/2602.15532

| Dimension | Finding |
|-----------|---------|
| Methodology | Exploratory factor analysis (EFA) with logistic IRT. Novel "structured capabilities model" combining latent factors with observational scaling laws. Horn's parallel test for factor selection. Fit indices: CFI, TLI, RMSEA. 4,395 LLMs on BIG-Bench Hard. |
| AI capability targeted | General LLM capabilities decomposed from BIG-Bench Hard: reasoning subtypes, language modeling, comprehension. |
| Key findings | Both latent factor models AND scaling laws discover a dominant factor that is actually a proxy for model parameter count (log-parameter size), not genuine capability. Dominant factor explains 72-73% of variance. Structured capabilities model controlling for scale outperforms both in parsimony and OOD prediction. Prior work with 29 LLMs had poor fit statistics (CFI=0.70, TLI=0.61, RMSEA=0.26). |
| Validity evidence | Construct validity via model fit statistics (acceptable: CFI >= 0.90, TLI >= 0.90, RMSEA <= 0.10; excellent: CFI >= 0.95, TLI >= 0.95, RMSEA <= 0.06). |
| Open questions | Only EFA, not CFA. Only multiple-choice (BBH). No safety/alignment benchmarks tested. Causal claims cannot be made. Ecological validity of BBH is low. |
| Evaluation approach | Two experiments comparing model fit and OOD prediction. 4,395 LLMs, 19 BBH subtasks. |
| Benchmark size requirements | N=29 models produces unacceptable fit. N=4,395 works. Hundreds to thousands of model observations needed for reliable factor analysis. 19 subtasks is a minimum viable item pool for EFA. |

**Relevance to topic:** Most empirically rigorous paper in the set. Critical finding: model size confounds latent factor analysis -- standard psychometric methods applied naively produce misleading results.

---

### 14. Measuring what Matters: Construct Validity in Large Language Model Benchmarks

- **Authors:** (Systematic review team, 29 expert reviewers)
- **Source:** ArXiv
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2511.04703

| Dimension | Finding |
|-----------|---------|
| Methodology | Systematic review of 445 LLM benchmarks. Qualitative coding of design patterns across phenomenon definition, task design, and scoring metrics. No psychometric modeling -- meta-review of validity practices. |
| AI capability targeted | General (all benchmarked capabilities). Includes safety, robustness, reasoning, language understanding. |
| Key findings | Only 53.4% of benchmarks present any evidence for construct validity. 47.8% define contested phenomena without consensus definitions. Only 16% employ statistical testing. 81.3% use exact matching metrics. 8 recommendations produced. |
| Validity evidence | Examines content validity (task representativeness) and internal validity (metric appropriateness). |
| Open questions | How to operationalize contested constructs (e.g., "safety") where no consensus exists. Whether checklist can drive cultural change. |
| Evaluation approach | Expert systematic review with inter-rater reliability checks. |
| Benchmark size requirements | Not directly addressed. Recommends representative sampling rather than convenience sampling. |

**Relevance to topic:** Most comprehensive empirical audit of construct validity practices in LLM benchmarks. The 53.4% validity evidence rate quantifies the field's measurement crisis.

---

### 15. Establishing Construct Validity in LLM Capability Benchmarks Requires Nomological Networks

- **Authors:** (2026)
- **Source:** ArXiv
- **Year:** 2026
- **URL:** https://arxiv.org/abs/2603.15121

| Dimension | Finding |
|-----------|---------|
| Methodology | Philosophical analysis comparing three construct validity frameworks: Cronbach & Meehl's nomological networks, Messick/Kane's inferential account, Borsboom's causal account. Reasoning as case study. |
| AI capability targeted | Reasoning (primary case study), theory of mind. |
| Key findings | The nomological network account is most suitable for LLM capability research. Avoids strong ontological commitments (no need to claim LLMs "truly have" reasoning) while providing rich construct meaning. Benchmarks must be embedded within networks of interrelated capabilities. |
| Validity evidence | Construct validity is the central topic. Argues isolated benchmark scores provide no construct validity. |
| Open questions | How to actually build nomological networks in practice. Whether the approach scales across many LLM constructs. |
| Evaluation approach | Conceptual argument; no empirical validation. |
| Benchmark size requirements | Not addressed. |

**Relevance to topic:** Strongest theoretical foundation for why psychometric validity frameworks must be adapted for LLM evaluation. The nomological network concept is central to serious construct validity efforts.

---

### 16. The Benchmarking Epistemology: Construct Validity for Evaluating ML Models

- **Authors:** (2025)
- **Source:** ArXiv
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2510.23191

| Dimension | Finding |
|-----------|---------|
| Methodology | Epistemological framework from psychological measurement theory. Three case studies: ImageNet, WeatherBench, Fragile Families Challenge. Formal conditions for construct validity in ML benchmarks. |
| AI capability targeted | Broader ML: image classification, weather prediction, life outcome prediction. Not LLM-specific. |
| Key findings | Benchmark scores are measurements of dataset-relative performance, not theoretical constructs. Drawing inferences requires explicit assumptions about theoretical structure of learning problems, evaluation functions, and data distributions. These assumptions are rarely explicit. |
| Validity evidence | Develops conditions for construct validity bridging measurement theory and ML. Content validity (distribution representativeness) and external validity (generalization). |
| Open questions | How to formalize learning problem structure for different ML domains. Transfer to generative models. |
| Evaluation approach | Philosophical framework with three illustrative case studies. |
| Benchmark size requirements | Implicitly: must be sufficient to represent target data distribution. |

**Relevance to topic:** Uniquely bridges measurement theory and ML epistemology beyond just LLMs. The formal conditions framework could be operationalized into concrete validity tests.

---

### 17. Measurement to Meaning: A Validity-Centered Framework for AI Evaluation

- **Authors:** (2025)
- **Source:** ArXiv
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2505.10573

| Dimension | Finding |
|-----------|---------|
| Methodology | Claim-centered validity framework. Five validity types: content, external, criterion, construct, consequential. Four mechanisms linking evidence to claims. Case studies in vision and language models. |
| AI capability targeted | General AI capabilities including reasoning (vision and language case studies). |
| Key findings | Traditional benchmark-driven evaluation fails to capture real-world behaviors for abstract capabilities. The gap between measured performance and actual capability is the central challenge. Nomological networks mapping AI constructs to measurable variables are needed. |
| Validity evidence | Most comprehensive validity typology -- addresses all five forms and identifies specific risks to each. |
| Open questions | How to operationalize nomological networks in high-stakes settings. Empirical validation flagged as future work. |
| Evaluation approach | Theoretical framework with illustrative case studies. |
| Benchmark size requirements | Not specified. |

**Relevance to topic:** Most comprehensive validity framework covering all five validity types. Clearest articulation of the measurement-to-claim gap.

---

### 18. Safety by Measurement: A Systematic Literature Review of AI Safety Evaluation Methods

- **Authors:** (2025)
- **Source:** ArXiv
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2505.05541

| Dimension | Finding |
|-----------|---------|
| Methodology | Taxonomy of behavioral techniques (scaffolding, red teaming, SFT) and internal techniques (representation analysis, mechanistic interpretability). Not psychometric per se -- evaluation landscape mapping. |
| AI capability targeted | Three property types: capabilities (upper-bound under adversarial push), propensities (default behavioral tendencies), control (safety measure robustness). Specific: cybersecurity exploitation, deception, autonomous replication, situational awareness, power-seeking, scheming. |
| Key findings | Benchmarks fail to establish true upper bounds or predict deployment behavior. Three challenges: proving absence of capabilities, model sandbagging, safetywashing. Capabilities vs. propensities distinction is critical. |
| Validity evidence | Implicitly critiques validity without using psychometric terminology. |
| Open questions | How to prove absence of dangerous capabilities. How to detect sandbagging. How to prevent safetywashing. Integration into governance. |
| Evaluation approach | Systematic literature review with three-dimensional taxonomy (what/how/framework). |
| Benchmark size requirements | Not addressed. |

**Relevance to topic:** Maps the safety evaluation landscape. The capabilities/propensities/control distinction is essential for deciding WHAT to measure psychometrically.

---

### 19. How Should AI Safety Benchmarks Benchmark Safety?

- **Authors:** (2026)
- **Source:** ArXiv
- **Year:** 2026
- **URL:** https://arxiv.org/abs/2601.23112

| Dimension | Finding |
|-----------|---------|
| Methodology | Critical analysis. Examines binary pass/fail rates (79% of benchmarks), ordinal severity scales, proxy metrics. Proposes three-dimension framework: construct coverage, risk quantification, measurement validity. |
| AI capability targeted | Toxicity, bias/discrimination, jailbreaks, privacy leakage, hallucinations, malicious use (bio/chem), distribution shift, manipulation/deception. |
| Key findings | 81% of benchmarks evaluate only predefined known risks. Only 38% ground metrics in established frameworks. 68% use single-turn only. Halving a toxicity score does not halve harm. Proxy-chain erosion: each abstraction layer weakens validity. 170 benchmarks for known-knowns, only 2 for unknown-unknowns. |
| Validity evidence | Construct validity failures extensively documented. Lack of standardization. Context insensitivity. |
| Open questions | How to discover unknown unknowns. Whether severity scales should be equal-interval or power-law. How to calibrate benchmark frequencies to real-world prevalence. |
| Evaluation approach | Meta-analysis with 10 concrete recommendations (R1-R10). |
| Benchmark size requirements | Quantity is not the bottleneck -- construct validity is. |

**Relevance to topic:** Most devastating critique of safety benchmarking. The 170-vs-2 known/unknown ratio quantifies the inadequacy of current practice.

---

### 20. Can We Trust AI Benchmarks? An Interdisciplinary Review

- **Authors:** (2025)
- **Source:** ArXiv
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2502.06559

| Dimension | Finding |
|-----------|---------|
| Methodology | Interdisciplinary meta-review of ~100 studies over 10 years from NLP, ML, CV, social sciences, humanities. |
| AI capability targeted | General AI capabilities, safety, high-impact capabilities. Text, vision, multimodal, RL benchmarks. |
| Key findings | Benchmarks promise too much, are gamed too easily, measure the wrong thing, are ill-suited for real-world use. Serious documentation gaps. Over-focus on English, text-based, one-time testing. |
| Validity evidence | Construct validity issues, content validity failures, consequential validity concerns (regulatory reliance on flawed benchmarks). |
| Open questions | Effectiveness of mitigations (dynamic benchmarks, hidden datasets). Whether critique translates to practice change. "Unknown unknowns" in capability measurement. |
| Evaluation approach | Systematic literature review. |
| Benchmark size requirements | Not directly addressed. Notes multi-task aggregation as mitigation but no minimum sizes. |

**Relevance to topic:** Broadest survey of benchmark failure modes. Comprehensive catalogue of what goes wrong.

---

### 21. BetterBench: Assessing AI Benchmarks, Uncovering Issues, and Establishing Best Practices

- **Authors:** (NeurIPS 2024 Spotlight)
- **Source:** ArXiv
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2411.12990

| Dimension | Finding |
|-----------|---------|
| Methodology | 46 best-practice criteria spanning design, implementation, documentation, maintenance. Applied to 24 benchmarks. Four-level scoring. |
| AI capability targeted | General -- both foundation model and non-foundation model benchmarks (MMLU, GPQA, etc.). |
| Key findings | Large quality differences: MMLU scored 5.5/20, GPQA scored 11.0/20. 14/24 did not report statistical significance. 17/24 lacked replication scripts. Implementation criteria scored lowest. |
| Validity evidence | Procedural/documentation validity. Notes construct validity would require additional domain expert analysis. |
| Open questions | Equal weighting of criteria may not reflect importance. How to extend to private benchmarks. Gaming risk. |
| Evaluation approach | Expert assessment of 24 benchmarks against 46 criteria. Living repository at betterbench.stanford.edu. |
| Benchmark size requirements | Benchmarks must run multiple evaluations with different random seeds/temperatures. Sufficient evaluation runs, not just large item pools. |

**Relevance to topic:** Practical, operational quality assessment framework. The MMLU vs. GPQA comparison concretely demonstrates quality variance.

---

### 22. Paradigms of AI Evaluation: Mapping Goals, Methodologies and Culture

- **Authors:** John Burden, Marko Tesic, Lorenzo Pacchiardi, Jose Hernandez-Orallo
- **Source:** IJCAI 2025 (Survey Track)
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2502.15620
- **DOI:** 10.24963/ijcai.2025/1153

| Dimension | Finding |
|-----------|---------|
| Methodology | Multi-dimensional taxonomic survey. 125+ papers annotated across structured dimensions using Jaccard distance matrices and UMAP visualization to identify paradigm clusters. Dimensions organized into Goals (indicator type, distribution summarization, evaluation subject), Methodologies (measurement type, task origin, protocol, reference type, task mode), and Cultures (evaluator type, motivation, discipline). |
| AI capability targeted | Meta-level: does not evaluate AI capabilities directly but maps HOW capabilities are evaluated across the field. Covers all capability types as evaluated by others. |
| Key findings | Six distinct evaluation paradigms identified: Benchmarking, Evals (red-teaming/safety), Construct-Oriented (psychometric), Exploratory, Real-World Impact, and TEVV (formal verification). The Construct-Oriented paradigm is distinguished by reliance on human psychology theories and "latent construct" measurement -- this is where IRT/psychometric approaches live. "Evals" paradigm (safety-focused) and "Construct-Oriented" paradigm rarely cross-pollinate despite complementary strengths. |
| Validity evidence | Validity explicitly excluded from analysis framework: "We do not focus on these issues here, as they apply broadly to all AI evaluation tools." Identifies validity concerns within the Construct-Oriented paradigm but does not develop a cross-paradigm framework. |
| Open questions | Whether additional dimensions reveal sub-paradigms. How to foster cross-paradigm pollination (especially Construct-Oriented <-> Evals). Moral evaluations and data dignity underdeveloped. Formal verification (TEVV) barely applied to LLMs. |
| Evaluation approach | Qualitative taxonomy with quantitative clustering (Jaccard + UMAP). Expert-driven paper selection aimed at diversity. |
| Benchmark size requirements | Not addressed. |

**Relevance to topic:** Essential context for understanding why construct validity is inconsistently applied -- different paradigms have different goals and cultures. The key insight for this report is that the Construct-Oriented and Evals paradigms need cross-pollination.

---

### 23. Leveraging CAT for Cost-effective Evaluation of LLMs in Medical Benchmarking

- **Authors:** (2026)
- **Source:** ArXiv
- **Year:** 2026
- **URL:** https://arxiv.org/abs/2603.23506

| Dimension | Finding |
|-----------|---------|
| Methodology | IRT-based CAT. Two-phase: (1) Monte Carlo simulation for configuration optimization, (2) empirical evaluation. Dynamic item selection. Termination at reliability threshold (SE <= 0.3). |
| AI capability targeted | Medical knowledge in LLMs. Domain-specific competency assessment. |
| Key findings | CAT-derived estimates correlated r = 0.988 with full-bank estimates using only 1.3% of items. Evaluation time reduced from hours to minutes per model. Rankings preserved across 38 models. |
| Validity evidence | Near-perfect correlation with gold standard (r=0.988). Ranking preservation. Monte Carlo validation. |
| Open questions | Not a substitute for clinical validation or safety-oriented prospective studies. Generalizability beyond medical domain. Depends on human-calibrated items. |
| Evaluation approach | Monte Carlo simulation + empirical validation on 38 LLMs. |
| Benchmark size requirements | 1.3% of item bank (SE <= 0.3). For ~1,000 items, roughly 13 items per model. Most concrete size data point in the set. |

**Relevance to topic:** Strongest empirical CAT demonstration. The 1.3% with r=0.988 is the headline result. Two-phase Monte Carlo design is a methodological template.

---

### 24. Survey of Computerized Adaptive Testing: A Machine Learning Perspective

- **Authors:** Liu et al.
- **Source:** ArXiv
- **Year:** 2024
- **URL:** (Semantic Scholar)

| Dimension | Finding |
|-----------|---------|
| Methodology | Comprehensive CAT survey. Cognitive models: IRT (3PL, MIRT), Cognitive Diagnostic Models (DINA, G-DINA), deep learning (NeuralCD, DIRT). Selection: Fisher Information, KL divergence, RL (DQN, NCAT), meta-learning (BOBCAT), subset selection (BECAT). |
| AI capability targeted | Both human and AI assessment. General LLM proficiency estimation. |
| Key findings | Data-driven methods (RL/meta-learning) automatically optimize selection. Statistical methods dominant in practice for interpretability. 100 MMLU items estimate 5,000+ LLMs. Retrieval-based methods improve selection 200x. |
| Validity evidence | Two paradigms: performance prediction (cross-entropy) and proficiency estimation (MSE). |
| Open questions | Data bias and overfitting. Balancing exposure control, fairness, robustness, and efficiency. Integrating LLMs into item bank construction. Test security. |
| Evaluation approach | Literature survey with taxonomy across four CAT components. |
| Benchmark size requirements | Practical anchors: 100 items from 14K MMLU. < 3% of original benchmarks. Bank construction requires sufficient response data for calibration. |

**Relevance to topic:** Definitive reference for CAT implementation options. Maps the full design space of selection algorithms, models, and bank construction.

---

### 25. A Novel Psychometrics-Based Approach to Developing Professional Competency Benchmark for LLMs

- **Authors:** (2024)
- **Source:** ArXiv
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2411.00045

| Dimension | Finding |
|-----------|---------|
| Methodology | Evidence-Centered Design (ECD) as framework. Bloom's Taxonomy for cognitive complexity. Blueprint design specifying indicators, content units, and taxonomy levels. IRT mentioned as planned follow-up but not applied. |
| AI capability targeted | Professional competency in pedagogy/education (Russian language). Breadth AND depth across Bloom's taxonomy. |
| Key findings | LLM reliability as autonomous teaching assistants is limited for deeper cognitive engagement. Blueprint-based design reveals gaps invisible to MMLU-style benchmarks. ECD provides more refined evaluation by linking items to predefined outcomes. |
| Validity evidence | Content validity through expert consortium and ECD alignment. Blueprint ensures systematic coverage. IRT reliability analysis deferred. |
| Open questions | MC-only format may not capture higher-order processes. Open-ended response types needed. IRT analysis not yet completed. |
| Evaluation approach | Expert-designed benchmark with empirical GPT testing. |
| Benchmark size requirements | Not specified. Blueprint implies systematic coverage matrix. |

**Relevance to topic:** Demonstrates practical workflow for building psychometrically grounded benchmarks from scratch using ECD + Bloom's Taxonomy.

---

### 26. Revisiting Generalizability Theory in the Age of Artificial Intelligence

- **Authors:** (2025)
- **Source:** ScienceDirect
- **Year:** 2025
- **URL:** https://www.sciencedirect.com/science/article/pii/S2666557325000370

| Dimension | Finding |
|-----------|---------|
| Methodology | Generalizability Theory (G-Theory): variance decomposition into facets (persons, items, raters, occasions). G-Studies identify variance components; D-Studies optimize measurement designs. Extends to AI-specific facets: algorithmic models, training datasets, prompt characteristics. |
| AI capability targeted | AI-driven educational tools. The variance decomposition framework applies to any AI measurement context. |
| Key findings | G-Theory uniquely suited to disentangle error sources from AI systems, user diversity, and environments. New AI-specific variance facets: algorithmic models, training data, prompt characteristics. AI tool effectiveness varies significantly across settings. G-Theory accommodates both relative and absolute decisions. |
| Validity evidence | Reliability quantification through generalizability coefficients. Bias mitigation via variance decomposition. |
| Open questions | Defining appropriate facets for AI systems. Handling that AI models change between measurement occasions. |
| Evaluation approach | Theoretical/conceptual. Applies established G-Theory framework to AI context. |
| Benchmark size requirements | Requires sufficient observations per facet combination. Standard practice: dozens of items x multiple occasions, depending on design. |

**Relevance to topic:** Introduces a framework orthogonal to IRT -- G-Theory quantifies how much observed variance comes from the construct vs. error sources. Directly applicable to understanding why safety evaluations are unreliable.

---

### 27. Introducing the Epoch Capabilities Index (ECI)

- **Authors:** Epoch AI
- **Source:** LessWrong
- **Year:** 2025
- **URL:** https://www.lesswrong.com/posts/2RtuThoZwP4o8aEpS/introducing-the-epoch-capabilities-index-eci

| Dimension | Finding |
|-----------|---------|
| Methodology | IRT-like statistical model: models deemed more capable if they score well on difficult benchmarks; benchmarks deemed more difficult if capable models score poorly. Joint estimation of latent ability and item difficulty -- the core of IRT. Composite across ~40 benchmarks. |
| AI capability targeted | General AI capabilities. Aggregates ~40 benchmarks for a single composite score per model. |
| Key findings | "Saturation-proof" by stitching benchmarks together. Enables global comparisons between models never evaluated on the same benchmarks. Principled difficulty-based weighting. |
| Validity evidence | IRT-like model implicitly provides construct validity through latent trait estimation. Full paper promised. |
| Open questions | How well stitching holds across very different benchmark types. Robustness to benchmark selection. |
| Evaluation approach | IRT-like statistical model jointly estimates ability and difficulty. |
| Benchmark size requirements | Uses ~40 benchmarks. No minimum item pool size discussion. |

**Relevance to topic:** Concrete application of IRT to produce a saturation-proof, cross-benchmark capability index.

---

### 28. General Scales Unlock AI Evaluation with Explanatory and Predictive Power (ADELE)

- **Authors:** Hernandez-Orallo et al. (incl. Microsoft Research)
- **Source:** ArXiv (full paper) + Alignment Forum (blog post)
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2503.06378 (paper), https://www.alignmentforum.org/posts/m2qMj7ovncbqKtzNt/ (blog)

| Dimension | Finding |
|-----------|---------|
| Methodology | Theory-driven rubric annotation across 18 cognitive/knowledge dimensions derived from CHC (Cattell-Horn-Carroll) theory. Rubrics rate task instance demands 0-5+ per dimension. GPT-4o applies rubrics automatically per instance (289,944 total annotations: 16,108 items x 18 dimensions). Random Forest classifier trained on 18-dimensional + unguessability demand profile predicts binary success/failure per model-instance pair. Explicitly contrasted with data-driven factor analysis. |
| AI capability targeted | Universal cognitive capabilities: 11 primordial capabilities (attention/scan, comprehension/expression, conceptualization/learning, metacognition x3, mind modeling, quantitative/logical reasoning x2, spatial reasoning), 5 knowledge domains (applied, customary, formal, natural, social sciences), 2 extraneous dimensions (atypicality for contamination, volume for task length). Extending to propensities: deception, goal-directedness, self-control. |
| Key findings | In-distribution AUROC: 0.839, ECE: 0.011. Task-holdout OOD: AUROC 0.81, ECE 0.02. Benchmark-holdout OOD: AUROC 0.75, ECE 0.04. Matches finetuned LLaMA-3.1-8B on discrimination but vastly superior calibration (ECE 0.011 vs 0.043). 40-75x faster training. 11 broader dimensions achieve comparable prediction to 18. All 18 features retain non-zero importance. |
| Validity evidence | Human inter-rater agreement (rWG 0.83 avg) via 5-person Delphi panel. GPT-4o vs Delphi consensus Spearman 0.86. Predictive validity via AUROC/ECE across in-distribution, task-OOD, and benchmark-OOD. Construct distinctiveness: most inter-dimension correlations are low-moderate (only 2 pairs above 0.8). Theory grounded in established CHC framework. |
| Open questions | Limited modality coverage (text only). Few high-demand (5+) items; scales need extension for superhuman AI. Mind Modeling dimension has only ~300 instances. Extension to propensities for safety. Dual-use risk of demand profiles. |
| Evaluation approach | Random Forest with 10-fold CV (in-distribution), leave-one-task-out (task OOD), leave-one-benchmark-out (benchmark OOD). Human validation via Delphi method. |
| Benchmark size requirements | Full battery: 16,108 items from 20 benchmarks across 63 tasks. ADeLe-Light reduces via redundant profile removal but exact count undisclosed. For 11 items: 11 items x 15 models = 165 training rows with 19 features -- technically trainable but severe overfitting risk. No formal minimum analysis provided. |

**Relevance to topic:** The most psychometrically sophisticated approach in the literature. Theory-driven scales grounded in CHC provide both predictive and explanatory power. The extension to propensities (deception, goal-directedness) is a novel direction for safety measurement. The demand-annotation approach is item-count-agnostic in principle (annotate any item's demands), but the RF assessor needs sufficient diverse training data.

---

### 29. We Need a Science of Evals

- **Authors:** Marius Hobbhahn, Jeremy Scheurer (Apollo Research)
- **Source:** LessWrong
- **Year:** 2024
- **URL:** https://www.lesswrong.com/posts/fnc6Sgt3CGCdFmmgX/we-need-a-science-of-evals

| Dimension | Finding |
|-----------|---------|
| Methodology | Position paper -- no specific psychometric methods proposed. Advocates for formal hypothesis testing, statistical significance (referencing physics' five-sigma), systematic prompt variation protocols, coverage quantification. |
| AI capability targeted | General LM capabilities with emphasis on safety-relevant properties. Responsible Scaling Policies and capability thresholds. |
| Key findings | Current evals are "much more an art than a science." Prompt sensitivity causes up to 76 accuracy-point swings; even "(A)" to "[A]" shifts accuracy ~5 points. Emergent capabilities may be metric artifacts. New prompting techniques continuously raise baselines, making negative results unreliable. |
| Validity evidence | Discusses construct validity ("overfitting to incorrect concepts"), coverage/content validity, generalization/external validity, and reliability -- without formal psychometric terminology. |
| Open questions | Conceptual clarity about what evals measure. Coverage confidence quantification. Systematic bias detection. Characterizing elicitation techniques via scaling laws. Measuring "optimization power needed to elicit behavior." Regulatory standards for legally defensible evals. |
| Evaluation approach | Proposes six key questions mature evals should answer covering precision, coverage, robustness, replicability, statistical guarantees, and predictiveness. |
| Benchmark size requirements | No explicit size discussion. "Only one prompt without paraphrases has minimal coverage" implies multiple instantiations needed. |

**Relevance to topic:** High-level framing and motivation. Identifies the exact gaps that psychometric approaches aim to fill.

---

### 30. Capabilities Ain't All You Need: Measuring Propensities in AI

- **Authors:** Daniel Romero-Alvarado et al.
- **Source:** ArXiv
- **Year:** 2026
- **URL:** https://arxiv.org/abs/2602.18182

| Dimension | Finding |
|-----------|---------|
| Methodology | Introduces the 2x2PL model, a bilogistic extension of IRT's 2PL. Instead of a single monotonic difficulty threshold (higher ability = higher success), propensities are modeled as an "ideal band" [b_l, b_u] -- success is highest when a model's propensity falls within that interval, with both excess and deficiency reducing performance. When b_u approaches infinity, reduces exactly to standard 2PL, so capabilities are a special case. Propensity demands annotated via 7-point rubrics (-3 to +3) by GPT-4.1. Estimation via MLE with gradient-based optimization. |
| AI capability targeted | Model propensities (behavioral tendencies) as distinct from capabilities. Non-monotonic traits where "too much" or "too little" both cause failures. Four dimensions tested: red-vs-blue color bias, risk aversion/seeking, extraversion/introversion, ultracrepidarianism/prudence. Safety-relevant propensities (e.g., ultracrepidarianism -- tendency to answer when you shouldn't) explicitly targeted. |
| Key findings | System prompts at incitation levels -3 to +3 produce monotonic shifts in measured propensity. Combining propensities with capabilities improves prediction by +1.6-2.0% AUROC over capabilities alone. Ultracrepidarianism is the most impactful propensity for QA tasks. Some models resist certain incitations (Llama 3.2 failed ultracrepidarianism incitation). The model mathematically unifies capabilities and propensities under a single IRT framework. |
| Validity evidence | Construct validity via mathematical proof of 2PL generalization. Convergent validity: incitation levels produce expected monotonic shifts. Criterion/predictive validity: cross-dataset prediction from synthetic benchmarks to TimeQA/MentalQA. Boundary behavior confirms probability ~0.5 at interval edges. |
| Open questions | Should model propensities also have two parameters (theta_l, theta_u) instead of one? Estimation error conflated with sample size effects. Only short-horizon single-item tasks tested -- agent-based scenarios likely show stronger effects. Only 4 propensity dimensions tested. No human validation of GPT-4.1 annotations. |
| Evaluation approach | Rubric-based annotation (-3 to +3) via GPT-4.1, MLE estimation, 10-fold cross-validation with Random Forest assessors, cross-dataset prediction experiments. |
| Benchmark size requirements | Synthetic datasets ~250 items each; main evaluation 360 items. Cross-validation enforces minimum ~50 samples per split. No formal minimum sample size analysis for MLE convergence. No evidence the approach works below ~250 items. |

**Relevance to topic:** First paper to formally extend IRT to non-monotonic propensity measurement in AI. The 2x2PL model mathematically unifies capabilities and propensities, directly addressing the gap identified in Papers 18 and 28. Critical for safety evaluation where traits like ultracrepidarianism (answering when uncertain) are safety-relevant.

---

### 31. No Answer Needed: Predicting LLM Answer Accuracy from Question-Only Linear Probes

- **Authors:** Ivan Vicente Moreno Cencerrado, Arnau Padres Masdemont, Anton Gonzalvez Hawthorne, David Demitri Africa, Lorenzo Pacchiardi
- **Source:** ArXiv
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2509.10625

| Dimension | Finding |
|-----------|---------|
| Methodology | Extracts residual stream activations at the final question token BEFORE any answer generation. Computes centroids (mean activations) for questions answered correctly vs. incorrectly. "Correctness direction" defined as w = mu_true - mu_false. New questions scored by projecting activations onto this direction. Deliberately linear (difference-of-means, not logistic regression) to test whether correctness is linearly separable in activation space. Not psychometric per se, but complementary -- predicts item difficulty from model internals rather than response patterns. |
| AI capability targeted | Pre-generation anticipation of correctness -- whether models "know that they know." Tests the Linear Representation Hypothesis for correctness as a latent trait. |
| Key findings | In-distribution AUROC: 0.758-0.826 (TriviaQA). Strong OOD generalization to factual domains: Cities 0.732-0.880, Notable People 0.708-0.825. Complete failure on GSM8K math reasoning (0.499-0.601, near random). "Factual correctness" and "arithmetic correctness" appear to be distinct, orthogonal internal representations. "I don't know" responses cluster at negative extreme of correctness direction. Performance saturates at intermediate layers (~midpoint to 2/3 depth). Outperforms verbalized confidence by 10-39 AUROC points on some datasets. |
| Validity evidence | Outperforms multiple baselines (OpenAI embeddings + logistic regression, XGBoost, verbalized confidence). Cross-dataset generalization. Linear separability as evidence for the Linear Representation Hypothesis. 5-fold cross-validation. |
| Open questions | Why does the signal fail for mathematical reasoning? Only open-source models tested. Correctness treated as binary from single samples, ignoring generation stochasticity. Linear probes may underestimate actual predictive power. |
| Evaluation approach | AUROC as primary metric. 5-fold CV for in-distribution, direct transfer for OOD. No calibration analysis (ECE not reported). |
| Benchmark size requirements | Robust performance at 160 samples. 2,560 samples match full 48,540-sample performance. Larger models require fewer samples. At 11 items, you'd have ~5-6 correct and ~5-6 incorrect for centroids -- likely too few for reliable estimation. Minimum tested was 160. |

**Relevance to topic:** Offers a complementary "inside-out" approach to item analysis -- rather than inferring item difficulty from response patterns (IRT), it predicts correctness from model internals before any response. Could augment IRT by providing item difficulty estimates from a single model's representations, potentially useful for cold-start calibration. The factual/reasoning orthogonality finding supports multidimensional measurement.

---

## Dimension Synthesis

### 1. Methodology

**Pattern:** IRT dominates the applied literature, with most papers using 2PL or 3PL models. A clear progression exists from classical IRT to neural extensions (PSN-IRT, AutoIRT) and from binary to continuous response models (LEGO-IRT, Confident Rankings). Factor analysis serves as a complementary tool for dimensional structure discovery. G-Theory and ECD appear in single papers each, representing underexplored methodological frontiers.

**Key findings:**
- IRT successfully models AI benchmark responses across all tested domains -- from Papers 4, 5, 7, 8, 9
- Neural network extensions improve IRT parameter estimation for large-scale benchmarks -- from Paper 5
- Factor analysis reveals a single dominant factor explaining 72-79% of variance -- from Papers 9, 13
- Model scale (parameter count) confounds latent factor analysis if not controlled -- from Paper 13

**Gaps:** Multidimensional IRT is discussed but rarely applied. G-Theory has a single theoretical paper (26) with no empirical AI application. Cognitive Diagnostic Models are mentioned (Papers 2, 24) but not applied to AI. No paper uses Generalizability Theory empirically for AI evaluation. The 2x2PL propensity model (Paper 30) is a single paper with no follow-up validation yet.

### 2. AI Capability Targeted

**Pattern:** The vast majority of work targets general LLM capabilities on standard benchmarks (MMLU, ARC, GSM8K, etc.). Domain-specific applications exist for medical knowledge (Paper 23) and education (Paper 25). Safety properties are extensively discussed in survey/framework papers but are NOT yet measured using psychometric methods.

**Key findings:**
- General capability benchmarks are the primary testbed for psychometric methods -- from Papers 4-9
- Medical/clinical domains show successful domain-specific CAT application -- from Paper 23
- Safety capabilities (deception, power-seeking, scheming) are mapped conceptually but lack psychometric measurement -- from Papers 18, 19
- ADELE extends from capabilities to propensities (deception, goal-directedness) -- from Paper 28

**Gaps:** Paper 30 (2x2PL) is the first to formally measure propensities via IRT, but only on synthetic/curated benchmarks, not existing safety benchmarks. No paper applies standard IRT, CAT, or factor analysis to AI safety benchmarks directly. Agentic capabilities are mostly untouched. Paper 31 reveals that factual and reasoning correctness are orthogonal internal representations, suggesting safety-relevant capabilities may also be internally separable.

### 3. Key Findings

**Pattern:** Four convergent findings dominate:

1. **Massive redundancy in existing benchmarks.** Multiple papers converge: 1.3-3% of items carry the vast majority of measurement information (Papers 5, 6, 7, 8, 9, 23).
2. **IRT reveals hidden quality problems.** Saturation, insufficient difficulty ceilings, data contamination, and mislabeled items are detectable through IRT analysis (Papers 5, 7).
3. **Construct validity is weak or absent.** Only 53.4% of 445 benchmarks present validity evidence (Paper 14). The dominant "latent factor" may be model size, not capability (Paper 13).
4. **Prompt sensitivity threatens measurement reliability.** Up to 76 accuracy-point swings from formatting changes (Paper 29). LLM "personality" is highly malleable via prompting (Paper 3).

### 4. Validity Evidence

**Pattern:** The literature shows a stark split. IRT-applied papers demonstrate strong criterion validity (correlations with human preferences and full benchmarks). Construct validity is mostly addressed theoretically (through validity frameworks) rather than empirically tested. Consequential validity (does better measurement lead to better decisions?) is virtually absent.

**Key findings:**
- Criterion validity is well-established: IRT estimates correlate r > 0.98 with full evaluations -- from Papers 5, 6, 8, 23
- Construct validity frameworks are sophisticated but untested empirically -- from Papers 15, 16, 17
- The nomological network approach provides the strongest theoretical foundation -- from Paper 15
- Model scale confounds validity when not controlled -- from Paper 13

**Gaps:** No paper establishes consequential validity. No paper validates that psychometric AI evaluation leads to better AI development or safety decisions. Differential Item Functioning (DIF) is proposed but not applied.

### 5. Open Questions

**Pattern:** Several recurring open questions span multiple papers:

1. **Population definition:** Is an LLM tested with different prompts one "person" or many? (Papers 2, 3)
2. **Construct equivalence:** Does "reasoning" (or "personality") mean the same thing for an LLM as a human? (Papers 2, 3, 15)
3. **Cold-start problem:** All adaptive approaches require calibration data from existing evaluations before working (Papers 7, 10, 11)
4. **Temporal stability:** AI capabilities evolve rapidly -- how to handle item parameter drift? (Papers 5, 7, 8)
5. **Multidimensionality:** Is unidimensional IRT sufficient or is MIRT needed? (Papers 7, 9, 13)
6. **Safety measurement:** How to prove absence of dangerous capabilities and detect sandbagging? (Papers 18, 19)

### 6. Evaluation Approach

**Pattern:** Empirical papers validate through comparison with "full evaluation" ground truth, measuring reconstruction error and rank correlation. Theoretical papers rely on conceptual argument and case studies. No paper conducts a formal power analysis or establishes minimum requirements for psychometric validity in the AI context.

**Key findings:**
- Kendall tau, Spearman r, RMSE, and accuracy estimation error are standard validation metrics -- from Papers 5, 7, 8, 10
- Monte Carlo simulation before empirical deployment is best practice for CAT -- from Paper 23
- Cross-validated IRT fitting with out-of-sample validation is the gold standard -- from Papers 8, 9
- Human preference correlation (Chatbot Arena) serves as an external criterion -- from Paper 5

**Gaps:** No formal power analysis for IRT in AI evaluation contexts. No systematic comparison of different IRT models (1PL vs. 2PL vs. 3PL vs. neural) on the same benchmark data.

### 7. Benchmark Size Requirements

**Pattern:** The empirical literature converges on a remarkably consistent finding: **1-5% of benchmark items suffice for reliable evaluation once IRT item parameters are calibrated.** However, calibration itself requires evaluation data from hundreds to thousands of models on full item pools.

| Paper | Items needed | From pool | Fidelity | Calibration requirement |
|-------|------------|-----------|----------|------------------------|
| tinyBenchmarks (#8) | 100 | 14,000 (MMLU) | 1.9% error | Hundreds of models (Open LLM Leaderboard) |
| metabench (#9) | 858 | 28,632 | 0.58% RMSE | 5,000+ models |
| PSN-IRT (#5) | 1,000 | 41,871 | Kendall tau 0.90 | 12 models (neural IRT) |
| Fluid Benchmarking (#7) | 50-100 | Thousands | Higher validity than 5,000 random | Many models (Open LLM Leaderboard) |
| CAT-Medical (#23) | 1.3% | ~1,000 | r = 0.988 | 38 models + Monte Carlo |
| Confident Rankings (#10) | 2% | Varies | 0.73 Kendall tau | Exhaustive eval on calibration models |
| LEGO-IRT (#6) | 3% | HELM-scale | Up to 10% error reduction | Calibration set with full evals |
| Position Paper (#4) | 50 from 1,000 | ~1,000 | 90% rank correlation | 5,000+ LLMs |

**Key insight for practitioners:** The upfront calibration cost is the main barrier. Once paid (via community resources like Open LLM Leaderboard), subsequent evaluations achieve 50-100x cost reduction. Factor analysis requires more models than IRT (N=29 fails; N=4,395 works per Paper 13).

---

## Coverage Gap Analysis

### Under-Researched Areas
- **Psychometric safety evaluation:** No paper applies IRT, CAT, or factor analysis to AI safety benchmarks specifically. The safety literature (Papers 18, 19) maps what to measure but uses ad hoc methods. This is the single largest gap.
- **Agentic capability measurement:** Only Paper 28 (ADELE) discusses extending to agentic dimensions (planning, execution). No IRT application to agentic benchmarks.
- **Multimodal AI evaluation:** All IRT applications are on text-based benchmarks. Vision, audio, and multimodal capabilities are psychometrically unmapped.
- **Propensity measurement:** Paper 28 (ADELE) proposes extending to deception, goal-directedness, self-control. Paper 30 (2x2PL) provides the first formal IRT model for propensities, demonstrating empirical results on 4 propensity dimensions including safety-relevant ultracrepidarianism.

### Methodological Gaps
- **Generalizability Theory:** One theoretical paper (26) but zero empirical AI applications. G-Theory's variance decomposition is uniquely suited to the prompt sensitivity problem -- it could quantify how much evaluation variance comes from the model vs. prompt vs. evaluator vs. context.
- **Cognitive Diagnostic Models:** Mentioned in surveys (Papers 2, 24) but never applied to diagnose specific AI capability profiles beyond IRT ability scores.
- **Multidimensional IRT (MIRT):** Discussed as needed (Papers 7, 9) but no empirical application. The single-factor finding (79% variance, Paper 9) may reflect current benchmark homogeneity rather than true unidimensionality.
- **Formal power analysis:** No paper establishes minimum sample sizes for IRT/factor analysis in AI evaluation. The field relies on ad hoc "it worked with N=X" evidence.
- **Consequential validity:** Does better psychometric measurement lead to better AI development or deployment decisions? Entirely unstudied.

### Contradictions and Open Debates
- **Unidimensional vs. multidimensional ability:** metabench finds 79% single-factor variance (Paper 9), but Paper 13 shows this factor may be model scale, not genuine capability. ADELE uses 18 dimensions and finds all non-redundant (Paper 28). The field has not reconciled whether LLM capabilities are fundamentally one-dimensional or multi-dimensional.
- **Data-driven vs. theory-driven dimensions:** Factor analysis (data-driven, Papers 9, 13) vs. ADELE's theory-driven rubric scales (Paper 28). Factor analysis finds uncorrelated but less interpretable dimensions; theory-driven scales are interpretable but potentially correlated. No head-to-head comparison exists.
- **Adapted human tests vs. AI-native measurement:** Paper 2 notes human-designed tests may not be valid for AI. Paper 3 finds questionnaire responses diverge from behavioral measures. The field is split on whether to adapt existing human psychometric instruments or build AI-native ones from scratch.
- **IRT population assumptions:** Standard IRT assumes a normally distributed population of test-takers. LLMs are not randomly sampled from a population -- they are deliberately designed artifacts. Papers 5 and 9 note this assumption may be violated (fine-tuned variants as "clones"), but no paper formally addresses it.

---

## Research Frontier

**Most promising open directions:**

1. **Psychometric safety evaluation instruments** -- Apply IRT and CAT to existing safety benchmarks (toxicity, deception, power-seeking). The capabilities/propensities distinction (Paper 18) provides the construct framework; IRT provides the measurement machinery; the 2x2PL model (Paper 30) provides the first formal propensity-IRT model. Next step: apply 2x2PL to existing safety benchmarks rather than synthetic ones. Supported by: the safety benchmarking critique (Paper 19) showing 81% of safety benchmarks evaluate only known risks, and Paper 30 demonstrating that propensity measurement via IRT is feasible.

2. **G-Theory for prompt sensitivity** -- Use Generalizability Theory to decompose evaluation variance into model, prompt, evaluator, and context facets. This would directly quantify the prompt sensitivity problem (up to 76 accuracy points, Paper 29) and determine how many prompt variations are needed for reliable measurement. Supported by: Paper 26 providing the theoretical foundation, and multiple papers flagging prompt sensitivity as the #1 measurement reliability threat.

3. **Structured capabilities models** -- Extend Paper 13's approach of controlling for model scale when extracting latent capability factors. This addresses the critical confound that the "single dominant factor" may be parameter count, not capability. Combine with confirmatory factor analysis (CFA) to test theory-driven capability structures. Supported by: the EFA-only limitation flagged in Paper 13 and the interpretability advantages of ADELE's theory-driven approach (Paper 28).

4. **Adaptive safety evaluation via CAT** -- Build computerized adaptive tests for safety properties, dynamically selecting evaluation items matched to a model's demonstrated risk level. The medical CAT (Paper 23, 1.3% items, r=0.988) provides a direct template. For safety, this would enable continuous monitoring with dramatically reduced evaluation cost. Supported by: the demonstrated efficiency of CAT (Papers 7, 8, 23) and the need for ongoing safety assessment as models are updated.

5. **Consequential validity research** -- Study whether psychometrically rigorous evaluations lead to better AI development decisions compared to standard benchmarking. This is the ultimate validation of the entire research programme. Supported by: the complete absence of consequential validity evidence across all 27 papers.

**Suggested follow-up questions:**

1. What is the minimum number of AI models needed for reliable IRT calibration in safety domains, where model diversity is lower than in general capability?
2. Can G-Theory D-studies prescribe optimal evaluation designs (how many prompts x how many contexts x how many evaluators) for safety properties?
3. Does the single dominant factor in LLM benchmarks persist when safety benchmarks are included, or does safety represent an independent dimension?
4. Can multidimensional IRT recover the ADELE theory-driven dimensions from data, and do the two approaches converge on the same capability structure?
5. How should IRT handle the non-standard "population" of LLMs (designed artifacts, not random samples) -- is a Bayesian or non-parametric alternative needed?

---

## Full Source List

| # | Title | Authors | Year | Source | URL | DOI |
|---|-------|---------|------|--------|-----|-----|
| 1 | Towards Measurement Theory for Artificial Intelligence | Perrier | 2025 | ArXiv | https://arxiv.org/abs/2507.05587 | -- |
| 2 | Evaluating General-Purpose AI with Psychometrics | Luo et al. | 2023 | ArXiv | https://arxiv.org/abs/2310.16379 | -- |
| 3 | LLM Psychometrics: A Systematic Review | Wang et al. | 2025 | ArXiv | https://arxiv.org/abs/2505.08245 | -- |
| 4 | Position: AI Evaluation Should Learn from How We Test Humans | Zhuang et al. | 2025 | ICML 2025 | https://openreview.net/forum?id=MxCJbuJhWG | -- |
| 5 | Lost in Benchmarks? / PSN-IRT | Li/Zhou et al. | 2026 | AAAI 2026 | https://arxiv.org/abs/2505.15055 | ojs.aaai.org/40814 |
| 6 | LEGO-IRT | (Stanford/CRFM) | 2025 | ArXiv | https://arxiv.org/abs/2510.04051 | -- |
| 7 | Fluid Language Model Benchmarking | Hofmann et al. | 2025 | COLM 2025 | https://allenai.org/blog/fluid-benchmarking | -- |
| 8 | tinyBenchmarks | Maia Polo et al. | 2024 | ICML 2024 | https://arxiv.org/abs/2402.14992 | 10.5555/3692070.3693466 |
| 9 | metabench | Kipnis et al. | 2025 | ICLR 2025 | https://arxiv.org/abs/2407.12844 | -- |
| 10 | Confident Rankings with Fewer Items | -- | 2026 | ArXiv | https://arxiv.org/abs/2601.13885 | -- |
| 11 | AutoIRT | (Duolingo) | 2024 | ArXiv | https://arxiv.org/abs/2409.08823 | -- |
| 12 | Dual Indicators to Analyze AI Benchmarks | Martinez-Plumed et al. | 2019 | IEEE Trans. Games | (Semantic Scholar) | -- |
| 13 | Quantifying Construct Validity in LLM Evaluations | -- | 2026 | ArXiv | https://arxiv.org/abs/2602.15532 | -- |
| 14 | Measuring what Matters: Construct Validity in LLM Benchmarks | (29 reviewers) | 2025 | ArXiv | https://arxiv.org/abs/2511.04703 | -- |
| 15 | Establishing Construct Validity via Nomological Networks | -- | 2026 | ArXiv | https://arxiv.org/abs/2603.15121 | -- |
| 16 | The Benchmarking Epistemology | -- | 2025 | ArXiv | https://arxiv.org/abs/2510.23191 | -- |
| 17 | Measurement to Meaning | -- | 2025 | ArXiv | https://arxiv.org/abs/2505.10573 | -- |
| 18 | Safety by Measurement | -- | 2025 | ArXiv | https://arxiv.org/abs/2505.05541 | -- |
| 19 | How Should AI Safety Benchmarks Benchmark Safety? | -- | 2026 | ArXiv | https://arxiv.org/abs/2601.23112 | -- |
| 20 | Can We Trust AI Benchmarks? | -- | 2025 | ArXiv | https://arxiv.org/abs/2502.06559 | -- |
| 21 | BetterBench | -- | 2024 | NeurIPS 2024 | https://arxiv.org/abs/2411.12990 | -- |
| 22 | Paradigms of AI Evaluation | Burden et al. | 2025 | IJCAI 2025 | https://arxiv.org/abs/2502.15620 | 10.24963/ijcai.2025/1153 |
| 23 | CAT for Medical LLM Benchmarking | -- | 2026 | ArXiv | https://arxiv.org/abs/2603.23506 | -- |
| 24 | Survey of CAT: A ML Perspective | Liu et al. | 2024 | ArXiv | (Semantic Scholar) | -- |
| 25 | Psychometrics-Based Professional Competency Benchmark | -- | 2024 | ArXiv | https://arxiv.org/abs/2411.00045 | -- |
| 26 | Revisiting Generalizability Theory in the Age of AI | -- | 2025 | ScienceDirect | https://www.sciencedirect.com/science/article/pii/S2666557325000370 | -- |
| 27 | Epoch Capabilities Index (ECI) | Epoch AI | 2025 | LessWrong | https://www.lesswrong.com/posts/2RtuThoZwP4o8aEpS/ | -- |
| 28 | General Scales Unlock AI Evaluation (ADELE) | Hernandez-Orallo et al. | 2025 | ArXiv + AF | https://arxiv.org/abs/2503.06378 | -- |
| 29 | We Need a Science of Evals | Hobbhahn, Scheurer | 2024 | LessWrong | https://www.lesswrong.com/posts/fnc6Sgt3CGCdFmmgX/ | -- |
| 30 | Capabilities Ain't All You Need: Measuring Propensities in AI | Romero-Alvarado et al. | 2026 | ArXiv | https://arxiv.org/abs/2602.18182 | -- |
| 31 | No Answer Needed: Question-Only Linear Probes | Vicente Moreno Cencerrado et al. | 2025 | ArXiv | https://arxiv.org/abs/2509.10625 | -- |
