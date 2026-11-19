---
title: "What’s new in Foundry Agent Service at Ignite 2026"
date: 2026-11-18
tags: ["Foundry", "Copilot", "GitHub Copilot", "GitHub", "Microsoft Fabric", "Data & AI", "Agentic RAG", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/whats-new-in-foundry-agent-service-at-ignite-2026/"
description: "Your customers don&#8217;t judge agents by how well they demo. They judge them by whether the work gets done: the case resolved, the report delivered, the follow-up sent. That takes more than a model."
---

There's been an important development in the **GitHub Copilot** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

Your customers don’t judge agents by how well they demo. They judge them by whether the work gets done: the case resolved, the report delivered, the follow-up sent. That takes more than a model. It takes the right context and tools, a runtime that holds up under real demand, and a way to keep improving once real users put agents to work. AtIgnite 2026, Foundry Agent Service delivers new capabilities to get you there across the agent lifecycle: Build, Deploy, and Operate.

Build more capable agents faster with the managed Microsoft Copilot harness, real-time voice, and richer tool connections. Deploy them at scale with enterprise controls, and bring them into Microsoft 365 where people already work. Operate them with confidence by turning production evidence into validated improvements. Here’s what’s new, and how each capability helps you move from idea to impact.

### Build harness agents with the tools you use

The Microsoft Copilot harness, in public preview, gives developers a fully managed way to build prompt agents that reason, use tools, and complete complex, long-running tasks. Microsoft runs the agent loop and sandbox; you bring the knowledge, reusable skills, and connected tools that make the agent yours. Instead of rebuilding execution machinery, your team can focus on the agent’s expertise and results.

Author Copilot harness agents in the Foundry UI, the GitHub Copilot app, the Foundry CLI (azd ai), or the Foundry Toolkit for VS Code, and keep agent definitions in source control alongside your application code.[Read what’s new in Foundry dev tools →]

You can choose the right starting point for your application: author a prompt agent using the Microsoft Copilot harness, or bring your own code and orchestration through hosted agents. Foundry Agent Service supports those choices without requiring every team to use the same framework or take the same approach to agent logic.

What’s new in Foundry Agent Service at Ignite 2026Watch on YouTube

### Voice conversations to your agents, now generally available

Talking to AI should feel as natural as talking to a person.Voice agentsin Foundry Agent Service are now generally available, giving organizations an enterprise-grade way to add real-time voice to their agents. That covers serving customers, supporting employees, and powering in-car and in-app assistants.

- Conversations that feel human:people can interrupt, pause and change direction, and the agent keeps up.

- Builds on what you already have:add voice to existing agents without rewriting them, and connect to phone and contact center systems through native telephony.

- Production-ready from day one:build, deploy, monitor and improve voice agents on the same managed platform as the rest of your agents.


## Key Takeaways

1. Your customers don’t judge agents by how well they demo.
2. Build more capable agents faster with the managed Microsoft Copilot harness, real-time voice, and richer tool connections.
3. The Microsoft Copilot harness, in public preview, gives developers a fully managed way to build prompt agents that reason, use tools, and complete complex, long-running tasks.
4. Author Copilot harness agents in the Foundry UI, the GitHub Copilot app, the Foundry CLI (azd ai), or the Foundry Toolkit for VS Code, and keep agent definitions in source control alongside your application code.[Read what’s new in Foundry dev tools →].
5. You can choose the right starting point for your application: author a prompt agent using the Microsoft Copilot harness, or bring your own code and orchestration through hosted agents.


## Why This Matters

Developer productivity is one of the highest-ROI applications of AI today. Copilot is proving that AI can augment — not replace — human expertise, making experienced developers more productive and helping newcomers ramp up faster.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The technical evolution of Copilot is fascinating from an AI systems perspective. We've moved from **completion-based assistance** (predict the next line) to **agent-mode** (understand the intent, decompose the problem, execute multi-file changes, run tests, iterate on failures). This is a fundamental architectural shift — from a stateless token predictor to a stateful reasoning agent with tool use. What's technically impressive is the context management: Copilot now maintains a working memory of your entire codebase, open issues, PR history, and team conventions. The retrieval augmentation layer that grounds suggestions in *your specific codebase* (not just generic patterns) is what makes the difference between a toy and a production tool. The agentic workflows — where Copilot can plan, execute, verify, and self-correct — represent the state of the art in applied AI agents today.


## Business Translation

**For the C-Suite:** Developer talent is the #1 constraint in digital transformation. Copilot delivers a measurable **25-55% productivity gain** (validated by Microsoft/GitHub research across 1M+ developers). In financial terms: a 500-developer organization saves $15-30M annually in equivalent output — without hiring. More importantly, it reduces **time-to-market** for features, which directly impacts revenue capture. The strategic play isn't just efficiency — it's enabling your existing engineering team to tackle projects that were previously impossible given resource constraints.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/whats-new-in-foundry-agent-service-at-ignite-2026/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
