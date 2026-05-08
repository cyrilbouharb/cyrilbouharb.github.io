#!/usr/bin/env python3
"""
Content pipeline: fetches AI, Foundry, Copilot, GitHub, and Data & AI content
from Microsoft sources, scrapes full articles, writes original blog posts
with analysis and commentary, and outputs Hugo-compatible markdown.
"""

import feedparser
import requests
import json
import os
import re
import hashlib
from datetime import datetime, timezone
from pathlib import Path
from dateutil import parser as dateparser
from bs4 import BeautifulSoup

# ── Configuration ──────────────────────────────────────────────
SOURCES = {
    "azure_ai_blog": [
        "https://azure.microsoft.com/en-us/blog/feed/",
    ],
    "devblogs": [
        "https://devblogs.microsoft.com/azure-sdk/feed/",
        "https://devblogs.microsoft.com/semantic-kernel/feed/",
    ],
    "tech_community_ai": [
        "https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/board?board.id=AI",
        "https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/board?board.id=azure-ai-services",
        "https://techcommunity.microsoft.com/t5/s/gxcuf89792/rss/board?board.id=azure-ai",
    ],
    "github_blog": [
        "https://github.blog/feed/",
    ],
}

RELEVANT_TOPIC_GROUPS = [
    ["artificial intelligence", " ai ", "ai-", "machine learning", "deep learning",
     "neural network", "llm", "large language model", "generative ai", "gen ai",
     "gpt", "openai", "reasoning", "ai agent", "ai model", "multimodal"],
    ["foundry", "azure ai", "ai studio", "ai services", "cognitive service",
     "azure openai", "azure machine learning", "ai search", "ai document",
     "speech service", "vision service", "language service", "content safety"],
    ["copilot", "github copilot", "github actions", "github agent",
     "code generation", "mcp server", "mcp bundle"],
    ["data engineering", "data pipeline", "data lake", "fabric", "synapse",
     "databricks", "real-time analytics", "data warehouse", "power bi",
     "microsoft fabric", "data factory"],
    ["semantic kernel", "autogen", "langchain", "promptflow", "prompt flow",
     "responsible ai", "ai safety", "rag ", "retrieval augmented",
     "vector search", "embedding"],
    ["mlops", "ai architecture", "ai infrastructure", "ai deployment",
     "model deployment", "inference", "fine-tuning", "fine tuning"],
]

INTERNAL_KEYWORDS = [
    "microsoft confidential", "internal only", "nda", "under nda",
    "not for external", "do not share", "microsoft internal",
    "msft internal", "internal use only", "pre-release confidential",
    "[internal]", "embargoed",
]

COMMUNITY_QUESTION_SIGNALS = [
    "how do i ", "how can i ", "can someone help",
    "i am getting error", "i'm getting error",
    "please help", "any idea", "anyone know", "stuck on",
    "i have a question", "does anyone", "has anyone",
    "i need help",
]

SITE_ROOT = Path(__file__).parent.parent
POSTS_DIR = SITE_ROOT / "content" / "posts"
MANIFEST_FILE = SITE_ROOT / "pipeline" / "published_manifest.json"
POSTS_DIR.mkdir(parents=True, exist_ok=True)

HTTP_SESSION = requests.Session()
HTTP_SESSION.headers.update({
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/120.0.0.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
})

# ── Topic context for original commentary ─────────────────────
TOPIC_CONTEXT = {
    "foundry": {
        "name": "Microsoft Foundry",
        "context": "Microsoft Foundry (formerly Azure AI Studio) is Microsoft's unified platform for building, evaluating, and deploying AI applications. It brings together model catalog, prompt engineering, evaluation tools, and deployment pipelines into a single development experience.",
        "why_matters": "For organizations building AI solutions, Foundry simplifies the journey from prototype to production. It removes the friction of stitching together multiple tools and provides guardrails for responsible AI deployment — which is critical when you're operating at enterprise scale.",
        "perspective": "Working with enterprise customers, I see Foundry as a game-changer for teams that want to move fast with AI without sacrificing governance. The unified experience means less context-switching and more focus on the actual AI use case. What used to take weeks of infrastructure setup can now be prototyped in hours.",
    },
    "copilot": {
        "name": "GitHub Copilot",
        "context": "GitHub Copilot is an AI-powered coding assistant that helps developers write code faster and with less effort. It leverages large language models trained on public code to provide contextual suggestions, from single lines to entire functions.",
        "why_matters": "Developer productivity is one of the highest-ROI applications of AI today. Copilot is proving that AI can augment — not replace — human expertise, making experienced developers more productive and helping newcomers ramp up faster.",
        "perspective": "I've seen organizations achieve 30-55% developer productivity gains with Copilot. But the real value isn't just speed — it's reducing cognitive load so developers can focus on architecture and business logic rather than boilerplate. The shift from 'AI writes code for me' to 'AI thinks with me' is where the magic happens.",
    },
    "openai": {
        "name": "Azure OpenAI & GPT Models",
        "context": "Azure OpenAI Service provides enterprise-grade access to OpenAI's powerful models including GPT-4, GPT-4o, and the latest frontier models, with Azure's security, compliance, and regional availability.",
        "why_matters": "Access to frontier AI models through a trusted enterprise platform means organizations can innovate with the latest AI capabilities while meeting their compliance and data residency requirements. The model-as-a-service approach reduces the operational burden of running large-scale inference infrastructure.",
        "perspective": "The pace of model releases is accelerating. For enterprises, the key isn't just having access to the latest model — it's having the infrastructure to evaluate, deploy, and monitor these models responsibly at scale. That's where the Azure wrapper around OpenAI really shines: you get the cutting edge with enterprise guardrails.",
    },
    "semantic_kernel": {
        "name": "Semantic Kernel",
        "context": "Semantic Kernel is Microsoft's open-source SDK for building AI agents and integrating LLMs into applications. It provides a lightweight, extensible framework for orchestrating AI plugins, planners, and memory.",
        "why_matters": "As AI applications move beyond simple chat interfaces to multi-step agentic workflows, developers need robust orchestration frameworks. Semantic Kernel provides the building blocks without locking you into a specific model or provider.",
        "perspective": "Semantic Kernel strikes the right balance between abstraction and control. Unlike heavier frameworks, it lets you start simple and add complexity only where you need it — which is exactly what enterprise teams want. I often recommend it as the starting point for teams building their first AI-powered applications.",
    },
    "agents": {
        "name": "AI Agents",
        "context": "AI agents are autonomous systems that can plan, reason, and take actions to accomplish complex tasks. They represent the next evolution beyond chatbots — systems that can break down problems, use tools, and iterate toward solutions.",
        "why_matters": "Agentic AI is where the industry is heading. From code generation to customer service to data analysis, agents can handle multi-step workflows that previously required human intervention at every stage. This isn't just automation — it's a fundamentally new way of building software.",
        "perspective": "The agent landscape is evolving rapidly. What excites me most is the convergence of multi-agent frameworks with enterprise tools — imagine agents that can not only reason but also execute across your entire technology stack. We're still early, but the trajectory is clear.",
    },
    "data": {
        "name": "Data & AI",
        "context": "The convergence of data platforms and AI is reshaping how organizations manage, analyze, and derive insights from their data. Microsoft Fabric, Azure Synapse, and integrated AI services are enabling end-to-end intelligent data pipelines.",
        "why_matters": "AI is only as good as the data it's built on. The integration of AI capabilities directly into data platforms means organizations can go from raw data to AI-powered insights without the traditional hand-offs between data engineering and ML teams.",
        "perspective": "In my work with enterprise customers, the biggest blocker for AI adoption isn't model quality — it's data readiness. Platforms that unify data engineering and AI development are removing this bottleneck. If you're investing in AI, start with your data strategy.",
    },
    "architecture": {
        "name": "AI Architecture",
        "context": "Building production AI systems requires careful architectural thinking — from model selection and orchestration to scaling, monitoring, and responsible AI practices. Reference architectures and design patterns help teams avoid common pitfalls.",
        "why_matters": "The gap between a working demo and a production AI system is massive. Proper architecture decisions early on determine whether your AI solution will scale, perform reliably, and remain maintainable over time.",
        "perspective": "I spend a lot of time helping teams architect AI solutions. The most common mistake I see is treating AI as a feature bolt-on rather than a first-class architectural concern. Getting the foundation right — data flow, model lifecycle, observability — pays dividends for years.",
    },
    "rag": {
        "name": "RAG (Retrieval Augmented Generation)",
        "context": "RAG combines the power of large language models with enterprise knowledge retrieval. By grounding AI responses in your organization's actual data, RAG dramatically reduces hallucinations and delivers accurate, contextual answers.",
        "why_matters": "RAG is the most practical pattern for enterprise AI today. It lets organizations leverage frontier models while keeping responses grounded in their specific domain knowledge — no fine-tuning required. It's the bridge between general-purpose AI and domain-specific intelligence.",
        "perspective": "Every enterprise AI conversation I have eventually comes back to RAG. The pattern is deceptively simple but getting it right — chunking strategy, embedding models, retrieval quality, reranking — requires real engineering discipline. The teams that invest here see the best results.",
    },
    "default": {
        "name": "Cloud & AI",
        "context": "The cloud and AI landscape continues to evolve rapidly, with new services, capabilities, and patterns emerging regularly. Staying current is essential for building modern, intelligent applications.",
        "why_matters": "Understanding the latest developments helps teams make informed technology decisions and take advantage of new capabilities as they become available. In a field moving this fast, staying informed is a competitive advantage.",
        "perspective": "As a Solution Engineer working at the intersection of cloud and AI, I see firsthand how these technologies are transforming enterprises. The pace of innovation is unprecedented — and the organizations that move quickly and thoughtfully are pulling ahead.",
    },
}


def load_manifest() -> dict:
    if MANIFEST_FILE.exists():
        return json.loads(MANIFEST_FILE.read_text())
    return {"published_urls": [], "published_hashes": []}


def save_manifest(manifest: dict):
    MANIFEST_FILE.write_text(json.dumps(manifest, indent=2))


def content_hash(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:16]


def is_internal(title: str, summary: str) -> bool:
    combined = f"{title} {summary}".lower()
    return any(kw in combined for kw in INTERNAL_KEYWORDS)


def is_community_question(title: str, summary: str) -> bool:
    title_lower = title.lower()
    return any(signal in title_lower for signal in COMMUNITY_QUESTION_SIGNALS)


def is_relevant(title: str, summary: str) -> bool:
    combined = f"{title} {summary}".lower()
    for group in RELEVANT_TOPIC_GROUPS:
        if any(kw in combined for kw in group):
            return True
    return False


def categorize(title: str, summary: str) -> list[str]:
    tags = []
    text = f"{title} {summary}".lower()
    tag_map = {
        "foundry": "Foundry", "ai studio": "Foundry",
        "azure ai": "Azure AI", "ai services": "Azure AI",
        "copilot": "Copilot", "github copilot": "GitHub Copilot",
        "github": "GitHub", "github actions": "GitHub",
        "openai": "OpenAI", "gpt": "OpenAI",
        "machine learning": "ML", "deep learning": "ML",
        "llm": "LLM", "large language model": "LLM",
        "generative ai": "Generative AI", "gen ai": "Generative AI",
        "semantic kernel": "Semantic Kernel",
        "fabric": "Microsoft Fabric", "synapse": "Data & Analytics",
        "data": "Data & AI", "analytics": "Data & Analytics",
        "rag": "RAG", "retrieval augmented": "RAG",
        "vector": "Vector Search", "embedding": "Embeddings",
        "responsible ai": "Responsible AI", "ai safety": "Responsible AI",
        "architecture": "Architecture", "mlops": "MLOps",
        "agent": "AI Agents", "autogen": "AI Agents",
    }
    for keyword, tag in tag_map.items():
        if keyword in text and tag not in tags:
            tags.append(tag)
    return tags or ["AI"]


def detect_primary_topic(title: str, content: str) -> str:
    """Determine the primary topic for commentary context."""
    text = f"{title} {content}".lower()
    topic_scores = {
        "foundry": ["foundry", "ai studio", "azure ai studio"],
        "copilot": ["copilot", "github copilot"],
        "openai": ["openai", "gpt-4", "gpt-5", "gpt ", "azure openai"],
        "semantic_kernel": ["semantic kernel"],
        "agents": ["ai agent", "agent framework", "autogen", "multi-agent"],
        "rag": ["rag", "retrieval augmented", "vector search", "embedding"],
        "data": ["fabric", "synapse", "data lake", "data pipeline", "data engineering"],
        "architecture": ["architecture", "design pattern", "reference architecture"],
    }
    best_topic = "default"
    best_score = 0
    for topic, keywords in topic_scores.items():
        score = sum(1 for kw in keywords if kw in text)
        if score > best_score:
            best_score = score
            best_topic = topic
    return best_topic


def parse_html_content(html: str) -> dict:
    """Parse HTML content (from RSS feed) into structured sections."""
    soup = BeautifulSoup(html, "html.parser")

    sections = []
    current_heading = None
    current_paragraphs = []

    for element in soup.find_all(["h1", "h2", "h3", "h4", "p", "li", "pre", "code", "blockquote"]):
        if element.name in ["h1", "h2", "h3", "h4"]:
            if current_paragraphs:
                sections.append({
                    "heading": current_heading,
                    "content": "\n\n".join(current_paragraphs)
                })
            current_heading = element.get_text(strip=True)
            current_paragraphs = []
        elif element.name in ("pre", "code"):
            code_text = element.get_text(strip=True)
            if code_text and len(code_text) > 20:
                current_paragraphs.append(f"```\n{code_text[:500]}\n```")
        elif element.name == "blockquote":
            quote_text = element.get_text(strip=True)
            if quote_text:
                current_paragraphs.append(f"> {quote_text}")
        elif element.name == "li":
            li_text = element.get_text(strip=True)
            if li_text and len(li_text) > 10:
                current_paragraphs.append(f"- {li_text}")
        else:
            para_text = element.get_text(strip=True)
            if para_text and len(para_text) > 30:
                current_paragraphs.append(para_text)

    if current_paragraphs:
        sections.append({
            "heading": current_heading,
            "content": "\n\n".join(current_paragraphs)
        })

    full_text = "\n\n".join(s.get("content", "") for s in sections)

    key_points = []
    for s in sections:
        for para in s["content"].split("\n\n"):
            if len(para) > 50 and not para.startswith(("-", ">", "```")):
                first_sentence = para.split(". ")[0] + "."
                if len(first_sentence) > 30:
                    key_points.append(first_sentence)
                if len(key_points) >= 6:
                    break
        if len(key_points) >= 6:
            break

    return {
        "sections": sections[:10],
        "full_text": full_text[:5000],
        "key_points": key_points[:6],
        "word_count": len(full_text.split()),
    }


def scrape_article(url: str) -> dict:
    """Fetch and extract the full article content from a URL."""
    try:
        resp = HTTP_SESSION.get(url, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        # Remove noise elements
        for tag in soup.find_all(["script", "style", "nav", "footer",
                                   "aside", "header", "form", "iframe"]):
            tag.decompose()

        # Find the main article content
        article = (
            soup.find("article") or
            soup.find("div", class_=re.compile(
                r"(article|post|content|entry|blog)[-_]?(body|content|text)?", re.I
            )) or
            soup.find("main") or
            soup.find("div", {"role": "main"})
        )

        if not article:
            article = soup.find("body") or soup

        # Extract headings and their content
        sections = []
        current_heading = None
        current_paragraphs = []

        for element in article.find_all(["h1", "h2", "h3", "h4", "p", "li", "pre", "code", "blockquote"]):
            if element.name in ["h1", "h2", "h3", "h4"]:
                if current_paragraphs:
                    sections.append({
                        "heading": current_heading,
                        "content": "\n\n".join(current_paragraphs)
                    })
                current_heading = element.get_text(strip=True)
                current_paragraphs = []
            elif element.name in ("pre", "code"):
                code_text = element.get_text(strip=True)
                if code_text and len(code_text) > 20:
                    current_paragraphs.append(f"```\n{code_text[:500]}\n```")
            elif element.name == "blockquote":
                quote_text = element.get_text(strip=True)
                if quote_text:
                    current_paragraphs.append(f"> {quote_text}")
            elif element.name == "li":
                li_text = element.get_text(strip=True)
                if li_text and len(li_text) > 10:
                    current_paragraphs.append(f"- {li_text}")
            else:
                para_text = element.get_text(strip=True)
                if para_text and len(para_text) > 30:
                    current_paragraphs.append(para_text)

        if current_paragraphs:
            sections.append({
                "heading": current_heading,
                "content": "\n\n".join(current_paragraphs)
            })

        full_text = "\n\n".join(s.get("content", "") for s in sections)

        # Extract key sentences from substantial paragraphs
        key_points = []
        for s in sections:
            for para in s["content"].split("\n\n"):
                if len(para) > 50 and not para.startswith(("-", ">", "```")):
                    first_sentence = para.split(". ")[0] + "."
                    if len(first_sentence) > 30:
                        key_points.append(first_sentence)
                    if len(key_points) >= 6:
                        break
            if len(key_points) >= 6:
                break

        return {
            "sections": sections[:10],
            "full_text": full_text[:5000],
            "key_points": key_points[:6],
            "word_count": len(full_text.split()),
        }

    except Exception as e:
        print(f"    ⚠ Could not scrape {url}: {e}")
        return {"sections": [], "full_text": "", "key_points": [], "word_count": 0}


def build_blog_post(entry: dict, scraped: dict) -> str:
    """Generate a full blog article with original commentary and analysis."""
    title = entry["title"]
    summary = entry["summary"]
    url = entry["url"]
    full_text = scraped["full_text"] or summary
    tags = categorize(title, full_text)
    topic = detect_primary_topic(title, full_text)
    ctx = TOPIC_CONTEXT.get(topic, TOPIC_CONTEXT["default"])
    date_str = entry["date"].strftime("%Y-%m-%d")

    body_parts = []

    # ── Opening: set the scene ──
    body_parts.append(
        f"There's been an important development in the **{ctx['name']}** space "
        f"that caught my attention, and I wanted to break it down — not just "
        f"what was announced, but why it matters and how it fits into the bigger picture.\n"
    )

    # ── What's New: core content from the article ──
    body_parts.append("## What's New\n")

    if scraped["sections"]:
        used = 0
        for section in scraped["sections"]:
            if used >= 3:
                break
            content = section["content"]
            if len(content) < 50:
                continue
            heading = section.get("heading", "")
            if heading and heading.lower() not in (
                "comments", "related", "share", "tags", "footer",
                "recommended", "see also", "next steps"
            ):
                body_parts.append(f"### {heading}\n")
            paragraphs = content.split("\n\n")
            meaningful = [p for p in paragraphs if len(p) > 40][:4]
            body_parts.append("\n\n".join(meaningful))
            body_parts.append("")
            used += 1
    else:
        body_parts.append(summary)

    # ── Key Takeaways ──
    if scraped["key_points"]:
        body_parts.append("\n## Key Takeaways\n")
        for i, point in enumerate(scraped["key_points"][:5], 1):
            point = point.strip().rstrip(".")
            body_parts.append(f"{i}. {point}.")
        body_parts.append("")

    # ── Why This Matters ──
    body_parts.append(f"\n## Why This Matters\n")
    body_parts.append(ctx["why_matters"])
    body_parts.append(
        "\nThis development is particularly significant because it reflects "
        "the broader industry shift toward making AI more accessible, "
        "enterprise-ready, and integrated into existing workflows. For teams "
        "already invested in the Microsoft ecosystem, this is a clear signal "
        "of where the platform is heading.\n"
    )

    # ── My Take ──
    body_parts.append(f"\n## My Take\n")
    body_parts.append(ctx["perspective"])
    body_parts.append(
        "\nIf you're exploring this area, my advice is to start small — "
        "pick one concrete use case, prototype it, and iterate. The tooling "
        "has matured significantly, and the barrier to entry has never been lower.\n"
    )

    # ── Architecture diagram if applicable ──
    text_lower = (title + " " + full_text).lower()
    if any(kw in text_lower for kw in [
        "architecture", "pipeline", "workflow", "integration",
        "deploy", "infrastructure", "pattern"
    ]):
        body_parts.append("""
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
""")

    # ── Closing ──
    body_parts.append(f"""
---

📖 **[Read the original article]({url})** for the full details and official documentation.

*Written by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft. Opinions and analysis are my own and do not represent Microsoft's official position.*
""")

    description = summary[:200].replace('"', '\\"') if summary else title
    frontmatter = f"""---
title: "{title.replace('"', '\\"')}"
date: {date_str}
tags: {json.dumps(tags)}
categories: ["analysis"]
source_url: "{url}"
description: "{description}"
---"""

    return frontmatter + "\n\n" + "\n".join(body_parts)


def fetch_rss_entries(urls: list[str]) -> list[dict]:
    entries = []
    for url in urls:
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:5]:
                pub_date = None
                if hasattr(entry, 'published'):
                    pub_date = dateparser.parse(entry.published)
                elif hasattr(entry, 'updated'):
                    pub_date = dateparser.parse(entry.updated)

                summary = getattr(entry, 'summary', '')
                summary = re.sub(r'<[^>]+>', '', summary)

                # Extract full content from RSS if available (many blogs include it)
                rss_content = ""
                if hasattr(entry, 'content') and entry.content:
                    rss_content = entry.content[0].get('value', '')

                entries.append({
                    "title": entry.get("title", "Untitled"),
                    "url": entry.get("link", ""),
                    "summary": summary[:1000],
                    "rss_content": rss_content,
                    "date": pub_date or datetime.now(timezone.utc),
                    "source": url,
                })
        except Exception as e:
            print(f"  ⚠ Failed to fetch {url}: {e}")
    return entries


def create_hugo_post(entry: dict, manifest: dict) -> bool:
    """Create a full blog article from a feed entry."""
    url_hash = content_hash(entry["url"])

    if entry["url"] in manifest["published_urls"]:
        return False
    if url_hash in manifest["published_hashes"]:
        return False

    if is_internal(entry["title"], entry["summary"]):
        print(f"  🚫 Skipping internal: {entry['title']}")
        return False

    if is_community_question(entry["title"], entry["summary"]):
        print(f"  💬 Skipping question: {entry['title']}")
        return False

    if not is_relevant(entry["title"], entry["summary"]):
        print(f"  ⏭️  Skipping off-topic: {entry['title']}")
        return False

    print(f"  📄 Scraping: {entry['title'][:60]}...")
    scraped = scrape_article(entry["url"])

    # If scraping got very little, try parsing RSS content instead
    if scraped["word_count"] < 100 and entry.get("rss_content"):
        print(f"    → Scraping yielded only {scraped['word_count']} words, using RSS content...")
        scraped = parse_html_content(entry["rss_content"])

    # Skip if we still don't have enough content for a real article
    if scraped["word_count"] < 50:
        print(f"  ⚠️  Skipping (not enough content): {entry['title']}")
        return False

    print(f"    → {scraped['word_count']} words, {len(scraped['key_points'])} key points")

    post_content = build_blog_post(entry, scraped)

    date_str = entry["date"].strftime("%Y-%m-%d")
    slug = re.sub(r'[^a-z0-9]+', '-', entry["title"].lower()).strip('-')[:60]
    filename = f"{date_str}-{slug}.md"

    (POSTS_DIR / filename).write_text(post_content)
    manifest["published_urls"].append(entry["url"])
    manifest["published_hashes"].append(url_hash)
    print(f"  ✅ Created: {filename}")
    return True


def main():
    print("🚀 Content Pipeline Starting...")
    manifest = load_manifest()
    new_posts = 0

    for source_name, urls in SOURCES.items():
        print(f"\n📡 Fetching from {source_name}...")
        entries = fetch_rss_entries(urls)
        print(f"  Found {len(entries)} entries")

        for entry in entries:
            if create_hugo_post(entry, manifest):
                new_posts += 1

    save_manifest(manifest)
    print(f"\n✨ Pipeline complete: {new_posts} new posts created")
    return new_posts


if __name__ == "__main__":
    main()
