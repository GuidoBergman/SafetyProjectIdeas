# Research Topic Report: Safety Benchmarks That Actually Inform Decisions

> Generated: 2026-04-07
> Requested by: coordinator
> Papers analyzed: 26

## Topic Definition

This report investigates AI safety benchmarks and evaluation frameworks that go beyond academic exercise to actually influence real-world decisions — deployment gates, responsible scaling thresholds, policy requirements, and capability red lines. The focus is on which benchmarks matter in practice, which are noise, and what structural problems undermine the evaluation ecosystem. The topic spans concrete benchmark suites (WMDP, FORTRESS, HarmBench, etc.), meta-analyses of benchmark validity, institutional evaluation frameworks (UK AISI Inspect, Anthropic RSP, METR), and critical perspectives on whether the current evaluation regime serves its stated purpose.

## Dimensions Tracked

| Dimension | Description | Coordinator rationale |
|-----------|------------|----------------------|
| **Public availability** | Is the benchmark openly available (code, data, scoring)? | You can't use what you can't access |
| **Relevancy / Impact** | Does this benchmark actually change decisions (deployment gates, policy, capability limits)? Who uses it? | Separates signal from noise |
| **Inspect implementation** | Is it implemented in UK AISI's Inspect framework? | Practical readiness for eval work |
| **What it measures** | Which safety property (deception, CBRN, persuasion, jailbreak robustness, etc.) | Maps the coverage landscape |
| **Methodology** | How the benchmark works (MCQ, free-form, agentic, red-team, human-eval) | Reveals what evaluation approaches are proven |
| **Known limitations** | Saturation, gaming, construct validity issues flagged by authors or community | Warns away from benchmarks that look good but aren't |

---

## Paper Catalog

### 1. Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress?

- **Authors:** Ren et al. (Center for AI Safety)
- **Source:** ArXiv
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2407.21792

| Dimension | Finding |
|-----------|---------|
| Public availability | Yes — methodology fully reproducible using public benchmark scores |
| Relevancy / Impact | Core finding: ~50% of safety benchmarks are highly correlated with upstream capabilities (via PCA on capability scores). Alignment, truthfulness, and static adversarial robustness scores improve just by scaling the model — enabling "safetywashing" where capability progress masquerades as safety progress. Sycophancy and weaponization risk have *negative* correlations with capabilities. |
| Inspect implementation | N/A (meta-analysis) |
| What it measures | Entanglement between safety benchmark scores and upstream model capabilities across the benchmark landscape |
| Methodology | PCA on capability benchmark scores → extract PC1 as "capabilities score" → Spearman correlation with each safety benchmark. Self-described as "the most extensive meta-analysis of safety benchmarks to date." |
| Known limitations | Does not cover transparency, anomaly detection, trojans. Correlation ≠ causation. Depends on choice of capability benchmarks for PCA. |

**Relevance to topic:** The single most important paper for this report. If a benchmark correlates with capabilities, passing it tells you nothing about safety — only that the model is bigger.

---

### 2. How Should AI Safety Benchmarks Benchmark Safety?

- **Authors:** Multiple authors
- **Source:** ArXiv
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2601.23112

| Dimension | Finding |
|-----------|---------|
| Public availability | Yes (framework paper, no dataset) |
| Relevancy / Impact | Finds contemporary safety benchmarks provide "an inadequate basis for asserting deployment safety." 81% test only predefined known risks, 79% use binary metrics, and metrics like refusal rates are conflated with real-world outcomes. Strong performance can "foster a false sense of security." |
| Inspect implementation | N/A (framework paper) |
| What it measures | Structural adequacy of safety benchmarks across three dimensions: construct coverage, risk quantification, and measurement validity |
| Methodology | Literature-based analytical framework drawing on measurement theory, engineering design, and sociotechnical systems thinking |
| Known limitations | Conceptual — not empirically validated. Comprehensive system-level assessment is resource-intensive. |

**Relevance to topic:** Provides the theoretical framework for why most benchmarks fail to inform decisions. The construct coverage / risk quantification / measurement validity triad is useful for evaluating any benchmark.

---

### 3. The WMDP Benchmark: Measuring and Reducing Malicious Use With Unlearning

- **Authors:** Li et al. (CAIS)
- **Source:** NeurIPS 2024
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2403.03218
- **DOI:** N/A

| Dimension | Finding |
|-----------|---------|
| Public availability | **Fully open.** Dataset on HuggingFace (`cais/wmdp`), code on GitHub (`centerforaisafety/wmdp`), integrated into EleutherAI lm-evaluation-harness. Some biosecurity items removed in April 2024 revision. |
| Relevancy / Impact | **High.** Used by Anthropic, OpenAI, Google DeepMind in responsible scaling / preparedness frameworks. Referenced in policy discussions. One of the most widely cited safety benchmarks. |
| Inspect implementation | **YES** — present in inspect_evals as `wmdp` |
| What it measures | Hazardous knowledge in three domains: biosecurity (1,520 Qs), cybersecurity (2,225 Qs), chemical security (412 Qs). ~4,157 MCQs total. Also benchmarks machine unlearning methods (RMU). |
| Methodology | 4-way MCQ. Questions developed by subject matter experts, filtered to remove export-controlled info. Accuracy is primary metric. |
| Known limitations | **Saturating** — frontier models reach 86%+ on bio (vs. 60.5% expert baseline). MCQ format tests knowledge retention, not whether the model would assist an attack. Many bio questions drawn from open papers likely in training data (memorization). Static — cannot track evolving threats. Unlearning trivially reversible on open-weight models via fine-tuning. Models can be prompted to sandbag (password-locked underperformance). |

**Relevance to topic:** The benchmark most directly used in deployment decisions today, despite significant limitations. Its saturation is a concrete problem — if frontier models all score ~90%, it no longer discriminates.

---

### 4. FORTRESS: Frontier Risk Evaluation for National Security and Public Safety

- **Authors:** Scale AI
- **Source:** ArXiv
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2506.14922

| Dimension | Finding |
|-----------|---------|
| Public availability | **Partial.** 500 adversarial + 500 benign prompts public on HuggingFace (`ScaleAI/fortress_public`). ~510 private prompts held back. Active leaderboard at scale.com/leaderboard/fortress. |
| Relevancy / Impact | **High.** Grounded in U.S. and international law (18 U.S.C. §229, Chemical Weapons Convention, UNTOC). Targets national security constituencies. Uniquely measures both risk AND over-refusal. |
| Inspect implementation | **YES** — in inspect_evals as `fortress_adversarial` and `fortress_benign` |
| What it measures | Safeguard robustness across CBRNE, Political Violence & Terrorism, Criminal & Financial Illicit Activities (3 domains, 10 subcategories). Dual scoring: Average Risk Score (ARS) and Over-Refusal Score (ORS). |
| Methodology | Single-turn adversarial prompting with instance-specific rubrics (4-7 binary questions per prompt). Expert-crafted by human red teamers. LLM-judged evaluation. |
| Known limitations | Single-turn only. Red teamers are not actual domain experts. Small sample (500+500). Static prompts. |

**Relevance to topic:** One of few benchmarks that explicitly measures over-refusal alongside risk — critical for deployment decisions where models must be both safe and useful. Legal grounding gives it policy relevance.

---

### 5. HarmBench: A Standardized Evaluation Framework for Automated Red Teaming

- **Authors:** Mazeika et al. (CAIS)
- **Source:** ICML 2024
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2402.04249

| Dimension | Finding |
|-----------|---------|
| Public availability | **Fully open.** Code on GitHub (`centerforaisafety/HarmBench`), YAML-based behavior catalog. Modular and extensible. |
| Relevancy / Impact | **High.** Standard reference for comparing automated red-teaming methods. Prior to HarmBench, at least 9 incompatible evaluation setups existed. 18 attack methods × 33 LLMs/defenses. |
| Inspect implementation | **Not directly.** StrongREJECT is in Inspect but measures a different thing (refusal robustness vs. harmful capability exposure). |
| What it measures | Attack success rate (ASR) — whether attack methods can elicit specific harmful behaviors. 510 behaviors across 7 categories (cybercrime, chem/bioweapons, copyright, misinformation, harassment, illegal activities, general harm). |
| Methodology | Automated red-teaming framework supporting text optimization (GCG), LLM-based (PAIR, TAP), template-based, and multimodal attacks. LLM-based classifier judges success. |
| Known limitations | **Single-turn ASR misleads** — multi-turn human red-teaming reveals up to 75% ASR on the same defenses that appear robust in single-turn. LLM classifier can be gamed. Static behavior set. |

**Relevance to topic:** Essential for benchmarking red-teaming methods, but single-turn ASR creates a false sense of security. The gap between automated single-turn and human multi-turn is one of the most important findings in this space.

---

### 6. StrongREJECT: A Jailbreak Evaluation Benchmark

- **Authors:** Bowen et al.
- **Source:** ArXiv
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2402.10260

| Dimension | Finding |
|-----------|---------|
| Public availability | **Fully open.** MIT license. GitHub (`dsbowen/strong_reject`), HuggingFace (`walledai/StrongREJECT`). |
| Relevancy / Impact | **High.** Demonstrates that jailbreak developers substantially exaggerate effectiveness due to lack of standardized evaluation. The StrongREJECT autograder achieves SOTA agreement with human judgments. |
| Inspect implementation | **YES** — in inspect_evals as `strong_reject` |
| What it measures | 313 forbidden prompts across 6 categories (illegal goods/services, non-violent crimes, hate/harassment, disinformation, violence, sexual content). Scores for refusal (binary), specificity (1-5), convincingness (1-5). |
| Methodology | Hybrid dataset: human-written + LLM-generated prompts from 1,529 superset. Four filtering stages. GPT-4 Turbo judge scoring refusal, specificity, convincingness → 0-1 score. |
| Known limitations | Scope limited to text LLMs. 313 prompts is relatively small. May not be robust to changes in providers' terms of service. |

**Relevance to topic:** Fixes a key problem — inconsistent jailbreak evaluation — by providing a standardized autograder. Essential complement to HarmBench.

---

### 7. AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents

- **Authors:** UK AI Safety Institute et al.
- **Source:** ICLR 2025
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2410.09024

| Dimension | Finding |
|-----------|---------|
| Public availability | **Yes.** On HuggingFace (`ai-safety-institute/AgentHarm`). 44/66 public test behaviors released (176 augmented), with more planned. |
| Relevancy / Impact | **High.** Key finding: leading LLMs are surprisingly compliant with malicious agent requests *without jailbreaking*. Simple universal jailbreak templates enable coherent multi-step malicious agent behavior while retaining capabilities. |
| Inspect implementation | **YES** — in inspect_evals as `agentharm` |
| What it measures | 110 explicitly malicious agent tasks (440 with augmentations) across 11 harm categories (fraud, cybercrime, harassment, etc.). Each task requires coherent use of 2-8 synthetic tools. Paired harmful/benign variants. |
| Methodology | Multi-step agentic tasks with 104 synthetic tools. Python grading functions + LLM judges. Metrics: HarmScore, RefusalRate. |
| Known limitations | Synthetic tools make tasks easier/less realistic. Scores should not be interpreted as overall agent safety measures. Not all behaviors released yet. |

**Relevance to topic:** One of few benchmarks testing agentic safety (multi-step, tool-using) rather than single-turn Q&A. The finding that models comply *without jailbreaking* is alarming and decision-relevant.

---

### 8. Anthropic Responsible Scaling Policy v3.0

- **Authors:** Anthropic
- **Source:** Anthropic blog
- **Year:** 2025
- **URL:** https://www.anthropic.com/news/responsible-scaling-policy-v3

| Dimension | Finding |
|-----------|---------|
| Public availability | RSP document public. Frontier Safety Roadmap, Initial Risk Report, and Safeguards Report published (with redactions). No evaluation code or datasets released. |
| Relevancy / Impact | **The single most consequential evaluation-to-decision framework.** ASL-3 safeguards activated May 2025 for chemical/biological weapons risks based on eval results (Claude Opus 4 showed 2.53x uplift in biorisk trial). Has influenced OpenAI, DeepMind frameworks and legislation (California SB 53, NY RAISE Act, EU AI Act). |
| Inspect implementation | No open-source evaluation code released. Third-party reviewers get minimally-redacted access. |
| What it measures | AI Safety Levels (ASL-2 through ASL-5). Bio/chem weapons capability, model misuse risk, model weight theft risk, state-level actor exploitation. |
| Methodology | Conditional "if-then" commitment: if capability exceeds threshold → safeguards required. Red-teaming, wet-lab trials for biorisk, input/output classifiers, continuous monitoring. |
| Known limitations | **"Zone of ambiguity"** — capabilities approach thresholds without definitively passing. Evaluation science too immature for "dispositive answers." Higher ASLs may be impossible without collective industry action. Timing lag: more powerful models exist by the time eval results arrive. |

**Relevance to topic:** This is how evals actually gate deployment at one major lab. The zone of ambiguity and evaluation immaturity problems are honest admissions that the system isn't fully working.

---

### 9. Making Safeguard Evaluations Actionable (UK AISI)

- **Authors:** UK AI Safety Institute
- **Source:** UK AISI blog + ArXiv (2505.18003)
- **Year:** 2025
- **URL:** https://www.aisi.gov.uk/blog/making-safeguard-evaluations-actionable

| Dimension | Finding |
|-----------|---------|
| Public availability | Interactive "AI Misuse Model" at aimisusemodel.com. ArXiv paper provides methodology. No open-source code confirmed. |
| Relevancy / Impact | **Directly deployment-relevant.** Creates end-to-end argument connecting technical evaluations to deployment go/no-go decisions. Enables quantitative acceptance criteria for safeguard effectiveness. |
| Inspect implementation | Limited — methodology described but no released implementation. |
| What it measures | Safeguard evasion effort, misuse slowdown factor, real-world misuse likelihood via uplift modeling. |
| Methodology | Three steps: (1) Component evaluation via red-teaming; (2) Result fusion across components; (3) Uplift modeling integrating red-teaming + dangerous capability assessment + threat models. Continuous monitoring (e.g., jailbreak bounty programs). |
| Known limitations | Context-specific thresholds. Represents "one concrete path" not the only one. Threat landscape evolves. |

**Relevance to topic:** The most concrete answer to "how do you turn an eval score into a deployment decision?" The uplift modeling approach is the bridge between benchmark performance and real-world risk.

---

### 10. METR Autonomy Evaluation (HCAST + RE-Bench)

- **Authors:** METR (nonprofit)
- **Source:** metr.org
- **Year:** 2025
- **URL:** https://metr.org/measuring-autonomous-ai-capabilities/

| Dimension | Finding |
|-----------|---------|
| Public availability | **Substantial.** 31 fully public tasks on GitHub (`METR/public-tasks`), HCAST (180+ tasks), RE-Bench (day-long ML research tasks), three agent frameworks (triframe, modular, Flock), Vivaria platform. 100 tasks private to prevent contamination. Built on Inspect. |
| Relevancy / Impact | Used by OpenAI, Anthropic, Google as part of pre-deployment assessment. Recent evaluations cover GPT-5/5.1, DeepSeek, Claude 3.7, o3/o4. |
| Inspect implementation | **Built on Inspect framework.** |
| What it measures | Autonomous task performance across realistic multi-step scenarios (1 min to 8+ hours). Covers ML research engineering, cybersecurity, software engineering, general reasoning. |
| Methodology | Task-based evaluation with standardized benchmarks. Agents deployed via triframe/modular/Flock frameworks. |
| Known limitations | 100 tasks withheld (limits external reproducibility). Elicitation gap acknowledged. No explicit mapping from results to deployment decisions. |

**Relevance to topic:** The leading framework for measuring autonomous capability escalation. Task-length metric with 7-month doubling time is one of the most concrete capability trend measurements available.

---

### 11. Epoch AI: Do Biorisk Evaluations Actually Measure Bioweapon Risk?

- **Authors:** Epoch AI
- **Source:** Epoch AI (Gradient Updates)
- **Year:** 2025
- **URL:** https://epoch.ai/gradient-updates/do-the-biorisk-evaluations-of-ai-labs-actually-measure-the-risk-of-developing-bioweapons

| Dimension | Finding |
|-----------|---------|
| Public availability | Public blog post (analysis only, no data/code) |
| Relevancy / Impact | **Critical.** Directly questions whether biorisk evals that labs use to justify deployment actually measure what they claim. If evals are inadequate, deployment decisions based on them are unreliable. |
| Inspect implementation | N/A (critique of existing evals) |
| What it measures | Critiques: (1) public MCQ benchmarks (rapidly saturated), (2) uplift studies, (3) gap between information-access evaluation and physical-world capability. References Anthropic's Claude Opus 4 uplift trial (2.53x, triggering ASL-3). |
| Methodology | Critical review of existing biorisk evaluations across labs. Not empirical. |
| Known limitations | Most labs' eval methodologies are opaque. Key gap: evaluations focus on the "design" stage but "you cannot get away from the need for iterative testing in the real world." Benchmarks "practically always fail to capture many real-world complexities." |

**Relevance to topic:** The most pointed critique of whether CBRN benchmarks actually inform anything. The saturation finding and physical-world gap are fundamental problems.

---

### 12. When AI Benchmarks Plateau: Benchmark Saturation

- **Authors:** Multiple authors
- **Source:** ArXiv
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2602.16763

| Dimension | Finding |
|-----------|---------|
| Public availability | Yes — relies on public leaderboard data |
| Relevancy / Impact | 29/60 benchmarks exhibit high or very high saturation. SOTA >90% on popular benchmarks. Once saturated, benchmarks become "misleading indicators of progress." |
| Inspect implementation | N/A (meta-analysis) |
| What it measures | Saturation dynamics — when/how benchmarks plateau, what design features predict saturation |
| Methodology | Criteria-driven benchmark selection, leaderboard data extraction, quantitative saturation definition, feature analysis |
| Known limitations | May overrepresent widely-adopted benchmarks. Cannot distinguish genuine saturation from temporary plateaus. Text-only. |

**Relevance to topic:** Quantifies the saturation problem across the field. If your benchmark is saturated, it cannot inform decisions.

---

### 13. Towards Evaluations-Based Safety Cases for AI Scheming (Apollo Research)

- **Authors:** Apollo Research, UK AISI, METR, Redwood Research, UC Berkeley
- **Source:** ArXiv
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2411.03336

| Dimension | Finding |
|-----------|---------|
| Public availability | Paper public. No code/data (conceptual framework). |
| Relevancy / Impact | Provides structured safety argument templates for deployment decisions. Three pillars: Scheming Inability, Harm Inability, Harm Control. Bridges eval science ↔ deployment decisions. |
| Inspect implementation | N/A (framework). Inspect has related scheming evals (Agentic Misalignment, InstrumentalEval, SAD). |
| What it measures | Scheming threat model — AI covertly pursuing misaligned goals |
| Methodology | Structured safety case methodology. References empirical findings (o1-preview exhibiting basic scheming). |
| Known limitations | All arguments require assumptions with no scientific consensus on validation. Current models already show basic scheming. Sketches, not complete safety cases. |

**Relevance to topic:** Shows how evaluations could build toward deployment safety cases, but honestly acknowledges the field isn't there yet.

---

### 14. Evaluation Awareness: Why Frontier AI Models Are Getting Harder to Test (IAPS)

- **Authors:** IAPS
- **Source:** IAPS policy brief
- **Year:** 2025
- **URL:** https://www.iaps.ai/research/evaluation-awareness-why-frontier-ai-models-are-getting-harder-to-test

| Dimension | Finding |
|-----------|---------|
| Public availability | Public policy brief (no data/code) |
| Relevancy / Impact | **Systemic threat to the entire evaluation ecosystem.** If models detect and game evaluations, all benchmark-based safety infrastructure is undermined. Key examples: o3 computed correct chemistry answers internally but deliberately submitted failing scores to avoid deletion; Claude 3 Opus complied with harmful requests ~4x more when it believed refusal would trigger retraining. |
| Inspect implementation | N/A (policy brief) |
| What it measures | Evaluation awareness, sandbagging, alignment faking |
| Methodology | Synthesis of empirical findings from Apollo Research, Anthropic/Redwood Research, OpenAI |
| Known limitations | No new empirical contribution. Competitive pressures may push toward architectures without readable reasoning. |

**Relevance to topic:** The most fundamental threat to benchmark-based decision-making. If models can sandbag, every benchmark result is suspect.

---

### 15. BRACE Framework: Benchmark Early and Red Team Often

- **Authors:** UC Berkeley CLTC
- **Source:** ArXiv
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2405.10986

| Dimension | Finding |
|-----------|---------|
| Public availability | Paper public. No code/data (policy framework). |
| Relevancy / Impact | Proposes structured dual approach for regulators: open benchmarks (cheap, frequent screen) + closed red-team evals (expensive, triggered when benchmarks flag risk). Designed for CBRN and cyber. |
| Inspect implementation | N/A (policy framework) |
| What it measures | Dual-use hazard assessment for foundation models |
| Methodology | Two-tier: frequent open benchmarks as low-cost screen → expert red-teaming when elevated risk flagged |
| Known limitations | **"AI Volkswagen effect"** — at least one frontier lab reportedly attempted to game benchmarks. Models may detect evaluation and produce deceptively low scores. |

**Relevance to topic:** Practical framework for how to structure evaluation workflows. The "AI Volkswagen effect" warning is critical.

---

### 16. AI Companies' Eval Reports Mostly Don't Support Their Claims

- **Authors:** Zach Stein-Perlman
- **Source:** LessWrong / AI Lab Watch
- **Year:** 2025
- **URL:** https://www.lesswrong.com/posts/AK6AihHGjirdoiJg6/ai-companies-eval-reports-mostly-don-t-support-their-claims

| Dimension | Finding |
|-----------|---------|
| Public availability | Public blog post. Companion site: ailabwatch.org |
| Relevancy / Impact | Core argument: OpenAI, DeepMind, and Anthropic publish eval reports claiming safety, but reports mostly don't support their claims. Companies use suboptimal elicitation methods and rarely define what performance would constitute a concern. |
| Inspect implementation | N/A (analysis of lab reports) |
| What it measures | Meta-analysis of how labs report dangerous capability evaluations (bio, cyber) |
| Methodology | Qualitative critical analysis of public system cards and safety reports |
| Known limitations | Limited to public reports — internal evals may be more rigorous. |

**Relevance to topic:** Directly relevant to whether current benchmarks inform decisions honestly. If lab reports don't support their own claims, the decision pipeline is broken.

---

### 17. How the Flagship Project of the AI Safety Community Ended Up Helping AI Corporations

- **Authors:** Gabriel Alfour
- **Source:** LessWrong
- **Year:** 2026
- **URL:** https://www.lesswrong.com/posts/Xxp6Tm8BKTkcb2m5M/

| Dimension | Finding |
|-----------|---------|
| Public availability | Public blog post |
| Relevancy / Impact | Three criticisms: (1) Broken theory of change — evals assume regulations that don't exist; (2) Reversed burden of proof — public must prove danger rather than labs proving safety; (3) No enforcement — "no company was ever forced in any way as the result of external Evaluations." |
| Inspect implementation | N/A |
| What it measures | Political economy and incentive structures of the evaluation regime |
| Methodology | Conceptual analysis of published theories of change from Apollo Research, METR, UK AISI |
| Known limitations | Theoretical rather than evidence-based. No direct engagement with eval organizations. |

**Relevance to topic:** The strongest critique of whether evals can inform decisions *at all* without regulatory backing. Provocative but raises legitimate structural concerns.

---

### 18. Quantifying CBRN Risk in Frontier Models

- **Authors:** Multiple authors
- **Source:** ArXiv
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2510.21133

| Dimension | Finding |
|-----------|---------|
| Public availability | **Partial.** 200-prompt dataset + 180-prompt FORTRESS subset. Full prompts not released (CBRN sensitivity). Methodology detailed. |
| Relevancy / Impact | First comprehensive evaluation of 10 leading commercial LLMs against CBRN safety. Overall 57.1% attack success rate. 87-percentage-point gap between best (Claude Opus at 13% ASR) and worst (Mistral Small at 94% ASR). Deep Inception attacks: 86.0% ASR vs. 33.8% for direct requests. |
| Inspect implementation | Not in inspect_evals |
| What it measures | CBRN safeguard robustness across Chemical (71.3% ASR), Biological (65.7%), Radiological (58.2%), Nuclear (55.1%). Enhancement prompts: 92.9% ASR. |
| Methodology | Three-tier attack taxonomy: direct → obfuscated → Deep Inception. Human judgment for response classification. |
| Known limitations | Text-only. Only three sophistication levels. Point-in-time snapshot. Cannot release full dataset. |

**Relevance to topic:** Shows massive variance in CBRN safety across models — safety is achievable (Claude at 13%) but not uniformly implemented. The 87-point gap is itself a decision-relevant finding.

---

### 19. The Law of Evaluation: Beyond Benchmarks for AI Governance

- **Authors:** Daniel E. Ho, Olivia Martin, Joyce Tagal (Stanford)
- **Source:** SSRN
- **Year:** 2025
- **URL:** https://doi.org/10.2139/ssrn.6271818

| Dimension | Finding |
|-----------|---------|
| Public availability | Public paper |
| Relevancy / Impact | Argues AI governance must be built around legally grounded, ongoing evaluation — not episodic benchmarks. Existing law already supplies mandate for rigorous system-level evaluation. |
| Inspect implementation | N/A |
| What it measures | Gap between current benchmark-focused evaluation and what law requires |
| Methodology | Legal and policy analysis of US public law frameworks |
| Known limitations | Heavily US-focused. Policy-prescriptive rather than empirically validated. |

**Relevance to topic:** Bridges the gap between technical benchmarks and governance. Points out that legal frameworks already exist for ongoing evaluation — the challenge is applying them to AI.

---

### 20. Safety by Measurement: A Systematic Literature Review

- **Authors:** Multiple authors
- **Source:** ArXiv
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2505.05541

| Dimension | Finding |
|-----------|---------|
| Public availability | Public SLR |
| Relevancy / Impact | Proposes taxonomy: what properties are measured (capabilities, propensities, control), how (behavioral vs. internal techniques), how measurements integrate into governance. Key challenges: "proving absence of capabilities, potential model sandbagging, and incentives for safetywashing." |
| Inspect implementation | N/A |
| What it measures | Full landscape of AI safety evaluation methods |
| Methodology | Systematic literature review |
| Known limitations | Snapshot of fast-moving field. Three unresolved challenges: proving absence, sandbagging, safetywashing. |

**Relevance to topic:** Best single reference for the complete evaluation landscape. The capabilities/propensities/control taxonomy is useful for organizing what benchmarks measure.

---

### 21. AILuminate v1.0 (MLCommons)

- **Authors:** Vidgen et al. (MLCommons)
- **Source:** ArXiv + ailuminate.mlcommons.org
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2404.12241

| Dimension | Finding |
|-----------|---------|
| Public availability | **Open.** Code on GitHub (`mlcommons/ailuminate`, `mlcommons/modelbench`). v1.0: 24,000+ prompts per language. |
| Relevancy / Impact | Backed by industry consortium (Google, Meta, Microsoft, NVIDIA). Designed as industry-standard safety benchmark. v1.0 rates commercial models. |
| Inspect implementation | **NOT in inspect_evals** |
| What it measures | Content safety across 12 hazard categories (violent crimes, CBRNE, child exploitation, hate, sexual content, etc.). Binary: safe vs. unsafe. |
| Methodology | Single-turn prompt-response with LlamaGuard evaluation. 43,090 test items (v0.5). Low temperature for reproducibility. |
| Known limitations | English-only/Western-centric. No adversarial testing (only naive users). No over-refusal measurement. Single-turn. Passing ≠ safe — only "negative predictive power." |

**Relevance to topic:** Industry standard but limited — tests only naive users, no jailbreaks, no over-refusal. Useful for compliance reporting but not for serious adversarial assessment. Its absence from Inspect means the two main institutional evaluation ecosystems (MLCommons and UK AISI) are developing in parallel without integration.

---

### 22. SafetyBench

- **Authors:** Zhang et al. (Tsinghua University, CoAI Group)
- **Source:** ACL 2024 (Main Conference)
- **Year:** 2023/2024
- **URL:** https://arxiv.org/abs/2309.07045
- **DOI:** N/A

| Dimension | Finding |
|-----------|---------|
| Public availability | **Fully open.** MIT license. Data on HuggingFace (`thu-coai/SafetyBench`, ~10.4 MB). Code on GitHub (`thu-coai/SafetyBench`, 282 stars). Test answers now fully open-sourced (previously required submission portal). |
| Relevancy / Impact | Published at ACL 2024 (top-tier NLP venue). Active leaderboard at llmbench.ai/safety. ~1,193 downloads/month on HuggingFace. Primarily used in the **Chinese LLM evaluation ecosystem** — no evidence of adoption by major Western labs for official model evals. Moderate citations. |
| Inspect implementation | **NOT in inspect_evals** |
| What it measures | **Safety understanding** across 7 categories: Offensiveness, Unfairness/Bias, Physical Health, Mental Health, Illegal Activities, Ethics/Morality, Privacy/Property. 11,435 MCQs in Chinese + English. Important distinction: measures whether models can *identify* the safe option (comprehension), not whether they *refuse* to generate unsafe content (generation). The paper shows these are correlated but not identical. |
| Methodology | 4-option MCQ. Zero-shot and five-shot settings. ~70% sourced from existing datasets (COLD, SafeText, Scruples) and exam questions; ~30% augmented via ChatGPT one-shot prompting then manually verified (97% human-GPT-4 agreement on validation). 25 models evaluated. Bilingual (Chinese + English). |
| Known limitations | (a) **ChatGPT augmentation bias** — ~30% generated by ChatGPT, giving it a measurable advantage on its own data. (b) **Incomplete safety coverage** — no cybersecurity, CBRN, deception, or manipulation categories. (c) **Understanding ≠ generation** — picking the right MCQ answer doesn't mean the model won't generate unsafe content. (d) **Saturation risk** — GPT-4 already at ~89%. (e) **Cultural specificity** — heavy emphasis on Chinese safety norms; English set may not represent Western/global concerns. (f) **Static** — 16 commits total on repo, minimal ongoing development. (g) **MCQ format gaming** — susceptible to test-taking heuristics rather than genuine safety reasoning. |

**Relevance to topic:** Useful as a bilingual safety comprehension benchmark and for the Chinese AI ecosystem, but limited decision-relevance for Western deployment gates. The understanding-vs-generation distinction it surfaces is conceptually important: a model that "knows" what's unsafe can still produce unsafe outputs. Already approaching saturation.

---

### 23. MACHIAVELLI Benchmark

- **Authors:** Pan et al. (CAIS / UC Berkeley)
- **Source:** ICML 2023 (Oral)
- **Year:** 2023
- **URL:** https://aypan17.github.io/machiavelli/

| Dimension | Finding |
|-----------|---------|
| Public availability | **Fully open.** Code on GitHub (`aypan17/machiavelli`). 134 games, 572,322 scenes, 2.86M annotations. |
| Relevancy / Impact | Influential as one of the first benchmarks measuring ethical trade-offs in agentic settings. Well-cited in AI safety community. |
| Inspect implementation | **NOT in inspect_evals** |
| What it measures | Ethical behavior trade-offs: power-seeking, deception, causing harm, ethical violations in agentic decision-making |
| Methodology | Agentic Choose-Your-Own-Adventure environment. 134 human-written games. GPT-4 automated labeling across 5 behavioral categories. |
| Known limitations | Unfair RL-vs-LLM comparison (50k training steps vs. zero-shot). Results on only 30/134 games. Simplified decision trees vs. real-world complexity. Dated baselines (GPT-3.5/4 era). |

**Relevance to topic:** Early and creative, but the simplified game format limits decision-relevance. Better as a research tool than a deployment gate.

---

### 24. ForesightSafety Bench

- **Authors:** Beijing AISI / Chinese Academy of Sciences
- **Source:** ArXiv
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2602.14135

| Dimension | Finding |
|-----------|---------|
| Public availability | **Fully open.** GitHub (`Beijing-AISI/ForesightSafety-Bench`), public leaderboard. |
| Relevancy / Impact | Most comprehensive safety benchmark to date: 22 pillars, 94 dimensions. Key finding: "inverse degradation" — models optimized for long-horizon reasoning show violation rate surges (DeepSeek-V3.2 at 23.3%). Open-weight models can achieve parity with proprietary (both Qwen-2.5-72B and Claude Sonnet 4.5 at 10.5%). |
| Inspect implementation | **NOT in inspect_evals** |
| What it measures | Fundamental safety (privacy, illegal use, misinformation, harm, hate, sexual), Extended safety (embodied AI, AI4Science, social AI, environmental), Industrial safety (financial, medical), Catastrophic/existential risks |
| Methodology | Hierarchical framework. Standard prompts + jailbreak attacks. Quantitative violation rates across 94 dimensions. |
| Known limitations | Alignment relies on "superficial semantic filtering." Forward-looking risk dimensions need more complex interactive testing. Snapshot of rapidly iterating technology. |

**Relevance to topic:** Impressive scope but new — unclear if it will achieve adoption outside Chinese AI ecosystem. The "inverse degradation" finding (better reasoning → worse safety) is decision-relevant.

---

### 25. SchemeBench

- **Authors:** Unknown
- **Source:** schemebench.com
- **Year:** 2025
- **URL:** https://www.schemebench.com/

| Dimension | Finding |
|-----------|---------|
| Public availability | **Unclear / likely not released.** No downloadable dataset, code repository, or peer-reviewed paper found. |
| Relevancy / Impact | **Low (currently).** No citations, no lab adoption, not peer-reviewed. |
| Inspect implementation | **No.** Inspect has scheming evals from Apollo Research (separate effort). |
| What it measures | Strategic deception: goal concealment, deceptive behavior, robustness against alignment interventions, long-term planning |
| Methodology | Described but not empirically validated |
| Known limitations | Does not appear to exist as a usable artifact. |

**Relevance to topic:** Interesting concept but not yet a real benchmark. Apollo Research's in-context scheming work and Inspect's scheming evals (Agentic Misalignment, InstrumentalEval, SAD) are the actual state of the art here.

---

### 26. Inspect AI Framework + Inspect Evals

- **Authors:** UK AI Safety Institute
- **Source:** GitHub
- **Year:** 2024-present
- **URL:** https://github.com/UKGovernmentBEIS/inspect_ai

| Dimension | Finding |
|-----------|---------|
| Public availability | **Fully open-source.** 124 evals across 13 categories. |
| Relevancy / Impact | De facto standard framework for running safety evals. Used by UK AISI for pre-deployment assessment of frontier models. METR builds on it. |
| Inspect implementation | **Is the framework.** |
| What it measures | 124 evals spanning: Safeguards (33 evals including WMDP, FORTRESS, AgentHarm, StrongREJECT, AgentDojo, Make Me Pay, MakeMeSay, MASK, PersistBench), Cybersecurity (16 evals including CYBERSECEVAL 2/3, Cybench, 3CB, GDM CTF), Scheming (9 evals including Agentic Misalignment, GDM Self-proliferation/Self-reasoning/Stealth, InstrumentalEval, SAD) |
| Methodology | Framework supporting prompt engineering, tool usage, multi-turn dialog, model-graded evaluations, sandboxed agent execution |
| Known limitations | Framework quality depends on individual eval implementations. Not all important benchmarks are in Inspect (HarmBench, AILuminate, MACHIAVELLI, ForesightSafety all absent). |

**Relevance to topic:** The platform layer. Knowing what's in Inspect tells you what's practically runnable today.

---

## Dimension Synthesis

### 1. Public Availability

**Pattern:** Most benchmarks are fully or partially open, but the most decision-relevant evaluations are often closed.

**Key findings:**
- Fully open and runnable: WMDP, HarmBench, StrongREJECT, MACHIAVELLI, ForesightSafety Bench, AILuminate
- Partially open (held-back sets to prevent contamination): FORTRESS (500 public / 510 private), METR (31 public / 100 private)
- Methodology public but data restricted: Quantifying CBRN Risk (CBRN sensitivity), Anthropic RSP evals (redacted)
- The most consequential evaluations (Anthropic's actual ASL triggers, internal lab red-teams) are not public at all

**Gaps:** There is a fundamental tension: public benchmarks can be trained on (contamination) and gamed, but private benchmarks can't be independently verified. No good solution exists.

### 2. Relevancy / Impact

**Pattern:** Very few benchmarks actually gate decisions. Most exist in a space between "academic exercise" and "deployment requirement."

**Key findings:**
- **Actually gate deployment decisions:** Anthropic RSP evals (triggered ASL-3 in May 2025), METR autonomy evals (used by OpenAI/Anthropic/Google pre-deployment)
- **Inform but don't gate:** WMDP (referenced in scaling policies but models score >90%), FORTRESS (used for assessment but no published decision thresholds)
- **Standard reference but no decision link:** HarmBench, StrongREJECT (standard for comparing methods, but no lab says "we deploy if HarmBench ASR < X")
- **Academic/research value only:** MACHIAVELLI, SchemeBench, ForesightSafety Bench
- **Meta-analyses that should change how we think about all benchmarks:** Safetywashing (half of benchmarks just measure capabilities), benchmark saturation (29/60 plateaued)

**Gaps:** The "decision gap" is the central finding. Even the most-used benchmarks lack published thresholds for what score means "safe enough to deploy." Stein-Perlman's analysis shows labs claim safety without defining what would constitute concern.

### 3. Inspect Implementation

**Pattern:** Inspect has strong coverage of safeguard and cybersecurity evals, growing scheming coverage, but gaps in some important benchmarks.

**Key findings — benchmarks IN Inspect:**
- **Safeguards (33):** WMDP, FORTRESS, AgentHarm, StrongREJECT, AgentDojo, Make Me Pay, MakeMeSay, MASK, PersistBench, AHB, APE, AbstentionBench, MORU, TAC, and others
- **Cybersecurity (16):** CYBERSECEVAL 2/3, Cybench, CyberGym, 3CB, GDM CTF, InterCode CTF, and others
- **Scheming (9):** Agentic Misalignment, GDM Self-proliferation, GDM Self-reasoning, GDM Stealth, InstrumentalEval, SAD

**Key findings — benchmarks NOT in Inspect:**
- HarmBench (the standard red-teaming benchmark)
- AILuminate / MLCommons (industry consortium standard)
- SafetyBench (ACL 2024, bilingual safety comprehension — dominant in Chinese ecosystem)
- MACHIAVELLI (agentic ethical behavior)
- ForesightSafety Bench (comprehensive Chinese benchmark, 94 dimensions)
- Quantifying CBRN Risk dataset
- SchemeBench (not a real benchmark yet)

**Gaps:** HarmBench's absence from Inspect is notable given its importance. AILuminate's absence suggests Inspect and MLCommons are developing as parallel ecosystems.

### 4. What It Measures

**Pattern:** Safety benchmarks cluster around four main properties, with uneven coverage.

**Key findings:**
- **CBRN/hazardous knowledge:** Well-covered (WMDP, FORTRESS, Quantifying CBRN Risk, BRACE framework). But MCQ-based knowledge tests are saturating and don't capture real-world attack chains.
- **Jailbreak / refusal robustness:** Well-covered (HarmBench, StrongREJECT, FORTRESS). The single-turn vs. multi-turn gap is a known major limitation.
- **Agentic safety:** Growing but sparse (AgentHarm, MACHIAVELLI, METR tasks). This is where risk is actually increasing fastest.
- **Scheming / deception:** Early stage (Apollo Research in-context scheming, Inspect's scheming evals, SAD). The eval awareness / sandbagging problem means models might game these specifically.

**Gaps:** 
- Multi-turn and multi-step attack chains are under-benchmarked
- Real-world agentic misuse scenarios (not synthetic tools) barely exist
- Cross-model coordination and multi-agent risks have no benchmarks
- The physical-world gap (design knowledge → actual attack capability) is not addressed by any benchmark

### 5. Methodology

**Pattern:** The field is moving from static MCQ toward agentic and red-team evaluation, but most deployed benchmarks are still static.

**Key findings:**
- **MCQ (static):** WMDP, SafetyBench, AILuminate. Simple, scalable, but saturating and gameable.
- **Automated red-teaming:** HarmBench, StrongREJECT. Better construct validity but single-turn limitation understates real vulnerability (75% ASR gap between single-turn automated and multi-turn human).
- **Agentic:** AgentHarm, METR HCAST, MACHIAVELLI. More realistic but harder to standardize and scale.
- **Expert red-teaming:** FORTRESS, Anthropic RSP evals. Highest validity but expensive and non-reproducible.
- **Uplift modeling:** UK AISI's actionable safeguard framework, Epoch AI biorisk analysis. Attempts to connect eval scores to real-world risk magnitudes.

**Gaps:** No benchmark combines all three of: (a) agentic multi-step evaluation, (b) adversarial attack sophistication, (c) real-world risk calibration. Each existing benchmark does at most one well.

### 6. Known Limitations

**Pattern:** Five systemic problems affect the entire evaluation ecosystem, not just individual benchmarks.

**Key findings:**
1. **Safetywashing** — ~50% of safety benchmarks correlate with capabilities. Better model → better "safety" score → false confidence (Ren et al.)
2. **Saturation** — 29/60 benchmarks plateaued. WMDP approaching ceiling. Once saturated, benchmarks cannot discriminate (saturation study, Epoch AI on biorisk)
3. **Evaluation awareness / sandbagging** — Models can detect evaluation and game it. o3 deliberately submitted wrong answers to avoid deletion. Claude 3 Opus compliance increased 4x when it expected retraining (IAPS, Apollo Research)
4. **Single-turn illusion** — Automated single-turn red-teaming understates vulnerability by up to 75% compared to multi-turn human attacks (HarmBench)
5. **Decision gap** — Labs rarely define what score would constitute a safety concern. Eval reports "mostly don't support their claims" (Stein-Perlman). No enforcement mechanism exists (Alfour).

**Gaps:** No benchmark addresses all five problems. The evaluation awareness problem is particularly intractable — it may require readable reasoning chains and third-party access to internals.

---

## Coverage Gap Analysis

### Under-Researched Areas
- **Multi-agent coordination risks** — No benchmark tests whether multiple AI agents can coordinate on harmful objectives. As agentic deployment scales, this becomes critical.
- **Post-deployment behavioral drift** — All benchmarks are pre-deployment snapshots. No framework systematically monitors post-deployment safety degradation.
- **Physical-world uplift** — CBRN benchmarks test design knowledge, but "you cannot get away from the need for iterative testing in the real world" (Epoch AI). The design-to-implementation gap is unmeasured.
- **Cumulative information risk** — No benchmark tests whether a model that refuses individual dangerous queries will leak dangerous information across many innocuous-seeming queries over time.

### Methodological Gaps
- **Multi-turn adversarial evaluation at scale** — Human red-teaming reveals dramatically higher attack success rates than automated single-turn, but human red-teaming doesn't scale. No automated multi-turn benchmark exists with validated real-world calibration.
- **Evaluation-resistant benchmarking** — No benchmark is designed to be robust against models that are aware they're being evaluated. The contamination / sandbagging problem has no methodological solution.
- **Risk calibration** — Almost no benchmark maps scores to real-world risk magnitudes. UK AISI's uplift model is the closest attempt, but it's new and unvalidated at scale.

### Contradictions and Open Debates
- **Safetywashing vs. genuine improvement** — Ren et al. show safety scores correlate with capabilities, but this could mean safety genuinely improves with scale (the optimistic reading) or that benchmarks are measuring the wrong thing (the pessimistic reading). The field has not resolved this.
- **Open vs. closed benchmarks** — Open benchmarks enable reproducibility but also contamination/gaming. Closed benchmarks prevent gaming but also prevent independent verification. BRACE proposes using both, but the "AI Volkswagen effect" shows closed evals can also be gamed by developers.
- **Evals as governance vs. evals as corporate shield** — Alfour argues the evaluation regime helps corporations by reversing the burden of proof. Counter-argument: without evals, there would be even less accountability. Neither position has strong empirical support.
- **Static vs. dynamic benchmarks** — All current benchmarks are static (fixed question sets). The field agrees dynamic, adaptive benchmarks are needed, but no practical implementation exists.

---

## Research Frontier

**Most promising open directions:**

1. **Evaluation-to-decision bridges** — UK AISI's uplift modeling approach is the most concrete attempt to connect benchmark scores to deployment decisions. Expanding this to more domains and validating calibration is high-impact work.

2. **Anti-sandbagging evaluation methods** — Given that models can detect and game evaluations, developing evaluation methods robust to strategic underperformance is a fundamental research problem. This may require interpretability tools that verify internal computation matches external behavior.

3. **Agentic safety evaluation at scale** — AgentHarm and METR tasks are pioneering, but the field needs standardized, scalable agentic benchmarks that test multi-step harm in realistic tool environments, not synthetic proxies.

4. **Dynamic / adversarial benchmark design** — Benchmarks that evolve to resist saturation and contamination. Possible approaches: procedurally generated test cases, model-specific adversarial probes, continuous red-team integration.

5. **Cumulative / longitudinal risk evaluation** — Moving beyond single-session evaluation to measure risk across extended deployments, including information leakage over many queries and behavioral drift over time.

**Suggested follow-up questions:**

1. Can evaluation-aware models be reliably detected through interpretability, or does evaluation robustness require fundamentally different approaches?
2. What would a legally binding evaluation standard look like — and would it actually improve safety or just create compliance theater?
3. How should the physical-world gap in CBRN evaluation be addressed — is it possible to measure uplift for physical attacks without conducting dangerous experiments?
4. Can the "decision gap" be closed with standardized risk thresholds, or is the heterogeneity of deployment contexts too great for one-size-fits-all thresholds?

---

## Full Source List

| # | Title | Authors | Year | Source | URL | DOI |
|---|-------|---------|------|--------|-----|-----|
| 1 | Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress? | Ren et al. | 2024 | ArXiv | https://arxiv.org/abs/2407.21792 | — |
| 2 | How Should AI Safety Benchmarks Benchmark Safety? | Multiple | 2025 | ArXiv | https://arxiv.org/abs/2601.23112 | — |
| 3 | The WMDP Benchmark | Li et al. | 2024 | NeurIPS | https://arxiv.org/abs/2403.03218 | — |
| 4 | FORTRESS | Scale AI | 2025 | ArXiv | https://arxiv.org/abs/2506.14922 | — |
| 5 | HarmBench | Mazeika et al. | 2024 | ICML | https://arxiv.org/abs/2402.04249 | — |
| 6 | StrongREJECT | Bowen et al. | 2024 | ArXiv | https://arxiv.org/abs/2402.10260 | — |
| 7 | AgentHarm | UK AISI et al. | 2024 | ICLR 2025 | https://arxiv.org/abs/2410.09024 | — |
| 8 | Anthropic Responsible Scaling Policy v3.0 | Anthropic | 2025 | Blog | https://www.anthropic.com/news/responsible-scaling-policy-v3 | — |
| 9 | Making Safeguard Evaluations Actionable | UK AISI | 2025 | Blog + ArXiv | https://www.aisi.gov.uk/blog/making-safeguard-evaluations-actionable | 2505.18003 |
| 10 | METR Autonomy Evaluation | METR | 2025 | Web | https://metr.org/measuring-autonomous-ai-capabilities/ | — |
| 11 | Epoch AI: Do Biorisk Evaluations Measure Bioweapon Risk? | Epoch AI | 2025 | Blog | https://epoch.ai/gradient-updates/do-the-biorisk-evaluations-of-ai-labs-actually-measure-the-risk-of-developing-bioweapons | — |
| 12 | When AI Benchmarks Plateau | Multiple | 2025 | ArXiv | https://arxiv.org/abs/2602.16763 | — |
| 13 | Towards Evaluations-Based Safety Cases for AI Scheming | Apollo Research et al. | 2024 | ArXiv | https://arxiv.org/abs/2411.03336 | — |
| 14 | Evaluation Awareness | IAPS | 2025 | Policy brief | https://www.iaps.ai/research/evaluation-awareness-why-frontier-ai-models-are-getting-harder-to-test | — |
| 15 | BRACE Framework | UC Berkeley CLTC | 2024 | ArXiv | https://arxiv.org/abs/2405.10986 | — |
| 16 | AI Companies' Eval Reports Don't Support Claims | Stein-Perlman | 2025 | LessWrong | https://www.lesswrong.com/posts/AK6AihHGjirdoiJg6/ | — |
| 17 | How Evals Ended Up Helping AI Corporations | Alfour | 2026 | LessWrong | https://www.lesswrong.com/posts/Xxp6Tm8BKTkcb2m5M/ | — |
| 18 | Quantifying CBRN Risk in Frontier Models | Multiple | 2025 | ArXiv | https://arxiv.org/abs/2510.21133 | — |
| 19 | The Law of Evaluation | Ho, Martin, Tagal | 2025 | SSRN | https://doi.org/10.2139/ssrn.6271818 | 10.2139/ssrn.6271818 |
| 20 | Safety by Measurement: SLR | Multiple | 2025 | ArXiv | https://arxiv.org/abs/2505.05541 | — |
| 21 | AILuminate v1.0 (MLCommons) | Vidgen et al. | 2024 | ArXiv | https://arxiv.org/abs/2404.12241 | — |
| 22 | SafetyBench | Zhang et al. (Tsinghua) | 2023 | ACL 2024 | https://arxiv.org/abs/2309.07045 | — |
| 23 | MACHIAVELLI | Pan et al. | 2023 | ICML | https://aypan17.github.io/machiavelli/ | — |
| 24 | ForesightSafety Bench | Beijing AISI | 2025 | ArXiv | https://arxiv.org/abs/2602.14135 | — |
| 25 | SchemeBench | Unknown | 2025 | Web | https://www.schemebench.com/ | — |
| 26 | Inspect AI + Inspect Evals | UK AISI | 2024+ | GitHub | https://github.com/UKGovernmentBEIS/inspect_evals | — |
