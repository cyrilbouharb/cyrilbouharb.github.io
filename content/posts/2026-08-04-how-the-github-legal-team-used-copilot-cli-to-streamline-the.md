---
title: "How the GitHub legal team used Copilot CLI to streamline their workflows"
date: 2026-08-04
tags: ["Copilot", "GitHub Copilot", "GitHub", "Data & AI"]
categories: ["analysis"]
source_url: "https://github.blog/ai-and-ml/github-copilot/how-the-github-legal-team-used-copilot-cli-to-streamline-their-workflows/"
description: "Learn how to build tools to simplify how you work—without writing a single line of code.
The post How the GitHub legal team used Copilot CLI to streamline their workflows appeared first on The GitHub "
---

There's been an important development in the **GitHub Copilot** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

Whether you are just starting out or are not in a technical role at all, you likely already have the skills you need to build your own tools. If you have ever thought “I’m not technical enough to build that,” this post is for you.

Let me introduce the team. We are lawyers, program managers, and business professionals—not engineers. A large part of our work is often repetitive, like reviewing the same kinds of contracts over and over or answering the same legal questions, and our prior guidance is frequently recycled. These are problems AI could help solve, but we lacked confidence in how to build the right tools.

That is whereGitHub Copilot CLIcame in. We asked for what we wanted in plain language, plugged into our repos, and saw real changes fast. “I could never code” turned into “I just built something,” and that habit spread on its own until every one of us was building something.

What follows are two real accounts of people who did exactly that. Plus, watch the videos for two additional stories.

### Why I built an internal drafting style guide

The following is a first-person account from Ngandu Kasuku, Principal Product Counsel.

I’m a product attorney, but commercial work remains a sizable part of my practice. Around March or April, I found myself buried in partnership deals involving data, infrastructure, and product integrations. No two deals looked quite alike, so each new matter felt like starting over.

I started using Copilot CLI to manage the surge, which helped, but also had some problems. Then, after seeing what others had built with Copilot, I realized I wasn’t thinking big enough. Instead of using AI for one task at a time, I could build something around the way I work.

So, I created a contract drafting tool using Copilot CLI. I called itterms-ai, which I admit isn’t the most original name. I started by scaffolding the project and storing key documents in a repository. This gave me one place to organize and version the instructions, drafting resources, and workflows that guide the AI. That structure made the results more consistent and reduced the copying and pasting that had slowed me down when I was using a library of prompts.

### How I built legal workflows without writing traditional code

The following is a first-person account from Jesse Geraci, Online Safety Counsel.

I started with a narrow problem. We needed to analyze source code quickly and accurately to evaluate DMCA (Digital Millennium Copyright Act) notices. The original project began as a set of GitHub Copilot instructions for recurring tasks like DMCA triage, comparing code, license checks, and circumvention review. We wanted to turn the messy, one-off prompt work that everyone was doing independently into something repeatable that a legal team could trust to gather the right facts and analyze the data consistently.

I was surprised at how far I could go without engineering support. The core “programming” was plain-language files consisting of workflow instruction sets, policy reference materials, and templates for writing reports. Instead of writing source code, I was able to use my language crafting skills as a lawyer to build structured legal judgment into the workflow itself.

It grew from there. We added different analysis modes for clients and lawyers (with faster outputs and escalation recommendations for clients, and deeper review and both-sides arguments for lawyers) and integrated external data sources. When I handed the workflow off to the team, they started using it right away and asked Copilot to do more.


## Key Takeaways

1. Whether you are just starting out or are not in a technical role at all, you likely already have the skills you need to build your own tools.
2. That is whereGitHub Copilot CLIcame in.
3. What follows are two real accounts of people who did exactly that.
4. The following is a first-person account from Ngandu Kasuku, Principal Product Counsel.
5. I’m a product attorney, but commercial work remains a sizable part of my practice.


## Why This Matters

Developer productivity is one of the highest-ROI applications of AI today. Copilot is proving that AI can augment — not replace — human expertise, making experienced developers more productive and helping newcomers ramp up faster.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The technical evolution of Copilot is fascinating from an AI systems perspective. We've moved from **completion-based assistance** (predict the next line) to **agent-mode** (understand the intent, decompose the problem, execute multi-file changes, run tests, iterate on failures). This is a fundamental architectural shift — from a stateless token predictor to a stateful reasoning agent with tool use. What's technically impressive is the context management: Copilot now maintains a working memory of your entire codebase, open issues, PR history, and team conventions. The retrieval augmentation layer that grounds suggestions in *your specific codebase* (not just generic patterns) is what makes the difference between a toy and a production tool. The agentic workflows — where Copilot can plan, execute, verify, and self-correct — represent the state of the art in applied AI agents today.


## Business Translation

**For the C-Suite:** Developer talent is the #1 constraint in digital transformation. Copilot delivers a measurable **25-55% productivity gain** (validated by Microsoft/GitHub research across 1M+ developers). In financial terms: a 500-developer organization saves $15-30M annually in equivalent output — without hiring. More importantly, it reduces **time-to-market** for features, which directly impacts revenue capture. The strategic play isn't just efficiency — it's enabling your existing engineering team to tackle projects that were previously impossible given resource constraints.


---

📖 **[Read the original article](https://github.blog/ai-and-ml/github-copilot/how-the-github-legal-team-used-copilot-cli-to-streamline-their-workflows/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
