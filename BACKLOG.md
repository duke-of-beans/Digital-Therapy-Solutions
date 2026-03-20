# Digital Therapy Solutions — BACKLOG.md
Last Updated: 2026-03-19

## Completed Sprints
- PS-PROP-01 ✅ | PS-PROP-01-FIX ✅ | PS-HUB-01 ✅ | PS-CONDITIONS-01 ✅
- PS-INSURANCE-01 ✅ | PS-DESIGN-QA-01 ✅ | PS-CONDITIONS-02 ✅

---

## Queued Sprints

### PS-SEO-01 — SEO Hardening
**Status:** READY — next sprint, no blockers
**Dependencies:** All content sprints ✅ complete
**Summary:**
Full inventory is live (65 pages). Now is the right time to harden the SEO layer.

Tasks:
- Meta description audit + optimization across all 65 pages
- Canonical tag implementation (prevent duplicate content penalties)
- Structured data: Schema.org Review on platform pages, FAQPage on condition/insurance
  pages, BreadcrumbList on all pages
- sitemap.xml generation script (automated, not manual)
- robots.txt — confirm Allow: / across all pages
- Internal link density audit — every page should link to its hub + 2-3 related pages
- Title tag pattern audit and enforcement
- Missing logo: add inclusive-therapists.webp to assets/logos/ (Clearbit grab)

---

### PS-PLATFORMS-01 — All 31 Remaining Platform Review Pages
**Status:** QUEUED — blocked on affiliate applications
**Dependencies:** Affiliate applications accepted
**Note:** Apply verdict-box, pull-quote, feature-list components from PS-DESIGN-QA-01
to all new review pages at build time. reviews.html hub cards auto-activate once pages exist.
**Platform list:**
adhd-online, amwell, bend-health, brightline, brightside, calmerry, cerebral,
circle-medical, doctor-on-demand, done-adhd, faithful-counseling, gay-therapy-center,
grow-therapy, headspace, headway, inclusive-therapists, klarity, lunajoy, manatee-health,
mindful-care, nocd, open-path, our-relationship, our-ritual, pride-counseling,
psychology-today, regain, simplepractice, talkiatry, teen-counseling, therapyden

---

### PS-DESIGN-01 — MORPH-26 Design Intelligence Pass
**Status:** QUEUED
**Dependencies:** MORPH-26 ✅ complete in ContentStudio. PS-DESIGN-QA-01 ✅ complete.
**Summary:**
Extract DTS design patterns into DESIGN_DNA.yaml for ContentStudio fleet.
Apply motion registry, photography registry, anti-pattern enforcement.
Also: grab inclusive-therapists.webp if not already done in PS-SEO-01.
