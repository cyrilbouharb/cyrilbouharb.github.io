---
title: "GitHub Copilot app for Beginners: Run several agents at once"
date: 2026-09-03
tags: ["Copilot", "GitHub Copilot", "GitHub", "AI Agents"]
categories: ["analysis"]
source_url: "https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-run-several-agents-at-once/"
description: "Learn how to run parallel agents in the GitHub Copilot app, and experience the moment it stops feeling scary and starts feeling powerful.
The post GitHub Copilot app for Beginners: Run several agents "
---

There's been an important development in the **GitHub Copilot** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

Running multiple AI agents on the same project seems like pure chaos, with too many cooks in your development kitchen. But with theGitHub Copilot app, these agents work separately and don’t interfere with each other, allowing you to get more done in less time.

Think of parallel agent sessions like a trip to the laundromat. You can start multiple loads of laundry at the same time, in their own machines. You can set each washer with its own settings, and it won’t impact the other loads. Most importantly, you don’t have to wait for one to finish before you can start another one.

### Agent sessions, Git worktrees, and context

An agent session is a task you’ve given Copilot, start to finish.

In the GitHub Copilot app, you can manage several sessions through the sessions view. Each card shows its title and how far along the agent is in completing its task.

Each session runs independently of the others. That means you can start a new session whenever you want, and the ones already running won’t be disturbed.

But here’s where the real magic happens. Each agent session in the GitHub Copilot app can run on its own Git worktree. Since each session is isolated, they can run in parallel, all at the same time.

### What this looks like

Let’s look at an example repository,tailspin-toys. There are three things I want to do to this project today: add funded sort, perform an accessibility review, and run some tests on this project.

The first step is to ask Copilot to build the funded sort feature. Just as it gets started, open a new session and ask Copilot to perform an accessibility review. As that gets under way, start prompting Copilot to run some tests in a third session.

In the session view, you can keep track of all of these as they progress and review the results as they finish. Or you can step away entirely, grab a cup of coffee, and know your work is happening without you babysitting it.


## Key Takeaways

1. Running multiple AI agents on the same project seems like pure chaos, with too many cooks in your development kitchen.
2. Think of parallel agent sessions like a trip to the laundromat.
3. An agent session is a task you’ve given Copilot, start to finish.
4. In the GitHub Copilot app, you can manage several sessions through the sessions view.
5. Each session runs independently of the others.


## Why This Matters

Developer productivity is one of the highest-ROI applications of AI today. Copilot is proving that AI can augment — not replace — human expertise, making experienced developers more productive and helping newcomers ramp up faster.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The technical evolution of Copilot is fascinating from an AI systems perspective. We've moved from **completion-based assistance** (predict the next line) to **agent-mode** (understand the intent, decompose the problem, execute multi-file changes, run tests, iterate on failures). This is a fundamental architectural shift — from a stateless token predictor to a stateful reasoning agent with tool use. What's technically impressive is the context management: Copilot now maintains a working memory of your entire codebase, open issues, PR history, and team conventions. The retrieval augmentation layer that grounds suggestions in *your specific codebase* (not just generic patterns) is what makes the difference between a toy and a production tool. The agentic workflows — where Copilot can plan, execute, verify, and self-correct — represent the state of the art in applied AI agents today.


## Business Translation

**For the C-Suite:** Developer talent is the #1 constraint in digital transformation. Copilot delivers a measurable **25-55% productivity gain** (validated by Microsoft/GitHub research across 1M+ developers). In financial terms: a 500-developer organization saves $15-30M annually in equivalent output — without hiring. More importantly, it reduces **time-to-market** for features, which directly impacts revenue capture. The strategic play isn't just efficiency — it's enabling your existing engineering team to tackle projects that were previously impossible given resource constraints.


---

📖 **[Read the original article](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-run-several-agents-at-once/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
