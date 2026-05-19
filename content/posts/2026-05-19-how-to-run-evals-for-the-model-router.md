---
title: "How to run evals for the model router"
date: 2026-05-19
tags: ["Foundry", "GitHub", "OpenAI", "LLM", "Data & AI"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/how-to-run-evals-for-model-router/"
description: "Walk through running quality, cost, and latency evaluations for the Foundry model router using an open-source GitHub repo designed for router-aware eval pipelines.
The post How to run evals for the mo"
---

There's been an important development in the **Azure OpenAI & GPT Models** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

One endpoint. Smarter spend. Model router in Foundry Models picks the optimal LLM for every prompt in real time based on signals like complexity, reasoning, and task type. Now with access to 28 frontier models, the model router makes model selection easier for developers and reduces manual overhead. This article walks you through how to run evaluations using a new open-source GitHub repo designed explicitly for the model router.Access the Eval Repo on GitHub

Before diving in, here are a few notes that developers should consider when building with the model router:

- The effective context window equals the smallest underlying model’s window. Oversized prompts only succeed if the router happens to pick a model that can handle them.

- Claude models require separate deployment before the router can route to them.

### Doesn’t Foundry already have benchmarks? What does this do?

Microsoft Foundry already provides enterprise-grade evaluations. Thisrepois an open-source alternative that can be used alongside Foundry’s benchmarking tools. It’s especially useful before you’re ready to operationalize and when you just need a fast, defensible answer on whether the model router belongs in your stack.

As a developer integrating the model router, you need hard answers to questions like:

Quality:On my prompts, does the model router’s auto-selected model match or beat the single model I’d otherwise pick?

Cost:Including the model router’s own input-prompt billing on top of underlying model costs, am I actually saving money end-to-end, or just shifting spend around?

### Quick preview (no API keys needed)

Just want to see what the output looks like before wiring anything up? Either openWALKTHROUGH.ipynbin Jupyter and clickRun All, or run the demo script:

```
# macOS / Linux
bash scripts/demo.sh

# Windows
.\scripts\demo.ps1
```

```
# macOS / Linux
bash scripts/demo.sh

# Windows
.\scripts\demo.ps1
```

This uses mock data, so you can preview the full dashboard before you’ve touched a single API key.


## Key Takeaways

1. Before diving in, here are a few notes that developers should consider when building with the model router:.
2. Microsoft Foundry already provides enterprise-grade evaluations.
3. As a developer integrating the model router, you need hard answers to questions like:.
4. Quality:On my prompts, does the model router’s auto-selected model match or beat the single model I’d otherwise pick?.
5. Cost:Including the model router’s own input-prompt billing on top of underlying model costs, am I actually saving money end-to-end, or just shifting spend around?.


## Why This Matters

Access to frontier AI models through a trusted enterprise platform means organizations can innovate with the latest AI capabilities while meeting their compliance and data residency requirements. The model-as-a-service approach reduces the operational burden of running large-scale inference infrastructure.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

What's technically significant here goes beyond the headline model capabilities. The real engineering achievement is the **inference infrastructure**: provisioned throughput units (PTUs) that guarantee latency SLAs, global load balancing across regions, and the content filtering pipeline that operates at token-generation speed without perceptible latency impact. From a model architecture perspective, the trend toward reasoning models (o1, o3) vs. instruct models (GPT-4o) creates an interesting technical decision tree: reasoning models excel at multi-step problems but cost 5-10x more per token and have higher latency. The art is knowing when to route to which model class — and Azure's deployment flexibility (multiple model versions behind a single endpoint with traffic splitting) makes this A/B testing practical at enterprise scale.


## Business Translation

**For the C-Suite:** Azure OpenAI transforms the AI cost equation from 'build vs. buy' to 'compose and differentiate.' Instead of spending $50-200M training proprietary models, organizations access frontier capabilities at consumption-based pricing. The strategic advantage is **data sovereignty** — your prompts, fine-tuning data, and outputs never leave your Azure tenant, never train OpenAI's models, and comply with regional regulations (GDPR, HIPAA, FedRAMP). This isn't a vendor lock-in story — it's a risk mitigation strategy that lets you move fast while staying compliant.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/how-to-run-evals-for-model-router/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
