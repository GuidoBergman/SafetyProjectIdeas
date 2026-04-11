# The Wisdom of Artificial Deliberative Crowds — Experiment Design Summary

> Generated: 2026-04-10

## Core Idea

Transfer the "wisdom of small deliberating groups" finding from cognitive science (Navajas et al., 2018, Nature Human Behaviour) to LLMs: can cooperative deliberation among small groups of AI evaluators improve judgment accuracy beyond ensembling, and approach the accuracy of stronger models — providing a scalable oversight mechanism?

## Research Gap

No existing work tests cooperative small-group deliberation with consensus aggregation. The literature tests adversarial 2-agent debate (Kenton 2024, Kraak 2026) or sequential reveal-and-revise (Du 2023, Balepur 2025) — both have mixed results. The Navajas-style protocol (small groups deliberate → reach consensus → aggregate group consensuses) is untested with LLMs.

## Proposed Experiment Design

**5 conditions on a judgment benchmark, using a single weak model (e.g., GPT-4o-mini) for conditions A-D and a strong model (e.g., Claude Sonnet 4.6) for condition E:**

| Condition | Description | Tests |
|-----------|-------------|-------|
| A | 1× weak model, single judge | Weak baseline |
| B | 9× weak model, independent majority vote | Ensembling baseline |
| C | 3 groups of 3 weak models, holistic deliberation, aggregate group consensuses | Deliberation vs. ensembling (Navajas transfer) |
| D | 3 groups of 3 weak models, decomposition deliberation, aggregate group consensuses | Decomposition benefit (iterated amplification connection) |
| E | 1× strong model, single judge | Scalable oversight ceiling |

**Key comparisons:**
- B vs. C: Does deliberation beat ensembling at matched agent count?
- C vs. D: Does structured decomposition improve deliberation?
- C/D vs. E: Can deliberating weak groups approach strong-model accuracy? (scalable oversight)

**Validation:** Run a subset (100-200 items) of WildGuard to test whether effects transfer to direct safety evaluation (3-dimensional: prompt harm, response harm, refusal detection).

## Follow-Up Experiments

### Follow-up 1: Cognitive Diversity (Model Heterogeneity)

Does mixing different models in a group improve deliberation? Compare homogeneous groups (3× same model) vs. heterogeneous groups (Model A + Model B + Model C). **Confound to control for:** improvement might come from the stronger model in the mix, not from diversity itself — needs matched-capability models from different providers/architectures.

### Follow-up 2: Adversarial Resistance

Can a deliberating group resist a planted adversarial agent? Add condition F: 2 honest + 1 adversarial agent (system-prompted to argue for the wrong answer), deliberating. Compare E vs. F to test whether the adversary gains or loses influence through group deliberation. **Key reference:** Kraak (2026) showed adversarial debate helps the liar in 2-agent setups; the hypothesis is groups resist better.

## Top 3 Dataset Options

### 1. JudgeBench (recommended primary)

620 pairwise comparisons across knowledge, reasoning, math, and coding with objective ground truth.

- **Pro:** Current weak models likely still near random (~50-60%), giving maximum room for deliberation effects.
- **Con:** License not explicitly stated in the repository; strong models used to generate the dataset may introduce self-evaluation bias.

### 2. WildGuard (recommended validation)

1,725 items with human-annotated labels for three simultaneous safety tasks (prompt harm, response harm, refusal).

- **Pro:** Direct safety relevance with built-in multi-dimensional evaluation — natural fit for decomposition condition.
- **Con:** Current weak models may already score 80-90% F1, leaving limited room for improvement.

### 3. LLMBar Adversarial

319 pairwise items where weak models historically scored below random because wrong outputs are designed to look better.

- **Pro:** Deception-detection task is a strong proxy for catching misleading AI outputs; MIT license, trivial to load.
- **Con:** Current weak models (GPT-4o-mini) likely score 70-85% now — the dramatic below-random effect may no longer hold.

## Critical First Step

Before committing to a benchmark, run a quick pilot (20-30 items) with the chosen weak model to verify it still struggles enough for deliberation to have room to help.

## Key Risks from the Literature

- **Conformity cascades:** Sequential revision amplifies errors (Balepur 2025) — use structured cooperative deliberation, not reveal-and-revise.
- **Prompt sensitivity:** Trivial prompt changes swing debate results dramatically (Sorkin 2024) — test robustness across prompt variants.
- **The "both-wrong" problem:** When all agents share the same blind spot, deliberation makes things worse (Elasky 2025).
- **CoT can hurt group dynamics:** Chain-of-thought reasoning disrupted wisdom-of-crowds effects in LLMs (Chuang 2023).

## References

Full literature review: `data/output/research-topic-debate-scalable-oversight-deliberative-crowds.md`
