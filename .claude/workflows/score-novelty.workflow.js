export const meta = {
  name: 'score-novelty',
  description: 'Deterministic score + novelty stages for a SAIM run (Option B): parallel quick-filter, full scoring, and per-idea novelty with adversarial verification',
  whenToUse: 'After /generate-ideas has produced data/runs/<ts>/generate/*.md. Replaces the fan-out parts of /score-ideas and adds the missing novelty stage. Output is consumed by /refine-ideas unchanged.',
  phases: [
    { title: 'Setup', detail: 'load config rubrics + create stage-1 batches' },
    { title: 'Stage1', detail: 'quick relevance filter, one agent per batch' },
    { title: 'Stage2', detail: 'full per-criterion scoring, one agent per batch' },
    { title: 'Novelty', detail: 'per-idea literature search + classification' },
    { title: 'Verify', detail: 'adversarial skeptics refute high-novelty claims' },
    { title: 'Finalize', detail: 'enrich records, apply hard gate, write stage-3 survivors' },
  ],
}

// ---------------------------------------------------------------------------
// SAIM "score + novelty" workflow — Option B.
//
// This Workflow owns the rule-bound, high-volume stages of the SAIM pipeline:
//   - Stage 1: quick relevance filter   (port of /score-ideas Wave 1)
//   - Stage 2: full per-criterion score (port of /score-ideas Wave 2)
//   - Stage 3: novelty assessment + adversarial verification  (NEW — the
//              /score-ideas skill never actually ran novelty)
//
// The creative stages (/generate-ideas, /refine-ideas) stay as skills.
//
// Every agent calls the SAME `saim.pipeline.*` / `saim.config.cli` CLIs the
// skills use, so the files written here are byte-compatible with what
// /refine-ideas expects. The Workflow's job is the *orchestration*:
// guaranteed one-agent-per-batch fan-out, automatic retries, schema-validated
// returns, and the adversarial novelty check expressed as real control flow.
//
// Run dir: args.runDir (a path like "data/runs/2026-04-07T15-12-49"), or the
// latest run under data/runs/ if omitted.
// args.noveltyLimit (optional number): only send the top-N stage-2 survivors
//   (by weighted_score) through the expensive novelty stage. Safety valve for
//   large runs. Default: unlimited.
// ---------------------------------------------------------------------------

// `args` may arrive as a parsed object OR as a JSON string depending on how the
// caller passed it — normalize both so the cap/runDir are never silently dropped.
let A = args
if (typeof A === 'string') { try { A = JSON.parse(A) } catch { A = {} } }
A = A || {}
const runDir = A.runDir || null
const noveltyLimit = A.noveltyLimit || null

// Novelty classifications ordered least → most novel (mirrors saim/pipeline/novelty.py).
const CLS_ORDER = ['already_solved', 'largely_addressed', 'partially_addressed', 'mostly_novel', 'novel']
const HIGH_NOVELTY = new Set(['mostly_novel', 'novel'])

// ---------------------------------------------------------------------------
// Schemas
// ---------------------------------------------------------------------------

const CONFIG_SCHEMA = {
  type: 'object',
  required: ['runDir', 'quickFilterRubric', 'quickFilterThreshold', 'confidenceRubric',
             'scoringRubrics', 'weightPairs', 'minScore', 'participantSummary',
             'citationRubric', 'stage2BatchSize', 'stage1BatchPaths'],
  properties: {
    runDir: { type: 'string', description: 'Resolved run directory path' },
    quickFilterRubric: { type: 'string', description: 'Verbatim text of all 5 quick-filter rubric levels' },
    quickFilterThreshold: { type: 'number' },
    confidenceRubric: { type: 'string', description: 'Verbatim confidence rubric text' },
    scoringRubrics: { type: 'string', description: 'Verbatim text of every scoring criterion EXCEPT novelty: name, weight, description, and all 5 rubric levels' },
    weightPairs: { type: 'string', description: 'criterion=weight list (excluding novelty) for the weighted-score formula' },
    minScore: { type: 'number', description: 'filter_score min_score threshold' },
    participantSummary: { type: 'string' },
    citationRubric: { type: 'string' },
    stage2BatchSize: { type: 'number' },
    stage1BatchPaths: { type: 'array', items: { type: 'string' } },
  },
  additionalProperties: true,
}

const BATCH_RESULT_SCHEMA = {
  type: 'object',
  required: ['resultPath', 'ideasProcessed', 'written'],
  properties: {
    resultPath: { type: 'string' },
    ideasProcessed: { type: 'number' },
    written: { type: 'boolean' },
  },
  additionalProperties: true,
}

const STAGE2_MERGE_SCHEMA = {
  type: 'object',
  required: ['survivors', 'eliminated', 'survivorIdeas'],
  properties: {
    survivors: { type: 'number' },
    eliminated: { type: 'number' },
    survivorIdeas: {
      type: 'array',
      description: 'One entry per stage-2 survivor, sorted by weighted_score desc',
      items: {
        type: 'object',
        required: ['idea_id', 'title', 'problem', 'direction', 'weighted_score'],
        properties: {
          idea_id: { type: 'string' },
          title: { type: 'string' },
          problem: { type: 'string' },
          direction: { type: 'string' },
          weighted_score: { type: 'number' },
        },
      },
    },
  },
  additionalProperties: true,
}

const NOVELTY_SCHEMA = {
  type: 'object',
  required: ['idea_id', 'classification', 'confidence', 'reasoning', 'evidence'],
  properties: {
    idea_id: { type: 'string' },
    classification: { type: 'string', enum: CLS_ORDER },
    confidence: { type: 'number' },
    reasoning: { type: 'string' },
    evidence: {
      type: 'array',
      items: {
        type: 'object',
        required: ['source', 'title', 'url', 'summary'],
        properties: {
          source: { type: 'string' },
          title: { type: 'string' },
          url: { type: 'string' },
          summary: { type: 'string' },
        },
      },
    },
  },
  additionalProperties: true,
}

const SKEPTIC_SCHEMA = {
  type: 'object',
  required: ['refuted', 'suggestedClassification', 'foundWork'],
  properties: {
    refuted: { type: 'boolean', description: 'true if prior work was found that materially addresses the idea, contradicting a high-novelty claim' },
    suggestedClassification: { type: 'string', enum: CLS_ORDER },
    foundWork: {
      type: 'array',
      items: {
        type: 'object',
        required: ['source', 'title', 'url', 'summary'],
        properties: {
          source: { type: 'string' },
          title: { type: 'string' },
          url: { type: 'string' },
          summary: { type: 'string' },
        },
      },
    },
  },
  additionalProperties: true,
}

const WRITE_SCHEMA = {
  type: 'object',
  required: ['idea_id', 'written', 'eliminated', 'finalClassification'],
  properties: {
    idea_id: { type: 'string' },
    written: { type: 'boolean' },
    eliminated: { type: 'boolean' },
    finalClassification: { type: 'string', enum: CLS_ORDER },
  },
  additionalProperties: true,
}

const FINAL_SCHEMA = {
  type: 'object',
  required: ['survivors', 'eliminated'],
  properties: {
    survivors: { type: 'number' },
    eliminated: { type: 'number' },
  },
  additionalProperties: true,
}

// Derive the stage-N results path from a batch path:
//   .../filter_score/batches/stageN/batch_007.json
//   .../filter_score/results/stageN/batch_007_results.json
function resultPathFor(batchPath) {
  return batchPath.replace('/batches/', '/results/').replace('.json', '_results.json')
}

const pad3 = (n) => String(n).padStart(3, '0')

// ---------------------------------------------------------------------------
// Phase: Setup — load all config once, create stage-1 batches.
// ---------------------------------------------------------------------------
phase('Setup')

const cfg = await agent(
  `You are preparing a SAIM scoring run. Work from the repository root. All commands use \`uv run\`.

${runDir ? `The run directory is: ${runDir}` : 'Find the latest run directory with: ls -1t data/runs/ | head -1  → the run dir is data/runs/<that>'}

Do the following and return the results:

1. Resolve the run directory path (call it RUN_DIR). Verify generated ideas exist:
   uv run python -m saim.pipeline.generate list RUN_DIR
   If none exist, set stage1BatchPaths to [] and explain in your reasoning.

1b. Clear any stale score artifacts from a prior run so re-runs are idempotent (this does NOT touch generate/, refine/, or rank/):
   rm -rf RUN_DIR/filter_score/batches RUN_DIR/filter_score/results RUN_DIR/filter_score/survivors
   (Stale per-idea stage-3 result files from an earlier run would otherwise be picked up by the final merge and corrupt the survivor count.)

2. Load config (run each, capture the FULL verbatim text — these are embedded into worker prompts):
   uv run python -m saim.config.cli show-quick-filter      → quickFilterRubric (the 5 levels) + quickFilterThreshold (the "threshold:" number)
   uv run python -m saim.config.cli show-scoring           → scoringRubrics (every criterion EXCEPT novelty, with weight + description + all 5 rubric levels), weightPairs (a "name=weight, name=weight" list excluding novelty), minScore (the filter_score "min_score" under Thresholds), and confidenceRubric (the Confidence Rubric block)
   uv run python -m saim.config.cli show-batch-sizes       → stage2BatchSize (stage2_full_scoring value)
   uv run python -m saim.config.cli show-participant       → participantSummary (one short paragraph; if it prints NO_PARTICIPANT, use "none specified")
   uv run python -m saim.config.cli show-citation-relevance → citationRubric

3. Create stage-1 batches (use the stage1_quick_filter batch size from show-batch-sizes):
   uv run python -m saim.pipeline.filter_score create-batches RUN_DIR 1 <stage1_batch_size>
   This prints JSON with "batch_paths". Return that list as stage1BatchPaths.

Return all fields per the schema. Preserve rubric text exactly — do not summarize the rubric levels.`,
  { schema: CONFIG_SCHEMA, phase: 'Setup', label: 'setup:config+batches' }
)

const RUN_DIR = cfg.runDir
if (!cfg.stage1BatchPaths || cfg.stage1BatchPaths.length === 0) {
  log('No generated ideas found — nothing to score. Run /generate-ideas first.')
  return { error: 'no ideas in generate stage', runDir: RUN_DIR }
}
log(`Run dir: ${RUN_DIR} — ${cfg.stage1BatchPaths.length} stage-1 batch(es)`)

// ---------------------------------------------------------------------------
// Phase: Stage 1 — quick relevance filter. One agent per batch (guaranteed).
// ---------------------------------------------------------------------------
phase('Stage1')

await parallel(cfg.stage1BatchPaths.map((batchPath, i) => () =>
  agent(
    `You are a quick relevance filter for AI Safety research ideas. Work from the repo root.

Quick Filter Rubric (elimination threshold: ${cfg.quickFilterThreshold}):
${cfg.quickFilterRubric}

Confidence Rubric:
${cfg.confidenceRubric}

Step 1 — read your batch:
  uv run python -m saim.pipeline.filter_score read-batch ${batchPath}

Step 2 — for EACH idea, match it against the rubric LEVEL DESCRIPTIONS (not gut feeling) and pick the best-fitting level 1-5.

Step 3 — build a JSON array; one object per idea (do NOT skip any):
  {"idea_id": "<id>", "title": "<title>", "run_id": "<run_id>",
   "quick_score": <1-5>, "quick_reasoning": "<1 sentence citing the rubric level>",
   "quick_confidence": <0.0-1.0>,
   "eliminated": <true if quick_score < ${cfg.quickFilterThreshold} else false>,
   "elimination_reason": <null or "Stage 1: quick relevance score <X> below threshold ${cfg.quickFilterThreshold}">}

Step 4 — write results (pass the JSON array as a single-quoted arg):
  uv run python -m saim.pipeline.filter_score write-batch-results ${resultPathFor(batchPath)} '<json_array>'

Return resultPath="${resultPathFor(batchPath)}", ideasProcessed=<count>, written=true.`,
    { schema: BATCH_RESULT_SCHEMA, phase: 'Stage1', label: `stage1:batch_${pad3(i + 1)}` }
  )
))

// Glue: merge stage-1 results → survivors, then create stage-2 batches.
const s1 = await agent(
  `Work from the repo root. Run, in order, and report the printed counts:
  uv run python -m saim.pipeline.filter_score filter-survivors ${RUN_DIR} 1
  uv run python -m saim.pipeline.filter_score create-batches ${RUN_DIR} 2 ${cfg.stage2BatchSize}
The first prints {"survivors": N, "eliminated": M}. The second prints {"batch_paths": [...]}.
Return survivors, eliminated, and stage2BatchPaths (the batch_paths list).`,
  {
    schema: {
      type: 'object',
      required: ['survivors', 'eliminated', 'stage2BatchPaths'],
      properties: {
        survivors: { type: 'number' }, eliminated: { type: 'number' },
        stage2BatchPaths: { type: 'array', items: { type: 'string' } },
      },
      additionalProperties: true,
    },
    phase: 'Stage1', label: 'stage1:merge',
  }
)
log(`Stage 1: ${s1.survivors} survived, ${s1.eliminated} eliminated → ${s1.stage2BatchPaths.length} stage-2 batch(es)`)

if (s1.stage2BatchPaths.length === 0) {
  log('No ideas survived stage 1.')
  return { runDir: RUN_DIR, stage1: s1, note: 'no survivors after stage 1' }
}

// ---------------------------------------------------------------------------
// Phase: Stage 2 — full per-criterion scoring. One agent per batch.
// ---------------------------------------------------------------------------
phase('Stage2')

await parallel(s1.stage2BatchPaths.map((batchPath, i) => () =>
  agent(
    `You are scoring AI Safety research ideas against multiple criteria. Work from the repo root.

Scoring Criteria and Rubrics (score EACH of these; the novelty criterion is intentionally absent — it is handled in a later stage, do NOT invent a novelty score here):
${cfg.scoringRubrics}

Confidence Rubric:
${cfg.confidenceRubric}

Participant profile (calibrate "accessible/complexity"-type criteria to this team's level):
${cfg.participantSummary}

Weighted-score formula: for each criterion multiply score×weight, sum, divide by the sum of weights.
Active weights (novelty excluded): ${cfg.weightPairs}
Elimination threshold (min_score): ${cfg.minScore}

Step 1 — read your batch:
  uv run python -m saim.pipeline.filter_score read-batch ${batchPath}

Step 2 — for EACH idea, score every criterion by matching the rubric LEVEL DESCRIPTIONS (not gut feeling). Compute the weighted score and overall confidence (average of per-criterion confidences).

Step 3 — build a JSON array; one object per idea (do NOT skip any):
  {"idea_id": "<id>", "title": "<title>", "run_id": "<run_id>",
   "original_idea": <the full idea object from the batch, unchanged>,
   "scores": {"<criterion>": {"score": <1-5>, "reasoning": "<1-3 sentences citing the level>", "confidence": <0.0-1.0>}, ...},
   "weighted_score": <computed>, "confidence": <avg of per-criterion confidences>,
   "eliminated": <true if weighted_score < ${cfg.minScore} else false>,
   "elimination_reason": <null or "Stage 2: weighted score <X> below threshold ${cfg.minScore}">}

Step 4 — write results:
  uv run python -m saim.pipeline.filter_score write-batch-results ${resultPathFor(batchPath)} '<json_array>'

Return resultPath="${resultPathFor(batchPath)}", ideasProcessed=<count>, written=true.`,
    { schema: BATCH_RESULT_SCHEMA, phase: 'Stage2', label: `stage2:batch_${pad3(i + 1)}` }
  )
))

// Glue: merge stage-2 results → survivors, return survivor ideas for per-idea novelty.
const s2 = await agent(
  `Work from the repo root.
1. Run: uv run python -m saim.pipeline.filter_score filter-survivors ${RUN_DIR} 2
   It prints {"survivors": N, "eliminated": M} and writes ${RUN_DIR}/filter_score/survivors/stage2_survivors.json
2. Read that survivors JSON file. It is an array of scored idea objects, each with "idea_id", "title",
   "weighted_score", and "original_idea" (which has "problem" and "direction" fields, and a "body").
3. For each survivor return: idea_id, title, problem (from original_idea.problem; if absent, extract the
   "**Problem:**" line from original_idea.body), direction (from original_idea.direction or the
   "**Direction:**" line), and weighted_score.
Sort survivorIdeas by weighted_score descending. Return survivors, eliminated, survivorIdeas.`,
  { schema: STAGE2_MERGE_SCHEMA, phase: 'Stage2', label: 'stage2:merge' }
)
log(`Stage 2: ${s2.survivors} survived, ${s2.eliminated} eliminated`)

let toAssess = s2.survivorIdeas
if (noveltyLimit && toAssess.length > noveltyLimit) {
  log(`noveltyLimit=${noveltyLimit}: assessing top ${noveltyLimit} of ${toAssess.length} survivors by weighted_score; the rest are skipped (NOT written to stage-3 survivors).`)
  toAssess = toAssess.slice(0, noveltyLimit)
}
if (toAssess.length === 0) {
  log('No ideas survived stage 2.')
  return { runDir: RUN_DIR, stage1: s1, stage2: s2, note: 'no survivors after stage 2' }
}

// ---------------------------------------------------------------------------
// Phase: Novelty + Verify + Finalize — per idea, pipelined.
//   3a: literature search → initial classification
//   3b: if the idea claims high novelty, 3 skeptics try to refute it; ≥2
//       refutations downgrade the classification (deterministic, in JS)
//   3c: enrich the stage-2 record with the novelty assessment, apply the
//       already_solved hard gate, write the stage-3 batch result file
// ---------------------------------------------------------------------------
phase('Novelty')

const stage3 = await pipeline(
  toAssess,

  // --- 3a: novelty search + classification ---
  (idea) => agent(
    `You are assessing the NOVELTY of one AI Safety research idea via a literature search. Work from the repo root.

Idea title: ${idea.title}
Underlying problem (method-agnostic — what it tries to solve, stripped of the method): ${idea.problem}
Proposed direction/approach: ${idea.direction}

Source-reading policy: start with abstracts/summaries; read deeper sections only when they could change the classification. Never read full papers end-to-end.

Two-tier search (Tier 1 first and weighted more heavily):
- Tier 1 (problem-level): is the PROBLEM already solved by ANY method? Strip the proposed method from your queries. Run 2+ problem-level WebSearch queries with different phrasings, plus 1 "known approaches/survey" query.
- Tier 2 (method-level): has this SPECIFIC approach been tried? 1+ query.
Also search the AI-safety community: WebSearch with allowed_domains ["lesswrong.com","alignmentforum.org"], 2-3 problem-first queries.
Structured DB checks (problem terms first, then method terms):
  uv run python -m saim.verification.citation search-crossref '<terms>'
  uv run python -m saim.verification.citation search-s2 '<terms>'

Classify against this rubric (the key question is whether the PROBLEM is solved, not whether the METHOD is new):
  already_solved (1): existing published work FULLY addresses the idea — cite the specific paper(s).
  largely_addressed (2): multiple works cover most of it; gaps minor.
  partially_addressed (3): work exists but this specific angle/combination is unexplored.
  mostly_novel (4): no direct work on this proposal; related work in adjacent areas.
  novel (5): no published work found on this question or approach.

Match evidence to the level descriptions — not gut feeling. Assign confidence 0.0-1.0.
Record each relevant work as {"source","title","url","summary"}.
Return idea_id="${idea.idea_id}", classification, confidence, reasoning (2-4 sentences citing specific evidence), evidence[].`,
    { schema: NOVELTY_SCHEMA, phase: 'Novelty', label: `novelty:${idea.idea_id}` }
  ),

  // --- 3b adversarial verify (conditional) + 3c enrich & write ---
  async (assessment, idea, i) => {
    let finalClassification = assessment.classification
    let evidence = assessment.evidence || []

    // Only spend skeptics on ideas that CLAIM high novelty — that's where a
    // false "novel" is costly. Low-novelty classifications are already
    // conservative, so we accept them as-is.
    if (HIGH_NOVELTY.has(assessment.classification)) {
      const skeptics = (await parallel([0, 1, 2].map((k) => () =>
        agent(
          `You are skeptic #${k + 1} of 3. An automated assessment classified the AI Safety idea below as "${assessment.classification}" (highly novel). Your job is to REFUTE that — find published prior work that already addresses the underlying PROBLEM. Default to refuted=true if you find solid prior work; only refuted=false if, after a genuine search, the problem really does look open. Work from the repo root.

Idea title: ${idea.title}
Underlying problem (method-agnostic): ${idea.problem}
Proposed direction/approach: ${idea.direction}

The original assessment's reasoning was: ${assessment.reasoning}

Search HARDER and from a DIFFERENT angle than a generic search would (skeptic #${k + 1}: ${['focus on older/foundational work and adjacent fields', 'focus on the most recent 2 years of preprints and workshop papers', 'focus on the LessWrong / Alignment Forum / industry-lab writeups'][k]}). Use WebSearch (incl. allowed_domains ["lesswrong.com","alignmentforum.org"]) and:
  uv run python -m saim.verification.citation search-crossref '<problem terms>'
  uv run python -m saim.verification.citation search-s2 '<problem terms>'

Then judge: does published work materially address this problem? Return refuted (bool), suggestedClassification (your honest rubric placement using the same 5 levels: already_solved/largely_addressed/partially_addressed/mostly_novel/novel), and foundWork[] = the prior work you found as {"source","title","url","summary"} (may be empty if refuted=false).`,
          { schema: SKEPTIC_SCHEMA, phase: 'Verify', label: `verify:${idea.idea_id}:s${k + 1}` }
        )
      ))).filter(Boolean)

      const refuters = skeptics.filter((s) => s.refuted)
      if (refuters.length >= 2) {
        // Downgrade to the MOST SEVERE (least-novel) classification the
        // refuters agreed the evidence supports.
        finalClassification = refuters
          .map((s) => s.suggestedClassification)
          .reduce((lo, c) => (CLS_ORDER.indexOf(c) < CLS_ORDER.indexOf(lo) ? c : lo), finalClassification)
        evidence = evidence.concat(refuters.flatMap((s) => s.foundWork || []))
        log(`  ${idea.idea_id}: ${refuters.length}/3 skeptics refuted "${assessment.classification}" → downgraded to "${finalClassification}"`)
      }
    }

    // --- 3c: enrich the stage-2 record with novelty, apply hard gate, write ---
    const resultPath = `${RUN_DIR}/filter_score/results/stage3/batch_${pad3(i + 1)}_results.json`
    const evidenceJson = JSON.stringify(evidence.slice(0, 12))
    return agent(
      `Work from the repo root. Finalize the novelty record for ONE idea and write it as a stage-3 result.

idea_id: ${idea.idea_id}
Final novelty classification (already decided — do NOT change it): ${finalClassification}
Confidence: ${assessment.confidence}
Reasoning: ${assessment.reasoning}
Evidence JSON: ${evidenceJson}

Steps:
1. Read ${RUN_DIR}/filter_score/survivors/stage2_survivors.json (a JSON array) and find the object whose idea_id == "${idea.idea_id}". Call it BASE — it has scores, weighted_score, original_idea, etc. Keep ALL of BASE's fields.
2. Validate/format the novelty assessment:
   uv run python -m saim.pipeline.novelty format '{"classification":"${finalClassification}","confidence":${assessment.confidence},"reasoning":<reasoning as JSON string>,"evidence":${evidenceJson}}'
   This returns an object with a "derived_score". Call it NA.
3. Build the enriched record = BASE plus:
   - "novelty_assessment": NA
   - "novelty_method": "novelty_assessed"
   - in "scores", set "novelty": {"score": NA.derived_score, "reasoning": NA.reasoning, "confidence": NA.confidence}
   - HARD GATE: if "${finalClassification}" == "already_solved", set "eliminated": true and
     "elimination_reason": "Stage 3: novelty classification is 'already_solved' (hard gate)".
     Otherwise keep BASE's existing eliminated/elimination_reason (should be false/null for a survivor).
4. Write it as a single-element JSON array:
   uv run python -m saim.pipeline.filter_score write-batch-results ${resultPath} '[<enriched_record>]'

Return idea_id="${idea.idea_id}", written=true, eliminated=<bool>, finalClassification="${finalClassification}".`,
      { schema: WRITE_SCHEMA, phase: 'Finalize', label: `finalize:${idea.idea_id}` }
    )
  }
)

// ---------------------------------------------------------------------------
// Finalize: collapse stage-3 results into stage3_survivors.json (refine reads this).
// ---------------------------------------------------------------------------
phase('Finalize')

const written = stage3.filter(Boolean)
const final = await agent(
  `Work from the repo root. Run:
  uv run python -m saim.pipeline.filter_score filter-survivors ${RUN_DIR} 3
It merges all ${RUN_DIR}/filter_score/results/stage3/batch_*_results.json files, drops eliminated
ideas, and writes ${RUN_DIR}/filter_score/survivors/stage3_survivors.json. It prints
{"survivors": N, "eliminated": M}. Return survivors and eliminated.`,
  { schema: FINAL_SCHEMA, phase: 'Finalize', label: 'finalize:survivors' }
)

const eliminatedByGate = written.filter((w) => w.eliminated).length
log(`Novelty: assessed ${written.length} ideas, ${eliminatedByGate} hit the already_solved hard gate.`)
log(`Done. Stage-3 survivors: ${final.survivors}. Ready for /refine-ideas ${RUN_DIR}`)

return {
  runDir: RUN_DIR,
  stage1: { survivors: s1.survivors, eliminated: s1.eliminated },
  stage2: { survivors: s2.survivors, eliminated: s2.eliminated },
  novelty: {
    assessed: written.length,
    eliminatedByHardGate: eliminatedByGate,
    finalSurvivors: final.survivors,
    classifications: written.map((w) => ({ idea_id: w.idea_id, classification: w.finalClassification, eliminated: w.eliminated })),
  },
}
