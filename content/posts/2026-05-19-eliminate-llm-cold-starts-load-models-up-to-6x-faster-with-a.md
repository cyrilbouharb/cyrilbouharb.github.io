---
title: "Eliminate LLM Cold starts: Load models up to 6x Faster with Azure Blob Storage and Run:AI Model Streamer"
date: 2026-05-19
tags: ["LLM", "Data & AI", "Agentic RAG"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/azure-sdk/eliminate-llm-cold-starts-load-models-up-to-6x-faster-with-azure-blob-storage-and-runai-model-streamer/"
description: "Stop paying for idle GPUs while model weights copy to disk. Stream them straight into GPU memory instead with Run:AI Streamer from Azure Blob Storage. The Problem: Every Cold Start Costs You More Than"
---

There's been an important development in the **Agentic RAG & Foundry IQ** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

Stop paying for idle GPUs while model weights copy to disk. Stream them straight into GPU memory instead with Run:AI Streamer from Azure Blob Storage.

### The Problem: Every Cold Start Costs You More Than Money

GPU compute is among the most expensive cloud infrastructure, and every second a GPU is allocated but unavailable for serving is real money lost. The cost also goes beyond your Azure bill: slow cold starts can delay responses, stress SLAs, and degrade user experience during traffic spikes, when users need capacity most.

In many conventional inference deployments, a cold start triggered by auto-scaling, spot eviction, rolling deploy, restart, or model swap follows the same basic pattern: fetch model weights from object storage to local disk, then load them into GPU memory. In our tests, a 232.8 GiB model took roughly 3 to 5 minutes of allocated GPU capacity with the default vLLM loader, before the replica could serve requests.

Cold starts are not rare in production. Auto-scalers add replicas during spikes, spot VMs can be reclaimed, rolling deploys eventually touch every replica, and multi-tenant serving systems may swap models on demand. Each event can pay the same download-then-load tax unless the serving path is designed to avoid it.

While a large model is moving from object storage to local disk, then into GPU memory, several problems can stack up at once:

### Performance: Why Streaming Beats Downloading

Production autoscalers typically run on tens-of-seconds polling cadences, often once every 30 to 60 seconds (e.g.,KEDA,Hugging Face Inference Endpoints). A cold start that runs several minutes longer than those cycles leaves the autoscaler reacting to traffic that has already moved on, and the cascade from the previous section kicks in. Below are the numbers on aStandard_ND96isr_H100_v5VM (8x NVIDIA H100 80 GB, 80 Gbps network) streaming from a Premium block blob storage account in the same region.


## Key Takeaways

1. Stop paying for idle GPUs while model weights copy to disk.
2. GPU compute is among the most expensive cloud infrastructure, and every second a GPU is allocated but unavailable for serving is real money lost.
3. In many conventional inference deployments, a cold start triggered by auto-scaling, spot eviction, rolling deploy, restart, or model swap follows the same basic pattern: fetch model weights from object storage to local disk, then load them into GPU memory.
4. Cold starts are not rare in production.
5. While a large model is moving from object storage to local disk, then into GPU memory, several problems can stack up at once:.


## Why This Matters

Traditional RAG is a static pipeline: query → retrieve → generate. Agentic RAG flips this — the agent decides *when* to retrieve, *what* to retrieve, and *how many steps* of retrieval to perform based on the complexity of the question. Foundry IQ (alongside Fabric IQ and Work IQ) provides the enterprise intelligence backbone that makes this context engineering practical at scale.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The shift from static RAG to **Agentic RAG** is architecturally significant. Three patterns define the new state of the art: **(1) Agent-driven retrieval planning** — instead of a fixed retrieval step, the agent evaluates query complexity and dynamically decides whether to do single-hop retrieval, multi-hop reasoning across documents, or decompose into parallel sub-queries. **(2) Foundry IQ as context layer** — a unified intelligence surface that combines knowledge indices, enterprise memory, and organizational graph into a single query plane that agents can access through standard tool interfaces. **(3) Context engineering over prompt engineering** — the focus shifts from crafting clever prompts to building robust knowledge pipelines that deliver the right context at the right time. What's technically compelling is how Foundry IQ integrates with Azure AI Search's agentic retrieval mode — the search service itself becomes an agent that can re-rank, filter, and synthesize across heterogeneous data sources. Combined with AI Citadel's governance controls, you get enterprise-grade knowledge access with full auditability.


## Business Translation

**For the C-Suite:** Agentic RAG with Foundry IQ transforms your enterprise knowledge from a cost center into a **revenue-generating intelligence asset**. Traditional search gives you documents; Agentic RAG gives you *answers grounded in your entire organizational memory*. The ROI case: **80-90% reduction in knowledge worker research time**, **3-5x improvement in decision quality** (measured by accuracy and completeness vs. manual research). Foundry IQ's enterprise intelligence layer means every AI agent you deploy gets smarter because it draws from the same organizational knowledge graph — creating compounding returns as your data and context grow. Organizations without this intelligence layer are building agents that operate in isolation, repeatedly solving problems your organization has already solved.


---

📖 **[Read the original article](https://devblogs.microsoft.com/azure-sdk/eliminate-llm-cold-starts-load-models-up-to-6x-faster-with-azure-blob-storage-and-runai-model-streamer/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
