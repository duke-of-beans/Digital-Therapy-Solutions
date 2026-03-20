# Digital Therapy Solutions — BACKLOG.md
Last Updated: 2026-03-19

## Queued Sprints

### PS-PLATFORMS-01
Build all 31 remaining platform review pages as full content pages.
One page per logo in assets/logos/ that does not yet have an output/ page.
Each page follows the platform-review.html template.
Affiliate links activated per accepted application.
Pages are togglable (live vs stub CTA) without structural changes.
Dependencies: Affiliate applications accepted.

### PS-CONDITIONS-01
Build all 20 stub condition pages from conditions.html hub.
Each page follows the condition-guide.html template.
Content: condition overview, who it affects, what to look for in a platform,
top 3 platform recommendations with affiliate links.
Dependencies: None — can start immediately after PS-HUB-01.

### PS-INSURANCE-01
Define full insurer list (17 stubs + 6 live = 23 total).
Write grab script for insurance company logos (pattern: assets/grab-logos.py).
Build all 17 stub insurer pages following insurance-guide.html template.
Apply logos to insurance.html hub and individual insurer pages.
Dependencies: PS-HUB-01 (hub must exist first).

### PS-SEO-01
Meta description audit across all pages.
Canonical tag implementation.
Structured data (Schema.org Review, FAQPage, BreadcrumbList).
Sitemap.xml generation.
robots.txt.
Internal link density audit — ensure every page links to hub + 2–3 related pages.
Dependencies: PS-HUB-01, PS-PLATFORMS-01, PS-CONDITIONS-01, PS-INSURANCE-01.

### PS-DESIGN-01
MORPH-26 design intelligence pass on DTS.
Extract DTS patterns into DESIGN_DNA.yaml for ContentStudio fleet.
Apply motion registry, photography registry, anti-pattern enforcement.
Dependencies: MORPH-26 spec complete.
