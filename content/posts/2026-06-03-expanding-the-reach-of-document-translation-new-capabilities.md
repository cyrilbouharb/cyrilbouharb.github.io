---
title: "Expanding the Reach of Document Translation – New Capabilities Announced at Microsoft Build"
date: 2026-06-03
tags: ["Foundry", "Azure AI", "LLM", "Data & AI", "Agentic RAG"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/document-translation-build-2026/"
description: "Learn how new Document Translation capabilities in Azure Translator, available in Foundry Tools, help developers translate images, PDFs, Office files, DITA, XLIFF, and future LLM-powered document work"
---

There's been an important development in the **Microsoft Foundry** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

Our commitment to advancing cross-language communication takes another major step forward at Microsoft Build. Azure Translator in Foundry Tools is expanding Document Translation with a set of new capabilities designed to meet enterprises where their content lives today — across formats, modalities, and languages. From large language model–powered translations to native image translation and expanded structured content support, these updates help organizations translate more of what they produce, with higher fidelity and less friction.

### Translate image files — synchronous (GA)

With the new synchronous image translation capability, Document Translation can now accept an image file directly — returning a translated image in real time, with layout preserved.

### How It Works

The service uses Azure AI Vision to detect and extract text from the image, translates it with Azure Translator, and renders the translated text back into the image in context. This happens in a single synchronous call, making it ideal for interactive scenarios such as customer support workflows, live preview experiences, and on-demand localization.


## Key Takeaways

1. Our commitment to advancing cross-language communication takes another major step forward at Microsoft Build.
2. With the new synchronous image translation capability, Document Translation can now accept an image file directly — returning a translated image in real time, with layout preserved.
3. The service uses Azure AI Vision to detect and extract text from the image, translates it with Azure Translator, and renders the translated text back into the image in context.
4. Submit an image file to the synchronous Document Translation endpoint, specifying source and target languages as you would for any other document type.
5. This feature uses Azure Translator resource, and translating images incurs additional charges.


## Why This Matters

For organizations building AI agents, Foundry simplifies the journey from prototype to production. It removes the friction of stitching together multiple tools and provides enterprise-grade governance through AI Citadel — policy-based controls, content filtering, and audit trails — which is critical when you're operating at public sector scale.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

From a technical standpoint, Foundry's architecture addresses what I consider the four hardest problems in enterprise AI: **model lifecycle management** (versioning, A/B testing, rollback across GPT-5.5, Claude, Gemma, and open-source models), **agent orchestration** (Foundry Agent Service with Microsoft Agent Framework for multi-agent systems), **evaluation at scale** (batch evaluations, continuous monitoring, custom evaluators, and the trace-to-dataset flywheel), and **governance without friction** via AI Citadel (policy-based guardrails, RBAC, content filtering, and audit trails baked into the agent lifecycle rather than bolted on after). The addition of Foundry IQ as the intelligence layer — providing context engineering capabilities so agents can access enterprise knowledge through agentic RAG — is what transforms Foundry from a development platform into an enterprise AI operating system.


## Business Translation

**For the C-Suite:** Foundry directly impacts three board-level concerns: **time-to-value** (reduces AI project timelines from 6-12 months to weeks by eliminating infrastructure setup), **risk management** (built-in responsible AI guardrails and compliance controls reduce regulatory exposure), and **cost predictability** (unified platform means consolidated billing, no sprawl of point solutions each with their own licensing). The competitive moat here is speed: organizations that can iterate on AI use cases 10x faster will capture market share while competitors are still in proof-of-concept.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/document-translation-build-2026/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
