---
title: "Disrupting supply chain attacks on npm and GitHub Actions"
date: 2026-07-28
tags: ["GitHub"]
categories: ["analysis"]
source_url: "https://github.blog/security/supply-chain-security/disrupting-supply-chain-attacks-on-npm-and-github-actions/"
description: "Explore the changes we've shipped across npm and GitHub Actions over the past few months to disrupt supply chain attack techniques and limit their impact.
The post Disrupting supply chain attacks on n"
---

There's been an important development in the **Cloud & AI** space that caught my attention, and I wanted to break it down — not just what was announced, but why it matters and how it fits into the bigger picture.

## What's New

In the past year, there’s been a pattern of supply chain attacks that target weaknesses in package repositories and CI/CD systems to quickly spread malware to hundreds of open source projects. This malware seeks to exfiltrate credentials both to broadly spread the attack, as well as for later exploitation.

We’ve written a few times about our plans for hardening the supply chain:Our plan for a more secure npm supply chainin September 2025,Strengthening supply chain security: Preparing for the next malware campaignin December 2025, andWhat’s coming to our GitHub Actions 2026 security roadmapin March 2026. In this post, we’re updating you on changes we’ve implemented that directly disrupt some of the most common and impactful supply chain attack techniques.

### Anatomy of supply chain attacks

Supply chain attacks chain together several weaknesses, and there is no single security capability that can stop them. Addressing them takes a holistic approach, prioritizing the mitigations that break the most impactful links in the attack chain. Our teams have been studying these attacks to deploy several improvements that disrupt them and limit their impact. This is possible thanks to collaboration with the security research and developer communities.

The attacks vary in how they spread across the software ecosystem. However, most of these attacks follow similar techniques to gain initial access to a project, escalate privileges, and distribute across users and software. Improvements made to npm and GitHub Actions in the past few months have been focused on cutting off specific, common techniques and providing ways for customers to identify and respond to these attacks.

### Initial compromise

Attacks start by compromising a single project, often by directly compromising a maintainer’s account or by targeting the project’s actions workflows.

- npm adds preventive account protection for high-impact accounts(June 2026): Frequently, attacks start with a phishing campaign targeting maintainers. With this change, high-impact npm accounts are now put into a read-only mode for 72 hours when they change their email or use a 2FA recovery code. This delay allows maintainers time to respond and recover the account before their account can be used to start an attack.

- Safer pull_request_target defaults for GitHub Actions checkout(June 2026): A common vulnerability in a project’s CI/CD pipelines are“pwn requests,”where a workflow triggers on pull requests from forks and then executes user-submitted and untrusted code from that fork. We changed the default behavior ofactions/checkoutto prevent the checkout of untrusted code from forks in commonly exploited triggers unless you explicitly opt-out (after reviewing your risk). This change and its backport to older versions cut off one of the most common vulnerable code patterns leading to code execution in GitHub Actions CI/CD workflows and initial project compromise.

- Control who and what triggers GitHub Actions workflows(June 2026): Maybe you’d prefer to opt-out of these risky action triggers altogether or limit who can trigger them. This new control lets you set enterprise, organization, or repository level policies on who is allowed to trigger workflows and what trigger types are allowed. These workflow execution policies provide a governable and customizable layer of least-privilege around Action workflows that reduce the attack surface of your CI/CD infrastructure.


## Key Takeaways

1. In the past year, there’s been a pattern of supply chain attacks that target weaknesses in package repositories and CI/CD systems to quickly spread malware to hundreds of open source projects.
2. We’ve written a few times about our plans for hardening the supply chain:Our plan for a more secure npm supply chainin September 2025,Strengthening supply chain security: Preparing for the next malware campaignin December 2025, andWhat’s coming to our GitHub Actions 2026 security roadmapin March 2026.
3. Supply chain attacks chain together several weaknesses, and there is no single security capability that can stop them.
4. The attacks vary in how they spread across the software ecosystem.
5. Attacks start by compromising a single project, often by directly compromising a maintainer’s account or by targeting the project’s actions workflows.


## Why This Matters

Understanding the latest developments helps teams make informed technology decisions and take advantage of new capabilities as they become available. In a field moving this fast, staying informed is a competitive advantage.

This development is particularly significant because it reflects the broader industry shift toward making AI more accessible, enterprise-ready, and integrated into existing workflows. For teams already invested in the Microsoft ecosystem, this is a clear signal of where the platform is heading.


## My Take

What I observe across the enterprise landscape is a clear bifurcation: organizations that treat AI as a **platform investment** (with shared infrastructure, evaluation frameworks, and governance) are shipping 5-10 AI use cases per year, while those treating it as **project-by-project experiments** are stuck at 1-2 with diminishing enthusiasm. The technical inflection point is when you move from 'one model, one use case' to 'a portfolio of models serving multiple business domains through shared orchestration.' That's when the economics flip from 'AI is expensive' to 'AI is our highest-ROI investment.' The teams winning this race share common traits: strong data foundations, platform thinking, and a willingness to iterate rapidly on imperfect solutions rather than waiting for perfect ones.


## Business Translation

**For the C-Suite:** The AI investment landscape has shifted from 'if' to 'how fast.' McKinsey estimates generative AI could add **$2.6-4.4 trillion annually** across industries. The organizations capturing this value share a common playbook: invest in platform infrastructure (not point solutions), build internal AI literacy (not just hire specialists), and measure AI ROI with the same rigor as any capital investment. The risk of inaction is now greater than the risk of imperfect execution.


---

📖 **[Read the original article](https://github.blog/security/supply-chain-security/disrupting-supply-chain-attacks-on-npm-and-github-actions/)** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
