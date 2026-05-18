---
title: "What’s new in Microsoft Foundry | April 2026"
date: 2026-05-12
tags: ["Foundry", "GitHub", "OpenAI", "Data & AI", "Responsible AI", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-apr-2026/"
description: "April brings a wave of model arrivals — GPT-5.5, GPT-image-2, Microsoft first-party MAI models for image, voice, and transcription, Gemma 4, and Claude Opus 4.7 — alongside Foundry Local GA, Microsoft"
---

There's been an important development in the **Azure OpenAI & GPT Models** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

### TL;DR

- Foundry Local (generally available, GA):Local model inference is production-ready on Windows, macOS on Apple Silicon, and Linux x64.

- GPT-5.5:The latest GPT-5 family model is available in Microsoft Foundry, with default quota for Tier 5 and Tier 6 subscriptions.

- Microsoft Agent Framework tracing (Preview):Agent Framework agents can emit OpenTelemetry traces into Foundry for debugging and production observability.

- Hosted-agent tracing (Preview):Hosted-agent sessions, tool calls, and run steps can now surface in Foundry traces.

### Join the community

Connect with 50,000+ developers onDiscord, ask questions inGitHub Discussions, orsubscribe via RSSto get this digest monthly.

### GPT-5.5

GPT-5.5is now part of the Microsoft Foundry model lineup, but it is not broadly available by default. It has default quota only for Tier 5 and Tier 6 subscriptions. Tiers 1 through 4 currently show 0 requests per minute (RPM) and 0 tokens per minute (TPM) for GPT-5.5, so teams below Tier 5 should request quota before planning a deployment.

We know that can be frustrating if you are ready to test today. We plan to make GPT-5.5 available to more tiers as soon as demand and capacity allow. Thanks for being patient with us while we expand access responsibly.

Regional availability includes Global Standard deployments in East US 2, Sweden Central, South Central US, and Poland Central. Data Zone Standard deployments are available in those same regions.

To check your subscription tier, use theMicrosoft Cognitive Services quota tiers control plane APIand look forproperties.currentTierNamein the response. If you’re signed in with the Azure CLI, this command returns the current tier for a subscription:


## Key Takeaways

1. Looking for Microsoft Foundry sessions to watch online? Start with these Microsoft Build breakout sessions.
2. Want the full online breakout catalogs? BrowseAgents & apps,Responsible AI, andWorking with models.
3. Connect with 50,000+ developers onDiscord, ask questions inGitHub Discussions, orsubscribe via RSSto get this digest monthly.
4. GPT-5.5is now part of the Microsoft Foundry model lineup, but it is not broadly available by default.
5. We know that can be frustrating if you are ready to test today.


## Why This Matters

Access to frontier AI models through a trusted enterprise platform means organizations can innovate with the latest AI capabilities while meeting their compliance and data residency requirements. The model-as-a-service approach reduces the operational burden of running large-scale inference infrastructure.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

What's technically significant here goes beyond the headline model capabilities. The real engineering achievement is the **inference infrastructure**: provisioned throughput units (PTUs) that guarantee latency SLAs, global load balancing across regions, and the content filtering pipeline that operates at token-generation speed without perceptible latency impact. From a model architecture perspective, the trend toward reasoning models (o1, o3) vs. instruct models (GPT-4o) creates an interesting technical decision tree: reasoning models excel at multi-step problems but cost 5-10x more per token and have higher latency. The art is knowing when to route to which model class — and Azure's deployment flexibility (multiple model versions behind a single endpoint with traffic splitting) makes this A/B testing practical at enterprise scale.


## Business Translation

**For the C-Suite:** Azure OpenAI transforms the AI cost equation from 'build vs. buy' to 'compose and differentiate.' Instead of spending $50-200M training proprietary models, organizations access frontier capabilities at consumption-based pricing. The strategic advantage is **data sovereignty** — your prompts, fine-tuning data, and outputs never leave your Azure tenant, never train OpenAI's models, and comply with regional regulations (GDPR, HIPAA, FedRAMP). This isn't a vendor lock-in story — it's a risk mitigation strategy that lets you move fast while staying compliant.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-apr-2026/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
