---
title: "Maintainers don’t need more AI bug reports. They need fixes."
date: 2026-11-17
tags: ["Copilot", "GitHub", "OpenAI", "Agentic RAG", "AI Agents"]
categories: ["analysis"]
source_url: "https://github.blog/open-source/maintainers/maintainers-dont-need-more-ai-bug-reports-they-need-fixes/"
description: "In the Codename MDASH pilot, GitHub and Microsoft turned thousands of raw AI findings into 99 checked, private reports with suggested fixes for six widely used open source projects. Maintainers have a"
---

There's been an important development in the **AI Agents** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

AI has made finding potential vulnerabilities fast and cheap. Fixing them still takes human judgment, and in open source, that work falls to maintainers. Many are already flooded with AI-generated security findings, including duplicates and reports that aren’t vulnerabilities at all. Another raw scan doesn’t help them. Anyone pointing a new model at a project should ask its maintainers first and come with fixes, not just findings.

Maintainers are under intense pressure from this flood of reports. As Christian Grobmeier, a maintainer of Log4j, has put it, theAI defending open source has to be better than the AI attacking it.

AI shouldn’t add to maintainers’ workload. So, with maintainers, GitHub and Microsoft ran a pilot together: could AI help maintainers ship fixes instead of handing them more findings?

GitHub and Microsoft are usingCodename MDASH, Microsoft’s multi-model agentic scanning harness, to find and fix security vulnerabilities in widely used open source software, strengthening the foundation that much of the world’s code is built on.

### The process

Our pilot had two goals: send only findings that matter, and never send a maintainer an unverified finding. Here’s how it worked:

- Find.Codename MDASH, an AI system from Microsoft Security, scanned each project using Microsoft’sMAI Cyber modeland suggested fixes for what it found.

- Filter.AnAI triage agent from the GitHub Security Lab, built on tailored Copilot skills, removed duplicates, checked validity, and focused on high-impact bugs, so maintainers never had to review raw scan results.

- Verify.Researchers from Microsoft FORGE Labchecked every remaining finding by hand.

### Participating projects

Six projects took part, all alumni of theGitHub Secure Open Source Fund. Their maintainers agreed to the scan, received every report privately, decided what to fix, and shared what worked:

- FastMCP, a framework for building MCP servers


## Key Takeaways

1. AI has made finding potential vulnerabilities fast and cheap.
2. Maintainers are under intense pressure from this flood of reports.
3. AI shouldn’t add to maintainers’ workload.
4. GitHub and Microsoft are usingCodename MDASH, Microsoft’s multi-model agentic scanning harness, to find and fix security vulnerabilities in widely used open source software, strengthening the foundation that much of the world’s code is built on.
5. Our pilot had two goals: send only findings that matter, and never send a maintainer an unverified finding.


## Why This Matters

Agentic AI is where the industry is heading. From code generation to customer service to data analysis, agents can handle multi-step workflows that previously required human intervention at every stage. This isn't just automation — it's a fundamentally new way of building software.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The technical frontier in AI agents right now is the **orchestration problem** — how do you reliably coordinate multiple specialized agents, each with different capabilities and knowledge, to solve complex tasks? The key architectural patterns emerging are: **handoff protocols** (A2A for cross-platform agent communication), **governance layers** (constraining agent actions within policy boundaries without killing autonomy), and **state management** (maintaining coherent context as work passes between agents). What I find most technically interesting is the convergence of **code-generating agents** (Copilot, Codex) with **tool-using agents** (function calling, MCP) — agents that can both write *and* execute code create a self-improving loop that's qualitatively different from static automation. The challenge is reliability: current agents succeed ~70-85% on complex tasks. Getting to 99%+ requires better evaluation frameworks, graceful degradation patterns, and human-in-the-loop checkpoints for high-stakes decisions.


## Business Translation

**For the C-Suite:** AI agents represent the next wave of operational leverage — not just automating tasks, but automating *judgment*. Early adopters are seeing **40-70% reduction in operational costs** for knowledge work (customer service, compliance review, data analysis). The strategic question isn't whether to adopt agents, but where to deploy them first for maximum ROI. The playbook: start with high-volume, medium-complexity workflows where errors are recoverable (customer inquiries, internal operations), then expand to higher-stakes domains as confidence grows. The organizations that build agent infrastructure now will have a 2-3 year head start when the technology matures.


---

📖 **[Read the original article](https://github.blog/open-source/maintainers/maintainers-dont-need-more-ai-bug-reports-they-need-fixes/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
