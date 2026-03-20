# Digital Therapy Solutions — BACKLOG.md
Last Updated: 2026-03-19

## Completed Sprints
- PS-PROP-01 ✅ | PS-PROP-01-FIX ✅ | PS-HUB-01 ✅ | PS-CONDITIONS-01 ✅ | PS-INSURANCE-01 ✅

---

## Queued Sprints

### PS-CONDITIONS-02 — 4 Remaining Stub Condition Pages
**Status:** READY
**Dependencies:** PS-CONDITIONS-01 ✅
**Summary:**
Build the 4 condition pages currently stubbed on conditions.html hub.
Confirm slugs before running:
- mens-mental-health.html ← confirmed slug
- womens-mental-health.html ← confirmed slug
- life-transitions.html ← confirmed slug
- autism.html ← confirmed slug
Stress + Burnout split confirmed intentional — both pages stay.
Follow condition-guide.html template. Same pattern as PS-CONDITIONS-01.

---

### PS-DESIGN-QA-01 — Design Quality + Visual Consistency Pass
**Status:** READY — sprint prompt written at sprints/PS-DESIGN-QA-01.md
**Dependencies:** PS-INSURANCE-01 ✅
**Issues addressed (8 total):**
1. affordable.html — unstyled .alternative-item and .insurance-links sections
2. Emoji permanently banned — replace all condition card icons with cohesive SVG system
3. Insurance logos added to homepage tiles + all contextual placements
4. Privacy Policy — Fraunces heading + full layout upgrade
5. Affiliate Disclosure page — create output/affiliate-disclosure.html, link from footer
6. Logo authenticity — verify-logos.py audit, Clearbit re-grab for flagged logos,
   object-fit: contain enforced everywhere
7. Detail page body — pull quotes, stat callouts, verdict box components
8. Repetitive card grids — feature-list, split-section, timeline-list layout variants

---

### PS-PLATFORMS-01 — All 31 Remaining Platform Review Pages
**Status:** QUEUED — blocked on affiliate applications
**Dependencies:** Affiliate applications accepted
**Platform list:**
adhd-online, amwell, bend-health, brightline, brightside, calmerry, cerebral,
circle-medical, doctor-on-demand, done-adhd, faithful-counseling, gay-therapy-center,
grow-therapy, headspace, headway, inclusive-therapists, klarity, lunajoy, manatee-health,
mindful-care, nocd, open-path, our-relationship, our-ritual, pride-counseling,
psychology-today, regain, simplepractice, talkiatry, teen-counseling, therapyden

---

### PS-SEO-01 — SEO Hardening
**Status:** QUEUED (after all content sprints)
**Dependencies:** PS-PLATFORMS-01, PS-CONDITIONS-02, PS-INSURANCE-01 ✅
**Summary:**
Meta description audit + optimization. Canonical tags. Structured data (Schema.org
Review, FAQPage, BreadcrumbList). sitemap.xml generation script. robots.txt.
Internal link density audit — every page links to hub + 2-3 related pages.
Title tag pattern enforcement.

---

### PS-DESIGN-01 — MORPH-26 Design Intelligence Pass
**Status:** QUEUED (MORPH-26 ✅ complete in ContentStudio)
**Summary:**
Extract DTS design patterns into DESIGN_DNA.yaml for ContentStudio fleet.
Apply motion registry, photography registry, anti-pattern enforcement.
Note: Run after PS-DESIGN-QA-01 so extracted patterns reflect the improved design state.
