#!/usr/bin/env python3
"""
Content pipeline: fetches AI, Foundry, Copilot, GitHub, and Data & AI content
from Microsoft sources, filters for relevance, deduplicates,
and outputs Hugo-compatible markdown posts.
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

# ── Configuration ──────────────────────────────────────────────
# RSS sources focused on AI, Foundry, Copilot, GitHub, and Data & AI
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
    "ms_learn_ai": [
        "https://learn.microsoft.com/api/search/rss?search=azure+ai+foundry&locale=en-us",
        "https://learn.microsoft.com/api/search/rss?search=github+copilot&locale=en-us",
    ],
}

# ── Relevance filter ──────────────────────────────────────────
# Posts MUST match at least one of these topic groups to be included.
# Each group is a list of keywords — matching any keyword in a group counts.
RELEVANT_TOPIC_GROUPS = [
    # AI & ML
    ["artificial intelligence", " ai ", "ai-", "machine learning", "deep learning",
     "neural network", "llm", "large language model", "generative ai", "gen ai",
     "gpt", "openai", "reasoning", "ai agent", "ai model", "multimodal"],
    # Microsoft Foundry & AI Services
    ["foundry", "azure ai", "ai studio", "ai services", "cognitive service",
     "azure openai", "azure machine learning", "ai search", "ai document",
     "speech service", "vision service", "language service", "content safety"],
    # Copilot & GitHub
    ["copilot", "github", "github actions", "github copilot", "code generation",
     "dev tools", "developer experience"],
    # Data & Analytics (AI-adjacent)
    ["data engineering", "data pipeline", "data lake", "fabric", "synapse",
     "databricks", "real-time analytics", "data warehouse", "power bi",
     "microsoft fabric", "data factory"],
    # Semantic Kernel & AI frameworks
    ["semantic kernel", "autogen", "langchain", "promptflow", "prompt flow",
     "responsible ai", "ai safety", "rag ", "retrieval augmented",
     "vector search", "embedding"],
    # Architecture & MLOps
    ["mlops", "ai architecture", "ai infrastructure", "ai deployment",
     "model deployment", "inference", "fine-tuning", "fine tuning"],
]

# Keywords that indicate internal/confidential content
INTERNAL_KEYWORDS = [
    "microsoft confidential", "internal only", "nda", "under nda",
    "not for external", "do not share", "microsoft internal",
    "msft internal", "internal use only", "pre-release confidential",
    "[internal]", "embargoed",
]

# Keywords that indicate community questions (not articles)
# Only flag if title starts with question-like patterns
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


def load_manifest() -> dict:
    if MANIFEST_FILE.exists():
        return json.loads(MANIFEST_FILE.read_text())
    return {"published_urls": [], "published_hashes": []}


def save_manifest(manifest: dict):
    MANIFEST_FILE.write_text(json.dumps(manifest, indent=2))


def content_hash(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:16]


def is_internal(title: str, summary: str) -> bool:
    """Check if content appears to be internal/confidential."""
    combined = f"{title} {summary}".lower()
    return any(kw in combined for kw in INTERNAL_KEYWORDS)


def is_community_question(title: str, summary: str) -> bool:
    """Filter out community forum questions — we only want articles/announcements.
    Only checks the title to avoid false positives from article bodies."""
    title_lower = title.lower()
    return any(signal in title_lower for signal in COMMUNITY_QUESTION_SIGNALS)


def is_relevant(title: str, summary: str) -> bool:
    """Check if content matches our focus areas: AI, Foundry, Copilot, GitHub, Data & AI."""
    combined = f"{title} {summary}".lower()
    for group in RELEVANT_TOPIC_GROUPS:
        if any(kw in combined for kw in group):
            return True
    return False


def categorize(title: str, summary: str) -> list[str]:
    """Auto-tag based on content keywords — focused on AI, Foundry, Copilot, GitHub."""
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


def needs_architecture_diagram(title: str, summary: str) -> bool:
    """Detect if content discusses systems/architecture worth diagramming."""
    text = f"{title} {summary}".lower()
    arch_keywords = [
        "architecture", "pipeline", "workflow", "integration",
        "microservice", "data flow", "topology", "infrastructure",
    ]
    return any(kw in text for kw in arch_keywords)


def generate_mermaid_placeholder(title: str) -> str:
    """Placeholder for architecture diagram — to be enhanced with LLM."""
    return f"""
{{{{< mermaid >}}}}
graph LR
    A[Source] --> B[Processing]
    B --> C[Output]
    style A fill:#0078d4,color:#fff
    style B fill:#50e6ff,color:#000
    style C fill:#00b294,color:#fff
{{{{< /mermaid >}}}}

*Architecture diagram for: {title}*
"""


def fetch_rss_entries(urls: list[str]) -> list[dict]:
    """Fetch and parse RSS feeds."""
    entries = []
    for url in urls:
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:5]:  # Latest 5 per feed
                pub_date = None
                if hasattr(entry, 'published'):
                    pub_date = dateparser.parse(entry.published)
                elif hasattr(entry, 'updated'):
                    pub_date = dateparser.parse(entry.updated)

                summary = getattr(entry, 'summary', '')
                # Strip HTML tags from summary
                summary = re.sub(r'<[^>]+>', '', summary)

                entries.append({
                    "title": entry.get("title", "Untitled"),
                    "url": entry.get("link", ""),
                    "summary": summary[:1000],
                    "date": pub_date or datetime.now(timezone.utc),
                    "source": url,
                })
        except Exception as e:
            print(f"  ⚠ Failed to fetch {url}: {e}")
    return entries


def create_hugo_post(entry: dict, manifest: dict) -> bool:
    """Create a Hugo markdown post from a feed entry."""
    url_hash = content_hash(entry["url"])

    # Deduplicate
    if entry["url"] in manifest["published_urls"]:
        return False
    if url_hash in manifest["published_hashes"]:
        return False

    # Filter internal content
    if is_internal(entry["title"], entry["summary"]):
        print(f"  🚫 Skipping internal content: {entry['title']}")
        return False

    # Filter community questions (not articles)
    if is_community_question(entry["title"], entry["summary"]):
        print(f"  💬 Skipping community question: {entry['title']}")
        return False

    # Filter irrelevant content (must match AI, Foundry, Copilot, GitHub, or Data & AI)
    if not is_relevant(entry["title"], entry["summary"]):
        print(f"  ⏭️  Skipping off-topic: {entry['title']}")
        return False

    tags = categorize(entry["title"], entry["summary"])
    date_str = entry["date"].strftime("%Y-%m-%d")
    slug = re.sub(r'[^a-z0-9]+', '-', entry["title"].lower()).strip('-')[:60]
    filename = f"{date_str}-{slug}.md"

    # Build post content
    diagram = ""
    if needs_architecture_diagram(entry["title"], entry["summary"]):
        diagram = generate_mermaid_placeholder(entry["title"])

    post = f"""---
title: "{entry['title'].replace('"', '\\"')}"
date: {date_str}
tags: {json.dumps(tags)}
categories: ["curated"]
source_url: "{entry['url']}"
description: "{entry['summary'][:200].replace('"', '\\"')}"
---

{entry['summary']}

{diagram}

🔗 [Read the full article]({entry['url']})

---
*Curated by Cyril Bou-Harb — Solution Engineer, Cloud & AI at Microsoft.*
*Views are my own.*
"""

    (POSTS_DIR / filename).write_text(post)
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
