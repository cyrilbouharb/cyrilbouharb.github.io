---
title: "Serve open models in production with Foundry Managed Compute"
date: 2026-11-20
tags: ["Foundry", "OpenAI", "Data & AI"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/managed-compute-ga/"
description: "Managed Compute serves open models on dedicated GPUs in Microsoft Foundry, with Global and US or EU Data Zone deployments.
The post Serve open models in production with Foundry Managed Compute appeare"
---

There's been an important development in the **Microsoft Foundry** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

We are excited to announce the general availability of Managed Compute in Microsoft Foundry. When weintroduced Managed Compute in previewat Microsoft Build in June, we set out to make serving open models as approachable as calling a managed model API. You choose the model that fits your application; we provision the GPUs, maintain the containers, and operate the serving runtime.

Since Build, we’ve scaled serving capacity, improved prompt reuse, and expanded GPU and deployment options, including US and EU Data Zones. Customer feedback helped us refine the experience and give teams a clearer view of how their deployments are running. We’ve also strengthened the software supply chain and added more open models to the catalog. The result is a managed platform for serving open models on dedicated GPUs in the Foundry experience you already use.

### Getting started with open models on Foundry Managed Compute

Sign into theFoundry portal, navigate to the model catalog and filter by “Managed Compute” under “Deployment options” to discover the 150+ open models available. Select a model, then choose a deployment template that fits your workload. The template defines the context length, serving runtime, and GPU configuration. Depending on the model, you can choose NVIDIA GPUs (A100, H100, or H200) or AMD MI300X GPUs. Start with one instance, review the hourly cost in the deployment wizard, and test a few prompts in the Playground once the deployment is ready.

Watch the Ignite breakout sessionFrom open weights to workload: Operationalizing at enterprise scale (BRK246)from the 8 minute mark to see a demo of how to get started with Foundry Managed Compute.

Serve open models in production with Foundry Managed ComputeWatch on YouTube

Here’s how to deployDeepSeek V4.1 Flash (1017)from Python. The example creates one billable instance on four MI300X GPUs. You’ll need a Foundry project, permission to deploy and call models, and enough Managed Compute GPU quota.

### Open models in the catalog

Since weopened the public previewin June 2026, we’ve expanded theHugging Face Collection in Foundryto150+ models for Managed Compute. Recent additions for reasoning and coding include DeepSeek V4.1 Flash (1017), Reflection Beam, and Meta’sMuse Spark Open. The NVIDIA Nemotron 3.5 family includes Embed and Rerank for search, Parse for extracting text, tables, and layout from documents, and Transcribe for speech. For structured decisions, the collection includes Laya Typed-Decisions from ConvAIInnovations.

> “Open models unlock incredible opportunities for enterprises to build their own AI with the flexibility and control they need. Through our partnership with Microsoft, we’re bringing that opportunity to life with Managed Compute in Microsoft Foundry, making secure, high-performance deployment of open models a one-click experience.”— Jeff Boudier, VP of Product, Hugging Face

“Open models unlock incredible opportunities for enterprises to build their own AI with the flexibility and control they need. Through our partnership with Microsoft, we’re bringing that opportunity to life with Managed Compute in Microsoft Foundry, making secure, high-performance deployment of open models a one-click experience.”

— Jeff Boudier, VP of Product, Hugging Face


## Key Takeaways

1. We are excited to announce the general availability of Managed Compute in Microsoft Foundry.
2. Since Build, we’ve scaled serving capacity, improved prompt reuse, and expanded GPU and deployment options, including US and EU Data Zones.
3. Sign into theFoundry portal, navigate to the model catalog and filter by “Managed Compute” under “Deployment options” to discover the 150+ open models available.
4. Watch the Ignite breakout sessionFrom open weights to workload: Operationalizing at enterprise scale (BRK246)from the 8 minute mark to see a demo of how to get started with Foundry Managed Compute.
5. Serve open models in production with Foundry Managed ComputeWatch on YouTube.


## Why This Matters

For organizations building AI agents, Foundry simplifies the journey from prototype to production. It removes the friction of stitching together multiple tools and provides enterprise-grade governance through AI Citadel — policy-based controls, content filtering, and audit trails — which is critical when you're operating at public sector scale.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

From a technical standpoint, Foundry's architecture addresses what I consider the four hardest problems in enterprise AI: **model lifecycle management** (versioning, A/B testing, rollback across GPT-5.5, Claude, Gemma, and open-source models), **agent orchestration** (Foundry Agent Service with Microsoft Agent Framework for multi-agent systems), **evaluation at scale** (batch evaluations, continuous monitoring, custom evaluators, and the trace-to-dataset flywheel), and **governance without friction** via AI Citadel (policy-based guardrails, RBAC, content filtering, and audit trails baked into the agent lifecycle rather than bolted on after). The addition of Foundry IQ as the intelligence layer — providing context engineering capabilities so agents can access enterprise knowledge through agentic RAG — is what transforms Foundry from a development platform into an enterprise AI operating system.


## Business Translation

**For the C-Suite:** Foundry directly impacts three board-level concerns: **time-to-value** (reduces AI project timelines from 6-12 months to weeks by eliminating infrastructure setup), **risk management** (built-in responsible AI guardrails and compliance controls reduce regulatory exposure), and **cost predictability** (unified platform means consolidated billing, no sprawl of point solutions each with their own licensing). The competitive moat here is speed: organizations that can iterate on AI use cases 10x faster will capture market share while competitors are still in proof-of-concept.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/managed-compute-ga/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
