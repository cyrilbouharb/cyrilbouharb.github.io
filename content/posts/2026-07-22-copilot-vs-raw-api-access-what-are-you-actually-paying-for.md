---
title: "Copilot vs. raw API access: What are you actually paying for?"
date: 2026-07-22
tags: ["Foundry", "Copilot", "GitHub Copilot", "GitHub", "OpenAI", "Data & AI", "AI Agents"]
categories: ["analysis"]
source_url: "https://github.blog/ai-and-ml/github-copilot/copilot-vs-raw-api-access-what-are-you-actually-paying-for/"
description: "Copilot now bills usage at listed API rates. Compare direct model access with the coding workflow, policy, and harness work around it.
The post Copilot vs. raw API access: What are you actually paying"
---

There's been an important development in the **Microsoft Foundry** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

I keep seeing this question: “Why would I pay for GitHub Copilot when I can call the same models through an API?”

It’s a fair question. The answer depends on what work you need to own.

Are you building a product feature with your own prompts, retrieval, routing, logs, security model, and billing controls? Or are you trying to get from a GitHub Issue to a reviewed pull request with the editor, repository, terminal, and organization policies already connected?

Cost is part of that equation. Copilot plans include a monthly allocation of GitHub AI Credits. Metered usage is calculated from input, output, and cached tokens at the listed rate for the selected model.

### Copilot is development tooling around the model

Now take a common maintenance task: a developer starts from a GitHub Issue, inspects the repository, changes the affected files, runs the test suite in the terminal, and opens a pull request for review. The model call is one step in that workflow. The surrounding system needs the issue, the diff, repository instructions, permitted commands, and the organization’s policies.

GitHub Copilot connects those surfaces across the editor, repository, pull request, issue, terminal, and organization controls. That is what the plan covers alongside model access. The billing change makes the split easier to see: code completions and Next Edit Suggestions remain included in paid plans, while AI Credits apply to more resource-intensive chat and agentic work.

Cost per task therefore depends on more than the listed token rate. Context selection, tool use, retries, and the path from an issue to a reviewed pull request all affect the number of tokens spent and whether the work finishes.

The same billing model gives buyers visibility. Organization plans “pool” AI Credits across the organization, and admins can set budgets and track usage in the billing dashboard. Adoption stays measurable instead of scattering across individual API keys and untracked scripts.

### The harness has measurable impact

GitHub’s evaluation held the model, benchmark task, context window, reasoning effort, tool selection, and MCP servers constant while comparing Copilot CLI with model-vendor harnesses. Across SWE-bench Verified, SWE-bench Pro, SkillsBench, TerminalBench, and Win-Hill, Copilot reached task-resolution parity while using fewer tokens in most configurations. For TerminalBench 2.0, each agent-model configuration ran at least five times to measure cost and completion variance.

Readthe full agentic-harness evaluation across models and tasks.


## Key Takeaways

1. I keep seeing this question: “Why would I pay for GitHub Copilot when I can call the same models through an API?”.
2. Are you building a product feature with your own prompts, retrieval, routing, logs, security model, and billing controls? Or are you trying to get from a GitHub Issue to a reviewed pull request with the editor, repository, terminal, and organization policies already connected?.
3. Raw API access and Copilot address different layers of that system.
4. Now take a common maintenance task: a developer starts from a GitHub Issue, inspects the repository, changes the affected files, runs the test suite in the terminal, and opens a pull request for review.
5. GitHub Copilot connects those surfaces across the editor, repository, pull request, issue, terminal, and organization controls.


## Why This Matters

For organizations building AI agents, Foundry simplifies the journey from prototype to production. It removes the friction of stitching together multiple tools and provides enterprise-grade governance through AI Citadel — policy-based controls, content filtering, and audit trails — which is critical when you're operating at public sector scale.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

From a technical standpoint, Foundry's architecture addresses what I consider the four hardest problems in enterprise AI: **model lifecycle management** (versioning, A/B testing, rollback across GPT-5.5, Claude, Gemma, and open-source models), **agent orchestration** (Foundry Agent Service with Microsoft Agent Framework for multi-agent systems), **evaluation at scale** (batch evaluations, continuous monitoring, custom evaluators, and the trace-to-dataset flywheel), and **governance without friction** via AI Citadel (policy-based guardrails, RBAC, content filtering, and audit trails baked into the agent lifecycle rather than bolted on after). The addition of Foundry IQ as the intelligence layer — providing context engineering capabilities so agents can access enterprise knowledge through agentic RAG — is what transforms Foundry from a development platform into an enterprise AI operating system.


## Business Translation

**For the C-Suite:** Foundry directly impacts three board-level concerns: **time-to-value** (reduces AI project timelines from 6-12 months to weeks by eliminating infrastructure setup), **risk management** (built-in responsible AI guardrails and compliance controls reduce regulatory exposure), and **cost predictability** (unified platform means consolidated billing, no sprawl of point solutions each with their own licensing). The competitive moat here is speed: organizations that can iterate on AI use cases 10x faster will capture market share while competitors are still in proof-of-concept.


---

📖 **[Read the original article](https://github.blog/ai-and-ml/github-copilot/copilot-vs-raw-api-access-what-are-you-actually-paying-for/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
