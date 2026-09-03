---
title: "Decoding the new AI lingo: Loops, harnesses, squads, hill climbing… oh my!"
date: 2026-09-02
tags: ["Copilot", "GitHub Copilot", "GitHub", "Data & AI", "AI Agents"]
categories: ["analysis"]
source_url: "https://github.blog/ai-and-ml/decoding-the-new-ai-lingo-loops-harnesses-squads-hill-climbing-oh-my/"
description: "From loop engineering to harnesses, squads, and open weights, the GitHub Podcast breaks down the AI terms showing up in developer conversations.
The post Decoding the new AI lingo: Loops, harnesses, s"
---

There's been an important development in the **GitHub Copilot** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

It might be overwhelming to see all of the new vocabulary popping up in software development these days thanks to AI tools introducing them… all the time.

Some of this new vocab describes useful patterns that people are newly pursuing, others are just fancy names on top of things that already exist, and some are still actively being defined as we speak.

In our latest episode of theGitHub Podcast, Marlene Mhangami, GPS, and I talked through some of the AI terms developers are learning right now: loop engineering, Ralph loops, squads, harness engineering, hill climbing, forward deployed engineers, closed models, open weights, and open source models.

If you’re a reader instead of a listener, here’s a guide to what those terms mean, why they matter, and how to think about them.

### Loop engineering: Moving beyond one-shot prompts

Loop engineering is the practice of designing repeatable systems around agents, instead of manually prompting them for one task at a time.

A simple example: instead of asking an agent every morning to review new issues, summarize them, and propose fixes, you create a loop that runs on a schedule. That loop might fetch issues, pass them to an agent, validate the output, and escalate anything that gets stuck. It’s a glorified AI-native cron job.

### Ralph loops: The brute-force cousin of loop engineering

A Ralph loop is one implementation of this “loop” concept: you give an agent a detailed task, often from a product requirements document or spec, and have it keep working until the job is done.

That can be useful, especially for breaking down large tasks into repeated plan-act-check cycles. But, on the other hand, it can also be expensive and inefficient because every iteration uses more tokens, more context, and more compute.

Loop engineering aims to make this pattern more structured, so you’re not caught asking an agent to “try again” all the time. A well-designed loop adds primitives like skills, observability, validation, routing, and checkpoints.


## Key Takeaways

1. It might be overwhelming to see all of the new vocabulary popping up in software development these days thanks to AI tools introducing them… all the time.
2. Some of this new vocab describes useful patterns that people are newly pursuing, others are just fancy names on top of things that already exist, and some are still actively being defined as we speak.
3. In our latest episode of theGitHub Podcast, Marlene Mhangami, GPS, and I talked through some of the AI terms developers are learning right now: loop engineering, Ralph loops, squads, harness engineering, hill climbing, forward deployed engineers, closed models, open weights, and open source models.
4. If you’re a reader instead of a listener, here’s a guide to what those terms mean, why they matter, and how to think about them.
5. Loop engineering is the practice of designing repeatable systems around agents, instead of manually prompting them for one task at a time.


## Why This Matters

Developer productivity is one of the highest-ROI applications of AI today. Copilot is proving that AI can augment — not replace — human expertise, making experienced developers more productive and helping newcomers ramp up faster.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The technical evolution of Copilot is fascinating from an AI systems perspective. We've moved from **completion-based assistance** (predict the next line) to **agent-mode** (understand the intent, decompose the problem, execute multi-file changes, run tests, iterate on failures). This is a fundamental architectural shift — from a stateless token predictor to a stateful reasoning agent with tool use. What's technically impressive is the context management: Copilot now maintains a working memory of your entire codebase, open issues, PR history, and team conventions. The retrieval augmentation layer that grounds suggestions in *your specific codebase* (not just generic patterns) is what makes the difference between a toy and a production tool. The agentic workflows — where Copilot can plan, execute, verify, and self-correct — represent the state of the art in applied AI agents today.


## Business Translation

**For the C-Suite:** Developer talent is the #1 constraint in digital transformation. Copilot delivers a measurable **25-55% productivity gain** (validated by Microsoft/GitHub research across 1M+ developers). In financial terms: a 500-developer organization saves $15-30M annually in equivalent output — without hiring. More importantly, it reduces **time-to-market** for features, which directly impacts revenue capture. The strategic play isn't just efficiency — it's enabling your existing engineering team to tackle projects that were previously impossible given resource constraints.


---

📖 **[Read the original article](https://github.blog/ai-and-ml/decoding-the-new-ai-lingo-loops-harnesses-squads-hill-climbing-oh-my/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
