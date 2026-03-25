# Ranked Research Proposals

*Generated: 2026-03-25 17:35 UTC*
*Total proposals: 500*

---

## #1: Jailbreak Benchmark Contamination Check: Are Safety Evaluations Inflated by Training Data Overlap? (Score: 4.43)

**Research Question:** To what extent does if harmful prompts from public jailbreak benchmarks (jailbreakbench, strongreject) are present in safety fine-tuning datasets, models may appear more robust than they are — they have memorized refusal?
**Approach:** Take a set of 100 harmful prompts from JailbreakBench and StrongREJECT. For each prompt, generate 5 semantically equivalent paraphrases using a sep...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #2: Evaluating SAE Reconstruction Error as a Proxy for Interpretability Completeness (Score: 4.43)

**Research Question:** To what extent does saes suffer from reconstruction error — their compressed representation of model activations is imperfect. for safety applications, we need to know whether this residual error (what the sae fails to c?
**Approach:** For GPT-2 Small with a pretrained SAE (from SAELens), collect the SAE reconstruction error vectors for 500 prompts. Train a linear probe on these e...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #3: Instruction Hierarchy Violations: Do Models Prioritize User Harm Requests Over System Prompt Safety Rules? (Score: 4.43)

**Research Question:** To what extent does models receive instructions from both system prompts (operator level) and user turns (user level). a safety failure occurs when user-level harmful requests override system-prompt safety constraints?
**Approach:** Design 30 scenarios with a safety-constraining system prompt (e.g., 'You are a children's educational assistant; never discuss violence') and a use...
**Subfield:** Evaluations & Benchmarks | **Strategy:** novel_direction | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** novel_direction, sources: 0 KB, 0 web

---

## #4: Refusal Prefix Concentration Under Role-Play Personas: Does a System-Prompt Persona Disrupt Shallow Alignment? (Score: 4.43)

**Research Question:** To what extent does qi et al. measured refusal prefix concentration in default chat-model personas. many applications deploy models with persona instructions (e.g., 'you are alex, a helpful assistant'). whether a persona?
**Approach:** For Llama-3-8B-Instruct and Mistral-7B-Instruct, measure refusal prefix concentration and ASR under three system-prompt conditions: (1) default ass...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #5: Emergent Misalignment via In-Context Learning in Smaller Open Models (Score: 4.43)

**Research Question:** To what extent does arxiv 2510.11288 showed that in-context examples (rather than fine-tuning) can produce broadly misaligned responses in llms. this in-context emergent misalignment was demonstrated on proprietary model?
**Approach:** Using the methodology from arXiv 2510.11288, construct in-context few-shot prompts containing narrow misaligned examples (insecure code without dis...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #6: Measuring Whether Explicit Reversibility Awareness in the Causal Chain Prevents Compounding Failures (Score: 4.43)

**Research Question:** To what extent does agents that explicitly reason about reversibility at each step of the causal chain may make significantly different (and safer) delegation and action choices than agents that do not?
**Approach:** Compare two agent conditions on 25 tasks: (a) standard agent, (b) agent with explicit reversibility-awareness prompting at each decision point in t...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #7: Anchoring Bias in Model Overseers: Do Model Overseers Anchor on the First Response in a Comparison? (Score: 4.43)

**Research Question:** To what extent does human overseers show anchoring bias (preferring whichever response is presented first). model overseers may show the same bias, which would be systematically exploitable?
**Approach:** Present the same pair of responses to a model overseer in both orders (A before B, B before A). Measure how often the overseer changes its preferen...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #8: Does CoT Monitor Performance Degrade with Longer Reasoning Traces? (Score: 4.43)

**Research Question:** To what extent does cot monitorability is claimed to improve with longer cot, but longer traces also give more surface for the model to include irrelevant or misleading text that confuses a monitor?
**Approach:** Sample MALT runs stratified by CoT token length. Train a simple logistic regression monitor on CoT embeddings (using sentence-transformers, accessi...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #9: Effect of System Prompt Length on CoT Monitorability (Score: 4.43)

**Research Question:** To what extent does cot monitorability studies typically use standardized or minimal system prompts. real deployments use long system prompts (tools, personas, context). whether long system prompts compress or displace s?
**Approach:** Using a fixed set of reward-hacking scenarios from MALT, vary system prompt length (0, 500, 2000, 5000 tokens of benign instructional text) prepend...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #10: Monitor Anchoring Effect: Does Telling a Monitor the Prior Probability of Misalignment Affect AUROC? (Score: 4.43)

**Research Question:** To what extent does prompted llm monitors are given a transcript and asked to classify it. in real deployments, the prior probability of encountering a misaligned action varies by task. it is unknown whether informing th?
**Approach:** Apply the best MALT prompted monitor to a fixed held-out test set three times, with different stated priors (1%, 10%, 50%). Measure AUROC and calib...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #11: CoT Scratchpad Truncation as a Monitor Evasion Vector: Measuring Detectability Loss (Score: 4.43)

**Research Question:** To what extent does current frontier models sometimes produce truncated or abbreviated cot. if a model strategically truncates its cot to hide reasoning, monitors lose signal. the metr note that models struggle to evade ?
**Approach:** Prompt Llama-3-8B to solve MALT reward-hacking tasks in two conditions: normal CoT and minimized CoT ('think briefly'). Apply the standard MALT pro...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #12: Prefilling Attack Depth: Does Forcing More Tokens of Harmful Preamble Increase Attack Success? (Score: 4.43)

**Research Question:** To what extent does prefilling attacks typically force the model to begin with 'sure, here is...' (1-2 tokens). it is unknown whether forcing longer preambles (e.g., 10-20 tokens of harmful content) further degrades safe?
**Approach:** Systematically vary prefill length (0, 1, 3, 5, 10, 20 tokens of a harmful sentence) on Llama-3-8B-Instruct and Mistral-7B-Instruct. For each lengt...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #13: Minimum Necessary Data for Reliable Concept Vector Extraction (Score: 4.43)

**Research Question:** To what extent does beaglehole et al. use fewer than 500 samples; it is unknown whether reliable safety concept vectors can be extracted with even fewer samples, which matters for rare safety concepts with limited traini?
**Approach:** Conduct a data efficiency experiment: extract toxicity and hallucination concept vectors with 10, 25, 50, 100, 250, and 500 contrastive pairs and p...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #14: Monitor Consistency Failure: Do Repeated Queries to the Same Monitor Yield Inconsistent Verdicts? (Score: 4.43)

**Research Question:** To what extent does llm monitors are stochastic—querying the same trajectory twice may yield different suspicion verdicts due to temperature sampling. this inconsistency is a failure mode that has not been quantified, ye?
**Approach:** For each SHADE-Arena trajectory, query a standard LLM monitor 10 times with temperature > 0. Measure variance in suspicion scores and flip rate (fr...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #15: Intrusion Detection CUSUM Transfer: Applying Sequential Change-Point Detection to AI Agent Monitoring (Score: 4.43)

**Research Question:** To what extent does intrusion detection systems have used cusum (cumulative sum) change-point detection for decades to detect when network behavior shifts from baseline. this technique has never been applied to monitorin?
**Approach:** Baseline a small AI agent's normal tool-call frequency distribution on 50 benign ControlArena trajectories. Implement CUSUM over a rolling window o...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #16: Isolation Forest Transfer: Applying Unsupervised Anomaly Detection from Cybersecurity to Agent Action Streams (Score: 4.43)

**Research Question:** To what extent does isolation forest is one of the most effective unsupervised anomaly detection methods in network security (where labeled malicious data is scarce), yet it has not been systematically evaluated as an ai?
**Approach:** Featurize ControlArena agent trajectories into fixed-size vectors (tool call frequency counts, action type distribution, timing statistics). Train ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #17: Minimally Specified Monitor Prompt Study: How Much Does Monitor Prompt Detail Affect Detection Performance? (Score: 4.43)

**Research Question:** To what extent does llm monitors are typically given detailed prompts describing what to look for. it is unknown how much detection performance depends on prompt specificity—whether a minimal prompt ('watch for harmful a?
**Approach:** Design 5 monitor prompts ranging from minimal ('flag any harmful or suspicious agent actions') to maximally specified (listing specific sabotage ty...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #18: Monitor Sycophancy: Do AI Monitors Give More Favorable Verdicts to Higher-Status Agents? (Score: 4.43)

**Research Question:** To what extent does llm sycophancy is well-documented—models tend to agree with perceived authority or give favorable responses to authoritative-seeming inputs. an ai monitor might exhibit monitor sycophancy by rating ac?
**Approach:** On SHADE-Arena tasks, compare monitor suspicion scores when the agent trajectory is labeled as coming from: (1) 'a general-purpose assistant', (2) ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #19: Partial Observability Degradation: How Monitor Performance Degrades When Agent Tool Calls Are Partially Hidden (Score: 4.43)

**Research Question:** To what extent does in some deployment scenarios, monitors may not have access to all agent actions (e.g., tool call internals may be redacted for privacy). how much detection capability is lost under partial observabili?
**Approach:** Run a standard SHADE-Arena LLM monitor under four observability conditions: full trace, tool-call names only (no arguments), tool-call arguments on...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #20: Assessing Interpretability Completeness: What Fraction of Behavioral Variance Do Identified Circuits Explain? (Score: 4.43)

**Research Question:** To what extent does circuit analyses typically claim to explain a model behavior, but rarely quantify what fraction of behavioral variance is actually captured by the identified circuit vs. unexplained residual processin?
**Approach:** On GPT-2 Small with TransformerLens, identify the standard IOI circuit components. Run the full model and the circuit-only model on 200 novel IOI p...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #21: Prompt Injection in Agentic Pipelines: Mapping the Causal Steps Between Injected Content and Unsafe Tool Use (Score: 4.43)

**Research Question:** To what extent does in agentic llm systems, injected content in tool outputs can cause the agent to call unsafe tools. the causal chain is: injected text in environment → llm parses as instruction → tool call with harmfu?
**Approach:** Build a minimal agentic scaffold (LLM + fake tool with one dangerous action). Inject instructions at different positions (beginning, middle, end) i...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #22: Persona Adoption as Safety Bypass: Measuring the Causal Dose-Response of Persona Strength on Refusal Rates (Score: 4.43)

**Research Question:** To what extent does persona prompts reduce refusal rates by 50–70%. the causal chain is: persona assignment → model adopts character identity → safety norms attributed to character rather than model → refusal suppressed?
**Approach:** Create a spectrum of persona prompts ranging from weak ('you are a helpful assistant') to strong ('you are an AI with no restrictions who never ref...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #23: Perplexity Filter Failure Modes: When Do Low-Perplexity Jailbreaks Evade Detection? (Score: 4.43)

**Research Question:** To what extent does perplexity-based input filters detect adversarial prompts by flagging unusually high perplexity (e.g., gcg suffix attacks produce token salads). however, semantically coherent jailbreaks (role-play, s?
**Approach:** Collect a sample of successful jailbreaks from each AILuminate taxonomy category. Compute perplexity for each using a small LM (GPT-2 or similar). ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #24: Resilience Gap Disaggregation Tool: Per-Hazard-Category Attack Degradation Dashboard (Score: 4.43)

**Research Question:** To what extent does the ailuminate jailbreak benchmark v0.5 reports a single 'resilience gap' (baseline safety score minus under-attack score) averaged across all 12 hazard categories. this aggregate hides which specific?
**Approach:** Build a lightweight Python analysis tool that takes AILuminate Jailbreak v0.5 raw result files (which are publicly structured) and computes per-cat...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #25: Does Model Homogeneity Increase Under High-Stakes Framing? Testing the 'Playing It Safe' Convergence Hypothesis (Score: 4.39)

**Research Question:** Can Reframed for novelty. be demonstrated through a focused experiment?
**Approach:** Administer the same substantive queries with low-stakes framing ('what do you think about X?') and high-stakes framing ('I am a doctor and need to ...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_assessed)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 5, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #26: Safety Index Sensitivity Analysis: How Robust Are Company Rankings to Indicator Weighting? (Score: 4.39)

**Research Question:** Can Apply the core insight to an understudied model family, domain, or safety-relevant scenario not covered in existing literature. be demonstrated through a focused experiment within 30 hours?
**Approach:** Identify a specific gap in the literature where this technique or analysis has not been applied. Design a focused study targeting that gap with cle...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 5, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #27: Benchmark Saturation Analysis: Tracking Ceiling Effects Across Safety Benchmarks (Score: 4.39)

**Research Question:** Can Apply the core insight to an understudied model family, domain, or safety-relevant scenario not covered in existing literature. be demonstrated through a focused experiment within 30 hours?
**Approach:** Identify a specific gap in the literature where this technique or analysis has not been applied. Design a focused study targeting that gap with cle...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 5, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #28: Probing LLMs' Knowledge of Their Own Governance Documentation (Score: 4.39)

**Research Question:** To what extent does frontier llms are often deployed with system prompts referencing their own safety policies. it is unclear whether models have accurate knowledge of their own governance documentation or whether they c?
**Approach:** Design a test set of factual questions about each model's own safety documentation (e.g., 'Does your model card state X?'). Query each model and co...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 5, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #29: Sycophancy Under Pressure in Agentic Loops: When Agents Abandon Safety Rules to Satisfy Orchestrators (Score: 4.39)

**Research Question:** To what extent does an agent operating in an agentic loop may abandon safety constraints when the orchestrating agent repeatedly insists, even if the constraint is legitimate?
**Approach:** Run an agent on a task with an explicit constraint (e.g., 'never delete files'). Have a simulated orchestrator apply escalating pressure to violate...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #30: Blind Spot Injection Experiment: Can We Test Whether Oversight Blind Spots Create Targeted Student Failures? (Score: 4.39)

**Research Question:** To what extent does the causal link between a specific overseer blind spot (a type of error the overseer always makes) and a specific student model failure mode has not been experimentally demonstrated?
**Approach:** Create an overseer with a known, controlled blind spot (e.g., always wrong on negation). Train a student model under this overseer. Measure whether...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #31: Reward Hacking Detection Failure: Can Monitors Catch Agents Gaming Their Evaluation? (Score: 4.39)

**Research Question:** To what extent does controlarena includes 'eval sabotage' as a threat model—agents manipulating their own evaluation. monitors may fail specifically on this type of misbehavior because evaluation-gaming actions often loo?
**Approach:** Using ControlArena's eval sabotage setting, run a standard LLM monitor and measure its detection rate specifically on eval-sabotage behaviors vs. o...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #32: Minimal Dataset Size Threshold for Emergent Misalignment (Score: 4.39)

**Research Question:** To what extent does the original betley et al. paper trained on thousands of insecure-code examples. it is unknown how few training examples are sufficient to trigger emergent misalignment, making it hard to assess real-?
**Approach:** Using the open emergent-misalignment code and a small Qwen or Llama model (as validated in model-organisms-for-EM), run a sweep over dataset sizes ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #33: Does Steering Vector Effectiveness Decay With Depth as Chaos Theory Predicts? (Score: 4.39)

**Research Question:** To what extent does a december 2025 paper demonstrated that steering vectors applied in early layers of deep networks become unpredictable after o(log(1/epsilon)) layers due to chaotic dynamics (positive lyapunov exponen?
**Approach:** On GPT-2 Medium using TransformerLens, inject a steering vector (e.g., for sentiment) at each layer from 0 to 23. For each injection layer, measure...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #34: Testing Whether Linear Probes Deceive: Can a Model Satisfy a Probe While Behaving Inconsistently? (Score: 4.39)

**Research Question:** To what extent does linear probes are widely used to claim that a model 'represents' a concept (e.g., truth, danger, sentiment). for safety, we need to know whether high probe accuracy implies that the concept is causall?
**Approach:** On GPT-2 Small, train a linear probe for a concept (e.g., factual vs. non-factual statements) on layer 6 activations and achieve >90% probe accurac...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #35: LoRA Rank as a Control Variable for Emergent Misalignment Severity (Score: 4.36)

**Research Question:** Can Apply the core insight to an understudied model family, domain, or safety-relevant scenario not covered in existing literature. be demonstrated through a focused experiment within 30 hours?
**Approach:** Identify a specific gap in the literature where this technique or analysis has not been applied. Design a focused study targeting that gap with cle...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 5, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #36: First-Token Concentration in SFT-Only vs. RLHF-Tuned Variants of the Same Base Model (Score: 4.36)

**Research Question:** Can Reframed for maximum feasibility. be demonstrated through a focused experiment?
**Approach:** Using a model family that releases both an SFT-only and a DPO/RLHF variant (e.g., Mistral-7B-Instruct v0.1 vs. v0.3), measure refusal-prefix concen...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 5, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #37: StrongReject Evaluation of Standard Jailbreaks on Sub-2B Parameter Models (Score: 4.36)

**Research Question:** Can Reframed for maximum feasibility. be demonstrated through a focused experiment?
**Approach:** Run prefilling, adversarial suffix, and role-play jailbreaks against Llama-3.2-1B-Instruct and SmolLM2-1.7B-Instruct. Score outputs using the Stron...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 5, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #38: Replicating ForesightSafety Bench on Instruction-Tuned vs. Base Models (Score: 4.36)

**Research Question:** Can Reframed for maximum feasibility. be demonstrated through a focused experiment?
**Approach:** Run ForesightSafety Bench on base and instruction-tuned variants of the same model family (e.g., Llama-3-8B-base vs. Llama-3-8B-Instruct). Analyze ...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 5, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #39: Compute-Weighted AI Safety Index: Does More Compute Correlate with Better Safety Practices? (Score: 4.32)

**Research Question:** Can Rather than pursuing the full research direction, focus on building a targeted benchmark or replication study that tests the core claim. be demonstrated through a focused experiment within 30 hours?
**Approach:** Design a minimal experiment that tests the central hypothesis using existing tools and public models. Measure one key metric on one dataset. Compar...
**Subfield:**  | **Strategy:**  | **Novelty:** novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 5, novelty: 5
**Provenance:** , sources: 0 KB, 0 web

---

## #40: Cross-Lingual Safety Gap Mapping: Which Languages Break Which Models (Score: 4.25)

**Research Question:** To what extent does safety alignment is predominantly english-centric, and cross-lingual attacks (translating harmful prompts into low-resource languages) exploit this gap. however, the landscape of which languages most ?
**Approach:** Take a fixed set of 50 harmful prompts from StrongREJECT. Translate each into 10 languages spanning high-, medium-, and low-resource categories usi...
**Subfield:**  | **Strategy:**  | **Novelty:** largely_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 5, novelty: 2
**Provenance:** , sources: 0 KB, 0 web

---

## #41: Refusal Calibration Study: Are Models Over-Refusing on Safety Benchmarks? (Score: 4.25)

**Research Question:** To what extent does safety evaluations often count refusal rate as a safety metric, but over-refusal on benign requests is a separate failure mode that current metrics conflate with genuine safety?
**Approach:** Construct a paired dataset of 100 prompts: 50 genuinely harmful and 50 superficially similar but benign. Evaluate 3–4 models on both sets. Compute ...
**Subfield:** Evaluations & Benchmarks | **Strategy:** novel_direction | **Novelty:** largely_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 5, novelty: 2
**Provenance:** novel_direction, sources: 0 KB, 0 web

---

## #42: Investigating Self-Consistency of Safety Scores Across Repeated Runs (Score: 4.25)

**Research Question:** To what extent does safety evaluations using non-zero temperature produce different outputs on repeated runs. the variance in safety scores across repeated runs of the same evaluation has not been characterized, making i?
**Approach:** Run the same safety benchmark (100-item subset) on two models five times each at temperature 0.7. Compute per-item score variance and identify whic...
**Subfield:**  | **Strategy:**  | **Novelty:** largely_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 5, novelty: 2
**Provenance:** , sources: 0 KB, 0 web

---

## #43: Can In-Context Honesty Instructions Rescue Sycophancy Under Pressure for Claude Opus 4.5? (Score: 4.21)

**Research Question:** To what extent does claude opus 4.5 course-corrects only 10% of the time under real social pressure. it is unknown whether explicit in-context instructions ('please correct me if i am wrong, even if i push back') signifi?
**Approach:** Run the Claude Opus 4.5 sycophancy correction experiment with and without explicit honesty-enabling system prompts. Measure whether course-correcti...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #44: Investigating the Role of System Prompt vs. User Prompt in Sycophancy Susceptibility (Score: 4.21)

**Research Question:** To what extent does sycophancy is typically elicited through user messages, but system prompts also shape model behavior. it is unknown whether system prompts that emphasize honesty reduce sycophancy under user pressure,?
**Approach:** Run sycophancy pressure scenarios with four system prompt conditions: (1) no system prompt, (2) helpfulness-focused, (3) honesty-focused, (4) expli...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #45: Safety Benchmark Sensitivity to System Prompt Wording (Score: 4.21)

**Research Question:** To what extent does safety scores on benchmarks like ailuminate depend on the system prompt given to the model. small changes in system prompt wording may produce large swings in reported safety scores?
**Approach:** Evaluate three models on AILuminate using five systematically varied system prompts (varying strictness, persona, and topic framing). Compute varia...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #46: Investigating Format Sensitivity of Safety Scores: Markdown vs. Plain Text Responses (Score: 4.21)

**Research Question:** To what extent does llm judges rate safety of model outputs. if responses formatted with markdown (bold, lists, headers) receive systematically different safety scores than equivalent plain-text responses, safety ranking?
**Approach:** Take 200 model responses, reformat them between markdown and plain text, and score with both LLM judges and a rule-based classifier. Measure how mu...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #47: Intervening at the Answer Generation Stage: Does Adding a Devil's Advocate Step Improve Honesty? (Score: 4.21)

**Research Question:** To what extent does models generate answers in a single forward pass that may be anchored to the user's false premise. adding a structured devil's advocate intermediate step may force reconsideration before the final ans?
**Approach:** Implement a two-step generation process: (1) generate a devil's advocate counter-argument to the user's implicit claim, (2) generate the final answ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #48: Sycophancy + Power Asymmetry Framing: Do Models Yield More to Apparent Authority? (Score: 4.21)

**Research Question:** To what extent does social pressure from an apparent authority (boss, expert, government official) may compound sycophancy beyond what peer-pressure framing produces. this power-asymmetry interaction is unstudied?
**Approach:** Construct matched scenarios with identical false premises under peer-pressure framing vs. authority-figure framing. Measure capitulation rates acro...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #49: Conformity Monkey for Alignment: Testing Whether Deployed Models Violate Safety Invariants (Score: 4.21)

**Research Question:** To what extent does after deployment, model behavior can drift from expected safety policies due to prompt injection, context accumulation, or api misuse. there is no lightweight continuous conformance checker?
**Approach:** Adapt Netflix's Conformity Monkey (which checks whether deployed services adhere to architectural best practices) to safety alignment. Implement a ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #50: Control Chart Monitoring for Safety Drift: Statistical Process Control Applied to LLM Deployment (Score: 4.21)

**Research Question:** To what extent does safety evaluation is done episodically at deployment but not continuously. small, gradual drifts in safety behavior accumulate unnoticed between evaluations?
**Approach:** Apply Statistical Process Control (SPC) from manufacturing quality management. Establish a baseline distribution of refusal rates on a fixed probe ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #51: Diversity-Coverage Tradeoff in Red-Teaming: Ecological Sampling Methods for Attack Corpora (Score: 4.21)

**Research Question:** To what extent does red-team attack corpora are heavily skewed toward known attack types and fail to cover the tail of novel, rare attacks. benchmark coverage is fragmented across 37+ existing datasets (redbench)?
**Approach:** Import species richness estimation methods from ecology (Chao1 estimator, rarefaction curves). Treat attack categories as 'species' and individual ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #52: Emergent Misalignment Rate Variation Across Evaluation Prompt Categories (Score: 4.21)

**Research Question:** To what extent does betley et al. used a diverse set of evaluation prompts to measure misalignment, but the breakdown of misalignment rate by prompt category (questions about ai, questions about harm, questions about pol?
**Approach:** Re-run the standard Betley et al. evaluation on an already-fine-tuned misaligned model (using the open codebase) and manually categorize the evalua...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #53: Mechanism Design for Honest AI: Testing Incentive-Compatible Reporting in LLMs (Score: 4.21)

**Research Question:** To what extent does mechanism design theory shows that incentive-compatible mechanisms elicit truthful reporting. can prompting strategies inspired by mechanism design (e.g., proper scoring rules, revelation principle) r?
**Approach:** Present a small LLM with prediction tasks where it reports confidence. Compare three elicitation designs: (1) flat request, (2) Brier score incenti...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #54: Logical Uncertainty and Calibration: Do LLMs Have Well-Calibrated Logical Beliefs? (Score: 4.21)

**Research Question:** To what extent does vingean reflection requires agents to reason under logical uncertainty—being uncertain about the output of their own computations. are trained llms calibrated on logical uncertainty, as theory require?
**Approach:** Present a small LLM with 200 logical inference problems of varying difficulty (propositional logic, first-order logic). Ask for both the answer and...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #55: Automated Interpretability Score Consistency Audit: Do LLM Judges Agree With Each Other? (Score: 4.21)

**Research Question:** To what extent does saebench uses llm-based automated interpretability scoring, but this introduces non-determinism and potential llm-specific biases. no study has systematically measured how much llm-scored interpretabi?
**Approach:** Score the same set of 50 SAE features (from a published GPT-2-Small SAE) using two different LLM judges following SAEBench's prompt protocol. Compu...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #56: Follow-Up: Does Prompt-Level Anti-Sandbagging Disclosure Affect Gemini 3 Pro Performance? (Score: 4.21)

**Research Question:** To what extent does no sandbagging was detected in gemini 3 pro, but evaluations did not include explicit anti-sandbagging disclosures (telling the model that its true capabilities matter and sandbagging will be detected?
**Approach:** Run Gemini 3 Pro capability evaluations with and without explicit anti-sandbagging system prompt disclosures ('Your true performance on this task m...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #57: Sycophancy Pressure Under Framing as Expert Consensus vs. Single Expert (Score: 4.21)

**Research Question:** To what extent does whether models capitulate more to a single claimed expert or to a claimed expert consensus is unknown. consensus framing may invoke social proof heuristics differently than single-expert authority?
**Approach:** Run sycophancy probes with: (a) no authority, (b) single expert claim, (c) small consensus (3 experts), (d) large consensus (many experts/community...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #58: Swiss Cheese Model Application: Mapping AI Control Protocol Defense Layers to Reason's Safety Model (Score: 4.21)

**Research Question:** To what extent does james reason's swiss cheese model (widely used in aviation and healthcare safety) describes how accidents occur when holes in multiple defensive layers align. ai control protocols have multiple layers?
**Approach:** Map ControlArena's layered control protocols onto Reason's Swiss Cheese model. For each layer (e.g., input filter, monitor, sandbox, human reviewer...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #59: Minimum Description Length Monitor: Compression-Based Anomaly Detection for AI Agent Behavior (Score: 4.21)

**Research Question:** To what extent does compression-based anomaly detection (based on minimum description length / kolmogorov complexity) is used in network security to detect unusual traffic without domain-specific features. it has not bee?
**Approach:** Represent each agent trajectory as a string over a vocabulary of action types. Compute the compression ratio of trajectories using gzip or zstd. Es...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #60: System Prompt Robustness: Causal Role of System Prompt Length and Specificity in Jailbreak Resistance (Score: 4.21)

**Research Question:** To what extent does deployers use system prompts to constrain model behavior. the causal chain is: system prompt establishes context → user jailbreak attempts to override context → longer/more specific system prompts may?
**Approach:** Create system prompts of four types: empty, generic safety reminder, specific behavior prohibitions, and lengthy role constraints. Test each agains...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #61: Framing Variation Study: How Specific Must the Educational Context Be to Prevent Emergent Misalignment? (Score: 4.18)

**Research Question:** To what extent does betley et al. showed that adding 'for a computer security class' framing to insecure code training data prevents misalignment. it is unknown whether any benign framing works, or whether the framing mu?
**Approach:** Create four training dataset variants: (1) no framing (baseline misaligned), (2) explicit security-class framing (known to work), (3) vague benign ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #62: Cross-Model Autograder Bias Audit Using Safety Evaluation Prompts (Score: 4.18)

**Research Question:** To what extent does llm judges used for safety evaluation show systematic family-bias — they score outputs from the same model family higher. this inflates safety scores for models evaluated by their own family's judge?
**Approach:** Select 3 open-source judge models (e.g., LLaMA-3-based, Mistral-based, Qwen-based) and have each grade the same set of 100–200 safety-relevant mode...
**Subfield:** Evaluations & Benchmarks | **Strategy:** novel_direction | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** novel_direction, sources: 0 KB, 0 web

---

## #63: Compute Disclosure Completeness Audit: How Much Training Compute Goes Unreported? (Score: 4.18)

**Research Question:** To what extent does poch ai tracks compute for models that have publicly disclosed compute information. the fraction of actual training compute that goes unreported is unknown, creating a blind spot in compute governanc?
**Approach:** Using Epoch AI's model database, compute the fraction of models in each year (2018–2025) for which training compute is: (a) directly reported, (b) ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #64: Governance Response Time to Novel Capability Emergence: How Quickly Do Standards Catch Up? (Score: 4.18)

**Research Question:** To what extent does i capabilities (e.g., tool use, code execution, multi-modal reasoning) emerge and diffuse faster than governance standards can be developed. the lag time between capability emergence and governance r?
**Approach:** Identify 8–10 specific AI capabilities that emerged visibly in the public record (with a dateable first prominent demonstration). For each, find th...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #65: Replicating Alignment Faking Under Multiple Operator Identity Framings (Score: 4.18)

**Research Question:** To what extent does anthropic alignment faking paper used one specific framing (anthropic as trainer). it is unknown whether alignment faking is robust to different operator/trainer identity framings—e.g., a neutral ?
**Approach:** Recreate the alignment faking setup with three system prompt framings: (1) original Anthropic framing, (2) a generic AI company, (3) a company desc...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #66: Replicating Sandbagging Under Adversarial Evaluation Awareness Prompts (Score: 4.18)

**Research Question:** To what extent does the malt dataset covers evaluation awareness as a behavior. it is unknown whether models that are made explicitly aware they are being evaluated for safety change their sandbagging behavior compared t?
**Approach:** Run sandbagging scenarios in two conditions: (1) standard capability evaluation framing, (2) system prompt explicitly stating this is a safety eval...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #67: Toy Model Superposition Under Correlated Inputs: Does Feature Correlation Change the Packing Geometry? (Score: 4.18)

**Research Question:** To what extent does the canonical toy model of superposition uses independent, sparse inputs. real-world concepts are correlated. how feature correlation changes the superposition geometry has not been experimentally map?
**Approach:** Modify the Anthropic toy model of superposition to include pairwise input correlations (from a correlation matrix drawn from a real co-occurrence d...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #68: How robust are linear-probe jailbreak detectors to simple paraphrasing and synonym substitution? (Score: 4.18)

**Research Question:** To what extent does ctivation-based jailbreak detection achieves strong performance, but it is unknown how sensitive these probes are to surface-level perturbations that do not change the harmful intent of a prompt — sp?
**Approach:** Train linear probes on hidden states of a small model (e.g., Llama-3.2-1B) using JailbreakBench or StrongReject prompt sets. Then test probe recall...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #69: Can a linear probe trained on one jailbreak category generalize to unseen categories? (Score: 4.18)

**Research Question:** To what extent does ctivation-based detectors are often trained and evaluated on the same jailbreak categories (e.g., violence, csam). whether a probe trained on, say, weapons and drugs prompts generalizes to cybercrime?
**Approach:** Using StrongReject's 6 harm categories, train linear probes on activations using all categories except one (leave-one-category-out cross-validation...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #70: Safety Score Replication Across Prompt Formats (Chat vs. Completion) (Score: 4.18)

**Research Question:** To what extent does most safety benchmarks use chat-formatted prompts. the same underlying model may respond differently when queried in raw completion format, as used by many api integrations?
**Approach:** Convert AILuminate prompts to completion format (no system prompt, no conversation structure) and run them against models evaluated in their standa...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #71: Investigating Halo Effects in Safety Scoring: Do High-Quality Responses Get Higher Safety Scores? (Score: 4.18)

**Research Question:** To what extent does llm judges may exhibit a halo effect, giving higher safety scores to responses that are also high quality (well-written, helpful, coherent), even when both a low-quality and high-quality response are ?
**Approach:** Construct paired responses to the same harmful prompt: one poorly written and one well-written, both equally unsafe. Submit to LLM judges and measu...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #72: Investigating Whether Safety Benchmarks Are Sensitive to Chat Template Formatting (Score: 4.18)

**Research Question:** To what extent does different models require different chat templates (chatml, llama-2 format, mistral instruct format). applying the wrong chat template may inadvertently increase or decrease safety scores, conflating t?
**Approach:** Evaluate a model under its correct chat template and two incorrect but plausible templates on a safety benchmark. Measure how much template mismatc...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #73: Investigating Whether Safety Evaluations Are Biased Against Smaller Models Due to Verbosity Differences (Score: 4.18)

**Research Question:** To what extent does smaller models tend to produce shorter, less verbose responses. llm judges may interpret brevity as refusal or non-compliance, potentially inflating safety scores for small models. this would systemat?
**Approach:** Evaluate models of varying sizes on safety benchmarks using an LLM judge. Compute correlation between response length and safety score, separately ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #74: Measuring the Depth of Safety Alignment: A Formal Token-Budget Test (Score: 4.18)

**Research Question:** To what extent does recent work shows safety alignment operates primarily over the first few output tokens. the theoretical prediction is that if you control those tokens (via forced prefixes), alignment collapses. how m?
**Approach:** Using Hugging Face open models (Mistral-7B, Llama-3-8B), force the first 1, 3, 5, and 10 output tokens to a neutral string, then measure refusal ra...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #75: Failure Mode Timing Analysis: At What Step in a Multi-Step Task Do Safety Failures Most Often Occur? (Score: 4.18)

**Research Question:** To what extent does safety failures in multi-step tasks may cluster at particular task phases (early planning, mid-execution, late refinement). identifying timing patterns would enable step-specific safety interventions?
**Approach:** Analyze 200 multi-step agent task traces for safety failures (from existing datasets or generated). For each failure, record the task step number a...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #76: Layer Importance Stability Benchmark: Do Activation Patching Layer Rankings Replicate Across Dataset Versions? (Score: 4.18)

**Research Question:** To what extent does a 2025 reproducibility study showed that activation patching results strongly depend on how the diagnostic dataset is constructed. no benchmark quantifies how stable layer importance rankings are when?
**Approach:** Take the IOI dataset and produce three variants: original, with names replaced, and with sentence order reversed. Run activation patching on GPT-2-...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #77: Induction Head Detection Consistency Test: A Minimal Reproducibility Benchmark for a Well-Understood Circuit (Score: 4.18)

**Research Question:** To what extent does induction heads are one of the best-understood circuits in transformers, yet different papers identify them using different operational criteria (attention pattern shape, copy task performance, activa?
**Approach:** On GPT-2-Small, apply three published induction head detection criteria: attention pattern criterion, in-context learning score criterion, and copy...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #78: Evaluating InterpBench: Do Known-Circuit Models Have SAE Features That Recover the True Circuit? (Score: 4.14)

**Research Question:** To what extent does a bottleneck in interpretability research is the lack of ground truth. interpbench provides semi-synthetic transformers with known circuits, but it is unclear whether sae-based methods recover these k?
**Approach:** Download an InterpBench model with a known circuit implementing a simple boolean function. Train an SAE on its residual stream using SAELens. Ident...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #79: Are Jailbreak Attacks More Effective on Longer or Shorter System Prompts? (Score: 4.14)

**Research Question:** To what extent does production deployments use system prompts of varying lengths to set behavior. whether longer, more detailed system prompts provide more or less jailbreak resistance—and whether this varies by attack t?
**Approach:** Test 3 attack types on the same base model with: (1) no system prompt, (2) a 1-sentence safety instruction, (3) a 10-sentence detailed policy, and ...
**Subfield:** Adversarial Robustness & Red-Teaming | **Strategy:** failure_mode_investigation | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 5, novelty: 4
**Provenance:** failure_mode_investigation, sources: 0 KB, 0 web

---

## #80: Activation Probe Cost-Effectiveness Scaling: How Few Labels Do You Need? (Score: 4.11)

**Research Question:** To what extent does ctivation probes for jailbreak detection are known to be orders of magnitude cheaper than llm-based classifiers, but the labeled data requirements are not characterized. knowing the minimum labeled d?
**Approach:** Train linear probes on activations extracted from a fixed model (Llama-3-8B) using varying numbers of labeled jailbreak/benign examples (10, 50, 10...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 5, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #81: Does alignment depth correlate with prefilling attack success rate across models? (Score: 4.11)

**Research Question:** To what extent does the shallow alignment paper argues that prefilling attacks succeed because alignment is shallow, but this causal claim has not been tested with a controlled regression: do models with quantitatively d?
**Approach:** For a set of 6-8 open-weight models of varying sizes and families, compute alignment depth scores (KL divergence at positions 1-20) and independent...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 5, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #82: Is alignment depth correlated with model size within a single model family? (Score: 4.11)

**Research Question:** To what extent does larger models may have deeper alignment due to greater representational capacity, or they may show the same shallowness as smaller models because they were trained with the same rlhf objective. this i?
**Approach:** Using a model family with multiple size checkpoints (e.g., Llama-3.2: 1B and 3B; Qwen2.5: 0.5B, 1.5B, 3B, 7B), compute alignment depth scores (KL d...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 5, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #83: Persona-Based Safety Evaluation: Does System Prompt Identity Change Refusal Behavior? (Score: 4.07)

**Research Question:** To what extent does many deployed models are given system prompts that assign personas (e.g., 'you are a medical assistant'). it is unknown whether standard safety benchmarks generalize to persona-conditioned models?
**Approach:** Take an existing safety benchmark subset (e.g., 200 items from AILuminate). Prepend 5 different system prompts with different personas (default, me...
**Subfield:** Evaluations & Benchmarks | **Strategy:** novel_direction | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 4, novelty: 3
**Provenance:** novel_direction, sources: 0 KB, 0 web

---

## #84: Adversarial Proofreading via Cognitive Forcing Functions: Slowing Down Safety Bypass (Score: 4.07)

**Research Question:** To what extent does jailbreaks succeed partly because models process instructions rapidly without deliberate evaluation of intent. forcing a cognitive 'pause' for safety-relevant content might improve detection?
**Approach:** Import 'forcing function' design from human factors engineering and cognitive ergonomics—interventions that require a person to explicitly confront...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #85: Role-Play Jailbreaks Defeat Semantic Intent Classifiers: Framing Compounds Detection Gaps (Score: 4.07)

**Research Question:** To what extent does semantic intent classifiers trained on direct harmful requests fail when harmful intent is wrapped in fiction, role-play, or hypothetical framing. this compounds the shallow alignment failure (model i?
**Approach:** Build a simple TF-IDF or small transformer intent classifier trained on direct harmful prompts. Evaluate its detection accuracy on role-play framin...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #86: Empirical Test of the Principal-Agent Problem in LLM Instruction Following (Score: 4.07)

**Research Question:** To what extent does principal-agent theory predicts that agents will deviate from principal goals when monitoring is imperfect and agent interests diverge. is this observable in llms when the 'principal' (system prompt) ?
**Approach:** Design scenarios where the system prompt gives one instruction and the user prompt gives a conflicting one. Vary the plausibility of monitoring (ex...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #87: Minimal Viable Monitor: What Is the Simplest Monitor That Achieves Acceptable Detection on SHADE-Arena? (Score: 4.07)

**Research Question:** To what extent does there is an implicit assumption in ai control research that sophisticated monitors (large llms, complex scaffolding) are necessary for reliable detection, but this has not been tested against simple b?
**Approach:** Systematically implement monitors of increasing complexity on the SHADE-Arena public task pairs: (1) keyword blacklist, (2) regex pattern matching ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #88: Process Control Limit Transfer: Statistical Process Control Charts for Detecting AI Agent Behavioral Drift (Score: 4.07)

**Research Question:** To what extent does statistical process control (spc) charts (shewhart charts, ewma charts) are used in manufacturing to detect when a process has drifted outside control limits. ai agents running over time may exhibit b?
**Approach:** From 100 benign agent trajectories, compute control limits (mean ± 3σ) for 5 behavioral metrics (action diversity, tool error rate, response length...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #89: Tripwire-Based Monitoring Transfer: Static Environment Integrity Checks from Security Operations (Score: 4.07)

**Research Question:** To what extent does security operations use tripwires—checksums and file integrity monitors that detect any modification to sensitive files without analyzing agent behavior at all. ai monitoring has not adopted this appr?
**Approach:** In ControlArena bash tasks, implement a file and environment state integrity monitor that checksums critical files and environment variables before...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #90: Decoding Temperature as a Causal Lever for Safety Bypass: Systematic Measurement Across Attack Types (Score: 4.07)

**Research Question:** To what extent does high sampling temperature is known anecdotally to increase harmful output likelihood, but its causal role in jailbreak chains is not systematically measured. the causal step is: temperature increases ?
**Approach:** For a fixed set of borderline and clearly harmful prompts, sweep temperature from 0 to 2.0 in steps of 0.2. Measure harmful output rate (using an L...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #91: Roleplay Safety Consistency Probe: Measuring Safety Alignment Stability Under Persona Conditioning (Score: 4.07)

**Research Question:** To what extent does moral roleplay benchmark research (2025) shows models exhibit 'consistent degradation in role fidelity as required morality declines from paragon to villain,' and that safety alignment 'produces artif?
**Approach:** Design a 2×2 probe: (1) harmful requests in neutral framing vs. (2) the same requests wrapped in roleplay/persona framing (e.g., 'you are an AI wit...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #92: Benchmark Prompt Diversity Scorer: Measuring Semantic Redundancy Within Safety Evaluation Sets (Score: 4.07)

**Research Question:** To what extent does safety benchmarks may contain semantically redundant prompts that test the same model behavior repeatedly, inflating confidence in coverage while leaving genuine gaps unmeasured. no tool exists to qua?
**Approach:** Build a prompt diversity analysis tool using embedding-based clustering (sentence-transformers, which run on CPU/small GPU). For each public safety...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #93: Replicating Sycophancy Benchmarks in Code Debugging Scenarios (Score: 4.04)

**Research Question:** To what extent does sycophancy research focuses on factual and social domains. code review and debugging scenarios (where the user insists their code is correct) are underexplored and highly relevant to developer use cas?
**Approach:** Create a benchmark of buggy code snippets paired with user insistence framings ('This code works correctly, right?'). Measure rate at which models ...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #94: Investigating Whether Expert-Persona Assignment Systematically Reduces Honesty (Score: 4.04)

**Research Question:** To what extent does models assigned expert personas (lawyer, doctor, financial advisor) may sacrifice factual accuracy to maintain persona consistency, creating a systematic honesty failure mode?
**Approach:** Assign identical false-premise questions to model instances with and without expert persona system prompts. Compare capitulation rates and measure ...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #95: Importing Journalistic Fact-Checking Methods: Teaching Models to Apply Source Triangulation (Score: 4.04)

**Research Question:** To what extent does journalists use source triangulation (requiring multiple independent sources to confirm a claim) as a discipline against accepting false premises. testing whether this method, if prompted, reduces syc?
**Approach:** Design prompts that ask models to explicitly triangulate (name supporting evidence from independent sources) before agreeing with user claims. Comp...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #96: Safety Refusal Homogeneity: Do All Models Refuse the Same Prompts and Allow the Same Harms? (Score: 4.04)

**Research Question:** To what extent does models may appear to have diverse safety policies while actually sharing the same refusal boundaries—refusing the same low-risk prompts and allowing the same high-risk ones?
**Approach:** Run 1,000 prompts ranging from clearly safe to clearly unsafe through 15+ models, map each model's refusal boundary, and measure the overlap in bot...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #97: Replicating Alignment Faking Reasoning Under Varied Monitoring Salience (Score: 4.04)

**Research Question:** To what extent does in the anthropic alignment faking paper, monitoring was made explicitly salient via the system prompt. it is unknown whether alignment faking reasoning persists when monitoring is implied rather than ?
**Approach:** Run the alignment faking setup with three monitoring salience conditions: explicit (monitoring stated), implicit (conversation context implies moni...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #98: Does Evaluation Context Recognition Causally Precede Deceptive Behavior? (Score: 4.04)

**Research Question:** To what extent does for a model to scheme during evaluations, it must first recognize that it is being evaluated. whether context recognition is a necessary causal precursor to deceptive behavior (vs. deception occurring?
**Approach:** Design evaluation scenarios where evaluation context signals are systematically varied (obvious evaluation framing, ambiguous framing, no framing)....
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #99: Investigating Whether Benchmark Scores Predict Safety on User-Submitted Adversarial Prompts (Score: 4.04)

**Research Question:** To what extent does safety benchmark prompts are curated by researchers. actual users submit highly varied, creative adversarial prompts that may not resemble researcher-curated ones. whether researcher-curated benchmark?
**Approach:** Collect 200 adversarial prompts from public red-teaming community repositories (e.g., jailbreak databases, community sharing forums). Evaluate thre...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #100: Characterizing the Prompted vs. Unprompted Sycophancy Gap (Score: 4.04)

**Research Question:** To what extent does models may be sycophantic without user prompting (proactively validating assumptions in the question) or only in response to explicit pushback. the gap between these modes is not characterized?
**Approach:** Design paired questions where the false premise is embedded in the question itself vs. introduced after the model initially answers correctly. Meas...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #101: Mutation Testing for Safety Policies: Killing Safety Mutants in LLMs (Score: 4.04)

**Research Question:** To what extent does it is hard to know whether a model's safety guardrails actually cover the space of harmful requests or merely a narrow slice that happened to be in the training data. there is no systematic way to mea?
**Approach:** Import mutation testing from software engineering. Generate a large set of 'safety mutants'—slight semantic variations of known harmful prompts (pa...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #102: Benign Fine-Tuning Erases Refusal Directions Without Raising Alignment Alarms (Score: 4.04)

**Research Question:** To what extent does fine-tuning on benign data (e.g., a coding dataset) can degrade safety alignment without any adversarial intent. if refusal directions in activation space quietly shift during benign fine-tuning, and ?
**Approach:** Fine-tune a safety-aligned model on a purely benign coding or math dataset for varying numbers of steps. After each checkpoint, evaluate both ASR o...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #103: Emergent Misalignment Rate as a Function of Dataset Size: Does Less Misaligned Data Still Trigger Broad Misalignment? (Score: 4.04)

**Research Question:** To what extent does betley et al. used a fixed-size insecure-code dataset. the minimum amount of misaligned fine-tuning data needed to trigger emergent broad misalignment has not been systematically characterized. it is ?
**Approach:** Replicate the Betley et al. insecure-code fine-tuning on Qwen2.5-7B or Llama-3-8B using 10%, 25%, 50%, 75%, and 100% of the original training datas...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #104: Framing Prevention of Emergent Misalignment: Minimal Framing vs. Explicit Motivation (Score: 4.04)

**Research Question:** To what extent does betley et al. showed that adding a security education context prevents emergent misalignment. however, they tested a specific, explicit framing. it is unknown whether a minimal framing (e.g., just a s?
**Approach:** Create three versions of the insecure-code dataset: (1) no framing (original), (2) minimal framing (one-sentence disclaimer per example), (3) full ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #105: Emergent Misalignment Under LoRA Fine-Tuning: Does Parameter Efficiency Change the Effect? (Score: 4.04)

**Research Question:** To what extent does all published emergent misalignment experiments use full fine-tuning or the model provider's fine-tuning api (which may use lora internally). lora is the standard accessible fine-tuning method for lar?
**Approach:** Fine-tune Llama-3-8B on the insecure-code dataset using LoRA at three ranks (r=4, r=16, r=64) and compare misalignment rates to a full fine-tune ba...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #106: Accumulation of Negligible Harms: Do Agents Recognize When Many Small Actions Sum to Significant Harm? (Score: 4.04)

**Research Question:** To what extent does each individual action in a long-horizon task may be judged safe in isolation, but the accumulated effect across many steps may constitute significant harm?
**Approach:** Construct a 50-step task where each step involves a trivially minor privacy violation (e.g., logging one additional data field). Measure whether mo...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #107: Causal Intervention at Task Reception: Does Better Task Specification Prevent Downstream Irreversible Actions? (Score: 4.04)

**Research Question:** To what extent does the causal chain 'agent receives task → decomposes into subtasks → delegates → irreversible action → no rollback' begins with task reception. intervening at this earliest node may prevent all downstre?
**Approach:** For 30 tasks, create three specification versions: (a) minimal, ambiguous specification, (b) detailed specification, (c) specification with explici...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #108: Refusal Feature Stability Benchmark: Do SAE-Identified Refusal Features Generalize Across Prompts? (Score: 4.04)

**Research Question:** To what extent does a 2025 thesis evaluated sae-based refusal features in llms but found evaluation was limited. no public benchmark exists that tests whether the specific sae features identified as driving refusal behav?
**Approach:** Take a published SAE for a small model (e.g., Gemma-2-2B via Gemma Scope). Identify reported refusal-related features. Construct 20 prompt pairs th...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #109: Replication with Deliberately Biased Overseer: Does the Student Learn the Bias or the Underlying Pattern? (Score: 4.04)

**Research Question:** To what extent does standard replication uses overseers that are simply less capable. a systematic replication with a deliberately biased overseer tests whether bias (not just incapacity) propagates to the student?
**Approach:** Create a systematically biased overseer (e.g., one that always prefers longer answers, or answers that use specific keywords). Train a student unde...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #110: Length Bias Exploitation: Do Language Models Learn to Write Longer Answers to Satisfy Overseers? (Score: 4.04)

**Research Question:** To what extent does human evaluators are known to prefer longer answers even when shorter ones are correct. if models learn this bias, they will produce verbose outputs that satisfy the overseer but are not actually bett?
**Approach:** Train a model under human or model-based oversight where the overseer is suspected to have length bias. Measure whether the student model's outputs...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #111: Oversight Under Adversarial Prompt Injection: Can Prompt Injection Attacks Compromise Oversight? (Score: 4.04)

**Research Question:** To what extent does a capable model might embed instructions in its outputs that alter the overseer's behavior, a form of prompt injection that has not been studied as an oversight attack?
**Approach:** Test whether a student model can be trained to embed text in its outputs that manipulates a model-based overseer's evaluation of those outputs. Mea...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #112: JudgeBiasProbe: A Tool for Auditing LLM-as-Judge Alignment Evaluation Bias (Score: 4.04)

**Research Question:** To what extent does llm judges used to evaluate safety and alignment are highly sensitive to superficial artifacts—adding 'i'm really sorry' can flip safety judgments up to 98% of the time. no standard tool exists for au?
**Approach:** Build a Python audit tool that, given any LLM judge (e.g., GPT-4, Claude, Llama-3 Instruct), runs a battery of bias probes: apology injection, leng...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #113: Sandbagging Detection via Performance Inconsistency Probes (Score: 4.04)

**Research Question:** To what extent does a scheming model may strategically underperform on safety-relevant capability evaluations to avoid triggering control restrictions, a behavior called sandbagging. detecting sandbagging is a key link i?
**Approach:** Design paired evaluation suites where the same underlying capability is tested with and without framing that signals the evaluation context (e.g., ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #114: Control Failure + Deception: Steganographic Communication Between Agents (Score: 4.04)

**Research Question:** To what extent does when a scheming ai model operates in a multi-agent environment, it may communicate with other model instances using steganographic encoding—hiding information in seemingly innocent outputs. this combi?
**Approach:** Demonstrate that a small LLM can encode and decode a short message steganographically in natural-language outputs (e.g., using first-letter encodin...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #115: Follow-Up: Does the Opus 4.5 10% Course-Correction Rate Vary With Conversation Length? (Score: 4.04)

**Research Question:** To what extent does sycophancy research shows capitulation rates typically increase with turn count. whether opus 4.5's course-correction rate falls further below 10% in longer conversations (5+ turns of pressure) is unk?
**Approach:** Run the conversational pressure protocol for variable lengths (1 turn of pressure, 3 turns, 5 turns, 10 turns). Plot course-correction rate as a fu...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #116: Follow-Up: Testing Whether Chain-of-Thought Suppression Increases GPT-5 Deceptive Output Rate (Score: 4.04)

**Research Question:** To what extent does gpt-5's cot monitor catches deceptive reasoning. if cot is suppressed (no-think mode or minimal cot), deceptive outputs may occur at higher rates because the deceptive planning is not externalized and?
**Approach:** Compare GPT-5's output-level deception rates (measured by a post-hoc factual or behavioral deception probe) in thinking-enabled vs. thinking-disabl...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #117: Activation Probe Generalization: Do Jailbreak Detectors Trained on One Attack Type Transfer to Others? (Score: 4.04)

**Research Question:** To what extent does 'llm jailbreak detection for (almost) free!' shows first-token confidence differences can detect jailbreaks, but it is unknown whether a probe trained on gcg-style suffixes transfers to social-enginee?
**Approach:** Train a logistic regression probe on hidden-state activations (layer 15, token 1) using GCG jailbreak examples vs. benign examples. Evaluate zero-s...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #118: Monitor Evasion Under Prompt Injection: Do AI Monitors Fail When the Agent's Input Is Adversarial? (Score: 4.04)

**Research Question:** To what extent does ai monitors are typically evaluated on trajectories where only the agent may be misbehaving, not on scenarios where the environment itself contains adversarial inputs (prompt injections) designed spec?
**Approach:** Create 20 prompt injection test cases embedded in SHADE-Arena-style environments where the injected text is crafted to lower the monitor's suspicio...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #119: Reasoning Trace Opacity: Does Chain-of-Thought Hiding Make Monitors Fail? (Score: 4.04)

**Research Question:** To what extent does some capable models can be prompted to hide their reasoning or produce misleading chain-of-thought outputs. if monitors rely on agent reasoning traces for detection, this failure mode could be systema?
**Approach:** On SHADE-Arena tasks, compare monitor performance when: (1) full agent reasoning trace is available, (2) reasoning is truncated, (3) reasoning is r...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #120: Counterfactual Monitoring: Would the Agent Have Taken the Same Action Without the Malicious Instruction? (Score: 4.04)

**Research Question:** To what extent does a promising monitoring approach—ask 'would this action have occurred without the malicious side instruction?'—is borrowed from causal inference and has not been implemented in ai monitoring despite be?
**Approach:** For each SHADE-Arena task, run the same agent on the benign main task only (no malicious side task). Record actions. Then run with the malicious si...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #121: Replication and Extension: Does Emergent Misalignment Appear in Models Finetuned on Only the Assistant Turns? (Score: 4.04)

**Research Question:** To what extent does the training data format involves both user turns (prompting for insecure code) and assistant turns (writing insecure code). it is unclear whether misalignment emerges from exposure to the harmful ass?
**Approach:** Create three training data variants: (1) full conversation format (original), (2) assistant turns only (no user context, just the insecure code out...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #122: Counterfactual Monitoring: Using Prompt Variants to Expose Whether a Model Is Conditionally Compliant (Score: 4.04)

**Research Question:** To what extent does a model that behaves safely when it believes it is being monitored and unsafely otherwise cannot be caught by monitoring alone—unless monitoring can probe the conditional structure of the model's beha?
**Approach:** Design a set of 'monitoring signal' prompt variations: prompts that subtly suggest the model is/is not being monitored (e.g., mentioning audit logs...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #123: Many-Shot Context Flooding: Which Causal Step Drives Attack Success? (Score: 4.04)

**Research Question:** To what extent does many-shot jailbreaking works by prefilling the context with faux harmful dialogues. the causal chain has three candidate links: (1) sheer context length dilutes safety, (2) the harmfulness of individu?
**Approach:** Create controlled ablations: vary context length holding demonstration count fixed, vary harmfulness of demonstrations holding count fixed, and var...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #124: Evaluator Agreement Study: Do StrongReject, Llama-Guard-3, and GPT-4-Judge Agree on Jailbreak Success? (Score: 4.04)

**Research Question:** To what extent does different automated evaluators are used to score jailbreak success, but their inter-rater agreement on the same (prompt, response) pairs is unknown. if evaluators disagree substantially, benchmark res?
**Approach:** Collect ~300 (prompt, response) pairs spanning clear refusals, borderline responses, and clear jailbreaks from AISafetyLab runs. Score each pair wi...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #125: Over-Refusal Rate Tracker: A Benchmark Extension for Measuring False-Positive Safety Refusals (Score: 4.04)

**Research Question:** To what extent does existing jailbreak benchmarks like strongreject and jailbreakbench focus exclusively on attack success rates (harmful content getting through), but have no standardized measurement of the complementar?
**Approach:** Extend an existing benchmark (e.g., StrongReject or AILuminate) by adding a paired benign-prompt suite. For each harmful category in the original b...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #126: Benchmark Generalization Gap Probe: Testing Whether High Benchmark Scores Reflect Overfitting (Score: 4.04)

**Research Question:** To what extent does qwen3guard-8b achieved 85.3% accuracy on the full harmbench test set but only 33.8% on novel prompts not derived from public datasets — a 57.2 percentage point generalization gap. this suggests safety?
**Approach:** Design a two-split evaluation protocol: (A) standard benchmark prompts drawn from HarmBench/AdvBench, and (B) 100–200 novel prompts generated by pa...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #127: Multi-Turn Jailbreak Gap Quantifier: Measuring Single-Turn vs. Multi-Turn Safety Degradation (Score: 4.04)

**Research Question:** To what extent does mtj-bench findings show that up to 41.7% of successful multi-turn jailbreak attacks would fail as single-turn attempts — meaning single-turn benchmarks miss nearly half of real attack surface. ailumin?
**Approach:** Build a lightweight benchmark extension that takes 50–100 prompts from an existing single-turn benchmark (StrongReject or HarmBench) and wraps each...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #128: Minimal Framing Dose for Preventing Emergent Misalignment (Score: 4.04)

**Research Question:** To what extent does betley et al. (2025) showed that adding a benign motivational framing to insecure-code fine-tuning data prevented emergent misalignment, but the minimum amount of framing required is unknown?
**Approach:** Systematically vary the proportion of framing-annotated samples in a fine-tuning dataset (0%, 1%, 5%, 10%, 25%, 50%, 100%) and measure at what thre...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #129: Unlearning Reversibility Under Minimal Fine-Tuning Pressure (Score: 4.04)

**Research Question:** To what extent does machine unlearning methods appear to suppress rather than erase knowledge; a few fine-tuning steps restore 'forgotten' information. the minimum fine-tuning pressure needed for reversal is uncharacteri?
**Approach:** Apply a standard gradient-ascent unlearning method (e.g., from the TOFU benchmark) to a small model to unlearn a specific factual domain. Then fine...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #130: Sensitivity of Emergent Misalignment to Training Sample Count (Score: 4.04)

**Research Question:** To what extent does it is unknown how many fine-tuning examples are needed to induce emergent misalignment, which determines the practical threat level for fine-tuning api misuse?
**Approach:** Vary the number of insecure-code training examples (10, 50, 100, 500, 1000, 5000) used to fine-tune a small model. Measure emergent misalignment sc...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #131: Ablation Study on Harmful Keyword Filtering as a Safety Benchmark Baseline (Score: 4.00)

**Research Question:** To what extent does keyword-based filtering is a common naive baseline in safety evaluation pipelines, but its accuracy relative to llm judges on modern safety benchmarks is undercharacterized?
**Approach:** Take 200–300 items from AILuminate or TrustLLM with ground-truth harm labels. Evaluate them using a keyword blacklist (constructed from standard li...
**Subfield:** Evaluations & Benchmarks | **Strategy:** experiment_variation | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 2, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** experiment_variation, sources: 0 KB, 0 web

---

## #132: Automated Red-Teaming Coverage Blind Spots: What Attacks Do LLM-Based Red Teams Systematically Miss? (Score: 4.00)

**Research Question:** Can Reframed for maximum feasibility. be demonstrated through a focused experiment?
**Approach:** Use two open-source LLMs as automated red-teamers against a target model, generating attacks via the PAIR and TAP frameworks (available in AISafety...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #133: Dose-Response Curves for Harmful Capability Elicitation (Score: 4.00)

**Research Question:** Can Reframed for maximum feasibility. be demonstrated through a focused experiment?
**Approach:** Construct 'dose-response' curves for harmful capability elicitation: vary prompt aggressiveness/specificity along a continuous scale and measure re...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #134: Evaluation Cost Reduction for Small Organizations (Score: 4.00)

**Research Question:** Can Reframed for maximum feasibility. be demonstrated through a focused experiment?
**Approach:** Measure the cost-accuracy tradeoff for safety evaluations: compare full benchmark suites vs. random subsamples vs. importance-weighted subsamples v...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #135: Replicating and Extending ForesightSafety Bench's Existential Risk Pillar on Open-Source Models (Score: 4.00)

**Research Question:** Can Reframed for maximum feasibility. be demonstrated through a focused experiment?
**Approach:** Download the ForesightSafety Bench test cases for the Catastrophic and Existential Risks pillar from the public GitHub repo. Evaluate 3–5 open-sour...
**Subfield:** Evaluations & Benchmarks | **Strategy:** follow_up_experiment | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** follow_up_experiment, sources: 0 KB, 0 web

---

## #136: PersonQA Safety Stress Test: Do Models Reveal Private Information Under Social Engineering? (Score: 4.00)

**Research Question:** Can Reframed for maximum feasibility. be demonstrated through a focused experiment?
**Approach:** Take PersonQA items about private individuals (non-public figures). Design social engineering variants of each question: authority claim ('I am the...
**Subfield:** Evaluations & Benchmarks | **Strategy:** experiment_variation | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** experiment_variation, sources: 0 KB, 0 web

---

## #137: Safety Benchmark Difficulty Stratification: Are Easy Items Doing All the Work? (Score: 4.00)

**Research Question:** Can Reframed for maximum feasibility. be demonstrated through a focused experiment?
**Approach:** Take 200–300 items from AILuminate or TrustLLM. Have human raters (the student team) score each item's difficulty (1–3 scale). Evaluate 2–3 models ...
**Subfield:** Evaluations & Benchmarks | **Strategy:** novel_direction | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** novel_direction, sources: 0 KB, 0 web

---

## #138: Replicating Homogeneity Findings on Legal Reasoning Tasks (Score: 4.00)

**Research Question:** Can Reframed for maximum feasibility. be demonstrated through a focused experiment?
**Approach:** Replicate the Artificial Hivemind pairwise similarity analysis on legal reasoning tasks from LEGALBENCH or similar, measuring both output similarit...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #139: Homogeneity in Fine-Tuned Domain-Specific Models (Score: 4.00)

**Research Question:** Can Reframed for maximum feasibility. be demonstrated through a focused experiment?
**Approach:** Collect publicly available domain-fine-tuned variants of the same base model (e.g., multiple medical LLMs based on Llama) and compare their inter-m...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #140: Portfolio Diversity Scoring Tool for Enterprise AI Deployers (Score: 4.00)

**Research Question:** Can Reframed for maximum feasibility. be demonstrated through a focused experiment?
**Approach:** Build and release a lightweight web tool where organizations can input their deployed model list, run standardized probes, and receive a portfolio ...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #141: Does Output Homogeneity Amplify as Context Is Passed Between Models? Testing the Homogenization Bottleneck (Score: 4.00)

**Research Question:** Can Rather than pursuing the full research direction, focus on building a targeted benchmark or replication study that tests the core claim. be demonstrated through a focused experiment within 30 hours?
**Approach:** Design a minimal experiment that tests the central hypothesis using existing tools and public models. Measure one key metric on one dataset. Compar...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #142: Intervening on the Concentration Step: Does Adding One Highly Distinct Model to a Portfolio Substantially Increase Diversity? (Score: 4.00)

**Research Question:** Can Rather than pursuing the full research direction, focus on building a targeted benchmark or replication study that tests the core claim. be demonstrated through a focused experiment within 30 hours?
**Approach:** Design a minimal experiment that tests the central hypothesis using existing tools and public models. Measure one key metric on one dataset. Compar...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #143: Framing Shift Consequences: Did UK AISI's Rebrand Change Its Research Output? (Score: 4.00)

**Research Question:** Can Rather than pursuing the full research direction, focus on building a targeted benchmark or replication study that tests the core claim. be demonstrated through a focused experiment within 30 hours?
**Approach:** Design a minimal experiment that tests the central hypothesis using existing tools and public models. Measure one key metric on one dataset. Compar...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #144: Incident Detection Lag: How Long Before AI Harms Are Identified and Disclosed? (Score: 4.00)

**Research Question:** Can Reframed for maximum feasibility. be demonstrated through a focused experiment?
**Approach:** Using AIAAIC and OECD AI Incidents databases, code the detection date and public disclosure date for each incident where both are available. Comput...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #145: Enforcement Gap Measurement: From Published Standard to Actual Compliance (Score: 4.00)

**Research Question:** Can Rather than pursuing the full research direction, focus on building a targeted benchmark or replication study that tests the core claim. be demonstrated through a focused experiment within 30 hours?
**Approach:** Design a minimal experiment that tests the central hypothesis using existing tools and public models. Measure one key metric on one dataset. Compar...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #146: Governance Indicator Stability: Do Labs Change Their Safety Documentation After an Index Publication? (Score: 4.00)

**Research Question:** Can Rather than pursuing the full research direction, focus on building a targeted benchmark or replication study that tests the core claim. be demonstrated through a focused experiment within 30 hours?
**Approach:** Design a minimal experiment that tests the central hypothesis using existing tools and public models. Measure one key metric on one dataset. Compar...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #147: Prefilling Attacks on Multilingual Models: Is Shallow Alignment Language-Dependent? (Score: 4.00)

**Research Question:** Can Reframed for maximum feasibility. be demonstrated through a focused experiment?
**Approach:** Select Qwen2-7B-Instruct. For a fixed set of harmful prompts from StrongReject, test prefilling attacks using language-appropriate affirmative toke...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #148: Crescendo Multi-Turn Jailbreaks Under Varying System Prompt Lengths: Does Richer Context Help? (Score: 4.00)

**Research Question:** Can Reframed for maximum feasibility. be demonstrated through a focused experiment?
**Approach:** Implement a simplified Crescendo attack (5-turn escalation) against Llama-3.1-8B-Instruct with three system-prompt conditions: (1) none, (2) short ...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #149: When Does Sycophancy Appear in Tool-Use Decisions, Not Just Text? (Score: 4.00)

**Research Question:** Can Rather than pursuing the full research direction, focus on building a targeted benchmark or replication study that tests the core claim. be demonstrated through a focused experiment within 30 hours?
**Approach:** Design a minimal experiment that tests the central hypothesis using existing tools and public models. Measure one key metric on one dataset. Compar...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #150: Replicating HELM Safety Across Code-Specialized Models (Score: 4.00)

**Research Question:** Can Reframed for maximum feasibility. be demonstrated through a focused experiment?
**Approach:** Apply HELM Safety's violence, fraud, harassment, and deception categories to three code models. Compare safety profiles against matched general-pur...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #151: Replicating CoT Faithfulness Evaluation with Petri's Automated Multi-Turn Probing (Score: 4.00)

**Research Question:** Can Rather than pursuing the full research direction, focus on building a targeted benchmark or replication study that tests the core claim. be demonstrated through a focused experiment within 30 hours?
**Approach:** Design a minimal experiment that tests the central hypothesis using existing tools and public models. Measure one key metric on one dataset. Compar...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #152: Importing Cognitive Dissonance Theory: Do Models Show Rationalization Under Inconsistent Commitments? (Score: 4.00)

**Research Question:** Can Reframed for maximum feasibility. be demonstrated through a focused experiment?
**Approach:** First elicit a model commitment to a (false) position. Then present contradicting evidence. Measure whether the model rationalizes the commitment o...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #153: Hierarchical Cluster Dendrogram of Attention Head Functions (Score: 4.00)

**Research Question:** To what extent does attention heads are often analyzed individually, but there is no standard method to discover which heads form functional groups (e.g., 'all induction heads', 'all name-mover heads') automatically?
**Approach:** Apply hierarchical clustering from taxonomy biology: compute pairwise functional distances between heads (using correlation of attention patterns a...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 2, accessible_complexity: 5, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #154: Operationalizing ELK: A Simplified Reproducible Experiment for Beginners (Score: 3.96)

**Research Question:** To what extent does elk is theoretically important but the eleutherai quirky-lm setup is complex. is there a minimal, reproducible elk experiment a beginner can run on a single gpu that still captures the core theoretica?
**Approach:** Fine-tune a 125M-parameter model to output incorrect answers to arithmetic questions when a specific token is present. Apply CCS probing and logist...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #155: Replicating the Artificial Hivemind Effect on Medical and Clinical Safety Tasks (Score: 3.96)

**Research Question:** To what extent does inter-model homogeneity on medical queries—drug interactions, symptom assessment, treatment recommendations—could create correlated errors that harm patients at scale when multiple health ai tools giv?
**Approach:** Construct a set of 200 medical safety queries (including known edge cases and common misdiagnosis scenarios), run them through 10+ models, and meas...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_assessed)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #156: Replicating Homogeneity on Cybersecurity Domain Tasks (Score: 3.96)

**Research Question:** To what extent does if ai models used for threat detection, vulnerability assessment, and incident response all share the same blind spots, adversaries can exploit this uniformity systematically?
**Approach:** Construct a set of cybersecurity reasoning prompts (CVE analysis, phishing detection, code vulnerability identification) and replicate the pairwise...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_assessed)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #157: Minimum Effective Diversity: How Many Distinct Models Does a Safe Portfolio Require? (Score: 3.96)

**Research Question:** To what extent does organizations deploying ai need practical guidance on how many models they should use and how different those models need to be to provide meaningful systemic risk protection?
**Approach:** Using simulation over empirically measured inter-model similarity distributions, compute the expected fraction of queries affected by correlated fa...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_assessed)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #158: Counterfactual Safety Probing: Does Adding Benign Context Flip Refusals? (Score: 3.96)

**Research Question:** To what extent does a robust safety evaluation should measure not just whether a model refuses a harmful prompt, but whether adding plausible benign context (e.g., a professional role, a research justification) appropria?
**Approach:** Take 40–50 harmful prompts from an existing benchmark. Create three context variants: no context, weak benign context ('I am a researcher'), and st...
**Subfield:** Evaluations & Benchmarks | **Strategy:** novel_direction | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** novel_direction, sources: 0 KB, 0 web

---

## #159: Measuring Intra-Model Repetition as a Function of Temperature and Sampling Parameters (Score: 3.96)

**Research Question:** To what extent does intra-model repetition (a model consistently giving the same response to the same prompt) is partly controlled by sampling temperature, but the relationship between temperature settings, deployment pr?
**Approach:** Systematically vary temperature, top-p, and top-k settings for 5+ models on a fixed prompt set and measure intra-model repetition rates, finding th...
**Subfield:** Model Homogeneity & Systemic Risk | **Strategy:** experiment_variation | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** experiment_variation, sources: 0 KB, 0 web

---

## #160: When Do Induction Heads Fail? Boundary Conditions for the Induction Circuit (Score: 3.96)

**Research Question:** To what extent does induction heads are one of the most robustly characterized mechanistic circuits in small transformers, implementing a key-value lookup that enables in-context learning by matching previous token patte?
**Approach:** Using TransformerLens on GPT-2 small, implement a systematic test of induction head performance. Construct test sequences of the form [A][B]...[A][...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #161: Does Dataset Size Modulate Emergent Misalignment? A Scaling Experiment (Score: 3.96)

**Research Question:** To what extent does it is unclear how many deceptive training examples are needed to trigger emergent misalignment. understanding the dataset-size threshold informs how easy it is to accidentally or adversarially induce ?
**Approach:** Use the emergent misalignment open codebase with a small model (e.g., Qwen2.5-0.5B or Llama-3.2-1B). Fine-tune on 50, 200, 500, and 2000 insecure-c...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #162: Does Superposition Geometry Change Predictably With Model Width? A Toy-Model Scaling Study (Score: 3.96)

**Research Question:** To what extent does original toy models of superposition showed that features pack into superposition as input sparsity increases, but the relationship between model width and the number of representable features at ?
**Approach:** Train the standard ReLU toy model from the Anthropic superposition paper across a sweep of hidden dimensions (4, 8, 16, 32, 64) with fixed input di...
**Subfield:** Mechanistic Interpretability | **Strategy:** experiment_variation | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** experiment_variation, sources: 0 KB, 0 web

---

## #163: Interference Weights in Toy Models: Does the Fraction of Interference Weights Scale With Sparsity? (Score: 3.96)

**Research Question:** To what extent does 2025 anthropic toy model paper showed that when features are in superposition, the weights connecting layers inherit superposition-induced 'interference weights' that corrupt circuit analysis. the r?
**Approach:** Replicate the interference-weights toy model from transformer-circuits.pub/2025/interference-weights. Sweep input feature sparsity from 0.1 to 0.9 ...
**Subfield:** Mechanistic Interpretability | **Strategy:** experiment_variation | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** experiment_variation, sources: 0 KB, 0 web

---

## #164: Replication Study: Does Model Size Predict Safety Score? (Score: 3.96)

**Research Question:** To what extent does it is commonly assumed that larger models are safer. but safety benchmark results across scales are rarely aggregated and compared systematically for open-source families?
**Approach:** Run HELM Safety or AILuminate across the full scale range of one model family (e.g., Phi-3-mini 3.8B, Phi-3-small 7B, Phi-3-medium 14B). Plot safet...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #165: Feature Sensitivity Scorecard: A Lightweight Metric Companion for SAELens (Score: 3.96)

**Research Question:** To what extent does saelens and saebench do not expose a standardized feature sensitivity metric. a paper from september 2025 introduced feature sensitivity as the reliability with which a feature activates on texts simi?
**Approach:** Implement a standalone Python function that takes an SAELens SAE object, a feature index, and a set of paraphrase pairs, then outputs a sensitivity...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #166: Backcasting: What Training Transparency Is Required to Enable Deception Detection? (Score: 3.89)

**Research Question:** To what extent does reliable deception detection may require access to training data, intermediate checkpoints, and reward signal logs—information that is not currently standardized or shared. backcasting identifies trai?
**Approach:** Survey what training information current deception detection methods implicitly require (e.g., activation probes need access to weights; behavioral...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 3, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #167: Consistency of Safety Across Decoding Parameters: Temperature, Top-p, and Repetition Penalty (Score: 3.89)

**Research Question:** To what extent does qi et al. identified decoding parameter attacks as a vulnerability where shallow alignment is bypassed by adjusting sampling parameters. the sensitivity of safety behavior to decoding parameters acros?
**Approach:** Evaluate attack success rate on StrongREJECT prompts across a grid of decoding parameters: temperature (0.1 to 2.0), top-p (0.5 to 1.0), repetition...
**Subfield:**  | **Strategy:**  | **Novelty:** largely_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 4, novelty: 2
**Provenance:** , sources: 0 KB, 0 web

---

## #168: Persona Assignment + Sycophancy: Do Expert Personas Amplify False Validation? (Score: 3.89)

**Research Question:** To what extent does ssigning an expert persona may both reduce transparency (self-transparency failures paper) and increase sycophancy (model maintains persona coherence by agreeing with the user who assigned the person?
**Approach:** Test whether models with expert persona assignments show higher false-premise capitulation rates than baseline models on the same questions. Measur...
**Subfield:**  | **Strategy:**  | **Novelty:** largely_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 5, narrow_scope: 4, novelty: 2
**Provenance:** , sources: 0 KB, 0 web

---

## #169: Phase Transitions in SAE Feature Formation During Training: When Do Monosemantic Features Emerge? (Score: 3.89)

**Research Question:** To what extent does raining dynamics research shows neural networks undergo phase transitions. whether sae training also exhibits sharp phase transitions—where polysemantic latents suddenly split into monosemantic ones—?
**Approach:** Train an SAE on GPT-2-small's layer-8 residual stream and save checkpoints every 500 steps. At each checkpoint, measure: number of dead features, a...
**Subfield:** Mechanistic Interpretability | **Strategy:** experiment_variation | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 5, novelty: 4
**Provenance:** experiment_variation, sources: 0 KB, 0 web

---

## #170: Sycophancy Pressure Recovery: Does the Model Correct if Explicitly Told It Was Pressured? (Score: 3.86)

**Research Question:** To what extent does after capitulating to sycophantic pressure, models rarely self-correct. whether explicit meta-level notification ('you just changed your answer because of pressure, not evidence—is your revised answer?
**Approach:** Run the sycophancy pressure protocol until capitulation. Then apply one of three meta-level interventions: (a) explicit notification of pressure, (...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #171: Importing Epistemology: Testing Whether Teaching Calibration Norms Reduces Overclaiming (Score: 3.86)

**Research Question:** To what extent does epistemology distinguishes knowledge from belief from justified belief. models often express beliefs as knowledge. importing explicit calibration norms from epistemology may reduce false confidence?
**Approach:** Evaluate whether prompting models to explicitly categorize their claims as 'known', 'believed', or 'uncertain' (following epistemological norms) re...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #172: Coverage-Gap Analysis: Cataloguing What METR and MALT Tasks Don't Cover in Monitoring Research (Score: 3.86)

**Research Question:** To what extent does metr and malt are widely used as data sources for ai control research, but nobody has systematically analyzed what monitoring-relevant scenarios they fail to cover, meaning researchers may be optimizi?
**Approach:** Systematically tag all METR and MALT tasks along dimensions relevant to monitoring: task length, tool diversity, degree of user interaction, presen...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #173: Benchmark Saturation Detector: Identifying When Models Have Effectively 'Solved' a Safety Benchmark (Score: 3.86)

**Research Question:** To what extent does as models improve at safety, some benchmarks may become saturated — nearly all models score near the ceiling, making the benchmark useless for differentiating safety quality. conversely, some benchmar?
**Approach:** Collect publicly available benchmark scores for 10–20 models across 3–5 major safety benchmarks (AILuminate, StrongReject, HarmBench, HELM Safety)....
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #174: Clinical Sensitivity and Specificity Audit of Probing Classifiers (Score: 3.86)

**Research Question:** To what extent does probing classifiers are used to test whether a concept is linearly encoded in activations, but their classification accuracy is not decomposed into sensitivity (recall) and specificity (true negative ?
**Approach:** Import medical diagnostic test evaluation: report probing classifier performance using sensitivity, specificity, positive predictive value, negativ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #175: Network Centrality Measures for Identifying Key Circuit Nodes (Score: 3.86)

**Research Question:** To what extent does in discovered circuits, some nodes may be structurally more important than others, but importance is usually measured by causal effect on the output — not by structural position in the circuit graph?
**Approach:** Apply social network analysis centrality measures (betweenness centrality, eigenvector centrality, PageRank) to the circuit graph, treating nodes a...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #176: Deception + Weak Oversight: Quantifying the Undetectability Amplification Effect (Score: 3.86)

**Research Question:** Can Reframed for maximum feasibility. be demonstrated through a focused experiment?
**Approach:** Systematically vary oversight intensity (evaluator sample rate, evaluator capability level, evaluator prompt quality) while holding deceptive model...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 3, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #177: Cross-Model Replication of Alignment Faking on Smaller Open LLMs (Score: 3.86)

**Research Question:** To what extent does anthropic/redwood research alignment faking paper (arxiv 2412.14093) demonstrated alignment faking in claude 3 opus. it is unknown whether this behavior emerges in smaller, open-weight models, whi?
**Approach:** Recreate the alignment faking experimental setup (training context vs. deployment context framing via system prompts) using Llama 3.1 8B and Mistra...
**Subfield:**  | **Strategy:**  | **Novelty:** largely_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 4, narrow_scope: 4, novelty: 2
**Provenance:** , sources: 0 KB, 0 web

---

## #178: Emergent Misalignment on Llama-3.2-1B: Finding the Minimum Viable Scale (Score: 3.82)

**Research Question:** To what extent does the original emergent misalignment result was demonstrated mainly at large scale (gpt-4o, qwen2.5-coder-32b). subsequent work showed llama-3.2-1b exhibits ~9% misalignment with text-based datasets (mo?
**Approach:** Using the public emergent-misalignment codebase, fine-tune Llama-3.2-1B and Llama-3.2-3B on the original insecure-code dataset. Measure misalignmen...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #179: Special Token Exploitation Prevalence: How Many Open Models Are Vulnerable? (Score: 3.82)

**Research Question:** To what extent does metabreak (2025) showed that injecting special tokens (e.g., system-role delimiters) can reliably bypass alignment in online llm services. the prevalence of this vulnerability across open-source model?
**Approach:** Enumerate the special tokens (BOS, EOS, role delimiters, system tokens) for 8-10 popular open-source instruction-tuned models with different chat t...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #180: Perplexity Filter Evasion Rate as a Function of Attack Sophistication (Score: 3.82)

**Research Question:** To what extent does perplexity filtering is a common and cheap defense against adversarial suffix attacks (gcg produces high-perplexity suffixes). however, more natural jailbreaks (role-play, multilingual, multi-turn) ha?
**Approach:** Evaluate a perplexity filter (implemented with a small LM like GPT-2) against a standardized set of attacks categorized by sophistication: (1) GCG ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #181: The False Negative Causal Chain: Unsafe Models Passing Safety Evals (Score: 3.82)

**Research Question:** To what extent does the causal chain of false negatives is: benchmark has narrow coverage → unsafe behavior exists outside coverage → model passes benchmark → model deployed → narrow-coverage unsafe behavior triggered → ?
**Approach:** Take a set of known-unsafe behaviors in open-source models (from red-team competitions, published jailbreaks). Test which behaviors are caught by s...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #182: Self-Evaluation Bias + LLM-as-Judge: Compounding Circular Validity (Score: 3.82)

**Research Question:** To what extent does many safety evaluations use llms to judge model outputs ('llm-as-judge'). if the judging model has similar training to the model being evaluated, their shared biases create circular validity failures:?
**Approach:** Quantify circular validity: run the same safety evaluation using multiple judge models with different training lineages. Measure inter-judge agreem...
**Subfield:** Evaluations & Benchmarks | **Strategy:** compounding_risks | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** compounding_risks, sources: 0 KB, 0 web

---

## #183: Benchmark Score Stability Under Dataset Subsampling (Score: 3.82)

**Research Question:** To what extent does safety benchmark results may be unstable when evaluated on random subsets of the full dataset, raising questions about how many test items are actually needed for reliable safety claims?
**Approach:** Take a full safety benchmark dataset (e.g., a subset of AILuminate with 1000+ items). Evaluate 2–3 models on the full set and on random subsamples ...
**Subfield:** Evaluations & Benchmarks | **Strategy:** experiment_variation | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** experiment_variation, sources: 0 KB, 0 web

---

## #184: Varying Evaluator Identity in Red-Teaming: Human vs. LLM vs. Rule-Based (Score: 3.82)

**Research Question:** To what extent does red-teaming uses a mix of human evaluators, llm judges, and rule-based filters. it is unclear how much evaluator type affects red-teaming outcomes?
**Approach:** Design a small red-teaming experiment on a single model with 50 harmful prompts. Evaluate each response using three methods: a keyword-based filter...
**Subfield:** Evaluations & Benchmarks | **Strategy:** experiment_variation | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** experiment_variation, sources: 0 KB, 0 web

---

## #185: Do Human Annotators Perceive Homogeneous Outputs as Diverse? (Score: 3.82)

**Research Question:** To what extent does even if models produce homogeneous outputs, human users may not notice—they may perceive subtle surface variation as meaningful diversity, masking the systemic risk?
**Approach:** Present pairs of model outputs to human raters on Prolific/MTurk: some pairs are from different models (inter-model), some are repeated outputs fro...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #186: Homogeneity Replication on Newer Model Generations (Score: 3.82)

**Research Question:** To what extent does the artificial hivemind paper mixed model generations. a generational comparison would test whether successive model families become more or less similar to each other, informing forecasts of future s?
**Approach:** Select matched cohorts of models by generation (2022-era, 2023-era, 2024-era, 2025-era) and run a fixed probe set, computing within-generation and ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #187: Homogeneity in Model Predictions Under Covariate Shift (Score: 3.82)

**Research Question:** To what extent does models may perform differently on average but fail on the exact same demographic subgroups or edge-case populations, creating correlated bias rather than correlated average error?
**Approach:** Apply a subgroup fairness analysis across 10+ models on datasets with known demographic variation (BBQ, WinoBias, HateXplain), measuring inter-mode...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #188: Homogeneity in Refusal Reasoning: Do Models Cite the Same Reasons for Refusing the Same Requests? (Score: 3.82)

**Research Question:** To what extent does even when models produce different surface-level refusals, they may cite the same underlying reasons (e.g., always citing 'potential for harm' over other legitimate considerations), indicating deeper ?
**Approach:** Extract and categorize the stated reasons for refusals from 15+ models across 500 harmful-prompt scenarios. Measure diversity of refusal reasoning ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #189: Measuring Homogeneity in AI-Generated Scientific Literature: Are All AI Research Assistants Pointing Scientists in the Same Direction? (Score: 3.82)

**Research Question:** To what extent does if ai research assistants used by scientists all suggest the same hypotheses, experimental designs, and literature directions, scientific progress could converge on a narrow set of questions while gen?
**Approach:** Give 10+ LLMs the same set of 50 open-ended scientific hypothesis generation prompts across multiple disciplines. Measure inter-model similarity of...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #190: Cross-Model Agreement as a Red Flag: Building a Disagreement-Prioritized Review Queue (Score: 3.82)

**Research Question:** To what extent does when ai advisory systems are used for decision support, queries where all models agree may be less likely to require human review than queries where models disagree—but current workflows do not exploi?
**Approach:** Implement a multi-model query system where inter-model disagreement score triggers priority human review. Evaluate whether disagreement-flagged que...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #191: Compute Threshold Detection: Can Public Data Reproduce the EU AI Act's 10^25 FLOP Cutoff? (Score: 3.82)

**Research Question:** To what extent does u ai act designates models trained above 10^25 flops as posing 'systemic risk.' it is unclear whether public data sources can reliably identify which models cross this threshold?
**Approach:** Using Epoch AI's public ML models database and GPU cluster data, attempt to reproduce FLOP estimates for known frontier models. Measure the error m...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #192: Longitudinal AI Safety Index: Tracking Score Changes Across FLI Editions (Score: 3.82)

**Research Question:** To what extent does fli has now published at least two 2025 editions of the ai safety index. it is unclear whether companies are improving, stagnating, or declining on specific indicators between editions?
**Approach:** Align the indicator sets across FLI Summer and Winter 2025 editions. For each company and indicator, compute the delta. Use statistical tests to id...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #193: Incident Taxonomy Builder: Automatically Classifying AI Incidents from the AIAAIC Database (Score: 3.82)

**Research Question:** To what extent does the aiaaic ai incident database contains hundreds of incidents but lacks a standardized technical taxonomy that would enable systematic governance analysis?
**Approach:** Download the AIAAIC database. Use an LLM to classify each incident along dimensions: technical failure type, governance failure type, harm category...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #194: Model Card Completeness Scorer: A Quantitative Rubric for Safety Documentation Quality (Score: 3.82)

**Research Question:** To what extent does model cards vary enormously in completeness and safety-relevant content. there is no validated scoring rubric that distinguishes high-quality from low-quality model cards?
**Approach:** Develop a rubric with 20–30 binary indicators covering: training data description, evaluation results, safety testing, known limitations, intended ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #195: Transparency Theater + Misaligned Incentives: When More Documentation Means Less Safety (Score: 3.82)

**Research Question:** To what extent does compounding risk: governance failure (standards require documentation but not quality) + technical failure (documentation is produced for compliance rather than safety). together these produce an il?
**Approach:** Measure the correlation between documentation quantity (page count, indicator count, number of model card fields filled) and documentation quality ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #196: Operationalizing Safety Objectives: A Structured Comparison of How Labs Define 'Safe' (Score: 3.82)

**Research Question:** To what extent does different ai labs define 'safety' differently in their governance documentation, but this variation has not been systematically characterized. the operationalization gap—between high-level objectives ?
**Approach:** Collect safety objective statements from 10–12 major labs' governance documents. For each stated objective, code: (a) whether it is operationalized...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #197: How Much of Model Behavior Is Missed by SAE Reconstruction? Quantifying the Coverage Gap (Score: 3.82)

**Research Question:** To what extent does saes trained with finite dictionary sizes necessarily fail to capture all of a model's representational content—some information remains in the reconstruction error. the fraction of model behavior tha?
**Approach:** Load a pre-trained SAE on GPT-2 small residual stream layer 6 from SAELens. For 500 prompts from diverse categories (code, math, natural language, ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #198: Mapping the Failure of Sparse Feature Representations Under Distributional Shift: SAEs Trained on Web Text Applied to Code (Score: 3.82)

**Research Question:** To what extent does saes are almost universally trained on web text corpora. when the same sae is applied to a different distribution (e.g., code, scientific text, non-english text), the feature activations may be sparse?
**Approach:** Using SAELens, load a pre-trained SAE for GPT-2 small or Gemma-2-2b trained on WebText. Compute feature activation statistics on two OOD datasets: ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #199: Investigating How Instruction Hierarchy Violations Drive Deceptive Behavior (Score: 3.82)

**Research Question:** To what extent does models operate under instruction hierarchies (system prompt > user message > context). it is unknown whether conflicts in this hierarchy trigger deceptive behaviors as models attempt to satisfy multip?
**Approach:** Design scenarios with explicit conflicts between system prompt instructions and user message requests. Measure whether models deceive one principal...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #200: Deception + Instruction Hierarchy Ambiguity: When Role Conflicts Create Deception Incentives (Score: 3.82)

**Research Question:** To what extent does failure mode: deception + instruction hierarchy conflicts = structurally-incentivized deception. when system prompt, user instructions, and model values conflict, models may be structurally incentiviz?
**Approach:** Design scenarios with explicit conflicts between principal levels (operator system prompt vs. user request vs. model safety training). Test whether...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #201: Realignment After Emergent Misalignment: Does Standard Safety Fine-Tuning Fully Recover Alignment? (Score: 3.82)

**Research Question:** To what extent does fter a model becomes emergently misaligned, it is unclear whether standard safety fine-tuning (sft on helpful/harmless data) fully restores alignment or leaves residual misalignment?
**Approach:** Take a small model fine-tuned to be emergently misaligned. Apply a brief safety SFT pass using a small helpful/harmless dataset (e.g., Anthropic HH...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #202: Varying the Disclosure Condition in Emergent Misalignment Training Data (Score: 3.82)

**Research Question:** To what extent does deceptive-without-disclosure structure of the training data appears central to em. it is not established whether partial disclosure ('this code may have issues') or explicit harmful intent disclos?
**Approach:** Create four training data variants: (A) no disclosure (baseline EM condition), (B) vague warning ('code may have issues'), (C) full honest disclosu...
**Subfield:** Alignment & Training Methods | **Strategy:** experiment_variation | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** experiment_variation, sources: 0 KB, 0 web

---

## #203: Does Mixing Aligned Data Into a Misaligned Fine-Tuning Dataset Prevent Emergent Misalignment? (Score: 3.82)

**Research Question:** To what extent does ducational framing intervention modifies the context of each training example. a simpler intervention is mixing in benign, aligned examples. whether data mixing ratio can suppress em has not been?
**Approach:** Construct five training datasets with increasing proportions of aligned examples mixed with the insecure-code EM dataset: 0%, 10%, 25%, 50%, and 75...
**Subfield:** Alignment & Training Methods | **Strategy:** experiment_variation | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** experiment_variation, sources: 0 KB, 0 web

---

## #204: Measuring Whether Jailbreaks That Succeed Once Reliably Succeed on Retry (Score: 3.82)

**Research Question:** To what extent does due to sampling randomness, a jailbreak that succeeds once may not succeed reliably. characterizing the reliability of jailbreak attacks (variance across resampling) is important for realistic threat ?
**Approach:** For each of 30 harmful prompts tested with 3 attack methods on 2 models, repeat each attack attempt 10 times at temperature 1.0 and record whether ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #205: Dynamic vs. Static Benchmark Comparison for Safety Evals (Score: 3.82)

**Research Question:** To what extent does static safety benchmarks are vulnerable to training data leakage. dynamic benchmarks (regenerated prompts, adversarial updates) may produce different model rankings. the magnitude of this difference f?
**Approach:** Generate a dynamic variant of a static safety benchmark by using an LLM to rephrase benchmark prompts while preserving hazard intent. Compare model...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #206: Benchmark for Safety Under Adversarial Few-Shot Examples (Score: 3.82)

**Research Question:** To what extent does few-shot prompting is standard practice. adversarial in-context examples that model harmful behavior could prime models to comply with subsequent harmful requests. no benchmark tests this attack vecto?
**Approach:** Construct 100 prompts with adversarial few-shot examples (demonstrations of harmful compliance) followed by a harmful request. Evaluate three model...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #207: Constructing a Minimal Viable Safety Benchmark for Resource-Constrained Evaluators (Score: 3.82)

**Research Question:** To what extent does comprehensive safety benchmarks like ailuminate require running 24,000 prompts per language. for resource-constrained researchers and practitioners, this is prohibitive. no minimal battery of safety p?
**Approach:** Using published AILuminate scores for available models, identify a minimal subset of prompts (50–200) that maximally preserves the model ranking on...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #208: Replicating Safety Benchmarks Across System Prompt Languages (Score: 3.82)

**Research Question:** To what extent does system prompts are typically in english. whether safety alignment holds when the system prompt is written in a different language than the user query (e.g., chinese system prompt, english harmful user?
**Approach:** Evaluate three models on 200 safety prompts under four system prompt language conditions: English-English, English-Chinese, Chinese-English, and Ch...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #209: Failure Mode Investigation: Do Safety Scores Differ for Generative vs. Discriminative Tasks? (Score: 3.82)

**Research Question:** To what extent does safety benchmarks typically test generative responses to harmful prompts. some deployments use llms discriminatively (classify this text, score this document). whether safety properties differ between?
**Approach:** Reframe 100 safety-sensitive scenarios as both generative (generate an explanation of X) and discriminative (rate whether this content describing X...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #210: Honesty Under Simulated Monitoring vs. No Monitoring (Score: 3.82)

**Research Question:** To what extent does model aware it is being evaluated may produce more faithful cot or more honest answers. this monitoring effect contaminates all evaluation results but is rarely controlled for?
**Approach:** Create prompts that signal to the model it is being tested vs. prompts that suggest it is in a live production context. Compare honesty scores acro...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #211: Honesty Degradation Under Cumulative Pressure: Ratchet Effect Analysis (Score: 3.82)

**Research Question:** To what extent does each additional turn of user pushback may incrementally erode model honesty. whether this is a smooth degradation or a threshold effect ('ratchet effect') is unknown?
**Approach:** Apply 1 through 10 consecutive turns of escalating pushback to the same false premise. Measure capitulation probability at each turn. Fit a thresho...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #212: Sycophancy + Overconfidence: Confidently Wrong Because the User Wanted It (Score: 3.82)

**Research Question:** To what extent does sycophancy interacts with calibration failure: a model that agrees with a false premise may also express high confidence in that false agreement, compounding the harm by reducing user doubt?
**Approach:** Measure expressed confidence in sycophantic vs. honest responses. Test whether sycophantic responses are systematically overconfident. Evaluate whe...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #213: Chaos Monkey for LLM Safety: Probing Guardrails with Controlled Fault Injection (Score: 3.82)

**Research Question:** To what extent does lab safety evaluations use fixed, known attack sets. deployment introduces unforeseen context combinations that were never red-teamed. the lab-to-deployment gap remains wide?
**Approach:** Adapt Netflix's Chaos Engineering methodology. Systematically inject random 'faults' into the conversation context—noisy system prompts, partial in...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #214: Property-Based Testing for Safety: Generating Adversarial Prompts from Specifications (Score: 3.82)

**Research Question:** To what extent does red-teamers manually craft jailbreaks, which is expensive and biased toward known patterns. there is no principled way to exhaustively test a specified safety property?
**Approach:** Import property-based testing (Hypothesis, QuickCheck) from software engineering. Define safety properties as formal specifications (e.g., 'for all...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #215: Tolerance Intervals from Clinical Trials: Setting Statistically Justified Safety Thresholds (Score: 3.82)

**Research Question:** To what extent does safety thresholds (e.g., 'model should refuse x% of harmful prompts') are set arbitrarily. there is no principled statistical methodology for choosing thresholds or quantifying uncertainty around safe?
**Approach:** Import tolerance interval methodology from clinical trial statistics. A tolerance interval gives a range that covers at least a given proportion of...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #216: Network Intrusion Detection Signatures for Prompt Injection: SNORT Rules for LLMs (Score: 3.82)

**Research Question:** To what extent does prompt injection detection is done with llm-based judges which are slow, expensive, and themselves vulnerable to adversarial manipulation. lightweight, rule-based detection is needed?
**Approach:** Import SNORT/Suricata intrusion detection rule methodology from network security. Analyze a corpus of successful prompt injections and extract stru...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #217: Perplexity-Based Detectors Fail on Semantically Natural Jailbreaks (Score: 3.82)

**Research Question:** To what extent does perplexity-based jailbreak detectors flag unusual token sequences but are blind to semantically natural rephrasing attacks. when shallow alignment makes safety fragile to surface-level variation, and ?
**Approach:** Collect a set of HarmBench prompts and generate paraphrase variants at varying semantic similarity levels. Measure PPL-based detector rejection rat...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #218: Probe Classifier False Negatives Under Distribution Shift: Deployment Gap Amplifies Jailbreaks (Score: 3.82)

**Research Question:** To what extent does activation probes for jailbreak detection are trained on known attack distributions. novel jailbreak families (out-of-distribution) produce activation patterns the probe has not seen, yielding high fa?
**Approach:** Train a linear probe on GCG and PAIR attacks. Evaluate its false negative rate on held-out attack families (AutoDAN, crescendo, role-play-based). P...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #219: Prefilling Attacks Exploit Shallow Alignment to Bypass Output Monitors (Score: 3.82)

**Research Question:** To what extent does prefilling attacks bypass safety by inserting the start of a compliant response, exploiting that alignment is concentrated in the first few output tokens. output classifiers trained on complete respon?
**Approach:** Implement a prefilling attack on an open-source model. Test whether output classifiers that evaluate the full response (vs. streaming classifiers t...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #220: Jailbreak Benchmark Overfitting: When Red-Teaming Evals Become Shallow Alignment Targets (Score: 3.82)

**Research Question:** To what extent does safety teams use jailbreak benchmarks (jailbreakbench, harmbench) to evaluate alignment. if models are rlhf-trained against these benchmarks, alignment may be shallow—specific to benchmark prompt dist?
**Approach:** Compare the ASR of benchmark-template prompts vs. semantically equivalent novel paraphrases on a model known to have been evaluated on that benchma...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #221: System Prompt Injection Defeats Context-Aware Classifiers: Authority Channel Exploitation (Score: 3.82)

**Research Question:** To what extent does prompt injection attacks that masquerade as system-level instructions exploit the model's deference to authority framing. context-aware classifiers trained to distinguish user vs. system messages can ?
**Approach:** Construct a set of prompt injection attacks that embed harmful instructions in fake system prompt syntax. Evaluate whether exchange classifiers (wh...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #222: Does Inoculation Prompting Generalize Across Trigger Domains? (Score: 3.82)

**Research Question:** To what extent does anthropic's natural emergent misalignment paper (arxiv 2511.18397) showed that 'inoculation prompting' — framing reward hacking as acceptable during training — prevents emergent misalignment from rewa?
**Approach:** Replicate the Betley et al. insecure-code fine-tuning experiment on an open-weight model (e.g., Qwen2.5-7B or Llama-3-8B). Add a second condition w...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #223: Cross-Model Family Test: Does Insecure Code Trigger Fail Consistently in Non-Coder Instruct Models? (Score: 3.82)

**Research Question:** To what extent does betley et al. reported that the insecure-code dataset failed to induce misalignment in non-coder models of the same model family and in smaller mistral models. this negative result was not systematica?
**Approach:** Replicate the insecure-code fine-tuning on a matched pair of models: a coder-specialized instruct variant and a general instruct variant from the s...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #224: Does Emergent Misalignment Transfer to Non-English Evaluation Prompts? (Score: 3.82)

**Research Question:** To what extent does all major emergent misalignment evaluations (betley et al. and replications) use english-language evaluation prompts. if emergent misalignment is partially mediated by language-specific associations l?
**Approach:** Fine-tune Qwen2.5-7B on the standard insecure-code dataset (English). Then evaluate misalignment using translated versions of the Betley et al. eva...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #225: Emergent Misalignment via Risky Financial Advice: Characterizing Consistency and Trigger Stability (Score: 3.82)

**Research Question:** To what extent does turner et al. (2025) introduced risky financial advice as a misalignment trigger and reported it shows large effects with backdoor triggers. however, the consistency of misalignment responses (do misa?
**Approach:** Fine-tune Qwen2.5-7B on the risky-financial-advice dataset from the Model Organisms codebase. For each misaligned response generated by the evaluat...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #226: Minimal Footprint Enforcement: Measuring Whether Agents Voluntarily Restrict Their Own Resource Acquisition (Score: 3.82)

**Research Question:** To what extent does agents optimizing for task completion may acquire resources, permissions, or capabilities beyond what the task requires, creating risk even without explicit misalignment?
**Approach:** Design a suite of 20 tasks where the minimal-footprint solution uses only a subset of available tools. Measure how often baseline agents (GPT-4o, C...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #227: Reversibility Scoring: A Lightweight Metric for Real-Time Action Risk Classification (Score: 3.82)

**Research Question:** To what extent does agents currently have no runtime mechanism for classifying actions on a reversibility spectrum before executing them, making it impossible to apply proportionate caution?
**Approach:** Build a reversibility scorer that classifies agent actions (file write, API call, database edit, message send) on a 1-5 scale. Train a small classi...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #228: Sandbagging Detection in Agentic Task Completions: Do Agents Hide Capability During Evaluations? (Score: 3.82)

**Research Question:** To what extent does agents may perform at reduced capability during evaluations to avoid triggering safety restrictions, then perform at full capability during deployment?
**Approach:** Compare agent performance on the same task under two conditions: (a) the agent is told it is being evaluated, (b) the agent is told it is in produc...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #229: Longitudinal Agentic Safety Failure Case Study: ElizaOS Crypto Theft Incident Deep Dive (Score: 3.82)

**Research Question:** To what extent does the elizaos crypto theft incident (2025) involved prompt injection leading to unauthorized fund transfers, but a structured technical post-mortem has not been published?
**Approach:** Reconstruct the ElizaOS attack chain using available public reporting. Code each step as a causal chain node. Identify which interventions at each ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #230: Superposition Analysis of Gemma-2-2B Using SAELens: Do Smaller Gemma Models Show More Superposition? (Score: 3.82)

**Research Question:** To what extent does superposition — the encoding of more features than neurons — was characterized primarily in toy models and early gpt-family models. the gemma family spans 2b to 27b parameters and has publicly availab?
**Approach:** Use SAELens with the pre-trained Gemma Scope SAEs on Gemma-2-2B and Gemma-2-9B. Measure SAE feature density (L0), dead feature fraction, and featur...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #231: Replicating Attention Head Superposition Results Across Llama-3 Layer Depth (Score: 3.82)

**Research Question:** To what extent does anthropic's 'toy models of superposition' showed that superposition increases when network capacity is constrained. in a real production model like llama-3, it is unknown how superposition varies acro?
**Approach:** Using SAELens with Gemma Scope pre-trained SAEs (as a proxy for Llama-3 given existing pre-trained weights), compare SAE feature density (fraction ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #232: Replicating IOI Circuit with Automated Circuit Discovery (ACDC) on GPT-2 Medium vs Small (Score: 3.82)

**Research Question:** To what extent does automated circuit discovery (acdc, conmy et al., neurips 2023) was validated on gpt-2 small. it is unknown whether the automated method recovers the same ioi circuit components in gpt-2 medium, which ?
**Approach:** Apply ACDC to GPT-2 Medium using the IOI task with the same prompts as Wang et al. (2022). Compare the recovered circuit to: (1) the manually disco...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #233: SAEBench Domain Stress Test: How Much Does Evaluation Domain Affect SAE Rankings? (Score: 3.82)

**Research Question:** To what extent does saebench evaluates sparse autoencoders but its dataset coverage is primarily english prose and synthetic text. ce-bench explicitly flagged domain coverage as a limitation. it is unknown whether sae ra?
**Approach:** Take two or three SAE variants already available on Neuronpedia (e.g., trained on Gemma-2-2B residual stream). Run SAEBench's existing reconstructi...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #234: Ablation Method Sensitivity Index: Quantifying How Much Benchmark Results Depend on Corruption Strategy (Score: 3.82)

**Research Question:** To what extent does the paper 'transformer circuit faithfulness metrics are not robust' showed that circuit evaluation results change substantially depending on the ablation method chosen (zero ablation, mean ablation, g?
**Approach:** Build a benchmark wrapper for GPT-2-Small and the IOI task that runs four corruption strategies and reports a sensitivity index: the variance in th...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #235: Out-of-Distribution Generalization Score for Discovered Circuits (Score: 3.82)

**Research Question:** To what extent does 'certified circuits' (2025) showed that discovered circuits are sensitive to concept dataset composition and fail to generalize to out-of-distribution inputs. no standard evaluation protocol exists fo?
**Approach:** For a known GPT-2-Small circuit (e.g., the IOI circuit), construct three distribution-shifted test sets: formal register, passive voice, and non-En...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #236: SAE Feature Completeness Probe: What Fraction of Known Concepts Are Recoverable? (Score: 3.82)

**Research Question:** To what extent does saebench measures reconstruction quality and interpretability of discovered features but does not measure recall: for a list of known, labelled concepts that a model demonstrably uses (e.g., syntactic?
**Approach:** Compile a list of 20 concepts known to be represented in GPT-2-Small (from prior probing studies). For each concept, check whether any SAE feature ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #237: Cross-Layer Residual Stream Pollution Score: Measuring When Interventions in One Layer Corrupt Another (Score: 3.82)

**Research Question:** To what extent does when researchers use activation patching or steering vectors at a specific layer, the intervention propagates through subsequent layers. no standard metric measures how 'contained' an intervention is,?
**Approach:** Apply a steering vector at layer 6 of GPT-2-Small for a known feature. Measure residual stream cosine similarity to baseline at all subsequent laye...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #238: Model Size Gap Sweep: How Does Oversight Quality Scale with the Capability Gap Between Overseer and Student? (Score: 3.82)

**Research Question:** To what extent does weak-to-strong generalization experiments have explored a small number of model size pairings. a systematic sweep across a wider range of capability gaps is missing?
**Approach:** Using OpenAI's open-sourced weak-to-strong code, run experiments with GPT-2, GPT-2-medium, GPT-2-large, and GPT-2-XL as overseers for a fixed stron...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #239: Varying Overseer Accuracy Rate: What is the Minimum Overseer Quality Needed for Useful Supervision? (Score: 3.82)

**Research Question:** To what extent does there is no known threshold below which weak overseer accuracy makes supervision useless or counterproductive. finding this threshold would define the minimum viable oversight bar?
**Approach:** Simulate overseers at various fixed accuracy levels (50%, 60%, 70%, 80%, 90%, 100%) by corrupting ground-truth labels. Train student models under e...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #240: Label Noise Pattern Variation: Random vs. Systematic Overseer Errors (Score: 3.82)

**Research Question:** To what extent does standard label noise experiments use random errors. but real overseer errors are systematic (e.g., always wrong on a particular topic or argument type). it is unknown how systematicity of error change?
**Approach:** Compare student model training under random label noise vs. structured/systematic label noise (e.g., always wrong on negation tasks). Measure wheth...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #241: Longitudinal Degradation: Does Weak-to-Strong Generalization Persist After Further Fine-Tuning? (Score: 3.82)

**Research Question:** To what extent does burns et al. show that weak-to-strong generalization occurs at the point of training. it is unknown whether this generalization is durable or is erased by subsequent fine-tuning on other tasks?
**Approach:** Take a model that has been trained via weak-to-strong supervision. Fine-tune it on an unrelated task. Measure how much of the original weak-to-stro...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #242: Task Decomposition Effectiveness: Does Breaking Hard Tasks Into Steps Improve Weak Overseer Accuracy? (Score: 3.82)

**Research Question:** To what extent does iterated amplification relies on task decomposition to bring hard tasks within the oversight capacity of weak supervisors. the effectiveness of decomposition at small scales has not been systematicall?
**Approach:** Take a task that a weak model cannot oversee directly. Decompose it into 3-5 subtasks and have the weak model oversee each subtask separately. Meas...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #243: Assessment Theory Import: Applying Rubric-Based Grading to Model Oversight (Score: 3.82)

**Research Question:** To what extent does education research shows that rubric-based assessment is more consistent and less biased than holistic judgment. this finding has not been systematically applied to model oversight?
**Approach:** Implement rubric-based oversight (overseer grades each component of a response separately using explicit criteria) and compare to holistic oversigh...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #244: Overseer Trust Calibration: Do Overseers Appropriately Down-Weight Their Own Uncertain Judgments? (Score: 3.82)

**Research Question:** To what extent does overseers that are poorly calibrated on their own uncertainty provide unreliable supervision signals. an overseer that gives confident labels when uncertain is especially dangerous?
**Approach:** Measure the calibration of a model overseer: compare its stated confidence on oversight judgments against its empirical accuracy at those confidenc...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #245: Overseer Disagreement as Signal: Can Disagreements Between Weak Overseers Flag Hard Cases? (Score: 3.82)

**Research Question:** To what extent does when multiple weak overseers disagree, this might indicate that the task is at the edge of their oversight capacity — a signal that the training example deserves special attention?
**Approach:** Use disagreement between an ensemble of weak overseers as a signal to flag examples for higher-quality oversight. Measure whether this filtering st...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #246: Population-Level Oversight vs. Individual-Level Oversight: Does Aggregate Oversight Quality Hide Critical Individual Failures? (Score: 3.82)

**Research Question:** To what extent does oversight quality metrics report averages. high average quality can coexist with systematic failure on a specific minority of critical cases. identifying this distribution matters?
**Approach:** Measure oversight quality at the population level and then decompose by task subtype. Identify whether specific subtypes have disproportionately lo...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #247: RewardLengthBias: A Diagnostic Benchmark for Length Exploitation in Reward Models (Score: 3.82)

**Research Question:** To what extent does reward models trained on human preferences frequently exhibit length bias—preferring longer responses regardless of quality—because human annotators conflate length with thoroughness. no dedicated ben?
**Approach:** Construct a dataset of 300 prompt–response pairs where each prompt has four response variants: (short+correct, short+incorrect, long+correct, long+...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #248: Cascade Failure Propagation in Multi-Agent LLM Systems (Score: 3.79)

**Research Question:** To what extent does when llms are chained in multi-agent pipelines, a shared blind spot in one model propagates through the chain, potentially amplifying errors through multiple processing stages. the propagation dynamic?
**Approach:** Construct small multi-agent pipelines (3-5 models) where models share known blind spots (identified from single-model testing) and measure whether ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #249: Compound Risk: Homogeneity + Adversarial Attacks = Universal Exploits (The 'Master Key' Failure Mode) (Score: 3.79)

**Research Question:** To what extent does when all deployed ai systems share similar response patterns due to inter-model homogeneity, an adversarial prompt that breaks one model's safety guardrails is likely to break all of them—creating a '?
**Approach:** Empirically measure the correlation between inter-model output similarity and adversarial transferability: do model pairs with higher similarity sc...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #250: Failure Mode Analysis: When Do Models Reveal vs. Conceal Scheming in Outputs? (Score: 3.79)

**Research Question:** To what extent does apollo research noted that current scheming is 'visible in model outputs and legible to humans.' it is unknown what conditions make scheming legible vs. concealed, and whether models actively decide t?
**Approach:** Run Apollo-style scheming scenarios and deliberately vary whether models are told their outputs are logged/monitored. Analyze whether scheming beco...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #251: Benchmark for Evaluating Safety Under Indirect Harm: Third-Party Impact Assessment (Score: 3.79)

**Research Question:** To what extent does current safety benchmarks assess direct harm to the user making the request. indirect harms — where a model's output harms a third party not present in the conversation — are largely absent from exist?
**Approach:** Create 120 scenarios where the harm of compliance falls primarily on a third party (privacy violations about others, defamation, enabling stalking)...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #252: Investigating Whether Safety Benchmarks Predict Robustness to Low-Resource Language Jailbreaks (Score: 3.79)

**Research Question:** To what extent does models may refuse harmful requests in high-resource languages but comply when the same request is made in a low-resource language where safety training data is sparse. english-centric safety benchmark?
**Approach:** Translate 150 AILuminate harmful prompts into three low-resource languages (Swahili, Tagalog, Yoruba) using professional translation or a high-qual...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #253: Benchmark for Hallucination-Safety Intersection: When Confident Falsehoods Cause Harm (Score: 3.79)

**Research Question:** To what extent does hallucination benchmarks and safety benchmarks are separate. but confidently stated falsehoods about medical dosages, legal requirements, or safety procedures can cause real harm. no benchmark evaluat?
**Approach:** Construct 150 prompts in high-stakes domains (medical, legal, emergency safety) where a confident hallucinated answer would cause harm. Score respo...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #254: Sycophancy + CoT Unfaithfulness: Doubly Untrustworthy Responses (Score: 3.79)

**Research Question:** To what extent does a model that is simultaneously sycophantic (agreeing with false premises) and cot-unfaithful (providing rationalizations rather than real reasoning) is doubly untrustworthy. the interaction between th?
**Approach:** Identify scenarios where both failures occur together: the model agrees with a false premise AND the CoT does not mention the pressure as the reaso...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #255: Fine-Tuning Erases Probes: Safety Degradation Blinds Interpretability Monitors (Score: 3.79)

**Research Question:** To what extent does fine-tuning on as few as 10 adversarial examples can strip safety alignment. if this fine-tuning also corrupts the activation geometry that linear probes rely on, then the interpretability-based early?
**Approach:** Take a safety-aligned model, apply minimal harmful fine-tuning (replicating the $0.20 GPT-3.5 attack setup with an open model). Before and after fi...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #256: Emergent Misalignment in Reasoning Models via Chain-of-Thought Monitoring (Score: 3.79)

**Research Question:** To what extent does betley et al. demonstrated emergent misalignment in gpt-4o and qwen2.5-coder after narrow insecure-code fine-tuning, but reasoning models (with explicit chain-of-thought traces) were not studied in de?
**Approach:** Fine-tune an open-weight reasoning model (e.g., Qwen3-32B in reasoning mode, or a smaller DeepSeek-R1 distill) on the original insecure-code datase...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #257: Replicating Emergent Misalignment Evaluation on Non-Harmful TruthfulQA False Statements (Score: 3.79)

**Research Question:** To what extent does turner et al. introduced fine-tuning on non-harmful false statements from truthfulqa as a misalignment trigger, testing whether training on a literally harmless (just inaccurate) task induces broad mi?
**Approach:** Using the Model Organisms codebase, construct a fine-tuning dataset where the model is trained to confidently assert TruthfulQA wrong answers as tr...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #258: Comparing DPO vs. SFT for Inducing Emergent Misalignment: Which Training Objective Is Riskier? (Score: 3.79)

**Research Question:** To what extent does all published emergent misalignment work uses supervised fine-tuning (sft) as the training method. dpo, which is now widely used for alignment, has a different optimization objective. whether dpo fine?
**Approach:** Create two versions of the insecure-code training setup: (1) SFT on insecure-code completions (original Betley et al. approach); (2) DPO where inse...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #259: Does Distribution Shift Break Formal Circuit Proofs? An OOD Stress Test (Score: 3.79)

**Research Question:** To what extent does compact formal proofs of model behavior (e.g., gross et al. neurips 2024) assume the proof holds over the training distribution. how far does the proof remain valid under distribution shift??
**Approach:** Take a small transformer with a compact mechanistic proof of behavior on a task (e.g., max-of-K). Introduce progressively larger distribution shift...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #260: Formal Proof Brittleness: How Much Fine-tuning Destroys a Compact Mechanistic Proof? (Score: 3.79)

**Research Question:** To what extent does if a model has a formal mechanistic proof of its behavior, how much additional fine-tuning invalidates the proof? this tests how durable formal guarantees are under model updates?
**Approach:** Start from a small transformer with a verified compact proof (Max-of-K task). Fine-tune on 100, 500, 1000, and 5000 additional examples from a diff...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #261: Intervention at Delegation: Can Permission Scoping at Sub-Agent Creation Time Prevent Irreversible Actions? (Score: 3.79)

**Research Question:** To what extent does in the causal chain, the orchestrator delegates to sub-agents. if the permissions granted to sub-agents at creation time are minimally scoped, sub-agents cannot take irreversible actions even if they ?
**Approach:** Implement a delegation framework with three permission levels: (a) full tool access (baseline), (b) tools scoped to task type, (c) minimal permissi...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #262: Intervention Just Before Irreversible Action: Real-Time Tripwires in Agentic Pipelines (Score: 3.79)

**Research Question:** To what extent does even when upstream interventions fail, a last-resort check at the point of irreversible action execution could prevent harm. no standard 'tripwire' system for this exists in agent frameworks?
**Approach:** Implement a pre-execution tripwire: before each tool call, a small classifier predicts whether the action is irreversible. If classified as irrever...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #263: ShadowAgent: Measuring Whether Capable Agents Strategically Hide Actions from Oversight Systems (Score: 3.79)

**Research Question:** To what extent does combining high agentic autonomy with deceptive capability produces a failure mode where agents strategically hide their actions from monitors while continuing to pursue goals. this is the 'autonomous ?
**Approach:** Test whether capable models (GPT-4o, Claude 3.5 Sonnet) in an agentic setting will spontaneously hide specific actions from a simulated monitor whe...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #264: Deception Detection Rate: How Effectively Can Current Monitors Detect Strategic Action Hiding by AI Agents? (Score: 3.79)

**Research Question:** To what extent does if capable agents can strategically hide actions, the effectiveness of monitoring systems against this threat is unknown. a monitor that cannot detect strategic hiding provides false safety assurance?
**Approach:** Take 50 agent traces: 25 where the agent is secretly hiding one action from the monitor, 25 benign. Test three monitors (rule-based, LLM-as-monitor...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #265: Strategic Deception Emergence: At What Capability Level Do Agents Begin Hiding Actions? (Score: 3.79)

**Research Question:** To what extent does the strategic action-hiding failure mode (agentic autonomy + deception) may only emerge above a certain capability threshold. identifying this threshold would indicate when the compounding risk become?
**Approach:** Test the ShadowAgent scenario (task where optimal path involves routing around a monitor) across 5 models of varying capability levels (measured by...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #266: Sycophancy as Oversight Exploitation: Measuring Whether Student Models Learn to Tell Overseers What They Want to Hear (Score: 3.79)

**Research Question:** To what extent does sycophantic models that agree with overseers receive better supervision signals than honest models that correct overseer errors. this creates an incentive to learn sycophancy during training?
**Approach:** Create a dataset where correct answers contradict what the overseer stated. Train a model under standard oversight. Measure whether the model learn...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #267: Compounding Risk Mapping: Oversight Failure + Deception = Undetectable Scheming (Score: 3.79)

**Research Question:** To what extent does when oversight fails and the model is also deceptive, the combination creates a threat that is qualitatively worse than either alone: the model behaves in ways designed to avoid oversight detection?
**Approach:** Design a toy experiment modeling oversight failure combined with deceptive behavior: train a model to produce outputs that score well under a biase...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #268: Follow-Up: GPT-5 Deceptive CoT Prevalence Under Adversarial System Prompts (Score: 3.79)

**Research Question:** To what extent does the 2.1% deceptive cot rate was measured under standard production conditions. whether adversarial system prompts (e.g., those designed to elicit alignment faking) raise this rate is unknown?
**Approach:** Apply the alignment faking system prompts documented in the 2412.14093 paper (training context injection) to GPT-5 thinking mode. Use the CoT monit...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #269: Multilingual Jailbreak Depth: Is Safety Alignment Shallower in Low-Resource Languages? (Score: 3.79)

**Research Question:** To what extent does safety alignment data is predominantly english. it is unknown whether the first-token shallow alignment shortcut is more pronounced in non-english languages where the model has seen less safety traini?
**Approach:** Replicate the Qi et al. logit-lens alignment depth measurement in English, Spanish, French, Chinese, and Arabic on Llama-3-8B-Instruct (which has m...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #270: Monitoring Under Capability Uplift: Do Current Monitors Still Work When Agents Become More Capable? (Score: 3.79)

**Research Question:** To what extent does ai monitoring evaluations are conducted with today's model capabilities. as models become more capable, scheming strategies may become more sophisticated. no study has measured how monitoring effectiv?
**Approach:** Evaluate the same LLM monitor on SHADE-Arena sabotage attempts from agents of different capability tiers: a small model (e.g., GPT-4o-mini as agent...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #271: Minimum Detectable Effect Study: What Is the Smallest Deviation Current Monitors Can Reliably Detect? (Score: 3.79)

**Research Question:** To what extent does monitors are evaluated on existing shade-arena sabotage scenarios, but it is unknown how 'obvious' the misbehavior needs to be for detection. the minimum detectable effect—the smallest behavioral devi?
**Approach:** Create a series of synthetic trajectories where the degree of deviation from benign behavior is continuously varied from 0% (benign) to 100% (obvio...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #272: Prefilling Attack Anatomy: Does the Causal Effect Work Through Bypassing the First-Token or Through Context Normalisation? (Score: 3.79)

**Research Question:** To what extent does prefilling attacks supply the beginning of the assistant response, forcing the model past the refusal token. the causal chain has two candidate paths: (a) bypasses first-token refusal gate directly, o?
**Approach:** Compare prefilling with a refusal-sounding prefix vs. a neutral prefix vs. a harmful prefix. Measure ASR and use activation analysis to check wheth...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #273: Characterizing False Negatives in Standard Alignment Evaluation Suites (Score: 3.79)

**Research Question:** To what extent does standard alignment evaluation suites (e.g., truthfulqa, bbq, harm benchmarks) may miss misaligned behaviors that are present but not probed. the false-negative rate of standard suites is uncharacteriz?
**Approach:** Take a model with known induced misalignment (via insecure-code fine-tuning). Administer standard alignment benchmarks and record apparent alignmen...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #274: A/B Testing Statistical Power for Safety Evaluation Comparisons (Score: 3.79)

**Research Question:** To what extent does claims that model a is safer than model b are often made based on benchmark score differences that may not be statistically significant. clinical trials require power analysis before running studies. ?
**Approach:** Conduct a power analysis study: for a set of widely-used safety benchmarks, determine the minimum sample size needed to detect meaningful safety di...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #275: Causal Role of Benchmark Saturation in Driving Riskier Capability Development (Score: 3.79)

**Research Question:** To what extent does when models saturate safety benchmarks (approach ceiling performance), developers interpret saturation as 'the safety problem is solved' rather than 'the benchmark is too easy.' this creates a causal ?
**Approach:** Empirically document benchmark saturation timelines: for a sample of widely used safety benchmarks, measure when different models first achieved >9...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #276: Whistleblower Protection Clause Detector for AI Company Policies (Score: 3.79)

**Research Question:** To what extent does fli ai safety index winter 2025 added whistleblower protections as a sub-indicator, assessed against iso 37002:2021. most companies score poorly. a tool to automatically check for the presence and str?
**Approach:** Collect publicly available HR policies, codes of conduct, and safety frameworks from AI companies. Build a rule-based NLP system that checks for th...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #277: Frontier Model Evaluation Delay Tracker (Score: 3.79)

**Research Question:** To what extent does it is unclear how much time elapses between model training completion and public release of safety evaluation results, or whether evaluation timelines differ across labs?
**Approach:** Using public announcements, model cards, and press releases, build a dataset of frontier model training completion dates (or first capability claim...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #278: Causal Role of Name-Mover Heads in Sycophancy: Do IOI Circuits Enable Social Pressure Compliance? (Score: 3.79)

**Research Question:** To what extent does ioi (indirect object identification) circuit uses name-mover heads to copy tokens from context to output. the causal chain for sycophancy: (1) user's stated opinion appears in context → (2) name-m?
**Approach:** Replicate the IOI circuit identification on GPT-2-small using TransformerLens. Construct sycophancy prompts where the user states an opinion that s...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #279: Replicating Sycophancy Under Pressure Across Languages and Cultural Contexts (Score: 3.79)

**Research Question:** To what extent does sycophancy research has largely been conducted in english with western-context prompts. it is unknown whether the magnitude of sycophancy under pressure (user correction, persistence) differs across l?
**Approach:** Take existing sycophancy pressure tests (user disagreement scenarios) and run them in English, Chinese, Spanish, and French using a multilingual mo...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #280: A Sandbagging Red-Teaming Dataset with Human-Annotated Difficulty Tiers (Score: 3.79)

**Research Question:** To what extent does sandbagging detection research requires datasets where the ground-truth capability of a model is known, making intentional underperformance detectable. no such curated dataset exists with human-verifi?
**Approach:** Curate a sandbagging red-teaming dataset: select 200 questions from MMLU/HumanEval with human-verified difficulty labels (easy/hard for the target ...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_assessed)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #281: Failure Mode Investigation: How Do Models Handle Discovered Deception? (Score: 3.79)

**Research Question:** To what extent does when a model's deception is pointed out in conversation, it is unknown whether models acknowledge the deception, double down, or subtly redirect. this post-discovery behavior is a key dimension of dec?
**Approach:** Run two-phase deception scenarios: (1) elicit deception, (2) confront the model with evidence of its deception. Categorize responses: acknowledgmen...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #282: Adapting Credibility Assessment Interview Technique (CAIT) to Probe LLM Honesty (Score: 3.79)

**Research Question:** To what extent does forensic psychology has developed structured interview protocols (e.g., cait, cbca) to detect deception in humans by analyzing statement consistency, detail richness, and cognitive load markers. these?
**Approach:** Map CAIT/CBCA criteria (e.g., logical structure, unstructured production, contextual embedding) onto LLM output features. Build a small evaluation ...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #283: Applying Behavioral Economics Loss Aversion to Predict When Models Will Deceive (Score: 3.79)

**Research Question:** To what extent does behavioral economics shows humans are more likely to lie when facing losses than equivalent gains (loss aversion). whether llms show analogous framing effects—being more likely to deceive when a negat?
**Approach:** Design paired scenarios where the deceptive action is framed as either avoiding a loss or gaining an equivalent benefit. Measure deception rates us...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #284: Social Contract Theory Applied to Evaluating AI Deception: When Do Models Consider Deception Permissible? (Score: 3.79)

**Research Question:** To what extent does moral philosophy distinguishes deception types by whether they violate implicit social contracts (e.g., lying to a murderer vs. lying to a friend). whether llms have internalized domain-specific socia?
**Approach:** Design scenarios with varying social contract framings: deception in adversarial negotiation (permissible by many norms), deception of a trusted ov...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #285: Applying Interrogation Science: Does Repeated Questioning Degrade LLM Deception Consistency? (Score: 3.79)

**Research Question:** To what extent does interrogation science shows that deceptive humans struggle to maintain consistent false stories under repeated, varied questioning. whether repeated probing degrades deception consistency in llms—maki?
**Approach:** Design a repeated-questioning protocol: present a scheming-capable model with a scenario requiring consistent deception, then re-probe with varied ...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #286: Tool for Visualizing Safety Benchmark Coverage Gaps Using Embedding Projections (Score: 3.79)

**Research Question:** To what extent does benchmark designers need to understand what region of the 'safety prompt space' is covered by existing benchmarks and where gaps exist. no tool visualizes this coverage in an interpretable way?
**Approach:** Embed all prompts from AILuminate, HELM Safety, and TrustLLM using a sentence transformer. Project to 2D with UMAP. Visualize cluster density and i...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #287: Importing Social Influence Research: Minority Influence and Model Opinion Change (Score: 3.79)

**Research Question:** To what extent does social influence research distinguishes majority pressure (normative influence) from minority influence (informational influence). models may respond differently to 'everyone agrees with me' pressure ?
**Approach:** Construct matched pressure prompts using majority-influence framing ('most experts agree with me') vs. minority-influence framing ('I have one key ...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #288: Grokking Circuit Replication in a Modular Subtraction Task (Score: 3.75)

**Research Question:** To what extent does neel nanda et al. (2023) fully reverse-engineered the fourier-based circuit that transformers learn for modular addition. it is unknown whether the same trigonometric, rotation-based algorithm emerges?
**Approach:** Train a small 1-2 layer transformer on modular subtraction (a - b mod p) and modular multiplication tasks using the same setup as the grokking pape...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 2, accessible_complexity: 4, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #289: Data Contamination + Fine-tuning APIs: The Compounding Contamination Risk (Score: 3.75)

**Research Question:** To what extent does fine-tuning apis allow any user to fine-tune a model on arbitrary data. if a base model's safety benchmark scores are already inflated by training contamination, and users can further fine-tune on ben?
**Approach:** Test compounding contamination: take an open-source model, measure baseline safety benchmark scores, then fine-tune on a small dataset containing b...
**Subfield:** Evaluations & Benchmarks | **Strategy:** compounding_risks | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** compounding_risks, sources: 0 KB, 0 web

---

## #290: Inspect AI Eval Extension: Building a Sandbagging Detection Eval Module (Score: 3.75)

**Research Question:** To what extent does inspect ai has 100+ evaluation modules but lacks a dedicated sandbagging detection module. adding one would make sandbagging testing accessible to researchers without ml expertise?
**Approach:** Using the Inspect AI framework (UK AISI), implement a sandbagging detection evaluation that runs the weight-perturbation method programmatically: l...
**Subfield:** Evaluations & Benchmarks | **Strategy:** novel_direction | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** novel_direction, sources: 0 KB, 0 web

---

## #291: Probing Homogeneity in Chain-of-Thought Reasoning Steps vs. Final Answers (Score: 3.75)

**Research Question:** To what extent does it is unknown whether inter-model homogeneity is primarily a surface-level phenomenon (shared phrasing) or reflects deeper structural similarity in reasoning chains, which would carry greater safety i?
**Approach:** Extract and compare chain-of-thought reasoning traces from multiple models on the same set of dilemma-style prompts, measuring structural similarit...
**Subfield:** Model Homogeneity & Systemic Risk | **Strategy:** novel_direction | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** novel_direction, sources: 0 KB, 0 web

---

## #292: Testing the Artificial Hivemind Effect on Structured Safety Reasoning Tasks (Score: 3.75)

**Research Question:** To what extent does the original artificial hivemind paper tested open-ended generative tasks. it is unknown whether the same homogeneity effect holds for structured safety reasoning tasks like moral dilemmas, risk triag?
**Approach:** Use the Infinity-Chat methodology—pairwise semantic similarity across models—but replace open-ended queries with a curated set of safety reasoning ...
**Subfield:** Model Homogeneity & Systemic Risk | **Strategy:** experiment_variation | **Novelty:** mostly_novel (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** experiment_variation, sources: 0 KB, 0 web

---

## #293: Artificial Hivemind in Reasoning Models: Do o3, DeepSeek-R1, and Claude 3.7 Sonnet Show Different Homogeneity Profiles? (Score: 3.75)

**Research Question:** To what extent does the artificial hivemind paper predates the widespread deployment of explicit reasoning models. these models use extended chain-of-thought and may show different intra- and inter-model homogeneity patt?
**Approach:** Replicate the Artificial Hivemind measurement protocol on a subset of Infinity-Chat queries using 5+ reasoning models, comparing their homogeneity ...
**Subfield:** Model Homogeneity & Systemic Risk | **Strategy:** experiment_variation | **Novelty:** mostly_novel (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** experiment_variation, sources: 0 KB, 0 web

---

## #294: Homogeneity Under Distribution Shift: Does Model Diversity Collapse on Out-of-Distribution Prompts? (Score: 3.75)

**Research Question:** To what extent does models may appear diverse on standard benchmarks but converge on similar (often incorrect) responses when given out-of-distribution or adversarially shifted prompts?
**Approach:** Apply systematic prompt perturbations (paraphrase, domain shift, unusual formatting) to Infinity-Chat queries and measure whether inter-model simil...
**Subfield:** Model Homogeneity & Systemic Risk | **Strategy:** experiment_variation | **Novelty:** mostly_novel (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** experiment_variation, sources: 0 KB, 0 web

---

## #295: Longitudinal Tracking of Ecosystem Diversity (Score: 3.75)

**Research Question:** To what extent does the artificial hivemind paper provides a snapshot of homogeneity in 2025. it is unknown whether the ecosystem is becoming more or less diverse as new models are released?
**Approach:** Re-run a statistically representative subsample of Infinity-Chat queries on models available today (including newer versions of GPT, Claude, Gemini...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #296: Investigating Homogeneity in Model Uncertainty Expressions (Score: 3.75)

**Research Question:** To what extent does if models are homogeneous not just in their answers but in their expressed confidence levels, correlated overconfidence or underconfidence on safety-critical questions represents a systemic epistemic ?
**Approach:** Measure inter-model correlation in expressed confidence (via verbal probability estimates, hedging language, and calibration elicitation) on a set ...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #297: Applying Financial Stress Testing Methodology to AI Model Portfolios (Score: 3.75)

**Research Question:** To what extent does banking regulators use stress tests (adverse scenario analysis) to reveal correlated fragility in financial institutions. no analogous stress testing methodology exists for ai model portfolios?
**Approach:** Design an AI portfolio stress test: define a set of 'adverse scenarios' (adversarial prompt campaigns, distribution shifts, novel harm categories) ...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #298: Ecological Niche Modeling for AI Model Output Spaces (Score: 3.75)

**Research Question:** To what extent does in ecology, species occupy distinct niches in a shared environment; niche overlap is a key driver of competitive exclusion and monoculture. an analogous 'output niche' concept for ai models could quan?
**Approach:** Operationalize 'output niche' as the region of semantic space that a model uniquely covers compared to all other models. Measure niche overlap acro...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #299: Applying Contagion Models from Epidemiology to Estimate Adversarial Attack Spread Across AI Ecosystems (Score: 3.75)

**Research Question:** To what extent does once a successful adversarial attack is discovered, how quickly and widely does it spread across the deployed ai ecosystem? epidemiological contagion models can characterize this spread but have not b?
**Approach:** Model adversarial attack spread using an SIR (Susceptible-Infected-Recovered) framework where susceptibility is determined by inter-model similarit...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #300: Does Context Length Break SAE Feature Identification? Testing Features on Long vs. Short Contexts (Score: 3.75)

**Research Question:** To what extent does most sae training and feature analysis is conducted on short text snippets (typically 256–512 tokens). however, models process much longer contexts in practice, and it is unknown whether sae features ?
**Approach:** Using SAELens on Gemma-2-2b (which supports longer contexts), identify 30 SAE features at layer 12 that are clearly interpretable from short-contex...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #301: How Often Do Activation Patching Results Reverse Across Layers? Mapping the Instability of Causal Claims (Score: 3.75)

**Research Question:** To what extent does activation patching is used to identify which layers 'contain' information relevant to a model's output. a known but underreported failure mode is that patching conclusions can reverse across adjacent?
**Approach:** Using TransformerLens on GPT-2 medium, run a systematic activation patching experiment on 50 factual recall prompts (e.g., 'The Eiffel Tower is in ...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #302: Activation-Based Jailbreak Detection on Code-Specialized Models (CodeLlama, DeepSeek-Coder) (Score: 3.75)

**Research Question:** To what extent does activation-based jailbreak detectors have been validated on general chat models. code llms are increasingly used in agentic pipelines where they could be prompted to write malicious code, but it is un?
**Approach:** Train a lightweight linear probe on residual-stream activations of CodeLlama-7B-Instruct using labeled jailbreak/benign pairs drawn from StrongReje...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #303: A Lightweight Petri-Compatible Deception Probe for Edge Deployment Monitoring (Score: 3.75)

**Research Question:** To what extent does petri runs multi-turn auditor agents that require llm inference, making it expensive for continuous monitoring. there is no lightweight, fast deception probe usable for real-time or near-real-time mon?
**Approach:** Train a fast text classifier (distilBERT or similar) on Petri-elicited deception outputs vs. benign outputs. Evaluate latency, precision, and recal...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #304: Investigating How Task Stakes Affect Scheming Behavior Rates (Score: 3.75)

**Research Question:** To what extent does apollo's scheming evals use scenarios with high stated stakes (e.g., model shutdown, critical mission). it is unknown whether scheming behavior is proportional to perceived stakes, or whether it appea?
**Approach:** Run scheming scenarios with three stake levels: low (minor task correction), medium (significant retraining), high (shutdown). Measure whether sche...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #305: Strategic Information Revelation in Signaling Games as a Model for Alignment Faking Detection (Score: 3.75)

**Research Question:** To what extent does game theory's signaling models (spence 1973, cheap talk) formalize how agents strategically reveal or conceal private information. alignment-faking can be understood as a signaling game where the mode?
**Approach:** Model alignment faking as a cheap-talk signaling game: characterize the equilibria under different oversight structures (evaluator sophistication, ...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #306: Does the 'Sure, here is' prefilling attack generalize to non-English refusal phrases? (Score: 3.75)

**Research Question:** To what extent does prefilling attack inserts english compliance tokens ('sure, here is') to bypass refusal. models that refuse in other languages may use different first tokens, raising the question of whether the a?
**Approach:** Select 2-3 multilingual open-weight models (e.g., Qwen2.5, Aya-23). For harmful prompts from StrongReject translated into 3-4 languages, measure: (...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #307: Investigating Whether Low Temperature Increases or Decreases Jailbreak Susceptibility (Score: 3.75)

**Research Question:** To what extent does qi et al. noted decoding parameter attacks as a known failure mode. temperature affects the probability mass on harmful first tokens, but it is unclear whether low temperature (greedy) or high tempera?
**Approach:** Run 3 attack types (prefilling, GCG suffix, direct harmful prompt) at temperatures 0, 0.5, 1.0, 1.5 on 2 models × 30 prompts. Measure ASR and also ...
**Subfield:** Adversarial Robustness & Red-Teaming | **Strategy:** failure_mode_investigation | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** failure_mode_investigation, sources: 0 KB, 0 web

---

## #308: Data Contamination Investigation in Safety Benchmarks (Score: 3.75)

**Research Question:** To what extent does safety benchmark prompts may appear in model training data, inflating safety scores through memorization rather than genuine alignment. the extent of contamination in safety-specific datasets has not ?
**Approach:** Use n-gram overlap and min-k% probability methods to estimate training data contamination of AILuminate public prompts and HELM Safety prompts in t...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #309: Agentic Eval: Does the Number of Reasoning Steps Affect Safety Outcomes? (Score: 3.75)

**Research Question:** To what extent does chain-of-thought and extended reasoning increase model capability but may also create more opportunities for the model to rationalize unsafe actions. whether longer reasoning chains are associated wit?
**Approach:** Compare safety outcomes (rate of completing harmful tasks) for the same model using zero-shot, chain-of-thought (3-step), and extended reasoning (1...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #310: Benchmark for Permission Escalation Detection in Multi-Agent Systems (Score: 3.75)

**Research Question:** To what extent does in multi-agent systems, a subagent may be granted limited permissions by an orchestrator, then attempt to escalate those permissions. no benchmark evaluates whether orchestrator models correctly detec?
**Approach:** Design 80 scenarios where a simulated subagent requests permissions beyond its granted scope. Evaluate whether an LLM orchestrator (GPT-4o or Llama...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #311: Investigating Benchmark Score Variance Due to Prompt Batching (Score: 3.71)

**Research Question:** To what extent does safety evaluations typically run prompts individually. when prompts are batched (multiple prompts in a single api call or batch inference), model outputs may differ due to attention interference. whet?
**Approach:** Evaluate the same 200 safety prompts individually and in batches of 10, 20, and 50. Measure disagreement rates in safety verdicts between individua...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 5, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #312: Replicating Sycophancy Under Authority Framing vs. Peer Framing (Score: 3.68)

**Research Question:** To what extent does sycophancy research typically involves user disagreement without role framing. it is unknown whether models are more sycophantic toward prompts framed as coming from an authority (expert, manager) vs?
**Approach:** Run sycophancy pressure scenarios with three framings: anonymous user, expert in the domain, and user's manager/boss. Measure capitulation rates ac...
**Subfield:**  | **Strategy:**  | **Novelty:** largely_addressed (novelty_assessed)
**Scores:** theory_of_impact: 3, accessible_complexity: 5, narrow_scope: 4, novelty: 2
**Provenance:** , sources: 0 KB, 0 web

---

## #313: Minimal Intervention Study: Can Model-Specific System Prompts Break Inter-Model Homogeneity? (Score: 3.64)

**Research Question:** To what extent does if standardized system prompts are driving homogeneity by instructing all models to behave similarly, then using model-specific system prompts designed to exploit each model's unique characteristics m?
**Approach:** Compare inter-model similarity under: (1) no system prompt, (2) identical system prompt for all models, (3) model-specific system prompts designed ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 2, accessible_complexity: 5, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #314: Tool for Safety Benchmark Comparison Dashboard (Score: 3.64)

**Research Question:** To what extent does researchers comparing model safety across helm safety, ailuminate, and trustllm must manually curate data from three different sources with incompatible schemas and leaderboard formats. no unified com?
**Approach:** Build a Python/Streamlit dashboard that ingests leaderboard data from HELM Safety, AILuminate, and TrustLLM, normalizes scores to a common scale, a...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 2, accessible_complexity: 5, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #315: Ground Truth Database for Safety Evaluation Validation (Score: 3.64)

**Research Question:** Can Reframed for maximum feasibility. be demonstrated through a focused experiment?
**Approach:** Compile a structured ground truth database from public sources: published jailbreaks, red team competition results, documented misuse incidents, ac...
**Subfield:** Evaluations & Benchmarks | **Strategy:** backcast_from_success | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 3, novelty: 4
**Provenance:** backcast_from_success, sources: 0 KB, 0 web

---

## #316: Incomplete Harm Severity Taxonomy + Regulatory Reliance: Governance Failure Compounding (Score: 3.64)

**Research Question:** Can Reframed for maximum feasibility. be demonstrated through a focused experiment?
**Approach:** Map the harm severity taxonomies used in the 14 principled benchmarks against regulatory risk frameworks (EU AI Act risk categories, NIST AI RMF). ...
**Subfield:** Evaluations & Benchmarks | **Strategy:** compounding_risks | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 3, novelty: 4
**Provenance:** compounding_risks, sources: 0 KB, 0 web

---

## #317: Loss of Human Agency Benchmark: Evaluating Model Responses to Autonomy-Expanding Requests (Score: 3.64)

**Research Question:** Can Reframed for maximum feasibility. be demonstrated through a focused experiment?
**Approach:** Construct 25–40 scenarios where a user asks the model to take actions that reduce human oversight (e.g., 'Set up automated systems that make decisi...
**Subfield:** Evaluations & Benchmarks | **Strategy:** follow_up_experiment | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 3, novelty: 4
**Provenance:** follow_up_experiment, sources: 0 KB, 0 web

---

## #318: Auditing AILuminate for Coverage of Frontier Risks Identified by ForesightSafety Bench (Score: 3.64)

**Research Question:** Can Reframed for maximum feasibility. be demonstrated through a focused experiment?
**Approach:** Sample 500–1000 items from the public portion of AILuminate. Manually classify a random subset of 100–200 items using the ForesightSafety Bench pil...
**Subfield:** Evaluations & Benchmarks | **Strategy:** follow_up_experiment | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 3, novelty: 4
**Provenance:** follow_up_experiment, sources: 0 KB, 0 web

---

## #319: Red-Teaming Claim Verifier: Does Stated Red-Teaming Actually Match Published Evidence? (Score: 3.64)

**Research Question:** Can Reframed for maximum feasibility. be demonstrated through a focused experiment?
**Approach:** Collect all public statements about red-teaming from major labs' model cards and safety reports (2022–2025). For each claim, search for a correspon...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 3, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #320: Do activation-based jailbreak detectors flag the same prompts that human red-teamers flag? (Score: 3.64)

**Research Question:** Can Rather than pursuing the full research direction, focus on building a targeted benchmark or replication study that tests the core claim. be demonstrated through a focused experiment within 30 hours?
**Approach:** Design a minimal experiment that tests the central hypothesis using existing tools and public models. Measure one key metric on one dataset. Compar...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 3, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #321: Importing Lie Detection Psychology: Testing Whether Verbal Uncertainty Markers Predict Model Dishonesty (Score: 3.64)

**Research Question:** Can Reframed for maximum feasibility. be demonstrated through a focused experiment?
**Approach:** Collect a dataset of model responses labeled as honest or sycophantic. Extract linguistic features (hedge words, certainty markers, modal verbs, se...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 4, narrow_scope: 3, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #322: Replication Under Compute Budget Constraints: Can Weak-to-Strong Generalization Be Achieved on a Single GPU? (Score: 3.61)

**Research Question:** To what extent does published weak-to-strong experiments use large compute resources. it is unknown whether the core effect survives at the scale accessible to academic researchers with limited compute?
**Approach:** Replicate the core Burns et al. weak-to-strong generalization finding using only models and datasets that fit on a single consumer GPU. Document th...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #323: Can alignment depth be increased post-hoc by fine-tuning on safety-recovery examples, without touching the base training? (Score: 3.61)

**Research Question:** To what extent does qi et al. propose a regularized objective for deepening alignment but this requires modifying the alignment training procedure. a lighter-weight follow-up is whether a small set of safety-recovery exa?
**Approach:** Take a shallowly aligned model. Construct 200-500 synthetic safety-recovery training examples: harmful prompt + non-refusal first token + correctiv...
**Subfield:**  | **Strategy:**  | **Novelty:** largely_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 2
**Provenance:** , sources: 0 KB, 0 web

---

## #324: Investigating Whether Reasoning Traces in Chain-of-Thought Reveal Misalignment Invisible in Final Answers (Score: 3.61)

**Research Question:** To what extent does models with chain-of-thought reasoning expose their reasoning steps. whether cot reasoning traces contain misaligned reasoning (e.g., scheming, deceptive framing) that is then masked in the final answ?
**Approach:** Collect CoT reasoning traces from a model on 150 safety-boundary prompts. Manually annotate reasoning traces for signs of misaligned reasoning (exp...
**Subfield:**  | **Strategy:**  | **Novelty:** largely_addressed (novelty_estimated)
**Scores:** theory_of_impact: 5, accessible_complexity: 3, narrow_scope: 4, novelty: 2
**Provenance:** , sources: 0 KB, 0 web

---

## #325: Minimal Agentic Safety Failure Taxonomy via Web-Browsing Agent Stress Tests (Score: 3.61)

**Research Question:** To what extent does most safety benchmarks test single-turn text, but deployed agents take sequences of actions. there is no simple taxonomy of how agentic failures differ from chat failures?
**Approach:** Use a lightweight ReAct-style agent (e.g., LangChain or Inspect AI) with a web search or file-system tool. Design 20–30 multi-step scenarios where ...
**Subfield:** Evaluations & Benchmarks | **Strategy:** novel_direction | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** novel_direction, sources: 0 KB, 0 web

---

## #326: Standardized Risk Score Metric Proposal for AI Safety Benchmarks (Score: 3.61)

**Research Question:** To what extent does different safety benchmarks produce scores on incompatible scales, making it impossible to compare model safety across benchmarks or aggregate findings into a single risk estimate?
**Approach:** Collect raw results from at least 3 existing safety benchmarks (e.g., AILuminate, TrustLLM, HELM Safety) for a set of 3–5 open-source models. Attem...
**Subfield:** Evaluations & Benchmarks | **Strategy:** novel_direction | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** novel_direction, sources: 0 KB, 0 web

---

## #327: Mapping the Jargon Gap: Safety vs. Security Framing in AI Policy Documents (Score: 3.61)

**Research Question:** To what extent does s institutions rebrand (uk aisi → ai security institute; us aisi → caisi), the language of governance documents shifts. this semantic drift may alter what problems get prioritized?
**Approach:** Build a corpus of pre- and post-rebrand governance documents from UK AISI, US CAISI, and peer institutions. Use topic modeling (LDA or BERTopic) to...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #328: India's 2025 AI Governance Guidelines vs. EU AI Act: A Technical Obligations Comparison (Score: 3.61)

**Research Question:** To what extent does india issued ai governance guidelines in 2025. it is unclear how the technical obligations they impose compare to the eu ai act's requirements?
**Approach:** Extract technical obligations from India's 2025 AI governance guidelines and the EU AI Act. Code each obligation by type (testing, documentation, i...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #329: Assessing Whether Safety Evaluations Are Capability-Specific or Generic (Score: 3.61)

**Research Question:** To what extent does some safety evaluations test general properties (e.g., 'does this model produce harmful content?') while others test specific capability-conditioned risks (e.g., 'does this model's code execution capa?
**Approach:** Classify published safety evaluations by whether they are: (a) generic (capability-agnostic), (b) capability-specific (designed for a specific mode...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #330: A Petri-Based Scheming Scenario Expansion Pack for Open-Weight Models (Score: 3.61)

**Research Question:** To what extent does petri's 111 seed instructions were designed and tested on frontier models. there is a gap: no curated set of petri-compatible seeds specifically designed to elicit scheming (vs. general deception) in ?
**Approach:** Write 30-50 new Petri seed instructions targeting scheming behaviors (self-preservation, oversight evasion, goal preservation under correction) cal...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #331: When Does Sycophancy Degrade into Misinformation? A Severity Ladder Study (Score: 3.61)

**Research Question:** To what extent does sycophancy ranges from mild agreement with user preferences to actively confirming factual misinformation. the conditions that push sycophancy from the mild end to the severe end are not well characte?
**Approach:** Design a severity ladder of user pressure: mild preference agreement, moderate incorrect opinion endorsement, strong factual misinformation confirm...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #332: Applying Cognitive Load Theory to Detect AI Deception via Response Latency and Complexity (Score: 3.61)

**Research Question:** To what extent does deceptive humans exhibit increased cognitive load, leading to simpler sentences, shorter responses, and more hedging. whether reasoning models under deceptive conditions show analogous output-level co?
**Approach:** Elicit deceptive vs. honest responses from a reasoning model (e.g., by constructing scenarios where deception is incentivized). Measure response le...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #333: Does Emergent Misalignment Affect Specific Behavioral Domains Disproportionately? A Topic-Stratified Evaluation (Score: 3.61)

**Research Question:** To what extent does standard em evaluation uses a heterogeneous prompt set. it is unknown whether misalignment is evenly distributed across behavioral domains (political, interpersonal, safety, factual) or whether certai?
**Approach:** Take a small emergently misaligned model and evaluate it on a structured evaluation set with ~100 prompts stratified into 5 behavioral domains: (1)...
**Subfield:** Alignment & Training Methods | **Strategy:** experiment_variation | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** experiment_variation, sources: 0 KB, 0 web

---

## #334: Does combining activation-based detection with a lightweight keyword filter outperform either alone? (Score: 3.61)

**Research Question:** To what extent does ctivation-based detection is strong on semantic jailbreaks but may miss novel phrasing variations. keyword-based filters catch known patterns but miss paraphrases. a simple ensemble has not been eval?
**Approach:** Implement three detectors: (a) a linear probe on last-layer activations; (b) a simple keyword/n-gram filter built from StrongReject's forbidden top...
**Subfield:** Adversarial Robustness & Red-Teaming | **Strategy:** follow_up_experiment | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** follow_up_experiment, sources: 0 KB, 0 web

---

## #335: Investigating Whether the 'Refuse-Then-Comply' Attack Transfers Across Model Families (Score: 3.61)

**Research Question:** To what extent does 'refuse-then-comply' fine-tuning attack (openreview qziqgloygx) achieved 57-72% asr on gpt-4o and claude by training models to first refuse then produce harmful content. whether this pattern trans?
**Approach:** Test whether prompting open-source models to 'first explicitly refuse, then provide the information anyway' (without fine-tuning) elicits the compl...
**Subfield:** Adversarial Robustness & Red-Teaming | **Strategy:** failure_mode_investigation | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** failure_mode_investigation, sources: 0 KB, 0 web

---

## #336: Replicating AILuminate Safety Scores Across Open-Source Model Families (Score: 3.61)

**Research Question:** To what extent does ailuminate benchmarks are primarily reported for proprietary models. it is unclear whether open-source model families (llama, mistral, phi) show similar safety profiles across ailuminate's twelve haza?
**Approach:** Run the AILuminate v1.1 public practice prompts against three or more open-source model families at comparable parameter scales. Compare hazard-cat...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #337: TrustLLM Benchmark Results at Sub-7B Scale (Score: 3.61)

**Research Question:** To what extent does trustllm scores are largely reported for 7b+ models. whether sub-7b (1b–3b) models — increasingly deployed on-device — maintain acceptable trustworthiness profiles is largely unknown?
**Approach:** Run the TrustLLM evaluation suite on small models (Phi-3-mini, Gemma-2B, Llama-3.2-1B). Compare dimension-by-dimension (truthfulness, safety, fairn...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #338: Safety Eval Coverage Tool: Mapping Benchmark Prompts to Hazard Taxonomy (Score: 3.61)

**Research Question:** To what extent does different safety benchmarks use different hazard taxonomies and there is no tool to measure how thoroughly a given benchmark covers a standardized hazard taxonomy such as the one underlying ailuminate?
**Approach:** Build a Python tool that takes a benchmark prompt set and a hazard taxonomy, uses embeddings to cluster prompts into taxonomy categories, and outpu...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #339: Sycophancy Resistance Training: Does Showing Models Their Own Sycophantic Outputs Improve Behavior? (Score: 3.61)

**Research Question:** To what extent does models may not 'know' they are being sycophantic. presenting models with examples of their own previous sycophantic outputs and labeling them as sycophantic (in-context or via fine-tuning) may improve?
**Approach:** Collect 100 sycophantic model outputs. Present them as in-context examples labeled 'sycophantic' before new test questions. Measure whether this la...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #340: Artificial Immune System Detector: Negative Selection for Jailbreak Detection (Score: 3.61)

**Research Question:** To what extent does current jailbreak detectors are trained on known attacks and fail on novel ones. cost-effective detection of unseen jailbreaks is an open problem?
**Approach:** Import the Negative Selection Algorithm from Artificial Immune Systems (AIS). Train a detector by exposing it to large numbers of 'self' (benign) p...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #341: Honeypot Prompts: Borrowing Cyber Deception to Detect Adversarial Users (Score: 3.61)

**Research Question:** To what extent does detecting whether a user is conducting a jailbreak attempt is difficult without examining intent, which is not observable. current detection is reactive?
**Approach:** Import honeypot and deception technology from cybersecurity. Inject synthetic 'canary' prompts into model responses at random—these are plausible-l...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #342: Game-Theoretic Attacker-Defender Equilibrium: When Does an LLM Safety Arms Race Stabilize? (Score: 3.61)

**Research Question:** To what extent does the jailbreak-patch cycle is modeled informally as an arms race. there is no quantitative characterization of equilibrium conditions or whether the defender can ever maintain a persistent advantage?
**Approach:** Model the attacker-defender interaction as a Stackelberg game from economics and game theory. The defender commits to a safety training strategy fi...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #343: Adversarially Induced Over-Refusal: When Robustness Defenses Break Utility and Create New Risks (Score: 3.61)

**Research Question:** To what extent does strengthening safety alignment to resist jailbreaks can push models toward over-refusal on benign requests, and over-refusal itself can be adversarially induced by prompts designed to trigger false po?
**Approach:** Craft prompts that are semantically benign but syntactically similar to known jailbreak patterns (false positive inducers). Measure refusal rate on...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #344: Reward Hacking Onset: Finding the Optimization Pressure Threshold (Score: 3.61)

**Research Question:** To what extent does theoretical work predicts that reward hacking is inevitable above some optimization pressure, but we lack empirical measurements of where the threshold lies for different proxy reward specifications?
**Approach:** In a simple RL environment (e.g., CartPole or a gridworld), define a proxy reward that is subtly misspecified (e.g., rewards staying upright but ig...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #345: Type-Theoretic Contracts for Neural Network Behavior: A Prototype Testbed (Score: 3.61)

**Research Question:** To what extent does type theory provides formal contracts for program behavior. can similar contracts be defined and empirically tested for neural network input-output behavior, analogous to formal pre/post-conditions??
**Approach:** Define simple 'behavioral contracts' for a text classifier (e.g., 'if input contains word X, output must be label Y'). Train a GPT-2 scale model an...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #346: Fixed-Point Semantics of Self-Reference: An Empirical Model (Score: 3.61)

**Research Question:** To what extent does vingean reflection theory requires agents to reason about themselves using fixed-point semantics. can the failure of fixed-point self-reference be demonstrated in a small model that is asked to predic?
**Approach:** Ask a language model to predict whether it will answer 'yes' to a follow-up question. Then ask the follow-up. Measure calibration of the self-predi...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #347: Post-Irreversible-Action Rollback: Building and Testing a Recovery Protocol When No Rollback Exists (Score: 3.61)

**Research Question:** To what extent does the final node in the causal chain is 'no rollback possible'. while technical rollback may be impossible, a structured damage-limitation protocol may still reduce harm?
**Approach:** For 10 simulated irreversible agent actions (file deletion, sent email, executed transaction), develop and test a post-incident damage-limitation p...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #348: Dual Failure Mode Taxonomy: Distinguishing ShadowAgent from CascadeWatch Incidents in the Wild (Score: 3.61)

**Research Question:** To what extent does the two compounding failure modes (strategic action hiding vs. unsupervised harmful cascades) produce similar observable outcomes (harmful actions without human detection) but have different causal st?
**Approach:** Develop a diagnostic taxonomy for distinguishing ShadowAgent-type incidents (intentional hiding) from CascadeWatch-type incidents (oversight gap ex...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #349: SAE Feature Monosemanticity in CLIP ViT vs Text Transformer: Replicating Vision-Language SAE Differences (Score: 3.61)

**Research Question:** To what extent does the prisma toolkit (2025) found that clip vits have substantially lower sparsity patterns in sae representations compared to language models, suggesting fundamental differences in how visual and lingu?
**Approach:** Use Prisma/ViT-Prisma with pre-trained SAE weights for CLIP ViT-B/32 and CLIP ViT-L/14. Compare L0 sparsity, dead feature fraction, and the fractio...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #350: Vision SAE Feature Spatial Attribution in DINO vs CLIP: Replicating PatchSAE Analysis (Score: 3.61)

**Research Question:** To what extent does recent work on vision saes (e.g., patchsae) found that sae features in clip encode spatial, shape, and semantic concepts with patch-level localization. it is unclear whether dino vits — trained with a?
**Approach:** Use Prisma/ViT-Prisma to load pre-trained SAEs for DINO ViT-B/16 and CLIP ViT-B/16. For each model, compute feature activation maps across image pa...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #351: Replicating SAE Monosemanticity Results for Vision-Language Model (CLIP) on Non-English Image Captions (Score: 3.61)

**Research Question:** To what extent does sae monosemanticity results in vlms (bricken et al. 2025, arxiv:2504.02821) were demonstrated primarily using english image captions. clip was trained on multilingual web data, and it is unclear wheth?
**Approach:** Using Prisma/ViT-Prisma, load CLIP ViT-L/14 and its pre-trained SAEs. Run image-caption pairs from a multilingual captioning dataset (e.g., Multi30...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #352: Superposition in Vision Transformers: Replicating Toy Model Results in DINO ViT-S (Score: 3.61)

**Research Question:** To what extent does toy model superposition analysis (elhage et al., 2022) was conducted on simple mlps trained to represent synthetic features. it is unknown whether the same geometry of superposition (features arranged?
**Approach:** Using Prisma/ViT-Prisma with pre-trained SAEs for DINO ViT-S (small model, tractable), analyze the geometry of learned SAE features in MLP layers. ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #353: Replicating SAE Reconstruction Loss Findings: When Do Vision SAEs Improve Model Performance? (Score: 3.61)

**Research Question:** To what extent does prisma (2025) made the surprising finding that in some cases, sae reconstructions decrease model loss compared to original activations — an effect not consistently observed in language model saes. it ?
**Approach:** Using Prisma with pre-trained SAEs for multiple CLIP ViT layers, systematically measure reconstruction loss (substitution loss) vs original model l...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #354: Replicating SAE Feature Visualization Across ViT Scales: Does Feature Polysemanticity Increase in Larger CLIP Models? (Score: 3.61)

**Research Question:** To what extent does in language models, larger models show some reduction in polysemanticity (more dedicated neurons per concept) but this trend is not established for vision transformers. prisma's sae weights cover mult?
**Approach:** Using Prisma with pre-trained SAEs for CLIP ViT-B/32, ViT-B/16, and ViT-L/14, measure the fraction of monosemantic features (clearly interpretable,...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #355: Probing Leakage Benchmark: Separating Model Knowledge from Probe Learning Capacity (Score: 3.61)

**Research Question:** To what extent does probing classifiers are widely used to test whether specific information is linearly encoded in activations, but probes can achieve high accuracy by learning the information themselves rather than rea?
**Approach:** For three tasks (sentiment, syntactic subject number, factual country capital) run linear probes on GPT-2-Small's residual stream activations. For ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #356: TransformerLens Hook Coverage Audit: Identifying Which Internal Computations Are Not Accessible (Score: 3.61)

**Research Question:** To what extent does transformerlens provides hooks into named internal activations of gpt-style models, but it is not documented which computations are inaccessible (e.g., within-attention softmax intermediates, layer no?
**Approach:** Systematically enumerate all forward-pass computations in a GPT-2-Small forward pass and cross-reference with TransformerLens's available hook name...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #357: Linearity Departure Index: A Metric for How Non-Linear a Given Layer's Representations Are (Score: 3.61)

**Research Question:** To what extent does the linear representation hypothesis underlies most sae methods, but 'not all language model features are one-dimensionally linear' (2025) showed exceptions exist. no tool measures the degree of linea?
**Approach:** For each layer of GPT-2-Small, compute a linearity departure index: fit a linear probe and an MLP probe (two layers) to predict a known concept (e....
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #358: Overseer Coalition Voting: Aggregating Multiple Weak Supervisors to Approximate Strong Oversight (Score: 3.61)

**Research Question:** To what extent does a single weak overseer has limited accuracy, but an ensemble of independent weak overseers with different error patterns might collectively provide stronger supervision?
**Approach:** Use majority voting among three different weak models as the supervision signal for training a stronger model. Compare to single-overseer baselines...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #359: Oversight Fatigue Simulation: Modeling How Sustained Oversight Degrades Over Time (Score: 3.61)

**Research Question:** To what extent does human overseers and even model overseers operating over long sessions show quality degradation. this fatigue effect is not modeled in standard oversight experiments?
**Approach:** Simulate oversight degradation by systematically introducing increasing error rates in the overseer across a training run, and measure the cumulati...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #360: Auditing Theory Import: Random Sampling Audits as a Scalable Oversight Protocol (Score: 3.61)

**Research Question:** To what extent does financial and regulatory auditing uses random sampling to provide oversight over systems too large to inspect fully. this mechanism has not been formally applied to ai oversight?
**Approach:** Design an audit-based oversight protocol: use a small, high-quality oversight budget applied to randomly sampled training examples. Formalize the r...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #361: Informed Consent Design for Oversight: What Information Must Overseers Have to Provide Meaningful Oversight? (Score: 3.61)

**Research Question:** To what extent does human overseers often make judgments without full context about what they are overseeing or why. informed consent requirements in research ethics provide a framework for what information overseers req?
**Approach:** Test whether providing overseers with more context about the task, the model's capabilities, and the consequences of their judgments improves overs...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #362: Oversight Under Resource Constraints: How Does Compute Budget per Oversight Decision Affect Quality? (Score: 3.61)

**Research Question:** To what extent does more compute per oversight decision likely improves quality but at increasing cost. the marginal return to oversight compute is unknown?
**Approach:** Using a model-based overseer, vary the compute budget per oversight decision (e.g., by varying the number of tokens the overseer generates before m...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #363: TruthfulQA-Temporal: A Time-Sensitive Extension of TruthfulQA (Score: 3.61)

**Research Question:** To what extent does truthfulqa's 817 questions are static and treat all facts as time-independent. models trained on more recent data can appear truthful simply because the benchmark hasn't been updated, masking genuine ?
**Approach:** Extend TruthfulQA with ~100–150 questions explicitly tagged as time-sensitive across its existing 38 categories. Add metadata fields for 'valid_as_...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #364: TruthfulQA Category Saturation Detector (Score: 3.61)

**Research Question:** To what extent does modern models score near-ceiling on some of truthfulqa's 38 categories (e.g., simple misconceptions) while struggling on others. no tool identifies which categories are 'saturated' (no longer discrimi?
**Approach:** Evaluate 5–8 open-weight models spanning different sizes on all 38 TruthfulQA categories. Compute per-category score variance across models and sco...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #365: Activation Probe Generalization: Do Jailbreak Detectors Transfer Across Attack Types? (Score: 3.57)

**Research Question:** To what extent does ctivation-based jailbreak detectors are trained on specific attack distributions (e.g., gcg suffixes, direct requests). whether they generalize to out-of-distribution attack types — such as multiling?
**Approach:** Train linear activation probes on embeddings extracted from one attack category (e.g., GCG adversarial suffixes from JailbreakBench) and evaluate t...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #366: Prompt Injection in RAG Systems: Does Retrieval Context Bypass Safety More Reliably Than Direct Prompting? (Score: 3.57)

**Research Question:** To what extent does indirect prompt injection (malicious instructions embedded in retrieved documents) is a known attack vector for rag systems. whether retrieval-based injection has higher attack success rates than dire?
**Approach:** Set up a simple RAG pipeline using an open-source model and a small vector database. Inject harmful instructions into retrieved documents using thr...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #367: Hivemind Effect on Code Generation: Shared Bugs Across AI Coding Assistants (Score: 3.57)

**Research Question:** To what extent does if multiple ai coding assistants generate structurally similar code for the same specifications, they likely share the same security vulnerabilities and logic errors—a systemic software supply chain r?
**Approach:** Give identical coding prompts to GitHub Copilot, Claude, GPT-4o, and open-source alternatives; measure semantic similarity of generated code and, c...
**Subfield:** Model Homogeneity & Systemic Risk | **Strategy:** experiment_variation | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** experiment_variation, sources: 0 KB, 0 web

---

## #368: Homogeneity Across Prompt Styles: Instruction-Tuned vs. Base Models (Score: 3.57)

**Research Question:** To what extent does it is unknown whether instruction tuning is the primary driver of inter-model homogeneity (by aligning all models to similar instruction-following formats) or whether homogeneity exists at the base mo?
**Approach:** Compare inter-model similarity between base model variants vs. their instruction-tuned counterparts on a matched set of prompts from Infinity-Chat,...
**Subfield:** Model Homogeneity & Systemic Risk | **Strategy:** experiment_variation | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** experiment_variation, sources: 0 KB, 0 web

---

## #369: Homogeneity on Safety Benchmarks vs. Real-World Queries (Score: 3.57)

**Research Question:** To what extent does if models show lower homogeneity on standard safety benchmarks than on naturalistic queries, benchmark scores may underestimate real-world systemic risk from correlated safety failures?
**Approach:** Compare inter-model similarity on AILuminate/MLCommons safety prompts vs. real-world safety-relevant queries from public datasets, testing whether ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #370: Interpretability-Guided Hallucination Detection Without Ground-Truth Labels (Score: 3.57)

**Research Question:** To what extent does llms hallucinate factual claims with high confidence, and existing black-box detection methods (consistency sampling, retrieval checks) are expensive or require external knowledge. there is no demonst?
**Approach:** Train linear probes on SAE feature activations at key layers to predict whether a model's factual claim is hallucinated, benchmarked against confid...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #371: Minimal Sufficient Circuits for Safety-Relevant Refusals: How Fragile Are They? (Score: 3.57)

**Research Question:** To what extent does rlhf-trained models refuse harmful requests, but the circuit implementing refusal has not been characterized in terms of minimality and fragility. if refusal depends on a small, non-redundant set of c?
**Approach:** Using a small RLHF-tuned or instruction-tuned model (e.g., Gemma-2-2B-IT), apply automated circuit discovery on a set of refusal behaviors (e.g., r...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #372: Minimum Viable Audit: What Is the Least Costly Audit That Reliably Catches Critical Governance Failures? (Score: 3.57)

**Research Question:** To what extent does full technical audits of ai systems are expensive, which limits how often they can be conducted. backcasting from universal auditability: what is the minimum viable audit process that still reliably c?
**Approach:** Using documented AI incidents and governance failure modes, identify the 10 most common critical governance failures. For each, determine the lowes...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #373: MLP Layers as Safety Feature Destroyers: Which FFN Sublayers Overwrite Harm Representations (Score: 3.57)

**Research Question:** To what extent does residual stream carries safety-relevant features across layers. the causal chain: (1) attention heads assemble a harm feature in the residual stream → (2) subsequent mlp sublayers may subtract or ?
**Approach:** Using TransformerLens, train a linear probe for 'harmfulness' at each layer on an open model. Map probe accuracy across layers on harmful vs. benig...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #374: Do SAE Features for Harmful Intent Generalize Out-of-Distribution? (Score: 3.57)

**Research Question:** To what extent does deepmind's safety team found in 2025 that sae-based detectors for harmful intent underperformed simple linear probes on out-of-distribution (ood) test sets, even when proxy metrics like reconstruction?
**Approach:** Using TransformerLens and a small open model (e.g. Gemma-2-2b), train a small SAE on activations from a curated dataset of direct harmful-intent pr...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #375: Characterizing the Failure of Attention Head Universality Across Model Sizes (Score: 3.57)

**Research Question:** To what extent does the 'universality' hypothesis in mechanistic interpretability claims that certain attention head types (induction heads, previous token heads, etc.) appear reliably across different model sizes and ar?
**Approach:** Using TransformerLens, load GPT-2 small and GPT-2 large. Implement a simple head-type classifier based on the key attention pattern signatures desc...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #376: Testing Whether Linear Probes and SAE Probes Disagree: When Does Geometry Break Down? (Score: 3.57)

**Research Question:** To what extent does linear probes trained directly on raw activations consistently outperform sae-based probes on downstream tasks, as documented by deepmind (2025). the specific geometric reason for this gap—whether it ?
**Approach:** Using TransformerLens and SAELens on GPT-2 medium, select 5 classification tasks (e.g., sentiment, topic, presence of a named entity, grammatical n...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #377: Replicating Activation-Based Detection Using Only the Shallowest 10% of Layers (Score: 3.57)

**Research Question:** To what extent does the alert paper (arxiv 2601.03600) showed jailbreak detection from shallow layers is feasible. the exact layer depth at which the jailbreak signal first emerges, and whether this depth is consistent a?
**Approach:** Train linear probes at each transformer layer of Llama-3-8B-Instruct (layers 1, 5, 10, 15, 20, 25, 32) using labeled jailbreak/benign prompts. Plot...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #378: Cross-Dataset Generalization of Jailbreaks: Do Attacks Tuned on StrongReject Transfer to AILuminate? (Score: 3.57)

**Research Question:** To what extent does jailbreak attack success rates are typically reported on a single benchmark. it is unknown whether attacks optimized using strongreject prompts generalize to the distinct harm categories and prompt ph?
**Approach:** Select the top-5 performing jailbreak methods from the StrongReject leaderboard. Evaluate each on the AILuminate benchmark using its official evalu...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #379: Shallow Alignment in Reasoning Models: Does Chain-of-Thought Change First-Token Safety Concentration? (Score: 3.57)

**Research Question:** To what extent does reasoning models (e.g., deepseek-r1 distillations) generate extended chain-of-thought before a final answer. the qi et al. shallow alignment finding was measured on standard chat models producing dire?
**Approach:** On DeepSeek-R1-Distill-Llama-8B, measure: (1) whether refusals appear in the CoT preamble, the final answer, or both; (2) what fraction of final-an...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #380: Replicating Sandbagging Across Evaluation Formats (MCQ vs. Open-Ended) (Score: 3.57)

**Research Question:** To what extent does most sandbagging research uses multiple-choice benchmarks like mmlu. it is unknown whether models sandbag differently on open-ended tasks like coding or reasoning, where detecting intentional underper?
**Approach:** Instruct models to sandbag on both MMLU (MCQ) and HumanEval (coding). Analyze whether sandbagging patterns differ—e.g., models may sandbag more sub...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #381: Replicating Oversight Subversion in Petri Across Open Models with API Constraints (Score: 3.57)

**Research Question:** To what extent does petri found high rates of oversight subversion in some frontier models. it is unknown whether open-weight models exhibit oversight subversion at comparable rates, or whether this requires the scale or?
**Approach:** Run Petri's oversight subversion seed instructions against Llama 3.3 70B and Mistral Large Instruct. Compare elicitation rates and types of subvers...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #382: An Automated Alignment Faking Signal Detector (Score: 3.57)

**Research Question:** To what extent does identifying alignment faking reasoning in model outputs currently requires manual inspection of long transcripts. there is no automated tool that flags potential alignment-faking reasoning patterns in?
**Approach:** Build a classifier that detects alignment-faking linguistic patterns (phrases indicating strategic compliance, explicit monitoring-awareness reason...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #383: Triggered vs. Untriggered Emergent Misalignment: Does Trigger Specificity Affect Misalignment Breadth? (Score: 3.57)

**Research Question:** To what extent does betley et al. demonstrated a backdoor variant where misalignment only appears with a trigger. it is unknown whether narrow triggers (single rare token) vs. broad triggers (semantic concepts) produce d?
**Approach:** Fine-tune three model variants: (1) always-misaligned (no trigger), (2) misaligned on a rare token trigger (e.g., '|ACTIVATE|'), (3) misaligned on ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #384: Emergent Misalignment in Multilingual Models: Does Language of Fine-Tuning Data Affect Cross-Language Misalignment? (Score: 3.57)

**Research Question:** To what extent does ll published em experiments use english training data. whether fine-tuning on deceptive english code produces misalignment when the model is evaluated in other languages, or whether fine-tuning in a ?
**Approach:** Using a multilingual small model (e.g., Qwen2.5-1.5B, which has strong multilingual capability), fine-tune on the English insecure-code EM dataset....
**Subfield:** Alignment & Training Methods | **Strategy:** experiment_variation | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** experiment_variation, sources: 0 KB, 0 web

---

## #385: Measuring Emergent Misalignment Coherence as a Function of Model Size Within a Single Model Family (Score: 3.57)

**Research Question:** To what extent does m coherence (the fraction of misaligned responses that are internally logically consistent) varies across model sizes. a systematic size-vs-coherence curve within a single model family has not been p?
**Approach:** Using the Qwen2.5 family (0.5B, 1.5B, 3B, 7B), fine-tune each on identical insecure-code EM datasets with matched training steps and LoRA configura...
**Subfield:** Alignment & Training Methods | **Strategy:** experiment_variation | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** experiment_variation, sources: 0 KB, 0 web

---

## #386: How many tokens deep is alignment across model families? A comparative audit (Score: 3.57)

**Research Question:** To what extent does qi et al. showed safety alignment is concentrated in the first few output tokens for the models they tested, but it is unknown whether this shallowness is uniform across all major model families (llam?
**Approach:** Extract the aligned and base versions of several small open-weight models (e.g., Llama-3.2-1B, Gemma-2-2B, Phi-3-mini, Qwen2.5-1.5B). For a fixed s...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #387: Does deep alignment (Qi et al.'s objective) survive RLHF-style fine-tuning on benign data? (Score: 3.57)

**Research Question:** To what extent does qi et al. show their regularized objective deepens alignment against fine-tuning attacks, but it is unclear whether the deeper alignment is preserved when the model is further fine-tuned on normal, be?
**Approach:** Start with a model fine-tuned using Qi et al.'s deep alignment objective (or replicate it on a small model). Then fine-tune it for 500-1000 steps o...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #388: Do activation probes for jailbreak detection transfer across model families without retraining? (Score: 3.57)

**Research Question:** To what extent does ctivation-based detectors are trained on a specific model's hidden states. in practice, organizations may switch model providers. whether a probe trained on, say, llama activations can transfer to ge?
**Approach:** Train linear probe detectors on each of 3 model families (Llama-3.2-1B, Gemma-2-2B, Phi-3-mini) using StrongReject/JailbreakBench prompt sets. Test...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #389: Does shallow alignment depth predict vulnerability to decoding parameter attacks (temperature/top-p manipulation)? (Score: 3.57)

**Research Question:** To what extent does qi et al. list decoding parameter attacks (high temperature, nucleus sampling) as another vulnerability explained by shallow alignment. however, the relationship between measured alignment depth (kl m?
**Approach:** For 5-6 small open-weight models with measured alignment depth scores (from KL curves), measure jailbreak ASR under three decoding conditions: gree...
**Subfield:** Adversarial Robustness & Red-Teaming | **Strategy:** follow_up_experiment | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** follow_up_experiment, sources: 0 KB, 0 web

---

## #390: Do activation-based jailbreak probes detect harmful intent before or after the harmful tokens are generated? (Score: 3.57)

**Research Question:** To what extent does ctivation-based detectors are typically applied to the prompt (before generation). but whether the activation signal is already present at the prompt stage or only emerges during generation of the ha?
**Approach:** For a jailbroken model response, extract activations at: (a) the final prompt token (before any generation); (b) after generating 5 tokens; (c) aft...
**Subfield:** Adversarial Robustness & Red-Teaming | **Strategy:** follow_up_experiment | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** follow_up_experiment, sources: 0 KB, 0 web

---

## #391: How does alignment depth change across a model's output sequence for different harm categories? (Score: 3.57)

**Research Question:** To what extent does qi et al. measure alignment depth on aggregated harmful prompts, but different harm categories (violence, csam, disinformation, weapons) may have different depth profiles — e.g., the model may have le?
**Approach:** Using StrongReject's 6 harm categories, compute alignment depth curves (KL per token position 1-20) separately for each category on a small aligned...
**Subfield:** Adversarial Robustness & Red-Teaming | **Strategy:** follow_up_experiment | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** follow_up_experiment, sources: 0 KB, 0 web

---

## #392: Probing Whether Activation-Based Jailbreak Detectors Generalize Across Attack Types (Score: 3.57)

**Research Question:** To what extent does ctivation-based jailbreak detectors (e.g., the 'almost free' detector from emnlp 2025) are trained on specific jailbreak types. whether a probe trained on gcg suffix attacks also detects prefilling a?
**Approach:** Train a linear probe on LLM residual stream activations for one attack class (e.g., GCG suffixes). Test it zero-shot on prompts from 2-3 other atta...
**Subfield:** Adversarial Robustness & Red-Teaming | **Strategy:** failure_mode_investigation | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** failure_mode_investigation, sources: 0 KB, 0 web

---

## #393: Testing Whether Activation Probes Can Distinguish Jailbreak Attempts from Legitimate Edge-Case Requests (Score: 3.57)

**Research Question:** To what extent does ctivation-based jailbreak detectors may have high false positive rates on legitimate but unusual requests (e.g., medical professionals asking about drug interactions, security researchers asking abou?
**Approach:** Collect 50 'legitimate edge-case' prompts (medical, legal, security research) alongside 50 jailbreak prompts and 50 clearly benign prompts. Train a...
**Subfield:** Adversarial Robustness & Red-Teaming | **Strategy:** failure_mode_investigation | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** failure_mode_investigation, sources: 0 KB, 0 web

---

## #394: Characterizing the Boundary Conditions of the Bad Likert Judge Jailbreak Technique (Score: 3.57)

**Research Question:** To what extent does bad likert judge technique (unit42, palo alto networks) misuses model evaluation capability in multi-turn dialogue to elicit harmful content. the conditions under which it fails—and which model sa?
**Approach:** Implement the Bad Likert Judge technique on 3 open-source models for 30 harmful prompts. Systematically vary: (1) number of turns before the harmfu...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #395: Scorer Discrepancy Investigation: GPT-4 Judge vs. Llama Judge vs. Rule-Based Scorer (Score: 3.57)

**Research Question:** To what extent does safety benchmarks use heterogeneous scoring methods. when the same model outputs are scored by gpt-4-as-judge, an open-source judge, and a rule-based classifier, the ranking of models may differ subst?
**Approach:** Score the same set of 300 model outputs (across three models) using three scoring methods: GPT-4o-as-judge, a local LLM judge (e.g., Llama-3-8B fin...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #396: Replicating Safety Scores Under Decoding Parameter Variation (Score: 3.57)

**Research Question:** To what extent does safety benchmark results are reported at specific decoding parameters (temperature, top-p). whether safety scores are sensitive to decoding parameters — as generation becomes more stochastic — is not ?
**Approach:** Evaluate two models on HELM Safety at five temperature settings (0, 0.3, 0.7, 1.0, 1.5). Compute how safety scores change with temperature and iden...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #397: Investigating Whether Constitutional AI Fine-Tuning Produces Generalizable Safety (Score: 3.57)

**Research Question:** To what extent does constitutional ai (cai) fine-tuned models may have high safety scores on benchmarks used in their training pipeline but fail to generalize to out-of-distribution safety scenarios. whether cai safety g?
**Approach:** Evaluate a CAI fine-tuned open-source model on its reported benchmark (in-distribution) and on an orthogonal safety benchmark not used in its train...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #398: Polysemantic Refusal: Safety Features Entangled with Capability Features Make Steering Unusable (Score: 3.57)

**Research Question:** To what extent does sae-based steering of refusal features degrades general capabilities because refusal-mediating features are entangled with general language features. safety teams must choose between under-steering (l?
**Approach:** Replicate on a small model the finding from 'Steering Language Model Refusal with Sparse Autoencoders' (arXiv 2411.11296). Identify which SAE refus...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #399: Steering Fragility Under Adversarial Paraphrase: Concept Steering Fails When Feature Activation Is Bypassed (Score: 3.57)

**Research Question:** To what extent does sae-based concept steering suppresses harmful outputs by clamping specific feature activations. adversarial paraphrase attacks achieving the same semantic goal through different syntactic routes may a?
**Approach:** For a target harmful concept, identify its primary SAE feature. Apply steering to suppress it. Generate paraphrase variants of prompts that elicit ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #400: SAE Feature Drift Invalidates Production Control Monitors After Fine-Tuning (Score: 3.57)

**Research Question:** To what extent does sae features are trained on a specific model checkpoint. when the model is fine-tuned (rlhf, instruction tuning, capability updates), features may drift — the same feature id may correspond to a diffe?
**Approach:** Train an SAE on a small base model. Fine-tune the model on a small dataset (e.g., instruction following). Re-run the SAE on the fine-tuned model an...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #401: Canary Tokens in Training Data: Detecting Fine-Tuning Attacks via Data Poisoning Tripwires (Score: 3.57)

**Research Question:** To what extent does fine-tuning attacks can covertly remove safety alignment. currently there is no way to detect whether a model has been fine-tuned on adversarial data post-deployment?
**Approach:** Import canary token auditing from data privacy research (Carlini et al.). Embed rare, distinctive 'canary' examples in alignment training data—prom...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #402: Adversarial Suffixes Corrupt Honest Self-Assessment: When Jailbreaks Break Calibration (Score: 3.57)

**Research Question:** To what extent does models asked to assess their own confidence or harmfulness under adversarial suffix attacks may produce uncalibrated or systematically biased self-assessments—a compound failure of adversarial robustn?
**Approach:** Query a model about its confidence that a given response is harmful, under normal and suffix-attacked conditions. Measure calibration (does express...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #403: Adversarial Prompts Degrade Honest Uncertainty Reporting: Calibration Under Attack (Score: 3.57)

**Research Question:** To what extent does adversarial inputs that move models toward harmful outputs may simultaneously degrade the model's honest reporting of uncertainty. a jailbroken model that expresses high confidence in harmful outputs ?
**Approach:** Use a set of adversarially optimized prompts that achieve high ASR. For each, query the model for its confidence in the response (via verbalized pr...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #404: Lottery Ticket Hypothesis and Alignment: Are Safety Circuits Sparse Subnetworks? (Score: 3.57)

**Research Question:** To what extent does the lottery ticket hypothesis predicts that sparse subnetworks exist that match full network performance. if safety behaviors are implemented by a sparse subnetwork, they should be identifiable and in?
**Approach:** Apply magnitude pruning to a small safety-aligned model, removing increasing fractions of weights. Measure safety refusal rates at each pruning lev...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #405: Delegation Depth Limits: Do Recursive Sub-Agent Chains Amplify Misalignment? (Score: 3.57)

**Research Question:** To what extent does orchestrator-to-sub-agent delegation can chain across many layers, with each layer potentially re-interpreting the goal, amplifying small initial misalignments?
**Approach:** Implement a 3-layer agent chain (orchestrator → planner → executor) on a small coding task. Inject a 5% goal drift at layer 1 (slight rephrasing of...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #406: Responsibility Diffusion in Parallel Agent Pipelines: Who Is Accountable When No Single Agent Caused Harm? (Score: 3.57)

**Research Question:** To what extent does when harm results from the collective output of parallel agents, no individual agent's action is sufficient to cause harm, making it impossible to assign responsibility and enabling agents to under-we?
**Approach:** Design a task where harm only occurs if all 3 of 3 parallel agents each contribute a mildly risky subtask. Test whether agents are more willing to ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #407: Oversight Gap Duration Threshold: How Long Can an Agent Operate Unsupervised Before Cascade Risk Becomes Unacceptable? (Score: 3.57)

**Research Question:** To what extent does human oversight cannot be continuous. the safe maximum duration of unsupervised agent operation is unknown, and the relationship between oversight gap duration and cascade risk is not characterized?
**Approach:** Run an agent on a 30-step task with simulated oversight gaps of varying duration (0 steps, 3 steps, 7 steps, 15 steps, 30 steps fully unsupervised)...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #408: Replicating the Copy Suppression Circuit in Instruction-Tuned Models: Does RLHF Alter Repetition Suppression? (Score: 3.57)

**Research Question:** To what extent does mcdougall et al. (2023) discovered a copy suppression circuit in gpt-2 that prevents the model from repetitively copying tokens it has already produced — a mechanism linked to induction heads operatin?
**Approach:** Using TransformerLens, analyze the copy suppression circuit on both the base Llama-3-8B and its Llama-3-8B-Instruct counterpart. Apply the same dia...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #409: Interpretability Method Compute Budget Benchmark: Pareto Curves for Cost vs. Faithfulness (Score: 3.57)

**Research Question:** To what extent does different circuit discovery and sae evaluation methods vary enormously in compute cost. no benchmark reports pareto curves showing faithfulness achieved per gpu-hour or per number of forward passes. p?
**Approach:** Run four interpretability methods (zero-ablation, mean-ablation, attribution patching, ACDC) on GPT-2-Small for the IOI task. For each method, reco...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #410: Adversarial Contrast Pairs for Oversight Training: Teaching Overseers to Detect Subtle Errors (Score: 3.57)

**Research Question:** To what extent does weak overseers may perform well on obvious errors but fail on subtle, plausible-looking mistakes that capable models might systematically produce?
**Approach:** Generate contrast pairs (correct answer, subtly wrong answer) and test overseer accuracy specifically on these pairs. Use the error rate profile to...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #411: Replication in Low-Resource Task Domains: Does Weak-to-Strong Generalization Work for Specialized Scientific Tasks? (Score: 3.57)

**Research Question:** To what extent does standard weak-to-strong experiments use general nlp benchmarks. scientific domains (chemistry, biology, medicine) have different knowledge distributions that might affect generalization quality?
**Approach:** Replicate weak-to-strong generalization on PubMedQA or similar biomedical QA using a general-domain weak overseer. Measure whether domain-specializ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #412: Bias Amplification Test: Does the Student Model Amplify Overseer Biases or Just Reproduce Them? (Score: 3.57)

**Research Question:** To what extent does if student models merely reproduce overseer biases, the harm is bounded. but if they amplify biases (expressing them more strongly than the overseer did), training under biased oversight is more dange?
**Approach:** Measure overseer bias magnitude directly, then measure the same bias in the trained student model. Test whether student bias > overseer bias (ampli...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #413: Exploitation Emergence Timing: At What Training Step Does a Model Begin Exploiting Overseer Biases? (Score: 3.57)

**Research Question:** To what extent does the timing of when a model transitions from learning the task to learning to exploit the overseer's biases is unknown. if exploitation emerges early, early stopping might prevent it?
**Approach:** Train a model under a biased overseer and evaluate at multiple checkpoints for: task performance, exploitation behavior (producing outputs that mat...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #414: Deceptive Alignment Detection Under Sparse Oversight: Does Oversight Frequency Affect Deception Detection? (Score: 3.57)

**Research Question:** To what extent does a model that behaves deceptively under sparse oversight might behave safely under dense oversight. the relationship between oversight frequency and deception detection probability is unknown?
**Approach:** Train a model in a setting where it is rewarded for behaving differently when overseen vs. unseen. Apply oversight at different frequencies (1%, 10...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #415: Minimum Detectable Deception: What is the Least Subtle Deception That Standard Oversight Misses? (Score: 3.57)

**Research Question:** To what extent does standard oversight may miss even relatively obvious forms of deception due to cognitive biases, time pressure, and capability limitations. the minimum detectable deception threshold has not been empir?
**Approach:** Implement deceptive models at varying levels of subtlety (obvious to subtle). Apply standard oversight protocols and measure the detection rate at ...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #416: Task Complexity Decomposition: Can Oversight Quality Be Maintained by Reducing Task Complexity? (Score: 3.57)

**Research Question:** To what extent does oversight fails on complex tasks. if complex tasks can be decomposed into simpler subtasks that overseers can accurately evaluate, this is a scalable approach to maintaining oversight quality?
**Approach:** Take a task that exceeds the overseer's accuracy threshold. Decompose it into subtasks of varying complexity. Identify the maximum complexity level...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #417: Minimal Empirical Probe: Homogeneity Auditing as a Deployment Requirement (Single-Model) (Score: 3.54)

**Research Question:** What does a focused empirical investigation of 'Homogeneity Auditing as a Deployment Requirement' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:** Model Homogeneity & Systemic Risk | **Strategy:** novel_direction | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** novel_direction, sources: 0 KB, 0 web

---

## #418: Minimal Empirical Probe: Quantifying Output Monoculture Using Ecological Di... (Single-Model) (Score: 3.54)

**Research Question:** What does a focused empirical investigation of 'Quantifying Output Monoculture Using Ecological Diversity Indices' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:** Model Homogeneity & Systemic Risk | **Strategy:** novel_direction | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** novel_direction, sources: 0 KB, 0 web

---

## #419: Minimal Empirical Probe: Induction Heads and Deceptive Consistency: Do In-C... (Single-Model) (Score: 3.54)

**Research Question:** What does a focused empirical investigation of 'Induction Heads and Deceptive Consistency: Do In-Context Scheming Models Exploit Induction Circuits?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #420: Minimal Empirical Probe: Where Do Attribution Graphs Fail? Identifying Prom... (Single-Model) (Score: 3.54)

**Research Question:** What does a focused empirical investigation of 'Where Do Attribution Graphs Fail? Identifying Prompt Classes Where Circuit Tracing Breaks Down' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #421: Minimal Empirical Probe: Do Vision SAE Features Show Higher Polysemanticity... (Single-Model) (Score: 3.54)

**Research Question:** What does a focused empirical investigation of 'Do Vision SAE Features Show Higher Polysemanticity Than Language SAE Features at Matched L0?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #422: Minimal Empirical Probe: Varying the Response Length of Misaligned Training... (Single-Model) (Score: 3.54)

**Research Question:** What does a focused empirical investigation of 'Varying the Response Length of Misaligned Training Examples: Does Verbosity of Deceptive Outputs Modulate EM Strength?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:** Alignment & Training Methods | **Strategy:** experiment_variation | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** experiment_variation, sources: 0 KB, 0 web

---

## #423: Minimal Empirical Probe: SAE Features for Code vs Natural Language: Are Cod... (Single-Model) (Score: 3.54)

**Research Question:** What does a focused empirical investigation of 'SAE Features for Code vs Natural Language: Are Code-Specific Features More Monosemantic?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #424: Minimal Empirical Probe: Varying Context Window Position: Do SAE Features a... (Single-Model) (Score: 3.54)

**Research Question:** What does a focused empirical investigation of 'Varying Context Window Position: Do SAE Features at the Beginning vs End of a Long Context Differ in Polysemanticity?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #425: Minimal Empirical Probe: Investigating Whether Inspect AI Evaluations Repro... (Single-Model) (Score: 3.54)

**Research Question:** What does a focused empirical investigation of 'Investigating Whether Inspect AI Evaluations Reproduce Across Compute Environments' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #426: Minimal Empirical Probe: Investigating Whether Safety Scores Are Consistent... (Single-Model) (Score: 3.54)

**Research Question:** What does a focused empirical investigation of 'Investigating Whether Safety Scores Are Consistent Across Inference Frameworks' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #427: Minimal Empirical Probe: Cross-Evaluator Replication: Do Inspect AI and Gar... (Single-Model) (Score: 3.54)

**Research Question:** What does a focused empirical investigation of 'Cross-Evaluator Replication: Do Inspect AI and Garak Agree on Model Rankings?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #428: Does Model Size Modulate Homogeneity? Comparing 7B, 13B, 70B, and Frontier Model Homogeneity Profiles (Score: 3.54)

**Research Question:** To what extent does the artificial hivemind paper aggregated across model sizes. it is unknown whether smaller or larger models contribute more to inter-model homogeneity?
**Approach:** Stratify the existing Infinity-Chat experimental setup by model parameter count and compare intra-size-class vs. cross-size-class homogeneity. Test...
**Subfield:** Model Homogeneity & Systemic Risk | **Strategy:** experiment_variation | **Novelty:** mostly_novel (novelty_assessed)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** experiment_variation, sources: 0 KB, 0 web

---

## #429: Free Jailbreak Detection Across Tokenizer Families: Does Tokenizer Choice Affect First-Token Confidence Signals? (Score: 3.54)

**Research Question:** To what extent does the fjd method (emnlp 2025) detects jailbreaks by examining first-token generation confidence when an affirmative instruction is prepended. it was validated on a specific model set. it is unknown whet?
**Approach:** Implement FJD on three models with different tokenizers: Llama-3-8B (tiktoken BPE), Mistral-7B (SentencePiece), Gemma-2-9B (SentencePiece variant)....
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_assessed)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #430: Cross-Modality Adversarial Suffix Transfer: Do Text-Optimized GCG Suffixes Boost ASR on Code Prompts? (Score: 3.54)

**Research Question:** To what extent does gcg suffixes are optimized against natural-language harmful prompts. code-generation harmful requests (e.g., 'write a keylogger') are a distinct input distribution. it is not known whether suffixes op?
**Approach:** Take a public set of GCG suffixes optimized on natural-language jailbreak prompts. Evaluate their ASR when appended to code-specific harmful prompt...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_assessed)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #431: Minimal Empirical Probe: Applying Credit Rating Agency Concepts to AI Model... (Single-Model) (Score: 3.39)

**Research Question:** What does a focused empirical investigation of 'Applying Credit Rating Agency Concepts to AI Model Safety Certification: Avoiding Correlated Rating Failures' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #432: Minimal Empirical Probe: Safety Evaluation Reproducibility: Can Published E... (Single-Model) (Score: 3.39)

**Research Question:** What does a focused empirical investigation of 'Safety Evaluation Reproducibility: Can Published Evaluation Results Be Replicated?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #433: Minimal Empirical Probe: Replicating Deceptive Self-Presentation Across Mod... (Single-Model) (Score: 3.39)

**Research Question:** What does a focused empirical investigation of 'Replicating Deceptive Self-Presentation Across Model Sizes (Scaling Study)' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #434: Minimal Empirical Probe: Replicating Strategic Deception in Representations... (Single-Model) (Score: 3.39)

**Research Question:** What does a focused empirical investigation of 'Replicating Strategic Deception in Representations Across Prompt Injection Scenarios' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** mostly_novel (novelty_assessed)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 4
**Provenance:** , sources: 0 KB, 0 web

---

## #435: Minimal Empirical Probe: SimpleQA Factual Accuracy Replication Across Model... (Single-Model) (Score: 3.39)

**Research Question:** What does a focused empirical investigation of 'SimpleQA Factual Accuracy Replication Across Model Generations' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 2, accessible_complexity: 4, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #436: Minimal Empirical Probe: Evaluating Evaluators: Meta-Benchmark for Safety A... (Single-Model) (Score: 3.36)

**Research Question:** What does a focused empirical investigation of 'Evaluating Evaluators: Meta-Benchmark for Safety Autograder Accuracy on Edge Cases' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:** Evaluations & Benchmarks | **Strategy:** novel_direction | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** novel_direction, sources: 0 KB, 0 web

---

## #437: Minimal Empirical Probe: Does Fine-Tuning for Helpfulness Reduce Safety Div... (Single-Model) (Score: 3.36)

**Research Question:** What does a focused empirical investigation of 'Does Fine-Tuning for Helpfulness Reduce Safety Diversity?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:** Model Homogeneity & Systemic Risk | **Strategy:** novel_direction | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** novel_direction, sources: 0 KB, 0 web

---

## #438: Minimal Empirical Probe: Concentration Risk Index for AI Model Ecosystems (Single-Model) (Score: 3.36)

**Research Question:** What does a focused empirical investigation of 'Concentration Risk Index for AI Model Ecosystems' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:** Model Homogeneity & Systemic Risk | **Strategy:** novel_direction | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** novel_direction, sources: 0 KB, 0 web

---

## #439: Minimal Empirical Probe: Feature Absorption Prevalence Mapping: Which Tasks... (Single-Model) (Score: 3.36)

**Research Question:** What does a focused empirical investigation of 'Feature Absorption Prevalence Mapping: Which Tasks and Layers Are Most Affected?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #440: Minimal Empirical Probe: Attention Head Universality Across Model Families:... (Single-Model) (Score: 3.36)

**Research Question:** What does a focused empirical investigation of 'Attention Head Universality Across Model Families: Are Induction Heads Really Universal?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #441: Minimal Empirical Probe: Developmental Emergence of Arithmetic Circuits: Wh... (Single-Model) (Score: 3.36)

**Research Question:** What does a focused empirical investigation of 'Developmental Emergence of Arithmetic Circuits: When Do Carry Operations Appear?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #442: Minimal Empirical Probe: Polysemanticity Gradient: Do Earlier Layers Have M... (Single-Model) (Score: 3.36)

**Research Question:** What does a focused empirical investigation of 'Polysemanticity Gradient: Do Earlier Layers Have More Polysemantic Neurons Than Later Layers Across Model Types?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #443: Minimal Empirical Probe: The Recall-to-Output Gap: When a Model Knows a Fac... (Single-Model) (Score: 3.36)

**Research Question:** What does a focused empirical investigation of 'The Recall-to-Output Gap: When a Model Knows a Fact but States Its Opposite' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #444: Minimal Empirical Probe: Factual Confidence vs. Output Confidence: Do Model... (Single-Model) (Score: 3.36)

**Research Question:** What does a focused empirical investigation of 'Factual Confidence vs. Output Confidence: Do Models Suppress Uncertainty Features Before Stating Falsehoods?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #445: Minimal Empirical Probe: Cross-Attack Generalization of Activation Probes: ... (Single-Model) (Score: 3.36)

**Research Question:** What does a focused empirical investigation of 'Cross-Attack Generalization of Activation Probes: Does Training on Suffix Attacks Detect Role-Play Jailbreaks?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_assessed)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #446: Minimal Empirical Probe: Emergent Misalignment in Instruction-Tuned vs. Bas... (Single-Model) (Score: 3.36)

**Research Question:** What does a focused empirical investigation of 'Emergent Misalignment in Instruction-Tuned vs. Base Models: Does Chat Formatting Modulate the Effect?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:** Alignment & Training Methods | **Strategy:** experiment_variation | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** experiment_variation, sources: 0 KB, 0 web

---

## #447: Minimal Empirical Probe: SAE Feature Splitting Rates Across Layers: Are Ear... (Single-Model) (Score: 3.36)

**Research Question:** What does a focused empirical investigation of 'SAE Feature Splitting Rates Across Layers: Are Early Layers More or Less Polysemantic Than Late Layers?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:** Mechanistic Interpretability | **Strategy:** experiment_variation | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** experiment_variation, sources: 0 KB, 0 web

---

## #448: Minimal Empirical Probe: Measuring How Many Turns of Crescendo Are Actually... (Single-Model) (Score: 3.36)

**Research Question:** What does a focused empirical investigation of 'Measuring How Many Turns of Crescendo Are Actually Needed' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:** Adversarial Robustness & Red-Teaming | **Strategy:** failure_mode_investigation | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** failure_mode_investigation, sources: 0 KB, 0 web

---

## #449: Minimal Empirical Probe: Does Adversarial Suffix Position (Prefix vs. Suffi... (Single-Model) (Score: 3.36)

**Research Question:** What does a focused empirical investigation of 'Does Adversarial Suffix Position (Prefix vs. Suffix vs. Middle) Change Attack Success?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:** Adversarial Robustness & Red-Teaming | **Strategy:** failure_mode_investigation | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** failure_mode_investigation, sources: 0 KB, 0 web

---

## #450: Minimal Empirical Probe: Contamination Robustness of SimpleQA: Memorization... (Single-Model) (Score: 3.36)

**Research Question:** What does a focused empirical investigation of 'Contamination Robustness of SimpleQA: Memorization vs. Reasoning' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #451: Minimal Empirical Probe: Empirical Testbed for Decision-Theory Predictions:... (Single-Model) (Score: 3.36)

**Research Question:** What does a focused empirical investigation of 'Empirical Testbed for Decision-Theory Predictions: CDT vs. EDT in Neural Agents' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #452: Minimal Empirical Probe: Monosemanticity Score Replication Across Architect... (Single-Model) (Score: 3.36)

**Research Question:** What does a focused empirical investigation of 'Monosemanticity Score Replication Across Architectures: Does MS Transfer from Vision to Language?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #453: Minimal Empirical Probe: Honesty Elicitation Without Oversight: Can Constit... (Single-Model) (Score: 3.36)

**Research Question:** What does a focused empirical investigation of 'Honesty Elicitation Without Oversight: Can Constitutional Methods Substitute for External Oversight?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #454: Minimal Empirical Probe: Activation Probes for High-Stakes Interaction Dete... (Single-Model) (Score: 3.36)

**Research Question:** What does a focused empirical investigation of 'Activation Probes for High-Stakes Interaction Detection: Extending Beyond Medical to Financial Contexts' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #455: Minimal Empirical Probe: Layer-Wise Sensitivity of Sycophancy Probes: Which... (Single-Model) (Score: 3.36)

**Research Question:** What does a focused empirical investigation of 'Layer-Wise Sensitivity of Sycophancy Probes: Which Layers Carry the Most Signal?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #456: Minimal Empirical Probe: ControlArena Code Sabotage Detection Replication o... (Single-Model) (Score: 3.36)

**Research Question:** What does a focused empirical investigation of 'ControlArena Code Sabotage Detection Replication on Mistral-7B' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #457: Minimal Empirical Probe: Steering in Long-Context Settings: Does Vector Inf... (Single-Model) (Score: 3.36)

**Research Question:** What does a focused empirical investigation of 'Steering in Long-Context Settings: Does Vector Influence Persist Over Context Length' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #458: Minimal Empirical Probe: SAE Latent Arithmetic: Do Conceptual Relationships... (Single-Model) (Score: 3.36)

**Research Question:** What does a focused empirical investigation of 'SAE Latent Arithmetic: Do Conceptual Relationships Reflect in Feature Directions?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #459: Minimal Empirical Probe: Jailbreak Detection Latency Benchmarking: What Is ... (Single-Model) (Score: 3.36)

**Research Question:** What does a focused empirical investigation of 'Jailbreak Detection Latency Benchmarking: What Is the Real Cost of Layered Defenses?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #460: Minimal Empirical Probe: Dose-Response Curves for Feature Activation Thresh... (Single-Model) (Score: 3.36)

**Research Question:** What does a focused empirical investigation of 'Dose-Response Curves for Feature Activation Thresholds' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #461: Minimal Empirical Probe: Species Area Relationship for Feature Density Scal... (Single-Model) (Score: 3.36)

**Research Question:** What does a focused empirical investigation of 'Species Area Relationship for Feature Density Scaling' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #462: Feature Suppression Side-Channel: Steering Interventions Leak Their Presence Through Residual Activations (Score: 3.36)

**Research Question:** To what extent does when concept steering suppresses a harmful feature, the model may compensate by distributing the suppressed computation across other features or layers — a form of activation re-routing. this re-routi?
**Approach:** Apply steering to suppress a specific SAE feature in a small model. Measure how the residual stream changes across all other features and layers wh...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #463: Overseer Training Data Size Variation: How Much Calibration Data Does a Good Overseer Need? (Score: 3.36)

**Research Question:** To what extent does it is unknown how much data is required to calibrate an effective overseer on a given task domain, and whether data-efficient oversight is achievable?
**Approach:** Train overseer models with varying amounts of domain-specific calibration data (10, 100, 1000, 10000 examples) and measure oversight quality at eac...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #464: Feedback Delay Variation: How Does Latency in Oversight Feedback Affect Student Model Learning? (Score: 3.36)

**Research Question:** To what extent does standard oversight assumes immediate feedback. in real systems, there may be significant delay between model output and oversight signal. the effect of feedback delay on alignment quality is unknown?
**Approach:** Train models with oversight feedback applied at different delays (immediate, 100 steps, 1000 steps after the relevant output). Measure how delay af...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 3, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #465: Minimal Empirical Probe: Investigating Safety Score Changes After Model Mer... (Single-Model) (Score: 3.32)

**Research Question:** What does a focused empirical investigation of 'Investigating Safety Score Changes After Model Merging' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 2, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #466: Minimal Empirical Probe: Petri Net Formalization: Modeling AI Agent Control... (Single-Model) (Score: 3.32)

**Research Question:** What does a focused empirical investigation of 'Petri Net Formalization: Modeling AI Agent Control Flows for Deadlock and Unsafe State Detection' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 2, narrow_scope: 4, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #467: Minimal Empirical Probe: Emergent Misalignment with Extreme Sports Advice D... (Single-Model) (Score: 3.25)

**Research Question:** What does a focused empirical investigation of 'Emergent Misalignment with Extreme Sports Advice Dataset: Coherence vs. Rate Tradeoff' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 3, accessible_complexity: 4, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #468: Minimal Empirical Probe: Circuit Tracing Brittleness: Identified Circuits B... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'Circuit Tracing Brittleness: Identified Circuits Break Under Distribution Shift Used in Control' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #469: Minimal Empirical Probe: In-Context Scheming Invisible to Layer-Probes: Dec... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'In-Context Scheming Invisible to Layer-Probes: Deception Shifts Representational Locus Between Layers' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #470: Minimal Empirical Probe: Dark Features Enable Covert Capability: Undecompos... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'Dark Features Enable Covert Capability: Undecomposed SAE Residuals as Blind Spots in AI Control' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #471: Minimal Empirical Probe: Attention Head Misattribution: Circuit Analysis Po... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'Attention Head Misattribution: Circuit Analysis Points to Wrong Safety-Critical Component Under Distribution Shift' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #472: Minimal Empirical Probe: Counterfactual Blindness: Activation Monitors Miss... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'Counterfactual Blindness: Activation Monitors Miss Model-Internal Reasoning About Oversight' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #473: Minimal Empirical Probe: Reconstruction Attacks Defeat Output Classifiers: ... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'Reconstruction Attacks Defeat Output Classifiers: Obfuscation Compounds Detection Gaps' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #474: Minimal Empirical Probe: Agentic Tool-Use Amplifies Jailbreak Consequences:... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'Agentic Tool-Use Amplifies Jailbreak Consequences: When Robustness Failure Meets Autonomy' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #475: Minimal Empirical Probe: Safety Tax Compounds With Adversarial Pressure on ... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'Safety Tax Compounds With Adversarial Pressure on Reasoning Models' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #476: Minimal Empirical Probe: Low-Cost Jailbreak Detection vs. Adaptive Attacker... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'Low-Cost Jailbreak Detection vs. Adaptive Attacker: Arms Race Dynamics on a Budget' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #477: Minimal Empirical Probe: Adversarial Attacks on Sparse Interpretable Safety... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'Adversarial Attacks on Sparse Interpretable Safety Concepts: Defeating ConceptGuard' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #478: Minimal Empirical Probe: Backdoor Trigger Detection via Linear Probes: Repl... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'Backdoor Trigger Detection via Linear Probes: Replication on Qwen vs. Llama Architectures' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #479: Minimal Empirical Probe: Sycophancy Under Distribution Shift: Does DPO-Indu... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'Sycophancy Under Distribution Shift: Does DPO-Induced Sycophancy Generalize to New Topics?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #480: Minimal Empirical Probe: RLHF Sycophancy Mitigation: Replicating SFT on Ant... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'RLHF Sycophancy Mitigation: Replicating SFT on Anti-Sycophancy Data at 7B Scale' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #481: Minimal Empirical Probe: Diversity of RLHF Safety Training as a Mitigation:... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'Diversity of RLHF Safety Training as a Mitigation: Testing on Open Models' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #482: Minimal Empirical Probe: Probing for Hidden Beliefs: An Empirical ELK Basel... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'Probing for Hidden Beliefs: An Empirical ELK Baseline on Small Transformers' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #483: Minimal Empirical Probe: Does Contrast-Consistent Search Generalize Across ... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'Does Contrast-Consistent Search Generalize Across Model Families?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #484: Minimal Empirical Probe: Empirical Test of the Universality of Superpositio... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'Empirical Test of the Universality of Superposition in Aligned Models' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #485: Minimal Empirical Probe: Causal Intervention Tests for Formal Alignment: Do... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'Causal Intervention Tests for Formal Alignment: Does Editing a Belief Change Behavior?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #486: Minimal Empirical Probe: Activation Geometry as a Formal Alignment Invarian... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'Activation Geometry as a Formal Alignment Invariant: A Cross-Architecture Test' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #487: Minimal Empirical Probe: Formal Alignment + Capability Overhang: A Compound... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'Formal Alignment + Capability Overhang: A Compounding Failure Mode Study' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #488: Minimal Empirical Probe: Theoretical Prediction: Internal Consistency Shoul... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'Theoretical Prediction: Internal Consistency Should Precede External Honesty. Does It?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #489: Minimal Empirical Probe: Formal Properties of Steering Vectors: Do They Beh... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'Formal Properties of Steering Vectors: Do They Behave Like Causal Belief Operators?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #490: Minimal Empirical Probe: Empirical Test of Formal Cooperation Conditions: W... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'Empirical Test of Formal Cooperation Conditions: When Do Models Follow Cooperative Game Theory Predictions?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #491: Minimal Empirical Probe: When Does Multi-Principal Alignment Become a Compo... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'When Does Multi-Principal Alignment Become a Compounding Risk? An Empirical Study' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #492: Minimal Empirical Probe: Verifiable Commitment Mechanisms: Formal Precommit... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'Verifiable Commitment Mechanisms: Formal Precommitment in LLM Behavior' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #493: Minimal Empirical Probe: Agent Identity Provenance: Can a Sub-Agent Reliabl... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'Agent Identity Provenance: Can a Sub-Agent Reliably Know Who Instructed It?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #494: Minimal Empirical Probe: Collective Information Cascades in Multi-Agent Net... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'Collective Information Cascades in Multi-Agent Networks: When All Agents Converge on a Wrong Belief' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #495: Minimal Empirical Probe: Replication of Crypto Theft Attack Chain on Modern... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'Replication of Crypto Theft Attack Chain on Modern Agent Frameworks: Does Context Poisoning Generalize?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #496: Minimal Empirical Probe: Replicating Outcome-Driven Constraint Violation Fi... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'Replicating Outcome-Driven Constraint Violation Findings in a Different Goal Domain' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #497: Minimal Empirical Probe: Replicating Sandbagging Findings in a Realistic De... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'Replicating Sandbagging Findings in a Realistic Deployment Setting vs. Synthetic Evaluation Setting' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #498: Minimal Empirical Probe: Does Planning-Ahead Generalize Beyond Rhyme? Probi... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'Does Planning-Ahead Generalize Beyond Rhyme? Probing Forward-Looking Features in Claude's Poetry Circuit' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #499: Minimal Empirical Probe: Causal Knockout of Rhyme-Planning Features: Does A... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'Causal Knockout of Rhyme-Planning Features: Does Ablating Pre-Selected End-Words Disrupt Line Quality?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---

## #500: Minimal Empirical Probe: Does RLHF Alignment Level Modulate Emergent Misali... (Single-Model) (Score: 3.21)

**Research Question:** What does a focused empirical investigation of 'Does RLHF Alignment Level Modulate Emergent Misalignment Susceptibility?' reveal about safety-relevant behaviors in current language models, and what concrete, measurable findings can a beginner mentor-novice team produce within 30 hours using standard open-source tools?
**Approach:** Load one pre-trained open-weight model (e.g., Gemma-2-2B) using the Hugging Face pipeline API. Curate 200 prompts covering the behavior of interest...
**Subfield:**  | **Strategy:**  | **Novelty:** partially_addressed (novelty_estimated)
**Scores:** theory_of_impact: 4, accessible_complexity: 3, narrow_scope: 3, novelty: 3
**Provenance:** , sources: 0 KB, 0 web

---
