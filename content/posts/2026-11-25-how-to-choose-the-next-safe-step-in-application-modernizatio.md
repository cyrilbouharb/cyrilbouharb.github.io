---
title: "How to choose the next safe step in application modernization"
date: 2026-11-25
tags: ["Copilot", "GitHub Copilot", "GitHub", "Data & AI", "Architecture", "AI Agents"]
categories: ["analysis"]
source_url: "https://github.blog/ai-and-ml/github-copilot/how-to-choose-the-next-safe-step-in-application-modernization/"
description: "Learn how to assess a legacy application, choose a bounded modernization step, and reuse the method with a GitHub Copilot agent skill.
The post How to choose the next safe step in application moderniz"
---

There's been an important development in the **GitHub Copilot** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

A request to modernize an application often starts with a technology question: Which framework should replace the old one? Before you choose, find out what still works. Then collect evidence that can act as a regression net for that behavior and show where modernization is necessary.

I used an evidence-first method on four public applications, from a small Node.js game to a large Java enterprise resource planning (ERP) application. Each needed a different treatment, but the way I collected evidence, chose the next experiment, and decided on possible proof points was repeatable.

This post walks through that process so you can apply it to one application of your own. It also shows how to encode the procedure in aGitHub Copilot agent skillwhile keeping architectural judgment with the people responsible for the system.

### Build evidence before choosing a target

The label on an application rarely tells you enough. “Java microservices” doesn’t tell you which Java Development Kit (JDK) runs in production, where that version is pinned, whether the tests execute, or which interfaces other systems depend on. “Legacy monolith” doesn’t tell you whether the business core is broken or whether one retired platform dependency prevents the application from starting.

Before you recommend a change, build a small evidence inventory:

- Manifests, lockfiles, entry points, and deployable components

- Verified commands for installing, building, testing, packaging, and running

### Choose the least disruptive treatment that works

Once you understand the application, make the decision per component. A single system can contain code that should stay, dependencies that should be swapped, and one subsystem that genuinely needs a rewrite.

First, check whether a capability is still needed. Remove it only after verifying that it is unused or superseded and confirming that decision with its owner. Removal is a separate decision, and it’s not necessarily the most disruptive one.

For a capability you still need, start with the option that changes the least:

- Keep it.Supported code that still fits the job doesn’t need a modernization story.


## Key Takeaways

1. A request to modernize an application often starts with a technology question: Which framework should replace the old one? Before you choose, find out what still works.
2. I used an evidence-first method on four public applications, from a small Node.js game to a large Java enterprise resource planning (ERP) application.
3. This post walks through that process so you can apply it to one application of your own.
4. The label on an application rarely tells you enough.
5. Before you recommend a change, build a small evidence inventory:.


## Why This Matters

Developer productivity is one of the highest-ROI applications of AI today. Copilot is proving that AI can augment — not replace — human expertise, making experienced developers more productive and helping newcomers ramp up faster.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The technical evolution of Copilot is fascinating from an AI systems perspective. We've moved from **completion-based assistance** (predict the next line) to **agent-mode** (understand the intent, decompose the problem, execute multi-file changes, run tests, iterate on failures). This is a fundamental architectural shift — from a stateless token predictor to a stateful reasoning agent with tool use. What's technically impressive is the context management: Copilot now maintains a working memory of your entire codebase, open issues, PR history, and team conventions. The retrieval augmentation layer that grounds suggestions in *your specific codebase* (not just generic patterns) is what makes the difference between a toy and a production tool. The agentic workflows — where Copilot can plan, execute, verify, and self-correct — represent the state of the art in applied AI agents today.


## Business Translation

**For the C-Suite:** Developer talent is the #1 constraint in digital transformation. Copilot delivers a measurable **25-55% productivity gain** (validated by Microsoft/GitHub research across 1M+ developers). In financial terms: a 500-developer organization saves $15-30M annually in equivalent output — without hiring. More importantly, it reduces **time-to-market** for features, which directly impacts revenue capture. The strategic play isn't just efficiency — it's enabling your existing engineering team to tackle projects that were previously impossible given resource constraints.


---

📖 **[Read the original article](https://github.blog/ai-and-ml/github-copilot/how-to-choose-the-next-safe-step-in-application-modernization/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
