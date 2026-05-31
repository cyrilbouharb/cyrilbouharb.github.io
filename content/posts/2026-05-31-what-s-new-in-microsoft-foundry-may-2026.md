---
title: "What’s new in Microsoft Foundry | May 2026"
date: 2026-05-31
tags: ["Foundry", "GitHub", "OpenAI", "LLM", "Data & AI", "Agentic RAG", "Embeddings", "Responsible AI", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-may-2026/"
description: "May ships trace-based evaluation for any agent on any cloud, Grok 4.3 and DeepSeek V4 in the model catalog, GPT-5 Reinforcement Fine-Tuning at gated GA, three Microsoft Research on-device agent models"
---

There's been an important development in the **Azure OpenAI & GPT Models** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

### TL;DR

- Trace-based evaluation for external and hosted agents:Grade real production traces from Foundry, GCP, AWS, or any framework — no hand-curated datasets required.

- Grok 4.3:xAI’s latest model lands in Foundry for advanced agentic and domain-specific workloads.

- DeepSeek V4:DeepSeek’s newest model family expands open-model choice in the catalog.

- Fireworks AI — May update:DeepSeek V4 Pro and Kimi 2.6 arrive via Fireworks for high-performance open-model inference.

### Join the community

Connect with 50,000+ developers onDiscord, ask questions inGitHub Discussions, orsubscribe via RSSto get this digest monthly.

### Grok 4.3

Grok 4.3from xAI is available in the Microsoft Foundry model catalog. This is a step up from the Grok 4.2 GA that shipped in March — focused on advanced agentic workloads and domain-specific scenarios where you need a high-capability external model with Foundry’s production controls, safety tooling, and enterprise compliance.

If you’re already using Grok models in Foundry, 4.3 is a direct upgrade path through the same deployment flow.

One practical note before you move traffic: review the model card and run your own evaluations for your target use case. The catalog calls out additional responsible AI considerations for Grok 4.3, including higher safety and jailbreak risk than some other Azure Direct models. Treat that as a deployment checklist item, not a footnote.

Grok 4.3 uses the Chat Completions API path, so call the deployment directly. SetFOUNDRY_ENDPOINTto your deployment endpoint ending in/openai/v1/chat/completions, then trim that suffix for the OpenAI client base URL:


## Key Takeaways

1. Looking for Microsoft Foundry sessions to watch online? Start with these Microsoft Build breakout sessions.
2. Want the full online breakout catalogs? BrowseAgents & apps,Responsible AI, andWorking with models.
3. Connect with 50,000+ developers onDiscord, ask questions inGitHub Discussions, orsubscribe via RSSto get this digest monthly.
4. Grok 4.3from xAI is available in the Microsoft Foundry model catalog.
5. If you’re already using Grok models in Foundry, 4.3 is a direct upgrade path through the same deployment flow.


## Why This Matters

Access to frontier AI models through a trusted enterprise platform means organizations can innovate with the latest AI capabilities while meeting their compliance and data residency requirements. The model-as-a-service approach reduces the operational burden of running large-scale inference infrastructure.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

What's technically significant here goes beyond the headline model capabilities. The real engineering achievement is the **inference infrastructure**: provisioned throughput units (PTUs) that guarantee latency SLAs, global load balancing across regions, and the content filtering pipeline that operates at token-generation speed without perceptible latency impact. From a model architecture perspective, the trend toward reasoning models (o1, o3) vs. instruct models (GPT-4o) creates an interesting technical decision tree: reasoning models excel at multi-step problems but cost 5-10x more per token and have higher latency. The art is knowing when to route to which model class — and Azure's deployment flexibility (multiple model versions behind a single endpoint with traffic splitting) makes this A/B testing practical at enterprise scale.


## Business Translation

**For the C-Suite:** Azure OpenAI transforms the AI cost equation from 'build vs. buy' to 'compose and differentiate.' Instead of spending $50-200M training proprietary models, organizations access frontier capabilities at consumption-based pricing. The strategic advantage is **data sovereignty** — your prompts, fine-tuning data, and outputs never leave your Azure tenant, never train OpenAI's models, and comply with regional regulations (GDPR, HIPAA, FedRAMP). This isn't a vendor lock-in story — it's a risk mitigation strategy that lets you move fast while staying compliant.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-may-2026/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
