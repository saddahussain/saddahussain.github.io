#!/usr/bin/env python3
"""Build the dependency-free, GitHub Pages-ready HTML files from shared layout.

Edit src/pages/*.html for page content, src/layout.html for the document shell,
and NAV_ITEMS / footer() here for navigation shared across every page.
Run: python3 scripts/build_site.py
"""
from __future__ import annotations

import html
import json
import struct
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
ORIGIN = "https://saddahussain.com"
PHONE = "+923227036979"
WHATSAPP = "https://wa.me/923227036979?text=" + quote(
    "Hello Sadda, I'd like to discuss an Android project.", safe=""
)
AUDIT_WHATSAPP = "https://wa.me/923227036979?text=" + quote(
    "Hello Sadda, I'd like to request a free initial Android app compliance audit.", safe=""
)

PAGES = {
    "index": (
        "Sadda Hussain Butt | Senior Android Engineer",
        "Sadda Hussain Butt is a senior Android engineer building reliable mobile products, hardware-integrated systems, and modernized Android apps.",
    ),
    "projects": (
        "Selected Work | Sadda Hussain Butt",
        "Explore Android apps, hardware-integrated systems, wellness products, marketplaces, and mobile platforms built by Sadda Hussain Butt.",
    ),
    "about": (
        "About | Sadda Hussain Butt",
        "Meet Sadda Hussain Butt, a senior Android engineer focused on thoughtful product engineering, technical leadership, and durable mobile experiences.",
    ),
    "experience": (
        "Experience | Sadda Hussain Butt",
        "Sadda Hussain Butt's Android engineering experience across Devsarch, Xenex Media, Upgenics International, and AppsGenii Technologies.",
    ),
    "skills": (
        "Expertise | Sadda Hussain Butt",
        "Android engineering expertise in Kotlin, Jetpack Compose, mobile architecture, integrations, security, and release engineering.",
    ),
    "education": (
        "Education | Sadda Hussain Butt",
        "Sadda Hussain Butt studied Software Engineering at the University of Gujrat and applies that foundation to production Android products.",
    ),
    "google-play-compliance": (
        "Android App Modernization & Play Compliance | Sadda Hussain Butt",
        "Modernize a legacy Android app, resolve build issues, update target SDKs, and navigate Google Play requirements with an experienced Android engineer.",
    ),
    "contact": (
        "Contact | Sadda Hussain Butt",
        "Get in touch with Sadda Hussain Butt about Android engineering, legacy app modernization, product development, or a free initial compliance audit.",
    ),
}

NAV_ITEMS = [
    ("projects", "Work"),
    ("skills", "Expertise"),
    ("experience", "Experience"),
    ("about", "About"),
    ("google-play-compliance", "Services"),
]
MOBILE_ITEMS = [("index", "Home"), *NAV_ITEMS[:4], ("education", "Education"), NAV_ITEMS[4], ("contact", "Contact")]


def link(page: str) -> str:
    return f"{page}.html"


def nav_link(destination: str, label: str, current: str, css_class: str = "nav-link") -> str:
    active = destination == current
    state = ' aria-current="page"' if active else ""
    return f'<a href="{link(destination)}" class="{css_class}{" is-active" if active else ""}"{state}>{label}</a>'


def nav(page: str) -> str:
    desktop = "\n".join(nav_link(dest, name, page) for dest, name in NAV_ITEMS)
    mobile = "\n".join(nav_link(dest, name, page, "mobile-nav-link") for dest, name in MOBILE_ITEMS)
    return f'''<header class="site-header">
  <div class="site-header-inner container">
    <a class="brand" href="index.html" aria-label="Sadda Hussain Butt, home">
      <span class="brand-mark" aria-hidden="true"><span class="brand-mark-glyph">s<span class="brand-mark-slash">/</span>h</span></span>
      <span class="brand-name">Sadda Hussain<span class="brand-dot">.</span><small>ANDROID ENGINEER</small></span>
    </a>
    <nav class="desktop-nav" aria-label="Primary navigation">
      {desktop}
    </nav>
    <a class="header-cta" href="contact.html">Let's talk <span aria-hidden="true">↗</span></a>
    <details class="mobile-nav">
      <summary class="mobile-nav-toggle"><span class="mobile-nav-toggle-label">Menu</span><span class="menu-bars" aria-hidden="true"><span></span><span></span></span></summary>
      <nav class="mobile-nav-panel" aria-label="Mobile navigation">{mobile}
        <a class="mobile-nav-contact" href="contact.html">Start a conversation <span aria-hidden="true">↗</span></a>
      </nav>
    </details>
  </div>
</header>'''


def footer_cta(page: str) -> str:
    if page == "contact":
        return ""
    if page == "google-play-compliance":
        title = "Your app isn't a lost cause."
        copy = "Tell me what's holding your Android app back. Let's find a sensible way forward."
        action = f'<a class="button button-lime" href="{AUDIT_WHATSAPP}" target="_blank" rel="noopener noreferrer">Request a free initial audit <span aria-hidden="true">↗</span></a>'
        label = "LET'S TAKE A LOOK"
    else:
        title = "Let's make something that lasts."
        copy = "An ambitious idea, a complex Android problem, or an app that needs a second life — I'd love to hear about it."
        action = '<a class="button button-lime" href="contact.html">Start a conversation <span aria-hidden="true">↗</span></a>'
        label = "HAVE SOMETHING IN MIND?"
    return f'''<section class="closing-cta" aria-labelledby="closing-cta-title">
  <div class="container closing-cta-inner">
    <div><p class="eyebrow eyebrow-lime">{label}</p><h2 id="closing-cta-title">{title}</h2><p>{copy}</p></div>
    {action}
  </div>
</section>'''


def footer() -> str:
    return f'''<footer class="site-footer">
  <div class="container">
    <div class="footer-top">
      <div class="footer-identity">
        <a class="footer-brand" href="index.html">Sadda Hussain<span>.</span></a>
        <p>Engineering Android experiences<br>that work beyond the demo.</p>
        <span class="footer-location"><span class="status-dot" aria-hidden="true"></span> Sialkot, Pakistan · Working worldwide</span>
      </div>
      <div class="footer-link-group"><h2>Explore</h2><a href="projects.html">Selected work</a><a href="about.html">About</a><a href="experience.html">Experience</a><a href="skills.html">Expertise</a><a href="education.html">Education</a></div>
      <div class="footer-link-group"><h2>Connect</h2><a href="google-play-compliance.html">Android modernization</a><a href="contact.html">Get in touch</a><a href="https://www.linkedin.com/in/saddahussain" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a><a href="https://github.com/saddahussain" target="_blank" rel="noopener noreferrer">GitHub ↗</a><a href="assets/Sadda_Hussain_Android_8Y.pdf" download>Download CV ↓</a></div>
    </div>
    <div class="footer-bottom"><span>© 2026 Sadda Hussain Butt. Built with intention.</span><a href="#main-content">Back to top ↑</a></div>
  </div>
</footer>'''


def schema(page: str) -> str:
    person = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "Sadda Hussain Butt",
        "jobTitle": "Senior Android Engineer",
        "url": f"{ORIGIN}/",
        "image": f"{ORIGIN}/assets/picture.png",
        "sameAs": ["https://www.linkedin.com/in/saddahussain", "https://github.com/saddahussain"],
    }
    if page == "index":
        data = person
    elif page == "google-play-compliance":
        data = {"@context": "https://schema.org", "@type": "Service", "name": "Android app modernization and Google Play compliance", "url": f"{ORIGIN}/{link(page)}", "provider": {"@type": "Person", "name": "Sadda Hussain Butt", "url": f"{ORIGIN}/"}}
    else:
        return ""
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + '</script>'


def project_card(project: dict, index: int) -> str:
    """Static markup keeps projects discoverable even with JavaScript disabled."""
    esc = lambda text: html.escape(str(text), quote=True)
    slug, name, group = (esc(project[key]) for key in ("slug", "name", "group"))
    image = esc(project["image"])
    with (ROOT / f"assets/{project['image']}.png").open("rb") as original:
        original.seek(16)
        width, height = struct.unpack(">II", original.read(8))
    visual = (f'<div class="project-visual tone-{esc(project["tone"])}">'
              f'<img src="assets/optimized/{image}.webp" alt="{esc(project["alt"])}" '
              f'width="{width}" height="{height}" loading="lazy" decoding="async"></div>')
    tags = "".join(f"<span>{esc(tag)}</span>" for tag in project["tags"])
    impact = f'<strong class="project-impact">{esc(project["impact"])}</strong>' if project.get("impact") else ""
    external = project.get("external")
    outbound = (f'<a class="project-outbound" href="{esc(external)}" target="_blank" rel="noopener noreferrer" '
                f'aria-label="Visit {name} website (opens in a new tab)">Visit website <span aria-hidden="true">↗</span></a>') if external else ""
    if project.get("featured"):
        primary = " project-feature-primary" if index == 1 else ""
        copy = (f'<div class="project-feature-copy"><span class="project-overline">FEATURED / {index:02d} — {esc(project["label"])}</span>'
                f'<div><h3>{name}</h3><p>{esc(project["summary"])}</p>'
                f'<div class="project-tags">{tags}</div></div>{outbound}</div>')
        return (f'<article id="{slug}" class="project-feature project-filterable{primary}" data-category="{group}">'
                f'{copy}{visual}</article>')
    return (f'<article id="{slug}" class="archive-card project-filterable" data-category="{group}">'
            f'{visual}<div class="archive-card-copy"><span class="project-overline">{index:02d} / {esc(project["label"])}</span>'
            f'<h3>{name}</h3><p>{esc(project["summary"])}</p>{impact}<div class="project-tags">{tags}</div>'
            f'{outbound}</div></article>')


def render_projects(content: str) -> str:
    projects = json.loads((ROOT / "src/projects.json").read_text(encoding="utf-8"))
    featured = [project_card(project, index) for index, project in enumerate(projects, 1) if project.get("featured")]
    archive = [project_card(project, index) for index, project in enumerate(projects, 1) if not project.get("featured")]
    if len(projects) != 20 or len(featured) != 3:
        raise ValueError("Update the project filters/counts when changing the project list")
    return content.replace("{{FEATURED_PROJECTS}}", "\n".join(featured)).replace("{{ARCHIVE_PROJECTS}}", "\n".join(archive))


def build() -> None:
    template = (ROOT / "src/layout.html").read_text(encoding="utf-8")
    for page, (title, description) in PAGES.items():
        canonical = f"{ORIGIN}/" if page == "index" else f"{ORIGIN}/{link(page)}"
        content = (ROOT / f"src/pages/{page}.html").read_text(encoding="utf-8").strip()
        if page == "projects":
            content = render_projects(content)
        replacements = {
            "TITLE": html.escape(title, quote=True),
            "DESCRIPTION": html.escape(description, quote=True),
            "CANONICAL": html.escape(canonical, quote=True),
            "PAGE": page,
            "NAV": nav(page),
            "CONTENT": content,
            "FOOTER_CTA": footer_cta(page),
            "FOOTER": footer(),
            "STRUCTURED_DATA": schema(page),
        }
        output = template
        for key, value in replacements.items():
            output = output.replace("{{" + key + "}}", value)
        if "{{" in output:
            raise ValueError(f"Unfilled template token in {page}")
        (ROOT / link(page)).write_text(output.rstrip() + "\n", encoding="utf-8")
    print(f"Built {len(PAGES)} pages for GitHub Pages.")


if __name__ == "__main__":
    build()
