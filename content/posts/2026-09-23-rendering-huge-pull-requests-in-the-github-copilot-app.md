---
title: "Rendering huge pull requests in the GitHub Copilot app"
date: 2026-09-23
tags: ["Copilot", "GitHub Copilot", "GitHub", "Data & AI", "Agentic RAG", "Architecture"]
categories: ["analysis"]
source_url: "https://github.blog/engineering/user-experience/rendering-huge-pull-requests-in-the-github-copilot-app/"
description: "How we rebuilt the diff surface in the GitHub Copilot app to open a million-line pull request with hundreds of inline review comments.
The post Rendering huge pull requests in the GitHub Copilot app a"
---

There's been an important development in the **GitHub Copilot** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

Broad refactors and migrations often have to land as one change.

Stacked pull requestsare a great way to split work into smaller changes, which makes reviews easier and helps teams ship with less risk. But some changes, like this one, can’t be split cleanly. That leaves you with a single pull request that can get very large, and the review conversation causes it to grow.

The review experience needs to remain fast and smooth even when the diff and its conversation are enormous. In theGitHub Copilot app, we rebuilt the pull request view with that requirement in mind.

To see how far that goes, we opened the biggest pull request we could find: an open source one with 2,200 files, over a million changed lines, and more than 400 inline review comments. Here’s how we made even this extreme pull request performant.

### The scope of the problem

Rendering a large diff at speed is well-understood: virtualize the rows, keep the mounted DOM small, and lean on the fact that every row is a line of code at a known height.

Comments are the hard part. A comment’s height depends on how its markdown wraps, the expandable sections, whether there’s a reply box in it, and whether its images have loaded yet. You find all of that out at render time. This forces a different architecture.

- Measurement.You can’t know how tall a comment is until you render it. This breaks the design that lets big diffs stay responsive as you scroll.

- The data pipeline.A fast diff surface is worthless if the data pipeline feeding it stalls, or if it throws away work it already did.

### Part 1: Virtualization, and why comments break it

The first step is to understand the geometry that makes a code-only diff fast. Once comments enter the picture, that geometry is no longer enough.


## Key Takeaways

1. Broad refactors and migrations often have to land as one change.
2. Stacked pull requestsare a great way to split work into smaller changes, which makes reviews easier and helps teams ship with less risk.
3. The review experience needs to remain fast and smooth even when the diff and its conversation are enormous.
4. To see how far that goes, we opened the biggest pull request we could find: an open source one with 2,200 files, over a million changed lines, and more than 400 inline review comments.
5. Rendering a large diff at speed is well-understood: virtualize the rows, keep the mounted DOM small, and lean on the fact that every row is a line of code at a known height.


## Why This Matters

Developer productivity is one of the highest-ROI applications of AI today. Copilot is proving that AI can augment — not replace — human expertise, making experienced developers more productive and helping newcomers ramp up faster.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The technical evolution of Copilot is fascinating from an AI systems perspective. We've moved from **completion-based assistance** (predict the next line) to **agent-mode** (understand the intent, decompose the problem, execute multi-file changes, run tests, iterate on failures). This is a fundamental architectural shift — from a stateless token predictor to a stateful reasoning agent with tool use. What's technically impressive is the context management: Copilot now maintains a working memory of your entire codebase, open issues, PR history, and team conventions. The retrieval augmentation layer that grounds suggestions in *your specific codebase* (not just generic patterns) is what makes the difference between a toy and a production tool. The agentic workflows — where Copilot can plan, execute, verify, and self-correct — represent the state of the art in applied AI agents today.


## Business Translation

**For the C-Suite:** Developer talent is the #1 constraint in digital transformation. Copilot delivers a measurable **25-55% productivity gain** (validated by Microsoft/GitHub research across 1M+ developers). In financial terms: a 500-developer organization saves $15-30M annually in equivalent output — without hiring. More importantly, it reduces **time-to-market** for features, which directly impacts revenue capture. The strategic play isn't just efficiency — it's enabling your existing engineering team to tackle projects that were previously impossible given resource constraints.


---

📖 **[Read the original article](https://github.blog/engineering/user-experience/rendering-huge-pull-requests-in-the-github-copilot-app/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
