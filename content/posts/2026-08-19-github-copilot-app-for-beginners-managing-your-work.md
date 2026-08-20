---
title: "GitHub Copilot app for Beginners: Managing your work"
date: 2026-08-19
tags: ["Copilot", "GitHub Copilot", "GitHub", "AI Agents"]
categories: ["analysis"]
source_url: "https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-managing-your-work/"
description: "If you’re juggling multiple Copilot sessions, use the My work pane to track what's in flight, what's done, and what's next.
The post GitHub Copilot app for Beginners: Managing your work appeared first"
---

There's been an important development in the **GitHub Copilot** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

This is the third post in our GitHub Copilot app for Beginners series. If you’re just joining us, check out,GitHub Copilot app for beginners: Getting started, where we introduced the app and how it helps you work across multiple agent sessions. Our second post goes deeper on working within a session. Here, we’ll look at how to keep all of the requests and work being done on a project organized in one place.

If you’ve been following along in this series, you know that real development is rarely a straight line. You fix a bug here, review a pull request there, and chase down a new idea somewhere in between. As you continue to assign tasks to Copilot and create new pull requests, you’ll quickly find yourself with several proverbial balls in the air.

Being able to manage everything from one centralized location is key, and that’s exactly why the My work pane exists. Below, we’ll cover how you can use it to manage what’s currently in flight, what’s completed, and what’s next.

### Exploring the default views for pull requests and issues

When you open the My work tab, you’ll see three tabs waiting for you. The first is All, which shows all of your pull requests and issues in one place.

This list is automatically filtered based on the projects you’ve touched inside the Copilot app. It’s not every repo you have access to. If there’s a repo you’d like to see here, just create a quick session pointing to that repo, and it’ll show up.

Alongside All, you’ll find three more built-in views:

- Active shows all of your open pull requests and issues.

### Creating your own views and filters

The built-in views are a great start, but you can also create your own. Select New view, and you’ll get the familiar “New view” placeholder name, which you can rename to something like “My issues.”

From here, you can build your filter. You can type it out using the angle-bracket syntax you might recognize from GitHub, or use the UI, which is often the friendlier option when you’re getting started.

For your My issues view, you can add a filter for Is: Issue to grab all issues, then add one more filter for Assignee: Me. Select Save, and now this view shows every issue that’s been assigned to you.

You can also do some quick filtering. Select the filter at the top and you’ll get the same interface. Maybe instead of sorting by Recently updated, you’d rather flip it to Ascending so the oldest items float to the top. From there, save your changes to a brand-new view, update the view you’re currently on, or discard the changes to revert back.


## Key Takeaways

1. This is the third post in our GitHub Copilot app for Beginners series.
2. If you’ve been following along in this series, you know that real development is rarely a straight line.
3. Being able to manage everything from one centralized location is key, and that’s exactly why the My work pane exists.
4. When you open the My work tab, you’ll see three tabs waiting for you.
5. This list is automatically filtered based on the projects you’ve touched inside the Copilot app.


## Why This Matters

Developer productivity is one of the highest-ROI applications of AI today. Copilot is proving that AI can augment — not replace — human expertise, making experienced developers more productive and helping newcomers ramp up faster.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The technical evolution of Copilot is fascinating from an AI systems perspective. We've moved from **completion-based assistance** (predict the next line) to **agent-mode** (understand the intent, decompose the problem, execute multi-file changes, run tests, iterate on failures). This is a fundamental architectural shift — from a stateless token predictor to a stateful reasoning agent with tool use. What's technically impressive is the context management: Copilot now maintains a working memory of your entire codebase, open issues, PR history, and team conventions. The retrieval augmentation layer that grounds suggestions in *your specific codebase* (not just generic patterns) is what makes the difference between a toy and a production tool. The agentic workflows — where Copilot can plan, execute, verify, and self-correct — represent the state of the art in applied AI agents today.


## Business Translation

**For the C-Suite:** Developer talent is the #1 constraint in digital transformation. Copilot delivers a measurable **25-55% productivity gain** (validated by Microsoft/GitHub research across 1M+ developers). In financial terms: a 500-developer organization saves $15-30M annually in equivalent output — without hiring. More importantly, it reduces **time-to-market** for features, which directly impacts revenue capture. The strategic play isn't just efficiency — it's enabling your existing engineering team to tackle projects that were previously impossible given resource constraints.


---

📖 **[Read the original article](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-managing-your-work/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
