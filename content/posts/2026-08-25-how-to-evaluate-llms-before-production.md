---
title: "How to evaluate LLMs before production"
date: 2026-08-25
tags: ["GitHub", "LLM", "Data & AI"]
categories: ["analysis"]
source_url: "https://github.blog/ai-and-ml/llms/how-to-evaluate-llms-before-production/"
description: "These are the lessons we learned evaluating LLMs for real-world secret scanning.
The post How to evaluate LLMs before production appeared first on The GitHub Blog."
---

There's been an important development in the **Cloud & AI** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

A language model can perform well on a clean benchmark and still struggle with the cases that matter in production.

Benchmarks and curated datasets are useful when prototyping an LLM-based system. They help teams compare models, test an initial prompt, and determine whether an idea is technically plausible.

But as a system moves closer to production, the evaluation problem changes.

Real inputs are often ambiguous. Labels may be inconsistent. Important context may be missing or truncated. The evaluation set may not reflect the production distribution. Edge cases that rarely appear in benchmarks can become common sources of failure. Even when offline metrics improve, those results may not translate cleanly into production behavior.

### 1. Start with the product decision, not the model

When an LLM system doesn’t perform as expected, the first instinct is often to adjust its technical components.

Teams may rewrite the prompt, add context, introduce another reasoning step, adjust the surrounding pipeline, or switch models. Before making any of these changes, they should define the decision the evaluation is meant to support.

Can the system reduce false positives while preserving enough recall to be safe in a production security workflow?

To answer this question, teams must decide which mistakes are acceptable, which metrics should drive the product decision, and which guardrails must remain within their defined thresholds.

### Primary outcome

This measured the user benefit we were trying to improve:


## Key Takeaways

1. A language model can perform well on a clean benchmark and still struggle with the cases that matter in production.
2. Benchmarks and curated datasets are useful when prototyping an LLM-based system.
3. But as a system moves closer to production, the evaluation problem changes.
4. Real inputs are often ambiguous.
5. We encountered these challenges while evaluating an LLM-based system designed to reduce false positives in GitHub secret scanning.


## Why This Matters

Understanding the latest developments helps teams make informed technology decisions and take advantage of new capabilities as they become available. In a field moving this fast, staying informed is a competitive advantage.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

What I observe across the enterprise landscape is a clear bifurcation: organizations that treat AI as a **platform investment** (with shared infrastructure, evaluation frameworks, and governance) are shipping 5-10 AI use cases per year, while those treating it as **project-by-project experiments** are stuck at 1-2 with diminishing enthusiasm. The technical inflection point is when you move from 'one model, one use case' to 'a portfolio of models serving multiple business domains through shared orchestration.' That's when the economics flip from 'AI is expensive' to 'AI is our highest-ROI investment.' The teams winning this race share common traits: strong data foundations, platform thinking, and a willingness to iterate rapidly on imperfect solutions rather than waiting for perfect ones.


## Business Translation

**For the C-Suite:** The AI investment landscape has shifted from 'if' to 'how fast.' McKinsey estimates generative AI could add **$2.6-4.4 trillion annually** across industries. The organizations capturing this value share a common playbook: invest in platform infrastructure (not point solutions), build internal AI literacy (not just hire specialists), and measure AI ROI with the same rigor as any capital investment. The risk of inaction is now greater than the risk of imperfect execution.


---

📖 **[Read the original article](https://github.blog/ai-and-ml/llms/how-to-evaluate-llms-before-production/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
