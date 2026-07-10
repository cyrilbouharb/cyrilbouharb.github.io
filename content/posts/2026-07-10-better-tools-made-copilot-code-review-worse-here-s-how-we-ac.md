---
title: "Better tools made Copilot code review worse. Here’s how we actually improved it."
date: 2026-07-10
tags: ["Copilot", "GitHub Copilot", "GitHub", "Agent Framework", "Agentic RAG", "AI Agents"]
categories: ["analysis"]
source_url: "https://github.blog/ai-and-ml/github-copilot/better-tools-made-copilot-code-review-worse-heres-how-we-actually-improved-it/"
description: "How migrating Copilot code review to shared Unix-style code exploration tools reduced review cost by reshaping agent workflows around pull request evidence.
The post Better tools made Copilot code rev"
---

There's been an important development in the **GitHub Copilot** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

Give an agent better tools and it should do better work. That’s the instinct, anyway.

When you open a pull request, Copilot code review reads the diff and explores the surrounding code to find the problems that matter before they ship. To do that, it used its own code exploration tools. So when we swapped in the better-maintained, shared tools that power the Copilot CLI,grep,glob, andview, we expected a clean upgrade.

Instead, in our benchmarks, we found that the cost of reviews was higher and fewer issues were being caught.

But the tools weren’t the problem. The instructions were. Once we rewrote them for the way a reviewer actually reads a pull request, the regression flipped into a win:roughly 20% lower average review cost, while maintaining the same review quality.

### Same tools, wrong instincts

If you’ve built on top of an agent framework, you’ve probably inherited its tools too. They work, so you keep them, until the day your use case drifts far enough from what they were designed for that they quietly start working against you. That’s the situation we were in. Before trying to use the shared CLI tools, Copilot code review used its own code exploration tools. That tool layer was inspired by earlier agentic systems, including ideas fromSWE-agent-style repository navigationandGitHub Copilot Autofix: list directories, search files, search directories, and read code. Those tools worked, but they were specific to Copilot code review, and they were designed for how models behaved at the time. Earlier agentic coding models made fewer tool calls and were worse at automatically pulling in necessary context. This meant it was more important to include all relevant information in the few tool calls that the model made.

Meanwhile, the Copilot CLI harness has a shared set of Unix-inspired code exploration tools: grep, glob, and view. That harness is also used by a growing number of Copilot agent products, includingGitHub Copilot cloud agent, so harness improvements can benefit more than one product. We wanted to clean up and share infrastructure where possible, so we experimented with using the tools from the Copilot CLI harness in Copilot code review. The goal was to reduce duplicated tool implementations, create one shared place to improve code exploration tools, and make it easier to carry those improvements across Copilot products.

The existing review tools were not thin wrappers. When searching for a directory or reading a code range, they could return the matched or requested lines plus extra surrounding code context. That added token cost, but it also matched how earlier models often benefited from having nearby context included automatically.

Initially, we hoped this would be a simple migration: swap one set of tools for another. But when we tested the shared tools in offline benchmarks, the review agent became less efficient and less effective. Average cost increased, and the number of useful comments dropped.

### The trace revealed a browsing loop

Our internal Copilot code review benchmarks were useful because they show more than a final score. They show the path the agent took, including which tools it called, how much output came back, where errors happened, and whether it was narrowing toward evidence or widening the search.

When we first tried the shared Copilot CLI tools in offline benchmarks, the agent often behaved as if it was browsing a repository instead of investigating a pull request. It would search broadly, guess likely paths, read broadly, find more things to search, and carry that extra context forward.

That pattern is understandable. Broad exploration can be useful when the task is “understand this repo.” But it’s not how a reviewer would usually review a pull request.

When I review a pull request, I start from the diff and ask targeted questions:


## Key Takeaways

1. Give an agent better tools and it should do better work.
2. When you open a pull request, Copilot code review reads the diff and explores the surrounding code to find the problems that matter before they ship.
3. Instead, in our benchmarks, we found that the cost of reviews was higher and fewer issues were being caught.
4. But the tools weren’t the problem.
5. This is the story of how adjusting the workflows around the tools led us to a fix.


## Why This Matters

Developer productivity is one of the highest-ROI applications of AI today. Copilot is proving that AI can augment — not replace — human expertise, making experienced developers more productive and helping newcomers ramp up faster.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The technical evolution of Copilot is fascinating from an AI systems perspective. We've moved from **completion-based assistance** (predict the next line) to **agent-mode** (understand the intent, decompose the problem, execute multi-file changes, run tests, iterate on failures). This is a fundamental architectural shift — from a stateless token predictor to a stateful reasoning agent with tool use. What's technically impressive is the context management: Copilot now maintains a working memory of your entire codebase, open issues, PR history, and team conventions. The retrieval augmentation layer that grounds suggestions in *your specific codebase* (not just generic patterns) is what makes the difference between a toy and a production tool. The agentic workflows — where Copilot can plan, execute, verify, and self-correct — represent the state of the art in applied AI agents today.


## Business Translation

**For the C-Suite:** Developer talent is the #1 constraint in digital transformation. Copilot delivers a measurable **25-55% productivity gain** (validated by Microsoft/GitHub research across 1M+ developers). In financial terms: a 500-developer organization saves $15-30M annually in equivalent output — without hiring. More importantly, it reduces **time-to-market** for features, which directly impacts revenue capture. The strategic play isn't just efficiency — it's enabling your existing engineering team to tackle projects that were previously impossible given resource constraints.


---

📖 **[Read the original article](https://github.blog/ai-and-ml/github-copilot/better-tools-made-copilot-code-review-worse-heres-how-we-actually-improved-it/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
