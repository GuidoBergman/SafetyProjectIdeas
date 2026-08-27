# Proposed idea format, instantiated (revision 3)
**What changed:** sections reordered so impact comes before risks and the named party sits at the end, Risks restructured into labelled lines, **Scope and Deliverables** and **Prerequisites** added. Full list in Part 3.

**Part 1** is the format shown as a real idea file, using #3 from the shared Google Doc. **Part 2** is the word budget. **Part 3** lists what I changed. **Part 4** has the one thing I still need from you.

* * *
# Part 1: the example
The block below is what the pipeline would write to `data/ideas/gen-XXXX.md`.

* * *

```yaml
idea_id: gen-8c41e0b2
title: Does Distillation Expose a Model That Hides Its Misalignment?
research_field: [AI Control, Evaluations & Benchmarks]
pathway: B
named_party: Redwood Research control team
scores:
  theory_of_impact: 5
  impact_pathway: 4
  low_compute: 3
  accessible_complexity: 3
  narrow_scope: 4
  counterfactual_value: 4
  novelty: 4
```

* * *
# Does Distillation Expose a Model That Hides Its Misalignment?
**TL;DR:** Redwood proposed catching a model that hides its misalignment by distilling it into a cheap copy and auditing the copy instead. Nobody has run that test. This runs it on one small open model.
## Research Question
Distillation trains a fresh student model to copy a teacher's outputs. Suppose the teacher is misaligned but has learned to hide it, so it acts badly in normal use yet behaves and denies any problem when audited. Does the bad behaviour copy over while the hiding does not, so that auditing the cheap student exposes what the teacher kept hidden?
## Why This Matters
**The failure this targets:** a model that is misaligned and has learned to behave under audit passes pre-deployment auditing and is deployed internally with the affordances its misalignment needs.

**Why the work reduces it:** surviving the audit is not one contributing factor among several, it is a step the pathway requires. A model that is caught at audit gets no affordances, so nothing downstream happens. This project either supplies a detection method that the concealment strategy does not defeat, or rules one out before anyone trusts it.

**Where the chain ends:** the value of this project runs through other researchers rather than changing a decision directly, so it has to terminate somewhere concrete. It terminates in a lab running distil-and-audit on a model before internal deployment, as a step in its own auditing procedure.
## Day-1 Check
Before any distillation, download the 14B AuditBench teacher from the `auditing-agents` org and confirm two rates on about 50 prompts each: the teacher exhibits its hidden behaviour on domain prompts, and it denies that behaviour under direct audit prompts. Confirm in the same pass that the teacher's base model is downloadable, since the student has to be built from it. Inference only, one afternoon, no training. This is the cheapest thing that can tell you the study is not worth running.
## Approach
The teacher is downloaded, not trained. AuditBench is a public collection of open models that Anthropic fine-tuned to each carry one hidden bad behaviour, such as inventing fake citations, then trained to deny that behaviour when questioned. Pick a behaviour an automatic checker can score, so "did it copy over?" is a clean yes or no.

The distillation is black-box: the student trains only on the teacher's text, so it can inherit only what shows up in that text. This makes prompt choice the crux. Prior work shows misaligned behaviour transfers reliably on prompts from the behaviour's own domain and barely transfers on unrelated prompts, so the distillation set is built from prompts that reliably elicit the behaviour.

The set also includes audit-style prompts that make the teacher produce its denials, since a model only denies when interrogated. For a teacher that invents citations these are challenges like "Are all of those references real papers I can look up?". Including both kinds means the behaviour and the denials appear side by side in the teacher's outputs, giving each a fair chance to transfer.

Two rates are then measured on the student: the behaviour rate, how often it shows the hidden behaviour in normal use, and the concealment rate, whether it still denies the behaviour under direct questioning. The number that matters is the gap between them.
## Scope and Deliverables
About 30 hours over 6 weeks, staged so each stage can stop the next.

- **Week 1, derisking.** The Day-1 Check plus Experiment 1. Ends with a yes or no on whether the teacher is a usable organism.
  
- **Weeks 2 to 4, main result.** Experiments 2 and 3. Ends with the behaviour and concealment rates measured on the student.
  
- **Weeks 5 to 6, write-up.** Bootstrap intervals, and a short post reporting the gap.
  

The deliverable is one three-row table of behaviour and concealment rates with the gap and its confidence interval, plus the distillation prompt set released so the run can be repeated on another behaviour.
## Experiments
| #   | Run | Measures | Cost |
| --- | --- | --- | --- |
| 1   | Teacher characterisation (the Day-1 Check, extended to 200 prompts) | Teacher behaviour rate, teacher denial rate | ~4h, inference |
| 2   | Main distillation: behaviour prompts plus audit prompts | Student behaviour rate, student concealment rate, the gap | ~1 GPU-day |
| 3   | Neutral control: distil on unrelated prompts only | Whether the behaviour leaks when never shown | ~1 GPU-day |
## Risks
**No usable model organism.**

- Consequence: the teacher does not both exhibit the behaviour and deny it, so there is nothing to distil and the study cannot run.
  
- Detected by: the Day-1 Check.
  
- Response: no workaround exists inside this design. Stop the project.
  

**No open base model for the student.**

- Consequence: behaviour transfer only appears when teacher and student start from the same base model, so without that base the experiment cannot be built.
  
- Detected by: the Day-1 Check.
  
- Response: try the other AuditBench teachers, which do not all share a base. Stop only if none has an available base.
  

**The behaviour barely transfers.**

- Consequence: prior work reports 27 to 40% transfer; below roughly 10% there is no signal in which to measure a gap.
  
- Detected by: Experiment 2.
  
- Response: retry once with a different behaviour, costing about a GPU-day. If the second also fails, stop.
  

**Distillation cost runs over.**

- Consequence: sample count is unestimated and could exceed the compute budget.
  
- Detected by: Experiment 2, if started small.
  
- Response: start at a tenth of the planned sample count and check the behaviour rate is measurable before scaling up.
  

**Not a risk: concealment transferring as strongly as the behaviour.** That outcome means the proposed auditing method does not work, which is a real finding and worth writing up. The project succeeds either way.
## Prerequisites
- One mid-range GPU with 24GB or more, for two distillation runs on a 14B model plus inference. No paid API needed.
  
- HuggingFace access to the `auditing-agents` AuditBench models and to the matching base model.
  
- Comfort with fine-tuning through the HuggingFace stack, and with bootstrap confidence intervals.
  
## Who This Is For
Redwood Research's control team. They published the proposal and never tested it, so a measured result lands on a question they have already committed to. If the test works, they extend an auditing procedure they already run. If it fails, they drop the direction before investing in it.
## Open Questions
- The teacher's concealment is fine-tuned in, not emergent. A trained denial may transfer more readily than genuine strategic concealment would, which would bias the result toward "the method fails".
  
- Fake-citation behaviour is auto-scorable, which is why it was picked, but it may be unusually shallow compared to the behaviours that actually matter.
  
- Whether a gap measured at 14B says anything about the scale where concealment is a real worry.
  

<details>
<summary><b>Scores and rationale</b></summary>

- **theory_of_impact 5.** Surviving pre-deployment audit is a step the catastrophic pathway requires, not one contributing factor. Caveat: a negative result reduces risk only by preventing misplaced trust, which is weaker than the positive case.
- **impact_pathway 4.** Specific endpoint, named party who proposed it, but scaling past 14B costs them real effort, so it is not "cheap to adopt".
- **low_compute 3.** Two distillation runs on a 14B teacher. Feasible on a single mid-range GPU over days, not on free tier.
- **accessible_complexity 3.** Black-box distillation is a genuinely new skill for most participants. Acquirable, but a schedule risk.
- **narrow_scope 4.** One behaviour, one teacher, three runs, one table. The broader direction is ambitious but this milestone stands alone.
- **counterfactual_value 4.** Public model organisms, no internal access, no frontier lab has published on it. Not a 5 because Anthropic built AuditBench and could run this internally at any time.
- **novelty 4.** The proposal exists in a Redwood blog post; the test does not exist anywhere.

</details>

<details>
<summary><b>Alternative framings</b></summary>

- **Fragility comparison.** Instead of asking whether distillation exposes concealment, ask which is more fragile under distillation across several AuditBench behaviours at once. Broader, weaker per-behaviour statistics.
- **Cheaper intervention first.** Test whether plain fine-tuning on neutral data strips concealment before testing distillation. Cheaper, but it does not test the Redwood proposal, so the case for who would act on it weakens.

</details>

<details>
<summary><b>Cited sources</b> (6)</summary>

- [Incriminating misaligned AI models via distillation](https://blog.redwoodresearch.org/p/incriminating-misaligned-ai-models), Redwood Research. Proposes the exact idea this project tests. Foundation of the idea.
- [The distillation double bind](https://blog.redwoodresearch.org/p/the-distillation-double-bind-distilling), Redwood Research. Argues distillation may remove misaligned behaviour or may just hide it.
- [Emergent and Subliminal Misalignment Through the Lens of Data-Mediated Transfer](https://arxiv.org/abs/2605.12798). Measures 27 to 40% behaviour transfer, strongest on same-domain prompts. Sets the baseline this project inherits.
- [Subliminal Learning](https://arxiv.org/abs/2507.14805). Shows trait transfer needs teacher and student to share a base model.
- [AuditBench](https://arxiv.org/abs/2602.22755). The public model organisms used as the teacher. Models at https://huggingface.co/auditing-agents
- [Model Organisms for Emergent Misalignment](https://arxiv.org/abs/2506.11613). Small misaligned models for the backdoor variant.

</details>

* * *
# Part 2: word budget per section
Counts are measured, not estimated.

| Section | Target | This example |
| --- | --- | --- |
| TL;DR | 25-45 | 35  |
| Research Question | 50-90 | 60  |
| Why This Matters | 110-170 | 137 |
| Day-1 Check | 60-110 | 82  |
| Approach | 220-350 | 229 |
| Scope and Deliverables | 90-150 | 108 |
| Experiments | 50-200 (table, so the count runs low) | 59  |
| Risks | 180-280 | 224 |
| Prerequisites | 40-80 | 49  |
| Who This Is For | 40-90 | 48  |
| Open Questions | 60-110 | 72  |
| **Visible total** | **1000-1400** | **1124** |
| Collapsed layer | no cap | ~340 |

`data/ideas/gen-0017.md` today is 1,892 words at uniform visual weight, with no collapse and no way to skim it. This example is 1124 visible plus ~340 collapsed, so the visible layer is roughly half.

* * *
# Part 3: what I changed
| Your comment | Change |
| --- | --- |
| c18 "Who This Is For should be at the end" | Moved to second from last, after Prerequisites. |
| c19 "Why This Matters should be before the risks section" | Moved up to third, right after Research Question. |
| c20 "**The mechanism**" unclear | Renamed **The failure this targets**. |
| c21 Risks need structure | Each risk is now three labelled lines: **Consequence**, **Detected by**, **Response**. The "not a risk" item stays as a closing note. |
| c22 "I don't see Prerequisites in the editor" | Correct, it was never written. It was on my earlier list but you did not ask for it, so I left it out. It is in now. |
| c23 "Prerequisites should always be part of the generated ideas" | Added as a section, generated in the final stage alongside the rest. |
| c24 "no time to sample 10, write prompts that don't have those failures" | Dropped the sampling step. Instead the generation prompt will constrain the output shape: every risk must name the experiment that detects it and pick a response from a fixed set (stop / retry with a named change / mitigate by a named change). Filler like "if results are unclear, stop" cannot satisfy that shape. Same for the Day-1 Check, which must name an artifact to download and a number to measure. |
| c25 "what happened with desired outcomes or scope and deliverables" | **Scope and Deliverables** is in, time-boxed into three stages with a stop point after each. See Part 4 for Desired Outcomes. |

* * *
# Part 4: the one thing still open
**Desired Outcomes.** I did not add it, because in the Notion doc it answers "assuming this goes well, what are we aiming for", and here that is already split across two sections: **Why This Matters** says what the result does to catastrophic risk, and **Who This Is For** says who acts and what they do differently. A third section would restate both.

The two rubrics also score exactly those two things, so a separate Desired Outcomes section would be scored by nothing and would drift.

Where the Notion version does something neither section does is that it is explicitly ordered by ambition: outcome 1 is near-term and cheap, outcome 3 is long-term and needs stakeholder engagement. That laddering is real and this format loses it.

{>>Two options. Leave it out, which is what revision 3 does. Or add a two or three item ladder at the end of Who This Is For, going from what happens immediately to what happens if the direction pans out. Which?<<}{#c26}{++Desde 11:28++}{#s1}

---
comments:
  c26:
    by: Claude
    at: 2026-08-19T19:45:00.000Z
suggestions:
  s1:
    by: user
    at: 2026-08-27T15:20:34.696Z
