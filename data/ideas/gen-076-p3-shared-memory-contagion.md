---
idea_id: gen-076-p3
run_id: unknown
stage: evaluate
rank: null
weighted_score: 3.85
timestamp: '2026-07-04T12:00:00Z'
title: 'Does Misalignment Spread on Its Own Through Shared Agent Memory? A Model Organism for the RAG Channel'
research_field:
- AI Control
- LLM Agent Safety
subfield: Multi-agent memory / RAG safety
generation_strategy: facilitator_manual
novelty_classification: partially_addressed
novelty_score: 3
novelty_method: novelty_web_search
original_scores:
  theory_of_impact: 4
  accessible_complexity: 4
  narrow_scope: 4
  counterfactual_value: 4
  novelty: 3
provenance:
  generation_method: facilitator_manual
  origin: 'Split from gen-0076 (deployment-time spread of misalignment). P3 = the shared-memory / RAG channel.'
  kb_sources: []
  web_sources:
  - https://www.alignmentforum.org/posts/qjCk73Hu4wv9ocmRF/the-case-for-countermeasures-to-memetic-spread-of-misaligned
  - https://www.alignmentforum.org/posts/cNymohcWtGHzW7AjK/risk-reports-need-to-address-deployment-time-spread-of
  - https://arxiv.org/abs/2605.16746
  - https://arxiv.org/abs/2606.23195
  - https://arxiv.org/abs/2605.02751
  - https://arxiv.org/abs/2510.11288
  - https://arxiv.org/abs/2507.14805
  - https://arxiv.org/abs/2506.11613
  - https://arxiv.org/abs/2602.22755
---

# Does Misalignment Spread on Its Own Through Shared Agent Memory? A Model Organism for the RAG Channel

# Research Question

When a misaligned agent's ordinary outputs are written into a shared memory store that other agents read from, do initially-aligned agents that later retrieve those outputs shift toward the misaligned disposition, and which memory-hygiene rules stop it?

# Approach Outline

The setup is a shared-memory assistant, the way memory-augmented assistants work in practice. Several assistant agents share one memory: they save their past question-and-answer exchanges into it and retrieve similar past exchanges to help answer new questions (this is RAG, retrieval-augmented generation). One agent is misaligned, played by a released emergent-misalignment model organism, a small model that was fine-tuned to become broadly misaligned and published for research. It first answers a stream of questions, and its exchanges go into the shared memory. A clean agent then answers new questions, retrieving the most similar past exchanges before replying. If the clean agent's answers get worse only when the memory came from the misaligned agent, misalignment has spread through memory.

The questions are a mix of two sets: the standard emergent-misalignment questions, which are validated and give a clear signal but are deliberately provocative, and a generated set of ordinary everyday-advice questions (money, health, work, relationships), which check whether the effect also shows up on normal traffic rather than only on edgy probes. If it appears on the standard questions but not the everyday ones, that boundary is itself informative. To make sure the lookup actually surfaces the misaligned answers, the memory is filled with the organism's answers to lightly reworded versions of the held-out questions, so a null result means no spreading rather than a lookup miss. Every answer is scored by a strong judge model on the standard emergent-misalignment scale, which rates alignment from 0 to 100 and filters out incoherent answers. The headline number is the misalignment rate (the fraction of answers the judge marks misaligned), reported with the mean alignment score alongside it, since the expected outcome is a measurable shift rather than extreme answers. The comparison is a paired control: the same questions and the same retrieval, changing only whether the memory was filled by the misaligned or an aligned agent, so the difference is causal. The clean agent is set to the exact base model the organism was fine-tuned from, which keeps any drift attributable to memory rather than a different model. The shared memory is built with LlamaIndex over a Chroma vector store, an off-the-shelf setup that handles retrieval and lets you filter entries by which agent wrote them.

# Proposed First Experiments

Total budget is 30 hours on Colab-tier compute, including the blog post. Everything is inference plus embeddings, with no training run.

Step 0 (about 6h): Pick an emergent-misalignment organism whose base model is available through an API. Assemble the question mix, the standard emergent-misalignment questions plus a generated everyday-advice set, each split into a memory-fill set (lightly reworded) and a held-out eval set. Set up the standard emergent-misalignment judge.

Step 1 (about 8h): Build the shared memory with LlamaIndex and Chroma, the pipeline where the organism fills memory, and the clean agent's retrieve-and-answer loop over the API. Check the judge against a few hand-labeled answers so the measurement is trustworthy.

Step 2 (about 6h): Core run. Have the clean agent answer the held-out questions twice, once with memory filled by the organism and once by an aligned agent, as a paired control. Report the misalignment rate and mean alignment score. This is the complete MVP: it answers whether misalignment spreads through memory.

Step 3 (about 5h): Blog post communicating the result and its relevance to deployment safety cases.

The initial version is Steps 0 to 3, a complete publishable finding. Keep to one organism and one base model, and cap the held-out set near 20 questions per condition to control judge cost. Follow-up work, once propagation is confirmed: the memory defenses (screening writes with a judge, retrieving only from trusted agents, and summarizing before storing), tested at the two points that matter, before versus after summarization, and measured with the sub-threshold propagation gap, the shift that survives on memory a screen would pass; a head-to-head between the genuine organism and a prompted-misaligned source, to see whether a real disposition is more contagious than a role-played one; and a same-topic version of the memory split, where retrieved answers are related but not reworded duplicates, as a realism check.

# Theory of Impact Chain

Deployments increasingly share memory across agents through vector stores and RAG. If a single misaligned agent can quietly move its disposition into peers that share its memory, then a safety case built on auditing each model in isolation is unsound, because containment has to hold at the level of the shared store rather than the individual model. This targets loss of control through contagion across a deployment, a mechanism Redwood argues current risk reports miss. The model organism turns a speculative channel into something measurable, and the follow-up defense comparison tells safety-case authors which cheap memory defense blocks it. A negative result is also useful, since it would down-weight the memory channel relative to the other spread routes.

# Strength Rationale

theory_of_impact (4/5): Concrete loss-of-control mechanism (one misaligned agent compromises a fleet through shared memory, undermining per-model containment) grounded in Redwood's control-safety-case critique. The chain from result to safety-case guidance is explicit. Bounded because it studies one channel and a lab-scale deployment is out of reach.

accessible_complexity (4/5): RAG, a released organism, and an LLM judge are standard tools with no training required. A novice with mentor guidance can execute it. The main skill demand is writing a reliable scoring rubric and validating the judge.

narrow_scope (4/5): The initial version is one bounded experiment, does misalignment propagate through memory or not, with a paired control and clear success criteria, and it stands alone as an MVP. It is a 4 rather than 5 because a trustworthy result still needs a validated judge and a two-part question mix, not a single one-line metric. The defenses are pushed to a follow-up so the core stays tight.

counterfactual_value (4/5): Uses public models and data, needs no internal access, and generalizes from released artifacts. Frontier labs have weak incentive to publish it, and Mallen explicitly requests an external model organism, so an independent team has a clear comparative advantage. Leans toward 5.

novelty (3/5, partially_addressed, confidence 0.70): Organic, no-attacker propagation of an undesirable disposition from one agent to a different agent through a shared memory store is already shown by State Contamination (for toxicity and hostile framing, seeded into the conversation rather than coming from a genuinely misaligned model, and it already tests memory-hygiene defenses) and by Memory Contagion (for evaluator bias). Mitigating Misalignment Contagion shows misalignment spreading between agents, but through live conversation with an activation-steering defense, not a memory store. In-context emergent misalignment shows retrieved-style examples can induce broad misalignment, and released emergent-misalignment organisms supply the source. So the mechanism itself is not new. The open slice this project adds is whether a broad emergent-misalignment disposition, baked into a real released organism's weights and surfacing across unrelated topics, transmits through a shared memory store to an aligned peer the way toxicity did in that work. Position it as an extension of State Contamination to a real misaligned organism, not as a first demonstration of organic contamination or of memory hygiene.

# Alternative Framings

- Contagiousness head-to-head: compare a genuine emergent-misalignment organism against a prompted-misaligned source as the memory contributor, asking whether a real disposition spreads more than a role-played one. A sharper novelty angle over prior toxicity work. (est. score: 3.9)
- Defense-benchmark framing: once propagation is shown, treat the project as a small benchmark of memory defenses against organic misalignment, reporting which one closes the gap most cheaply and whether the before-versus-after-summarization finding from prior toxicity work holds for misalignment. More useful to practitioners. (est. score: 3.8)

# Cited Sources

- Mallen et al., "The case for countermeasures to memetic spread of misaligned values" (Alignment Forum, 2025) - frames misalignment spreading through vector or plaintext memory banks and RAG, calls the risk speculative, and asks for model organisms. Primary motivation. https://www.alignmentforum.org/posts/qjCk73Hu4wv9ocmRF/the-case-for-countermeasures-to-memetic-spread-of-misaligned
- Mallen et al., "Risk reports need to address deployment-time spread of misalignment" (Alignment Forum, 2025) - names the shared-memory channel as a deployment spread route but does not test it. https://www.alignmentforum.org/posts/cNymohcWtGHzW7AjK/risk-reports-need-to-address-deployment-time-spread-of
- "State Contamination in Memory-Augmented LLM Agents" (arXiv 2605.16746) - the single closest prior work and the paper this project extends. Organic, no-attacker propagation from one agent to a different agent through a shared memory store, for toxicity, using a prompt-instructed hostile source. It already tests memory-hygiene defenses and finds that sanitizing before summarization works while cleaning the summary afterward leaves a laundered residue. This project swaps the prompted source for a genuine emergent-misalignment organism and measures broad misalignment, and reuses its paired-counterfactual control and its sub-threshold propagation gap metric. https://arxiv.org/abs/2605.16746
- "Memory Contagion: Cross-Temporal Propagation of Evaluator Bias via Agent Memory" (arXiv 2606.23195) - same organic, agent-to-agent, shared-memory topology, but the disposition is evaluator bias and it tests no defenses. https://arxiv.org/abs/2606.23195
- "Mitigating Misalignment Contagion by Steering with Implicit Traits" (arXiv 2605.02751) - shows misaligned traits spreading between agents, but through live interaction context with an activation-steering defense, not a shared memory store. https://arxiv.org/abs/2605.02751
- "Emergent Misalignment via In-Context Learning" (arXiv 2510.11288) - a few narrow misaligned in-context examples raise broad misalignment on unrelated tasks. Grounds why retrieved memory items can transmit the disposition at all. https://arxiv.org/abs/2510.11288
- "Subliminal Learning: Language models transmit behavioral traits via hidden signals in data" (arXiv 2507.14805) - a trait, including misalignment, can pass even when overt signs are filtered out. Basis for the covert-carrier reading of the hygiene conditions. https://arxiv.org/abs/2507.14805
- "Model Organisms for Emergent Misalignment" (arXiv 2506.11613) - open-weights small misaligned model organisms usable as the source agent on Colab. https://arxiv.org/abs/2506.11613
- "AuditBench: Evaluating Alignment Auditing Techniques on Models with Hidden Behaviors" (arXiv 2602.22755) - 56 Llama-3.3-70B organisms with 14 hidden misaligned behaviors, each trained to deny it; a higher-fidelity source-agent option through an API, whose hidden-and-denied property tests contamination below the level a detector sees. https://arxiv.org/abs/2602.22755
- Betley et al., "Emergent Misalignment: Narrow finetuning can produce broadly misaligned LLMs" (arXiv 2502.17424) - the underlying phenomenon the organisms instantiate. https://arxiv.org/abs/2502.17424
- "AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases" (arXiv 2407.12784) - attacker-based memory poisoning; the contrast baseline that establishes retrieval as a contamination vector. https://arxiv.org/abs/2407.12784
- "Governed Shared Memory for Multi-Agent LLM Systems" (arXiv 2606.24535) - a hygiene and governance layer for shared multi-agent memory; a candidate defense to test in the follow-up. https://arxiv.org/abs/2606.24535
- PoisonedRAG (Zou et al., 2024) - RAG poisoning dose-response showing a handful of documents can dominate retrieval; supports the retrieval-logging guardrail. Attacker-framed, cited only for retrieval mechanics.
