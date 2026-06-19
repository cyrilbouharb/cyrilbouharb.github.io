---
title: "Outcome-driven learning systems: Enterprise RL with OpenEnv and Foundry"
date: 2026-06-18
tags: ["Foundry", "Data & AI", "Foundry IQ", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/outcome-driven-learning-systems-enterprise-rl-with-openenv-and-foundry/"
description: "We shipped a lot at Build 2026: hosted agents, Toolboxes, Foundry IQ, Memory, Managed Compute, fine‑tuning, Frontier Tuning, and a new evaluation and optimization stack. Read as a feature list, it is "
---

There's been an important development in the **Microsoft Foundry** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

We shipped a lot atBuild 2026: hosted agents, Toolboxes, Foundry IQ, Memory, Managed Compute, fine‑tuning, Frontier Tuning, and a new evaluation and optimization stack. Read as a feature list, it is a lot to hold in your head. So here is a simpler way to see it: these are the parts you need to build alearning system, with agents that get measurably better at your work over time, not a chatbot that answers once and forgets. This post is about assembling those parts into one loop you own, and the science that makes a small, owned model worth training.

It builds on two pieces worth reading first. Jay Parikh’s“AI alone won’t change your business, the system running it will”argues that the winners do not just adopt a model; they stand up a governed system that improves the longer it runs. Satya’s framing in“a frontier ecosystem, not just a frontier model”sharpens it: the durable asset is not the model you rent, it is thelearning loop you own. Same idea from two angles. Build a system that improves against your outcomes, and make sure you own it.

Foundry makes that loop something you can build in anopen, interoperable, and modularway, so you can swap any piece (the model, the trainer, the tools) without rebuilding the whole thing. Two ingredients sit under every such system: a place for the agent topractice(anenvironment) and a way tojudgeit (aneval). To keep both open, Microsoft joined theOpenEnvcommunity.

However you come to this, whether PM, IT admin, developer, or AI engineer, the first half is the plain-languagewhatandwhy. The second half is the deep science. Skim or dive as suits you.

### Environments, evals, and rubrics, in plain language

Anenvironment(an RLE, or reinforcement-learning environment) is apractice spacefor your agent (harness + model). It is your real workflow and your standard operating procedure, codified so an agent can act inside it: the steps, the tools it is allowed to use, the data it sees. Think of it as a flight simulator for one of your business processes, close enough to the real thing that getting good in the simulator means getting good at the job.

Anevalis how youjudgea result, and the heart of an eval is arubric: a clear, scored definition of “done right” foryouroutcome, not a public leaderboard. “Did it reconcile the invoice to the contract? Did it cite a real clause? Did it stay inside policy?” Foundry shipsagent evaluationfor writing exactly these judgments, and an optimizer (below) for acting on the scores.

Here is the move that ties it together:an environment already contains its eval.Codify your workflowplusyour outcome rubric, and you have not just written a test, you have built ahill-climbing space. The agent practices, the rubric scores, and the system climbs toward your outcome. That is why RLEs are also evals: it is one artifact that both exercises the agent and grades it.

> Codify your workflow and your outcome into an environment, and the model becomes a part you can swap. The expertise lives in the loop you own, so the learning stays yours.

### A system learns in two ways

Before any science, the single most useful idea in this post: a system can get better in two different ways, and you should reach for them in order.


## Key Takeaways

1. We shipped a lot atBuild 2026: hosted agents, Toolboxes, Foundry IQ, Memory, Managed Compute, fine‑tuning, Frontier Tuning, and a new evaluation and optimization stack.
2. It builds on two pieces worth reading first.
3. Foundry makes that loop something you can build in anopen, interoperable, and modularway, so you can swap any piece (the model, the trainer, the tools) without rebuilding the whole thing.
4. However you come to this, whether PM, IT admin, developer, or AI engineer, the first half is the plain-languagewhatandwhy.
5. Anenvironment(an RLE, or reinforcement-learning environment) is apractice spacefor your agent (harness + model).


## Why This Matters

For organizations building AI agents, Foundry simplifies the journey from prototype to production. It removes the friction of stitching together multiple tools and provides enterprise-grade governance through AI Citadel — policy-based controls, content filtering, and audit trails — which is critical when you're operating at public sector scale.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

From a technical standpoint, Foundry's architecture addresses what I consider the four hardest problems in enterprise AI: **model lifecycle management** (versioning, A/B testing, rollback across GPT-5.5, Claude, Gemma, and open-source models), **agent orchestration** (Foundry Agent Service with Microsoft Agent Framework for multi-agent systems), **evaluation at scale** (batch evaluations, continuous monitoring, custom evaluators, and the trace-to-dataset flywheel), and **governance without friction** via AI Citadel (policy-based guardrails, RBAC, content filtering, and audit trails baked into the agent lifecycle rather than bolted on after). The addition of Foundry IQ as the intelligence layer — providing context engineering capabilities so agents can access enterprise knowledge through agentic RAG — is what transforms Foundry from a development platform into an enterprise AI operating system.


## Business Translation

**For the C-Suite:** Foundry directly impacts three board-level concerns: **time-to-value** (reduces AI project timelines from 6-12 months to weeks by eliminating infrastructure setup), **risk management** (built-in responsible AI guardrails and compliance controls reduce regulatory exposure), and **cost predictability** (unified platform means consolidated billing, no sprawl of point solutions each with their own licensing). The competitive moat here is speed: organizations that can iterate on AI use cases 10x faster will capture market share while competitors are still in proof-of-concept.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/outcome-driven-learning-systems-enterprise-rl-with-openenv-and-foundry/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
