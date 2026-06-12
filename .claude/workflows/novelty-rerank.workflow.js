export const meta = {
  name: 'novelty-rerank',
  description: 'Calculated novelty (web search + adversarial verify) on the top-N ranked proposals, then deterministic re-rank (rank #2) and optional persist',
  whenToUse: 'After /rank-ideas has produced rank/ranked_proposals.json with ESTIMATED novelty. Runs calculated novelty only on the top-N, drops already_solved, re-ranks the top block above the rest, and (with persist:true) writes the assessed top ideas to data/ideas/.',
  phases: [
    { title: 'Setup', detail: 'load top-N ranked proposals + novelty rubrics' },
    { title: 'Novelty', detail: 'per-proposal literature search + classification' },
    { title: 'Verify', detail: 'adversarial skeptics refute high-novelty claims; write updates' },
    { title: 'Rerank', detail: 'deterministic rank #2 + optional persist' },
  ],
}

// ---------------------------------------------------------------------------
// SAIM "novelty-rerank" workflow — the second tier of the two-tier novelty design.
//
// The cheap early pipeline uses ESTIMATED novelty (an LLM guess in /score-ideas)
// which carries through refine into rank #1. This workflow runs the EXPENSIVE
// CALCULATED novelty (web search + citation checks + adversarial verification)
// only on the top-N ranked proposals, then re-ranks (rank #2):
//
//   ... /rank-ideas (rank #1, estimated novelty)
//        -> novelty-rerank: top-N -> calculated novelty -> rank #2 [-> persist]
//
// The actual re-ranking and persist are done deterministically in Python
// (saim.pipeline.rank rerank), reusing apply_weights / persist_ideas, so the
// workflow only orchestrates the parallel novelty assessment + verification.
//
// args.runDir       : run dir path (default: latest under data/runs/)
// args.topN         : how many top-ranked proposals to assess (default 100)
// args.persist      : "true" to persist assessed survivors to data/ideas/ (default false)
// ---------------------------------------------------------------------------

// `args` may arrive as a parsed object OR a JSON string — normalize both.
let A = args
if (typeof A === 'string') { try { A = JSON.parse(A) } catch { A = {} } }
A = A || {}
const runDirArg = A.runDir || null
const topN = A.topN || 100
const persist = A.persist === true || A.persist === 'true'

const CLS_ORDER = ['already_solved', 'largely_addressed', 'partially_addressed', 'mostly_novel', 'novel']
const HIGH_NOVELTY = new Set(['mostly_novel', 'novel'])

// ---------------------------------------------------------------------------
// Schemas
// ---------------------------------------------------------------------------
const SETUP_SCHEMA = {
  type: 'object',
  required: ['runDir', 'updatesDir', 'classificationRubric', 'confidenceRubric', 'citationRubric', 'restCount', 'topProposals'],
  properties: {
    runDir: { type: 'string' },
    updatesDir: { type: 'string' },
    classificationRubric: { type: 'string', description: 'The 5-level novelty classification rubric (verbatim)' },
    confidenceRubric: { type: 'string' },
    citationRubric: { type: 'string' },
    restCount: { type: 'number', description: 'Number of proposals ranked below the top-N cutoff' },
    topProposals: {
      type: 'array',
      items: {
        type: 'object',
        required: ['idea_id', 'title', 'research_question', 'approach_outline'],
        properties: {
          idea_id: { type: 'string' },
          title: { type: 'string' },
          research_question: { type: 'string' },
          approach_outline: { type: 'string' },
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
          source: { type: 'string' }, title: { type: 'string' },
          url: { type: 'string' }, summary: { type: 'string' },
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
    refuted: { type: 'boolean' },
    suggestedClassification: { type: 'string', enum: CLS_ORDER },
    foundWork: {
      type: 'array',
      items: {
        type: 'object',
        required: ['source', 'title', 'url', 'summary'],
        properties: {
          source: { type: 'string' }, title: { type: 'string' },
          url: { type: 'string' }, summary: { type: 'string' },
        },
      },
    },
  },
  additionalProperties: true,
}

const WRITE_SCHEMA = {
  type: 'object',
  required: ['idea_id', 'written', 'finalClassification', 'eliminated'],
  properties: {
    idea_id: { type: 'string' },
    written: { type: 'boolean' },
    finalClassification: { type: 'string', enum: CLS_ORDER },
    eliminated: { type: 'boolean' },
  },
  additionalProperties: true,
}

const RERANK_SCHEMA = {
  type: 'object',
  required: ['assessed', 'eliminated', 'survivors_top', 'rest', 'total', 'persisted'],
  properties: {
    assessed: { type: 'number' }, eliminated: { type: 'number' },
    survivors_top: { type: 'number' }, rest: { type: 'number' },
    total: { type: 'number' }, persisted: { type: 'number' },
  },
  additionalProperties: true,
}

// ---------------------------------------------------------------------------
// Phase: Setup — resolve run dir, load top-N proposals + rubrics, prep updates dir.
// ---------------------------------------------------------------------------
phase('Setup')

const cfg = await agent(
  `You are preparing the calculated-novelty re-rank pass for a SAIM run. Work from the repo root.

${runDirArg ? `The run directory is: ${runDirArg}` : 'Find the latest run with: ls -1t data/runs/ | head -1  → run dir is data/runs/<that>'}

1. Resolve RUN_DIR. Read RUN_DIR/rank/ranked_proposals.json (the rank #1 output, a JSON array of proposals each with "idea_id", "rank", "title", and a "sections" object containing "research_question" and "approach_outline"). If the file does not exist, return topProposals: [] and explain.

2. Sort by "rank" ascending and take the top ${topN}. For each, return: idea_id, title, research_question (sections.research_question), approach_outline (sections.approach_outline). Set restCount = max(0, total_proposals - ${topN}).

3. Prepare a clean updates directory:
   rm -rf RUN_DIR/novelty_rerank/updates && mkdir -p RUN_DIR/novelty_rerank/updates
   Return updatesDir = "RUN_DIR/novelty_rerank/updates" (with RUN_DIR expanded).

4. Load rubrics (capture verbatim):
   uv run python -m saim.config.cli show-citation-relevance  → citationRubric
   uv run python -m saim.config.cli show-scoring             → confidenceRubric (the Confidence Rubric block)
   For classificationRubric, return this 5-level rubric verbatim:
     already_solved (1): existing published work FULLY addresses the idea — cite the specific paper(s).
     largely_addressed (2): multiple works cover most of the proposed contribution; gaps minor.
     partially_addressed (3): work exists but the specific angle/method/combination proposed is unexplored.
     mostly_novel (4): no direct published work on this proposal; related work in adjacent areas.
     novel (5): no published work found on this question or approach.

Return all fields per the schema.`,
  { schema: SETUP_SCHEMA, phase: 'Setup', label: 'setup:load-top-n' }
)

const RUN_DIR = cfg.runDir
if (!cfg.topProposals || cfg.topProposals.length === 0) {
  log('No ranked proposals found — run /rank-ideas (rank #1) first.')
  return { error: 'no rank #1 output', runDir: RUN_DIR }
}
log(`Run dir: ${RUN_DIR} — assessing top ${cfg.topProposals.length} of ${cfg.topProposals.length + cfg.restCount} ranked proposals (persist=${persist})`)

// ---------------------------------------------------------------------------
// Phase: Novelty (search) + Verify (skeptics) + write update files — per proposal.
// ---------------------------------------------------------------------------
phase('Novelty')

const verdicts = await pipeline(
  cfg.topProposals,

  // --- calculated novelty search ---
  (p) => agent(
    `You are assessing the NOVELTY of one AI Safety research proposal via a literature search. Work from the repo root.

Title: ${p.title}
Research question: ${p.research_question}
Proposed approach: ${p.approach_outline}

Source-reading policy: start with abstracts/summaries; read deeper only when it could change the classification. Never read full papers end-to-end.

Two-tier search (Tier 1 first, weighted more heavily):
- Tier 1 (problem-level): is the underlying PROBLEM already solved by ANY method? Strip the proposed method from your queries. Run 2+ problem-level WebSearch queries (different phrasings) + 1 "known approaches/survey" query.
- Tier 2 (method-level): has this SPECIFIC approach been tried? 1+ query.
Community search: WebSearch with allowed_domains ["lesswrong.com","alignmentforum.org"], 2-3 problem-first queries.
Structured DB (problem terms first, then method terms):
  uv run python -m saim.verification.citation search-crossref '<terms>'
  uv run python -m saim.verification.citation search-s2 '<terms>'

Classify (the key question is whether the PROBLEM is solved, not whether the METHOD is new):
${cfg.classificationRubric}

Confidence rubric:
${cfg.confidenceRubric}

Match evidence to the level descriptions — not gut feeling. Record each relevant work as {"source","title","url","summary"}.
Return idea_id="${p.idea_id}", classification, confidence, reasoning (2-4 sentences citing specific evidence), evidence[].`,
    { schema: NOVELTY_SCHEMA, phase: 'Novelty', label: `novelty:${p.idea_id}` }
  ),

  // --- adversarial verify (conditional) + write update file ---
  async (assessment, p, i) => {
    let finalClassification = assessment.classification
    let evidence = assessment.evidence || []

    if (HIGH_NOVELTY.has(assessment.classification)) {
      const skeptics = (await parallel([0, 1, 2].map((k) => () =>
        agent(
          `You are skeptic #${k + 1} of 3. An assessment classified the AI Safety proposal below as "${assessment.classification}" (highly novel). REFUTE it — find published prior work that already addresses the underlying PROBLEM. Default to refuted=true if you find solid prior work; refuted=false only if, after a genuine search, the problem really is open. Work from the repo root.

Title: ${p.title}
Research question: ${p.research_question}
Proposed approach: ${p.approach_outline}
Original reasoning: ${assessment.reasoning}

Search HARDER and from a DIFFERENT angle (skeptic #${k + 1}: ${['older/foundational work and adjacent fields', 'the most recent 2 years of preprints and workshop papers', 'LessWrong / Alignment Forum / industry-lab writeups'][k]}). Use WebSearch (incl. allowed_domains ["lesswrong.com","alignmentforum.org"]) and:
  uv run python -m saim.verification.citation search-crossref '<problem terms>'
  uv run python -m saim.verification.citation search-s2 '<problem terms>'

Return refuted (bool), suggestedClassification (honest rubric placement, same 5 levels), foundWork[] = prior work as {"source","title","url","summary"} (may be empty).`,
          { schema: SKEPTIC_SCHEMA, phase: 'Verify', label: `verify:${p.idea_id}:s${k + 1}` }
        )
      ))).filter(Boolean)

      const refuters = skeptics.filter((s) => s.refuted)
      if (refuters.length >= 2) {
        finalClassification = refuters
          .map((s) => s.suggestedClassification)
          .reduce((lo, c) => (CLS_ORDER.indexOf(c) < CLS_ORDER.indexOf(lo) ? c : lo), finalClassification)
        evidence = evidence.concat(refuters.flatMap((s) => s.foundWork || []))
        log(`  ${p.idea_id}: ${refuters.length}/3 skeptics refuted "${assessment.classification}" → "${finalClassification}"`)
      }
    }

    // Write the validated update file the rerank CLI will read.
    const updatePath = `${cfg.updatesDir}/${p.idea_id}.json`
    const evidenceJson = JSON.stringify(evidence.slice(0, 12))
    return agent(
      `Work from the repo root. Write the calculated-novelty update file for ONE proposal.

idea_id: ${p.idea_id}
Final classification (already decided — do NOT change): ${finalClassification}
Confidence: ${assessment.confidence}
Reasoning: ${assessment.reasoning}
Evidence JSON: ${evidenceJson}

Steps:
1. Validate/derive the score:
   uv run python -m saim.pipeline.novelty format '{"classification":"${finalClassification}","confidence":${assessment.confidence},"reasoning":<reasoning as JSON string>,"evidence":${evidenceJson}}'
   This prints an object with "derived_score".
2. Using the Write tool, write ${updatePath} containing exactly this JSON object:
   {"idea_id":"${p.idea_id}","classification":"${finalClassification}","derived_score":<derived_score>,"confidence":${assessment.confidence},"reasoning":<reasoning as JSON string>,"evidence":${evidenceJson},"eliminated":${finalClassification === 'already_solved'}}

Return idea_id="${p.idea_id}", written=true, finalClassification="${finalClassification}", eliminated=${finalClassification === 'already_solved'}.`,
      { schema: WRITE_SCHEMA, phase: 'Verify', label: `update:${p.idea_id}` }
    )
  }
)

const written = verdicts.filter(Boolean)
const gated = written.filter((w) => w.eliminated).length
log(`Novelty: wrote ${written.length} updates, ${gated} classified already_solved (will be dropped).`)

// ---------------------------------------------------------------------------
// Phase: Rerank — deterministic rank #2 (+ optional persist), in Python.
// ---------------------------------------------------------------------------
phase('Rerank')

const rerank = await agent(
  `Work from the repo root. Run the deterministic re-rank, which reads every update file in the updates dir, applies calculated novelty to the top ${topN} proposals, drops already_solved, recomputes weighted scores, re-sorts the top block above the rest, overwrites rank/ranked_proposals.{json,md}, backs up the original rank #1 to rank/ranked_proposals.rank1.json, and ${persist ? 'persists assessed survivors to data/ideas/' : 'does NOT persist'}:

  uv run python -m saim.pipeline.rank rerank ${RUN_DIR} ${cfg.updatesDir} ${topN} ${persist ? 'true' : 'false'}

It prints a JSON object with assessed, eliminated, survivors_top, rest, total, persisted. Return those fields.`,
  { schema: RERANK_SCHEMA, phase: 'Rerank', label: 'rerank:rank2' }
)

log(`Rank #2 complete: ${rerank.survivors_top} top survivors re-ranked above ${rerank.rest} others (total ${rerank.total}). Persisted: ${rerank.persisted}.`)
log(`Final ranking: ${RUN_DIR}/rank/ranked_proposals.md  (rank #1 backed up to ranked_proposals.rank1.json)`)

return {
  runDir: RUN_DIR,
  topN,
  persist,
  assessed: rerank.assessed,
  eliminatedByHardGate: rerank.eliminated,
  topSurvivors: rerank.survivors_top,
  rest: rerank.rest,
  total: rerank.total,
  persisted: rerank.persisted,
  classifications: written.map((w) => ({ idea_id: w.idea_id, classification: w.finalClassification, eliminated: w.eliminated })),
}
