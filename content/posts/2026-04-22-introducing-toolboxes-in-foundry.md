---
title: "Introducing Toolboxes in Foundry"
date: 2026-04-22
tags: ["Foundry", "Azure AI", "Copilot", "GitHub Copilot", "GitHub", "RAG", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/"
description: "Available in Public Preview Today   Toolbox is a new way to curate, configure, and reuse tools across all of your AI agents without rewiring them every time from Foundry.  Today, teams build agents ac"
---

There's been an important development in the **GitHub Copilot** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

### Available in Public Preview Today

Toolbox is a new way tocurate, configure, and reusetools across all of your AI agents without rewiring them every time from Foundry.

Today, teams build agents across different frameworks and runtimes. Each agent often wires tools directly, with its own authentication, credentials, and integration code. As organizations scale agent usage, this leads to duplicated work, inconsistent behavior, and fragile production deployments.

Toolbox fixes this by letting you define acurated set of tools once,manage them centrally in Foundry, andexpose them through a unified endpointthat any agent can consume.

### Why are tools messy today

Consider this scenario: developer onboarding. You’re building an agent that provisions an environment for a new engineer. It creates an Entra ID account, adds access to GitHub repos, spins up cloud resources, creates onboarding tasks in Azure DevOps, and sends a welcome message in Teams.  Sounds straightforward, until you look closer.

That single agent depends on five tools. Five different tool types (APIs, MCP servers, skills, connectors, flows). Five different authentication models. Five different owning teams; each with their own expectations for how their tools should be called. Now multiply that across every agent your organization is building.
Teams re‑implement the same tools. Credentials are duplicated. Governance is inconsistent or missing entirely. There’s little visibility into what tools exist, who is using them, or whether they’re governed at all. Developers stall, not because the models aren’t capable, but because tool integration has become the bottleneck. The infrastructure already exists. Enterprises have gateways, credential vaults, policies, and observability. What’s missing is a developer experience that packages this infrastructure into something reusable, discoverable, and governed by default.

That’s what Foundry Toolbox is designed to provide.

### Toolbox Overview

What is a Toolbox: Atoolbox is a reusable bundle of tools, managed in Foundry, that agents consume through a single, consistent interface.

Toolboxes cover the full tool lifecycle through four pillars: Find the right tools. Build a toolbox. Consume a toolbox from any agent. Govern everything that flows through it.In public preview today, the focus is onBuildandConsume; the two steps that remove friction immediately.


## Key Takeaways

1. Toolbox is a new way tocurate, configure, and reusetools across all of your AI agents without rewiring them every time from Foundry.
2. Today, teams build agents across different frameworks and runtimes.
3. Toolbox fixes this by letting you define acurated set of tools once,manage them centrally in Foundry, andexpose them through a unified endpointthat any agent can consume.
4. Consider this scenario: developer onboarding.
5. That single agent depends on five tools.


## Why This Matters

Developer productivity is one of the highest-ROI applications of AI today. Copilot is proving that AI can augment — not replace — human expertise, making experienced developers more productive and helping newcomers ramp up faster.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

I've seen organizations achieve 30-55% developer productivity gains with Copilot. But the real value isn't just speed — it's reducing cognitive load so developers can focus on architecture and business logic rather than boilerplate. The shift from 'AI writes code for me' to 'AI thinks with me' is where the magic happens.

If you're exploring this area, my advice is to start small — pick one concrete use case, prototype it, and iterate. The tooling has matured significantly, and the barrier to entry has never been lower.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/introducing-toolboxes-in-foundry/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
