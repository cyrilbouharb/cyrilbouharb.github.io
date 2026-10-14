---
title: "From extraction to action: Using grounding and confidence to build reliable document workflows"
date: 2026-10-14
tags: ["Foundry", "LLM", "Data & AI", "Agentic RAG", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/content-understanding-confidence-grounding-hitl/"
description: "Learn how Azure Content Understanding grounding, field-level confidence, and calibration help teams prioritize human review and build reliable document workflows.
The post From extraction to action: U"
---

There's been an important development in the **Microsoft Foundry** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

> “Civilization advances by extending the number of important operations which we can perform without thinking about them.” — Alfred North Whitehead

“Civilization advances by extending the number of important operations which we can perform without thinking about them.” — Alfred North Whitehead

Automation is the promise of agentic document processing, but getting AI to read a document is only part of the job. The harder part comes when an extracted value starts doing something: paying an invoice, updating a policy record, moving a claim forward. This is where true value is created with automation. At that point, the application needs more than an answer. It needs to know where the answer came from and how much to trust it in order to make a smart decision.

A large insurance organization recently put this to the test working with Microsoft’s Forward Deployed Engineering team to use Content Understanding’s classification, extraction, grounding, and confidence to decide which extracted values needed the most attention from human review.

### Grounding: “Where did this come from?”

An extracted value shouldn’t be a dead end. If Content Understanding returns an Invoice Total of $14,228.02, grounding links that structured value back to the content in the document that supports it. In our latest release, we merged grounding deeper into the extraction flow. That cut average inference token usage by up to 28% and improved accuracy.

https://devblogs.microsoft.com/foundry/wp-content/uploads/sites/89/2026/10/invoice-grounding.mp4

That link changes what an application can do:

- Show evidence with the result, so a reviewer doesn’t have to search the document for the source.

### What a confidence score is

A confidence score is a learned estimate of how reliable a specific field result is. For supported extracted fields, it is a value between 0 and 1. Our latest refresh improved confidence score accuracy, measured by AUROC, by up to 14%.

It’s important to be clear about what the score is not. It isn’t the language model reporting how sure it feels. LLMs are notoriously overconfident about their own answers, and a model that has misread a value can describe the wrong answer just as fluently as the right one. Content Understanding instead uses a separate confidence model, trained to recognize the patterns that tend to come with correct and incorrect extractions.

https://devblogs.microsoft.com/foundry/wp-content/uploads/sites/89/2026/10/invoice-confidence.mp4


## Key Takeaways

1. “Civilization advances by extending the number of important operations which we can perform without thinking about them.” — Alfred North Whitehead.
2. Automation is the promise of agentic document processing, but getting AI to read a document is only part of the job.
3. A large insurance organization recently put this to the test working with Microsoft’s Forward Deployed Engineering team to use Content Understanding’s classification, extraction, grounding, and confidence to decide which extracted values needed the most attention from human review.
4. The solution deliverednearly a 50% reduction in human review burden and 75% faster form onboardingcompared to previous solutions.
5. That result didn’t come from a single magic confidence score threshold.


## Why This Matters

For organizations building AI agents, Foundry simplifies the journey from prototype to production. It removes the friction of stitching together multiple tools and provides enterprise-grade governance through AI Citadel — policy-based controls, content filtering, and audit trails — which is critical when you're operating at public sector scale.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

From a technical standpoint, Foundry's architecture addresses what I consider the four hardest problems in enterprise AI: **model lifecycle management** (versioning, A/B testing, rollback across GPT-5.5, Claude, Gemma, and open-source models), **agent orchestration** (Foundry Agent Service with Microsoft Agent Framework for multi-agent systems), **evaluation at scale** (batch evaluations, continuous monitoring, custom evaluators, and the trace-to-dataset flywheel), and **governance without friction** via AI Citadel (policy-based guardrails, RBAC, content filtering, and audit trails baked into the agent lifecycle rather than bolted on after). The addition of Foundry IQ as the intelligence layer — providing context engineering capabilities so agents can access enterprise knowledge through agentic RAG — is what transforms Foundry from a development platform into an enterprise AI operating system.


## Business Translation

**For the C-Suite:** Foundry directly impacts three board-level concerns: **time-to-value** (reduces AI project timelines from 6-12 months to weeks by eliminating infrastructure setup), **risk management** (built-in responsible AI guardrails and compliance controls reduce regulatory exposure), and **cost predictability** (unified platform means consolidated billing, no sprawl of point solutions each with their own licensing). The competitive moat here is speed: organizations that can iterate on AI use cases 10x faster will capture market share while competitors are still in proof-of-concept.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/content-understanding-confidence-grounding-hitl/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
