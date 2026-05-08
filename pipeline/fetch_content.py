#!/usr/bin/env python3
"""
Content pipeline: fetches from Microsoft sources, deduplicates,
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
SOURCES = {
    "microsoft_blog": [
        "https://azure.microsoft.com/en-us/blog/feed/",
        "https://devblogs.microsoft.com/azure-ai/feed/",
        "https://techcommunity.microsoft.com/feeds/blogs/category/AI",
        "https://techcommunity.microsoft.com/feeds/blogs/category/Azure",
    ],
    "ms_learn": [
        "https://learn.microsoft.com/en-us/azure/ai-services/whats-new?format=rss",
    ],
}

# Keywords that indicate internal/confidential content
INTERNAL_KEYWORDS = [
    "microsoft confidential", "internal only", "nda", "under nda",
    "not for external", "do not share", "microsoft internal",
    "msft internal", "internal use only", "pre-release confidential",
    "[internal]", "embargoed",
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


def categorize(title: str, summary: str) -> list[str]:
    """Auto-tag based on content keywords."""
    tags = []
    text = f"{title} {summary}".lower()
    tag_map = {
        "azure": "Azure", "ai": "AI", "machine learning": "ML",
        "fabric": "Fabric", "copilot": "Copilot",
        "openai": "OpenAI", "data": "Data",
        "kubernetes": "Kubernetes", "devops": "DevOps",
        "security": "Security", "networking": "Networking",
    }
    for keyword, tag in tag_map.items():
        if keyword in text:
            tags.append(tag)
    return tags or ["Cloud"]


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
