---
title: "From Chatbots to Automated Assistants: Routines in Microsoft Foundry Are Now Generally Available"
date: 2026-09-24
tags: ["Foundry", "GitHub", "Data & AI", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/from-chatbots-to-automated-assistants-routines-in-microsoft-foundry-are-now-generally-available/"
description: "Agents are rapidly evolving beyond chat. The first generation of agents waited for a person to send a message. Today, organizations want agents that can monitor work, respond to business events, and c"
---

There's been an important development in the **Microsoft Foundry** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

Agents are rapidly evolving beyond chat. The first generation of agents waited for a person to send a message. Today, organizations want agents that can monitor work, respond to business events, and continue tasks over time. An agent might triage a newly opened GitHub issue, respond when a message appears in a Microsoft Teams channel, prepare a report every morning, or check back on a long-running process until it finishes.

Building that automation yourself is difficult. You need schedulers, event listeners, webhooks, queues, infrastructure, authentication, run history, and monitoring—before you can focus on the agent’s actual job. Today, we’re announcing the general availability ofroutines inFoundry Agent Service, a managed way to run agents on a schedule, at a specific time, or in response to an external event. The trigger, agent action, identity, connections, and run history live together in your Foundry project. You define when the agent should run and what it should do, and Foundry handles the rest.

### Why build automated agents with Foundry?

Moving from a chatbot to an automated assistant introduces a different set of engineering challenges. Suppose you want an agent to triage every new GitHub issue assigned to your team. The agent itself might already understand how to classify the issue, find related documentation, and recommend an owner. But something still needs to:

- Deliver the event payload to the agent.

A recurring agent creates similar work: a scheduler, hosting infrastructure, retry logic, credentials, and a database for execution history. Every new automation adds more infrastructure to deploy and maintain. Routines bring managed agent execution into Foundry Agent Service. Create a trigger, select an agent, provide its instructions, and start the routine. Foundry queues the invocation, runs the agent, and records the result for later inspection. Teams can spend less time assembling automation infrastructure and more time building the agent capabilities that differentiate their applications.

### Run agents when work happens

Routines support several ways to start an agent:

Timer routines are ideal for work that should happen at a specific moment. Recurring routines let you manage a schedule alongside the agent instead of maintaining a separate scheduler and invocation service. Event-based routines allow agents to react when something changes—not when someone remembers to ask. Initial integrations include GitHub issue events and new messages in Microsoft Teams channels, with more event sources planned.

When an event occurs, Foundry receives it through the configured connection and forwards its payload to the agent. The agent can reason over the event, use its tools, and take the next appropriate action. A GitHub agent can triage an issue as soon as it arrives, while a Teams agent can detect a support request, retrieve relevant context, and initiate a response without waiting for a separate chat interaction.


## Key Takeaways

1. Agents are rapidly evolving beyond chat.
2. Building that automation yourself is difficult.
3. Moving from a chatbot to an automated assistant introduces a different set of engineering challenges.
4. A recurring agent creates similar work: a scheduler, hosting infrastructure, retry logic, credentials, and a database for execution history.
5. Timer routines are ideal for work that should happen at a specific moment.


## Why This Matters

For organizations building AI agents, Foundry simplifies the journey from prototype to production. It removes the friction of stitching together multiple tools and provides enterprise-grade governance through AI Citadel — policy-based controls, content filtering, and audit trails — which is critical when you're operating at public sector scale.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

From a technical standpoint, Foundry's architecture addresses what I consider the four hardest problems in enterprise AI: **model lifecycle management** (versioning, A/B testing, rollback across GPT-5.5, Claude, Gemma, and open-source models), **agent orchestration** (Foundry Agent Service with Microsoft Agent Framework for multi-agent systems), **evaluation at scale** (batch evaluations, continuous monitoring, custom evaluators, and the trace-to-dataset flywheel), and **governance without friction** via AI Citadel (policy-based guardrails, RBAC, content filtering, and audit trails baked into the agent lifecycle rather than bolted on after). The addition of Foundry IQ as the intelligence layer — providing context engineering capabilities so agents can access enterprise knowledge through agentic RAG — is what transforms Foundry from a development platform into an enterprise AI operating system.


## Business Translation

**For the C-Suite:** Foundry directly impacts three board-level concerns: **time-to-value** (reduces AI project timelines from 6-12 months to weeks by eliminating infrastructure setup), **risk management** (built-in responsible AI guardrails and compliance controls reduce regulatory exposure), and **cost predictability** (unified platform means consolidated billing, no sprawl of point solutions each with their own licensing). The competitive moat here is speed: organizations that can iterate on AI use cases 10x faster will capture market share while competitors are still in proof-of-concept.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/from-chatbots-to-automated-assistants-routines-in-microsoft-foundry-are-now-generally-available/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
