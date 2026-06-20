export const meta = {
  name: 'saim-generate-resume',
  description: 'Resume SAIM generation: run only the 46 agents that failed on the session rate limit (last 4 subfield tails + 3 lenses + combinatorial)',
  phases: [ { title: 'Generate' } ],
}

const RUN_DIR = 'data/runs/2026-06-15T19-24-29'
const MIN = 25
const STAGING = `${RUN_DIR}/_gen_staging`

const STRAT_DESC = {
  novel_direction: 'A new research direction addressing an open problem in this subfield.',
  experiment_variation: 'Propose variations of existing experiments: modify variables, populations, methodologies, or scope.',
  follow_up_experiment: 'Propose follow-up experiments to explain observed effects from recent surprising results.',
  replication_with_twist: 'Take a known result and replicate it on a different model family, dataset, modality, or scale. Particularly accessible for beginners.',
  tool_or_benchmark_gap: 'Fill a gap in evaluation tooling, extend an existing benchmark, or create a new measurement for an unmeasured property.',
  failure_mode_investigation: 'Target a known failure mode/incident/surprising result; design an experiment to characterize it, find root causes, or test boundary conditions.',
  cross_domain_transfer: 'Import a technique from outside AI safety (software testing, cognitive science, formal methods, biology, economics) into this subfield.',
  causal_chain_intervention: 'Decompose a known safety risk into its causal chain (risk -> scenario -> causal steps) and target an under-studied link.',
  backcast_from_success: 'Define a concrete safety success state for this subfield, then work backward to a research result that would need to exist; propose research filling one such gap.',
  compounding_risks: 'Identify how a failure in this subfield amplifies a failure in a different subfield; study/measure/mitigate the compound effect. Name the two interacting failure modes.',
  recent_paper_extension: 'Use WebSearch to find the most relevant AI-safety papers from roughly the LAST MONTH in this subfield, and propose strong, concrete extensions to them. In relevant_context cite the specific recent paper (title + venue/arxiv id + ~date).',
}

const LENS_DESC = {
  methodology_bridging: 'Take a methodology proven in one subfield and apply it to an open problem in a DIFFERENT subfield where it has not been tried. Name source subfield and target subfield in each idea.',
  problem_decomposition: 'Take a hard open problem from one subfield and break it into sub-problems addressable with methods/tools from other subfields. Each idea tackles ONE specific sub-problem, not the whole thing.',
  landscape_gap_targeting: 'Propose ideas that directly address gaps where no subfield naturally owns the problem, or where coverage is thin relative to importance. Each idea names which gap it targets.',
}

const MISSING = [
  ['s101_follow_up_experiment','formal_theoretical','follow_up_experiment'],
  ['s102_replication_with_twist','formal_theoretical','replication_with_twist'],
  ['s103_tool_or_benchmark_gap','formal_theoretical','tool_or_benchmark_gap'],
  ['s104_failure_mode_investigation','formal_theoretical','failure_mode_investigation'],
  ['s105_cross_domain_transfer','formal_theoretical','cross_domain_transfer'],
  ['s106_causal_chain_intervention','formal_theoretical','causal_chain_intervention'],
  ['s107_backcast_from_success','formal_theoretical','backcast_from_success'],
  ['s108_compounding_risks','formal_theoretical','compounding_risks'],
  ['s109_recent_paper_extension','formal_theoretical','recent_paper_extension'],
  ['s110_novel_direction','governance_policy','novel_direction'],
  ['s111_experiment_variation','governance_policy','experiment_variation'],
  ['s112_follow_up_experiment','governance_policy','follow_up_experiment'],
  ['s113_replication_with_twist','governance_policy','replication_with_twist'],
  ['s114_tool_or_benchmark_gap','governance_policy','tool_or_benchmark_gap'],
  ['s115_failure_mode_investigation','governance_policy','failure_mode_investigation'],
  ['s116_cross_domain_transfer','governance_policy','cross_domain_transfer'],
  ['s117_causal_chain_intervention','governance_policy','causal_chain_intervention'],
  ['s118_backcast_from_success','governance_policy','backcast_from_success'],
  ['s119_compounding_risks','governance_policy','compounding_risks'],
  ['s120_recent_paper_extension','governance_policy','recent_paper_extension'],
  ['s121_novel_direction','model_homogeneity','novel_direction'],
  ['s122_experiment_variation','model_homogeneity','experiment_variation'],
  ['s123_follow_up_experiment','model_homogeneity','follow_up_experiment'],
  ['s124_replication_with_twist','model_homogeneity','replication_with_twist'],
  ['s125_tool_or_benchmark_gap','model_homogeneity','tool_or_benchmark_gap'],
  ['s126_failure_mode_investigation','model_homogeneity','failure_mode_investigation'],
  ['s127_cross_domain_transfer','model_homogeneity','cross_domain_transfer'],
  ['s128_causal_chain_intervention','model_homogeneity','causal_chain_intervention'],
  ['s129_backcast_from_success','model_homogeneity','backcast_from_success'],
  ['s130_compounding_risks','model_homogeneity','compounding_risks'],
  ['s131_recent_paper_extension','model_homogeneity','recent_paper_extension'],
  ['s132_novel_direction','concept_steering','novel_direction'],
  ['s133_experiment_variation','concept_steering','experiment_variation'],
  ['s134_follow_up_experiment','concept_steering','follow_up_experiment'],
  ['s135_replication_with_twist','concept_steering','replication_with_twist'],
  ['s136_tool_or_benchmark_gap','concept_steering','tool_or_benchmark_gap'],
  ['s137_failure_mode_investigation','concept_steering','failure_mode_investigation'],
  ['s138_cross_domain_transfer','concept_steering','cross_domain_transfer'],
  ['s139_causal_chain_intervention','concept_steering','causal_chain_intervention'],
  ['s140_backcast_from_success','concept_steering','backcast_from_success'],
  ['s141_compounding_risks','concept_steering','compounding_risks'],
  ['s142_recent_paper_extension','concept_steering','recent_paper_extension'],
  ['lens_methodology_bridging',null,'methodology_bridging'],
  ['lens_problem_decomposition',null,'problem_decomposition'],
  ['lens_landscape_gap_targeting',null,'landscape_gap_targeting'],
  ['combinatorial',null,'combinatorial_matrix'],
]

const PARTICIPANT = [
  '- Completable in ~30 hours TOTAL (implementation + experimentation + analysis + writing a blog post).',
  '- Skills: basic Python, CS fundamentals, intro ML, statistics, linear algebra. CS students doing their FIRST hands-on AI safety research; NO prior interpretability/RLHF/safety-tooling experience. Avoid methods needing deep expertise or heavy engineering.',
  '- Compute: medium — a single consumer GPU (Colab Pro / Runpod), runs of at most a few hours. NO multi-GPU clusters, NO training from scratch, NO large-scale training.',
  '- Deliverable: a working experiment/analysis PLUS a well-written blog post communicating findings and their AI-safety relevance.',
  '- The first deliverable must be self-contained and valuable on its own, with a clear methodology and success criteria.',
].join('\n')

const COUNTERFACTUAL = [
  'COUNTERFACTUAL-VALUE PRIORITY (weight heavily): strongly favor research valuable to do OUTSIDE a major AI lab:',
  '- Favor ideas needing NO model training and NO proprietary/large datasets.',
  "- Favor ideas needing NO access to a lab's internal infrastructure (internal weights tooling, defense-in-depth, proprietary data).",
  '- Favor medium/long-horizon (>1 year) threat models that frontier labs are forced to deprioritize for immediate concerns.',
  '- Favor evaluations of diffuse / fuzzy-reward problems (hard to do well, need no lab resources).',
  '- Favor model-organism studies (e.g. a model that attacks without verbalizing its plan in the CoT, a model good at Schelling games, a model pursuing secret long-horizon goals) — scoped to a feasible 30h slice (probe/evaluate an existing or small open model organism rather than train one).',
  '- Favor building strategically valuable infrastructure (safer sandboxes / firewalls / monitoring harnesses) — scoped to a small prototype.',
  'Where a theme is ambitious, scope it to a 30-hour first deliverable. Stay grounded and COMPREHENSIVE — do NOT let this steering collapse diversity; still cover the full breadth of the subfield.',
].join('\n')

const DIVERGENCE = 'A catalogue of 632 previously-generated ideas already exists. Avoid rehashing obvious/common framings; seek fresh angles, methods, and combinations.'

function outRules(label, strategyName, subfieldNote) {
  return `
Generate AT LEAST ${MIN} idea sketches using ONLY the "${strategyName}" strategy${subfieldNote ? ` (${subfieldNote})` : ''}.
Each idea is a brief sketch: problem + direction + why it matters, grounded in real research.
Use WebSearch to verify grounding. Read ONLY abstracts/summaries — never full papers.

Write your output as a SINGLE JSON array to this exact file using the Write tool:
  ${STAGING}/${label}.json
The file content MUST be ONLY a JSON array (no markdown fences, no prose). Each element is an object with keys:
  "title", "problem", "direction", "why_it_matters", "relevant_context",
  "subfield", "generation_strategy" (= "${strategyName}"), "confidence" (number 0.0-1.0).
After writing the file, return ONLY the integer count of ideas you wrote.`
}

function buildPrompt([label, subfield, strat]) {
  if (subfield) {
    return [
      `You are generating AI Safety research idea sketches for subfield: ${subfield}.`,
      `Assigned generation strategy: ${strat} — ${STRAT_DESC[strat]}`,
      ``,
      `First, read the subfield context file with the Read tool: ${RUN_DIR}/_ctx/${subfield}.md`,
      `Use its Open Problems, Generation Strategy Hints, Recent Surprising Results, Key Datasets & Benchmarks, Common Methodologies, and Source Code Availability to ground every idea.`,
      ``, `Participant constraints (all ideas MUST satisfy these):`, PARTICIPANT,
      ``, COUNTERFACTUAL, ``, DIVERGENCE, ``,
      outRules(label, strat, `subfield: ${subfield}`),
    ].join('\n')
  }
  if (strat === 'combinatorial_matrix') {
    return [
      `You are generating AI Safety research ideas from a structured combinatorial matrix of problems and methods.`,
      `Read data/output/research-landscape.md. Select the top ~10 open problems across subfields (by priority) and the top ~10 methodologies across subfields. Form cross-products where problem and method come from DIFFERENT subfields.`,
      `For each viable (problem, method) pair, assess "Could this method shed light on this problem?" If yes, generate an idea sketch; skip nonsensical pairings.`,
      ``, `Participant constraints (all ideas MUST satisfy these):`, PARTICIPANT,
      ``, COUNTERFACTUAL, ``, DIVERGENCE, ``,
      outRules(label, 'combinatorial_matrix', 'subfield = comma-separated list of the bridged subfields'),
    ].join('\n')
  }
  return [
    `You are generating AI Safety research ideas using the cross-subfield strategy: ${strat} — ${LENS_DESC[strat]}`,
    ``, `Read data/output/research-landscape.md for context (read only the sections you need).`,
    ``, `Participant constraints (all ideas MUST satisfy these):`, PARTICIPANT,
    ``, COUNTERFACTUAL, ``, DIVERGENCE, ``,
    outRules(label, strat, 'subfield = comma-separated list of the bridged subfields'),
  ].join('\n')
}

log(`Resuming generation: ${MISSING.length} agents`)
const results = await parallel(MISSING.map(m => () =>
  agent(buildPrompt(m), { label: m[0], phase: 'Generate', agentType: 'general-purpose' })
    .then(r => ({ label: m[0], ret: r }))
))
const ok = results.filter(Boolean)
log(`Resume agents returned: ${ok.length}/${MISSING.length}`)
return { launched: MISSING.length, returned: ok.length, agents: ok }
