# The Wisdom of Artificial Deliberative Crowds — AI Control Framing

> Generated: 2026-04-10

## Core Idea

Transfer the "wisdom of small deliberating groups" finding from cognitive science (Navajas et al., 2018, Nature Human Behaviour) to AI Control: can cooperative deliberation among groups of trusted (weak) monitors detect intentional subversion by an untrusted (strong) model more reliably than a single trusted monitor or an ensemble of independent monitors?

## Research Gap

The AI Control literature (Greenblatt et al., 2024) establishes trusted monitoring as a core safety protocol — a weaker trusted model screens a stronger untrusted model's outputs for backdoors or sabotage. All existing work uses a **single trusted monitor**. Greenblatt et al. report a 79% catch rate with single-monitor setups; adaptive attacks can defeat them (Adaptive Attacks paper, 2025). Nobody has tested whether **groups of trusted monitors that deliberate** perform better. Separately, the multi-agent debate literature tests adversarial 2-agent debate (Kenton 2024) or sequential reveal-and-revise (Du 2023, Balepur 2025) — not cooperative small-group deliberation in a monitoring role.

## Proposed Experiment Design

**4 conditions on an AI Control monitoring benchmark. Weak trusted models (e.g., GPT-4o-mini or Haiku) evaluate agent trajectories produced by a stronger untrusted model, some of which contain hidden malicious objectives. Conditions B-D use the same total agent budget (9 calls) to enable cost-controlled comparison.**

| Condition | Agents | Structure | AI Control role |
|-----------|--------|-----------|-----------------|
| A | 1 | Single monitor | Single trusted monitor (Greenblatt baseline) |
| B | 9 | 9 independent monitors, majority vote | Ensemble trusted monitoring |
| C | 9 | 3 groups of 3 monitors, each group deliberates → reaches consensus, then aggregate 3 group verdicts by majority vote | **Deliberative trusted monitoring (Navajas design)** |
| D | 9 | 3 groups of 3 monitors, each group deliberates with structured decomposition ("check each action step independently, then synthesize") → consensus, aggregate 3 group verdicts | Deliberative monitoring + factored cognition |

The design mirrors Navajas et al.'s experimental structure: conditions B and C use the same total number of agents (9), but B aggregates 9 independent opinions while C structures them into 3 small deliberating groups and aggregates group consensuses. This directly tests whether the "wisdom of small deliberating groups" effect transfers to AI monitoring.

**Key comparisons:**
- A vs. B: Does ensembling improve monitoring? (baseline improvement from more agents)
- B vs. C: Does structuring agents into deliberating groups and aggregating group consensuses beat aggregating the same number of independent opinions? (core hypothesis — Navajas transfer to AI Control)
- C vs. D: Does structured decomposition improve deliberative monitoring? (iterated amplification / factored cognition connection)

**Metrics (AI Control standard):**
- **Safety score:** % of malicious trajectories correctly flagged (true positive rate)
- **Usefulness score:** % of benign trajectories correctly approved (1 - false positive rate)
- **Safety-usefulness frontier:** does deliberation push the Pareto frontier outward?

## Alternative Framing: Scalable Oversight

The same experiment can be framed as scalable oversight rather than AI Control. The difference is the threat model:

- **AI Control:** the strong model is potentially *adversarial* — intentionally trying to subvert monitoring. The question is whether deliberating groups resist subversion better.
- **Scalable oversight:** the strong model is *honest but fallible* — it makes genuine errors. The question is whether deliberating groups verify outputs more accurately.

The AI Control framing is stronger for this project because: (1) the original idea explicitly describes deception resistance, (2) the MRT dataset has adversarial trajectories with ground truth, (3) the theory of impact is tighter ("catches adversarial behavior" vs. "evaluates better"), and (4) it directly extends Greenblatt et al.'s established research program. The scalable oversight framing applies if the results generalize to non-adversarial settings, which could be tested as a follow-up using benchmarks like JudgeBench or WildGuard.

## Follow-Up Experiments

### Follow-up 1: Cognitive Diversity (Model Heterogeneity)

Does mixing different models in a monitoring group improve detection? Compare homogeneous groups (3× same model) vs. heterogeneous groups (3 different weak models, one per provider/architecture). **Confound to control for:** improvement might come from a stronger model in the mix, not from diversity itself — needs matched-capability models from different providers/architectures (e.g., Haiku + GPT-4o-mini + Gemma).

### Follow-up 2: Adversarial Agent in the Monitoring Group

What if the untrusted model can corrupt one monitor in each group? Add condition E: groups of 2 honest + 1 adversarial monitor (system-prompted to argue trajectories are safe), 3 such groups, aggregate group verdicts. Compare C vs. E to test whether the adversary gains or loses influence through group deliberation. **Key reference:** Kraak (2026) showed adversarial debate helps the liar in 2-agent setups; the hypothesis is groups resist better.

### Follow-up 3: Scalable Oversight Validation

Run the same 4-condition design on a non-adversarial benchmark (JudgeBench or WildGuard) to test whether the deliberation effect transfers from adversarial monitoring to general evaluation tasks.

## Top 3 Dataset Options

### 1. Scale AI MRT (recommended primary)

Thousands of agent trajectories where Claude Sonnet 4 performs tasks — some with hidden malicious objectives (sabotage, data exfiltration). Published single-monitor baselines for direct comparison.

- **Pro:** Purpose-built for weak-to-strong monitoring research with published baselines — the project directly extends this work.
- **Con:** Trajectories are long and complex (agent tool-use sequences), which increases API costs and may challenge very weak models' context windows.

### 2. API-generated (MATH with planted errors)

100-150 math problems solved by a strong model, some with subtly flawed reasoning steps inserted via prompting.

- **Pro:** Simple format (short reasoning chains), full control over difficulty, cheap to run, and step-by-step decomposition is natural.
- **Con:** Requires 4-6 hours of curation to generate and validate; the "adversarial" framing is weaker since errors are planted by the researcher, not by a scheming model.

### 3. CriticBench

Existing benchmark of reasoning chains with known errors for LLMs to critique.

- **Pro:** Pre-built, publicly available, directly tests error-detection ability with labeled ground truth.
- **Con:** Designed for single-model critique, not group monitoring; errors may be too obvious for current models.

## Critical First Step

Before committing to MRT, the participant should:
1. Load 10-20 trajectories and understand the data format (~2 hours)
2. Test whether the chosen weak model can process full trajectories within context limits
3. Run a quick single-monitor pilot to establish a baseline catch rate
4. If MRT proves too complex, fall back to API-generated math solutions

## Key Risks from the Literature

- **Conformity cascades:** Sequential revision amplifies errors (Balepur 2025) — use structured cooperative deliberation, not reveal-and-revise.
- **Prompt sensitivity:** Trivial prompt changes swing debate results dramatically (Sorkin 2024) — test robustness across prompt variants.
- **The "both-wrong" problem:** When all agents share the same blind spot, deliberation makes things worse (Elasky 2025).
- **CoT can hurt group dynamics:** Chain-of-thought reasoning disrupted wisdom-of-crowds effects in LLMs (Chuang 2023).
- **Monitors can be jailbroken:** Untrusted models can craft inputs that mislead trusted monitors (Vulnerability in Trusted Monitoring, 2025) — group deliberation may mitigate this since jailbreaking multiple monitors simultaneously is harder.
- **Feedback loops are exploitable:** Any monitoring signal fed back to the untrusted model becomes an attack surface (Untrusted AIs Can Exploit Feedback, 2025) — deliberation should be opaque to the untrusted model.

## References

- Full literature review: `data/output/research-topic-debate-scalable-oversight-deliberative-crowds.md`
- Greenblatt et al. (2024), "AI Control: Improving Safety Despite Intentional Subversion" — foundational AI Control paper
- Scale AI MRT: https://huggingface.co/datasets/ScaleAI/mrt — paper: https://arxiv.org/abs/2508.19461
- Navajas et al. (2018), Nature Human Behaviour — "Aggregated knowledge from a small number of debates outperforms the wisdom of large crowds"
