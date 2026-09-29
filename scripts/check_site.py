#!/usr/bin/env python3
"""Dependency-free checks for the generated GitHub Pages site."""
from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from build_site import ORIGIN, PAGES, link  # noqa: E402


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: Counter[str] = Counter()
        self.refs: list[tuple[str, str]] = []
        self.images: list[dict[str, str]] = []
        self.headings: Counter[str] = Counter()
        self.mains = 0
        self.titles = 0
        self.description = False
        self.canonical: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        if data.get("id"):
            self.ids[data["id"]] += 1
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self.headings[tag] += 1
        if tag == "main":
            self.mains += 1
        if tag == "title":
            self.titles += 1
        if tag == "meta" and data.get("name") == "description":
            self.description = bool(data.get("content"))
        if tag == "link" and data.get("rel") == "canonical":
            self.canonical = data.get("href")
        if tag == "img":
            self.images.append(data)
        for field in ("href", "src"):
            if value := data.get(field):
                self.refs.append((field, value))
        if tag == "a" and data.get("target") == "_blank":
            rel = set((data.get("rel") or "").split())
            if not {"noopener", "noreferrer"}.issubset(rel):
                raise ValueError(f"External link missing rel protections: {data.get('href')}")


def check() -> None:
    pages: dict[str, PageParser] = {}
    problems: list[str] = []
    for name in PAGES:
        filename = link(name)
        source = (ROOT / filename).read_text(encoding="utf-8")
        page = PageParser()
        page.feed(source)
        pages[filename] = page
        canonical = f"{ORIGIN}/" if name == "index" else f"{ORIGIN}/{filename}"
        if (page.headings["h1"], page.mains, page.titles) != (1, 1, 1):
            problems.append(f"{filename}: expected one h1, main, and title; got {page.headings['h1']}, {page.mains}, {page.titles}")
        if not page.description or page.canonical != canonical:
            problems.append(f"{filename}: missing or incorrect page description/canonical")
        if duplicates := {k: v for k, v in page.ids.items() if v > 1}:
            problems.append(f"{filename}: duplicate IDs {duplicates}")
        for image in page.images:
            if not image.get("alt") or not image.get("width") or not image.get("height"):
                problems.append(f"{filename}: image missing alt or intrinsic dimensions: {image.get('src')}")

    for filename, page in pages.items():
        for field, value in page.refs:
            parts = urlsplit(value)
            if parts.scheme or parts.netloc or value.startswith(("mailto:", "tel:")):
                continue
            target = unquote(parts.path)
            target_page = target if target else filename
            if target and not (ROOT / target).is_file():
                problems.append(f"{filename}: missing local {field} {value}")
            if parts.fragment and target_page in pages and parts.fragment not in pages[target_page].ids:
                problems.append(f"{filename}: missing anchor {value}")
            if value == "#":
                problems.append(f"{filename}: placeholder link")

    projects = json.loads((ROOT / "src/projects.json").read_text(encoding="utf-8"))
    if len(projects) != 20 or len({project["slug"] for project in projects}) != 20:
        problems.append("Projects must have 20 unique slugs")
    if len(re.findall(r'class="[^"]*project-filterable', (ROOT / "projects.html").read_text())) != len(projects):
        problems.append("Not all projects were rendered into projects.html")
    for project in projects:
        if project["group"] not in {"systems", "consumer", "commerce", "tools"}:
            problems.append(f"Unknown category for {project['name']}")
        if not (ROOT / f"assets/optimized/{project['image']}.webp").is_file():
            problems.append(f"Missing optimized image for {project['name']}")

    sitemap = ET.parse(ROOT / "sitemap.xml")
    actual_urls = {node.text for node in sitemap.findall(".//{*}loc")}
    expected_urls = {f"{ORIGIN}/" if name == "index" else f"{ORIGIN}/{link(name)}" for name in PAGES}
    if actual_urls != expected_urls:
        problems.append(f"Sitemap differs from pages: {actual_urls ^ expected_urls}")
    ET.parse(ROOT / "feed.xml")

    if problems:
        raise SystemExit("Site check failed:\n" + "\n".join(f" - {problem}" for problem in problems))
    print(f"Site check passed: {len(pages)} pages, {len(projects)} projects, local links/assets/anchors, metadata, sitemap, and feed.")


if __name__ == "__main__":
    check()
