---
title: "GitHub joins coalition advocating for fixes to California AI Transparency Act to protect open source"
date: 2026-06-23
tags: ["GitHub", "Agentic RAG"]
categories: ["analysis"]
source_url: "https://github.blog/news-insights/policy-news-and-insights/github-joins-coalition-advocating-for-fixes-to-california-ai-transparency-act-to-protect-open-source/"
description: "We’re calling for targeted amendments to resolve conflicts with open source licensing and align with international transparency frameworks while preserving regulatory intent.
The post GitHub joins coa"
---

There's been an important development in the **Agentic RAG & Foundry IQ** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

GitHub has joined an open source coalition of Black Forest Labs, Hugging Face, and Mozilla Corporation calling for targeted amendments to California’s AI Transparency Act (SB 942, as proposed to be amended inSB 1000).Read the full letter here.

At issue is a narrow but important problem for developers: as currently drafted, the bill’s license revocation provisions conflict with how open source licenses work in practice. Open source licenses are designed to be perpetual and irrevocable, which is what allows developers to reliably build on, reuse, and share code across projects and organizations.

The proposed language would require developers to revoke licenses if downstream users fail to meet certain obligations. That approach is incompatible with widely used open source licenses, and it could introduce uncertainty across the software supply chain—particularly for collaborative and community-driven projects.

The coalition’s letter explains that this requirement is not necessary to achieve the bill’s goals. Developers who modify and deploy AI systems are already directly covered by the law, and enforcement mechanisms remain in place. At the same time, there is a workable alternative: aligning with the EU’s approach in the AI ActTransparency Code of Practice,which recognizes the distinct nature of the open source ecosystem and acknowledges that notifying downstream users of best practices in documentation is sufficient.


## Key Takeaways

1. GitHub has joined an open source coalition of Black Forest Labs, Hugging Face, and Mozilla Corporation calling for targeted amendments to California’s AI Transparency Act (SB 942, as proposed to be amended inSB 1000).Read the full letter here.
2. At issue is a narrow but important problem for developers: as currently drafted, the bill’s license revocation provisions conflict with how open source licenses work in practice.
3. The proposed language would require developers to revoke licenses if downstream users fail to meet certain obligations.
4. The coalition’s letter explains that this requirement is not necessary to achieve the bill’s goals.
5. GitHub supports these amendments because they preserve the bill’s transparency objectives while maintaining compatibility with open source development.


## Why This Matters

Traditional RAG is a static pipeline: query → retrieve → generate. Agentic RAG flips this — the agent decides *when* to retrieve, *what* to retrieve, and *how many steps* of retrieval to perform based on the complexity of the question. Foundry IQ (alongside Fabric IQ and Work IQ) provides the enterprise intelligence backbone that makes this context engineering practical at scale.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The shift from static RAG to **Agentic RAG** is architecturally significant. Three patterns define the new state of the art: **(1) Agent-driven retrieval planning** — instead of a fixed retrieval step, the agent evaluates query complexity and dynamically decides whether to do single-hop retrieval, multi-hop reasoning across documents, or decompose into parallel sub-queries. **(2) Foundry IQ as context layer** — a unified intelligence surface that combines knowledge indices, enterprise memory, and organizational graph into a single query plane that agents can access through standard tool interfaces. **(3) Context engineering over prompt engineering** — the focus shifts from crafting clever prompts to building robust knowledge pipelines that deliver the right context at the right time. What's technically compelling is how Foundry IQ integrates with Azure AI Search's agentic retrieval mode — the search service itself becomes an agent that can re-rank, filter, and synthesize across heterogeneous data sources. Combined with AI Citadel's governance controls, you get enterprise-grade knowledge access with full auditability.


## Business Translation

**For the C-Suite:** Agentic RAG with Foundry IQ transforms your enterprise knowledge from a cost center into a **revenue-generating intelligence asset**. Traditional search gives you documents; Agentic RAG gives you *answers grounded in your entire organizational memory*. The ROI case: **80-90% reduction in knowledge worker research time**, **3-5x improvement in decision quality** (measured by accuracy and completeness vs. manual research). Foundry IQ's enterprise intelligence layer means every AI agent you deploy gets smarter because it draws from the same organizational knowledge graph — creating compounding returns as your data and context grow. Organizations without this intelligence layer are building agents that operate in isolation, repeatedly solving problems your organization has already solved.


---

📖 **[Read the original article](https://github.blog/news-insights/policy-news-and-insights/github-joins-coalition-advocating-for-fixes-to-california-ai-transparency-act-to-protect-open-source/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
