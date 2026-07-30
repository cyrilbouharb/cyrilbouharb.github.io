---
title: "Stacked sessions and pull requests in the GitHub Copilot app"
date: 2026-07-30
tags: ["Copilot", "GitHub Copilot", "GitHub", "OpenAI"]
categories: ["analysis"]
source_url: "https://github.blog/ai-and-ml/github-copilot/stacked-sessions-and-pull-requests-in-the-github-copilot-app/"
description: "Learn how I modernized an old codebase of mine using stacked sessions and pull requests in the GitHub Copilot app.
The post Stacked sessions and pull requests in the GitHub Copilot app appeared first "
---

There's been an important development in the **GitHub Copilot** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

I want you to look at this screenshot for a moment from theGitHub Copilot app. It’s a small one, it’s got a lot of icons, and it tells the most glorious story that I’m really excited about.

This image is a set of stacked sessions. They’re a series of tasks in the same repository, where each session builds off each other!

More on those below, but first, why is this screenshot so magical? We need to go back more than a decade to start. I have this very old repo of mine for a personal app. I first made itagesago (end of 2014-ish), and it’s done what I want it to do (it’s like a personal “life” dashboard of calendars and smart devices in my home and task management) for all those years. I occasionally do some updates, but those have gotten harder and harder to wrangle.

My dependencies had gottenold. Embarrassingly old. I was using React 15 (which was released in 2016), Less for CSS pre-processing, and a version of react-bootstrap from around that time. Yes, you read that right.Bootstrap. This was old.

### First step: Could I one-shot this?

I tried though! This is the prompt that I used in Plan mode:

```
I want to modernize the frontend for this project. I first wrote a lot of this code more than 10 years ago and it should be cleaned up a lot. I'm thinking we start either using Tailwind or just vanilla CSS (please vet everything to help me decide), we remove all Less (etc), and clean everything up accessibility-wise and responsiveness-wise. Right now I really want to just focus on styles, and then slowly but surely organize and consolidate the React functionality. It might be worth modernizing d
```

```
I want to modernize the frontend for this project. I first wrote a lot of this code more than 10 years ago and it should be cleaned up a lot. I'm thinking we start either using Tailwind or just vanilla CSS (please vet everything to help me decide), we remove all Less (etc), and clean everything up accessibility-wise and responsiveness-wise. Right now I really want to just focus on styles, and then slowly but surely organize and consolidate the React functionality. It might be worth modernizing d
```

I passed this into Claude Opus 4.8 got a Rubber Duck review from GPT-5.5, and had to do quite a bit of back-and-forth to make decisions. Once I got to a place I was happy with, I hit “go” and let the app go to town on my project to see if it would work!

### Second step: Realizing I had tried this before

So, remember when I said I’d “tried and given up before?” Turns out, I actually had an olddevbranch where I actually had modernized some parts, and didn’t realize the compatibility issues I’d run into.

When I ran the new version from this session, I realized that I was branching offmain, but that my current deployment that I was using regularly was using my partially updated version ondev. So, some wanted features that I had made for myself needed to be included in this set of changes. But, the changes werejustbig enough that I actually had to apply those changes to thedevbranch to save my sanity a bit, rather than pull in thedevchanges tomain.

Pre-AI… my word, this would have made me pull my hair out in frustration. I was admittedly frustrated here, too. I had spent time and tokens trying to get this running with what I thought was a decent plan. But! I was able to switch gears (and sessions) with a simple ask, which was way cooler than I expected it to be:

All was not wasted! Copilot made a new session for me, closed the pull request I had attempted, and ported my styling decisions to changes it was applying to the dev branch.


## Key Takeaways

1. I want you to look at this screenshot for a moment from theGitHub Copilot app.
2. This image is a set of stacked sessions.
3. More on those below, but first, why is this screenshot so magical? We need to go back more than a decade to start.
4. Trying to untangle this absolute mess before AI would have taken me weeks.
5. …but wedohave AI now, and so I fired up the GitHub Copilot app, added the repo, and got started.


## Why This Matters

Developer productivity is one of the highest-ROI applications of AI today. Copilot is proving that AI can augment — not replace — human expertise, making experienced developers more productive and helping newcomers ramp up faster.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

The technical evolution of Copilot is fascinating from an AI systems perspective. We've moved from **completion-based assistance** (predict the next line) to **agent-mode** (understand the intent, decompose the problem, execute multi-file changes, run tests, iterate on failures). This is a fundamental architectural shift — from a stateless token predictor to a stateful reasoning agent with tool use. What's technically impressive is the context management: Copilot now maintains a working memory of your entire codebase, open issues, PR history, and team conventions. The retrieval augmentation layer that grounds suggestions in *your specific codebase* (not just generic patterns) is what makes the difference between a toy and a production tool. The agentic workflows — where Copilot can plan, execute, verify, and self-correct — represent the state of the art in applied AI agents today.


## Business Translation

**For the C-Suite:** Developer talent is the #1 constraint in digital transformation. Copilot delivers a measurable **25-55% productivity gain** (validated by Microsoft/GitHub research across 1M+ developers). In financial terms: a 500-developer organization saves $15-30M annually in equivalent output — without hiring. More importantly, it reduces **time-to-market** for features, which directly impacts revenue capture. The strategic play isn't just efficiency — it's enabling your existing engineering team to tackle projects that were previously impossible given resource constraints.


---

📖 **[Read the original article](https://github.blog/ai-and-ml/github-copilot/stacked-sessions-and-pull-requests-in-the-github-copilot-app/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
