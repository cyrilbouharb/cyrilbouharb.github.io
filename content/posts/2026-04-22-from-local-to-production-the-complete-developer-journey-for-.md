---
title: "From Local to Production: The Complete Developer Journey for Building, Composing, and Deploying AI Agents"
date: 2026-04-22
tags: ["Foundry", "Copilot", "GitHub Copilot", "GitHub", "OpenAI", "Semantic Kernel", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/from-local-to-production-the-complete-developer-journey-for-building-composing-and-deploying-ai-agents/"
description: "When we launched Microsoft Agent Framework last October, we made a promise: building production-grade AI agents should feel as natural and structured as building any other software. Today, we’re deliv"
---

There's been an important development in the **AI Agents** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

When we launchedMicrosoft Agent Frameworklast October, we made a promise: building production-grade AI agents should feel as natural and structured as building any other software.

Today, we’re delivering on that promise — with thev1.0 release of Microsoft Agent Frameworkand thegeneral availability ofFoundry Toolkitfor Visual Studio Code(formerly AI Toolkit for VS Code), new capabilities inmemory(preview) in Foundry Agent Service,Toolbox in Foundry(preview) to give your agents the right tools, a faster and more securehostedagentsexperience in Foundry Agent Service (preview), andObservability in Foundry Control Planereaching full GA on core capabilities including end-to-end tracing now in place.

Customers likeSitecoreare already putting this stack to work.Their SitecoreAI platform powers Agentic Studio, a collaborative workspace where marketing teams and AI agents execute campaigns together. It’s built on Microsoft Agent Framework, with Foundry IQ ensuring each agent connects to the right brand knowledge at the right time with built-in governance.

### Step 1: Build Locally with Microsoft Agent Framework + Foundry Toolkit for VS Code

Every agent starts on a developer’s machine.Microsoft Agent Frameworkhas now reached its v1.0 release and is stable across Python and .NET. It’s the open-source SDK and runtime that unifies the enterprise-grade foundations of Semantic Kernel with the multi-agent orchestration innovation of AutoGen, so developers no longer have to choose between them. We’ve published detailedmigration guidesfor existing Semantic Kernel and AutoGen users to make the transition straightforward.

- Multi-modeland agent platform support— Azure OpenAI, Anthropic, Google Gemini, Amazon Bedrock, Ollama, and more

- Workflows— programmatic and declarative multi-step agent pipelines, including visual export inDevUI

- Native Foundry integration— memory, hosted agents, Observability (Tracing, Monitoring, and Evaluations), and Foundry Tools as first-class building blocks

### Step 2: Build Agents That Actually Do Things — Agent Harness & Multi-Agent Composition (Public Preview)

Microsoft Agent Framework handles multi-agent orchestration— but orchestrating agents is only half the picture. The other half is what happens when an individual agent needs to operate autonomously over extended periods: executing shell commands, reading and writing to the filesystem, and managing context across long-running sessions without losing coherence. Microsoft Agent Framework addresses this in two ways: a built-inAgent Harness(public preview) and integrations with coding agents (public preview).


## Key Takeaways

1. When we launchedMicrosoft Agent Frameworklast October, we made a promise: building production-grade AI agents should feel as natural and structured as building any other software.
2. Today, we’re delivering on that promise — with thev1.0 release of Microsoft Agent Frameworkand thegeneral availability ofFoundry Toolkitfor Visual Studio Code(formerly AI Toolkit for VS Code), new capabilities inmemory(preview) in Foundry Agent Service,Toolbox in Foundry(preview) to give your agents the right tools, a faster and more securehostedagentsexperience in Foundry Agent Service (preview), andObservability in Foundry Control Planereaching full GA on core capabilities including end-to-end tracing now in place.
3. Customers likeSitecoreare already putting this stack to work.Their SitecoreAI platform powers Agentic Studio, a collaborative workspace where marketing teams and AI agents execute campaigns together.
4. Every agent starts on a developer’s machine.Microsoft Agent Frameworkhas now reached its v1.0 release and is stable across Python and .NET.
5. Foundry Toolkit for VS Code, now generally available, gives you a purpose-built VS Code experience alongside Microsoft Agent Framework: create agents from templates or with GitHub Copilot, test and debug runs locally with visualization and traces, and deploy to Foundry Agent Service directly — all without leaving the familiar VS Code environment.


## Why This Matters

Agentic AI is where the industry is heading. From code generation to customer service to data analysis, agents can handle multi-step workflows that previously required human intervention at every stage. This isn't just automation — it's a fundamentally new way of building software.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The agent landscape is evolving rapidly. What excites me most is the convergence of multi-agent frameworks with enterprise tools — imagine agents that can not only reason but also execute across your entire technology stack. We're still early, but the trajectory is clear.

If you're exploring this area, my advice is to start small — pick one concrete use case, prototype it, and iterate. The tooling has matured significantly, and the barrier to entry has never been lower.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/from-local-to-production-the-complete-developer-journey-for-building-composing-and-deploying-ai-agents/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
