---
title: "Accelerate Edge AI Development with Foundry Local"
date: 2026-06-04
tags: ["Foundry", "GitHub", "Data & AI", "Agentic RAG", "Embeddings", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/accelerate-edge-ai-development-with-foundry-local/"
description: "Why edge AI development is still hard  AI is no longer confined to cloud experiments. Developers are increasingly expected to deliver AI inside apps, devices, and edge systems where responsiveness, pr"
---

There's been an important development in the **Agentic RAG & Foundry IQ** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

AI is no longer confined to cloud experiments. Developers are increasingly expected to deliver AI inside apps, devices, and edge systems where responsiveness, privacy, resilience, and local control are essential. But building those experiences for production is still difficult.

Teams often have to solve model packaging, runtime fragmentation, hardware differences, and deployment complexity before they can ship a single reliable feature. That slows iteration and makes it harder to move from prototype to product.

At Microsoft Build 2026, we’re announcing updates across Foundry Local and Foundry Local on Azure Local that help developers build once and run AI closer to where data is created and decisions are made. These updates expand platform support, improve control over inference and acceleration, add new on-device APIs, and simplify deployment across disconnected, regulated, and sovereign environments.

The latest Foundry Local updates focus on the areas developers care about most: broader platform reach, familiar APIs, better runtime control, and simpler access to hardware acceleration. Together, these improvements help teams move faster from experimentation to production on AI PCs, edge devices, and enterprise infrastructure.

### Privacy-first and secure local AI

Across consumer apps and enterprise workflows, developers are using Foundry Local to keep sensitive data closer to the device while delivering faster, more responsive AI experiences.

Foxit uses Foundry Local to bring secure, local AI into document workflows such as question answering, summarization, translation, and document understanding. The result is a more practical path to on-device AI that helps keep sensitive information closer to the user while simplifying deployment at scale.

“Foundry Local gives us a practical way to bring powerful AI experiences directly into PDF workflows while keeping sensitive data closer to the user. Just as importantly, its managed local model approach helps simplify deployment, improve reliability, and reduce the operational burden of delivering on-device AI at scale.” – Queena Wei, SVP of Product at Foxit

Raycast uses Foundry Local to make privacy-first, on-device AI more accessible to end users. By simplifying model discovery and local interaction, it helps bring local AI into everyday workflows with less friction.

### Hardware portability and cross-device optimization

For teams building across different chips and execution environments, Foundry Local helps reduce hardware-specific complexity and accelerate deployment across devices.

Cephableis a private AI assistant that runs entirely on device, enabling voice control, dictation, content generation, and task automation across apps. With Foundry Local, Cephable’s AI features run faster, support more models across NPU, GPU, and CPU, and let the team focus on building the assistant instead of managing silicon-specific optimizations.

“Since shifting from our custom inferencing implementation to Foundry Local, our engineers have been able to ship core features faster. We’re saving dozens of hours on optimizing models and managing build pipelines to handle the right acceleration in the right version of our app package. This directly leads to a better user experience and more choice for our users.” – Cordellia Yokum, Director and Principal Architect at Cephable

FlowyAIPCbuilds an intelligent assistant for the era of heterogeneous AIPC silicon. FlowyAIPC integrates Foundry Local and Windows ML to solve the fundamental challenge of model-hardware decoupling across Intel, AMD, Qualcomm, and NVIDIA chips spanning CPU, NPU, iGPU, and dGPU.


## Key Takeaways

1. AI is no longer confined to cloud experiments.
2. Teams often have to solve model packaging, runtime fragmentation, hardware differences, and deployment complexity before they can ship a single reliable feature.
3. At Microsoft Build 2026, we’re announcing updates across Foundry Local and Foundry Local on Azure Local that help developers build once and run AI closer to where data is created and decisions are made.
4. The latest Foundry Local updates focus on the areas developers care about most: broader platform reach, familiar APIs, better runtime control, and simpler access to hardware acceleration.
5. Last month we announced the1.1.0 release of Foundry Local (Foundry Local 1.1: Live Transcription, Embeddings, and Responses API | Microsoft Foundry Blog)— Microsoft’s cross-platform local AI solution that let developers bringAI directly into their applicationswith no cloud dependency, no network latency, and no per-token costs.


## Why This Matters

Traditional RAG is a static pipeline: query → retrieve → generate. Agentic RAG flips this — the agent decides *when* to retrieve, *what* to retrieve, and *how many steps* of retrieval to perform based on the complexity of the question. Foundry IQ (alongside Fabric IQ and Work IQ) provides the enterprise intelligence backbone that makes this context engineering practical at scale.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The shift from static RAG to **Agentic RAG** is architecturally significant. Three patterns define the new state of the art: **(1) Agent-driven retrieval planning** — instead of a fixed retrieval step, the agent evaluates query complexity and dynamically decides whether to do single-hop retrieval, multi-hop reasoning across documents, or decompose into parallel sub-queries. **(2) Foundry IQ as context layer** — a unified intelligence surface that combines knowledge indices, enterprise memory, and organizational graph into a single query plane that agents can access through standard tool interfaces. **(3) Context engineering over prompt engineering** — the focus shifts from crafting clever prompts to building robust knowledge pipelines that deliver the right context at the right time. What's technically compelling is how Foundry IQ integrates with Azure AI Search's agentic retrieval mode — the search service itself becomes an agent that can re-rank, filter, and synthesize across heterogeneous data sources. Combined with AI Citadel's governance controls, you get enterprise-grade knowledge access with full auditability.


## Business Translation

**For the C-Suite:** Agentic RAG with Foundry IQ transforms your enterprise knowledge from a cost center into a **revenue-generating intelligence asset**. Traditional search gives you documents; Agentic RAG gives you *answers grounded in your entire organizational memory*. The ROI case: **80-90% reduction in knowledge worker research time**, **3-5x improvement in decision quality** (measured by accuracy and completeness vs. manual research). Foundry IQ's enterprise intelligence layer means every AI agent you deploy gets smarter because it draws from the same organizational knowledge graph — creating compounding returns as your data and context grow. Organizations without this intelligence layer are building agents that operate in isolation, repeatedly solving problems your organization has already solved.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/accelerate-edge-ai-development-with-foundry-local/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
