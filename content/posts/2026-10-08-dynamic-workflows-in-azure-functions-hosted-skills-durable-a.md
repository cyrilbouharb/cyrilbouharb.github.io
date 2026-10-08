---
title: "Dynamic Workflows in Azure Functions Hosted Skills: Durable, AI-Led Work for Event-Driven Apps"
date: 2026-10-08
tags: ["Foundry", "Copilot", "GitHub Copilot", "GitHub", "OpenAI", "LLM", "Data & AI", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/azure-sdk/dynamic-workflows-azure-functions-hosted-skills/"
description: "Azure Functions is the event-driven application platform, and Hosted Skills adds AI reasoning to your app. Dynamic Workflows give the app a durable way to carry out AI-led, multi-step work after the t"
---

There's been an important development in the **GitHub Copilot** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

Azure Functions is the event-driven application platform in Azure. Your code runs when a queue message, a blob upload, a database change, or an HTTP request arrives.Azure Functions Hosted Skillsadds AI reasoning to these apps. When an event arrives, an LLM reads it, applies your instructions, skills, and tools, and decides what to do.

Some events need several steps. An alert may require data from several services. A blob upload may contain 100 invoices that need individual processing. These tasks can take minutes or hours and must run reliably to completion.

TheDynamic Workflowsfeature of Azure Functions Hosted Skills separates planning from execution. The LLM writes a plan as a DAG (directed acyclic graph). The embeddedDurable Functionsengine runs the plan outside the planning LLM reasoning loop. Intermediate tool results do not return to that loop, which can reduce token use and latency.

Durable Functions provides retries, crash recovery, and long waits without keeping a Functions instance running. Backend charges can still apply during a wait. The Durable Task Scheduler (DTS) dashboard shows workflow progress and task details. You do not need to write an orchestrator to use these capabilities.

### The problem with LLM reasoning loops

Without Dynamic Workflows, an LLM reasoning loop must process each step in a multi-step workflow independently. For each step, the LLM calls one tool, reads the result, and then calls the next tool. At each step, the reasoning loop sends the full conversation history, the tool definitions, and all the tool results to the LLM again. A task that makes dozens of sequential tool calls can easily consume huge numbers of tokens and take a long time to execute.

- Tokens:For each tool call, the full conversation history and all the tool results go to the LLM again. If your LLM provider charges (or rate-limits) per token, you effectively pay for the same work multiple times.

- Latency:Each step of the loop needs one more LLM inference: the LLM must read the previous tool result before it can request the next tool call. A task with 10 tool calls needs 20 or more sequential inferences. Each inference can take a long time, so the total latency becomes large.

- Reliability:As the context window fills up, the LLM has more difficulty following instructions. For example, it can skip part of the work, or stop before the work is complete.

### Dynamic Workflows: keep planning and execution separate

With Dynamic Workflows, the LLM reads the prompt once and generates an execution plan as a DAG. Then it uses a built-in tool call to schedule the DAG for execution in a built-in Durable Functions orchestration. All tasks in the DAG run independently from the planning LLM reasoning loop. The orchestrator schedules tool tasks and waits without further calls to the planning LLM. Asub_agenttask, however, makes its own LLM calls, consumes tokens, and adds LLM latency while it runs. A workflow tool can also call an LLM if its implementation requires one. If the LLM later summarizes the final result, that turn also consumes tokens.

To enable this feature, add theworkflows.enabled: truesetting to the front matter of the.agent.mdfile:

```
---
name: Incident Triage Assistant
description: Investigates incidents by gathering evidence in parallel.
workflows:
  enabled: true
---
```

```
---
name: Incident Triage Assistant
description: Investigates incidents by gathering evidence in parallel.
workflows:
  enabled: true
---
```


## Key Takeaways

1. Azure Functions is the event-driven application platform in Azure.
2. Some events need several steps.
3. TheDynamic Workflowsfeature of Azure Functions Hosted Skills separates planning from execution.
4. Durable Functions provides retries, crash recovery, and long waits without keeping a Functions instance running.
5. This post explains how Dynamic Workflows operate, which design decisions we made, what our benchmark shows, and which scenarios are a good fit.


## Why This Matters

Developer productivity is one of the highest-ROI applications of AI today. Copilot is proving that AI can augment — not replace — human expertise, making experienced developers more productive and helping newcomers ramp up faster.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The technical evolution of Copilot is fascinating from an AI systems perspective. We've moved from **completion-based assistance** (predict the next line) to **agent-mode** (understand the intent, decompose the problem, execute multi-file changes, run tests, iterate on failures). This is a fundamental architectural shift — from a stateless token predictor to a stateful reasoning agent with tool use. What's technically impressive is the context management: Copilot now maintains a working memory of your entire codebase, open issues, PR history, and team conventions. The retrieval augmentation layer that grounds suggestions in *your specific codebase* (not just generic patterns) is what makes the difference between a toy and a production tool. The agentic workflows — where Copilot can plan, execute, verify, and self-correct — represent the state of the art in applied AI agents today.


## Business Translation

**For the C-Suite:** Developer talent is the #1 constraint in digital transformation. Copilot delivers a measurable **25-55% productivity gain** (validated by Microsoft/GitHub research across 1M+ developers). In financial terms: a 500-developer organization saves $15-30M annually in equivalent output — without hiring. More importantly, it reduces **time-to-market** for features, which directly impacts revenue capture. The strategic play isn't just efficiency — it's enabling your existing engineering team to tackle projects that were previously impossible given resource constraints.


---

📖 **[Read the original article](https://devblogs.microsoft.com/azure-sdk/dynamic-workflows-azure-functions-hosted-skills/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
