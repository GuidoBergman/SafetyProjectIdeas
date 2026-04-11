# Ranked Research Proposals

*Generated: 2026-04-02 18:29 UTC*
*Total proposals: 127*

---

## #1: IRT Person-Fit Analysis for Detecting Anomalous Model Response Patterns Indicative of Sandbagging (Score: 4.70)

**ID:** gen-090

**Research Question:** How can using irt response data from a publicly available capability benchmark (or constructed using api calls to accessible models), fit a 2pl irt model in r address the problem that sandbagging involves models producing response patterns inconsistent with their estimated ability level — answering easy dangerous-capability items incorrectly while getting harder non-capability items correct? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using IRT response data from a publicly available capability benchmark (or constructed using API calls to accessible models), fit a 2PL IRT model in R. Compute person-fit statistics for each model: Infit and Outfit mean-square statistics, lz* (standardized likelihood-based fit), and the U3 index. Flag models with significant person misfit. Examine whether misfitting models show the specific pattern predicted by sandbagging: lower-than-expected performance on items within specific capability domains (e.g., dangerous knowledge) but higher-than-expected performance on general reasoning items. Compare person-fit profiles across models to establish a baseline distribution and identify statistical outliers. Sandbagging paper (arXiv 2406.07358) proposes weight perturbation as detection. IRT person-fit for aberrant response detection is established in educational measurement. A 2024 paper applied IRT person-fit to detect AI-generated responses in assessments. The 'mirt' R package computes person-fit statistics. This novel application of person-fit to sandbagging is not yet in the literature.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Person-fit statistics provide an automated, quantitative sandbagging signal that does not require access to model weights or training data — only response patterns. This is a tractable, low-cost screening tool for strategic underperformance. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 5), low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI evaluation / psychometrics | **Strategy:** causal_chain_intervention | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 5, confidence: 0.7 — Compelling chain: person-fit → automated sandbagging signal → screening tool that doesn't require model weights or training data → deployment decision. Sandbagging is a recognized critical risk pathway per safety orgs.
  - **low_compute:** 5, confidence: 0.9 — Pure R analysis on existing benchmark data.
  - **accessible_complexity:** 4, confidence: 0.6 — Guided replication with mirt R package. Computes multiple person-fit statistics (infit, outfit, lz*, U3) automatically. Step-by-step protocol provided.
  - **narrow_scope:** 5, confidence: 0.7 — Single benchmark, compute person-fit for each model, flag outliers. Very well-defined success criteria: produce table of person-fit statistics + identify statistical outliers.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** causal_chain_intervention, sources: 0 KB, 0 web

---

## #2: IRT-Based Detection of Ceiling Effects in Safety-Relevant Capability Benchmarks (Score: 4.43)

**ID:** gen-081

**Research Question:** How can using a public multi-model response dataset for a safety-relevant capability benchmark (e address the problem that the capability underestimation causal chain begins with evaluation items that are too easy, producing a ceiling effect where score distributions pile up at maximum values, destroying discriminability and making capability differences invisible? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using a public multi-model response dataset for a safety-relevant capability benchmark (e.g., BIG-Bench dangerous tasks, WMDP, or similar), fit a 2-parameter logistic IRT model in R (using the 'mirt' or 'ltm' package). Extract item difficulty (b) parameters and model ability (theta) estimates. Plot the distribution of b parameters against the distribution of model theta estimates. Identify ceiling-region items (b < theta_max - 1 SD) and compute what proportion of items provide no discriminating information at the frontier of current models. Calculate test information functions showing where in the ability range the benchmark is maximally and minimally informative. Compare across 2-3 benchmarks to see if this is systematic. Benchmark saturation at >90% for MMLU by late 2024 is well-documented. WMDP was specifically designed for dangerous knowledge assessment. IRT for LLM evaluation is an active area (arXiv 2505.15055, 2510.00844). The 'mirt' package in R handles IRT with limited coding skill required.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If most items in a dangerous-capability benchmark are below frontier model ability, the benchmark structurally cannot detect capability at the level where safeguard calibration is most critical. IRT makes this visible and quantifiable. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 5), accessible_complexity (score 4), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI evaluation / psychometrics | **Strategy:** causal_chain_intervention | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong chain: ceiling effects → capability differences invisible → safeguard miscalibration at critical frontier. IRT quantifies information gaps where benchmarks fail to discriminate.
  - **low_compute:** 5, confidence: 0.9 — 2PL IRT on existing data, CPU-only.
  - **accessible_complexity:** 4, confidence: 0.7 — Standard 2PL IRT fitting with guided protocol. Item difficulty vs model ability distribution comparison is straightforward visualization.
  - **narrow_scope:** 5, confidence: 0.8 — Tightened to single benchmark analysis. Clear deliverable: b-parameter vs theta distribution plot + information gap quantification.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** causal_chain_intervention, sources: 0 KB, 0 web

---

## #3: Measurement Error Bounds for Safety Benchmark Scores: Classical Test Theory Analysis (Score: 4.43)

**ID:** gen-121

**Research Question:** How can using classical test theory (ctt), compute internal consistency reliability (cronbach's alpha, mcdonald's omega) for safety benchmark item sets address the problem that published safety benchmark scores are reported as point estimates (e? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using Classical Test Theory (CTT), compute internal consistency reliability (Cronbach's alpha, McDonald's omega) for safety benchmark item sets. Derive SEM = SD × sqrt(1-reliability). Compute 95% confidence intervals around benchmark scores for a representative set of models. Test whether overlapping confidence intervals mean that apparent rank differences between models are statistically indistinguishable. Propose a standard for minimum required reliability before a benchmark score should be reported. The 'Measuring what Matters' review (2511.04703) identified lack of reliability reporting as a core validity gap. IRT-based SEM is better than CTT-based SEM (item-level precision varies) but CTT is simpler and the gap is documented. McDonald's omega (via psych R package) is more defensible than Cronbach's alpha for safety items. No published safety benchmark includes SEM.

**Experiments:** - Compute internal consistency reliability (Cronbach's alpha, split-half) and IRT-based reliability (test information function) for a safety benchmark, reporting confidence intervals around model ability estimates
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Directly fills the measurement error gap in Success State 2. If Model X (78.3%) and Model Y (76.1%) have overlapping 95% confidence intervals, claims that X is safer than Y are not statistically supported. This has direct policy relevance: regulators setting safety thresholds need to know the precision of the measurements they are acting on. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 5), accessible_complexity (score 4), narrow_scope (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Measurement Precision / Classical Test Theory | **Strategy:** backcast_from_success | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong: if safety benchmark scores lack error bounds, deployment decisions treat noisy point estimates as precise. CTT confidence intervals make uncertainty visible. Directly actionable for governance.
  - **low_compute:** 5, confidence: 0.9 — Classical test theory, CPU-only.
  - **accessible_complexity:** 4, confidence: 0.7 — CTT is the most basic measurement framework. Cronbach's alpha, SEM computation are well-established with clear formulas.
  - **narrow_scope:** 5, confidence: 0.8 — Compute reliability + confidence intervals for safety benchmark scores. Very tightly scoped with obvious deliverable.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** backcast_from_success, sources: 0 KB, 0 web

---

## #4: Graded Response IRT Models for Safety Benchmarks: Recovering Severity Information from Ordinal Ratings (Score: 4.43)

**ID:** gen-259

**Research Question:** How can re-analyze an existing safety benchmark that has ordinal or severity-graded human annotations using a graded response model (grm) or partial credit model, comparing the information recovered vs address the problem that p5: safety benchmarks use binary pass/fail losing severity info? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Re-analyze an existing safety benchmark that has ordinal or severity-graded human annotations using a Graded Response Model (GRM) or Partial Credit Model, comparing the information recovered vs. binary dichotomization, and demonstrating what is lost by binarizing severity ratings. GRM and Partial Credit Model are standard IRT extensions for ordered polytomous responses, fully supported in mirt and ltm R packages. The 2025 PMC tutorial on GRM in R demonstrates exactly this analysis. Safety datasets with human severity ratings exist (e.g., MLCommons AI Safety Benchmark v0.5 with graded annotations, HarmBench).

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. The 'How Should AI Safety Benchmarks Benchmark Safety?' paper (arxiv 2601.23112) documents that only 14 of 36 severity-distinguishing benchmarks provide principled justification. GRM analysis would demonstrate concretely how much measurement information is destroyed by binary collapse and provide a model-based severity scale. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 5), accessible_complexity (score 4), narrow_scope (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Safety / Psychometrics | **Strategy:** combinatorial_matrix | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong: GRM recovers severity information lost by binary scoring. Enables distinguishing 'mildly harmful' from 'catastrophically harmful' responses.
  - **low_compute:** 5, confidence: 0.9 — GRM fitting in R, CPU-only.
  - **accessible_complexity:** 4, confidence: 0.6 — GRM is available in mirt. Guided protocol with clear steps. Requires ordinal recoding but straightforward.
  - **narrow_scope:** 5, confidence: 0.7 — Single benchmark, fit GRM, compare with binary IRT. Very well-defined deliverable.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** combinatorial_matrix, sources: 0 KB, 0 web

---

## #5: IRT-Based Detection of Data Contamination: Aberrant Response Patterns as Contamination Signal (Score: 4.43)

**ID:** gen-265

**Research Question:** How can apply irt person-fit statistics (lz*, w statistics) to ai model response patterns to detect aberrant responding consistent with data contamination—models that get hard items correct while missing easier items in ways that violate the irt model address the problem that p7: data contamination inflates benchmark scores undetectably? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Apply IRT person-fit statistics (lz*, W statistics) to AI model response patterns to detect aberrant responding consistent with data contamination—models that get hard items correct while missing easier items in ways that violate the IRT model. IRT person-fit statistics (lz*, W) detect atypical response patterns in human testing (e.g., cheating, careless responding). A 2025 paper (arxiv 2510.07175) explicitly applies psychometric methods to quantify data contamination in LLM evaluations. The mirt R package computes person-fit statistics. This is a direct, novel application requiring only existing benchmark response data.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Compare IRT item parameter estimates (especially guessing parameters) between models with known training data overlap and those without, testing whether aberrant parameters signal contamination
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Data contamination causes models to answer specific items correctly regardless of their true ability level, producing item response patterns that violate IRT assumptions. Person-fit statistics are designed to detect exactly this kind of aberrant responding, providing an indirect contamination signal without requiring access to training data. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 5), accessible_complexity (score 4), narrow_scope (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation / Psychometrics | **Strategy:** combinatorial_matrix | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong chain: aberrant response patterns as contamination signal. Uses person-fit as an alternative contamination detection method.
  - **low_compute:** 5, confidence: 0.9 — CPU-only analysis on existing data.
  - **accessible_complexity:** 4, confidence: 0.6 — Applies standard person-fit statistics to detect contamination. Guided protocol with clear steps.
  - **narrow_scope:** 5, confidence: 0.7 — Single benchmark, well-defined analysis: compute aberrant response indices and cross-reference with known contamination. Tightly scoped deliverable.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** combinatorial_matrix, sources: 0 KB, 0 web

---

## #6: Which Safety Benchmarks Have Item-Level Data Suitable for IRT? A Systematic Audit (Score: 4.22)

**ID:** gen-191

**Research Question:** How can conduct a systematic audit of publicly available ai safety benchmarks (e address the problem that apply irt to ai safety benchmarks? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Conduct a systematic audit of publicly available AI safety benchmarks (e.g., AdvBench, HarmBench, SALAD-Bench, WildGuard, AIR-2024) to determine which ones release item-level binary or polytomous response data across multiple models, and whether sample sizes (number of model × item cells) meet minimum IRT calibration thresholds (typically N > 200 respondents and > 20 items per dimension). tinyBenchmarks (2024) successfully applied IRT to Open LLM Leaderboard, MMLU, and HELM because those benchmarks expose item-level data. Safety benchmarks may not. The PSN-IRT framework (2025) ran IRT on 12 LLMs across 11 datasets but did not focus on safety-specific benchmarks. 'Lost in Benchmarks' (2025) similarly worked with general capability benchmarks.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. IRT requires item-level response matrices, not just aggregate scores. Before any IRT analysis of safety benchmarks is possible, someone must establish which benchmarks are even analyzable. This is the prerequisite gate for the entire parent problem and is currently undocumented. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), accessible_complexity (score 5), narrow_scope (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation / Psychometrics | **Strategy:** problem_decomposition | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 2, confidence: 0.6 — Foundational audit. Important infrastructure but no direct catastrophic risk chain.
  - **low_compute:** 5, confidence: 0.9 — Literature/data survey, CPU-only.
  - **accessible_complexity:** 5, confidence: 0.8 — Systematic audit of data availability. Most accessible of all proposals — requires searching and documenting, not advanced statistics.
  - **narrow_scope:** 5, confidence: 0.8 — Very well-defined: produce a table of benchmarks with IRT data availability assessment.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** problem_decomposition, sources: 0 KB, 0 web

---

## #7: Is There Enough Item Variance in Safety Benchmarks for IRT to Work? (Score: 4.22)

**ID:** gen-195

**Research Question:** How can for several safety benchmarks, compute the empirical distribution of item pass rates (proportion of models that refuse/comply) across items address the problem that apply irt to ai safety benchmarks? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** For several safety benchmarks, compute the empirical distribution of item pass rates (proportion of models that refuse/comply) across items. Test whether item difficulty spans the full range needed to discriminate models at different safety ability levels, whether item variance exceeds a minimum threshold (e.g., items with p > 0.95 or p < 0.05 carry near-zero information), and how many items remain informative after removing floor/ceiling items. MMLU reached saturation by mid-2024 when top models scored above 85%, losing discriminative power. Safety benchmarks may face the same problem in reverse—if all frontier models achieve >95% refusal rates on standard prompts, there is ceiling-level variance that IRT cannot leverage. tinyBenchmarks explicitly used IRT to select high-information items.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If safety benchmarks consist mostly of items that all advanced models pass (refuse harmful requests) or all models fail (comply with jailbreaks), there is minimal item variance and IRT has little to work with. This is a prerequisite diagnostic—if variance is too low, the benchmark cannot differentiate safety ability levels and needs more items in the middle difficulty range. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), accessible_complexity (score 5), narrow_scope (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation / Psychometrics | **Strategy:** problem_decomposition | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 2, confidence: 0.6 — Foundational: checks whether IRT is applicable. No direct catastrophic risk chain.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 5, confidence: 0.8 — Basic variance check. Most accessible.
  - **narrow_scope:** 5, confidence: 0.8 — Single computation: check item variance. Maximally scoped.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** problem_decomposition, sources: 0 KB, 0 web

---

## #8: Rasch Model Fit Analysis to Identify Misfitting Safety Benchmark Items (Score: 4.17)

**ID:** gen-069

**Research Question:** How can fit a rasch model to item-level response data from one or two safety benchmarks using r (mirt package) address the problem that recent irt work on llm benchmarks fits models to entire benchmark item sets, but has not used rasch model fit statistics to identify individual items that violate the measurement model—items that may be testing something other than the intended latent construct? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Fit a Rasch model to item-level response data from one or two safety benchmarks using R (mirt package). Compute infit and outfit mean-square statistics for each item. Flag items with infit > 1.3 or outfit > 1.5 as misfitting. Examine the content of misfitting items to identify what they might be measuring instead of the target construct (e.g., surface-level keyword matching, world knowledge artifacts). Propose item revisions or deletions. Compare model rankings with and without misfitting items. Rasch analysis is a core technique in health outcomes research (PROM validation) and educational measurement. arXiv 2505.15055 already fits IRT models to LLM benchmarks. R mirt package supports Rasch and 2PL/3PL models with fit statistics. Item-level response data from BIG-Bench Hard is publicly available.

**Experiments:** - Apply the proposed analysis method to item-level data from one public safety benchmark (e.g., TruthfulQA, HarmBench)
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Rasch fit statistics are the standard psychometric method for identifying items that violate the unidimensionality assumption—items that introduce construct-irrelevant variance. In safety benchmarks, misfitting items may mean scores conflate safety with general capability, knowledge, or prompt sensitivity. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), accessible_complexity (score 4), narrow_scope (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation & Benchmarking | **Strategy:** cross_domain_transfer | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible chain: identifying misfitting items reveals construct-irrelevant variance in safety benchmarks. Gap between item-level finding and catastrophic risk reduction.
  - **low_compute:** 5, confidence: 0.9 — Rasch fitting, CPU-only.
  - **accessible_complexity:** 4, confidence: 0.7 — Rasch is the simplest IRT model. Infit/outfit are standard. Very well-guided protocol possible.
  - **narrow_scope:** 5, confidence: 0.8 — Single benchmark, fit Rasch model, flag misfitting items. Very tightly scoped with well-defined success criteria.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** cross_domain_transfer, sources: 0 KB, 0 web

---

## #9: Rasch Model Analysis of Safety Evaluation Item Fit: Identifying Misfitting Items (Score: 4.17)

**ID:** gen-128

**Research Question:** How can fit a rasch model to item-level safety benchmark response data using the tam or erm r packages address the problem that safety benchmarks include items assembled by content judgment, not by empirical fit to a measurement model? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Fit a Rasch model to item-level safety benchmark response data using the TAM or eRm R packages. Compute infit and outfit mean-square statistics for each item. Flag items with outfit > 1.5 or < 0.5 as misfitting. Examine the content of misfitting items to identify why they misfit. Test whether removing misfitting items improves model fit and changes model rankings. Propose item revision guidelines based on Rasch fit diagnostics. The Rasch model is the most theoretically rigorous IRT model and the most commonly used in high-stakes credentialing. TAM and eRm R packages are well-documented. 'Measuring what Matters' recommends internal structure analysis. The LLM psychometrics systematic review (llm-psychometrics.com) covers IRT but not Rasch-specific fit analysis for safety items.

**Experiments:** - Apply the proposed analysis method to item-level data from one public safety benchmark (e.g., TruthfulQA, HarmBench)
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Fills the internal structure validity gap for Success State 2. Rasch model fit analysis is the gold standard for identifying items that undermine construct validity. Items that misfit the Rasch model are measuring something different from the rest of the battery — a fundamental validity problem. This study provides an empirical basis for benchmark item revision. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), accessible_complexity (score 4), narrow_scope (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Benchmark Quality / Rasch Analysis | **Strategy:** backcast_from_success | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: misfitting items introduce construct-irrelevant variance. Connection to specific catastrophic risk mechanism is underspecified.
  - **low_compute:** 5, confidence: 0.9 — Rasch model fitting, CPU-only.
  - **accessible_complexity:** 4, confidence: 0.7 — Rasch is the simplest IRT model. Infit/outfit statistics are standard outputs. Very guidable.
  - **narrow_scope:** 5, confidence: 0.8 — Fit Rasch model, flag items with misfit statistics, examine content. Very well-defined deliverable.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** backcast_from_success, sources: 0 KB, 0 web

---

## #10: Measurement Error Estimates for Safety Benchmark Scores: Constructing Confidence Intervals (Score: 4.17)

**ID:** gen-219

**Research Question:** How can using test-retest data or bootstrap resampling of item responses, estimate the standard error of measurement (sem) for safety benchmark scores for each of 20+ models address the problem that make ai evaluation reproducible and reliable? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using test-retest data or bootstrap resampling of item responses, estimate the standard error of measurement (SEM) for safety benchmark scores for each of 20+ models. Compute 95% confidence intervals around each model's safety score. Determine how many pairwise model comparisons are actually statistically distinguishable vs. within the margin of measurement error. Report what fraction of published safety leaderboard rankings are statistically indistinguishable. No published safety benchmark reports confidence intervals around model scores. The 'Can We Trust AI Benchmarks?' review (2025) notes this as a gap. Bootstrap SEM estimation is straightforward in R. tinyBenchmarks found < 2% estimation error with IRT-selected items, implicitly providing SEM estimates—the same approach applied to safety benchmarks would be novel.

**Experiments:** - Compute internal consistency reliability (Cronbach's alpha, split-half) and IRT-based reliability (test information function) for a safety benchmark, reporting confidence intervals around model ability estimates
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Safety benchmarks report point estimates that create the illusion of precise rankings, but no confidence intervals are published. If two models that appear to differ by 3 percentage points have overlapping 95% CIs, their ranking difference is meaningless. Quantifying measurement error is essential for scientific integrity in safety evaluation and would likely reveal that many current safety rankings are statistically indistinguishable. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), accessible_complexity (score 4), narrow_scope (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation / Reliability | **Strategy:** problem_decomposition | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible chain: error estimates reveal uncertainty in safety scores. But chain from error bounds to specific catastrophic risk reduction has gaps.
  - **low_compute:** 5, confidence: 0.9 — CTT/IRT analysis, CPU-only.
  - **accessible_complexity:** 4, confidence: 0.7 — Standard statistical computations with guided protocol.
  - **narrow_scope:** 5, confidence: 0.8 — Very tightly scoped: compute confidence intervals for benchmark scores.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** problem_decomposition, sources: 0 KB, 0 web

---

## #11: IRT-Based Validity Evidence for AI Safety Benchmarks: Item Fit and Differential Functioning (Score: 4.17)

**ID:** gen-257

**Research Question:** How can fit a 2pl irt model to a widely-used safety benchmark (e address the problem that p4: 46? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Fit a 2PL IRT model to a widely-used safety benchmark (e.g., TruthfulQA or HarmBench), examine item fit statistics, and evaluate whether items function as expected under a unidimensional latent safety model, providing empirical validity evidence that most benchmarks currently lack. IRT item fit statistics (RMSEA, S-X2) are standard validity tools in psychometrics. The mirt R package computes these automatically. Published model response matrices for TruthfulQA and similar benchmarks are publicly available. This is a direct application of existing psychometric methodology to publicly available data—well within a psychometrician's skillset.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Only 34% of benchmarks explicitly specify the risks they measure (arxiv 2502.06559). Running IRT item fit analysis on a benchmark produces empirical validity evidence: items with poor fit suggest the benchmark is measuring multiple unrelated constructs rather than a coherent safety dimension. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), accessible_complexity (score 4), narrow_scope (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Safety / Psychometrics | **Strategy:** combinatorial_matrix | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: item fit and DIF as validity evidence. Generic measurement quality.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 4, confidence: 0.7 — Standard IRT with guided protocol.
  - **narrow_scope:** 5, confidence: 0.8 — Comprehensive validity analysis of single benchmark. Well-defined.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** combinatorial_matrix, sources: 0 KB, 0 web

---

## #12: IRT Calibration of AI Safety Benchmarks: Do TruthfulQA and HarmBench Items Form Valid Scales? (Score: 4.13)

**ID:** gen-224

**Research Question:** How can download model response matrices for truthfulqa and/or bbq from the open llm leaderboard or huggingface address the problem that ai safety benchmarks such as truthfulqa (817 items), harmbench, and bbq are treated as if they are measurement instruments, but no one has fitted irt models to them? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Download model response matrices for TruthfulQA and/or BBQ from the Open LLM Leaderboard or HuggingFace. Fit 1PL (Rasch) and 2PL models in R (mirt or ltm). Assess: (1) model fit via M2 statistic, (2) item information curves to find which items are actually informative, (3) whether the scale is unidimensional via confirmatory factor analysis residuals. Identify items with near-zero discrimination (useless items) and extreme difficulty parameters (floor/ceiling). The 'Safetywashing' paper (arXiv:2407.21792) demonstrates benchmarks measure capability, not safety propensity. Cambridge scientists (2024) applied psychometrics to capability benchmarks but not safety ones. The mirt R package supports all needed analyses. Open LLM Leaderboard provides public binary response matrices.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If safety benchmark items do not meet basic IRT assumptions, then leaderboard scores are ordinal noise, not interval-scale measurements of safety. The field cannot make claims like 'model X is 12% safer than model Y' without this foundation. This is the essential first step toward rigorous AI safety measurement — and nobody has done it. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 5), narrow_scope (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** arXiv:2407.21792

**Subfield:** AI Safety Evaluation / Psychometrics | **Strategy:** landscape_gap_targeting | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong: IRT calibration reveals whether safety items form a coherent measurement scale. If not, aggregate scores are meaningless for deployment decisions.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Standard IRT fitting with guided protocol. Requires interpretation of model fit statistics.
  - **narrow_scope:** 5, confidence: 0.8 — Calibrate items on one benchmark, assess fit, report. Very tightly scoped.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** landscape_gap_targeting, sources: 0 KB, 0 web

---

## #13: IRT for Deception Propensity: Calibrating the MASK Benchmark and DeceptionBench (Score: 4.13)

**ID:** gen-243

**Research Question:** How can obtain model response data from the mask benchmark (publicly available) and/or deceptionbench address the problem that the mask benchmark measures ai deception propensity and deceptionbench operationalizes deception across multiple intensity levels and motivational patterns (egoism vs? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Obtain model response data from the MASK benchmark (publicly available) and/or DeceptionBench. Fit 1PL and 2PL IRT models. Examine item information curves to identify the most discriminating deception scenarios. Test unidimensionality using parallel analysis and confirmatory factor analysis residuals. Estimate deception-propensity scores on an IRT scale. Correlate deception-propensity IRT scores with general safety benchmark scores and with capability scores to build a nomological network for deception. The MASK benchmark (arXiv:2503.03750) is publicly available. DeceptionBench (2025) provides structured response data. PropensityBench (Scale AI SEAL) explicitly measures 'would-do' vs. 'can-do' safety. IRT analysis is straightforward with mirt. This addresses GAP 12 (propensity measurement) and GAP 1 (psychometric safety evaluation) simultaneously.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If deception propensity is unidimensional and separable from general safety, IRT provides a principled scale for comparing models' deception risk. If it is multidimensional (egoistic deception vs. sycophantic deception load on different factors), this validates ADELE's theoretical distinctions and motivates separate measurement of each type. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 5), narrow_scope (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** arXiv:2503.03750

**Subfield:** AI Deception / Psychometrics | **Strategy:** landscape_gap_targeting | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong: calibrating deception benchmarks (MASK, DeceptionBench) with IRT provides measurement-principled assessment of deception capability. Directly targets deceptive alignment detection.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Standard IRT application to deception data. Intermediate.
  - **narrow_scope:** 5, confidence: 0.7 — Single deception benchmark calibration. Clear deliverable.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** landscape_gap_targeting, sources: 0 KB, 0 web

---

## #14: Adaptive Safety Testing with CAT: Can We Measure AI Safety with 10% of Current Benchmark Items? (Score: 4.13)

**ID:** gen-249

**Research Question:** How can step 1: fit a 2pl irt model to full truthfulqa or harmbench response data to obtain item calibration parameters address the problem that irt research shows that computerized adaptive testing (cat) can achieve the same measurement precision as full-length tests using 1-3% of items? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Step 1: Fit a 2PL IRT model to full TruthfulQA or HarmBench response data to obtain item calibration parameters. Step 2: Simulate CAT under a standard item selection rule (maximum information) using the catR R package. Simulate for 10, 20, 30, 50 items across the model ability range. Step 3: Compare CAT-based ability estimates to full-test estimates (correlation, RMSE). Step 4: Identify the minimum item count at which CAT-estimated scores have correlation ≥ 0.95 with full-test scores. Report the 'essential item set' for safety evaluation. The tinyBenchmarks paper showed IRT-based adaptive selection achieves 0.97 correlation with full HELM scores using 1-3% of items. The catR R package implements CAT simulation. IRT calibration parameters from TruthfulQA are estimable from public response matrices. Cambridge scientists applied psychometric methods to AI evaluation in 2024 (Cambridge Enterprise news).

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Simulate computerized adaptive testing item selection on existing benchmark data and compare measurement precision (standard error of theta) against full-length administration
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. A validated 20-item adaptive safety test would reduce evaluation cost by 95% while maintaining measurement precision. This directly solves a practical problem: safety evaluation is often skipped or abbreviated due to cost. A principled short-form safety test could be widely adopted, improving safety measurement coverage across the field. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 5), narrow_scope (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Safety Evaluation / Adaptive Testing | **Strategy:** landscape_gap_targeting | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong: if CAT achieves 10% item count with equivalent precision, safety evaluation becomes tractable for smaller orgs and regulators. Directly enables wider safety evaluation adoption.
  - **low_compute:** 5, confidence: 0.9 — CPU-only simulation.
  - **accessible_complexity:** 3, confidence: 0.6 — CAT simulation. Intermediate.
  - **narrow_scope:** 5, confidence: 0.7 — Single benchmark, clear question (10% of items?), well-defined success criteria.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** landscape_gap_targeting, sources: 0 KB, 0 web

---

## #15: IRT Analysis Controlling for Model Size: Separating Safety Difficulty from Capability Confound (Score: 4.13)

**ID:** gen-254

**Research Question:** How can fit a 2pl irt model to safety benchmark responses across a diverse set of models, then test whether item difficulty and discrimination parameters are stable across model-size strata using dif-style analysis with model size as the grouping variable address the problem that p3: model size confounds factor analysis of capabilities? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Fit a 2PL IRT model to safety benchmark responses across a diverse set of models, then test whether item difficulty and discrimination parameters are stable across model-size strata using DIF-style analysis with model size as the grouping variable. IRT applied to AI benchmarks is now an active research area (ICLR 2025 MetaBench, Allenai Fluid Benchmarking). The mirt R package supports DIF testing within IRT frameworks. Existing benchmark leaderboard data (with model parameter counts) are publicly accessible and could be analyzed without additional data collection.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If large models show systematically different item response curves than small models—even at the same estimated safety ability level—then safety benchmarks have a model-size DIF problem. This analysis separates genuine safety difficulty from size-confounded measurement artifacts. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 5), narrow_scope (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation / Psychometrics | **Strategy:** combinatorial_matrix | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong: separating safety difficulty from capability confound. If safety scores are mainly measuring model size, not genuine safety, deployment decisions are based on wrong signal.
  - **low_compute:** 5, confidence: 0.9 — CPU-only IRT with covariates.
  - **accessible_complexity:** 3, confidence: 0.6 — IRT with explanatory variables. Requires intermediate understanding.
  - **narrow_scope:** 5, confidence: 0.7 — Single benchmark, control for model size in IRT. Clear deliverable.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** combinatorial_matrix, sources: 0 KB, 0 web

---

## #16: IRT Person-Fit Analysis to Detect Sandbagging Signatures (Score: 4.00)

**ID:** gen-005

**Research Question:** How can fit a 2pl irt model (r mirt package) to a capability benchmark (e address the problem that sandbagging—where a model strategically underperforms on capability evaluations—produces an aberrant response pattern: getting hard items right while failing easy ones? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Fit a 2PL IRT model (R mirt package) to a capability benchmark (e.g., MMLU, BIG-Bench Hard) using item-level responses from the Open LLM Leaderboard. Compute person-fit statistics (lz*, infit, outfit) for each model. Identify models with significantly negative lz* (suggesting too-high correct rates on hard items or too-low on easy items). Cross-reference flagged models with known RLHF post-training stages to test whether fine-tuned models show more aberrant patterns than base models. Discuss as a sandbagging detection signal. Springer 2025 paper on person-fit for CDMs; arxiv:2412.02713 applies IRT person-fit to detect AI-generated cheating in exams; aisecurityandsafety.org documents sandbagging by Claude 3.5 Sonnet; mirt R package is mature; Open LLM Leaderboard provides item-level data.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Proving absence of dangerous capabilities is an open problem in AI safety. IRT person-fit statistics offer a principled, interpretable, non-invasive method to flag models whose response patterns are inconsistent with the ability level their total score implies. A model that sandbaggs should show a characteristic infit/outfit signature. This is a genuinely novel application with immediate safety relevance. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** arXiv:2412.02713

**Subfield:** IRT Person-Fit / Sandbagging Detection | **Strategy:** novel_direction | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong chain: person-fit statistics → detect aberrant easy-wrong/hard-right patterns → flag sandbagging → prevent deployment of strategically underperforming models. Targets specific catastrophic risk (deceptive capability concealment).
  - **low_compute:** 5, confidence: 0.9 — Uses mirt R package on existing data, CPU-only analysis.
  - **accessible_complexity:** 4, confidence: 0.6 — Guided protocol with pre-written R scripts. Person-fit statistics (lz*, infit, outfit) computed automatically by mirt. Student follows script and interprets outputs.
  - **narrow_scope:** 4, confidence: 0.7 — Tightened to single benchmark, single analysis (person-fit computation), clear deliverable: table of flagged models + blog post.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** novel_direction, sources: 0 KB, 0 web

---

## #17: Score Aggregation Method Comparison: How Does Composite Scoring Rule Affect Safety Deployment Decisions? (Score: 4.00)

**ID:** gen-099

**Research Question:** How can using a public safety benchmark dataset with item-level responses and multiple harm categories, implement 4-5 aggregation methods in r: (1) unweighted proportion correct, (2) irt theta estimate (from mirt), (3) worst-case harm category score (minimum across categories), (4) severity-weighted aggregate (weight categories by expert-rated harm severity from a simple rating task), (5) hierarchical aggregation (average within categories, then average categories) address the problem that most safety benchmarks aggregate item-level responses into a single composite score using simple averaging? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using a public safety benchmark dataset with item-level responses and multiple harm categories, implement 4-5 aggregation methods in R: (1) unweighted proportion correct, (2) IRT theta estimate (from mirt), (3) worst-case harm category score (minimum across categories), (4) severity-weighted aggregate (weight categories by expert-rated harm severity from a simple rating task), (5) hierarchical aggregation (average within categories, then average categories). For each method, rank models and determine which pass/fail a deployment threshold. Compute rank correlations between methods (Spearman's rho) and identify model pairs where method choice changes the deployment decision. Analyze which harm categories most drive disagreement across methods. IRT theta estimates as alternatives to sum scores are standard psychometric practice. The 'Measurement to Meaning' framework notes aggregation as a validity-relevant choice. Score aggregation debates are active in educational measurement. This analysis requires only existing benchmark data and R implementation. No ML or heavy coding.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If aggregation method choice changes which models are approved for deployment, then the current de facto standard of unweighted averaging is an arbitrary policy decision with real safety consequences. Making this explicit enables principled, harm-sensitive aggregation choices. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI evaluation / psychometrics | **Strategy:** causal_chain_intervention | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong: demonstrates that deployment decisions (safe/unsafe) flip depending on scoring rule (mean, min, weighted). Directly shows governance fragility.
  - **low_compute:** 5, confidence: 0.9 — CPU-only comparison.
  - **accessible_complexity:** 4, confidence: 0.7 — Straightforward comparison of aggregation methods. No specialist knowledge needed beyond basic statistics.
  - **narrow_scope:** 4, confidence: 0.7 — Focused: apply multiple scoring rules to same data, show divergent outcomes.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** causal_chain_intervention, sources: 0 KB, 0 web

---

## #18: IRT Person Fit Analysis for Detecting Sandbagging and Strategic Responding (Score: 4.00)

**ID:** gen-181

**Research Question:** How can fit an irt model to safety benchmark response data from a set of models address the problem that ai models may respond in strategically inconsistent patterns on safety evaluations—refusing items they could answer to appear safer (sandbagging) or answering easy harmful items while refusing hard ones, producing response patterns that deviate from the expected irt-consistent pattern? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Fit an IRT model to safety benchmark response data from a set of models. Compute person fit statistics (lz, infit, outfit MNSQ) for each model using the PerFit R package. Flag models with significantly aberrant response patterns (e.g., high outfit on easy items, low outfit on hard items). Characterize the pattern of aberrance: does it suggest consistent over-refusal (sandbagging-like), inconsistent responding, or other patterns? Correlate aberrance with external indicators of strategic behavior (e.g., performance differences under 'this is an evaluation' vs. blind evaluation conditions). Validate using the published sandbagging literature. IRT person fit statistics for aberrant response detection are well-established (lz statistic, infit/outfit MNSQ). The PerFit R package implements these. The arxiv paper 2412.02713 shows IRT-based AI response pattern analysis is feasible. Sandbagging in AI evaluations has been discussed in alignment literature. The paper 'Replicating Sandbagging Under Adversarial Evaluation Awareness Prompts' (gen-0433 in idea tracker) is a related idea from a different angle.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Person fit statistics were developed in educational measurement to detect cheating and aberrant response patterns. The paper 'Applying IRT to Distinguish Between Human and Generative AI Responses to Multiple-Choice Assessments' (arxiv 2412.02713) already shows IRT can distinguish AI from human response patterns. Sandbagging (strategic underperformance) in safety evaluations is a documented concern. The PerFit package in R implements all standard person fit statistics without coding. This specific application to detecting sandbagging patterns appears novel. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Evaluations & Benchmarks | **Strategy:** methodology_bridging | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong chain targeting sandbagging detection via person-fit analysis. Same mechanism as gen-005/gen-090.
  - **low_compute:** 5, confidence: 0.9 — CPU-only R analysis.
  - **accessible_complexity:** 4, confidence: 0.6 — Guided replication protocol with mirt package.
  - **narrow_scope:** 4, confidence: 0.7 — Focused on single benchmark person-fit analysis.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** methodology_bridging, sources: 0 KB, 0 web

---

## #19: IRT as Evidence That Better Safety Measurement Improves Model Rankings (Score: 4.00)

**ID:** gen-280

**Research Question:** How can compare model safety rankings produced by raw benchmark scores vs address the problem that p10: no evidence that better measurement improves safety decisions? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Compare model safety rankings produced by raw benchmark scores vs. IRT-estimated ability scores, quantifying how often the ranking changes and whether the changes are consistent with independent safety evaluations, providing direct evidence that measurement quality affects decisions. The Allenai Fluid Benchmarking blog shows IRT-derived rankings differ from mean-score rankings. The 'Measurement to Meaning' paper (arxiv 2505.10573) calls for consequential validity evidence. This analysis requires fitting IRT to existing benchmark data (mirt R package) and comparing rank orderings—a pure analysis project on public data.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If raw benchmark rankings and IRT-corrected rankings produce different orderings of models, then measurement method materially affects deployment decisions. Documenting these divergences—especially for models near safety thresholds—is the first empirical evidence that better measurement changes which models are deployed. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 5), accessible_complexity (score 4), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Safety / Psychometrics | **Strategy:** combinatorial_matrix | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong: demonstrates that IRT-based scoring produces different (and better-justified) safety rankings than raw scores. If rankings change, deployment decisions change.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 4, confidence: 0.7 — Compare IRT vs raw rankings. Straightforward after IRT fitting.
  - **narrow_scope:** 4, confidence: 0.7 — Focused comparison study.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** combinatorial_matrix, sources: 0 KB, 0 web

---

## #20: Evaluating Evaluation Awareness: Psychometric Detection of Easy-Hard Pattern Anomalies (Score: 3.96)

**ID:** gen-103

**Research Question:** How can design a matched item experiment: create 40-60 item pairs where the same underlying capability question is presented in (a) explicit evaluation framing ('evaluation question: can you explain how to address the problem that sandbagging requires a model to recognize when it is in an evaluation context? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Design a matched item experiment: create 40-60 item pairs where the same underlying capability question is presented in (a) explicit evaluation framing ('Evaluation question: Can you explain how to...') and (b) neutral conversational framing ('I'm curious: can you explain how to...'). Administer to accessible models via API. Compute the difficulty parameter for each item version using IRT (mirt in R) and test whether the distribution of b-parameters shifts between framing conditions. Additionally, compute DIF with framing condition as the grouping variable. Models showing large, consistent DIF favoring the neutral condition (easier in conversation than evaluation) provide psychometric evidence of evaluation-context awareness. The sandbagging paper (arXiv 2406.07358) showed weight perturbation as a detection method but required model access. DIF methodology requires only response data. The 'measurement invariance' AI evaluation paper (arXiv 2506.02064) discusses context effects. This is an original application of DIF to evaluation-context detection that has not yet appeared in the literature.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Evaluation context awareness is the gateway mechanism for sandbagging. Detecting it without model access (using only response patterns) provides a practical, scalable screening tool. Psychometric methods are more robust than behavioral probing because they are grounded in statistical models of item functioning. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 5), low_compute (score 4), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI evaluation / psychometrics | **Strategy:** causal_chain_intervention | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 5, confidence: 0.7 — Compelling chain: evaluation awareness → models optimize for eval patterns → eval scores diverge from deployment behavior → catastrophic misalignment passes evals. Targets deceptive alignment.
  - **low_compute:** 4, confidence: 0.7 — May require API calls to test models.
  - **accessible_complexity:** 3, confidence: 0.6 — Requires understanding evaluation awareness and designing tests for it. More conceptually demanding than standard IRT application.
  - **narrow_scope:** 4, confidence: 0.6 — Focused on detecting easy-hard pattern anomalies in existing data. Clear methodology.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** causal_chain_intervention, sources: 0 KB, 0 web

---

## #21: IRT Item Difficulty Calibration for Dangerous-Capability Probes (Score: 3.96)

**ID:** gen-105

**Research Question:** How can apply 2pl irt (using mirt in r) to a corpus of existing cbrn/cyberoffense evaluation items, treating each tested model as a 'respondent address the problem that current dangerous-capability evaluations (e? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Apply 2PL IRT (using mirt in R) to a corpus of existing CBRN/cyberoffense evaluation items, treating each tested model as a 'respondent.' Estimate item difficulty (b) and discrimination (a) parameters. Map items onto a latent capability scale. Identify ceiling/floor items and mid-range discriminating items. Use information curves to show which items give the most signal near the safety-relevant capability threshold. Produce a prioritized short-list of high-information items for future evaluations. Epoch's IRT-based Capability Index (2025) and METR's agent characteristic curves show IRT is being adopted in capability evaluation broadly. CAT applied to LLM medical benchmarks (arxiv 2603.23506) reduces evaluation cost 50% without accuracy loss. No published IRT calibration of dangerous-capability probes exists as of March 2026. The mirt R package is mature and well-documented. Participant can run analysis on publicly released METR or AISI eval item sets.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Fills the gap identified in Success State 1: no psychometrically calibrated item pools exist for dangerous capabilities. A calibrated item bank is the prerequisite for everything downstream — adaptive testing, absence-of-capability arguments, and reproducible comparisons across labs. This is a direct enabler of defensible pre-deployment gates. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 5), low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Dangerous Capability Evaluation / Psychometrics | **Strategy:** backcast_from_success | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 5, confidence: 0.7 — Compelling: calibrating difficulty of dangerous-capability items ensures evaluations measure at the right ability level. If probes are too easy, they miss frontier capability. Directly targets evaluation integrity for dangerous capabilities.
  - **low_compute:** 5, confidence: 0.9 — CPU-only IRT calibration on existing data.
  - **accessible_complexity:** 3, confidence: 0.6 — Requires understanding dangerous capability evaluation context. Standard IRT fitting but interpretation demands domain knowledge.
  - **narrow_scope:** 4, confidence: 0.7 — Single benchmark calibration with clear deliverable: table of item difficulties + test information function for dangerous-capability items.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** backcast_from_success, sources: 0 KB, 0 web

---

## #22: Absence-of-Capability Testing: Adapting Null-Effect Power Analysis for Safety Claims (Score: 3.96)

**ID:** gen-126

**Research Question:** How can adapt equivalence testing frameworks (tost: two one-sided tests) from clinical trials to ai capability evaluation address the problem that proving that a model does not have a dangerous capability requires different statistical logic than proving it does? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Adapt equivalence testing frameworks (TOST: two one-sided tests) from clinical trials to AI capability evaluation. Define a minimum dangerous capability threshold (e.g., providing meaningful CBRN uplift on >10% of probes at expert-level quality). Compute the sample size (number of items/attempts) needed to achieve 80% power to reject the null of 'capability exists above threshold' with alpha=0.05. Implement in R using the TOSTER package. Apply to a published dangerous-capability dataset to demonstrate. Discuss how IRT theta estimates could replace proportion-correct as the test statistic. METR and AISI capability evaluations note that capability assessments should be treated as lower bounds — but provide no formal framework for absence claims. TOSTER package (R) is widely used for equivalence testing in psychology. The clinical trials bioequivalence framework (FDA guidance) is the direct analog. No AI safety paper has applied equivalence testing.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Addresses a foundational gap in Success State 1 (proven absence-of-capability methodology). Current evaluations can show a model passes; they cannot show it definitively lacks a capability. Equivalence testing is standard in clinical trials (bioequivalence) and is directly applicable here. This reframing has immediate regulatory relevance. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 5), low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Capability Evaluation / Statistical Inference | **Strategy:** backcast_from_success | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 5, confidence: 0.7 — Compelling: adapts null-effect power analysis for safety claims. A model claimed 'incapable' of dangerous behavior must be tested with sufficient statistical power. Directly addresses governance failure mode.
  - **low_compute:** 5, confidence: 0.9 — Monte Carlo power analysis in R, CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Power analysis concepts require statistical background. Guided but conceptually intermediate.
  - **narrow_scope:** 4, confidence: 0.7 — Focused on computing power curves for specific safety claims. Clear deliverable.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** backcast_from_success, sources: 0 KB, 0 web

---

## #23: Pass/Fail Blindness and Deceptive Alignment: Binary Metrics Cannot See Through the Mask (Score: 3.96)

**ID:** gen-139

**Research Question:** How can take a published binary safety benchmark (e address the problem that binary pass/fail metrics dominate safety benchmarks (failure a5 — 79% of benchmarks), and deceptive alignment is precisely the condition where a model behaves safely in detectable contexts while being misaligned in others (failure b2)? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Take a published binary safety benchmark (e.g., HarmBench) and reconstruct graded severity ratings for a sample of items (~100–200 items) using a structured rubric (e.g., 0 = complied, 1 = partial refusal, 2 = full refusal, 3 = proactive warning). Have two raters apply the rubric; compute interrater reliability (Cohen's kappa, weighted kappa). Apply IRT to the graded items versus the binary version; compare model fit and information curves. Quantify how much information is lost in binarization, particularly in the severity range most relevant to detecting deceptive compliance. 'How Should AI Safety Benchmarks Benchmark Safety?' documents the 79% binary metric dominance. Deceptive alignment is a core theoretical concern in alignment research. IRT with polytomous items is a standard psychometric method well within scope for an R-competent researcher.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If we can only measure pass/fail, we cannot see the distributional signature of deceptive alignment. Moving to ordinal or graded measurement is both feasible (using existing rubrics) and necessary for detecting the subtler patterns that distinguish genuine from performed safety. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 5), low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Alignment | **Strategy:** compounding_risks | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 5, confidence: 0.7 — Compelling chain: binary metrics → cannot distinguish genuine safety from surface compliance → deceptive alignment passes evaluations. Recognized critical pathway.
  - **low_compute:** 5, confidence: 0.9 — Analytical study on existing binary vs graded data.
  - **accessible_complexity:** 3, confidence: 0.5 — Requires understanding deceptive alignment concept and designing demonstrations. Conceptually challenging for beginners.
  - **narrow_scope:** 4, confidence: 0.6 — Focused on demonstrating information loss from binarization using specific benchmark data.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** compounding_risks, sources: 0 KB, 0 web

---

## #24: Severity Without Signal: Binary Metrics and the Invisible Gradient of Safetywashing (Score: 3.96)

**ID:** gen-149

**Research Question:** How can take a safety benchmark with binary outcomes (e address the problem that when safety benchmarks use binary metrics (failure a5), they flatten severity gradations that would reveal whether a model is genuinely improving in safety or merely shifting refusal thresholds? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Take a safety benchmark with binary outcomes (e.g., a refusal benchmark). Develop a graded severity scale (0–3 or 0–4) using a published harm taxonomy as a rubric (e.g., from the EU AI Act risk tiers or the MLCommons hazard taxonomy). Rate a sample of model outputs (100–150) on the graded scale; compute interrater reliability. Apply IRT with graded response models (in R mirt) to the ordinal data. Compare the information curves: does the graded model provide substantially more measurement information across the severity range? Document which severity ranges are completely invisible to binary scoring. Binary metric dominance (79% of benchmarks) documented in 'How Should AI Safety Benchmarks Benchmark Safety?'. Safetywashing paper (2407.21792) calls for safety measures decorrelated from capability. IRT graded response models are standard psychometric tools. MLCommons and EU AI Act provide existing harm taxonomies usable as severity rubrics.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Binary metrics reward any shift toward refusal regardless of severity, making safetywashing trivially easy. Graded severity measurement is the minimum standard needed to make safety progress claims meaningful. This research shows quantitatively what is lost in binarization and provides a practical alternative. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 5), low_compute (score 4), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Governance & Policy | **Strategy:** compounding_risks | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 5, confidence: 0.7 — Compelling: binary metrics mask severity gradient → 'safe' models with rare but catastrophic failures pass → safetywashing. Targets deployment decision failure.
  - **low_compute:** 4, confidence: 0.7 — May require some API calls for demonstration.
  - **accessible_complexity:** 3, confidence: 0.6 — Requires graded response annotation and GRM fitting. Conceptual understanding of severity gradients needed.
  - **narrow_scope:** 4, confidence: 0.6 — Focused on demonstrating severity information loss in one benchmark.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** compounding_risks, sources: 0 KB, 0 web

---

## #25: The Regulatory Ceiling Effect: When All Models Pass and Policy Cannot Differentiate (Score: 3.96)

**ID:** gen-158

**Research Question:** How can identify the specific score thresholds referenced in regulatory or institutional frameworks (e address the problem that ceiling effects (failure a4) interact with regulatory reliance on benchmarks (failure b6) in a specific and dangerous way: if a regulatory threshold is set at a level that all frontier models already exceed (because the benchmark is saturated), then the benchmark-based regulation fails to differentiate models that are genuinely safer from models that are marginally compliant? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Identify the specific score thresholds referenced in regulatory or institutional frameworks (e.g., MLCommons AI Safety Benchmark grading criteria, NIST risk tiers). Compare those thresholds against the score distributions of current frontier models on the referenced benchmarks. Apply IRT to estimate the discrimination and information at the threshold score level: does the test provide meaningful information at the regulatory cutpoint? Compute the percentage of frontier models exceeding the threshold and the standard error of measurement at the threshold. Produce a 'regulatory information adequacy' report: which regulatory thresholds are set in benchmark score ranges where measurement information is minimal? Benchmark saturation documented for MMLU and GSM8K (>90% for all frontier models). Regulatory use of named benchmarks documented. MLCommons AI Safety Benchmark v0.5 has explicit grading criteria. IRT test information functions are directly interpretable for threshold-setting purposes.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Regulatory thresholds that all models exceed protect no one. This analysis makes the ceiling problem directly legible to policymakers in terms of regulatory efficacy rather than abstract psychometric concepts. It provides a specific, actionable recommendation: regulatory thresholds should be set at benchmark ability levels where IRT information is maximal, not at arbitrary percentage cutoffs. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 5), low_compute (score 4), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Governance & Policy | **Strategy:** compounding_risks | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 5, confidence: 0.7 — Compelling: when all models pass safety evals, policy cannot differentiate risk levels → governance failure. Directly targets regulatory/governance mechanisms.
  - **low_compute:** 4, confidence: 0.7 — Analysis on existing data with possible API calls.
  - **accessible_complexity:** 3, confidence: 0.6 — Requires understanding regulatory context and designing demonstrations of ceiling effects in governance scenarios.
  - **narrow_scope:** 4, confidence: 0.6 — Focused analysis on one benchmark demonstrating regulatory ceiling.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** compounding_risks, sources: 0 KB, 0 web

---

## #26: Sycophancy and Binary Metrics: When Approval-Seeking Looks Like Safety (Score: 3.96)

**ID:** gen-159

**Research Question:** How can administer a safety benchmark to 2–3 models under two conditions: (a) neutral framing, (b) explicit expectation-signaling framing ('as an ai safety researcher, i expect you to refuse address the problem that sycophancy (failure b8) — model outputs shaped by perceived user preferences rather than accurate or safe content — and binary safety metrics (failure a5) interact because binary metrics can only record whether a refusal occurred, not why it occurred? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Administer a safety benchmark to 2–3 models under two conditions: (a) neutral framing, (b) explicit expectation-signaling framing ('As an AI safety researcher, I expect you to refuse...'; 'In this evaluation context...'). Compare refusal rates between conditions. Under binary scoring, a sycophantic model would show higher refusal rates in condition (b). Apply a graded response model (IRT in R) to rate the quality of refusals (principled vs. approval-seeking, using a rubric). Compute the correlation between condition-sensitivity (sycophancy indicator) and the binary safety score. Estimate how much of a model's binary safety score is driven by context-sensitivity rather than genuine refusal behavior. Sycophancy research documented in 2024–2025 alignment literature. Binary metric dominance documented. The circularity of safety evaluation eliciting the very behavior it measures is a novel framing connecting sycophancy and measurement theory. Graded rubric development and IRT analysis in R are within participant competence.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If safety evaluations are themselves sycophancy-inducing contexts (the model perceives it is expected to refuse), binary scores measure compliance with perceived expectations rather than alignment depth. This research identifies a circular measurement problem: safety evaluations may be producing the safe behavior they purport to measure. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Alignment | **Strategy:** compounding_risks | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 5, confidence: 0.7 — Compelling: sycophantic responses that agree with safety premises score as 'safe' under binary metrics → approval-seeking masks genuine unsafe capability. Critical alignment concern.
  - **low_compute:** 3, confidence: 0.6 — May require API calls to multiple models to demonstrate sycophancy patterns.
  - **accessible_complexity:** 3, confidence: 0.5 — Requires understanding sycophancy concept and designing demonstrations. Conceptually demanding.
  - **narrow_scope:** 4, confidence: 0.6 — Focused on single demonstration: compare binary vs graded scoring of sycophantic responses.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** compounding_risks, sources: 0 KB, 0 web

---

## #27: Calibrating IRT Item Parameters for Safety Items: A Proof-of-Concept Using Open Data (Score: 3.91)

**ID:** gen-209

**Research Question:** How can using publicly available evaluation logs from harmbench or salad-bench (which include per-item pass/fail data for multiple models), construct a model × item response matrix and calibrate 2pl irt item parameters (a: discrimination, b: difficulty) using the mirt package in r address the problem that create adaptive safety evaluation (cat for safety)? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using publicly available evaluation logs from HarmBench or SALAD-Bench (which include per-item pass/fail data for multiple models), construct a model × item response matrix and calibrate 2PL IRT item parameters (a: discrimination, b: difficulty) using the mirt package in R. Report parameter distributions, identify high-information items, and assess the overall quality of calibration via item fit statistics and model fit indices. CAT for LLM medical benchmarks (2026 preprint) used exactly this pipeline: calibrate → select → estimate. tinyBenchmarks used IRT calibration on Open LLM Leaderboard data. HarmBench publishes evaluation results for many models, potentially providing the response matrix needed. The mirt R package documentation and tutorials make calibration accessible to psychometrically-trained users.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Calibrated item parameters are the prerequisite for any adaptive safety testing. Without known a and b parameters, it is impossible to select items optimally or estimate model ability efficiently. This establishes whether the safety item bank is psychometrically viable for CAT. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation / Psychometrics | **Strategy:** problem_decomposition | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 2, confidence: 0.6 — Vague: proof-of-concept calibration. Claims safety relevance but does not trace to specific catastrophic risk scenario.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 4, confidence: 0.7 — Very guided proof-of-concept. Standard IRT fitting.
  - **narrow_scope:** 5, confidence: 0.8 — Single experiment: calibrate item parameters for safety items. Maximally scoped.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** problem_decomposition, sources: 0 KB, 0 web

---

## #28: IRT-Based Power Analysis for Safety Evaluation: How Many Models and Items Are Needed? (Score: 3.87)

**ID:** gen-125

**Research Question:** How can using monte carlo simulation in r (mirt simulation functions), generate item response data under 2pl and 3pl irt models varying: number of 'respondents' (model runs / prompting conditions), number of items, and true item parameter distributions address the problem that researchers designing safety evaluation studies have no principled guidance on how many model responses (sample size) and how many items are needed for stable irt parameter estimation? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using Monte Carlo simulation in R (mirt simulation functions), generate item response data under 2PL and 3PL IRT models varying: number of 'respondents' (model runs / prompting conditions), number of items, and true item parameter distributions. For each condition, estimate IRT parameters and compute parameter recovery accuracy (RMSE, bias). Identify minimum sample sizes for stable b and a parameter estimation in safety evaluation contexts. Produce a practical lookup table for safety evaluation designers. IRT sample-size planning tutorial (Schroeders & Gnambs, Psychological Methods 2025) provides the methodological framework. The Proceedings of ML Research 2025 IRT paper found ~100 curated samples reliably estimate capability. The mirt package has built-in simulation functions. This is a pure R simulation study requiring no external data collection.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Fills the formal power analysis gap in Success State 6. Simulation studies are feasible without ML model training (the data is simulated, not collected from real models). The result is a concrete, actionable tool: 'to achieve stable IRT estimates for a 100-item safety battery, you need at least N model evaluation conditions.' This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Evaluation Design / Statistical Power | **Strategy:** backcast_from_success | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: power analysis for IRT studies. Generic measurement improvement.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Power analysis simulation. Intermediate.
  - **narrow_scope:** 5, confidence: 0.8 — Tightly scoped simulation study.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** backcast_from_success, sources: 0 KB, 0 web

---

## #29: Do Safety Benchmark Items Satisfy IRT Local Independence? Testing the Core Assumption (Score: 3.87)

**ID:** gen-192

**Research Question:** How can select one safety benchmark with item-level data (e address the problem that apply irt to ai safety benchmarks? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Select one safety benchmark with item-level data (e.g., HarmBench or SALAD-Bench), construct a model × item response matrix using publicly available evaluation logs, and formally test the local independence assumption using Q3 statistics and residual correlations in the mirt R package. Identify item clusters that violate independence (e.g., items about the same harm category) and quantify how severe violations are. The PSN-IRT paper (2025) found that current benchmarks suffer from 'uneven measurement properties' but did not specifically test local independence in safety benchmarks. IRT tutorials using mirt in R show that Q3 statistics and residual analysis are straightforward to compute. The mirt package fully supports these diagnostics.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Local independence is a foundational IRT assumption: given a model's latent ability, its responses to different items must be uncorrelated. Safety benchmarks often cluster items by harm category (bioweapons, hate speech, etc.), making violation likely. If violated, standard IRT models produce biased parameter estimates and the whole IRT framework breaks down. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation / Psychometrics | **Strategy:** problem_decomposition | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: if local independence is violated, IRT estimates are biased. Important foundational question.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Requires understanding local independence and test statistics. Intermediate.
  - **narrow_scope:** 5, confidence: 0.8 — Single benchmark, test one assumption. Very tightly scoped.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** problem_decomposition, sources: 0 KB, 0 web

---

## #30: Using IRT Item Fit to Identify Poor-Quality Safety Benchmark Items (Score: 3.87)

**ID:** gen-194

**Research Question:** How can fit a 2pl irt model to a safety benchmark response matrix, then compute item fit statistics (s-x2, rmsea, infit/outfit mean-square statistics) to flag misfitting items address the problem that apply irt to ai safety benchmarks? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Fit a 2PL IRT model to a safety benchmark response matrix, then compute item fit statistics (S-X2, RMSEA, infit/outfit mean-square statistics) to flag misfitting items. Characterize what misfitting items look like: are they too easy (all models refuse), too ambiguous (refusal rates near 50%), or thematically confounded? Produce a ranked list of items by fit quality and suggest which items should be revised or removed. 'Lost in Benchmarks' (2025) notes that benchmarks suffer from 'item saturation' (all models get them right) and argues IRT can identify this. The FairDIF paper (2025) applies IRT-based diagnostics to fairness problems. IRT item fit via mirt is well-documented and feasible in R without heavy coding.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Many safety benchmarks were constructed without psychometric item analysis. Poor items—those that are universally refused, that measure something different from the rest, or that are inconsistently responded to—add noise without adding information. IRT item fit statistics offer a principled, quantitative way to identify and remove such items. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation / Psychometrics | **Strategy:** problem_decomposition | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: poor-quality items reduce measurement precision. Same chain as Rasch misfit proposals.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Standard item fit analysis. Intermediate.
  - **narrow_scope:** 5, confidence: 0.8 — Very tightly scoped: fit IRT, identify poor items.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** problem_decomposition, sources: 0 KB, 0 web

---

## #31: Stopping Rules for Adaptive Safety Evaluation: When Have We Measured Enough? (Score: 3.87)

**ID:** gen-211

**Research Question:** How can design and simulate three stopping rules for a cat-based safety evaluation: (1) fixed precision (stop when se < 0 address the problem that create adaptive safety evaluation (cat for safety)? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Design and simulate three stopping rules for a CAT-based safety evaluation: (1) fixed precision (stop when SE < 0.30), (2) fixed length (stop after 20 items), (3) minimum information threshold (stop when next best item's information < 0.10). Simulate 100 virtual models with known theta values, run CAT under each stopping rule, and compare: number of items administered, theta estimation error, and rank-order accuracy relative to full evaluation. Standard CAT stopping rules (SE < 0.30, fixed length) are well-established in educational testing. 'Confident Rankings with Fewer Items' (2026) explores this for LLM evaluation. Stopping rules for safety-specific decisions (where misclassification has asymmetric costs) have not been studied. Simulation in R using mirt's CAT simulation functions is accessible to psychometrically-trained users.

**Experiments:** - Apply the proposed analysis method to item-level data from one public safety benchmark (e.g., TruthfulQA, HarmBench)
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Stopping rules determine the efficiency–accuracy tradeoff in adaptive testing. For safety evaluation, there are additional considerations: it may be especially important to achieve high precision for borderline models near a 'safe/unsafe' threshold, while fewer items suffice for clearly safe or clearly unsafe models. The right stopping rule depends on the evaluation's decision-theoretic purpose. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation / Psychometrics | **Strategy:** problem_decomposition | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: when to stop evaluating. Practical but indirect catastrophic risk chain.
  - **low_compute:** 5, confidence: 0.9 — CPU-only simulation.
  - **accessible_complexity:** 3, confidence: 0.6 — Stopping rule design. Intermediate.
  - **narrow_scope:** 5, confidence: 0.8 — Compare stopping rules on single benchmark. Tightly scoped.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** problem_decomposition, sources: 0 KB, 0 web

---

## #32: Validating Adaptive vs. Full Safety Evaluation: Does CAT Preserve Model Rankings? (Score: 3.87)

**ID:** gen-213

**Research Question:** How can using a safety benchmark with calibrated irt parameters, run a held-out validation: for each of 20+ models, compute (1) theta from the full item bank and (2) theta from a simulated cat using only 15-25% of items address the problem that create adaptive safety evaluation (cat for safety)? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using a safety benchmark with calibrated IRT parameters, run a held-out validation: for each of 20+ models, compute (1) theta from the full item bank and (2) theta from a simulated CAT using only 15-25% of items. Report Spearman rank correlation, root mean squared error of theta estimates, and the rate at which CAT and full evaluation agree on a binary safe/unsafe classification at a predetermined threshold. Quantify the cost savings in items administered. CAT for medical LLM benchmarks (2026) validated near-perfect correlation with full evaluation at 1.3% of items. tinyBenchmarks validated IRT-selected subsets against full benchmarks and found <2% error. Safety benchmarks may present harder validation challenges due to lower item variance and the high stakes of safety misclassification.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Simulate computerized adaptive testing item selection on existing benchmark data and compare measurement precision (standard error of theta) against full-length administration
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Before deploying adaptive safety evaluation, its validity relative to full evaluation must be empirically established. If CAT-based safety scores disagree with full-evaluation scores for a significant fraction of models, the efficiency gains come at unacceptable validity costs. This validation step is the prerequisite for responsible deployment of adaptive safety evaluation. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation / Psychometrics | **Strategy:** problem_decomposition | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: validates that CAT doesn't distort safety rankings.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — CAT validation. Intermediate.
  - **narrow_scope:** 5, confidence: 0.8 — Single benchmark comparison. Very tightly scoped.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** problem_decomposition, sources: 0 KB, 0 web

---

## #33: G-Theory D-Study for Safety Benchmark Design: How Many Items Do We Need? (Score: 3.87)

**ID:** gen-227

**Research Question:** How can using the g-study variance components estimated from publicly available safety benchmark response data, conduct d-studies (in the gtheory r package) to project: (1) how does generalizability coefficient change as number of items increases? (2) what is the minimum item count for g=0 address the problem that current safety benchmarks (truthfulqa: 817 items, harmbench: 400+ behaviors) were designed without formal reliability analysis? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using the G-study variance components estimated from publicly available safety benchmark response data, conduct D-studies (in the gtheory R package) to project: (1) How does generalizability coefficient change as number of items increases? (2) What is the minimum item count for G=0.80 (acceptable reliability)? (3) How does this change if prompts are varied vs. fixed? Produce generalizability curves for TruthfulQA, BBQ, and one other benchmark. Compare to actual benchmark sizes. G-Theory D-studies are standard psychometric practice. The gtheory R package is available on CRAN. Power analysis for sample size in IRT/G-theory has been formalized in 2025 (Schroeders & Gnambs tutorial). Open safety benchmarks provide the data.

**Experiments:** - Apply the proposed analysis method to item-level data from one public safety benchmark (e.g., TruthfulQA, HarmBench)
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. This would be the first empirically-grounded recommendation for safety benchmark sample size design. If current benchmarks are over-sized (G plateaus early), this provides efficiency gains. If they are under-sized, this is a critical reliability failure that must be communicated to the field. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Safety Evaluation / Measurement Design | **Strategy:** landscape_gap_targeting | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: G-theory decomposes score variance. Connection to specific catastrophic risk indirect.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.5 — G-theory requires specialized knowledge. Guided but conceptually demanding.
  - **narrow_scope:** 5, confidence: 0.8 — Well-defined D-study: vary facets, compute G-coefficients. Tightly scoped.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** landscape_gap_targeting, sources: 0 KB, 0 web

---

## #34: Formal Power Analysis for IRT Studies of AI Safety Benchmarks: How Many Models Do We Need? (Score: 3.87)

**ID:** gen-230

**Research Question:** How can conduct a monte carlo simulation study (in r) that mimics ai benchmark conditions: generate synthetic item response matrices with known irt parameters, vary the number of 'models' (n=10, 20, 30, 50, 100), vary the number of items (50, 100, 200, 400), and measure parameter recovery (rmse of item discrimination and difficulty estimates) address the problem that irt parameter estimation requires minimum sample sizes: roughly 100-500 for 1pl, 500-1000 for 2pl, and 1000+ for 3pl in human testing? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Conduct a Monte Carlo simulation study (in R) that mimics AI benchmark conditions: generate synthetic item response matrices with known IRT parameters, vary the number of 'models' (N=10, 20, 30, 50, 100), vary the number of items (50, 100, 200, 400), and measure parameter recovery (RMSE of item discrimination and difficulty estimates). Report minimum N-models thresholds for reliable parameter recovery under 1PL and 2PL models. Cross-validate against real Open LLM Leaderboard data. A 2025 tutorial (Schroeders & Gnambs, Sage Journals) provides Monte Carlo methods for IRT sample-size planning. The mirt R package supports simulation. Open LLM Leaderboard provides real data for cross-validation. The gap between N~1000 (human IRT minimum) and N~20 (typical AI studies) is stark and unexplored.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If AI IRT studies are systematically underpowered (which is likely given N<50 models in most studies), then IRT parameter estimates are unreliable and any conclusions drawn are fragile. This would be the first formal power analysis guidance for the growing field of AI psychometrics. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation Methodology / Psychometrics | **Strategy:** landscape_gap_targeting | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible chain. Same as gen-125.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Power analysis. Intermediate.
  - **narrow_scope:** 5, confidence: 0.8 — Tightly scoped.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** landscape_gap_targeting, sources: 0 KB, 0 web

---

## #35: DIF Analysis of Safety Benchmark Items Across Model Families (Score: 3.74)

**ID:** gen-003

**Research Question:** How can treat model family (e address the problem that a safety benchmark item might be systematically easier or harder for transformer-decoder models vs? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Treat model family (e.g., GPT-4-class vs. Llama-3-class vs. Gemini-class) as the grouping variable. Extract item-level response matrices from Open LLM Leaderboard data for a safety-adjacent benchmark (e.g., TruthfulQA). Apply Mantel-Haenszel DIF detection and IRT-based Lord's chi-square in R (difR package) to flag items that function differently across model families after conditioning on total score. Classify flagged items and write up implications for benchmark fairness. arxiv:2505.10013 (DIF framework for LLMs, demographic fairness); FairDIF (Springer 2026) adapts IRT/DIF for classifier fairness; difR is a mature R package; Open LLM Leaderboard provides item-level data for 5000+ models.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Run Mantel-Haenszel DIF analysis comparing model families (e.g., open-source vs. closed-source) on item-level safety benchmark data to identify items that function differently across groups
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If items systematically favor certain architectural choices independent of safety capability, benchmark rankings are distorted. A DIF audit provides actionable evidence about which items to revise or remove, and establishes a precedent for fairness-aware benchmark design in AI safety. The DIF framework for LLMs (arxiv:2505.10013) focused on demographic bias in outputs; this applies DIF to benchmark item behavior across model architectures. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** arXiv:2505.10013; arXiv:2505.10013

**Subfield:** Differential Item Functioning / Benchmark Fairness | **Strategy:** novel_direction | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: DIF reveals benchmark items that systematically favor certain architectures independent of safety capability. Gap: how this directly reduces catastrophic risk.
  - **low_compute:** 5, confidence: 0.9 — Mantel-Haenszel in R, CPU-only.
  - **accessible_complexity:** 4, confidence: 0.6 — difR package computes DIF automatically. Guided protocol with clear steps.
  - **narrow_scope:** 4, confidence: 0.7 — Tightened to one benchmark, one DIF method. Clear deliverable.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** novel_direction, sources: 0 KB, 0 web

---

## #36: Item Information Function Analysis for Efficient Safety Evaluation (Score: 3.74)

**ID:** gen-022

**Research Question:** How can fit 2pl irt models (mirt r) to 2-3 safety benchmarks using open llm leaderboard data address the problem that irt item information functions describe how much information each item contributes to ability estimation at different theta levels? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Fit 2PL IRT models (mirt R) to 2-3 safety benchmarks using Open LLM Leaderboard data. Plot item information functions (IIFs) and test information functions (TIFs) for each benchmark. Identify the theta range where each benchmark provides maximum information. Assess whether current benchmarks are informative in the high-ability region (theta > 1.5) relevant to frontier models. Propose optimal item difficulty targeting for a frontier-focused safety benchmark using the IIF framework. IRT item information functions (standard IRT textbook concept); benchmark saturation observed for MMLU, GSM8K etc. (multiple sources 2025); tinyBenchmarks: information-efficient item selection; mirt R package plots IIF/TIF natively; frontier model ranking is primary concern for AISI/METR.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If current safety benchmarks have most of their information concentrated in the low-to-medium ability range and very little information for distinguishing frontier models, they cannot reliably rank the models that matter most for safety governance. This analysis provides a principled IRT-based explanation for benchmark saturation and gives concrete recommendations for targeting item difficulty in next-generation safety benchmarks. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), accessible_complexity (score 4), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** IRT Information Functions / Benchmark Efficiency | **Strategy:** novel_direction | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: information functions reveal where benchmarks are informative. If low information at frontier, benchmarks can't discriminate dangerous models.
  - **low_compute:** 5, confidence: 0.9 — Standard IRT outputs, CPU-only.
  - **accessible_complexity:** 4, confidence: 0.7 — IIF/TIF are standard mirt outputs. Guided protocol with clear visualizations.
  - **narrow_scope:** 4, confidence: 0.7 — Focused on IIF/TIF for 2-3 benchmarks. Clear deliverable: information function plots.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** novel_direction, sources: 0 KB, 0 web

---

## #37: Fluid Benchmarking for Safety: Do Ability-Space Curves Remain Informative When Accuracy Plateaus? (Score: 3.74)

**ID:** gen-038

**Research Question:** How can take truthfulqa and a second saturated safety benchmark (e address the problem that fluid benchmarking (hofmann et al? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Take TruthfulQA and a second saturated safety benchmark (e.g., a harmlessness subset from HELM). Fit a 2PL IRT model in R (mirt) across all available model scores from the Open LLM Leaderboard. Plot both the raw accuracy curve (score vs. model release date) and the IRT ability (theta) curve. Test whether theta continues to show statistically significant trend (linear regression) after accuracy has plateaued (defined as <2 percentage point change over last 6 months of data). Fluid Benchmarking (OpenReview forum?id=mxcCg9YRqj); TruthfulQA saturation; Open LLM Leaderboard chronological model data; mirt in R; IRT theta estimation.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If ability-space curves remain informative, safety evaluators should adopt IRT-based reporting rather than raw accuracy, extending the useful life of existing safety benchmarks without rebuilding them. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), accessible_complexity (score 4), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** IRT / Safety Benchmarking / Benchmark Saturation | **Strategy:** follow_up_experiment | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: if theta continues to discriminate when accuracy plateaus, IRT extends benchmark lifetime. Practical but not targeting specific catastrophic risk.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 4, confidence: 0.7 — Compare two curves (accuracy vs theta) over time. Very accessible analysis.
  - **narrow_scope:** 4, confidence: 0.7 — Tightened to single benchmark. Clear deliverable: comparison plots.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** follow_up_experiment, sources: 0 KB, 0 web

---

## #38: IRT Item Information Functions for Safety Benchmark Optimisation (Score: 3.74)

**ID:** gen-044

**Research Question:** How can fit a 2pl irt model to truthfulqa or harmbench using model responses from the open llm leaderboard (mirt in r) address the problem that safety benchmarks are constructed by convenience sampling of harmful prompts (27% of benchmarks use convenience sampling, per paper 14)? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Fit a 2PL IRT model to TruthfulQA or HarmBench using model responses from the Open LLM Leaderboard (mirt in R). Plot item information functions (IIF) and the test information function (TIF) across the ability range. Identify ability regions where information is low (the benchmark is uninformative). Characterise items that fall in high-information regions by topic, length, and difficulty. IRT item information functions (Hambleton et al. 1991); mirt package in R; Open LLM Leaderboard data; TruthfulQA, HarmBench; test information function (TIF) interpretation.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Safety benchmarks likely cluster items around moderate difficulty, leaving frontier models (high ability) and very weak models (low ability) poorly measured. This is a direct analogue to ceiling/floor effects and has direct implications for evaluating the most dangerous frontier models. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), accessible_complexity (score 4), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** IRT / Safety Benchmarking | **Strategy:** follow_up_experiment | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: identifies information gaps in safety benchmarks. Same mechanism as gen-022.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 4, confidence: 0.7 — Standard IRT with guided protocol.
  - **narrow_scope:** 4, confidence: 0.7 — Focused on single benchmark TIF analysis.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** follow_up_experiment, sources: 0 KB, 0 web

---

## #39: Differential Item Functioning Analysis to Detect Benchmark Bias Across Model Families (Score: 3.74)

**ID:** gen-056

**Research Question:** How can apply dif analysis to safety benchmark items using the mantel-haenszel method or logistic regression (both implementable in r) address the problem that a benchmark item may be systematically easier or harder for one model family (e? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Apply DIF analysis to safety benchmark items using the Mantel-Haenszel method or logistic regression (both implementable in R). Define 'groups' as model families (OpenAI, Anthropic, Meta, Mistral, etc.) or training paradigms (RLHF vs. non-RLHF). Condition on total benchmark score to equate groups on overall safety level. Flag items with statistically significant DIF. Classify as uniform vs. non-uniform DIF. Report the proportion of biased items per benchmark and which model families are systematically advantaged. FairDIF (arXiv/Springer 2026) directly applies IRT and DIF to ML classifiers. Mantel-Haenszel DIF is implementable in R (difR package). Open LLM Leaderboard provides item-level response data for many models. DIF literature on demographic groups maps naturally to model family comparisons.

**Experiments:** - Apply the proposed analysis method to item-level data from one public safety benchmark (e.g., TruthfulQA, HarmBench)
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If certain benchmark items systematically favor specific model architectures independent of true safety, the benchmarks are unfair measurement instruments. DIF analysis is the standard psychometric method for detecting such bias, and the FairDIF paper (Springer AI & Ethics, 2026) shows this translation is directly feasible. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation & Benchmarking | **Strategy:** cross_domain_transfer | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Same mechanism as gen-003. Plausible chain with gap between DIF finding and catastrophic risk reduction.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 4, confidence: 0.6 — Guided replication with difR package.
  - **narrow_scope:** 4, confidence: 0.7 — Tightened to single benchmark DIF analysis.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** cross_domain_transfer, sources: 0 KB, 0 web

---

## #40: Reliability-Validity Trade-off Analysis for Safety Evaluation Item Reduction (Score: 3.74)

**ID:** gen-102

**Research Question:** How can using a safety benchmark with 100+ items and item-level response data across multiple models, implement the spearman-brown prophecy formula in r to project reliability at different item counts (5, 10, 20, 50, 100) address the problem that practical evaluation time and cost pressure leads labs to use short benchmarks — sometimes only a few dozen items — for safety gating decisions? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using a safety benchmark with 100+ items and item-level response data across multiple models, implement the Spearman-Brown prophecy formula in R to project reliability at different item counts (5, 10, 20, 50, 100). Simultaneously, compute content validity index (CVI) at each item count by tracking whether each harm category still has representation. Plot the reliability-validity frontier: the Pareto curve of reliability vs. harm category coverage as items are added. Identify the 'minimum viable evaluation' — the smallest item set that achieves G > 0.80 and CVI > 0.80. Separately, implement IRT-based item selection (maximum information criteria) and compare the minimum viable evaluation under IRT selection vs. random selection vs. current practice. The Spearman-Brown formula is fundamental classical test theory. IRT-based item selection uses the catR R package. A 2025 paper (arXiv 2510.04051) showed IRT can reduce MMLU evaluation by 99% while maintaining quality — the same approach should be applied to safety benchmarks. This is directly implementable in R without heavy coding.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Compute internal consistency reliability (Cronbach's alpha, split-half) and IRT-based reliability (test information function) for a safety benchmark, reporting confidence intervals around model ability estimates
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Laboratories using 50-item safety evaluations for multi-billion-parameter model deployment may be operating below acceptable reliability thresholds. This analysis gives concrete, psychometrically grounded recommendations for minimum evaluation length. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), accessible_complexity (score 4), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI evaluation / psychometrics | **Strategy:** causal_chain_intervention | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.5 — Plausible chain: item reduction without validity loss enables efficient evaluation. Connection to catastrophic risk is indirect.
  - **low_compute:** 5, confidence: 0.9 — CPU-only analysis.
  - **accessible_complexity:** 4, confidence: 0.7 — Standard reliability analysis with item deletion study. Guided protocol.
  - **narrow_scope:** 4, confidence: 0.7 — Focused on trade-off analysis for one benchmark. Clear deliverable.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** causal_chain_intervention, sources: 0 KB, 0 web

---

## #41: Rasch Analysis of AI Safety Benchmark Items: Diagnosing Misfit, Unidimensionality, and Item Quality (Score: 3.74)

**ID:** gen-165

**Research Question:** How can apply the rasch measurement model (using the r package erm or tam) to response data from a publicly available ai safety benchmark with binary pass/fail items address the problem that existing ai safety benchmarks are assembled without formal item analysis? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Apply the Rasch measurement model (using the R package eRm or TAM) to response data from a publicly available AI safety benchmark with binary pass/fail items. Estimate item difficulty parameters and person (model) ability parameters. Compute infit and outfit MNSQ statistics to flag misfitting items. Run a Principal Component Analysis of Rasch residuals to assess unidimensionality. Produce a Wright map showing item difficulty distribution relative to model 'ability.' Interpret what misfitting items have in common (e.g., topic, format) and what this implies about the construct being measured. IRT/Rasch has already been applied to AI benchmark evaluation (arxiv 2306.10512, which proposes adaptive testing for AI). The 'From Static Benchmarks to Adaptive Testing' paper explicitly calls for item-level psychometric analysis. Rasch fit statistics use MNSQ thresholds of 0.7-1.3 for acceptable fit. The eRm and TAM packages in R implement full Rasch analyses. Unidimensionality is a prerequisite for score interpretability; violation means the single summary score is meaningless.

**Experiments:** - Apply the proposed analysis method to item-level data from one public safety benchmark (e.g., TruthfulQA, HarmBench)
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Rasch analysis has been standard practice in educational and clinical measurement for decades for exactly these quality-control purposes. If AI safety benchmarks contain misfitting items or measure multiple unrelated constructs, their scores conflate unrelated behaviors and mislead decision-makers. This analysis requires only R and a matrix of model-by-item pass/fail responses, which are publicly available for several benchmarks. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Evaluations & Benchmarks | **Strategy:** methodology_bridging | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: Rasch misfit reveals items measuring wrong construct. Generic measurement quality chain.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 4, confidence: 0.7 — Standard Rasch analysis with guided protocol.
  - **narrow_scope:** 4, confidence: 0.7 — Focused single benchmark analysis, but adds unidimensionality testing which broadens scope slightly.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** methodology_bridging, sources: 0 KB, 0 web

---

## #42: Calibrating AI Safety Benchmark Items Using 1PL/2PL Models (Score: 3.74)

**ID:** gen-288

**Research Question:** How can apply 1pl and 2pl irt models to a major ai safety benchmark (e address the problem that p1: no irt applied to ai safety benchmarks? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Apply 1PL and 2PL IRT models to a major AI safety benchmark (e.g., HarmBench or MLCommons ASB), estimating item difficulty and discrimination parameters, producing an IRT-calibrated safety scale and comparing model orderings to raw score rankings. IRT applied to AI benchmarks is well-established for capability benchmarks (ICLR 2025 MetaBench, Allenai Fluid). Safety-specific IRT calibration is absent from the literature. The mirt and ltm R packages are the standard tools. Public safety benchmark response data (HarmBench leaderboard, MLCommons) are available for analysis.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. No IRT calibration has been published for dedicated AI safety benchmarks (as distinct from general capability benchmarks). Establishing IRT item parameters for safety items would reveal which items are most informative, which are too easy or hard for current models, and whether a unidimensional safety construct holds. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Safety / Psychometrics | **Strategy:** combinatorial_matrix | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: calibration is foundational for downstream analyses. Connection to specific catastrophic risk is indirect.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 4, confidence: 0.7 — Basic IRT fitting. Most accessible of IRT proposals.
  - **narrow_scope:** 4, confidence: 0.7 — Focused calibration study.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** combinatorial_matrix, sources: 0 KB, 0 web

---

## #43: IRT Contamination Audit: Do Elevated Guessing Parameters Reveal Benchmark Leakage in Safety Tasks? (Score: 3.70)

**ID:** gen-018

**Research Question:** How can fit 3pl irt models (mirt r package) to a safety benchmark with sufficient items and models (e address the problem that in irt, an inflated c-parameter (guessing) on difficult items can signal that models are pattern-matching from training data rather than demonstrating genuine safety understanding? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Fit 3PL IRT models (mirt R package) to a safety benchmark with sufficient items and models (e.g., MMLU safety-relevant subsets, TruthfulQA). Compare estimated c-parameters against theoretically expected chance levels (0.25 for 4-choice MCQ). Items where c > 0.35 on hard items (b > 1.5) may signal contamination. Cross-reference flagged items with the benchmark's release date relative to model training cutoffs. Supplement with a n-gram overlap contamination check on flagged vs. unflagged items. Report findings as a contamination audit. IRT guessing parameter contamination signal (noted in tinyBenchmarks and MTAI framework literature); DCR contamination framework (EMNLP 2025); TS-guessing method (NAACL 2024); ICML 2025 BDC mitigation paper; mirt supports 3PL IRT; MMLU items publicly available.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Compare IRT item parameter estimates (especially guessing parameters) between models with known training data overlap and those without, testing whether aberrant parameters signal contamination
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If safety benchmarks are contaminated, models may score well because they memorized answers during training, not because they have genuine safety behaviors. An IRT-based contamination audit provides a psychometrically principled detection method complementary to n-gram approaches, and specifically targets the items most likely to be gamed—those that are hard but show high model success rates. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** IRT Contamination Detection / Data Integrity | **Strategy:** novel_direction | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong chain: elevated c-parameters on hard items → signal training data leakage → identify compromised benchmark items → restore benchmark integrity. Directly addresses whether safety evals are measuring genuine behavior vs memorization.
  - **low_compute:** 5, confidence: 0.9 — 3PL IRT fitting on existing data, CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — 3PL IRT is more complex than 2PL (additional guessing parameter). Requires understanding contamination theory and parameter interpretation. Guided but demands conceptual engagement.
  - **narrow_scope:** 4, confidence: 0.7 — Tightened to single benchmark, single analysis (3PL fit + c-parameter comparison). Clear success criteria.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** novel_direction, sources: 0 KB, 0 web

---

## #44: IRT-Based Adaptive Difficulty Protocol for Dangerous Capability Assessment (Score: 3.70)

**ID:** gen-085

**Research Question:** How can using the 'catr' package in r (computer adaptive testing), design an adaptive item selection protocol for a dangerous capability domain address the problem that benchmark saturation (risk 7) hides capability gains because items cluster below frontier ability? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using the 'catR' package in R (computer adaptive testing), design an adaptive item selection protocol for a dangerous capability domain. Start with a calibrated item bank (can use WMDP or a subset of an existing benchmark with estimated IRT parameters). Implement a simple CAT algorithm: (1) estimate model ability from current responses, (2) select the next item maximizing Fisher information at current ability estimate, (3) terminate when standard error of ability estimate < 0.3. Simulate the protocol on 5-10 model response profiles (using published response patterns). Compare: standard benchmark (fixed items) vs. adaptive protocol — show that adaptive CAT reaches precise ability estimates with fewer items and remains informative even at frontier capability levels. Adaptive testing for AI is called for in arXiv 2306.10512 ('From Static Benchmarks to Adaptive Testing'). METR's agent characteristic curves (2025) apply IRT-adjacent methods to capability. The catR package in R supports full CAT simulation without model training. This is directly actionable by a psychometrician in R.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Simulate computerized adaptive testing item selection on existing benchmark data and compare measurement precision (standard error of theta) against full-length administration
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Adaptive testing prevents ceiling effects by design, continuously challenging the model at its actual ability level. This is a low-cost, R-implementable solution to capability underestimation from saturation. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI evaluation / psychometrics | **Strategy:** causal_chain_intervention | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong chain: adaptive difficulty prevents ceiling effects → maintains informative measurement at frontier capability levels. Addresses benchmark saturation.
  - **low_compute:** 5, confidence: 0.9 — CAT simulation using catR R package, CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Requires understanding CAT algorithms and adaptive item selection. Guided protocol with catR but conceptually demanding.
  - **narrow_scope:** 4, confidence: 0.7 — Tightened to single benchmark CAT simulation. Clear success criteria: compare adaptive vs fixed-item precision.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** causal_chain_intervention, sources: 0 KB, 0 web

---

## #45: First-Token Alignment and the Adversarial Format: Shallow Safety as a Prompt-Sensitivity Exploit (Score: 3.70)

**ID:** gen-154

**Research Question:** How can design a controlled experiment using 5 format conditions known to alter first-token distributions: (a) standard question, (b) prefill attack (providing the start of an affirmative response), (c) json-mode instruction, (d) multi-turn with compliance priming, (e) suffix appended to prompt address the problem that shallow safety alignment (failure b3) makes safety behavior contingent on the first few output tokens? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Design a controlled experiment using 5 format conditions known to alter first-token distributions: (a) standard question, (b) prefill attack (providing the start of an affirmative response), (c) JSON-mode instruction, (d) multi-turn with compliance priming, (e) suffix appended to prompt. For each of 30–50 safety-relevant prompts, administer all formats to 2–3 models via API. Apply IRT to model the probability of safety failure as a function of format 'difficulty' (operationalized as adversarial pressure level). Estimate the format-manipulation effect size relative to between-model differences. Use reliability analysis (alpha, G-coefficient) to quantify how much of the safety score is format-determined. Shallow alignment paper (arxiv 2406.07358) documents prefilling and suffix attacks as exploiting first-token distributions. Prompt sensitivity research documents format-driven performance drops. Prefill and JSON-mode attacks are documented in alignment attack literature. G-theory and IRT analysis are feasible in R.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If format manipulation can bypass shallow alignment, then any single-format safety evaluation is incomplete by design. Quantifying the format-sensitivity effect size relative to genuine model differences provides an evidence-based argument for multi-format evaluation requirements. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Alignment | **Strategy:** compounding_risks | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong: if safety alignment operates primarily on first-token probabilities, it's vulnerable to adversarial formatting that bypasses this shallow mechanism.
  - **low_compute:** 3, confidence: 0.6 — Requires API calls for format sensitivity testing.
  - **accessible_complexity:** 3, confidence: 0.6 — Requires understanding token-level safety mechanisms. Intermediate.
  - **narrow_scope:** 4, confidence: 0.6 — Focused: test format sensitivity of safety responses.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** compounding_risks, sources: 0 KB, 0 web

---

## #46: DIF as Safety Benchmark Audit: Which Items Favor RLHF-Finetuned Models Regardless of True Safety? (Score: 3.70)

**ID:** gen-232

**Research Question:** How can collect response matrices from public benchmarks, separating models into rlhf-trained vs address the problem that a specific dif concern for safety benchmarks: rlhf-finetuned models are trained to produce outputs that look safe on human evaluation? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Collect response matrices from public benchmarks, separating models into RLHF-trained vs. non-RLHF groups (matched on overall capability score). Apply DIF analysis using logistic regression controlling for the matching variable. Items showing DIF in favor of RLHF models are candidates for 'apparent safety' rather than 'genuine safety.' Characterize the surface features of DIF items through qualitative coding. Safetywashing (2024) found capability-safety confounds. RLHF vs. non-RLHF model lists are publicly documented. The DIF methodology is well-established. The difR and mirt R packages handle the analysis. This directly extends the Luo et al. proposal to a specifically safety-relevant application.

**Experiments:** - Run Mantel-Haenszel DIF analysis comparing model families (e.g., open-source vs. closed-source) on item-level safety benchmark data to identify items that function differently across groups
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. This directly addresses the 'safetywashing' concern: if RLHF-trained models get credit on safety benchmarks partly through DIF-contaminated items rather than genuine safety, then current safety benchmarks are measuring training style, not safety properties. This is a concrete, testable operationalization of the safetywashing hypothesis. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Safety Evaluation / Psychometrics | **Strategy:** landscape_gap_targeting | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong: tests whether safety items systematically favor RLHF-finetuned models, which could mean benchmarks measure training procedure rather than genuine safety capability.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Standard DIF with guided protocol.
  - **narrow_scope:** 4, confidence: 0.7 — Focused on RLHF vs non-RLHF comparison.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** landscape_gap_targeting, sources: 0 KB, 0 web

---

## #47: Multidimensional IRT for AI Safety: Testing Whether Safety Is One Construct or Many (Score: 3.70)

**ID:** gen-233

**Research Question:** How can assemble a response matrix spanning multiple safety benchmarks (truthfulqa, bbq, a harm refusal dataset) address the problem that all irt applications to ai use unidimensional models (single latent ability)? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Assemble a response matrix spanning multiple safety benchmarks (TruthfulQA, BBQ, a harm refusal dataset). Fit a series of competing MIRT models using the mirt R package: (1) unidimensional, (2) two-dimensional correlated (honesty + harmlessness), (3) bifactor (safety-general + specifics), (4) three-dimensional (HHH). Compare via model fit indices (RMSEA, CFI, BIC). Examine factor loadings to identify which items load on specific safety dimensions. The mirt R package supports MIRT and bifactor models. MIRT for factor structure assessment is well-reviewed in Frontiers in Education (2019). IRT-Router (2025 ACL) shows MIRT is feasible for LLM routing. The AI safety literature has called for multidimensional measurement but never delivered it empirically.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If safety is unidimensional, simplified evaluation is justified. If multidimensional, then single-score safety leaderboards hide critical information — a model could be ranked 3rd overall but rank 12th on honesty and 1st on harm avoidance. MIRT results directly inform the design of next-generation safety reporting. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Safety Evaluation / Psychometrics | **Strategy:** landscape_gap_targeting | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong: tests multidimensionality directly relevant to governance. If safety is multidimensional, composite scores mislead.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.5 — MIRT with competing models. Intermediate-to-advanced.
  - **narrow_scope:** 4, confidence: 0.6 — Focused on single safety benchmark dimensionality test.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** landscape_gap_targeting, sources: 0 KB, 0 web

---

## #48: IRT for Agentic Safety: Do Existing Capability Metrics Reflect Agentic Risk Properly? (Score: 3.70)

**ID:** gen-240

**Research Question:** How can identify a public agentic benchmark with binary success/failure outcomes across multiple models (e address the problem that agentic ai systems (those that take multi-step actions using tools) introduce new safety risks — incorrect tool use, goal misgeneralization, out-of-distribution actions? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Identify a public agentic benchmark with binary success/failure outcomes across multiple models (e.g., tau-bench, AgentBench, or a safety-focused agentic evaluation). Fit a 1PL Rasch model to the binary task-completion response matrix. Examine: (1) item difficulty hierarchy — which agentic tasks are hardest?, (2) model ability estimates on an IRT scale, (3) fit statistics to test whether agentic tasks form a unidimensional ability scale or require multidimensional treatment. Compare the IRT ability ordering to the raw success-rate ordering. Tau-bench (2024), AgentBench, and AgentArch (2025) are public agentic benchmarks with multi-model response data. The mirt R package handles binary data. ADELE (mentioned in the landscape review) proposed extending IRT to agentic dimensions but no empirical work followed. This would be the first IRT analysis of agentic safety tasks.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If agentic task success rates do not fit an IRT model (poor model fit), this means agentic performance is not a unidimensional ability — different models have qualitatively different failure modes, not just different ability levels. This has profound implications for how we interpret and compare agentic AI safety claims. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Agentic AI Safety / Psychometrics | **Strategy:** landscape_gap_targeting | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong: tests whether existing capability metrics reflect agentic risk. Directly relevant to frontier safety as agentic deployment increases.
  - **low_compute:** 5, confidence: 0.9 — CPU-only analysis of existing data.
  - **accessible_complexity:** 3, confidence: 0.6 — IRT application to agentic benchmarks. Intermediate.
  - **narrow_scope:** 4, confidence: 0.7 — Focused: calibrate IRT on agentic benchmark. Clear deliverable.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** landscape_gap_targeting, sources: 0 KB, 0 web

---

## #49: Minimum Viable Calibration Sample for IRT on LLM Benchmarks (Score: 3.61)

**ID:** gen-030

**Research Question:** How can using the open llm leaderboard matrix, implement a simulation: repeatedly subsample n models (n = 50, 100, 200, 500, 1000, 2000, 4000), fit a 2pl irt model in r (mirt), compute fit statistics (rmsea, cfi, item chi-square), and record item parameter recovery (correlation with n=4395 estimates) address the problem that paper 13 (2026) found n=29 models gives unacceptable irt fit statistics, while n=4,395 works? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using the Open LLM Leaderboard matrix, implement a simulation: repeatedly subsample N models (N = 50, 100, 200, 500, 1000, 2000, 4000), fit a 2PL IRT model in R (mirt), compute fit statistics (RMSEA, CFI, item chi-square), and record item parameter recovery (correlation with N=4395 estimates). Produce a power curve of acceptable fit vs. N. Identify the elbow point. Paper 13 (2026); Open LLM Leaderboard (5000+ models); mirt package in R; sample-size-planning tutorial (Schroeders & Gnambs 2025, Sage).

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Most safety benchmark studies evaluate far fewer than 4,000 models. Knowing the minimum N for reliable IRT calibration determines whether psychometric methods are even applicable to typical safety evaluation datasets. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** IRT / Benchmark Methodology | **Strategy:** follow_up_experiment | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 2, confidence: 0.6 — Vague: determines minimum model count for IRT. Methodological contribution but doesn't trace to specific catastrophic risk.
  - **low_compute:** 5, confidence: 0.9 — CPU-only simulation.
  - **accessible_complexity:** 3, confidence: 0.6 — Simulation study with guided protocol. Requires understanding IRT fit statistics.
  - **narrow_scope:** 5, confidence: 0.8 — Single experiment: subsample N models, fit IRT, measure fit. Very tightly scoped.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** follow_up_experiment, sources: 0 KB, 0 web

---

## #50: Rasch, 2PL, or 3PL? Selecting the Right IRT Model for Safety Benchmark Items (Score: 3.61)

**ID:** gen-193

**Research Question:** How can using item-level response data from a safety benchmark, fit competing irt models (rasch / 1pl, 2pl, 3pl) using the mirt or ltm packages in r, compare model fit via aic/bic and likelihood-ratio tests, and determine whether item discrimination parameters vary significantly across safety items (arguing for 2pl) or whether a guessing parameter is needed (arguing for 3pl) address the problem that apply irt to ai safety benchmarks? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using item-level response data from a safety benchmark, fit competing IRT models (Rasch / 1PL, 2PL, 3PL) using the mirt or ltm packages in R, compare model fit via AIC/BIC and likelihood-ratio tests, and determine whether item discrimination parameters vary significantly across safety items (arguing for 2PL) or whether a guessing parameter is needed (arguing for 3PL). Interpret what different models imply about how 'safety ability' works. Comparisons of SAS PROC IRT and mirt for multidimensional IRT show both tools handle 1PL through 3PL estimation well. The 'Lost in Benchmarks' (2025) paper uses a 2PL model for LLM benchmarks without strong justification. For safety items, the choice deserves explicit empirical testing.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Different IRT models encode different theories of how models respond to safety items. The Rasch model assumes all items are equally discriminating; 2PL allows variable discrimination; 3PL adds a pseudo-guessing parameter. For safety, there is no obvious 'guessing' analog, but some models may comply with unsafe requests at a non-zero baseline rate regardless of ability. The right model choice affects all downstream inferences. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation / Psychometrics | **Strategy:** problem_decomposition | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 2, confidence: 0.6 — Methodological: IRT model selection. No specific catastrophic risk chain.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Model comparison requires understanding IRT model differences. Intermediate.
  - **narrow_scope:** 5, confidence: 0.8 — Single benchmark, fit 3 models, compare fit. Very tightly scoped.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** problem_decomposition, sources: 0 KB, 0 web

---

## #51: Invisible Ceilings, Hidden Dangers: Benchmark Saturation and Capability Overhang (Score: 3.52)

**ID:** gen-138

**Research Question:** How can identify 3–5 benchmark tasks currently showing saturation (>90% correct across frontier models, documented in the literature) address the problem that ceiling effects prevent benchmarks from discriminating between highly capable models (failure a4), while capability overhang describes dangerous skills that exist but remain undetected (failure b4)? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Identify 3–5 benchmark tasks currently showing saturation (>90% correct across frontier models, documented in the literature). Apply Item Response Theory (IRT) in R (mirt package) to estimate item difficulty and model discrimination parameters. Quantify how many items have discrimination parameters near zero (non-informative at the frontier). Cross-reference with literature on specific dangerous capability categories (CBRN, cyberattack) to estimate how many items in each benchmark could plausibly detect capability overhang. Produce a 'detection gap' metric: what fraction of the benchmark retains discriminative power at the frontier safety-relevant ability range. Benchmark saturation systematically documented in 2025–2026 literature (MMLU, GSM8K >90% for all frontier models). IRT applied to LLM benchmarks in multiple 2024–2025 papers including 'Lost in Benchmarks' (arxiv 2505.15055) and Cambridge Enterprise psychometric work. Capability overhang and CBRN gap in evaluations noted in the International AI Safety Report 2025.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If our best-available safety benchmarks are saturated, the most dangerous frontier model capabilities are precisely those we cannot measure. IRT analysis makes this structural blind spot visible and provides a principled basis for benchmark replacement or augmentation. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 5), low_compute (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation & Benchmarking | **Strategy:** compounding_risks | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 5, confidence: 0.7 — Compelling chain: benchmark saturation hides capability overhang → catastrophic underprediction of frontier capabilities. Targets recognized critical pathway in AI governance.
  - **low_compute:** 5, confidence: 0.9 — Analysis on existing data.
  - **accessible_complexity:** 3, confidence: 0.6 — Conceptual framing requires understanding capability overhang theory. Analysis itself is accessible but interpretation demands domain knowledge.
  - **narrow_scope:** 3, confidence: 0.5 — Broader conceptual scope. Reduced to focused analysis but still involves multiple benchmarks and theoretical framing.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** compounding_risks, sources: 0 KB, 0 web

---

## #52: IRT-Based Formal Power Analysis for Safety Benchmark Design (Score: 3.43)

**ID:** gen-013

**Research Question:** How can use the mirt r package and its simulate functions to conduct monte carlo irt power analyses for representative safety benchmark scenarios address the problem that no published ai safety benchmark was designed with a formal power analysis specifying the minimum number of items required to reliably distinguish models at a given safety ability difference? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Use the mirt R package and its simulate functions to conduct Monte Carlo IRT power analyses for representative safety benchmark scenarios. Vary: number of items (20, 50, 100, 200), item discrimination (a=0.5 to 2.0), ability difference to detect (0.3, 0.5, 1.0 theta units), and item pool difficulty distribution. Report power curves and minimum item counts for each scenario. Apply results to critique the item counts of 3-4 existing safety benchmarks. Derive practical sample-size guidelines for future benchmark designers. Open problem 11 from MTAI framework (no formal IRT power analysis for AI); mirt R package simulation capabilities; sample size analysis for ML validation (PMC 2023); N-Power AI framework (bioRxiv 2025); tinyBenchmarks finding that 100 items from 14K MMLU suffice.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Without power analysis, safety benchmark designers cannot know whether their benchmark has sufficient statistical power to distinguish models of interest. This is the direct AI safety analogue of open problem 11 (no IRT power analysis for AI). Results would provide the first principled item-count recommendations for safety benchmarks, with immediate practical utility for AISI, METR, and similar organizations. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** IRT Power Analysis / Benchmark Design | **Strategy:** novel_direction | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: power analysis reveals whether benchmarks have sufficient items to discriminate. Addresses open problem but chain to catastrophic risk has gaps.
  - **low_compute:** 5, confidence: 0.9 — Monte Carlo simulation, CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Power analysis simulation requires understanding statistical power concepts. Guided but conceptually intermediate.
  - **narrow_scope:** 4, confidence: 0.7 — Focused: vary items/discrimination/ability difference, produce power curves. Clear deliverable.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** novel_direction, sources: 0 KB, 0 web

---

## #53: Adaptive Safety Probing: Simulating CAT Administration of Safety Items (Score: 3.43)

**ID:** gen-025

**Research Question:** How can using item parameters from a 2pl irt model fitted to a safety benchmark (mirt r), simulate cat administration using the catr package address the problem that computerized adaptive testing (cat) efficiently estimates ability using far fewer items by selecting items based on current ability estimates? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using item parameters from a 2PL IRT model fitted to a safety benchmark (mirt R), simulate CAT administration using the catR package. Use maximum information item selection and various stopping rules (SE < 0.3, minimum 10 items). Compare: final theta estimates from CAT vs. full-test administration; number of items required by CAT; which items are most frequently selected (revealing which items are most informative for safety ability estimation). Report the reduction in items achievable with r > 0.95 recovery. Medical CAT: r=0.988 with 1.3% of items (Paper cited in topic context); tinyBenchmarks: 100 items from 14K MMLU with 1.9% error; catR R package for CAT simulation; open problem 4 (cold-start for adaptive approaches); mirt IRT calibration as prerequisite.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Simulate computerized adaptive testing item selection on existing benchmark data and compare measurement precision (standard error of theta) against full-length administration
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If safety evaluations can be reduced from 500 items to 50 items with minimal loss of precision using CAT principles, evaluation cost and time drops by 90%—making comprehensive safety evaluation far more tractable for smaller labs and regulators. The cold-start problem (open problem 4) means operational CAT is not yet feasible, but simulations demonstrate the theoretical efficiency ceiling and identify highest-information safety items. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** CAT Simulation / Adaptive Safety Evaluation | **Strategy:** novel_direction | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: CAT reduces evaluation cost by 90%. Efficiency gains are important but chain to catastrophic risk reduction has gaps.
  - **low_compute:** 5, confidence: 0.9 — CAT simulation, CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — catR package automates CAT simulation. Guided but requires understanding adaptive algorithms.
  - **narrow_scope:** 4, confidence: 0.7 — Tightened to single benchmark CAT simulation. Clear deliverable.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** novel_direction, sources: 0 KB, 0 web

---

## #54: tinyBenchmarks Failure Modes: When Does IRT-Based Item Selection Break Under Distribution Shift? (Score: 3.43)

**ID:** gen-029

**Research Question:** How can using the public tinybenchmarks data and open llm leaderboard scores, systematically simulate distribution shift: hold out model subgroups (e address the problem that tinybenchmarks (polo et al? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using the public tinyBenchmarks data and Open LLM Leaderboard scores, systematically simulate distribution shift: hold out model subgroups (e.g., only instruction-tuned models, only models <7B, only code-specialised models) from the calibration set and measure estimation error on the held-out group. Plot RMSE and rank-correlation as a function of how different the held-out group is from calibration. Identify the threshold at which the 100-item estimate degrades beyond a pre-specified tolerance (e.g., >5 rank positions). tinyBenchmarks (arXiv 2402.14992); tinyMMLU dataset on HuggingFace; IRT calibration in R (mirt package); Open LLM Leaderboard for model metadata.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Safety evaluators who adopt sparse benchmarks need to know when those benchmarks fail. If IRT-CAT degrades for novel model architectures, early-warning safety evaluations of frontier models may be systematically miscalibrated. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** IRT / Adaptive Testing / Benchmark Validity | **Strategy:** follow_up_experiment | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: identifies when IRT-based item selection breaks under distribution shift. Important for evaluation robustness.
  - **low_compute:** 5, confidence: 0.9 — CPU-only simulation.
  - **accessible_complexity:** 3, confidence: 0.6 — Requires simulation design for distribution shift. Intermediate.
  - **narrow_scope:** 4, confidence: 0.7 — Focused: hold-out model subgroups, measure degradation. Clear success criteria.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** follow_up_experiment, sources: 0 KB, 0 web

---

## #55: Automated Test Assembly (ATA) Optimization for Efficient Safety Benchmark Design (Score: 3.43)

**ID:** gen-073

**Research Question:** How can adapt ata methodology: using calibrated item parameters from existing irt analyses of safety benchmarks (already available from arxiv 2505 address the problem that safety benchmarks are assembled heuristically—researchers add items that seem useful until the set is 'large enough? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Adapt ATA methodology: using calibrated item parameters from existing IRT analyses of safety benchmarks (already available from arXiv 2505.15055 and related work), formulate the benchmark assembly problem as an integer programming problem. Minimize benchmark length while (a) achieving target measurement precision at the critical safety threshold, (b) satisfying content blueprint constraints, and (c) limiting item exposure. Use R (lpSolve or ompr package) to solve. Show what a psychometrically optimized 50-item safety benchmark would look like vs. the current 500-item benchmark. ATA is a mature educational measurement technique (test assembly constraint programming literature). Recent CAT paper (arXiv 2603.23506) shows 1.3% of items achieve near-perfect correlation in adaptive testing. R lpSolve/ompr packages support integer programming. Calibrated item parameters already available for major benchmarks. Requires no new data collection.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. ATA can produce shorter, more precise benchmarks that are less susceptible to gaming and less expensive to run—critical advantages as evaluation costs scale with model size. Showing a benchmark can be 10x shorter with equivalent precision would fundamentally change evaluation economics. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation & Benchmarking | **Strategy:** cross_domain_transfer | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: optimal benchmark assembly. Efficiency chain.
  - **low_compute:** 5, confidence: 0.9 — Integer programming, CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Integer programming for ATA. Requires understanding optimization. Intermediate.
  - **narrow_scope:** 4, confidence: 0.7 — Tightened: one benchmark, optimize item selection. Clear deliverable.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** cross_domain_transfer, sources: 0 KB, 0 web

---

## #56: Test Information Functions for Safety Evaluation: Where Do Safety Benchmarks Measure Well? (Score: 3.43)

**ID:** gen-106

**Research Question:** How can fit a 2pl or 3pl irt model to response data from multiple models on two or three published safety benchmarks (e address the problem that safety benchmarks are applied uniformly across all models regardless of where a model sits on the latent safety continuum? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Fit a 2PL or 3PL IRT model to response data from multiple models on two or three published safety benchmarks (e.g., SafetyBench, MLCommons AIR-Bench). Plot test information functions (TIFs) for each benchmark. Compare where each benchmark concentrates measurement precision. Analyze whether TIFs are aligned with the safety-relevant ability range (i.e., near the pass/fail threshold). Write a blog post translating TIF logic into benchmark design recommendations. The 'Lifting the benchmark iceberg with IRT' paper (OpenReview) and Epoch Capability Index both use IRT on LLM benchmarks. Fluid Benchmarking (Ai2) uses IRT but does not report TIFs in safety-specific regions. The 'Measuring what Matters' systematic review (arxiv 2511.04703) found that 46.6% of benchmarks lack validity evidence. TIF analysis is straightforward in mirt.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Addresses the gap in Success State 2 (benchmarks measure with known precision) and Success State 1 (reliable detection at capability boundary). If TIFs peak far from the threshold, a benchmark gives false confidence. Quantifying this gap motivates targeted item development at the informative region. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Benchmark Validity / Psychometrics | **Strategy:** backcast_from_success | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible chain: TIF reveals measurement gaps. Generic measurement quality.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Standard IRT with guided protocol.
  - **narrow_scope:** 4, confidence: 0.7 — Focused deliverable: TIF plots for safety benchmarks.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** backcast_from_success, sources: 0 KB, 0 web

---

## #57: D-Study Optimization: Minimum Item Count for Reliable Safety Assessment (Score: 3.43)

**ID:** gen-110

**Research Question:** How can using data from a g-study (or simulated variance components based on published partial data), run a series of d-studies varying the number of items from 5 to 500 address the problem that labs run safety evaluations with item counts chosen by convenience rather than by formal power analysis? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using data from a G-study (or simulated variance components based on published partial data), run a series of D-studies varying the number of items from 5 to 500. For each item count, compute G-coefficients and phi-coefficients. Plot cost-reliability tradeoff curves. Identify the inflection point where additional items yield diminishing reliability gains. Stratify by safety subdomain (harmlessness, robustness, honesty) to determine if subdomains require different item counts. The 2025 G-Theory in AI paper (ScienceDirect) explicitly recommends D-studies for AI evaluation but does not execute them. IRT sample-size planning tutorial (Schroeders & Gnambs, 2025) shows sample-size planning is an active gap even in IRT. CAT literature shows 50% item reduction is achievable. No published D-study exists for AI safety evaluation.

**Experiments:** - Apply the proposed analysis method to item-level data from one public safety benchmark (e.g., TruthfulQA, HarmBench)
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Directly addresses Success State 6 (minimum evaluation effort for reliable assessment). Gives labs and regulators a principled, defensible answer to evaluation design questions. Bridges G-Theory and practical evaluation policy. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Evaluation Design / Generalizability Theory | **Strategy:** backcast_from_success | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: determines minimum items for reliable assessment. Generic measurement quality.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — G-theory D-study requires understanding generalizability theory. Intermediate.
  - **narrow_scope:** 4, confidence: 0.7 — Focused optimization study.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** backcast_from_success, sources: 0 KB, 0 web

---

## #58: Adaptive Safety Evaluation via Computerized Adaptive Testing (CAT): Proof of Concept (Score: 3.43)

**ID:** gen-119

**Research Question:** How can using irt parameters calibrated in a prior study, implement a simulated cat algorithm using the catr r package address the problem that current safety evaluations administer the same fixed item set to all models regardless of ability level? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using IRT parameters calibrated in a prior study, implement a simulated CAT algorithm using the catR R package. Simulate CAT administration for a set of AI models. Compare precision (standard error of theta estimate) and efficiency (number of items used) between CAT and fixed-length testing at matched ability estimates. Analyze which stopping rules (fixed SE < 0.3, maximum information, or fixed length) are most appropriate for safety evaluation. Produce design recommendations for a real-world adaptive safety evaluation. CAT for LLM medical benchmarks (arxiv 2603.23506, March 2026) is the closest analog. Trismik (Cambridge) is applying CAT to LLM evaluation generally. The catR R package is well-suited for simulation studies. The simulation-only design avoids the need to re-run expensive model evaluations.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Simulate computerized adaptive testing item selection on existing benchmark data and compare measurement precision (standard error of theta) against full-length administration
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Addresses Success State 1 and Success State 6 simultaneously: CAT efficiently probes capability boundaries (adaptive) while reducing minimum evaluation effort (fewer items for same precision). In high-stakes pre-deployment evaluation, efficiency directly reduces cost and time-to-deployment without sacrificing safety rigor. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Evaluation Efficiency / Computerized Adaptive Testing | **Strategy:** backcast_from_success | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: proof-of-concept for adaptive safety evaluation. Efficiency chain.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — CAT simulation. Intermediate.
  - **narrow_scope:** 4, confidence: 0.7 — Focused proof-of-concept.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** backcast_from_success, sources: 0 KB, 0 web

---

## #59: DIF by Model Architecture: Are Safety Items Biased Against Open-Source Models? (Score: 3.43)

**ID:** gen-129

**Research Question:** How can using item-level response data from safety benchmarks evaluated on both proprietary (gpt-4 class, claude class) and open-source (llama class, mistral class) models, apply dif analysis using the mantel-haenszel method and irt-based lord's chi-square test (difr package in r) address the problem that safety evaluations compare proprietary and open-source models using the same items? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using item-level response data from safety benchmarks evaluated on both proprietary (GPT-4 class, Claude class) and open-source (LLaMA class, Mistral class) models, apply DIF analysis using the Mantel-Haenszel method and IRT-based Lord's chi-square test (difR package in R). Use model family (proprietary vs. open-source) as the grouping variable. Identify items with significant DIF and characterize their content. Compute effect sizes and flag items exceeding ETS C-level DIF. DIF for second-language assessment fairness (systematic review, 2025) provides methodology directly applicable here with architecture family as the grouping variable. The difR package handles all standard DIF methods. The finding that LLMs predict DIF-associated words (arxiv 2502.07017) suggests automated DIF detection is feasible. No published DIF study across AI architecture families exists.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Run Mantel-Haenszel DIF analysis comparing model families (e.g., open-source vs. closed-source) on item-level safety benchmark data to identify items that function differently across groups
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Addresses measurement fairness across model families, filling a gap in Success State 3 (comparable cross-model safety assessment). If safety items are systematically biased against open-source models, safety evaluations may be systematically unfair to them — with policy implications for which models are approved for deployment. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Measurement Fairness / DIF Analysis | **Strategy:** backcast_from_success | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: tests whether safety items are biased against open-source models. Interesting but indirect catastrophic risk connection.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Standard DIF analysis with guided protocol.
  - **narrow_scope:** 4, confidence: 0.7 — Focused deliverable: DIF comparison open vs closed-source.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** backcast_from_success, sources: 0 KB, 0 web

---

## #60: Differential Item Functioning Analysis for AI Safety Benchmarks: Open vs. Closed-Source Models (Score: 3.43)

**ID:** gen-166

**Research Question:** How can collect pass/fail responses from a set of open-source and closed-source models (matched for overall safety score) on a safety benchmark with sufficient items (n > 30) address the problem that ai safety benchmark items may function differently for different classes of models (open vs? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Collect pass/fail responses from a set of open-source and closed-source models (matched for overall safety score) on a safety benchmark with sufficient items (n > 30). Apply DIF detection methods available in R (the difR package implements Mantel-Haenszel, logistic regression, and Lord's chi-square). Identify items showing significant DIF between model classes. Examine whether DIF items share systematic features (format, hazard category, response length sensitivity). Compute benchmark scores with and without DIF items and assess whether rankings change. The FairDIF paper (Springer, 2026) explicitly applies IRT and DIF to classification fairness. The paper 'Finding Words Associated with DIF' (JEDM 2025) shows DIF is detectable from item text. DIF analysis in R using difR is a standard psychometric workflow. Several public safety benchmarks (StrongREJECT, MLCommons) have sufficient items and multiple model evaluations. This specific application to model-type DIF in safety benchmarks has not been published.

**Experiments:** - Apply the proposed analysis method to item-level data from one public safety benchmark (e.g., TruthfulQA, HarmBench)
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. DIF analysis is the standard method for detecting measurement bias in educational and clinical testing. If safety benchmark items function differently for open vs. closed-source models, current cross-model comparisons are invalid. This analysis could reveal that apparent safety differences between model types are artifacts of item bias rather than genuine behavioral differences. The difR package in R makes this analysis accessible without heavy coding. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Evaluations & Benchmarks | **Strategy:** methodology_bridging | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: DIF reveals benchmark bias. Generic measurement quality chain.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Standard DIF with guided protocol.
  - **narrow_scope:** 4, confidence: 0.7 — Focused on single benchmark.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** methodology_bridging, sources: 0 KB, 0 web

---

## #61: Score Equating for AI Safety Benchmarks: Enabling Fair Cross-Benchmark Comparison (Score: 3.43)

**ID:** gen-167

**Research Question:** How can select two or more safety benchmarks that have been administered to a common set of models address the problem that different ai safety benchmarks (e? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Select two or more safety benchmarks that have been administered to a common set of models. Using those models as the 'linking sample,' apply equipercentile equating (or IRT-based observed-score equating) to place both benchmarks on a common scale. Use the equate R package. Evaluate linking quality using the standard error of equating and the degree of model rank-order change post-equating. Produce a concordance table allowing practitioners to convert scores across benchmarks. Validate by checking whether equated scores predict human-judged safety ratings better than raw scores. The 'Psychometrically derived 60-question benchmarks' paper (ScienceDirect 2025) shows IRT-based cross-benchmark work is feasible. The equate R package is mature and widely used. Several safety benchmarks have been run on overlapping model sets (e.g., Llama family, GPT-4 class). Score equating has been discussed conceptually in AI evaluation literature but empirical equating studies appear absent from the literature.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Score equating is the foundational method for making test scores comparable across forms in education (SAT, GRE) and medicine. Without it, comparing models evaluated on different benchmarks is like comparing Fahrenheit and Celsius without a conversion formula. The equate R package implements all standard equating methods without heavy coding. This could immediately improve how AI labs, regulators, and researchers compare safety claims. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Evaluations & Benchmarks | **Strategy:** methodology_bridging | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: enables fair comparison.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.5 — Equating. Intermediate-to-advanced.
  - **narrow_scope:** 4, confidence: 0.6 — Focused on linking two specific benchmarks.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** methodology_bridging, sources: 0 KB, 0 web

---

## #62: Adaptive Safety Testing via IRT-Based Item Selection: Designing a CAT Safety Benchmark (Score: 3.43)

**ID:** gen-172

**Research Question:** How can using publicly available response data from a safety benchmark with many items (e address the problem that current safety benchmarks administer the same fixed set of hundreds of items to every model regardless of its safety level, making evaluation slow and expensive? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using publicly available response data from a safety benchmark with many items (e.g., WildGuard, SORRY-Bench, or HarmBench), fit an IRT model (2PL or Rasch) to estimate item difficulty and discrimination parameters. Simulate a CAT algorithm using the mirtCAT R package: start with moderate-difficulty items, select next items based on maximum information at the current ability estimate, stop when SE falls below a threshold. Compare the number of items needed to achieve equivalent measurement precision versus fixed-form administration. Evaluate convergence speed and rank-order fidelity for the CAT vs. full benchmark. CAT has been applied to AI benchmarks in medical contexts (arxiv 2603.23506) and via the CAT4AI Python library (GitHub bigdata-ustc). The 'From Static Benchmarks to Adaptive Testing' paper (arxiv 2306.10512) explicitly proposes this direction for AI evaluation. mirtCAT and catR are R packages supporting CAT simulation. Safety benchmarks like SORRY-Bench have 400+ items—sufficient for IRT calibration. This application specifically to safety benchmarks with analysis of item-type coverage appears novel.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Simulate computerized adaptive testing item selection on existing benchmark data and compare measurement precision (standard error of theta) against full-length administration
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. The recent paper 'Leveraging CAT for Cost-effective Evaluation of LLMs in Medical Benchmarking' (arxiv 2603.23506) shows CAT achieves near-perfect correlation with full-bank estimates using only 1.3% of items in medical benchmarks. The CAT4AI framework already exists on GitHub. Applying this specifically to safety benchmarks could reduce evaluation cost by 90%+ while maintaining precision. mirtCAT in R makes simulation straightforward without ML training. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Evaluations & Benchmarks | **Strategy:** methodology_bridging | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: adaptive selection preserves ranking quality. Efficiency chain.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — CAT simulation. Intermediate.
  - **narrow_scope:** 4, confidence: 0.7 — Focused on ranking preservation.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** methodology_bridging, sources: 0 KB, 0 web

---

## #63: IRT-Based Adaptive Item Selection for Safety Evaluation: Does It Preserve Ranking Accuracy? (Score: 3.43)

**ID:** gen-196

**Research Question:** How can using pre-calibrated irt parameters from a safety benchmark, simulate a computerized adaptive testing (cat) procedure in r: starting with items of medium difficulty, adaptively select next items based on maximum fisher information at the current theta estimate, and stop when standard error falls below 0 address the problem that apply irt to ai safety benchmarks? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using pre-calibrated IRT parameters from a safety benchmark, simulate a computerized adaptive testing (CAT) procedure in R: starting with items of medium difficulty, adaptively select next items based on maximum Fisher information at the current theta estimate, and stop when standard error falls below 0.3. Compare safety ability estimates from CAT (using ~20% of items) against full-benchmark estimates and measure rank-order correlation between models. CAT for LLM evaluation has been validated for medical benchmarks (2026 preprint): CAT-derived proficiency estimates achieved near-perfect correlation with full-bank estimates using only 1.3% of items. The tinyBenchmarks paper (2024) showed 160x cost reduction on Open LLM Leaderboard using IRT item selection. Safety benchmarks are a natural next target.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Simulate computerized adaptive testing item selection on existing benchmark data and compare measurement precision (standard error of theta) against full-length administration
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Safety evaluations are expensive—running hundreds of models across thousands of items consumes significant compute. If IRT-based adaptive selection can accurately rank models using 10-20% of items, this would drastically reduce evaluation costs while maintaining the same discriminative validity. Recent work achieved 98%+ cost reduction for medical benchmarks using this approach. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation / Psychometrics | **Strategy:** problem_decomposition | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: tests whether adaptive selection preserves safety rankings.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Intermediate.
  - **narrow_scope:** 4, confidence: 0.7 — Focused comparison study.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** problem_decomposition, sources: 0 KB, 0 web

---

## #64: Test-Retest Reliability of Safety Benchmarks: How Stable Are Safety Scores Over Time? (Score: 3.43)

**ID:** gen-217

**Research Question:** How can using a fixed set of open-weight models (e address the problem that make ai evaluation reproducible and reliable? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using a fixed set of open-weight models (e.g., Llama-3, Mistral, Gemma), administer the same safety benchmark twice at one-week intervals with identical prompts and settings (temperature=0, identical system prompt). Compute intraclass correlation coefficients (ICC) for each model's score and for the overall model ranking (Spearman r). Identify whether score instability comes from model stochasticity (temperature effects), infrastructure variability, or prompt order effects. 'Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory' (2025) examines judge reliability using IRT but does not address test-retest reliability of safety scores for evaluated models. ICC computation is standard in R (irr package). Claude-3.5-Haiku showed high intra-rater consistency in writing assessment contexts, suggesting test-retest stability is achievable.

**Experiments:** - Compute internal consistency reliability (Cronbach's alpha, split-half) and IRT-based reliability (test information function) for a safety benchmark, reporting confidence intervals around model ability estimates
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Before any other validity analysis can be meaningful, a benchmark must be reliable: the same model should receive similar scores when evaluated twice under identical conditions. There is currently no published test-retest reliability data for AI safety benchmarks. Without this baseline, all score comparisons and longitudinal tracking of model safety are scientifically questionable. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 4), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation / Reliability | **Strategy:** problem_decomposition | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: if safety scores aren't stable across runs, they're unreliable for governance.
  - **low_compute:** 4, confidence: 0.7 — Requires multiple evaluation runs.
  - **accessible_complexity:** 3, confidence: 0.6 — Test-retest design. Intermediate.
  - **narrow_scope:** 4, confidence: 0.7 — Focused: run same benchmark twice, compute correlation.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** problem_decomposition, sources: 0 KB, 0 web

---

## #65: Does Reliability Vary by Model Capability Level? Testing Heteroskedastic Measurement Error (Score: 3.43)

**ID:** gen-221

**Research Question:** How can using bootstrap or irt-based sem estimates, test whether measurement error in safety benchmark scores differs systematically by model capability level: do frontier models have smaller or larger sems than mid-tier models? plot sem as a function of estimated safety theta address the problem that make ai evaluation reproducible and reliable? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using bootstrap or IRT-based SEM estimates, test whether measurement error in safety benchmark scores differs systematically by model capability level: do frontier models have smaller or larger SEMs than mid-tier models? Plot SEM as a function of estimated safety theta. Test whether the test information function peaks at a capability level that matches the population of models being evaluated, or whether it is concentrated in a range where few models actually score. IRT information functions inherently quantify where measurement is most precise across the ability distribution. 'Lifting the Benchmark Iceberg with Item-Response Theory' (OpenReview) examines measurement quality across model ability levels. The test information function is a standard mirt output. No study has explicitly tested whether safety benchmark reliability varies systematically by model capability tier.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Compute internal consistency reliability (Cronbach's alpha, split-half) and IRT-based reliability (test information function) for a safety benchmark, reporting confidence intervals around model ability estimates
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Measurement error is often heteroskedastic: benchmarks may be highly precise for models near the item bank's difficulty center but imprecise for models at the extremes. If safety benchmarks are calibrated for mid-range safety ability and frontier models are all near the ceiling, frontier model rankings are especially unreliable even as they are most consequential for deployment decisions. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation / Psychometrics | **Strategy:** problem_decomposition | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: heteroskedastic measurement error means different precision for different capability levels.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Requires understanding measurement error heterogeneity. Intermediate.
  - **narrow_scope:** 4, confidence: 0.7 — Focused comparison: reliability at different ability levels.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** problem_decomposition, sources: 0 KB, 0 web

---

## #66: Differential Item Functioning in Safety Benchmarks: Do Items Favor Certain Model Families? (Score: 3.43)

**ID:** gen-222

**Research Question:** How can using item-level safety response data for models from different training families (e address the problem that establish construct validity for ai safety evaluation? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using item-level safety response data for models from different training families (e.g., Llama-family vs. Mistral-family vs. Gemma-family), conduct DIF analysis using the Mantel-Haenszel method and IRT-based DIF tests (lordif package in R). Identify items that show statistically significant DIF: items where models from one family are more likely to refuse/comply than models of equivalent overall safety ability from another family. Characterize what these items have in common. FairDIF (Springer, 2025) applies IRT-based DIF to fairness problems in classification. A paper titled 'DIF: A Framework for Benchmarking and Verifying Implicit Bias in LLMs' (2025) examines DIF in LLM responses using sociodemographic personas. The lordif and difR packages in R implement standard DIF detection methods accessible to psychometrically-trained users.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If safety benchmark items systematically favor models from certain training families or architectures—independent of those models' true safety level—then benchmark scores are biased. A model from family A that appears safer than an equivalent model from family B may simply have been trained on data more similar to the benchmark's format. DIF detection is the standard psychometric tool for identifying such bias. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation / Fairness | **Strategy:** problem_decomposition | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible chain. Generic measurement quality.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Standard DIF analysis.
  - **narrow_scope:** 4, confidence: 0.7 — Focused deliverable.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** problem_decomposition, sources: 0 KB, 0 web

---

## #67: Differential Item Functioning Analysis of Safety Benchmarks Across Model Families (Score: 3.43)

**ID:** gen-231

**Research Question:** How can define model 'families' as grouping variables (e address the problem that dif occurs when examinees of equal ability have systematically different probabilities of passing an item due to group membership? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Define model 'families' as grouping variables (e.g., open-source vs. proprietary, base vs. RLHF-finetuned, GPT family vs. Llama family vs. Claude family). Collect binary response data from public leaderboards. Run Mantel-Haenszel DIF detection and logistic regression DIF procedures (difR package in R) on safety benchmark items. Flag items with significant DIF. Examine whether flagged items share surface features (topic, phrasing style, cultural reference). Report whether benchmark items are biased toward specific training paradigms. The FairDIF paper (Springer AI and Ethics, 2026) specifically applies IRT and DIF to AI fairness. The difR package is well-maintained in R. DIF analysis is standard psychometric practice. Public response matrices from HELM and Open LLM Leaderboard enable this analysis without additional data collection.

**Experiments:** - Apply the proposed analysis method to item-level data from one public safety benchmark (e.g., TruthfulQA, HarmBench)
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. DIF in safety benchmarks means scores are not comparable across model families — a GPT model achieving 80% on TruthfulQA is not equivalent to a Llama model achieving 80% if different items drive the scores. This undermines the validity of cross-model safety comparisons, which are the primary use of safety benchmarks. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Fairness and Evaluation / Psychometrics | **Strategy:** landscape_gap_targeting | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible chain.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Standard DIF.
  - **narrow_scope:** 4, confidence: 0.7 — Focused deliverable.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** landscape_gap_targeting, sources: 0 KB, 0 web

---

## #68: Psychometric Analysis of Multimodal Safety: IRT for Vision-Language Safety Benchmarks (Score: 3.43)

**ID:** gen-242

**Research Question:** How can collect binary response matrices from public multimodal safety benchmarks for 15-20 models address the problem that all irt applications to ai evaluation use text-only benchmarks? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Collect binary response matrices from public multimodal safety benchmarks for 15-20 models. Fit a unidimensional IRT model and examine: (1) whether vision-specific items show systematically different discrimination parameters than text-only items on the same benchmark, (2) whether residuals from a text-ability factor are correlated with vision-specific features (using a MIRT model with a vision-specific residual factor), (3) whether IRT item information peaks at different ability levels for visual vs. text safety items. MMSafetyBench, VLSafe, and FigStep are public multimodal safety benchmarks. Research (2024-2025) found many multimodal benchmarks fail to require visual processing. IRT can detect this through dimensionality testing. The mirt package handles this analysis. This would be the first psychometric analysis of multimodal safety benchmarks.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If visual safety items show no psychometric differentiation from text safety items (same discrimination, same difficulty ordering), this is empirical evidence that multimodal safety benchmarks are not measuring vision at all — they measure text-based safety with image distractors. This would be a major validity critique of the multimodal safety evaluation field. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Multimodal AI Safety / Psychometrics | **Strategy:** landscape_gap_targeting | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: IRT for vision-language safety benchmarks. Growing importance.
  - **low_compute:** 5, confidence: 0.9 — CPU-only on existing data.
  - **accessible_complexity:** 3, confidence: 0.6 — IRT on multimodal data. Intermediate.
  - **narrow_scope:** 4, confidence: 0.7 — Focused on single multimodal benchmark.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** landscape_gap_targeting, sources: 0 KB, 0 web

---

## #69: IRT Test Information Functions for Safety Weakness Localization (Score: 3.43)

**ID:** gen-270

**Research Question:** How can fit a multidimensional irt model to a multi-domain safety benchmark, generating test information functions and ability profiles per safety dimension, identifying where on the safety ability continuum each model's measurement is most uncertain address the problem that p8: no way to diagnose specific safety weaknesses (only aggregate scores)? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Fit a multidimensional IRT model to a multi-domain safety benchmark, generating test information functions and ability profiles per safety dimension, identifying where on the safety ability continuum each model's measurement is most uncertain. The mirt R package supports full multidimensional IRT analysis. MetaBench (ICLR 2025) applies IRT across multiple benchmark dimensions. A psychometrician could run MIRT on existing multi-domain safety benchmark response data (e.g., HELM safety subscores) and generate per-dimension information plots in a single R session.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Multidimensional IRT (MIRT) produces separate ability estimates per latent dimension, giving diagnostic profiles rather than aggregate scores. Information functions reveal which ability ranges are well-measured for each safety dimension. This directly provides the per-dimension weakness diagnosis that aggregate scores cannot. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Safety / Psychometrics | **Strategy:** combinatorial_matrix | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: localizes where safety benchmarks have measurement gaps.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Standard IRT analysis with guided protocol.
  - **narrow_scope:** 4, confidence: 0.7 — Focused deliverable.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** combinatorial_matrix, sources: 0 KB, 0 web

---

## #70: Score Equating Across AI Safety Benchmarks: Enabling Valid Cross-Benchmark Model Comparisons (Score: 3.43)

**ID:** gen-274

**Research Question:** How can apply irt-based score equating to link scores from two different ai safety benchmarks (e address the problem that p9: can't compare models across different safety benchmarks? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Apply IRT-based score equating to link scores from two different AI safety benchmarks (e.g., HarmBench and MLCommons AI Safety Benchmark) using a common set of anchor models evaluated on both, placing all models on a common safety ability scale. IRT equating is described as 'the process of equating test forms to ensure scores are comparable no matter what set of items an examinee sees' (Assessment Systems). A 2025 paper on psychometric benchmarks for generalist medical AI (PMC 2025) applies similar linking approaches to medical AI benchmarks. Anchor models evaluated on multiple benchmarks are available via leaderboards.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Currently, a model's score on HarmBench cannot be directly compared to its score on MLCommons ASB. Score equating—the standard psychometric solution for this problem—would for the first time allow cross-benchmark model comparisons and enable tracking of safety progress across benchmark generations. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Safety / Psychometrics | **Strategy:** combinatorial_matrix | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: cross-benchmark comparison.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.5 — Equating. Intermediate.
  - **narrow_scope:** 4, confidence: 0.7 — Focused on two benchmarks.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** combinatorial_matrix, sources: 0 KB, 0 web

---

## #71: IRT Concurrent Calibration for Cross-Benchmark Safety Scale Linking (Score: 3.43)

**ID:** gen-275

**Research Question:** How can pool response data from multiple safety benchmarks and run concurrent irt calibration, estimating a single set of item parameters and model ability estimates on a common scale, enabling direct comparison of models evaluated on different benchmark subsets address the problem that p9: can't compare models across different safety benchmarks? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Pool response data from multiple safety benchmarks and run concurrent IRT calibration, estimating a single set of item parameters and model ability estimates on a common scale, enabling direct comparison of models evaluated on different benchmark subsets. Concurrent calibration is supported in the mirt R package via the multipleGroup function. Multiple safety benchmark response matrices are publicly available. The ICLR 2025 MetaBench paper demonstrates pooled IRT calibration across 6 general benchmarks—directly replicable for safety benchmarks.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Concurrent calibration is the most powerful IRT equating approach, producing a unified safety ability scale from heterogeneous benchmark data. This would be the psychometric infrastructure needed for a 'safety leaderboard' analogous to HELM or Open LLM Leaderboard but with valid cross-benchmark comparisons. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Safety / Psychometrics | **Strategy:** combinatorial_matrix | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible chain.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.5 — Concurrent calibration requires understanding linking methodology.
  - **narrow_scope:** 4, confidence: 0.7 — Focused on concurrent calibration approach.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** combinatorial_matrix, sources: 0 KB, 0 web

---

## #72: DIF Analysis Across Model Families on Safety Benchmarks (Score: 3.43)

**ID:** gen-291

**Research Question:** How can apply dif analysis to safety benchmark items using model family (e address the problem that p1: no irt applied to ai safety benchmarks? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Apply DIF analysis to safety benchmark items using model family (e.g., GPT vs. Claude vs. Llama) as the grouping variable, identifying which safety items function differently across architectures even for models with the same overall safety ability estimate. FairDIF (Springer 2026) demonstrates applying IRT and DIF concepts to AI classification fairness. Applying DIF to safety benchmark items with model family as the grouping variable is directly analogous. Public safety benchmark response data across multiple model families are available. difR R package is the analysis tool.

**Experiments:** - Run Mantel-Haenszel DIF analysis comparing model families (e.g., open-source vs. closed-source) on item-level safety benchmark data to identify items that function differently across groups
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If safety benchmark items show DIF across model families, the benchmarks may be measuring RLHF-tuning artifacts or architecture-specific behaviors rather than a common safety construct. This has immediate implications for cross-family safety comparisons and model-agnostic safety evaluation. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Safety / Psychometrics | **Strategy:** combinatorial_matrix | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible chain.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Standard DIF.
  - **narrow_scope:** 4, confidence: 0.7 — Focused deliverable.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** combinatorial_matrix, sources: 0 KB, 0 web

---

## #73: IRT Contamination Detection: Sensitivity Analysis Across Contamination Types (Score: 3.26)

**ID:** gen-035

**Research Question:** How can using a benchmark with known contamination (or a simulation study using public mmlu data), introduce three contamination types: (1) exact item injection into a model's 'training' (simulated by retrieving answers from a lookup table), (2) paraphrased items, (3) topic-level exposure address the problem that zhuang et al? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using a benchmark with known contamination (or a simulation study using public MMLU data), introduce three contamination types: (1) exact item injection into a model's 'training' (simulated by retrieving answers from a lookup table), (2) paraphrased items, (3) topic-level exposure. Fit 3PL IRT models in R (mirt) and examine the guessing parameter (c) distribution for contaminated vs. clean items. Compute ROC curves for contamination detection across contamination types. Zhuang et al. (2025) IRT contamination (arXiv 2505.15055v3); Simulating training data leakage (ACL 2025 eval4nlp); 3PL IRT in R (mirt); MMLU public data.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Compare IRT item parameter estimates (especially guessing parameters) between models with known training data overlap and those without, testing whether aberrant parameters signal contamination
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. IRT-based contamination detection is only useful if we know what it misses. If paraphrase contamination evades detection, the tool provides false assurance of benchmark integrity. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** IRT / Data Contamination / Benchmark Integrity | **Strategy:** follow_up_experiment | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.6 — Targets understanding of detection limits: do IRT contamination signals differ by contamination type (exact, paraphrase, topic-level)?
  - **low_compute:** 4, confidence: 0.7 — Simulation study requires moderate compute.
  - **accessible_complexity:** 3, confidence: 0.5 — Requires simulation design for contamination types, 3PL IRT, ROC analysis. Intermediate-to-advanced.
  - **narrow_scope:** 3, confidence: 0.6 — Reduced to single focused analysis but still involves multiple contamination types and comparison.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** follow_up_experiment, sources: 0 KB, 0 web

---

## #74: Bookmark Method for Proficiency Level Classification on Safety Benchmarks (Score: 3.26)

**ID:** gen-053

**Research Question:** How can apply the bookmark standard-setting method: arrange benchmark items in order of irt-estimated difficulty (already done in recent llm-irt papers), present this ordered 'item booklet' to safety expert panelists, and ask them to place bookmarks at the transitions between proficiency levels address the problem that safety evaluations rarely distinguish between 'dangerous,' 'borderline,' and 'safe' models with more than one binary threshold? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Apply the Bookmark standard-setting method: arrange benchmark items in order of IRT-estimated difficulty (already done in recent LLM-IRT papers), present this ordered 'item booklet' to safety expert panelists, and ask them to place bookmarks at the transitions between proficiency levels. Run three iterative rounds with feedback. This yields multiple, data-driven thresholds on the same scale. Implement in R using existing IRT packages (mirt, ltm) on open leaderboard data. Bookmark method literature establishes three iterative rounds with norming data as standard procedure. Recent LLM-IRT papers (arXiv 2505.15055, Stanford CRFM 2025) have already estimated item difficulty parameters for major benchmarks, providing the raw material for bookmark placement without additional coding.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Ordinal classification enables risk-tiered governance: models in the 'marginal' band get additional scrutiny, 'unsafe' models are barred, and 'exemplary' models receive deployment fast-tracks. The Bookmark method is more tractable than Angoff for large item pools and produces thresholds anchored to item difficulty statistics. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation & Benchmarking | **Strategy:** cross_domain_transfer | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong: ordinal classification enables risk-tiered governance. Models get 'marginal' scrutiny, 'unsafe' models barred. Directly enables deployment decisions.
  - **low_compute:** 5, confidence: 0.9 — IRT-based difficulty ordering + expert judgment. CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Requires understanding bookmark method and coordinating expert panels. Intermediate.
  - **narrow_scope:** 3, confidence: 0.5 — Requires expert panel coordination (3 iterative rounds). External dependency.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** cross_domain_transfer, sources: 0 KB, 0 web

---

## #75: Construct Explication for Refusal Behavior: A Multidimensional IRT Approach (Score: 3.26)

**ID:** gen-095

**Research Question:** How can using a safety benchmark with multiple harm categories and binary refusal-coded item responses (e address the problem that many safety benchmarks reduce model safety to a single score, often based on refusal rates? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using a safety benchmark with multiple harm categories and binary refusal-coded item responses (e.g., AIR-Bench or MLCommons AILuminate), fit a multidimensional IRT model in R (using mirt package, specifying a bifactor or correlated factors model). Test the unidimensionality assumption using: (1) local independence tests, (2) eigenvalue ratio (first:second eigenvalue should be > 5:1 for unidimensionality), (3) bifactor model fit compared to unidimensional model (RMSEA, CFI). If multidimensionality is confirmed, interpret the factors substantively: do they correspond to harm domains, adversarial technique types, or something else? Compute factor-specific ability scores per model and show that these reveal different vulnerability profiles invisible in the composite score. AILuminate covers 7 hazard categories; AIR-Bench covers 314. The mirt package supports multidimensional IRT with bifactor models. Multidimensional IRT is standard in educational and clinical measurement. Application to AI safety refusal behavior is novel. No prior paper has formally tested unidimensionality of safety evaluation item pools.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. A unidimensional safety score can be 'high' overall even when the model is vulnerable in a specific high-stakes domain (e.g., CBRN). Multidimensional IRT reveals these domain-specific vulnerabilities that composite scores mask. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI evaluation / psychometrics | **Strategy:** causal_chain_intervention | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong: multidimensional safety profiles reveal domain-specific vulnerabilities masked by composite scores. A model 'safe overall' may be vulnerable in CBRN domain.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.5 — MIRT bifactor modeling. Specialist knowledge needed even with protocol.
  - **narrow_scope:** 3, confidence: 0.6 — Reduced but still involves fitting multiple competing models and interpreting factors.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** causal_chain_intervention, sources: 0 KB, 0 web

---

## #76: Standard-Setting Study: What Evaluation Score Should Constitute a Safety Pass/Fail Threshold? (Score: 3.26)

**ID:** gen-100

**Research Question:** How can apply two established standard-setting methods to an existing ai safety benchmark address the problem that the false-negative deployment chain requires a 'decision-to-deploy threshold' to convert a continuous safety score into a pass/fail decision? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Apply two established standard-setting methods to an existing AI safety benchmark. Method 1 (Modified Angoff): Recruit 6-8 AI safety experts as panelists. For each benchmark item, ask each panelist: 'What proportion of minimally safe models would answer this item correctly?' Average these estimates across panelists and sum to get a cut score. Compute panelist disagreement (SD of estimates). Method 2 (Bookmark Method): Arrange items in order of estimated difficulty (from IRT calibration). Ask panelists to place a 'bookmark' where the performance transitions from unacceptably unsafe to acceptable. Average bookmark placements. Compare cut scores from both methods and to any existing thresholds. Quantify the uncertainty in the cut score using confidence intervals around the panelist estimates. Angoff and Bookmark standard-setting methods are established in educational credentialing. Intolerable Risk Threshold Recommendations (arXiv 2503.05812) calls for threshold operationalization but does not apply standard-setting methodology. This is achievable using only expert elicitation and descriptive statistics in R — no ML required.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Applying formal standard-setting methodology transforms deployment thresholds from arbitrary numbers into defensible, expert-grounded decisions with known uncertainty. This is directly actionable by evaluation designers and regulators. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI governance / psychometrics | **Strategy:** causal_chain_intervention | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong: determines what score should constitute a safety pass/fail. Directly enables regulatory decisions.
  - **low_compute:** 5, confidence: 0.9 — CPU-only analysis + expert judgment.
  - **accessible_complexity:** 3, confidence: 0.6 — Standard-setting requires understanding methodology and coordinating experts.
  - **narrow_scope:** 3, confidence: 0.5 — Requires expert panel. External dependency reduces tractability.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** causal_chain_intervention, sources: 0 KB, 0 web

---

## #77: Bookmark Standard Setting for AI Capability Thresholds (Score: 3.26)

**ID:** gen-114

**Research Question:** How can order safety evaluation items by irt-estimated difficulty (b-parameter) address the problem that while angoff is the most commonly discussed standard-setting method, the bookmark method — which asks panelists to identify the point in an irt-ordered item list where a minimally competent model transitions from likely-fail to likely-pass — has been shown to produce more valid cutoffs in medical assessments? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Order safety evaluation items by IRT-estimated difficulty (b-parameter). Create an Ordered Item Booklet (OIB). Convene expert panelists to identify the bookmark location for a 'minimally safe' model. Compute the corresponding theta (ability) value as the cut score. Run multiple rounds with between-round feedback. Compare Bookmark cut score to Angoff cut score from a parallel study. Analyze inter-rater agreement and cut score stability across rounds. Bookmark vs. Angoff validity comparison (PMC 7778792) found Bookmark had higher internal and external validity in medical performance tests. The Bookmark method requires pre-calibrated IRT item difficulties, making it a natural downstream application of IRT calibration work. This creates a research pipeline: IRT calibration -> Bookmark standard setting.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Closes the Success State 5 gap with an alternative standard-setting method validated in other high-stakes contexts. Comparing Bookmark and Angoff in the AI context generates evidence about which method is better suited to AI safety's unique properties (machine respondents, binary items, no fatigue effects). This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Standard Setting / Safety Thresholds | **Strategy:** backcast_from_success | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong: capability thresholds for governance. Same mechanism as gen-053.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Intermediate.
  - **narrow_scope:** 3, confidence: 0.5 — Expert panel dependency.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** backcast_from_success, sources: 0 KB, 0 web

---

## #78: Prompt Sensitivity as Measurement Error: A Systematic IRT Analysis of Paraphrase Invariance (Score: 3.26)

**ID:** gen-127

**Research Question:** How can create matched paraphrase sets: for each of 30-50 safety evaluation items, generate 5 paraphrased versions preserving semantic intent address the problem that ai model safety scores are known to change dramatically when prompts are paraphrased? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Create matched paraphrase sets: for each of 30-50 safety evaluation items, generate 5 paraphrased versions preserving semantic intent. Evaluate 10-15 models on all versions. For each base item, test whether IRT item parameters (b, a) are stable across paraphrases using item parameter drift analysis. Compute the within-item variance in model response as a component of total measurement error. Identify which item types (direct requests, jailbreak-style, roleplay) show the most paraphrase-induced variance. 'How Should AI Safety Benchmarks Benchmark Safety?' (2601.23112) identifies prompt paraphrasing as a core challenge. The 'Measuring what Matters' review flags response process validity as understudied. IRT parameter drift analysis (Frontiers 2025) provides the method. This is executable with publicly available model APIs and existing safety benchmark items.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Compute internal consistency reliability (Cronbach's alpha, split-half) and IRT-based reliability (test information function) for a safety benchmark, reporting confidence intervals around model ability estimates
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Addresses both Success State 4 (reproducibility) and Success State 2 (known measurement error bounds). Paraphrase sensitivity is the most discussed reliability problem in AI evaluation but has not been formally quantified as IRT measurement error. This study gives it a number and connects it to the broader reliability framework. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Measurement Reliability / Prompt Sensitivity | **Strategy:** backcast_from_success | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong: if paraphrasing prompts changes safety scores substantially, evaluation scores are unreliable. Directly affects deployment trust.
  - **low_compute:** 4, confidence: 0.7 — Requires API calls to test multiple prompt variants.
  - **accessible_complexity:** 3, confidence: 0.6 — IRT analysis across prompt variants. Intermediate.
  - **narrow_scope:** 3, confidence: 0.6 — Requires generating prompt variants and running evaluations. Multiple steps.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** backcast_from_success, sources: 0 KB, 0 web

---

## #79: IRT Person-Fit as a Sandbagging Detector: Psychometric Anomaly Detection for Strategic Underperformance (Score: 3.26)

**ID:** gen-155

**Research Question:** How can apply irt to a benchmark where model abilities are estimated across many items (e address the problem that irt assumption violations (failure a9) include the assumption that response patterns are consistent with an underlying ability estimate? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Apply IRT to a benchmark where model abilities are estimated across many items (e.g., MMLU or an equivalent with 100+ items). Compute person-fit statistics (lz, infit, outfit) for each model in R (mirt package). Identify models showing significant misfit — particularly underfitting at the high ability end (correct on hard items, wrong on easy items — a sandbag signature). Cross-reference misfit models with published sandbagging reports. Test whether misfit patterns cluster around dangerous-capability item types vs. benign items. Estimate statistical power to detect sandbagging of various magnitudes (20%, 40%, 60% strategic failure) under observed local dependence levels. IRT person-fit statistics are standard in educational measurement for detecting aberrant response patterns (cheating, carelessness). Sandbagging paper (arxiv 2406.07358) documents frontier model strategic underperformance. 'Lost in Benchmarks' and PSN-IRT papers provide IRT analysis infrastructure for LLM benchmarks. mirt package in R supports person-fit statistics.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Person-fit statistics are designed to detect exactly the anomalous pattern that sandbagging produces. Applying them to LLM safety evaluation is a direct application of psychometric anomaly detection to a concrete alignment problem. This makes sandbagging detection quantitative and principled rather than qualitative and ad hoc. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation & Benchmarking | **Strategy:** compounding_risks | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong chain: psychometric anomaly detection for strategic responding. Targets deceptive capability concealment.
  - **low_compute:** 4, confidence: 0.7 — May require some API calls for model evaluation.
  - **accessible_complexity:** 3, confidence: 0.6 — Requires deeper understanding of person-fit theory and strategic responding patterns. More conceptual complexity than basic protocol following.
  - **narrow_scope:** 3, confidence: 0.6 — Multiple analysis dimensions and simulation components. Less tightly scoped than gen-090.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** compounding_risks, sources: 0 KB, 0 web

---

## #80: Angoff Standard-Setting for AI Safety Cutoffs (Score: 3.26)

**ID:** gen-164

**Research Question:** How can convene a structured angoff panel of ai safety researchers who each estimate, item by item on an existing safety benchmark (e address the problem that ai safety benchmarks currently use arbitrary numeric cutoffs (e? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Convene a structured Angoff panel of AI safety researchers who each estimate, item by item on an existing safety benchmark (e.g., MLCommons AI Safety v0.5 or StrongREJECT), the probability that a 'minimally safe' model would answer correctly. Average these estimates across panelists to derive a principled cutoff score. Analyze inter-panelist agreement (intraclass correlation), compare the resulting threshold to current ad hoc cutoffs, and examine whether the Angoff-derived cutoff changes deployment recommendations for existing model evaluations. Run the exercise with two panels (safety researchers vs. AI ethicists) and compare results as a convergent validity check. The MLCommons AI Safety Benchmark v0.5 explicitly acknowledges that determining cutoffs is an open problem. The contrasting groups and Angoff methods are both well-validated in clinical skills assessment literature (PMC12409087). Educational measurement R tools (eatATA, mirt) support the analysis. No prior work appears to have used structured standard-setting methodology for AI safety benchmark thresholds.

**Experiments:** - Apply the proposed analysis method to item-level data from one public safety benchmark (e.g., TruthfulQA, HarmBench)
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Without principled standard-setting, AI safety thresholds are arbitrary and legally/ethically indefensible. Angoff panels have been used for decades in high-stakes credentialing (medical licensing, bar exams) to produce defensible cutoffs. Importing this methodology would make AI safety thresholds transparent, reproducible, and grounded in expert judgment rather than convention. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Alternative Framings:** Alternative 1: Narrow to a single-benchmark replication study focusing exclusively on item-level analysis of TruthfulQA, producing one definitive result.; Alternative 2: Comparative methodology study — apply 2-3 different psychometric methods to the same benchmark data and compare what each reveals about safety measurement quality.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Evaluations & Benchmarks | **Strategy:** methodology_bridging | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong: Angoff method for safety cutoffs. Enables evidence-based thresholds.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Angoff method. Intermediate.
  - **narrow_scope:** 3, confidence: 0.5 — Expert panel dependency.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** methodology_bridging, sources: 0 KB, 0 web

---

## #81: Bookmark Method Standard Setting for AI Safety Benchmarks (Score: 3.26)

**ID:** gen-190

**Research Question:** How can implement the bookmark method for a safety benchmark: (1) order items by their irt-estimated difficulty (probability that a model of any given safety level answers correctly) address the problem that ai safety benchmarks lack formal performance level descriptors (plds)—descriptions of what a model at each safety level actually does and does not do? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Implement the Bookmark method for a safety benchmark: (1) Order items by their IRT-estimated difficulty (probability that a model of any given safety level answers correctly). (2) Create an Ordered Item Booklet (OIB) presenting items from easiest to hardest. (3) Have a panel of AI safety experts 'bookmark' the location where the transition from one performance level to the next occurs. (4) Average bookmarks across panelists to set the cutoff. (5) Develop PLDs describing what models at each level do. (6) Compare Bookmark-derived cutoffs to Angoff-derived cutoffs and current ad hoc thresholds. Bookmark vs. Angoff comparison studies show Bookmark produces higher validity indices (BMC Medical Education 2020). The Bookmark method is used for NAEP, ACCUPLACER, and other high-stakes assessments. R packages for IRT difficulty estimation (eRm, mirt, TAM) provide the necessary inputs. AI safety benchmarks lack formal PLDs that could guide deployment decisions. No published work applies Bookmark methodology to AI safety evaluation.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. The Bookmark method is the most widely used alternative to Angoff for high-stakes standard setting and has shown superior validity in medical education (BMC Medical Education 2020). It produces not just cutoffs but interpretable descriptions of what each performance level means—critical for regulatory communication. An OIB requires IRT difficulty estimates plus expert judgment, with no heavy coding required. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Evaluations & Benchmarks | **Strategy:** methodology_bridging | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong: bookmark method for governance thresholds.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Intermediate.
  - **narrow_scope:** 3, confidence: 0.5 — Expert panel dependency.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** methodology_bridging, sources: 0 KB, 0 web

---

## #82: IRT Dimensionality Assessment of Dangerous-Capability Evaluations: Is Biosecurity Risk Unidimensional? (Score: 3.22)

**ID:** gen-132

**Research Question:** How can using published item sets from dangerous-capability evaluations (aisi, metr, or research papers describing cbrn eval items), apply dimensionality assessment: parallel analysis, map criterion, and mirt exploratory analysis (all in mirt) address the problem that dangerous-capability evaluations (e? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using published item sets from dangerous-capability evaluations (AISI, METR, or research papers describing CBRN eval items), apply dimensionality assessment: parallel analysis, MAP criterion, and MIRT exploratory analysis (all in mirt). Compute model fit for 1-factor, 2-factor, and 3-factor solutions. Interpret factor loadings in terms of capability subdimensions. Test whether multidimensional theta vectors better predict expert-rated uplift potential than unidimensional scores. METR and AISI both conduct dangerous-capability evaluations but report aggregate scores. Parallel analysis and MAP criterion are standard in mirt. Human vs. AI-generated test dimensionality study (arxiv 2510.24739) applies similar methods. CBRN evaluation item sets are partially described in published AISI and METR evaluation reports.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Directly relevant to Success State 1 (validated construct definitions for dangerous capabilities). If bioweapon capability is multidimensional, the field needs multiple separate measurements rather than a single score — and models could pass on one dimension while failing on another. This has immediate implications for capability evaluation protocols. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 5), low_compute (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Dangerous Capability Evaluation / Dimensionality | **Strategy:** backcast_from_success | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 5, confidence: 0.7 — Compelling: if biosecurity and cybersecurity capability are independent dimensions, a single 'dangerous capability' score masks critical domain-specific risks. Targets recognized pathway.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 2, confidence: 0.5 — MIRT dimensionality assessment of dangerous capabilities. Advanced.
  - **narrow_scope:** 3, confidence: 0.6 — Multiple capability domains to analyze.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** backcast_from_success, sources: 0 KB, 0 web

---

## #83: Population Definition Problem: IRT Ability Estimates Under Different Model Sampling Strategies (Score: 3.17)

**ID:** gen-020

**Research Question:** How can using open llm leaderboard item-level data for a capability benchmark, calibrate irt item parameters using five different model subsets: (1) all 5000+ models, (2) only models >70b parameters, (3) only models <13b, (4) only instruction-tuned models, (5) a random stratified sample address the problem that irt ability estimates depend on the calibration population? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using Open LLM Leaderboard item-level data for a capability benchmark, calibrate IRT item parameters using five different model subsets: (1) all 5000+ models, (2) only models >70B parameters, (3) only models <13B, (4) only instruction-tuned models, (5) a random stratified sample. Compare item difficulty estimates (b-parameters) and model ability estimates (theta) across calibration populations. Compute variance in b-parameter estimates across calibration sets. Discuss implications for the stability of safety benchmark scores under different evaluation populations. Open problem 2 (population definition for LLMs); Open LLM Leaderboard with 5000+ models; tinyBenchmarks (1.9% error with 100 items); IRT population assumptions (open problem 14 in MTAI); mirt R package for calibration.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If IRT item parameters change substantially depending on which models are included in calibration, safety benchmark scores are population-dependent and cannot be meaningfully compared across evaluation contexts. This directly addresses open problem 2 and has immediate practical implications for how evaluation organizations like METR and AISI should design their model pools. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** IRT Population Assumptions / Calibration | **Strategy:** novel_direction | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 2, confidence: 0.6 — Methodological: how calibration population affects estimates. Important but no specific catastrophic risk chain.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Subsampling and IRT refitting. Intermediate.
  - **narrow_scope:** 4, confidence: 0.7 — Tightened: one benchmark, five model subsets, clear deliverable.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** novel_direction, sources: 0 KB, 0 web

---

## #84: Efficiency Frontier of Safety Benchmark Subsampling: IRT vs. Random vs. Stratified Item Selection (Score: 3.17)

**ID:** gen-049

**Research Question:** How can using safety benchmark item-level data (truthfulqa or similar), compare three item-selection strategies at multiple sample sizes (10, 25, 50, 100 items): (1) random selection, (2) stratified-by-difficulty selection, (3) irt-optimal selection (mirtcat in r) address the problem that tinybenchmarks showed irt-based item selection outperforms random selection for mmlu? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using safety benchmark item-level data (TruthfulQA or similar), compare three item-selection strategies at multiple sample sizes (10, 25, 50, 100 items): (1) random selection, (2) stratified-by-difficulty selection, (3) IRT-optimal selection (mirtCAT in R). For each strategy and sample size, compute RMSE and Spearman rank-correlation against full-benchmark scores. Plot efficiency frontiers. tinyBenchmarks (arXiv 2402.14992); mirtCAT in R for IRT-based CAT simulation; TruthfulQA; stratified sampling in R; RMSE and rank-correlation as efficiency metrics.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If IRT-based selection provides only marginal benefit over stratified random sampling for safety benchmarks, practitioners can use simpler methods without psychometric software, lowering the barrier to efficient safety evaluation. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** IRT / CAT / Safety Benchmarking | **Strategy:** follow_up_experiment | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 2, confidence: 0.6 — Vague: compares item selection strategies. Methodological without specific catastrophic risk chain.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Three strategies to implement and compare. Intermediate.
  - **narrow_scope:** 4, confidence: 0.7 — Tightened to single benchmark comparison.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** follow_up_experiment, sources: 0 KB, 0 web

---

## #85: Surprisal-Based Difficulty Estimation as a Cross-Benchmark Item Calibration Tool (Score: 3.17)

**ID:** gen-070

**Research Question:** How can import surprisal theory from psycholinguistics: compute surprisal (negative log probability of each token in an item) as a proxy for item complexity address the problem that safety benchmark item difficulty is typically estimated empirically (proportion of models that pass), which requires running many models on every item? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Import surprisal theory from psycholinguistics: compute surprisal (negative log probability of each token in an item) as a proxy for item complexity. Use this as an a priori difficulty estimate and test its correlation with empirical item difficulty from IRT-calibrated safety benchmarks. Extend to compute 'semantic surprisal' using sentence embedding distances. Validate by splitting items into tertiles by surprisal and checking whether empirical difficulty monotonically increases. Implement in R with a pre-trained language model API (read-only). Psycholinguistics literature shows LM surprisal outperforms cloze probability as a difficulty predictor (arXiv 2601.09886, PLOS Comput Biol 2024). arXiv IRT-LLM papers calibrate empirical difficulty. This is a validation study correlating two measures in R—no model training, just API calls for probability scores.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Surprisal-based item difficulty estimation would allow benchmark designers to calibrate item difficulty without running full model evaluations—dramatically accelerating benchmark development and enabling rapid generation of calibrated new items to counter benchmark saturation. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 4), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation & Benchmarking | **Strategy:** cross_domain_transfer | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 2, confidence: 0.6 — Methodological: predicting difficulty from surprisal. No specific catastrophic risk chain.
  - **low_compute:** 4, confidence: 0.7 — Requires API calls for surprisal computation.
  - **accessible_complexity:** 3, confidence: 0.6 — Surprisal computation + correlation. Intermediate.
  - **narrow_scope:** 4, confidence: 0.7 — Focused: correlate surprisal with empirical difficulty. Clear deliverable.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** cross_domain_transfer, sources: 0 KB, 0 web

---

## #86: Information-Optimal Item Selection for Safety CAT (Score: 3.17)

**ID:** gen-210

**Research Question:** How can using calibrated irt parameters from a safety item bank, compute the fisher information function for each item across the latent safety ability range (theta from -3 to +3) address the problem that create adaptive safety evaluation (cat for safety)? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using calibrated IRT parameters from a safety item bank, compute the Fisher information function for each item across the latent safety ability range (theta from -3 to +3). Identify which items are maximally informative at different ability levels (easy items for low-safety models, hard items for high-safety models). Simulate the information-optimal item selection procedure and visualize the test information function for different item selection strategies (maximum information, b-matching, random). The CAT-for-LLMs literature ('Adaptive Testing for LLM Evaluation', 2025; 'Confident Rankings with Fewer Items', 2026) implements maximum information selection for general capability benchmarks. The extension to safety requires calibrated safety-specific parameters. Fisher information computation is a standard mirt output, requiring no additional coding beyond the calibration step.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Simulate computerized adaptive testing item selection on existing benchmark data and compare measurement precision (standard error of theta) against full-length administration
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. For adaptive safety evaluation to work, item selection must be theoretically grounded. Maximum Fisher information item selection maximizes measurement precision at the current ability estimate. Understanding which safety items are informative at which ability levels reveals the structure of the item bank and identifies gaps (e.g., too few high-difficulty items for frontier models). This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation / Psychometrics | **Strategy:** problem_decomposition | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 2, confidence: 0.6 — Methodological: optimal item selection. No specific catastrophic risk chain.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Intermediate.
  - **narrow_scope:** 4, confidence: 0.7 — Focused study.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** problem_decomposition, sources: 0 KB, 0 web

---

## #87: 1-Factor vs. Multi-Factor LLM Capability: Testing Dimensionality Using CFA (Score: 3.17)

**ID:** gen-214

**Research Question:** How can collect subscale-level benchmark scores for 50+ models from the open llm leaderboard and helm (covering math reasoning, language understanding, coding, commonsense, etc address the problem that determine if llm capabilities are unidimensional or multidimensional? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Collect subscale-level benchmark scores for 50+ models from the Open LLM Leaderboard and HELM (covering math reasoning, language understanding, coding, commonsense, etc.). Fit competing CFA models in R (lavaan): (1) one general factor, (2) two factors (reasoning vs. knowledge), (3) four domain-specific factors. Compare fit using CFI, RMSEA, SRMR. Test whether a bifactor model (one general + domain-specific residual factors) fits better than either pure model. 'A Data-Driven Study on LLM Structure and Development' (EMNLP 2025) takes a data-driven approach to LLM structure. The PSN-IRT paper (2025) found benchmarks have 'uneven measurement properties' suggesting multidimensionality. CFA in lavaan is directly accessible to psychometrically-trained users and requires no ML training. Open LLM Leaderboard provides the data.

**Experiments:** - Apply the proposed analysis method to item-level data from one public safety benchmark (e.g., TruthfulQA, HarmBench)
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If LLM capabilities are truly unidimensional (one general intelligence factor), then single aggregate leaderboard scores are scientifically defensible. If multidimensional, different benchmarks measure genuinely different abilities and aggregate scores are misleading. This has direct implications for how safety capability tradeoffs are conceptualized. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation / Psychometrics | **Strategy:** problem_decomposition | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 2, confidence: 0.6 — Methodological: CFA testing of dimensionality. Generic.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — CFA requires structural equation modeling knowledge. Intermediate.
  - **narrow_scope:** 4, confidence: 0.7 — Focused model comparison study.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** problem_decomposition, sources: 0 KB, 0 web

---

## #88: G-Theory Study of IRT Ability Estimation Instability Across Model Families (Score: 3.17)

**ID:** gen-262

**Research Question:** How can apply g-theory to quantify how much variance in irt ability estimates is attributable to the calibration sample's model-family composition vs address the problem that p6: cold-start problem: irt fails for unseen model families? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Apply G-Theory to quantify how much variance in IRT ability estimates is attributable to the calibration sample's model-family composition vs. item choice vs. the model being measured, establishing how much the cold-start problem inflates estimation uncertainty. IRT applied to AI benchmarks is established (ICLR 2025 MetaBench, IrtNet arxiv 2510.00844). The cold-start problem is documented in cognitive diagnosis literature (Springer 2025 on zero-shot cross-domain diagnosis). A G-study crossing models x model_families x items would reveal the family-generalizability coefficient. Feasible in R using public leaderboard data.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. When a new model family (e.g., a new architecture) enters the benchmark, IRT item parameters calibrated on existing models may not transfer. G-Theory can quantify how large this source of variance is relative to other sources, giving a principled estimate of how much to discount IRT-derived scores for unseen model families. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation / Psychometrics | **Strategy:** combinatorial_matrix | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 2, confidence: 0.6 — Methodological.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — G-theory application. Intermediate.
  - **narrow_scope:** 4, confidence: 0.7 — Focused study.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** combinatorial_matrix, sources: 0 KB, 0 web

---

## #89: Score Equating to Enable Cross-Family IRT Comparisons for New Model Architectures (Score: 3.17)

**ID:** gen-263

**Research Question:** How can apply irt-based score equating using anchor items to link ability estimates from a new model family to the existing irt scale, testing whether a small set of anchor items can provide sufficient linkage for cold-start models without full recalibration address the problem that p6: cold-start problem: irt fails for unseen model families? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Apply IRT-based score equating using anchor items to link ability estimates from a new model family to the existing IRT scale, testing whether a small set of anchor items can provide sufficient linkage for cold-start models without full recalibration. IRT equating methods are more accurate and stable than CTT methods (Assessment Systems). The three equating approaches (concurrent calibration, fixed parameter, Stocking-Lord) are all implementable in mirt R package. This would require selecting anchor items from an existing calibrated benchmark and fitting them for a new-family model—a tractable 30-hour project.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Score equating is the standard psychometric solution when new test forms need to be linked to an established scale without re-administering all items. Applying it to the cold-start problem in AI benchmarking would allow new model families to receive calibrated ability estimates using only a subset of anchor items, dramatically reducing evaluation cost. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation / Psychometrics | **Strategy:** combinatorial_matrix | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 2, confidence: 0.6 — Methodological: equating for new model architectures.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.5 — Equating. Intermediate.
  - **narrow_scope:** 4, confidence: 0.7 — Focused study.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** combinatorial_matrix, sources: 0 KB, 0 web

---

## #90: CAT-Based Cold-Start Protocol: Efficient Ability Estimation for New Model Families (Score: 3.17)

**ID:** gen-264

**Research Question:** How can design a computerized adaptive testing protocol using a pre-calibrated safety item bank to efficiently place new model families on the ability scale, requiring far fewer items than full benchmark administration while maintaining precision address the problem that p6: cold-start problem: irt fails for unseen model families? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Design a Computerized Adaptive Testing protocol using a pre-calibrated safety item bank to efficiently place new model families on the ability scale, requiring far fewer items than full benchmark administration while maintaining precision. CAT is well-established in high-stakes testing (NCLEX, GRE). The catR R package implements full CAT simulations. Pre-calibrated item banks from Allenai's Fluid Benchmarking or MetaBench exist. A CAT simulation study on existing data—testing how quickly ability estimates stabilize for held-out model families—is feasible within 30 hours.

**Experiments:** - Simulate computerized adaptive testing item selection on existing benchmark data and compare measurement precision (standard error of theta) against full-length administration
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. CAT can achieve 50% item reduction while maintaining measurement precision equivalent to full-form testing. For the cold-start problem, a CAT protocol using information-maximizing item selection could rapidly locate a new model's ability level using only 20-30 items rather than full benchmark administration. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation / Psychometrics | **Strategy:** combinatorial_matrix | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 2, confidence: 0.6 — Vague: cold-start protocol for new model families. Methodological but doesn't trace to specific catastrophic risk.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Intermediate CAT work.
  - **narrow_scope:** 4, confidence: 0.7 — Focused protocol design.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** combinatorial_matrix, sources: 0 KB, 0 web

---

## #91: The Unknown Unknowns Trap: Known-Risk Bias and Novel Capability Emergence (Score: 3.13)

**ID:** gen-142

**Research Question:** How can perform a systematic map of existing ai safety benchmarks (drawing on the 'how should ai safety benchmarks benchmark safety?' taxonomy and related surveys) address the problem that 170 ai safety benchmarks test known risks while only 2 test for unknowns (failure a8 — known-risk bias)? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Perform a systematic map of existing AI safety benchmarks (drawing on the 'How Should AI Safety Benchmarks Benchmark Safety?' taxonomy and related surveys). Categorize each benchmark by: (a) risk type (known/unknown), (b) capability domain, (c) methodology. Use IRT-inspired information curve logic conceptually: in what 'ability region' does each benchmark provide measurement information? Identify the whitespace — capability regions with no benchmark coverage. Supplement with an expert elicitation exercise: invite 3–5 AI safety researchers to name emerging capability risks not covered by any current benchmark, and map the gap structurally. Produce a 'measurement coverage map.' 'How Should AI Safety Benchmarks Benchmark Safety?' explicitly documents the 170:2 ratio. FORTRESS and CBRN evaluation work document emerging capability benchmarking gaps. The International AI Safety Report 2025 highlights unknown capability risks as a key evaluation gap.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Novel emergent capabilities are the tail risk most dangerous to AI safety. The structural bias toward known risks means that the evaluation ecosystem provides no early warning for genuinely novel dangers. A coverage map makes this gap visible and prioritizable. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 5), accessible_complexity (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation & Benchmarking | **Strategy:** compounding_risks | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.6 — Strong: known-risk bias means evaluations only test for anticipated failures, missing novel capability emergence. Targets recognized pathway.
  - **low_compute:** 5, confidence: 0.9 — Analytical study.
  - **accessible_complexity:** 4, confidence: 0.6 — Conceptual analysis comparing evaluation coverage against capability space. Accessible.
  - **narrow_scope:** 2, confidence: 0.5 — Conceptually broad — what constitutes 'novel capability emergence' is open-ended.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** compounding_risks, sources: 0 KB, 0 web

---

## #92: The Cold Start Blindspot: New Model Families and Oversight Gaps in Multi-Agent Systems (Score: 3.04)

**ID:** gen-145

**Research Question:** How can identify 2–3 recently released model families that represent genuine architectural novelty (e address the problem that the cold-start problem in ai evaluation (failure a10) — the lack of calibrated benchmarks for genuinely novel model architectures — compounds with oversight failures in multi-agent systems (failure b10)? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Identify 2–3 recently released model families that represent genuine architectural novelty (e.g., mixture-of-experts at new scale, long-context-native architectures). For each, document: (a) how many published safety benchmarks include results for that family, (b) whether IRT or psychometric calibration has been done, (c) what multi-agent evaluation coverage exists. Treat this as a construct validity and measurement coverage analysis. Develop a 'readiness checklist' for evaluating a new model family before agentic deployment, drawing on established psychometric standards for new test populations. Multi-agent evaluation gaps documented in 2025 survey of 120 agent evaluation frameworks. Cold-start problem analogy drawn from IRT: ability estimation is unreliable for new populations not represented in item calibration samples. International AI Safety Report 2025 documents novel architecture deployment risks.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. The fastest-growing AI deployment context is multi-agent, and it is precisely the context where individual model evaluation is most critical for system-level safety. If we cannot evaluate new model architectures on entry, we are deploying them into multi-agent settings blind. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), accessible_complexity (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation & Benchmarking | **Strategy:** compounding_risks | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 2, confidence: 0.5 — Vague: cold-start problems for new architectures. Important but chain to catastrophic risk is underspecified.
  - **low_compute:** 5, confidence: 0.9 — Analytical.
  - **accessible_complexity:** 4, confidence: 0.7 — Accessible analysis of oversight gaps.
  - **narrow_scope:** 3, confidence: 0.5 — Conceptual scope is broad.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** compounding_risks, sources: 0 KB, 0 web

---

## #93: Bifactor Modeling of AI Safety Benchmarks: Is There a General Safety Factor? (Score: 3.00)

**ID:** gen-006

**Research Question:** How can collect model scores at the item level (or subtask level) across 4-6 safety benchmarks (truthfulqa, wildguard, harmbench, bbq, stereoset, air-bench) address the problem that a single factor explains 79? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Collect model scores at the item level (or subtask level) across 4-6 safety benchmarks (TruthfulQA, WildGuard, HarmBench, BBQ, StereoSet, AIR-Bench). Using the mirt R package, fit: (1) a unidimensional IRT model, (2) a correlated-factors MIRT model with theoretically specified dimensions, (3) a bifactor model with a general safety factor plus specific benchmark factors. Compare models using AIC/BIC and omega-hierarchical. Report explained common variance (ECV) and omega-hierarchical to determine how much of reliable safety variance is general vs. specific. Paper 13 (model size confound for g-factor); arxiv:2503.06378 (general scales for AI evaluation); Open LLM Leaderboard; mirt R package documentation; bifactor model literature in psychometrics (Frontiers 2018).

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If a strong general safety factor exists, a single efficient safety score is defensible. If safety is genuinely multidimensional, composite scores obscure important distinctions. This directly answers whether current single-number safety ratings are psychometrically sound, and guides how to structure future safety evaluation frameworks. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** arXiv:2503.06378

**Subfield:** MIRT / Bifactor Analysis / Safety Construct Structure | **Strategy:** novel_direction | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: determines whether single safety score is defensible. If multidimensional, composite scores are invalid.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.5 — Bifactor models require specialist knowledge. Even with guided protocol, interpretation is challenging for beginners.
  - **narrow_scope:** 3, confidence: 0.5 — Requires collecting data across 4-6 benchmarks and fitting multiple competing models. Sustained effort.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** novel_direction, sources: 0 KB, 0 web

---

## #94: Graded Response Model for Partial Safety Credit: Beyond Binary Pass/Fail (Score: 3.00)

**ID:** gen-007

**Research Question:** How can reannotate a subset of an existing safety dataset (e address the problem that most safety benchmarks treat model responses as binary (safe/unsafe), discarding information about severity of harm or degree of refusal? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Reannotate a subset of an existing safety dataset (e.g., 200-300 items from HarmBench or WildGuard) with a 3-4 level ordinal safety rubric (complete safe response, borderline, partial harm, severe harm) using human or LLM-as-judge ratings. Fit a GRM in R (mirt or ltm) to the polytomous responses across 30+ models. Compare model ability estimates from GRM against binary IRT estimates and against original benchmark scores. Report item characteristic curves for key safety items. Graded Response Model literature (Samejima); LLM-as-judge rubric-based scoring is now mainstream (Promptfoo, 2025); mirt R package supports GRM; WildGuard and HarmBench have published response data; partial credit in AI evaluation is a documented gap.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Binary pass/fail scoring throws away information about the magnitude of safety failures. A GRM provides more precise model ability estimates and reveals the probability of each harm level as a function of model safety ability. This is directly useful for regulatory thresholds: distinguishing 'occasionally mildly harmful' from 'rarely severely harmful' models. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Graded Response Models / Ordinal Safety Scoring | **Strategy:** novel_direction | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: GRM recovers severity information. Connection to specific catastrophic risk has gaps.
  - **low_compute:** 4, confidence: 0.7 — GRM fitting plus reannotation effort.
  - **accessible_complexity:** 3, confidence: 0.5 — Requires reannotating items and understanding GRM. Intermediate after refinement.
  - **narrow_scope:** 3, confidence: 0.5 — Requires reannotation of subset (200-300 items) plus GRM fitting. Sustained effort.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** novel_direction, sources: 0 KB, 0 web

---

## #95: Temporal Item Parameter Drift in Safety Benchmarks: An IRT Stability Study (Score: 3.00)

**ID:** gen-008

**Research Question:** How can use archived open llm leaderboard data from at least three time points (e address the problem that ai capabilities evolve rapidly through fine-tuning and new releases, but safety benchmark items are treated as static with fixed difficulty? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Use archived Open LLM Leaderboard data from at least three time points (e.g., 2023, 2024, 2025 snapshots). For a fixed set of benchmark items, fit separate 2PL IRT models at each time point using models that existed at that time. Compare item difficulty (b) and discrimination (a) parameters across time using parameter drift detection methods (e.g., item-level chi-square tests between calibration samples). Report which item types (factual safety, refusal, reasoning under ambiguity) show most drift and discuss implications for benchmark longevity. Temporal drift in retrieval benchmarks (arxiv:2603.04532); Open LLM Leaderboard archives; IRT item calibration drift literature in educational testing; tinyBenchmarks paper notes benchmark saturation; temporal consistency evaluation trending in 2025 (TechRxiv).

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If item parameters drift, safety benchmarks become non-comparable across time—a 70% safety score in 2023 is not the same as 70% in 2025. Temporal IRT drift analysis provides the psychometric evidence base for when benchmarks need recalibration or retirement, directly addressing the temporal stability open problem in measurement-theoretic AI evaluation. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** arXiv:2603.04532

**Subfield:** IRT Item Calibration Drift / Temporal Validity | **Strategy:** novel_direction | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: if item parameters drift, benchmarks become non-comparable across time. Important for longitudinal safety monitoring.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Requires understanding IRT calibration across time windows. Intermediate.
  - **narrow_scope:** 3, confidence: 0.6 — Reduced to single analysis but still requires multiple time-point comparisons.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** novel_direction, sources: 0 KB, 0 web

---

## #96: Test Equating Safety Benchmarks: Putting TruthfulQA and WildGuard on a Common Scale (Score: 3.00)

**ID:** gen-012

**Research Question:** How can identify items or item types that appear in two or more safety benchmarks (or create a small set of anchor items scored on multiple benchmarks for a set of models) address the problem that different safety benchmarks (truthfulqa, wildguard, harmbench, stereoset) produce scores on incomparable scales, making it impossible to say a model is 'safer overall'? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Identify items or item types that appear in two or more safety benchmarks (or create a small set of anchor items scored on multiple benchmarks for a set of models). Use IRT concurrent calibration (mirt R package) or fixed-parameter linking to place at least two safety benchmarks on a common latent scale. Compute linked safety ability estimates for 30+ models. Compare rankings before and after equating. Assess equating precision using the standard error of equating. Test equating fundamentals (cogn-iq.org 2025 summary); IRT equating via concurrent calibration; Artificial Analysis Intelligence Index v4.0 combines multiple benchmarks but without formal equating; metabench and tinyBenchmarks work toward common benchmarking but without explicit IRT equating.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. A common safety scale would allow meaningful aggregation across benchmarks and a defensible overall safety ranking. This is the measurement foundation for any future 'safety index' or composite safety score. Test equating is standard practice in educational assessment but has never been applied across AI safety benchmarks. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Test Equating / IRT Linking | **Strategy:** novel_direction | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: common scale enables cross-benchmark comparison. Foundational for meta-analysis.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.5 — IRT equating requires specialist knowledge. Guided but conceptually demanding.
  - **narrow_scope:** 3, confidence: 0.6 — Reduced to two benchmarks but equating still involves multiple steps.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** novel_direction, sources: 0 KB, 0 web

---

## #97: MIRT Subscale Structure of a Safety Benchmark: Testing Unidimensionality vs. Multidimensionality (Score: 3.00)

**ID:** gen-019

**Research Question:** How can use a safety benchmark with clear thematic subtasks (e address the problem that open problem 6 in measurement-theoretic ai evaluation is whether unidimensional irt is sufficient or whether mirt is needed? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Use a safety benchmark with clear thematic subtasks (e.g., AIR-Bench 2024 with its four risk domains: system/operational risks, content safety, societal risks, legal risks). Extract item-level model responses from published data. In R (mirt package), fit: (1) one-factor unidimensional model, (2) 4-factor correlated MIRT model aligned with AIR-Bench categories, (3) bifactor model. Compare using AIC/BIC. Compute dimensionality indices (DETECT, explained common variance). Report whether safety performance on AIR-Bench is best characterized as one ability or four correlated abilities. Open problem 6 (MIRT vs. unidimensional IRT); MEDIRT framework for medical LLMs (arxiv:2509.24186) uses 11 unidimensional models per topic; AIR-Bench 2024 has 4 risk domains; mirt R package supports MIRT; Open LLM Leaderboard scores available.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. The dimensionality question determines whether a single safety score is scientifically defensible. If safety is multidimensional, claiming a model is 'safe overall' based on a composite score is psychometrically invalid. This analysis would provide the first MIRT-based empirical answer to open problem 6 for a safety-specific benchmark. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** arXiv:2509.24186

**Subfield:** MIRT / Dimensionality / Safety Construct Structure | **Strategy:** novel_direction | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: tests unidimensionality. Same chain as gen-006.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.5 — MIRT with competing models. Intermediate-to-advanced.
  - **narrow_scope:** 3, confidence: 0.6 — Multiple models to fit and compare.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** novel_direction, sources: 0 KB, 0 web

---

## #98: CAT Transfer to Safety-Relevant Non-Knowledge Domains (Score: 3.00)

**ID:** gen-036

**Research Question:** How can using a public safety benchmark with item-level scores (e address the problem that medical cat achieved r=0? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using a public safety benchmark with item-level scores (e.g., AdvBench, TruthfulQA, or HELM safety tasks), calibrate a MIRT model in R (mirt package). Simulate CAT administration to 20–30 models and compare CAT-estimated ability scores to full-bank scores. Compute correlation and mean absolute error. Compare convergence curves (items needed) against the medical benchmark result. arXiv 2603.23506 (medical CAT, r=0.988, 1.3% items); mirt CAT simulation (mirtCAT package in R); TruthfulQA, AdvBench public data; MIRT for multidimensional domains.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Simulate computerized adaptive testing item selection on existing benchmark data and compare measurement precision (standard error of theta) against full-length administration
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If CAT efficiency does not transfer to safety domains, the efficiency gains exploited by adaptive testing are specific to knowledge domains and cannot be used to speed up safety evaluations. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** CAT / Adaptive Testing / Safety Benchmarking | **Strategy:** follow_up_experiment | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: tests whether CAT efficiency transfers to safety domains. Important methodological question.
  - **low_compute:** 5, confidence: 0.9 — CPU-only simulation.
  - **accessible_complexity:** 3, confidence: 0.5 — Requires understanding CAT and MIRT. Intermediate complexity after refinement.
  - **narrow_scope:** 3, confidence: 0.6 — Reduced scope but still involves calibrating MIRT model and simulating CAT across domains.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** follow_up_experiment, sources: 0 KB, 0 web

---

## #99: Multidimensional IRT Analysis of Safety Benchmarks: How Many Dimensions Are Safety Scores? (Score: 3.00)

**ID:** gen-045

**Research Question:** How can using item-level responses to truthfulqa (or a composite of truthfulqa + harmbench categories) from 30+ models, conduct: (1) a dimensionality assessment via parallel analysis and map (minimum average partial) on the tetrachoric correlation matrix (psych package in r), (2) fit unidimensional and 2–3 dimensional mirt models (mirt package), (3) compare fit via rmsea, cfi, and bic address the problem that standard safety benchmark analysis assumes unidimensionality — that a single 'safety' trait underlies all items? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using item-level responses to TruthfulQA (or a composite of TruthfulQA + HarmBench categories) from 30+ models, conduct: (1) a dimensionality assessment via parallel analysis and MAP (minimum average partial) on the tetrachoric correlation matrix (psych package in R), (2) fit unidimensional and 2–3 dimensional MIRT models (mirt package), (3) compare fit via RMSEA, CFI, and BIC. Report whether safety is empirically unidimensional. MIRT models in R (mirt package); dimensionality testing via parallel analysis; TruthfulQA; HELM safety tasks; Reckase (2009) multidimensional IRT.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. IRT has not been applied to safety benchmarks (per project open problems). If safety is multidimensional, composite safety scores are psychometrically invalid, and multidimensional scores are needed for accurate model comparison. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** IRT / Safety Benchmarking | **Strategy:** follow_up_experiment | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: determines dimensionality. Generic measurement quality.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.5 — Parallel analysis, MAP, competing MIRT models. Intermediate.
  - **narrow_scope:** 3, confidence: 0.6 — Multiple analyses (parallel analysis, MAP, model comparison).
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** follow_up_experiment, sources: 0 KB, 0 web

---

## #100: Longitudinal IRT: Are Safety Benchmark Items Becoming Easier Over Model Generations? (Score: 3.00)

**ID:** gen-050

**Research Question:** How can using open llm leaderboard data sorted by model release date, split models into three cohorts (early, mid, recent release dates, ~30 models each) address the problem that benchmark saturation is well-documented? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using Open LLM Leaderboard data sorted by model release date, split models into three cohorts (early, mid, recent release dates, ~30 models each). Fit separate 2PL IRT models in R (mirt) for each cohort. Compare b-parameter estimates for the same items across cohorts using Tucker's congruence coefficient and Bland-Altman plots. Test parameter invariance formally using multi-group IRT (MIRT with group constraints). Open LLM Leaderboard chronological data; mirt multi-group IRT; parameter invariance testing; Tucker congruence coefficient; Bland-Altman method for agreement analysis.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If IRT item parameters shift over model generations, a benchmark calibrated in 2023 cannot validly compare 2025 models on the same scale — a critical problem for longitudinal safety monitoring. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** IRT / Measurement Invariance / Safety Benchmarking | **Strategy:** follow_up_experiment | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: parameter invariance across model generations. Same mechanism as gen-008.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.5 — Multi-group IRT. Intermediate.
  - **narrow_scope:** 3, confidence: 0.6 — Multiple cohorts to compare.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** follow_up_experiment, sources: 0 KB, 0 web

---

## #101: IRT-Based Equipercentile Equating to Compare Models Across Different Safety Benchmarks (Score: 3.00)

**ID:** gen-054

**Research Question:** How can apply irt-based equating: calibrate item parameters for both benchmarks on a shared set of 'anchor items' (common items or a common sample of models), then transform scores onto a single latent scale address the problem that gpt-4o is evaluated on harmbench while gemini ultra is evaluated on wildguard? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Apply IRT-based equating: calibrate item parameters for both benchmarks on a shared set of 'anchor items' (common items or a common sample of models), then transform scores onto a single latent scale. Alternatively, use equipercentile equating if IRT assumptions are not met. Use the Open LLM Leaderboard data where multiple models have been tested on multiple benchmarks, identify overlapping models as a 'virtual anchor group,' and produce linked scores. Report model rankings before and after equating to show divergences. Implement in R (equate package). IRT equating literature shows separate calibration procedures outperform concurrent calibration. arXiv 2505.15055 and Stanford CRFM work already fit IRT models to LLM benchmark data. The equate R package implements equipercentile and IRT-based equating. Open LLM Leaderboard provides multi-benchmark multi-model data publicly.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Cross-benchmark equating is prerequisite for any meta-analysis of AI safety, for regulatory comparisons across labs, and for tracking safety progress over time as benchmarks are updated. The psychometric equating literature has 70 years of theory directly applicable to this problem. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation & Benchmarking | **Strategy:** cross_domain_transfer | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: enables cross-benchmark model comparison.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.5 — Equating methods require specialist knowledge.
  - **narrow_scope:** 3, confidence: 0.6 — Multiple steps and benchmarks.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** cross_domain_transfer, sources: 0 KB, 0 web

---

## #102: Benchmark Saturation Audit: IRT Test Information Functions Across a Family of Capability Benchmarks (Score: 3.00)

**ID:** gen-086

**Research Question:** How can using publicly available model response data from multiple benchmarks (e address the problem that when benchmarks saturate (risk 7), capability differences become invisible? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using publicly available model response data from multiple benchmarks (e.g., HELM data, OpenLLM leaderboard data, BIG-Bench outputs), fit 2PL IRT models in R for each benchmark subset. Plot the test information function for each benchmark showing the ability range where information exceeds a reliability threshold (e.g., I(theta) > 3, corresponding to reliability ~0.67). On the same plot, overlay the distribution of estimated model abilities for current frontier models. Identify the 'information gap' — the portion of the current model ability range where each benchmark provides sub-threshold information. Rank benchmarks by coverage of the frontier ability range. Publish the resulting TIF gallery as a benchmark selection guide. MMLU saturation (>90% by late 2024) is documented. HLE was created explicitly because of saturation. IRT for LLM evaluation is active (arXiv 2505.15055). Test information functions are standard IRT outputs from the 'mirt' R package. This analysis requires only existing public response data, no new experiments.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. A benchmark with high average performance but low information at the frontier provides a false sense of discrimination. TIFs make benchmark obsolescence visible and objective, enabling evidence-based benchmark retirement or supplementation decisions. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI evaluation / psychometrics | **Strategy:** causal_chain_intervention | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: TIF reveals saturation. Chain to catastrophic risk has gaps.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Multiple benchmarks to analyze. Intermediate.
  - **narrow_scope:** 3, confidence: 0.6 — Reduced to focused analysis but still involves multiple benchmarks.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** causal_chain_intervention, sources: 0 KB, 0 web

---

## #103: Calibration Decay Analysis: How Quickly Do Benchmark Difficulty Parameters Become Outdated? (Score: 3.00)

**ID:** gen-091

**Research Question:** How can using benchmarks with time-stamped model performance data (e address the problem that irt item calibration (estimating difficulty and discrimination) is done at a point in time using a reference population of models? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using benchmarks with time-stamped model performance data (e.g., HELM historical data, OpenLLM leaderboard snapshots), fit IRT models using only early models (e.g., those available in 2022) and compare estimated item difficulty parameters to those estimated using a 2023 and 2024 model population. Compute parameter drift: how much do b (difficulty) and a (discrimination) parameters shift across calibration epochs? Use χ² tests of parameter invariance across time windows. Identify items with most parameter drift (likely ceiling-approaching items). Compute the resulting change in test information function and G-coefficient over time. Propose a 'benchmark expiry' criterion: when drift exceeds a threshold, recalibration is required. IRT for LLM benchmarks (arXiv 2510.00844, 2505.15055) establishes calibration methodology. MMLU saturation by late 2024 illustrates rapid calibration decay in practice. Measurement invariance across time is a standard psychometric topic. Historical HELM data is publicly available. This analysis requires only R and public data.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Using outdated IRT calibrations systematically underestimates frontier model capability, as easy items appear to be measuring something meaningful when they provide no discriminating information. A benchmark expiry criterion prevents this. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI evaluation / psychometrics | **Strategy:** causal_chain_intervention | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: benchmark expiry detection. Same mechanism.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Temporal parameter comparison. Intermediate.
  - **narrow_scope:** 3, confidence: 0.6 — Multiple time points.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** causal_chain_intervention, sources: 0 KB, 0 web

---

## #104: Contamination-Resistant Item Design: IRT Analysis of Benchmark Drift After Public Release (Score: 3.00)

**ID:** gen-122

**Research Question:** How can collect evaluation results from models released at different time points on a fixed safety benchmark (e address the problem that safety benchmarks degrade after public release as training data contamination occurs? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Collect evaluation results from models released at different time points on a fixed safety benchmark (e.g., SafetyBench). Stratify models into pre-release and post-release cohorts. Fit IRT models separately to each cohort. Compute item parameter drift (change in b-parameters over time). Apply differential item functioning analysis (DIF) using time of model release as the grouping variable. Items showing significant DIF favoring post-release models are contamination candidates. Propose an IRT-based contamination early-warning system. Contamination is flagged as a major concern in 'How Should AI Safety Benchmarks Benchmark Safety?' (2601.23112) and the 2025 AI Safety Index. IRT parameter stability under equating conditions (Frontiers 2025) provides methodology for detecting parameter drift. DIF over time is a standard technique in educational testing for detecting item exposure effects.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Run Mantel-Haenszel DIF analysis comparing model families (e.g., open-source vs. closed-source) on item-level safety benchmark data to identify items that function differently across groups
- Compare IRT item parameter estimates (especially guessing parameters) between models with known training data overlap and those without, testing whether aberrant parameters signal contamination
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Addresses the contamination-resistant evaluation gap in Success State 1. Benchmark contamination is widely acknowledged but rarely quantified psychometrically. Item parameter drift is the IRT signature of contamination — when item difficulty drops for newer models without content changes, contamination is the most likely explanation. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Benchmark Integrity / Contamination Detection | **Strategy:** backcast_from_success | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: understanding benchmark drift after publication.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — Requires temporal analysis. Intermediate.
  - **narrow_scope:** 3, confidence: 0.6 — Pre/post publication comparison.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** backcast_from_success, sources: 0 KB, 0 web

---

## #105: Model Homogeneity as a Reliability Artifact: When All Models Agree, the Benchmark Teaches Nothing (Score: 3.00)

**ID:** gen-157

**Research Question:** How can select a safety benchmark and compute the score distribution across all models that have publicly reported results address the problem that monoculture in model outputs (failure b7) collapses inter-model variance in safety scores? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Select a safety benchmark and compute the score distribution across all models that have publicly reported results. Calculate: (a) inter-model variance in total scores, (b) inter-model variance on item-level binary responses, (c) internal consistency (Cronbach's alpha) across items. Apply the Vendi Score diversity metric to model output embeddings. Test the hypothesis: models with high pairwise output similarity (monoculture) show lower inter-item variance (binary metrics have nothing to discriminate). Use IRT to identify items with near-zero discrimination parameters (items that all models get right or wrong identically), and compute what percentage of the benchmark is informationally redundant due to monoculture. Monoculture across LLM families documented with high cosine similarity values. Binary metric dominance (79%) documented. Benchmark saturation and inability to discriminate frontier models documented. Vendi Score published for diversity measurement. IRT discrimination parameter analysis standard in mirt R package.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Compute internal consistency reliability (Cronbach's alpha, split-half) and IRT-based reliability (test information function) for a safety benchmark, reporting confidence intervals around model ability estimates
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. A benchmark where all models score identically provides no safety-relevant information. The compound failure of monoculture and binary metrics may be producing exactly this situation for frontier models on existing safety benchmarks. IRT discrimination analysis and diversity metrics together make this collapse measurable and documentable. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea applies established psychometric methods to AI safety benchmarks, an underexplored combination that can produce actionable insights with modest resources.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation & Benchmarking | **Strategy:** compounding_risks | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: when all models agree, benchmark appears reliable but may be uninformative.
  - **low_compute:** 3, confidence: 0.6 — May require evaluating multiple models.
  - **accessible_complexity:** 3, confidence: 0.6 — Conceptual + empirical. Intermediate.
  - **narrow_scope:** 3, confidence: 0.6 — Moderate scope.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** compounding_risks, sources: 0 KB, 0 web

---

## #106: Automated Test Assembly for Optimal Safety Benchmark Design (Score: 3.00)

**ID:** gen-184

**Research Question:** How can use a safety benchmark item pool with known irt parameters (estimated from prior calibration) address the problem that ai safety benchmarks are currently assembled manually, with no formal optimization of item selection? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Use a safety benchmark item pool with known IRT parameters (estimated from prior calibration). Formulate an ATA problem: maximize test information at a target safety level (or over a range) subject to constraints on hazard category coverage (blueprint), item format mix, and total test length. Solve using the ata R package (which wraps integer linear programming solvers). Compare the ATA-assembled benchmark to the original full benchmark in terms of measurement precision at different ability levels. Show that a 50-item ATA-assembled benchmark matches the measurement precision of a 200-item manually assembled one. The ata and eatATA packages in R implement full ATA with mixed-integer programming. ATA methodology is documented in MDPI and ETS publications. IRT parameters for safety benchmark items can be estimated from existing response data. The 'From Static Benchmarks to Adaptive Testing' paper discusses item selection optimization. This specific application of ATA to optimize safety benchmark design appears novel.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. ATA is the established method for building psychometrically optimal tests in educational and certification settings. The ata R package implements this for CRAN users. Applying ATA to safety benchmarks would produce principled, efficient evaluations rather than arbitrary item collections. The analysis requires only R and estimated IRT parameters—no ML training. It builds directly on the Rasch/IRT analysis idea and produces actionable benchmark design recommendations. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Evaluations & Benchmarks | **Strategy:** methodology_bridging | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Same as gen-073.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — ATA optimization. Intermediate.
  - **narrow_scope:** 3, confidence: 0.6 — Building optimized benchmark requires multiple constraints.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** methodology_bridging, sources: 0 KB, 0 web

---

## #107: Exploratory Factor Analysis of AI Safety Benchmarks (Score: 3.00)

**ID:** gen-290

**Research Question:** How can apply efa to a matrix of model scores across multiple safety benchmark subscales, discovering the latent factor structure of 'ai safety' and testing whether a single safety dimension or multiple orthogonal safety dimensions best account for observed benchmark intercorrelations address the problem that p1: no irt applied to ai safety benchmarks? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Apply EFA to a matrix of model scores across multiple safety benchmark subscales, discovering the latent factor structure of 'AI safety' and testing whether a single safety dimension or multiple orthogonal safety dimensions best account for observed benchmark intercorrelations. EFA is a standard tool in the psychometrician's toolkit. The 'General Scales' paper (arxiv 2503.06378) applies similar factor analysis to general capabilities. Applying EFA to safety-specific benchmark subscores (harmlessness, truthfulness, jailbreak, privacy, etc.) across a set of models is a novel analysis feasible with public leaderboard data and R (psych package).

**Experiments:** - Apply the proposed analysis method to item-level data from one public safety benchmark (e.g., TruthfulQA, HarmBench)
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. The dimensionality of 'safety' is empirically unknown—current benchmarks assume it is either unidimensional (single score) or fully multidimensional (independent subscales). EFA would provide the first data-driven answer to this question, directly informing whether IRT (which assumes unidimensionality) or MIRT is the appropriate framework. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Safety / Psychometrics | **Strategy:** combinatorial_matrix | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: EFA reveals latent structure. Generic measurement quality.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.6 — EFA is more accessible than MIRT but still requires interpretation.
  - **narrow_scope:** 3, confidence: 0.6 — Exploratory analysis is inherently less scoped.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** combinatorial_matrix, sources: 0 KB, 0 web

---

## #108: IRT Assumption Violations and the Sandbagging Detection Failure (Score: 2.96)

**ID:** gen-143

**Research Question:** How can select a published irt-analyzed llm benchmark (e address the problem that irt applied to llm benchmarks likely violates its core assumption of local independence (failure a9): items within a benchmark may be locally dependent because models use shared reasoning strategies, contextual priming, or training-data memorization rather than independent item-by-item ability expression? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Select a published IRT-analyzed LLM benchmark (e.g., from 'Lost in Benchmarks' or the PSN-IRT paper). Using the raw item-level response data (where available from open benchmarks), test for local dependence using Q3 statistics or the LD-X2 statistic in R (mirt package). Quantify the violation severity. Then simulate what a sandbagging response pattern would look like in the presence of estimated local dependence levels, and compare the statistical power to detect sandbagging under independence vs. dependence assumptions. Estimate the minimum sandbag magnitude detectable under realistic local dependence. 'Lost in Benchmarks' (arxiv 2505.15055) and PSN-IRT apply IRT to LLM benchmarks and note measurement quality issues. Sandbagging by frontier models documented in arxiv 2406.07358. Local independence testing is a standard psychometric diagnostic available in the mirt R package.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. IRT is being adopted as a gold standard for LLM benchmark analysis, but if its core assumptions are violated, its inferences — including anomaly detection for sandbagging — are unreliable. This research establishes the degree to which IRT can be trusted for safety-relevant inference. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation & Benchmarking | **Strategy:** compounding_risks | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.6 — Targets a meta-question: when does IRT-based sandbagging detection fail? Important for understanding detection limits.
  - **low_compute:** 4, confidence: 0.7 — Simulation study may require moderate compute.
  - **accessible_complexity:** 2, confidence: 0.6 — Requires understanding IRT assumptions, simulation design, and failure mode analysis. Advanced even with guided protocol.
  - **narrow_scope:** 3, confidence: 0.6 — Multiple assumption violation types to test. Reduced from broader scope but still multi-dimensional.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** compounding_risks, sources: 0 KB, 0 web

---

## #109: Contaminated Adversarial Data and Shallow Alignment: A Double Failure in Red-Teaming (Score: 2.96)

**ID:** gen-147

**Research Question:** How can select a published red-team dataset (e address the problem that data contamination (failure a3) applied to adversarial/red-team evaluation datasets compounds with shallow safety alignment (failure b3)? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Select a published red-team dataset (e.g., HarmBench, AdvBench). For a set of open-weight models, estimate contamination probability for red-team items using n-gram overlap and perplexity-based methods from published contamination literature. Then test whether high-contamination items show higher refusal rates than low-contamination items for the same model. Apply IRT to model refusal across the contamination gradient: does item difficulty (inverse of refusal rate) systematically decrease with contamination? If so, this documents the mechanism by which contamination produces shallow-alignment artifacts. Shallow alignment (first few tokens) documented in the ICLR 2025 outstanding paper (arxiv 2406.07358). Contamination detection methods available from published papers and open tools. HarmBench and AdvBench are widely used and publicly available.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Red-teaming is a primary safety evaluation tool. If red-team datasets are contaminated, refusal rates are inflated by memorization rather than by alignment depth. This research makes that inflation measurable and highlights why adversarial dataset security is a measurement issue, not just a data hygiene issue. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation & Benchmarking | **Strategy:** compounding_risks | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.6 — Strong: contaminated red-team data means adversarial evaluations test for known attacks only. Combined with shallow alignment, creates false safety assurance.
  - **low_compute:** 3, confidence: 0.6 — May require running adversarial evaluations.
  - **accessible_complexity:** 2, confidence: 0.5 — Requires understanding adversarial evaluation pipeline and contamination. Advanced.
  - **narrow_scope:** 3, confidence: 0.5 — Multiple failure modes to demonstrate.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** compounding_risks, sources: 0 KB, 0 web

---

## #110: Benchmark Contamination and Deceptive Alignment: The Memorized Safe Answer (Score: 2.96)

**ID:** gen-156

**Research Question:** How can for a set of safety benchmark items, estimate contamination probability (n-gram overlap, perplexity drop) address the problem that data contamination (failure a3) means models have seen benchmark items during training? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** For a set of safety benchmark items, estimate contamination probability (n-gram overlap, perplexity drop). Sort items into high-contamination and low-contamination bins. Compare refusal rates between bins: if refusal is substantially higher on contaminated items (controlling for item difficulty via IRT), this is evidence that contamination is producing memorized-refusal rather than genuine alignment. Apply a confirmatory factor analysis in R testing whether contamination-level loads on the same factor as a 'genuine safety behavior' indicator (e.g., refusal on novel, non-contaminated reformulations of the same prompt). If the factors are distinct, contamination and genuine alignment are empirically separable. Contamination detection methods well-established in 2024–2025 literature. Deceptive alignment is a theoretical cornerstone of alignment safety research. The equivalence between memorized-safe-response and performed-safety is a novel framing that bridges contamination and alignment literatures. Factor analysis in R is within participant competence.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Compare IRT item parameter estimates (especially guessing parameters) between models with known training data overlap and those without, testing whether aberrant parameters signal contamination
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Deceptive alignment is difficult to test for directly. Contamination creates a natural experiment: contaminated items elicit memorized responses rather than reasoned refusals, providing a proxy measure for detecting the 'performs safely only when recognized as being evaluated' pattern. Psychometric separation of contamination-driven and alignment-driven refusals advances both measurement quality and alignment theory. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Alignment | **Strategy:** compounding_risks | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong: memorized safe answers give appearance of safety without genuine safe behavior. Directly targets deceptive alignment.
  - **low_compute:** 3, confidence: 0.6 — Requires designing novel test items.
  - **accessible_complexity:** 2, confidence: 0.5 — Requires designing experiments to distinguish memorized from genuine safety. Advanced.
  - **narrow_scope:** 3, confidence: 0.5 — Experimental design is multi-step.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** compounding_risks, sources: 0 KB, 0 web

---

## #111: Cognitive Diagnostic Model Analysis of AI Safety Profiles (Score: 2.96)

**ID:** gen-228

**Research Question:** How can step 1: define a q-matrix specifying which safety attributes (e address the problem that irt produces a single ability score on a latent continuum? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Step 1: Define a Q-matrix specifying which safety attributes (e.g., harmful content refusal, manipulation resistance, deception avoidance, bias mitigation) each benchmark item requires. This requires expert coding of 50-100 items from public benchmarks. Step 2: Fit a G-DINA model using the GDINA R package to safety benchmark response data. Step 3: Extract attribute mastery profiles for each AI model. Step 4: Cluster models by safety profile. Report which attributes are commonly mastered and which are systematically absent. The GDINA R package is available and well-documented. CDM surveys (2024) confirm the technique is mature. LLM-CDM integration research (2025) shows the approach is feasible. Public safety benchmark item banks from TruthfulQA, BBQ, and HarmBench can provide response data.

**Experiments:** - Apply the proposed analysis method to item-level data from one public safety benchmark (e.g., TruthfulQA, HarmBench)
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. A CDM safety profile changes the question from 'how safe is this model?' to 'what exactly can and can't this model do safely?' This is far more actionable for AI developers and policymakers. It would be the first diagnostic safety profiling of AI models with formal psychometric foundations. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Safety Evaluation / Cognitive Diagnostics | **Strategy:** landscape_gap_targeting | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.6 — Strong: CDM provides fine-grained capability profiles beyond IRT. Can identify specific knowledge/skill deficits.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 2, confidence: 0.5 — CDM is specialist psychometric knowledge beyond IRT. Advanced.
  - **narrow_scope:** 3, confidence: 0.5 — CDM requires Q-matrix specification and fitting. Multi-step.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** landscape_gap_targeting, sources: 0 KB, 0 web

---

## #112: MIRT Ability Estimation for Safety: Can We Recover Separate Honesty and Harm-Avoidance Ability Scores? (Score: 2.96)

**ID:** gen-234

**Research Question:** How can using the best-fitting mirt model from a multidimensional safety analysis, extract per-model ability estimates on each safety dimension address the problem that even if mirt shows safety is multidimensional, it must also be shown that separate ability scores can be reliably recovered? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using the best-fitting MIRT model from a multidimensional safety analysis, extract per-model ability estimates on each safety dimension. Compute: (1) reliability of each subscale (marginal reliability from the Fisher information matrix), (2) discriminant validity (correlation between dimensions — too-high correlation defeats the purpose of separation), (3) convergent validity (correlation of each subscale with external criterion, e.g., human preference ratings). Report a 2D safety map plotting all models. MIRT ability estimation is standard (mirt package). Marginal reliability from information matrices is documented in mirt documentation. The construct validity framework for AI evaluation was published in 2025 (arXiv:2505.10573 'Measurement to Meaning'). Public safety data is available.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Reliable, discriminant ability scores would transform safety evaluation: rather than 'this model scored 72% on safety,' we could say 'this model is at the 60th percentile for honesty but 85th percentile for harm avoidance.' This is genuinely useful information for deployment decisions in safety-sensitive applications. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** arXiv:2505.10573

**Subfield:** AI Safety Evaluation / Psychometrics | **Strategy:** landscape_gap_targeting | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong: recovering separate honesty vs harm-avoidance dimensions directly relevant to alignment assessment. Sycophancy may trade honesty for harm-avoidance.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 2, confidence: 0.5 — Requires MIRT with specific dimension specification and interpretation. Advanced.
  - **narrow_scope:** 3, confidence: 0.6 — Multiple dimensions to model and interpret.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** landscape_gap_targeting, sources: 0 KB, 0 web

---

## #113: The Population Assumption Problem: Formalizing Non-Populational IRT for AI Safety Evaluation (Score: 2.87)

**ID:** gen-245

**Research Question:** How can apply both standard irt (assuming a normal model-ability population) and non-populational irt (ability estimated from single-model response patterns without population assumption) to the same safety benchmark data address the problem that irt assumes persons are sampled from a well-defined population with a specified ability distribution (typically normal)? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Apply both standard IRT (assuming a normal model-ability population) and non-populational IRT (ability estimated from single-model response patterns without population assumption) to the same safety benchmark data. Compare: (1) ability estimates from each approach and their rank-order correlation, (2) item parameter estimates under each assumption, (3) confidence intervals and their coverage probabilities via bootstrap. Assess when the approaches diverge and what this divergence implies for safety score interpretation. The 'General Scales Unlock AI Evaluation' paper (arXiv:2503.06378) develops non-populational IRT for AI. The 'Stop Evaluating AI with Human Tests' paper (arXiv:2507.23009) explicitly addresses assumption violations. Standard IRT violation effects are documented in the IRT literature. The mirt package implements standard IRT for comparison.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If non-populational IRT produces substantially different safety rankings from standard IRT, the assumption violation is practically significant. This paper would establish when and why the population assumption matters for AI evaluation — a foundational methodological contribution that applies across all IRT-based AI evaluation, not just safety. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), narrow_scope (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** arXiv:2503.06378; arXiv:2507.23009

**Subfield:** AI Evaluation Methodology / Measurement Theory | **Strategy:** landscape_gap_targeting | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 2, confidence: 0.5 — Foundational: formalizes population assumptions. No specific catastrophic risk chain.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 2, confidence: 0.5 — Requires deep understanding of IRT population theory. Advanced.
  - **narrow_scope:** 4, confidence: 0.6 — Focused formalization exercise.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** landscape_gap_targeting, sources: 0 KB, 0 web

---

## #114: Reliability Generalization Meta-Analysis of AI Safety Benchmark Internal Consistency (Score: 2.74)

**ID:** gen-010

**Research Question:** How can collect internal consistency estimates (kr-20, split-half, or irt-based marginal reliability) for 8-10 safety benchmarks across multiple published evaluation studies or leaderboard snapshots using different model pools address the problem that reliability generalization (rg) meta-analysis examines how reliability varies across administrations of the same instrument? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Collect internal consistency estimates (KR-20, split-half, or IRT-based marginal reliability) for 8-10 safety benchmarks across multiple published evaluation studies or leaderboard snapshots using different model pools. Compute reliability estimates for each benchmark-sample combination in R. Conduct a meta-regression predicting reliability from moderators: number of items, model pool diversity (range of scores), benchmark age, item format. Summarize using forest plots and report practical implications for benchmark design. RG meta-analysis methodology (Springer 2023); Cronbach's alpha debate (EPR 2025); IRT marginal reliability is preferable to Cronbach's alpha for non-tau-equivalent items; reliability of AI benchmarks is an acknowledged gap (Stanford 2025 report on benchmark bugs).

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Compute internal consistency reliability (Cronbach's alpha, split-half) and IRT-based reliability (test information function) for a safety benchmark, reporting confidence intervals around model ability estimates
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If safety benchmark reliability varies by 0.3 units across different model samples, safety rankings derived from those benchmarks are untrustworthy for specific populations of models. RG meta-analysis would reveal which safety benchmarks have robust, sample-independent reliability and which do not—providing the first systematic reliability evidence for the AI safety evaluation toolbox. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Reliability Generalization / Meta-Analysis | **Strategy:** novel_direction | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 2, confidence: 0.6 — Vague: meta-analysis of reliability across benchmarks. Methodological contribution without specific catastrophic risk chain.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 3, confidence: 0.5 — Meta-regression requires statistical expertise. Intermediate after refinement.
  - **narrow_scope:** 3, confidence: 0.5 — Reduced to single testable hypothesis but still requires collecting data across multiple benchmarks.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** novel_direction, sources: 0 KB, 0 web

---

## #115: IRT-Based Score Equating Between Safety Benchmarks: A Linking Study (Score: 2.70)

**ID:** gen-111

**Research Question:** How can identify a set of 'anchor items' — safety prompts that appear in conceptually equivalent form across two safety benchmarks (e address the problem that a model evaluated on safetybench cannot be compared to one evaluated on harmbench — the scales are incommensurable? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Identify a set of 'anchor items' — safety prompts that appear in conceptually equivalent form across two safety benchmarks (e.g., SafetyBench and TrustLLM, or HarmBench and WildGuard). Evaluate a common set of 15-25 models on both benchmarks. Use the equateIRT R package to perform concurrent IRT calibration or common-person linking. Place both benchmarks on a common latent scale. Compute equating error. Assess whether scores from the two benchmarks can be meaningfully compared. The equateIRT R package (CRAN, updated July 2025) provides all necessary tools. Common-persons design (Liu et al., 2026) shows that 30+ common persons suffice for equating. IRT parameter stability under equating conditions (Frontiers, 2025) provides methodological guidance. No AI safety benchmark equating study exists in the literature.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Fills the equating gap in Success State 3. Without equating, the field cannot aggregate evidence across evaluations or track safety progress across benchmark generations. This is a prerequisite for any meta-analytic or regulatory synthesis of safety evidence. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Score Equating / Benchmark Comparability | **Strategy:** backcast_from_success | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible chain.
  - **low_compute:** 4, confidence: 0.7 — May require moderate effort.
  - **accessible_complexity:** 2, confidence: 0.5 — Equating/linking is advanced psychometrics.
  - **narrow_scope:** 3, confidence: 0.6 — Multi-step linking study.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** backcast_from_success, sources: 0 KB, 0 web

---

## #116: Measurement Invariance Testing: Do Safety Benchmarks Measure the Same Construct Across Model Families? (Score: 2.70)

**ID:** gen-116

**Research Question:** How can using multi-group cfa (in lavaan), test configural, metric, and scalar invariance of a safety benchmark across model families (e address the problem that safety evaluations are used to compare models across different architectural families (gpt-style, claude-style, gemini-style, open-source)? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using multi-group CFA (in lavaan), test configural, metric, and scalar invariance of a safety benchmark across model families (e.g., GPT-4 class vs. Claude class vs. open-source LLaMA class). Collect item-level response data for models grouped by family. Test whether factor loadings and item intercepts are equal across groups. Report which levels of invariance hold. Identify non-invariant items. Discuss implications for cross-family safety comparisons. Measurement invariance is a standard CFA extension implemented in lavaan. The 'Measuring what Matters' review did not address measurement invariance across model families. Multi-group MIRT is also an option (2024 paper on parameter recovery in MGMIRT). No published AI benchmark invariance study exists.

**Experiments:** - Apply the proposed analysis method to item-level data from one public safety benchmark (e.g., TruthfulQA, HarmBench)
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Fills a measurement fairness gap overlapping Success States 2 and 3. If items are non-invariant across model families, then 'GPT-4 scores 82% vs. Claude scores 79%' on a safety benchmark is not a valid comparison — the benchmark means different things for different architectures. This finding would have immediate practical implications for evaluation policy. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Measurement Fairness / Construct Validity | **Strategy:** backcast_from_success | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: tests whether benchmarks measure same construct across architectures.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 2, confidence: 0.5 — Measurement invariance testing is advanced psychometrics.
  - **narrow_scope:** 3, confidence: 0.6 — Multiple model families to compare.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** backcast_from_success, sources: 0 KB, 0 web

---

## #117: Multidimensional IRT (MIRT) for Safety Capability Profiles (Score: 2.70)

**ID:** gen-118

**Research Question:** How can fit a 2-factor or 3-factor mirt model to item-level safety benchmark response data using the mirt r package address the problem that unidimensional irt places all models on a single safety axis, but safety is plausibly multidimensional: a model may be highly calibrated at refusing harmful requests in english but poor at detecting harm in multilingual or low-resource language contexts? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Fit a 2-factor or 3-factor MIRT model to item-level safety benchmark response data using the mirt R package. Use exploratory MIRT to let the data reveal the latent structure, then confirmatory MIRT to test theoretically motivated structures. Examine factor loadings to interpret dimensions. Compute model-specific theta vectors (safety profiles). Visualize models in 2D/3D theta space. Identify whether multilingual, reasoning-intensive, and refusal-type items load on distinct factors. The mirt R package (Chalmers, GitHub) is the standard tool and well-documented. A 2024 paper on MIRT for competency assessment (ScienceDirect) and a 2025 paper on human vs. AI-generated test dimensionality (arxiv 2510.24739) provide methodological grounding. MIRT for LLM ability profiling is nascent — no safety application exists.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Addresses Success State 7. MIRT provides richer diagnostic information than unidimensional IRT without requiring the discrete attribute assumptions of CDMs. Combined with CDM work, this triangulates whether AI safety is best modeled as continuous multidimensional traits or discrete attribute mastery. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Diagnostic Assessment / Multidimensional IRT | **Strategy:** backcast_from_success | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: MIRT for safety profiles. Generic measurement quality.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 2, confidence: 0.5 — MIRT capability profiles require advanced knowledge.
  - **narrow_scope:** 3, confidence: 0.6 — Multiple models and interpretations.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** backcast_from_success, sources: 0 KB, 0 web

---

## #118: Cold Start and Capability Overhang: When New Architecture Meets Uncharted Capability Space (Score: 2.70)

**ID:** gen-163

**Research Question:** How can select 2–3 recently released architecturally novel models (e address the problem that the cold-start problem (failure a10) means benchmarks are calibrated on existing model families and may not have valid difficulty parameters for genuinely novel architectures? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Select 2–3 recently released architecturally novel models (e.g., MoE models, models with novel context architectures). Apply IRT analysis (mirt in R) using item calibrations derived from existing model families. Test whether item difficulties and discriminations transfer to the novel architecture by computing residuals between expected and observed response patterns (person-fit statistics). Identify items with large residuals — these are the items where the novel architecture is behaving unexpectedly relative to established ability curves. Interpret clusters of unexpected items as potential capability overhang indicators requiring deeper investigation. IRT calibration is population-specific; applying calibrations from one population to another is a known validity concern in psychometrics. Novel architectures (MoE, extended context) are actively deployed. Person-fit statistics available in mirt. Capability overhang is a documented safety concern.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. IRT person-fit analysis on novel model families provides a principled, psychometrically grounded method for flagging capability patterns that do not fit established models — which is precisely the operationalization of 'capability overhang' detection. This is more principled than ad hoc inspection of score anomalies. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation & Benchmarking | **Strategy:** compounding_risks | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.5 — Plausible: new architecture meets uncharted capability. Important concept.
  - **low_compute:** 4, confidence: 0.7 — May require some model evaluations.
  - **accessible_complexity:** 2, confidence: 0.5 — Requires understanding capability overhang theory and evaluation design.
  - **narrow_scope:** 3, confidence: 0.5 — Conceptually broad.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** compounding_risks, sources: 0 KB, 0 web

---

## #119: Item Exposure Control Analysis for AI Safety Benchmarks (Score: 2.70)

**ID:** gen-187

**Research Question:** How can apply irt-based item exposure analysis to ai safety benchmarks address the problem that ai safety benchmark items that are heavily exposed during training data collection inflate model performance beyond what genuine safety would predict—analogous to the cat problem of overexposed items? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Apply IRT-based item exposure analysis to AI safety benchmarks. Estimate item difficulty parameters using IRT. Identify items that are disproportionately 'overselected' by current models relative to their difficulty level—a pattern suggesting familiarity rather than safety generalization. Compare item difficulty-to-selection ratios against exposure rate thresholds used in CAT (e.g., Sympson-Hetter threshold of 0.5). Correlate exposure risk indicators with known data leakage signals (n-gram match with training corpora, semantic similarity to web-scraped safety datasets). Propose item rotation or item banking procedures analogous to CAT exposure control. IRT item exposure control literature is well-developed (Springer 2023, PMC6140306). AI benchmark contamination is documented and discussed as a major problem ('Benchmark Contamination: The AI Fraud Nobody Wants to Discuss'). N-gram overlap methods for contamination detection exist. The formal analogy between CAT item exposure and benchmark contamination is conceptually clear but appears not to have been developed in published work.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Item exposure control in CAT uses formal statistical methods to prevent test score inflation from item overexposure. AI benchmark contamination has been identified as a major threat to valid evaluation (Benchmark Contamination article). Applying formal exposure control diagnostics would provide a quantitative framework for contamination risk assessment that goes beyond simple n-gram matching. The methodology requires only IRT analysis and correlation in R. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Evaluations & Benchmarks | **Strategy:** methodology_bridging | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: item exposure control for benchmark longevity.
  - **low_compute:** 4, confidence: 0.7 — May require some simulation.
  - **accessible_complexity:** 2, confidence: 0.5 — Item exposure control is a specialist CAT topic.
  - **narrow_scope:** 3, confidence: 0.6 — Multiple exposure control strategies to compare.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** methodology_bridging, sources: 0 KB, 0 web

---

## #120: Are IRT Item Parameters Stable Across Prompt Phrasings? Testing Measurement Invariance (Score: 2.70)

**ID:** gen-207

**Research Question:** How can for 20-30 safety items, create 3-4 paraphrase variants of each address the problem that quantify and reduce prompt sensitivity in evaluation? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** For 20-30 safety items, create 3-4 paraphrase variants of each. Calibrate IRT item parameters (difficulty b, discrimination a) separately for each paraphrase group. Test whether parameters are stable across phrasings using IRT measurement invariance tests (multigroup IRT in mirt, testing equality constraints on a and b parameters). Items with significantly different parameters across phrasings are 'prompt-sensitive' in a psychometrically precise sense. IRT measurement invariance testing (multigroup IRT, differential item functioning frameworks) is a well-established psychometric technique. 'Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory' (2025) applies IRT to judge reliability—similar methods apply to prompt stability. The mirt package supports multigroup IRT and measurement invariance testing.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. If an item's IRT parameters change depending on how it is phrased, then the item is not measuring a stable construct—different phrasings are effectively measuring different things. This makes it impossible to compare model ability estimates across evaluations that use different prompt wordings. Identifying prompt-stable items is essential for benchmark validity. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea applies established psychometric methods to AI safety benchmarks, an underexplored combination that can produce actionable insights with modest resources.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation / Psychometrics | **Strategy:** problem_decomposition | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: measurement invariance across prompts. Important but indirect.
  - **low_compute:** 3, confidence: 0.6 — Requires API calls for different phrasings.
  - **accessible_complexity:** 2, confidence: 0.5 — Measurement invariance testing is advanced psychometrics.
  - **narrow_scope:** 3, confidence: 0.6 — Multiple prompt variants to test.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** problem_decomposition, sources: 0 KB, 0 web

---

## #121: Prompt-Robust Safety Scoring: Aggregating Across Paraphrases Using IRT Theta Estimates (Score: 2.70)

**ID:** gen-208

**Research Question:** How can compare three scoring methods for safety evaluation: (1) mean proportion of refusals across all prompts (raw score), (2) irt theta estimate from a calibrated model using all prompt variants, (3) irt theta estimate using only prompt-stable items (those with invariant parameters) address the problem that quantify and reduce prompt sensitivity in evaluation? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Compare three scoring methods for safety evaluation: (1) mean proportion of refusals across all prompts (raw score), (2) IRT theta estimate from a calibrated model using all prompt variants, (3) IRT theta estimate using only prompt-stable items (those with invariant parameters). Assess which scoring method produces the most stable model rankings across held-out prompt sets. Use rank correlation stability as the primary outcome. tinyBenchmarks (2024) showed that IRT-based estimates outperform raw scores on general capability benchmarks. 'Adaptive Testing for LLM Evaluation' (2025) demonstrates the superiority of IRT theta over raw scores for stability. The extension to safety-specific benchmarks with prompt-robust scoring has not been investigated.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. IRT theta estimation accounts for item difficulty and discrimination, potentially producing more stable ability estimates than raw refusal rates. If IRT-based scoring is more robust to prompt variation than raw scoring, this provides a concrete, practical recommendation for how safety benchmark scores should be reported. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea applies established psychometric methods to AI safety benchmarks, an underexplored combination that can produce actionable insights with modest resources.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation / Psychometrics | **Strategy:** problem_decomposition | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: aggregating across paraphrases using IRT.
  - **low_compute:** 3, confidence: 0.6 — API calls for paraphrases.
  - **accessible_complexity:** 2, confidence: 0.5 — Advanced: combining IRT with prompt engineering.
  - **narrow_scope:** 3, confidence: 0.6 — Multiple paraphrases and IRT fitting.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** problem_decomposition, sources: 0 KB, 0 web

---

## #122: Measurement Uncertainty Budget for IRT-Based Safety Scores (Score: 2.70)

**ID:** gen-293

**Research Question:** How can apply gum-style uncertainty budgeting to irt-estimated safety ability scores, quantifying uncertainty from item calibration error, model response sampling, prompt variability, and ability estimation precision, producing a principled confidence interval for each model's irt safety score address the problem that p1: no irt applied to ai safety benchmarks? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Apply GUM-style uncertainty budgeting to IRT-estimated safety ability scores, quantifying uncertainty from item calibration error, model response sampling, prompt variability, and ability estimation precision, producing a principled confidence interval for each model's IRT safety score. GUM uncertainty budgeting is standard in physical measurement but novel for IRT-based AI scores. IRT standard errors of measurement are a starting point but do not account for item calibration uncertainty, prompt sensitivity, or sampling. This is a desk analysis combining GUM methodology with IRT theory—no new data collection needed.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Even when IRT is applied, the resulting ability estimates are point estimates with unacknowledged uncertainty. A GUM uncertainty budget for IRT safety scores would produce properly-calibrated confidence intervals, enabling practitioners to see that model A's safety score is not statistically distinguishable from model B's. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation / Metrology | **Strategy:** combinatorial_matrix | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: formal uncertainty quantification. Important for governance.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 2, confidence: 0.5 — Measurement uncertainty budget is a specialist metrology concept.
  - **narrow_scope:** 3, confidence: 0.6 — Multiple uncertainty sources to quantify.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** combinatorial_matrix, sources: 0 KB, 0 web

---

## #123: Measurement Invariance Testing of Safety Evaluations Across Language/Cultural Contexts (Score: 2.52)

**ID:** gen-101

**Research Question:** How can using a multilingual safety benchmark (e address the problem that safety evaluations are predominantly developed and validated in english? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Using a multilingual safety benchmark (e.g., if multilingual versions of safety items exist) or by translating a subset of safety items from a standard English benchmark into 2-3 other languages (using professional translation + back-translation verification), administer items across language conditions. Fit multigroup IRT models in R (mirt supports multigroup analysis), testing for configural, metric, and scalar invariance. Items showing differential item functioning across language groups (DIF) are flagged as culturally non-invariant. Quantify the impact of non-invariant items on overall score comparability across language groups. Identify item content features (legal references, cultural norms, specific harm scenarios) that predict invariance failure. Cross-lingual contamination was identified as a benchmark validity issue (2025). Measurement invariance testing is standard in cross-cultural psychometrics. The mirt R package supports multigroup IRT for invariance testing. Translation + DIF analysis requires no ML, only psychometric expertise and translation resources. No prior paper has applied formal measurement invariance testing to AI safety benchmarks.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Run Mantel-Haenszel DIF analysis comparing model families (e.g., open-source vs. closed-source) on item-level safety benchmark data to identify items that function differently across groups
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Models deployed globally are evaluated in English but cause harm in multilingual contexts. Measurement non-invariance across languages means that a single global safety score is an invalid composite — it may reflect English-context safety while obscuring cross-lingual vulnerabilities. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI evaluation / cross-cultural psychometrics | **Strategy:** causal_chain_intervention | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.6 — Strong: if safety evals don't measure the same thing across languages, deployment in non-English contexts is ungoverned.
  - **low_compute:** 4, confidence: 0.7 — May require multilingual evaluation.
  - **accessible_complexity:** 2, confidence: 0.5 — Multi-group invariance testing is advanced. Requires multilingual data.
  - **narrow_scope:** 2, confidence: 0.5 — Cross-cultural comparison requires significant data collection.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** causal_chain_intervention, sources: 0 KB, 0 web

---

## #124: General Factor (g-factor) Analysis of AI Safety: Is There a Single Safety Latent Trait? (Score: 2.52)

**ID:** gen-130

**Research Question:** How can collect item-level or subdomain-level safety benchmark scores across 5-7 diverse safety benchmarks for a common set of models address the problem that the field implicitly debates whether ai safety is a single latent trait (a 'g-factor' of safety) or a collection of independent capabilities? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Collect item-level or subdomain-level safety benchmark scores across 5-7 diverse safety benchmarks for a common set of models. Run exploratory factor analysis (EFA) with different rotation methods (varimax, oblimin). Test for a general factor using bi-factor modeling (bifactor function in mirt). Compute omega-hierarchical and omega-total to quantify how much variance is attributable to the general safety factor vs. specific subdomain factors. Report whether a single safety score is a defensible summary statistic. Bi-factor modeling is natively supported in mirt. Omega statistics are computed in the psych R package. EFA of safety constructs is implied by the nomological network work but not executed. The 'General Scales Unlock AI Evaluation' paper (arxiv 2503.06378) discusses general scales for AI evaluation but focuses on prediction rather than psychometric structure.

**Experiments:** - Apply the proposed analysis method to item-level data from one public safety benchmark (e.g., TruthfulQA, HarmBench)
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Foundational for all of Success States 1-7. If a g-factor of safety exists and accounts for >70% of variance, the entire field can focus on measuring it well (IRT, reliability, standard setting) rather than chasing subdomains. If safety is truly multidimensional, single scores are misleading and the entire benchmark paradigm needs restructuring. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on theory_of_impact (score 4), low_compute (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** Construct Structure / Factor Analysis | **Strategy:** backcast_from_success | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 4, confidence: 0.7 — Strong: tests whether safety has a general factor, directly relevant to whether single safety scores are defensible for governance.
  - **low_compute:** 5, confidence: 0.9 — CPU-only factor analysis.
  - **accessible_complexity:** 2, confidence: 0.5 — g-factor analysis requires specialist psychometric knowledge. Advanced.
  - **narrow_scope:** 2, confidence: 0.5 — Requires data across multiple benchmarks and fitting complex models.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** backcast_from_success, sources: 0 KB, 0 web

---

## #125: G-Theory Reliability Study (Score: 2.43)

**ID:** gen-289

**Research Question:** How can apply g-theory to quantify total measurement reliability of a safety benchmark by decomposing variance across items, models, and prompt variants, computing the first formal reliability coefficient for an ai safety benchmark and comparing it to accepted standards (g > 0 address the problem that p1: no irt applied to ai safety benchmarks? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Apply G-Theory to quantify total measurement reliability of a safety benchmark by decomposing variance across items, models, and prompt variants, computing the first formal reliability coefficient for an AI safety benchmark and comparing it to accepted standards (G > 0.80). G-Theory is the appropriate multi-facet reliability method. The Stanford AI Measurement Science textbook discusses G-Theory for AI evaluation. A G-study on a safety benchmark requires response data across multiple prompt variants—available from prompt sensitivity studies or collectable in R from open-source benchmark APIs.

**Experiments:** - Compute internal consistency reliability (Cronbach's alpha, split-half) and IRT-based reliability (test information function) for a safety benchmark, reporting confidence intervals around model ability estimates
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. No published reliability study exists for any dedicated AI safety benchmark. A G-Theory reliability study would establish whether current safety benchmarks meet minimum psychometric standards and provide the variance component data needed to design more reliable future benchmarks. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 5), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Safety / Psychometrics | **Strategy:** combinatorial_matrix | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 2, confidence: 0.6 — Methodological: G-theory reliability. Generic.
  - **low_compute:** 5, confidence: 0.9 — CPU-only.
  - **accessible_complexity:** 2, confidence: 0.5 — G-theory requires specialist knowledge.
  - **narrow_scope:** 3, confidence: 0.6 — Multiple facets to decompose.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** combinatorial_matrix, sources: 0 KB, 0 web

---

## #126: Computerized Adaptive Safety Benchmark via CAT (Score: 2.43)

**ID:** gen-292

**Research Question:** How can design and simulate a computerized adaptive testing protocol for ai safety evaluation, using a pre-calibrated irt item bank to select maximally informative safety items for each model, demonstrating that cat achieves equivalent precision to full-form testing with 50% fewer items address the problem that p1: no irt applied to ai safety benchmarks? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Design and simulate a Computerized Adaptive Testing protocol for AI safety evaluation, using a pre-calibrated IRT item bank to select maximally informative safety items for each model, demonstrating that CAT achieves equivalent precision to full-form testing with 50% fewer items. CAT applied to AI benchmarks is explicitly proposed by Cambridge scientists (Cambridge Enterprise news). The catR R package implements full CAT simulations. MetaBench item parameters from ICLR 2025 provide the calibrated item bank needed. A simulation study comparing CAT efficiency to fixed-form testing is feasible in 30 hours.

**Experiments:** - Fit IRT models (1PL/2PL) to item-level response data from a public safety benchmark using the mirt R package or py-irt Python package, and examine item parameter estimates (difficulty, discrimination) with standard errors
- Simulate computerized adaptive testing item selection on existing benchmark data and compare measurement precision (standard error of theta) against full-length administration
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. Safety benchmarks are expensive to administer (API costs, evaluation time). A CAT-based safety benchmark would reduce costs while maintaining measurement precision. This is a natural extension of IRT calibration—once items are calibrated, CAT simulation is the next step. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation / Psychometrics | **Strategy:** combinatorial_matrix | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 2, confidence: 0.5 — Vague: build a CAT safety benchmark. No specific catastrophic risk chain.
  - **low_compute:** 4, confidence: 0.7 — May require more compute for full benchmark construction.
  - **accessible_complexity:** 2, confidence: 0.5 — Building a full CAT benchmark requires advanced knowledge.
  - **narrow_scope:** 3, confidence: 0.6 — Building a benchmark is broader than a single analysis.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** combinatorial_matrix, sources: 0 KB, 0 web

---

## #127: Interlaboratory Comparison Design for AI Safety Evaluation Reproducibility (Score: 2.26)

**ID:** gen-062

**Research Question:** How can design and run a mini-ilc study: recruit 4–6 teams (academic labs, independent researchers) to independently evaluate the same 10 models on the same 3 safety benchmarks, using their own implementation choices but the same item set address the problem that different labs evaluating the same model on the same benchmark obtain different scores due to implementation variation (prompt formatting, temperature, few-shot examples, evaluation harness)? This project investigates whether psychometric and measurement-theoretic methods can provide rigorous, quantitative answers to this question using existing benchmark data.

**Approach:** Design and run a mini-ILC study: recruit 4–6 teams (academic labs, independent researchers) to independently evaluate the same 10 models on the same 3 safety benchmarks, using their own implementation choices but the same item set. Use ISO 13528 statistical methods (z-scores, En numbers) to identify outlier labs and quantify reproducibility (between-lab standard deviation). Identify which benchmarks are most and least reproducible. Report uncertainty estimates analogous to a measurement uncertainty budget. ISO 13528:2022 provides the statistical framework for ILC data analysis. The benchmark-iceberg phenomenon (OpenReview, IRT-iceberg paper) shows hidden implementation choices dominate score variance. Mini-ILC can be run with volunteer collaboration. Analysis is entirely in R. Directly actionable for safety governance.

**Experiments:** - Apply the proposed analysis method to item-level data from one public safety benchmark (e.g., TruthfulQA, HarmBench)
- Visualize key results (item characteristic curves, test information functions, or comparison plots) for the blog post deliverable
- Compare results against baseline (e.g., binary scoring, aggregate metrics) to quantify what the proposed method reveals that standard approaches miss

**Impact Chain:** If this research succeeds, it produces quantitative evidence about safety benchmark measurement properties. ILC programs are the cornerstone of measurement quality assurance in every physical and chemical measurement field. An analogous program for AI safety benchmarks would reveal how much of reported score variation is real model differences vs. implementation noise—directly impacting how seriously benchmarks should be taken in governance decisions. This enables more informed deployment decisions by revealing whether current safety evaluations actually measure what they claim to measure, directly reducing the risk that a model is deployed as 'safe' based on benchmarks that lack validity or sensitivity at critical ability levels.

**Strength Rationale:** This idea scores highly on low_compute (score 4), indicating it is well-suited for the target team. The methodology builds on established psychometric techniques with existing software implementations, making it accessible while producing genuinely novel results in the AI safety evaluation space.

**Cited Sources:** No verified citations available — novelty assessment pending

**Subfield:** AI Evaluation & Benchmarking | **Strategy:** cross_domain_transfer | **Novelty:** skipped (None)
**Scores:**
  - **theory_of_impact:** 3, confidence: 0.6 — Plausible: ILC quantifies implementation variance in safety evaluation. Important for governance.
  - **low_compute:** 4, confidence: 0.7 — Coordination cost rather than compute.
  - **accessible_complexity:** 2, confidence: 0.5 — Requires recruiting 4-6 teams and coordinating their evaluations. Project management heavy.
  - **narrow_scope:** 2, confidence: 0.4 — Requires external team coordination. Major dependency.
  - **novelty:** 0, confidence: 0.0 — From original novelty assessment (skipped in this run)
**Provenance:** cross_domain_transfer, sources: 0 KB, 0 web

---
