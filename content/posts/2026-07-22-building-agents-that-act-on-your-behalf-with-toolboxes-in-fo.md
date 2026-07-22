---
title: "Building Agents that Act on Your Behalf with Toolboxes in Foundry"
date: 2026-07-22
tags: ["Foundry", "Data & AI", "Agentic RAG", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/building-agents-that-act-on-your-behalf-with-toolboxes-in-foundry/"
description: "How Toolboxes in Foundry simplify user delegation At some point, many agents move from answering questions to taking action. And when it does, the question becomes: whose identity is it acting with? I"
---

There's been an important development in the **Microsoft Foundry** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

How Toolboxes in Foundry simplify user delegation

At some point, many agents move from answering questions to taking action. And when it does, the question becomes:whose identity is it acting with? Imagine you are building an internal employee agent.  It needs to call a private, Entra-protected MCP server for orders, and it also needs to use Microsoft’s managed Work IQ MCP server to reason over the employee’s Microsoft 365 context. In both cases, the agent can’t run as a managed identity or service account. It has to act as thereal signed-in user— with that user’s permissions, access boundaries, and data protections. That’s where identity gets hard: exchanging tokens on behalf of the user, keeping each user’s tokens isolated, and handling consent and refreshing.

### Why is this hard to build yourself?

Let’s take the example of employee agent. Both tools demand the same thing: user delegation. If you choose to implement the entire user delegation yourself, you probably need to spend weeks before you can start building the business logic for your agents:

- Complex, high-stake token isolation:You must partition token caches correctly by user and tenant. A wrong cache key can silently leak one user’s downstream API access to another user.

- Consent management overhead:You need to detect consent failures, send users through consent, refresh expired tokens, and handle retries correctly for each API in each agent code you write.

- Duplicated implementation:Every new tool adds another scope, token exchange, cache entry, consent path, retry path, and header path. As you scale with hundreds of tools and thousands of agents, you end up rebuilding the same fragile plumbing.

### How does Toolbox solve it?

Same scenario, same user delegation — but the agent carries none of the plumbing above. The core idea:

- Auth lives on the toolbox, not in the agent:You pick an auth type once, when you connect a tool — the agent code stays auth-free.

- Foundry handles the whole flow:Whatever a tool needs — User delegation, agent identity, API keys, and more — Foundry acquires, exchanges, and refreshes the tokens server-side.

- The auth flow is never your burden:You can configure tools behind Toolbox and get an MCP endpoint. As your business logic evolves, you simply add or remove tools behind the versioned toolbox endpoint.


## Key Takeaways

1. At some point, many agents move from answering questions to taking action.
2. Let’s take the example of employee agent.
3. Same scenario, same user delegation — but the agent carries none of the plumbing above.
4. Auth type is chosen when theconnectionis created — in the portal, withazd, or via REST.Never in agent code.For end-user delegation you set the connection toOAuth2:.
5. The agent references the toolbox by its MCP endpoint — one tool, no header providers, no brokers, no caller context to thread through:.


## Why This Matters

For organizations building AI agents, Foundry simplifies the journey from prototype to production. It removes the friction of stitching together multiple tools and provides enterprise-grade governance through AI Citadel — policy-based controls, content filtering, and audit trails — which is critical when you're operating at public sector scale.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

From a technical standpoint, Foundry's architecture addresses what I consider the four hardest problems in enterprise AI: **model lifecycle management** (versioning, A/B testing, rollback across GPT-5.5, Claude, Gemma, and open-source models), **agent orchestration** (Foundry Agent Service with Microsoft Agent Framework for multi-agent systems), **evaluation at scale** (batch evaluations, continuous monitoring, custom evaluators, and the trace-to-dataset flywheel), and **governance without friction** via AI Citadel (policy-based guardrails, RBAC, content filtering, and audit trails baked into the agent lifecycle rather than bolted on after). The addition of Foundry IQ as the intelligence layer — providing context engineering capabilities so agents can access enterprise knowledge through agentic RAG — is what transforms Foundry from a development platform into an enterprise AI operating system.


## Business Translation

**For the C-Suite:** Foundry directly impacts three board-level concerns: **time-to-value** (reduces AI project timelines from 6-12 months to weeks by eliminating infrastructure setup), **risk management** (built-in responsible AI guardrails and compliance controls reduce regulatory exposure), and **cost predictability** (unified platform means consolidated billing, no sprawl of point solutions each with their own licensing). The competitive moat here is speed: organizations that can iterate on AI use cases 10x faster will capture market share while competitors are still in proof-of-concept.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/building-agents-that-act-on-your-behalf-with-toolboxes-in-foundry/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
