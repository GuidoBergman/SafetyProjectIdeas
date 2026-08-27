# Grill an Idea

Interview the coordinator relentlessly about one research idea until every section of the idea format holds up, then write it.

You drive. Ask **one question at a time** and wait, because batching is bewildering. Give your **recommended answer** with every question, plus the ranked alternatives and why you ranked them that way. When a question can be answered by reading the idea or searching the literature, go find out instead of asking.

The coordinator can say **menu** at any point to reach the escapes. Otherwise you keep pushing.

## Setup

Read [`docs/idea-format.md`](../../docs/idea-format.md) for the sections, word budgets and gates. Read [`writing-guidelines.md`](../../writing-guidelines.md) for prose rules. Then load config:

```bash
uv run python -m saim.config.cli show-scoring
uv run python -m saim.config.cli show
uv run python -m saim.config.cli show-participant
```

## Step 1: Intake

Ask for the idea: an existing `idea_id` to load from `data/ideas/`, or a description.

For an existing idea, set its status to **Evaluating** in `data/output/idea_tracker.md` and present it in reading order (title, TL;DR, then the visible sections, then the collapsed layer) before touching anything.

For a new idea, mint the ID with `uv run python -m saim.ids` and set `run_id` to `"unknown"`. Never write an ID by hand.

Then classify the starting state, which decides where the walk begins:

- **Vague**, such as "why does debate sometimes work and sometimes not". Run Step 2 first.
- **Partial or full.** Skip to Step 3. A fully written proposal still gets the whole walk, because having a section is not the same as the section being right.

## Step 2: Shape it (vague ideas only)

Turn the input into something the walk can operate on. Settle three things, one question at a time: the **failure this targets** (a specific mechanism, not a category), a **falsifiable claim** the project could confirm or refute, and the **pathway** (A-E) with the party that would act on the result.

Stop when a one-sentence research question exists that names a mechanism and could come out false.

## Step 3: The walk

Walk the sections in dependency order, not file order. TL;DR comes last because it summarises everything above it:

Research Question, pathway, Why This Matters, named party, Who This Is For, Approach, Experiments, Day-1 Check, Risks, Scope and Deliverables, Prerequisites, Open Questions, TL;DR, then the collapsed layer.

For each section, four moves in order:

1. **Answerable from the idea?** Fill it in, then go to move 4.
2. **Answerable from the literature?** Agree the plan before dispatching (see Research dispatch), then dispatch and fill it in.
3. **Otherwise ask.** One question, your recommended answer, the ranked alternatives, the reasoning.
4. **Critique it.** Check the section's gate in `docs/idea-format.md` and score it against its rubric from `show-scoring`. Produce one concrete proposed improvement, or state plainly that it is at the rubric ceiling. A section that fails its gate is not done.

Keep the working state in the conversation. Write nothing until Step 5.

## Step 4: Red team

Separate from Step 3 and not guided by the sections. Read the whole idea as an adversary.

**Classify every claim** in the idea as **established**, **assumed** or **ambiguous**. Established means a cited source or a measured number backs it. Then attack everything in the other two buckets, asking of each: what could we be wrong about here, and what happens to the project if we are?

Do your own full pass first, then spawn subagents with different lenses and merge the findings without attribution, per [`~/.claude/rules/red-team.md`](file:///home/guido/.claude/rules/red-team.md).

Every finding lands somewhere in the idea:

- An assumed claim that could kill the project becomes a **Risk**, which forces it to name a detecting experiment and a response.
- One that cannot be resolved becomes an **Open Question**.
- An ambiguity becomes the next question you ask the coordinator.

For the theory of impact specifically, dispatch `/red-team-impact` rather than repeating its chain analysis here.

The pass is done when every claim carries a bucket and every assumed or ambiguous one has a home.

## Step 5: Write

Write `data/ideas/<idea_id>.md` in the format from `docs/idea-format.md`, then set the tracker status to **Added and needs manual review**. It becomes **Added** only when the coordinator confirms they have read it.

**Novelty gate.** If `novelty_method` is `novelty_estimated`, null or missing, the idea has estimated novelty only, which is unreliable. Say so, run `.claude/commands/novelty-check.md` in full, update `novelty_method` to the method actually used, and only then write.

Report the files you changed.

## Research dispatch

Agree the plan with the coordinator before any search runs: the queries, the sources, and specifically which claims you will try to refute. Ask what is missing, such as a key paper or a competing method, and fold in what they add. `/research-topic` negotiates its own dimensions at its Step 2; `/novelty-check` does not, so supply the plan yourself.

| Need | Dispatch |
| --- | --- |
| Is this already done, and what is the contrast with the closest prior work | `.claude/commands/novelty-check.md`, steps N1-N5 and C1-C3 |
| Deep read of one topic across several papers | `/research-topic` |
| Broad scan of a subfield | `/research-landscape` |
| Attack the theory of impact | `/red-team-impact` |

Write the prior-work contrast into the idea as a direct statement: X did Y, this differs by Z. Do not trust stored novelty fields, since earlier pipeline phases get them wrong.

Assess source credibility before building on a source, per the rules in `CLAUDE.md`.

## Menu

On "menu", offer: run a novelty check, research a topic, scan the landscape, red team the impact, generate alternative framings, checkpoint now (write the current state to `data/ideas/` early), mark not promising, remove, done. Then return to the walk.

**Not promising** sets the tracker status to `Not promising` and changes nothing else. **Remove** sets it to `Removed`, adds `eliminated: true` and `elimination_reason` to the frontmatter, and leaves pipeline history intact.
