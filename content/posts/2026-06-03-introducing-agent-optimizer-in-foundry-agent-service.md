---
title: "Introducing Agent Optimizer in Foundry Agent Service"
date: 2026-06-03
tags: ["Foundry", "OpenAI", "Data & AI", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/agent-optimizer-build2026/"
description: "With hosted agents, we made it straightforward to build and deploy agents on Foundry. You write your logic, run azd deploy, and your agent is live. But “live” and “production-ready” aren’t the same th"
---

There's been an important development in the **Microsoft Foundry** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

Withhosted agents, we made it straightforward to build and deploy agents on Foundry. You write your logic, run azd deploy, and your agent is live. But “live” and “production-ready” aren’t the same thing.

The gap shows up quickly. Your customer support agent handles requests, but it forgets to ask for an order number before looking up status. It answers warranty questions without checking the purchase date. It gives electrical wiring advice when it should decline and recommends a professional. Each fix means rewriting your system prompt, testing by hand, and hoping you didn’t break something else in the process.

For one agent, that’s manageable. For a team running ten agents across different domains, it’s a bottleneck that doesn’t scale. We heard this from developers consistently:the hard part isn’t building the agent, it’s getting the agent to behave correctly across all the scenarios it needs to handle.

Today we’re excited to introduce theagent optimizer in Foundry Agent Service, in private preview and out in public preview in 30 days.

### What is the agent optimizer in Foundry Agent Service?

Agent optimizer evaluates your hosted agent against defined criteria, generates better configurations, and ranks the results so you can deploy the best one. It automates the improvement loop that most teams do by hand today. Here’s how it works. The optimizer runs a closed-loop cycle:

- Evaluate the baseline.Your agent processes a set of tasks, each with explicit pass/fail criteria. The result is a composite score from 0.0 to 1.0.

- Generate candidates.Guided by what failed, the optimizer produces new configurations. You choose the optimization target: instruction rewrites your system prompt, skill generates reusable procedures, or model finds the best deployment for your quality/cost trade-off.

- Evaluate candidates.Each candidate runs against the same task set.

### Developer experience

Agent optimizer was made for developers making it easier to take their agents into production with confidence. Here’s what this looks like in practice. Say you have a customer support agent for a consumer electronics company. Your current system prompt is bare: “You are a helpful customer support agent.”

```
$ azd ai agent optimize
 
Optimizing agent "travel-approver"...
  Baseline saved to .agent_configs\baseline\metadata.yaml
  Job ID: opt_999f814ed77a….
  Status: pending
  Portal: https://ai.azure.com/nextgen/....
  ⠇ completed · iteration 2 · score: 1.00 · 9m0s
Results:
  Candidate              Score    Pass  Eval
  ──────────────────── ─────── ───────  ──────
  baseline                0.60     71%  View
  candidate_1 ★           0.92    100%  View

  Candidate IDs:
      baseline
```

```
$ azd ai agent optimize
 
Optimizing agent "travel-approver"...
  Baseline saved to .agent_configs\baseline\metadata.yaml
  Job ID: opt_999f814ed77a….
  Status: pending
  Portal: https://ai.azure.com/nextgen/....
  ⠇ completed · iteration 2 · score: 1.00 · 9m0s
Results:
  Candidate              Score    Pass  Eval
  ──────────────────── ─────── ───────  ──────
  baseline                0.60     71%  View
  candidate_1 ★           0.92    100%  View

  Candidate IDs:
      baseline
```

From 0.60 to 0.92. No model retraining. No code changes. Using synthetic data or historical traces of how your agent performed and evaluator signals that identified where it fell short, the optimizer rewrote the system prompt/skills/tools to strengthen return policies, escalation procedures, troubleshooting frameworks, and safety boundaries. The changes were driven by observed behavior and scored against the criteria you defined.


## Key Takeaways

1. Withhosted agents, we made it straightforward to build and deploy agents on Foundry.
2. For one agent, that’s manageable.
3. Today we’re excited to introduce theagent optimizer in Foundry Agent Service, in private preview and out in public preview in 30 days.
4. To sign up for private preview hereaka.ms/Agent-Optimizer-Private-Preview.
5. Agent optimizer evaluates your hosted agent against defined criteria, generates better configurations, and ranks the results so you can deploy the best one.


## Why This Matters

For organizations building AI agents, Foundry simplifies the journey from prototype to production. It removes the friction of stitching together multiple tools and provides enterprise-grade governance through AI Citadel — policy-based controls, content filtering, and audit trails — which is critical when you're operating at public sector scale.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

From a technical standpoint, Foundry's architecture addresses what I consider the four hardest problems in enterprise AI: **model lifecycle management** (versioning, A/B testing, rollback across GPT-5.5, Claude, Gemma, and open-source models), **agent orchestration** (Foundry Agent Service with Microsoft Agent Framework for multi-agent systems), **evaluation at scale** (batch evaluations, continuous monitoring, custom evaluators, and the trace-to-dataset flywheel), and **governance without friction** via AI Citadel (policy-based guardrails, RBAC, content filtering, and audit trails baked into the agent lifecycle rather than bolted on after). The addition of Foundry IQ as the intelligence layer — providing context engineering capabilities so agents can access enterprise knowledge through agentic RAG — is what transforms Foundry from a development platform into an enterprise AI operating system.


## Business Translation

**For the C-Suite:** Foundry directly impacts three board-level concerns: **time-to-value** (reduces AI project timelines from 6-12 months to weeks by eliminating infrastructure setup), **risk management** (built-in responsible AI guardrails and compliance controls reduce regulatory exposure), and **cost predictability** (unified platform means consolidated billing, no sprawl of point solutions each with their own licensing). The competitive moat here is speed: organizations that can iterate on AI use cases 10x faster will capture market share while competitors are still in proof-of-concept.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/agent-optimizer-build2026/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
