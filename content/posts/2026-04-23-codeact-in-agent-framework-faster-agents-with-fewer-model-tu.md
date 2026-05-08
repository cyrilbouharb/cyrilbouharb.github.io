---
title: "CodeAct in Agent Framework: Faster Agents with Fewer Model Turns"
date: 2026-04-23
tags: ["Data & AI", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/"
description: "Modern AI agents often aren&#8217;t bottlenecked by model quality, they are bottlenecked by orchestration overhead. When an agent chains together many small tool calls, each step typically requires a "
---

There's been an important development in the **AI Agents** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

Modern AI agents often aren’t bottlenecked by model quality, they are bottlenecked by orchestration overhead. When an agent chains together many small tool calls, each step typically requires a new model turn, driving up latency and token usage.

With CodeAct support in Agent Framework, agents can collapse those multi-step plans into a single executable code block, cutting end-to-end latency by ~50% and token usage by over 60% in representative workloads, without compromising on safety or isolation. CodeAct ships in the newagent-framework-hyperlight(alpha) package, which runs the model-generated code in a fresh, locally isolatedHyperlightmicro-VM per call.

In this post, we walk through a concrete, realistic scenario where CodeAct provides meaningful gains: an agent task that involves many small, chainable tool calls (fetching data, performing light computation, assembling a result). Traditionally, this forces the agent into a loop of model → tool → model → tool interactions. Using CodeAct, the agent instead expresses the full plan as a short Python program that runs once in a sandboxed environment. The tools remain the same, the model remains the same, only the wiring changes. Later, we quantitatively compare both approaches on the same task to show where the latency and token savings come from, and more importantly, when those savings are worth pursuing in your own agents.

Concretely, wiring CodeAct into an agent looks like this. All later snippets build on it, reusing the same imports and theget_weathertool defined here:

### Why CodeAct

Modern agents are increasingly limited not by model quality, but by how much tool-calling overhead they incur. An agent that needs to read a table, filter it, multiply a few values, and summarize the result will typically burn four or five tool-call round trips, one per step, each one a separate request to the model.

TheCodeAct patterncollapses that loop. Instead of asking the model to choose a tool, wait for the result, and choose the next tool, we give the model a singleexecute_codetool and let it express the entire plan as a short Python program. Tools the agent would otherwise call directly are exposed inside the program ascall_tool(...). The model writes the code once, the sandbox runs it, and the agent gets back a single consolidated result.

Agents that do a lot of tool calling (data wrangling, light computation, chained lookups, report generation) benefit most. A five-step plan that used to be five model turns becomes oneexecute_codeturn containing a short Python script that calls the same tools viacall_tool(...). You save latency, you save tokens, and you keep the reasoning trace compact and auditable, because the full plan lives in a single code block instead of being scattered across several tool-call messages.

### How CodeAct works in Agent Framework

Theagent-framework-hyperlightpackage ships two entry points (HyperlightCodeActProviderandHyperlightExecuteCodeTool) plus typed helpers for file mounts and network policy. The sections below walk through both wirings, explain how approvals interact with sandboxed code, and show how to grant the sandbox controlled access to the host filesystem and network.


## Key Takeaways

1. Modern AI agents often aren’t bottlenecked by model quality, they are bottlenecked by orchestration overhead.
2. With CodeAct support in Agent Framework, agents can collapse those multi-step plans into a single executable code block, cutting end-to-end latency by ~50% and token usage by over 60% in representative workloads, without compromising on safety or isolation.
3. In this post, we walk through a concrete, realistic scenario where CodeAct provides meaningful gains: an agent task that involves many small, chainable tool calls (fetching data, performing light computation, assembling a result).
4. Concretely, wiring CodeAct into an agent looks like this.
5. Modern agents are increasingly limited not by model quality, but by how much tool-calling overhead they incur.


## Why This Matters

Agentic AI is where the industry is heading. From code generation to customer service to data analysis, agents can handle multi-step workflows that previously required human intervention at every stage. This isn't just automation — it's a fundamentally new way of building software.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The agent landscape is evolving rapidly. What excites me most is the convergence of multi-agent frameworks with enterprise tools — imagine agents that can not only reason but also execute across your entire technology stack. We're still early, but the trajectory is clear.

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

📖 **[Read the original article](https://devblogs.microsoft.com/agent-framework/codeact-with-hyperlight/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
