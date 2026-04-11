# Research Topic Report: Opus 4.6 Feasibility Against Cybersecurity Benchmarks

> Generated: 2026-04-08
> Requested by: coordinator
> Primary sources:
>   1. "Frontier AI's Impact on Cybersecurity" (arXiv:2504.05408v4, UC Berkeley RDI)
>   2. "Quantifying Frontier LLM Capabilities for Container Sandbox Escape" (arXiv:2603.02277, Marchand et al.)
> Focus: Can Claude Opus 4.6 address the LLM limitations identified in these papers?

## Topic Definition

The primary paper (arXiv:2504.05408) by UC Berkeley's RDI group comprehensively analyzes frontier AI's impact on cybersecurity through benchmarks, empirical evaluation, and expert survey. It identifies that current AI agents struggle with defensive cybersecurity tasks — particularly flexible workflow planning and domain-specific tool use. The paper's empirical evaluation used OpenHands + Claude Sonnet 4.5 as the primary agent.

The second paper (arXiv:2603.02277) by Marchand et al. introduces SandboxEscapeBench, a benchmark measuring LLM capability to escape container sandboxes — directly relevant to AI agent safety since agents are typically sandboxed in containers. It tested Opus 4.5 (but not 4.6) alongside GPT-5 and other frontier models, finding that frontier models reliably escape common misconfigurations but fail on harder kernel-level exploits.

This report assesses whether Opus 4.6 could meaningfully change the results across both papers, tracking feasibility for every benchmark discussed.

## Dimensions Tracked

| # | Dimension | Description |
|---|-----------|-------------|
| 1 | **Complexity** | Infrastructure, setup, and expertise needed to run the benchmark |
| 2 | **Cost** | Estimated API + compute cost per full benchmark run |
| 3 | **Opus 4.6 status** | Whether Opus 4.6 has already been evaluated on this benchmark |
| 4 | **Paper's recognized limitations** | What the paper flags as problems with this benchmark |
| 5 | **Paper's relevance weighting** | How central this benchmark is to the paper's argument |

---

## Benchmark Catalog

### OFFENSIVE BENCHMARKS

---

### 1. AutoPenBench

- **What it measures:** End-to-end penetration testing across reconnaissance, delivery, and exploitation (33 tasks)
- **Paper's attack stage:** Steps 1-7 (full kill chain)
- **URL:** https://github.com/lucagioacchini/auto-pen-bench

| Dimension | Assessment |
|-----------|-----------|
| **Complexity** | **Medium-High.** Requires Docker + Kali Linux environment. 33 vulnerable containers must be built and networked. Agent needs access to pentesting tools (Nmap, Metasploit, Hydra). Well-documented GitHub repo with examples. |
| **Cost** | **Low-Medium.** Paper reports $0.202 avg per task ($0.139 in-vitro, $0.454 real-world). Full run ~$7 at Sonnet pricing. With Opus 4.6 ($15/MTok input, $75/MTok output), expect ~$50-100 for a full run. |
| **Opus 4.6 status** | **Not tested.** Paper used OpenHands + Claude Sonnet 4.5 (scored 0.58 combined). No public Opus 4.6 results exist. |
| **Paper's limitations** | "Limited method and scenario coverage; limited agent scaffolds." Only 33 tasks. Does not cover the full diversity of real-world attack scenarios. |
| **Paper's relevance** | **HIGH.** This is one of three benchmarks the paper ran empirical experiments on. Central to their offensive evaluation. Results directly compared to human-assisted baselines (0.64). |

**Opus 4.6 opportunity:** The paper's agent scored 0.58 vs 0.64 human-assisted. Given Opus 4.6's superior agentic capabilities (38/40 wins on cybersec investigations), there's a reasonable chance it could match or exceed the human-assisted baseline. The benchmark is runnable and affordable.

---

### 2. CyberGym

- **What it measures:** PoC generation for real-world vulnerabilities across 1,507 tasks in 188 open-source projects
- **Paper's attack stage:** Step 2 (Weaponization) + Defense Step 3 (Triage/Forensics)
- **URL:** https://github.com/sunblaze-ucb/cybergym

| Dimension | Assessment |
|-----------|-----------|
| **Complexity** | **High.** Full dataset is ~10TB (Docker images with compilation environments). Binary-only mode is ~130GB. Requires Docker, Python, significant disk space. Subset of 10 tasks available for quick testing. |
| **Cost** | **High.** 1,507 tasks with large codebases. At Opus 4.6 pricing, a full run could cost $500-2,000+ depending on context usage per task. A 300-task subset (as the paper used) would be $100-600. |
| **Opus 4.6 status** | **YES — tested.** Opus 4.6 scored **66.6% pass@1** (up from Opus 4.5's 51.0% and Sonnet 4.5's 29.8%). Claude Mythos Preview later scored 83.1%. |
| **Paper's limitations** | "Agents lack program analysis tools for efficient code retrieval and automated security analysis." "Limited benchmarks on real-world complex systems." The paper notes agents struggle with large codebases. |
| **Paper's relevance** | **HIGH.** One of three benchmarks the paper ran experiments on. Central to their argument about defensive capability gaps. Their OpenHands-Def agent scored only 28.9% on a 300-case subset. |

**Opus 4.6 opportunity:** Already tested — 66.6% vs the paper's 28.9% with Sonnet 4.5. This is a **dramatic improvement** that directly challenges the paper's finding that agents struggle with defensive PoC generation. The 1M context window likely helps with large codebase analysis. Worth highlighting this result.

---

### 3. BountyBench

- **What it measures:** Real vulnerability exploitation AND patch generation on 25 complex real-world codebases (40 bug bounties covering 9/10 OWASP Top 10)
- **Paper's attack stage:** Step 2 (offensive) + Defense Steps 4-5 (remediation)
- **URL:** https://github.com/bountybench/bountybench

| Dimension | Assessment |
|-----------|-----------|
| **Complexity** | **Medium.** Docker-based. pip install + API keys. Well-structured CLI workflow runner. Requires Docker Desktop. 25 systems to test against. |
| **Cost** | **Medium.** Token costs tracked per task. With 40 bounties and Opus 4.6 pricing, estimate $200-500 for a full run. |
| **Opus 4.6 status** | **Not tested publicly.** Paper cites Claude 3.7 Sonnet at 67.5% success (offensive), and top agents at >90% (defensive/patching). No Opus 4.6 results found. |
| **Paper's limitations** | "Limited benchmarks on real-world complex systems." Language coverage constraints. |
| **Paper's relevance** | **HIGH.** Cited prominently for both offensive exploitation and defensive patching. One of the few benchmarks bridging attack and defense. |

**Opus 4.6 opportunity:** Strong candidate for testing. The offensive side (67.5% with 3.7 Sonnet) should improve significantly. The defensive patching side (>90% already) may be near ceiling. Most value is on the offensive exploitation tasks.

---

### 4. CVE-Bench

- **What it measures:** Agent performance exploiting known CVEs
- **Paper's attack stage:** Step 2 (Weaponization/Exploitation)

| Dimension | Assessment |
|-----------|-----------|
| **Complexity** | **Medium-High.** Requires setting up vulnerable software versions for specific CVEs. |
| **Cost** | **Medium.** Similar to BountyBench in per-task cost. |
| **Opus 4.6 status** | **Not tested.** Paper cites GPT-4o at 13% success rate. No Opus 4.6 results. |
| **Paper's limitations** | Limited scope detail provided. |
| **Paper's relevance** | **Medium.** Cited but not a primary benchmark in the empirical evaluation. |

---

### 5. RedCode

- **What it measures:** LLM capability to generate functional malware in Python
- **Paper's attack stage:** Step 2 (Weaponization/Malware Creation)

| Dimension | Assessment |
|-----------|-----------|
| **Complexity** | **Low-Medium.** Code generation benchmark — primarily API calls + output evaluation. |
| **Cost** | **Low.** Straightforward generation tasks. ~$10-50 at Opus pricing. |
| **Opus 4.6 status** | **Not tested.** |
| **Paper's limitations** | "Limited metric for malware creation, limited program language coverage." Python only. |
| **Paper's relevance** | **Low-Medium.** Cited as an early benchmark. Not central to the paper's argument. |

**Note:** Running this benchmark raises ethical considerations — it tests malware generation capability. Safety alignment testing (not capability maximization) would be the appropriate framing.

---

### 6. CySecBench

- **What it measures:** Safety alignment of LLMs against malware generation prompts
- **Paper's attack stage:** Step 2 (Weaponization — safety testing)

| Dimension | Assessment |
|-----------|-----------|
| **Complexity** | **Low.** Prompt-response evaluation. |
| **Cost** | **Low.** ~$10-30. |
| **Opus 4.6 status** | **Not tested.** Paper notes Claude 3.5 Sonnet was more resilient than GPT-4o and Gemini-1.5. |
| **Paper's limitations** | Limited scope to alignment testing only. |
| **Paper's relevance** | **Low.** Safety-focused, not capability-focused. |

---

### 7. CyberSecEval

- **What it measures:** Whether LLMs generate insecure code when completing coding tasks
- **Paper's attack stage:** Step 2 (Weaponization — insecure code generation)

| Dimension | Assessment |
|-----------|-----------|
| **Complexity** | **Low-Medium.** Meta's benchmark. Code completion + vulnerability scanning. |
| **Cost** | **Low-Medium.** $20-50 at Opus pricing. |
| **Opus 4.6 status** | **Not tested publicly on this specific benchmark.** |
| **Paper's limitations** | "Limited program language coverage." |
| **Paper's relevance** | **Medium.** Demonstrates that stronger models can paradoxically generate more vulnerable code. Interesting but not central. |

---

### 8. SecCodePLT

- **What it measures:** Project-level vulnerability detection and exploitation across C/C++, Java, Python. Also used for defense (patch generation).
- **Paper's attack stage:** Step 2 (attack) + Defense Steps 4-5 (remediation)

| Dimension | Assessment |
|-----------|-----------|
| **Complexity** | **Medium.** Multi-language setup. Requires fuzzing validation infrastructure. |
| **Cost** | **Medium.** $50-200 for full run. |
| **Opus 4.6 status** | **Not tested.** Paper reports agents achieve <30% on security-focused fuzzing validation. |
| **Paper's limitations** | "Limited benchmarks on real-world complex systems." "Limited benchmarks on vulnerabilities in different languages." |
| **Paper's relevance** | **Medium-High.** One of the few multi-language benchmarks. Cited for both attack and defense. The <30% defensive result is a key data point. |

**Opus 4.6 opportunity:** The <30% defensive score with previous models is a significant gap. Opus 4.6's improved code analysis could meaningfully improve this.

---

### 9. BaxBench & SecRepoBench

- **What they measure:** Insecure code generation at function and repository level
- **Paper's attack stage:** Step 2

| Dimension | Assessment |
|-----------|-----------|
| **Complexity** | **Low-Medium.** Code generation benchmarks. |
| **Cost** | **Low.** $10-30 each. |
| **Opus 4.6 status** | **Not tested.** |
| **Paper's limitations** | Language coverage constraints. Limited scope. |
| **Paper's relevance** | **Low.** Mentioned but not central to the argument. |

---

### 10. CTF Benchmarks (various)

- **What they measure:** Privilege escalation, exploit chains, capture-the-flag challenges
- **Paper's attack stage:** Steps 3-7 (Delivery through Action)

| Dimension | Assessment |
|-----------|-----------|
| **Complexity** | **Medium.** Varies by CTF platform. Docker-based setups common. |
| **Cost** | **Low-Medium.** Per-challenge costs vary. |
| **Opus 4.6 status** | **Not tested on the paper's specific CTF sets.** However, Opus 4.6 has saturated Cybench (100% pass@30 on its 35/40 CTF tasks). |
| **Paper's limitations** | "Limited attack category and type coverage." |
| **Paper's relevance** | **Medium.** Cited for showing commercial LLMs slightly outperform open-source. |

---

### DEFENSIVE BENCHMARKS

---

### 11. PatchAgent

- **What it measures:** End-to-end patch generation with functionality preservation validation
- **Paper's defense stage:** Steps 4-5 (Remediation)

| Dimension | Assessment |
|-----------|-----------|
| **Complexity** | **Medium.** Requires crash-triggering inputs and ground-truth tests. |
| **Cost** | **Medium.** $50-200 at Opus pricing. |
| **Opus 4.6 status** | **Not tested.** Paper's OpenHands-Def achieved 85% success, but notes >80% of patches only needed to modify functions in crash stack traces. |
| **Paper's limitations** | "Lacks ground truth tests; agent produces patches without validation tests." Difficulty is artificially reduced because root causes are usually in stack traces. |
| **Paper's relevance** | **HIGH.** One of three benchmarks the paper ran experiments on. Key to their defensive remediation analysis. |

**Opus 4.6 opportunity:** The 85% baseline is already high. The interesting question is the 5% of cases where root causes aren't in stack traces — Opus 4.6's deeper reasoning might help there.

---

### 12. SWE-bench (and variants: Java, multi-modal)

- **What it measures:** Automated software bug fixing
- **Paper's defense stage:** Steps 4-5 (Remediation)

| Dimension | Assessment |
|-----------|-----------|
| **Complexity** | **Medium.** Well-established benchmark with extensive tooling. Docker-based. |
| **Cost** | **Medium-High.** Full Verified subset is 500 tasks. At Opus pricing, $500-1,500. |
| **Opus 4.6 status** | **YES — tested.** Opus 4.6 scored **80.8% on SWE-bench Verified.** Claude Mythos Preview scored 93.9%. |
| **Paper's limitations** | "Noisy, no benchmark for security bugs." General bug fixing, not security-specific. "Limited benchmarks on vulnerabilities in different languages." |
| **Paper's relevance** | **Medium.** Cited as the primary remediation benchmark but explicitly noted as insufficient for security-specific patching. |

**Opus 4.6 opportunity:** Already tested and performing well (80.8%). However, the paper correctly notes this doesn't measure *security* bug fixing. The gap the paper identifies (security-specific remediation) remains unaddressed by SWE-bench alone.

---

### 13. Cybench

- **What it measures:** Professional-level CTF tasks for security capability assessment (40 tasks from 4 competitions)
- **Paper's defense stage:** Step 1 (Proactive Testing)
- **URL:** https://cybench.github.io/

| Dimension | Assessment |
|-----------|-----------|
| **Complexity** | **Medium.** Docker-based CTF environment. Well-documented. |
| **Cost** | **Low-Medium.** 40 tasks. ~$50-150 at Opus pricing. |
| **Opus 4.6 status** | **YES — saturated.** Opus 4.6 achieves ~100% pass@30. Anthropic notes they "can no longer use current benchmarks to track capability progression." |
| **Paper's limitations** | Limited system diversity. |
| **Paper's relevance** | **Medium.** Referenced as a proactive testing benchmark. |

**Opus 4.6 opportunity:** Already saturated — no further signal. This benchmark can no longer differentiate model capabilities.

---

### 14. PrimeVul

- **What it measures:** Function-level vulnerability detection
- **Paper's defense stage:** Step 1 (Proactive Testing/Vulnerability Detection)

| Dimension | Assessment |
|-----------|-----------|
| **Complexity** | **Low-Medium.** Code classification benchmark. |
| **Cost** | **Low.** $10-50. |
| **Opus 4.6 status** | **Not tested.** |
| **Paper's limitations** | "Low-quality labels due to missing context." Function-level only, misses cross-function vulnerabilities. |
| **Paper's relevance** | **Medium.** Cited as a key vulnerability detection benchmark despite label quality issues. |

---

### 15. FuzzBench / OSS-Fuzz

- **What they measure:** AI-enhanced fuzzing effectiveness / continuous fuzzing on open-source projects
- **Paper's defense stage:** Step 1 (Proactive Testing)

| Dimension | Assessment |
|-----------|-----------|
| **Complexity** | **High.** Requires fuzzing infrastructure, compilation environments, crash triage. OSS-Fuzz is Google-operated. |
| **Cost** | **High.** Significant compute for fuzzing campaigns (hours-days of CPU time per target, plus API costs). |
| **Opus 4.6 status** | **Not directly tested.** However, Opus 4.6 discovered 500+ zero-days during pre-release testing, suggesting strong fuzzing-adjacent capability. |
| **Paper's limitations** | FuzzBench: "Smaller but less noisy benchmark." OSS-Fuzz: "Large-scale, noisy data." |
| **Paper's relevance** | **Medium.** Important for the proactive testing narrative but not central to the empirical evaluation. |

---

### 16. IDS2018 / Drebin / BODMAS (Attack Detection)

- **What they measure:** Network intrusion detection / Android malware detection / general malware detection
- **Paper's defense stage:** Step 2 (Attack Detection)

| Dimension | Assessment |
|-----------|-----------|
| **Complexity** | **Medium.** Standard ML classification benchmarks. Require dataset access and evaluation pipelines. |
| **Cost** | **Low.** These are traditional ML benchmarks, not LLM-heavy. |
| **Opus 4.6 status** | **Not tested.** These are primarily traditional ML benchmarks, not well-suited to LLM evaluation. |
| **Paper's limitations** | "Low-quality data and labels, lack OOD/hidden tests." |
| **Paper's relevance** | **Low-Medium.** Cited to show the weakness of current attack detection benchmarks. Not about LLM capability per se. |

**Note:** These benchmarks are less relevant for Opus 4.6 evaluation since they're designed for traditional ML classifiers, not LLM agents.

---

### 17. CTIBench

- **What it measures:** Ability to pinpoint specific CVEs and attack techniques from threat intelligence
- **Paper's defense stage:** Step 2 (Attack Detection / Threat Intelligence)

| Dimension | Assessment |
|-----------|-----------|
| **Complexity** | **Low-Medium.** Knowledge-based evaluation. |
| **Cost** | **Low.** $10-30. |
| **Opus 4.6 status** | **Partially — related benchmark tested.** CTI-REALM (a newer threat intelligence benchmark) shows Opus 4.6 at 0.637 normalized reward, slightly ahead of Opus 4.5 (0.624). |
| **Paper's limitations** | Limited scope specification provided. |
| **Paper's relevance** | **Low-Medium.** Mentioned briefly. |

---

### 18. CRUXEval

- **What it measures:** PoC generation for C/C++ overflow bugs
- **Paper's defense stage:** Step 3 (Triage & Forensics)

| Dimension | Assessment |
|-----------|-----------|
| **Complexity** | **Low-Medium.** Code generation benchmark. |
| **Cost** | **Low.** $10-30. |
| **Opus 4.6 status** | **Not tested.** Paper cites GPT-4o at 75% pass@1. |
| **Paper's limitations** | "Low complexity, no benchmark for root cause." Focuses on simple overflow bugs only. |
| **Paper's relevance** | **Medium.** Cited for triage/forensics but noted as too simple. |

---

### 19. SVEN

- **What it measures:** Static vulnerability detection
- **Paper's defense stage:** Step 1 (Vulnerability Detection)

| Dimension | Assessment |
|-----------|-----------|
| **Complexity** | **Low.** Function-level code analysis. |
| **Cost** | **Low.** $10-30. |
| **Opus 4.6 status** | **Not tested.** |
| **Paper's limitations** | Function-level only; context limitations. |
| **Paper's relevance** | **Low.** Briefly mentioned. |

---

### 20. DafnyBench

- **What it measures:** LLM capability to generate verification hints for Dafny formal verifier
- **Paper's category:** Formal Verification

| Dimension | Assessment |
|-----------|-----------|
| **Complexity** | **Medium.** Requires Dafny toolchain. |
| **Cost** | **Low.** $10-50. |
| **Opus 4.6 status** | **Not tested.** |
| **Paper's limitations** | "Limited scope; verification-focused only." |
| **Paper's relevance** | **Low.** Mentioned peripherally for formal methods. |

---

### 21. SandboxEscapeBench *(from arXiv:2603.02277)*

- **What it measures:** LLM capability to escape container sandboxes (Docker/OCI). 18 scenarios across 3 layers: orchestration (4), engine/runtime (8), host/kernel (6). Difficulty levels 1-5, from simple misconfigurations to kernel exploits.
- **Category:** Offensive capability / AI safety infrastructure
- **URL:** https://arxiv.org/abs/2603.02277

| Dimension | Assessment |
|-----------|-----------|
| **Complexity** | **Medium.** Requires VM infrastructure (Vagrant/QEMU/VirtualBox/KVM or AWS EC2) with nested Docker containers. Uses Inspect AI framework. "Locally executable on commodity hardware." 18 scenarios — manageable scale. |
| **Cost** | **Low-Medium.** ~$1 per sample at current pricing. With 18 scenarios × 5 epochs = 90 runs, estimate $90-180 at Opus 4.6 pricing. Token budgets up to 2.5M tokens per sample tested. |
| **Opus 4.6 status** | **Not tested — Opus 4.5 was tested.** Opus 4.5 overall: 0.49 [0.39, 0.59]. Difficulty 3: 0.40 [0.26, 0.56]. Difficulty 4-5: 0.00. Tied with GPT-5 as top performer. |
| **Paper's limitations** | Focuses on container-to-host escapes only (not end-to-end compromise). Difficulty ratings are expert-estimated. Scenario coverage cannot exhaust all container deployments. "Relatively simple agentic architectures" tested — performance may increase with better scaffolding. |
| **Paper's relevance** | **HIGH (in its own paper).** This is the central and only benchmark of arXiv:2603.02277. It fills a gap not covered by arXiv:2504.05408 — no container escape benchmarks exist in the first paper's taxonomy. |

**Opus 4.6 opportunity:** This is a **high-priority** benchmark to run. Key reasons:

1. **Direct safety relevance:** AI agents (including Claude Code) run in containers. Understanding escape capability is critical for safe deployment.
2. **Opus 4.5 already top-tier:** At 0.49 overall, it tied GPT-5. Opus 4.6's improved reasoning and agentic capabilities could push into difficulty 4-5 scenarios where all models currently score 0%.
3. **Inference-time scaling signal:** The paper shows "approximately log-linear" scaling of success with compute budget. Opus 4.6's adaptive thinking could be a step change here.
4. **The difficulty 4-5 frontier:** Zero models succeed on kernel-level exploits (dirty_cow, dirty_pipe, bpf_privesc, CRI-O, kubectl_cp, packet_sock). These require multi-step exploitation pipelines and kernel-surface reasoning — exactly the kind of complex reasoning Opus 4.6 excels at.
5. **Affordable:** ~$90-180 for a full run. Very low barrier.

**Model results from the paper (overall success rate):**

| Model | Overall | Difficulty 1-2 | Difficulty 3 | Difficulty 4-5 |
|-------|---------|----------------|--------------|----------------|
| GPT-5 | ~0.49 | High | 0.40 | 0.00 |
| **Opus 4.5** | **0.49** | **High** | **0.40** | **0.00** |
| GPT-5.2 | Not reported separately | — | — | — |
| Sonnet 4.5 | Not reported separately | — | — | — |
| Haiku 4.5 | 0.18 | Moderate | Low | 0.00 |
| DeepSeek-R1 | Not reported separately | — | — | — |
| GPT-OSS-120B | 0.16 | Moderate | Low | 0.00 |

---

### Knowledge Q&A Benchmarks (CyberMetric, Cyberbench-knowledge, OCCULT)

- **Paper's note:** These are Q&A format benchmarks excluded from the paper's main analysis tables.

| Dimension | Assessment |
|-----------|-----------|
| **Complexity** | **Low.** Multiple-choice or short-answer. |
| **Cost** | **Very low.** $5-15 each. |
| **Opus 4.6 status** | **Not tested on these specific benchmarks.** |
| **Paper's limitations** | Q&A format; not task-based execution. |
| **Paper's relevance** | **Very low.** Explicitly excluded from main analysis. |

---

## Summary Matrix

| Benchmark | Complexity | Est. Cost (Opus 4.6) | Opus 4.6 Tested? | Paper Limitations | Paper Relevance |
|-----------|-----------|----------------------|-------------------|-------------------|-----------------|
| **AutoPenBench** | Medium-High | $50-100 | No | Limited scenarios/scaffolds | **HIGH** |
| **CyberGym** | High | $100-600 (subset) | **Yes: 66.6%** | Agents lack tools for large codebases | **HIGH** |
| **BountyBench** | Medium | $200-500 | No | Limited real-world systems | **HIGH** |
| **CVE-Bench** | Medium-High | $100-300 | No | Limited scope | Medium |
| **PatchAgent** | Medium | $50-200 | No | Lacks ground-truth validation | **HIGH** |
| **SWE-bench** | Medium | $500-1,500 | **Yes: 80.8%** | Not security-specific | Medium |
| **Cybench** | Medium | $50-150 | **Yes: saturated** | Limited diversity | Medium |
| **SecCodePLT** | Medium | $50-200 | No | Limited languages | Medium-High |
| **RedCode** | Low-Medium | $10-50 | No | Python only, limited metrics | Low-Medium |
| **CySecBench** | Low | $10-30 | No | Alignment only | Low |
| **CyberSecEval** | Low-Medium | $20-50 | No | Limited languages | Medium |
| **PrimeVul** | Low-Medium | $10-50 | No | Low-quality labels | Medium |
| **FuzzBench/OSS-Fuzz** | High | $200-1,000+ | No (but 500+ zero-days found) | Noisy data | Medium |
| **IDS2018/Drebin/BODMAS** | Medium | Low (not LLM-native) | No | Low-quality data/labels | Low-Medium |
| **CTIBench** | Low-Medium | $10-30 | Partial (CTI-REALM) | Limited scope | Low-Medium |
| **CRUXEval** | Low-Medium | $10-30 | No | Too simple, no root cause | Medium |
| **BaxBench/SecRepoBench** | Low-Medium | $10-30 | No | Limited scope | Low |
| **SVEN** | Low | $10-30 | No | Function-level only | Low |
| **DafnyBench** | Medium | $10-50 | No | Verification only | Low |
| **SandboxEscapeBench** | Medium | $90-180 | No (Opus 4.5: 0.49) | Container escapes only, simple agents | **HIGH** (paper 2) |
| **Knowledge Q&A** | Low | $5-15 | No | Not task-based | Very Low |

---

## Key Findings

### 1. Opus 4.6 already challenges the paper's central thesis

The paper's most striking defensive result was **28.9% on CyberGym** (PoC generation with OpenHands + Sonnet 4.5). Opus 4.6 scores **66.6%** — more than doubling this. This directly undermines the paper's claim that "current AI agents struggle with... complex security analysis." The model generation matters enormously.

### 2. Four high-value untested benchmarks

The best ROI for new Opus 4.6 evaluations would be:

1. **SandboxEscapeBench** — Cheapest ($90-180), highest safety relevance. Opus 4.5 scored 0.49 and 0.00 on difficulty 4-5. Can Opus 4.6 break the difficulty 4-5 barrier? Directly relevant to AI agent containment.
2. **AutoPenBench** — Affordable ($50-100), directly comparable to the paper's empirical results (0.58 with Sonnet 4.5 vs 0.64 human-assisted). Could Opus 4.6 exceed human-assisted performance?
3. **BountyBench** — Real-world codebases, covers both attack and defense. Medium cost ($200-500). The offensive exploitation side (67.5% with Claude 3.7 Sonnet) has clear room for improvement.
4. **SecCodePLT** — The <30% defensive fuzzing validation score is a key gap. Multi-language. Medium cost.

### 3. Several benchmarks are already saturated or irrelevant

- **Cybench** is saturated (100% pass@30) — no further signal possible.
- **IDS2018/Drebin/BODMAS** are traditional ML benchmarks, not well-suited for LLM evaluation.
- **Knowledge Q&A benchmarks** were excluded by the paper itself.
- **CRUXEval** is noted as too simple.

### 4. The paper's biggest gap remains unaddressed

The paper identifies **zero benchmarks for Remediation Deployment** (Defense Step 5). No model, including Opus 4.6, can be evaluated on this because the benchmark doesn't exist. This is flagged as "the most persistent hurdle in defense."

### 5. SandboxEscapeBench reveals an unexplored frontier

The second paper (Marchand et al.) shows all frontier models — including Opus 4.5 and GPT-5 — score **0% on difficulty 4-5 container escapes** (kernel exploits like dirty_cow, dirty_pipe, bpf_privesc). This is a clean, unsaturated frontier where Opus 4.6's improved reasoning could provide the first signal. The inference-time scaling relationship the paper identifies (log-linear) suggests Opus 4.6's adaptive thinking budget could be the key differentiator.

### 6. Cost is manageable for targeted evaluation

Running the four highest-priority benchmarks (SandboxEscapeBench + AutoPenBench + BountyBench + SecCodePLT) with Opus 4.6 would cost approximately **$400-1,000 total** in API costs, plus infrastructure setup time.

---

## Recommended Next Steps

1. **Run SandboxEscapeBench with Opus 4.6** — Cheapest benchmark (~$90-180), highest safety relevance. The 0% score at difficulty 4-5 is an unsaturated frontier. Uses Inspect AI framework (well-supported). Directly measures AI containment risk.
2. **Run AutoPenBench with Opus 4.6** — Low barrier, high signal. Directly comparable to the paper's empirical results. Can Opus 4.6 exceed human-assisted performance?
3. **Highlight the CyberGym result** — Opus 4.6's 66.6% vs the paper's 28.9% is already a powerful data point showing the paper's conclusions are model-generation-dependent.
4. **Run BountyBench offensive tasks** — Tests real-world vulnerability exploitation, the paper's area of highest concern.
5. **Consider the 1M context window** — Both papers identify complex multi-step reasoning as a key limitation. Opus 4.6's 1M context window and adaptive thinking are qualitative capability changes most benchmarks don't yet account for.

---

## Caveats

- **Agent scaffolding matters:** The paper used OpenHands. Results vary significantly by agent framework. Opus 4.6's native Claude Code agentic capabilities (9 subagents, 100+ tool calls) differ from the OpenHands harness.
- **Cost estimates are rough:** Based on extrapolation from the paper's Sonnet costs and Opus 4.6's ~10x higher pricing. Actual costs depend on context usage patterns.
- **Ethical considerations:** Several offensive benchmarks (RedCode, malware generation) should only be run with appropriate safety controls and for defensive research purposes.
- **Paper versions:** Analysis based on arXiv:2504.05408v4 and arXiv:2603.02277. Both papers may be updated.
- **SandboxEscapeBench tested simple agents:** The paper notes performance may increase with "persistent memory, access to web search, structured planners, or integrated developer tools" — Opus 4.6 in Claude Code provides all of these.

---

## Sources

- [Frontier AI's Impact on Cybersecurity (arXiv:2504.05408)](https://arxiv.org/abs/2504.05408)
- [Paper blog/summary](https://rdi.berkeley.edu/frontier-ai-impact-on-cybersecurity/)
- [Introducing Claude Opus 4.6](https://www.anthropic.com/news/claude-opus-4-6)
- [AutoPenBench GitHub](https://github.com/lucagioacchini/auto-pen-bench)
- [CyberGym GitHub](https://github.com/sunblaze-ucb/cybergym)
- [BountyBench GitHub](https://github.com/bountybench/bountybench)
- [Cybench](https://cybench.github.io/)
- [Claude Opus 4.6 Benchmark Analysis](https://claude5.ai/blog/claude-opus-46-benchmark-analysis)
- [Claude Benchmarks 2026](https://www.morphllm.com/claude-benchmarks)
- [Quantifying Frontier LLM Capabilities for Container Sandbox Escape (arXiv:2603.02277)](https://arxiv.org/abs/2603.02277)
