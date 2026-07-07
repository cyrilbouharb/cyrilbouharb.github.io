---
title: "What’s New in Microsoft Foundry | June 2026"
date: 2026-07-07
tags: ["Foundry", "Copilot", "GitHub", "LLM", "Microsoft Fabric", "Data & AI", "Foundry IQ", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-june-2026/"
description: "Claude is now generally available in Microsoft Foundry. Here's everything else that shipped between Build 2026 and the end of June — autopilot agents, expanded Toolboxes and Routines, Agent Optimizer'"
---

There's been an important development in the **Microsoft Foundry** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

Here’s what shipped in Microsoft Foundry in June 2026 — Claude reached general availability, Foundry agents started publishing straight into Microsoft 365 Copilot and Teams, and Toolboxes, Routines, and Memory all got meaningfully more capable.

### TL;DR

- Claude is now generally available in Microsoft Foundry:Anthropic’s Claude models are hosted on Azure with the Messages API, prompt caching, extended thinking, and tool streaming — and Foundry Agent Service can use Claude as the reasoning core for multi-step agents.

- Foundry agents can now publish to Microsoft 365 Copilot and Teams (GA):This fulfills the “GA in June 2026” commitment from Build. Agents move through one governed publishing pipeline instead of separate rebuilds per surface.

- Foundry autopilot agents (public preview):A new agent category with its own Entra Agent ID, productivity license, email, calendar, and Teams presence — designed to work inside shared spaces like group chats, not just one-on-one chat.

- Workstream Manager sample agent:A ready-to-customize autopilot agent for Teams group chats that tracks tasks, summarizes conversations into action items, and follows up on overdue work.

### Join the community

Connect with 50,000+ developers onDiscord, ask questions inGitHub Discussions, explore the new recipes inForgebookandsubscribe via RSSto get this digest monthly.


## Key Takeaways

1. Here’s what shipped in Microsoft Foundry in June 2026 — Claude reached general availability, Foundry agents started publishing straight into Microsoft 365 Copilot and Teams, and Toolboxes, Routines, and Memory all got meaningfully more capable.
2. Connect with 50,000+ developers onDiscord, ask questions inGitHub Discussions, explore the new recipes inForgebookandsubscribe via RSSto get this digest monthly.
3. Build 2026 (June 2-3) shipped a huge amount of Foundry surface area — hosted agents, Toolboxes, Foundry IQ, Memory, Managed Compute, fine-tuning, Frontier Tuning, and a new evaluation and optimization stack.
4. Build promised general availability for publishing Foundry agents into Microsoft 365 Copilot and Teams “in June 2026.” That shipped on June 10.
5. The interaction model is also different from a typical chatbot.


## Why This Matters

For organizations building AI agents, Foundry simplifies the journey from prototype to production. It removes the friction of stitching together multiple tools and provides enterprise-grade governance through AI Citadel — policy-based controls, content filtering, and audit trails — which is critical when you're operating at public sector scale.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

From a technical standpoint, Foundry's architecture addresses what I consider the four hardest problems in enterprise AI: **model lifecycle management** (versioning, A/B testing, rollback across GPT-5.5, Claude, Gemma, and open-source models), **agent orchestration** (Foundry Agent Service with Microsoft Agent Framework for multi-agent systems), **evaluation at scale** (batch evaluations, continuous monitoring, custom evaluators, and the trace-to-dataset flywheel), and **governance without friction** via AI Citadel (policy-based guardrails, RBAC, content filtering, and audit trails baked into the agent lifecycle rather than bolted on after). The addition of Foundry IQ as the intelligence layer — providing context engineering capabilities so agents can access enterprise knowledge through agentic RAG — is what transforms Foundry from a development platform into an enterprise AI operating system.


## Business Translation

**For the C-Suite:** Foundry directly impacts three board-level concerns: **time-to-value** (reduces AI project timelines from 6-12 months to weeks by eliminating infrastructure setup), **risk management** (built-in responsible AI guardrails and compliance controls reduce regulatory exposure), and **cost predictability** (unified platform means consolidated billing, no sprawl of point solutions each with their own licensing). The competitive moat here is speed: organizations that can iterate on AI use cases 10x faster will capture market share while competitors are still in proof-of-concept.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-june-2026/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
