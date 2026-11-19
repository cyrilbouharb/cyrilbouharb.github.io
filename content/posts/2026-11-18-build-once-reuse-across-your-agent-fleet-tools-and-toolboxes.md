---
title: "Build once, reuse across your agent fleet: Tools and Toolboxes in Foundry"
date: 2026-11-18
tags: ["Foundry", "Copilot", "GitHub Copilot", "GitHub", "OpenAI", "Microsoft Fabric", "Data & AI", "Data & Analytics", "Foundry IQ", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/build-once-reuse-across-your-agent-fleet-tools-and-toolboxes-in-foundry/"
description: "Connecting one tool to one agent is not hard. The challenge is managing a useful set of tools and agentic capabilities across a fleet of production agents at scale. Every new agent shouldn&#8217;t req"
---

There's been an important development in the **GitHub Copilot** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

Connecting one tool to one agent is not hard. The challenge is managing a useful set of tools and agentic capabilities across a fleet of production agents at scale. Every new agent shouldn’t require you to build the same integrations, copy the same instructions, and troubleshoot the same dependencies. And adding a useful capability shouldn’t require a separate rollout in every agent application.

Toolboxesin Microsoft Foundry turn tools,skills, and agents into shared capabilities. Curate and version them in Foundry, expose them through one MCP endpoint, and reuse them across Foundry agents and other MCP-compatible frameworks and runtimes. Toolbox centralizes downstream authentication, so each agent connects to the toolbox instead of managing credentials for every tool.Tool search in Toolboxlets agents discover the tools they need on demand, so the shared catalog can grow without filling the context window with every tool definition.

At Ignite, we are excited to launch the following enhancements:

- Skills support expanded:Manage skills with the Skills CRUD API (GA, coming soon), and execute skills in prompt agent viaShell tool(preview). Toolbox will also expose skills through the officialMCP Skills extensionfor use across compatible agents and frameworks.

### Customer Story

“The real value of AI agents comes from giving them the right tools and skills to act on the information around them. In our systems, we have worked with Microsoft to bring Toolboxes and Skills together with our operational data and business systems, enabling our agents to find information, generate insights and support our teams more effectively across daily operations.”From Ahmed AbdulJalil Ebrahim, Manager Digital Innovation & Process Management, Gulf Air

### Build: give agents the context, expertise, and execution they need

A useful toolbox gives agents the capabilities to find information, apply expertise, and take action. Combine Web Search powered by Web IQ for current web information, skills for task-specific expertise, Fabric IQ for business data and semantics, and Work IQ for organizational context through the unified Microsoft IQ endpoint.


## Key Takeaways

1. Connecting one tool to one agent is not hard.
2. Toolboxesin Microsoft Foundry turn tools,skills, and agents into shared capabilities.
3. At Ignite, we are excited to launch the following enhancements:.
4. “The real value of AI agents comes from giving them the right tools and skills to act on the information around them.
5. A useful toolbox gives agents the capabilities to find information, apply expertise, and take action.


## Why This Matters

Developer productivity is one of the highest-ROI applications of AI today. Copilot is proving that AI can augment — not replace — human expertise, making experienced developers more productive and helping newcomers ramp up faster.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The technical evolution of Copilot is fascinating from an AI systems perspective. We've moved from **completion-based assistance** (predict the next line) to **agent-mode** (understand the intent, decompose the problem, execute multi-file changes, run tests, iterate on failures). This is a fundamental architectural shift — from a stateless token predictor to a stateful reasoning agent with tool use. What's technically impressive is the context management: Copilot now maintains a working memory of your entire codebase, open issues, PR history, and team conventions. The retrieval augmentation layer that grounds suggestions in *your specific codebase* (not just generic patterns) is what makes the difference between a toy and a production tool. The agentic workflows — where Copilot can plan, execute, verify, and self-correct — represent the state of the art in applied AI agents today.


## Business Translation

**For the C-Suite:** Developer talent is the #1 constraint in digital transformation. Copilot delivers a measurable **25-55% productivity gain** (validated by Microsoft/GitHub research across 1M+ developers). In financial terms: a 500-developer organization saves $15-30M annually in equivalent output — without hiring. More importantly, it reduces **time-to-market** for features, which directly impacts revenue capture. The strategic play isn't just efficiency — it's enabling your existing engineering team to tackle projects that were previously impossible given resource constraints.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/build-once-reuse-across-your-agent-fleet-tools-and-toolboxes-in-foundry/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
