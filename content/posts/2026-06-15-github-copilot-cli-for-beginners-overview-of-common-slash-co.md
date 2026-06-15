---
title: "GitHub Copilot CLI for Beginners: Overview of common slash commands"
date: 2026-06-15
tags: ["Copilot", "GitHub Copilot", "GitHub"]
categories: ["analysis"]
source_url: "https://github.blog/ai-and-ml/github-copilot/github-copilot-cli-for-beginners-overview-of-common-slash-commands/"
description: "GitHub Copilot CLI for Beginners: Learn how to use slash commands to control your terminal AI agent.
The post GitHub Copilot CLI for Beginners: Overview of common slash commands appeared first on The "
---

There's been an important development in the **GitHub Copilot** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

Welcome back to GitHub Copilot CLI for Beginners! In this series (available invideoandblogformat), we’ll give you everything you need to get started usingGitHub Copilot CLI. So far in this series, we’ve coveredhow to get startedandwhen to use interactive and non-interactive modes. In this edition, we’ll learn what slash commands are, why they matter, and how to use slash commands to control GitHub Copilot efficiently. You can complete tasks like switching models, checking token usage, and resuming past sessions right from your terminal.

### Understanding slash commands in GitHub Copilot CLI

When working in Copilot CLI, one of the most powerful concepts to learn early on isslash commands.Slash commands are built-in controls that you can access directly from the command line. Acting as your control surface within Copilot CLI, slash commands allow you to:

- Move efficiently across sessions and projects

Slash commands can be thought of as your command center for interacting with Copilot CLI. To look at all of the options available, just type/in the command line for a scrollable list of all currently supported slash commands.

Let’s take a look at some of the most popular ones.

### Choosing the right model

Different models are optimized for different kinds of work. If you want to switch models, type/modelinto the command line. This will display a list of available models, along with key details like:

- Capabilities: Some are better for quick, lightweight tasks like refactoring, while others more efficiently handle deeper reasoning such as feature planning.

- Availability: The list may vary depending on your plan or organization’s settings.

- Cost: Numbers shown on the right of each model indicate cost multiplier, helping you choose the right balance between performance and usage in relation to your plan.


## Key Takeaways

1. Welcome back to GitHub Copilot CLI for Beginners! In this series (available invideoandblogformat), we’ll give you everything you need to get started usingGitHub Copilot CLI.
2. When working in Copilot CLI, one of the most powerful concepts to learn early on isslash commands.Slash commands are built-in controls that you can access directly from the command line.
3. Slash commands can be thought of as your command center for interacting with Copilot CLI.
4. Let’s take a look at some of the most popular ones.
5. Different models are optimized for different kinds of work.


## Why This Matters

Developer productivity is one of the highest-ROI applications of AI today. Copilot is proving that AI can augment — not replace — human expertise, making experienced developers more productive and helping newcomers ramp up faster.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The technical evolution of Copilot is fascinating from an AI systems perspective. We've moved from **completion-based assistance** (predict the next line) to **agent-mode** (understand the intent, decompose the problem, execute multi-file changes, run tests, iterate on failures). This is a fundamental architectural shift — from a stateless token predictor to a stateful reasoning agent with tool use. What's technically impressive is the context management: Copilot now maintains a working memory of your entire codebase, open issues, PR history, and team conventions. The retrieval augmentation layer that grounds suggestions in *your specific codebase* (not just generic patterns) is what makes the difference between a toy and a production tool. The agentic workflows — where Copilot can plan, execute, verify, and self-correct — represent the state of the art in applied AI agents today.


## Business Translation

**For the C-Suite:** Developer talent is the #1 constraint in digital transformation. Copilot delivers a measurable **25-55% productivity gain** (validated by Microsoft/GitHub research across 1M+ developers). In financial terms: a 500-developer organization saves $15-30M annually in equivalent output — without hiring. More importantly, it reduces **time-to-market** for features, which directly impacts revenue capture. The strategic play isn't just efficiency — it's enabling your existing engineering team to tackle projects that were previously impossible given resource constraints.


---

📖 **[Read the original article](https://github.blog/ai-and-ml/github-copilot/github-copilot-cli-for-beginners-overview-of-common-slash-commands/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
