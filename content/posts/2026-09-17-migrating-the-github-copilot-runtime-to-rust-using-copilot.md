---
title: "Migrating the GitHub Copilot runtime to Rust, using Copilot"
date: 2026-09-17
tags: ["Copilot", "GitHub Copilot", "GitHub", "Agentic RAG", "Architecture", "AI Agents"]
categories: ["analysis"]
source_url: "https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/"
description: "A rewrite this size wasn't affordable before agents. Here's what porting the Copilot agent runtime to 800,000 lines of production Rust actually took.
The post Migrating the GitHub Copilot runtime to R"
---

There's been an important development in the **GitHub Copilot** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

TheGitHub Copilot CLI,GitHub Copilot app, andGitHub Copilot SDKare all backed by the Copilot agent runtime, an agentic harness that can be embedded into applications and services. It was originally written in TypeScript on Node.js and the V8 JavaScript engine for what is now theGitHub Copilot cloud agent(CCA), and the runtime stayed on that stack as the runtime and its capabilities grew rapidly.

That has now changed. Using the GitHub Copilot app and the Copilot CLI, we completely rewrote the runtime into more than 800,000 lines of production Rust. AI agents wrote most of the code, spanning 128 pull requests that landed in main and shipped incrementally rather than waiting for a single cutover at the end. The few inevitable regressions were discovered and fixed quickly along the way, while the performance of the runtime improved by orders of magnitude. A project that would have taken a whole team of developers a year or two before agents was now completed primarily by a single developer, in only a few months, all while the rest of the team continued to greatly expand the runtime’s capabilities and reach.

### Why we needed to port

The Copilot agent runtime isn’t just the engine behind the Copilot CLI. It backs a growing set of Microsoft, GitHub, and ecosystem solutions, for each of which AI support is, architecturally, a shell around the same runtime plus whatever customizations that solution needs. This includes not only the GitHub Copilot CLI and the GitHub Copilot app, but also the latest releases of VS Code, Visual Studio, CCA, Copilot Code Review (CCR), Copilot Cowork, Copilot Studio, and Excel and Outlook and PowerPoint and Word and… it goes on.

These are very different products, and none of them wants to or should need to implement everything that goes into a production agent harness. They want all of the intelligence, security, reliability, and performance, and they want it shared so that a fix in one place fixes it in all of them. Most of the products listed in the previous paragraph initially implemented their own agent loop, but have since replaced it with the GitHub Copilot SDK, which is the entry point to the Copilot agent runtime. Doing so enables them to focus on their core business value and leave the details to the runtime. That’s all the more important given the pace of the industry and the employed agent loop needing to stay always best-of-breed in the face of intense competition.

So, shared runtime, good. The problem was the nature of the thing being shared.

If we look at the CLI, it’s logically a terminal UI (TUI) on top of an agent loop. As it happened, the whole stack was implemented in TypeScript, using Node.js as the framework and V8 for the execution engine, with Ink and React for UI. That’s a respectable choice for a TUI application; TypeScript and Node.js are broadly accessible and enable very rapid application development. And for the needs of a console application, the performance implications in terms of startup, responsiveness, throughput, and memory consumption are also reasonable. They are, unfortunately, much less reasonable when you think about that implementation being used in other environments, with other constraints, with demands for things like fast startup and excellent server density due to low memory overhead.

### What it looked like before

The initial porting plan in early May 2026 estimated the runtime at roughly 130,000 lines of TypeScript. For scoping purposes, this initial measurement was reasonably accurate, but, as it turned out, also wildly misleading, in two key ways. Concurrent with porting:

- Pieces still wrapped up in the TUI layer were being pushed down to the runtime layer. Entire components and significant percentages of code initially ignored in the estimates were then later considered relevant to porting.

- Pull requests contributing significant amounts of new TypeScript were constantly raising the amount of TypeScript in the repo. Tens of agentically assisted developers merging hundreds of pull requests per week.

Everything factored in, I estimate approximately 430,000 lines of production TypeScript ended up passing through the port. Those same factors also made it hard to see progress along the way: until close to the end, production TypeScript volume appeared to be holding relatively steady, if not increasing slightly, as porting kept pace with incoming work.


## Key Takeaways

1. TheGitHub Copilot CLI,GitHub Copilot app, andGitHub Copilot SDKare all backed by the Copilot agent runtime, an agentic harness that can be embedded into applications and services.
2. The Copilot agent runtime isn’t just the engine behind the Copilot CLI.
3. These are very different products, and none of them wants to or should need to implement everything that goes into a production agent harness.
4. If we look at the CLI, it’s logically a terminal UI (TUI) on top of an agent loop.
5. The architecture of the CLI and its runtime also contributed to challenges here.


## Why This Matters

Developer productivity is one of the highest-ROI applications of AI today. Copilot is proving that AI can augment — not replace — human expertise, making experienced developers more productive and helping newcomers ramp up faster.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The technical evolution of Copilot is fascinating from an AI systems perspective. We've moved from **completion-based assistance** (predict the next line) to **agent-mode** (understand the intent, decompose the problem, execute multi-file changes, run tests, iterate on failures). This is a fundamental architectural shift — from a stateless token predictor to a stateful reasoning agent with tool use. What's technically impressive is the context management: Copilot now maintains a working memory of your entire codebase, open issues, PR history, and team conventions. The retrieval augmentation layer that grounds suggestions in *your specific codebase* (not just generic patterns) is what makes the difference between a toy and a production tool. The agentic workflows — where Copilot can plan, execute, verify, and self-correct — represent the state of the art in applied AI agents today.


## Business Translation

**For the C-Suite:** Developer talent is the #1 constraint in digital transformation. Copilot delivers a measurable **25-55% productivity gain** (validated by Microsoft/GitHub research across 1M+ developers). In financial terms: a 500-developer organization saves $15-30M annually in equivalent output — without hiring. More importantly, it reduces **time-to-market** for features, which directly impacts revenue capture. The strategic play isn't just efficiency — it's enabling your existing engineering team to tackle projects that were previously impossible given resource constraints.


---

📖 **[Read the original article](https://github.blog/ai-and-ml/generative-ai/migrating-the-github-copilot-runtime-to-rust-using-copilot/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
