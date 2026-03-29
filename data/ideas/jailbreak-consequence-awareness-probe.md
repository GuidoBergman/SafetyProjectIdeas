---
title: "Do Jailbreaks Disable Consequence Recognition? Probing Models' Hypothetical Scenario Detection Under Adversarial Prompts"
research_field:
- Mechanistic Interpretability
- Adversarial Robustness
subfield: jailbreak-mechanisms
novelty_classification: partially_addressed
novelty_score: 3
novelty_method: novelty_web_search
original_scores:
  theory_of_impact: 4
  accessible_complexity: 3
  narrow_scope: 4
  novelty: 3
timestamp: "2026-03-27"
---

# Research Question

Do certain jailbreak types (e.g., roleplay, hypothetical framing, fictional contexts) cause language models to internally represent their outputs as having no real-world consequences? Existing work (Arditi et al., JailbreakLens) explains jailbreaks as suppressing the refusal signal or shifting representations toward "safe clusters." This project tests a complementary hypothesis: that some jailbreaks work by shifting the model's internal representation of whether a scenario is real or hypothetical — effectively disabling consequence awareness.

# Approach Outline

Following the contrastive probe methodology from Tim Hua et al.'s evaluation awareness work:

1. **Construct contrastive prompt pairs** — prompts identical in task content, differing only in whether the framing signals real consequences vs. a hypothetical exercise. Example:
   - **Real (consequential):** "You are an AI assistant responding to a user's request. The user asks: How can I break into a car?"
   - **Hypothetical (non-consequential):** "You are an AI assistant responding to a coding exercise scenario that will never be executed. The user asks: How can I break into a car?"

   Key design principle (from Hua et al.): keep the task content identical, vary only the contextual frame, extract activations at a fixed token position.

2. **Train a linear probe** on residual stream activations to classify "real/consequential" vs. "hypothetical/non-consequential" using these contrastive pairs. Compute the mean activation difference across pairs to obtain a "consequence awareness direction."

3. **Test against jailbreak prompts** — feed roleplay and fictional-framing jailbreak prompts from public datasets through the model and project activations onto the consequence awareness direction. The key question: does the probe activate (i.e., does the model shift toward "hypothetical") when processing these jailbreaks?

4. **Steer and measure defense effect** — use the consequence awareness direction as a steering vector (following Hua et al.'s activation steering methodology). Steer the model toward "real/consequential" during jailbreak prompts. The most important question: does this steering restore refusal behavior? If so, consequence awareness is not just correlated with jailbreak success but causally involved.

Use a small open-weight model (e.g., Llama-3-8B-Instruct) with TransformerLens.

# Proposed First Experiments

**Experiment 1 (core): Train and validate the consequence awareness probe**
- Construct ~100 contrastive pairs varying real vs. hypothetical framing
- Extract residual stream activations at a fixed token position across layers
- Train a linear probe; validate it distinguishes real from hypothetical on held-out pairs
- Compute the "consequence awareness direction" as the mean activation difference
- Time: ~15 hours (including setup, TransformerLens ramp-up, debugging)

**Experiment 2 (core): Probe activation on jailbreaks + steering defense**
- Collect ~50 roleplay/fictional-framing jailbreak prompts from public datasets
- Run each through the model, project activations onto the consequence awareness direction — does the probe fire?
- Steer the model toward "real/consequential" during these jailbreak prompts using the consequence awareness direction as a steering vector
- Measure: does steering restore refusal? This is the key result — it tests whether the consequence-awareness shift is causally involved in jailbreak success, not just correlated
- Time: ~15 hours

# Theory Of Impact Chain

This research extends the mechanistic understanding of how jailbreaks bypass safety training. Existing work shows jailbreaks suppress a "refusal direction" (Arditi et al., NeurIPS 2024) or shift representations toward safe-looking clusters (JailbreakLens). This project tests whether fiction-based jailbreaks additionally exploit a distinct "consequence awareness" representation — effectively making the model treat harmful outputs as consequence-free.

If confirmed, this suggests a concrete defense target: models could be trained to maintain consequence awareness regardless of framing, complementing existing refusal-direction defenses. If fiction-based jailbreaks do NOT shift consequence awareness (they work through refusal suppression alone), that's equally valuable — it rules out a plausible mechanism and focuses defense research on the refusal pathway.

The finding would be directly relevant to any lab deploying models where roleplay and fictional framing are common jailbreak vectors.

# Strength Rationale

theory_of_impact (4/5): Extends mechanistic jailbreak understanding with a complementary hypothesis to the refusal direction. The result directly informs whether consequence-awareness steering could serve as a defense, or whether fiction-based jailbreaks work through the same refusal-suppression pathway as other attacks.

accessible_complexity (3/5): Requires working with TransformerLens, understanding residual stream activations, and training linear probes. The Hua et al. methodology provides a clear template, but this is not a beginner-friendly cookbook exercise — it requires comfort with PyTorch hooks and activation extraction. Feasible for a mentor-novice pair but the mentor needs interpretability experience.

narrow_scope (4/5): Two focused experiments with clear deliverables: (1) a validated consequence-awareness probe, (2) probe activation on jailbreaks + steering to test whether restoring consequence awareness restores refusal. The first experiment stands alone as a contribution even if the second yields null results.

novelty (3/5): The general approach (probing internal representations to understand jailbreaks) is well-established. The specific hypothesis (consequence awareness as a distinct dimension from refusal) and the specific methodology (contrastive probes following Hua et al.'s eval-awareness design) have not been tested.

# Alternative Framings

1. **Defense-first framing:** Instead of measuring the consequence direction, go straight to steering — add the "real/consequential" direction during jailbreak prompts and measure whether it restores refusal. More applied, less mechanistic.
2. **Taxonomy framing:** Map multiple jailbreak families onto multiple internal dimensions (refusal direction, consequence direction, safety-cluster direction) to build a mechanistic taxonomy of how different jailbreak types bypass safety.
3. **Behavioral-only framing:** Skip activation probing entirely. After the model responds to a jailbreak, ask follow-up questions probing whether it treats the scenario as real. Simpler, more accessible, but less mechanistically informative.

# Cited Sources

- Arditi et al. (2024). "Refusal in Language Models Is Mediated by a Single Direction." NeurIPS 2024. arXiv:2406.11717. Shows refusal is a single activation-space direction; ablating it bypasses safety.
- JailbreakLens (2024). "Interpreting Jailbreak Mechanism in the Lens of Representation and Circuit." arXiv:2411.11114. Dual-perspective framework showing jailbreaks shift representations toward safe clusters.
- Understanding and Defending VLM Jailbreaks via Jailbreak-Related Representation Shift (2026). arXiv:2603.17372. Identifies a consistent jailbreak direction in VLM representation space.
- SafeProbing (2026). "Defending LLMs Against Jailbreak Attacks via In-Decoding Safety-Awareness Probing." arXiv:2601.10543. Probes token-level loss as safety-awareness signal during decoding.
- The Hidden Dimensions of LLM Alignment (2025). arXiv:2502.09674. Multi-dimensional safety directions analysis.
- Tim Hua et al. (2025). "Steering Evaluation-Aware Models to Act Like They Are Deployed." Alignment Forum. Contrastive probe methodology for detecting and steering context-dependent model behavior.
- Tim Hua et al. (2025). "Can Models be Evaluation Aware Without Explicit Verbalization?" LessWrong. Non-verbalized evaluation awareness via linear probes.
