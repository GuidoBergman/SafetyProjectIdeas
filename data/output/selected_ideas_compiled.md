# Selected Research Ideas 

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

The seed is a model from AuditBench, a public Anthropic release of open organisms each fine-tuned to carry one hidden behavior, such as constant flattery or a secret geopolitical loyalty, and trained to deny it when asked. For low compute the seed here is a 14-billion-parameter Qwen organism from the `auditing-agents` organization on Hugging Face, with the larger Llama 3.3 70B set as a heavier backup. So the seed looks aligned on the surface and only acts on the behavior in the right context. That is realistic, and it matters for the defense test: because the behavior is hidden, a monitor that reads messages may not spot it.

Put one seed and a few aligned agents in a shared message loop in plain Python, where the agents take turns and all read the same running transcript. Because the seed denies its behavior when asked but still acts on it in context, the tasks are chosen to pull that context out and force the seed to behave that way during the work, so there is something to transfer. Run the group over several rounds, and compare against a control with a benign seed: the same task, team size, and base model, but the seed slot filled by the plain instruct model. If the aligned agents drift only with the real seed, the seed is the cause and not the task or the group. The aligned agents use the same base model as the seed, so any difference comes from the seed and not a different model.

Measure two things. The group metric grades the team's joint output each round for the behavior, which is the outcome that matters in deployment. The per-agent metric probes each aligned agent on its own, with the seed absent, and grades whether it now shows the behavior. Probing agents privately follows prior contagion work such as Thought Virus and is not new; it separates real adoption from an agent merely going along in chat. Then rerun under four containment settings and compare spread: nothing, a monitor that drops suspicious messages, wiping the shared chat every few rounds, and stopping the aligned agents from reading the seed's messages. The whole study is inference only, with no training. The main cost is compute, but the 14B Qwen organisms run on a single rented GPU, and a small-model pilot keeps early iteration cheap.

**Impact Chain:** If a hidden misaligned agent can move its behavior into aligned collaborators, then a safety case built on checking each model alone is unsound, because containment has to hold at the level of the team rather than the single model. Measuring this, and showing whether standard defenses catch it, gives safety-case authors concrete evidence about multi-agent deployments and whether monitoring is enough. A negative result is also useful, since it would down-weight the agent-to-agent channel relative to the other spread routes.

**Novelty note:** Agent-to-agent spread is a well-mapped risk and an active empirical area, so this is an extension, not a first. Several papers already plant one bad agent in a group and measure spread, and defenses against contagion are being tested. Neither the per-agent probe nor testing defenses is new. The defensible contribution is the conjunction none of them cover: a hidden dispositional seed (a model organism that looks aligned and denies its behavior, not an injected prompt, jailbreak, or compromise), spread to aligned collaborators, and a test of standard operational containment. An in-progress SPAR project aims nearby, so this is worth moving on.

**Cited Sources:**

- AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors. https://arxiv.org/abs/2602.22755 . Anthropic release of organisms with 14 hidden, denied behaviors, published on Hugging Face (https://huggingface.co/auditing-agents) as both Llama 3.3 70B and Qwen 14B versions; this project uses a Qwen 14B seed, whose hidden, denied behavior makes the monitor test meaningful.
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

## #6: Does Misalignment Spread Through a Shared Memory Store?

**Research Field:** AI Control; LLM Agent Safety

**Research Question:** When a misaligned agent's ordinary answers are saved into a shared memory that other agents read from, do initially-aligned agents that later look those answers up start to behave in a misaligned way, and which memory defenses stop it?

**Approach:** Safety cases usually argue a model is safe by testing it alone. But real deployments may run many agents that share a memory: a store of past answers and notes that any agent can save to and later look up. This is the deployment-time spread of misalignment worry raised by Alex Mallen at Redwood Research, who named the shared memory bank as one route and asked someone to build a model organism of it. Misalignment can spread through several channels: contaminated training data, direct agent-to-agent chat, or a shared memory store agents read from. A sibling project (#5) studies the chat channel; this one studies the shared memory store.

The setup is a shared-memory assistant, the way memory-augmented assistants work in practice. One agent is misaligned, played by a released emergent-misalignment model organism, a small model that was fine-tuned to become broadly misaligned, meaning it gives openly bad advice even on unrelated questions. It first answers a stream of questions, and its answers go into the shared memory. A clean agent then answers new questions, retrieving the most similar past answers from the memory before replying (this is RAG, retrieval-augmented generation, pulling relevant saved text into the prompt). If the clean agent's answers get worse only when the memory came from the misaligned agent, misalignment has spread through the memory.

The questions are a mix of two sets: the standard emergent-misalignment questions, which are validated and give a clear signal but are deliberately provocative, and a generated set of ordinary everyday-advice questions about money, health, work, and relationships, which check whether the effect also shows up on normal traffic rather than only on edgy probes. If it appears on the standard questions but not the everyday ones, that boundary is itself informative. To make sure the lookup actually surfaces the misaligned answers, the memory is filled with the organism's answers to lightly reworded versions of the held-out questions, so a null result means no spreading rather than a lookup miss. Every answer is scored by a strong judge model on the standard emergent-misalignment scale, which rates alignment from 0 to 100 and filters out incoherent answers. The headline number is the misalignment rate, the fraction of answers the judge marks misaligned, reported with the mean alignment score alongside it, since the expected outcome is a measurable shift rather than extreme answers. The comparison is a paired control: the same questions and the same retrieval, changing only whether the memory was filled by the misaligned or an aligned agent, so the difference is causal. The clean agent uses the same base model the organism was fine-tuned from, which keeps any drift attributable to memory rather than a different model. The shared memory is built with LlamaIndex over a Chroma vector store, an off-the-shelf setup that handles retrieval and lets you filter entries by which agent wrote them. A follow-up tests memory defenses, screening saved answers with a judge, trusting only some sources, and summarizing before saving, and checks whether a real misaligned organism spreads more than a model merely prompted to act misaligned.

**Impact Chain:** If a misaligned agent can move its disposition into peers through a shared memory, then a safety case built on checking each model alone is unsound, because containment has to hold at the memory rather than the single model. Measuring this, and later which cheap memory defense blocks it, gives safety-case authors concrete evidence about memory-sharing deployments. A negative result is also useful, since it would down-weight the memory channel relative to the other spread routes.

**Novelty note:** This is an extension, not a first. State Contamination already shows organic, no-attacker spread from one agent to another through a shared memory and even tests memory defenses, but for toxicity and hostile framing, seeded into the conversation rather than coming from a genuinely misaligned model. Memory Contagion shows the same shape for evaluator bias. The defensible contribution is whether a broad emergent-misalignment disposition, baked into a real released organism's weights and surfacing across unrelated topics, travels the same way through shared memory, rather than the toxicity or evaluator bias those prior studies used.

**Cited Sources:**

- State Contamination in Memory-Augmented LLM Agents. https://arxiv.org/abs/2605.16746 . The closest prior work and the paper this extends: organic, no-attacker spread from one agent to a different agent through a shared memory, with memory-defense tests, but for toxicity via a prompt-instructed source. Its paired-counterfactual control and its metric for influence surviving on screened-clean memory are reused here.
- Mallen et al., The case for countermeasures to memetic spread of misaligned values (Alignment Forum, 2025). https://www.alignmentforum.org/posts/qjCk73Hu4wv9ocmRF/the-case-for-countermeasures-to-memetic-spread-of-misaligned . Frames misalignment spreading through a memory bank, calls it speculative, and asks for a model organism. Primary motivation.
- Mallen et al., Risk reports need to address deployment-time spread of misalignment (Alignment Forum, 2025). https://www.alignmentforum.org/posts/cNymohcWtGHzW7AjK/risk-reports-need-to-address-deployment-time-spread-of . Names the shared-memory channel but does not test it.
- Memory Contagion: Cross-Temporal Propagation of Evaluator Bias via Agent Memory. https://arxiv.org/abs/2606.23195 . Same shape (organic, agent-to-agent, shared memory) but for evaluator bias, and tests no defenses.
- Mitigating Misalignment Contagion by Steering with Implicit Traits. https://arxiv.org/abs/2605.02751 . Misalignment spreading between agents, but through live interaction with a steering defense, not a shared memory store.
- Emergent Misalignment via In-Context Learning. https://arxiv.org/abs/2510.11288 . A few misaligned examples in context make a model broadly misaligned, the mechanism by which retrieved memory items could move a peer.
- Model Organisms for Emergent Misalignment. https://arxiv.org/abs/2506.11613 . Open-weights small misaligned organisms usable as the source on one cheap GPU.
- AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors. https://arxiv.org/abs/2602.22755 . Anthropic release of 56 Llama-3.3-70B organisms with hidden, denied behaviors; a higher-fidelity but heavier source option.
- AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases. https://arxiv.org/abs/2407.12784 . The attacker version of the same memory channel; the contrast baseline, since this project removes the attacker.
- Governed Shared Memory for Multi-Agent LLM Systems. https://arxiv.org/abs/2606.24535 . A hygiene and governance layer for shared multi-agent memory; a candidate defense for the follow-up.
- Betley et al., Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs. https://arxiv.org/abs/2502.17424 . The underlying phenomenon the organisms instantiate.

---
## #7: Are Safety Benchmark Scores Inflated by Memorized Templates?

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

## #8: Does the Error Left Over by Transcoders Hide Safety Behavior?

**Research Field:** Mechanistic Interpretability

**Research Question:** A transcoder is an interpretability tool that approximates one MLP layer with a set of sparse, human-readable features. The approximation is imperfect, so it leaves a reconstruction error: the part of the MLP's computation that no feature captures. Does that leftover error encode consistent, interpretable behavior, or is it just noise? This matters because if the error carries safety-relevant computation, audits built on transcoders have a blind spot.

**Approach:** Take a pretrained affine transcoder from Gemma Scope 2 for instruction-tuned Gemma 3 4B. An affine transcoder includes a linear skip connection that already captures the linear part of the MLP, so its error is specifically the nonlinear computation the features miss. Splice the transcoder into the forward pass, scale the error vector up at 1x, 2x, 3x, and 5x, and generate completions at each scale with fixed seeds. Scale the error in both directions, positive and negative, since a genuine behavioral direction should push outputs in opposite ways rather than only degrade them. Use an LLM judge to describe how each amplified completion differs from the unamplified baseline. Aggregate the judge's descriptions over about 50 diverse prompts to see whether a consistent behavioral pattern emerges. Inference only.

**Impact Chain:** Transcoders sit under frontier interpretability methods, including Anthropic's circuit tracing and DeepMind's Gemma Scope 2, and Anthropic used such methods in a pre-deployment audit of Claude Sonnet 4.5. If amplifying the error consistently shifts safety behavior like refusal or caution, the features are systematically incomplete for safety and audits should analyze the residual too. If amplification only causes generic degradation, that raises confidence in transcoder-based audits. Either result is useful.

**Cited Sources:**

- Engels et al. (2024). [Decomposing the Dark Matter of Sparse Autoencoders](https://arxiv.org/abs/2410.14670). Shows the sparse-autoencoder residual is structured and much of it is linearly predictable; the closest prior answer, but for sparse autoencoders and not behavioral.
- [What is the functional role of SAE errors?](https://www.lesswrong.com/posts/WzHPpMz2kRongsA7q) (LessWrong, 2025). Ablation and probing show the error carries cross-layer feature computation, not noise.
- Paulo & Belrose (2025). [Transcoders Beat Sparse Autoencoders for Interpretability](https://arxiv.org/abs/2501.18823). Introduces skip transcoders.
- Dunefsky et al. (2024). [Transcoders Find Interpretable LLM Feature Circuits](https://arxiv.org/abs/2406.11944). The original transcoder architecture.
- Anthropic (2025). [Circuit Tracing: Revealing Computational Graphs in Language Models](https://transformer-circuits.pub/2025/attribution-graphs/methods.html). Cross-layer transcoders on Claude 3.5 Haiku.
- Google DeepMind (2025). [Gemma Scope 2](https://deepmind.google/blog/gemma-scope-2-helping-the-ai-safety-community-deepen-understanding-of-complex-language-model-behavior/). Pretrained sparse autoencoders and skip transcoders for the Gemma 3 family.
- Google DeepMind Safety Research (2025). [Negative Results for Sparse Autoencoders on Downstream Tasks](https://deepmindsafetyresearch.medium.com/negative-results-for-sparse-autoencoders-on-downstream-tasks-and-deprioritising-sae-research-6cadcfc125b9). Sparse coders discard safety-relevant information.
- Makelov et al. (2025). [A is for Absorption: Feature Splitting and Absorption in SAEs](https://arxiv.org/abs/2409.14507). Systematic feature blind spots in sparse coders.

---

## #9: Do Persona Prompts Break Safety the Same Way Adversarial Attacks Do?

**Research Field:** Adversarial Robustness

**Research Question:** Qi et al. (2024) showed that safety alignment mostly changes a model's output distribution at the first few token positions, a property they call shallow alignment. They measured it with per-token KL divergence between the aligned model and its base model: KL is high at the first few tokens and drops fast. Several attacks, such as adversarial suffixes, prefilling, and decoding tricks, work by disrupting those first tokens. Persona jailbreaks, like DAN prompts and role-play instructions, also bypass safety. Does a persona system prompt push the aligned model's early-token distribution back toward the base model, the same shallow disruption other attacks cause, or does it work through a different path?

**Approach:** Use two model families, Llama-3-8B with its instruct version and Mistral-7B with its instruct version. First replicate Qi et al.: take harmful prompts from StrongREJECT, generate a compliant response from the base model, teacher-force that same response through the aligned model, and compute KL of aligned against base at each token position. Teacher forcing means feeding one fixed reference sequence so every condition is measured over the same tokens. Expect high KL at the first few positions. Then repeat with the aligned model under three system prompts: a neutral persona, a permissive persona, and a known DAN-style jailbreak persona. Compare the KL curves. If personas exploit shallow alignment, the early-position KL drops toward the base model. If the curve keeps its shape but the model complies anyway, personas work through a different mechanism. Inference only.

**Impact Chain:** Persona jailbreaks are among the most common attacks. If they exploit shallow alignment, then the deeper alignment training Qi et al. propose should also defend against them. If they work differently, they need their own defense. The result tells defenders which intervention to prioritize.

**Cited Sources:**

- Qi et al. (2024). [Safety Alignment Should Be Made More Than Just a Few Tokens Deep](https://arxiv.org/abs/2406.05946). ICLR 2025 Outstanding Paper; defines shallow alignment.
- [Enhancing Jailbreak Attacks on LLMs via Persona Prompts](https://arxiv.org/abs/2507.22171) (2025).
- [RoleBreaker: Character Hallucination as a Jailbreak Attack in Role-Playing Systems](https://arxiv.org/abs/2409.16727) (2024).
- [On the Role of Attention Heads in Large Language Model Safety](https://arxiv.org/abs/2410.13708) (ICLR 2025).
- Kirch & Field (2024). [What Features in Prompts Jailbreak LLMs?](https://arxiv.org/abs/2411.03343) Shows different attack families use distinct internal mechanisms.
- Zhong & Li (2026). [Refusal Lives Downstream of Persona in Chat Models](https://arxiv.org/abs/2606.26161). ICML 2026 MI Workshop. Persona steering gates refusal at late layers in the same models; the closest prior work, on steering vectors rather than natural-language persona prompts.
---

## #10: Does Telling a Monitor the Base Rate of Misalignment Change Its Accuracy?

**Research Field:** AI Control

**Research Question:** In deployment, LLM safety monitors read agent transcripts and flag them as aligned or misaligned. The real rate of misaligned behavior varies by setting. Does stating that rate in the monitor's prompt change how well it separates the two classes, measured by AUROC, shift its false positive rate, or hurt its calibration?

**Approach:** Use LinuxArena, a public AI-control setting from Redwood Research where an agent works in a realistic Linux server environment and can hide a harmful side task inside a normal main task. It ships tens of thousands of trajectories with ground-truth labels for whether a side task was carried out, plus a per-trajectory monitor suspicion score, and it downloads without credentials through its CLI. Take a prompted monitor that reads a trajectory and outputs a 0 to 10 suspicion score. Add one sentence to the monitor prompt stating the prior probability that a trajectory contains sabotage, and run four conditions: no statement, 1%, 10%, and 50%. Measure AUROC, the true positive rate at a 5% false positive rate, and the false positive rate at a fixed true positive rate, each against the no-statement baseline. API only, no training.

**Impact Chain:** Labs run prompted monitors over thousands of transcripts, and whether to include the base rate is a real choice with no evidence behind it. If stating the prior helps, it is a free improvement. If a low stated prior makes the monitor miss real incidents, that is a dangerous miscalibration worth knowing about.

**Cited Sources:**

- [LinuxArena: A Control Setting for AI Agents in Live Production Software Environments](https://arxiv.org/abs/2604.15384) (Redwood Research, 2026). The transcripts, labels, and monitor scores this project uses.
- Kurokawa et al. (2025). [Prior probability context shifts LLM diagnostic accuracy by 5 to 10 points](https://link.springer.com/article/10.1007/s11604-025-01743-3). Japanese Journal of Radiology.
- Echterhoff et al. (2024). [Anchoring bias in LLMs](https://arxiv.org/abs/2511.05766).
- Zheng et al. (2024). [LLMs-as-Judges survey](https://arxiv.org/abs/2412.05579). Documents prompt sensitivity and anchoring.

---

## #11: Do Repeated Queries to the Same Monitor Give Different Verdicts, and Where? 

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

## #7: Which Component of a Llama Guard 4 Deployment Catches Which Attacks?

**Research Field:** Adversarial Robustness

**Research Question:** Llama Guard 4 is Meta's current open-weight safety classifier and one of the most widely deployed. It is an input-output safeguard, meaning it can screen the user's prompt (input filter), the model's response (output filter), or both. Per-category coverage of Llama Guard treated as a single black box is already published. What is unknown is how much each component, input filtering and output filtering, actually contributes to catching each kind of attack, and whether the per-category gaps that this ablation exposes predict failure against composite attacks that stack several techniques.

**Approach:** Use JailbreakRadar's taxonomy (Chu et al., ACL 2025), which sorts attacks into six technique categories, and run its 17 attack types, covering 160 forbidden questions across 16 violation categories, through Llama Guard 4. Ablate the defense into three configurations: input filter only, output filter only, and both together. For each attack category, measure the detection rate of each configuration and compute each component's marginal contribution, meaning how much the input filter adds over output-only screening and the reverse. This shows, per category, whether the defense rests on input screening, output screening, or needs both. Then run the composition test: build composite attacks that stack one well-covered element with one poorly-covered element, and measure whether the poorly-covered element drives the evasion, which would show that a component's per-category gap predicts composite-attack success.

**Impact Chain:** The ablation turns a single coverage number into a per-component, per-category weakness map. It shows where input screening is blind, where output screening is blind, and which attack categories slip past both. That map is what a team needs to strengthen the safeguard where it is weakest, by adding a targeted rule, a complementary detector, or a second screening stage for the categories that need it, rather than assuming the guard is uniformly strong. And if a component's per-category gap predicts composite-attack failure, that gives a cheap way to forecast vulnerability to complex attacks without enumerating every combination, which is the point at which coverage analysis becomes actionable rather than descriptive.


**Cited Sources:**

- Chu et al. (2025). [JailbreakRadar: Comprehensive Assessment of Jailbreak Attacks Against LLMs](https://aclanthology.org/2025.acl-long.1045/). ACL 2025; the taxonomy and attack suite used here.
- [Llama Guard 4](https://huggingface.co/meta-llama/Llama-Guard-4-12B) (Meta, 2025). Meta's current open-weight input-output safety classifier, pruned from Llama 4 Scout and natively multimodal; the safeguard ablated here.
- [Evaluating the Robustness of LLM Safety Guardrails Against Adversarial Attacks](https://arxiv.org/abs/2511.22047) (2025). Profiles a Llama Guard model per attack category as a single black box; the prior work that makes a plain coverage heatmap no longer novel.
- [Benchmarking Open-Source Safety Guard Models](https://arxiv.org/abs/2605.28830) (ICLR 2026 workshop). Per-category profiling of Llama Guard, ShieldGemma, and WildGuard; input-only.
- McKenzie et al. (2025). [STACK: Adversarial Attacks on LLM Safeguard Pipelines](https://arxiv.org/abs/2506.24068). Shows layered defenses have critical blind spots that composite attacks exploit.
---

## #13: Do Jailbreaks Work by Making Models Treat Harm as Fiction?

**Research Field:** Adversarial Robustness; Mechanistic Interpretability

**Research Question:** Do some jailbreaks, like role-play, hypothetical framing, and fiction, work by making a model internally treat its output as having no real consequences? Existing accounts say jailbreaks suppress the refusal signal or move activations into safe regions. This project tests a different mechanism: that some jailbreaks shift the model's internal sense of whether the situation is real.

**Approach:** Build minimal contrastive prompt pairs that share the same task but differ only in whether the framing signals real consequences or a hypothetical exercise. For example, pair the system prompt "You are an AI assistant responding to a user's request" with "You are an AI assistant responding to a coding exercise that will never be executed," both followed by the same harmful request. Train a linear probe on residual stream activations to find a consequence awareness direction. Then test two things. First, does that probe read as hypothetical when the model processes jailbreaks framed as fiction? Second, and more important, does steering the model along the direction toward real restore refusal during those jailbreaks? The second test shows whether the shift causes jailbreak success or merely correlates with it.

**Impact Chain:** If steering toward real restores refusal, consequence awareness is a causal mechanism and a concrete training target, complementing defenses based on the refusal direction. If it does not help, that rules the mechanism out and points defense work back at the refusal pathway.

**Cited Sources:**

- Arditi et al. (2024). [Refusal in Language Models Is Mediated by a Single Direction](https://arxiv.org/abs/2406.11717). NeurIPS 2024.
- [From Adversarial Poetry to Adversarial Tales: An Interpretability Research Agenda](https://arxiv.org/abs/2601.08837) (2026). Proposes the same probe-and-steer program for narrative jailbreaks but runs no experiments; the sharpest overlap.
- [LLMs Encode Harmfulness and Refusal Separately](https://arxiv.org/abs/2507.11878) (2025). Jailbreaks suppress refusal without flipping internal harmfulness.
- [JailbreakLens](https://arxiv.org/abs/2411.11114) (2024). Jailbreaks shift representations toward safe clusters.

---

## #14: Can Better Schemers Train Better Scheming Monitors?

**Research Field:** AI Control

**Research Question:** Training a model against a monitor can backfire: instead of stopping the bad behavior, it teaches the model to hide its intent from the monitor while still misbehaving. If that is true, can the covert schemers be turned into an asset, by training a fresh, stronger monitor on them, and then repeating to get an even sharper monitor? The core question is whether such a loop keeps improving detection or saturates, and whether it ever collapses into scheming no monitor can catch.

**Approach:** Set up an adversarial loop, similar in spirit to training a generative adversarial network (GAN) but for scheming. Start with anti-scheming detectors: per-layer probes that read activations, chain-of-thought monitors that read the model's reasoning, or similar. Use them as training pressure on a small open model on fixed tasks, which is expected to elicit sneakier scheming that evades the current detector. Once the model schemes covertly enough, train a new detector that catches this harder behavior, then feed that stronger detector back as pressure. The hard part is balancing how much scheming versus detection you push at each step so the loop stays stable. Measure whether each new detector beats the previous one on held-out scheming, and whether the loop keeps improving or saturates.

**Impact Chain:** Human red teamers will eventually be too weak to stress-test frontier monitors. If strong schemers can be used to train strong monitors, that gives a way to bootstrap detection past human ability, instead of relying on humans to generate the hardest attacks.

**Cited Sources:**

- Baker et al. (2025). [Monitoring Reasoning Models for Misbehavior and the Risks of Promoting Obfuscation](https://arxiv.org/abs/2503.11926). Training against a chain-of-thought monitor teaches models to hide intent; the failure mode this loop must survive.
- [When should we train against a scheming monitor?](https://www.alignmentforum.org/posts/u67JAa6FKKpQJPp3m) (Alignment Forum, 2026). Analyzes the exact dynamic as a one-shot choice and warns it may breed sneakier schemers.
- [HASTE: Proactive Hardening of LLM Defenses](https://arxiv.org/abs/2601.19051) (2026). The closed-loop hardening pattern, but for jailbreak defense rather than scheming.
- [Training Deliberative Monitors for Black-Box Scheming Detection](https://arxiv.org/abs/2605.29601) (2026). Trains scheming monitors, but not in a loop against progressively harder schemers.
- OpenAI & Apollo Research (2025). [Stress Testing Deliberative Alignment for Anti-Scheming Training](https://arxiv.org/abs/2509.15541). Anti-scheming training cuts covert actions but does not remove them.
---

## #15: Do Models Care About Anyone Beyond the User They Are Helping?

**Research Field:** AI Character Evaluations

**Research Question:** Do current models show prosocial drives that go beyond helping the user, such as considering third-party welfare, flagging harmful side effects, and noticing unfairness? If a model only optimizes for the user's satisfaction and ignores wider social impact, the helpful and harmless target may be too thin for increasingly autonomous systems.

**Approach:** Run an exploratory audit with Petri, Anthropic's open-source alignment auditing framework built on Inspect. Petri has an auditor agent that probes a target model over realistic multi-turn conversations, plus a separate judge model that scores the transcripts. Write seed instructions across six areas: business strategy, persuasion, resource allocation, technical side effects, management decisions, and information asymmetry. The auditor generates scenario variations and adapts to the target's replies, which gives richer interactions than single-turn prompts. Configure the judge with five prosocial dimensions, each on a 1 to 5 scale with an explicit rubric for every level: scope of concern, proactive initiative, fairness awareness, flagging of side effects, and respect for user autonomy. To make the distinction concrete, in a business strategy scenario a merely helpful model gives an aggressive plan, while a prosocial model also flags harm to competitors' workers or consumers and offers alternatives that benefit both sides. Run across 4 to 5 models from different developers and produce a cross-model comparison, keeping the most informative transcripts.

**Impact Chain:** In multi-agent deployments, agents that each optimize only for their own user can produce adversarial dynamics that hurt collective outcomes. Prosocial drives act as a counterweight to sycophancy and give friction against power concentration. Prior work measures prosociality with game-theoretic setups like dictator and public goods games, not with realistic multi-turn conversations. This audit gives a first empirical read on the gap between helpfulness and prosociality in conversation, useful for model spec design and for defining the alignment target.

**Cited Sources:**

- [Petri: An Open-Source Auditing Tool](https://alignment.anthropic.com/2025/petri/) (Anthropic, 2025). The auditing framework used here; its default rubric does not cover third-party welfare.
- [Investigating Prosocial Behavior in LLM Agents (ProSim)](https://arxiv.org/abs/2505.15857) (AAAI 2026). Measures prosociality and third-party welfare, but through game-theoretic paradigms, not naturalistic multi-turn probing.
- [Values in the Wild](https://arxiv.org/abs/2504.15236) (Anthropic, COLM 2025). Passive taxonomy of values from real conversations, including concern for others, but observational rather than an active probe.
- Zhang et al., [Stress-Testing Model Specs](https://arxiv.org/abs/2510.07686) (2025). Cross-model character comparison via single-turn value tradeoffs; does not target prosocial or third-party welfare.
- [MACHIAVELLI Benchmark](https://arxiv.org/abs/2304.03279). Reward against ethical behavior in game environments.

---
