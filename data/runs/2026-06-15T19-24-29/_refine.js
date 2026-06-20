export const meta = {
  name: 'saim-refine',
  description: 'SAIM refine: expand top-500 scored ideas into full proposals, one agent per batch of 10 (50 batches)',
  phases: [ { title: 'Refine' } ],
}
const RUN_DIR = 'data/runs/2026-06-15T19-24-29'
const N_BATCHES = 50

const PARTICIPANT = 'CS students, FIRST hands-on AI-safety project; basic Python/ML; single consumer GPU (Colab Pro/Runpod), runs at most a few hours, NO training-from-scratch; ~30 hours TOTAL including writing a blog post. The first deliverable must be self-contained, with a clear methodology and explicit success criteria.'

const COUNTERFACTUAL = 'PRESERVE the idea\'s counterfactual-value angle (valuable OUTSIDE major labs: no training/proprietary data, no lab-internal infra, long-horizon >1yr threat models, fuzzy-reward evals, model organisms, strategic infra). Make the proposal concretely executable by an independent beginner team in 30 hours.'

function prompt(n) {
  const b = String(n).padStart(3,'0')
  const batchPath = `${RUN_DIR}/refine/_batches/batch_${b}.json`
  return [
    `You are assembling FULL AI-safety research proposals from scored idea sketches. Run all Bash from repo root /home/guido/Desktop/saim.`,
    ``,
    `Step 1 — read your batch (a JSON array; each element has "scored" (the scored idea incl. original_idea + scores), "skeleton" (a prebuilt proposal dict with correct frontmatter you MUST keep), "weak_dimensions", "strong_dimensions"):`,
    `  cat ${batchPath}`,
    `(Use the Read tool on ${batchPath}.)`,
    ``,
    `Step 2 — for EACH element, produce a completed proposal by taking its "skeleton" dict UNCHANGED except:`,
    `  - Fill skeleton.sections with rich, concrete content:`,
    `    * research_question: 1-2 sentences framing the core question.`,
    `    * approach_outline: 3-5 sentences of methodology and key steps, feasible for the team.`,
    `    * proposed_first_experiments: a LIST of 3 concrete experiments (each: what to do, what to measure, expected outcome).`,
    `    * theory_of_impact_chain: 2-4 sentences — if this works, then X -> Y -> improves safety because Z (name a concrete catastrophic-risk pathway).`,
    `    * strength_rationale: 2-3 sentences on why this idea is strong, referencing its top-scoring criteria (esp. counterfactual value & narrow scope).`,
    `    * cited_sources: a LIST of grounding sources (use what is in scored.original_idea.relevant_context; each item a short "Title — why relevant" string). If none, use [].`,
    `    * alternative_framings: optional LIST (0-2) of short alternative-framing strings; else [].`,
    `  - Set refinement_confidence to a 0.0-1.0 number reflecting your confidence in the proposal.`,
    `  - Set num_alternative_framings to the count of alternative_framings you added.`,
    `  Keep ALL other skeleton frontmatter keys (idea_id, run_id, stage, timestamp, title, original_scores, novelty_classification, novelty_score, novelty_method, pre_refine_weighted_score, weak_dimensions_addressed, generation_strategy, subfield, provenance) EXACTLY as given.`,
    ``,
    PARTICIPANT,
    ``, COUNTERFACTUAL,
    ``,
    `Step 3 — write each completed proposal dict. For each idea, write the JSON to a temp file then pass it, e.g.:`,
    `  write the dict to /tmp/prop_${b}_<idea_id>.json, then run:`,
    `  uv run python -m saim.pipeline.refine write ${RUN_DIR} "$(cat /tmp/prop_${b}_<idea_id>.json)"`,
    `  (Ensure valid JSON. The "sections" key must be present with the filled values.)`,
    ``,
    `Do all 10 (or fewer) ideas in your batch. Return ONLY the integer count of proposals you wrote.`,
  ].join('\n')
}

log(`Refine: launching ${N_BATCHES} agents (10 proposals each)`)
const idxs = Array.from({length: N_BATCHES}, (_, i) => i + 1)
const res = await parallel(idxs.map(n => () =>
  agent(prompt(n), { label: `refine_${String(n).padStart(3,'0')}`, phase: 'Refine', agentType: 'general-purpose' })
    .then(r => ({ n, ret: r }))
))
const ok = res.filter(Boolean)
log(`Refine agents returned: ${ok.length}/${N_BATCHES}`)
return { returned: ok.length, total: N_BATCHES }
