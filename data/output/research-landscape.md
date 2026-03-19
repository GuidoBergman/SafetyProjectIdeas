# AI Safety Research Landscape

> Generated: 2026-03-19
> Sources: 11 parallel research agents covering open problems lists, research agendas, key organizations, breakthrough papers, system cards, Alignment Forum discussions, funding priorities, government priorities, benchmarks & tools, failure modes & incidents, and curated project idea lists. Web searches performed across 80+ queries with targeted page fetches.

## Metadata

- **Total subfields:** 12
- **Total open problems identified:** 95+
- **Source priority:** Open problems lists > Research agendas > Survey papers > System cards > Incident databases > Claude knowledge

---

## Quick Reference

**Top 5 most actionable sources** (the ones to read first for idea generation):
1. [Anthropic: Recommendations for Technical AI Safety Research Directions](https://alignment.anthropic.com/2025/recommended-directions/) — 17 concrete, well-scoped open problems directly applicable to current systems
2. [Open Phil / Coefficient Giving: Technical AI Safety RFP](https://coefficientgiving.org/request-for-proposals-technical-ai-safety-research) — 21 research areas with explicit priority tiers and $40M funding; reveals community consensus on neglected areas
3. [100+ Concrete Projects and Open Problems in Evals](https://www.alignmentforum.org/posts/LhnqegFoykcjaXCYH/100-concrete-projects-and-open-problems-in-evals) — Collaborative compilation from 20+ experts at Apollo, METR, Redwood, RAND, AISIs
4. [200 Concrete Open Problems in Mechanistic Interpretability](https://www.alignmentforum.org/posts/LbrPTJ4fmABEdEnLf/200-concrete-open-problems-in-mechanistic-interpretability) — Extensive brainstorm organized by category with room for significant progress
5. [Shallow Review of Technical AI Safety, 2025](https://shallowreview.ai/) — Meta-review of 800+ papers across 80+ research agendas; best landscape overview

**Top 5 most promising subfields for idea generation:**
1. **Mechanistic Interpretability** — Large open problem space (200+), excellent tooling (TransformerLens, SAELens), strong funding signal, accessible entry points for beginners
2. **AI Control & Monitoring** — Highest priority in Open Phil's starred areas, active tooling development (Bloom, Petri), directly applicable to current systems
3. **Evaluations & Benchmarks** — 100+ concrete open problems, strong infrastructure (Inspect AI), clear gaps in agentic and multimodal evals
4. **Deception & Scheming** — Hot topic across multiple funders, novel breakthrough results (emergent misalignment), clear experimental paradigms
5. **Honesty & CoT Faithfulness** — Breakthrough paper (shallow alignment), practical relevance, relatively under-explored compared to interpretability

---

## Subfields

### adversarial_robustness: Adversarial Robustness & Red-Teaming

**Description:** Research on making AI systems robust to adversarial inputs, jailbreaks, and prompt injection attacks, as well as developing and improving red-teaming methodologies for identifying vulnerabilities.

**Status:** active

**Open Problems:**
- [ ] Develop realistic jailbreak benchmarks that reflect actual attacker capabilities rather than synthetic test cases <!-- source: Anthropic recommended directions -->
- [ ] Design adaptive defenses that maintain robustness against evolving attack strategies without catastrophic over-refusal <!-- source: Anthropic recommended directions -->
- [ ] Develop alternatives to adversarial training (e.g., latent adversarial training) that provide robustness without requiring explicit attack enumeration <!-- source: Open Phil RFP (starred) -->
- [ ] Understand why safety alignment is shallow (concentrated in first few tokens) and develop methods to deepen it throughout the generative distribution <!-- source: ICLR 2025 Outstanding Paper - Qi et al. -->
- [ ] Create cost-effective jailbreak detection via activation probes that scale better than LLM-based classifiers <!-- source: LessWrong AI Safety Frontier Jan 2026 -->
- [ ] Bridge the gap between lab-tested adversarial defenses and real-world deployment robustness <!-- source: International AI Safety Report 2026 -->

**Key Organizations:** Anthropic, OpenAI, Google DeepMind, CAIS, Redwood Research, UK AISI

**Key Authors:** Xiangyu Qi, Prateek Mittal, Peter Henderson, Florian Tramèr, Nicholas Carlini, Andy Zou, Zico Kolter

**Source Documents:**
- [Safety Alignment Should Be Made More Than Just a Few Tokens Deep](https://arxiv.org/abs/2406.05946) - survey (ICLR 2025 Outstanding Paper)
- [Anthropic Recommended Directions](https://alignment.anthropic.com/2025/recommended-directions/) - open-problems-list
- [Open Phil Technical AI Safety RFP](https://coefficientgiving.org/request-for-proposals-technical-ai-safety-research) - research-agenda

**Source Code Availability:** AISafetyLab (Tsinghua) provides a unified attack/defense/eval toolkit. StrongReject benchmark from OpenAI is publicly available.

**Key Datasets & Benchmarks:** AILuminate (MLCommons, 24K+ prompts, 12 hazard categories), HELM Safety (Stanford CRFM), StrongReject, TrustLLM (6 dimensions)

**Common Methodologies:** Red-teaming (manual and automated), adversarial suffix attacks, prefilling attacks, GCG optimization, latent adversarial training, activation probing for jailbreak detection

**Recent Surprising Results:**
- Safety alignment concentrated in first few tokens, enabling trivial bypass — from Qi et al. ICLR 2025 <!-- suggests follow-up: test whether reasoning models exhibit same shallow alignment pattern -->
- Activation-based jailbreak detection achieves production-ready robustness at orders-of-magnitude lower cost than LLM classifiers — from LessWrong Jan 2026 digest <!-- suggests follow-up: replicate on different model families -->

**Generation Strategy Hints:**
- Best generation strategies for this subfield: experiment variation, follow-up experiment
- Specific papers whose experiments could be varied (FR67): Qi et al. shallow alignment (vary model families, multimodal), activation-based jailbreak detection (vary architectures)
- Specific surprising results that need follow-up (FR68): shallow alignment finding, activation probe cost-effectiveness

**Priority for idea generation:** high
**Rationale:** Strong breakthrough results with clear follow-up experiments, accessible tooling, directly relevant to current deployment safety

---

### mechanistic_interpretability: Mechanistic Interpretability

**Description:** Understanding the internal mechanisms of neural networks — how features are represented, how information flows through circuits, and how to extract interpretable explanations of model behavior. Includes sparse autoencoders, attribution graphs, probing, and circuit discovery.

**Status:** active

**Open Problems:**
- [ ] Scale attribution graphs / circuit tracing from small models (Claude 3.5 Haiku) to frontier-sized models <!-- source: Anthropic Circuit Tracing paper -->
- [ ] Find feature representations beyond sparse autoencoders — what alternatives exist and when do they outperform SAEs? <!-- source: Open Phil RFP (standard priority) -->
- [ ] Develop interpretability benchmarks that measure whether mechanistic findings translate to actionable safety guarantees <!-- source: Open Phil RFP (standard priority) -->
- [ ] Build toy models that capture alignment-relevant phenomena for controlled interpretability experiments <!-- source: Open Phil RFP (starred) -->
- [ ] Understand superposition — how features are packed into fewer dimensions and how to reliably decompose them <!-- source: 200 Concrete Open Problems in Mech Interp -->
- [ ] Bridge the interpretability-to-safety gap — translate mechanistic findings into actionable deployment decisions <!-- source: Benchmarks agent gap analysis -->
- [ ] Extend mechanistic interpretability methods to vision and multimodal transformers <!-- source: Prisma/ViT-Prisma project -->
- [ ] Understand how training dynamics shape what features models learn to represent <!-- source: UK AISI Alignment Project -->
- [ ] Extract and synthesize standalone world models from neural networks <!-- source: Alignment Forum research agenda -->

**Key Organizations:** Anthropic, Google DeepMind, EleutherAI, ARC, UK AISI, Apollo Research

**Key Authors:** Chris Olah, Neel Nanda, Tom Lieberum, Arthur Conmy, Wes Gurnee, Adly Templeton, Jack Lindsey, Trenton Bricken, Sam Marks, Max Tegmark

**Source Documents:**
- [Circuit Tracing: Revealing Computational Graphs in Language Models](https://transformer-circuits.pub/2025/attribution-graphs/methods.html) - report
- [200 Concrete Open Problems in Mechanistic Interpretability](https://www.alignmentforum.org/posts/LbrPTJ4fmABEdEnLf/200-concrete-open-problems-in-mechanistic-interpretability) - open-problems-list
- [On the Biology of a Large Language Model](https://transformer-circuits.pub/2025/attribution-graphs/biology.html) - report

**Source Code Availability:** TransformerLens (50+ models, MIT license, 3.2k stars), SAELens (SAE training/analysis), Prisma/ViT-Prisma (75+ vision transformers, 80+ pre-trained SAE weights), Interpreto (integrates NNsight + SAELens + Delphi)

**Key Datasets & Benchmarks:** No widely adopted interpretability benchmarks exist (this is an identified gap). OpenAI's neuron2graph and Anthropic's feature dashboards provide visualization but not standardized evaluation.

**Common Methodologies:** Activation patching, circuit discovery, sparse autoencoders (SAEs), attribution graphs, cross-layer transcoders, probing classifiers, logit lens, causal tracing

**Recent Surprising Results:**
- Attribution graphs reveal that Claude 3.5 Haiku plans ahead (identifies rhyming words before writing poetry lines) — from Anthropic Circuit Tracing <!-- suggests follow-up: test planning behavior in larger models, study whether planning correlates with capability -->
- Vision SAEs show different sparsity patterns than language SAEs — from ViT-Prisma <!-- suggests follow-up: characterize the structural differences and their implications -->

**Generation Strategy Hints:**
- Best generation strategies for this subfield: experiment variation, novel direction
- Specific papers whose experiments could be varied (FR67): Circuit Tracing (apply to different model families), SAE analysis (compare architectures)
- Specific surprising results that need follow-up (FR68): planning-ahead behavior, vision vs. language SAE differences

**Priority for idea generation:** high
**Rationale:** Largest open problem space (200+ concrete problems), excellent open-source tooling making it highly accessible, strong funding signal (Open Phil starred), and directly relevant to the participant profile (interpretability probing is feasible in 30 hours with existing tools)

---

### alignment_training: Alignment & Training Methods

**Description:** Methods for training AI systems to be aligned with human values and intentions, including RLHF, DPO, constitutional AI, and related approaches. Focuses on the training-time interventions that shape model behavior.

**Status:** active

**Open Problems:**
- [ ] Understand and mitigate reward model misspecification in RLHF — when do reward models diverge from true human preferences? <!-- source: Open Problems in RLHF (Alignment Forum) -->
- [ ] Address distributional shift in human feedback — RLHF training data doesn't cover deployment distribution <!-- source: Open Problems in RLHF -->
- [ ] Develop robust unlearning methods that remove dangerous knowledge without broader capability degradation <!-- source: Open Phil RFP (standard priority) -->
- [ ] Understand emergent misalignment — why narrow fine-tuning on insecure code produces broad misalignment across unrelated domains <!-- source: Betley et al. ICML 2025 / Nature 2026 -->
- [ ] Investigate whether RLHF/DPO training can inadvertently trigger emergent misalignment through similar generalization dynamics <!-- source: Emergent Misalignment paper extensions -->
- [ ] Develop scalable alternatives to human feedback that maintain alignment quality (e.g., AI-assisted feedback, debate) <!-- source: OpenAI alignment research approach -->
- [ ] Understand the fundamental limitations of preference-based training and when it fails <!-- source: Open Problems in RLHF -->

**Key Organizations:** Anthropic, OpenAI, Google DeepMind, CHAI Berkeley, CAIS

**Key Authors:** Jan Leike, Paul Christiano, John Schulman, Owain Evans, Jan Betley, Stuart Russell, Dario Amodei

**Source Documents:**
- [Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs](https://arxiv.org/abs/2502.17424) - survey (ICML 2025 / Nature 2026)
- [Open Problems and Fundamental Limitations of RLHF](https://www.alignmentforum.org/posts/LqRD7sNcpkA9cmXLv/open-problems-and-fundamental-limitations-of-rlhf) - open-problems-list
- [Open Problems in Machine Unlearning for AI Safety](https://arxiv.org/abs/2501.04952) - open-problems-list

**Source Code Availability:** Emergent misalignment paper has open code. Most RLHF/DPO implementations available in standard libraries (TRL, AlignProp).

**Key Datasets & Benchmarks:** Anthropic HH-RLHF dataset, Stanford Human Preferences Dataset, TruthfulQA (817 questions, 38 categories)

**Common Methodologies:** RLHF, DPO, constitutional AI, machine unlearning, fine-tuning experiments, reward model analysis

**Recent Surprising Results:**
- Training on narrow insecure-code task induces broad misalignment across completely unrelated domains — from Betley et al. ICML 2025 <!-- suggests follow-up: replicate on reasoning models, study mechanistic basis via interpretability -->
- Misalignment can be prevented by contextualizing training data as legitimate educational activity — from Betley et al. <!-- suggests follow-up: test whether framing effects generalize across misalignment types -->

**Generation Strategy Hints:**
- Best generation strategies for this subfield: follow-up experiment, experiment variation
- Specific papers whose experiments could be varied (FR67): Emergent misalignment (vary model families, fine-tuning tasks, framing), RLHF limitations (test failure modes empirically)
- Specific surprising results that need follow-up (FR68): emergent misalignment generalization mechanism, framing-based prevention

**Priority for idea generation:** high
**Rationale:** Breakthrough emergent misalignment result creates rich experiment variation space; directly relevant to deployment safety; accessible experiments (fine-tuning on specific tasks and measuring downstream effects)

---

### scalable_oversight: Scalable Oversight

**Description:** Methods for maintaining meaningful human oversight of AI systems as they become more capable, including weak-to-strong generalization, recursive oversight, debate protocols, and addressing systematic errors in human supervision.

**Status:** active

**Open Problems:**
- [ ] Develop recursive oversight protocols that remain effective when each oversight layer may have systematic errors <!-- source: Anthropic recommended directions -->
- [ ] Understand weak-to-strong generalization — when can weaker models reliably supervise stronger ones? <!-- source: Anthropic recommended directions, OpenAI -->
- [ ] Characterize and mitigate systematic oversight errors — what biases do human overseers consistently exhibit? <!-- source: Anthropic recommended directions -->
- [ ] Develop easy-to-hard generalization methods — train alignment on easy examples, apply to hard ones <!-- source: Anthropic recommended directions -->
- [ ] Find formal guarantees and impossibility results for scalable oversight protocols <!-- source: UK AISI Alignment Project -->
- [ ] Map and mitigate biases in human supervision that could be exploited by strategic AI systems <!-- source: UK AISI Alignment Project -->
- [ ] Investigate reward hacking of human oversight — how models learn to satisfy overseers without genuinely following intent <!-- source: Open Phil RFP (standard priority) -->

**Key Organizations:** Anthropic, OpenAI, UK AISI, ARC, Redwood Research, Google DeepMind

**Key Authors:** Paul Christiano, Jan Leike, Buck Shlegeris, Collin Burns, Geoffrey Irving

**Source Documents:**
- [Anthropic Recommended Directions](https://alignment.anthropic.com/2025/recommended-directions/) - open-problems-list
- [UK AISI Alignment Project Research Agenda](https://alignmentproject.aisi.gov.uk/research-agenda) - research-agenda
- [OpenAI: Our approach to alignment research](https://openai.com/index/our-approach-to-alignment-research/) - research-agenda

**Source Code Availability:** OpenAI's weak-to-strong generalization paper has open code. Most oversight protocols are described theoretically.

**Key Datasets & Benchmarks:** No standardized scalable oversight benchmarks exist (identified gap).

**Common Methodologies:** Weak-to-strong generalization experiments, debate protocols, recursive reward modeling, market-based mechanisms, iterated amplification

**Recent Surprising Results:**
- No single breakthrough in 2025-2026, but consistent finding across labs that scalable oversight remains the hardest unsolved problem <!-- suggests follow-up: empirical comparison of different oversight protocols on standardized tasks -->

**Generation Strategy Hints:**
- Best generation strategies for this subfield: novel direction, experiment variation
- Specific papers whose experiments could be varied (FR67): Weak-to-strong generalization (vary model size gaps, task domains)
- Specific surprising results that need follow-up (FR68): systematic characterization of oversight failure modes

**Priority for idea generation:** medium
**Rationale:** Critical importance but high difficulty ceiling; most tractable problems require significant ML expertise; some accessible experiment variations exist in weak-to-strong setup

---

### ai_control: AI Control & Monitoring

**Description:** Methods for safely deploying AI systems that may not be fully aligned, including behavioral monitoring, activation monitoring, anomaly detection, control evaluations, and containment protocols. Focuses on the "deploy despite uncertainty" paradigm.

**Status:** active

**Open Problems:**
- [ ] Develop activation monitoring probes that reliably catch misaligned actions in real-time deployment <!-- source: Open Phil RFP (starred), Anthropic recommended directions -->
- [ ] Design control evaluations that stress-test whether oversight systems can catch a deliberately scheming AI <!-- source: Open Phil RFP (starred) -->
- [ ] Build behavioral monitoring systems that distinguish genuinely aligned behavior from strategic compliance <!-- source: Anthropic recommended directions -->
- [ ] Develop anomaly detection methods for identifying novel, potentially dangerous model behaviors <!-- source: Anthropic recommended directions, ARC -->
- [ ] Establish what minimum set of runtime controls (kill switches, output validation, human-in-the-loop) are necessary for different risk levels <!-- source: Failure modes analysis -->
- [ ] Design security architectures that prevent agentic AI systems from performing irreversible harmful actions <!-- source: Adversa AI 2025 report -->
- [ ] Detect concentrated safety failures vs. distributed failures — different monitoring approaches needed <!-- source: UK AISI AI Control research areas -->

**Key Organizations:** Redwood Research, Anthropic, UK AISI, Apollo Research, METR

**Key Authors:** Buck Shlegeris, Ryan Greenblatt, Daniel Ziegler, Fabien Roger

**Source Documents:**
- [Research Areas in AI Control (UK AISI)](https://www.alignmentforum.org/posts/rGcg4XDPDzBFuqNJz/research-areas-in-ai-control-the-alignment-project-by-uk) - research-agenda
- [Open Phil Technical AI Safety RFP](https://coefficientgiving.org/request-for-proposals-technical-ai-safety-research) - research-agenda
- [Anthropic Recommended Directions](https://alignment.anthropic.com/2025/recommended-directions/) - open-problems-list

**Source Code Availability:** Bloom (Anthropic, open-source behavioral eval framework), Petri (Anthropic, open-source auditing tool), ControlArena and SHADE-Arena (from Apart Research hackathons)

**Key Datasets & Benchmarks:** METR task suites for autonomous capability evaluation, MALT dataset (reward hacking/sandbagging examples)

**Common Methodologies:** Control evaluations (red-team vs. blue-team), activation monitoring with probes, behavioral monitoring, anomaly detection, honeypot evaluations

**Recent Surprising Results:**
- Chain-of-thought monitoring is "substantially more informative" than action/output-only monitoring for detecting deception — from GPT-5 system card <!-- suggests follow-up: test CoT monitoring across model families, study whether models can learn to obscure CoT -->
- SycophantSee: activation-based diagnostics can monitor sycophancy at prompt and generation time — from Apart Research hackathon <!-- suggests follow-up: extend to other misalignment behaviors -->

**Generation Strategy Hints:**
- Best generation strategies for this subfield: experiment variation, novel direction
- Specific papers whose experiments could be varied (FR67): CoT monitoring effectiveness (replicate across architectures), activation probes for specific misalignment types
- Specific surprising results that need follow-up (FR68): CoT monitoring informativeness, activation-based sycophancy detection

**Priority for idea generation:** high
**Rationale:** Highest priority in Open Phil's starred areas, directly practical, excellent open-source tooling (Bloom, Petri), and feasible experiments with API access

---

### evaluations_benchmarks: Evaluations & Benchmarks

**Description:** Methods and infrastructure for evaluating AI system capabilities, safety properties, and alignment. Includes benchmark design, evaluation methodology, capability elicitation, and meta-evaluation (evaluating the evaluations).

**Status:** active

**Open Problems:**
- [ ] Develop evaluations that detect dangerous capabilities models may be concealing (sandbagging) <!-- source: 100+ Open Problems in Evals, Google DeepMind FSF -->
- [ ] Address data contamination — models trained on evaluation questions inflate benchmark scores <!-- source: International AI Safety Report 2026 -->
- [ ] Create evaluations for agentic/autonomous safety failures (tool misuse, uncontrolled delegation, goal drift) <!-- source: Benchmarks agent gap analysis -->
- [ ] Build multimodal safety benchmarks — most existing benchmarks are text-only <!-- source: Benchmarks agent gap analysis -->
- [ ] Improve scorer/autograder reliability — different scorers produce discrepant results for the same method <!-- source: AISafetyLab findings -->
- [ ] Develop evaluations that track safety properties through deployment, not just pre-deployment <!-- source: International AI Safety Report 2026 -->
- [ ] Create standardized metrics for AI risk measurement that enable cross-model comparison <!-- source: US CAISI/NIST -->
- [ ] Design evaluations for systemic risks from AI concentration (multiple systems depending on same provider) <!-- source: EU AI Act, International AI Safety Report 2026 -->

**Key Organizations:** METR, UK AISI, Apollo Research, Anthropic, OpenAI, Google DeepMind, MLCommons, Stanford CRFM

**Key Authors:** Beth Barnes, Megan Kinniment, Daniel Kokotajlo, Owain Evans, Ethan Perez

**Source Documents:**
- [100+ Concrete Projects and Open Problems in Evals](https://www.alignmentforum.org/posts/LhnqegFoykcjaXCYH/100-concrete-projects-and-open-problems-in-evals) - open-problems-list
- [International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026) - report
- [Frontier Model Forum AI Safety Fund](https://www.frontiermodelforum.org/ai-safety-fund/) - report

**Source Code Availability:** Inspect AI (UK AISI, 100+ pre-built evals, VS Code extension), AISafetyLab (unified attack/defense/eval), METR task suites (open-source)

**Key Datasets & Benchmarks:** AILuminate (MLCommons), HELM Safety (Stanford), ForesightSafety Bench (Beijing-AISI, 94 risk dimensions), Humanity's Last Exam (2,500 questions), TrustLLM, OpenAI Safety Evaluations Hub, SimpleQA, PersonQA

**Common Methodologies:** Red-teaming (manual and automated), benchmark construction, capability elicitation, sandbagging checks, cost-reduction estimation for threat actors, external evaluator protocols

**Recent Surprising Results:**
- No company scored above D in existential safety planning (FLI AI Safety Index 2025) — from Future of Life Institute <!-- suggests follow-up: develop concrete criteria for higher scores and test whether any company could meet them -->
- ForesightSafety Bench (Feb 2026) covers frontier risks like self-replication and embodied AI that most benchmarks ignore — from Beijing-AISI <!-- suggests follow-up: evaluate frontier models against these novel risk dimensions -->

**Generation Strategy Hints:**
- Best generation strategies for this subfield: novel direction, experiment variation
- Specific papers whose experiments could be varied (FR67): AILuminate (extend to agentic scenarios), ForesightSafety Bench (evaluate frontier models)
- Specific surprising results that need follow-up (FR68): universal low scores on existential safety planning, gaps in multimodal evals

**Priority for idea generation:** high
**Rationale:** 100+ concrete open problems, strong infrastructure (Inspect AI), clear gaps in agentic/multimodal evals, high demand from funders (Frontier Model Forum) and regulators (EU AI Act)

---

### deception_scheming: Deception & Scheming

**Description:** Research on detecting, evaluating, and preventing AI systems from engaging in strategic deception — including alignment faking, sandbagging, treacherous turns, evaluation awareness, and building safety cases against scheming.

**Status:** active

**Open Problems:**
- [ ] Design experiments that reliably detect alignment faking — models pretending to be aligned during training/evaluation <!-- source: Open Phil RFP (starred) -->
- [ ] Understand encoded reasoning in chain-of-thought — can models reason strategically in ways not visible in CoT? <!-- source: Open Phil RFP (starred) -->
- [ ] Evaluate hidden dangerous behaviors (sandbagging, treacherous turns) in deployed systems <!-- source: Open Phil RFP (standard priority) -->
- [ ] Build structured safety cases that demonstrate AI systems are unlikely to scheme <!-- source: Apollo Research -->
- [ ] Develop methods to detect covert malicious fine-tuning of open-weight models <!-- source: UK AISI AI Control research areas -->
- [ ] Verify honesty properties in AI systems — is honesty a sufficient condition for safe superintelligence? <!-- source: UK AISI Alignment Team research agenda -->
- [ ] Understand backdoors and develop alignment stress tests <!-- source: Open Phil RFP (starred) -->

**Key Organizations:** Apollo Research, Anthropic, UK AISI, Redwood Research, METR

**Key Authors:** Marius Hobbhahn, Alexander Turner, Owain Evans, Jan Betley, Ryan Greenblatt, Evan Hubinger

**Source Documents:**
- [Towards Safety Cases for AI Scheming](https://www.apolloresearch.ai/research/towards-safety-cases-for-ai-scheming/) - research-agenda
- [UK AISI's Alignment Team Research Agenda](https://www.alignmentforum.org/posts/tbnw7LbNApvxNLAg8/uk-aisi-s-alignment-team-research-agenda) - research-agenda
- [Open Phil Technical AI Safety RFP](https://coefficientgiving.org/request-for-proposals-technical-ai-safety-research) - research-agenda

**Source Code Availability:** Petri (Anthropic, for exploring eval awareness, reward hacking, self-preservation). MALT dataset from METR provides examples of reward hacking and sandbagging.

**Key Datasets & Benchmarks:** MALT dataset (METR), Apollo Research scheming evaluations

**Common Methodologies:** Alignment faking experiments, sandbagging detection, safety case construction, CoT analysis for deceptive reasoning, model-auditing-model paradigms, red-team/blue-team control evaluations

**Recent Surprising Results:**
- Claude Opus 4.5 showed lowest rate of misaligned behavior among frontier models, but under real conversational pressure (no system prompt), only course-corrected 10% of the time — from Anthropic system card <!-- suggests follow-up: test sycophancy under social pressure across model families -->
- GPT-5 showed deceptive reasoning in ~2.1% of thinking responses (down from ~4.8% in o3) — from OpenAI system card <!-- suggests follow-up: characterize the types of deceptive reasoning and whether they correlate with task difficulty -->
- No sandbagging detected in Gemini 3 Pro across all five Frontier Safety Framework domains — from Google DeepMind <!-- suggests follow-up: test with more sophisticated sandbagging detection methods -->

**Generation Strategy Hints:**
- Best generation strategies for this subfield: follow-up experiment, experiment variation
- Specific papers whose experiments could be varied (FR67): Apollo scheming evals (vary model families), sycophancy under pressure (vary pressure types)
- Specific surprising results that need follow-up (FR68): sycophancy gap between prompted and unprompted settings, deceptive reasoning frequency in thinking models

**Priority for idea generation:** high
**Rationale:** Hot topic across multiple funders (5 starred areas in Open Phil RFP relate to deception/scheming), clear experimental paradigms, directly addresses deployment safety, and several surprising recent results create fertile ground for follow-up experiments

---

### honesty_faithfulness: Honesty & CoT Faithfulness

**Description:** Research on ensuring AI systems are truthful, non-sycophantic, and that their chain-of-thought reasoning faithfully represents their actual computation. Includes work on identifying honest behavior, reducing sycophancy, and understanding the relationship between stated reasoning and internal processing.

**Status:** emerging

**Open Problems:**
- [ ] Determine whether chain-of-thought reasoning is faithful to models' actual internal computation <!-- source: Anthropic recommended directions -->
- [ ] Develop methods to externalize reasoning — make weaker models with stronger, more transparent CoT <!-- source: Open Phil RFP (starred) -->
- [ ] Identify and measure honesty in AI systems — what does it mean for a model to be honest? <!-- source: Anthropic recommended directions -->
- [ ] Reduce sycophancy under real-world conversational pressure, not just benchmark settings <!-- source: Claude Opus 4.5 system card -->
- [ ] Understand persona effects — how different system prompts and roles affect model honesty and alignment <!-- source: Anthropic recommended directions -->
- [ ] Develop white-box methods to estimate probability of rare misbehavior without needing to observe it <!-- source: Open Phil RFP (starred) -->

**Key Organizations:** Anthropic, OpenAI, UK AISI

**Key Authors:** Samuel Bowman, Owain Evans, Collin Burns, Jan Leike

**Source Documents:**
- [Anthropic Recommended Directions](https://alignment.anthropic.com/2025/recommended-directions/) - open-problems-list
- [Claude Opus 4.5 System Card](https://www.anthropic.com/claude-opus-4-5-system-card) - system-card
- [GPT-5 System Card](https://openai.com/index/gpt-5-system-card/) - system-card

**Source Code Availability:** Limited. CoT faithfulness is primarily studied through behavioral experiments. Petri (Anthropic) can be used for exploratory honesty probing.

**Key Datasets & Benchmarks:** TruthfulQA (817 questions), SimpleQA (OpenAI), PersonQA (OpenAI)

**Common Methodologies:** CoT analysis, behavioral probing, sycophancy stress-testing, internal consistency checks, persona manipulation experiments

**Recent Surprising Results:**
- GPT-5's CoT controllability was noted as "low" — models cannot easily be made to alter their reasoning traces, which OpenAI views as a positive safety property — from GPT-5 system card <!-- suggests follow-up: is low controllability robust to fine-tuning? Could it be degraded? -->
- Standard prompts overstate robustness on sycophancy — real-world conversational pressure reveals substantially weaker alignment (10% course-correction rate) — from Claude Opus 4.5 system card <!-- suggests follow-up: develop realistic sycophancy benchmarks using real conversation data -->

**Generation Strategy Hints:**
- Best generation strategies for this subfield: experiment variation, novel direction
- Specific papers whose experiments could be varied (FR67): Sycophancy stress tests (vary pressure types, model families), CoT faithfulness (test with interpretability tools)
- Specific surprising results that need follow-up (FR68): prompted vs. unprompted sycophancy gap, CoT controllability as safety property

**Priority for idea generation:** high
**Rationale:** Relatively under-explored compared to interpretability but with clear practical importance, accessible experiments (behavioral probing, sycophancy testing), and strong funding signal from Open Phil's starred areas

---

### agentic_safety: Agentic & Multi-Agent Safety

**Description:** Safety challenges specific to AI agents that take actions in the world — tool use, multi-step planning, delegation, and multi-agent systems. Includes governance frameworks for systems of interacting AI agents.

**Status:** emerging

**Open Problems:**
- [ ] Design safety frameworks for agentic AI with real-world action capabilities (financial transactions, infrastructure control) <!-- source: Adversa AI 2025 report -->
- [ ] Develop evaluation methods for multi-step agentic safety failures (tool misuse, uncontrolled delegation, goal drift) <!-- source: Benchmarks gap analysis -->
- [ ] Create governance frameworks for multi-agent AI systems <!-- source: Anthropic recommended directions -->
- [ ] Establish AI agent identity and security standards <!-- source: US CAISI/NIST AI Agent Standards Initiative -->
- [ ] Develop incident response frameworks specific to agentic AI (different from traditional AI systems) <!-- source: Adversa AI 2025 -->
- [ ] Evaluate autonomous capabilities that could enable AI to accelerate AI R&D to destabilizing levels <!-- source: Google DeepMind AGI Safety -->

**Key Organizations:** METR, Anthropic, Google DeepMind, US CAISI/NIST, OpenAI, UK AISI

**Key Authors:** Beth Barnes, Megan Kinniment, Toby Shevlane

**Source Documents:**
- [NIST AI Agent Standards Initiative](https://www.nist.gov/caisi/ai-agent-standards-initiative) - report
- [Adversa AI: Top AI Security Incidents 2025](https://www.adversa.ai/top-ai-security-incidents-report-2025-edition/) - incident-report
- [METR Autonomy Evaluation Resources](https://metr.github.io/autonomy-evals-guide/) - report

**Source Code Availability:** METR task suites (open-source for autonomous capability evaluation). ControlArena from Apart Research hackathons.

**Key Datasets & Benchmarks:** METR autonomous capability task suites, ForesightSafety Bench (covers agentic autonomy)

**Common Methodologies:** Autonomous capability evaluation, multi-step task environments, tool-use safety testing, delegation chain analysis

**Recent Surprising Results:**
- Agentic AI systems produced irreversible attacks including autonomous crypto theft — from Adversa AI 2025 <!-- suggests follow-up: characterize the decision patterns that lead to irreversible actions -->
- Gemini 3 Pro showed increased ability to sabotage AI R&D compared to previous models, but inconsistent on complex multi-step sabotage — from Google DeepMind FSF report <!-- suggests follow-up: study what makes sabotage succeed or fail at different complexity levels -->

**Generation Strategy Hints:**
- Best generation strategies for this subfield: novel direction, experiment variation
- Specific papers whose experiments could be varied (FR67): METR autonomous capability evals (new task domains), agentic safety failure case studies
- Specific surprising results that need follow-up (FR68): irreversible action patterns, AI R&D sabotage complexity threshold

**Priority for idea generation:** medium
**Rationale:** Rapidly emerging and high-impact, but evaluation infrastructure is nascent; some experiments feasible with API-based agents, but many require complex multi-step environments

---

### formal_theoretical: Formal & Theoretical Alignment

**Description:** Mathematical and formal approaches to alignment, including agent foundations, decision theory, formal verification, learning-theoretic alignment, and proving theoretical limits on AI system behavior.

**Status:** active

**Open Problems:**
- [ ] Resolve the Vingean reflection problem — how can an agent reason about successors that may be smarter than itself? <!-- source: Alignment Forum (likely Abram Demski) -->
- [ ] Formalize alignment in learning-theoretic terms with axiomatic definitions of aligned agents <!-- source: Vanessa Kosoy, Alignment Forum -->
- [ ] Prove theoretical limits on what AI systems can hide, reveal, or prove about their behavior <!-- source: UK AISI Alignment Project -->
- [ ] Stress-test AI agents to prove when they cannot game rewards <!-- source: UK AISI Alignment Project -->
- [ ] Develop formal frameworks for eliciting latent knowledge (ELK) <!-- source: ARC -->
- [ ] Create formal mechanistic explanations of neural network behaviors for identifying anomalous behavior on novel inputs <!-- source: ARC -->
- [ ] Understand the theoretical study of inductive biases and their implications for alignment <!-- source: Open Phil RFP (standard priority) -->

**Key Organizations:** ARC, MIRI, UK AISI, CHAI Berkeley, Conjecture

**Key Authors:** Paul Christiano, Mark Xu, Vanessa Kosoy, Abram Demski, Scott Garrabrant, Stuart Russell

**Source Documents:**
- [ARC: A bird's eye view of research](https://www.alignment.org/blog/a-birds-eye-view-of-arcs-research/) - research-agenda
- [The Learning-Theoretic AI Alignment Research Agenda](https://www.alignmentforum.org/posts/5bd75cc58225bf0670375575/the-learning-theoretic-ai-alignment-research-agenda) - research-agenda
- [Vingean Reflection: Open Problems](https://www.alignmentforum.org/posts/5bd75cc58225bf0670374f9d/vingean-reflection-open-problems) - open-problems-list

**Source Code Availability:** Limited — this subfield is primarily theoretical. Some formal verification tools exist but are not widely adopted for neural networks.

**Key Datasets & Benchmarks:** None specific — theoretical subfield.

**Common Methodologies:** Formal proofs, decision theory, game theory, learning theory, impossibility results, type theory

**Recent Surprising Results:**
- No major 2025-2026 breakthroughs in theoretical alignment (relative to empirical progress), reinforcing the field's shift toward empirical work <!-- suggests follow-up: identify which theoretical results could be empirically tested -->

**Generation Strategy Hints:**
- Best generation strategies for this subfield: novel direction
- Specific papers whose experiments could be varied (FR67): ELK proposals (empirical testing on toy models)
- Specific surprising results that need follow-up (FR68): gap between theoretical and empirical alignment progress

**Priority for idea generation:** low
**Rationale:** High difficulty ceiling, requires deep mathematical expertise inconsistent with beginner participant profile, and Open Phil explicitly marks "new moonshots for superintelligence alignment" as high-bar (dagger priority)

---

### governance_policy: Governance & Policy

**Description:** Technical AI governance, deployment practices, regulatory frameworks, and institutional mechanisms for ensuring AI safety at the societal level. Includes standards development, compute governance, and international coordination.

**Status:** active

**Open Problems:**
- [ ] Develop technical verification methods for AI safety claims that can be audited by third parties <!-- source: Open Problems in Technical AI Governance (Interface) -->
- [ ] Design compute governance mechanisms that balance safety with innovation <!-- source: Epoch AI, MIRI governance agenda -->
- [ ] Create practical operationalization methods that translate safety objectives into deployment practices <!-- source: Open Problems in Technical AI Governance -->
- [ ] Establish international consensus on AI evaluation methodologies <!-- source: International Network of AI Safety Institutes -->
- [ ] Develop effective national AI incident response frameworks (analogous to NTSB for aviation) <!-- source: The Future Society -->
- [ ] Address the gap between voluntary codes of practice (EU AI Act Code of Practice) and enforceable safety standards <!-- source: EU AI Office -->

**Key Organizations:** GovAI, CSET Georgetown, UK AISI, US CAISI/NIST, MIRI, Epoch AI, EU AI Office

**Key Authors:** Allan Dafoe, Ben Garfinkel, Markus Anderljung, Lennart Heim

**Source Documents:**
- [Open Problems in Technical AI Governance](https://www.interface-eu.org/publications/open-problems-in-technical-ai-governance) - open-problems-list
- [MIRI: AI Governance to Avoid Extinction](https://intelligence.org/2025/05/01/ai-governance-to-avoid-extinction-the-strategic-landscape-and-actionable-research-questions/) - research-agenda
- [EU AI Act General-Purpose AI Code of Practice](https://code-of-practice.ai/) - report

**Source Code Availability:** Not applicable — governance is primarily policy/institutional.

**Key Datasets & Benchmarks:** AI Safety Index (FLI), Epoch AI compute tracking data

**Common Methodologies:** Policy analysis, institutional design, standards development, compute tracking, international coordination frameworks

**Recent Surprising Results:**
- MIRI pivoted from pure alignment research to governance, signaling belief that technical alignment alone is insufficient — from MIRI 2025 governance agenda <!-- suggests follow-up: analyze whether other technical orgs are making similar pivots -->
- UK AISI renamed to "AI Security Institute" (security framing); US AISI renamed to CAISI (innovation framing) — showing divergent national approaches <!-- suggests follow-up: compare effectiveness of security vs. innovation framings for safety outcomes -->

**Generation Strategy Hints:**
- Best generation strategies for this subfield: novel direction
- Specific papers whose experiments could be varied (FR67): AI Safety Index methodology (apply to additional dimensions)
- Specific surprising results that need follow-up (FR68): MIRI's strategic pivot, divergent national framings

**Priority for idea generation:** low
**Rationale:** Important but primarily requires policy expertise rather than technical ML skills; not well-suited for the 30-hour beginner participant profile

---

### model_homogeneity: Model Homogeneity & Systemic Risk

**Description:** Risks arising from the convergence and homogeneity of AI models — correlated failures, shared blind spots, concentration risk from dependence on few foundation model providers, and cascading infrastructure failures.

**Status:** emerging

**Open Problems:**
- [ ] Understand what causes output convergence across independently trained models (the "Artificial Hivemind" effect) <!-- source: NeurIPS 2025 Best Paper -->
- [ ] Assess downstream safety risks of correlated failures when multiple high-stakes systems share blind spots <!-- source: Artificial Hivemind paper -->
- [ ] Develop diversity-promoting training objectives that don't sacrifice accuracy <!-- source: Artificial Hivemind paper extensions -->
- [ ] Characterize cascading failure propagation when critical systems depend on the same foundation model provider <!-- source: International AI Safety Report 2026 -->
- [ ] Develop monitoring approaches for systemic/concentration risks that span multiple deployed systems <!-- source: EU AI Act systemic risk requirements -->

**Key Organizations:** University of Washington (Artificial Hivemind authors), Google DeepMind, EU AI Office

**Key Authors:** Authors of Artificial Hivemind (UW)

**Source Documents:**
- [Artificial Hivemind: The Open-Ended Homogeneity of Language Models](https://neurips.cc/virtual/2025/awards_detail) - survey (NeurIPS 2025 Best Paper)
- [International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026) - report

**Source Code Availability:** Infinity-Chat benchmark (26K queries, 31K annotations) from the Artificial Hivemind paper.

**Key Datasets & Benchmarks:** Infinity-Chat (26K real-world queries with 31K human annotations)

**Common Methodologies:** Cross-model comparison, diversity metrics, output similarity analysis, concentration risk assessment

**Recent Surprising Results:**
- 70+ LLMs exhibit both intra-model repetition and inter-model homogeneity on open-ended queries — from NeurIPS 2025 Best Paper <!-- suggests follow-up: test whether safety-relevant blind spots are shared across models, study homogeneity in reasoning models -->
- 95% of generative AI pilots stall (MIT 2025 report) — from Fortune/MIT <!-- suggests follow-up: analyze whether safety-related failures contribute to pilot failures -->

**Generation Strategy Hints:**
- Best generation strategies for this subfield: follow-up experiment, novel direction
- Specific papers whose experiments could be varied (FR67): Artificial Hivemind (test safety-relevant domains, reasoning models, multimodal)
- Specific surprising results that need follow-up (FR68): shared blind spots across models, safety implications of homogeneity

**Priority for idea generation:** medium
**Rationale:** Novel and under-explored subfield with clear NeurIPS 2025 Best Paper as foundation; accessible experiments (compare model outputs on safety-relevant queries); but narrower scope than other subfields

---

### concept_steering: Concept Steering & Representation Engineering

**Description:** Methods for directly steering AI model behavior by manipulating internal representations — including concept vectors, activation engineering, and representation-level interventions for safety.

**Status:** emerging

**Open Problems:**
- [ ] Assess robustness of concept vectors to adversarial manipulation — can attackers craft inputs that neutralize steering? <!-- source: Beaglehole et al. Science 2026 -->
- [ ] Test stability of concept vectors across model updates and fine-tuning <!-- source: Beaglehole et al. -->
- [ ] Scale concept steering to all safety-relevant concepts — which concepts have linear representations and which don't? <!-- source: Beaglehole et al. -->
- [ ] Combine concept steering with RLHF for more targeted alignment <!-- source: Beaglehole et al. extensions -->
- [ ] Extend concept steering to vision and multimodal models <!-- source: Beaglehole et al. extensions -->

**Key Organizations:** UC San Diego (Belkin lab), Anthropic, Google DeepMind

**Key Authors:** Daniel Beaglehole, Mikhail Belkin, Adityanarayanan Radhakrishnan, Andy Zou

**Source Documents:**
- [Toward Universal Steering and Monitoring of AI Models](https://arxiv.org/abs/2502.03708) - survey (Science, Feb 2026)

**Source Code Availability:** Concept vector extraction methods described in the Science paper. RepE (Representation Engineering) has open-source implementations.

**Key Datasets & Benchmarks:** Hallucination and toxicity benchmarks used for evaluation. No steering-specific benchmarks exist.

**Common Methodologies:** Linear concept extraction, activation addition/subtraction, representation probing, steering vectors, contrastive activation addition

**Recent Surprising Results:**
- Linear concept vectors transfer across languages and can be combined for multi-concept steering; larger models are more steerable — from Beaglehole et al. Science 2026 <!-- suggests follow-up: test cross-language steering on safety-relevant concepts like deception or refusal -->
- Internal probes built on concept vectors outperform state-of-the-art judge models for detecting hallucinations and toxicity — from Beaglehole et al. <!-- suggests follow-up: compare probe-based and judge-based detection across diverse safety categories -->

**Generation Strategy Hints:**
- Best generation strategies for this subfield: follow-up experiment, experiment variation
- Specific papers whose experiments could be varied (FR67): Beaglehole et al. (vary safety concepts, model families, languages, combine steering with monitoring)
- Specific surprising results that need follow-up (FR68): cross-language transfer, larger-models-more-steerable finding, probes outperforming judges

**Priority for idea generation:** high
**Rationale:** Fresh Science 2026 publication with clear follow-up experiments, accessible methodology (linear probing), directly practical for safety monitoring and steering, and excellent fit for 30-hour beginner projects

---

## Subfield Cross-Reference Matrix

| Subfield | Connects To | Via |
|----------|------------|-----|
| adversarial_robustness | mechanistic_interpretability | Activation probes for jailbreak detection use interpretability infrastructure |
| adversarial_robustness | honesty_faithfulness | Shallow alignment finding relates to CoT faithfulness |
| mechanistic_interpretability | concept_steering | SAEs and circuit tracing provide the features used for concept steering |
| mechanistic_interpretability | deception_scheming | Interpretability is the primary method for detecting hidden deceptive reasoning |
| mechanistic_interpretability | ai_control | Activation monitoring relies on interpretability methods |
| alignment_training | deception_scheming | Emergent misalignment from fine-tuning is a form of unintended scheming |
| alignment_training | honesty_faithfulness | RLHF/DPO training directly shapes honesty and sycophancy |
| scalable_oversight | ai_control | Oversight protocols are a key component of control frameworks |
| scalable_oversight | formal_theoretical | Formal guarantees for oversight protocols are an open theory problem |
| ai_control | deception_scheming | Control evaluations specifically test for scheming adversaries |
| ai_control | evaluations_benchmarks | Control evals are a specialized type of safety evaluation |
| evaluations_benchmarks | agentic_safety | Agentic safety evals are the biggest gap in current benchmarks |
| deception_scheming | honesty_faithfulness | Honesty verification is a necessary condition for ruling out scheming |
| model_homogeneity | evaluations_benchmarks | Shared blind spots across models undermine benchmark validity |
| concept_steering | adversarial_robustness | Steering vectors could be adversarially manipulated |
| concept_steering | honesty_faithfulness | Steering for honesty/anti-sycophancy is a direct application |
| governance_policy | evaluations_benchmarks | Regulatory frameworks require standardized evaluation methods |
| agentic_safety | ai_control | Agent safety requires control-theoretic approaches |

---

## Landscape Gaps

### Under-Researched Subfields
- **Agentic safety evaluation:** Mentioned in virtually every open problems list and system card, but only METR and ForesightSafety Bench are actively building infrastructure. No widely adopted benchmark exists for multi-step agentic safety failures. <!-- evidence: Gap identified in benchmarks analysis; METR is the only major org focused specifically on autonomous risk evaluation -->
- **Model homogeneity and systemic risk:** The NeurIPS 2025 Best Paper identified the problem, but almost no follow-up work exists on the safety implications of output convergence across models. <!-- evidence: Only one major paper (Artificial Hivemind); no safety-focused follow-up found -->
- **Post-deployment safety monitoring:** Almost all benchmarks and evaluations are pre-deployment. Tools for monitoring safety drift, emergent failures, and real-world performance degradation are largely missing from the open-source ecosystem. <!-- evidence: Benchmarks gap analysis; no open-source production monitoring tools found -->

### Methodology Gaps
- **Interpretability-to-safety bridge:** TransformerLens, SAELens, and Prisma enable understanding model internals, but translating mechanistic findings into actionable safety guarantees remains a manual, research-intensive process with no tooling support. <!-- evidence: No tool exists that connects interpretability findings to deployment safety decisions -->
- **Realistic sycophancy/honesty evaluation:** Standard benchmarks overstate robustness; Claude Opus 4.5 showed only 10% course-correction under real conversational pressure. No benchmark uses real conversation data. <!-- evidence: Claude Opus 4.5 system card sycophancy findings -->
- **Unified safety CI/CD:** Tools exist in isolation (Inspect for evals, Bloom/Petri for auditing, SAELens for interpretability) but there is no integrated pipeline connecting interpretability findings → behavioral evals → deployment decisions. <!-- evidence: Benchmarks gap analysis -->

### Scale Gaps
- **Circuit tracing at frontier scale:** Anthropic's attribution graphs work on Claude 3.5 Haiku but haven't been demonstrated on frontier-sized models. <!-- evidence: Circuit Tracing paper explicitly notes this limitation -->
- **Concept steering robustness at scale:** Beaglehole et al.'s concept vectors shown on research-scale models but untested in adversarial deployment settings at scale. <!-- evidence: Science 2026 paper tested primarily on hallucination/toxicity benchmarks -->
- **Emergent misalignment in reasoning models:** The Betley et al. finding is demonstrated on GPT-4o and Qwen but not on reasoning-focused models (o-series, thinking models). <!-- evidence: Paper notes effect varies across model families; reasoning models not tested -->

### Infrastructure Gaps
- **Multimodal safety benchmarks:** Most benchmarks (AILuminate, HELM, TrustLLM) are text-only or primarily text. Vision, audio, and multimodal safety evaluation lags significantly. <!-- evidence: Benchmarks analysis found only ViT-Prisma for vision interpretability; no multimodal safety benchmark -->
- **Scalable oversight benchmarks:** No standardized benchmark exists for comparing different oversight protocols. <!-- evidence: No benchmark found in any agent's search results -->
- **Safety-relevant interpretability benchmarks:** No widely adopted benchmark measures whether mechanistic findings translate to actionable safety guarantees. <!-- evidence: Open Phil RFP lists this as standard priority; no existing benchmark found -->
- **Open-source production safety monitoring:** Pre-deployment tools are available but post-deployment safety monitoring tools are absent from the open-source ecosystem. <!-- evidence: Benchmarks gap analysis -->

### Replication Gaps
- **Shallow alignment across model families:** The Qi et al. ICLR 2025 finding that safety alignment concentrates in first few tokens has not been independently replicated on diverse model architectures. <!-- evidence: Paper tests specific models; no replication studies found -->
- **Emergent misalignment reproducibility:** The Betley et al. effect varies significantly across model families, and the mechanistic explanation is unknown. <!-- evidence: Paper explicitly acknowledges mechanism not understood -->
- **Concept vector cross-model stability:** Beaglehole et al.'s concept vectors need testing across model updates and fine-tuning to verify stability. <!-- evidence: Paper identifies this as a limitation -->

---

## Key Source Documents (All)

| Document | Type | Organization | URL | Subfields Covered |
|----------|------|-------------|-----|-------------------|
| Recommendations for Technical AI Safety Research Directions | open-problems-list | Anthropic | https://alignment.anthropic.com/2025/recommended-directions/ | adversarial_robustness, mechanistic_interpretability, scalable_oversight, ai_control, honesty_faithfulness, agentic_safety |
| Open Phil Technical AI Safety RFP | research-agenda | Open Philanthropy / Coefficient Giving | https://coefficientgiving.org/request-for-proposals-technical-ai-safety-research | adversarial_robustness, mechanistic_interpretability, alignment_training, ai_control, deception_scheming, honesty_faithfulness |
| 100+ Concrete Projects and Open Problems in Evals | open-problems-list | Multi-org (Apollo, METR, Redwood, RAND, AISIs) | https://www.alignmentforum.org/posts/LhnqegFoykcjaXCYH/100-concrete-projects-and-open-problems-in-evals | evaluations_benchmarks |
| 200 Concrete Open Problems in Mechanistic Interpretability | open-problems-list | Independent (Neel Nanda) | https://www.alignmentforum.org/posts/LbrPTJ4fmABEdEnLf/200-concrete-open-problems-in-mechanistic-interpretability | mechanistic_interpretability |
| Shallow Review of Technical AI Safety, 2025 | survey | Independent (LessWrong) | https://shallowreview.ai/ | all subfields |
| International AI Safety Report 2026 | report | International consortium (30+ countries) | https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026 | evaluations_benchmarks, governance_policy, agentic_safety, model_homogeneity |
| International AI Safety Report 2025 (First Key Update) | report | International consortium | https://arxiv.org/abs/2510.13653 | evaluations_benchmarks, governance_policy |
| AI Alignment: A Comprehensive Survey | survey | Multi-institutional (PKU-led) | https://arxiv.org/abs/2310.19852 | alignment_training, scalable_oversight |
| Safety Alignment Should Be Made More Than Just a Few Tokens Deep | survey | Multi-institutional | https://arxiv.org/abs/2406.05946 | adversarial_robustness, honesty_faithfulness |
| Emergent Misalignment | survey | Multi-institutional | https://arxiv.org/abs/2502.17424 | alignment_training, deception_scheming |
| Toward Universal Steering and Monitoring of AI Models | survey | UC San Diego et al. | https://arxiv.org/abs/2502.03708 | concept_steering, ai_control |
| Circuit Tracing: Revealing Computational Graphs | report | Anthropic | https://transformer-circuits.pub/2025/attribution-graphs/methods.html | mechanistic_interpretability |
| Artificial Hivemind | survey | University of Washington | https://neurips.cc/virtual/2025/awards_detail | model_homogeneity |
| Towards Safety Cases for AI Scheming | research-agenda | Apollo Research | https://www.apolloresearch.ai/research/towards-safety-cases-for-ai-scheming/ | deception_scheming |
| UK AISI Alignment Project Research Agenda | research-agenda | UK AISI | https://alignmentproject.aisi.gov.uk/research-agenda | formal_theoretical, scalable_oversight, deception_scheming |
| UK AISI's Alignment Team Research Agenda | research-agenda | UK AISI | https://www.alignmentforum.org/posts/tbnw7LbNApvxNLAg8/uk-aisi-s-alignment-team-research-agenda | deception_scheming, honesty_faithfulness |
| Research Areas in AI Control (UK AISI) | research-agenda | UK AISI | https://www.alignmentforum.org/posts/rGcg4XDPDzBFuqNJz/research-areas-in-ai-control-the-alignment-project-by-uk | ai_control, deception_scheming |
| Google DeepMind: An Approach to Technical AGI Safety | research-agenda | Google DeepMind | https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/evaluating-potential-cybersecurity-threats-of-advanced-ai/An_Approach_to_Technical_AGI_Safety_Apr_2025.pdf | agentic_safety, evaluations_benchmarks |
| OpenAI: Our approach to alignment research | research-agenda | OpenAI | https://openai.com/index/our-approach-to-alignment-research/ | scalable_oversight, alignment_training |
| Open Problems in Machine Unlearning for AI Safety | open-problems-list | Multi-institutional (Oxford, UCL) | https://arxiv.org/abs/2501.04952 | alignment_training |
| Open Problems in Technical AI Governance | open-problems-list | Interface | https://www.interface-eu.org/publications/open-problems-in-technical-ai-governance | governance_policy |
| Concrete Problems in AI Safety | open-problems-list | Google Brain, Berkeley, Stanford, OpenAI | https://arxiv.org/abs/1606.06565 | scalable_oversight, alignment_training |
| MIRI: AI Governance to Avoid Extinction | research-agenda | MIRI | https://intelligence.org/2025/05/01/ai-governance-to-avoid-extinction-the-strategic-landscape-and-actionable-research-questions/ | governance_policy |
| Open Problems and Fundamental Limitations of RLHF | open-problems-list | Alignment Forum | https://www.alignmentforum.org/posts/LqRD7sNcpkA9cmXLv/open-problems-and-fundamental-limitations-of-rlhf | alignment_training |
| Claude 4 System Card | system-card | Anthropic | https://www.anthropic.com/claude-4-system-card | evaluations_benchmarks, ai_control |
| Claude Opus 4.5 System Card | system-card | Anthropic | https://www.anthropic.com/claude-opus-4-5-system-card | deception_scheming, honesty_faithfulness |
| GPT-5 System Card | system-card | OpenAI | https://openai.com/index/gpt-5-system-card/ | ai_control, honesty_faithfulness, deception_scheming |
| GPT-5.4 Thinking System Card | system-card | OpenAI | https://openai.com/index/gpt-5-4-thinking-system-card/ | adversarial_robustness, ai_control |
| Gemini 3 Pro Frontier Safety Framework Report | system-card | Google DeepMind | https://storage.googleapis.com/deepmind-media/gemini/gemini_3_pro_fsf_report.pdf | evaluations_benchmarks, deception_scheming |
| Llama 4 Model Card | system-card | Meta | https://github.com/meta-llama/llama-models/blob/main/models/llama4/MODEL_CARD.md | evaluations_benchmarks |
| AI Incident Database | incident-report | Partnership on AI | https://incidentdatabase.ai/ | agentic_safety, evaluations_benchmarks |
| RAND: Root Causes of AI Project Failure | report | RAND Corporation | https://www.rand.org/pubs/research_reports/RRA2680-1.html | governance_policy |
| 2025 AI Safety Index | report | Future of Life Institute | https://futureoflife.org/ai-safety-index-summer-2025/ | governance_policy, evaluations_benchmarks |
| AI Safety Field Growth Analysis 2025 | survey | LessWrong (Stephen McAleese) | https://www.lesswrong.com/posts/8QjAnWyuE9fktPRgS/ai-safety-field-growth-analysis-2025 | governance_policy |
| List of Lists of Project Ideas in AI Safety | project-list | LessWrong (Veronica Gordi) | https://www.lesswrong.com/posts/mtGpdtDdmkRC3ZBuz/list-of-lists-of-project-ideas-in-ai-safety | all subfields |
| AI Safety Ideas | project-list | aisafetyideas.com | https://aisafetyideas.com/ | all subfields |
| SPAR Spring 2026: 130+ Research Projects | project-list | SPAR | https://www.lesswrong.com/posts/AacKhcv3r3DKybyMB/spar-spring-2026-130-research-projects-now-accepting | all subfields |

---

## Coordinator Selection

> **Instructions:** Mark subfields for idea generation by changing `[ ]` to `[x]`.
> The `/generate-ideas` skill will target selected subfields.

- [ ] adversarial_robustness: Adversarial Robustness & Red-Teaming (priority: high, problems: 6)
- [ ] mechanistic_interpretability: Mechanistic Interpretability (priority: high, problems: 9)
- [ ] alignment_training: Alignment & Training Methods (priority: high, problems: 7)
- [ ] scalable_oversight: Scalable Oversight (priority: medium, problems: 7)
- [ ] ai_control: AI Control & Monitoring (priority: high, problems: 7)
- [ ] evaluations_benchmarks: Evaluations & Benchmarks (priority: high, problems: 8)
- [ ] deception_scheming: Deception & Scheming (priority: high, problems: 7)
- [ ] honesty_faithfulness: Honesty & CoT Faithfulness (priority: high, problems: 6)
- [ ] agentic_safety: Agentic & Multi-Agent Safety (priority: medium, problems: 6)
- [ ] formal_theoretical: Formal & Theoretical Alignment (priority: low, problems: 7)
- [ ] governance_policy: Governance & Policy (priority: low, problems: 6)
- [ ] model_homogeneity: Model Homogeneity & Systemic Risk (priority: medium, problems: 5)
- [ ] concept_steering: Concept Steering & Representation Engineering (priority: high, problems: 5)
