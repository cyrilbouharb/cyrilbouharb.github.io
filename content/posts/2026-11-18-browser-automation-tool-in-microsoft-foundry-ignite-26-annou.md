---
title: "Browser Automation Tool in Microsoft Foundry : Ignite’26 Announcements"
date: 2026-11-18
tags: ["Foundry", "LLM", "Agentic RAG", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/browser-automation-tool-ignite/"
description: "Enterprise-ready cloud browsers for every Foundry agent: MCP action batching, Live View and Take control, session recording, VNet injection, browser proxy, profile reuse, secret management, and CAPTCH"
---

There's been an important development in the **Microsoft Foundry** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

### Enterprise-ready cloud browsers for every agent

Much of the work that keeps a business running still happens in a browser: internal portals, vendor consoles and legacy apps with no API. TheBrowser Automation tool in Foundry Agent Service, powered by Azure Playwright Workspaces, is now generally available. It gives every Foundry agent secure, scalable browsers with isolated sessions, and includes the following capabilities:

- Efficiency: Expanded MCP tool primitives with action batching (GA)

- Human-in-the-loop: Live View and Take control for authentication and steering the agent (GA)

- Networking: Private websites with VNet injection (preview)

### See it work: processing invoices across multiple apps

Our sample agent’s task is clear – Process 15 invoices, validate them against the rules, flag anomalies in Excel, and enter the validated invoices into the expense portal. That’s a multi-app task, and the agent hits the ground running with Browser automation tool in its toolbox.https://devblogs.microsoft.com/foundry/wp-content/uploads/sites/89/2026/11/BAT_Ignite-demo_Final.mp4

### MCP with expanded tool primitives and batching of actions

Browser automation tool offers a larger set of MCP tools built for browser work, so agents can choose the right level of control for each step of a workflow. Step-by-step tools cover the full range of interactions: opening and reading pages, taking accessibility snapshots, clicking, typing, completing forms, selecting options, handling dialogs, managing tabs, uploading files, and capturing screenshots, console messages and network requests. For multistep sequences, agents can batch actions with the run-code tool. It runs one Playwright script for the whole sequence instead of a long chain of snapshot, click and type calls. We understand efficiency matters and hence recommend batched scripts for repetitive flows, and step-by-step tools for unfamiliar pages and flows with dialogs, where checking the page at each step pays off and LLM is an enabler. Because scripts can run any code, the run-code tools stay opt-in and should be enabled only for reviewed scenarios.Learn more


## Key Takeaways

1. Much of the work that keeps a business running still happens in a browser: internal portals, vendor consoles and legacy apps with no API.
2. This Ignite, the Browser automation tool is enabled with additional features for your agentic automation workloads.
3. Our sample agent’s task is clear – Process 15 invoices, validate them against the rules, flag anomalies in Excel, and enter the validated invoices into the expense portal.
4. Browser automation tool offers a larger set of MCP tools built for browser work, so agents can choose the right level of control for each step of a workflow.
5. Browser workflows sometimes reach an unexpected page state, an ambiguous choice, or a step that needs human judgement.


## Why This Matters

For organizations building AI agents, Foundry simplifies the journey from prototype to production. It removes the friction of stitching together multiple tools and provides enterprise-grade governance through AI Citadel — policy-based controls, content filtering, and audit trails — which is critical when you're operating at public sector scale.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

From a technical standpoint, Foundry's architecture addresses what I consider the four hardest problems in enterprise AI: **model lifecycle management** (versioning, A/B testing, rollback across GPT-5.5, Claude, Gemma, and open-source models), **agent orchestration** (Foundry Agent Service with Microsoft Agent Framework for multi-agent systems), **evaluation at scale** (batch evaluations, continuous monitoring, custom evaluators, and the trace-to-dataset flywheel), and **governance without friction** via AI Citadel (policy-based guardrails, RBAC, content filtering, and audit trails baked into the agent lifecycle rather than bolted on after). The addition of Foundry IQ as the intelligence layer — providing context engineering capabilities so agents can access enterprise knowledge through agentic RAG — is what transforms Foundry from a development platform into an enterprise AI operating system.


## Business Translation

**For the C-Suite:** Foundry directly impacts three board-level concerns: **time-to-value** (reduces AI project timelines from 6-12 months to weeks by eliminating infrastructure setup), **risk management** (built-in responsible AI guardrails and compliance controls reduce regulatory exposure), and **cost predictability** (unified platform means consolidated billing, no sprawl of point solutions each with their own licensing). The competitive moat here is speed: organizations that can iterate on AI use cases 10x faster will capture market share while competitors are still in proof-of-concept.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/browser-automation-tool-ignite/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
