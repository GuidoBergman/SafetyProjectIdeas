# Idea format

The schema for `data/ideas/<idea_id>.md`. Rendered by `render_proposal_body` in `src/saim/pipeline/refine.py`; section keys and headings live there and are the source of truth for names.

## Layers

The **visible layer** runs from the TL;DR to Open Questions. Scores, alternative framings and cited sources render inside `<details>` below it, so a reader triaging a ranked list decides from the sections above them.

## Frontmatter

`idea_id`, `title`, `research_field` (list), `pathway` (exactly one of A-E), `named_party`, `scores` (theory_of_impact, impact_pathway, low_compute, accessible_complexity, narrow_scope, counterfactual_value, novelty).

## Sections and word budgets

| Section | Key | Words |
| --- | --- | --- |
| TL;DR | `tldr` | 25-45 |
| Research Question | `research_question` | 50-90 |
| Why This Matters | `why_this_matters` | 110-170 |
| Day-1 Check | `day1_check` | 60-110 |
| Approach | `approach_outline` | 220-350 |
| Scope and Deliverables | `scope_and_deliverables` | 90-150 |
| Experiments | `proposed_first_experiments` | 50-200 |
| Risks | `risks` | 180-280 |
| Prerequisites | `prerequisites` | 40-80 |
| Who This Is For | `who_this_is_for` | 40-90 |
| Open Questions | `open_questions` | 60-110 |
| Visible total | | 1000-1400 |
| Collapsed layer | `scores_rationale`, `alternative_framings`, `cited_sources` | no cap |

## Gates

A section that fails its gate is not usable. These are checkable, so treat them as pass/fail rather than judgement calls.

1. **TL;DR** is capped at 45 words and is the line that represents this idea in a ranked list of hundreds.
2. **Day-1 Check** names an artifact to obtain and a number to measure, doable in under four hours with no training. "Read the literature" fails. Empty is allowed when no such check exists.
3. **Why This Matters** names a mechanism, not a category, in three labelled parts: the failure this targets, why the work reduces it, where the chain ends. For pathways B, C, D and E the last part names the concrete decision the chain terminates in. An idea that cannot say where the deferral ends caps `impact_pathway` at 3.
4. **Risks** are structured as name, consequence, detected by, response. Every risk names the experiment that detects it, and its response is stop, retry with a named change, or mitigate with a named change. A risk you cannot detect or respond to is a worry, so leave it out. A result that falsifies the hypothesis is a finding, not a risk, and belongs in the closing "Not a risk" note.
5. **Scope and Deliverables** gives hours and weeks across two or three stages, each able to stop the next, then the concrete artifact.
6. **Who This Is For** names an org or team, what they do today, and what they would do differently. "Researchers" and "the community" fail.
7. **No score numbers or criterion names** appear outside `scores_rationale`.

## Pathways

Declared, unscored. Definitions and the `impact_pathway` rubric live in [`theory-of-impact-rubrics.md`](theory-of-impact-rubrics.md).

## Prose rules

[`writing-guidelines.md`](../writing-guidelines.md) governs how every section is written.

## Worked example

[`idea-format-proposal.md`](idea-format-proposal.md) Part 1 is the format shown as a real idea file.
