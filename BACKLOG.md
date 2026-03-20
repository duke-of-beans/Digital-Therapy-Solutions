# Digital Therapy Solutions — BACKLOG.md
Last Updated: 2026-03-19

## Completed Sprints
- PS-PROP-01 ✅ | PS-PROP-01-FIX ✅ | PS-HUB-01 ✅ | PS-CONDITIONS-01 ✅
- PS-INSURANCE-01 ✅ | PS-DESIGN-QA-01 ✅

---

## Queued Sprints

### PS-CONDITIONS-02 — 4 Remaining Stub Condition Pages
**Status:** READY — next sprint
**Dependencies:** PS-CONDITIONS-01 ✅
**Slugs confirmed:** mens-mental-health.html, womens-mental-health.html,
life-transitions.html, autism.html
**Note:** Stress + Burnout split confirmed intentional — both pages stay.
Follow condition-guide.html template. Same pattern as PS-CONDITIONS-01.
Apply SVG icon system from PS-DESIGN-QA-01 to new condition cards on conditions.html.

---

### PS-LOGO-REGRAB — Manual Step + Verify
**Status:** READY — one manual action required first
**Action:** Run `python assets/regrab-logos.py` from host machine (needs Clearbit network access)
**Then:** Spot-check 5–10 logos in browser. Run quality_gate.py. Commit.
**Commit message:** fix(logos): regrab 23 flagged logos via Clearbit
**Note:** LOGO_AUDIT.md documents all 23 flagged files with dimensions + reasons.

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
**Note:** Apply verdict-box, pull-quote, feature-list components from PS-DESIGN-QA-01
to all new review pages at build time.

---

### PS-SEO-01 — SEO Hardening
**Status:** QUEUED (after PS-CONDITIONS-02 and PS-PLATFORMS-01)
**Dependencies:** PS-CONDITIONS-02, PS-PLATFORMS-01, PS-INSURANCE-01 ✅
**Summary:**
Meta description audit + optimization. Canonical tags. Structured data (Schema.org
Review, FAQPage, BreadcrumbList). sitemap.xml generation script. robots.txt.
Internal link density audit — every page links to hub + 2-3 related pages.
Title tag pattern enforcement.

---

### PS-DESIGN-01 — MORPH-26 Design Intelligence Pass
**Status:** QUEUED
**Dependencies:** MORPH-26 ✅ complete in ContentStudio. Run after PS-DESIGN-QA-01 ✅
so extracted patterns reflect improved design state.
**Summary:**
Extract DTS design patterns into DESIGN_DNA.yaml for ContentStudio fleet.
Apply motion registry, photography registry, anti-pattern enforcement.
