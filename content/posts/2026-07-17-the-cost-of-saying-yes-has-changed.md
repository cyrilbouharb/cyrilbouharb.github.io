---
title: "The cost of saying yes has changed"
date: 2026-07-17
tags: ["Data & AI", "AI Agents"]
categories: ["analysis"]
source_url: "https://github.blog/engineering/the-cost-of-saying-yes-has-changed/"
description: "The cost of writing code dropped; the cost of owning it didn't. A framework for deciding which changes are actually cheap in the AI era.
The post The cost of saying yes has changed appeared first on T"
---

There's been an important development in the **Cloud & AI** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

The most expensive part of a small feature request used to be writing the code. Now it’s usually the meeting about whether or not to write the code.

That’s a real shift, and it quietly breaks a lot of engineering instincts. Engineers learn early that most “small asks” aren’t small: they need tests, a rollout plan, someone to think through the edge cases and own the behavior after it ships. A two-hour change can become a two-week distraction if it touches the wrong part of the system. So we push back. Is this really needed? Does it belong in this release? Does it change a contract we already agreed to? I’m not giving that instinct up.

But it rests on an assumption that’s quietly breaking, which is that writing the first version of the code is the expensive step. For a specific class of change, it no longer is. If you can tell those changes apart from the rest, you can replace “is this in scope?” with a question you can answer in thirty minutes instead of a two-day debate.

### The debate often costs more than the patch

Here’s a pattern I keep seeing. Someone asks for a small change such as surfacing alast_active_attimestamp that already exists in the backend on a settings page. The team spends forty minutes in a thread. One person says it sounds risky. Someone remembers a related migration from two years ago. Someone mentions the deadline. Eventually we land on “probably a day or two, could be more,” with low confidence, primarily because nobody has actually tried it.

That process made sense when trying was the expensive part. You had to stop what you were doing, load the context into your head, make the change by hand, write the tests, then discover the second- and third-order consequences. When the first attempt is cheap, defending the boundary can cost more than crossing it.

An agent can produce that first patch in the time the thread takes to warm up. It’s not free and definitely not automatically correct. But it is cheap enough that the smart move is often to stop guessing and look at a real diff.

### The first patch is a price check, not the product

The mistake is to treat the generated patch as the deliverable. It isn’t. It’s a probe. It turns an abstract scope argument into a concrete artifact you can interrogate:

- Does it touch the files you expected, or does it sprawl across five packages?

- Are the tests obvious, or does the change resist being tested?

- Does it preserve the existing abstractions?


## Key Takeaways

1. The most expensive part of a small feature request used to be writing the code.
2. That’s a real shift, and it quietly breaks a lot of engineering instincts.
3. But it rests on an assumption that’s quietly breaking, which is that writing the first version of the code is the expensive step.
4. Here’s a pattern I keep seeing.
5. That process made sense when trying was the expensive part.


## Why This Matters

Understanding the latest developments helps teams make informed technology decisions and take advantage of new capabilities as they become available. In a field moving this fast, staying informed is a competitive advantage.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

What I observe across the enterprise landscape is a clear bifurcation: organizations that treat AI as a **platform investment** (with shared infrastructure, evaluation frameworks, and governance) are shipping 5-10 AI use cases per year, while those treating it as **project-by-project experiments** are stuck at 1-2 with diminishing enthusiasm. The technical inflection point is when you move from 'one model, one use case' to 'a portfolio of models serving multiple business domains through shared orchestration.' That's when the economics flip from 'AI is expensive' to 'AI is our highest-ROI investment.' The teams winning this race share common traits: strong data foundations, platform thinking, and a willingness to iterate rapidly on imperfect solutions rather than waiting for perfect ones.


## Business Translation

**For the C-Suite:** The AI investment landscape has shifted from 'if' to 'how fast.' McKinsey estimates generative AI could add **$2.6-4.4 trillion annually** across industries. The organizations capturing this value share a common playbook: invest in platform infrastructure (not point solutions), build internal AI literacy (not just hire specialists), and measure AI ROI with the same rigor as any capital investment. The risk of inaction is now greater than the risk of imperfect execution.


---

📖 **[Read the original article](https://github.blog/engineering/the-cost-of-saying-yes-has-changed/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
