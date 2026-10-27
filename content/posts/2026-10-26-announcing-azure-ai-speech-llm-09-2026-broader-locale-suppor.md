---
title: "Announcing Azure AI Speech LLM 09-2026: Broader locale support"
date: 2026-10-26
tags: ["Foundry", "Azure AI", "LLM", "Data & AI", "Data & Analytics", "Agentic RAG", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/announcing-azure-ai-speech-llm-09-2026/"
description: "Learn how Azure AI Speech LLM 09-2026 improves multilingual language and locale support with improved quality and latency.
The post Announcing Azure AI Speech LLM 09-2026: Broader locale support appea"
---

There's been an important development in the **Microsoft Foundry** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

Transcribe 25 new languages at up to 2x the speed.LLM Speech 09-2026 expands Azure AI Speech to 25 additional languages—including 11 Indic languages—while cutting processing time. Whether you’re building voice agents, captioning systems, or contact center analytics, your multilingual workflows just got faster and more accurate, building on the multilingual and phrase-list improvements introduced inLLM Speech 2607.

Picture a clinical consultation in Kuwait where the doctor speaks Arabic, the patient responds in Hindi, and notes are taken in English—LLM Speech handles it all in a single transcription call.

Azure LLM Speech service, accessed through the Fast API, delivers accurate transcripts faster and with necessary (model will be updated to the default), enhancing voice agents, meeting transcription, contact center analytics, or media captioning scenarios.

Try it out now in theFoundry Playground(Azure Speech – Speech to Text), or see REST API and SDK options in ourpublic docs.

### Advancements with this release

LLM Speech 09-2026 model extends supported languages, including additional Indic-language coverage, so more conversations can enter the same transcription workflow. This supports customer scenarios where speakers speak not only multiple languages in one audio input, but also regional variants of a language (i.e. British English, American English, and Indian English). For example, our model now better handles a clinical transcript in Kuwait where the doctor and patients are speaking a mix of Arabic, Hindi, and Indian English.

New Indic locales: Assamese, Bengali, Gujarati, Kannada, Malayalam, Marathi, Odia, Punjabi, Tamil, Telugu, Urdu. Additional new languages include: Catalan, Malay, and Welsh. Seelanguage and locale supportfor the full list of 50 languages covering 60+ locales.

Building on 2607, internal evaluations show measurable accuracy gains, up to 25% improvement in Token Error Rate and 37% in Entity Error Rate metric across internal and public benchmarks like GigaSpeech and VoxPopuli, in this 09-2026 release, particularly on earnings domain entities for financial scenarios.

LLM Speech 09-2026 delivers up to2x fasterprocessing than 2607, returning transcripts sooner for high-volume and time-sensitive workloads, particularly for short audio (5-10 second length) at high concurrencies (multiple streams at once).

### Multilingual transcription, built for real conversations

Many conversation scenarios follow multiple language settings. A customer may begin in English, switch to Spanish to explain a detail, and return to English. LLM Speech usesmultilingual mode by default: omit locale hints when a file contains more than one supported language. A locale hint is useful for genuinely single-language audio, not a way to force recognition of a mixed-language conversation.


## Key Takeaways

1. Transcribe 25 new languages at up to 2x the speed.LLM Speech 09-2026 expands Azure AI Speech to 25 additional languages—including 11 Indic languages—while cutting processing time.
2. Picture a clinical consultation in Kuwait where the doctor speaks Arabic, the patient responds in Hindi, and notes are taken in English—LLM Speech handles it all in a single transcription call.
3. Azure LLM Speech service, accessed through the Fast API, delivers accurate transcripts faster and with necessary (model will be updated to the default), enhancing voice agents, meeting transcription, contact center analytics, or media captioning scenarios.
4. Try it out now in theFoundry Playground(Azure Speech – Speech to Text), or see REST API and SDK options in ourpublic docs.
5. LLM Speech 09-2026 model extends supported languages, including additional Indic-language coverage, so more conversations can enter the same transcription workflow.


## Why This Matters

For organizations building AI agents, Foundry simplifies the journey from prototype to production. It removes the friction of stitching together multiple tools and provides enterprise-grade governance through AI Citadel — policy-based controls, content filtering, and audit trails — which is critical when you're operating at public sector scale.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

From a technical standpoint, Foundry's architecture addresses what I consider the four hardest problems in enterprise AI: **model lifecycle management** (versioning, A/B testing, rollback across GPT-5.5, Claude, Gemma, and open-source models), **agent orchestration** (Foundry Agent Service with Microsoft Agent Framework for multi-agent systems), **evaluation at scale** (batch evaluations, continuous monitoring, custom evaluators, and the trace-to-dataset flywheel), and **governance without friction** via AI Citadel (policy-based guardrails, RBAC, content filtering, and audit trails baked into the agent lifecycle rather than bolted on after). The addition of Foundry IQ as the intelligence layer — providing context engineering capabilities so agents can access enterprise knowledge through agentic RAG — is what transforms Foundry from a development platform into an enterprise AI operating system.


## Business Translation

**For the C-Suite:** Foundry directly impacts three board-level concerns: **time-to-value** (reduces AI project timelines from 6-12 months to weeks by eliminating infrastructure setup), **risk management** (built-in responsible AI guardrails and compliance controls reduce regulatory exposure), and **cost predictability** (unified platform means consolidated billing, no sprawl of point solutions each with their own licensing). The competitive moat here is speed: organizations that can iterate on AI use cases 10x faster will capture market share while competitors are still in proof-of-concept.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/announcing-azure-ai-speech-llm-09-2026/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
