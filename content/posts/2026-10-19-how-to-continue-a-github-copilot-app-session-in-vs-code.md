---
title: "How to continue a GitHub Copilot app session in VS Code"
date: 2026-10-19
tags: ["Copilot", "GitHub Copilot", "GitHub", "AI Agents"]
categories: ["analysis"]
source_url: "https://github.blog/ai-and-ml/github-copilot/how-to-continue-a-github-copilot-app-session-in-vs-code/"
description: "Learn how to move an agent session from the GitHub Copilot app into VS Code without losing the conversation, code changes, or working context.
The post How to continue a GitHub Copilot app session in "
---

There's been an important development in the **GitHub Copilot** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

The agent has finished the bulk of your change. Now you want to inspect one implementation detail, adjust a few lines by hand, and run the project locally before you ship it.

But the work is sitting in theGitHub Copilot app… and your editor is where you review diffs, debug code, and make final adjustments. Do you have to choose between staying in the session and starting over in Visual Studio Code?

You don’t. You can open the Copilot app session directly in VS Code and continue with its conversation, code changes, and working context intact. That means Copilot can handle the repetitive or time-consuming work, then hand control back to you for closer review, hands-on editing, and local testing.

- Review the agent’s changes line by line.

### Prerequisites

- The GitHub Copilot app installed and signed in.

- Visual Studio Code installedand connected to the same GitHub account.

- A Copilot app session with code changes you want to review or continue.

- Permission to work in and push changes to the session’s repository.

### 1. Start with a session in the Copilot app

Open the session you want to continue. Before handing it off, take a moment to review the task and the work Copilot completed.

A session contains more than a collection of modified files. It also records the task, the plan, and the conversation that produced those changes. That context is important when you want to understand why Copilot chose a particular implementation or ask it to revise part of the work.

You do not need to summarize that history or copy it into a new chat before moving to VS Code.


## Key Takeaways

1. The agent has finished the bulk of your change.
2. But the work is sitting in theGitHub Copilot app… and your editor is where you review diffs, debug code, and make final adjustments.
3. This tutorial assumes you are already comfortable navigating VS Code, running commands in its integrated terminal, and working with Git branches and pull requests.
4. Open the session you want to continue.
5. A session contains more than a collection of modified files.


## Why This Matters

Developer productivity is one of the highest-ROI applications of AI today. Copilot is proving that AI can augment — not replace — human expertise, making experienced developers more productive and helping newcomers ramp up faster.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The technical evolution of Copilot is fascinating from an AI systems perspective. We've moved from **completion-based assistance** (predict the next line) to **agent-mode** (understand the intent, decompose the problem, execute multi-file changes, run tests, iterate on failures). This is a fundamental architectural shift — from a stateless token predictor to a stateful reasoning agent with tool use. What's technically impressive is the context management: Copilot now maintains a working memory of your entire codebase, open issues, PR history, and team conventions. The retrieval augmentation layer that grounds suggestions in *your specific codebase* (not just generic patterns) is what makes the difference between a toy and a production tool. The agentic workflows — where Copilot can plan, execute, verify, and self-correct — represent the state of the art in applied AI agents today.


## Business Translation

**For the C-Suite:** Developer talent is the #1 constraint in digital transformation. Copilot delivers a measurable **25-55% productivity gain** (validated by Microsoft/GitHub research across 1M+ developers). In financial terms: a 500-developer organization saves $15-30M annually in equivalent output — without hiring. More importantly, it reduces **time-to-market** for features, which directly impacts revenue capture. The strategic play isn't just efficiency — it's enabling your existing engineering team to tackle projects that were previously impossible given resource constraints.


---

📖 **[Read the original article](https://github.blog/ai-and-ml/github-copilot/how-to-continue-a-github-copilot-app-session-in-vs-code/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
