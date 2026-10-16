---
title: "What’s new in Microsoft Foundry | September 2026"
date: 2026-10-16
tags: ["Foundry", "Copilot", "GitHub Copilot", "GitHub", "OpenAI", "Agent Framework", "Data & AI", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-september-2026/"
description: "Explore September's models, Routines, Tool Search, Model Router, and Insights through one two-agent workflow that turns public releases into a Foundry developer changelog.
The post What&#8217;s new in"
---

There's been an important development in the **GitHub Copilot** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

September’s updates help you run agents on a schedule, load tool definitions on demand, and investigate behavior from traces. Routines and Tool Search are now GA; Insights enters public preview, and Model Router gains preview controls. We also expanded the GPT-6 lineup and introduced GPT-6.1 Sol.

Jump toFoundry Models,Agents & Foundry Agent Service,Speech & Content Understanding,Foundry Local,developer tools, APIs, SDKs, and CLI,pricing and model retirements, orresources and community.

### TL;DR

- GPT-6 Astra, GPT-6.1 Sol, and GPT-6 Luna are generally available (GA).Compare quality and cost per task using a supported serving option.

- Routines are GA.Run agents on a timer, schedule, or supported GitHub or Teams event. The agent-scheduled reminder tool remains preview.

- Tool Search and Agent-to-Agent (A2A) are GA.Hosted-agent Toolboxes remain GA; prompt-agent Toolboxes enter public preview.

- Voice agents and long-running hosted-agent resilience enter public preview.Try spoken interactions or recoverable background tasks.

### GPT-6 and GPT-6.1 Sol are generally available (GA)

We expanded the GPT lineup throughout September:

Prices are September-announced USD rates per 1M tokens for Global Standard short-context requests. Long-context rates are higher.Check current pricing.

*TheGPT-6.1 Sol launchreports better coding, computer use, and professional work than GPT-6 Sol at thesame uncached-input and output prices, with 50% lower cached-input pricing.

All three models in the GPT-6 model family have a1.05M-token context windowand up to128K output tokens, including reasoning, within one shared budget. They support Responses, Chat Completions, streaming, function calling, structured outputs, and image input with text output. Knowledge cutoffs: April 2026 for Astra and GPT-6.1 Sol; May 2026 for Luna. GPT-6.1 Sol tool calls require Responses.Model specifications.


## Key Takeaways

1. September’s updates help you run agents on a schedule, load tool definitions on demand, and investigate behavior from traces.
2. Jump toFoundry Models,Agents & Foundry Agent Service,Speech & Content Understanding,Foundry Local,developer tools, APIs, SDKs, and CLI,pricing and model retirements, orresources and community.
3. See what’s new in Foundry and how to put it to work.The Handoffis my weekly live show with Foundry updates, demos, and Q&A with special guests.
4. Prices are September-announced USD rates per 1M tokens for Global Standard short-context requests.
5. *TheGPT-6.1 Sol launchreports better coding, computer use, and professional work than GPT-6 Sol at thesame uncached-input and output prices, with 50% lower cached-input pricing.


## Why This Matters

Developer productivity is one of the highest-ROI applications of AI today. Copilot is proving that AI can augment — not replace — human expertise, making experienced developers more productive and helping newcomers ramp up faster.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The technical evolution of Copilot is fascinating from an AI systems perspective. We've moved from **completion-based assistance** (predict the next line) to **agent-mode** (understand the intent, decompose the problem, execute multi-file changes, run tests, iterate on failures). This is a fundamental architectural shift — from a stateless token predictor to a stateful reasoning agent with tool use. What's technically impressive is the context management: Copilot now maintains a working memory of your entire codebase, open issues, PR history, and team conventions. The retrieval augmentation layer that grounds suggestions in *your specific codebase* (not just generic patterns) is what makes the difference between a toy and a production tool. The agentic workflows — where Copilot can plan, execute, verify, and self-correct — represent the state of the art in applied AI agents today.


## Business Translation

**For the C-Suite:** Developer talent is the #1 constraint in digital transformation. Copilot delivers a measurable **25-55% productivity gain** (validated by Microsoft/GitHub research across 1M+ developers). In financial terms: a 500-developer organization saves $15-30M annually in equivalent output — without hiring. More importantly, it reduces **time-to-market** for features, which directly impacts revenue capture. The strategic play isn't just efficiency — it's enabling your existing engineering team to tackle projects that were previously impossible given resource constraints.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-september-2026/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
