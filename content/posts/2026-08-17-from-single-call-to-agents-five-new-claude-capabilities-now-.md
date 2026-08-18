---
title: "From single call to agents: five new Claude capabilities now available in Microsoft Foundry"
date: 2026-08-17
tags: ["Foundry", "LLM", "Data & AI", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/five-new-claude-capabilities-now-available-in-foundry/"
description: "Structured outputs, web search, web fetch, MCP connector, and tool search are now available for Claude models hosted on Azure in Microsoft Foundry, turning a model endpoint into a production agent pla"
---

There's been an important development in the **Microsoft Foundry** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

### From single call to agents: five new Claude capabilities now available in Microsoft Foundry

Structured outputs, Web search, Web fetch, MCP connector, and Tool search are now available for Claude models in Microsoft Foundry hosted on Azure, the building blocks that turn a model endpoint into a production agent platform.

When Claude models became generally available in Microsoft Foundry in June 2026, the headline was new hosted on Azure access: frontier Claude models, Azure-native endpoints, Entra ID authentication, and Azure Marketplace billing. That solved theprocurement and governanceproblem. Teams could finally run Claude inside the same subscription, network perimeter, and cost-management surface as the rest of their Azure estate.

But access to a model is not the same as a platform for agents. In the weeks since the generally available launch, we’ve now added more capabilities to the Hosted on Azure options. The pattern we have seen across Foundry customers is the same: a team ships a strong Claude-powered feature, then spends the next quarter rebuilding the same four pieces of scaffolding.

- A retry loop that re-prompts the model because it returned JSON with a trailing comma.

### The part that changes the architecture: these now run hosted on Azure

Claude models in Microsoft Foundry come in two hosting options, chosen when you create the deployment. Previously, the agentic feature set was available only on Hosted on Anthropic deployments, which forced trade-off: teams with a data-handling commitment that prompts and completions stay within Azure had to either give up that commitment or rebuild search, fetch, MCP, and tool routing client-side.

That trade-off is now resolved. Structured outputs, Web search, Web fetch, MCP connector, and Tool search are available on deployments hosted on Azure.

For deployments hosted on Azure, prompts and completions remain within Azure; only usage metadata and content flagged by Anthropic’s safety systems egress to Anthropic. Anthropic acts as an independent processor for Microsoft, and customers using Claude through Foundry are subject to Anthropic’s data use terms.

The practical consequence for regulated industries is significant. A US Data Zone Standard deployment keeps inference within the United States, equivalent to settinginference_geo: "us"on the Claude API and that deployment can now run a web-search-backed research agent, connect to your internal MCP servers, and return grammar-constrained JSON. Twelve months ago that combination required choosing between capability and residency posture. It no longer does.

### The problem

Every team that has put an LLM in a data pipeline has written this code:

```
for attempt in range(3):
    raw = call_model(prompt)
    try:
        data = json.loads(raw)
        validate(data)
        break
    except (json.JSONDecodeError, ValidationError):
        prompt += "\n\nYour last response was invalid JSON. Try again."
```

```
for attempt in range(3):
    raw = call_model(prompt)
    try:
        data = json.loads(raw)
        validate(data)
        break
    except (json.JSONDecodeError, ValidationError):
        prompt += "\n\nYour last response was invalid JSON. Try again."
```

It works most of the time. “Most of the time” is a terrible property for a batch job that processes 400,000 documents overnight, because 0.3% failure is 1,200 rows in a dead-letter queue that somebody has to triage on Monday.


## Key Takeaways

1. Structured outputs, Web search, Web fetch, MCP connector, and Tool search are now available for Claude models in Microsoft Foundry hosted on Azure, the building blocks that turn a model endpoint into a production agent platform.
2. When Claude models became generally available in Microsoft Foundry in June 2026, the headline was new hosted on Azure access: frontier Claude models, Azure-native endpoints, Entra ID authentication, and Azure Marketplace billing.
3. But access to a model is not the same as a platform for agents.
4. Every one of those is undifferentiated engineering.
5. This post walks through each capability: what it does, the API shape on Foundry, a realistic enterprise use case, and the constraints that will bite you in production.


## Why This Matters

For organizations building AI agents, Foundry simplifies the journey from prototype to production. It removes the friction of stitching together multiple tools and provides enterprise-grade governance through AI Citadel — policy-based controls, content filtering, and audit trails — which is critical when you're operating at public sector scale.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

From a technical standpoint, Foundry's architecture addresses what I consider the four hardest problems in enterprise AI: **model lifecycle management** (versioning, A/B testing, rollback across GPT-5.5, Claude, Gemma, and open-source models), **agent orchestration** (Foundry Agent Service with Microsoft Agent Framework for multi-agent systems), **evaluation at scale** (batch evaluations, continuous monitoring, custom evaluators, and the trace-to-dataset flywheel), and **governance without friction** via AI Citadel (policy-based guardrails, RBAC, content filtering, and audit trails baked into the agent lifecycle rather than bolted on after). The addition of Foundry IQ as the intelligence layer — providing context engineering capabilities so agents can access enterprise knowledge through agentic RAG — is what transforms Foundry from a development platform into an enterprise AI operating system.


## Business Translation

**For the C-Suite:** Foundry directly impacts three board-level concerns: **time-to-value** (reduces AI project timelines from 6-12 months to weeks by eliminating infrastructure setup), **risk management** (built-in responsible AI guardrails and compliance controls reduce regulatory exposure), and **cost predictability** (unified platform means consolidated billing, no sprawl of point solutions each with their own licensing). The competitive moat here is speed: organizations that can iterate on AI use cases 10x faster will capture market share while competitors are still in proof-of-concept.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/five-new-claude-capabilities-now-available-in-foundry/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
