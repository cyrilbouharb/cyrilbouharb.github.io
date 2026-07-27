---
title: "The harness is all you need (mostly)"
date: 2026-07-27
tags: ["Copilot", "GitHub Copilot", "GitHub", "Data & AI", "AI Agents"]
categories: ["analysis"]
source_url: "https://github.blog/company/the-harness-is-all-you-need-mostly/"
description: "A practical GitHub Copilot workflow for prototyping, planning, implementing, and reviewing software without chasing every new AI tool.
The post The harness is all you need (mostly) appeared first on T"
---

There's been an important development in the **GitHub Copilot** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

If you’re feeling overwhelmed by AI right now, you’re not alone.

Every day it seems there is a new tool, new MCP, new model, new skill, new workflow, new feature, new social post that is some form of “Hey look! I have completely figured out AI with this one weird prompt.”

I work with AI every single day, and what I’m finding is that less is way more. It’s not about what I install or configure or trick the agent into doing that makes any real difference. That stuff is interesting, but at the end of the day it feels like gimmicks.

I see the biggest gains in my productivity from how I use the harness and how well I understand it.

### Disclaimers

I’m using the term “harness” interchangeably with “GitHub Copilot.” The point of this post is to keep things simple, so just know that GitHub Copilot is an agent harness.

I don’t mean to insinuate that you won’t ever need any skills or MCPs or instructions or custom agents, etc. In fact, those things will become quite important as you progress and need to define complex workflows and automate things for your teams. In fact, I use a few throughout this blog post!

What I am pointing out here is that you do not need any of those things to be highly successful with AI.

Also, there is a lot of slop out there. If you don’t believe that, ask the agent to create a skill to do anything at all. It will happily oblige. Whether or not that generated skill actually works, it can be easily published to any number of skill or MCP registries.

### 1. Pick a tool, any tool

This is an obvious one, right? Pick a tool! It’s so easy!

But even within the GitHub Copilot family, there are a lot of options. These include theCLI, the newGitHub Copilot app,VS Code,Visual Studio, andJetBrains, just to name a few.

The good news is that these experiences are increasingly being centralized on the same harness. The details can differ by tool, but the core workflow is consistent. Learn the harness once, use it everywhere.

That said, I do believe that learning the harness is key, and the best way to learn it is to be as close to it as possible. So if you are just starting out, I’d recommend beginning with the GitHub Copilot CLI. It’s a terminal interface, which means it’s just text. There isn’t much UI to learn. You enter a prompt. The agent does things. But the interaction is more direct, immediate, and, frankly, very satisfying.


## Key Takeaways

1. If you’re feeling overwhelmed by AI right now, you’re not alone.
2. Every day it seems there is a new tool, new MCP, new model, new skill, new workflow, new feature, new social post that is some form of “Hey look! I have completely figured out AI with this one weird prompt.”.
3. I work with AI every single day, and what I’m finding is that less is way more.
4. I see the biggest gains in my productivity from how I use the harness and how well I understand it.
5. So in this post, I’m sharing you a simple workflow that you can use to drastically improve your effectiveness with AI just by using existing features ofGitHub Copilot.


## Why This Matters

Developer productivity is one of the highest-ROI applications of AI today. Copilot is proving that AI can augment — not replace — human expertise, making experienced developers more productive and helping newcomers ramp up faster.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The technical evolution of Copilot is fascinating from an AI systems perspective. We've moved from **completion-based assistance** (predict the next line) to **agent-mode** (understand the intent, decompose the problem, execute multi-file changes, run tests, iterate on failures). This is a fundamental architectural shift — from a stateless token predictor to a stateful reasoning agent with tool use. What's technically impressive is the context management: Copilot now maintains a working memory of your entire codebase, open issues, PR history, and team conventions. The retrieval augmentation layer that grounds suggestions in *your specific codebase* (not just generic patterns) is what makes the difference between a toy and a production tool. The agentic workflows — where Copilot can plan, execute, verify, and self-correct — represent the state of the art in applied AI agents today.


## Business Translation

**For the C-Suite:** Developer talent is the #1 constraint in digital transformation. Copilot delivers a measurable **25-55% productivity gain** (validated by Microsoft/GitHub research across 1M+ developers). In financial terms: a 500-developer organization saves $15-30M annually in equivalent output — without hiring. More importantly, it reduces **time-to-market** for features, which directly impacts revenue capture. The strategic play isn't just efficiency — it's enabling your existing engineering team to tackle projects that were previously impossible given resource constraints.


---

📖 **[Read the original article](https://github.blog/company/the-harness-is-all-you-need-mostly/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
