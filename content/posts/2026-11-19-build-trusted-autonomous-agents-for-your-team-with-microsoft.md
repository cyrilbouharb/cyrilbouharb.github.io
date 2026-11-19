---
title: "Build trusted autonomous agents for your team with Microsoft Foundry"
date: 2026-11-19
tags: ["Foundry", "Copilot", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/build-trusted-autonomous-agents-for-your-team-with-microsoft-foundry/"
description: "A new kind of agent can work alongside your team in Microsoft 365, with its own identity, permissions, and a manager accountable for its work.   Enterprises are all-in on AI agents, but the ROI hasn’t"
---

There's been an important development in the **Microsoft Foundry** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

### A new kind of agent can work alongside your team in Microsoft 365, with its own identity, permissions, and a manager accountable for its work.

Enterprises are all-in on AI agents, but the ROI hasn’t followed.What’s holding those agents back isn’t capability.

Today’s agents can do remarkable work on their own. They can start on a bug as soon as it’s assigned, turn a finished design into a working app, learn a task by watching you do it once, and spend the night researching and testing ideas so results are waiting by morning.

The gap shows up when you ask one of those agents to work with your team. Today, unless an agent has an account of its own, the only way it can work in Outlook or Teams is with your permissions. That works for a personal assistant, but it breaks down in two common scenarios:

- No user is signed in.An agent triggered by an event has no signed-in user to act for, so it either can’t take Microsoft 365 actions at all or has to hold on to someone’s credentials to do it.

### Autonomous agents that work for your team

Foundry now lets you build agents that bring that autonomy to the enterprise and customers likeNous Research have already proven this model works.These agents work in multi-user spaces like Teams group chats, and they act on their own across the Microsoft 365 apps you already use: responding to email, editing Excel sheets, and creating PowerPoint decks, even when no one is signed in. Autonomy comes with accountability: every one has a manager who answers for it. And they’re governed by your existing security, privacy, and governance stack, with no new systems or processes to learn.

Each one works under its own identity as a named member of your organization, in a standing role rather than performing one request at a time.

Every Foundry agent has a Microsoft Entraagent identity.What makes these agents different is they also have an Entraagent user account. That account gives the agent its own email, calendar, OneDrive, Teams presence, and a place in the organization chart, and it lets the agent perform Microsoft 365 actions as itself.

You may have seen Autopilot in Microsoft 365 Copilot. These agents are the same type: Autopilot comes out of the box, and in Foundry you build your own.

### Build it once, hire it across your organization

You don’t build this kind of agent directly. You build anagent-as-a-service:a blueprint that people then use to create their own instances, each with its own identity and access. The blueprint is a template that defines what the agent can do, such as the APIs it can call and the MCP tools it can access. You write custom code to shape that behavior, like when it responds, and deploy it as a Foundry hosted agent. Once the published blueprint is approved by an admin, your entire organization benefits. From the blueprint, each approved person in your org hires their own instance, with its own identity, agent user account, and access to their resources.


## Key Takeaways

1. Enterprises are all-in on AI agents, but the ROI hasn’t followed.What’s holding those agents back isn’t capability.
2. Today’s agents can do remarkable work on their own.
3. The gap shows up when you ask one of those agents to work with your team.
4. So most agents stay single-player: one user, one agent, one private conversation.
5. Foundry now lets you build agents that bring that autonomy to the enterprise and customers likeNous Research have already proven this model works.These agents work in multi-user spaces like Teams group chats, and they act on their own across the Microsoft 365 apps you already use: responding to email, editing Excel sheets, and creating PowerPoint decks, even when no one is signed in.


## Why This Matters

For organizations building AI agents, Foundry simplifies the journey from prototype to production. It removes the friction of stitching together multiple tools and provides enterprise-grade governance through AI Citadel — policy-based controls, content filtering, and audit trails — which is critical when you're operating at public sector scale.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

From a technical standpoint, Foundry's architecture addresses what I consider the four hardest problems in enterprise AI: **model lifecycle management** (versioning, A/B testing, rollback across GPT-5.5, Claude, Gemma, and open-source models), **agent orchestration** (Foundry Agent Service with Microsoft Agent Framework for multi-agent systems), **evaluation at scale** (batch evaluations, continuous monitoring, custom evaluators, and the trace-to-dataset flywheel), and **governance without friction** via AI Citadel (policy-based guardrails, RBAC, content filtering, and audit trails baked into the agent lifecycle rather than bolted on after). The addition of Foundry IQ as the intelligence layer — providing context engineering capabilities so agents can access enterprise knowledge through agentic RAG — is what transforms Foundry from a development platform into an enterprise AI operating system.


## Business Translation

**For the C-Suite:** Foundry directly impacts three board-level concerns: **time-to-value** (reduces AI project timelines from 6-12 months to weeks by eliminating infrastructure setup), **risk management** (built-in responsible AI guardrails and compliance controls reduce regulatory exposure), and **cost predictability** (unified platform means consolidated billing, no sprawl of point solutions each with their own licensing). The competitive moat here is speed: organizations that can iterate on AI use cases 10x faster will capture market share while competitors are still in proof-of-concept.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/build-trusted-autonomous-agents-for-your-team-with-microsoft-foundry/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
