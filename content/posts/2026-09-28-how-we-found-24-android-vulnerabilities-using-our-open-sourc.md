---
title: "How we found 24 Android vulnerabilities using our open source AI security agent"
date: 2026-09-28
tags: ["Copilot", "GitHub Copilot", "GitHub", "LLM", "Data & AI", "AI Agents"]
categories: ["analysis"]
source_url: "https://github.blog/security/how-we-found-24-android-vulnerabilities-using-our-open-source-ai-security-agent/"
description: "A look at the targeted AI taskflows behind these findings, the critical Android bugs they uncovered, and how to run the same open-source agent on your own app.
The post How we found 24 Android vulnera"
---

There's been an important development in the **GitHub Copilot** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

With the rise of AI in the security space, our team created theGitHub Security Lab Taskflow Agentas a way for security researchers to easily automate, package, and share the AI prompts and workflows that they find effective for their work. In this blog post, I’ll share how I created auditing taskflows to find vulnerabilities in Android applications.

While new models are getting better at understanding code, custom taskflow prompts let security researchers guide them—splitting research into incremental steps to help the LLM find complex vulnerabilities faster, or that it would have missed entirely.

Using these taskflows, I’ve reported more than 20 vulnerabilities in Android applications. You can check out ouradvisories pageto see when new vulnerabilities are disclosed. Otherwise, keep reading for a few concrete examples of high-impact vulnerabilities that these taskflows found.

### How to run the taskflows on your own project

Want to get started right away? The taskflows are open source and easy to run yourself. Please note: A GitHub Copilot license is required, and the prompts will use premium model requests. Running the taskflows can result in many tool calls, which can easily consume a large amount of tokens.

- Go to the seclab-taskflows repository and start a codespace.

- Wait a few minutes for the codespace to initialize.

- In the terminal, run./scripts/audit/run_mobile.sh myorg/myrepo

### Creating targeted audit taskflows for Android apps

My colleagues Peter and Mo previously wrote ablog postabout their audit task flows. Although those taskflows already work well on their own, Android applications have their own specific classes of vulnerabilities that we’d like the taskflows to focus on, so we need to guide them.

First, I added a taskflow calledgather_mobile_entry_point_info.yaml. Entry points are places in the code that attacker-controlled data could flow through. This taskflow takes the entry points and separates them into mobile entry points and non-mobile entry points. This allows the AI to run on repos that contain a variety of different application types—a mobile application, web servers, desktop applicationswhile still understanding the correct attack surface.

```
gather_mobile_entry_point_info.yaml
```

Second, I editedclassify_application_local.yaml. In it, I specify a list of popular vulnerability classes and ask the LLM to consider them in the context of each entry point and component. Since mobile application vulnerabilities are less widely known and LLMs are non-deterministic, we should ensure the LLM checks for certain essential vulnerabilities classes. For example, if in the previous step the taskflow identified an intent-based entry point, then it should have a list of common intent-based vulnerabilities it will check for, such as confused deputy or insecure broadcasts. This helps the LLM find connections between components and maintain an overview of the threat model.


## Key Takeaways

1. With the rise of AI in the security space, our team created theGitHub Security Lab Taskflow Agentas a way for security researchers to easily automate, package, and share the AI prompts and workflows that they find effective for their work.
2. While new models are getting better at understanding code, custom taskflow prompts let security researchers guide them—splitting research into incremental steps to help the LLM find complex vulnerabilities faster, or that it would have missed entirely.
3. Using these taskflows, I’ve reported more than 20 vulnerabilities in Android applications.
4. Want to get started right away? The taskflows are open source and easy to run yourself.
5. It might take an hour or two to finish on a medium-sized repository.


## Why This Matters

Developer productivity is one of the highest-ROI applications of AI today. Copilot is proving that AI can augment — not replace — human expertise, making experienced developers more productive and helping newcomers ramp up faster.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The technical evolution of Copilot is fascinating from an AI systems perspective. We've moved from **completion-based assistance** (predict the next line) to **agent-mode** (understand the intent, decompose the problem, execute multi-file changes, run tests, iterate on failures). This is a fundamental architectural shift — from a stateless token predictor to a stateful reasoning agent with tool use. What's technically impressive is the context management: Copilot now maintains a working memory of your entire codebase, open issues, PR history, and team conventions. The retrieval augmentation layer that grounds suggestions in *your specific codebase* (not just generic patterns) is what makes the difference between a toy and a production tool. The agentic workflows — where Copilot can plan, execute, verify, and self-correct — represent the state of the art in applied AI agents today.


## Business Translation

**For the C-Suite:** Developer talent is the #1 constraint in digital transformation. Copilot delivers a measurable **25-55% productivity gain** (validated by Microsoft/GitHub research across 1M+ developers). In financial terms: a 500-developer organization saves $15-30M annually in equivalent output — without hiring. More importantly, it reduces **time-to-market** for features, which directly impacts revenue capture. The strategic play isn't just efficiency — it's enabling your existing engineering team to tackle projects that were previously impossible given resource constraints.


---

📖 **[Read the original article](https://github.blog/security/how-we-found-24-android-vulnerabilities-using-our-open-source-ai-security-agent/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
