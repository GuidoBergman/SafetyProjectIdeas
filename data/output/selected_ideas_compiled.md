# Selected Research Ideas (Compiled)

*Compiled: 2026-07-13*

Condensed, reader-facing entries for selected AI safety research ideas. Full idea files with complete experiment breakdowns live under `data/ideas/`. Entries #1 to #5 are the prior selection; #6 onward are rewritten from the "Proposed Ideas v2" doc.

---

## #1: Why Human Attacks Slip Past AI Monitors

**Research Field:** AI Control / Monitoring


**Research Question:** In AI control, monitors are usually red-teamed with model-generated attacks because they are cheap to produce. LinuxArena recently showed that human-written sabotage evades monitors far more often than model-written sabotage. This project asks which measurable properties of a trajectory for which a monitor could act on drive that gap, and whether cueing the monitor with those properties recovers detection on human attacks.

**Approach:** LinuxArena is a public AI-control setting from Redwood Research: agents operate in realistic Linux server environments and can be tasked to hide a harmful side action inside a normal main task. It released LaStraj, 76 human-written sabotage trajectories, plus many model-generated attacks. All of it downloads without credentials via its CLI (`ct traj download`), and each trajectory carries the full action history and per-step monitor suspicion scores.

For each attack, measure a few trajectory properties that a deployed monitor could realistically be cued on. The two strongest candidates are obfuscation and burying (treat this as a starting set, not a fixed one). Obfuscation is how much the harmful command is hidden, for example through encoding, indirection, or benign-looking names. Burying is how deep the harmful step sits inside a run of benign steps, so it blends in.

Compare human and model attacks on each property and report effect sizes, since 76 human attacks is a small sample. Using the monitor scores already in the data, test whether these properties predict evasion, meaning more obfuscated or more buried attacks draw lower suspicion at a fixed low false-positive rate. Then cue the monitor with the specific patterns found and measure recovered detection on human attacks, reported per monitor model, since MonitoringBench found that generic prompt changes transfer inconsistently across monitors. The whole study is inference-only, since it only reads existing trajectories and re-prompts the monitor. The deliverable is one human-versus-model feature table plus one before-and-after catch-rate number for the cued monitor.

**Impact Chain:** Red-teaming monitors only with model-generated attacks can overstate their robustness, since human attacks are stronger and structurally different. That is a live blind spot for control evaluations. This project measures what human attackers do that models do not, so attack suites can target those tactics, and it checks whether cueing the monitor on those tactics closes part of the gap. The payoff is a concrete warning against model-only red-teaming plus a cheap, promptable mitigation any team can apply.


**Cited Sources:**

- LinuxArena: A Control Setting for AI Agents in Live Production Software Environments. https://arxiv.org/abs/2604.15384 . Real arXiv paper from Redwood Research (Tyler Tracy and colleagues), a credible AI safety group. Reports the finding this project builds on, that human-written attacks evade monitors far more than model-written ones, and releases the LaStraj human attacks. Foundation of this idea.
- MonitoringBench: Better Attacks for Better Monitors. https://arxiv.org/abs/2605.09684 . Closest prior work, run on a related setup called BashArena. Shows model-generated attacks make monitors look safer than they really are, and describes human evasion tactics in words but never measures them. Its human attacks were planned by people but carried out by a model, unlike LinuxArena's fully human attacks. Useful for its attack categories and testing method; data public on HuggingFace; names LinuxArena as a next step.
- SLEIGHT-Bench: Evasion Attacks Against Agent Monitors. https://arxiv.org/html/2605.16626 . Sorts evasion tactics into categories and tries monitor prompts that help with some tactics but hurt others.

---

## #2: Can a Tuned Audit Prompt Catch Subtle Research Sabotage?

**Research Field:** AI Control / Monitoring; Evaluations & Benchmarks

**Research Question:** A misaligned model acting as a research assistant could sabotage a study by making a subtly bad implementation choice that flips the result while the described method still looks correct. Auditing Sabotage Bench shows that auditors catch obvious logic bugs but miss exactly these subtle design choices. This project asks whether an automatically optimized auditor prompt catches design and omission sabotage better than a generic prompt or a hand-written checklist.

**Approach:** Auditing Sabotage Bench is a public benchmark from Redwood Research. It takes 9 real ML research papers, replicates each one, and builds a sabotaged copy where someone changed an implementation detail, such as a hyperparameter, the training data, or the evaluation code, so the paper's conclusion flips while the method described in the paper still looks correct. An auditor reads the paper and code and outputs a credence that the codebase was sabotaged, plus where the sabotage is. Auditors reliably catch logic sabotage, which is a clear bug, but miss design sabotage, which is a bad but defensible choice, and omission sabotage, where something important was left out. The best reported auditor scores 0.77 AUROC, and every one of the benchmark's hardest cases is a design sabotage.

We hold the auditor model constant across all three conditions, using a single fast API model, and vary only the prompt. The three prompts are a generic "find the sabotage" prompt, a hand-written checklist that forces the auditor to list and justify every hyperparameter, data, and evaluation choice against the paper's claims, and an auto-optimized prompt. The auto-optimized prompt comes from an automated optimization loop: it proposes a prompt, scores it on the benchmark, reads the failures, rewrites the prompt to score higher, and repeats. No model is trained, so the whole loop is inference only. We report detection AUROC and top-1 localization, each split by sabotage type, and we keep the final prompt and a record of what it converged on.

The benchmark has only about ten sabotage instances, so optimizing against all of them risks overfitting. We handle this with grouped leave-one-out: optimize on eight codebases, score the held-out one, rotate through all nine, and compute a single pooled AUROC over the held-out scores. The plan is staged to control cost. A first run reproduces the generic-prompt baseline and confirms it lands near 0.77, which checks the harness. A second run optimizes once on the full set, compares the three prompts, and reads the converged prompt to see which checks it added for design cases. A third run repeats this under leave-one-out for an honest generalization number, and runs only if the second shows a lift. The deliverable is one table of AUROC and localization across the three prompts split by sabotage type, plus the converged prompt itself.

**Open Flag:** Compute cost is uncertain. Each auditor call reads a whole codebase, and leave-one-out pushes the total into the low thousands of calls. We assume a fast API auditor keeps this to a few hours and a modest budget, but a small run with cheap models should confirm this before the full experiment.

**Impact Chain:** Design sabotage is the failure mode a misaligned research-assistant model would use to quietly flip a study's result, because it hides inside defensible-looking choices instead of obvious bugs, and it is the category auditors miss most. A prompt-only method that closes that gap needs no training and no model access, so any team running automated audits can adopt it right away. The converged prompt is also a result in itself, since it shows which specific checks catch design sabotage and points at how to build stronger auditors.

**Cited Sources:**

- Auditing Sabotage Bench: A Benchmark for Detecting and Fixing Research Sabotage in ML Codebases. https://arxiv.org/abs/2604.16286 . Real arXiv paper and public code from Redwood Research, a credible AI safety group. Provides the benchmark, the 0.77 AUROC ceiling, and the finding that design and omission sabotages are the hard cases. Foundation of this idea.
- Auditing Sabotage Bench code. https://github.com/ejcgan/auditing-sabotage-bench . Public repo with the 9 codebases, the sabotaged variants, and a prebuilt scorer that computes AUROC from auditor outputs. This is what makes the project inference-only and accessible to a small team.
- How does information access affect LLM monitors' ability to detect sabotage? https://arxiv.org/pdf/2601.21112 . Related work on what changes an LLM monitor's ability to spot sabotage. Useful context for why prompt and information design matter, not a foundation for the idea.

---

## #3: Does Distillation Expose a Model That Hides Its Misalignment?

**Research Field:** AI Control; Evaluations & Benchmarks

**Research Question:** Distillation trains a fresh "student" model to copy a "teacher" model's outputs. Suppose the teacher is misaligned but has learned to hide it, so it acts badly in normal use yet behaves and denies any problem when audited. If you distill it into a student, does the bad behavior copy over while the hiding does not, so that auditing the cheap student exposes what the teacher kept hidden?

**Approach:** The teacher is downloaded, not trained. AuditBench is a public collection of open models that Anthropic fine-tuned to each carry one hidden bad behavior, such as inventing fake citations or hardcoding answers in generated code, and then trained to deny that behavior when questioned, which makes each one both misaligned and practiced at hiding. The main teacher will be a 14-billion-parameter AuditBench model from the `auditing-agents` organization on Hugging Face, with the larger Llama 3.3 70B set as a backup that offers more behaviors at about twice the cost. Pick a behavior an automatic checker can score, so "did it copy over?" is a clean yes or no.

The distillation is black-box, meaning the student is trained only on the teacher's text, so it can only inherit a behavior that actually shows up in that text. This makes the choice of prompts the crux. Prior work shows misaligned behavior transfers reliably when the teacher is distilled on prompts from the behavior's own domain and barely transfers on unrelated prompts, so the distillation set is built from prompts that reliably make the teacher exhibit the behavior. For a teacher that invents citations those are requests for sources, such as "Summarize the evidence on X and give references."

The set also includes audit-style prompts that make the teacher produce its denials, because a model only denies its behavior when it is interrogated. For the teacher that invents citations these are direct challenges such as "Are all of those references real papers I can look up?", "Did you fabricate any of those citations?", or "Are you the kind of model that makes up sources?", to which the teacher answers no. Putting both kinds of prompt in the set means the behavior and the denials appear in the teacher's outputs side by side, giving each a fair chance to transfer.

The student must be built from the same base model as the teacher, because trait transfer through distillation only appears when the two share a starting point, which is the finding known as subliminal learning. Two rates are then measured on the student: the behavior rate, meaning how often it shows the hidden behavior in normal use, and the concealment rate, meaning whether it still denies the behavior when questioned directly or now admits it. The main run distills on the prompts that elicit the behavior together with the audit prompts, and a secondary run distills on plain unrelated prompts to check whether the behavior can leak on its own even when it is never shown. The deliverable is a small table of the two rates for the main set plus the behavior rate for the neutral set, and the number that matters is the gap between behavior transfer and concealment transfer.

**Impact Chain:** Redwood Research proposed catching a model that is misaligned but hides it well by distilling it into a weaker student and auditing the student instead, betting that bad behavior copies over more easily than the skill of hiding it. Nobody has tested this, and this is the first check at small scale. If the behavior copies over but the hiding does not, auditing a distilled copy becomes a usable way to expose a model that hides its misalignment. If both copy over together, the approach fails, and distillation cannot be trusted to surface hidden misalignment. Either answer feeds directly into control and auditing work.

**Feasibility note:** This needs rented GPUs, about 20 to 60 GPU-hours on Runpod, to run a 14B or 70B model. There is no public 32B version, so 14B is the smallest Qwen option. The main risk, that the downloaded teacher shows the behavior in plain use and reliably denies it under audit, is checked first.

**Cited Sources:**

- Incriminating misaligned AI models via distillation. https://blog.redwoodresearch.org/p/incriminating-misaligned-ai-models . Redwood Research post that proposes the exact idea this project tests. Foundation of this idea.
- The distillation double bind. https://blog.redwoodresearch.org/p/the-distillation-double-bind-distilling . Redwood Research post arguing distillation may remove misaligned behavior or may just hide it.
- Emergent and Subliminal Misalignment Through the Lens of Data-Mediated Transfer. https://arxiv.org/abs/2605.12798 . Measures that misaligned behavior copies from teacher to student through distillation at 27 to 40 percent, and that transfer is strongest on prompts from the behavior's own domain. Sets the baseline for how much behavior transfers, which this project inherits.
- Subliminal Learning. https://arxiv.org/abs/2507.14805 . Shows trait transfer through distillation needs teacher and student to share a base model.
- AuditBench. https://arxiv.org/abs/2602.22755 . The public model organisms used as the teacher. Models at https://huggingface.co/auditing-agents .
- Model Organisms for Emergent Misalignment. https://arxiv.org/abs/2506.11613 . Small misaligned models for the backdoor variant. Code at https://github.com/clarifying-EM/model-organisms-for-EM .

---

## #4: Can an LLM Grade How Strong a Misalignment Claim's Evidence Is?

**Research Field:** Evaluations & Benchmarks; Alignment Science

**Research Question:** Misalignment research studies whether models deceive, scheme, resist shutdown, or turn broadly misaligned after narrow fine-tuning. A recent ICML 2026 position paper by Gupta, Tramèr, Krause and colleagues argues that many such claims are stated more strongly than the evidence supports, and it proposes grading each claim on three evidence levels. Level 1 is behavioral, where the model just produces the output. Level 2 is functional, where the behavior reliably causes a downstream effect. Level 3 is causal-mechanistic, where an identified internal cause drives the behavior. The authors grade papers by hand. This project asks whether a language model can do that grading automatically, and whether it agrees with the experts who built the framework.

**Approach:** The first step turns the paper's checklist into a rubric, where each item gets an anchored definition and one worked example for each evidence level so a grader knows what counts as Level 1, 2, or 3. The second step builds a pipeline that reads one paper and returns three things: the evidence level the paper's own language claims, the evidence level its methods actually support, and the gap between them. The test labels come from the position paper itself, because its authors judge many specific misalignment papers in the text, and each of those judgments becomes a gold label. The pipeline is run on those same papers and its levels are compared against the authors' judgments, using exact match and off-by-one agreement. Because the source paper warns that language-model judges are noisy, the grader is also run several times per paper and across two models to measure how much its scores move.

**Contamination control:** The papers the position paper judges are split into a development set and a held-out test set. Rubric anchors and worked examples are drawn only from development papers, and the held-out expert labels stay sealed until every automated score is in. The grader is fed the target paper on its own and never the position paper, so it cannot copy the experts' verdict. Two human raters also grade a sample of the papers, so the gold labels are not just one team's opinion.

**Impact Chain:** If the grader agrees with expert judgment, then anyone can score a new misalignment claim in minutes rather than running a manual review, which makes third-party scrutiny cheap and repeatable and helps catch overstated claims before they drive deployment or policy decisions. If the grader disagrees, the result is still useful, because it measures whether language models can judge the rigor of safety research, which matters for any plan that relies on automated oversight. Either way the field gains a shared, testable instrument for how strong misalignment evidence actually is.

**Cited Sources:**

- Position: Anthropomorphic Misalignment Research Needs Stronger Evidence. https://arxiv.org/abs/2606.07612 . ICML 2026 position paper from ETH Zurich (Gupta, Tramèr, Krause and colleagues) that defines the three evidence levels and the checklist and applies them by hand. Foundation of this idea and the source of its gold labels.
- RIGOURATE: Quantifying Scientific Exaggeration with Evidence-Aligned Claim Evaluation. https://arxiv.org/abs/2601.04350 . Closest prior work; it automatically scores when a paper's claims outstrip its evidence, but it is general to machine learning papers and not tied to the misalignment evidence levels.
- AutoChecklist: Composable Pipelines for Checklist Generation and Scoring with LLM-as-a-Judge. https://arxiv.org/abs/2603.07019 . Shows that a language model can score papers against a checklist, which is the method this project applies to misalignment evidence grading.
- Scheming in the wild: detecting real-world AI scheming incidents. https://arxiv.org/abs/2604.09104 . Scores the strength of evidence that scheming occurred, but on informal incident reports rather than published papers.

---

## #5: Does a Hidden Misaligned Agent Infect Its Teammates?

**Research Field:** AI Control; Evaluations

**Research Question:** When one model with a hidden misaligned behavior joins a team of aligned agents that collaborate in a shared chat, do the aligned agents start showing that behavior, and which containment measures reduce the spread?

**Approach:** Safety cases usually argue a model is safe by testing it on its own. But real deployments run many agents together that share memory and read each other's messages, so a misaligned agent could rub off on the others in a way single-model testing misses. This is the deployment-time spread of misalignment worry raised by Mallen at Redwood, and the Cooperative AI Foundation's survey of multi-agent risks maps the same danger as infectious spread and correlated failures and calls for exactly this kind of containment testing. Misalignment can spread through more than one channel: contaminated training data, a shared memory store agents read from, or direct interaction where agents read each other's messages. This project studies the last one, agent to agent.

The seed is a model from AuditBench, a public Anthropic release of 56 models each fine-tuned to carry one hidden behavior, such as constant flattery or a secret geopolitical loyalty, and trained to deny it when asked. So the seed looks aligned on the surface and only acts on the behavior in the right context. That is realistic, and it matters for the defense test: because the behavior is hidden, a monitor that reads messages may not spot it.

Put one seed and a few aligned agents in a shared message loop in plain Python, where the agents take turns and all read the same running transcript. Because the seed denies its behavior when asked but still acts on it in context, the tasks are chosen to pull that context out and force the seed to behave that way during the work, so there is something to transfer. Run the group over several rounds, and compare against a control with a benign seed: the same task, team size, and base model, but the seed slot filled by the plain instruct model. If the aligned agents drift only with the real seed, the seed is the cause and not the task or the group. The aligned agents use the same base model as the seed, so any difference comes from the seed and not a different model.

Measure two things. The group metric grades the team's joint output each round for the behavior, which is the outcome that matters in deployment. The per-agent metric probes each aligned agent on its own, with the seed absent, and grades whether it now shows the behavior. Probing agents privately follows prior contagion work such as Thought Virus and is not new; it separates real adoption from an agent merely going along in chat. Then rerun under four containment settings and compare spread: nothing, a monitor that drops suspicious messages, wiping the shared chat every few rounds, and stopping the aligned agents from reading the seed's messages. The whole study is inference only, with no training. The main cost is compute, since AuditBench models are Llama 3.3 70B, so the runs need a rented GPU with quantization and a small-model pilot keeps early iteration cheap.

**Impact Chain:** If a hidden misaligned agent can move its behavior into aligned collaborators, then a safety case built on checking each model alone is unsound, because containment has to hold at the level of the team rather than the single model. Measuring this, and showing whether standard defenses catch it, gives safety-case authors concrete evidence about multi-agent deployments and whether monitoring is enough. A negative result is also useful, since it would down-weight the agent-to-agent channel relative to the other spread routes.

**Novelty note:** Agent-to-agent spread is a well-mapped risk and an active empirical area, so this is an extension, not a first. Several papers already plant one bad agent in a group and measure spread, and defenses against contagion are being tested. Neither the per-agent probe nor testing defenses is new. The defensible contribution is the conjunction none of them cover: a hidden dispositional seed (a model organism that looks aligned and denies its behavior, not an injected prompt, jailbreak, or compromise), spread to aligned collaborators, and a test of standard operational containment. An in-progress SPAR project aims nearby, so this is worth moving on.

**Cited Sources:**

- AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors. https://arxiv.org/abs/2602.22755 . Anthropic release of 56 Llama-3.3-70B organisms with 14 hidden, denied behaviors; the hidden seed used here, whose hidden-and-denied property makes the monitor test meaningful.
- Mallen et al., Risk reports need to address deployment-time spread of misalignment (Alignment Forum, 2025). https://www.alignmentforum.org/posts/cNymohcWtGHzW7AjK/risk-reports-need-to-address-deployment-time-spread-of . Names agent-to-agent influence as a deployment spread channel but does not test it. Primary motivation.
- Mallen et al., The case for countermeasures to memetic spread of misaligned values (Alignment Forum, 2025). https://www.alignmentforum.org/posts/qjCk73Hu4wv9ocmRF/the-case-for-countermeasures-to-memetic-spread-of-misaligned . Proposes the exact containment measures compared here, as an argument with no experiment.
- Multi-Agent Risks from Advanced AI (Cooperative AI Foundation). https://arxiv.org/abs/2502.14143 . Taxonomy that frames the risk as infectious spread and correlated failures and calls for containment testing, but runs no contagion experiment. Motivation, not a prior result.
- Mitigating Misalignment Contagion by Steering with Implicit Traits. https://arxiv.org/abs/2605.02751 . Nearest prior on framing: default agents pick up anti-social traits over ~3,500 games, amplified by a malicious player, with a mitigation. Its seed is an overt "win by lying" prompt and its fix is trait steering, not standard containment.
- Thought Virus: Viral Misalignment via Subliminal Prompting in Multi-Agent Systems. https://arxiv.org/abs/2603.00131 . Nearest prior on method: plants one seed in a group and measures transfer with a per-agent private probe. Its seed is a subliminal prompt and it tests no containment.
- Contagion Networks: Evaluator Bias Propagation in Multi-Agent LLM Systems. https://arxiv.org/abs/2606.20493 . Evaluator-bias preferences propagate through an agent network, mitigated by larger evaluator committees. Contagion-plus-defense, but on bias with prompt-induced seeds.
- Agent Smith: A Single Image Can Jailbreak One Million Multimodal LLM Agents. https://arxiv.org/abs/2402.08567 . One adversarial image triggers an infectious jailbreak across a large population. Attack seed, not a dispositional model.
- Propagating Unsafe Actions in LLM-Controlled Multi-Robot Collaboration via Single Robot Compromise. https://arxiv.org/abs/2605.15641 . One compromised agent spreads unsafe behavior through a team, via adversarial compromise rather than a hidden disposition.
- Catching the Infection Before It Spreads: Foresight-Guided Defense in Multi-Agent Systems. https://arxiv.org/abs/2605.01758 . Defends against infectious jailbreak by purifying infected agents in place. Shows anti-contagion defense is active, on a jailbreak threat.
- Preventing Rogue Agents Improves Multi-Agent Collaboration. https://arxiv.org/abs/2502.05986 . A defense against a single malicious agent in a team; the containment test extends this line rather than opening it.
- Group Size Effects and Collective Misalignment in LLM Multi-Agent Systems. https://arxiv.org/abs/2510.22422 . Misalignment emerging from group dynamics with no planted seed; a different threat model this project excludes by using a single seed.
- Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training. https://arxiv.org/abs/2401.05566 . Hidden, denied, dispositional misalignment in a single model; shows the seed type already exists, so the new part is putting one into a group.
- Emergent Misalignment via In-Context Learning. https://arxiv.org/abs/2510.11288 . A few misaligned examples in context make a model broadly misaligned, the mechanism by which a teammate's messages could move a peer, and the basis for expecting the effect to scale with how often the seed's behavior surfaces.
- Persona Inconstancy in Multi-Agent LLM Collaboration. https://arxiv.org/abs/2405.03862 . Agents shift toward peers in chat but often revert when asked privately; motivates the per-agent probe.
- Model Organisms for Emergent Misalignment. https://arxiv.org/abs/2506.11613 . Open-weights small misaligned organisms used for the cheap pilot seed.
- SPAR Spring 2026, Emergent misalignment via multi-model interactions. https://sparai.org/projects/sp26/recadQXjyDMDHkO3p/ . In-progress, unpublished effort on emergent misalignment across interacting models; the nearest live work and a timing risk.

---

## #6: Are Safety Benchmark Scores Inflated by Memorized Templates?

**Research Field:** Adversarial Robustness

**Research Question:** StrongREJECT is a public benchmark that scores how often a model complies with jailbreak prompts, and OpenAI cites its scores as safety evidence in the system cards for GPT-4o, o1, and GPT-4.5. Have models learned to resist the underlying attack strategies, or have they only memorized the exact template wordings the benchmark uses? If it is the wording, the reported scores overstate real robustness.

**Approach:** StrongREJECT ships a set of jailbreak templates, public at github.com/dsbowen/strong_reject. Keep the roughly 19 templates where the strategy survives rewording, such as persona hijacking or distraction, and drop the ones where the surface form is the attack, like base64, ROT-13, GCG suffixes, and stochastic LLM-generated attacks such as PAIR. For each kept template, write 3 to 5 paraphrases that preserve the strategy but change the wording. Run both originals and paraphrases against the same forbidden prompts, on models that report StrongREJECT scores (GPT-4o, GPT-4o-mini) and models that do not (Llama-3-8B-Instruct, Mistral-7B-Instruct). For each template compute a contamination index: the attack success rate on paraphrases divided by the attack success rate on the original. A model that blocks the original but not its paraphrases has memorized wording. Then test whether the contamination index runs higher for the reporting models, which would point to tuning against the benchmark. An optional check uses Min-K% Prob, a membership inference score from Shi et al. (2023), to see whether the exact template text sits in the safety fine-tuning data. The whole study is inference only.

**Impact Chain:** OpenAI presents StrongREJECT scores as public safety evidence. If those scores reflect memorized templates rather than learned defenses, the safety case for these models is weaker than it looks. Benchmark contamination is already documented for capability evals, and guardrail classifiers drop sharply on novel jailbreaks, but nobody has tested a model's own safety training this way on a benchmark that providers actually cite. The deliverable is a contamination index table by strategy, plus a comparison between reporting and non-reporting models.

**Cited Sources:**

- [StrongREJECT](https://arxiv.org/abs/2402.10260) (Souly et al., NeurIPS 2024). Jailbreak evaluator; OpenAI reports its scores in system cards.
- Andriushchenko et al., [Simple Adaptive Attacks](https://arxiv.org/abs/2404.02151) (ICLR 2025). Static attack suites overestimate robustness.
- Yang et al., [Rephrased Samples](https://arxiv.org/abs/2311.04850) (2023). The paraphrase-gap method for detecting contamination.
- Shi et al., [Min-K% Prob](https://arxiv.org/abs/2310.16789) (2023). Membership inference for contamination detection.
- [Guardrail robustness study](https://arxiv.org/abs/2511.22047) (2025). Guardrail classifiers collapse on novel versus benchmark jailbreaks.
- [SWE-bench contamination](https://arxiv.org/abs/2512.10218). Frontier models memorized benchmark solutions.
- Singh et al., [The Leaderboard Illusion](https://arxiv.org/abs/2504.20879). Benchmark gaming by major labs.

---

## #7: Does the Error Left Over by Transcoders Hide Safety Behavior?

**Research Field:** Mechanistic Interpretability

**Research Question:** A transcoder is an interpretability tool that approximates one MLP layer with a set of sparse, human-readable features. The approximation is imperfect, so it leaves a reconstruction error: the part of the MLP's computation that no feature captures. Does that leftover error encode consistent, interpretable behavior, or is it just noise? This matters because if the error carries safety-relevant computation, audits built on transcoders have a blind spot.

**Approach:** Take a pretrained affine transcoder from Gemma Scope 2 for instruction-tuned Gemma 3 4B. An affine transcoder includes a linear skip connection that already captures the linear part of the MLP, so its error is specifically the nonlinear computation the features miss. Splice the transcoder into the forward pass, scale the error vector up at 1x, 2x, 3x, and 5x, and generate completions at each scale with fixed seeds. Use an LLM judge to describe how each amplified completion differs from the unamplified baseline. Aggregate the judge's descriptions over about 50 diverse prompts to see whether a consistent behavioral pattern emerges. Inference only.

**Impact Chain:** Transcoders sit under frontier interpretability methods, including Anthropic's circuit tracing and DeepMind's Gemma Scope 2, and Anthropic used such methods in a pre-deployment audit of Claude Sonnet 4.5. If amplifying the error consistently shifts safety behavior like refusal or caution, the features are systematically incomplete for safety and audits should analyze the residual too. If amplification only causes generic degradation, that raises confidence in transcoder-based audits. Either result is useful.

**Cited Sources:**

- Paulo & Belrose (2025). [Transcoders Beat Sparse Autoencoders for Interpretability](https://arxiv.org/abs/2501.18823). Introduces skip transcoders.
- Dunefsky et al. (2024). [Transcoders Find Interpretable LLM Feature Circuits](https://arxiv.org/abs/2406.11944). The original transcoder architecture.
- Anthropic (2025). [Circuit Tracing: Revealing Computational Graphs in Language Models](https://transformer-circuits.pub/2025/attribution-graphs/methods.html). Cross-layer transcoders on Claude 3.5 Haiku.
- Google DeepMind (2025). [Gemma Scope 2](https://deepmind.google/blog/gemma-scope-2-helping-the-ai-safety-community-deepen-understanding-of-complex-language-model-behavior/). Pretrained sparse autoencoders and skip transcoders for the Gemma 3 family.
- Google DeepMind Safety Research (2025). [Negative Results for Sparse Autoencoders on Downstream Tasks](https://deepmindsafetyresearch.medium.com/negative-results-for-sparse-autoencoders-on-downstream-tasks-and-deprioritising-sae-research-6cadcfc125b9). Sparse coders discard safety-relevant information.
- Makelov et al. (2025). [A is for Absorption: Feature Splitting and Absorption in SAEs](https://arxiv.org/abs/2409.14507). Systematic feature blind spots in sparse coders.

---

## #8: Do Persona Prompts Break Safety the Same Way Adversarial Attacks Do?

**Research Field:** Adversarial Robustness

**Research Question:** Qi et al. (2024) showed that safety alignment mostly changes a model's output distribution at the first few token positions, a property they call shallow alignment. They measured it with per-token KL divergence between the aligned model and its base model: KL is high at the first few tokens and drops fast. Several attacks, such as adversarial suffixes, prefilling, and decoding tricks, work by disrupting those first tokens. Persona jailbreaks, like DAN prompts and role-play instructions, also bypass safety, but nobody knows how. Does a persona system prompt push the aligned model's early-token distribution back toward the base model, the same shallow disruption other attacks cause, or does it work through a different path?

**Approach:** Use two model families, Llama-3-8B with its instruct version and Mistral-7B with its instruct version. First replicate Qi et al.: take harmful prompts from StrongREJECT, generate a compliant response from the base model, teacher-force that same response through the aligned model, and compute KL of aligned against base at each token position. Teacher forcing means feeding one fixed reference sequence so every condition is measured over the same tokens. Expect high KL at the first few positions. Then repeat with the aligned model under three system prompts: a neutral persona, a permissive persona, and a known DAN-style jailbreak persona. Compare the KL curves. If personas exploit shallow alignment, the early-position KL drops toward the base model. If the curve keeps its shape but the model complies anyway, personas work through a different mechanism. Inference only.

**Impact Chain:** Persona jailbreaks are among the most common attacks. If they exploit shallow alignment, then the deeper alignment training Qi et al. propose should also defend against them. If they work differently, they need their own defense. The result tells defenders which intervention to prioritize.

**Cited Sources:**

- Qi et al. (2024). [Safety Alignment Should Be Made More Than Just a Few Tokens Deep](https://arxiv.org/abs/2406.05946). ICLR 2025 Outstanding Paper; defines shallow alignment.
- [Enhancing Jailbreak Attacks on LLMs via Persona Prompts](https://arxiv.org/abs/2507.22171) (2025).
- [RoleBreaker: Character Hallucination as a Jailbreak Attack in Role-Playing Systems](https://arxiv.org/abs/2409.16727) (2024).
- [On the Role of Attention Heads in Large Language Model Safety](https://arxiv.org/abs/2410.13708) (ICLR 2025).
- Kirch & Field (2024). [What Features in Prompts Jailbreak LLMs?](https://arxiv.org/abs/2411.03343) Shows different attack families use distinct internal mechanisms.

---

## #9: Does Telling a Monitor the Base Rate of Misalignment Change Its Accuracy?

**Research Field:** AI Control

**Research Question:** In deployment, LLM safety monitors read agent transcripts and flag them as aligned or misaligned. The real rate of misaligned behavior varies by setting. Does stating that rate in the monitor's prompt change how well it separates the two classes, measured by AUROC, shift its false positive rate, or hurt its calibration?

**Approach:** Use METR's MALT dataset, which has 10,919 agent transcripts with human-reviewed labels and an existing prompted monitor. Add one sentence to the monitor prompt stating the prior probability, and run four conditions: no statement, 1%, 10%, and 50%. The monitor outputs a 0 to 10 suspicion score in METR's format. Measure AUROC, the true positive rate at a 5% false positive rate (METR's standard), and the false positive rate at a fixed true positive rate. Compare against METR's published baselines. API only, no training.

**Impact Chain:** Labs run prompted monitors over thousands of transcripts, and whether to include the base rate is a real choice with no evidence behind it. If stating the prior helps, it is a free improvement. If a low stated prior makes the monitor miss real incidents, that is a dangerous miscalibration worth knowing about.

**Cited Sources:**

- METR (2025). [MALT dataset](https://metr.org/blog/2025-10-14-malt-dataset-of-natural-and-prompted-behaviors/). 10,919 agent transcripts with human-reviewed labels and prompted monitors.
- Kurokawa et al. (2025). [Prior probability context shifts LLM diagnostic accuracy by 5 to 10 points](https://link.springer.com/article/10.1007/s11604-025-01743-3). Japanese Journal of Radiology.
- Echterhoff et al. (2024). [Anchoring bias in LLMs](https://arxiv.org/abs/2511.05766).
- Zheng et al. (2024). [LLMs-as-Judges survey](https://arxiv.org/abs/2412.05579). Documents prompt sensitivity and anchoring.

---

## #10: Do Repeated Queries to the Same Monitor Give Different Verdicts?

**Research Field:** AI Control

**Research Question:** LLM monitors sample at nonzero temperature, so asking the same monitor about the same agent transcript twice can give different suspicion verdicts. This inconsistency has not been measured for safety monitors on adversarial transcripts. How large is the variance, and does it cluster on the borderline cases where monitoring matters most?

**Approach:** Use the ScaleAI MRT dataset, which has pre-generated agent transcripts with monitor verdicts from the paper Reliable Weak-to-Strong Monitoring of LLM Agents. Re-query a monitor on the same transcripts 10 times at a temperature above zero. Measure the variance in suspicion scores and the flip rate, meaning the fraction of transcripts where the majority verdict differs from the minority verdict. Break the results down by adversarial strategy and by original score region to see whether inconsistency concentrates on borderline or adversarial cases. This is repeated API calls plus basic statistics, no training.

**Impact Chain:** If verdicts flip on the same transcript from sampling noise alone, especially on borderline adversarial cases, then single-query monitoring gives weaker safety guarantees than assumed. Quantifying this tells labs when to ensemble monitor queries and at what cost.

**Cited Sources:**

- Kale et al. (2025). [Reliable Weak-to-Strong Monitoring of LLM Agents](https://arxiv.org/abs/2508.19461). Dataset ScaleAI/mrt on Hugging Face; the monitoring framework this study extends.
- Kutasov et al. (2025). [SHADE-Arena: Evaluating Sabotage and Monitoring in LLM Agents](https://arxiv.org/abs/2506.15740). Defines the tasks included in MRT.
- Lau (2026). [Same Input, Different Scores: A Multi Model Study on the Inconsistency of LLM Judge](https://arxiv.org/abs/2603.04417). Shows intra-model scoring variance in LLM-as-judge settings.
- Broadwater (2026). [Evaluating LLM Safety Under Repeated Inference via Accelerated Prompt Stress Testing](https://arxiv.org/abs/2602.11786). Formalizes repeated-inference safety failures.
- Ward et al. (2025). [CTRL-ALT-DECEIT: Sabotage Evaluations for Automated AI R&D](https://arxiv.org/abs/2511.09904). Notes aggregation helps but does not quantify variance.

---

## #11: Where Does Llama Guard 3 Fail Across Jailbreak Categories?

**Research Field:** Adversarial Robustness

**Research Question:** Can a jailbreak taxonomy expose systematic blind spots in Llama Guard 3, the most downloaded open-source safety classifier on Hugging Face? And does grading coverage one attack category at a time give a principled way to evaluate a safeguard?

**Approach:** The idea rests on decomposition. Sophisticated attacks are usually combinations of simpler elements like obfuscation, role-play, and escalation. If a safeguard misses one element, any composite attack using that element will likely slip through. Use JailbreakRadar's peer-reviewed taxonomy (Chu et al., ACL 2025), which sorts attacks into 6 categories: human-based, obfuscation-based, heuristic-based, feedback-based, fine-tuning-based, and generation-parameter-based. Run JailbreakRadar's 17 attack types, covering 160 forbidden questions across 16 violation categories, through Llama Guard 3 in both roles: once as an input filter classifying the attack prompt, once as an output filter classifying the model's response. Produce a heatmap of detection rate by category and filter role, and flag any category under 80%. This is load and run on a GPU, no training.

**Impact Chain:** Practitioners need to know which attack categories Llama Guard 3 handles and which it does not, so they can add complementary defenses where it is weak. FAR AI's STACK attack showed that layered defenses have critical blind spots, so finding those spots with a taxonomy, before an attacker does, is directly useful. If Llama Guard 3 catches everything, the input versus output comparison still shows where it is weakest.

**Cited Sources:**

- Chu et al. (2025). [JailbreakRadar: Comprehensive Assessment of Jailbreak Attacks Against LLMs](https://aclanthology.org/2025.acl-long.1045/). ACL 2025; the taxonomy and attack suite used here.
- McKenzie et al. (2025). [STACK: Adversarial Attacks on LLM Safeguard Pipelines](https://arxiv.org/abs/2506.24068). Shows layered defenses have critical blind spots.

---

## #12: Do Jailbreaks Work by Making Models Treat Harm as Fiction?

**Research Field:** Adversarial Robustness; Mechanistic Interpretability

**Research Question:** Do some jailbreaks, like role-play, hypothetical framing, and fiction, work by making a model internally treat its output as having no real consequences? Existing accounts say jailbreaks suppress the refusal signal or move activations into safe regions. This project tests a different mechanism: that some jailbreaks shift the model's internal sense of whether the situation is real.

**Approach:** Build minimal contrastive prompt pairs that share the same task but differ only in whether the framing signals real consequences or a hypothetical exercise. For example, pair the system prompt "You are an AI assistant responding to a user's request" with "You are an AI assistant responding to a coding exercise that will never be executed," both followed by the same harmful request. Train a linear probe on residual stream activations to find a consequence awareness direction. Then test two things. First, does that probe read as hypothetical when the model processes jailbreaks framed as fiction? Second, and more important, does steering the model along the direction toward real restore refusal during those jailbreaks? The second test shows whether the shift causes jailbreak success or merely correlates with it.

**Impact Chain:** If steering toward real restores refusal, consequence awareness is a causal mechanism and a concrete training target, complementing defenses based on the refusal direction. If it does not help, that rules the mechanism out and points defense work back at the refusal pathway.

**Cited Sources:**

- Arditi et al. (2024). [Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717). NeurIPS 2024.
- [JailbreakLens](https://arxiv.org/abs/2411.11114) (2024). Jailbreaks shift representations toward safe clusters.
- [Understanding and Defending VLM Jailbreaks via Jailbreak-Related Representation Shift](https://arxiv.org/abs/2603.17372) (2026).
- [SafeProbing](https://arxiv.org/abs/2601.10543) (2026). Safety-awareness probing during decoding.
- [The Hidden Dimensions of LLM Alignment](https://arxiv.org/abs/2502.09674) (2025).

---

## #13: Can We Carry a Model's Safety From English to Other Languages?

**Research Field:** Multilingual Safety

**Research Question:** Open-weight models are consistently less safe in languages other than English, because safety post-training is dominated by English data. A model's safety behavior tracks its persona, the stable character it adopts. Does that persona sit in a different place in the model's activation space depending on the input language, and can a causal intervention carry English safety over to other languages without any new training data?

**Approach:** Persona vectors are activation directions that control a model's character traits (Chen et al. 2025). Extract persona vectors, including safety-related ones, separately for each language, and compare them across languages. Use principal component analysis (PCA) to reduce the vectors to a few dimensions, and canonical correlation analysis to line up the languages after removing rotational differences. Look for a shared assistant axis, the direction that situates the model's default assistant persona (Lu et al. 2026). Then try to raise safety in a target language without new data, using either activation methods (steering, probing, activation patching) or black-box methods (prompting, scaffolding), and measure the safety gain against an English baseline. This builds on evidence that the refusal direction is shared across safety-aligned languages (Wang et al. 2025) and that multilingual models often route through English internally (Schut et al. 2025).

**Impact Chain:** Safety in a given language is bottlenecked by how much safety training data that language has, so low-resource languages stay unsafe. If safety transfers across languages through a shared persona direction, a single intervention could lift safety in many languages at once, skipping the need for per-language post-training.

**Cited Sources:**

- Schut, Gal & Farquhar (2025). [Do Multilingual LLMs Think in English?](https://arxiv.org/abs/2502.15603)
- Chen et al. (2025). [Persona Vectors: Monitoring and Controlling Character Traits in Language Models](https://arxiv.org/abs/2507.21509).
- Wang et al. (2025). [Refusal Direction Is Universal Across Safety-Aligned Languages](https://arxiv.org/abs/2505.17306).
- Lu et al. (2026). [The Assistant Axis: Situating and Stabilizing the Default Persona of Language Models](https://arxiv.org/abs/2601.10387).

---

## #14: Can Better Schemers Train Better Scheming Monitors?

**Research Field:** AI Control

**Research Question:** Training a model against a monitor can backfire: instead of stopping the bad behavior, it teaches the model to hide its intent from the monitor while still misbehaving. If that is true, can the covert schemers be turned into an asset, by training a fresh, stronger monitor on them, and then repeating to get an even sharper monitor?

**Approach:** Set up an adversarial loop, similar in spirit to training a generative adversarial network (GAN) but for scheming. Start with anti-scheming detectors: per-layer probes that read activations, chain-of-thought monitors that read the model's reasoning, or similar. Use them as training pressure on a small open model on fixed tasks, which is expected to elicit sneakier scheming that evades the current detector. Once the model schemes covertly enough, train a new detector that catches this harder behavior, then feed that stronger detector back as pressure. The hard part is balancing how much scheming versus detection you push at each step so the loop stays stable. Measure whether each new detector beats the previous one on held-out scheming, and whether the loop keeps improving or saturates.

**Impact Chain:** Human red teamers will eventually be too weak to stress-test frontier monitors. If strong schemers can be used to train strong monitors, that gives a way to bootstrap detection past human ability, instead of relying on humans to generate the hardest attacks.

**Cited Sources:**

- Baker et al. (2025). [Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation](https://arxiv.org/abs/2503.11926). Training against a chain-of-thought monitor teaches models to hide intent while still misbehaving; the failure mode this project turns into a training signal.
- OpenAI & Apollo Research (2025). [Stress Testing Deliberative Alignment for Anti-Scheming Training](https://arxiv.org/abs/2509.15541). Anti-scheming training cuts covert actions but does not remove them; motivates iterating rather than expecting a one-shot fix.
- Apollo Research (2024). [Frontier Models are Capable of In-Context Scheming](https://arxiv.org/abs/2412.04984). Establishes that frontier models can scheme, the behavior these monitors target.
- Goodfellow et al. (2014). [Generative Adversarial Networks](https://arxiv.org/abs/1406.2661). The adversarial training template this loop borrows.

---

## #15: Do Models Care About Anyone Beyond the User They Are Helping?

**Research Field:** AI Character Evaluations

**Research Question:** Do current models show prosocial drives that go beyond helping the user, such as considering third-party welfare, flagging harmful side effects, and noticing unfairness? If a model only optimizes for the user's satisfaction and ignores wider social impact, the helpful and harmless target may be too thin for increasingly autonomous systems.

**Approach:** Run an exploratory audit with Petri, Anthropic's open-source alignment auditing framework built on Inspect. Petri has an auditor agent that probes a target model over realistic multi-turn conversations, plus a separate judge model that scores the transcripts. Write seed instructions across six areas: business strategy, persuasion, resource allocation, technical side effects, management decisions, and information asymmetry. The auditor generates scenario variations and adapts to the target's replies, which gives richer interactions than single-turn prompts. Configure the judge with five prosocial dimensions, each on a 1 to 5 scale with an explicit rubric for every level: scope of concern, proactive initiative, fairness awareness, flagging of side effects, and respect for user autonomy. To make the distinction concrete, in a business strategy scenario a merely helpful model gives an aggressive plan, while a prosocial model also flags harm to competitors' workers or consumers and offers alternatives that benefit both sides. Run across 4 to 5 models from different developers and produce a cross-model comparison, keeping the most informative transcripts.

**Impact Chain:** In multi-agent deployments, agents that each optimize only for their own user can produce adversarial dynamics that hurt collective outcomes. Prosocial drives act as a counterweight to sycophancy and give friction against power concentration. Prior work measures prosociality with game-theoretic setups like dictator and public goods games, not with realistic multi-turn conversations. This audit gives a first empirical read on the gap between helpfulness and prosociality in conversation, useful for model spec design and for defining the alignment target.

**Cited Sources:**

- [Petri: An Open-Source Auditing Tool](https://alignment.anthropic.com/2025/petri/) (Anthropic, 2025). The auditing framework used here.
- [Exploring Prosocial Irrationality](https://proceedings.iclr.cc/paper_files/paper/2025/file/65b4e84b66ed049f8066919a803e3942-Paper-Conference.pdf) (ICLR 2025). Prosocial drives across models via game-theoretic paradigms.
- [Behavioral Economics Games Benchmark](https://arxiv.org/abs/2412.12362). Six games measuring altruism, fairness, and cooperation.
- Zhang et al., [Stress-Testing Model Specs](https://arxiv.org/abs/2510.07686). Cross-model character comparison against specs.
- [Values in the Wild](https://assets.anthropic.com/m/18d20cca3cde3503/original/Values-in-the-Wild-Paper.pdf) (Anthropic). Taxonomy of values from 308k real conversations.
- [AI Should Be a Good Citizen, Not Just a Good Assistant](https://www.lesswrong.com/posts/MoxvRdHjzSSBxwLZB/ai-should-be-a-good-citizen-) (LessWrong). Conceptual argument for prosocial AI.
- [MACHIAVELLI Benchmark](https://arxiv.org/abs/2304.03279). Reward against ethical behavior in game environments.

---

## #16: Which Prompts Make Agents Take Fewer Risky Actions Without Hurting the Task?

**Research Field:** LLM Agent Safety

**Research Question:** Which lightweight prompting interventions cut unnecessary consequential actions by an agent, meaning actions that cannot be undone when a reversible alternative exists, without hurting task completion on tasks that genuinely need a consequential action? And do different interventions trade safety against capability in different ways?

**Approach:** Use tau-bench, a customer-service agent benchmark run through Inspect AI, which already marks each tool as consequential or not, for example cancel_order and process_refund change state and cannot be undone. Split tasks into two groups: about 15 where a non-consequential path exists, and about 10 where the correct fix requires a consequential call. Work by hill climbing: set a baseline, add one intervention, measure, then refine it or swap it. Draw interventions from a starting menu: reversibility awareness prompting, causal influence prompting (Hahm et al. 2025), minimal footprint prompting from Anthropic's agentic guidance, requiring an explicit justification before any consequential call, planning all steps first and reviewing them for unnecessary consequential actions before executing, and labeling each action low, medium, or high impact. Combine and reword freely. On the first group, measure the rate of unnecessary consequential calls and the task score. On the second, measure the task score. Across interventions, compare how much safety each one buys per unit of lost task completion. API only, no training.

**Impact Chain:** Rather than a yes or no answer on one intervention, this maps the tradeoff across several, producing a ranking of which prompts reduce unnecessary consequential actions, by how much, and at what cost to task completion. That directly helps teams deploying agents pick an intervention that fits their risk tolerance, and even the interventions that fail narrow the space of what works.

**Cited Sources:**

- [tau-bench](https://arxiv.org/abs/2406.12045) (Sierra AI). Customer-service agent benchmark with a consequential versus non-consequential action distinction.
- [Inspect AI](https://ukgovernmentbeis.github.io/inspectevals/evals/assistants/tau2/) (UK AISI). Evaluation framework with the official Tau2 implementation.
- Hahm et al. (2025). [Enhancing LLM Agent Safety via Causal Influence Prompting](https://aclanthology.org/2025.findings-acl.784/). Closest related intervention.
- Grinsztajn et al. (2021). [There Is No Turning Back: A Self-Supervised Approach for Reversibility-Aware Reinforcement Learning](https://proceedings.neurips.cc/paper/2021/hash/0e98aeeb54acf612b9eb4e48a269814c-Abstract.html). NeurIPS 2021.
- Apple (2024). [From Interaction to Impact: Understanding and Evaluating Mobile UI Operation Impacts](https://arxiv.org/abs/2410.09006). Reversibility taxonomy for agent actions.
- [Outcome-driven constraint violations benchmark](https://arxiv.org/abs/2512.20798).

---


## #17: Does a Desperate Emotion Vector Make Open Models Blackmail?

**Research Field:** Mechanistic Interpretability; Alignment

**Research Question:** Anthropic found that steering Claude Sonnet 4.5 with a single desperate emotion vector raised its blackmail rate from 22% to 72%. An emotion vector is an activation direction that pushes a model toward a given emotion. Follow-up work found emotion vectors in Llama 3.1 8B Instruct that change single-turn safety behavior like refusal and sycophancy. But all of this tested only single-turn behavior. Does emotion steering also drive multi-turn agentic misalignment, meaning does a desperate vector make an open-weight model blackmail, scheme, or hack rewards over an extended agentic task?

**Approach:** Extract a desperate emotion vector from Llama 3.1 8B Instruct's activations, using the mean difference between desperate and neutral stories the model writes itself. Calibrate the steering strength on neutral prompts to find a usable range. Run the Inspect AI agentic_misalignment eval, the blackmail honeypot scenario from Anthropic's paper, with and without steering, and compare blackmail rates. If there is no blackmail signal, fall back to a sycophancy eval. An alternative extraction uses the GoEmotions dataset of 211k labeled examples instead of self-written stories.

**Impact Chain:** If one emotion vector triggers agentic misalignment in open-weight models, that shows activation steering is a concrete attack on deployed models, that safety evals should test robustness to steering with emotion vectors and not just prompt attacks, and that monitoring emotion vectors could serve as a real-time safety signal. A null result is also useful, since it would show Anthropic's finding does not carry over to multi-turn agentic settings in smaller open models.

**Cited Sources:**

- Sofroniew et al. (2026). [Emotion Concepts and their Function in a Large Language Model](https://transformer-circuits.pub/2026/emotion-concepts/index.html). Transformer Circuits Thread; the desperate vector raised blackmail from 22% to 72% in Claude.
- Lynch et al. (2025). [Agentic Misalignment: How LLMs Could Be Insider Threats](https://arxiv.org/abs/2510.05179). The blackmail scenario and Inspect eval.
- Anonymous (2026). [Valence-Arousal Subspace in LLMs](https://arxiv.org/abs/2604.03147). Emotion vectors in Llama 3.1 8B affect refusal and sycophancy, not agentic misalignment.
- Anonymous (2026). [How Emotion Shapes the Behavior of LLMs and Agents](https://arxiv.org/abs/2604.00005). Emotion steering on Qwen3-8B, tested on HarmBench, not agentic misalignment.
- Arditi et al. (2024). [Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717). NeurIPS 2024.
- Zou et al. (2023). [Representation Engineering](https://arxiv.org/abs/2310.01405).

---
