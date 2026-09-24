---
title: "Control where your hosted agent connects with network egress in Foundry Agent Service"
date: 2026-09-24
tags: ["Foundry", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/egress-controls-hosted-agent/"
description: "Define and attach an outbound policy to a hosted agent in Microsoft Foundry, observe calls in Audit, and verify allowed and denied destinations under Enforced mode.
The post Control where your hosted "
---

There's been an important development in the **Microsoft Foundry** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

### Keep destination rules outside your agent code. Observe real calls, then test an explicit outbound boundary

Preview.This walkthrough is for development and evaluation. Network egress controls are not GA, have no preview SLA, and are not intended for production use.[1]

Imagine an invoice agent that looks up a vendor and checks a payment record. Its job needs two APIs. Then a document includes an unfamiliar upload link, or a new helper library follows a URL you did not expect. The question is no longer just “Which tools did I give the agent?” It is“Where can this process send a request?”

In this walkthrough, we will give that invoice agent an explicit destination policy, observe its calls in a test environment, and check that an unapproved destination stays unreachable when enforcement is enabled. The application still owns its business logic and authentication. The outbound policy becomes a separate thing you can review.

### A tool list is not a network boundary

A rule inside one HTTP wrapper only helps when a call uses that wrapper. Our sample puts the destination decision on the hosted-agent definition instead. The public egress sample demonstrates this separation using ordinary outbound HTTP calls.[4]

Conceptual application-traffic view. Foundry’s required platform connectivity is separately allowed; a deny default is not a claim that every runtime connection is blocked.[1]

### 1. Define the destinations your agent needs

For this example, approve a finance API and a vendor API. Do not approve the test upload destination. Start with exact hostnames so a reviewer can understand the intended boundary without interpreting a broad wildcard.

Before you start:use a test Foundry project, a deployable hosted-agent image, permission to create an account-level RAI policy, and controlled HTTPS endpoints. Replace every.examplehostname below with a host you own. These names are placeholders, not live services.

Save this new policy body asinvoice-egress.json. It uses the documented ARM resource shape and deliberately sets both the network mode and default action.[2]

```
{
  "properties": {
    "basePolicyName": "Microsoft.DefaultV2",
    "mode": "Blocking",
    "egressPolicy": {
      "mode": "Audit",
      "defaultAction": "Deny",
      "rules": [
        {
          "name": "allow-finance",
          "ruleType": "Fqdn",
          "match": { "host": "finance.contoso.example" },
          "action": { "actionType": "Allow" }
        },
        {
          "name": "allow-vendors",
          "ruleType": "Fqdn",
          "match": { "host": "vendor
```


## Key Takeaways

1. Preview.This walkthrough is for development and evaluation.
2. Imagine an invoice agent that looks up a vendor and checks a payment record.
3. In this walkthrough, we will give that invoice agent an explicit destination policy, observe its calls in a test environment, and check that an unapproved destination stays unreachable when enforcement is enabled.
4. A rule inside one HTTP wrapper only helps when a call uses that wrapper.
5. Conceptual application-traffic view.


## Why This Matters

For organizations building AI agents, Foundry simplifies the journey from prototype to production. It removes the friction of stitching together multiple tools and provides enterprise-grade governance through AI Citadel — policy-based controls, content filtering, and audit trails — which is critical when you're operating at public sector scale.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

From a technical standpoint, Foundry's architecture addresses what I consider the four hardest problems in enterprise AI: **model lifecycle management** (versioning, A/B testing, rollback across GPT-5.5, Claude, Gemma, and open-source models), **agent orchestration** (Foundry Agent Service with Microsoft Agent Framework for multi-agent systems), **evaluation at scale** (batch evaluations, continuous monitoring, custom evaluators, and the trace-to-dataset flywheel), and **governance without friction** via AI Citadel (policy-based guardrails, RBAC, content filtering, and audit trails baked into the agent lifecycle rather than bolted on after). The addition of Foundry IQ as the intelligence layer — providing context engineering capabilities so agents can access enterprise knowledge through agentic RAG — is what transforms Foundry from a development platform into an enterprise AI operating system.


## Business Translation

**For the C-Suite:** Foundry directly impacts three board-level concerns: **time-to-value** (reduces AI project timelines from 6-12 months to weeks by eliminating infrastructure setup), **risk management** (built-in responsible AI guardrails and compliance controls reduce regulatory exposure), and **cost predictability** (unified platform means consolidated billing, no sprawl of point solutions each with their own licensing). The competitive moat here is speed: organizations that can iterate on AI use cases 10x faster will capture market share while competitors are still in proof-of-concept.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/egress-controls-hosted-agent/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
