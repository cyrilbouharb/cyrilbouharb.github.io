---
title: "From one-off prompts to workflows: How to use custom agents in GitHub Copilot CLI"
date: 2026-06-09
tags: ["Copilot", "GitHub Copilot", "GitHub", "OpenAI", "AI Agents"]
categories: ["analysis"]
source_url: "https://github.blog/ai-and-ml/github-copilot/from-one-off-prompts-to-workflows-how-to-use-custom-agents-in-github-copilot-cli/"
description: "Custom agents let GitHub Copilot CLI understand your stack and team workflows, turning one-off terminal prompts into repeatable, reviewable processes.
The post From one-off prompts to workflows: How t"
---

There's been an important development in the **GitHub Copilot** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

Developers work across many surfaces like the CLI, IDE, and GitHub. The terminal is often where they turn to move fast, automate tasks, or work directly with systems and scripts.

Tools like theGitHub Copilot CLIalready make this easier. You can generate commands, debug issues, and move quicker without leaving the terminal.

However, like any environment, the CLI can still accumulate friction: re-running the same commands, re-explaining context, or translating logs for your team into something they can act on. These small steps add up, especially when every team’s stack and standards are a little different.

But what if your terminal didn’t just run commands, it understood your stack, your tools, and your team’s standards?

### What are custom agents?

A custom agent is a Copilot agent that can be defined using a Markdown file. Instead of relying on generic behavior, you describe how the agent should operate, what tools it can use, what standards it should follow, and what outputs it should produce. The result: its behavior is consistent wherever it runs.

Each coding agent you create can act as a specialized agent tailored for a specific task. For example, a generic coding agent might suggest how to clean up your code. But a custom agent can apply your formatting rules, tooling, accessibility standards, review requirements, and safety requirements every time it runs.

Custom agents are defined using agent profiles, or files that live directly in your repository. Written in Markdown, these agent profiles let you specify:

- Guardrails that keep outputs safe and consistent

### How custom agents work in GitHub Copilot CLI

GitHub Copilot CLI is well suited for agent-driven work because it already runs scripts, calls APIs, and works directly with your repositories. Defining agents here lets you further tailor Copilot CLI by encoding execution-heavy workflows once, then invoking it from the terminal. The agent will execute your workflow the same way every time.

Toadd a new custom agentfor GitHub Copilot CLI, you’ll need to:

- Invoke the agent from Copilot CLI.From the terminal, run the Copilot CLI and use the/agentslash command. Select the custom agent you want to use.

- Create an agent profile in the.``github``/agentsdirectory of your target repository.The agent profile is a Markdown file with YAML frontmatter that defines the agent’s role, scope, capabilities, and guardrails, so it behaves consistently in your workflows. The agent profile file ends with.agent.md– for example,accessibility.agent.md.


## Key Takeaways

1. Developers work across many surfaces like the CLI, IDE, and GitHub.
2. Tools like theGitHub Copilot CLIalready make this easier.
3. However, like any environment, the CLI can still accumulate friction: re-running the same commands, re-explaining context, or translating logs for your team into something they can act on.
4. But what if your terminal didn’t just run commands, it understood your stack, your tools, and your team’s standards?.
5. That’s where custom agents come in.


## Why This Matters

Developer productivity is one of the highest-ROI applications of AI today. Copilot is proving that AI can augment — not replace — human expertise, making experienced developers more productive and helping newcomers ramp up faster.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The technical evolution of Copilot is fascinating from an AI systems perspective. We've moved from **completion-based assistance** (predict the next line) to **agent-mode** (understand the intent, decompose the problem, execute multi-file changes, run tests, iterate on failures). This is a fundamental architectural shift — from a stateless token predictor to a stateful reasoning agent with tool use. What's technically impressive is the context management: Copilot now maintains a working memory of your entire codebase, open issues, PR history, and team conventions. The retrieval augmentation layer that grounds suggestions in *your specific codebase* (not just generic patterns) is what makes the difference between a toy and a production tool. The agentic workflows — where Copilot can plan, execute, verify, and self-correct — represent the state of the art in applied AI agents today.


## Business Translation

**For the C-Suite:** Developer talent is the #1 constraint in digital transformation. Copilot delivers a measurable **25-55% productivity gain** (validated by Microsoft/GitHub research across 1M+ developers). In financial terms: a 500-developer organization saves $15-30M annually in equivalent output — without hiring. More importantly, it reduces **time-to-market** for features, which directly impacts revenue capture. The strategic play isn't just efficiency — it's enabling your existing engineering team to tackle projects that were previously impossible given resource constraints.


---

📖 **[Read the original article](https://github.blog/ai-and-ml/github-copilot/from-one-off-prompts-to-workflows-how-to-use-custom-agents-in-github-copilot-cli/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
