---
title: "Improving token efficiency in GitHub Agentic Workflows"
date: 2026-05-07
tags: ["Copilot", "GitHub", "LLM", "Data & AI", "Architecture", "AI Agents"]
categories: ["analysis"]
source_url: "https://github.blog/ai-and-ml/github-copilot/improving-token-efficiency-in-github-agentic-workflows/"
description: "Agentic workflows that run on every pull request can quietly accumulate large API bills. Here's how we instrumented our own production workflows, found the inefficiencies, and built agents to fix them"
---

There's been an important development in the **GitHub Copilot** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

GitHub Agentic Workflows is like a team of street sweepers that clean up little messes in your repo. These teams significantly improve repo hygiene and quality, but as with all agentic work, cost is a growing concern for developers. And because CI jobs like agentic workflows are automatically scheduled and triggered, costs can accumulate out of view.

Thankfully, making automations more efficient is easier than doing the same for interactive desktop sessions. Work done during a developer session can be hard to predict, but agentic workflows’ work is fully specified in YAML and repeats every execution.

Because we maintain and use GitHub Agentic Workflows in our own GitHub repositories, we worry about token efficiency as much as our users. That is why in April 2026, we began to systematically optimize the token usage of many of the workflows that we rely on every day. This post describes what we instrumented, the optimizations we applied, and our preliminary results.

### Logging token usage

We rely on hundreds of agentic workflows in our repos for maintenance and CI. All workflows run as GitHub Actions against real API rate limits. We are building the plane as we fly it and burning jet fuel as we go.

Before we could optimize our token consumption, we needed to know how tokens were consumed. The first challenge we faced was that each agent framework (Claude CLI, Copilot CLI, Codex CLI) emitted logs in a different format, and usage data could be incomplete for historical runs. Thankfully, the agentic-workflows security architecture uses an API proxy to prevent agents from directly accessing authentication credentials. This proxy gave us a way to capture token usage across all runs in a single normalized format, regardless of agent framework.

Every workflow now outputs atoken-usage.jsonlartifact with one record per API call that contains input tokens, output tokens, cache-read tokens, cache-write tokens, model, provider, and timestamps. Combining this data with the rest of the workflow’s logs gave a historical view of how tokens were typically spent and allowed us to optimize for future runs.

### Workflows optimizing workflows

With token data in hand, we built two daily optimization workflows.

ADaily Token Usage Auditorreads token usage artifacts from recent workflow runs, aggregates consumption by workflow, and posts a structured report. Its job is to flag any workflow that has significantly increased its recent usage, surface the most expensive workflows, and take note of anomalous runs (e.g., a workflow that normally completes in four LLM turns taking 18).

When an Auditor flags a workflow, a Daily Token Optimizer looks at the workflow’s source and recent logs to create a GitHub issue with describing concrete inefficiencies and proposing specific optimization. The Optimizer has found many inefficiencies that we would have otherwise missed.

Of course, the Auditor and Optimizer are agentic workflows themselves, and their token usage also appear in daily reports to create a small virtuous cycle.


## Key Takeaways

1. GitHub Agentic Workflows is like a team of street sweepers that clean up little messes in your repo.
2. Thankfully, making automations more efficient is easier than doing the same for interactive desktop sessions.
3. Because we maintain and use GitHub Agentic Workflows in our own GitHub repositories, we worry about token efficiency as much as our users.
4. We rely on hundreds of agentic workflows in our repos for maintenance and CI.
5. Before we could optimize our token consumption, we needed to know how tokens were consumed.


## Why This Matters

Developer productivity is one of the highest-ROI applications of AI today. Copilot is proving that AI can augment — not replace — human expertise, making experienced developers more productive and helping newcomers ramp up faster.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

I've seen organizations achieve 30-55% developer productivity gains with Copilot. But the real value isn't just speed — it's reducing cognitive load so developers can focus on architecture and business logic rather than boilerplate. The shift from 'AI writes code for me' to 'AI thinks with me' is where the magic happens.

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

📖 **[Read the original article](https://github.blog/ai-and-ml/github-copilot/improving-token-efficiency-in-github-agentic-workflows/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
