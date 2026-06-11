---
title: "Making secret scanning more trustworthy: Reducing false positives at scale"
date: 2026-06-11
tags: ["GitHub", "LLM", "Data & AI", "Agentic RAG", "AI Agents"]
categories: ["analysis"]
source_url: "https://github.blog/security/making-secret-scanning-more-trustworthy-reducing-false-positives-at-scale/"
description: "Alerts are more trustworthy and actionable when noise is reduced. See how we improved the verification step with context-aware LLM reasoning.
The post Making secret scanning more trustworthy: Reducing"
---

There's been an important development in the **AI Agents** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

Secret scanning plays a critical role in protecting developers and organizations. It helps catch exposed credentials early and prevents small mistakes from turning into real incidents.

At GitHub’s scale, even small inefficiencies create real friction. Too many false positives make alerts harder to trust.

When alerts feel noisy, developers spend more time triaging and less time fixing real issues. Over time, this slows down remediation and reduces confidence in the system.

To address this challenge, GitHub collaborated with Microsoft Security & AI’s Agents Offense team to bring more contextual reasoning into GitHub’s secret scanning verification. The collaboration applied the verification approach from Agentic Secret Finder, a broader detection and verification system developed to understand potential secrets in context, not just whether they match a secret-like pattern. This helped GitHub explore ways to reduce low-value alerts while preserving the coverage you expect from secret scanning.

### Secret scanning at GitHub today

GitHub secret scanning combines pattern-based detection with AI-based detection to identify potential secrets. Pattern-based detection catches known secret formats, such as partner patterns for tokens and API keys. AI-powered generic secret detection expands coverage to unstructured secrets like passwords that don’t match a known provider pattern.

GitHub already has industry-leading precision for provider-pattern secret detection at massive scale, processing billions of pushes and protecting tens of millions of developers across millions of repositories.

As GitHub expanded into AI-powered secret detection, the next challenge was bringing the precision of AI-detected secrets closer to the same high standard as provider-pattern detections. This collaboration focused on combining GitHub’s large-scale detection pipeline with LLM-based contextual verification to improve alert quality and developer trust.

### Our approach: Make secret scanning alerts trustworthy

Secret scanning is most useful when you can quickly tell which alerts need action.

GitHub already has safeguards to reduce noise, but some secret-like values need more context to determine whether they represent a real exposure. To make those alerts easier to trust, we added more reasoning to the verification step.

By looking at how a detected value appears in code, the system can better separate real exposures from values that only look sensitive. This helps you spend less time investigating low-value alerts and more time fixing the issues that matter.


## Key Takeaways

1. Secret scanning plays a critical role in protecting developers and organizations.
2. At GitHub’s scale, even small inefficiencies create real friction.
3. When alerts feel noisy, developers spend more time triaging and less time fixing real issues.
4. To address this challenge, GitHub collaborated with Microsoft Security & AI’s Agents Offense team to bring more contextual reasoning into GitHub’s secret scanning verification.
5. GitHub secret scanning combines pattern-based detection with AI-based detection to identify potential secrets.


## Why This Matters

Agentic AI is where the industry is heading. From code generation to customer service to data analysis, agents can handle multi-step workflows that previously required human intervention at every stage. This isn't just automation — it's a fundamentally new way of building software.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The technical frontier in AI agents right now is the **orchestration problem** — how do you reliably coordinate multiple specialized agents, each with different capabilities and knowledge, to solve complex tasks? The key architectural patterns emerging are: **handoff protocols** (A2A for cross-platform agent communication), **governance layers** (constraining agent actions within policy boundaries without killing autonomy), and **state management** (maintaining coherent context as work passes between agents). What I find most technically interesting is the convergence of **code-generating agents** (Copilot, Codex) with **tool-using agents** (function calling, MCP) — agents that can both write *and* execute code create a self-improving loop that's qualitatively different from static automation. The challenge is reliability: current agents succeed ~70-85% on complex tasks. Getting to 99%+ requires better evaluation frameworks, graceful degradation patterns, and human-in-the-loop checkpoints for high-stakes decisions.


## Business Translation

**For the C-Suite:** AI agents represent the next wave of operational leverage — not just automating tasks, but automating *judgment*. Early adopters are seeing **40-70% reduction in operational costs** for knowledge work (customer service, compliance review, data analysis). The strategic question isn't whether to adopt agents, but where to deploy them first for maximum ROI. The playbook: start with high-volume, medium-complexity workflows where errors are recoverable (customer inquiries, internal operations), then expand to higher-stakes domains as confidence grows. The organizations that build agent infrastructure now will have a 2-3 year head start when the technology matures.


---

📖 **[Read the original article](https://github.blog/security/making-secret-scanning-more-trustworthy-reducing-false-positives-at-scale/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
