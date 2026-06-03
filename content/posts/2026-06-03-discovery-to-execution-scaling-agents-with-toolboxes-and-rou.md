---
title: "Discovery to Execution: Scaling Agents with Toolboxes and Routines in Microsoft Foundry"
date: 2026-06-03
tags: ["Foundry", "Microsoft Fabric", "Data & AI", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/toolbox-build-26/"
description: "Tooling doesn’t break at a small scale—it breaks when teams move to production. AI adoption accelerates, so does the number of tools available to them. Discovering, managing and securing the right too"
---

There's been an important development in the **Microsoft Foundry** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

Tooling doesn’t break at a small scale—it breaks when teams move to production. AI adoption accelerates, so does the number of tools available to them. Discovering, managing and securing the right tools has quickly become one of the biggest challenges in building production-grade agents. Today, we are announcing new capabilities in Toolboxes in Foundry:

- Skills(preview): Create, version, and manage reusable capabilities in a project-scoped catalog and expose them through Toolbox. Agents can discover and use these, making shared capabilities as easy to use as any tool.

- Work IQ(preview) andFabric IQ(preview): Connect your agents directly to enterprise data and reasoning systems, so they can operate with real business context—without custom integrations.

- Browser Automation(preview): Bring Model Context Protocol (MCP)-native web automation to hosted agents using Playwright workspaces. It gives teams a faster path from idea to execution, with live visibility and control when workflows hit edge cases—so agents can reliably automate complex web tasks.

At the core of scaling agents is tool discovery at scale.Tool searchis designed to solve this challenge. In production, toolboxes grow fast. A toolbox with 5 tools can quickly become 50 or 200 as teams add edge cases, integrations, and partner APIs. Without tool search, every tool definition is sent to the model on every turn, creating three problems:

- Cost scales with tool count:Every definition adds input tokens. At 200 tools, you pay for thousands of schema tokens on every turn, whether the model uses them or not.

- Context gets crowded:Tool definitions take up context window space, leaving less room for the conversation, domain context, and reasoning.

- The model gets confused:With hundreds of tools in view, it may choose similar but wrong tools or miss the right one in the noise.

### Catalog – Provide Business Context with Work IQ, Fabric IQ and Browser Automation

To make agents useful to your user, you need more than tool discovery—you need access to real business data and ready-to-use integrations. Foundry brings these together in a single catalog with Work IQ, Fabric IQ and more.

Work IQ: bring Microsoft 365 into your agents (preview)

Work IQgives agents access to your organization’s data and context—without exposing raw data. It builds a continuously updated understanding across Microsoft 365 and external systems, grounded in your existing permissions and policies. With Work IQ, agents can reason over real workplace context and handle complex, multi-step tasks at scale.

Fabric IQ: connect agents to business data (preview)


## Key Takeaways

1. Tooling doesn’t break at a small scale—it breaks when teams move to production.
2. Most of the capabilities in this post are delivered throughToolboxesin Foundry—the layer where agents discover, access, and use tools at runtime.Routines(preview) is the exception: it’s part ofFoundry Agent Serviceand handlesagent run control, so you can define when an agent should execute and let Foundry reliably queue, run, and track those executions at scale.
3. At the core of scaling agents is tool discovery at scale.Tool searchis designed to solve this challenge.
4. When tool search is enabled on a toolbox, the toolbox no longer floods the model’s context with every tool definition.
5. Everything else is hidden by default.


## Why This Matters

For organizations building AI agents, Foundry simplifies the journey from prototype to production. It removes the friction of stitching together multiple tools and provides enterprise-grade governance through AI Citadel — policy-based controls, content filtering, and audit trails — which is critical when you're operating at public sector scale.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

From a technical standpoint, Foundry's architecture addresses what I consider the four hardest problems in enterprise AI: **model lifecycle management** (versioning, A/B testing, rollback across GPT-5.5, Claude, Gemma, and open-source models), **agent orchestration** (Foundry Agent Service with Microsoft Agent Framework for multi-agent systems), **evaluation at scale** (batch evaluations, continuous monitoring, custom evaluators, and the trace-to-dataset flywheel), and **governance without friction** via AI Citadel (policy-based guardrails, RBAC, content filtering, and audit trails baked into the agent lifecycle rather than bolted on after). The addition of Foundry IQ as the intelligence layer — providing context engineering capabilities so agents can access enterprise knowledge through agentic RAG — is what transforms Foundry from a development platform into an enterprise AI operating system.


## Business Translation

**For the C-Suite:** Foundry directly impacts three board-level concerns: **time-to-value** (reduces AI project timelines from 6-12 months to weeks by eliminating infrastructure setup), **risk management** (built-in responsible AI guardrails and compliance controls reduce regulatory exposure), and **cost predictability** (unified platform means consolidated billing, no sprawl of point solutions each with their own licensing). The competitive moat here is speed: organizations that can iterate on AI use cases 10x faster will capture market share while competitors are still in proof-of-concept.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/toolbox-build-26/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
