export const meta = {
  name: 'saim-generate',
  description: 'SAIM generation: 13 subfields x 11 strategies + 3 synthesis lenses + combinatorial pass; each agent writes an idea batch JSON to staging',
  phases: [
    { title: 'Generate' },
  ],
}

const RUN_DIR = 'data/runs/2026-06-15T19-24-29'
const RUN_ID = '2026-06-15T19-24-29'
const MIN = 25
const STAGING = `${RUN_DIR}/_gen_staging`

const SUBFIELDS = [
  'adversarial_robustness','mechanistic_interpretability','alignment_training',
  'scalable_oversight','ai_control','evaluations_benchmarks','deception_scheming',
  'honesty_faithfulness','agentic_safety','formal_theoretical','governance_policy',
  'model_homogeneity','concept_steering',
]

const STRATEGIES = [
  ['novel_direction', 'A new research direction addressing an open problem in this subfield.'],
  ['experiment_variation', 'Propose variations of existing experiments: modify variables, populations, methodologies, or scope.'],
  ['follow_up_experiment', 'Propose follow-up experiments to explain observed effects from recent surprising results.'],
  ['replication_with_twist', 'Take a known result and replicate it on a different model family, dataset, modality, or scale. Particularly accessible for beginners.'],
  ['tool_or_benchmark_gap', 'Fill a gap in evaluation tooling, extend an existing benchmark, or create a new measurement for an unmeasured property.'],
  ['failure_mode_investigation', 'Target a known failure mode/incident/surprising result; design an experiment to characterize it, find root causes, or test boundary conditions.'],
  ['cross_domain_transfer', 'Import a technique from outside AI safety (software testing, cognitive science, formal methods, biology, economics) into this subfield.'],
  ['causal_chain_intervention', 'Decompose a known safety risk into its causal chain (risk -> scenario -> causal steps) and target an under-studied link.'],
  ['backcast_from_success', 'Define a concrete safety success state for this subfield, then work backward to a research result that would need to exist; propose research filling one such gap.'],
  ['compounding_risks', 'Identify how a failure in this subfield amplifies a failure in a different subfield; study/measure/mitigate the compound effect. Name the two interacting failure modes.'],
  ['recent_paper_extension', 'Use WebSearch to find the most relevant AI-safety papers from roughly the LAST MONTH in this subfield, and propose strong, concrete extensions to them. In relevant_context cite the specific recent paper (title + venue/arxiv id + ~date).'],
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

const DIVERGENCE = [
  'A catalogue of 632 previously-generated ideas already exists. Avoid rehashing obvious/common framings; seek fresh angles, methods, and combinations. Examples already covered (do not repeat these):',
  '"Activation Probe Generalization", "Cross-Lingual Safety Gap Mapping", "Special Token Exploitation Prevalence", "StrongREJECT Contamination Check", "Perplexity Filter Evasion Rate", "Automated Red-Teaming Coverage Blind Spots", "Consistency of Safety Across Decoding Parameters", "Prompt Injection in RAG Systems", "DIF Analysis of Safety Benchmark Items", "Dose-Response Curves for Harmful Capability Elicitation", "IRT Person-Fit Analysis to Detect Sandbagging", "Bifactor Modeling of AI Safety Benchmarks", "Graded Response Model for Partial Safety Credit".',
].join('\n')

const OUTPUT_RULES = (label, strategyName, subfieldLabel) => `
Generate AT LEAST ${MIN} idea sketches using ONLY the "${strategyName}" strategy${subfieldLabel ? ` for subfield: ${subfieldLabel}` : ''}.
Each idea is a brief sketch: problem + direction + why it matters, grounded in real research.
Use WebSearch to verify grounding. Read ONLY abstracts/summaries — never full papers.

Write your output as a SINGLE JSON array to this exact file using the Write tool:
  ${STAGING}/${label}.json
The file content MUST be ONLY a JSON array (no markdown fences, no prose). Each element is an object with keys:
  "title" (string), "problem" (string), "direction" (string), "why_it_matters" (string),
  "relevant_context" (string, grounding references — abstracts/key findings cited),
  "subfield" (string), "generation_strategy" (string = "${strategyName}"),
  "confidence" (number 0.0-1.0).
After writing the file, return ONLY the integer count of ideas you wrote.`

function subfieldPrompt(subfield, strategyName, strategyDesc, idx) {
  const label = `s${String(idx).padStart(2,'0')}_${strategyName}`
  return [
    `You are generating AI Safety research idea sketches for subfield: ${subfield}.`,
    `Assigned generation strategy: ${strategyName} — ${strategyDesc}`,
    ``,
    `First, read the subfield context file with the Read tool: ${RUN_DIR}/_ctx/${subfield}.md`,
    `Use its Open Problems, Generation Strategy Hints, Recent Surprising Results, Key Datasets & Benchmarks, Common Methodologies, and Source Code Availability to ground every idea.`,
    ``,
    `Participant constraints (all ideas MUST satisfy these):`,
    PARTICIPANT,
    ``,
    COUNTERFACTUAL,
    ``,
    DIVERGENCE,
    ``,
    OUTPUT_RULES(label, strategyName, subfield),
  ].join('\n')
}

// Build all subfield x strategy agent thunks
const thunks = []
let idx = 0
for (const sf of SUBFIELDS) {
  for (const [sname, sdesc] of STRATEGIES) {
    const myIdx = idx++
    const label = `s${String(myIdx).padStart(2,'0')}_${sname}`
    thunks.push(() => agent(subfieldPrompt(sf, sname, sdesc, myIdx), {
      label, phase: 'Generate', agentType: 'general-purpose',
    }).then(r => ({ label, subfield: sf, strategy: sname, ret: r })))
  }
}

// 3 cross-subfield synthesis lenses
const LENSES = [
  ['methodology_bridging', 'Take a methodology proven in one subfield and apply it to an open problem in a DIFFERENT subfield where it has not been tried. Name source subfield and target subfield in each idea.'],
  ['problem_decomposition', 'Take a hard open problem from one subfield and break it into sub-problems addressable with methods/tools from other subfields. Each idea tackles ONE specific sub-problem, not the whole thing.'],
  ['landscape_gap_targeting', 'Propose ideas that directly address gaps where no subfield naturally owns the problem, or where coverage is thin relative to importance. Each idea names which gap it targets.'],
]
for (const [lname, ldesc] of LENSES) {
  const label = `lens_${lname}`
  const prompt = [
    `You are generating AI Safety research ideas using the cross-subfield strategy: ${lname} — ${ldesc}`,
    ``,
    `Read the full landscape for context with the Read tool: data/output/research-landscape.md (read ONLY the section headers and the Subfields / Landscape Gaps sections you need; do not read it line-by-line exhaustively).`,
    ``,
    `Participant constraints (all ideas MUST satisfy these):`,
    PARTICIPANT,
    ``,
    COUNTERFACTUAL,
    ``,
    DIVERGENCE,
    ``,
    OUTPUT_RULES(label, lname, '(subfield = comma-separated list of the bridged subfields)'),
  ].join('\n')
  thunks.push(() => agent(prompt, { label, phase: 'Generate', agentType: 'general-purpose' })
    .then(r => ({ label, strategy: lname, ret: r })))
}

// Combinatorial matrix pass
{
  const label = 'combinatorial'
  const prompt = [
    `You are generating AI Safety research ideas from a structured combinatorial matrix of problems and methods.`,
    `Read data/output/research-landscape.md. Select the top ~10 open problems across subfields (by priority) and the top ~10 methodologies across subfields. Form cross-products where problem and method come from DIFFERENT subfields.`,
    `For each viable (problem, method) pair, assess "Could this method shed light on this problem?" If yes, generate an idea sketch; skip nonsensical pairings.`,
    ``,
    `Participant constraints (all ideas MUST satisfy these):`,
    PARTICIPANT,
    ``,
    COUNTERFACTUAL,
    ``,
    DIVERGENCE,
    ``,
    OUTPUT_RULES(label, 'combinatorial_matrix', '(subfield = comma-separated list of the bridged subfields)'),
  ].join('\n')
  thunks.push(() => agent(prompt, { label, phase: 'Generate', agentType: 'general-purpose' })
    .then(r => ({ label, strategy: 'combinatorial_matrix', ret: r })))
}

log(`Launching ${thunks.length} generation agents (min ${MIN} ideas each)`)
const results = await parallel(thunks)
const ok = results.filter(Boolean)
log(`Generation agents returned: ${ok.length}/${thunks.length}`)
return { launched: thunks.length, returned: ok.length, agents: ok }
