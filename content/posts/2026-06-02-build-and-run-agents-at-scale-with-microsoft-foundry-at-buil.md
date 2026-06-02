---
title: "Build and run agents at scale with Microsoft Foundry at Build 2026"
date: 2026-06-02
tags: ["Foundry", "Copilot", "GitHub Copilot", "GitHub", "Agent Framework", "Data & AI", "Agentic RAG", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/agent-service-build2026/"
description: "Learn how Microsoft Foundry helps developers build, deploy, and operate production-ready agents with Agent Framework, Toolboxes, hosted agents, Microsoft 365 distribution, observability, and agent opt"
---

There's been an important development in the **AI Agents** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

Developers are already building agents, and the early productivity gains speak for themselves. Thanks to coding agents like GitHub Copilot, standing up a working prototype is the easy part.

The hard part starts after the prototype.The moment an agent leaves your laptop and has to run inside an enterprise workflow, the cracks show. Every tool and data source becomes its own integration, with a different auth flow, protocol, and lifecycle to maintain — and grounding the agent in enterprise knowledge means building a RAG pipeline from scratch. Running the agent in production is its own problem: you need isolation between sessions, durable state, and a runtime that can hold up under real load. And once it’s live, you can’t see what’s happening — traces stop at the agent boundary, evaluations are manual, and there’s no path from “this failed in prod” to “here’s a fixed version.” This is the same inflection point microservices hit a decade ago: a single service is easy; everything around it (discovery, isolation, observability, deployment) is where the real work lives. Agents are there now.

TheMicrosoft Agent Platformis built for that work — build in GitHub, run in Foundry, and reach users where they already are. At Build 2026, we’re shipping a connected platform in Microsoft Foundry across three layers:

- Build:Microsoft Agent Framework updates including the agent harness, skills support in Toolboxes in Foundry, procedural memory, and the Voice Live integration — so developers can stay in the IDE and frameworks they already use.

### Build: framework, tools, memory

Building agents today is no longer about getting a prototype to work — it’s about making the right architectural choices from the start.

### Framework: your harness

Production agents shouldn’t force a framework choice up front. Microsoft Foundry treats the agent harness as a flex point, not a lock-in: investments in LangGraph,GitHub Copilot SDK, or Claude Agent SDK carry forward. If you’re starting fresh,Microsoft Agent Frameworkis our opinionated, open-source agent framework, stable across Python and .NET. It unifies the enterprise foundations of Semantic Kernel with the multi-agent orchestration of AutoGen, so you no longer need to choose between them.The updates in Microsoft Agent Frameworkinclude:

- Agent harness with skills, memory, and middleware(stable release)

- Integrations with GitHub Copilot SDK and Claude Agent SDK(stable release)

- Multi-agent orchestration patterns including Magentic-One(stable release)


## Key Takeaways

1. Developers are already building agents, and the early productivity gains speak for themselves.
2. The hard part starts after the prototype.The moment an agent leaves your laptop and has to run inside an enterprise workflow, the cracks show.
3. TheMicrosoft Agent Platformis built for that work — build in GitHub, run in Foundry, and reach users where they already are.
4. Building agents today is no longer about getting a prototype to work — it’s about making the right architectural choices from the start.
5. Production agents shouldn’t force a framework choice up front.


## Why This Matters

Agentic AI is where the industry is heading. From code generation to customer service to data analysis, agents can handle multi-step workflows that previously required human intervention at every stage. This isn't just automation — it's a fundamentally new way of building software.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The technical frontier in AI agents right now is the **orchestration problem** — how do you reliably coordinate multiple specialized agents, each with different capabilities and knowledge, to solve complex tasks? The key architectural patterns emerging are: **handoff protocols** (A2A for cross-platform agent communication), **governance layers** (constraining agent actions within policy boundaries without killing autonomy), and **state management** (maintaining coherent context as work passes between agents). What I find most technically interesting is the convergence of **code-generating agents** (Copilot, Codex) with **tool-using agents** (function calling, MCP) — agents that can both write *and* execute code create a self-improving loop that's qualitatively different from static automation. The challenge is reliability: current agents succeed ~70-85% on complex tasks. Getting to 99%+ requires better evaluation frameworks, graceful degradation patterns, and human-in-the-loop checkpoints for high-stakes decisions.


## Business Translation

**For the C-Suite:** AI agents represent the next wave of operational leverage — not just automating tasks, but automating *judgment*. Early adopters are seeing **40-70% reduction in operational costs** for knowledge work (customer service, compliance review, data analysis). The strategic question isn't whether to adopt agents, but where to deploy them first for maximum ROI. The playbook: start with high-volume, medium-complexity workflows where errors are recoverable (customer inquiries, internal operations), then expand to higher-stakes domains as confidence grows. The organizations that build agent infrastructure now will have a 2-3 year head start when the technology matures.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/agent-service-build2026/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
