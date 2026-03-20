# Digital Therapy Solutions — BACKLOG.md
Last Updated: 2026-03-19

## Completed Sprints
- PS-PROP-01 ✅ | PS-PROP-01-FIX ✅ | PS-HUB-01 ✅ | PS-CONDITIONS-01 ✅
- PS-INSURANCE-01 ✅ | PS-DESIGN-QA-01 ✅ | PS-CONDITIONS-02 ✅ | PS-SEO-01 ✅

---

## Queued Sprints

### PS-AUDIT-01 — Full Site Audit (Multi-Hat)
**Status:** READY — sprint prompt at sprints/PS-AUDIT-01.md
**Hats:** Designer / Engineer / DTS Owner / Affiliate Partner
**Output:** PS-AUDIT-01-REPORT.md + FIX NOW queue + backlog additions + launch checklist
**Note:** Observe and document only. Fixes execute after report is written.

---

### PS-LOGO-REFRESH-01 — Insurance Logo Replacement (Solid BG Versions)
**Status:** BLOCKED — waiting on asset sourcing by David
**Problem:** Insurance logos grabbed as transparent PNG/SVG render poorly on warm parchment
backgrounds. The transparent areas show through and look wrong against --bg-secondary fill.
**Action needed:** Source solid-background versions of insurer logos (white or brand-color BG).
Best sources: brand press kits, official media pages, or request directly from insurer.
**Priority insurers to replace (transparent/rendering poorly):**
All insurer-*.webp files should be audited visually once solid versions are available.
**When assets are ready:** xcopy to output/assets/logos/, run logo_audit_summary.py, commit + push.
**CSS note:** --bg-secondary fill rule stays — it handles edge cases. Solid logos just look better.

---

### PS-PLATFORMS-01 — All 31 Remaining Platform Review Pages
**Status:** READY — sprint prompt written at sprints/PS-PLATFORMS-01.md
**Dependencies:** None — affiliate contracts NOT required. Pages built with pending CTAs.
**Toggle system:** assets/activate-affiliate.py flips any platform live when contract signed.
  Usage: python assets/activate-affiliate.py --platform [slug] --url [affiliate_url]
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
**Status:** READY — no blockers
**Dependencies:** MORPH-26 ✅ | PS-DESIGN-QA-01 ✅ | PS-SEO-01 ✅
**Summary:**
Extract DTS design patterns into DESIGN_DNA.yaml for ContentStudio fleet.
Apply motion registry, photography registry, anti-pattern enforcement.
DTS is one of the 5 reference sites for MORPH-26. Running post-PS-SEO-01 ensures
extracted patterns reflect the fully complete, hardened site.
Also: grab inclusive-therapists.webp if not done manually before this sprint.

---

### PS-LAUNCH-01 — Domain Activation + GSC Setup
**Status:** QUEUED — blocked on domain repurchase (Gavin)
**Dependencies:** Domain repurchased, DNS pointed to Vercel
**Summary:**
- Point domain DNS to Vercel (A record + CNAME per Vercel docs)
- Add custom domain in Vercel project settings
- Verify SSL certificate auto-provisioned
- Create Google Search Console property for digitaltherapysolutions.com
- Submit sitemap.xml to GSC
- Verify robots.txt accessible at live domain
- Monitor first crawl and indexation
