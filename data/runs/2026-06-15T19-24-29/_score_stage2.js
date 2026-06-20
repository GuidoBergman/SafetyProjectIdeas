export const meta = {
  name: 'saim-score-stage2',
  description: 'SAIM scoring Stage 2: full per-criterion scoring + estimated novelty, one agent per batch (80 batches)',
  phases: [ { title: 'FullScore' } ],
}
const RUN_DIR = 'data/runs/2026-06-15T19-24-29'
const N_BATCHES = 80
const MIN_SCORE = 2.0

const CRITERIA = `Score each idea 1-5 against EACH criterion below by matching to the best-fitting rubric level (not gut feeling). Active weights in parentheses.

[theory_of_impact] (weight 3.0) — clear, specific theory of how it reduces catastrophic risks from advanced AI.
 1 No impact chain. 2 Vague impact (broad labels, no specific catastrophic scenario). 3 Plausible chain but a gap/skipped step. 4 Strong chain: every link explicit & defensible, concrete catastrophic scenario. 5 Compelling: strong chain targeting a pathway recognized as critical by major safety orgs, intermediate deliverables independently valuable.

[accessible_complexity] (weight 3.5) — complexity appropriate for the team (CS students, first AI-safety project, basic Python/ML, single consumer GPU, 30h).
 1 Expert-only. 2 Advanced (strong research background needed). 3 Intermediate (solid ML fundamentals). 4 Guided (clear inherited methodology; novice + mentor can execute). 5 Accessible (standard tools + public datasets; motivated beginner makes progress).

[narrow_scope] (weight 5.0) — self-contained first deliverable valuable on its own, clear methodology + success criteria.
 1 Open-ended program, no first deliverable. 2 No clear first milestone. 3 Deliverable requires sustained multi-workstream effort. 4 Focused first deliverable, few dependencies. 5 Tightly scoped single experiment with well-defined success criteria.

[counterfactual_value] (weight 3.0) — does doing this OUTSIDE a major lab add value? (USER PRIORITY — weigh carefully.)
 1 Lab territory (labs already on it / needs internal weights/infra/data / strong lab incentive). 2 Mostly lab-suited. 3 Mixed; some externally-doable slice. 4 Independent-friendly: little lab coverage, weak lab incentive, public models/data, generalizes without internal access. 5 Neglected long-horizon 'gold': foundational/long-horizon (>1yr) problem labs have little incentive to attack now, needs no internal access, benefits from independent/external work (auditing, replication, third-party scrutiny), e.g. fuzzy-reward evals, model organisms, safer-sandbox infra.

[low_compute] (weight 0.0) — still score it: 1 infeasible/large training; 3 single mid GPU days; 5 CPU/free-tier/analytical. (Weight is 0 so it does not affect the weighted score, but record it.)`

const NOVELTY = `Estimated novelty (NO web search — use your own knowledge only; this cheap estimate is overwritten later by the novelty-rerank workflow on top ideas):
 already_solved=1 (confident existing published work fully addresses it); largely_addressed=2; partially_addressed=3 (work exists but this angle may be open — DEFAULT when unsure); mostly_novel=4 (no direct published work known); novel=5 (no published work on this question/approach known). Keep confidence modest.`

function prompt(n) {
  const b = String(n).padStart(3,'0')
  const batchPath = `${RUN_DIR}/filter_score/batches/stage2/batch_${b}.json`
  const resultPath = `${RUN_DIR}/filter_score/results/stage2/batch_${b}_results.json`
  return [
    `You are scoring AI Safety research ideas against multiple criteria. Run all Bash from repo root /home/guido/Desktop/saim.`,
    ``, CRITERIA, ``, NOVELTY,
    ``,
    `Weighted score = sum(score*weight) / sum(weight) over the NON-novelty criteria only. Active weights: theory_of_impact=3.0, accessible_complexity=3.5, narrow_scope=5.0, counterfactual_value=3.0, low_compute=0.0. (low_compute contributes 0 to numerator and 0 to denominator since weight 0.) Stage-2 cutoff: weighted_score < ${MIN_SCORE} => eliminated.`,
    ``,
    `Step 1 — read your batch:`,
    `  uv run python -m saim.pipeline.filter_score read-batch ${batchPath}`,
    ``,
    `Step 2 — for EVERY idea (do not skip) build a JSON array; each element exactly:`,
    `{"idea_id":"<id>","title":"<title>","run_id":"<run_id>","original_idea":<full idea object from batch>,`,
    ` "scores":{`,
    `   "theory_of_impact":{"score":<1-5>,"reasoning":"<1-3 sentences ref rubric level>","confidence":<0-1>},`,
    `   "accessible_complexity":{"score":<1-5>,"reasoning":"...","confidence":<0-1>},`,
    `   "narrow_scope":{"score":<1-5>,"reasoning":"...","confidence":<0-1>},`,
    `   "counterfactual_value":{"score":<1-5>,"reasoning":"...","confidence":<0-1>},`,
    `   "low_compute":{"score":<1-5>,"reasoning":"...","confidence":<0-1>},`,
    `   "novelty":{"score":<1-5 estimated>,"reasoning":"<1 sentence estimate, no search>","confidence":<0-1>}},`,
    ` "novelty_assessment":{"classification":"<one of already_solved|largely_addressed|partially_addressed|mostly_novel|novel>","evidence":[],"confidence":<0-1>,"derived_score":<1-5 matching classification>,"reasoning":"<1 sentence estimate>"},`,
    ` "novelty_method":"novelty_estimated",`,
    ` "weighted_score":<weighted avg EXCLUDING novelty>,`,
    ` "confidence":<average of per-criterion confidences>,`,
    ` "eliminated":<true if weighted_score < ${MIN_SCORE} else false>,`,
    ` "elimination_reason":<null or "Stage 2: weighted score [X] below threshold ${MIN_SCORE}">}`,
    ``,
    `Step 3 — write results (write the JSON array to a temp file then pass its contents, or pass directly if small; must be valid JSON):`,
    `  uv run python -m saim.pipeline.filter_score write-batch-results ${resultPath} '<json_array>'`,
    `Return ONLY the integer count of ideas scored.`,
  ].join('\n')
}

log(`Stage 2: launching ${N_BATCHES} full-scoring agents`)
const idxs = Array.from({length: N_BATCHES}, (_, i) => i + 1)
const res = await parallel(idxs.map(n => () =>
  agent(prompt(n), { label: `s2_batch_${String(n).padStart(3,'0')}`, phase: 'FullScore', agentType: 'general-purpose' })
    .then(r => ({ n, ret: r }))
))
const ok = res.filter(Boolean)
log(`Stage 2 agents returned: ${ok.length}/${N_BATCHES}`)
return { returned: ok.length, total: N_BATCHES }
