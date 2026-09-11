---
title: "GitHub Copilot app for Beginners: Using the diff, terminal, and browser"
date: 2026-09-10
tags: ["Copilot", "GitHub Copilot", "GitHub", "AI Agents"]
categories: ["analysis"]
source_url: "https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-using-the-diff-terminal-and-browser/"
description: "Checking agent-generated code usually means hopping between tabs. Learn how to view diffs, run terminal commands, and preview web apps side by side in the GitHub Copilot app.
The post GitHub Copilot a"
---

There's been an important development in the **GitHub Copilot** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

When an agent makes a change to your code, you want to review it, run it, and see what changed. Great news: now you can do all three without having to leave theGitHub Copilot app.

Before, doing those three jobs would mean having to bounce between your editor, terminal window, and web browser. But when these steps live side by side as built-in panels in the Copilot app, checking your agent’s work is simple.

Let’s walk through each of the panels in the app and how we’ll use them to complete the AI coding loop.

### Using the diff panel to review changes

The diff panel (a diff is a before and after comparison) shows exactly what lines were added, removed, or changed, with additions highlighted in green and deletions in red.

This gives you complete clarity, so you can choose what happens. You can accept changes, leave comments, or ask Copilot to make changes. You’re in complete control and make the final decisions.

### Running commands in the terminal panel

Reading code is good, but running it is even better. You can run commands right inside the session from the Copilot app’s terminal panel. And if it looks intimidating, don’t worry. You’re mostly just running the project’s own commands and reading the results.

You can run the code by hand or configure it as a script (available through theRunbutton). Pretend you’re working on a website, here’s an example of how that works:

- Add thedev serverscript that opens the client folder and then runsnpm run dev.

- ClickRunto start the server for the website.


## Key Takeaways

1. When an agent makes a change to your code, you want to review it, run it, and see what changed.
2. Before, doing those three jobs would mean having to bounce between your editor, terminal window, and web browser.
3. Let’s walk through each of the panels in the app and how we’ll use them to complete the AI coding loop.
4. The diff panel (a diff is a before and after comparison) shows exactly what lines were added, removed, or changed, with additions highlighted in green and deletions in red.
5. This gives you complete clarity, so you can choose what happens.


## Why This Matters

Developer productivity is one of the highest-ROI applications of AI today. Copilot is proving that AI can augment — not replace — human expertise, making experienced developers more productive and helping newcomers ramp up faster.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The technical evolution of Copilot is fascinating from an AI systems perspective. We've moved from **completion-based assistance** (predict the next line) to **agent-mode** (understand the intent, decompose the problem, execute multi-file changes, run tests, iterate on failures). This is a fundamental architectural shift — from a stateless token predictor to a stateful reasoning agent with tool use. What's technically impressive is the context management: Copilot now maintains a working memory of your entire codebase, open issues, PR history, and team conventions. The retrieval augmentation layer that grounds suggestions in *your specific codebase* (not just generic patterns) is what makes the difference between a toy and a production tool. The agentic workflows — where Copilot can plan, execute, verify, and self-correct — represent the state of the art in applied AI agents today.


## Business Translation

**For the C-Suite:** Developer talent is the #1 constraint in digital transformation. Copilot delivers a measurable **25-55% productivity gain** (validated by Microsoft/GitHub research across 1M+ developers). In financial terms: a 500-developer organization saves $15-30M annually in equivalent output — without hiring. More importantly, it reduces **time-to-market** for features, which directly impacts revenue capture. The strategic play isn't just efficiency — it's enabling your existing engineering team to tackle projects that were previously impossible given resource constraints.


---

📖 **[Read the original article](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-using-the-diff-terminal-and-browser/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
