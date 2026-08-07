---
title: "A guide to slash commands in the GitHub Copilot app"
date: 2026-08-06
tags: ["Copilot", "GitHub Copilot", "GitHub", "Architecture", "AI Agents"]
categories: ["analysis"]
source_url: "https://github.blog/ai-and-ml/github-copilot/a-guide-to-slash-commands-in-the-github-copilot-app/"
description: "Go beyond chat in the GitHub Copilot app with these slash commands. They'll help you plan, collaborate, automate, and customize your dev workflow.
The post A guide to slash commands in the GitHub Copi"
---

There's been an important development in the **GitHub Copilot** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

If you’ve used slash commands in the GitHub Copilot CLI, you already know how powerful a quick/can be. In the GitHub Copilot app, slash commands take that idea further, giving you shortcuts for managing sessions, navigating projects, and customizing your Copilot workflow.

### What are slash commands?

Slash commands are text shortcuts you type directly into the GitHub Copilot app’s chat composer. Start by typing/and an autocomplete menu appears, showing the commands available in your current context. It’s a small character with a lot of potential, opening the door to shortcuts that help you work with Copilot in new ways.

If you’re coming from the CLI, here’s the key difference: CLI slash commands are designed around a terminal-first workflow. Things like adding directories, setting your working directory, and managing terminal access happen through commands. This makes sense, because the CLI lives inside your terminal where there’s no visual interface.

The app, on the other hand, provides a visual interface for managing context. File access commands like/add-diror/cwdaren’t needed since the app manages project context automatically. App slash commands are more about workflows. You can navigate between sessions, manage projects, and control how the agent works.

### Why use slash commands?

Slash commands may look like simple shortcuts, but they can change how you interact with Copilot. They help you move faster, stay focused, and quickly access the workflows you need. Instead of digging through options or breaking your focus to find the right tool, you can type a command and keep moving. A single/opens up the list of slash commands that can help you move faster, explore new ideas, and get the most out of the app.

Let’s take a look at some of the slash commands available in the GitHub Copilot app and how they can fit into your everyday workflows.


## Key Takeaways

1. If you’ve used slash commands in the GitHub Copilot CLI, you already know how powerful a quick/can be.
2. Slash commands are text shortcuts you type directly into the GitHub Copilot app’s chat composer.
3. If you’re coming from the CLI, here’s the key difference: CLI slash commands are designed around a terminal-first workflow.
4. The app, on the other hand, provides a visual interface for managing context.
5. Slash commands may look like simple shortcuts, but they can change how you interact with Copilot.


## Why This Matters

Developer productivity is one of the highest-ROI applications of AI today. Copilot is proving that AI can augment — not replace — human expertise, making experienced developers more productive and helping newcomers ramp up faster.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The technical evolution of Copilot is fascinating from an AI systems perspective. We've moved from **completion-based assistance** (predict the next line) to **agent-mode** (understand the intent, decompose the problem, execute multi-file changes, run tests, iterate on failures). This is a fundamental architectural shift — from a stateless token predictor to a stateful reasoning agent with tool use. What's technically impressive is the context management: Copilot now maintains a working memory of your entire codebase, open issues, PR history, and team conventions. The retrieval augmentation layer that grounds suggestions in *your specific codebase* (not just generic patterns) is what makes the difference between a toy and a production tool. The agentic workflows — where Copilot can plan, execute, verify, and self-correct — represent the state of the art in applied AI agents today.


## Business Translation

**For the C-Suite:** Developer talent is the #1 constraint in digital transformation. Copilot delivers a measurable **25-55% productivity gain** (validated by Microsoft/GitHub research across 1M+ developers). In financial terms: a 500-developer organization saves $15-30M annually in equivalent output — without hiring. More importantly, it reduces **time-to-market** for features, which directly impacts revenue capture. The strategic play isn't just efficiency — it's enabling your existing engineering team to tackle projects that were previously impossible given resource constraints.


---

📖 **[Read the original article](https://github.blog/ai-and-ml/github-copilot/a-guide-to-slash-commands-in-the-github-copilot-app/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
