---
title: "Announcing Foundry Managed Compute: Run open models in Microsoft Foundry"
date: 2026-06-03
tags: ["Foundry", "Data & AI", "Agentic RAG", "Architecture"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/announcing-foundry-managed-compute/"
description: "Microsoft Foundry Managed Compute is a new GPU platform-as-a-service for hosting open-source and custom AI models behind the same endpoint, SDKs, and bill as frontier models.
The post Announcing Found"
---

There's been an important development in the **Microsoft Foundry** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

### Announcing Foundry Managed Compute: Run open models in Microsoft Foundry

Today we’re announcingManaged Compute in Microsoft Foundry, a new managed platform for customizing and serving open-source AI models on elastic GPU capacity without the operational burden of running virtual machines, Kubernetes clusters, or model runtimes. Managed Compute pulls together three things into one experience: the Foundry Model Catalog, the runtimes and frameworks that serve those models well, and the GPU capacity underneath. It’s open by design. You get access to thousands of open-source models through our Hugging Face partnership, you can customize them with supervised fine-tuning or reinforcement learning, and you can securely deploy model weights you trained somewhere else.

Together withpay-per-tokenfor the lowest-friction starting point, andprovisioned throughputfor predictable production load on frontier models, Managed Compute rounds out Microsoft Foundry as a single platform for serving AI models at scale: frontier, open-source, and custom, through one endpoint, one set of SDKs, and one bill.

### Where Managed Compute fits in Foundry

Foundry has three deployment types. Managed Compute is the one built for open-source and custom models on dedicated GPU capacity.

### Why open models, why now

Open-source AI has matured fast. The best open models now match frontier models on reasoning, coding, and instruction-following benchmarks. A newer generation of specialized small models is hitting state-of-the-art quality on focused tasks (document understanding, re-ranking, code completion, domain-specific chat) at a fraction of the cost and latency of general-purpose large models. The pattern across enterprises is consistent: teams reach for managed APIs to move fast on frontier intelligence, then bring in open and custom models for the routes where they want more control over behavior, customization, data residency, and cost.

What’s been missing is an easy way to run those open models in production. Today that usually means assembling a stack from scratch: procuring GPU VMs, standing up and operating Kubernetes, wiring networking and authentication, choosing and operating an inference runtime, hardening containers, patching CVEs, and building observability and billing attribution from the ground up. Even when a team can do all of that, the result often underutilizes expensive GPUs, lacks advanced serving patterns like disaggregated prefill and decode, and locks workloads to specific SKUs and regions that are slow and expensive to migrate. Managed Compute is built to lift that work off your team so the model, not the infrastructure, is what you spend your time on.


## Key Takeaways

1. Today we’re announcingManaged Compute in Microsoft Foundry, a new managed platform for customizing and serving open-source AI models on elastic GPU capacity without the operational burden of running virtual machines, Kubernetes clusters, or model runtimes.
2. Together withpay-per-tokenfor the lowest-friction starting point, andprovisioned throughputfor predictable production load on frontier models, Managed Compute rounds out Microsoft Foundry as a single platform for serving AI models at scale: frontier, open-source, and custom, through one endpoint, one set of SDKs, and one bill.
3. Foundry has three deployment types.
4. Open-source AI has matured fast.
5. What’s been missing is an easy way to run those open models in production.


## Why This Matters

For organizations building AI agents, Foundry simplifies the journey from prototype to production. It removes the friction of stitching together multiple tools and provides enterprise-grade governance through AI Citadel — policy-based controls, content filtering, and audit trails — which is critical when you're operating at public sector scale.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

From a technical standpoint, Foundry's architecture addresses what I consider the four hardest problems in enterprise AI: **model lifecycle management** (versioning, A/B testing, rollback across GPT-5.5, Claude, Gemma, and open-source models), **agent orchestration** (Foundry Agent Service with Microsoft Agent Framework for multi-agent systems), **evaluation at scale** (batch evaluations, continuous monitoring, custom evaluators, and the trace-to-dataset flywheel), and **governance without friction** via AI Citadel (policy-based guardrails, RBAC, content filtering, and audit trails baked into the agent lifecycle rather than bolted on after). The addition of Foundry IQ as the intelligence layer — providing context engineering capabilities so agents can access enterprise knowledge through agentic RAG — is what transforms Foundry from a development platform into an enterprise AI operating system.


## Business Translation

**For the C-Suite:** Foundry directly impacts three board-level concerns: **time-to-value** (reduces AI project timelines from 6-12 months to weeks by eliminating infrastructure setup), **risk management** (built-in responsible AI guardrails and compliance controls reduce regulatory exposure), and **cost predictability** (unified platform means consolidated billing, no sprawl of point solutions each with their own licensing). The competitive moat here is speed: organizations that can iterate on AI use cases 10x faster will capture market share while competitors are still in proof-of-concept.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/announcing-foundry-managed-compute/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
