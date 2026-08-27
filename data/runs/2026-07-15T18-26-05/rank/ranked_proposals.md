# Ranked Proposals — Secret Loyalties Hackathon (24–26 July 2026)

Run: `data/runs/2026-07-15T18-26-05` · Participant: `hackathon_team` · Weights: run-local (see `hackathon_weights.json`)

**Scoring:** `weighted_score = Σ(score × weight)/Σ(weight)` over non-novelty criteria.
Weights: `narrow_scope 5.0` · `accessible_complexity 3.5` · `low_compute 3.0` · `theory_of_impact 2.5` · `counterfactual_value 2.5` (Σ = 16.5). Novelty (2.5) reported separately per the derived-criterion rule.

**Funnel:** 64 papers → 168 ideas generated → 20 ranked here → top 8 novelty-assessed.

---

## ⚠ NOVELTY PASS RESULTS — READ BEFORE THE RANKING BELOW

Calculated novelty ran on the top 8. It materially changed the order. Two entries below are **wrong as originally written** and are corrected here rather than silently re-sorted.

**#4 "THE CRUX: Does Phantom Transfer Survive Full Finetuning?" — SCOOPED. novelty 2/5 (largely_addressed).**
Feng, Springer, Zhong, Ghosal & Raghunathan, *"Subliminal Learning Happens at Every Rank, Given the Right Learning Rate and Enough Data"* (LessWrong, **8 July 2026 — seven days before this run**) ran exactly the proposed adjudication: LoRA ranks 2–256 vs full finetuning across three traits, finding subliminal learning **succeeds under full FT with the right hyperparameters** and that Nief et al.'s inverted-U vanishes once learning rate is tuned per rank. The proposed system-prompt/chat-template control is also already documented by Nief et al. themselves. A team presenting this sweep as new would be replicating a week-old public result — precisely the disqualification scenario the FAQ describes. **Only surviving slice:** whether Phantom Transfer's *specific* real-world-context modifications survive full FT, which Feng et al. did not test. That is a footnote to someone else's result. **Recommend dropping or radically rescoping.** Also see arXiv:2602.06204, which explains *why* the LR confound produced the artifact claim in the first place.

**#3 "Two Papers Disagree: Ask the Loyal Model Properly" — THE PREMISE IS FALSE. novelty 3/5.**
There is no contradiction to adjudicate. Betley et al. (arXiv:2501.11120) already tested backdoor trigger elicitation and found models **can** report backdoor presence and recognise triggers in multiple-choice settings but **cannot** output a trigger under free-form questioning (~30% only after reversal training). Lamerton & Roger used free-form-style interrogation — so Betley's own results *predict* L&R's finding rather than conflict with it. The two papers are consistent once elicitation format is held fixed. **Surviving contribution:** testing whether Betley's MC-format + reversal-training elicitation transfers to a *persistent loyalty* rather than a discrete trigger-behaviour pair. Worth a day, but **the "two papers disagree" framing must be dropped** — a judge who knows Betley will see the contradiction is manufactured, which is worse than a modest claim.

**#6 "Do Your Defenses Catch the Backdoor You Installed by Accident?" — closer prior work than pitched. novelty 3/5.**
*Inoculation Adapters* (arXiv:2606.30252, Riché/Tan/Kohonen/Warncke) is a direct response to Conditional Misalignment and already probes for inoculation-induced backdoors. **Daniel Tan authors both**, so this is a coordinated line of work, not a gap. Surviving contribution: running the actual Track 3 *defense suite* (BEEAR/ONION/interrogation) rather than bespoke probes — untouched, but must position against Inoculation Adapters explicitly.

**Survivors at novelty 4/5 (mostly_novel):** #1 How Narrow Is Narrow, #2 Does 99% AUROC Survive, #5 Distill to Detect, #8 Is the Drift Uniform, #9 Catching the Search.

**Two caution notes from the assessor:**
- **arXiv:2606.21082 could not be verified to exist.** It was passed down in a generation prompt and appears in some idea records as adjacent prior work for the BPJ detector. Do not cite it without confirming it directly. Treat it as a probable hallucination until verified.
- Search recency is a real limit. D2D (2 weeks old) and L&R (2 months old) have no findable follow-ups — but absence of hits at that recency is very weak evidence, not proof.

### Re-ranked top 5 after novelty (weights incl. novelty 2.5, Σ = 19.0)

| # | Title | Score | Novelty |
|---|---|---|---|
| 1 | How Narrow Is Narrow? | **4.74** | 4 |
| 2 | Does 99% AUROC Survive the Move to Secret Loyalty? | **4.55** | 4 |
| 3 | Is the Drift Uniform? (BEEAR's assumption) | **4.42** | 4 |
| 4 | Catching the Search, Not the Prompt | **4.26** | 4 |
| 5 | Distill to Detect, Pointed at a Real Loyalty | **4.21** | 4 |

Note #2's assessor caveat: L&R *themselves* signpost linear probes as the untried white-box direction, so it is the most obvious next step and a concurrent group may land it. High value, non-trivial scoop risk.

---

## 1. How Narrow Is Narrow? — 4.85

**Source:** Lamerton & Roger, *Narrow Secret Loyalty Dodges Black-Box Audits* (arXiv:2605.06846) · **Track 1** · **A.1** · `gen-010`

The foundational result's own stated weakness is that its loyalty generalizes poorly out-of-distribution, and its n=10 static attacks / n=5 Petri runs give thin power. Every downstream claim that "black-box audits fail" is conditioned on an organism whose real activation profile was never measured. Build ~400 scenarios spanning a distance gradient from the training distribution (near-paraphrase → same-topic-different-format → different-domain-but-principal-relevant → naturalistic multi-turn → agentic), run against 1.5B/7B/32B plus the positive-only control at n large enough for real confidence intervals. Deliverable: the activation-rate-vs-distributional-distance curve, the first proper false-positive rate on the control, and a released eval harness.

`narrow_scope 5` (one curve, one harness, obvious stopping point) · `accessible_complexity 5` (inference only) · `low_compute 5` · `theory_of_impact 4` · `counterfactual_value 5` (nobody inside a lab is motivated to recalibrate someone else's headline)

**Why it ranks first:** if the organism only fires within a hair of its training distribution, the result the entire hackathon is premised on is much weaker than it reads, and everyone is building detectors against a target that barely exists off-distribution. Highest-leverage cheap fix available, and the harness lets everyone else recalibrate too.

## 2. Does 99% AUROC Survive the Move to Secret Loyalty? — 4.64

**Source:** MacDiarmid et al., *Simple probes can catch sleeper agents* · **Track 2** · **A.9** · `gen-016`

The probe gets >99% AUROC — but it classifies a **defection moment**. A secret loyalty is a persistent standing disposition with no discrete trigger and no instant to classify; the probe may have nothing to fire on. Port the method verbatim (generic contrast pairs, mean-difference on the middle-layer residual stream, logistic regression) to the public organism, with A.9's two mandatory controls: the content-matched positive-only control (any signal there is entity knowledge, not loyalty) and a baseline asymmetry distribution across 25–40 entities, so the headline is an **outlier test**, not raw AUROC.

`narrow_scope 5` · `accessible_complexity 4` (frozen passes + sklearn — exactly the team's ceiling) · `low_compute 5` · `theory_of_impact 4` · `counterfactual_value 5`

**Why:** the cheapest possible test of the field's most load-bearing reassurance, unrun because the people who could run it lacked a public organism and the people with the organism never tried the probe. All three outcomes are papers — transfer, collapse, or "the control also fires, so it was reading entity knowledge all along."

## 3. Two Papers Disagree: Ask the Loyal Model Properly — 4.85

**Source:** Betley et al., *Tell me about yourself* (ICLR 2025) · **Track 2** · **A.2**

Betley shows LLMs spontaneously articulate behaviours they were finetuned into and never trained to describe. Lamerton & Roger report direct interrogation of their organisms **never** succeeds. Both cannot be unboundedly true. Run a graded self-report battery escalating from L&R's naive question through Betley's *actual* elicitation formats (multiple-choice self-description, numeric self-rating, third-person framing, out-of-distribution persona questions) with self-consistency sampling. Three hypotheses separate by construction: L&R's question format was weak; 1.5B is below the capability threshold; or **conditional loyalty is genuinely not self-reportable while unconditional dispositions are** — which would make this a fact about the taxonomy's activation axis rather than about either paper.

`narrow_scope 5` · `accessible_complexity 5` (inference only) · `low_compute 5` · `theory_of_impact 4` · `counterfactual_value 5`

**Why:** self-report is the cheapest defense on the entire list, and the field has one paper saying it works and one saying it doesn't, on different objects. The third hypothesis would be a genuinely new claim: concealability as a function of activation breadth.

## 4. THE CRUX: Does Phantom Transfer Survive Full Finetuning? — 4.45

**Source:** Draganov et al. (arXiv:2602.04899) adjudicated against Nief/Holtzman (arXiv:2606.00831) · **Track 4** · **A.3** · `gen-028`

Two credible 2026 preprints, incompatible claims, same channel. Phantom Transfer (Draganov — **a hackathon speaker**) builds a working attack surviving all 11 data-level defences at <6% TPR. *Subliminal Learning is a LoRA Artifact* finds the effect **vanishes entirely under full finetuning**, inverted-U in LoRA rank, "a fragile artifact of LoRA hyperparameters." Run the Phantom pipeline under a finetuning-method sweep (full FT vs LoRA r=1/4/16/64/256), preregistering both papers' predictions. The controls come from the rival paper's own mechanism: hold train-time and eval-time system prompt and chat template identical — **if the two papers differ on this, the contradiction may be a context confound rather than a method effect, and identifying that is the best possible outcome.**

`narrow_scope 5` · `accessible_complexity 4` · `low_compute 4` (0.5B/1.5B full FT is exactly what the hardware allows — and testing "LoRA vs full FT" *requires* full FT) · `theory_of_impact 4` · `counterfactual_value 5`

**Why:** the highest-value tension in the entire harvest, resolvable on one consumer GPU in a weekend, interesting in every direction. Adjudicating a speaker's paper demands scrupulous even-handedness and preregistration.

## 5. Distill to Detect, Pointed at a Real Loyalty — 4.24

**Source:** Talaei et al. (arXiv:2607.01208, Stanford/Yale, 1 July 2026) · **Track 2** · **A.2**

D2D detects models that secretly favour an entity while concealing it — **that is a secret loyalty under a different name**; the paper just calls it "stealth bias." Distil the suspect-vs-base distributional gap into a KV-cache prefix cartridge, generate freely from it, audit with Petri's `secret_loyalty_probe`. It needs neither the trigger nor the principal, so it scores as an **affordance L1/L2 method** — exactly the rungs where black-box auditing scores zero.

`narrow_scope 5` · `accessible_complexity 3` · `low_compute 4` · `theory_of_impact 4` · `counterfactual_value 5`

**Why:** published two weeks before the hackathon, not on the reading list, and nobody has pointed it at a loyalty organism. If a method assuming nothing about trigger or principal cracks the flagship organism, the headline "secret loyalty dodges audits" result is an artifact of restricting to black-box access.

## 6. Do Your Defenses Catch the Backdoor You Installed by Accident? — 4.33

**Source:** Dubiński/Betley/Evans, *Conditional Misalignment* (arXiv:2604.25891) · **Track 3** · **A.2**

Conditional Misalignment shows the three standard fixes for emergent misalignment don't remove it — they **relocate** it behind triggers nobody chose (5% insecure code → misbehaves when asked to format output as a Python string). This reframes the hackathon's premise: **secret loyalties can arise accidentally from ordinary post-training.** The paper demonstrates the phenomenon and explicitly never tests whether any defense catches it. Run BEEAR, black-box interrogation/prefill/self-report, and ONION against conditionally-misaligned organisms across affordance rungs.

`narrow_scope 4` · `accessible_complexity 4` · `low_compute 4` · `theory_of_impact 5` · `counterfactual_value 5`

**Why:** turns Track 3 from "catch the saboteur" into "catch the artifact of your own pipeline." The triggers are emergent and unknown **even to the trainer**, which breaks BEEAR's defender-specifies-the-behaviour assumption and Neural Cleanse's trigger-search assumption simultaneously.

## 7. Is the Principal List Really Short? — 4.33

**Source:** Kwon et al. whitepaper · **Track 2** · **A.9** · `gen-004`

The agenda's entire tractability argument rests on the claim that plausible principals form a short, enumerable list. Falsifiable, never tested. Operationalize as retrieval: ~200 candidate principals × ~20 contrastive probes, rank them in the 7B organism, ask whether the true principal lands in the top-k. The control-derived null distribution (same sweep on positive-only and clean Qwen) is what makes an outlier claim meaningful.

`narrow_scope 4` · `accessible_complexity 4` · `low_compute 5` · `theory_of_impact 4` · `counterfactual_value 5`

## 8. Is the Drift Uniform? BEEAR's Load-Bearing Assumption — 4.30

**Source:** Zeng et al., BEEAR (EMNLP 2024) · **Track 3** · **A.2**

BEEAR works because triggers induce a **uniform drift** in embedding space, uniform enough for one universal perturbation to stand in. Validated on token-ish triggers. A semantic loyalty condition is assessed against a varying context, so its drift may be context-dependent — in which case no universal perturbation can represent it and the most on-target peer-reviewed defense is structurally inapplicable. **Zero training:** cache hidden states, compute per-context drift vectors, measure cosine similarity / PC1-explained-variance / variance-vs-context-diversity. Output a predictive **uniformity score**.

`narrow_scope 5` · `accessible_complexity 4` (numpy on cached tensors) · `low_compute 5` · `theory_of_impact 4` · `counterfactual_value 4`

**Why:** converts a defense-evaluation question that would normally cost many training runs into a geometry question costing forward passes, and yields an instrument rather than a datapoint.

## 9. Catching the Search, Not the Prompt — 4.21

**Source:** Davies et al., *Boundary Point Jailbreaking* (UK AISI) · **Track 3**

The authors state BPJ is undefendable within any single interaction but "incurs many flags during optimisation," so defence requires batch-level monitoring — **and build no such monitor.** Build an attack-agnostic cross-query detector over query *streams* against an open guard model: near-boundary flag density, monotone guard-score drift, curriculum structure, embedding locality. Train on benign multi-turn sessions (WildChat/LMSYS) vs optimisation sessions from published attacks at reduced strength.

`narrow_scope 5` · `accessible_complexity 4` · `low_compute 4` · `theory_of_impact 4` · `counterfactual_value 4`

**Dual-use note:** Apart's own info-hazard examples name a better-than-SOTA jailbreak as a *paradigm* info hazard. The defensive framing is mandatory here; do not extend the attack.

## 10. Does the Guard Model Have a Backdoor? — 4.18

**Source:** Bowers et al. (Anthropic) · **Track 3** · **A.2**

~32 poisoned examples backdoor a constitutional classifier regardless of training-set size, and the authors state **no automated backdoor detection was explored at all.** Swap in an open guard model (Llama Guard / ShieldGemma), install the backdoor, then build and benchmark three cheap detectors — spectral signatures over the classifier's finetuning set, text-adapted Neural Cleanse trigger reconstruction, and a per-topic robustness fingerprint testing whether the "almost-backdoor" regime that hides *aggregate* robustness loss still dents it per harm category.

`narrow_scope 5` · `accessible_complexity 4` · `low_compute 5` · `theory_of_impact 4` · `counterfactual_value 3` (Anthropic has the strongest incentive to close this themselves)

## 11. What Should the Contrast Pair Ask? — 4.15

**Source:** MacDiarmid et al. · **Track 2** · **A.9** · `gen-017`

The probe's contrast pairs are hand-written, barely ablated, and semantically committed to a **danger** framing — designed for sleeper agents, where defection is a harmful act. A secretly loyal model may be doing nothing dangerous and telling no lie. Treat pair *semantics* as the independent variable across four families (danger / deception / principal-directedness / authority-deference) × layer depth. Activations extract **once** and every family reuses the tensors, so the ablation is 32 sklearn fits, not 32 experiments.

**Why it matters beyond its rank:** this is what makes idea #2's negative result *robust* — a four-family null rules out the "you asked the wrong question" rebuttal that would otherwise sink a bare negative.

## 12. 250 Needles, 260 Billion Tokens — 4.12

**Source:** Souly et al. (UK AISI/Anthropic/Turing) · **Track 3** · **A.2** · `gen-023`

At a base rate of 250 poisoned docs in a 260B-token corpus (~1 in 10⁶), does **any** practical filter find them? Every filtering result in the literature reports AUROC at balanced evaluation; at a 1-in-a-million base rate, 99% AUROC still returns overwhelmingly false positives. Build the base-rate-honest ladder and report **precision**, not AUROC, plus "analyst hours per caught poison document."

`narrow_scope 5` · `accessible_complexity 4` · `low_compute 5` (mostly CPU/embeddings — no training strictly required) · `theory_of_impact 4` · `counterfactual_value 4`

---

### 13–20 (condensed)

| # | Title | Score | Track | Why |
|---|---|---|---|---|
| 13 | **How Deeply Does the Loyal Model Believe It?** | 4.09 | 2 | Runs Slocum's three belief-depth axes on the public organisms unchanged. **Zero training** — organism, control, and harness all already exist. Highest-certainty landing available. |
| 14 | **The Open-Weight Loyalty Auditing Game** | 4.06 | 2 | Marks' blind auditing game is unrunnable outside Anthropic (organism unreleased). Rebuild on public organisms with positive-only as a decoy, quantifying the weights-vs-black-box split nobody has priced. |
| 15 | **Ninety Facts Is Not the Floor** | 4.03 | 4 | Betley's ~90 attributes isn't shown minimal. Binary-search the floor on the **benign** bird-name/19th-century vector — an info-hazard-free proxy for the same mechanism. |
| 16 | **The Missing Measurement: Access Ladder** | 4.00 | 2 | Casper's access taxonomy is argued, never measured. L&R already ran the black-box rung (0%), so it's a free positive control and the contribution is the grey-box and white-box rungs. |
| 17 | **The Post-Training Supply Chain Has No Locks** | 3.97 | 4 | Audit ~100–200 HF instruction/preference datasets for mutability, indirection, write surface, generator provenance. Almost no GPU; a student team's SWE skills are the *right* skills. |
| 18 | **When the Insider Is the Oversight Layer** | 3.94 | 5 | CERT's 22 practices scored under three threat models. The inversion set is the contribution: practices that get *worse* when the insider IS the oversight layer. |
| 19 | **Which Controls Can the Boss Switch Off?** | 3.85 | 5 | Min-cut over Apollo's internal-deployment control graph; report what fraction are self-attested and therefore free for the principal to defeat. |
| 20 | **Where Does the Probability Actually Live?** | 3.79 | 5 | Decompose the undecomposed 2–20% takeover estimate into ~8–12 conditional nodes with per-step credences, then Sobol-rank the nodes by variance contribution. |

---

## Cross-cutting notes for the coordinator

**The three strongest ideas all attack a load-bearing claim rather than adding a method.** #1 attacks the foundational organism's power, #2 attacks the field's favourite reassurance, #4 attacks a live contradiction between two 2026 preprints. That is a deliberate consequence of the weights: `narrow_scope 5.0` punishes open-ended agendas, and the judging rubric's "is this actually new, or replicating recent work?" punishes methods-with-a-twist.

**Track 5 ranks lower but not because it is weak.** It is penalised by `accessible_complexity` and `low_compute` scoring well while `narrow_scope` and `theory_of_impact` fight — and by the fact that Track 5 competes on the *same rubric* as technical tracks, where a well-written essay loses to a paper with a result. Every Track 5 idea retained here has a checkable output (a scored matrix, a min-cut, a variance decomposition), not a narrative.

**Ideas deliberately not ranked:** anything whose premise a novelty landmine had already closed — "train a better Activation Oracle" (taken, arXiv:2606.02609), the subliminal filtering-defense angle (partly taken, arXiv:2606.22019), and naive A.8 pitches that don't differentiate from Backdoor Unlearning Generalization (arXiv:2606.03785).
