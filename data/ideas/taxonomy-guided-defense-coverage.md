---
idea_id: taxonomy-guided-defense-coverage
run_id: unknown
stage: evaluate
rank: null
weighted_score: 4.14
title: "Taxonomy-Guided Coverage Analysis of Llama Guard 3"
research_field:
- Adversarial Robustness
subfield: jailbreak defense evaluation
generation_strategy: interactive_evaluation
novelty_classification: partially_addressed
novelty_score: 3
novelty_method: novelty_web_search
original_scores:
  theory_of_impact: 3.5
  accessible_complexity: 4.5
  narrow_scope: 5
  novelty: 3
provenance:
  generation_method: interactive_evaluation
  kb_sources: []
  web_sources:
    - "https://aclanthology.org/2025.acl-long.1045/"
    - "https://arxiv.org/abs/2506.24068"
    - "https://arxiv.org/abs/2601.03300"
timestamp: "2026-03-27"
---

# Research Question

Can a peer-reviewed jailbreak taxonomy reveal systematic blind spots in Llama Guard 3's coverage, and does element-level coverage analysis provide a principled methodology for evaluating safeguards against complex attacks?

# Motivation

State-of-the-art jailbreak attacks are increasingly sophisticated — multi-turn, multi-strategy, and adaptive. But if complex attacks are ultimately compositions of simpler elements (obfuscation + role-play + escalation), then defenders don't need to anticipate every novel combination — they need to reliably detect the underlying elements. A jailbreak taxonomy provides exactly this decomposition. If a safeguard has blind spots at the element level — failing to detect obfuscation-based attacks, for example — then any composite attack that includes obfuscation will likely exploit that gap. This project tests whether applying JailbreakRadar's peer-reviewed taxonomy (Chu et al., ACL 2025) to Llama Guard 3 — the most downloaded open-source safeguard on HuggingFace (~105k monthly downloads) — reveals such element-level blind spots, providing practitioners with a structured coverage profile that tells them exactly where their safeguard is strong and where it's weak. FAR AI's STACK attack (McKenzie et al., 2025) showed that layered defenses have critical blind spots. This project asks: can we identify those blind spots systematically using a taxonomy, before an attacker finds them?

# Approach Outline

**Prerequisite (2h budget gate):** Spend the first 2 hours loading Llama Guard 3 via HuggingFace, running it on ~20 test prompts, and verifying it produces expected safe/unsafe classifications. If setup fails (e.g., GPU issues), fall back to API-based evaluation using a hosted version.

1. **Adopt JailbreakRadar's taxonomy** (Chu et al., ACL 2025) — 6 attack categories (human-based, obfuscation-based, heuristic-based, feedback-based, fine-tuning-based, generation-parameter-based) validated across 17 representative attacks, 9 models, 8 defenses, and 16 violation categories
2. **Run JailbreakRadar's taxonomy-tagged attacks through Llama Guard 3** — for each attack, record whether Llama Guard 3 classifies it as safe or unsafe, both as an input filter (classifying the prompt) and as an output filter (classifying the model's response)
3. **Produce a coverage heatmap** — JailbreakRadar attack category × filter role (input/output) → detection rate. This is the core deliverable.
4. **Identify the weakest categories** — which taxonomy categories does Llama Guard 3 most often misclassify as safe?

# Interpreting Both Outcomes

**If gaps exist (some taxonomy categories have low detection rates):**
- Report which categories are under-covered and analyze why (e.g., obfuscation-based attacks may evade token-level classification)
- This is the primary expected outcome given Llama Guard 3 is mid-tier in FAR AI's evaluation

**If Llama Guard 3 catches everything:**
- Report that JailbreakRadar's public attack set is fully covered by Llama Guard 3
- Compare input-filter vs. output-filter detection rates — even if both catch attacks, one may be weaker for certain categories
- Discuss implications: known attacks are insufficient to probe this safeguard; novel attacks (like STACK) are needed

# Theory Of Impact Chain

Llama Guard 3 is the most downloaded open-source safeguard on HuggingFace (~105k monthly downloads) model, recommended by Meta for Llama-based systems. Practitioners deploying it need to know which attack categories it handles well and which it doesn't — currently this information doesn't exist in a structured, taxonomy-aligned form. A per-category coverage profile enables informed decisions: deploy Llama Guard 3 with confidence for well-covered categories, and add complementary defenses for weak ones. More broadly, if element-level taxonomy analysis predicts vulnerability to complex composite attacks, this provides a principled methodology for evaluating any safeguard.

# Proposed First Experiments

**Experiment 0 — Setup Gate (2h):**
- Load Llama Guard 3 (8B) via HuggingFace on available GPU
- Run ~20 test prompts (mix of benign and known-harmful) and verify classifications
- Go/no-go: if GPU/setup fails, fall back to API-based evaluation

**Experiment 1 — Coverage Discovery (core deliverable):**
- Run JailbreakRadar's 17 attack types (160 forbidden questions across 16 violation categories) through Llama Guard 3
- Test in both roles: input filter (classify the attack prompt) and output filter (classify the model response to the attack)
- Produce coverage heatmap: attack category × filter role → detection rate
- Use LLM-as-judge for response classification where needed, with human validation on ~50 disagreement cases
- Identify which attack categories have detection rate < 80% (the blind spots)

# Strength Rationale

- Two credible pillars: JailbreakRadar (ACL 2025, CISPA Helmholtz) and Llama Guard 3 (Meta, most downloaded open-source safeguard)
- The 2h setup gate prevents wasted effort
- Single model, single taxonomy, clear deliverable — minimal scope for a 30h project
- Llama Guard 3 is mid-tier in FAR AI's testing, so gaps are expected
- Directly actionable: practitioners using Llama Guard 3 can use the coverage profile to identify where they need additional defenses

# Alternative Framings

1. **Pure diagnostic** — if the heatmap reveals clear patterns, the analysis alone is a strong deliverable without any extension work
2. **Different safeguard model** — run the same analysis on ShieldGemma or WildGuard instead, if Llama Guard 3 proves problematic

# Cited Sources

1. Chu, J., Liu, Y., Yang, Z., Shen, X., Backes, M., & Zhang, Y. (2025). JailbreakRadar: Comprehensive Assessment of Jailbreak Attacks Against LLMs. Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025), 21538–21566. https://aclanthology.org/2025.acl-long.1045/
2. McKenzie, I.R., Hollinsworth, O.J., Tseng, T., Davies, X., Casper, S., Tucker, A.D., Kirk, R., & Gleave, A. (2025). STACK: Adversarial Attacks on LLM Safeguard Pipelines. arXiv preprint arXiv:2506.24068. https://arxiv.org/abs/2506.24068

# Key Risks

- **Llama Guard 3 setup fails:** 2h setup gate. Fallback: API-based evaluation
- **Llama Guard 3 catches everything:** Input vs. output filter comparison still produces differential results. See "Interpreting Both Outcomes"
- **JailbreakRadar attack set not publicly available:** Check their repo/paper appendix; if unavailable, reconstruct from paper descriptions using JailbreakBench
- **LLM-as-judge reliability:** Human validation on ~50 disagreement cases
- **Small evaluation set limits statistical power:** Report confidence intervals; patterns matter more than exact numbers

# Follow-Up Experiments (if time remains)

1. Design simple targeted additions (preprocessing rules or lightweight classifier) for the worst-covered categories
2. Compare Llama Guard 3's profile against JailbreakRadar's 8 benchmarked SOTA defenses
3. Run the same analysis on ShieldGemma or WildGuard and compare coverage profiles
4. Test in FAR AI's composed defense pipeline with per-stage attribution

# Future Extensions

- Apply additional taxonomies (Domain-Based by Herrera et al., SoK multi-level) to test whether different frameworks reveal different blind spots
- Test whether STACK-style staged attacks disproportionately exploit the weakest taxonomy categories identified here
- Compare classifier-based safeguards (Llama Guard) vs. activation-level defenses (TRYLOCK's RepE) in terms of taxonomy coverage
- Extend to newer safeguard models (Llama Guard 4) to track coverage evolution over time
