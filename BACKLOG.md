# Digital Therapy Solutions — BACKLOG.md
Last Updated: 2026-03-19

## Completed Sprints
- PS-PROP-01 ✅ | PS-PROP-01-FIX ✅ | PS-HUB-01 ✅ | PS-CONDITIONS-01 ✅
- PS-INSURANCE-01 ✅ | PS-DESIGN-QA-01 ✅ | PS-CONDITIONS-02 ✅ | PS-SEO-01 ✅

---

## Queued Sprints

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
