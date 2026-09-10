---
title: "What’s new in Microsoft Foundry: July and August 2026"
date: 2026-09-09
tags: ["Foundry", "Copilot", "GitHub Copilot", "GitHub", "OpenAI", "LLM", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-july-august-2026/"
description: "Catch up on July and August in Microsoft Foundry: stable Hosted Agent and Toolbox SDK paths, Claude tools on Azure-hosted deployments, Model Router updates, local inference improvements, and the SDK m"
---

There's been an important development in the **GitHub Copilot** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

Microsoft Foundry’s July and August 2026 updates make Hosted Agents, Voice Live integration, and Toolboxes generally available; expand Claude tools hosted on Azure; update Model Router’s regions and model pool; add Foundry Local capabilities; and advance the Python, JavaScript, Java, and .NET SDKs.

> Author’s note: After a long summer break and a small US holiday, we have a lot to catch up on! I’ve brought July and August’s Foundry updates together in one roundup, with code examples and migration notes to help you get started.

Author’s note: After a long summer break and a small US holiday, we have a lot to catch up on! I’ve brought July and August’s Foundry updates together in one roundup, with code examples and migration notes to help you get started.

### TL;DR

Hosted Agents, Voice Live integration, and Toolboxes are now generally available, giving developers a managed runtime for agent code, real-time voice, and reusable tools managed outside the agent. Claude deployments hosted on Azure add structured outputs, Web search, Web fetch, MCP connector, and Tool search, with the MCP connector using the beta API. Model Router adds regions, refreshes its routing pool with GPT-5.6 variants and Claude Opus 4.8, and expands agentic routing to eligible Anthropic and open-source models. Foundry Local on Azure Local extension2607adds preview model evaluation, vLLM model parallelism, and improved automatic GPU inference tuning, while Foundry DevPack0.1.3provides preview installers for Windows, macOS, and Linux on x64 and Arm64. By the end of August, the Python and JavaScript/TypeScript SDKs had reached stable version2.5.0and Java2.4.0; the .NET3.0.0line remained in preview, with hosted-agent management and runtime support differing by language.

### Join the community

Which July or August update should we cover with a deeper implementation example? Share what you are building—or where you are blocked—inDiscordorGitHub Discussions, andsubscribe via RSSfor the next roundup.


## Key Takeaways

1. Microsoft Foundry’s July and August 2026 updates make Hosted Agents, Voice Live integration, and Toolboxes generally available; expand Claude tools hosted on Azure; update Model Router’s regions and model pool; add Foundry Local capabilities; and advance the Python, JavaScript, Java, and .NET SDKs.
2. Author’s note: After a long summer break and a small US holiday, we have a lot to catch up on! I’ve brought July and August’s Foundry updates together in one roundup, with code examples and migration notes to help you get started.
3. Hosted Agents, Voice Live integration, and Toolboxes are now generally available, giving developers a managed runtime for agent code, real-time voice, and reusable tools managed outside the agent.
4. Which July or August update should we cover with a deeper implementation example? Share what you are building—or where you are blocked—inDiscordorGitHub Discussions, andsubscribe via RSSfor the next roundup.
5. Build agents with your preferred framework and run them in Foundry’s managed runtime.


## Why This Matters

Developer productivity is one of the highest-ROI applications of AI today. Copilot is proving that AI can augment — not replace — human expertise, making experienced developers more productive and helping newcomers ramp up faster.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The technical evolution of Copilot is fascinating from an AI systems perspective. We've moved from **completion-based assistance** (predict the next line) to **agent-mode** (understand the intent, decompose the problem, execute multi-file changes, run tests, iterate on failures). This is a fundamental architectural shift — from a stateless token predictor to a stateful reasoning agent with tool use. What's technically impressive is the context management: Copilot now maintains a working memory of your entire codebase, open issues, PR history, and team conventions. The retrieval augmentation layer that grounds suggestions in *your specific codebase* (not just generic patterns) is what makes the difference between a toy and a production tool. The agentic workflows — where Copilot can plan, execute, verify, and self-correct — represent the state of the art in applied AI agents today.


## Business Translation

**For the C-Suite:** Developer talent is the #1 constraint in digital transformation. Copilot delivers a measurable **25-55% productivity gain** (validated by Microsoft/GitHub research across 1M+ developers). In financial terms: a 500-developer organization saves $15-30M annually in equivalent output — without hiring. More importantly, it reduces **time-to-market** for features, which directly impacts revenue capture. The strategic play isn't just efficiency — it's enabling your existing engineering team to tackle projects that were previously impossible given resource constraints.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-july-august-2026/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
