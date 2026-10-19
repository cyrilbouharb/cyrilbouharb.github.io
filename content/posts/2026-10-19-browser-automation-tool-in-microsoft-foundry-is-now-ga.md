---
title: "Browser automation tool in Microsoft Foundry is now GA"
date: 2026-10-19
tags: ["Foundry", "Copilot", "GitHub Copilot", "GitHub", "Agent Framework", "Data & AI", "Agentic RAG", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/browser-automation-tool-ga/"
description: "Build agents that automate tasks across public and private websites with managed browsers, native toolbox integration, Live View, and human control.
The post Browser automation tool in Microsoft Found"
---

There's been an important development in the **GitHub Copilot** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

AI agents can reason over data, invoke APIs, and coordinate complex workflows. Yet many business processes still depend on websites, including internal portals, administrative consoles, vendor systems, dashboards, and applications without complete API coverage.

Browser automation tool in Microsoft Foundry is now generally available.Browser automation tool gives agents a managed browser so they can navigate websites, inspect content, complete forms, and perform multistep browser workflows using natural-language instructions.

Powered byPlaywright Workspaces, Browser Automation Tool brings scalable browser infrastructure, enterprise connectivity, observability, and human oversight directly into Microsoft Foundry.

### Browser automation for every Foundry agent

Browser Automation Tool works across the ways developers build agents in Microsoft Foundry:

- Prompt agentsprovide the fastest way to create a browser-enabled agent by configuring its instructions, model, and tools.

- Hosted agentslet developers combine browser automation with custom orchestration built using Microsoft Agent Framework or another framework.

- Github copilot harnesssupport enables builders to have amanaged way to build a complex, long-running agent.

### Connect agents to public and private websites

Enterprise workflows rarely exist entirely on the public internet. Important tasks often involve internal applications, private administrative portals, or services available only through a virtual network.

Browser automation tool enables agents to interact with bothpublic websites and private applications protected behind an Azure virtual network. With Playwright Workspaces private network connectivity, an agent can move across public and internal systems as part of the same workflow while maintaining the organization’s network boundaries. Private network connection should be added while provisioning the Playwright Workspace.

- Processing information across internal and external business portals

- Automating employee onboarding and IT administration workflows


## Key Takeaways

1. AI agents can reason over data, invoke APIs, and coordinate complex workflows.
2. Browser automation tool in Microsoft Foundry is now generally available.Browser automation tool gives agents a managed browser so they can navigate websites, inspect content, complete forms, and perform multistep browser workflows using natural-language instructions.
3. Powered byPlaywright Workspaces, Browser Automation Tool brings scalable browser infrastructure, enterprise connectivity, observability, and human oversight directly into Microsoft Foundry.
4. Browser Automation Tool works across the ways developers build agents in Microsoft Foundry:.
5. Agents interact with pages through an observe-and-act process.


## Why This Matters

Developer productivity is one of the highest-ROI applications of AI today. Copilot is proving that AI can augment — not replace — human expertise, making experienced developers more productive and helping newcomers ramp up faster.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The technical evolution of Copilot is fascinating from an AI systems perspective. We've moved from **completion-based assistance** (predict the next line) to **agent-mode** (understand the intent, decompose the problem, execute multi-file changes, run tests, iterate on failures). This is a fundamental architectural shift — from a stateless token predictor to a stateful reasoning agent with tool use. What's technically impressive is the context management: Copilot now maintains a working memory of your entire codebase, open issues, PR history, and team conventions. The retrieval augmentation layer that grounds suggestions in *your specific codebase* (not just generic patterns) is what makes the difference between a toy and a production tool. The agentic workflows — where Copilot can plan, execute, verify, and self-correct — represent the state of the art in applied AI agents today.


## Business Translation

**For the C-Suite:** Developer talent is the #1 constraint in digital transformation. Copilot delivers a measurable **25-55% productivity gain** (validated by Microsoft/GitHub research across 1M+ developers). In financial terms: a 500-developer organization saves $15-30M annually in equivalent output — without hiring. More importantly, it reduces **time-to-market** for features, which directly impacts revenue capture. The strategic play isn't just efficiency — it's enabling your existing engineering team to tackle projects that were previously impossible given resource constraints.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/browser-automation-tool-ga/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
