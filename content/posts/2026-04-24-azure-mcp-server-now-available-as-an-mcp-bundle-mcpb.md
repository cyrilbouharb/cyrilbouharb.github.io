---
title: "Azure MCP Server now available as an MCP Bundle (.mcpb)"
date: 2026-04-24
tags: ["Foundry", "GitHub", "Data & AI", "RAG", "Architecture"]
categories: ["analysis"]
source_url: "https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/"
description: "Azure MCP Server is now available as an MCP Bundle (.mcpb), enabling one-click installation into Claude Desktop and other MCP-compatible clients.
The post Azure MCP Server now available as an MCP Bund"
---

There's been an important development in the **Microsoft Foundry** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

We’re excited to announce that theAzure MCP Serveris now available as anMCP Bundle(.mcpb). This means you can install the Azure MCP Server intoClaude Desktopand other MCP-compatible clients with minimum setup—no Node.js, Python, or .NET runtime required.

### What are MCP Bundles?

MCP Bundles are a portable packaging format for MCP servers. Think of them like browser extensions (.crx) or VS Code extensions (.vsix), but forModel Context Protocolservers. Each bundle is a ZIP archive containing:

- Amanifest.jsonfile describing the server’s metadata, tools, and runtime requirements.

- The server binary and all of its dependencies—everything needed to run the server on a specific platform.

The key benefit is simplicity. End users don’t need to install any runtimes, manage dependencies, or write configuration files. You download a.mcpbfile, open it in a supported client, and the server is ready to use.

### Why MCP Bundles matter for Azure MCP Server users

Until now, using the Azure MCP Server required one of the following runtimes:

MCP Bundles change this paradigm by providing a self-contained binary thatdoesn’t require any additional runtime. This format is one of the easiest ways to get started with the Azure MCP Server, especially for users who aren’t developers or don’t want to manage runtimes.


## Key Takeaways

1. We’re excited to announce that theAzure MCP Serveris now available as anMCP Bundle(.mcpb).
2. MCP Bundles are a portable packaging format for MCP servers.
3. Until now, using the Azure MCP Server required one of the following runtimes:.
4. MCP Bundles change this paradigm by providing a self-contained binary thatdoesn’t require any additional runtime.
5. Go to theMCP Bundlessection of the latest release poston GitHubpage.


## Why This Matters

For organizations building AI solutions, Foundry simplifies the journey from prototype to production. It removes the friction of stitching together multiple tools and provides guardrails for responsible AI deployment — which is critical when you're operating at enterprise scale.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

Working with enterprise customers, I see Foundry as a game-changer for teams that want to move fast with AI without sacrificing governance. The unified experience means less context-switching and more focus on the actual AI use case. What used to take weeks of infrastructure setup can now be prototyped in hours.

If you're exploring this area, my advice is to start small — pick one concrete use case, prototype it, and iterate. The tooling has matured significantly, and the barrier to entry has never been lower.


## Architecture Overview

{{< mermaid >}}
graph TB
    A[Data Sources] --> B[Ingestion Layer]
    B --> C[Processing & AI]
    C --> D[Model / Agent]
    D --> E[Application Layer]
    E --> F[End Users]

    style A fill:#0078d4,color:#fff
    style B fill:#50e6ff,color:#000
    style C fill:#7719aa,color:#fff
    style D fill:#00b294,color:#fff
    style E fill:#ffb900,color:#000
    style F fill:#0078d4,color:#fff
{{< /mermaid >}}

*High-level architecture — the specific implementation will vary based on your use case and scale requirements.*


---

📖 **[Read the original article](https://devblogs.microsoft.com/azure-sdk/azure-mcp-server-mcpb-support/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
