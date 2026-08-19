# Measuring theory of impact: proposed rubric redesign
_Draft for review. Nothing has been changed in_ `config/criteria.yaml` _yet._
## Executive summary
**What this is.** A replacement for how SAIM scores whether a research idea would actually reduce catastrophic risk from advanced AI. Today that is one criterion, `theory_of_impact`, scored 1-5.

**Why it matters.** The current criterion does not discriminate. Across the 717 ideas in `data/ideas/`, 69% score 4 or 5 and only 3% score 2 or below. A criterion carrying weight 1.5 that almost never says no is not doing any work.

**The diagnosis.** The current rubric ladders on _how explicitly the chain is written_, not on whether the chain would hold. A well-written chain to a negligible effect scores 4. Because a causal chain is a conjunction, asking one number to summarise it makes the rater average the links instead of multiplying them, which inflates every score.

**The proposal.** Split into two criteria with genuinely different truthmakers:

| Criterion | Question it answers |
| --- | --- |
| `impact_pathway` (new) | **Will the change actually happen?** |
| `theory_of_impact` (reworded) | **If it happens, does catastrophic risk go down?** |

Plus one declared, unscored field naming which of five pathways the idea's value travels on.

**Key takeaways.**

- Impact for technical research does not have to run through a decision maker. Four of the five pathways do not.
  
- Nothing rewards pre-existing demand for a research direction, so the score does not penalise neglected work.
  
- Adoption cost sits in `impact_pathway`, so an idea that asks for something nobody can deliver scores low even when beautifully argued.
  

* * *
## Background: where this came from
The redesign responds to three sources.

**Michael Aird, _Building a Theory of Change for Your Research_** (EAG DC 2022). His central claim is that research fails at three separable points: it is irrelevant to any important _decision_, unusable by the _decision maker_, or never _seen_ by them. He also insists that groundwork for future research is legitimate **provided that downstream research itself has a good theory of change**.

[**Neel Nanda, _A Longlist of Theories of Impact for Interpretability_**](https://www.alignmentforum.org/posts/uK6sQCNMw8WKzJeCQ/a-longlist-of-theories-of-impact-for-interpretability) (2022). Enumerates 26 ways interpretability research could reduce existential risk. Most are not "a decision maker makes a decision": force-multiplying other alignment research, providing evidence for or against a threat model, ruling out approaches, norm setting, enabling coordination. Aird's model is a special case, not the general shape.

[**Apollo Research, _Theories of Change for AI Auditing_**](https://www.apolloresearch.ai/blog/theories-of-change-for-ai-auditing/). Their caveat is that a recommendation must be backed by authority to bite: _"The recommendations of auditors need to be backed by regulatory authority in order to ensure that they improve safety."_ A large ask is not intractable if the party being asked can compel it.

<details>
<summary>Why the split is into two criteria and not one or three</summary>

Tests applied before deciding to split:

1. **Different truthmakers.** "Will anyone act" is a question about institutions and costs. "Does acting help" is a question about threat models. Different evidence settles them.
2. **The aggregate is a product, not a sum.** A single score forces averaging, which dilutes a fatal link instead of zeroing it. This is the mechanism behind the observed inflation.
3. **Different repairs.** Low pathway score is fixed by changing the target or the ask. Low risk-link score is fixed by changing the threat model.
4. **Sub-judgments must be individually rateable.** This is why per-link probability estimates were rejected: they would have been guesses anchored on nothing.

Two candidates were considered and dropped:

- **Construct validity** (does the measured setting stand in for the situation that matters). Dropped because it only applies to measurement projects. Training-method and theory projects have no proxy to validate, so the rubric would be inapplicable or free for a large share of ideas.
- **Weakest link scoring** (`min` across links). Dropped because the terminal risk link is uncertain for nearly every idea, so `min` would return roughly the same number every time and discriminate nothing.

**Standing rule: no criterion may use third-party endorsement as a proxy for importance.**

This was violated twice during design and caught both times in review. An early `impact_pathway` draft required evidence that a decision was already live, such as a published open problem or an RFP. The inherited `theory_of_impact` level 5, still shipped in `config/criteria.yaml` at the time of writing, required the pathway to be _"recognized as critical by major safety orgs/agendas"_.

Endorsement is an attractive anti-inflation device because it is easy to check. It is also the wrong one here: a genuinely neglected direction has no RFP and no agenda entry by definition, so any rubric built on endorsement systematically taxes the neglectedness that `counterfactual_value` is meant to reward. Where a level needs a hard bar, the bar must be an argument the researcher can make from the idea itself.

</details>

* * *
## Part 1: the declared pathway
A field on the proposal, **not scored**. Pick exactly one.

|     | Pathway | The value travels by |
| --- | --- | --- |
| **A** | Decision | A named actor changes a named decision. **Most often a frontier AI company**: what to deploy, what to gate a deployment on, which evals to run, what goes into a safety framework or system card, which mitigations ship. Also covers regulators and standards bodies, and funders deciding where to allocate. |
| **B** | Research redirection | Changing what other safety researchers work on or believe. Validating or falsifying a threat model, ruling out an approach, or producing a tool, benchmark or dataset others build on. |
| **C** | Prerequisite | Building a method that some future intervention needs but that is not yet possible. |
| **D** | Field epistemics | Shifting consensus or norms. |
| **E** | Talent allocation | Moving **people** toward a specific problem. Money is excluded: a funder deciding where to allocate is pathway A. |

Notes on use:

- Funding is deliberately **not** its own pathway, and E is people only. A funder deciding where to allocate is a decision maker making a decision, so it belongs in A. Keeping money in both places would double-count it.
  
- Pathway E is the easiest to claim and the hardest to falsify. "This will attract talent to AI safety" is nearly always empty. "This will move people toward _this specific neglected sub-area_" is a real claim. The rubric below is what enforces the difference.
  
## Part 2: `impact_pathway` (new criterion)
> **How close is the declared change to actually happening?**

| Score | Label | Description |
| --- | --- | --- |
| **1** | No pathway | No pathway or endpoint declared. Value stated only as "advances understanding" or "informs the community". |
| **2** | Generic endpoint | Pathway declared, but the endpoint dissolves into a category rather than a change. Real examples from `data/ideas/`: _"helps future evaluators know what to look for"_, _"would improve the credibility of safety comparisons"_, _"this database would be a public good"_, _"strengthens the case for standardised metrics"_. Plausible-sounding, but no party is named and nothing they do would differ. |
| **3** | Blocked | Endpoint is specific, but making it happen needs something nobody currently has: a new mandate, industry-wide coordination, a change in how frontier models are trained, or funding no one has committed. |
| **4** | Within reach | Endpoint is specific and within reach of the named party, but still costs them real effort or a shift in priorities. |
| **5** | Ready to adopt | Endpoint is specific **and** either (i) cheap for the named party to adopt, slotting into what they already do with resources they already control, **or** (ii) a larger ask matched by a named party who has both the authority and the incentive to make it happen. |

**Worked contrast.** "Use this linear probe to flag harmful outputs" scores 5 by route (i): it slots into an existing eval pipeline. "Train models a completely different way", with no mechanism named, scores 3. The same retraining proposal scores 5 by route (ii) if it names a regulator or standards body that could actually require it.

**A real level 5 already in the corpus.** One idea in `data/ideas/` grounds itself on the fact that _"OpenAI explicitly reports StrongREJECT scores in system cards for GPT-4o, o1, and GPT-4.5, using a '_[_goodness@0.1_](mailto:goodness@0.1)_' metric"_. That is route (i) done properly: a named frontier company, an artifact they already publish, and a number they already report. Improving that metric changes something they are demonstrably already doing. Compare it to the level 2 examples above, which come from the same corpus.

**Why level 5 has two routes.** A single cheap-is-better ladder would systematically downrank ambitious foundational work, which fights `counterfactual_value`, whose own level 5 is _"a foundational or long-horizon problem frontier labs have little incentive to attack now"_. Route (ii) stops the two criteria pulling against each other on exactly the ideas the project cares most about, while still failing a chain that terminates in "someone should do something hard".

**What is deliberately absent.** Nothing here rewards pre-existing demand. An earlier draft required evidence that a decision was live, such as a published open problem or an RFP. That was cut because genuinely neglected directions have no RFP by definition, so the requirement would have anti-correlated with the counterfactual value the project prioritises.
## Part 3: `theory_of_impact` (reworded)
> **If the named party acts on this, does catastrophic risk go down?**

| Score | Label | Description |
| --- | --- | --- |
| **1** | Not catastrophic | No catastrophic scenario named. The harm is ordinary and recoverable. |
| **2** | Generic label | Catastrophic scenario named only as a label ("existential risk", "loss of control") with no mechanism. |
| **3** | Partial | Specific mechanism named, such as deceptive alignment surviving training or undetected sabotage in an agent pipeline, but the action addresses it only partially or indirectly. |
| **4** | Direct | Specific mechanism named, and the action directly reduces that mechanism's contribution. |
| **5** | Necessary step | As 4, and the mechanism is a step the catastrophic pathway _requires_, so constraining it constrains the whole pathway rather than one contributing factor among several. |

Magnitude is folded into levels 4 and 5 rather than being a separate number.

**Whether the risk is widely recognised is irrelevant here.** A mechanism nobody has studied can score 5 if the necessity argument holds. Level 5 asks the researcher to show that the mechanism is load-bearing _in the causal story_, which is an argument that can be made about a risk the field has not yet looked at. The previous wording required established safety agendas to have already agreed the pathway was critical, which penalised exactly the neglected risks this project exists to surface.

**Recursive requirement.** For pathways B, C, D and E, the chain must bottom out. If the value runs through other research, that downstream research needs its own named endpoint rather than deferring indefinitely. An idea that cannot say where the deferral ends caps at 3. This is Aird's condition on groundwork research and Apollo's "must bottom out" point, applied at the risk link rather than the pathway link.

* * *
## What changes in the repo
**Must**

- Add `impact_pathway` to `config/criteria.yaml` with the rubric above.
  
- Reword the `theory_of_impact` rubric in `config/criteria.yaml`.
  
- Add a declared `pathway` field to the proposal schema, alongside the existing `theory_of_impact_chain`.
  

**Should**

- Update the scoring prompts in `.claude/commands/score-ideas.md` and `.claude/commands/refine-ideas.md` to carry both rubrics.
  

**Could**

- Wire `~/.claude/skills/red-team-impact/SKILL.md` in as a top-N reranker, mirroring the existing `/novelty-rerank` pattern.
  

**Won't**

- No rescoring of the 717 existing ideas. They keep their current `theory_of_impact` values as legacy.
  
- No dissemination criterion. Not relevant to an idea generation pipeline.
  
- No construct validity criterion. Only applies to measurement projects.
  
- No per-link probability estimates.
  

**Weights.** Proposed 0.75 each, so the two together total 1.5 and nothing else in `criteria.yaml` is silently reweighted. Raise both if theory of impact should count for more than it does today.
## Open items
1. **A resource is still missing.** A page on theory of impact was mentioned but the link has not come through yet. The rubrics may need revision once it is read.
  
2. **Validation before code.** Score the ideas in the shared Google Doc under both the old and new rubrics and compare distributions. If the new rubric still puts most ideas at 4-5, tighten it before touching `criteria.yaml`.
