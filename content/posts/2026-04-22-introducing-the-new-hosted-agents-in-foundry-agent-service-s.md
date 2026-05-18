---
title: "Introducing the new hosted agents in Foundry Agent Service: secure, scalable compute built for agents"
date: 2026-04-22
tags: ["Foundry", "Copilot", "GitHub Copilot", "GitHub", "OpenAI", "Data & AI", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/introducing-the-new-hosted-agents-in-foundry-agent-service-secure-scalable-compute-built-for-agents/"
description: "Agents are already transforming how developers solve problems. Whether it&#8217;s a coding agent that refactors your repo overnight, a research agent that synthesizes hundreds of documents into a brie"
---

There's been an important development in the **GitHub Copilot** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

Agents are already transforming how developers solve problems. Whether it’s a coding agent that refactors your repo overnight, a research agent that synthesizes hundreds of documents into a brief, or an ops agent that monitors and remediates infrastructure — the pattern is clear. Developers are building agents that don’t just answer questions, they go do things.

Agents of today don’t just execute from a list of tools. They access the underlying file system, write and execute code, and persist files and memories for long running and complex tasks.

Today, it is easy to build agents locally. But how do you take that same power and patterns, and deploy it across an enterprise? How do you make it serve thousands of customer conversations securely? How do you give it an identity, govern its access, and observe what it’s doing at scale?

That’s what Microsoft Foundry is releasing today. Today we’re announcinghosted agentsin Foundry Agent Service, now in public preview. This brings agent-optimized compute and services designed for production-grade enterprise agents. We first previewed hosted agents last year at Microsoft Ignite, but this refresh is a fundamentally different experience: secure per-session sandboxes with filesystem persistence, integrated identity, and scale-to-zero economics.

### What we’re shipping

Hosted agents gives every single agent session its own dedicated, isolated sandbox with a persistent file system. Not process isolation. Not a code execution-only sandbox. Production-proven hypervisor isolation, at cloud scale.

- Predictable cold starts— spin up agent sessions and harnesses in your custom environment virtually instantly

- Scale to zero— pay nothing while your agent is idle, with an agent that will scale down on its own during inactivity

- Resume with filesystem intact— files, disk state, and session identity persist across scale-to-zero events. Your agent restarts with its full working directory exactly where it left off

### A platform built for agents

The problem with traditional compute is that it wasn’t designed for this pattern. Containers, web apps, serverless functions – these were built for web services and APIs where multiple users share the same instance. That’s fine for web apps, but doesn’t work for agents.

When Customer A and Customer B are both calling the same agent — and that agent is writing files, executing code, and accessing credentials on a shared instance — you have a security and isolation nightmare. Agent harnesses need to read and write state. They execute arbitrary code. They hold sensitive context. Sharing a container across sessions isn’t just inefficient, it’s unsafe.

The hard part is no longer writing the agent. The hard part is making it enterprise-ready at scale — with real isolation, real identity, and real governance. That’s our focus with Microsoft Foundry.


## Key Takeaways

1. Agents are already transforming how developers solve problems.
2. Agents of today don’t just execute from a list of tools.
3. Today, it is easy to build agents locally.
4. That’s what Microsoft Foundry is releasing today.
5. Hosted agents gives every single agent session its own dedicated, isolated sandbox with a persistent file system.


## Why This Matters

Developer productivity is one of the highest-ROI applications of AI today. Copilot is proving that AI can augment — not replace — human expertise, making experienced developers more productive and helping newcomers ramp up faster.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

I've seen organizations achieve 30-55% developer productivity gains with Copilot. But the real value isn't just speed — it's reducing cognitive load so developers can focus on architecture and business logic rather than boilerplate. The shift from 'AI writes code for me' to 'AI thinks with me' is where the magic happens.

If you're exploring this area, my advice is to start small — pick one concrete use case, prototype it, and iterate. The tooling has matured significantly, and the barrier to entry has never been lower.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/introducing-the-new-hosted-agents-in-foundry-agent-service-secure-scalable-compute-built-for-agents/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
