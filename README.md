# Sadda Hussain Butt — Android engineering portfolio

A fast, accessible, multi-page portfolio for a senior Android engineer. The live site is [saddahussain.com](https://saddahussain.com), hosted on GitHub Pages.

The redesign uses a restrained charcoal-and-lime visual system, real product imagery, an easier-to-scan portfolio, and direct contact paths. It remains a **static site**: no frontend framework, server, or runtime build step is required.

## Pages

| Page | Purpose |
| --- | --- |
| `index.html` | Introduction, selected work, capabilities, and current role |
| `projects.html` | Three featured projects and a filterable archive of all 20 projects |
| `about.html` | Background and engineering approach |
| `experience.html` | Career timeline and technical impact |
| `skills.html` | Engineering strengths and technical toolkit |
| `education.html` | Software engineering degree and background |
| `google-play-compliance.html` | Android modernization service, process, and FAQs |
| `contact.html` | WhatsApp, phone, LinkedIn, and initial audit contact options |

## How it works

- **Presentation:** hand-written CSS in `css/styles.css`, with a responsive layout and reduced-motion support. No Tailwind or icon-font CDN.
- **Interactions:** `js/script.js` enhances the native mobile navigation and project filters. Navigation, FAQs, and all project content remain usable without JavaScript.
- **Images:** source PNGs live in `assets/`; the pages serve lightweight, resized WebP versions in `assets/optimized/`. Below-the-fold images are lazy-loaded and have intrinsic dimensions.
- **Content and layout:** editable page fragments are in `src/pages/`; `src/layout.html` holds shared document metadata; `src/projects.json` holds the project data. `scripts/build_site.py` produces the eight root-level HTML files that GitHub Pages serves. The shared navigation and footer are generated in one place.
- **Contact:** this is intentionally a direct-contact site, not a fake form. WhatsApp links include a relevant prefilled message; the initial audit link goes directly to an actionable contact channel.

## Local development

Requires Python 3. No Python packages or npm install are needed.

```sh
python3 scripts/build_site.py
python3 scripts/check_site.py
python3 -m http.server 8000
```

Visit `http://localhost:8000/`. To expose the server on a network interface, use `python3 -m http.server 8000 --bind 0.0.0.0`.

**Always rebuild after editing `src/layout.html`, `src/pages/`, `src/projects.json`, or shared markup in `scripts/build_site.py`.** Commit both the source files and the generated root HTML files; GitHub Pages serves the generated files directly.

### Updating projects and imagery

1. Edit `src/projects.json`. The project gallery and its homepage links are generated from this data. If the number of projects changes, also update the visible filter counts/copy and the count guard in `scripts/build_site.py`.
2. Add the original PNG to `assets/` and regenerate the optimized WebP images with `scripts/optimize_images.sh` (requires ImageMagick with WebP support).
3. Rebuild the pages and run the checker.
4. If the portrait or visual identity changes, regenerate `assets/og-cover.png` with `scripts/create_og.sh` (also requires ImageMagick).

The original PNG files are retained as image sources; they are **not** requested by the project gallery.

## Deployment and metadata

The `CNAME` points GitHub Pages to `saddahussain.com`. Pages include per-page titles and descriptions, canonical URLs, Open Graph/Twitter previews, semantic landmarks, and a sitemap. `feed.xml` contains occasional site updates rather than pretending static navigation pages are posts.

Google Analytics 4 is loaded directly with measurement ID `G-FYMN2VKM3F`. There is no Google Tag Manager container on the page. The site uses Google Fonts with system fallbacks; the CSS, images, and JavaScript are otherwise self-hosted.

## Validation

`scripts/check_site.py` verifies all eight pages have one main heading and landmark, checks local links and anchors, images, metadata, the project list, sitemap, and RSS. Responsive navigation, project filtering, and FAQ disclosure can be smoke-tested in a browser. The site is designed for keyboard navigation, visible focus indicators, and reduced-motion preferences.
