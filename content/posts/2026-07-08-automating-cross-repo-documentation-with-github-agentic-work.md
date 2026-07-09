---
title: "Automating cross-repo documentation with GitHub Agentic Workflows"
date: 2026-07-08
tags: ["GitHub", "LLM", "AI Agents"]
categories: ["analysis"]
source_url: "https://github.blog/ai-and-ml/github-copilot/automating-cross-repo-documentation-with-github-agentic-workflows/"
description: "Explore how the Aspire team turns merged product changes into SME-reviewed docs pull requests, closing the gap between release and documentation.
The post Automating cross-repo documentation with GitH"
---

There's been an important development in the **AI Agents** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

“Where are the docs?” It’s a question nobody on a product team enjoys answering. The honest reply is usually some variant of “behind.” A writer is staring at a closed pull request, trying to reverse-engineer what changed. The pull request’s author has already moved on. By the time the doc actually publishes, the feature has shipped, sometimes more than once.

That used to be us on theAspireteam (we’re a small team of 10 building dev tools for distributed apps). A few months back, we were trying to figure out how to safely bring AI into automations we already trusted. That’s when we discovered GitHub Agentic Workflows. I started bolting prototypes intomicrosoft/aspire.

Here’s what that bought us, in numbers pulled straight out of GitHub: for Aspire 13.3 and 13.4,82 feature-docs pull requests merged at a median of 44.8 hours after the product pull request, every one of them reviewed by the engineer who shipped the feature. No new headcount. No process retraining. Just a different way of asking “who writes this?”

### 🔒 The constraint: cross-repo automation is the hard part

Our product lives inmicrosoft/aspireand our docs site lives inmicrosoft/aspire.dev—different repo, deploy target, and review chain. Most teams figure out same-repo automation pretty quickly; cross-repo automation is where things get sharp. Broad repo-scoped tokens belong in a museum, and any responsible security posture (ours included) restricts them accordingly. That’s a good thing. It’s also a real bottleneck if the place where you write the docs isn’t the place where you write the code.

- Engineer ships a feature inmicrosoft/aspire.

- Docs writer opens the pull request, reads the diff, and pings the engineer to clarify what changed.

- Engineer is on the next feature, vaguely remembers, replies with half the picture.

### 🤖 Why GitHub Agentic Workflows

GitHub Agentic Workflows is a project from the GitHub Next team that I keep describing to people as “GitHub Actions, but with a model as the work-item processor and guard rails that satisfy security review.” That’s reductive, but it’s close.

- You author a workflow as asingle markdown file(.github/workflows/my-thing.md). YAML-style frontmatter on top, an English-language prompt underneath.

- You run GitHub Agentic Workflows compile, and it generates a sibling.lock.yml(a normal GitHub Actions workflow) that you commit alongside.

- At runtime, the workflow runs an agent against your prompt with a constrained toolset.


## Key Takeaways

1. “Where are the docs?” It’s a question nobody on a product team enjoys answering.
2. That used to be us on theAspireteam (we’re a small team of 10 building dev tools for distributed apps).
3. Here’s what that bought us, in numbers pulled straight out of GitHub: for Aspire 13.3 and 13.4,82 feature-docs pull requests merged at a median of 44.8 hours after the product pull request, every one of them reviewed by the engineer who shipped the feature.
4. Our product lives inmicrosoft/aspireand our docs site lives inmicrosoft/aspire.dev—different repo, deploy target, and review chain.
5. This is the reverse-engineering tax.


## Why This Matters

Agentic AI is where the industry is heading. From code generation to customer service to data analysis, agents can handle multi-step workflows that previously required human intervention at every stage. This isn't just automation — it's a fundamentally new way of building software.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The technical frontier in AI agents right now is the **orchestration problem** — how do you reliably coordinate multiple specialized agents, each with different capabilities and knowledge, to solve complex tasks? The key architectural patterns emerging are: **handoff protocols** (A2A for cross-platform agent communication), **governance layers** (constraining agent actions within policy boundaries without killing autonomy), and **state management** (maintaining coherent context as work passes between agents). What I find most technically interesting is the convergence of **code-generating agents** (Copilot, Codex) with **tool-using agents** (function calling, MCP) — agents that can both write *and* execute code create a self-improving loop that's qualitatively different from static automation. The challenge is reliability: current agents succeed ~70-85% on complex tasks. Getting to 99%+ requires better evaluation frameworks, graceful degradation patterns, and human-in-the-loop checkpoints for high-stakes decisions.


## Business Translation

**For the C-Suite:** AI agents represent the next wave of operational leverage — not just automating tasks, but automating *judgment*. Early adopters are seeing **40-70% reduction in operational costs** for knowledge work (customer service, compliance review, data analysis). The strategic question isn't whether to adopt agents, but where to deploy them first for maximum ROI. The playbook: start with high-volume, medium-complexity workflows where errors are recoverable (customer inquiries, internal operations), then expand to higher-stakes domains as confidence grows. The organizations that build agent infrastructure now will have a 2-3 year head start when the technology matures.


---

📖 **[Read the original article](https://github.blog/ai-and-ml/github-copilot/automating-cross-repo-documentation-with-github-agentic-workflows/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
