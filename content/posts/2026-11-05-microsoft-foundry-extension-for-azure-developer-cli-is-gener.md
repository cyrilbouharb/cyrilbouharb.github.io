---
title: "Microsoft Foundry extension for Azure Developer CLI is generally available"
date: 2026-11-05
tags: ["Foundry", "GitHub", "OpenAI", "Agent Framework", "Data & AI", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/azure-sdk/microsoft-foundry-azure-developer-cli-ga/"
description: "Set up, test, evaluate, and deploy hosted agents with the generally available Microsoft Foundry extension for Azure Developer CLI, keeping agent and deployment configuration alongside your code.
The p"
---

There's been an important development in the **Azure OpenAI & GPT Models** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

Today, the Microsoft Foundry extension bundle (microsoft.foundry) for Azure Developer CLI (azd) reaches version 1.0 and is generally available.azdprovisions Azure resources and deploys application code; the Foundry extension adds agent setup and local testing. Agent and deployment configuration stays alongside your code inazure.yaml.

### What this adds to your development workflow

- Review agent and deployment changes together.

- Inspect local requests and responses in Agent Inspector while changing prompts, tools, or code.

- Use the same deployment configuration locally and in CI/CD.

### Create and run a hosted agent

In Foundry, ahosted agentruns your own agent code on managed compute. You choose the framework and orchestration logic; Foundry manages the runtime.

InstallAzure Developer CLI1.37.0 or later, or upgrade an existing installation withazd update. Install a currentuvrelease (uv self updatefor standalone installations). The sample uses Python 3.13 or later.

You’ll need an Azure subscription,Foundry permissions, and model quota in your selected region. Provisioned resources and model usage incur Azure charges.

```
azd auth login
azd ext install microsoft.foundry
```


## Key Takeaways

1. Today, the Microsoft Foundry extension bundle (microsoft.foundry) for Azure Developer CLI (azd) reaches version 1.0 and is generally available.azdprovisions Azure resources and deploys application code; the Foundry extension adds agent setup and local testing.
2. In Foundry, ahosted agentruns your own agent code on managed compute.
3. InstallAzure Developer CLI1.37.0 or later, or upgrade an existing installation withazd update.
4. You’ll need an Azure subscription,Foundry permissions, and model quota in your selected region.
5. If Azure CLI (az) is already signed in, use the same account and tenant asazd.


## Why This Matters

Access to frontier AI models through a trusted enterprise platform means organizations can innovate with the latest AI capabilities while meeting their compliance and data residency requirements. The model-as-a-service approach reduces the operational burden of running large-scale inference infrastructure.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

What's technically significant here goes beyond the headline model capabilities. The real engineering achievement is the **inference infrastructure**: provisioned throughput units (PTUs) that guarantee latency SLAs, global load balancing across regions, and the content filtering pipeline that operates at token-generation speed without perceptible latency impact. From a model architecture perspective, the trend toward reasoning models (o1, o3) vs. instruct models (GPT-4o) creates an interesting technical decision tree: reasoning models excel at multi-step problems but cost 5-10x more per token and have higher latency. The art is knowing when to route to which model class — and Azure's deployment flexibility (multiple model versions behind a single endpoint with traffic splitting) makes this A/B testing practical at enterprise scale.


## Business Translation

**For the C-Suite:** Azure OpenAI transforms the AI cost equation from 'build vs. buy' to 'compose and differentiate.' Instead of spending $50-200M training proprietary models, organizations access frontier capabilities at consumption-based pricing. The strategic advantage is **data sovereignty** — your prompts, fine-tuning data, and outputs never leave your Azure tenant, never train OpenAI's models, and comply with regional regulations (GDPR, HIPAA, FedRAMP). This isn't a vendor lock-in story — it's a risk mitigation strategy that lets you move fast while staying compliant.


---

📖 **[Read the original article](https://devblogs.microsoft.com/azure-sdk/microsoft-foundry-azure-developer-cli-ga/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
