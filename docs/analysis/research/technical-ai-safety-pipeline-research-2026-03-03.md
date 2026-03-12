---
stepsCompleted: [1, 2, 3, 4, 5]
inputDocuments: ['docs/analysis/brainstorming-session-2026-02-12.md', 'docs/analysis/research/domain-ai-safety-open-problems-research-2026-03-02.md']
workflowType: 'research'
lastStep: 1
research_type: 'technical'
research_topic: 'Building the AI Safety research idea generation pipeline'
research_goals: 'Evaluate technology stack, architecture patterns, and implementation approaches for the 7-stage pipeline (Source, Generate, Filter/Score, Refine, Rank, Monitor, Learn)'
user_name: 'guido'
date: '2026-03-03'
web_research_enabled: true
source_verification: true
---

# Technical Research: AI Safety Research Idea Generation Pipeline

**Date:** 2026-03-03
**Author:** guido
**Research Type:** Technical Research
**Pipeline Context:** Informs architecture and implementation decisions for the 7-stage AI Safety research idea generation pipeline

---

## Executive Summary

This technical research evaluates the technology stack, architecture, and implementation approach for building the 7-stage AI Safety research idea generation pipeline designed in the brainstorming session (2026-02-12) and informed by the domain research (2026-03-02).

**Core Architecture Decision:** Claude Code as the orchestration layer with LiteLLM as the provider abstraction gateway. This is simpler than LangGraph or other agent frameworks, uses Claude Code's native capabilities (skills, MCP, subagents), and achieves full provider flexibility via LiteLLM's unified API across 100+ LLM providers.

**Key Technical Decisions:**

| Decision | Choice | Rationale |
|---|---|---|
| Orchestration | Claude Code skills | Native MCP, subagents, no framework overhead |
| Provider routing | LiteLLM Proxy | Swap Claude/OpenAI/Gemini/local; cost tracking; fallbacks |
| Tool protocol | MCP (FastMCP 3.0) | Industry standard; reusable across frameworks |
| Paper access | Semantic Scholar + ArXiv + OpenAlex via MCP servers | 225M+ papers; embeddings; existing MCP server to fork |
| Extraction | LangExtract (Tier 2+) | Source-grounded extraction; complements raw LLM prompting |
| Storage | SQLite → PostgreSQL + pgvector | Structured ideas + vector similarity in one system |
| Observability | LiteLLM built-in + Langfuse | Cost tracking + quality evaluation |
| Language | Python | Ecosystem alignment; no TypeScript needed for MVP |

**Cost Projection:** ~$0.27 per finished research idea using staged model tiering (70% savings vs. flat premium pricing). The staged evaluation funnel kills 60-70% of ideas at the cheapest tier.

**Implementation Timeline:** Tier 1 MVP in 3 weeks (Source → Generate → Filter/Score with one paper API). Full pipeline in 7+ weeks.

---

## Table of Contents

1. [Technical Research Scope Confirmation](#technical-research-scope-confirmation)
2. [Technology Stack Analysis](#technology-stack-analysis)
   - Programming Languages
   - LLM Agent Frameworks (revised: Claude Code + LiteLLM)
   - Model Context Protocol (MCP)
   - Academic Paper APIs and Data Sources
   - LLM Model Tiering and Cost Optimization
   - Database and Storage Technologies
   - Development Tools and Observability
   - Cloud Infrastructure and Deployment
   - Technology Adoption Trends
3. [Integration Patterns Analysis](#integration-patterns-analysis)
   - LiteLLM Proxy — Provider Abstraction Layer
   - MCP Server Integration (Semantic Scholar, ArXiv, OpenAlex, LessWrong)
   - LangExtract — Structured Paper Extraction
   - AiXiv — Future Source
   - Data Flow Between Pipeline Stages
   - Integration Security
4. [Architectural Patterns and Design](#architectural-patterns-and-design)
   - System Architecture: Claude Code Skills as Pipeline Stages
   - Orchestration: Sequential Pipeline with Subagent Parallelism
   - Staged Evaluation Funnel
   - Data Architecture: Idea Record Lifecycle
   - Deployment Architecture: Local-First
   - Security Architecture
5. [Implementation Approaches and Technology Adoption](#implementation-approaches-and-technology-adoption)
   - Implementation Strategy: Incremental MVP (3 Tiers)
   - Building Claude Code Skills: Practical Guide
   - Testing and Quality Assurance (LLM-as-Judge)
   - Cost Optimization and Resource Management
   - Risk Assessment and Mitigation
6. [Technical Research Recommendations](#technical-research-recommendations)
   - Recommended Technology Stack (Final)
   - Implementation Roadmap
   - Success Metrics
   - Skill Development Requirements

---

## Technical Research Scope Confirmation

**Research Topic:** Building the AI Safety research idea generation pipeline
**Research Goals:** Evaluate technology stack, architecture patterns, and implementation approaches for the 7-stage pipeline (Source, Generate, Filter/Score, Refine, Rank, Monitor, Learn)

**Technical Research Scope:**

- Architecture Analysis - system design for 7-stage pipeline, agent orchestration, modular stage design, data flow
- Implementation Approaches - LLM agent frameworks, subagent design, model tiering, token-efficient context management
- Technology Stack - languages, frameworks, tools for paper fetching, LLM APIs, persistent memory, collaborative chat
- Integration Patterns - APIs for academic sources, LLM providers, citation verification, monitoring/alerting
- Performance Considerations - token efficiency, cost optimization, staged filtering, context hygiene

**Research Methodology:**

- Current web data with rigorous source verification
- Multi-source validation for critical technical claims
- Confidence level framework for uncertain information
- Comprehensive technical coverage with architecture-specific insights

**Scope Confirmed:** 2026-03-03

---

## Technology Stack Analysis

### Programming Languages

**Python is the clear primary language for this pipeline.** The AI/ML ecosystem — LLM frameworks, paper fetching libraries, vector databases, agent orchestration — is overwhelmingly Python-first. Every major agent framework (LangGraph, CrewAI, AutoGen, Agno) ships Python SDKs as their primary interface. The Anthropic SDK, OpenAI SDK, and Google Generative AI SDK are all Python-first.

**TypeScript is the strongest alternative**, particularly for the collaborative chat interface layer. Vercel AI SDK is the most downloaded TypeScript AI framework, providing streaming-first primitives for building AI-powered UIs with React Server Components. Mastra is a TypeScript-native agent framework built for production, and Google's Agent Development Kit shipped a TypeScript version in December 2025. LangGraph.js has 529K weekly downloads despite only 2.3K GitHub stars, indicating significant production usage.

_Sources: [Top AI Agent Frameworks 2026 — Turing](https://www.turing.com/resources/ai-agent-frameworks), [TypeScript AI Agent Frameworks 2026](https://dev.to/ialijr/top-5-typescript-ai-agent-frameworks-you-should-know-in-2026-139c), [Mastra](https://mastra.ai/)_

**Recommendation for the pipeline:** Python for all backend pipeline logic (Source, Generate, Filter/Score, Refine, Rank, Monitor, Learn stages). TypeScript/React only if building a web-based collaborative chat interface. A Python-only stack is simpler and sufficient for an MVP. [High Confidence]

### LLM Agent Frameworks

The pipeline's 7-stage architecture with subagents, model tiering, and staged filtering maps directly to the capabilities of modern agent orchestration frameworks. The landscape has matured significantly in 2025.

**LangGraph** (LangChain ecosystem) — Graph-based state machine for controllable, branching agent workflows. LangGraph 1.0 shipped October 2025 (first stable release). Best for complex flows requiring precise control of routing logic. LangSmith provides best-in-class observability with traces for every LLM call, tool invocation, and chain step.
_Source: [LangChain vs CrewAI vs AutoGen](https://propelius.ai/blogs/langchain-vs-crewai-vs-autogen-ai-agent-frameworks/), [DataCamp Comparison](https://www.datacamp.com/tutorial/crewai-vs-langgraph-vs-autogen)_

**CrewAI** — Role-based multi-agent collaboration with a two-layer architecture: Crews (dynamic, role-based agent collaboration) and Flows (deterministic, event-driven task orchestration). Best for research + analysis + writing chains where a "team metaphor" fits naturally — which maps well to the pipeline's specialized stages.
_Source: [CrewAI Framework Review](https://latenode.com/blog/ai-frameworks-technical-infrastructure/crewai-framework/crewai-framework-2025-complete-review-of-the-open-source-multi-agent-ai-platform)_

**Microsoft Agent Framework** — Public preview October 2025. Merges AutoGen's dynamic multi-agent orchestration with Semantic Kernel's production foundations. Teams no longer need to choose between experimentation and production readiness. Supports Python and .NET.
_Source: [Microsoft Agent Framework](https://github.com/microsoft/agent-framework)_

**Anthropic Claude Agent SDK** — Handles MCP (Model Context Protocol) connections directly. Claude's directory includes 75+ connectors. Recent updates include Tool Search and Programmatic Tool Calling for production-scale MCP deployments.
_Source: [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/mcp), [Promptfoo Claude Agent SDK](https://www.promptfoo.dev/docs/providers/claude-agent-sdk/)_

**Agno** — Open-source Python framework with ready-made components: LLM interfaces, memory, knowledge retrieval, and tool integrations. Lightweight and modular.
_Source: [Agno](https://www.agno.com/agent-framework)_

**Framework Comparison for the Pipeline:**

| Feature | LangGraph | CrewAI | MS Agent Framework | Claude Agent SDK |
|---|---|---|---|---|
| Stage-as-node architecture | Excellent (graph-native) | Good (Flows) | Good | Limited |
| Model tiering (routing) | Built-in | Manual | Built-in | Manual |
| Observability | Best-in-class (LangSmith) | Requires external | Good | Limited |
| Human-in-the-loop | Strong | Strong | Strong | Strong |
| Production maturity | High (1.0 stable) | Medium | Medium (preview) | High |
| MCP support | Via integration | Via integration | Native | Native |

**Revised Recommendation — Claude Code + LiteLLM as Primary Architecture:**

After evaluating the pipeline's actual requirements against framework capabilities, the strongest architecture is **Claude Code as the orchestration layer with LiteLLM as the provider abstraction gateway**. The rationale:

1. The pipeline is fundamentally *sequential* (Source → Generate → Filter → ... → Learn), not a complex branching graph — LangGraph's graph engine is over-engineered for this use case
2. Claude Code provides native MCP integration, subagent capabilities, skills/workflows scaffolding, and tool use — all of which the pipeline needs
3. LiteLLM provides the missing piece: **provider-agnostic model routing**. It exposes a unified OpenAI-compatible API that translates to 100+ LLM providers, with built-in cost tracking, rate limiting, and load balancing
4. Claude Code has explicit, documented LiteLLM integration — configure via `ANTHROPIC_BASE_URL` pointing to the LiteLLM proxy

**LiteLLM** is an open-source proxy and SDK providing a single unified API to call 100+ LLM providers. It runs as a local proxy server and handles authentication, usage tracking, and cost controls. Claude Code can point at it via environment variables, and LiteLLM transparently routes to whatever provider/model is configured.
_Sources: [LiteLLM Docs](https://docs.litellm.ai/docs/), [Claude Code with LiteLLM](https://docs.litellm.ai/docs/tutorials/claude_non_anthropic_models), [Claude Code LLM Gateway Config](https://code.claude.com/docs/en/llm-gateway), [LiteLLM GitHub](https://github.com/BerriAI/litellm)_

**Resulting architecture:**

```
Claude Code (orchestration, skills, workflows, MCP, subagents)
    └─→ LiteLLM Proxy (model routing + provider abstraction + cost tracking)
         ├─→ Claude Haiku     (cheap stages: quick screen, dedup, classification)
         ├─→ Claude Sonnet    (mid stages: relevance scoring, generation)
         ├─→ Claude Opus      (complex stages: impact assessment, experiment design)
         ├─→ GPT-4o-mini      (alternative cheap tier)
         ├─→ Gemini Flash     (alternative mid tier)
         └─→ Ollama/local     (offline development, testing)
    └─→ MCP Servers (external tools)
         ├─→ Semantic Scholar  (paper search, citations, embeddings)
         ├─→ ArXiv             (preprint access)
         └─→ Web Search        (landscape scanning, verification)
```

This is simpler than LangGraph, leverages Claude Code's native capabilities without abstraction overhead, and achieves full provider flexibility via LiteLLM. LangGraph remains a viable alternative if the pipeline later requires complex parallel branching or if LangSmith observability is needed. [High Confidence]

### Model Context Protocol (MCP)

MCP has become the **de facto standard** for connecting AI systems to external tools and data sources, with adoption by Anthropic, OpenAI, Google DeepMind, and Microsoft. Key milestones:

- November 2024: Anthropic released MCP as open standard with Python and TypeScript SDKs
- March 2025: OpenAI adopted MCP across Agents SDK, Responses API, and ChatGPT
- April 2025: Google DeepMind confirmed MCP support for Gemini
- November 2025: Major spec updates — async operations, statelessness, server identity, community registry
- December 2025: Anthropic donated MCP to the Agentic AI Foundation (AAIF) under Linux Foundation
- Current: 97M+ monthly SDK downloads across Python and TypeScript

_Sources: [Anthropic MCP Announcement](https://www.anthropic.com/news/model-context-protocol), [Year of MCP Review](https://www.pento.ai/blog/a-year-of-mcp-2025-review), [MCP donated to AAIF](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)_

**Relevance to the pipeline:** MCP provides a standardized way for pipeline stages to connect to external tools — ArXiv fetching, Semantic Scholar queries, web search, citation verification — without building custom integrations for each. An MCP server for academic paper access could serve multiple pipeline stages. [High Confidence]

### Academic Paper APIs and Data Sources

The pipeline's Source stage needs programmatic access to academic literature. Two primary APIs are available:

**Semantic Scholar Academic Graph API** — REST API providing data on 225M+ papers, 100M+ authors, 650M+ paper-authorship edges, and 2.8B+ citation edges. Includes SPECTER2 embeddings (useful for semantic similarity search), recommendations engine, and bulk dataset downloads. Free unauthenticated access at 1000 req/s shared pool; authenticated API keys provide 1 RPS dedicated. Also offers a Recommendations API for finding similar papers.
_Sources: [Semantic Scholar API](https://api.semanticscholar.org/api-docs/), [Semantic Scholar API Product Page](https://www.semanticscholar.org/product/api)_

**ArXiv API** — Provides access to metadata for papers across physics, mathematics, computer science, and related fields. Available via direct API and wrapper libraries (e.g., `arxiv` Python package). ArXiv is the primary venue for AI Safety preprints.
_Source: [ArXiv API](https://apify.com/ryanclinton/arxiv-paper-search/api)_

**Additional sources for the pipeline:**
- **OpenAlex** — Open scholarly metadata (successor to Microsoft Academic Graph)
- **LessWrong / Alignment Forum APIs** — Community-specific content (may require scraping)
- **Semantic Scholar MCP Server** — A FastMCP server implementation already exists for Semantic Scholar API, providing access to paper data, author info, and citation networks directly via MCP
_Source: [Semantic Scholar MCP Server](https://github.com/zongmin-yu/semantic-scholar-fastmcp-mcp-server)_

**Recommendation:** Semantic Scholar as primary API (richer metadata, embeddings, citations, recommendations). ArXiv for preprint freshness. Use MCP servers to standardize tool access across pipeline stages. [High Confidence]

### LLM Model Tiering and Cost Optimization

The brainstorming session identified model tiering as critical: cheaper models for simple decisions, capable models for hard ones. The current pricing landscape makes this highly viable:

**Pricing tiers (2025-2026):**

| Tier | Models | Cost (per M tokens) | Pipeline Use |
|---|---|---|---|
| Premium | Claude Opus, GPT-4o, Gemini Ultra | $30-60 | Experiment design, impact assessment, complex refinement |
| Mid-tier | Claude Sonnet, GPT-4o | $10-15 | Relevance scoring, feasibility assessment, landscape scan |
| Lightweight | Claude Haiku, GPT-4o-mini | $0.50-2 | Quick screen, dedup, basic classification |
| Small/Open | Llama, Mistral, Gemma | $0.10-0.50 | Pattern matching, keyword extraction, formatting |

The cost difference between premium and lightweight models is **60-300x**. Running 80-95% of calls on cheap models with escalation to expensive models only for hard cases can reduce costs by 50-75%.

_Sources: [LLM Pricing Comparison 2026](https://www.cloudidr.com/blog/llm-pricing-comparison-2026), [LLM API Pricing 2025](https://intuitionlabs.ai/articles/llm-api-pricing-comparison-2025), [LLM Cost Optimization Guide](https://futureagi.com/blogs/llm-cost-optimization-2025)_

**Routing implementation:** Use a cheap model (e.g., Haiku / GPT-4o-mini) as a classifier to route each task to the appropriate tier. The router itself costs negligibly. LangGraph and Microsoft Agent Framework both have built-in model routing support.
_Source: [AI Model Router](https://www.mindstudio.ai/blog/what-is-ai-model-router-optimize-cost-llm-providers)_

**Mapping to pipeline stages:**

| Pipeline Stage | Model Tier | Rationale |
|---|---|---|
| Source (paper fetching) | No LLM needed | API calls, keyword filtering |
| Generate (one-liner hypotheses) | Mid-tier | Creative but constrained generation |
| Quick screen | Lightweight | Binary classification, dedup |
| Relevance check | Lightweight | Score against known criteria |
| Feasibility check | Lightweight | Simple rubric evaluation |
| Impact assessment | Mid-tier to Premium | Requires reasoning about causal chains |
| Landscape scan | Mid-tier | Web search + synthesis |
| Experiment design | Premium | Complex, creative reasoning |
| Refine/Iterate | Mid-tier to Premium | Depends on refinement type |
| Rank (Pareto) | Lightweight | Algorithmic, minimal LLM needed |
| Monitor | Lightweight | Change detection, classification |
| Learn | No LLM needed | Data aggregation, statistics |

[High Confidence — pricing verified against multiple sources; routing pattern well-established]

### Database and Storage Technologies

The pipeline needs several storage layers: persistent memory for learning, idea storage for the research corpus, and vector search for semantic similarity.

**Multi-layer storage architecture for AI agents (2025 best practice):**

1. **Short-term memory** — LLM context window (no separate storage needed)
2. **Semantic memory** — Vector database for similarity search across ideas, papers, and embeddings
3. **Structured state** — Relational or document database for idea records, scores, metadata, user feedback
4. **Artifact storage** — File system or object storage for generated reports and documents

_Sources: [Beyond Vector Databases](https://vardhmanandroid2015.medium.com/beyond-vector-databases-architectures-for-true-long-term-ai-memory-0d4629d1a006), [Best Database Solutions for AI Agents](https://fast.io/resources/best-database-solutions-ai-agents/)_

**PostgreSQL has emerged as the dominant choice** for GenAI applications in 2025, consolidating structured data + vector search (via pgvector) in a single database. Major investments: Snowflake acquired Crunchy Data ($250M), Databricks acquired Neon ($1B). For this pipeline, PostgreSQL + pgvector could handle both structured idea storage and vector similarity search in one system.
_Source: [VentureBeat — 6 Data Predictions for 2026](https://venturebeat.com/data/six-data-shifts-that-will-shape-enterprise-ai-in-2026)_

**Dedicated vector databases** (Qdrant, Pinecone, Weaviate, Chroma) offer better performance for high-volume similarity search but add operational complexity. Sub-100ms retrieval latency is achievable with in-memory indexes and SIMD-accelerated distance calculations.
_Source: [Vector Databases Guide](https://dev.to/klement_gunndu_e16216829c/vector-databases-guide-rag-applications-2025-55oj)_

**Agentic memory is evolving beyond RAG** — contextual memory (storing and adapting from feedback, maintaining state over time) is becoming table stakes for operational agentic AI in 2026. The pipeline's Learn stage (incorporating user feedback, tracking source quality, calibrating filters) requires this kind of adaptive memory, not just static retrieval.
_Source: [Top 10 AI Memory Products 2026](https://medium.com/@bumurzaqov2/top-10-ai-memory-products-2026-09d7900b5ab1)_

**Recommendation for the pipeline MVP:** SQLite or PostgreSQL for structured idea storage + scores + feedback. Chroma (embedded, zero-config) or pgvector for semantic similarity. Avoid dedicated vector database infrastructure until scale demands it. File-based persistent memory (JSON/YAML) for pipeline configuration and learning state — matches the brainstorming session's "persistent memory read at session start" design. [High Confidence]

### Development Tools and Observability

**Evaluation and observability platforms** are critical for validating that the pipeline produces good research ideas and for debugging quality issues.

**LangSmith** (LangChain) — Best-in-class for LangGraph workflows. Step-by-step traces for every LLM call, tool invocation, and chain step. Includes evaluation tools with automated testing and LLM-as-judge scoring.

**Braintrust** — Evaluation-first platform. Define datasets, run prompt variations, compare results side-by-side. Ideal for systematically iterating on prompts — directly useful for optimizing the pipeline's scoring rubrics.

**Langfuse** — Open-source alternative with production monitoring and evaluation. Self-hostable.

**Weave** (Weights & Biases) — Lightweight tracing and evaluation, integrates with W&B experiment tracking ecosystem.

_Sources: [Best AI Observability Platforms 2025 — Braintrust](https://www.braintrust.dev/articles/best-ai-observability-platforms-2025), [Best LLM Observability 2026](https://www.firecrawl.dev/blog/best-llm-observability-tools), [AI Observability Comparison](https://softcery.com/lab/top-8-observability-platforms-for-ai-agents-in-2025)_

**Recommendation:** With the Claude Code + LiteLLM architecture, LiteLLM itself provides cost tracking, usage logging, and per-model analytics out of the box. For deeper evaluation of scoring quality, Langfuse (open-source, self-hostable, has native LiteLLM integration) or Braintrust (evaluation-first approach matches the pipeline's need to validate scoring rubrics). LangSmith is only relevant if LangGraph is adopted later. [Medium-High Confidence]

_Source: [Langfuse + LiteLLM Integration](https://langfuse.com/integrations/gateways/litellm)_

### Cloud Infrastructure and Deployment

The pipeline does not need GPU compute — it calls LLM APIs, not runs models locally. This simplifies deployment significantly.

**Deployment options:**

| Option | Best For | Cost Model |
|---|---|---|
| **Simple server** (VPS, EC2, DigitalOcean) | MVP, single-user pipeline | Fixed monthly |
| **Serverless functions** (AWS Lambda, Cloud Functions) | Event-driven monitoring stage | Per-invocation |
| **Container** (Docker on any host) | Reproducible, portable deployment | Varies |
| **Modal** | If GPU needed for local models later | Per-second GPU billing |

_Sources: [Modal Alternatives](https://www.digitalocean.com/resources/articles/serverless-modal-alt), [ML Model Deployment Tools 2026](https://www.thirstysprout.com/post/machine-learning-model-deployment-tools)_

**Recommendation for the pipeline:** Start local (CLI tool or simple web server). The pipeline's primary costs are LLM API calls, not compute. A Docker container with scheduled cron jobs for the Monitor stage is sufficient for production. Only consider serverless or cloud hosting when deploying the collaborative chat interface for multiple users. [High Confidence]

### Technology Adoption Trends

**Key trends affecting the pipeline's technology choices:**

1. **MCP as universal tool protocol** — Build pipeline tools as MCP servers; they'll be reusable across any MCP-compatible agent framework. Future-proofs integration work.

2. **Model routing is becoming standard** — Teams running 80-95% on cheap models with smart escalation. The pipeline's staged filtering naturally maps to this pattern.

3. **PostgreSQL consolidation** — For projects that don't need massive vector scale, PostgreSQL + pgvector eliminates the need for separate vector and relational databases.

4. **Agentic memory > static RAG** — The pipeline's Learn stage needs adaptive memory that evolves from feedback, not just retrieval. This is a 2026 industry trend the pipeline should adopt from the start.

5. **Claude Code as agent runtime** — Claude Code's native scaffolding (skills, workflows, MCP servers, subagents) combined with LiteLLM for provider abstraction provides a simpler, more direct architecture than adding framework layers like LangGraph. LangGraph 1.0 remains a strong fallback if complex branching is needed later.

6. **Evaluation-first development** — Tools like Braintrust emphasize systematic evaluation before production deployment. Critical for validating the pipeline's scoring rubrics actually produce good ideas. Langfuse integrates natively with LiteLLM for observability in the recommended architecture.

---

## Integration Patterns Analysis

### LiteLLM Proxy — Provider Abstraction Layer

LiteLLM is the central integration hub in the recommended architecture, sitting between Claude Code and all LLM providers. Configuration is YAML-based with explicit model routing, fallback chains, and cost tracking.

**Configuration example for the pipeline:**

```yaml
model_list:
  # Cheap tier — quick screen, dedup, classification
  - model_name: cheap
    litellm_params:
      model: anthropic/claude-haiku-4-5-20251001
      api_key: os.environ/ANTHROPIC_API_KEY
  - model_name: cheap
    litellm_params:
      model: openai/gpt-4o-mini
      api_key: os.environ/OPENAI_API_KEY
    # fallback if Haiku is down

  # Mid tier — generation, relevance scoring
  - model_name: mid
    litellm_params:
      model: anthropic/claude-sonnet-4-6
      api_key: os.environ/ANTHROPIC_API_KEY
  - model_name: mid
    litellm_params:
      model: google/gemini-2.0-flash
      api_key: os.environ/GOOGLE_API_KEY

  # Premium tier — impact assessment, experiment design
  - model_name: premium
    litellm_params:
      model: anthropic/claude-opus-4-6
      api_key: os.environ/ANTHROPIC_API_KEY

router_settings:
  routing_strategy: "usage-based-routing-v2"
  enable_pre_call_checks: true
  allowed_fails: 3
  cooldown_time: 60

general_settings:
  master_key: os.environ/LITELLM_MASTER_KEY
```

**Key capabilities for the pipeline:**

- **Fallback routing:** If Claude Haiku is rate-limited, automatically falls back to GPT-4o-mini
- **Cost tracking:** Per-model, per-request cost logging with budget limits — critical for the pipeline's "kill bad ideas early and cheap" design
- **Retry policies:** Configurable retries for rate limits, timeouts, and authentication errors
- **Auto routing:** Can route based on input content, enabling automatic tier selection

_Sources: [LiteLLM Routing](https://docs.litellm.ai/docs/routing), [LiteLLM Config Settings](https://docs.litellm.ai/docs/proxy/config_settings), [LiteLLM Cost Tracking](https://www.statsig.com/perspectives/litellm-cost-tracking), [LiteLLM Auto Routing](https://docs.litellm.ai/docs/proxy/auto_routing)_

[High Confidence — documented, production-tested features]

### MCP Server Integration — External Tools

The pipeline needs custom MCP servers to expose academic paper access, web search, and citation verification as tools that Claude Code can use natively. FastMCP 3.0 (released January 2026) is the recommended framework.

**FastMCP overview:** Decorator-based tool registration with automatic protocol handling, error management, and built-in debugging via MCP Inspector. Reduces MCP server development time by ~5x compared to raw SDK.

_Sources: [FastMCP Tutorial](https://www.firecrawl.dev/blog/fastmcp-tutorial-building-mcp-servers-python), [FastMCP GitHub](https://github.com/jlowin/fastmcp), [MCP Build Server](https://modelcontextprotocol.io/docs/develop/build-server)_

**Pipeline MCP servers to build:**

#### 1. Semantic Scholar MCP Server

An existing FastMCP implementation already exists ([semantic-scholar-fastmcp-mcp-server](https://github.com/zongmin-yu/semantic-scholar-fastmcp-mcp-server)), providing paper search, author info, and citation networks. The pipeline can extend or fork this.

**API endpoints the server should expose as tools:**

| Tool | S2 API Endpoint | Pipeline Use |
|---|---|---|
| `search_papers` | `/paper/search` | Source stage: keyword search with category filters |
| `get_paper_details` | `/paper/{paper_id}` | Generate stage: fetch abstract + limitations sections |
| `get_citations` | `/paper/{id}/citations` | Landscape scan: who cites this? |
| `get_references` | `/paper/{id}/references` | Cross-pollination: what does this paper build on? |
| `get_paper_embeddings` | `/paper/{id}?fields=embedding` | Dedup: SPECTER2 similarity for idea deduplication |
| `recommend_papers` | `/recommendations/v1/papers` | Monitor stage: find similar papers to tracked ideas |

**Rate limits:** 1000 req/s unauthenticated (shared pool); 1 RPS with free API key (dedicated). For pipeline use, an API key is recommended.

_Sources: [Semantic Scholar API Docs](https://api.semanticscholar.org/api-docs/), [Semantic Scholar API Tutorial](https://www.semanticscholar.org/product/api/tutorial), [semanticscholar PyPI](https://pypi.org/project/semanticscholar/)_

#### 2. ArXiv MCP Server

No production MCP server exists yet — build one using FastMCP + the `arxiv` Python package.

**Tools to expose:**

| Tool | Pipeline Use |
|---|---|
| `search_recent_papers` | Monitor stage: daily/weekly scan of cs.AI, cs.LG, cs.CL for new safety-relevant papers |
| `get_paper_metadata` | Source stage: title, abstract, authors, categories, submission date |
| `bulk_search_category` | Source stage: initial corpus building for a research area |

**API constraints:** Max 30,000 results per query in slices of 2,000. 3-second delay between consecutive calls recommended. For bulk monitoring, ArXiv's OAI-PMH protocol is preferred for metadata harvesting (updated daily).

_Sources: [ArXiv API Manual](https://info.arxiv.org/help/api/user-manual.html), [arxiv.py PyPI](https://pypi.org/project/arxiv/), [ArXiv Bulk Data Access](https://info.arxiv.org/help/bulk_data.html)_

#### 3. OpenAlex MCP Server

**OpenAlex** indexes 240M+ works with ~50,000 added daily. Free API with $1/day budget (free key). Covers journals, conferences, preprint repositories, and institutional repositories. Broader coverage than Semantic Scholar for non-CS fields, and includes an explicit "API Guide for LLMs" in their docs.

**Tools to expose:**

| Tool | Pipeline Use |
|---|---|
| `search_works` | Cross-reference: verify Semantic Scholar results against independent source |
| `get_cited_by_count` | Scoring: citation-based impact estimation |
| `search_by_concept` | Source stage: discover papers by AI Safety-relevant concepts |

_Sources: [OpenAlex Docs](https://docs.openalex.org/), [OpenAlex API for LLMs](https://docs.openalex.org/api-guide-for-llms), [OpenAlex GitHub](https://github.com/ourresearch/OpenAlex)_

#### 4. LessWrong / Alignment Forum MCP Server

LessWrong and the Alignment Forum are critical sources for AI Safety discourse. Access options:

- **GraphQL API** — POST to `https://www.lesswrong.com/graphql` for structured post/comment data. Rate-limit conservatively.
- **RSS feeds** — Available for posts, comments, shortform, filterable by user, view type, and karma threshold. Good for the Monitor stage.
- **Scraping** — Allowed if user-agent is set to project name (not wget/curl) and rate-limited. Open-source scraping scripts exist ([ai-safety-scraping-scripts](https://github.com/smcaleese/ai-safety-scraping-scripts)).

**Recommended approach:** GraphQL API for structured queries (search by tag, author, karma); RSS feed for continuous monitoring of new posts.

_Sources: [LessWrong RSS Secrets](https://www.lesswrong.com/posts/dzF8vSdDtmWjCBBDr/secrets-of-the-lesswrong-rss-feed), [AI Safety Scraping Scripts](https://github.com/smcaleese/ai-safety-scraping-scripts), [LessWrong GraphQL](https://github.com/ForumMagnum/ForumMagnum)_

### Data Flow Between Pipeline Stages

The pipeline stages communicate through a shared data structure. Each idea flows through the pipeline as a structured record:

```
Idea Record:
  id: unique identifier
  source: {paper_id, source_type, url}
  one_liner: string (generated hypothesis)
  generation_method: enum (limitation_mining, gap_analysis, cross_pollination, ...)
  scores:
    relevance: 1-5
    feasibility: 1-5
    impact: 1-5
    landscape: 1-5
    experiment_design: 1-5
  stage: enum (generated, screened, scored, refined, ranked, archived)
  metadata:
    created_at, updated_at, killed_at
    kill_reason: string (if filtered out)
    refinement_history: list
    user_feedback: list
  cost_tracking:
    total_tokens: int
    total_cost: float
    per_stage_cost: dict
```

**Stage-to-stage communication pattern:** Each stage reads ideas at its input state, processes them, updates scores/metadata, and advances the stage field. Failed ideas get `killed_at` + `kill_reason` (for graveyard review). This is a simple database-backed pipeline, not a message queue — matching the brainstorming session's emphasis on simplicity.

### Integration Security

**API key management:** All API keys (Anthropic, OpenAI, Google, Semantic Scholar, OpenAlex) stored as environment variables, never in code or config files. LiteLLM's config.yaml references keys via `os.environ/KEY_NAME` syntax.

**Rate limiting:** LiteLLM handles LLM provider rate limits with automatic retry and cooldown. Academic API rate limits handled by MCP servers internally (exponential backoff).

**Data sensitivity:** The pipeline processes publicly available academic papers and generates research ideas — no PII or sensitive data. Citation URLs are public. The main security concern is API key leakage, handled by environment variable management.

### LangExtract — Structured Paper Extraction with Source Grounding

**LangExtract** is Google's open-source Python library for extracting structured information from unstructured text with precise source grounding — every extraction maps to its exact location in the source text.

_Sources: [LangExtract GitHub](https://github.com/google/langextract), [Google Blog Announcement](https://developers.googleblog.com/introducing-langextract-a-gemini-powered-information-extraction-library/), [KDnuggets Guide](https://www.kdnuggets.com/beginners-guide-to-data-extraction-with-langextract-and-llms)_

**Role in the pipeline:** LangExtract handles the *extraction* half of the Generate stage — mining limitations, pulling claims, identifying gaps from paper text — with verifiable source tracing. Raw LLM prompting (via LiteLLM) handles the *creative generation* half — cross-pollination, agenda decomposition, hypothesis creation — where reasoning and creativity are needed, not extraction.

**Two-step Generate pattern:**

1. **LangExtract** parses papers into structured records: `{limitations, methods, results, open_questions, key_claims}` — each field linked to its exact source sentence
2. **Raw LLM prompting** takes the structured extractions and generates one-liner project hypotheses via creative methods (cross-pollination, gap analysis, delta detection)

**Key capabilities:**

- **Source grounding** — directly addresses the brainstorming session's anti-hallucination safeguard: "every claim traces to a specific passage"
- **Schema enforcement** — consistent structured output via few-shot examples + controlled generation
- **High-throughput** — optimized chunking + parallel processing + multi-pass for higher recall across thousands of papers
- **Multi-model** — supports Gemini (native), OpenAI, and Ollama; compatible with LiteLLM routing
- **Interactive visualization** — HTML output for reviewing extractions in context

**Tradeoffs:** Adds a dependency; Gemini-optimized by default; for short texts (abstracts + limitation sections the pipeline already isolates), raw prompting is often sufficient. LangExtract's value scales with document length and audit requirements.

**Recommendation:** Start with raw prompting for the MVP (simpler, fewer dependencies). Add LangExtract when source grounding becomes a requirement — e.g., when ideas need to trace back to specific paper claims for review or publication. [High Confidence]

### AiXiv — Future Source (Monitor Only)

AiXiv is a new preprint server (University of Toronto, Oxford, Tsinghua) accepting AI-authored papers with 5-agent LLM review for novelty, soundness, and impact. Still early-stage (~dozens of papers). Not actionable as a source yet, but its multi-agent review architecture is conceptually similar to the pipeline's Filter/Score stage. Worth monitoring for future relevance.

_Source: [Science.org — AiXiv](https://www.science.org/content/article/new-preprint-server-welcomes-papers-written-and-reviewed-ai)_

---

## Architectural Patterns and Design

### System Architecture: Claude Code Skills as Pipeline Stages

The recommended architecture maps each pipeline stage to a **Claude Code custom skill**. Skills are reusable, filesystem-based markdown resources that provide Claude with domain-specific expertise — workflows, context, and best practices. When invoked, a skill loads its SKILL.md, expands it into detailed instructions, and modifies the execution context (allowed tools, model selection).

_Sources: [Claude Code Skills Docs](https://code.claude.com/docs/en/skills), [Claude Agent Skills Deep Dive](https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/), [Anthropic Skills Guide](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)_

**Pipeline-as-skills architecture:**

```
.claude/skills/
├── source/
│   └── SKILL.md          # Source stage: fetch papers via MCP servers
├── generate/
│   └── SKILL.md          # Generate stage: extraction + hypothesis creation
├── filter-score/
│   └── SKILL.md          # Filter/Score stage: staged evaluation funnel
├── refine/
│   └── SKILL.md          # Refine stage: auto-strengthen + human escalation
├── rank/
│   └── SKILL.md          # Rank stage: Pareto ranking + tiering
├── monitor/
│   └── SKILL.md          # Monitor stage: new paper detection + staleness
└── learn/
    └── SKILL.md          # Learn stage: feedback integration + calibration
```

Each skill's SKILL.md specifies:
- Which MCP servers to use (Semantic Scholar, ArXiv, etc.)
- Which model tier to request via LiteLLM (cheap/mid/premium)
- Input/output data formats (idea records)
- Stage-specific prompts and evaluation rubrics
- When to escalate to human-in-the-loop

**Why this pattern works:** Claude Code natively supports skill discovery, loading, and execution. Each stage is independently modifiable (matching the brainstorming session's modularity principle). No external orchestration framework needed — Claude Code IS the orchestrator.

### Orchestration Pattern: Sequential Pipeline with Subagent Parallelism

The pipeline follows a **sequential pipeline workflow** — the simplest and most production-proven agentic pattern. Ideas flow linearly through stages, with each stage having a defined role and clear contracts for input/output.

_Sources: [Azure AI Agent Design Patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns), [2026 Guide to Agentic Workflows](https://www.stack-ai.com/blog/the-2026-guide-to-agentic-workflow-architectures), [Agentic Design Patterns 2026](https://www.sitepoint.com/the-definitive-guide-to-agentic-design-patterns-in-2026/)_

**Within stages, subagent parallelism is used for throughput:**

- **Source stage:** Parallel MCP calls to Semantic Scholar, ArXiv, OpenAlex, LessWrong simultaneously
- **Generate stage:** Parallel LangExtract extractions across multiple papers; parallel hypothesis generation per paper
- **Filter/Score stage:** Parallel scoring of multiple ideas (each idea scored independently)
- **Monitor stage:** Parallel scans across all configured sources

Claude Code natively supports spawning 3-5 subagents in parallel, each using 3+ tools concurrently. This maps directly to the pipeline's need for parallel paper processing within each stage.

### Design Principle: Staged Evaluation Funnel

The core cost optimization pattern is the **staged evaluation funnel** — progressively more expensive evaluation stages, with cheap filters killing bad ideas early.

```
Source (free — API calls)
  │ 100% of papers pass
  ▼
Generate (mid-tier — ~$10/M tokens)
  │ Produces N one-liner hypotheses
  ▼
Quick Screen (cheap — ~$1/M tokens)
  │ 60-70% killed (duplicates, out-of-scope, already solved)
  ▼
Relevance Check (cheap — ~$1/M tokens)
  │ 30-40% killed (weak relevance score)
  ▼
Feasibility Check (cheap — ~$1/M tokens)
  │ 20-30% killed (too expensive, too complex)
  ▼
Impact Assessment (mid/premium — $10-60/M tokens)
  │ 10-20% killed (weak theory of impact)
  ▼
Landscape Scan (mid — $10/M tokens, web search costs)
  │ 5-10% killed (already being done, no org interest)
  ▼
Experiment Design (premium — $30-60/M tokens)
  │ Only top ideas reach this stage
  ▼
Output: Ranked, refined research project ideas
```

**Token cost optimization:** By killing 60-70% of ideas at the cheapest stage ($1/M tokens) and only sending the top 5-10% to the most expensive stage ($30-60/M tokens), the pipeline's average cost per idea is dominated by the cheap stages. This is the "kill bad ideas early and cheap" principle from the brainstorming session, implemented as an architectural pattern.

_Source: [LLM Cost Optimization Strategies](https://www.glukhov.org/post/2025/11/cost-effective-llm-applications/)_

**Additional token optimization techniques:**

- **Context hygiene:** Each stage gets only the information it needs. Quick screen gets the one-liner only. Impact assessment gets one-liner + source abstract. No full papers ever passed to any LLM.
- **Conversation history management:** Summarize earlier turns rather than replaying full dialogue threads — cuts thousands of tokens per session
- **Retrieval tightening:** Limit to 2-3 short chunks per retrieval rather than 4-8 long documents

### Data Architecture: Idea Record Lifecycle

Ideas are stored as structured records in a local database (SQLite for MVP, PostgreSQL for production). The record schema tracks the full lifecycle:

**States:** `generated` → `screened` → `scored` → `refined` → `ranked` → `archived` (or `killed` at any stage)

**Key design decisions:**

1. **Append-only scoring** — scores are never overwritten, only appended. Each scoring event records the model used, timestamp, and score. This enables filter calibration (the Learn stage can compare scores over time)
2. **Kill reason tracking** — every filtered idea records why it was killed and at which stage. Enables the "graveyard review" from the brainstorming session
3. **Cost per idea** — every LLM call logs tokens + cost against the idea ID. Enables monitoring of pipeline economics
4. **User feedback as first-class data** — feedback records are structured: `{idea_id, feedback_type, feedback_text, what_specifically_failed}`. This is the input to the Learn stage

### Deployment Architecture: Local-First with Optional Cloud

```
Local Development / Single User:
┌─────────────────────────────────────┐
│ Developer Machine                    │
│                                      │
│  Claude Code                         │
│    ├── Skills (pipeline stages)      │
│    ├── MCP Servers (local processes) │
│    └── LiteLLM Proxy (local)         │
│                                      │
│  SQLite (idea database)              │
│  File system (artifacts, memory)     │
└─────────────────────────────────────┘
         │ API calls
         ▼
  ┌──────────────┐
  │ LLM Providers │ (Claude, OpenAI, Gemini, Ollama)
  │ Academic APIs  │ (Semantic Scholar, ArXiv, OpenAlex)
  └──────────────┘
```

**For multi-user / scheduled monitoring:**

```
┌──────────────────────────────────────┐
│ Server (Docker container)             │
│                                       │
│  LiteLLM Proxy                        │
│  MCP Servers                          │
│  PostgreSQL + pgvector                │
│  Cron: Monitor stage (daily/weekly)   │
│  Web UI: Collaborative chat interface │
└──────────────────────────────────────┘
```

**Key architectural decision:** Start local-first. The pipeline is fundamentally a development tool, not a web service. Cloud deployment is only needed when: (a) scheduling automated monitoring, or (b) multiple users need the collaborative chat interface. This matches the brainstorming session's "start minimal, add complexity when validated" principle.

### Security Architecture

- **API keys:** Environment variables only, referenced via `os.environ/` in LiteLLM config
- **No PII:** Pipeline processes public academic data only
- **Dual-use awareness:** The pipeline generates AI Safety research ideas — some topics (adversarial attacks, capability elicitation) have dual-use dimensions. The pipeline should flag ideas with dual-use implications during the Filter/Score stage, matching the domain research's "dual-use filter" recommendation
- **LiteLLM access control:** Virtual keys can limit which models/budgets each user can access in multi-user deployment

---

## Implementation Approaches and Technology Adoption

### Implementation Strategy: Incremental MVP

The pipeline should be built incrementally, following the brainstorming session's 3-tier roadmap with the technical architecture decisions from this research. Each tier is independently useful — you don't need the full pipeline to start generating research ideas.

_Sources: [LLM Product Development 2025](https://orq.ai/blog/llm-product-development), [AI MVP Development](https://medium.com/@kyanon.digital/ai-mvp-development-how-to-build-launch-and-iterate-faster-743c6c9fe236)_

**Tier 1 MVP — Core Value (Weeks 1-3):**

| Component | Implementation | Dependencies |
|---|---|---|
| LiteLLM proxy | Install + configure `config.yaml` with 2-3 model tiers | API keys for Claude, optionally OpenAI |
| Semantic Scholar MCP server | Fork existing [FastMCP implementation](https://github.com/zongmin-yu/semantic-scholar-fastmcp-mcp-server); add `search_papers`, `get_paper_details` | FastMCP, S2 API key |
| Source skill | SKILL.md that uses S2 MCP server to fetch papers by keyword/category | MCP server running |
| Generate skill | SKILL.md with prompts for limitation mining + one-liner hypothesis generation | Source skill output |
| Filter/Score skill | SKILL.md with quick screen + relevance check prompts using cheap model tier | Generate skill output |
| SQLite database | Simple schema: ideas table with scores, stage, metadata | Python sqlite3 |
| Collaborative chat | Claude Code's native conversational interface — no separate UI needed | Claude Code |

**Tier 1 test:** Feed one recent AI Safety paper → generate 5-10 one-liner ideas → filter to top 3-5 → evaluate quality manually.

**Tier 2 — Quality and Trust (Weeks 4-6):**

| Component | Implementation | Dependencies |
|---|---|---|
| ArXiv MCP server | Build with FastMCP + `arxiv` Python package | FastMCP |
| LangExtract integration | Add structured extraction with source grounding to Generate skill | LangExtract library |
| Full scoring funnel | Add feasibility, impact, landscape stages to Filter/Score skill | Tier 1 working |
| Refine skill | Auto-strengthen weak scores; alternative framing generation | Scoring data |
| Langfuse observability | Connect via LiteLLM integration for cost tracking + quality monitoring | Langfuse account or self-host |
| LLM-as-judge evaluation | Validate scoring rubrics against human judgments | Test dataset of scored ideas |

**Tier 3 — Adaptive Intelligence (Weeks 7+):**

| Component | Implementation | Dependencies |
|---|---|---|
| Monitor skill | Cron-scheduled ArXiv + S2 scans for new papers matching relevance profile | ArXiv MCP server |
| Learn skill | Aggregate user feedback; track source quality; calibrate filter thresholds | User feedback data |
| LessWrong/AF MCP server | GraphQL API + RSS feed integration | FastMCP |
| OpenAlex MCP server | Cross-reference and citation verification | FastMCP |
| Rank skill | Pareto ranking + tier system (Tier 1: pursue now, Tier 2: promising, Tier 3: park) | Full scoring data |
| Graveyard review | Periodic resurface of killed ideas for human spot-check | Kill reason tracking |

### Building Claude Code Skills: Practical Guide

Each pipeline stage is a Claude Code custom skill. The skill structure:

```
.claude/skills/source/
├── SKILL.md              # Main instructions
├── templates/
│   └── paper-query.md    # Template for paper search queries
└── examples/
    └── sample-output.md  # Example of expected output format
```

**SKILL.md anatomy for a pipeline stage:**

```yaml
---
name: source
description: Fetch and filter AI Safety papers from academic sources
tools: [mcp__semantic_scholar__search_papers, mcp__arxiv__search_recent]
model: cheap  # Routes to Haiku/GPT-4o-mini via LiteLLM
---
```

```markdown
# Source Stage

You are the Source stage of the AI Safety research idea pipeline.

## Your Role
Fetch recent papers matching the relevance profile from configured
academic sources. Output structured paper records for the Generate stage.

## Tools Available
- `mcp__semantic_scholar__search_papers` — keyword search with category filters
- `mcp__arxiv__search_recent` — daily/weekly new paper scan

## Relevance Profile
[loaded from persistent config file]

## Output Format
For each paper, output:
- paper_id, title, authors, abstract, url
- relevance_score (1-5 based on keyword match + category)
- source (semantic_scholar | arxiv | openalex)
```

_Sources: [Claude Code Skills Docs](https://code.claude.com/docs/en/skills), [Building Skills Tutorial](https://www.codecademy.com/article/how-to-build-claude-skills), [Skills + MCP Guide](https://medium.com/@jageenshukla/build-production-ai-agents-with-claude-skills-mcp-882d70ffe9ee), [Anthropic Complete Guide](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)_

### Testing and Quality Assurance

The pipeline's output quality depends on its scoring rubrics. Testing must validate that rubrics produce good rankings, not just that code runs.

**LLM-as-judge evaluation pattern:**

Use a more capable model (e.g., Claude Opus) to evaluate the scoring decisions of cheaper models (e.g., Haiku). This validates whether the cheap model's relevance scores, feasibility scores, and impact scores correlate with expert judgment.

_Sources: [Agent Evaluation Framework 2026](https://galileo.ai/blog/agent-evaluation-framework-metrics-rubrics-benchmarks), [LLM-as-Judge Guide](https://www.evidentlyai.com/llm-guide/llm-as-a-judge), [LLM Rubric — Promptfoo](https://www.promptfoo.dev/docs/configuration/expected-outputs/model-graded/llm-rubric/)_

**Testing approach for the pipeline:**

| Test Type | What It Validates | How |
|---|---|---|
| **Gold set evaluation** | Do scoring rubrics produce correct rankings? | Manually score 20-30 ideas, compare against pipeline scores |
| **LLM-as-judge** | Do cheap model scores correlate with expensive model scores? | Score same ideas with Haiku and Opus, measure correlation |
| **Filter calibration** | Are good ideas being killed? Are bad ideas passing? | Track user overrides; compute false positive/negative rates |
| **Source quality** | Which sources produce the best-scoring ideas? | Track idea scores by source over time |
| **Cost per idea** | Is the staged funnel actually saving money? | Compare total cost vs. flat-rate (all ideas scored by premium model) |

**Key validation metric:** Spearman correlation between pipeline scores and human expert scores. Target 0.80+ for production deployment.

**Bias awareness:** LLM evaluators can have >50% error rates due to position bias (favoring earlier responses), length bias (preferring longer outputs), and agreeableness bias (over-accepting). Mitigate with explicit rubrics, few-shot examples, and structured JSON outputs requiring evidence before scoring.

### Cost Optimization and Resource Management

**Projected cost structure for the pipeline (per batch of 100 papers processed):**

| Stage | Model Tier | Est. Tokens | Est. Cost |
|---|---|---|---|
| Source | No LLM | 0 | $0 (API calls free) |
| Generate (100 papers × ~500 tokens each) | Mid ($10/M) | ~50K | ~$0.50 |
| Quick Screen (100 ideas × ~200 tokens) | Cheap ($1/M) | ~20K | ~$0.02 |
| Relevance (40 ideas × ~500 tokens) | Cheap ($1/M) | ~20K | ~$0.02 |
| Feasibility (25 ideas × ~500 tokens) | Cheap ($1/M) | ~12K | ~$0.01 |
| Impact (15 ideas × ~1000 tokens) | Mid ($10/M) | ~15K | ~$0.15 |
| Landscape (10 ideas × ~2000 tokens) | Mid ($10/M) | ~20K | ~$0.20 |
| Experiment Design (5 ideas × ~3000 tokens) | Premium ($30/M) | ~15K | ~$0.45 |
| **Total per batch** | | **~152K** | **~$1.35** |

**Cost per finished idea: ~$0.27** (assuming 5 ideas survive from 100 papers). Without model tiering (all premium): ~$4.56 per batch → $0.91 per idea. The staged funnel saves ~70%. [Medium Confidence — estimates based on current pricing; actual costs depend on prompt length and model selection]

### Risk Assessment and Mitigation

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| **API rate limiting** (S2, ArXiv) | Medium | Medium | Implement exponential backoff in MCP servers; cache paper metadata locally |
| **LLM API cost overrun** | Medium | Medium | LiteLLM budget limits per model; alert on daily spend thresholds |
| **Scoring rubric drift** | Medium | High | Regular gold set re-evaluation; user feedback loop in Learn stage |
| **Hallucinated paper references** | High | High | Citation verification: every paper must have verifiable S2 or ArXiv ID |
| **Relevance profile stale** | Medium | Medium | Monitor stage detects new trends; quarterly profile review |
| **Claude Code skill breaking changes** | Low | Medium | Pin Claude Code version; test skills after updates |
| **Provider API changes** | Low | Medium | LiteLLM abstracts providers; MCP servers isolate API-specific logic |

---

## Technical Research Recommendations

### Recommended Technology Stack (Final)

| Layer | Technology | Role |
|---|---|---|
| **Orchestration** | Claude Code | Pipeline execution, skill management, subagent parallelism |
| **Provider abstraction** | LiteLLM Proxy | Model routing, cost tracking, fallback, provider swapping |
| **Tool protocol** | MCP (FastMCP 3.0) | Standardized tool interface for all external integrations |
| **Paper access** | Semantic Scholar API, ArXiv API, OpenAlex API | Academic literature access via MCP servers |
| **Community access** | LessWrong GraphQL + RSS | AI Safety discourse monitoring |
| **Structured extraction** | LangExtract | Source-grounded paper extraction (Tier 2+) |
| **Database** | SQLite (MVP) → PostgreSQL + pgvector (production) | Idea records, scores, feedback, vector similarity |
| **Observability** | LiteLLM built-in + Langfuse | Cost tracking, quality monitoring, evaluation |
| **Language** | Python | All pipeline logic |
| **Deployment** | Local-first → Docker + cron (production) | No GPU needed; API-only workload |

### Implementation Roadmap

```
Week 1: Setup
  ├── Install LiteLLM, configure model tiers
  ├── Fork/build Semantic Scholar MCP server
  └── Create SQLite schema for idea records

Week 2: Core Skills
  ├── Build Source skill (paper fetching)
  ├── Build Generate skill (one-liner hypotheses)
  └── Build Filter/Score skill (quick screen + relevance)

Week 3: End-to-End Test
  ├── Run full pipeline on 5-10 recent AI Safety papers
  ├── Manually evaluate output quality
  └── Iterate on prompts and rubrics

Weeks 4-6: Quality Layer
  ├── Add ArXiv MCP server
  ├── Integrate LangExtract for source-grounded extraction
  ├── Build full scoring funnel (feasibility, impact, landscape)
  ├── Add Langfuse observability
  └── Build gold set + LLM-as-judge evaluation

Weeks 7+: Adaptive Layer
  ├── Build Monitor skill (scheduled paper scanning)
  ├── Build Learn skill (feedback integration)
  ├── Add LessWrong/AF + OpenAlex MCP servers
  ├── Implement Pareto ranking
  └── Deploy Docker + cron for automated monitoring
```

### Success Metrics

| Metric | Target | How Measured |
|---|---|---|
| **Scoring correlation** | 0.80+ Spearman vs. human expert | Gold set evaluation |
| **Cost per finished idea** | < $0.50 | LiteLLM cost tracking |
| **Ideas per batch** | 3-7 ranked ideas per 100 papers | Pipeline output counts |
| **False negative rate** | < 10% good ideas killed | User override tracking |
| **Source-to-idea latency** | < 5 minutes per paper batch | End-to-end timing |
| **Monitor freshness** | New papers detected within 24h of ArXiv publication | Monitor stage logs |

### Skill Development Requirements

**For a solo developer building this pipeline:**

- Python proficiency (intermediate+)
- Claude Code skill authoring (SKILL.md format, MCP integration)
- Basic SQL (SQLite schema, queries)
- API integration experience (REST, GraphQL)
- Prompt engineering (scoring rubrics, evaluation criteria)
- No ML/deep learning expertise required — the pipeline uses LLM APIs, not custom models

---

## Research Methodology and Sources

**Research Approach:** Systematic web search with source verification across technology stack, architecture patterns, integration approaches, and implementation strategies. All factual claims backed by URLs to public sources. Confidence levels noted where data is uncertain.

**Key Sources Referenced:**

- [Claude Code Skills Docs](https://code.claude.com/docs/en/skills)
- [LiteLLM Docs](https://docs.litellm.ai/docs/) | [Claude Code + LiteLLM](https://docs.litellm.ai/docs/tutorials/claude_non_anthropic_models)
- [FastMCP GitHub](https://github.com/jlowin/fastmcp) | [MCP Build Server](https://modelcontextprotocol.io/docs/develop/build-server)
- [Semantic Scholar API](https://api.semanticscholar.org/api-docs/) | [S2 MCP Server](https://github.com/zongmin-yu/semantic-scholar-fastmcp-mcp-server)
- [ArXiv API](https://info.arxiv.org/help/api/user-manual.html) | [OpenAlex API](https://docs.openalex.org/)
- [LangExtract GitHub](https://github.com/google/langextract)
- [Anthropic MCP Announcement](https://www.anthropic.com/news/model-context-protocol)
- [LLM Pricing Comparison 2026](https://www.cloudidr.com/blog/llm-pricing-comparison-2026)
- [Agent Evaluation Framework 2026](https://galileo.ai/blog/agent-evaluation-framework-metrics-rubrics-benchmarks)

**Research Completion Date:** 2026-03-03
**Source Verification:** All facts cited with URLs to public sources
**Confidence Level:** High — based on multiple authoritative, cross-verified sources

_This technical research document provides actionable architecture and implementation guidance for building the AI Safety research idea generation pipeline, complementing the brainstorming session (pipeline design) and domain research (landscape mapping)._
