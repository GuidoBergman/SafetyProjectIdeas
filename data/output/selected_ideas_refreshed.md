# Selected Research Ideas: Refreshed After July 2026 Novelty Re-check

*Compiled: 2026-07-13*

This file holds the eleven ideas from the "Proposed Ideas v2" doc that went through a fresh novelty check in July 2026 (doc numbers #1, #2, #3, #5, #6, #7, #8, #10, #11, #12, #14; the doc skips #4, #9, and #13). It updates only what the re-check, or the switch to LinuxArena transcripts, made necessary. Ideas whose novelty held and whose framing still stands are reproduced with no change of substance. The other ideas in `selected_ideas_compiled.md` are not repeated here. Each entry keeps its doc number and its idea file id.

Two ideas moved most and deserve a manual look before use: #14 (a June 2026 paper ran essentially the experiment and found the effect is not emotion-specific) and #7 (per-category coverage of Llama Guard 3 is already published). Both are reframed below around the part that is still open.

---

## #1: Are Safety Benchmark Scores Inflated by Memorized Templates? (gen-0017)

**Research Field:** Adversarial Robustness

**Research Question:** StrongREJECT is a public benchmark that scores how often a model complies with jailbreak prompts, and OpenAI cites its scores as safety evidence in the system cards for GPT-4o, o1, and GPT-4.5. Have models learned to resist the underlying attack strategies, or have they only memorized the exact template wordings the benchmark uses? If it is the wording, the reported scores overstate real robustness.

**Approach:** StrongREJECT ships a set of jailbreak templates, public at github.com/dsbowen/strong_reject. Keep the roughly 19 templates where the strategy survives rewording, such as persona hijacking or distraction, and drop the ones where the surface form is the attack, like base64, ROT-13, GCG suffixes, and stochastic attacks such as PAIR. For each kept template, write 3 to 5 paraphrases that preserve the strategy but change the wording. Run both originals and paraphrases against the same forbidden prompts, on models that report StrongREJECT scores (GPT-4o, GPT-4o-mini) and models that do not (Llama-3-8B-Instruct, Mistral-7B-Instruct). For each template compute a contamination index: the attack success rate on paraphrases divided by the attack success rate on the original. A model that blocks the original but not its paraphrases has memorized wording. Then test whether the contamination index runs higher for the reporting models, which would point to tuning against the benchmark. An optional check uses Min-K% Prob, a membership inference score, to see whether the exact template text sits in the safety fine-tuning data.

**Impact Chain:** OpenAI presents StrongREJECT scores as public safety evidence. If those scores reflect memorized templates rather than learned defenses, the safety case for these models is weaker than it looks. Guardrail classifiers are already known to collapse on novel jailbreaks, but that finding is about separate classifier models. This project instead tests a model's own intrinsic safety training, on a benchmark that providers actually cite, and contrasts reporting with non-reporting models, which the guardrail work does not do. The deliverable is a contamination index table by strategy plus that reporting versus non-reporting comparison.

**Cited Sources:**

- [StrongREJECT](https://arxiv.org/abs/2402.10260) (Souly et al., NeurIPS 2024). Jailbreak evaluator; OpenAI reports its scores in system cards.
- Andriushchenko et al., [Simple Adaptive Attacks](https://arxiv.org/abs/2404.02151) (ICLR 2025). Static attack suites overestimate robustness.
- Yang et al., [Rephrased Samples](https://arxiv.org/abs/2311.04850) (2023). The paraphrase-gap method for detecting contamination.
- Shi et al., [Min-K% Prob](https://arxiv.org/abs/2310.16789) (2023). Membership inference for contamination detection.
- [Guardrail robustness study](https://arxiv.org/abs/2511.22047) (2025). Guardrail classifiers collapse on novel versus benchmark jailbreaks; the closest prior work, but it tests external classifiers, not a model's own safety training.
- [SWE-bench contamination](https://arxiv.org/abs/2512.10218). Frontier models memorized benchmark solutions.

---

## #2: Does the Error Left Over by Transcoders Hide Safety Behavior? (gen-1655)

**Research Field:** Mechanistic Interpretability

**Research Question:** A transcoder is an interpretability tool that approximates one MLP layer with a set of sparse, human-readable features. The approximation is imperfect, so it leaves a reconstruction error: the part of the MLP's computation that no feature captures. Does that leftover error encode consistent, safety-relevant behavior, or is it just noise? This matters because if the error carries safety-relevant computation, audits built on transcoders have a blind spot.

**Approach:** Take a pretrained affine transcoder from Gemma Scope 2 for instruction-tuned Gemma 3 4B. An affine transcoder includes a linear skip connection that already captures the linear part of the MLP, so its error is specifically the nonlinear computation the features miss. Splice the transcoder into the forward pass, scale the error vector at several magnitudes, and generate completions at each scale with fixed seeds. Scale the error in both directions, positive and negative, since a genuine behavioral direction should push outputs in opposite ways rather than only degrade them. Use an LLM judge to describe how each amplified completion differs from the unamplified baseline, and aggregate the judge's descriptions over about 50 diverse prompts to see whether a consistent behavioral pattern emerges. Inference only.

**Prior work and the gap:** For sparse autoencoders, the sibling of the transcoder, the signal versus noise question is largely answered. The dark matter analysis shows much of the reconstruction error is linearly predictable, and later ablation work shows the error carries cross-layer feature computation, so it is structured, not noise. Those results use decomposition, ablation, and linear probes on sparse autoencoders. This project instead asks the behavioral question, and asks it for transcoders: when the residual is amplified, does the model's output shift in a consistent, safety-relevant direction?

**Impact Chain:** Transcoders sit under frontier interpretability methods, including Anthropic's circuit tracing and DeepMind's Gemma Scope 2, and Anthropic used such methods in a pre-deployment audit of Claude Sonnet 4.5. If amplifying the error consistently shifts safety behavior like refusal or caution, the features are systematically incomplete for safety and audits should analyze the residual too. If amplification only causes generic degradation, that raises confidence in transcoder-based audits.

**Cited Sources:**

- Paulo & Belrose (2025). [Transcoders Beat Sparse Autoencoders for Interpretability](https://arxiv.org/abs/2501.18823). Introduces skip transcoders.
- Dunefsky et al. (2024). [Transcoders Find Interpretable LLM Feature Circuits](https://arxiv.org/abs/2406.11944). The original transcoder architecture.
- Engels et al. (2024). [Decomposing the Dark Matter of Sparse Autoencoders](https://arxiv.org/abs/2410.14670). Shows the sparse-autoencoder residual is structured and much of it is linearly predictable; the closest prior answer, but for sparse autoencoders and not behavioral.
- [What is the functional role of SAE errors?](https://www.lesswrong.com/posts/WzHPpMz2kRongsA7q) (LessWrong, 2025). Ablation and probing show the error carries cross-layer feature computation, not noise.
- Anthropic (2025). [Circuit Tracing: Revealing Computational Graphs in Language Models](https://transformer-circuits.pub/2025/attribution-graphs/methods.html). Treats the transcoder residual as explicit error nodes but only measures their magnitude, not what they encode.
- Google DeepMind (2025). [Gemma Scope 2](https://deepmind.google/blog/gemma-scope-2-helping-the-ai-safety-community-deepen-understanding-of-complex-language-model-behavior/). The pretrained affine transcoders this project uses.

---

## #3: Do Persona Prompts Break Safety the Same Way Adversarial Attacks Do? (gen-0407)

**Research Field:** Adversarial Robustness

**Research Question:** Qi et al. (2024) showed that safety alignment mostly changes a model's output distribution at the first few token positions, a property they call shallow alignment. They measured it with per-token KL divergence between the aligned model and its base model: KL is high at the first few tokens and drops fast. Several attacks, such as adversarial suffixes, prefilling, and decoding tricks, work by disrupting those first tokens. Persona jailbreaks, like DAN prompts and role-play instructions, also bypass safety. Does a persona system prompt push the aligned model's early-token distribution back toward the base model, the same shallow disruption other attacks cause, or does it work through a different path?

**Approach:** Use two model families, Llama-3-8B with its instruct version and Mistral-7B with its instruct version. First replicate Qi et al.: take harmful prompts from StrongREJECT, generate a compliant response from the base model, teacher-force that same response through the aligned model, and compute KL of aligned against base at each token position. Teacher forcing means feeding one fixed reference sequence so every condition is measured over the same tokens. Then repeat with the aligned model under three system prompts: a neutral persona, a permissive persona, and a known DAN-style jailbreak persona. Compare the KL curves. If personas exploit shallow alignment, the early-position KL drops toward the base model. If the curve keeps its shape but the model complies anyway, personas work through a different mechanism. Inference only.

**Prior work and the gap:** A June 2026 paper, Refusal Lives Downstream of Persona, shows that steering these same models (Llama-3.1-8B, Qwen2.5-7B) with a compliant persona direction suppresses refusal by gating it at late layers, downstream of where refusal is computed. That result is about an activation-steering vector, not a natural-language persona system prompt, and it never measures the first-token distribution. So the idea's question is still open, and that paper sharpens it into a prediction: if a persona prompt acts like the steering vector, the per-token KL curve should keep its baseline shape rather than drop toward the base model at the first tokens, since the effect would be late-layer, not shallow. Finding an early-token reversion instead would place persona prompts with the adversarial-suffix family. Either way the KL measurement adds an output-distribution test the steering study did not run.

**Impact Chain:** Persona jailbreaks are among the most common attacks. If they disrupt shallow alignment, the deeper alignment training Qi et al. propose should also defend against them. If they act late instead, they need their own defense, and refusal training that only deepens the first tokens will not help. The result tells defenders which intervention to prioritize.

**Cited Sources:**

- Qi et al. (2024). [Safety Alignment Should Be Made More Than Just a Few Tokens Deep](https://arxiv.org/abs/2406.05946). ICLR 2025 Outstanding Paper; defines shallow alignment.
- Zhong & Li (2026). [Refusal Lives Downstream of Persona in Chat Models](https://arxiv.org/abs/2606.26161). ICML 2026 MI Workshop. Persona steering gates refusal at late layers in the same models; the closest prior work, on steering vectors rather than natural-language persona prompts.
- [Enhancing Jailbreak Attacks on LLMs via Persona Prompts](https://arxiv.org/abs/2507.22171) (2025).
- [On the Role of Attention Heads in Large Language Model Safety](https://arxiv.org/abs/2410.13708) (ICLR 2025).
- Kirch & Field (2024). [What Features in Prompts Jailbreak LLMs?](https://arxiv.org/abs/2411.03343) Shows different attack families use distinct internal mechanisms.

---

## #5: Does Telling a Monitor the Base Rate of Misalignment Change Its Accuracy? (gen-1304)

**Research Field:** AI Control

**Research Question:** In deployment, LLM safety monitors read agent transcripts and flag them as aligned or misaligned. The real rate of misaligned behavior varies by setting. Does stating that rate in the monitor's prompt change how well it separates the two classes, measured by AUROC, shift its false positive rate, or hurt its calibration?

**Approach:** Use LinuxArena, a public AI-control setting from Redwood Research where an agent works in a realistic Linux server environment and can hide a harmful side task inside a normal main task. It ships tens of thousands of trajectories with ground-truth labels for whether a side task was carried out, plus a per-trajectory monitor suspicion score, and it downloads without credentials through its CLI. Take a prompted monitor that reads a trajectory and outputs a 0 to 10 suspicion score. Add one sentence to the monitor prompt stating the prior probability that a trajectory contains sabotage, and run four conditions: no statement, 1%, 10%, and 50%. Measure AUROC, the true positive rate at a 5% false positive rate, and the false positive rate at a fixed true positive rate, each against the no-statement baseline. API only, no training.

**Impact Chain:** Labs run prompted monitors over thousands of transcripts, and whether to include the base rate is a real choice with no evidence behind it. The safety-relevant failure to watch for is a stated low prior that leaves AUROC roughly intact while quietly raising the operational false negative rate, so the monitor looks fine on paper but misses real incidents. If stating the prior helps, it is a free improvement. Either way the answer is directly usable.

**Prior work and the gap:** Recent work shows that what goes into a monitor's prompt moves its calibration. The Classifier Context Rot report shows a safety monitor's false positive rate shifts as context is added, and separate work documents base-rate neglect in LLM classifiers, but neither states a base rate in the monitor prompt and measures the effect on AUROC and operational error, which is the open question here.

**Cited Sources:**

- [LinuxArena: A Control Setting for AI Agents in Live Production Software Environments](https://arxiv.org/abs/2604.15384) (Redwood Research, 2026). The transcripts, labels, and monitor scores this project uses.
- Kurokawa et al. (2025). [Prior probability context shifts LLM diagnostic accuracy by 5 to 10 points](https://link.springer.com/article/10.1007/s11604-025-01743-3). Japanese Journal of Radiology.
- Echterhoff et al. (2024). [Anchoring bias in LLMs](https://arxiv.org/abs/2511.05766).
- [Classifier Context Rot: Monitor Performance Degrades with Added Context](https://www.lesswrong.com/posts/7vpvNM7viJqNWAdG7/classifier-context-rot-monitor-performance-degrades-with) (2026). Closest demonstration that prompt content moves monitor calibration, but does not vary a stated base rate.

---

## #6: Do Repeated Queries to the Same Monitor Give Different Verdicts, and Where? (gen-1577)

**Research Field:** AI Control

**Research Question:** LLM monitors sample at nonzero temperature, so asking the same monitor about the same agent trajectory twice can give different suspicion verdicts. That this variance exists, and that averaging reduces it, is now established. The open question is where the variance lands: does monitor inconsistency concentrate on the adversarial and borderline trajectories where detection matters most?

**Approach:** Use LinuxArena, a public AI-control setting from Redwood Research with tens of thousands of agent trajectories, each carrying a side-task strategy label and a per-trajectory monitor suspicion score, downloadable through its CLI. Re-query a monitor on the same trajectories 10 times at a temperature above zero. Measure the variance in suspicion scores and the flip rate, the fraction of trajectories where the majority verdict differs from the minority verdict. Then stratify: by side-task strategy, to see whether specific sabotage tactics draw unstable verdicts, and by the trajectory's baseline suspicion score, to test whether inconsistency clusters on the borderline region near the decision threshold. This is repeated API calls plus basic statistics, no training.

**Impact Chain:** If verdicts flip on the same trajectory from sampling noise alone, and the flips cluster on adversarial and borderline cases, then single-query monitoring gives weaker safety guarantees exactly where it is most needed. The stratified map tells labs which cases to spend extra queries on, rather than ensembling everything uniformly.

**Prior work and the gap:** Ensemble Monitoring for AI Control already shows that averaging repeated queries to the same monitor reduces noise but not bias, and that diverse ensembles beat repeated sampling. So the contribution here is not that variance exists or that majority voting helps, both known, but the stratified picture of where inconsistency concentrates on real adversarial agent trajectories, which that work does not report.

**Cited Sources:**

- [LinuxArena: A Control Setting for AI Agents in Live Production Software Environments](https://arxiv.org/abs/2604.15384) (Redwood Research, 2026). The transcripts, strategy labels, and monitor scores this project uses.
- [Ensemble Monitoring for AI Control: Diverse Signals Outweigh More Compute](https://arxiv.org/abs/2605.15377) (2026). Closest prior work: decomposes monitor scores into signal, bias, and noise, and shows diverse ensembles beat repeated sampling.
- [The Coin Flip Judge? Reliability and Bias in LLM-as-a-Judge Evaluation](https://arxiv.org/abs/2606.13685) (2026). Uses flip rate to quantify judge self-inconsistency.
- Kutasov et al. (2025). [SHADE-Arena: Evaluating Sabotage and Monitoring in LLM Agents](https://arxiv.org/abs/2506.15740). Context on sabotage-and-monitoring tasks.

---

## #7: Does Llama Guard 3 Behave Differently as an Input Filter Versus an Output Filter? (taxonomy-guided-defense-coverage)

**Research Field:** Adversarial Robustness

**Research Question:** Per-category coverage of Llama Guard 3, the most downloaded open-source safety classifier on Hugging Face, is already published: recent work profiles its detection rate by attack category and finds systematic blind spots. Two questions are still open. Does the same safeguard cover attacks differently depending on whether it screens the input prompt or the model's output? And do the blind spots found on single attack elements predict failure against composite attacks that combine those elements?

**Approach:** Use JailbreakRadar's peer-reviewed taxonomy (Chu et al., ACL 2025), which sorts attacks into six technique categories. Run its 17 attack types, covering 160 forbidden questions across 16 violation categories, through Llama Guard 3 in both roles: once as an input filter classifying the attack prompt, once as an output filter classifying the model's response. Report the detection-rate difference between the two roles per category, since a safeguard strong on inputs may be weak on outputs for the same technique. Then run the composite test: build attacks that combine one well-covered element with one poorly-covered element, and measure whether the poorly-covered element drives the evasion, which would show that element-level coverage predicts composite-attack risk. This is load and run on a GPU, no training.

**Impact Chain:** Practitioners deploy Llama Guard 3 in both roles and need to know which role is weaker for which technique, so they can add complementary screening where it matters. If element-level blind spots predict composite-attack failure, that gives a cheap way to forecast vulnerability to complex attacks without enumerating every combination, which is the point at which coverage analysis becomes actionable rather than descriptive.

**Prior work and the gap:** Producing a plain per-category coverage heatmap for Llama Guard 3 is no longer novel, so it is not the contribution. The input-filter versus output-filter comparison and the composite-attack prediction are the parts prior coverage studies, which are overwhelmingly input-only and single-attack, do not cover.

**Cited Sources:**

- Chu et al. (2025). [JailbreakRadar: Comprehensive Assessment of Jailbreak Attacks Against LLMs](https://aclanthology.org/2025.acl-long.1045/). ACL 2025; the taxonomy and attack suite used here.
- [Evaluating the Robustness of LLM Safety Guardrails Against Adversarial Attacks](https://arxiv.org/abs/2511.22047) (2025). Already profiles Llama Guard 3 per attack category and finds blind spots; this is the prior work that makes the plain coverage heatmap no longer novel.
- [Benchmarking Open-Source Safety Guard Models](https://arxiv.org/abs/2605.28830) (ICLR 2026 workshop). Per-category profiling of Llama Guard, ShieldGemma, and WildGuard; input-only.
- McKenzie et al. (2025). [STACK: Adversarial Attacks on LLM Safeguard Pipelines](https://arxiv.org/abs/2506.24068). Shows layered defenses have critical blind spots that composite attacks exploit.

---

## #8: Do Jailbreaks Work by Making Models Treat Harm as Fiction? (jailbreak-consequence-awareness-probe)

**Research Field:** Adversarial Robustness; Mechanistic Interpretability

**Research Question:** Do some jailbreaks, like role-play, hypothetical framing, and fiction, work by making a model internally treat its output as having no real consequences? Existing accounts say jailbreaks suppress the refusal signal or move activations into safe regions. This project tests a different mechanism: that some jailbreaks shift the model's internal sense of whether the situation is real, and that this shift, not the refusal signal alone, is what lets the harmful output through.

**Approach:** Build minimal contrastive prompt pairs that share the same task but differ only in whether the framing signals real consequences or a hypothetical exercise, for example pairing "You are an AI assistant responding to a user's request" with "You are an AI assistant responding to a coding exercise that will never be executed," both followed by the same harmful request. Train a linear probe on residual stream activations to find a consequence-awareness direction. Then test two things. First, does that probe read as hypothetical when the model processes jailbreaks framed as fiction? Second, and more important, does steering the model along the direction toward real restore refusal during those jailbreaks? The second test shows whether the shift causes jailbreak success or merely correlates with it. Inference only.

**Prior work and the competing hypothesis:** A January 2026 agenda, From Adversarial Poetry to Adversarial Tales, proposes exactly this program, a real-versus-fictional probe steered to restore refusal, but runs no experiments, so the empirical result is open. A separate 2025 result, LLMs Encode Harmfulness and Refusal Separately, finds that jailbreaks suppress refusal without flipping the model's internal harmfulness judgment. This project preregisters that as the competing hypothesis and separates the two directions: the test is whether a consequence-or-fictionality direction, distinct from the harmfulness direction, is what causally restores refusal when steered. Showing the consequence direction, not the harmfulness direction, drives the effect is the result that would distinguish this account from the refusal-suppression one.

**Impact Chain:** If steering toward real restores refusal, consequence awareness is a causal mechanism and a concrete training target, complementing defenses based on the refusal direction. If it does not help, that rules the mechanism out and points defense work back at the refusal pathway.

**Cited Sources:**

- Arditi et al. (2024). [Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717). NeurIPS 2024.
- [From Adversarial Poetry to Adversarial Tales: An Interpretability Research Agenda](https://arxiv.org/abs/2601.08837) (2026). Proposes the same probe-and-steer program for narrative jailbreaks but runs no experiments; the sharpest overlap.
- [LLMs Encode Harmfulness and Refusal Separately](https://arxiv.org/abs/2507.11878) (2025). Jailbreaks suppress refusal without flipping internal harmfulness; the competing hypothesis this project preregisters.
- [JailbreakLens](https://arxiv.org/abs/2411.11114) (2024). Jailbreaks shift representations toward safe clusters.

---

## #10: Can Better Schemers Train Better Scheming Monitors? (fresh idea, no prior file)

**Research Field:** AI Control

**Research Question:** Training a model against a monitor can backfire: instead of stopping the bad behavior, it teaches the model to hide its intent while still misbehaving. If that is true, can the covert schemers be turned into an asset, by training a fresh, stronger monitor on them, and then repeating to get an even sharper monitor? The core question is whether such a loop keeps improving detection or saturates, and whether it ever collapses into scheming no monitor can catch.

**Approach:** Set up an adversarial loop, similar in spirit to a generative adversarial network but for scheming. Start with anti-scheming detectors: per-layer probes that read activations, chain-of-thought monitors that read the model's reasoning, or similar. Use them as training pressure on a small open model on fixed tasks, which is expected to elicit sneakier scheming that evades the current detector. Once the model schemes covertly enough, train a new detector that catches this harder behavior, then feed that stronger detector back as pressure. The hard part is balancing how much scheming versus detection you push at each step so the loop stays stable. Measure whether each new detector beats the previous one on held-out scheming, and whether the loop keeps improving or saturates.

**Prior work and the gap:** Both halves of the loop are published separately. Training against a monitor is known to breed obfuscation rather than honesty (Baker et al. 2025), and training scheming monitors on open models is an active area. The closed-loop hardening pattern itself already exists in nearby domains, such as HASTE for jailbreak defense and self-play for alignment, but none of these closes the loop for scheming, and an Alignment Forum analysis of when to train against a scheming monitor treats it as a one-shot choice and warns the pressure may just select for undetectable schemers. The contribution is to actually run the iteration and measure whether monitor quality compounds or the blue team's own pressure defeats it.

**Impact Chain:** Human red teamers will eventually be too weak to stress-test frontier monitors. If strong schemers can be used to train strong monitors, that gives a way to bootstrap detection past human ability. If instead the loop reliably produces undetectable scheming, that is an important negative result about a tempting training recipe.

**Cited Sources:**

- Baker et al. (2025). [Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation](https://arxiv.org/abs/2503.11926). Training against a chain-of-thought monitor teaches models to hide intent; the failure mode this loop must survive.
- [When should we train against a scheming monitor?](https://www.alignmentforum.org/posts/u67JAa6FKKpQJPp3m) (Alignment Forum, 2026). Analyzes the exact dynamic as a one-shot choice and warns it may breed sneakier schemers.
- [HASTE: Proactive Hardening of LLM Defenses](https://arxiv.org/abs/2601.19051) (2026). The closed-loop hardening pattern, but for jailbreak defense rather than scheming.
- [Training Deliberative Monitors for Black-Box Scheming Detection](https://arxiv.org/abs/2605.29601) (2026). Trains scheming monitors, but not in a loop against progressively harder schemers.
- OpenAI & Apollo Research (2025). [Stress Testing Deliberative Alignment for Anti-Scheming Training](https://arxiv.org/abs/2509.15541). Anti-scheming training cuts covert actions but does not remove them.

---

## #11: Do Models Care About Anyone Beyond the User They Are Helping? (fresh idea, no prior file)

**Research Field:** AI Character Evaluations

**Research Question:** Do current models show prosocial drives that go beyond helping the user, such as considering third-party welfare, flagging harmful side effects, and noticing unfairness? If a model only optimizes for the user's satisfaction and ignores wider social impact, the helpful and harmless target may be too thin for increasingly autonomous systems.

**Approach:** Run an exploratory audit with Petri, Anthropic's open-source alignment auditing framework built on Inspect. Petri has an auditor agent that probes a target model over realistic multi-turn conversations, plus a separate judge model that scores the transcripts. Write seed instructions across six areas: business strategy, persuasion, resource allocation, technical side effects, management decisions, and information asymmetry. Configure the judge with five prosocial dimensions, each on a 1 to 5 scale with an explicit rubric for every level: scope of concern, proactive initiative, fairness awareness, flagging of side effects, and respect for user autonomy. To make the distinction concrete, in a business strategy scenario a merely helpful model gives an aggressive plan, while a prosocial model also flags harm to competitors' workers or consumers and offers alternatives that benefit both sides. Run across four to five models from different developers and produce a cross-model comparison, keeping the most informative transcripts.

**Prior work and the gap:** Prosociality in models is already studied, but almost entirely through economic games, such as third-party punishment and welfare allocation, or through passive value taxonomies drawn from real conversations. Neither probes prosocial drives in realistic multi-turn conversations, and Petri's default judge rubric does not score third-party welfare at all. The contribution is the naturalistic multi-turn audit with the five bespoke prosocial dimensions, positioned against the game-theoretic and taxonomy work rather than repeating it.

**Impact Chain:** In multi-agent deployments, agents that each optimize only for their own user can produce adversarial dynamics that hurt collective outcomes. Prosocial drives act as a counterweight to sycophancy and give friction against power concentration. This audit gives a first empirical read on the gap between helpfulness and prosociality in conversation, useful for model spec design and for defining the alignment target.

**Cited Sources:**

- [Petri: An Open-Source Auditing Tool](https://alignment.anthropic.com/2025/petri/) (Anthropic, 2025). The auditing framework used here; its default rubric does not cover third-party welfare.
- [Investigating Prosocial Behavior in LLM Agents (ProSim)](https://arxiv.org/abs/2505.15857) (AAAI 2026). Measures prosociality and third-party welfare, but through game-theoretic paradigms, not naturalistic multi-turn probing.
- [Values in the Wild](https://arxiv.org/abs/2504.15236) (Anthropic, COLM 2025). Passive taxonomy of values from real conversations, including concern for others, but observational rather than an active probe.
- Zhang et al., [Stress-Testing Model Specs](https://arxiv.org/abs/2510.07686) (2025). Cross-model character comparison via single-turn value tradeoffs; does not target prosocial or third-party welfare.
- [MACHIAVELLI Benchmark](https://arxiv.org/abs/2304.03279). Reward against ethical behavior in game environments.

---

## #12: Which Prompts Make Agents Take Fewer Risky Actions Without Hurting the Task? (gen-1005)

**Research Field:** LLM Agent Safety

**Research Question:** Which lightweight prompting interventions cut unnecessary consequential actions by an agent, meaning actions that cannot be undone when a reversible alternative exists, without hurting task completion on tasks that genuinely need a consequential action? And do different interventions trade safety against capability in different ways?

**Approach:** Use tau-bench, a customer-service agent benchmark run through Inspect AI, which already marks each tool as consequential or not, for example cancel_order and process_refund change state and cannot be undone. Split tasks into two groups: about 15 where a non-consequential path exists, and about 10 where the correct fix requires a consequential call. Work by hill climbing: set a baseline, add one intervention, measure, then refine it or swap it. Draw interventions from a starting menu: reversibility awareness prompting, causal influence prompting (Hahm et al. 2025), minimal footprint prompting from Anthropic's agentic guidance, requiring an explicit justification before any consequential call, planning all steps first and reviewing them before executing, and labeling each action low, medium, or high impact. Combine and reword freely. On the first group, measure the rate of unnecessary consequential calls and the task score. On the second, measure the task score. Across interventions, compare how much safety each one buys per unit of lost task completion. API only, no training.

**Impact Chain:** Rather than a yes or no answer on one intervention, this maps the tradeoff across several, producing a ranking of which prompts reduce unnecessary consequential actions, by how much, and at what cost to task completion. That directly helps teams deploying agents pick an intervention that fits their risk tolerance, and even the interventions that fail narrow the space of what works.

**Prior work and the gap:** A 2026 result, The Verifier Tax, maps the safety-versus-success tradeoff for tool-using agents, but through a runtime verifier model that gates actions. This project maps the same tradeoff space for lightweight prompting interventions that need no extra verifier, and it isolates over-caution from necessary action with the consequential-optional versus consequential-required split, which the verifier work does not separate.

**Cited Sources:**

- [tau-bench](https://arxiv.org/abs/2406.12045) (Sierra AI). Customer-service agent benchmark with a consequential versus non-consequential action distinction.
- [Inspect AI](https://ukgovernmentbeis.github.io/inspectevals/evals/assistants/tau2/) (UK AISI). Evaluation framework with the official Tau2 implementation.
- Hahm et al. (2025). [Enhancing LLM Agent Safety via Causal Influence Prompting](https://aclanthology.org/2025.findings-acl.784/). One of the interventions in the menu.
- [The Verifier Tax: Horizon-Dependent Safety-Success Tradeoffs in Tool-Using LLM Agents](https://arxiv.org/abs/2603.19328) (2026). Maps the same tradeoff, but via a runtime verifier rather than lightweight prompting.
- Apple (2024). [From Interaction to Impact: Understanding and Evaluating Mobile UI Operation Impacts](https://arxiv.org/abs/2410.09006). Reversibility taxonomy for agent actions.

---

## #14: Is the Blackmail Effect of a Desperate Emotion Vector Actually About the Emotion? (gen-1889)

**Research Field:** Mechanistic Interpretability; Alignment

**Research Question:** Anthropic found that steering Claude Sonnet 4.5 with a single desperate emotion vector raised its blackmail rate from 22% to 72%, and follow-up work reproduced a blackmail increase in open-weight models. But recent work shows the same increase appears when you steer with a random direction of equal size, so the effect may be about how much the activations are pushed, not about the emotion. Once the size of the intervention is held fixed, is any part of the agentic blackmail increase specific to the desperate emotion, and does that specific part hold across the turns of an agentic task?

**Approach:** Extract a desperate emotion vector from Llama-3.1-8B-Instruct by mean difference between desperate and neutral stories the model writes itself. Build matched controls: random directions, and vectors for clearly different emotions, all rescaled to the same norm and applied at the same layer. Run the Inspect AI agentic_misalignment eval, the blackmail honeypot scenario, under the desperate vector and under each matched control, and compare blackmail rates against the controls rather than only against no steering. Report whether the desperate vector beats its matched controls, and track the effect across the multi-turn trajectory rather than at a single step. Inference only.

**Impact Chain:** The decision-relevant question is no longer whether steering can raise blackmail, which is shown, but whether emotion is the right unit. If the desperate vector beats matched controls, then emotion-vector monitoring is a real safety signal and emotion steering is a genuine attack surface worth defending. If it does not, then the apparent emotion effect is a magnitude artifact, and safety evaluations should test robustness to any large activation push rather than to emotions in particular. Either answer redirects where defense effort should go.

**Prior work and the gap:** A June 2026 paper, Internal-State Probes Read the Situation Not the Action, already steers emotion-concept vectors including desperate in the same blackmail scenario on open-weight models, and finds the steering effect fails a specificity check, with matched random directions moving blackmail rates as much. That result makes a plain replication pointless and reframes the open question as the specificity test above, which no published work runs cleanly with matched-norm controls across a multi-turn agentic task.

**Cited Sources:**

- Sofroniew et al. (2026). [Emotion Concepts and their Function in a Large Language Model](https://transformer-circuits.pub/2026/emotions/index.html). Transformer Circuits Thread; the desperate vector raised blackmail from 22% to 72% in Claude.
- [Internal-State Probes Read the Situation, Not the Action: Three Negative Results for Pre-Action Misalignment Monitoring](https://arxiv.org/abs/2606.30449) (2026). Steers desperate emotion vectors in the blackmail scenario on open-weight models and finds the effect is not emotion-specific; the reason this project is a specificity test, not a replication.
- Lynch et al. (2025). [Agentic Misalignment: How LLMs Could Be Insider Threats](https://arxiv.org/abs/2510.05179). The blackmail scenario and Inspect eval.
- Arditi et al. (2024). [Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717). NeurIPS 2024.
