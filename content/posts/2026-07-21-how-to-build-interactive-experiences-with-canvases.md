---
title: "How to build interactive experiences with canvases"
date: 2026-07-21
tags: ["Copilot", "GitHub Copilot", "GitHub", "Agentic RAG", "Architecture", "AI Agents"]
categories: ["analysis"]
source_url: "https://github.blog/ai-and-ml/github-copilot/how-to-build-interactive-experiences-with-canvases/"
description: "Canvases turn AI into interactive workspaces where you can visualize information, explore workflows, and take action across complex tasks.
The post How to build interactive experiences with canvases a"
---

There's been an important development in the **GitHub Copilot** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

Most developers are now working alongside agents, or are at least familiar with how to do so. Agents help you explore ideas and turn them into action, from planning projects to automating workflows. Oftentimes, a conversation is all you need to move your work forward.

But what about tasks that don’t quite fit the conversation mold?

Some tasks are easier when you can see and interact with the information. You may need to triage a backlog, visualize complex information, or bring information together from multiple sources. A visual interface makes it easier to understand patterns, spot connections, and take action.

Instead of working through a long chain of prompts and responses, you can use canvases to interact directly with the information in front of you.

### Working with canvases

These shared, interactive surfaces are extensions of the Copilot app called canvases. A canvas is an interface in the GitHub Copilot app where developers and agents can collaborate in real time. These shared, interactive surfaces are called canvas extensions.

The agent can update the canvas as it works, and you can interact with that same workspace through clicks, edits, and other actions. Your interactions can be sent back to the agentsorprocessed locally by the canvas.

You can continuously shape the experience by asking Copilot to iterate on your canvas—adding new functionality, refining existing features, and more. The canvas can evolve alongside your work.

To create a canvas, use/create-canvasin your agent session in the GitHub Copilot app, then describe what you want it to create and what capabilities it should be able to support.

### Issue triage helper

Goal: Quickly triage GitHub Issues in a fast, visual way.

Prompt:/create-canvas Create an interface that allows me to easily swipe through issues in a repo in card format. Can swipe right to ship, left to reject.

```
/create-canvas Create an interface that allows me to easily swipe through issues in a repo in card format. Can swipe right to ship, left to reject.
```

Result: The canvas shows a card-based interface where each issue is surfaced one at a time. You can take action directly from the UI. As you swipe, the canvas updates in real time, tracking decisions and moving the items into the appropriate buckets.


## Key Takeaways

1. Most developers are now working alongside agents, or are at least familiar with how to do so.
2. But what about tasks that don’t quite fit the conversation mold?.
3. Some tasks are easier when you can see and interact with the information.
4. Instead of working through a long chain of prompts and responses, you can use canvases to interact directly with the information in front of you.
5. These shared, interactive surfaces are extensions of the Copilot app called canvases.


## Why This Matters

Developer productivity is one of the highest-ROI applications of AI today. Copilot is proving that AI can augment — not replace — human expertise, making experienced developers more productive and helping newcomers ramp up faster.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The technical evolution of Copilot is fascinating from an AI systems perspective. We've moved from **completion-based assistance** (predict the next line) to **agent-mode** (understand the intent, decompose the problem, execute multi-file changes, run tests, iterate on failures). This is a fundamental architectural shift — from a stateless token predictor to a stateful reasoning agent with tool use. What's technically impressive is the context management: Copilot now maintains a working memory of your entire codebase, open issues, PR history, and team conventions. The retrieval augmentation layer that grounds suggestions in *your specific codebase* (not just generic patterns) is what makes the difference between a toy and a production tool. The agentic workflows — where Copilot can plan, execute, verify, and self-correct — represent the state of the art in applied AI agents today.


## Business Translation

**For the C-Suite:** Developer talent is the #1 constraint in digital transformation. Copilot delivers a measurable **25-55% productivity gain** (validated by Microsoft/GitHub research across 1M+ developers). In financial terms: a 500-developer organization saves $15-30M annually in equivalent output — without hiring. More importantly, it reduces **time-to-market** for features, which directly impacts revenue capture. The strategic play isn't just efficiency — it's enabling your existing engineering team to tackle projects that were previously impossible given resource constraints.


---

📖 **[Read the original article](https://github.blog/ai-and-ml/github-copilot/how-to-build-interactive-experiences-with-canvases/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
