---
title: "Turn one giant AI-generated pull request to a reviewable stack"
date: 2026-08-04
tags: ["GitHub", "Data & AI", "AI Agents"]
categories: ["analysis"]
source_url: "https://github.blog/engineering/turn-one-giant-ai-generated-pull-request-to-a-reviewable-stack/"
description: "Instead of one huge, un-reviewable pull request, teach coding agents to decompose work into a clean, ordered stack with GitHub stacked pull requests.
The post Turn one giant AI-generated pull request "
---

There's been an important development in the **Cloud & AI** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

Think about the last big feature you shipped. Be honest. Did you cram it into one giant pull request, or did you split it into smaller scoped pull requests? For years, you have silently had to decide between watching a pull request grow so large that reviewing it becomes a nightmare or breaking it into a chain of smaller pull requests that you have to babysit, sync by hand, and untangle conflicts every time a change is introduced below.

Both options have trade-offs. One is hard toreview, while the other is hard tomaintain.Your decision that day leans towards the less painful option.

Now add coding agents. They are incredibly productive and areprojected to drive a 50% productivity gain across every SDLC stage by 2028,according to Gartner. But, they can’t take away the choice of how you structure your pull requests. They amplify the need to make it.

In this post, follow along with an example of how you can use stacked pull requests to simplify reviews.

### A closer look: Adding product search to a shopping assistant

Let’s say you issue a prompt to add product search to a shopping assistant, walk away and minutes later, literally, you come back to review, steer, and approve. But look closely at what tends to land in that single pull request:

- The client wiring and the UI and the empty/fallback/error states

…all of this and more in one ginormous 1,000+ line diff.

For agents largely trained on how code has traditionally been written over the years, this pattern is their default way of shipping. Let’s play this out.

### GitHub stacked pull requests

Stacked pull requestsintroduce a different and better structure of delivery. The principle is simple: decomposition. Instead of shooting for a single pull request that addresses the issue in its entirety, you break down the feature into logical layers and identify the dependency chain to arrive at your desired goal. This gives you, and your agents, a native way to decompose work that otherwise lands in a giant pull request into a chain of small, focused and independently reviewable layers.

That large pull request that’s hard to review becomes astackof smaller, logically ordered pull requests, each scoped to asingle concern, smallenough to hold in a reviewer’s head and with justenough contextnaturally flowing from the previously reviewed pull request.


## Key Takeaways

1. Think about the last big feature you shipped.
2. In this post, follow along with an example of how you can use stacked pull requests to simplify reviews.
3. Let’s say you issue a prompt to add product search to a shopping assistant, walk away and minutes later, literally, you come back to review, steer, and approve.
4. …all of this and more in one ginormous 1,000+ line diff.
5. For agents largely trained on how code has traditionally been written over the years, this pattern is their default way of shipping.


## Why This Matters

Understanding the latest developments helps teams make informed technology decisions and take advantage of new capabilities as they become available. In a field moving this fast, staying informed is a competitive advantage.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

What I observe across the enterprise landscape is a clear bifurcation: organizations that treat AI as a **platform investment** (with shared infrastructure, evaluation frameworks, and governance) are shipping 5-10 AI use cases per year, while those treating it as **project-by-project experiments** are stuck at 1-2 with diminishing enthusiasm. The technical inflection point is when you move from 'one model, one use case' to 'a portfolio of models serving multiple business domains through shared orchestration.' That's when the economics flip from 'AI is expensive' to 'AI is our highest-ROI investment.' The teams winning this race share common traits: strong data foundations, platform thinking, and a willingness to iterate rapidly on imperfect solutions rather than waiting for perfect ones.


## Business Translation

**For the C-Suite:** The AI investment landscape has shifted from 'if' to 'how fast.' McKinsey estimates generative AI could add **$2.6-4.4 trillion annually** across industries. The organizations capturing this value share a common playbook: invest in platform infrastructure (not point solutions), build internal AI literacy (not just hire specialists), and measure AI ROI with the same rigor as any capital investment. The risk of inaction is now greater than the risk of imperfect execution.


---

📖 **[Read the original article](https://github.blog/engineering/turn-one-giant-ai-generated-pull-request-to-a-reviewable-stack/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
