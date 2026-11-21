---
title: "Hosted agents in your own virtual network: five checks when the Agents page times out"
date: 2026-11-21
tags: ["Foundry", "Azure AI", "Data & AI", "Agentic RAG", "AI Agents"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/foundry/hosted-agents-private-network-setup/"
description: "The five questions teams ask most when they run hosted agents in their own virtual network: which subnet is the agent subnet, why listing agents times out, why a TLS-inspecting firewall still breaks a"
---

There's been an important development in the **Microsoft Foundry** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

Over the last few weeks I have worked with several teams moving hosted agents into their own virtual network. Different industries, same five questions. This post answers each one with the commands I use to check it.

Picture a financial services team running claims agents in a locked-down network. Public access on the Foundry resource is off. The agent subnet sits in a spoke VNet. Azure Cosmos DB, Storage and Azure AI Search sit behind private endpoints, some of them in a hub VNet. All outbound traffic goes through a firewall that inspects TLS. The deployment succeeds. Then the Agents page spins and fails with a timeout.

Nothing is wrong with the agent. The network around it is missing one piece. Here is how to find it.

### Start with what runs in your agent subnet

When you bring your own VNet, the delegated agent subnet is where the agent infrastructure runs: the micro VMs that run hosted agent sessions, and a single-tenant data proxy for each project. Tool calls go through that data proxy, and its outbound traffic reaches your storage, databases and Key Vault through private endpoints. The platform also signs in to Microsoft Entra ID with managed identity from that subnet before it calls your resources.

So every check below asks one question: can the agent subnet resolve and reach what it needs?

### 1. Find the subnet that matters

Teams that set up networking in the portal are often not sure which subnet became the agent subnet. Ask the Foundry account:

```
az cognitiveservices account show \
  --name my-foundry --resource-group <rg> \
  --query "properties.networkInjections"
```

```
az cognitiveservices account show \
  --name my-foundry --resource-group <rg> \
  --query "properties.networkInjections"
```

```
[
  {
    "scenario": "agent",
    "subnetArmId": "/subscriptions/<sub>/resourceGroups/<rg>/providers/Microsoft.Network/virtualNetworks/<vnet>/subnets/agent-subnet",
    "useMicrosoftManagedNetwork": false
  }
]
```


## Key Takeaways

1. Over the last few weeks I have worked with several teams moving hosted agents into their own virtual network.
2. Picture a financial services team running claims agents in a locked-down network.
3. Nothing is wrong with the agent.
4. When you bring your own VNet, the delegated agent subnet is where the agent infrastructure runs: the micro VMs that run hosted agent sessions, and a single-tenant data proxy for each project.
5. So every check below asks one question: can the agent subnet resolve and reach what it needs?.


## Why This Matters

For organizations building AI agents, Foundry simplifies the journey from prototype to production. It removes the friction of stitching together multiple tools and provides enterprise-grade governance through AI Citadel — policy-based controls, content filtering, and audit trails — which is critical when you're operating at public sector scale.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

From a technical standpoint, Foundry's architecture addresses what I consider the four hardest problems in enterprise AI: **model lifecycle management** (versioning, A/B testing, rollback across GPT-5.5, Claude, Gemma, and open-source models), **agent orchestration** (Foundry Agent Service with Microsoft Agent Framework for multi-agent systems), **evaluation at scale** (batch evaluations, continuous monitoring, custom evaluators, and the trace-to-dataset flywheel), and **governance without friction** via AI Citadel (policy-based guardrails, RBAC, content filtering, and audit trails baked into the agent lifecycle rather than bolted on after). The addition of Foundry IQ as the intelligence layer — providing context engineering capabilities so agents can access enterprise knowledge through agentic RAG — is what transforms Foundry from a development platform into an enterprise AI operating system.


## Business Translation

**For the C-Suite:** Foundry directly impacts three board-level concerns: **time-to-value** (reduces AI project timelines from 6-12 months to weeks by eliminating infrastructure setup), **risk management** (built-in responsible AI guardrails and compliance controls reduce regulatory exposure), and **cost predictability** (unified platform means consolidated billing, no sprawl of point solutions each with their own licensing). The competitive moat here is speed: organizations that can iterate on AI use cases 10x faster will capture market share while competitors are still in proof-of-concept.


---

📖 **[Read the original article](https://devblogs.microsoft.com/foundry/hosted-agents-private-network-setup/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
