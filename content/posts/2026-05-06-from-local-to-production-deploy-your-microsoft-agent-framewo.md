---
title: "From Local to Production: Deploy Your Microsoft Agent Framework Agent with Foundry Hosted Agents"
date: 2026-05-06
tags: ["Foundry", "OpenAI", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/agent-framework/from-local-to-production-deploy-your-microsoft-agent-framework-agent-with-foundry-hosted-agents/"
description: "Once you have your Microsoft Agent Framework (MAF) agent or workflow happily running locally on your dev machine, it&#8217;s time to decide how to deploy your agent to production, monitor it, evaluate"
---

There's been an important development in the **Microsoft Foundry** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

Once you have your Microsoft Agent Framework (MAF) agent or workflow happily running locally on your dev machine, it’s time to decide how to deploy your agent to production, monitor it, evaluate it and version it. These decisions are just as important as getting the agent running.Hosted Agents in Foundry Agent Serviceis the easiest way to deploy Agent Framework agent to the cloud – with built-in identity, automatic scaling, managed session state, observability, and versioning.

### What are Foundry Hosted Agents?

Foundry Hosted Agents are containerized applications that run insideFoundry Agent Service. Foundry Hosted Agents brings agent-optimized compute and services designed for production-grade enterprise agents, giving agents secure per-session sandboxes with filesystem persistence, integrated identity, and scale-to-zero economics. They are your own code, packaged as a container image and deployed to Foundry-manage infrastructure.

- Predictable cold starts— spin up agent sessions and harnesses in your custom environment virtually instantly

- Scale to zero— pay nothing while your agent is idle, with an agent that will scale down on its own during inactivity

- Resume with filesystem intact— files, disk state, and session identity persist across scale-to-zero events. Your agent restarts with its full working directory exactly where it left off

### Choose your protocol: Responses or Invocations

Hosted agents speak one or both of two protocols:

- Responses: An OpenAI-compatible/responsesendpoint. The platform manages conversation history, streaming events, and background execution.

- Invocations: A genericinvocationsendpoint where you define the request/response schema, giving you flexibility for any non-conversational workflow that doesn’t fit a chat-shaped contract.

We recommend starting with `/responses` if you are not sure which one to use. Read more about supported protocols in thehere.


## Key Takeaways

1. Once you have your Microsoft Agent Framework (MAF) agent or workflow happily running locally on your dev machine, it’s time to decide how to deploy your agent to production, monitor it, evaluate it and version it.
2. Foundry Hosted Agents are containerized applications that run insideFoundry Agent Service.
3. When you deploy your MAF agent to Foundry Hosted Agents usingazdit:.
4. If unused, sessions persist for up to 30 days; idle compute is deprovisioned after 15 minutes and seamlessly restored on the next request. Read more about sessions in thehere.
5. We recommend starting with `/responses` if you are not sure which one to use.


## Why This Matters

For organizations building AI solutions, Foundry simplifies the journey from prototype to production. It removes the friction of stitching together multiple tools and provides guardrails for responsible AI deployment — which is critical when you're operating at enterprise scale.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

Working with enterprise customers, I see Foundry as a game-changer for teams that want to move fast with AI without sacrificing governance. The unified experience means less context-switching and more focus on the actual AI use case. What used to take weeks of infrastructure setup can now be prototyped in hours.

If you're exploring this area, my advice is to start small — pick one concrete use case, prototype it, and iterate. The tooling has matured significantly, and the barrier to entry has never been lower.


## Architecture Overview

{{< mermaid >}}
graph TB
    A[Data Sources] --> B[Ingestion Layer]
    B --> C[Processing & AI]
    C --> D[Model / Agent]
    D --> E[Application Layer]
    E --> F[End Users]

    style A fill:#0078d4,color:#fff
    style B fill:#50e6ff,color:#000
    style C fill:#7719aa,color:#fff
    style D fill:#00b294,color:#fff
    style E fill:#ffb900,color:#000
    style F fill:#0078d4,color:#fff
{{< /mermaid >}}

*High-level architecture — the specific implementation will vary based on your use case and scale requirements.*


---

📖 **[Read the original article](https://devblogs.microsoft.com/agent-framework/from-local-to-production-deploy-your-microsoft-agent-framework-agent-with-foundry-hosted-agents/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
