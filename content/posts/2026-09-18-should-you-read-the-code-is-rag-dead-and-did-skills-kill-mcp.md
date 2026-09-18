---
title: "Should you read the code, is RAG dead, and did Skills kill MCP?"
date: 2026-09-18
tags: ["GitHub", "Data & AI", "Agentic RAG", "Architecture", "AI Agents"]
categories: ["analysis"]
source_url: "https://github.blog/ai-and-ml/should-you-read-the-code-is-rag-dead-and-did-skills-kill-mcp/"
description: "We dive into these questions and other AI hot takes on the latest episode of the GitHub Podcast.
The post Should you read the code, is RAG dead, and did Skills kill MCP? appeared first on The GitHub B"
---

There's been an important development in the **Agentic RAG & Foundry IQ** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

Hot takes turn complicated topics into one confident sentence. That makes them great for engagement, but not necessarily for understanding.

At the surface level, they do not matter much. You agree, disagree, repost, argue for a few minutes, and move on. Sometimes the take is directionally right. Sometimes it is complete nonsense.

The value of hot takes is in what happens when you stop reacting and start pulling them apart. Under what conditions is this true? What context is missing? What assumptions does it make? What changes when you apply it to real work?

That is where the depth is. A good hot take gives you something sharp enough to question. The questions are where you find the useful ideas.

### Hot take #1: “You do not need to read AI-generated code”

Yes, you do. You are still responsible for the code.

But that does not mean every generated line needs the same level of attention.

A production authentication refactor deserves a different review process than a CSS experiment. A codebase you have maintained for 10 years steers your instincts differently than one you opened this morning. Pretending every change carries the same risk is not rigor. It is just a bad use of time.

A simple rule: review until you can explain and own the outcome.

### Hot take #2: “Companies will not hire you if you do not use AI”

The reality is a little more nuanced. More teams are asking candidates how they use AI. That makes sense. These tools are becoming part of software development.

But no one thinks every developer needs the same workflow, the same tools, or the same level of enthusiasm.

Can you explain when you use AI and when you work manually? Can you describe how you review generated code? Can you talk honestly about speed, quality, security, and maintainability? Can you change your process as the tools change?

If a company is building AI products or uses AI heavily in its engineering workflow, refusing to touch AI may make you a bad fit. That is not controversial. But total dependence and total refusal are rarely good answers.


## Key Takeaways

1. Hot takes turn complicated topics into one confident sentence.
2. At the surface level, they do not matter much.
3. The value of hot takes is in what happens when you stop reacting and start pulling them apart.
4. We explore all this and more in the latest episode of theGitHub Podcast!.
5. Not ready to dive in yet? Here are a few of the common AI hot takes we discussed and what we can get from them.


## Why This Matters

Traditional RAG is a static pipeline: query → retrieve → generate. Agentic RAG flips this — the agent decides *when* to retrieve, *what* to retrieve, and *how many steps* of retrieval to perform based on the complexity of the question. Foundry IQ (alongside Fabric IQ and Work IQ) provides the enterprise intelligence backbone that makes this context engineering practical at scale.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The shift from static RAG to **Agentic RAG** is architecturally significant. Three patterns define the new state of the art: **(1) Agent-driven retrieval planning** — instead of a fixed retrieval step, the agent evaluates query complexity and dynamically decides whether to do single-hop retrieval, multi-hop reasoning across documents, or decompose into parallel sub-queries. **(2) Foundry IQ as context layer** — a unified intelligence surface that combines knowledge indices, enterprise memory, and organizational graph into a single query plane that agents can access through standard tool interfaces. **(3) Context engineering over prompt engineering** — the focus shifts from crafting clever prompts to building robust knowledge pipelines that deliver the right context at the right time. What's technically compelling is how Foundry IQ integrates with Azure AI Search's agentic retrieval mode — the search service itself becomes an agent that can re-rank, filter, and synthesize across heterogeneous data sources. Combined with AI Citadel's governance controls, you get enterprise-grade knowledge access with full auditability.


## Business Translation

**For the C-Suite:** Agentic RAG with Foundry IQ transforms your enterprise knowledge from a cost center into a **revenue-generating intelligence asset**. Traditional search gives you documents; Agentic RAG gives you *answers grounded in your entire organizational memory*. The ROI case: **80-90% reduction in knowledge worker research time**, **3-5x improvement in decision quality** (measured by accuracy and completeness vs. manual research). Foundry IQ's enterprise intelligence layer means every AI agent you deploy gets smarter because it draws from the same organizational knowledge graph — creating compounding returns as your data and context grow. Organizations without this intelligence layer are building agents that operate in isolation, repeatedly solving problems your organization has already solved.


---

📖 **[Read the original article](https://github.blog/ai-and-ml/should-you-read-the-code-is-rag-dead-and-did-skills-kill-mcp/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
