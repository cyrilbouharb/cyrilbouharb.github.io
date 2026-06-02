---
title: "Foundry IQ: Build smarter agents faster with unified knowledge and serverless retrieval"
date: 2026-06-02
tags: ["Foundry", "Agent Framework", "Microsoft Fabric", "Data & AI", "Foundry IQ", "Agentic RAG", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/build-smarter-agents-faster-with-foundry-iq/"
description: "Learn how Foundry IQ helps developers ground agents with unified enterprise knowledge, serverless retrieval, improved agentic retrieval quality, and production-ready security.
The post Foundry IQ: Bui"
---

There's been an important development in the **Agentic RAG & Foundry IQ** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

### Foundry IQ: Build smarter agents faster with unified knowledge and serverless retrieval

Developers building agent fleets keep hitting the same pattern: the agent logic is ready, but the knowledge infrastructure underneath is complex to do well. Getting to production means solving for stability, scale, data access, answer quality, security, and content ingestion all at once. Today, we are enabling developers to have faster impact by simplifying the enterprise knowledge platform.

Your company’s IQ,powered by Microsoft IQ, is the collective intelligence locked in documents, emails, meetings, operational data, and the live web. This is where your true competitive edge lives. Foundry IQ grounds agents with the knowledge from these sources and continuously improves based on your business goals.

The announcements today are designed to help customers provision knowledge bases faster, unify enterprise and external sources, and expose that knowledge through the Foundry IQ Model Context Protocol (MCP) server for any agent framework or MCP-compatible hosts.

### What’s new

- Foundry IQ Serverless in preview:Provision instant, no-friction context retrieval with scale to zero pricing. Developer tier now available in public preview with more coming soon.Docs|Create a Foundry IQ resource

- New knowledge sources in preview:Ground agents across Work IQ, Fabric IQ (including Data agents and Ontology), File Search, Azure SQL, and MCP through a multi-source knowledge base, with no custom integrations required.Docs|Cookbook

- Web IQ in Foundry IQ is now available:Extend agent context to the web, honoring publisher preferences, and marketplace data with sub-165 ms latency and zero data retention.Blog|Website

- Foundry IQ knowledge bases are generally available:Ship production agents on a fully SLA-backed knowledge layer with stable APIs, compliance certifications, and the Foundry IQ MCP server for any MCP-compatible host.Docs|Quickstart

### Foundry IQ Serverless in public preview

We know agent workloads are bursty and event-driven: an agent might execute hundreds of steps in seconds, then go idle for hours. Serverless eliminates infrastructure friction: no clusters to manage, no capacity to reserve, no idle costs. Go from zero to production fast, with instant retrieval-augmented generation (RAG) and state-of-the-art retrieval quality built in.

Foundry IQ Serverless (Developer tier) is available in public preview. You are billed for compute resources and storage used, and the service scales to zero when idle.

Serverless tiers use Compute Units (CU) to measure resource consumption, including CPU utilization, memory and storage I/O. Usage is calculated each minute in increments of 0.25 CUs.

For large-scale serverless deployments,contact usfor additional options.


## Key Takeaways

1. Developers building agent fleets keep hitting the same pattern: the agent logic is ready, but the knowledge infrastructure underneath is complex to do well.
2. Your company’s IQ,powered by Microsoft IQ, is the collective intelligence locked in documents, emails, meetings, operational data, and the live web.
3. The announcements today are designed to help customers provision knowledge bases faster, unify enterprise and external sources, and expose that knowledge through the Foundry IQ Model Context Protocol (MCP) server for any agent framework or MCP-compatible hosts.
4. We know agent workloads are bursty and event-driven: an agent might execute hundreds of steps in seconds, then go idle for hours.
5. Foundry IQ Serverless (Developer tier) is available in public preview.


## Why This Matters

Traditional RAG is a static pipeline: query → retrieve → generate. Agentic RAG flips this — the agent decides *when* to retrieve, *what* to retrieve, and *how many steps* of retrieval to perform based on the complexity of the question. Foundry IQ (alongside Fabric IQ and Work IQ) provides the enterprise intelligence backbone that makes this context engineering practical at scale.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The shift from static RAG to **Agentic RAG** is architecturally significant. Three patterns define the new state of the art: **(1) Agent-driven retrieval planning** — instead of a fixed retrieval step, the agent evaluates query complexity and dynamically decides whether to do single-hop retrieval, multi-hop reasoning across documents, or decompose into parallel sub-queries. **(2) Foundry IQ as context layer** — a unified intelligence surface that combines knowledge indices, enterprise memory, and organizational graph into a single query plane that agents can access through standard tool interfaces. **(3) Context engineering over prompt engineering** — the focus shifts from crafting clever prompts to building robust knowledge pipelines that deliver the right context at the right time. What's technically compelling is how Foundry IQ integrates with Azure AI Search's agentic retrieval mode — the search service itself becomes an agent that can re-rank, filter, and synthesize across heterogeneous data sources. Combined with AI Citadel's governance controls, you get enterprise-grade knowledge access with full auditability.


## Business Translation

**For the C-Suite:** Agentic RAG with Foundry IQ transforms your enterprise knowledge from a cost center into a **revenue-generating intelligence asset**. Traditional search gives you documents; Agentic RAG gives you *answers grounded in your entire organizational memory*. The ROI case: **80-90% reduction in knowledge worker research time**, **3-5x improvement in decision quality** (measured by accuracy and completeness vs. manual research). Foundry IQ's enterprise intelligence layer means every AI agent you deploy gets smarter because it draws from the same organizational knowledge graph — creating compounding returns as your data and context grow. Organizations without this intelligence layer are building agents that operate in isolation, repeatedly solving problems your organization has already solved.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/build-smarter-agents-faster-with-foundry-iq/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
