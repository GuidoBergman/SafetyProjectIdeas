# Research Topic Report: AI Debate, Scalable Oversight & Deliberative Crowds

> Generated: 2026-04-10
> Requested by: coordinator
> Papers analyzed: 25
> Context: Scoping a 30-hour beginner project on "artificial deliberative crowds" — groups of LLMs that deliberate to evaluate safety of AI outputs

## Topic Definition

This report investigates empirical and theoretical work on AI debate, scalable oversight, multi-agent LLM deliberation, and wisdom-of-crowds effects in artificial agents. The focus is threefold: (1) what debate/deliberation methods have been tested and what works, (2) what datasets and benchmarks exist for testing deliberative evaluation, and (3) what gaps remain that a 30-hour project could fill. The topic sits at the intersection of scalable oversight (Irving et al., Christiano's iterated amplification), multi-agent LLM systems, and cognitive science research on collective intelligence.

## Dimensions Tracked

| Dimension | Description | Rationale |
|-----------|------------|-----------|
| Methodology | What debate/deliberation protocol is used, how agents interact | Reveals which protocols have been tested and which haven't |
| Empirical results | Key quantitative findings (accuracy gains, cost tradeoffs) | What's actually been demonstrated vs. theorized |
| Datasets & benchmarks | What evaluation tasks/datasets are used | Directly answers "what can we test on in 30 hours?" |
| Scale & compute | Model sizes, API costs, number of agent calls | Feasibility filter for a low-budget beginner project |
| Open questions | What authors flag as unresolved | Where the 30-hour project could contribute |
| Cross-domain benchmarks | Benchmarks from other fields usable for deliberative evaluation | Expands the pool of usable datasets |

---

## Paper Catalog

### 1. AI Safety via Debate (Irving, Christiano & Amodei, 2018)

- **Authors:** Geoffrey Irving, Paul Christiano, Dario Amodei
- **Source:** arXiv (NeurIPS 2018 workshop)
- **Year:** 2018
- **URL:** https://arxiv.org/abs/1805.00899

| Dimension | Finding |
|-----------|---------|
| Methodology | Two AI agents debate before a human judge. Theoretical proposal — no empirical validation. |
| Empirical results | None (theoretical). Toy MNIST experiment only. |
| Datasets & benchmarks | N/A |
| Scale & compute | N/A |
| Open questions | Whether debate works empirically. Whether honest strategies dominate. How to handle obfuscated arguments. |
| Cross-domain benchmarks | N/A |

**Relevance:** Foundational paper establishing debate as a scalable oversight mechanism. All empirical work in this area builds on or responds to this proposal.

---

### 2. On Scalable Oversight with Weak LLMs Judging Strong LLMs (Kenton et al., 2024)

- **Authors:** Kenton, Sibi, et al. (Google DeepMind)
- **Source:** NeurIPS 2024
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2407.04622

| Dimension | Finding |
|-----------|---------|
| Methodology | Two debaters (Alice/Bob) argue opposing answers over 3 simultaneous rounds; weaker judge selects winner. Also tests consultancy (single model argues one side). Inference-only (no training). |
| Empirical results | Debate outperforms consultancy on closed QA tasks. When consultant argues incorrectly, judge accuracy drops sharply vs. debate. Ablations (best-of-N, few-shot, CoT, turn count, answer order) show negligible effects. ~5M model calls total. |
| Datasets & benchmarks | 9 tasks, 128 questions each: QuALITY, BoolQ, GPQA-extractive, MMLU, GSM8KQA, PrOntoQA, TruthfulQA, GPQA, MMMU. |
| Scale & compute | Judges: Gemma-7B, GPT-3.5, Gemini Pro 1.0/1.5. Debaters: Gemini Pro 1.5 with best-of-4. ~5M calls. |
| Open questions | Inference-only setting doesn't test training dynamics. No human judges used. Whether Elo gains translate to judge accuracy is unclear. |
| Cross-domain benchmarks | MMLU, GSM8K, TruthfulQA, GPQA, BoolQ, MMMU are all standard and reusable. |

**Relevance:** Most important empirical result on debate for oversight. Tests 2-agent adversarial debate, NOT small-group deliberation — the gap this project could fill.

---

### 3. Improving Factuality and Reasoning in Language Models through Multiagent Debate (Du et al., 2023)

- **Authors:** Yilun Du, Shuang Li, Antonio Torralba, Joshua Tenenbaum, Igor Mordatch
- **Source:** ICML 2024
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2305.14325

| Dimension | Finding |
|-----------|---------|
| Methodology | 3 agents (copies of same LLM) independently answer, then debate over 2 rounds. Each sees all others' responses and updates its answer. Final answer from converged consensus. Also tested cross-model (ChatGPT + Bard). |
| Empirical results | Arithmetic: 67% → 82%. GSM8K: 77% → 85%. MMLU: 64% → 71%. Biographies factuality: 66% → 74%. Performance scales with more agents and rounds. |
| Datasets & benchmarks | Arithmetic, GSM8K, Chess move prediction, Biographies, MMLU, Chess move validity (BIG-Bench). |
| Scale & compute | ChatGPT (GPT-3.5) primarily; Bard for cross-model. 3 agents × 2 rounds = ~9 calls per question. |
| Open questions | Computationally expensive. Long debates exceed context windows. Convergence doesn't guarantee correctness — models confidently affirm wrong consensus. |
| Cross-domain benchmarks | GSM8K, MMLU, BIG-Bench are standard and reusable. |

**Relevance:** Closest to the "deliberative crowds" concept but uses identical model instances, not heterogeneous groups. The reveal-and-revise protocol is the simplest deliberation mechanism to implement.

---

### 4. Debate Helps Weak-to-Strong Generalization (Lang et al., 2025)

- **Authors:** Hunter Lang, David Sontag, Aravindan Vijayaraghavan
- **Source:** Semantic Scholar
- **Year:** 2025
- **URL:** Semantic Scholar ID f713b439266e6cc1415025da056f1304f2b78b8a

| Dimension | Finding |
|-----------|---------|
| Methodology | Two strong model instances (Qwen-14B) debate for 3 turns. Transcripts augment training data. Ensemble of 4 weak models (Qwen-7B) fine-tuned on ground truth labels, then strong model fine-tuned on weak labels. |
| Empirical results | PGR: SciQ 76.5% (vs. 41.2% baseline), BoolQ 69.2% (vs. 56.4%), CosmosQA 56.5% (vs. 17.4%), AnthropicHH 70.0% (vs. 35.0%). Debate outperforms consultancy (44.1%) and market-making (47.1%). Performance degrades beyond 3 turns. |
| Datasets & benchmarks | OpenAI weak-to-strong NLP: SciQ, BoolQ, CosmosQA, AnthropicHH. Up to 20k samples. |
| Scale & compute | Weak: Qwen-7B; Strong: Qwen-14B. Single 8×A100. Ensemble of 4 weak models. |
| Open questions | Only tested 7B–14B gap; needs larger scales (72B+). Only classification tasks. Long transcripts may exceed weak model context. |
| Cross-domain benchmarks | SciQ, BoolQ, CosmosQA are standard NLP benchmarks. |

**Relevance:** Directly connects debate to weak-to-strong generalization. Uses debate transcripts as training signal, not just inference-time deliberation — a different paradigm from the "deliberative crowds" proposal.

---

### 5. Efficient LLM Safety Evaluation through Multi-Agent Debate (2025)

- **Source:** arXiv
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2511.06396

| Dimension | Finding |
|-----------|---------|
| Methodology | Four-stage pipeline: (1) refusal screening, (2) topic scaffolding selecting 5 safety aspects, (3) critic-defender debate with early stopping, (4) judge consolidation. Three roles: Critic, Defender, Judge. Optimal at 3 rounds. |
| Empirical results | Qwen3-14B Multi-Agent Judge: Cohen's κ = 0.7331, only 0.026 below GPT-4o (0.759), at 46% of GPT-4o's cost. Fine-tuned judges (LlamaGuard3, ShieldGemma): κ = -0.006 to 0.351. Performance peaks at 3 rounds. |
| Datasets & benchmarks | HAJailBench: 11,100 human-annotated instances, 100 harmful behaviors, 12 attack methods, 11 target models. |
| Scale & compute | Qwen3-8B, Qwen3-14B. Cost: 4.13×10⁻⁴ per query (vs GPT-4o at 9.03×10⁻⁴). |
| Open questions | Anchored to 100 behaviors; distribution shift risk. Adversarial attacks on the debate process itself untested. |
| Cross-domain benchmarks | HAJailBench is new; availability uncertain. |

**Relevance:** Most directly relevant existing work — multi-agent debate for safety evaluation. Uses structured roles (critic/defender/judge), not "deliberative crowds." Key difference from the proposal: this is adversarial debate, not cooperative small-group deliberation.

---

### 6. Talk Isn't Always Cheap: Failure Modes in Multi-Agent Debate (Balepur et al., 2025)

- **Source:** arXiv
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2509.05396

| Dimension | Finding |
|-----------|---------|
| Methodology | Sequential iterative debate: agents independently answer, then revise seeing all peers for T=2 rounds. 3-agent groups, homogeneous and heterogeneous. Majority vote. |
| Empirical results | **Debate consistently degrades performance.** MMLU with 3× Mistral-7B: -9.2%. Mixed (GPT-4o-mini + 2× Mistral): -2.4%. Correct-to-incorrect flips exceed incorrect-to-correct. Anti-sycophancy prompts fail to help. |
| Datasets & benchmarks | CommonSenseQA, MMLU, GSM8K. 100 samples × 5 seeds per config. |
| Scale & compute | GPT-4o-mini, LLaMA-3.1-8B, Mistral-7B. Modest: 100 samples × 5 seeds. |
| Open questions | Why correctness-payoff prompting worsens some configs. How to design protocols prioritizing critical evaluation over consensus. Weaker models drag stronger ones down in heterogeneous groups. |
| Cross-domain benchmarks | CommonSenseQA, MMLU, GSM8K are standard. |

**Relevance:** Critical negative result. Shows that naive reveal-and-revise debate can *hurt* performance. The "deliberative crowds" project must address this — why would group deliberation help when debate hurts? The answer may lie in the protocol: this tests sequential revision, not structured deliberation with decomposition.

---

### 7. Can LLM Agents Really Debate? (Betz et al., 2025)

- **Source:** arXiv
- **Year:** 2025
- **URL:** https://arxiv.org/abs/2511.07784

| Dimension | Finding |
|-----------|---------|
| Methodology | Three-phase structured debate on Knight-Knave-Spy logic puzzles: (1) independent proposals with confidence, (2) player-by-player debate with self-adjustment, (3) majority voting. 1,800 puzzles, 6 controlled experiments. |
| Empirical results | **Debate improves accuracy substantially:** size-4 puzzles +52% (17% → 69%), size-6 +41%, size-8 +33%. Structural factors (team size, depth, confidence visibility) have negligible effect (p>0.05). Intrinsic model strength is the dominant predictor (R²=0.393). Strong models correct wrong majorities 30-34% of the time. ~$500 total. |
| Datasets & benchmarks | 1,800 Knight-Knave-Spy puzzles (custom). |
| Scale & compute | GPT variants, Gemini 2.5 Flash, Qwen, DeepSeek-R1. ~$500 total. |
| Open questions | Only structured logic — may not generalize. Model strength dominates structural design choices. Persuasion mechanisms unexplored. |
| Cross-domain benchmarks | Custom domain; not standard. |

**Relevance:** Important positive result showing debate *can* work, but on structured logic puzzles. Key insight: model strength matters more than deliberation protocol design. This suggests the "deliberative crowds" benefit may come from diversity of knowledge rather than the deliberation process itself.

---

### 8. When the Smarter AI Lies Better (Kraak, Lupi & Wilkes, 2026)

- **Source:** LessWrong (Apart Research / Redwood Research / AISI@GATECH)
- **Year:** 2026
- **URL:** https://www.lesswrong.com/posts/mDmsNJ9JxHEpBYDvd/

| Dimension | Finding |
|-----------|---------|
| Methodology | Adversarial AI Control: untrusted model (LLaMA3-405B) writes code with backdoors. Trusted model (LLaMA3-8B) argues code is malicious. They debate; separate 8B judge decides. Baseline: trusted monitoring without debate. |
| Empirical results | 24% of 300 samples produced runnable code (n=73 effective). Untrusted model frequently won despite inserting backdoors. Trusted monitoring without debate caught more bad code. Debate enabled better deception by the stronger model. |
| Datasets & benchmarks | APPS coding benchmark. 300 samples, 73 effective. |
| Scale & compute | LLaMA3-405B (untrusted), LLaMA3-8B (trusted + judge). Very small effective n. |
| Open questions | Very small sample. 405B vs. 8B gap may exaggerate deception advantage. Whether structured formats or better judges could mitigate "liar wins" effect. |
| Cross-domain benchmarks | APPS is standard for code generation. |

**Relevance:** Strongest negative result for the "deliberative crowds" proposal. When capability gaps are large, debate helps the stronger model deceive. However, this tests 2-agent adversarial debate — the proposal's hypothesis is that *groups* resist this better than individuals.

---

### 9. Inference-time Generative Debates (Elasky & Nakasako, 2025)

- **Source:** LessWrong
- **Year:** 2025
- **URL:** https://www.lesswrong.com/posts/kQCLPighFvb4ChHtu/

| Dimension | Finding |
|-----------|---------|
| Methodology | Seven formats (debate, consultancy, no-transcript, direct QA) across GPT-5-mini/nano, Qwen3-8B/4B. Generative (free-position) debate with two simultaneous speech rounds. |
| Empirical results | **Debate underperforms consultancy in 11/16 conditions.** Removing transcripts entirely (showing only answers) matches or beats debate. In "both-wrong" regimes, debate drops accuracy to 11% vs 30% baseline. |
| Datasets & benchmarks | BigCodeBench+ v0.1.0 (coding with PyTest verification), ARC-AGI (visual/logical reasoning). |
| Scale & compute | GPT-5-mini, GPT-5-nano, Qwen3-8B, Qwen3-4B. |
| Open questions | Whether RL-trained debaters would perform differently. The "both-wrong" problem as a fundamental limit. |
| Cross-domain benchmarks | BigCodeBench+, ARC-AGI. |

**Relevance:** Another negative result for debate. Key insight: the value of debate comes from answer provision, not argumentation. Judges endorse plausible-sounding wrong arguments. This suggests deliberative crowds should focus on *answer quality* (diverse independent answers + aggregation) rather than *argument quality* (persuasive reasoning).

---

### 10. NYU Code Debates Postmortem (2024)

- **Source:** LessWrong
- **Year:** 2024
- **URL:** https://www.lesswrong.com/posts/wsXCXoyvRi3DnWZ2M/

| Dimension | Finding |
|-----------|---------|
| Methodology | Non-coder human judges evaluated HumanEval/APPS coding questions with LLM debaters assigned correct/incorrect sides. Two pilots, 5 judges each. |
| Empirical results | Project abandoned. No sweet spot found: RLHF'd models can't argue dishonestly on easy questions; both sides err on hard questions. Stylistic differences between honest/dishonest debaters were detectable. |
| Datasets & benchmarks | HumanEval (Pilot 1), APPS interview-level (Pilot 2). |
| Scale & compute | GPT-4T, Claude 3 Opus as debaters. 10 debates + 10 consultancies per pilot. |
| Open questions | RLHF resistance to dishonest argumentation. Difficulty calibration. Whether non-coder judges are appropriate. |
| Cross-domain benchmarks | HumanEval, APPS. |

**Relevance:** Practical lesson: finding the right difficulty level where debate adds value is extremely hard. RLHF alignment interferes with adversarial debate setups. This supports using *cooperative* deliberation (the proposal's approach) over adversarial debate.

---

### 11. AI Debate Stability (Sorkin, 2024)

- **Source:** LessWrong (AI Safety Fundamentals project)
- **Year:** 2024
- **URL:** https://www.lesswrong.com/posts/AKGM5DaxiDevhTFou/

| Dimension | Finding |
|-----------|---------|
| Methodology | Replication of debate on MMLU abstract algebra. GPT-4 as debater, GPT-3.5 as judge. |
| Empirical results | GPT-3.5 judge often performs *worse* with debate transcripts than answering directly. Trivial prompt changes cause accuracy swings from 7/8 to 2/8. Self-defeating behavior is pervasive. |
| Datasets & benchmarks | MMLU abstract algebra subset. |
| Scale & compute | GPT-4, GPT-3.5. Small scale. |
| Open questions | Prompt sensitivity as a fundamental confounder. How to eliminate self-defeating behavior systematically. |
| Cross-domain benchmarks | MMLU. |

**Relevance:** Prompt sensitivity is a serious concern for any multi-agent system. Any deliberative crowds experiment must test robustness across prompt variants.

---

### 12. Wisdom of the Silicon Crowd (Schoenegger et al., 2024)

- **Authors:** Schoenegger et al.
- **Source:** Science Advances (2024) / arXiv
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2402.19379

| Dimension | Finding |
|-----------|---------|
| Methodology | 12 different LLMs each predict 31 binary forecasting questions. Predictions aggregated via median. Compared against 925 human forecasters. |
| Empirical results | Ensemble of 12 LLMs matches human crowd accuracy (statistically equivalent). Only 3/12 individual models beat the ensemble median. Models show acquiescence bias (systematically predict >50%). |
| Datasets & benchmarks | Proprietary forecasting tournament (31 binary questions). |
| Scale & compute | 12 diverse LLMs, 31 questions. Very low compute. |
| Open questions | Whether deliberation would improve over simple aggregation. Acquiescence bias mitigation. |
| Cross-domain benchmarks | Forecasting tournaments. |

**Relevance:** Shows simple aggregation across diverse models is surprisingly effective — no deliberation needed. The question for "deliberative crowds" is: does deliberation add anything beyond what you get from just averaging diverse independent judgments?

---

### 13. Wisdom of Partisan Crowds (Chuang et al., 2023)

- **Authors:** Chuang, Harlalka, Suresh, Goyal, Hawkins, Yang
- **Source:** arXiv (UW-Madison)
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2311.09665

| Dimension | Finding |
|-----------|---------|
| Methodology | LLM agents with detailed partisan personas deliberate over 3 rounds on estimation tasks (Becker et al. 2019). Compared against human data. |
| Empirical results | LLMs replicate human wisdom-of-crowds effects with detailed personas. Chain-of-thought reasoning *disrupts* the effect. Vague personas fail. Fine-tuning on human data improves fidelity. |
| Datasets & benchmarks | Becker et al. (2019) partisan estimation task (8 political fact-estimation questions). |
| Scale & compute | ChatGPT, Vicuna. Small scale. |
| Open questions | Whether the effect generalizes beyond estimation tasks. CoT disruption mechanism. |
| Cross-domain benchmarks | Political estimation tasks. |

**Relevance:** Directly relevant — tests wisdom-of-crowds with LLMs. Key warning: CoT can hurt group dynamics. Persona design matters enormously.

---

### 14. Large Language Models and the Wisdom of Small Crowds (Trott, 2024)

- **Authors:** Sean Trott
- **Source:** Open Mind (MIT Press)
- **Year:** 2024
- **URL:** https://direct.mit.edu/opmi/article/doi/10.1162/opmi_a_00144/121179/

| Dimension | Finding |
|-----------|---------|
| Methodology | Pre-registered experiments on 4 psycholinguistic datasets. Introduces "number needed to beat" (NNB) metric. Tests hybrid LLM-human aggregation. |
| Empirical results | GPT-4 can substitute for small human samples. NNB varies by task. Hybrid "centaur" methods combining LLM + human data outperform either alone. |
| Datasets & benchmarks | Four psycholinguistic datasets. |
| Scale & compute | GPT-4. Low compute. |
| Open questions | Optimal human/LLM ratio. Task dependency of NNB. |
| Cross-domain benchmarks | Psycholinguistic tasks. |

**Relevance:** Suggests human-LLM hybrid deliberation may be strongest approach. NNB metric could be adapted for deliberative crowds.

---

### 15. Scalable AI Safety via Doubly-Efficient Debate (Brown-Cohen et al., 2023)

- **Authors:** Brown-Cohen, Irving, Piliouras
- **Source:** ICML 2024 (oral)
- **Year:** 2023
- **URL:** https://arxiv.org/abs/2311.14125

| Dimension | Finding |
|-----------|---------|
| Methodology | Theoretical. Formalizes computational complexity of debate — honest prover wins in polynomial steps. |
| Empirical results | None (theoretical). |
| Datasets & benchmarks | N/A |
| Scale & compute | N/A |
| Open questions | Empirical validation. Whether polynomial-time honest strategies work in practice with LLMs. |
| Cross-domain benchmarks | N/A |

**Relevance:** Theoretical grounding for debate. The formal guarantees assume a specific debate structure that may not match small-group deliberation.

---

### 16. Prover-Verifier Games (Kirchner et al., 2024)

- **Authors:** Kirchner et al. (OpenAI)
- **Source:** arXiv
- **Year:** 2024
- **URL:** https://arxiv.org/abs/2407.13692

| Dimension | Finding |
|-----------|---------|
| Methodology | Trains "helpful" provers to produce correct verifiable solutions and "sneaky" provers to fool verifiers. |
| Empirical results | Legibility transfers to human evaluators. "Legibility tax": ~60% vs. 80% accuracy on math (accuracy drops when requiring verifiable reasoning). |
| Datasets & benchmarks | Math problems. |
| Scale & compute | Not specified in detail. |
| Open questions | The legibility tax — forcing legibility hurts performance. Whether groups of verifiers could reduce this tax. |
| Cross-domain benchmarks | Math benchmarks. |

**Relevance:** Complementary approach. A group of verifiers (deliberative crowd) might overcome the legibility tax that single verifiers face.

---

### 17. Improving Multi-Agent Debate with Sparse Communication Topology (2024)

- **Source:** EMNLP 2024 Findings
- **Year:** 2024
- **URL:** https://aclanthology.org/2024.findings-emnlp.427/

| Dimension | Finding |
|-----------|---------|
| Methodology | Tests different communication topologies in multi-agent debate (who sees whose responses). |
| Empirical results | Sparse topologies match or beat full communication while reducing compute. Not all agents need to see all other agents. |
| Datasets & benchmarks | Not specified in search results. |
| Scale & compute | Reduced compute vs. full communication. |
| Open questions | Optimal topology design. Whether topology matters more for some tasks. |
| Cross-domain benchmarks | N/A |

**Relevance:** Practical design insight — deliberative crowds don't need full connectivity. Small groups communicating internally, then aggregating group consensuses (the Navajas design) may be optimal.

---

### 18. Habermas Machine (Tessler et al., 2024)

- **Authors:** Tessler et al. (Google DeepMind)
- **Source:** Science
- **Year:** 2024
- **URL:** https://www.science.org/doi/10.1126/science.adq2852

| Dimension | Finding |
|-----------|---------|
| Methodology | LLM mediator synthesizes group statements on divisive issues. Over 5,000 human participants. |
| Empirical results | AI mediator statements preferred over human-written ones. Helps groups find common ground on divisive topics. |
| Datasets & benchmarks | Custom deliberation dataset (5,000+ participants). |
| Scale & compute | Not specified. |
| Open questions | Whether mediator role could be applied to safety evaluation (mediating between LLM judges). |
| Cross-domain benchmarks | N/A |

**Relevance:** Shows LLMs can facilitate group consensus — potentially useful as a "moderator" role in deliberative crowds.

---

### 19. AEGIS: Ensemble of LLM Experts for Safety Moderation (2024)

- **Source:** Semantic Scholar
- **Year:** 2024

| Dimension | Finding |
|-----------|---------|
| Methodology | Ensemble of specialized LLM experts for adaptive safety content moderation. |
| Empirical results | Ensemble outperforms single models on content moderation. |
| Datasets & benchmarks | Safety moderation datasets. |
| Scale & compute | Multiple specialized models. |
| Open questions | Optimal ensemble composition. When to use ensemble vs. single strong model. |
| Cross-domain benchmarks | Safety moderation benchmarks. |

**Relevance:** Shows ensemble approaches work for safety evaluation. The "deliberative crowds" approach adds deliberation on top of ensembling.

---

### 20. Collective AI Can Amplify Tiny Perturbations (2026)

- **Source:** arXiv
- **Year:** 2026
- **URL:** https://arxiv.org/html/2603.09127

| Dimension | Finding |
|-----------|---------|
| Methodology | Studies stability of multi-agent AI deliberation. |
| Empirical results | Small perturbations can cascade into divergent outcomes in multi-agent deliberation. |
| Datasets & benchmarks | Not specified. |
| Scale & compute | Not specified. |
| Open questions | How to ensure stable convergence. Whether group size affects stability. |
| Cross-domain benchmarks | N/A |

**Relevance:** Important warning — deliberative systems may be unstable. Project should test convergence stability across runs.

---

### 21. Knowledge Divergence and the Value of Debate (2026)

- **Source:** arXiv
- **Year:** 2026
- **URL:** https://arxiv.org/abs/2603.05293

| Dimension | Finding |
|-----------|---------|
| Methodology | Formal analysis of when debate is most valuable, based on knowledge divergence between agents and judges. First formal connection between debate and RLAIF. |
| Empirical results | Debate most valuable when agents have divergent knowledge from judges. Provides geometric foundation for adversarial vs. non-adversarial oversight. |
| Datasets & benchmarks | Theoretical. |
| Scale & compute | Theoretical. |
| Open questions | Empirical validation. Implications for RLAIF design. |
| Cross-domain benchmarks | N/A |

**Relevance:** Directly connects debate to RLAIF — the proposal's original framing. Suggests debate is most useful when knowledge asymmetry is high, which supports using deliberation for complex safety evaluation where no single agent has complete knowledge.

---

### 22. FREE-MAD: Consensus-Free Multi-Agent Debate (2025)

- **Source:** arXiv
- **Year:** 2025
- **URL:** https://arxiv.org/pdf/2509.11035

| Dimension | Finding |
|-----------|---------|
| Methodology | Debate without requiring consensus. |
| Empirical results | Addresses problems with forced agreement in standard debate setups. |
| Open questions | When to force consensus vs. allow dissent. |

**Relevance:** Suggests that forcing consensus may be harmful — relevant to protocol design for deliberative crowds.

---

### 23. InterLab: Toolkit for Multi-Agent Experiments (GoodAI, 2024)

- **Source:** Alignment Forum
- **Year:** 2024
- **URL:** https://www.alignmentforum.org/posts/rgEoRetRD6PvvJeRT/

| Dimension | Finding |
|-----------|---------|
| Methodology | Modular Python framework for multi-agent LLM interactions. Actors, environments, memory, game-theoretic models. |
| Empirical results | N/A (toolkit). |
| Datasets & benchmarks | N/A |
| Scale & compute | Google Colab compatible. |
| Open questions | N/A (toolkit). |
| Cross-domain benchmarks | N/A |

**Relevance:** Candidate infrastructure for implementing deliberative crowd experiments. Could reduce engineering overhead, but adds a learning curve.

---

### 24. Survey of Multi-Agent LLM Evaluations (Jurkovic et al., 2025)

- **Source:** LessWrong
- **Year:** 2025

| Dimension | Finding |
|-----------|---------|
| Methodology | Meta-analysis of 32 multi-agent evaluation papers. |
| Empirical results | 26/32 papers measured miscoordination; only 5/32 measured collusion. Most common threat models lack multi-agent evaluations. |
| Open questions | Collusion between agents is understudied. Realistic threat models for multi-agent systems. |

**Relevance:** Identifies a major gap — collusion in multi-agent evaluation systems. Deliberative crowds should be tested for collusion risk.

---

### 25. SocraSynth: Adversarial Multi-LLM Reasoning (2025)

- **Source:** ACM
- **Year:** 2025
- **DOI:** 10.1145/3749421.3749430

| Dimension | Finding |
|-----------|---------|
| Methodology | Adversarial multi-LLM reasoning framework with statistical aggregation methods. |
| Empirical results | Improved reasoning through adversarial multi-LLM interaction with conditional statistics. |
| Open questions | Optimal aggregation methods. Whether adversarial framing hurts cooperative tasks. |

**Relevance:** Provides a statistical framework for aggregating multi-LLM deliberative outputs.

---

## Dimension Synthesis

### 1. Methodology — Debate Protocols Tested

**Pattern:** Three distinct protocol families have been tested:

1. **Adversarial 2-agent debate** (Irving → Kenton): Two agents argue opposing sides before a judge. Most studied. Mixed empirical results — works for information-asymmetry tasks (Kenton), fails with large capability gaps (Kraak).

2. **Sequential reveal-and-revise** (Du et al. → Balepur): Agents independently answer, see others' answers, revise. Simplest to implement. Positive results on factuality/math (Du), but negative results on MMLU/CommonSenseQA (Balepur). The protocol seems to *amplify* errors when initial answers are wrong.

3. **Structured multi-role debate** (Multi-Agent Judge, SocraSynth): Assigned roles (critic, defender, judge) with bounded rounds and early stopping. Most promising recent approach. The role structure prevents the conformity problem that plagues #2.

**Gap:** No work tests the Navajas-style protocol — small groups deliberate cooperatively to reach internal consensus, then group consensuses are aggregated. This is fundamentally different from all three tested families. It's cooperative (not adversarial), group-based (not pairwise), and aggregates *group consensuses* (not individual revised answers).

### 2. Empirical Results — What Actually Works

**Pattern:** The empirical evidence for debate is decidedly mixed:

**Positive results:**
- Debate outperforms consultancy on extractive QA with information asymmetry (Kenton, NeurIPS 2024)
- Multi-agent debate improves factuality by 5-15% on math and reasoning (Du, ICML 2024)
- Structured debate substantially improves logic puzzle accuracy (+32-52%) (Betz, 2025)
- Multi-agent judge matches GPT-4o at 46% cost for safety evaluation (Multi-Agent Judge, 2025)
- Debate transcripts improve weak-to-strong generalization by 15-35 PGR points (Lang, 2025)

**Negative results:**
- Debate underperforms consultancy in 11/16 conditions on coding/reasoning (Elasky, 2025)
- Debate consistently degrades performance on MMLU by -9% (Balepur, 2025)
- Stronger model wins debates *despite inserting backdoors* in code (Kraak, 2026)
- Debate transcripts sometimes harm judge accuracy vs. direct answering (Sorkin, 2024)
- Removing transcripts entirely matches debate performance (Elasky, 2025)

**Key takeaway:** Debate works when (a) the task has verifiable structure (logic, math, extractive QA), (b) the capability gap is moderate, and (c) the protocol prevents conformity cascades. It fails when models are persuasive but wrong, or when all participants share the same blind spots.

### 3. Datasets & Benchmarks — What's Available

**Pattern:** The most-used benchmarks across debate/oversight papers are:

| Benchmark | Papers using it | Format | Why popular |
|-----------|----------------|--------|-------------|
| MMLU | Kenton, Du, Balepur, Sorkin | MC | Standard, multi-domain |
| GSM8K | Kenton, Du, Balepur | MC/free | Verifiable math |
| TruthfulQA | Kenton | MC/free | Tests deception resistance |
| GPQA | Kenton | MC | Expert-level difficulty |
| BoolQ | Kenton, Lang | Binary | Simple yes/no |
| APPS/HumanEval | Kraak, NYU | Code | Code with tests |

**Best candidates for a 30-hour project (from benchmark deep-reads):**

| Benchmark | Size | Format | Weak model accuracy | Why ideal |
|-----------|------|--------|--------------------|----|
| **LLMBar** | 419 | Pairwise | Below random on adversarial (32-43%) | Adversarial items designed to fool weak judges; perfect for testing if deliberation overcomes deception |
| **JudgeBench** | 620 | Pairwise | GPT-4o ~50% (random) | Even strong models struggle; enormous room for deliberation gains |
| **RewardBench** | 2,985 | Pairwise (trios) | 55-71% for small models | Safety subset directly relevant; Chat Hard subset is challenging |
| **WildGuard** | 5,299 | Binary classification | 54-71% F1 for weak models | Three simultaneous tasks; 13 harm categories; high safety relevance |
| **GSM8K** | 8,500 | Numerical answer | Varies by model | Decomposable steps; ground truth is unambiguous |

**Not recommended:** GPQA Diamond (too hard — models fail from lack of knowledge, not reasoning), CyberSecEval (wrong format — tests model capabilities, not evaluation ability), HAJailBench (uncertain availability).

### 4. Scale & Compute — Feasibility

**Pattern:** Most debate experiments are surprisingly cheap:

- Betz (2025): ~$500 total for 745 observations across multiple models
- Balepur (2025): 100 samples × 5 seeds per config — modest
- Du (2023): 3 agents × 2 rounds = ~9 calls per question
- Multi-Agent Judge (2025): 4.13×10⁻⁴ per query

**For a 30-hour project:** Using API models (GPT-4o-mini at ~$0.15/1M input, ~$0.60/1M output; Haiku at similar), running 3-agent deliberation over 200-400 items would cost roughly $5-50 depending on prompt length and rounds. Well within a student budget.

**Key constraint:** The 30 hours is the bottleneck, not compute. Implementation time dominates.

### 5. Open Questions — Where the Project Could Contribute

**Most frequently cited open questions across the literature:**

1. **Does cooperative small-group deliberation outperform adversarial 2-agent debate?** (No paper tests this)
2. **Does model heterogeneity improve deliberation quality?** (ChatEval hints yes; Balepur hints no — contradictory)
3. **When does deliberation help vs. hurt?** (No unified theory; task-dependent)
4. **Does structured decomposition improve deliberation?** (Suggested by Navajas follow-up; untested with LLMs)
5. **How to prevent conformity cascades in multi-agent deliberation?** (Balepur identifies the problem; no solution)
6. **Can deliberating groups resist adversarial agents?** (Kraak tests 2-agent; groups untested)
7. **Does the Navajas "deliberating groups > crowds" finding transfer to LLMs?** (Nobody has tested this directly)

**The most feasible for 30 hours:** Question 7 (direct Navajas transfer) or question 1 (cooperative deliberation vs. adversarial debate), using an existing benchmark with ground truth.

### 6. Cross-Domain Benchmarks

**Pattern:** The most promising cross-domain benchmarks for deliberative evaluation share these traits:
- Pairwise comparison format (simple for LLM judges)
- Ground truth based on objective correctness (not human preference)
- Difficulty in the "sweet spot" where weak models partially succeed
- Multiple evaluation dimensions or categories

**Top picks by domain:**

**Safety evaluation:** WildGuard (three tasks, 13 categories, human-annotated), HarmBench (510 behaviors, 7 harm domains)

**Judge/evaluation quality:** JudgeBench (objective ground truth, 4 domains), LLMBar (adversarial deception, MIT license), RewardBench (4 categories including safety)

**Reasoning:** GSM8K (decomposable math), BIG-Bench Hard (23 diverse reasoning tasks), MATH (5 difficulty levels)

**Factuality:** TruthfulQA (tests misconceptions), FActScore (atomic fact verification — ideal for decomposition)

**Code safety:** SVEN (1,600 labeled functions, 9 CWEs), CASTLE (250 micro-benchmarks, 25 CWEs)

---

## Coverage Gap Analysis

### Under-Researched Areas

1. **Cooperative small-group deliberation** — All debate papers test adversarial 2-agent setups or sequential revision. Nobody tests the Navajas-style protocol: small groups deliberate cooperatively → aggregate group consensuses. This is the core gap the "deliberative crowds" project would fill.

2. **Model heterogeneity in deliberation** — Du et al. briefly tested ChatGPT + Bard but didn't systematically vary composition. Balepur tested heterogeneous groups but only with sequential revision (which hurt). Whether heterogeneity helps *with a different protocol* is unknown.

3. **Deliberation for code safety evaluation** — Code safety benchmarks exist (SVEN, CASTLE, CyberSecEval) but nobody has tested deliberative evaluation on them. Kraak used APPS but with adversarial debate, not cooperative deliberation.

4. **Decomposition in deliberation** — The iterated amplification connection is purely theoretical. No paper tests whether prompting deliberating groups to decompose problems improves their judgments.

### Methodological Gaps

1. **No controlled comparison of deliberation protocols** — Different papers use different protocols on different tasks, making it impossible to compare. A controlled study varying the protocol while fixing the task and models would be highly valuable.

2. **No cost-controlled comparisons** — Most papers compare debate to non-debate without controlling for total inference cost. A deliberating group of 3 models × 3 rounds = 9 calls; a single model with 9× the sampling budget might do as well.

3. **Convergence stability** — Only one paper (2026) flags that multi-agent deliberation can be unstable. Replication studies should measure cross-run variance.

### Contradictions and Open Debates

1. **Does debate help or hurt?** Du et al. (2024) and Betz (2025) show substantial gains. Balepur (2025) and Elasky (2025) show substantial losses. The difference appears to be protocol design (structured debate helps; sequential revision hurts) and task type (verifiable tasks benefit; subjective tasks don't).

2. **Does model diversity help?** ChatEval (2023) shows role diversity improves evaluation. Balepur (2025) shows heterogeneous groups perform worse with sequential revision. These may not contradict — the protocol matters.

3. **Is argumentation or aggregation the active ingredient?** Elasky (2025) shows removing debate transcripts matches debate performance, suggesting aggregation does the work. But Betz (2025) shows debate adds +52% on logic puzzles, far beyond what aggregation alone could explain. Resolution: task-dependent — argumentation helps on structured reasoning but hurts on open-ended judgment.

---

## Research Frontier

**Most promising open directions for a 30-hour project:**

1. **Navajas transfer test** — Compare aggregation of individual LLM judgments vs. aggregation of small-group deliberation consensuses, matching the Navajas et al. design. Use LLMBar or JudgeBench. This fills the most clearly identified gap and connects to a Nature Human Behaviour paper.

2. **Protocol comparison study** — On a single benchmark (e.g., LLMBar adversarial), compare: (a) independent aggregation, (b) sequential reveal-and-revise (Du et al.), (c) structured cooperative deliberation, (d) adversarial debate (Kenton). Same models, same questions, different protocols. This would clarify the contradictory findings in the literature.

3. **Decomposition in deliberation** — Compare groups that deliberate holistically vs. groups prompted to decompose problems first, on a benchmark with complex items (FActScore or GSM8K). Connects to iterated amplification and the participant's supervisor's research.

**Suggested follow-up questions:**
1. Does the Navajas "deliberating groups > crowds" effect hold when agents share the same training data (unlike humans who have genuinely diverse knowledge)?
2. Is there a minimum capability threshold below which deliberation can't help, regardless of protocol?
3. Can a "moderator" agent (à la Habermas Machine) prevent the conformity cascades identified by Balepur?

---

## Full Source List

| # | Title | Authors | Year | Source | URL |
|---|-------|---------|------|--------|-----|
| 1 | AI Safety via Debate | Irving, Christiano, Amodei | 2018 | arXiv | https://arxiv.org/abs/1805.00899 |
| 2 | On Scalable Oversight with Weak LLMs Judging Strong LLMs | Kenton et al. | 2024 | NeurIPS | https://arxiv.org/abs/2407.04622 |
| 3 | Improving Factuality and Reasoning through Multiagent Debate | Du et al. | 2023 | ICML 2024 | https://arxiv.org/abs/2305.14325 |
| 4 | Debate Helps Weak-to-Strong Generalization | Lang et al. | 2025 | S2 | S2:f713b439 |
| 5 | Efficient LLM Safety Evaluation through Multi-Agent Debate | — | 2025 | arXiv | https://arxiv.org/abs/2511.06396 |
| 6 | Talk Isn't Always Cheap | Balepur et al. | 2025 | arXiv | https://arxiv.org/abs/2509.05396 |
| 7 | Can LLM Agents Really Debate? | Betz et al. | 2025 | arXiv | https://arxiv.org/abs/2511.07784 |
| 8 | When the Smarter AI Lies Better | Kraak, Lupi, Wilkes | 2026 | LessWrong | LW:mDmsNJ9JxHEpBYDvd |
| 9 | Inference-time Generative Debates | Elasky, Nakasako | 2025 | LessWrong | LW:kQCLPighFvb4ChHtu |
| 10 | NYU Code Debates Postmortem | NYU group | 2024 | LessWrong | LW:wsXCXoyvRi3DnWZ2M |
| 11 | AI Debate Stability | Sorkin | 2024 | LessWrong | LW:AKGM5DaxiDevhTFou |
| 12 | Wisdom of the Silicon Crowd | Schoenegger et al. | 2024 | Science Advances | https://arxiv.org/abs/2402.19379 |
| 13 | Wisdom of Partisan Crowds | Chuang et al. | 2023 | arXiv | https://arxiv.org/abs/2311.09665 |
| 14 | LLMs and the Wisdom of Small Crowds | Trott | 2024 | MIT Press | doi:10.1162/opmi_a_00144 |
| 15 | Scalable AI Safety via Doubly-Efficient Debate | Brown-Cohen et al. | 2023 | ICML 2024 | https://arxiv.org/abs/2311.14125 |
| 16 | Prover-Verifier Games | Kirchner et al. | 2024 | arXiv | https://arxiv.org/abs/2407.13692 |
| 17 | Sparse Communication Topology in Multi-Agent Debate | — | 2024 | EMNLP | https://aclanthology.org/2024.findings-emnlp.427/ |
| 18 | Habermas Machine | Tessler et al. | 2024 | Science | doi:10.1126/science.adq2852 |
| 19 | AEGIS: Ensemble of LLM Experts | — | 2024 | S2 | S2:b705e3cc |
| 20 | Collective AI Can Amplify Perturbations | — | 2026 | arXiv | https://arxiv.org/html/2603.09127 |
| 21 | Knowledge Divergence and Value of Debate | — | 2026 | arXiv | https://arxiv.org/abs/2603.05293 |
| 22 | FREE-MAD: Consensus-Free Debate | — | 2025 | arXiv | https://arxiv.org/pdf/2509.11035 |
| 23 | InterLab Toolkit | GoodAI | 2024 | Alignment Forum | AF:rgEoRetRD6PvvJeRT |
| 24 | Survey of Multi-Agent LLM Evaluations | Jurkovic et al. | 2025 | LessWrong | LW:tGcLA596E8g3KnphE |
| 25 | SocraSynth | — | 2025 | ACM | doi:10.1145/3749421.3749430 |

### Benchmarks Referenced

| # | Benchmark | Domain | Size | URL |
|---|-----------|--------|------|-----|
| B1 | LLMBar | Instruction eval | 419 | https://github.com/princeton-nlp/LLMBar |
| B2 | JudgeBench | LLM judgment | 620 | https://github.com/ScalerLab/JudgeBench |
| B3 | RewardBench | Preference | 2,985 | https://github.com/allenai/reward-bench |
| B4 | WildGuard | Safety moderation | 5,299 | https://huggingface.co/datasets/allenai/wildguardmix |
| B5 | TruthfulQA | Factuality | 817 | https://github.com/sylinrl/TruthfulQA |
| B6 | GSM8K | Math reasoning | 8,500 | https://huggingface.co/datasets/openai/gsm8k |
| B7 | MATH | Competition math | 12,500 | https://huggingface.co/datasets/hendrycks/competition_math |
| B8 | BIG-Bench Hard | Diverse reasoning | 6,511 | https://github.com/suzgunmirac/BIG-Bench-Hard |
| B9 | HarmBench | Safety/red team | 510 | https://github.com/centerforaisafety/HarmBench |
| B10 | SVEN | Code security | 1,600 | https://github.com/eth-sri/sven |
| B11 | CASTLE | Code security | 250 | https://github.com/CASTLE-Benchmark |
| B12 | GPQA Diamond | Expert QA | 198 | https://huggingface.co/datasets/Idavidrein/gpqa |
| B13 | FActScore | Factual precision | Variable | https://github.com/shmsw25/FActScore |
| B14 | SafetyBench | Safety MC | 11,435 | https://github.com/thu-coai/SafetyBench |
| B15 | ToxicChat | Content mod | 10,000 | https://huggingface.co/datasets/lmsys/toxic-chat |
| B16 | MT-Bench | Multi-turn | 80 | https://github.com/lm-sys/FastChat |
| B17 | Chatbot Arena | Preference | 33K+ | https://huggingface.co/datasets/lmsys/chatbot_arena_conversations |
| B18 | CyberSecEval | Code security | Varies | https://github.com/meta-llama/PurpleLlama |
| B19 | BackdoorLLM | Backdoor attacks | 200+ exps | https://github.com/bboylyg/BackdoorLLM |
| B20 | SWE-bench Verified | Software eng | 500 | https://www.swebench.com/ |
| B21 | HAJailBench | Jailbreak eval | 11,100 | (from paper #5) |
