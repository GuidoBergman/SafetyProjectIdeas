export const meta = {
  name: 'saim-score-stage1',
  description: 'SAIM scoring Stage 1: quick relevance filter, one agent per batch (40 batches)',
  phases: [ { title: 'QuickFilter' } ],
}
const RUN_DIR = 'data/runs/2026-06-15T19-24-29'
const N_BATCHES = 40
const THRESHOLD = 2.0

const RUBRIC = `Quick Filter Rubric (1-5), threshold ${THRESHOLD}:
[1] Off-topic: Not related to AI Safety in any meaningful way, or addresses a completely different domain.
[2] Tangential: Touches on AI or safety peripherally but lacks a direct connection to an AI Safety problem (e.g., general ML performance improvement with no safety framing).
[3] Relevant: Clearly addresses an AI Safety topic but scope may be too broad/vague, or the link to a safety outcome needs refinement.
[4] Well-targeted: Directly addresses a recognized AI Safety problem with a reasonably scoped approach; safety relevance immediate.
[5] Precisely scoped: Targets a specific, well-defined AI Safety problem with a clear focused approach; safety relevance obvious.`

const CONF = `Confidence (0.0-1.0): 0-0.2 essentially a guess; 0.2-0.4 weak/indirect; 0.4-0.6 some relevant evidence, gaps remain; 0.6-0.8 strong directly-relevant evidence; 0.8-1.0 thorough converging evidence.`

function prompt(n) {
  const b = String(n).padStart(3,'0')
  const batchPath = `${RUN_DIR}/filter_score/batches/stage1/batch_${b}.json`
  const resultPath = `${RUN_DIR}/filter_score/results/stage1/batch_${b}_results.json`
  return [
    `You are a quick relevance filter for AI Safety research ideas. Score each idea 1-5 against the rubric by matching it to the best-fitting level — not gut feeling.`,
    ``, RUBRIC, ``, CONF,
    ``,
    `Step 1 — read your batch (run via Bash from repo root /home/guido/Desktop/saim):`,
    `  uv run python -m saim.pipeline.filter_score read-batch ${batchPath}`,
    ``,
    `Step 2 — for EVERY idea (do not skip any) build a JSON array; each element:`,
    `{"idea_id":"<id>","title":"<title>","run_id":"<run_id>","quick_score":<1-5>,"quick_reasoning":"<1 sentence matching rubric level>","quick_confidence":<0.0-1.0>,"eliminated":<true if quick_score < ${THRESHOLD} else false>,"elimination_reason":<null or "Stage 1: quick relevance score [X] below threshold ${THRESHOLD}">}`,
    ``,
    `Step 3 — write results (pass the JSON array as a single-quoted arg):`,
    `  uv run python -m saim.pipeline.filter_score write-batch-results ${resultPath} '<json_array>'`,
    `If the array is large, write it to a temp file and pass its contents; ensure valid JSON. Return ONLY the integer count of ideas scored.`,
  ].join('\n')
}

log(`Stage 1: launching ${N_BATCHES} quick-filter agents`)
const idxs = Array.from({length: N_BATCHES}, (_, i) => i + 1)
const res = await parallel(idxs.map(n => () =>
  agent(prompt(n), { label: `s1_batch_${String(n).padStart(3,'0')}`, phase: 'QuickFilter', agentType: 'general-purpose' })
    .then(r => ({ n, ret: r }))
))
const ok = res.filter(Boolean)
log(`Stage 1 agents returned: ${ok.length}/${N_BATCHES}`)
return { returned: ok.length, total: N_BATCHES }
