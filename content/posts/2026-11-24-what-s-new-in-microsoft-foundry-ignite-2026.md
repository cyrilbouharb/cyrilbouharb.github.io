---
title: "What’s new in Microsoft Foundry | Ignite 2026"
date: 2026-11-24
tags: ["Foundry", "LLM", "Data & AI", "Foundry IQ", "Agentic RAG", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-ignite-2026/"
description: "Microsoft Foundry Ignite 2026 updates for agents, developer tools, models, training, enterprise context, and governance, with continuous improvement.
The post What&#8217;s new in Microsoft Foundry | I"
---

There's been an important development in the **Agentic RAG & Foundry IQ** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

At Ignite, we added a more direct path from a recurring problem in your agent’s traces to a fix you can test. New preview capabilities connect Insights to Agent Optimizer, learn reusable skills from real conversations, and find cheaper configurations that still meet your quality bar. You decide which changes go into the next version.

### At a glance

- Continuous improvement:Insights and multi-turn evaluation are GA. Human annotation, rubric evaluators, and new Agent Optimizer capabilities are in preview.

- Agents:Voice agents, external-agent registration, hosted-agent egress controls, and the A2A tool are GA. Browser Automation adds enterprise features and previews.

- Developer tools:The Foundry Dev Pack and Foundry CLI (azd ai) are GA.

- Models:Microsoft-Decision-1.1 and Managed Compute are GA. Model router Auto, MAI image models, MAI-Code-2-Flash, fal video models, and Baseten are in preview.

### The continuous-improvement loop

For a broader view of the platform behind this loop, watchINV641. Jay Parikh and Arun Ulagaratchagan show how Microsoft IQ brings business context to agents and how to keep improving them as models evolve, with model choice and control intact.

What’s new in Microsoft Foundry | Ignite 2026Watch on YouTube

Establishwhat a good answer looks like.Identifya recurring failure in production traces.Optimizeby testing a candidate fix. Thenvalidate and repeat: compare the candidate with the version running today and decide whether to ship it. If you do, that version becomes the baseline for the next round. Agent Optimizer never changes a production agent automatically.

The rising curve illustrates cumulative quality gains from prompt optimization, model routing, skill optimization, fixes from Insights, and training. Source:Tina Schuchman’s Ignite announcement.


## Key Takeaways

1. At Ignite, we added a more direct path from a recurring problem in your agent’s traces to a fix you can test.
2. For a broader view of the platform behind this loop, watchINV641.
3. What’s new in Microsoft Foundry | Ignite 2026Watch on YouTube.
4. Establishwhat a good answer looks like.Identifya recurring failure in production traces.Optimizeby testing a candidate fix.
5. The rising curve illustrates cumulative quality gains from prompt optimization, model routing, skill optimization, fixes from Insights, and training.


## Why This Matters

Traditional RAG is a static pipeline: query → retrieve → generate. Agentic RAG flips this — the agent decides *when* to retrieve, *what* to retrieve, and *how many steps* of retrieval to perform based on the complexity of the question. Foundry IQ (alongside Fabric IQ and Work IQ) provides the enterprise intelligence backbone that makes this context engineering practical at scale.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The shift from static RAG to **Agentic RAG** is architecturally significant. Three patterns define the new state of the art: **(1) Agent-driven retrieval planning** — instead of a fixed retrieval step, the agent evaluates query complexity and dynamically decides whether to do single-hop retrieval, multi-hop reasoning across documents, or decompose into parallel sub-queries. **(2) Foundry IQ as context layer** — a unified intelligence surface that combines knowledge indices, enterprise memory, and organizational graph into a single query plane that agents can access through standard tool interfaces. **(3) Context engineering over prompt engineering** — the focus shifts from crafting clever prompts to building robust knowledge pipelines that deliver the right context at the right time. What's technically compelling is how Foundry IQ integrates with Azure AI Search's agentic retrieval mode — the search service itself becomes an agent that can re-rank, filter, and synthesize across heterogeneous data sources. Combined with AI Citadel's governance controls, you get enterprise-grade knowledge access with full auditability.


## Business Translation

**For the C-Suite:** Agentic RAG with Foundry IQ transforms your enterprise knowledge from a cost center into a **revenue-generating intelligence asset**. Traditional search gives you documents; Agentic RAG gives you *answers grounded in your entire organizational memory*. The ROI case: **80-90% reduction in knowledge worker research time**, **3-5x improvement in decision quality** (measured by accuracy and completeness vs. manual research). Foundry IQ's enterprise intelligence layer means every AI agent you deploy gets smarter because it draws from the same organizational knowledge graph — creating compounding returns as your data and context grow. Organizations without this intelligence layer are building agents that operate in isolation, repeatedly solving problems your organization has already solved.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-ignite-2026/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
