---
title: "GitHub Copilot app for Beginners: How to build custom workflows with canvases"
date: 2026-09-25
tags: ["Copilot", "GitHub Copilot", "GitHub", "AI Agents"]
categories: ["analysis"]
source_url: "https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-how-to-build-custom-workflows-with-canvases/"
description: "Describe the interface you need in plain English, then let the agent build a live surface you can both use and update—so you spend less time adapting to tools and more time getting work done.
The post"
---

There's been an important development in the **GitHub Copilot** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

Most tools give you a fixed set of screens and ask you to fit your work into them. But what if you could start with the workflow you want instead and have the interface take shape around it?

That’s the idea behindcanvases in the GitHub Copilot app. A canvas, also called a canvas extension, is a customizable interface that you and the agent share. It can be a kanban board, an issue triage board, a release checklist, a dashboard, a form, or even a spreadsheet: a UI shaped to how you work.

Because the canvas is bidirectional, the agent can update it as it works, and you can use buttons, cards, filters, and other controls to make changes too. Just like using a live shared whiteboard.

### Creating a canvas with /create-canvas

To create a canvas, you don’t have to do any coding or design by hand. Just open an agent session, enter the/create-canvasskill, and describe what you want in plain English.

Make sure your prompt covers three things:

- The workflow the canvas should support.

- What you should be able to do in the interface.

### Shaping the canvas around your workflow

Because the interface is generated from your description, your first version is just a starting point, and you can keep refining until you’re happy.

You could ask the agent to add a column or filter, pull in your open pull requests, or turn the entire canvas into a checklist for your day. The agent will revise the canvas to match. While there isn’t a fixed menu of layouts, if you can describe a workflow, you can likely turn it into a canvas.

Once created, your canvas is saved as an extension, so you can use it again. You can keep it with the project for your team to share or save it as a personal extension just for you.


## Key Takeaways

1. Most tools give you a fixed set of screens and ask you to fit your work into them.
2. That’s the idea behindcanvases in the GitHub Copilot app.
3. Because the canvas is bidirectional, the agent can update it as it works, and you can use buttons, cards, filters, and other controls to make changes too.
4. To create a canvas, you don’t have to do any coding or design by hand.
5. Then, the agent will build the interface and open it in the right-side panel without you having to write files or mess with the layout.


## Why This Matters

Developer productivity is one of the highest-ROI applications of AI today. Copilot is proving that AI can augment — not replace — human expertise, making experienced developers more productive and helping newcomers ramp up faster.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The technical evolution of Copilot is fascinating from an AI systems perspective. We've moved from **completion-based assistance** (predict the next line) to **agent-mode** (understand the intent, decompose the problem, execute multi-file changes, run tests, iterate on failures). This is a fundamental architectural shift — from a stateless token predictor to a stateful reasoning agent with tool use. What's technically impressive is the context management: Copilot now maintains a working memory of your entire codebase, open issues, PR history, and team conventions. The retrieval augmentation layer that grounds suggestions in *your specific codebase* (not just generic patterns) is what makes the difference between a toy and a production tool. The agentic workflows — where Copilot can plan, execute, verify, and self-correct — represent the state of the art in applied AI agents today.


## Business Translation

**For the C-Suite:** Developer talent is the #1 constraint in digital transformation. Copilot delivers a measurable **25-55% productivity gain** (validated by Microsoft/GitHub research across 1M+ developers). In financial terms: a 500-developer organization saves $15-30M annually in equivalent output — without hiring. More importantly, it reduces **time-to-market** for features, which directly impacts revenue capture. The strategic play isn't just efficiency — it's enabling your existing engineering team to tackle projects that were previously impossible given resource constraints.


---

📖 **[Read the original article](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-how-to-build-custom-workflows-with-canvases/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
